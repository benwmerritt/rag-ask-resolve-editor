---
title: "Making Selections"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 109
---

# Making Selections

As you continue to work in the Cut page, it becomes increasingly helpful to know how to make different

kinds of selections, both in the Media Pool and in the Timeline. Most of these methods of selection

should be familiar to you if you have experience with other media applications or file managers.

Methods of selecting clips in the Media Pool:

�To select a single clip: Click a clip in the Media Pool. Once you’ve selected a clip, you can use the

Up and Down arrow keys to move the selection to other clips.

�To select a contiguous range of clips: Drag a selection box over all the clips you want to select,

or click to select the first clip in a series, then Shift-click the last clip to select those clips and

everything in between.

�To select a noncontiguous range of clips: Command-click each clip you want to include in

the selection. Or, you can hold the Command key down while you drag bounding boxes over

unselected clips to add them to the current selection, or over selected clips to remove them from

the selection.

�To select all clips: Select one clip, then choose Edit > Select All (Command-A).


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

Methods of selecting clips in the Timeline:

�To select one clip: Click a clip with the mouse. Command-clicking that clip de-selects it.

�To de-select all clips in the Timeline: Click in any empty area of the Timeline to de-select

everything, or press Command-Shift-A.

�To select a continuous range of clips by dragging: Drag a bounding box from an empty area of

the Timeline to surround a group of clips.

�To select a continuous range of clips by Shift-clicking: Click the first clip you want to select,

and then Shift-click the last clip you want to select, and all clips in-between will automatically be

selected as well.

�To select a discontinuous range of clips: Command-click any clips to select them no matter

where they appear on the Timeline. Command-clicking a selected clip deselects it.

�To select all clips under the playhead: You can select all the clips under the playhead at once,

regardless of how many tracks they are spread across by selecting Trim > Select All Clips Under

Playhead (Option-Shift-V).

�To select all clips in the Timeline from the playhead forward: Right-click the top handle of the

playhead, and click the right button on the radial menu that appears.

�To select all clips in the Timeline from the playhead backward: Right-click the top handle of the

playhead, and click the left button on the radial menu that appears.

The radial menu that appears

when you right-click the

top handle of the playhead

Methods of selecting edits in the Timeline using the pointer:

�To select an edit to roll: Move the mouse to the center of an edit point, and when the ripple cursor

appears, click to select the edit.

�To select just the incoming or outgoing half of an edit point to resize: Move the mouse to the

left or right of the center of an edit, and when the resize/ripple cursor appears, click to select that

portion of the edit.

�To select multiple roll points: Command-click the center of multiple edit points. Command-click a

selected edit point to deselect it.

�To select multiple resize points: Command-click the left or right sides of multiple edit points.

�To de-select all clips in the Timeline: Click in any empty area of the timeline to

de-select everything.

Keyboard shortcuts for selecting edits in the Timeline:

�To select an edit point from the keyboard: Press V to select the nearest edit

point to the playhead.

�To change an edit selection from the keyboard: Once you’ve selected an edit point,

press U to toggle among selecting the outgoing half, incoming half, or the entire edit.

�To de-select all edits in the timeline: Press Command-Shift-A.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

Moving Clips in the Timeline

Once you’ve edited some clips into the Timeline, you’ll probably want to start fine-tuning the edit by

moving clips around. Different operations can be performed depending on how you move these clips.

All of these techniques work in both the Upper Timeline and the Timeline Editor.

Ripple Overwriting An Entire Clip in Track 1

Drag a clip in the Timeline or Upper Timeline over another clip in the Timeline so that the pointer

overlaps that clip, and quickly drop it onto another clip in Track 1. The clip you dragged replaces the

clip you dropped it onto, and all clips to the right are moved to either make room (if the dragged clip is

longer) or to close the gap (if the dragged clip is shorter).

Clicking clip BB to begin dragging it

Dragging clip BB onto clip DD to ripple overwrite it

Clip BB is moved and takes the place of clip DD, while the rest of the Timeline moves left to close the gaps in Track 1

NOTE: If you wait too long, this Ripple Overwrite operation will turn into an overwrite

operation. If you drag a clip in Track 1 onto a clip in any other track, you can only do an

overwrite, not a ripple overwrite.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

Ripple Trimming on Secondary Tracks

You can use the Cut page’s ripple editing on secondary tracks as well, but only when there is no

underlying video on the primary video track (Track 1). Use the Ripple On control in the Cut page

timeline header to toggle this ripple behavior on or off.

We want to delete the selected clip and close the gap, even though our clips are

on a secondary track. Note the primary track (Track 1) is empty.

Deleting a clip leaves a gap in the secondary track when Ripple On is disabled.

Deleting a clip closes the gap in the secondary track when Ripple On is enabled.

Overwriting the Middle of Other Clips

Drag a clip in the Timeline or Upper Timeline over another clip in the Timeline so that the pointer

overlaps that clip, and pause until the clip you’ve selected is overlaid on top of the second clip, and

release the mouse button. The target clip is overwritten by the duration of the clip you dragged and

split in two.

(Top) Dragging clip BB

and pausing to overwrite

part of clip DD

(Bottom) Clip BB is moved,

overwriting the middle

of clip DD which is now

in two pieces; the rest

of the Timeline moves

left to fill the gap left by

moving clip BB in Track 1

Overwriting The Edges of Other Clips

Drag a clip in the Timeline or Upper Timeline over the edge of a neighboring clip without letting your

pointer overlap it, then drop the clip. The overlapping part of the neighboring clip will be overwritten.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

(Top) Dragging clip CC to

partially overlap clip DD

in order to overwrite it

(Bottom) After dropping clip

CC to partially overwrite the

beginning of clip DD, clip DD

is shortened and the other

clips in the Timeline move

left to fill the gap in Track 1

Swapping Clips

Drag one or more clips from one part of the Timeline or Upper Timeline to another so that the pointer

overlaps an edit between two clips (the edit point turns purple), and drop the clip. The clip(s) you

dragged are now moved so that they’re inserted at the edit point you targeted.

Dragging clip CC to swap it between clip II and JJ

Dropping clip CC rearranges the Timeline, which automatically closes all gaps and move clips to the

right where necessary; superimposed clips are kept in sync with clips in Track 1 that have moved

Copy, Cut, and Paste

Clips can be cut, copied, and pasted in the timeline or Upper Timeline to duplicate them or move them

around, just like words in a word processor.

To cut/copy and paste in the Timeline:


Select one or more clips in the Timeline.


Do one of the following:

a)	 Press Command-C to copy them (the selected clips remain where they are).

b)	 Press Command-X to cut them (the selected clips are removed and the Timeline

automatically ripples itself to close the gap).

c)	 Move to another part of the Timeline, then press Command-V to paste the clips. The clips are

pasted to the frame at the playhead, to the same track they were copied from, and overwrite

whatever other clips are at that part of the Timeline.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT