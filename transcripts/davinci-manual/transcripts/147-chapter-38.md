---
title: "Chapter 38"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 147
---

# Chapter 38

Modifying Clips

in the Timeline

Once you’ve edited a variety of clips into the Timeline, you’ll start working with

them as you refine your edit. In this chapter, you’ll learn simple methods of

modifying clips, including resizing, splitting, shuffling, disabling, copying and

pasting, and duplicating.

Contents

Keyboard Shortcuts in This Chapter������������������������������������������������������������������������������������������������������������������������������������������ 796

Moving, Resizing, and Rolling Clips in Selection Mode��������������������������������������������������������������������������������������������������� 797

Trimming Gaps�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 800

Modifying Clip Duration Via Timecode������������������������������������������������������������������������������������������������������������������������������������ 800

Resizing or Trimming Clips in the Source Viewer����������������������������������������������������������������������������������������������������������������� 801

Using the Selection Tool�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 801

Using the Trim Tool������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 801

Doing a Slip Edit in the Viewer�������������������������������������������������������������������������������������������������������������������������������������������������������� 801

Shuffle/Swap Insert Edits����������������������������������������������������������������������������������������������������������������������������������������������������������������� 802

Splitting and Joining Clips��������������������������������������������������������������������������������������������������������������������������������������������������������������� 804

Through Edits������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 804

Enabling and Disabling Clips and Tracks��������������������������������������������������������������������������������������������������������������������������������� 805

Copying and Pasting Clips in the Timeline����������������������������������������������������������������������������������������������������������������������������� 807

Paste Insert���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 807

Cut/Copy/Paste of Partial Clip Segments Using In and Out Points����������������������������������������������������������������������������� 807

Copying and Pasting Clips to a Different Track��������������������������������������������������������������������������������������������������������������������� 808

Audio Channels When Copying and Pasting Audio Clips������������������������������������������������������������������������������������������������ 808

Auto Align Clips������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 809

Duplicating Clips and Transitions in the Timeline����������������������������������������������������������������������������������������������������������������� 811

Smart Reframe (Studio Version Only)�������������������������������������������������������������������������������������������������������������������������������������������� 811

Split Photoshop PSD Layers into Individual Timeline Tracks����������������������������������������������������������������������������������������� 812


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

Keyboard Shortcuts in This Chapter

Here’s a list of of keyboard shortcuts you might find helpful that relate to topics found in this chapter.

Key Shortcut

Function

A

Selection tool/mode

V

Select nearest edit to playhead

Shift-V

Select clip intersecting playhead

U

Select incoming, outgoing, or centered part of edit

Option-U

Toggle selection among video+audio, video only, and audio only

Up, Down Arrow Keys

Move selection to previous/next edit or clip

Comma, Period

“Nudge” keys to move a selected edit or clip left or right a

frame at a time

Shift-Comma, Period

“Fast Nudge” keys to move a selected edit or clip left or right

5 frames at a time (customizable)

Shift-Left, Right Bracket ([, ])

Trim Start to Playhead and Trim End to Playhead to trim a clip

at the position of the playhead

E

Extend edit to move a selected edit point to the playhead

B

Razor blade tool for adding cuts to clips using the pointer

Command-Backslash (\)

Insert edit; adds a cut to the clip(s) at the position of

the playhead

Delete

Delete clip and leave gap (lift edit)

Forward Delete

Ripple delete; deletes a clip and moves the rest of the

Timeline left to fill the gap

N

Toggle timeline snapping off and on

Command-Shift-L

Toggle linked selection off and on

Command-D

Change clip duration

Command-Shift (modifier)

While dragging, holding Command-Shift lets you “shuffle” or

“swap” edit clips forward or backward to rearrange clips in

the Timeline

D

Disable/Enable selected clips

Command-X

Cut selected clips, leave gap

Apple Cinematic Mode (Mac OS Only)���������������������������������������������������������������������������������������������������������������������������������������� 814

Using Apple Cinematic Mode in DaVinci Resolve����������������������������������������������������������������������������������������������������������������� 814

Scene Cut Detection on the Timeline ��������������������������������������������������������������������������������������������������������������������������������������� 816

Clean Up Video Tracks����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 817


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

Key Shortcut

Function

Command-Shift-X

Ripple cut selection; close gap left by cut clip(s)

Command-C

Copy selected clips

Command-V

Paste clips

Command-Shift-V

Paste insert clips

Moving, Resizing, and

Rolling Clips in Selection Mode

After editing a series of clips into a timeline, the next thing even the most careful of editors probably

needs to do is to start making changes. The simplest changes are made in Selection Mode, using the

regular arrow pointer.

The Selection Mode button at

left is enabled; the Trim mode

button at right is disabled

This is the default mode when you open DaVinci Resolve, and allows you to move clips to other places

in the Timeline, resize them to make them longer or shorter, and roll the edit points between two clips

to move the edit to an earlier or later position on the Timeline. What this tool does depends entirely on

what you click to select as you work.

Manipulating clips using the mouse:


Click the Selection Mode tool (the arrow), or press A.


Do one of the following:

To move clips in the Timeline: Drag any clip in the Timeline to any other position. If you drag a clip

to overlap another clip, the clip you’re dragging overwrites the clip you’re dropping it onto.

Moving a clip in the Timeline to overwrite part of another clip;

a tooltip shows you how many frames you’ve moved

To move clips in the Timeline up or down to other tracks while keeping them at the same time:

Hold the Shift key down while dragging clips up or down in the Timeline. Or, you can hold the

Option key down and press Up or Down Arrow.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

Moving a clip into another track without sliding it in time by holding the Shift key down

To shorten or lengthen clips: Move the Selection Mode pointer over the beginning or end of a

clip, and when it turns into the Resize cursor, drag the In or Out point to the left or right to change

the clip’s length. As you do so, the audio will scrub along with the Resize cursor.

Resizing a clip in the Timeline to create a gap; a tooltip shows the offset, and outlines

show you how much media is available in the clip being adjusted

To roll any edit: Move the Selection Mode pointer over any edit point, and when it turns into the

Roll Edit cursor, drag it to the left or right to move the edit point while simultaneously resizing the

outgoing and incoming edits points of the two clips surrounding it. As you do so, the audio will

scrub along with the right clip’s In point.

Rolling an edit; a tooltip shows the offset, and an outline shows the available area you can roll within


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

Manipulating clips using the keyboard:


Press A to choose Selection Mode.


Do one of the following:

�To roll any edit incrementally: Select the closest edit point to the playhead using the V key,

moving the selection to another edit, if necessary, by using the Up Arrow and Down Arrow keys.

Then press the Comma key (nudge 1 frame left) or Period key (nudge 1 frame right) to roll the

selected edit to the left or right. Shift-Comma and Shift-Period nudges by 5 frames.

�To roll any edit using the playhead: Select the closest edit point to the playhead using the V

key, moving the selection to another edit, if necessary, by using the Up Arrow and Down Arrow

keys. Then use the JKL keys to move the playhead to the frame you want to move the edit to,

and press E to do an “extend” edit.

�To shorten or lengthen clips incrementally: Select the closest edit point to the playhead using

the V key, then use the U key to toggle the selection among the end of the outgoing clip and

the beginning of the incoming clip. Then, press the Comma key (nudge 1 frame left) or Period

key (nudge 1 frame right) to shorten or lengthen that side of the clip. If you nudge one end of

a clip to overlap another, the clip you’re nudging overwrites the adjacent clip. Shift-Comma

and Shift-Period nudges by 5 frames. In Selection mode, this either leaves a gap or overwrites

neighboring clips.

�To shorten clips using the playhead: Use the JKL keys to move the playhead over the frame

in the Timeline where you want to set a new In or Out point for that clip, then press Shift-Left

Bracket ([) to “trim start,” or Shift-Right Bracket (]) to “trim end.” No selection is necessary. In

Selection mode, this leaves a gap.

�To lengthen clips using the playhead: Select the closest edit point to the playhead using the

V key, then use the U key to toggle the selection among the end of the outgoing clip and the

beginning of the incoming clip. Then, use the JKL keys to move the playhead to the frame to

want to extend that edit point to, and press E to do an “extend” edit. In Selection mode, this

overwrites neighboring clips.

�To move clips forward or back in the Timeline: To select a clip in preparation for moving it,

either click it, or use the Spacebar or JKL keys to move the playhead over it and press Shift-V.

Then press the Comma key (nudge 1 frame left) or Period key (nudge 1 frame right) to move

the clip to the left or right. If you nudge a clip to overlap another clip, the clip you’re nudging

overwrites the adjacent clip. Shift-Comma and Shift-Period nudges by 5 frames. In Selection

mode, this leaves a gap.

�To move clips up or down to other tracks: To select a clip in preparation for moving it,

either click it, or use the Spacebar or JKL keys to move the playhead over it and press

Shift-V. Then, press Option-Up Arrow to move the Video and Audio of that clip to the next

higher‑numbered track, or press Option-Down Arrow to move the Video and Audio to the next

lower‑numbered track.

TIP: You can hold down the Shift key while nudging a selection to do a “fast nudge.”

The duration of a fast nudge is customizable in the Editing panel of the User Preferences.

By default it’s five frames, but you can set it to whatever you want.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT