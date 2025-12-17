---
title: "Commands to Make Selections and Trim"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 171
---

# Commands to Make Selections and Trim

A series of commands in the Trim menu make it fast to automatically select the In or Out point of the

clip that’s nearest to the current position of the playhead, and go into either Selection or Trim mode in

preparation for resizing or ripple trimming that edit point. These commands are:

�Select Nearest Edit to Resize In

�Select Nearest Edit to Resize Out

�Select Nearest Edit to Ripple In

�Select Nearest Edit to Ripple Out

�Select Nearest Edit to Roll

�Select Nearest Clip to Move

�Select Nearest Clip to Slip

�Select Nearest Clip to Slide

These commands are similar to using the Edit Selection (V) or Clip Selection (Shift-V) keyboard

shortcuts along with those for choosing the Selection (A) or Trim tool (T) both at once, to get you ready

for trimming in the way that you want. However, they have the added benefit of, in some cases, letting

you specifically choose the In or Out points of the clip nearest the current position of the playhead.

These commands don’t have keyboard shortcuts by default, but if you prefer this way of working,

you can assign them to keyboard shortcuts of your choosing using the Keyboard Customization tool

(Option - Command - K).


Edit | Chapter 44 Trimming

EDIT

Trimming Clips in the Source Viewer

Additionally, you can double-click a clip in the Timeline to open it into the Source Viewer for trimming.

When the Selection tool is selected, you can drag the In and Out markers, or use the playhead and I

and O keyboard shortcuts to resize that clip in the Timeline. With the Trim tool selected, you can ripple

the In and Out points of the clip.

A Timeline clip being ripple-resized by opening it

into the Source Viewer dragging its In point using the Trim tool


Edit | Chapter 44 Trimming

EDIT

You can slip the contents of the clip by holding the Shift key down and dragging either the In

or Out point.

A Timeline clip being slipped by opening it into the

Source Viewer and Shift-dragging its In point using the Trim tool

NOTE: To open a match frame of a clip that’s part of an edited sequence into the

Source Viewer using the mouse, hold the Option key down while double-clicking a clip in the

Timeline.

Ripple Editing Rules

Ripple operations are the only trim functions that change the duration of the overall Timeline, and that

can potentially alter the sync relationship between multiple clips on different tracks. This makes them

incredibly useful, but it’s important to understand which parts of the Timeline will move as part of a

ripple operation, and which parts won’t.

The following operations ripple the Timeline:

�Ripple deleting a clip or gap (Forward-Delete)

�Ripple cutting a clip (Shift-Command-X)

�Rippling one or more edits or gaps using the Trim tool (press T to choose the Trim tool)

�Using the Extend Edit (E), Trim Start (Shift-[), or Trim End (Shift-]) commands in Trim mode

�Using the Ripple Start (Command-Shift-[) or Ripple End (Command-Shift-]) commands in any mode

�Performing an insert edit (F9) or ripple overwrite edit (Shift-F10)

�Using the Retime controls to speed up or slow down a clip in Trim mode

�Using the Change Speed dialog with the Ripple Sequence checkbox turned on

�Changing clips in a Take Selector with the Ripple control enabled

During a ripple edit, superimposed clips with an In point that’s to the left of the edit point or clip

being rippled are not moved. This can be seen in the previous example via the audio clip at the

bottom of the Timeline, which stays in place even as the clips on track V1 and A1 are rippled. All clips

with In points to the right of the edit point or clip being rippled move left to follow the trim operation

you’re making.


Edit | Chapter 44 Trimming

EDIT

Before Ripple

After Ripple

Before Ripple

Before Ripple

After Ripple

After Ripple

The rules of timeline rippling illustrated. All clips with In points to the left of Subclip B

(the clip being rippled) are left in place (area in blue), while all clips to the right of the

edit being rippled are moved by the duration of the ripple operation (in red)


Edit | Chapter 44 Trimming

EDIT

This simple rule means that, if you’re in the habit of building sequences of clips from left to right, long

overlapping superimpositions such as titles, graphics, and music clips will stay in place while you’re

rippling various clips within a montage that you’re editing in relation to these longer clips.

However, there’s one exception to this rule. It is often the case that split edits, where linked audio and

video are cut at different places, create a situation where the audio In point of a pair of linked audio

and video items precedes a video In point that you want to ripple. In other words, the audio In point

extends to the left of the video In point, which ordinarily would trigger the rule that clips with edit

points to the left of a rippled edit point won’t be moved, which would throw the audio and video of this

item out of sync. In this case, you probably want to maintain sync, so all items that are linked to a clip

being rippled always ripple along with it, even if they do have In points that extend to the left of the

edit point being rippled.

Using Auto Select Controls

to Control Trimming

The Auto Select buttons on each track in the Timeline control a host of different operations, but while

they’re deceptively powerful, they’re also among the most misunderstood controls of the Timeline.

When a track’s Auto Select control is on, clips on that track are automatically included in three different

types of operations:

�Operations that affect clips intersecting the position of the playhead

�Operations that affect clips intersecting a region defined by timeline In and Out points

�Operations that ripple clips to the right of an affected clip on the Timeline

When a track’s Auto Select control is off, clips on that track are ignored by those same categories of

operations, unless you manually select one or more clips or edit points.

The next three sections go into detail on how the Auto Select buttons help you control the trimming

operations described in this chapter, particularly when it comes to operations that ripple the Timeline,

and the kinds of “playhead-targeted” trim operations described later in this chapter.

For more information on using the Auto Select controls to define selections and control other

editing operations, see Chapter 36, “Editing Basics.”

Using Auto Select to Control Which Clips Are Trimmed

One of the principal uses of the Auto Select controls is to let keyboard shortcut-driven editors choose

which specific clips on which tracks will be affected by an operation that would otherwise affect

every superimposed clip at the position of the playhead or encompassed by In and Out points set in

the timeline.

For example, if multiple clips are superimposed in V1, V2, and V3, and A1, A2, and A3, all six tracks

have their Auto Select controls turned on, and you park the playhead over one of them and use the

Trim End command in Selection mode, then all six superimposed clips will be trimmed.


Edit | Chapter 44 Trimming

EDIT

Trimming all clips at the position of the playhead

However, if you only want to trim the clip in track V3, then you can solo the Auto Select control of

V3 by Option-clicking it, and then when you use the Trim End command, the clip on V3 is the only

one that’s trimmed, the other clips are ignored.

Trimming only the clip in V3 by soloing the V3 Auto Select controls


Edit | Chapter 44 Trimming

EDIT