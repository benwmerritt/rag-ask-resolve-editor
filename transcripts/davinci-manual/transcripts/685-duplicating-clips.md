---
title: "Duplicating Clips"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 685
---

# Duplicating Clips

The Duplicate Selection command duplicates one or more selected clips, placing the duplicates

immediately after the Out point of the selection. If you’re duplicating a region of a clip with tails, or a

clip that’s in between other clips, the duplicated selection will overwrite whatever is to the right of the

current selection, for the duration of the duplicate.

Using the Duplicate Selection command to duplicate a selected region

If you hold the Option key down while dragging a clip in the Timeline, you’ll place a duplicate clip

wherever you drop it.

Option-dragging to duplicate a clip in the Timeline


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Disabling and Re-Enabling

Clips in the Timeline

Sometimes there’s one or more audio clips in the Timeline that you don’t want to play along with

the rest of the edited sequence, but you don’t want to remove from the Timeline either, in case you

change your mind later. For this reason, it’s possible to disable clips, effectively turning them off

without removing them. Previous versions of Fairlight referred to this operation as Mute clip.

Disabled clips appear dimmed in the Timeline. They don’t play back, they’re not rendered, and they’re

not output to video. However, their position is preserved in the Timeline, so you can always re-enable

them at a later time if you change your mind and decide you want to use them.

Disabled clips appear in the Timeline in gray.

To disable or re-enable one or more selected clips:

�Right-click part of the selection and choose Enable Clip from the contextual menu.

�Choose Clip > Enable Clip.

�Press D.

Deleting Audio Clips and Regions

You can delete any clips or clip regions that are selected, in either Pointer or Range modes,

by pressing the Delete key, or by right-clicking a clip and choosing Delete Selected from the

contextual menu. By default in the Fairlight page, deleting anything leaves a gap. Under the Edit Menu

> Ripple Delete you can ripple delete selected clips changing the placement of all of the clips

that follow.

Cut, Copy, and Paste

The Fairlight page has a unique copy and paste methodology that takes advantage of the “ghost”

overlays that are used for the waveforms of selected audio clips. This method makes it easy to copy

and paste clips using keyboard shortcuts and the JKL keys.

Conventional Cut, Copy, and Paste

The typical cut, copy, and paste commands expected of every software application are available in

the Fairlight page, but with a unique twist that’s particularly advantageous for users of the Fairlight

control surface, or for anyone who uses the JKL transport key shortcuts to move around the Timeline

for keyboard-driven editing.

To cut or copy and paste either all or part of a clip:


If you’re cutting or copying a whole clip, then choose either the Selection (press A) or Range

Selection (press R) mode. If you’re cutting or copying part of a clip, then make sure you’re in

Range mode (press R).


To use the playhead to make a clip selection, select the track that contains the clip you want to

copy or cut. If one or more tracks are already selected, you can use the Control-Option-Up or

Down Arrow key shortcuts to move the track selection state up or down to the tracks with the clip

you want to cut or copy.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Selecting the track with a clip you need to cut


Do one of the following:

a)	 To cut or copy a whole clip, move the playhead so that it intersects the clip you want to cut or

copy. If the playhead intersects a clip on a selected track, that clip should become selected.

You should note that even if you use the mouse to select a clip without selecting a track first,

you should still move the playhead to intersect the clip you’re copying or pasting, as this sets

up an important reference point for the operation.

b)	 To cut or copy a segment of a clip, move the playhead so that it intersects the clip you want

to cut or copy. If the playhead intersects a clip on a selected track, that clip should become

selected. Then, using JKL and the I (In) and O (Out) keys, mark a range in the Timeline

that includes the segment of the clip you want. That segment should appear highlighted

as a result.

Cutting or copying a segment of a clip using In and Out points


Making sure the playhead is over the section of the waveform that you want to use as the frame to

move the clip by, press Command-X to cut or Command-C to copy that clip (you can also right-

click a clip and choose Copy or Cut). That clip will immediately become highlighted.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Cutting or copying a clip at the position of the playhead


At this point, there are two things you can do to position the cut or copied clip to the position in

the Timeline at which you want to paste it:

a)	 Moving the playhead will now also move the clip you cut or copied, shown as a ghost clip with

waveform that’s “attached” to the playhead at the frame you chose. Whether you drag the

playhead with your mouse or use JKL to move the playhead through the Timeline, the cut or

copied clip will move along with it, so that moving the playhead repositions the cut or copied

clip on that track.

b)	 If you want to move the cut or copied clip to another track, use the Control-Option-Up or

Down Arrow key shortcuts to change the selected track; the ghost clip will move along with

change in track selection.

Positioning the cut or copied clip before you paste it

This way, you can use the playhead to align the ghost waveform with other audio clips surrounding

it in preparation for pasting it.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT


When the clip is positioned where you want it, press Command-V to paste the clip at the position

you’ve chosen (you can also right-click a track and choose Paste from the contextual menu).

The clip becomes solid, and you’re finished.

The pasted clip

Using this method of cutting and pasting makes it quick to cut or copy clips using only keyboard

commands, with the clip’s ghost overlay making it easy to precisely align the clip you’re pasting to

fit exactly where you need it to, perfectly in sync.

Using the Cut/Copy Head and Tail Commands

Four additional commands make it easy to cut or copy portions of one or more clips that intersect

the playhead, either from the In point to the current position of the playhead (the Head), or from the

current position of the playhead to the Out point (the Tail).

To cut or copy the head or tail of a clip, and paste the result:


Using these commands, there’s no need to make a partial selection, so you can use either the

Selection (press A) or Range Selection (press T) modes.


Select the track that contains the clip you want to copy or cut. If one or more tracks are already

selected, you can use the Control-Option-Up or Down Arrow key shortcuts to move the track

selection state up or down to the tracks with the clip you want to cut or copy.


Move the playhead so that it intersects the clip you want to cut or copy at the frame you want to

define, either the end of the head or the beginning of the tail. If the playhead intersects a clip on

a selected track, that clip should automatically become selected. You should note that even if you

use the mouse to select a clip without selecting a track first, you should still move the playhead

to intersect the clip you’re copying or pasting, as this sets up an important reference point for

the operation.


Choose Edit > Cut/Copy Head/Tail to cut or copy the portion of the selected clip you want to

paste. That portion of the clip will immediately become highlighted.


At this point, there are two things you can do to position the cut or copied head or tail of the clip to

the position in the Timeline at which you want to paste it:


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

a)	 Moving the playhead will now also move the clip you cut or copied, shown as a ghost clip with

waveform that’s “attached” to the playhead at the frame you chose. Whether you drag the

playhead with your mouse or use JKL to move the playhead through the Timeline, the cut or

copied clip will move along with it so that moving the playhead repositions the cut or copied

clip on that track.

b)	 If you want to move the cut or copied clip to another track, use the Control-Option-Up or

Down Arrow key shortcuts to change the selected track; the ghost clip will move along with

change in track selection.

This way, you can use the playhead to align the ghost waveform with other audio clips surrounding

it in preparation for pasting it.


When the clip is positioned where you want it, press Command-V to paste the clip at the position

you’ve chosen (you can also right-click a track and choose Paste from the contextual menu).

The clip becomes solid, and you’re finished.