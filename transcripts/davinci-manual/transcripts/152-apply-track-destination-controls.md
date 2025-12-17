---
title: "Apply Track Destination Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 152
---

# Apply Track Destination Controls

Using the Track Header Context Menu

In addition to dragging the track destination controls between tracks in the timeline track headers, you

can right-click in a track destination to access a context menu to quickly choose and assign a source

audio or video track.

Right-clicking on the destination

control (A1) opens a contextual

menu, letting you quickly

choose which audio track of

your source clip will be edited

to track A1 on the timeline.

This is especially useful for source clips with multiple audio tracks or timelines with multiple video

tracks to quickly assign track destination controls. Additionally, when your source has more tracks

than available on the timeline, the context menu gives you access to patch the additional tracks in

the source.

Setting In and Out Points in the Timeline

When you’re setting up an edit to the Timeline, you can oftentimes get away with simply putting the

Timeline playhead at the frame where you want to edit the incoming source clip. In the absence of In

or Out points, the playhead is used as the In point. However, you can set up different kinds of edits by

setting specific In and Out points to define different ranges of the Timeline.

Methods of setting and clearing In and Out points in the Timeline:

�To set an In or Out point: Select the Timeline or Timeline Viewer by clicking or pressing the Q key,

then use the transport controls, jog bar, or control panel buttons to move the playhead, and press

the I key to set an In point, or the O key to set an Out point.

�To clear In or Out points: With the Timeline Viewer selected, press Option-I to clear the current In

point, or Option-O to clear the current Out point.

�To clear both the In and Out points at once: Press Option-X.

´In and Out points shown

in the Timeline, with

unmarked areas outside

the selection dimmed


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Methods of moving In and Out points in the Timeline:

�Move the playhead, and then press the I or O keys to change the In or Out points to the new

position of the playhead.

�Drag any In or Out point in the Timeline ruler to another position.

The area of the Timeline outside the region that’s currently defined by In and Out points is dimmed, to

call attention to the portion of the Timeline that will be affected by the next edit you’ll make.

To move the playhead to an In or Out point in preparation for making an adjustment:

�Press Shift-I to immediately move the playhead to the current In point, or Shift-O to move the

playhead to the current Out point.

The Go to In and Go to Out commands are capable of placing the playhead at the implicit (but

unmarked) In and Out points defined by a three point edit you’re setting up, even when Preview

Marks have not been enabled. For example, if you mark In and Out points in the Timeline, and you

then mark an In point for a clip in the Source Viewer, pressing Shift-O (Go to Out) automatically

moves the Source Viewer playhead to the frame that will be the Out point of that clip were you to

execute this edit.

In and Out points set in the Timeline and an In point set in the Source Viewer set up a three point edit.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Using Go to Out to move the Source Viewer playhead to the implicit Out point defined by a three point edit

Mark Clip and Mark Current Selection

These commands are automatic ways of setting In and Out points in the Timeline both at once, using

the timing of other clips. They’re both exceptionally handy for defining the range of an incoming edit

using clips that are already in the Timeline that you want to replace, or gaps in the Timeline that you

want to fill.

In short, Mark Clip uses the first and last frame of a target clip or gap in the Timeline to automatically

set Timeline In and Out points for editing. For example, if there’s a shot in an edit that you want to

replace with a different take of the same action, or there’s a gap in a sequence of clips that you’d like

to quickly fill with B-roll, you can use the Mark Clip command to help set this up.

Mark Current Selection uses the first and last frames of a range of selected clips to automatically

set Timeline In and Out points for editing. A good example is when you have a series of clips in the

Timeline, all of which you’d like to overwrite with a single incoming source clip, you can use the Mark

Current Selection command.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

To use Mark Clip:


Move the playhead to intersect either a clip you want to use to set In and Out points, or a gap

(empty area) between two other clips that you want to target. The playhead can be on any frame of

this clip, it doesn’t matter which.

Positioning the playhead

at a clip you want to mark


If there are other clips on a multi-track timeline that overlap the clip you’re targeting for this

operation, then the clip on the lowest video track will be used as the target to set the In and Out

points. If you want to target a clip on a higher track, then either disable the Auto Selection controls

of all timelines underneath, or Option-click the Auto Selection control of the track with the clip

you’re targeting to solo it, which will force that track to be the target of this operation.


Press the X key to automatically set In and Out points that match the first and last frames of the

target clip.

Using Mark Clip to set

In and Out points that

match a clip’s duration

TIP: To clear both In and Out points, press Option-X, which is the opposite of this command.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

To use Mark Selection:


Select one or more clips in the Timeline.

Selecting clips you want

to use as a range to

mark In and Out points


Press Shift-A to automatically set In and Out points that match the first and last frames of

the selection. A range of discontinuous clips will produce the same result as a range of

continuous clips.

Marking a selection to

set In and Out points

TIP: You can also mark gaps in the Timeline with Mark Selection.

Preview Marks During Three‑Point Editing

In order to help you see what will happen whenever you execute a three-point edit, preview marks

appear in either the Source Viewer or the Timeline Ruler to let you know the exact duration of the

Timeline that’s about to be affected by the edit you’re preparing to make. To prevent them from being

a distraction, preview marks only appear once you’ve explicitly marked three edit points in the Source

Viewer and Timeline, and they can be turned on and off by choosing View > Show Preview Marks.

For example, if you set In and Out points in the Source Viewer, and an In point in the Timeline, then a

preview marker will appear in the Timeline Ruler to show the implied Out point in the Timeline of the

edit you’re about to make.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

A preview marker in

the Timeline shows the

Timeline Out point being

automatically calculated

by DaVinci Resolve

based on the In and

Out points that are set

in the Viewer, and the

In point in the Timeline

On the other hand, if you set both In and Out points in the Timeline, and only an Out point in the

Source Viewer, a preview marker appears in the jog bar of the Source Viewer to show you the

implied In point, in the Source Viewer, of the edit you’re about to make.

A preview marker in the

Source Viewer shows

the Source Viewer In

point being automatically

calculated by DaVinci

Resolve based on the

In and Out points that

are set in the Timeline,

and the In point in

the Source Viewer

If you like, you can move the playhead to the position of the preview mark by using Shift-I if the

preview mark is an In point, or Shift-O if the preview marker is an Out point.