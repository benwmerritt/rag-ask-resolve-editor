---
title: "Dragging Preview Marks to Change an Edit"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 153
---

# Dragging Preview Marks to Change an Edit

You can drag preview marks to alter the edit you’re about to make. When you drag a preview mark,

the corresponding In or Out point that’s opposite the Viewer with focus is altered to accommodate

the new three-point edit you’re setting up. For example, if you have an In point in the Source Viewer,

and In and Out points set in the Timeline, a preview mark appears in the Source Viewer to show the

Out point that will be used to edit the clip in the Source Viewer into the Timeline. However, you can

drag this preview mark to the left in the Source Viewer, and the result will be that the Out point in the

Timeline will move along with it, since you’re retiming the edit.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Dragging a preview mark

in the Source Viewer

changes the opposite

edit point in the Timeline

The Rules of Three-Point Editing

In the previous examples, three-point editing was being used by virtue of source In and Out points

being set to define a range of the source clip to be edited into the Timeline, and the Timeline playhead

being used as the acting Timeline In point; three points defined the edit to be made. However, three-

point editing is also very useful when you need to overwrite sections of a previously edited timeline

with new source clips in a controlled manner, such as when adding an insert shot to a scene to cover a

particular change you’re making that would break continuity.

Depending on the combination of Source and Timeline In and Out points you set, the following rules

govern three-point editing:

�If there is no In point in the source clip: The first frame of media will be used as the acting source

In point. This can be seen by the thick bar that extends to the left of the Out point in the Source

Viewer’s jog bar.

A thick bar indicates which part of the source clip will be used in the absence of a Source In point


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

�If there is no Out point in the source clip: The last frame of media will used as the acting source

Out point. This can be seen by the thick bar that extends to the right of the In point in the Source

Viewer’s jog bar.

A thick bar indicates which part of the source clip will be used in the absence of a Source Out point

�If there are no In or Out points in the Timeline: The playhead will be used as the acting

Timeline In point.

�If you set a Timeline In point but no Timeline Out point: The whole range from the In to Out

points of the source clip is edited into the Timeline such that the Source In point is aligned with the

Timeline In point. This can be seen by the thick bar that extends to the right of the In point in the

Timeline Ruler.

A thick bar indicates where the Source clip will be edited in the absence of a Timeline Out point

�If you set a Timeline Out point but no Timeline In point: The incoming source clip will be

backtimed so the Out point of the source clip is aligned with the Timeline Out point. This can be

seen by the thick bar that extends to the left of the Out point in the Timeline Ruler.

A thick bar indicates a backtimed edit in the absence of a Timeline In point

�If you set Timeline In and Out points but only a Source Out point: In this case, the incoming

source clip will also be backtimed so the Out point of the source clip is aligned with the Timeline

Out point, with the Timeline edit points defining the duration of the source clip being edited.

�If you set all four Source In and Out and Timeline In and Out edit points: The Timeline edit points

dictate the duration of source clip that is edited into the Timeline, and the frame at the Source In

point is aligned with the Timeline In point, unless you perform a Fit to Fill or ripple overwrite edit,

both of which can be done as four-point edits.

TIP: If you want to use all four Source and Timeline edit points to retime a source clip to fit

into a specific range of the Timeline, use a Fit to Fill edit instead of an overwrite edit.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Editing Rules for Split In and Out Points

If you’ve created split In and Out points in the Source Viewer or Timeline, the following rules apply:

�If the Source Viewer has split In and Out Points: The leftmost split point of the incoming clip,

whether video or audio, will be aligned with the playhead when the clip is edited; the other split

point will be offset to the right.

�If the Timeline has split In and Out Points: The In point of the incoming clip will be aligned with

the leftmost split point, whether video or audio; the accompanying audio or video In point will be

offset to the split point to the right.

Editing a Specific Range of the Source Clip Into the Timeline

This section provides some common examples of three-point editing when performing edits in the

middle of a previously edited timeline. In the following example, you have a specific range of source

media that you need to edit into the Timeline, and you don’t particularly care what gets overwritten in

the Timeline by the incoming clip.


Set In and Out points in a source clip, either in the Media Pool or in the Source Viewer.

Setting source clip In and Out points


To set where you want the incoming clip to go, set the destination control to the tracks you want to

edit onto, and then do one of the following:

�Move the Timeline playhead to the frame you want to use as the Timeline In point for the edit.

�Set a Timeline In point for the edit.

Using the playhead to act as a Timeline In point


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT


To make the edit, click the Overwrite Clip button in the toolbar, press the F10 key, or drag a clip

onto the appropriate overlay in the Timeline Viewer.

The resulting edit; the duration of the source clip defines the duration of the edit

Editing Part of a Source Clip to Fit Into

a Specific Range of the Timeline

In this example, you have a section of a clip or a gap in the edited sequence of clips in the Timeline

that you want to fill with as much of the current source clip as it will take to “plug the hole.”


Set an In point in the source clip, if necessary, to define the first frame of the range of source

media that you want to edit into the Timeline.

Setting a source clip In point only


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT


Set In and Out points in the Timeline to set both where you want the incoming clip to go, and how

much of the incoming clip you want to use.

Setting both In and Out points of the Timeline for a gap


To make the edit, click the Overwrite Clip button in the toolbar, press the F10 key, or drag a clip

onto the appropriate overlay in the Timeline Viewer.

The resulting edit; the duration of the Timeline edit points define how much of the source clip is edited

Backtiming a Source Clip When Editing Into the Timeline

In this last example, you’ve got a specific moment in the second half of a source clip that you need to

align with an Out point in the Timeline, such that the remaining duration of the incoming clip overwrites

the edited sequence of clips from the right to the left. This is referred to as backtiming, when you’re

lining up a Source Out point with a Timeline Out point in order to make an edit, and can be set up one

of two ways.

Backtiming method one:


Set In and Out points in the source clip, either in the Media Pool or in the Source Viewer.


Set an Out point in the Timeline, at the frame where you want the corresponding Out point of the

incoming source clip to be aligned.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Setting up a backtimed match-on-action edit via In and Out points in the

Source Viewer, and only an Out point in the Timeline


To make the edit, click the Overwrite Clip button in the toolbar, press the F10 key, or drag a clip

onto the overwrite overlay in the Timeline Viewer.

The resulting edit, aligning the Out point of the source clip with the Out point of the Timeline

Backtiming method two:


Set an Out point in the source clip, either in the Media Pool or in the Source Viewer.


Set In and Out points in the Timeline to set both where you want the incoming clip to go, and how

much of the incoming clip you want to use.

Setting up a backtimed edit by setting an Out point in the Source Viewer, and In

and Out points in the Timeline to define the duration of the edit


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT


To make the edit, click the Overwrite Clip button in the toolbar, press the F10 key, or drag a clip

onto the appropriate overlay in the Timeline Viewer.

The resulting edit, aligning the Out point of the source clip with the Out point of the Timeline