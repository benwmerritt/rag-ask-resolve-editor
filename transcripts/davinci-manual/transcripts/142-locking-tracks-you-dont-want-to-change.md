---
title: "Locking Tracks You Don’t Want to Change"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 142
---

# Locking Tracks You Don’t Want to Change

Another step you can take to prepare before performing any kind of editorial operation is to lock

tracks with media that you don’t want to be affected by whatever it is you’re about to do. For example,

if you have a complex set of music edits on track A3 that you don’t want to be affected by operations

that will ripple the Timeline, you can lock track A3 so those clips remain unaffected.

Tracks V2, V1, and A1 are unlocked, while tracks A2, A3, and A4 are locked

Clips on locked tracks cannot be moved, deleted, cut, or otherwise affected by editorial operations.

Furthermore, parameters of locked clips cannot be edited in the Inspector. However, clips on locked

tracks can be graded and otherwise modified in the Color page.

To toggle the lock or unlock state of tracks, do one of the following:

�Click any track’s lock control to toggle lock on and off.

�Shift-click any track’s lock control to toggle locking on and off for all tracks.

�Press Option-Shift-1 through 8 to lock or unlock tracks V1 through V8.

�Press Option-Shift-9 to lock or unlock all video tracks.

�Press Option-Shift-F1 through F8 to lock or unlock tracks A1 through A8.

�Press Option-Shift-F9 to lock or unlock all audio tracks.


Edit | Chapter 36 Editing Basics

EDIT

Position Lock for Finishing

In a nutshell, turning position lock on prevents clips from being moved to the left or right, and it

prevents all ripple operations. This is primarily useful when you’re near the end of post on a project for

which the cut has been locked (or at least as “locked” as directors and producers allow any more), but

you still need to make surgical changes that don’t risk throwing the video out of sync with audio that

may be being edited and mixed elsewhere because of an accidentally rippled edit.

With position lock on, you can still make edits (such as Replace), slip clips, roll edits, add Resolve FX

and other Open FX, and alter all manner of effects in the Inspector. You just can’t do anything that

alters the position of clips in the Timeline, or ripples entire sections of the Timeline.

There are two ways you can enable Position Lock.

Position Locking All Tracks

You can turn Position Lock on and off for all tracks via a button in the toolbar above the Timeline.

The Position Lock button on the toolbar

When you turn position lock on, the Lock button of all tracks changes to show that position lock is

enabled instead.

Position lock indicated by each track’s Lock icon changing

Position Locking Individual Tracks

You can also be extra tricky and enable position lock on a track-by-track basis by Command-clicking

any track’s Lock button.

Position lock can be released by simply clicking that track’s Lock icon.


Edit | Chapter 36 Editing Basics

EDIT

Command-click any track’s Lock button to

put that track into Position Lock mode

Disabling and Re-Enabling

Clips in the Timeline

Sometimes there’s one or more video or audio clips in the Timeline that you don’t want to play along

with the rest of the edited sequence, but you don’t want to remove from the Timeline either, in case

you change your mind later. For this reason, it’s possible to Disable clips, effectively turning them off

without removing them.

Disabled clips appear dimmed in the Timeline. They don’t play back, they’re not rendered, and they’re

not output to video. However, their position is preserved in the Timeline, so you can always re-enable

them at a later time if you change your mind and decide you want to use them.

A clip that’s been disabled between two enabled clips; the disabled clip is dimmed

To disable or re-enable one or more selected clips:

�Right-click part of the selection and choose Enable Clip from the contextual menu.

�Choose Clip > Enable Clip.

�Press D.


Edit | Chapter 36 Editing Basics

EDIT

Deleting Clips and Gaps From the Timeline

There are two ways you can delete clips you don’t want in the Timeline. Using the Delete key, you can

perform what’s sometimes called a “lift edit,” removing the unwanted clips and leaving a gap. Using

the Forward Delete key, you can perform a “ripple delete,” removing unwanted clips and closing the

gap by rippling the rest of the edited Timeline to the right of the deleted clip(s) by moving it to the left.

Deleting clips as a “lift edit” operation:

�To remove one or more clips from the Timeline, leaving a gap: Select a clip in the Timeline, or

Shift-click or Command-click to select the clips you want to remove, and press the Delete key (or

right-click the selection and choose Delete).

�To remove a range of media from the Timeline on multiple tracks, leaving a gap: Set Timeline

In and Out points defining the range of media you want to delete, then turn off the Auto Select

controls of any tracks with media you want to preserve, and press the Delete key (or right-click the

selection and choose Delete).

Deleting Clip I using the Backspace or Delete key and leaving a gap

Deleting clips as a “ripple delete” operation:

�To delete one or more clips and close the gap by rippling the Timeline left: Select a clip in the

Timeline, or Shift-click or Command-click to select the clips you want to remove, and press the

Forward Delete key.

�To delete a range of media and close the gap by rippling the Timeline left: Set Timeline In and

Out points defining the range of media you want to delete, then turn off the Auto Select controls of

any tracks with media you want to preserve, and press the Forward Delete key.


Edit | Chapter 36 Editing Basics

EDIT

Deleting Clip I using the Forward Delete key to ripple all clips with In

points to the right in the Timeline to close the gap

As with any ripple operation, all clips with In points to the right of the deleted range of media on

tracks with auto select enabled are rippled to close the gap, and any clips with In points to the left

of the In point of the affected range of media are unaffected.

Finding, Selecting, and Deleting Gaps in the Timeline

A gap is defined as a space between any two clips on the same track. Often gaps are desirable as

they allow audio or video clips to be spaced apart from one another very specifically, but sometimes

they’re not. If you want to find accidental gaps in your timeline that may be too small to see, a pair of

commands lets you do this.

To move the playhead to the next gap on the Timeline:


Turn off the Auto Select controls of any tracks you want to omit from this operation.


Do one of the following:

�Choose Playback > Previous Gap, or press Option-Command-Semicolon (;) to move the

playhead to the next gap to the left of the playhead’s current position.

�Choose Playback > Next Gap, or press Option-Command-Apostrophe (‘) to move the playhead

to the next gap to the right of the playhead’s current position.

To select or deselect a gap:

Click once to select a gap, and click that gap again to deselect it.

You can only select one gap at a time. The principal reason to select a gap is to delete it, in the

process rippling the Timeline to close the gap. In the following example, there’s a gap between two

clips on track V1 that you’d like to close.

Selecting a gap on track V1


Edit | Chapter 36 Editing Basics

EDIT

To delete a gap:

Press the Delete key to close the gap. All clips to the right of it on tracks with Auto Select enabled will

be rippled to the left to close the gap. Clips on tracks with Auto Select disabled will not ripple.

If you select a gap in a timeline with clips on multiple tracks, which clips will be deleted depends on

the state of the Auto Select controls for each track in the Timeline.

�All tracks with Auto Select enabled: The range of media that overlaps the selected gap will also

be deleted. Clips on those tracks will ripple left to fill the gap.

�All tracks with Auto Select disabled: The range of media that overlaps the selected gap will

be left intact, and clips on those tracks will not ripple left, going out of sync with whichever

clips do ripple.