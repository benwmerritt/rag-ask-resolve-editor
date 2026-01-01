"""LLM-based chunk enrichment for improved semantic search."""
import os
import json
import logging
from typing import List, Dict, Any
from dataclasses import dataclass
from tqdm import tqdm

logger = logging.getLogger(__name__)

# Anthropic for chunk enrichment
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

# OpenAI client for OpenRouter (OpenAI-compatible API)
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


@dataclass
class EnrichmentResult:
    summary: str
    keywords: List[str]


class ChunkEnricher:
    """Enrich chunks with LLM-generated summaries and keywords."""

    def __init__(self, config: Dict[str, Any]):
        self.config = config.get('metadata_injection', {})
        self.enabled = self.config.get('enabled', False)
        self.provider = self.config.get('provider', 'anthropic')
        self.model = self.config.get('model', 'claude-3-5-haiku-20241022')
        self.batch_size = self.config.get('batch_size', 5)
        self.client = None

        if not self.enabled:
            return

        # Initialize the appropriate client based on provider
        if self.provider == 'openrouter':
            self._init_openrouter()
        else:
            self._init_anthropic()

    def _init_openrouter(self):
        """Initialize OpenRouter client (OpenAI-compatible API)."""
        if not OPENAI_AVAILABLE:
            logger.warning("openai package not installed, falling back to Anthropic")
            self.provider = 'anthropic'
            self._init_anthropic()
            return

        api_key = os.getenv('OPENROUTER_API_KEY')
        if api_key:
            self.client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key
            )
            logger.info(f"Enrichment using OpenRouter with model: {self.model}")
        else:
            logger.warning("OPENROUTER_API_KEY not set, falling back to Anthropic")
            self.provider = 'anthropic'
            self._init_anthropic()

    def _init_anthropic(self):
        """Initialize Anthropic client."""
        if not ANTHROPIC_AVAILABLE:
            logger.warning("anthropic package not installed, enrichment disabled")
            return

        api_key = os.getenv('ANTHROPIC_API_KEY')
        if api_key:
            self.client = anthropic.Anthropic(api_key=api_key)
            logger.info(f"Enrichment using Anthropic with model: {self.model}")
        else:
            logger.warning("ANTHROPIC_API_KEY not set, enrichment disabled")

    def _call_llm(self, prompt: str) -> str:
        """Call the configured LLM provider and return response text."""
        if self.provider == 'openrouter':
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        else:  # anthropic
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text

    def enrich_chunks(self, chunks: List) -> List:
        """Add LLM-generated summaries and keywords to chunks."""
        if not self.enabled:
            return chunks

        if not self.client:
            logger.warning("Enrichment enabled but no LLM client available")
            return chunks

        enriched = []
        failed_batches = 0

        # Process in batches
        for i in tqdm(range(0, len(chunks), self.batch_size), desc="Enriching chunks"):
            batch = chunks[i:i + self.batch_size]
            results = self._enrich_batch(batch)

            if not any(r.summary for r in results):
                failed_batches += 1

            for chunk, result in zip(batch, results):
                # Add to metadata
                chunk.metadata['llm_summary'] = result.summary
                chunk.metadata['llm_keywords'] = result.keywords

                # Create enriched content for embedding
                if result.summary:
                    chunk.enriched_content = (
                        f"Summary: {result.summary}\n"
                        f"Keywords: {', '.join(result.keywords)}\n\n"
                        f"{chunk.content}"
                    )
                else:
                    chunk.enriched_content = chunk.content

                enriched.append(chunk)

        success_rate = ((len(chunks) // self.batch_size) - failed_batches) / max(1, len(chunks) // self.batch_size)
        logger.info(f"Enriched {len(enriched)} chunks (success rate: {success_rate:.0%})")
        return enriched

    def _enrich_batch(self, batch: List) -> List[EnrichmentResult]:
        """Process a batch of chunks with a single LLM call."""
        # Build batch prompt
        chunks_text = ""
        for idx, chunk in enumerate(batch):
            content_preview = chunk.content[:1200]  # Limit per chunk
            chunks_text += f"\n---CHUNK {idx}---\n{content_preview}\n"

        prompt = f"""Analyze these content excerpts and provide a summary and keywords for each.

{chunks_text}

For each chunk, provide:
1. A 1-2 sentence summary of the main point
2. 3-5 key concepts/keywords

Respond in JSON format as an array:
[
  {{"chunk": 0, "summary": "...", "keywords": ["...", "..."]}},
  {{"chunk": 1, "summary": "...", "keywords": ["...", "..."]}}
]

Return ONLY valid JSON, no other text."""

        try:
            text = self._call_llm(prompt).strip()

            # Handle potential markdown code blocks
            if text.startswith("```"):
                lines = text.split("\n")
                # Remove first and last lines (```json and ```)
                text = "\n".join(lines[1:-1] if lines[-1] == "```" else lines[1:])
                if text.startswith("json"):
                    text = text[4:].strip()

            results = json.loads(text)

            # Convert to EnrichmentResult objects
            enrichments = []
            for item in results:
                enrichments.append(EnrichmentResult(
                    summary=item.get('summary', ''),
                    keywords=item.get('keywords', [])
                ))

            # Pad if needed (in case LLM missed some)
            while len(enrichments) < len(batch):
                enrichments.append(EnrichmentResult(summary='', keywords=[]))

            return enrichments

        except json.JSONDecodeError as e:
            logger.warning(f"JSON parse error in batch: {e}")
            return [EnrichmentResult(summary='', keywords=[]) for _ in batch]
        except Exception as e:
            logger.warning(f"Batch enrichment failed: {e}")
            return [EnrichmentResult(summary='', keywords=[]) for _ in batch]
