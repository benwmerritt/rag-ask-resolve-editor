---
title: "Compatible Audio Formats"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 681
---

# Compatible Audio Formats

DaVinci Resolve is compatible with WAVE, Broadcast WAVE, AIFF, MP3, AAC (M4A), CAF (macOS only),

both MTS and QuickTime containers that use the AC3 audio format, and Enhanced AC-3 (macOS and

Windows only). DaVinci Resolve is compatible with audio at sample rates including 32, 44.1, 48, 88.2,

96, and 192 kHz. Linux users have the added ability to encode and decode MP3 files in Fairlight.

DaVinci Resolve 17 adds Dolby Atmos ADM file creation and manipulation as well as the ability to

export Dolby Atmos masters as IMF deliverables. IMF (Interoperable Master Format) is a SMPTE

standard for a single master file format that incorporates all the media and metadata necessary to

deliver what’s necessary.

ADM Import

Importing an ADM file into a project will open the Bed mix or mixes and any associated Object tracks

into a timeline. They will be imported onto corresponding track types of the audio files embedded into

the ADM. For instance, if a Bed file is 7.1.2, then on import that file will open in a 7.1.2 track in Fairlight.

Object files will be created as separate tracks in Fairlight containing all of their panning data.

NOTE: If bringing in a Dolby Atmos file from the Media Pool, it will render the file dynamically

to the chosen output format directly on the Timeline using the Dolby Renderer. However,

Fairlight can import the full Atmos file with beds and objects if imported from the Fairlight

menu instead - Fairlight > Immersive > Audio > Import Master File. By bringing a file in this

way, it will create a timeline with all of that file’s Atmos program and dynamic metadata

properly mapped and routed.

Editing Audio Clips Into the Timeline

The Fairlight page offers a complete audio editing environment that lets you either record and

assemble clips from scratch, or refine tracks full of audio clips that have been edited together in

different ways. There are four ways of adding media to the Timeline in the Fairlight page, depending

on the type of work you do:

�Recording new audio into one or more tracks,.

For more information, see Chapter 173, “Recording.”

�By dragging and dropping new audio clips from the Media Pool into the Fairlight timeline

�By editing audio clips into audio tracks on the Edit page

�By importing a project with audio clips

�By auditioning and confirming sound effects from the Sound Library

However audio clips come to be in your timeline, the rest of this chapter covers the myriad methods

available to edit and sweeten the contents.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Overwriting Vs. Layering Clips That Overlap

When you add clips to the Timeline, what happens when you add a clip that overlaps another clip

that’s already in the track you’re editing to depends on the Timeline > Layered Audio Editing setting.

By default, with Layered Audio Editing turned off, overwriting one audio clip with another results in

the overlapping part of the overwritten clip being non-destructively deleted from the Timeline by the

incoming clip.

However, if you turn Layered Audio Editing on, then incoming clips do not overwrite overlapping

clips in the Timeline; instead, they’re layered within that track, such that the incoming audio clip takes

precedence over what was previously there, but overlapping audio segments that were previously in

the Timeline are preserved, which can be seen when you choose View > Show Audio Track Layers.

In this way, you can choose whether you want to overwrite previously edited clips, or layer newly

edited clips, as your needs require, regardless of whether or not Audio Track Layers are visible. Audio

layering can be enabled in both the Edit and Fairlight pages.

For more information about audio layering, see the section later in this chapter.

Choosing Parts of Clips to Edit in the Media Pool

The Media Pool has a preview player at the top that provides a place to open selected source clips in

the Media Pool, play them, add marks to log them, and set In and Out points in preparation for editing

them into the Timeline via drag and drop. The Media Pool Preview Player effectively acts as a Source

monitor for editing in the Fairlight page.

The preview player in the Media Pool

�Various viewing controls populate the title bar at the top. A dropdown menu at the upper left lets

you choose a zoom level for the audio waveform that’s displayed. To the right of that, a Timecode

window shows you the duration of the clip or the duration that’s marked with In and Out points.

Next to the right, a real-time performance indicator shows you playback performance. In the

center the title of the currently selected clip is shown, with a dropdown menu to the right that

shows you the most recent 10 clips you’ve browsed. To the far left, a Timecode field shows you

the current position of the playhead (right-clicking this opens a contextual menu with options to

change the timecode that’s displayed, and to copy and paste timecode).

�The center of the Media Pool Preview Player shows you the waveforms in all channels of the

currently selected clip, at whatever zoom level is currently selected.

�Transport controls at the bottom consist of a jog bar for scrubbing, Stop, Play, and Loop buttons,

and In and Out buttons.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Dragging Audio Clips Into the Timeline

You can open the Media Pool in the Fairlight page, and edit audio clips into the Timeline in their

entirety by dragging and dropping individual clips onto whichever audio track you want them to

appear. You can drag any clip onto any track, regardless of whether or not the channels of the clip

match the channel mapping of the track. However, if you edit a clip with more channels than a track

has (for example, editing a stereo clip onto a mono track), only the channels supported by that track

will be output, with all other channels in that clip being muted. If this happens, you can always remap

the audio track by right-clicking the track header and choosing a new mapping from the Change Track

Type To submenu.

TIP: Dragging one or more clips to the empty area underneath the existing audio tracks of

the Timeline results in the creation of new tracks, each of which is automatically mapped to

however many channels are required by each audio clip being edited.

When working with Ambisonics files, dragging a clip to the timeline or creating a new timeline

that refers to a clip creates a track of the appropriate type, matching the file’s Ambisonic order

and channels.

If you want to edit several clips into the Timeline at once by dragging them from the Media Pool, you’ll

probably want to do a bit of preparation to make sure they’re edited in the right order.

Dragging several clips into the Timeline as one contiguous series of edited clips:


Change the sort order of the Media Pool’s browser area to put the clips into the order in which you

want them to appear. In Thumbnail view you can use the Sort Order menu, but in List view you can

click the header of any metadata column to sort by that column’s data.

Using the Sort

Order menu to

change the sort

order of clips in

the Media Pool


Use the Media Pool thumbnails, the Media Pool List view Filmstrip, or the Source Viewer to set In

and Out points to define the part of each clip that you want to edit into the Timeline.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT


Select the Media Pool clips you want to edit into the Timeline by dragging a bounding box,

Command-dragging multiple bounding boxes over different sets of clips, by Shift-clicking a range

of clips, or by Command-clicking individual non-contiguous clips.


Drag any of the selected clips to the desired position in the Timeline to perform an overwrite edit.

The clip(s) you drag overwrite whatever other clips they overlap in the Timeline. Multiple clips

dragged from the Media Pool will be edited in the order in which they’re sorted in the Media Pool,

using each clip’s In and Out points.

It’s possible to edit audio clips into the Timeline so that each clip’s timecode lines up with the

Timeline Ruler. This can be useful if you’re organizing multiple source audio recordings that

you want to synchronize together on multiple tracks.

Dragging multiple clips to edit them into a track at their timecode positions:


Select the Media Pool clips you want to edit into the Timeline by dragging a bounding box,

Command-dragging multiple bounding boxes over different sets of clips, by Shift-clicking a range

of clips, or by Command-clicking individual non-contiguous clips.


Hold Command-Shift down, and drag the selected clips into the track you want them to appear, to

perform an overwrite edit.

A series of audio clips edited into the Timeline by timecode position

Each clip edited into that track appears at the same timecode position as its embedded timecode.

This means that if you were recording time-of-day timecode, each clip will appear on the Timeline

at the time it was recorded. A series of clips recorded during hour 10 through 13 will appear

distributed throughout hours 10-13 on your timeline.

You can also edit two or more audio clips into the Timeline as a stack, in preparation for layering

multiple sound effects for doing sound design work.

Dragging multiple clips to edit them into a track as a parallel stack:


Select the Media Pool clips you want to edit into the Timeline by dragging a bounding box,

Command-dragging multiple bounding boxes over different sets of clips, by Shift-clicking a range

of clips, or by Command-clicking individual non-contiguous clips.


Command-drag the selected clips into a track of the Timeline. The first of the selected clips

appears in the track you’re dragging to, the other clips appear either in audio tracks underneath

the first one, or if there are no audio tracks available, in new audio tracks that will be created to

hold those clips.

All clips you’ve edited appear as a parallel stack, in separate tracks, one on top of another.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Moving Audio Clips to Embedded Timecode Position

All clips have a timecode embedded into their metadata. There are options to place clips onto the

Timeline from either the Media Pool or in the Timeline itself with this metadata.

Right-clicking a clip in the Timeline has the choice to Move to Embedded Start Timecode. When this is

clicked the clip will spot onto the Timeline on a selected track with the timecode.

It’s important to be aware of the embedded audio timecode and the Timeline timecode.

The two must have overlapping timecode, or this function will not work.

For example, a clip that has an embedded timecode of 00:00:00:00 may be difficult to find on

a Timeline that starts at 00:59:58:00. If you have spotted a clip using these tools and still don’t

see the clip in question, then check the embedded timecode in the Metadata panel of the

Inspector as well as the timecode of the Timeline itself.

Right-clicking a clip in a Timeline reveals the

Move to Embedded Start Timecode option.

Right-clicking a clip in the Media Pool reveals

the Insert Selected Clips to Timeline option.

Right-clicking a clip in the Media Pool has the choice to Insert Selected Clips to Timeline Using

Timecode. When this is clicked the clip will spot onto the Timeline on a selected track with the

embedded timecode.

NOTE: You can find the embedded timecode for a clip in the Inspector in the File tab under

timecode.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Timecode metadata is in the

Inspector window under the File tab.

Support for Mixed Audio Track Formats from Source Clips

DaVinci Resolve supports media with multiple audio tracks that have differently formatted channels

embedded within them. For example, a clip with one stereo track, one 5.1 surround track, and

six mono tracks can all be appropriately set up in the Audio panel of Clip Attributes after that clip has

been imported.

The Audio panel of Clip Attributes has controls over what format (Mono, Stereo, 5.1, 7.1, Adaptive)

the channels embedded within a particular audio track should be configured as. This means you

can set up clips with multiple tracks, each one using different formats of audio employing different

combinations of channels, which is useful for setting up imported audio mix files that you want to

output when mastering a program.

Clip Attributes now lets you assign channels among

different tracks with different channel assignments


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT