---
title: "Export Audio Transcriptions with Speaker and"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 158
---

# Export Audio Transcriptions with Speaker and

Timecode Information (Studio Version Only)

In DaVinci Resolve Studio when you export a transcription, the resulting text file will include speaker

name and timecode information for each speech block. This useful information will make searching

and navigating transcriptions much easier.

Transcripts include speaker and timecode information for dialog blocks.


Edit | Chapter 40 Text Based Editing

EDIT

Audio Transcription Supported Languages

You can choose which language is used to generate the transcription in the Project Settings > Subtitle

and Transcription> Transcription Setup section. You can select any of the supported language models,

or keep it on Auto for DaVinci Resolve to figure out who is speaking what.

As of this writing Audio Transcription and Text-Based Editing support the following languages:

�Danish, Dutch, English, French, German, Italian, Japanese, Korean, Mandarin

(Simplified Traditional), Norwegian, Portuguese, Russian, Spanish and Swedish.

�Many other languages are also available by using the Extended AI Transcription Support

Package in the Extras Downloads Manager. These include: Afrikaans, Arabic, Armenian,

Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Croatian, Czech, Estonian, Finnish, Galician,

Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Kannada, Kazakh, Latvian, Lithuanian,

Macedonian, Malay, Marathi, Maori, Nepali, Persian, Polish, Romanian, Serbian, Slovak, Slovenian,

Swahili, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.

IntelliScript for Creating Timelines

from Scripts (Studio Version Only)

DaVinci Resolve 20 has a powerful AI-powered IntelliScript tool which uses the Transcription Engine

to match and generate a timeline using an original script. This feature lets you quickly assemble rough

cuts of scenes and even organizes multiple takes for you in the timeline. IntelliScript is smart enough

to understand context, so if your actor ad-libs and uses a similar phrase rather than the exact phrase

written in the script, it should still find it.

A simple text file script to feed into IntelliScript


Edit | Chapter 40 Text Based Editing

EDIT

To Use IntelliScript to generate a timeline based on a script:


Create a script file in plain text (.txt) format of just the spoken text. IntelliScript requires just the

plain spoken text that has full stops (.) after sentences. Standard script formatting with scene

descriptions, parentheticals, and character names will likely cause transcription issues.


Select all the clips you want to use for IntelliScript, right-click, and select AI Tools > Create New

Timeline Using IntelliScript.


DaVinci Resolve will then prompt you to load the text script file. Press Open.

When the transcription process is done, IntelliScript will create a new timeline, and on track one, lay

out the best clips in order based on the dialog in the script file. Any alternative takes are automatically

placed on additionally created tracks that are disabled by default. Once the timeline is set up, you

can review the best take on track one and preview alternative takes for specific regions, enabling and

disabling them as needed.

The IntelliScript results in the timeline. It places the best takes on track one, alternative takes on separate tracks, and

disables them by default. Here we overrode its choices at the end and manually enabled what take we thought was best.

NOTE: IntelliScript chooses the “best” take by matching the spoken dialog only. It does not use

any good take metadata or make any judgments based on anything other than dialog matching.

Text-Based Video Editing

(Studio Version Only)

After a Transcribe command has been applied, DaVinci Resolve now knows the exact timecode position

of each word in the clip, and that information opens up several useful text-based editing tools using

the Transcription window. Text-based video editing is available in the both the Cut and Edit pages.

The cursor in the Transcription window and the playhead in the Viewer are linked. As you move the

cursor in the text, the playhead updates to that respective position in the clip in the Viewer. This allows

you to precisely place the playhead exactly where you want it based on the text word, rather than

having to scrub back and forth through the audio track.

To move the playhead to a specific word in the clip:

�Click on a word in the Transcript window, and it will highlight with a red arrow. The viewer playhead

will then jump directly to the end of that word in the clip in the Viewer.

In addition to the cursor and playhead being linked, the In and Out points of a clip are also linked to

the selected range of the text in the Transcription window.


Edit | Chapter 40 Text Based Editing

EDIT

To select an In and Out range in the clip:

�Click and drag over the text in the Transcription window to highlight it in teal. The In point of

the clip is set just before the first word, and the Out point is set just after the last word in the

highlighted text.

To select the In and Out range of a sentence:

�Click on any word in the sentence and press the X key to select the whole sentence

and highlight it in teal.

Selecting a text range in the Transcription window (R) automatically sets In

and Out points for that range on the clip in the Viewer (L).

With an In and Out range set, you can now use the editing tools in the Transcription window to

perform some common editing and media management functions.

The Create Subclip and Add Marker

tools in the Transcription window

To create a new subclip from a selected range:


Select a range of text in the Transcription window, by clicking and dragging to highlight the

text in teal.


Press the Create Subclip icon in the lower left of the Transcription window.


In the Create Subclip window, enter a new name for the subclip and select the Create button.

To add a marker to a clip:


Either select a specific word in the Transcription window (red arrow) for a standard marker, or

select a range of text by clicking and dragging to highlight the text in teal for a duration marker.


Click on the Marker icon in the lower left of the Transcription window.

The Place on Top, Insert, and Append Edit icons

in the Transcription window


Edit | Chapter 40 Text Based Editing

EDIT

To edit an In and Out range into the current timeline:


Select a range of text in the Transcription window by clicking and dragging to highlight the

text in teal.


Click one of the Edit icons in the lower right of the Transcription window.

�Place on Top: Puts the selected edit range on a track above the one currently

selected in the timeline.

�Insert Edit: Inserts the selected edit range into the timeline at the timeline In point.

�Append: Adds the selected edit range to the end of the timeline.

Edit Timelines Based on Source Clip Transcription

You can use the transcription you generated from the original source clip to subsequently modify that

clip on the timeline. Entering this mode in the Transcription window will let you select, cut, and paste

text, and then mirror those changes to the timeline.

To use Timeline mode in the Transcription window, the clips on the timeline must be transcribed in the

Media Pool. To enter Timeline Transcription mode, click on the Timeline icon in the upper left of the

Transcription window.

The Timeline Transcription Mode icon in

the upper right of the Transcription window

Once you’ve activated the Timeline Transcription mode, you can use the text editing tools in the

window, and those changes will also appear on the timeline.

For example, in the clip below we selected a sentence in the Transcription window, and as you can

see, the In and Out points of that sentence were automatically set in the Timeline behind it.

Selecting a sentence in the Transcription window sets the corresponding In and Out points in the timeline.


Edit | Chapter 40 Text Based Editing

EDIT

Once you have the text selected, you can manipulate that selection using the standard Cut, Copy,

Paste, and Delete tools, and mirror those changes to the timeline. In the example below we will chop

out one sentence of a clip, then move it to an earlier position in the timeline.

Selecting the first sentence of the second clip and then right-clicking and using the Cut tool

Here we see the sentence cut out of the timeline

and replaced by silence (…) in the Transcription window.

Now we select the new In point of in the timeline by selecting the first part of the sentence of the

first clip in the Transcription window. Then we right-click and hit the Paste command.


Edit | Chapter 40 Text Based Editing

EDIT

The video of the sentence we cut out is pasted in that spot and now comes first in the Transcription window.

Now we select the hole in the timeline where we cut out the sentence originally by selecting

the (…) silence in the Transcription window. Then right-click and choose Delete.

The final timeline with the sentence moved and the hole deleted. All done

just by manipulating the text in the Transcription window.

Adding Clips to Timeline Transcriptions

While you are editing you can continue to add un-transcribed clips into the timeline. When an

un‑transcribed clip is detected, it is flagged in the Transcription window as “Transcription Pending”

in this case, simply select “Transcribe Missing Clips in Timeline” from the Option menu to start the

transcription of the all missing clips.


Edit | Chapter 40 Text Based Editing

EDIT

When an un-transcribed clip is added to the timeline, it’s flagged Transcription Pending in the Transcription window