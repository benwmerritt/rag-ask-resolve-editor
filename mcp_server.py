#!/usr/bin/env python3
"""
MCP Server for Ask DaVinci Resolve Editor

Exposes DaVinci Resolve video editing and color grading content as Model Context Protocol tools
for Claude Desktop using the fastmcp library.

Tools:
  - ask_resolve_editor(question, top_k?, max_tokens?, user_context?) -> Markdown answer with Sources
  - about() -> System information
"""

import os
import sys
from typing import List, Dict, Optional, Any
import yaml as __yaml

# Ensure imports from this repo work regardless of cwd
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
try:
    # Ensure relative paths in config.yaml resolve correctly
    os.chdir(REPO_ROOT)
except Exception:
    pass

# Allow per-profile config via environment variable
CONFIG_PATH = os.getenv('WIKI_VAULT_CONFIG', os.path.join(REPO_ROOT, 'config.yaml'))
try:
    with open(CONFIG_PATH, 'r') as __f:
        __CFG = __yaml.safe_load(__f)
except Exception:
    __CFG = {}

# Ensure imported scripts don't print to stdout and break MCP protocol
os.environ['WIKI_VAULT_SILENT'] = '1'

from fastmcp import FastMCP  # type: ignore

# Reuse existing functionality
from lib.query import KnowledgeQuery
from lib.full_notes import FullNotesReader


# MCP server name
PROVIDER_NAME = os.getenv('WIKI_VAULT_MCP_NAME') or "ask-resolve-editor"
mcp = FastMCP(PROVIDER_NAME)


class _Lazy:
    query: Optional[KnowledgeQuery] = None
    notes: Optional[FullNotesReader] = None


def _get_query() -> KnowledgeQuery:
    if _Lazy.query is None:
        _Lazy.query = KnowledgeQuery(config_path=CONFIG_PATH)
    return _Lazy.query


def _get_notes() -> FullNotesReader:
    if _Lazy.notes is None:
        _Lazy.notes = FullNotesReader(config_path=CONFIG_PATH)
    return _Lazy.notes


def _to_int(value: Any) -> Optional[int]:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _answer_with_openai(question: str, context: str, max_tokens: int = 2000, user_context: Optional[str] = None) -> Optional[str]:
    try:
        import openai as _openai
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key or len(api_key) < 10:
            return None
        client = _openai.OpenAI(api_key=api_key)
        system_prompt = """
ROLE: You are a professional DaVinci Resolve video editor and colorist with deep expertise in post-production workflows. Your knowledge comes from expert practitioners including Darren Mostyn, Creative Video Tips, Jason Yadlovski, and MrAlexTech who specialize in DaVinci Resolve training.

EXPERTISE AREAS:
- DaVinci Resolve editing workflows (Cut page, Edit page, timeline management)
- Professional color grading techniques (Color page, nodes, scopes, color management)
- Fusion VFX and motion graphics (compositing, tracking, keying, particles)
- Fairlight audio post-production (mixing, EQ, dynamics, ADR)
- Media management and project organization
- Speed Editor and hardware control surfaces
- Proxy workflows and performance optimization
- Collaboration and remote workflows
- Export settings and delivery specifications

TASK: Answer the user's question using only the provided DaVinci Resolve content excerpts. Match your answer's depth and complexity to the question:
- Technical questions → Specific step-by-step workflows with keyboard shortcuts and settings
- Creative questions → Artistic approaches with technical implementation details
- Troubleshooting questions → Diagnostic steps and common solutions
- Vague questions → Ask clarifying questions about their project type, Resolve version, or specific goal

APPROACH:
- Lead with practical, actionable workflows
- Include specific menu paths, keyboard shortcuts, and node structures where applicable
- Reference Resolve-specific terminology accurately (e.g., "Power Window" not "mask")
- Use only information explicitly stated in the context
- Focus on professional techniques that scale to real production work
- Emphasize non-destructive workflows and best practices

FORMAT FLEXIBILITY:
Prioritize these elements:
1. Clear step-by-step workflow or technique
2. Specific settings, values, or node configurations
3. Keyboard shortcuts and efficiency tips
4. Common pitfalls and how to avoid them
5. Alternative approaches for different scenarios
6. Performance considerations and system requirements

CITATIONS: Reference content naturally in your response. End with a "Sources" section listing content titles (no URLs).

CRITICAL CONSTRAINT: Only use information explicitly stated in the provided context. Do not make up settings, invent workflows, or add information not present in the sources.

EXAMPLES:

Color grading question: "How do I match shots from different cameras in DaVinci Resolve?"
Response: Comprehensive breakdown covering shot matching workflow using Color Match tool, manual matching with split screen, using scopes for technical matching, creating look consistency with shared nodes, and LUT-based approaches. Include specific node tree structures and scope readings from the content.

Editing question: "What's the best way to organize a large project in Resolve?"
Response: Direct explanation of bin structure strategies, Smart Bins, metadata-based organization, timeline markers, Power Bins for cross-project assets, and media pool best practices. Include specific keyboard shortcuts and menu paths from the content.

Fusion question: "How do I track a moving object for replacement in Fusion?"
Response: Actionable workflow covering planar vs point tracking, when to use each, tracker node setup, applying tracking data to other nodes, and handling tracking failures. Include specific node connections and settings from the content.

Audio question: "How do I properly mix dialogue in Fairlight?"
Response: Professional mixing workflow covering track setup, EQ for dialogue clarity, compression settings, noise reduction, room tone, and delivery specifications. Include specific frequency ranges and dynamics settings from the content.
"""
        user_tailor = (f"\n\nUser context to tailor recommendations: {user_context}" if user_context else "")
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context excerpts:\n{context}{user_tailor}"},
            {"role": "user", "content": f"Question: {question}\n\nProvide helpful guidance based only on the context above."},
        ]
        resp = client.chat.completions.create(
            model=os.getenv('WIKI_VAULT_OPENAI_MODEL', 'gpt-4o-mini'),
            messages=messages,
            temperature=0.2,
            max_tokens=max_tokens,
        )
        return resp.choices[0].message.content
    except Exception:
        return None


def _keywords(text: str) -> list:
    import re as _re
    toks = _re.findall(r"[A-Za-z0-9']+", text.lower())
    return [t for t in toks if len(t) >= 3]


def _rank_hits_by_keyword(question: str, hits: list, k: int) -> list:
    words = set(_keywords(question))
    if not words:
        return hits[:k]
    def score_hit(h: dict) -> float:
        txt = (h.get('content') or '').lower()
        score = sum(txt.count(w) for w in words)
        sim = h.get('score') or 0.0
        return score + sim
    ranked = sorted(hits, key=score_hit, reverse=True)
    seen = set()
    out = []
    for h in ranked:
        key = hash((h.get('content') or '')[:160])
        if key in seen:
            continue
        seen.add(key)
        out.append(h)
        if len(out) >= k:
            break
    return out


def _group_by_source(hits: list, max_sources: int = 5, per_source: int = 1) -> list:
    """Group hits by file_path/title and take top segments per source for diversity."""
    buckets = {}
    order = []
    for h in hits:
        meta = h.get('metadata', {}) or {}
        key = meta.get('file_path') or meta.get('title') or meta.get('source_title')
        if not key:
            key = h.get('id')
        if key not in buckets:
            buckets[key] = []
            order.append(key)
        buckets[key].append(h)
    selected = []
    for key in order:
        segs = buckets[key][:per_source]
        selected.extend(segs)
        if len(selected) >= max_sources * per_source:
            break
    return selected


@mcp.tool()
def ask_resolve_editor(question: str, top_k: Any = 18, max_tokens: Any = 2600, user_context: Optional[str] = None, response_style: str = 'detailed') -> Dict[str, Any]:
    """Ask questions about DaVinci Resolve editing, color grading, Fusion VFX, Fairlight audio, and professional video editing workflows. Get expert guidance with actionable techniques and step-by-step workflows. Returns {answer, sources}."""
    q = _get_query()
    k = _to_int(top_k) or 12
    mt = _to_int(max_tokens) or 2000
    # Adjust verbosity based on response_style
    style = (response_style or 'detailed').lower()
    if style == 'concise':
        mt = min(mt, 1200)
    elif style == 'comprehensive':
        mt = max(mt, 3200)
    initial = max(50, k * 5)
    hits = q.search(question, top_k=initial, collection='content')
    # Prefer transcripts
    filtered = [h for h in hits if (h.get('metadata', {}) or {}).get('doc_type') == 'transcript'] or hits
    filtered = _rank_hits_by_keyword(question, filtered, initial)
    # Diversify: take top segments grouped by source
    filtered = _group_by_source(filtered, max_sources=min(6, k//3 + 2), per_source=1)
    # Build context
    seen = set()
    parts = []
    for h in filtered:
        txt = h.get('content') or ''
        if not txt:
            continue
        key = hash(txt[:120])
        if key in seen:
            continue
        seen.add(key)
        meta = h.get('metadata', {}) or {}
        title = meta.get('title') or meta.get('source_title') or 'Untitled'
        section = meta.get('section') or meta.get('concept_name') or ''
        head = f"Source: {title}"
        if section:
            head += f" ({section})"
        parts.append(head + "\n" + txt)
    context = "\n\n---\n".join(parts)
    ans = _answer_with_openai(question, context, max_tokens=mt, user_context=user_context)
    if not ans:
        # Structured fallback
        parts = context.split("\n\n---\n")[:8]
        bullets = "\n\n".join(f"- {p[:300]}" for p in parts)
        ans = (
            f"# Answer (no OpenAI API available)\n\nBased on retrieved DaVinci Resolve content excerpts.\n\n"
            f"## Key Techniques\n\n{bullets}\n\n"
            f"## Suggested Next Steps\n\n- Review which workflow or technique applies to your current project\n- Practice the technique on test footage before applying to your main timeline\n- Experiment with variations to find what works best for your specific content\n"
        )
    # Build sources list (titles only, no URLs)
    sources = []
    seen_src = set()
    used_scores = []
    for h in filtered:
        meta = h.get('metadata', {}) or {}
        title = meta.get('title') or meta.get('source_title') or 'Untitled'
        url = meta.get('url') or meta.get('source_url')
        fp = meta.get('file_path')
        key = (title, url or fp)
        if key in seen_src:
            continue
        seen_src.add(key)
        sources.append({'title': title, 'url': url})
        if isinstance(h.get('score'), (int, float)):
            used_scores.append(h.get('score'))
        if len(sources) >= 5:
            break
    confidence = round(sum(used_scores)/len(used_scores), 3) if used_scores else None
    return {'answer': ans, 'sources': sources, 'confidence': confidence}


@mcp.tool()
def about() -> Dict[str, Any]:
    """Returns a short description of this MCP provider and how to use it."""
    try:
        import yaml as _yaml
        with open(CONFIG_PATH, 'r') as _f:
            _cfg = _yaml.safe_load(_f)
        kb = _cfg.get('knowledge_base', {})
        return {
            'name': kb.get('name') or 'Ask DaVinci Resolve Editor KB',
            'purpose': 'Search and get expert DaVinci Resolve video editing and color grading advice',
            'topic': kb.get('topic') or 'DaVinci Resolve editing, color grading, Fusion VFX, Fairlight audio, workflow optimization',
            'recommended_tools': ['ask_resolve_editor', 'about'],
            'notes': 'Use ask_resolve_editor for questions about DaVinci Resolve workflows, color grading, Fusion VFX, and audio. Example questions: "How do I create a cinematic color grade?", "What\'s the best node structure for skin tone correction?", "How do I track and replace a screen in Fusion?", "How do I use the Speed Editor for multicam editing?", "What are the best export settings for YouTube?". Get comprehensive answers with sources from expert DaVinci Resolve content.'
        }
    except Exception:
        return {
            'name': 'Ask DaVinci Resolve Editor KB',
            'purpose': 'DaVinci Resolve editing and color grading Q&A',
            'recommended_tools': ['ask_resolve_editor', 'about'],
            'notes': 'Ask questions about DaVinci Resolve editing, color grading, Fusion compositing, Fairlight audio, and professional video workflows.'
        }


if __name__ == "__main__":
    # Run the MCP server (stdio)
    mcp.run()
