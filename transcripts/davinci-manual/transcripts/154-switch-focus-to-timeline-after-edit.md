---
title: "Switch Focus to Timeline After Edit"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 154
---

# Switch Focus to Timeline After Edit

A setting in the Edit menu, “Switch focus to timeline after edit” (Option-Shift-Q), lets you set whether

or not DaVinci Resolve changes the application focus from the Source Viewer to the Timeline Viewer/

Timeline every time you make an edit. This setting is on by default.

For example, if you’re assembling clips from many different source files into the Timeline, and trimming

the results as you go, leaving this option on may save you time. In this case, after every edit, the

focus switches from the Source Viewer to the Timeline, so you can quickly select the clip or edit point

you want to trim and make your adjustments before loading the next clip into the Source Viewer in

preparation for the next edit.

On the other hand, if you’re editing several pieces from a long interview clip into the Timeline, you may

want to turn this setting off to make it easy to continue playing forward in the Source Viewer, setting

In and Out points and editing clips into the Timeline as you go. After every edit, focus remains on the

Source Viewer, so you can continue making edits from the same source clip without interruption.

Different Types of

Three‑ and Four‑Point Edits

This section covers the different types of edits that are available for cutting source clips into the

currently open Timeline.

Overwrite Edits

The most common type of edit you’ll make, an overwrite edit eliminates whatever media was in the

Timeline previously with the incoming source clip taking the place of whatever was there. Overwrite

edits are commonly used when initially assembling clips, or doing three-point editing.

Overwrite edits do not ripple the Timeline.

To overwrite one or more clips in the Timeline:


Move the playhead to the frame of the Timeline where you want to insert a clip.


Click the appropriate audio and video destination controls of the tracks you want to edit the

incoming source clip onto. If necessary, create new tracks.


Select a single clip in the Media Pool to open it into the Source Viewer, then set In and Out points

to define the range of media you want to insert.


To make the edit, choose Edit > Overwrite, click the Overwrite Clip button in the toolbar, press the

F10 key, or drag a clip onto the Overwrite overlay in the Timeline Viewer.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Before and after an overwrite edit, the Timeline duration stays the same

The selected clips in the Media Pool are overwrite edited to the selected track starting at the position

of the playhead, eliminating whatever was there originally while adding incoming clip. No other clips

are rippled during this operation.

Insert Edits

An insert edit splits whatever media is already in the Timeline at the position of the playhead, and

pushes that media to the right to make room for the incoming clip.

Insert edits have the effect of rippling almost all clips in the Timeline that are to the right of the insert

edit point you’re making, pushing them farther to the right by the duration of the incoming source

clip. However, clips in any tracks of the Timeline that overlap to the left of the insert edit point aren’t

rippled, and remain in place.

For example, if you’re insert editing a clip into the middle of a sequence of clips in track V1 and A1 of

the Timeline, and there’s also a clip of music edited into track A2 that overlaps well to the left of the

insert edit point, the music clip remains where it is, but the other clips on track V1 and A1 that are to the

right of your edit point on are pushed to the right.

To insert edit one or more clips into the Timeline:


Move the playhead to the frame of the Timeline where you want to insert a clip.


Click the appropriate audio and video destination controls of the tracks you want to edit the

incoming source clip onto. If necessary, create new tracks.


If necessary, set In and Out points in the clip or clips you want to insert edit into the Timeline using

the controls of the Media Pool or the Source Viewer.


Do one of the following:

�Select one or more clips in the Media Pool, right-click one of the selected clips, and choose

“Insert Selected Clips to Timeline.”

�Choose Edit > Insert, click the Insert Edit button in the toolbar, press the F9 key, or drag any clip

onto the Insert overlay in the Timeline Viewer.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

The selected clips are insert edited to the selected track at the position of the playhead, pushing

all other media in the destination track back by the total duration of the selected clips, except for

clips on other tracks that overlap to the left of the edit point (as seen by the overlapping music clip

in the example below).

Before and after an insert edit, the Timeline gets longer as non-overlapping

clips to the left of the edit point are rippled to the right

Replace Edits

Replace edits are a unique three-point edit type that aligns the frame at the Source Viewer playhead

with the frame at the Timeline playhead when the edit is executed. This is the fastest edit type to use

when you need to align an action at a specific frame of video, or a sound at a specific frame of audio,

to a particular frame’s action or sound in the video or audio of the Timeline.

The fastest way of using the replace edit is to not bother setting either In or Out points in the Source

Viewer, and to either use the duration of an existing clip intersecting the Timeline to define the edit, or

a pair of timeline In/Out points specifying either a section of a clip you want to overwrite, or an empty

section of the Timeline to which you want to edit.

Replace edits do not ripple the Timeline.

Replace Edits to Replace Existing Clips in the Timeline

A replace edit automatically replaces an existing clip in the Timeline with a clip in the Source Viewer,

so long as that clip overlaps the playhead and is on a track with its destination control enabled. When

you make a replace edit in this way, DaVinci Resolve automatically uses the duration of the Timeline

clip to define the duration of the incoming media, and the positions of the Viewer and Timeline

playheads to line up how the incoming media should be placed. This is an extremely fast edit to make,

since you needn’t use any In or Out points at all.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

To replace a clip in the Timeline:


Move the playhead in the Timeline to the clip that you want to replace, and align it with a frame

that you want to line up with a frame in the clip you’ll be replace editing into the Timeline.


Click the appropriate audio and video destination controls of the track containing the

clip you want to replace.


Open a clip into the Source Viewer.


Move the playhead in the Source Viewer to the frame that you want to line up with the frame at the

position of the playhead in the Timeline.

In the Source Viewer to the left is a VFX clip we want to edit into the Timeline to

replace the existing Timeline clip, shown in the Timeline Viewer at right

In the example shown above, the original clip that was shot on location of a car driving past a slab

of real concrete (shown in the Timeline Viewer at right) is going to be replaced by a VFX shot of

a concrete wall with a small hole for the car to drive through (shown in the Source Viewer at left).

The playhead in the Source Viewer is aligned on the very same frame as the playhead in the

Timeline Viewer, which can be seen by the identical position of the white stripe on the road in the

lower right-hand corner of the picture.


Now that the playheads are aligned on the frames that must match one another in both the Source

and Timeline Viewers, choose Edit > Replace, click the Replace Clip button in the toolbar, press

F11, or drag any clip onto the Replace overlay in the Timeline Viewer.

The resulting replace edit, in which the original timeline clip is replaced by the

incoming Source Viewer clip by aligning the frames at each playhead

The camera original clip in the Timeline is now replaced with the VFX source clip from the

Media Pool, with the source frame at the Source Viewer playhead aligned with the frame at the

Timeline playhead.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Replace Edits to Edit Clips Into Empty Tracks

You can also use a replace edit to edit a clip into an empty track of the Timeline so that the frame at

the position of the Source playhead is aligned with the Timeline playhead, and the In and Out points

of the incoming clip fall where they may. This is useful when you want to “spot” a particular action of an

alternate take or a cue in a sound effect to a specific frame of the Timeline.

To use replace edit to spot a sound effect or action video clip into the Timeline:


Move the playhead in the Timeline to the clip that contains the moment you want to align the new

incoming audio or video clip with, and position it on the exact frame that you want to line up with a

frame of the clip you’re going to edit into the Timeline.


Click the appropriate audio and video destination controls of the empty track you want to edit the

incoming clip into.


Open a clip into the Source Viewer.


Move the playhead in the Source Viewer to the frame that you want to line up with the frame

at the position of the playhead in the Timeline. This may be the sample of a sound effect that

corresponds to the action in a particular frame of your program’s video, or a frame of video that

corresponds to a particular sound in your program’s audio.


In the example shown below, the beginning of an audio cue of a billiard ball being hit is being lined

up with the frame in which the cue ball is first hit in the video.


If necessary, set In and Out points in the Timeline to restrict how much of the incoming clip will be

edited. Otherwise, the entire source clip will be edited into the Timeline.

In the Source Viewer to the left is an SFX clip we want to edit into the Timeline to match

the visuals of a cue ball being hit, shown in the Timeline Viewer at right


Now that the playheads are aligned on the frames that must match one another in both the Source

and Timeline Viewers, choose Edit > Replace, click the Replace Clip button in the toolbar, press

F11, or drag any clip onto the Replace overlay in the Timeline Viewer.

The resulting replace edit, in which the incoming

Source Viewer clip is aligned perfectly with the video


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

The SFX source clip has now been edited into the specified audio track, with the source frame at the

Source Viewer playhead perfectly aligned with the frame at the Timeline playhead so that the cue ball

hit is in sync with the visuals.

Replace Edit Using Clips Already in the Timeline

To facilitate workflows where multiple clips are stacked in the Timeline to manually track different

takes or versions of stock footage, VFX clips, or other versionable media, there’s a method of drag

and drop replace editing that copies the grade of the clip being replaced to the clip you’re replacing

it with at the same time, so that newer versions of effects can inherit the same grade as the previous

version of the effect being replaced. This only works for clips that have already been edited into the

Timeline and that are superimposed (over or under) other clips in the Timeline, such as in the following

screenshot. Be aware that this technique can also be used for multiple selected clips on the Timeline

to do several replace edits all at once.

(Left) Before replace editing

a clip in the Timeline,

(Right) After Command-

dragging a clip over one

under it in the Timeline to

replace edit the one below

with the one above

To replace edit one clip that’s stacked on the Timeline into another:


Select one or more clips that are already on the Timeline. Typically these will be clips that are

superimposed over other clips.


Hold the command key down while dragging one superimposed clip on top of another to

overwrite a clip and copy its grade to the clip you’re overwriting it with.

NOTE: This won’t work with clips you’re editing into the Timeline from the Media Pool or

Source Viewer.