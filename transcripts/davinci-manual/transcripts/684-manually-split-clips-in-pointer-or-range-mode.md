---
title: "Manually Split Clips in Pointer or Range Mode"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 684
---

# Manually Split Clips in Pointer or Range Mode

To split one or more clips in either Pointer or Range mode:


Select each track that has a clip you want to split.


Move the playhead to intersect the clips you want to split at the frame where you want the split

to happen.


Do one of the following:

a)	 Choose Timeline > Split Clip or press Command-\ (backslash).

b)	 Choose Timeline > Razor or press Command-B.

When splitting a clip in the Edit page, a through edit appears to show that you currently have an edit

with continuous timecode running from the outgoing to the incoming half. This is called a through edit

and is displayed in the Edit page with a dotted line running along its edge so you know that it’s special.

The Fairlight page doesn’t display through edits as of the time of this writing.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Linked Clips in the Fairlight Page

Clips can be linked together in the Fairlight page. When multiple clips are linked, Fairlight editing

commands treat all linked clips as if they were a single clip. Anything you would do to a single clip is

done to all linked clips at once. Selecting one item of a linked clip selects all items. Editing the In point

of one item of a linked clip edits them all.

To link two or more clips together:


Select all clips you want to link together.


Right-click one of the selected clips, and choose Link Clips from the contextual menu.

A link indicator at the bottom left of every clip you’ve just linked shows their new linked status.

Trimming Clips Without

Rippling the Timeline

Most basic adjustments in the Fairlight page only affect the selected clip or region of the Timeline.

Clips to the right of the adjusted area of the Timeline are generally left alone so as not to inadvertently

change sync when you don’t expect it. This section covers the most basic parts of the Fairlight page’s

“seven-point editing” paradigm.

Multi-Point Editing Overview

Each clip in the Timeline has several draggable handles and click targets that let you perform different

editing tasks using the pointer.

�In point: The left edge of the clip can be dragged to resize the beginning of the clip.

�Out point: The right edge of the clip can be dragged to resize the end of the clip.

�Fade In handle: A handle at the upper left-hand corner of the clip that only appears when the

mouse is positioned over that clip, used to fade the audio in by dragging it to the right, or as

part of a crossfade between two audio clips. Fades can be reset (eliminated) by double-clicking

the fade handle.

�Fade In curve: A handle at the center of the Fade In curve that only appears when the curve is

exposed, used to adjust the power of the fade in. This handle can be dragged vertically to change

the X-Level of the fade, and horizontally to change the X-Point of the fade. Fade curves can be

reset by double-clicking the curve handle.

�Fade Out handle: A handle at the upper right-hand corner of the clip that only appears when

the mouse is positioned over that clip, used to fade the audio out by dragging it to the left, or as

part of a crossfade between two audio clips. Fades can be reset (eliminated) by double-clicking

the fade handle.

�Fade Out curve: A handle at the center of the Fade Out curve that only appears when the curve

is exposed, used to adjust the power of the fade out. This handle can be dragged vertically to

change the X-Level of the fade, and horizontally to change the X-Point of the fade. Fade curves

can be reset by double-clicking the curve handle.

�Level: Considered an editorial characteristic, the level of any given audio clip can be adjusted via

a level overlay running across each clip. The level of any clip can be reset to the default 0.0 dB by

double-clicking the level overlay.

�Position: Clicking anywhere within the middle of a clip in Pointer or Range mode, or on the bottom

of Focus mode, lets you drag that clip either forward or backward in time, or to another track.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Resizing the In and Out Points of a Clip

Trimming the head or tail of a clip in the Fairlight page means to resize the In or Out point of that clip,

making it shorter or longer accordingly.

To resize the beginning or end of a clip:

�To shorten or lengthen clips: Move the pointer over the beginning or end of a clip, and when

it turns into the Resize cursor, drag the In or Out point to the left or right to change the clip’s

length. As you drag the In or Out point of an audio clip in the Fairlight page, an overlay appears

showing the waveform of all available media at the head (if you’re dragging the In point) or tail

(if you’re dragging the Out point) of the clip you are resizing.

The overlay seen when resizing the In point of an audio clip in the Fairlight page

To quickly resize the beginning or end of a clip to

the very beginning or end of available media:

�Double-click the In point of the clip to move the In point to the very beginning of that clip’s media.

�Double-click the Out point of the clip to move the Out point to the very end of that clip’s media.

If you resize a clip’s In or Out point to overlap one or more neighboring clips in the Timeline, the

overlapping parts of the neighboring clips will be overwritten by the clip you’ve resized.

Trim Start and Trim End

The Trim > Trim Start (Shift-[) and Trim End (Shift-]) commands let you move the In or Out point of

all clips that intersect the playhead as either a ripple operation (in Trim mode) or a resize operation

(in Selection mode). You do not need to make a selection to use Trim Start and Trim End, making

these commands fast to use in the right situation. A classic use of Trim End is when you have several

superimposed clips of different lengths that you want to either start or end at the same time.

�Trim Start resizes or ripples (depending on what mode you’re in) all clips that intersect the

playhead, so that each clip’s In point is moved to the current playhead position.

�Trim End resizes or ripples intersecting clips so that each intersecting clip’s Out point is moved to

the current playhead position.

Clips that don’t intersect the playhead are not affected. Furthermore, you can exclude clips on specific

tracks from this operation by locking those tracks.

Trim to Selection

The Trim > Trim to Selection (Shift-Command-T) command simultaneously trims the heads and tails

outside of a selection of one or more clips so that the selection is all that remains. This command is

found within the Timeline contextual menu when you right-click on a clip.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

(Left) A selection that includes parts of two clips, (Right) The result of using

Trim to Selection to eliminate the heads and tails outside of this selection.

Moving and Overwriting Clips

There are a number of ways to move clips in the Timeline. Clips can be nudged and moved within

a track, changing the timing of that clip’s position in the edit or they can be moved up or down to

other tracks.

To move clips in the Timeline, do one of the following:

�To move one or more selected clips in the Timeline: Drag any clip in the Timeline to any other

position. If you’re in Focus mode, you must drag using the bottom half of the selection. If you drag

a clip to overlap another clip, the clip you’re dragging overwrites the clip you’re moving it over.

�To nudge one or more selected clips in the Timeline by frame using the keyboard: Make a

selection, then press the Comma key (nudge 1 frame left) or Period key (nudge 1 frame right) to roll

the selected edit to the left or right. Shift-Comma and Shift-Period nudges by 5 frames.

�To move one or more selected clips up or down to other tracks at the same time: Make a

selection, then hold the Shift key down while dragging one of the selected clips up or down in

the Timeline to lock their position in time while moving them to other tracks. Or, you can hold the

Option key down and press Up or Down Arrow.

Sync Offset Indicator

Audio clips in the Fairlight page display an “out-of-sync” or sync offset indicators when they’re moved

out of sync with the video items they’re linked to.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Snap to Playhead

While in Focus Mode, you can snap the head (beginning) or tail (end) of an audio clip to the playhead

location (destination). This is useful when you want to line up audio with an onscreen event, such as a

ball smashing a window.

Although “Automation follows edit” works with this function, there are some things to consider:

�This function works even if the playhead is offscreen.

�Clips can only be snapped individually and to a location on the same track.

�A “snapped” clip overwrites existing audio at the destination, even if the affected audio is on the

top layer of a layered clip.

�A group of clips on a single track selected in Range mode using the playhead position can also

be a destination. However, you would need to snap the clip to the side of the playhead that

doesn’t have pre-existing audio you want to keep. For more information Range Mode, see “Using

Range Mode.”

To Snap to the clip head to the playhead:


Activate Focus Mode and move the playhead to the intended destination.


Hold down Command-Option and click the clip you want to move.

The Audio is now in the new location with the head of the clip snapped to the playhead.

To Snap to the clip tail to the playhead:


With Focus Mode active, move the playhead to the intended destination.


Hold down Command-Option-Control and click the clip you want to move.

The Audio is in the new location with the tail of the clip snapped to the playhead.

Subframe Nudging

In the Preferences/User/Editing panel under General Settings you can change the nudge amount by

either subframes or by milliseconds for the Fairlight page. These are completely user definable so that

you can type your desired nudge amount into the corresponding box.

Be sure to fully investigate this settings panel, which includes pre-roll and post-roll settings and other

useful Fairlight adjustments.

Slipping

Formerly called re-syncing, slipping an audio clip keeps that clip in the same place in the Timeline

while changing the range of media that appears in that spot. Slip edits do not change the duration of

the overall Timeline, and they don’t move the clip’s position relative to the other clips in the Timeline.

Slipping simply changes the range of media that clip represents.

NOTE: While available in previous versions of Fairlight, slipping is not available at the time of

this writing.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT