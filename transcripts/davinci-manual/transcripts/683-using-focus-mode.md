---
title: "Using Focus Mode"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 683
---

# Using Focus Mode

Focus mode works as a Multi Tool that is designed for making efficient pointer-based selections and

edits, in conjunction with an assortment of commands for extending and editing selections that can

be triggered via customizable keyboard shortcuts. If you’re editing with a mouse and keyboard, this

mode is designed to let you work quickly by enabling a variety of different functions based on clicking

different parts of each clip in the Timeline.

Additionally, an important aspect of working in Focus mode is that this is the only mode that lets you

edit the Timeline during playback, which you can’t do in Pointer and Range modes.

�If no tracks have been selected: Whenever you make a selection with the hand, Timeline In and

Out points are set to the boundaries of the selection. Whenever you make a selection with the

crosshairs, Timeline In and Out points are set to the boundaries of the region you dragged. In all

cases, the tracks that contain selected clips and regions of clips are also selected.

�If tracks have been selected: Any clip on a selected track that intersects the playhead will

be automatically highlighted brightly. Clips on de-selected tracks will be ignored. Dragging a

crosshairs over one or more clips with the pointer overrides all automatic selections and selects

the regions of the clips you drag over, and the tracks they’re on.

�If In and Out points have been set: Clicking the bottom half of clips in the Timeline will select that

clip and track, and the In and Out points will change to encompass that clip.

To choose Range mode:

�Click the Range Selection tool (the crosshairs at the bottom of a track) in the toolbar.

�Choose Trim > Range mode.

�The keyboard shortcut is pressing - R.

To select an entire clip using the Hand tool of the Focus mode:

�Move the pointer to the bottom half of a clip until a hand cursor appears, and click once to select

that clip in its entirety.

Clicking the bottom half of a clip to select that clip in Focus mode

�Use the Hand to Command-click multiple clips to make either contiguous or noncontiguous selections.

�Use the Hand to Shift-click multiple clips to make contiguous selections.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

To select a range using the I-beam cursor of the Focus mode:

�Move the pointer to the top half of a clip until an I-beam cursor appears, and drag to select a

region of one or more clips. As you drag, the playhead follows the Out point.

Dragging within the top half of a clip to select a region in Focus mode

�Using the crosshairs, you can also Shift-click to expand or contract the selected region across

one or more clips.

�Using the crosshairs, you can also double-click to select an entire clip.

�Partial edit selections that contain a fade will copy with the fade intact.

To select a single frame using the I-beam cursor of the Focus mode:

�Move the pointer to the top half of a clip until the I-beam cursor appears, and click once to place a

point selection at the frame you clicked. The playhead also moves to this frame.

Clicking within the top half of a clip to make a single frame selection


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

�Using the I-beam cursor, you can also Command-click clips on higher and lower tracks to add

them to the single frame selection, aligned at the same frame. For example, you could do this to

split multiple clips at once. One frame selections can be on discontiguous tracks.

Command-clicking within the top half of multiple clips on multiple

tracks to add single frame selections at the same frame

To move a selection using the Hand tool of the Focus mode:

Once you’ve made a selection of one or more clips or regions using the Hand or I-beam cursor of the

Focus mode, you can move the pointer to the bottom half of any selected clip and drag the selection

to another position on the Timeline.

Commands For Editing and Extending the Selection

Once you’ve made one or more selections in the Timeline, there are a series of commands you can

use to modify or expand the selection. These commands were designed to be used alongside the

Focus mode, but they can be used in any mode.

Editing the Selection

There are six commands for changing the current selection, which let you move it from one clip

or group of clips in the Timeline to another. These commands only move the selected range of

clips/frames; they do not move the clips themselves. These commands are located in the Timeline

contextual menu under Edit Operations when you right-click on a clip.

�Move To Previous/Next Edit: Moves the current selection to the next clip/edit point to the left or

right in the Timeline.

�Move To Previous/Next Track: Moves the current selection to the next track up or

down in the Timeline.

�Move to Previous/Next Frame: Nudges the current selection to the left or right in the Timeline.

Extend Edit Selection

There are four commands for expanding the range of what’s selected in the Timeline, one clip or track

at a time. These commands are located in the Timeline contextual menu under Edit Operations when

you right-click on a clip.

�To Previous Edit: Expands the selection to include the previous clip to the left in the Timeline.

�To Next Edit: Expands the selection to include the next clip to the right in the Timeline.

�To Previous Track: Expands the selection to include the clip in the next track up in the Timeline.

�To Next Track: Expands the selection to include the clip in the next track down in the Timeline.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Locking Audio Tracks

Another step you can take to prepare before performing any kind of editorial operation is to lock

tracks with media that you don’t want to be affected by whatever it is you’re about to do. For example,

if you have a complex set of music edits on track A3 that you don’t want to be affected by operations

that will delete media that overlaps it, you can lock track A3 so those clips remain unaffected.

Locking an audio track

Clips on locked tracks cannot be moved, deleted, cut, or otherwise affected by editorial operations.

Furthermore, parameters of clips on locked tracks cannot be edited in the Inspector. However, clips on

locked tracks can be played back and mixed like any other audio clips.

To toggle the lock or unlock state of audio tracks in the Fairlight page, do one of the following:

�Click any track’s lock control to toggle lock on and off.

�Click any track’s lock control and drag over the lock controls of other tracks in the Timeline to

quickly lock or unlock several adjacent clips.

�Open the Index and click/drag one or more track lock controls to toggle lock on and off.

Splitting Clips

In addition to manually splitting timeline clips in either Pointer or Range mode, Fairlight offers two

additional methods of managing your timeline audio. These are Remove Silence and AI Checkerboard

to New Tracks, which, along with AI Create ADR Cues, comprise the Intellicut feature set. For more

information about AI Create ADR Cues, see Chapter 172 “ADR (Automated Dialog Replacement).”

Remove Silence (Studio Version Only)

This feature identifies silent sections of a timeline clip and non-destructively removes them to increase

the efficiency of your workflow.

Audio clip with silence indicators


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Remove Silence Parameters

Remove Silence dialog

�Threshold: This determines the maximum signal level of your audio (in dB) that will be recognized

as silence. Audio signals below the threshold value will be treated as silence and removed. Higher

threshold values result in more audio being removed.

�Pre Head: Sets the amount of silence or pre-roll before each audible section.

�Minimum to Strip: This parameter determines the minimum amount of silence (in milliseconds) to

be stripped from selected timeline clips.

�Higher values leave more silent sections in the audio. Lower values will result in more strips, but

you may find that some of the remaining audio sounds “chopped up” because it abruptly cuts off.

�Fade Head and Tail: When this checkbox is filled, fades are applied to the beginning and end of

each remaining clip based on the Pre Head and Post Tail values.

To remove silences from a timeline clip:


Select a clip or collection of clips on a track.


Right-click the selection and choose Remove Silence in the contextual menu.


The appearance of the selected audio will change to include vertical red stripes showing you

the position and duration of the resulting silences based on the parameter values in the Remove

Silence dialog.

AI Checkerboard to New Tracks (Studio Version Only)

If, for example, multiple actors were recorded with a boom mic on a single track and you need them on

separate tracks, this feature will analyze and transcribe the original audio, then organize the resulting

audio clips on separate tracks for each speaker’s voice.

To split speakers to new tracks:


Right-click the timeline clip, or range of a clip, and choose AI Tools > Checkerboard to New Tracks

in the contextual menu.

AI Tools contextual menu


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT


When the Transcribing Audio dialog opens, Fairlight will use AI to analyze the audio and identify

each voice.

Transcribing Audio dialog


A new track is created for each speaker, containing their new clips. The source timeline clip will be

muted and left intact.

New track timeline clips for each speaker

NOTE: You may find it helpful to change the colors of the new timeline clips and tracks and

timeline clips.

For more information on changing the color of a timeline clip, see “Changing Clip Color in the

Timeline,” later in this chapter.

For more information on changing the track color, see Chapter 170, “Using the Fairlight Page.”