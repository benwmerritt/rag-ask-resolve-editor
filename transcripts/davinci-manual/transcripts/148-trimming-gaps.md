---
title: "Trimming Gaps"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 148
---

# Trimming Gaps

The start and end of gaps can also be rippled using the Trim tool.

For more information, see Chapter 44, “Trimming.”

Using the Trim tool to ripple the Out point of a gap to narrow it

Modifying Clip Duration Via Timecode

You can change a clip’s duration numerically in one of two ways.

To change a selected clip’s duration:


Decide if you want to ripple the Timeline or overwrite neighboring clips when you change a

clip’s duration. If you want to ripple the Timeline, choose the Trim tool. If you want to overwrite

neighboring clips or leave a gap, choose the Selection tool.


Do one of the following:

�Select a clip and choose Clip > Change Clip Duration.

�Right-click any clip in the Timeline and choose Change Clip Duration from the contextual menu.


When the Edit Duration Change dialog appears, enter a new duration in the Timecode field, and

click Change.

For more information on timecode entry, refer to “Moving the Playhead Using Timecode”

see Chapter 35, “Preparing Clips for Editing and Viewer Playback.”

A window for changing the duration

of a clip in the Timeline


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

Resizing or Trimming Clips

in the Source Viewer

You can also open a clip from the Timeline into the Source Viewer to perform trimming in different

ways. You can do this in one of two ways:

�Double-click a clip in the Timeline to open it into the Source Viewer.

�Move the playhead over a clip in the Timeline, press Shift-V to select that clip, and then press the

Return or Enter key to open it into the Source Viewer.

Once you open a clip into the Source Viewer, the Source Viewer has focus, enabling you to use the

Spacebar or JKL commands to move the playhead around in the Viewer in order to make edits. How

these edits affect the Timeline depends on whether you use the Selection tool or the Trim tool.

TIP: To instead open a match frame of a clip in the Timeline using the pointer, hold the

Option key down while double-clicking a clip.

Using the Selection Tool

When the Selection tool is selected, you can drag the In and Out markers, or use the playhead and I

and O keyboard shortcuts to resize that clip in the Timeline.

(Left) A Timeline clip opened in the Source Viewer, (Right) resizing the clip and

leaving a gap by dragging its In point in the Source Viewer

Using the Trim Tool

When the Trim tool is selected, dragging the In and Out points, or setting new ones using the I and

O keys resizes the clip while rippling the Timeline left or right as necessary.

Doing a Slip Edit in the Viewer

If you hold the Shift key down while dragging the In or Out point of a timeline clip you’ve opened in the

Source Viewer, you’ll move both the In and Out points together, doing a slip edit of that clip’s content

in the Timeline. This works using either the Selection or Edit tools.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

Shuffle/Swap Insert Edits

A Shuffle Insert edit (sometimes referred to as a Swap Insert edit) lets you quickly rearrange one or

more selected clips in the Timeline simply by Command-Shift dragging them to the left or right. When

you do so, the surrounding clips automatically move to the right or left to switch places with the clip

or clips that you’re dragging. This is a really fast way to reorder clips to try out different arrangements,

without needing to drag clips onto multiple tracks to get them out of the way, first.

You have a lot of flexibility in how you shuffle clips around. You can select one clip, or multiple

consecutive clips to shuffle. If you select multiple consecutive clips, they’ll move together as a single

block. You can even select multiple consecutive clips on multiple tracks to shuffle around the Timeline

as a single item.

Furthermore, you can also select clips that are part of split edits, where the audio and video In and Out

points start or end at different frames. In this case, how other clips move in the Timeline to make room

for the split edit clip you’re dragging depends on whether you click the video or audio portion of the

clip to start dragging:

�If you click-and-drag the video portion of the clip, then all clips will rearrange themselves based

on the duration of that video item on that track, so that all video items on that track rearrange

themselves without either overwriting one another or leaving gaps. As you drag to shuffle the

selection through the Timeline, overlapping linked audio items will either overwrite the audio on

neighboring clips, or leave a gap.

�If you click-and-drag the audio portion of the clip, then all clips will rearrange themselves based

on the duration of that audio item on that track, so that all audio items on that track rearrange

themselves without either overwriting one another or leaving gaps. As you drag to shuffle the

selection through the Timeline, overlapping linked video items will either overwrite the video on

neighboring clips, or leave a gap.

Given the rules previously described, shuffling clips is really easy, and you can do so in one

of two ways.

To shuffle insert clips with adjacent clips in the Timeline:


Turn snapping on.


Select one or more consecutive clips you want to shuffle.


Press and hold the Command and Shift keys down and drag either the video or audio portion of

the selected clips to the left or right.

So long as you move clips to the In or Out points of adjacent clips, they’ll automatically switch

places with the selection of clips you’re dragging. Snapping will help make sure that you align

clip(s) you’re dragging with previously existing edit points until dropped in the desired location.

Before and after clip L being shuffled with clips I, K, and J in a scene to rearrange the sequence


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

To shuffle insert one clip into adjacent clips in the Timeline:


Turn snapping off.


Select one or more consecutive clips in the Timeline that you want to shuffle.


Press and hold the Command and Shift keys down and drag either the video or audio portion of

the selected clips to the left or right.


The selection of clips you’re dragging will be more easily inserted in the middle of adjacent clips

as you drag with snapping turned off, and the cut portion of each clip will be moved into the

gap that’s left behind by the clip(s) you’re dragging. Drop the clip into the desired location when

you’re finished.

Before and after clip L being inserted into the middle of Clip K, which is split in half to make way for it

To shuffle insert multiple clips to another position in the Timeline:


Select all of the clips you want to move to another position on the Timeline.


Press and hold the Command and Shift keys, and drag the clips left or right. Make sure the item

you click to drag is on the same track as the majority of clips you’re rearranging; the item you click

defines which track is used to guide the rearrangement of clips.

In the following example, the video item of Clip C is selected on track V1, so as it’s dragged to

the right, all clips on other tracks are rearranged according to the duration and location of clips B

and C on track V1. As a result, clips on tracks other than V1 may be overwritten, or leave gaps, as

necessary for the items on track V1 to be rearranged cleanly.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

Before and after a group of clips being shuffled to the right. The clip that was

clicked to drag defines how all other clips will be rearranged

To shuffle insert multiple clips from the Media Pool or Source Viewer into the Timeline:


Either select one or more clips in the Media Pool or open a clip in the Source Viewer.


Press and hold the Command and Shift keys, and drag the selection from the Media Pool or

Source Viewer into the Timeline.


As you drag, the clips you’re dragging will be inserted into the Timeline at the pointer location.

Release the mouse to finish making the edit.

Splitting and Joining Clips

In many situations you may find yourself splitting clips (adding edits) in order to separate multiple clips

that were inadvertently baked together, or to cut up clips into sections that you’re planning on applying

different effects to or grading differently.

Methods of splitting and joining clips:

�To split a clip once: Drag the playhead to the frame where you want to split a clip, and press

Command-Backslash (\) to split every clip on a track with Auto Select enabled.

�To split many clips: Click the Razor Edit mode button (or press B), and then click clips in the

Timeline to split as many clips as you want.

TIP: Using the Blade Edit Mode or Split Clip command on a clip that’s currently selected

preserves the selection on the first half of the clip after cutting.

Through Edits

When you split a clip, a through edit appears to show that you currently have an edit with continuous

timecode running from the outgoing to the incoming half. This is called a through edit, and is displayed

with a dotted line running along its edge so you know that it’s special.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

A through edit seen in the Timeline

To eliminate a through edit, do one of the following:

�Select it in the Timeline, and press Delete.

�Right-click a through edit in the Timeline, and choose Delete Through Edit.

TIP: You can show an isolated list of every through edit in the Timeline by opening the

Edit Index and choosing “Show Through Edits” in the Edit Index Option menu. Clicking any

item in the list jumps the playhead to that through edit, making it easy to check all the through

edits in a timeline to see if they’re necessary or not.