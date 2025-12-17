---
title: "Append to End"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 156
---

# Append to End

Append to end always puts the edited clip at the very end of the current Timeline. It’s a very useful

edit type when you’re quickly stringing together a series of clips.

To use append to end to edit a clip into the Timeline:


Set In and Out points in a source clip that you want to add to the end of the current Timeline. If

necessary, change the sort order of the Media Pool to put these clips into the order in which you

want them to be added to the Timeline.


Click the audio and video destination controls of the tracks you want to edit the incoming source

clip onto. If necessary, create new tracks.


Choose Edit > Append to End of Timeline, drag the clip to the Append at end overlay of the

Timeline Viewer, or press Shift-F12.

Incoming video clips are added after the very end of the last clip in the Timeline.

Insert Selected Clips to Timeline Using Timecode

Clips can be edited directly from the Media Pool into a timeline, such that each clip’s source timecode

is aligned with an identical record timecode value in the Timeline. This can be useful for long form

multi-camera events, like weddings or concerts, where all cameras are linked by the same timecode

to ensure all edits are perfectly synced. This function matches the Source Overwrite edit on

the Cut page.

IMPORTANT: The timecode of the Timeline must overlap the timecode of the clip(s) for this

edit to function. This can be set in the Start Timecode field of the New Timeline settings.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

To insert selected clips to timeline using timecode:


Select one or more clips to edit into the Timeline in the Media Pool. If there are In and Out points

set on the clip, the edit will respect those boundaries. If no In/Out points are set, each selected

clip’s full duration will be edited in its entirety.


Set a destination control to determine which track in the Timeline you want to edit to.


Right-click one of the selected clips and choose “Insert Selected Clips to Timeline Using

Timecode” from the drop-down menu.


All of the selected clips will be overwritten into the Timeline at their appropriate timecode

locations onto the destination track.

IMPORTANT: If multiple selected clips have overlapping timecode, no edit will occur.

Insert Selected Clips to Timeline With Handles

“Insert Selected Clips to Timeline With Handles” is a command that’s available from the Media Pool

contextual menu for editing one or more selected clips to the currently open timeline, such that the

default handle length is subtracted from the beginning and end of each clip. The goal is to make it

easy to string together a series of clips that you want to connect using transitions by automatically

changing the In and Out points of each clip being edited into the Timeline in order to add handles.

To use insert selected clips to timeline with handles to edit one or more clips into the Timeline:


Select one or more clips in the Media Pool that you want to add to the Timeline. If necessary,

change the sort order of the Media Pool to put these clips into the order in which you want them to

be added to the Timeline.


Click the audio and video destination controls of the tracks you want to edit the incoming source

clip onto, and position the playhead where you want the incoming clips to start. If necessary,

create new tracks.


Right-click one of the selected clips in the Media Pool and choose “Insert selected clips to timeline

with handles” from the contextual menu.

The selected clips are added to the Timeline starting at the position of the playhead.

To change the length of handles that are removed, open the Editing panel of the User Preferences

and change the “Default handles length” setting. Handles will not be added in either of the following

two cases:

�If any of the selected clips in the Media Pool already have handles because of In and Out points

that you’ve set, then additional handles won’t be added.

�If the duration of the frames to be removed to create handles in this operation is greater than the

duration of one or more of the clips you’ve selected in the Media Pool, then handles won’t be

added at all.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Three-Point Editing From the Media Pool

You can also execute three-point edits directly from the Media Pool, with no need to use the

Source Viewer.

Example: Assembling Clips Into the

Timeline From the Media Pool

If you want, you can also edit clips directly into the Timeline from the Media Pool using a variety of

commands. This can be a fast way of appending clips to the end of the Timeline (although you can also

perform insert edits this way).

To edit one or more clips from the Media Pool to the Timeline:


If necessary, set In and Out points for each of the clips you want to edit into the Timeline

using either the Media pool thumbnails (in Thumbnail view), the Media Pool Filmstrip Viewer

(in List view), or by opening each one into the Source Viewer. For each method, press I to set an In

point, and O to set an Out point.


Change the sort order of the Media Pool’s browser area to put the clips into the order in which you

want them to appear. In Thumbnail view you can use the Sort Order menu, but in List view you can

click the header of any metadata column to sort by that column’s data.


Position the playhead to where you want to edit the clips.


Click, drag, use the Command-Option and Command-Shift Up and Down Arrow Key shortcuts,

or use the Option-1–8 and Command-Option-1–8 key shortcuts to assign the video and audio

destination controls to the tracks you want to edit the video and audio of the incoming clip(s) to.

Click any destination control itself to disable it if you want to edit clips into the Timeline as audio or

video only.


Select one or more clips you want to edit. Insert, overwrite, place on top, ripple overwrite, and

append at end edits are all capable of editing multiple clips at once, while replace and fit to fill

edits can only edit one clip at a time, and will only edit the first of multiple selected clips into

the Timeline.


To perform the edit, do one of the following:

�Drag the selected clips to the Timeline Viewer and drop them on an editing overlay to execute

that edit type.

�Right-click one or more selected clips in the Media Pool, and choose “Insert Selected Clips to

Timeline,” or “Append Selected Clips to Timeline.”

The selected clip(s) are edited into the Timeline.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Chapter 40

Text Based Editing

Recent advances in Machine Learning have made it possible to organize, edit, and

refine clips by analyzing the spoken dialog, then converting that speech into text.

This chapter covers the usage of DaVinici Resolve’s Text Based Editing toolset.

Contents

Audio Transcription (Studio Version Only)�������������������������������������������������������������������������������������������������������������������������������� 848

Transcribe Audio����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 848

The Transcription Window���������������������������������������������������������������������������������������������������������������������������������������������������������������� 849

Editing Text in the Transcription Window����������������������������������������������������������������������������������������������������������������������������������� 851

Detect Speakers During Transcription (Studio Version Only)������������������������������������������������������������������������������������������ 853

Export Audio Transcriptions with Speaker and Timecode Information (Studio Version Only)������������������������ 855

Audio Transcription Supported Languages����������������������������������������������������������������������������������������������������������������������������� 856

IntelliScript for Creating Timelines from Scripts (Studio Version Only)��������������������������������������������������������������������� 856

Text-Based Video Editing (Studio Version Only)������������������������������������������������������������������������������������������������������������������� 857

Edit Timelines Based on Source Clip Transcription������������������������������������������������������������������������������������������������������������� 859

Import and Export Transcriptions using SRT Files�������������������������������������������������������������������������������������������������������������� 862


Edit | Chapter 40 Text Based Editing

EDIT

Audio Transcription (Studio Version Only)

The most critical metadata about any clip is knowing what people have said in it. A full transcription

of a shot is useful in narrative film letting you find specific clips based on the dialog in the script, but a

transcript is especially important in unscripted documentary and news production, both to understand

what pieces of the story you actually captured and for a variety of organizational, creative and

legal requirements.

Until recently, transcribing audio was a labor-intensive process requiring a human being to listen to

a clip in real time and then type out what was being said in a log sheet. With recent advances in the

DaVinci Resolve Neural Engine, your computer can now perform the tedious work of transcribing each

clip for you automatically, and most importantly, accurately. In addition, having text transcripts attached

to the clips in your project gives you powerful new text-based editing tools to select, search and insert

clips into your timeline.

Transcribe Audio

The Transcribe Audio feature is accessed via the Media Pool in the Media, Cut, Edit, and Fairlight

pages and is a fully automated process.

The Transcribe Audio

icon in the Media

and Edit pages

To automatically transcribe the audio of a clip:


Select a clip or clips with audio to transcribe in the Media Pool.


Right-click on any of the selected clips and select AI Tools > Audio Transcription > Transcribe from

the contextual menu. Or click on the Transcribe Audio icon in the Media Pool toolbar.

The Transcribing

Audio window

At this point the Transcribing Audio window will appear, showing you how many clips are left to

analyze, the speed at which the analysis is taking place vs. real time, and approximately how

much longer the analysis of the selected clips will take. There is a button to cancel this operation

at any time.

The speech balloon icon

showing that a clip has

been transcribed

Any clip that has a transcription attached to it will have a small speech balloon icon appear in the

lower left of its thumbnail in the Media Pool.


Edit | Chapter 40 Text Based Editing

EDIT

To remove a transcription from a clip:


Select a clip you want to delete the transcription from in the Media Pool.


Right-click on the selected clips and select AI Tools > Audio Transcription > Clear Transcription

from the contextual menu.

Audio Transcription of Timelines

Audio Transcription works not just with clips but for timelines as well and in the same way as described

above. There are several practical uses for a text transcription of a timeline for legal and organizational

requirements. However, if you’re intending to make subtitles or captions for the Timeline, there is a

dedicated tool specifically for that purpose.

For more information on the Create Subtitles from Audio feature, see Chapter 52, “Subtitles

and Closed Captioning.”