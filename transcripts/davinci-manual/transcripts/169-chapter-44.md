---
title: "Chapter 44"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 169
---

# Chapter 44

Trimming

Most editors would agree that trimming is half the job of editing.

While you can make many kinds of changes in the Timeline using the selection and razor blade

tools, there is a dedicated Trim mode in which you can perform more sophisticated trim operations

in fewer steps using either the mouse or keyboard shortcuts, depending on how you like to work.

Mastering DaVinci Resolve’s trimming operations will save you time when doing the necessary work of

fine‑tuning your edit.

Contents

Summarizing Trim Operations�������������������������������������������������������������������������������������������������������������������������������������������������������� 916

Selection-Based Trimming Using the Trim Tool�������������������������������������������������������������������������������������������������������������������� 916

How the Trim Tool Differs From the Selection Tool�������������������������������������������������������������������������������������������������������������� 917

Using the Trim Tool With the Mouse������������������������������������������������������������������������������������������������������������������������������������������� 918

Turning Off the Heads Up Display While You Trim��������������������������������������������������������������������������������������������������������������� 922

The Precision Trim Editor����������������������������������������������������������������������������������������������������������������������������������������������������������������� 922

Trimming Edits in the Timeline Viewer��������������������������������������������������������������������������������������������������������������������������������������� 922

Trim Tool Operations With the Keyboard��������������������������������������������������������������������������������������������������������������������������������� 923

Important Trimming Keyboard Shortcuts���������������������������������������������������������������������������������������������������������������������������������� 924

Trimming Using Timecode Entry�������������������������������������������������������������������������������������������������������������������������������������������������� 926

How to Enter Timecode Values����������������������������������������������������������������������������������������������������������������������������������������������������� 926

Commands to Make Selections and Trim�������������������������������������������������������������������������������������������������������������������������������� 927

Trimming Clips in the Source Viewer����������������������������������������������������������������������������������������������������������������������������������������� 928

Ripple Editing Rules���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 929

Using Auto Select Controls to Control Trimming����������������������������������������������������������������������������������������������������������������� 931

Using Auto Select to Control Which Clips Are Trimmed����������������������������������������������������������������������������������������������������� 931

Using Manual Selections to Control Which Clips Are Trimmed������������������������������������������������������������������������������������� 933

Using Auto Select to Control Which Tracks Are Rippled�������������������������������������������������������������������������������������������������� 933

Trimming Multiple Edits or Clips at Once�������������������������������������������������������������������������������������������������������������������������������� 935

Resizing and Rolling Multiple Edit Points���������������������������������������������������������������������������������������������������������������������������������� 936

Rippling Multiple Edit Points������������������������������������������������������������������������������������������������������������������������������������������������������������ 936

Asymmetric Trimming������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 938

Slipping Multiple Clips������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 940

Sliding Multiple Clips��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 940


Edit | Chapter 44 Trimming

EDIT

Summarizing Trim Operations

Before going into the different methods of trimming that are available, users who are new to editing

might benefit from a quick summary of what each trimming operation actually does. Each trim

operation is designed to let you move edits and clips in relation to whichever clips are around them,

by performing several operations at once. The five primary methods of trimming are:

�Resize: Shortens or lengthens the end of an outgoing clip or the beginning of an incoming

clip, while either overwriting a neighboring clip or leaving a gap behind as necessary.

While this isn’t usually included iç a discussion of “trim” operations, it’s actually the simplest

kind of trimming you can do.

�Roll: Moves an edit point to the left or right by either shortening the outgoing clip while

lengthening the incoming clip, or vice versa. Roll edits do not change the duration of the

overall Timeline.

�Ripple: Shortens or lengthens the end of an outgoing clip or the beginning of an incoming

clip, while simultaneously moving all clips either to the right in the Timeline (if you’re rippling to

lengthen a clip) or left in the Timeline (if you’re rippling to shorten a clip) to fill the gap or prevent

overwriting that would otherwise occur if you were doing a resize operation. Ripple edits do

change the duration of the overall Timeline and can alter the sync relation between different

tracks if you’re not careful.

�Slip: Keeps a clip in the same place in the Timeline, while changing the range of media that

appears in that spot. Slip edits do not change the duration of the overall Timeline.

�Slide: Keeps a clip’s range of media the same, but moves that clip to the left or right by either

shortening the outgoing clip to its left while lengthening the incoming clip to its right, or vice versa.

Selection-Based Trimming

Using the Trim Tool

Trim mode differs from Selection mode in that operations that would move clips with the Selection

tool will either slip or slide clips with the Trim tool. Other operations that would resize edits with the

Selection tool instead ripple the Timeline to automatically close gaps when using the Trim tool. The

following sections describe the various trim operations that are available, both when using the mouse,

and when using the keyboard.

To enter Trim Edit mode:

�Click the Trim Edit button, or press the T key.

Keyboard Trimming During Looped Playback������������������������������������������������������������������������������������������������������������������������ 941

Dynamic JKL Trimming����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 941

Quick Trimming�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 942

Dynamic Trimming (or “JKL Trimming”)���������������������������������������������������������������������������������������������������������������������������������������� 943

Trim Operations that are Targeted Using the Playhead�������������������������������������������������������������������������������������������������� 944

Trim Start and Trim End���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 944

Resize, Ripple, and Roll Start and End Commands�������������������������������������������������������������������������������������������������������������� 946

Slip and Slide Playhead to In and Out Commands��������������������������������������������������������������������������������������������������������������� 946

Extend Edits��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 946


Edit | Chapter 44 Trimming

EDIT

How the Trim Tool Differs From the Selection Tool

Aside from the actual trimming operations that are available, there are a few other important

differences between the Trim tool and the Selection tool.

Selecting Edit Points

When the Trim tool is selected, dragging a bounding box over a series of clips in the Timeline selects

the edit points to join clips together, instead of the clips themselves. This makes it fast and easy to

select multiple edit points that you want to operate on simultaneously.

Selecting edit points in the Timeline using the Trim tool

Rippling the Timeline With Different Operations

When the Trim tool is selected, other commands and controls that would ordinarily resize a clip or clips

and leave gaps in the Timeline instead move (ripple) clips that are to the right of the clip or edit you’re

trimming over to the left to prevent gaps whenever clips or edits are moved or resized.

Rippling the incoming edit point of Clip L to resize it and prevent a gap from appearing

by moving all clips that are to the right (Clips P, L, and N) over to the left

For example, the Retime controls, the Extend and Trim Start/End commands, and the Nudge keyboard

shortcuts all work differently depending on whether you’re using the Selection or Trim tools. This lets

you use one set of tools to do different operations, depending on what you need to do.

Rippling Gap

You can also use the Trim tool (or other trim operations described later in this chapter) to ripple the

start and end of a gap in the Timeline. Rippling a gap lets you grow or shrink the gap while moving

the portion of the Timeline to the right of the gap forward or backward in time. Whenever you ripple

against gap, a 2-up display appears that lets you see both the clip you’re trimming and whatever

superimposed clips may be showing through that gap.


Edit | Chapter 44 Trimming

EDIT

Using the Trim tool to ripple the Out point of a gap to narrow it

TIP: You can temporarily toggle between the selection (A) and trim tools (T) while using these

operators to see their effects. Releasing the key will return you to the originally selected mode.

Using the Trim Tool With the Mouse

When trimming using the mouse, you can perform every kind of trim operation that’s available using a

single tool, simply by clicking the Trim mode/tool button, and then dragging on the appropriate area of

a clip in the Timeline.

Methods of trimming with the mouse in Trim Edit mode:

�To slip a clip: To slip a clip’s range of content without changing its position in the Timeline, click

the middle top region of a clip, and then drag to the left or right to “slip” the clip to contain a

different range of frames. A dashed overlay shows the total duration of media available for you to

slip with, which moves left and right as you drag.

Clicking the top clip area before a slip, an overlay shows the clip’s available range of media

After dragging to slip, clips don’t move, but the slipped clip’s range of media has changed

When slipping clips, a 4-up display shows all relevant outgoing and incoming frames, so you can

compare the continuity of action from one clip to the next. During a slip, the top two frames update

to show you the new incoming and outgoing frames of the clip being slipped, relative to the

unchanging outgoing frame of the clip to the left and incoming frame of the clip to the right.


Edit | Chapter 44 Trimming

EDIT

TIP: You can temporarily disable this four-up display by pressing the Shift key while you slip

so that you only see the frame at the position of the playhead. This makes it possible for you

to see which frame passes the playhead by as you ripple the Timeline. You can toggle this

two-up display off completely by selecting View > Enable Multiview Edit Preview.

Four-up display when slipping a clip

�To slide a clip: To slide a clip, moving it to another position in the Timeline while simultaneously

adjusting the Out point of the previous clip and the In point of the next clip to accommodate the

change in position of the current clip being dragged, click the bottom-middle name bar of the clip

and drag it to another position.

After dragging to slide, the selected clip is at a new location, surrounding clips filled the gap

When sliding clips, a 4-up display shows all relevant outgoing and incoming frames, so you can

compare the continuity of action from one clip to the next. During a slide, the bottom two frames

update to show you the new outgoing frame of the clip to the left, and the new incoming frame of

the clip to the right of the clip being slid.


Edit | Chapter 44 Trimming

EDIT

TIP: You can temporarily disable this four-up display by pressing the Shift key while you slide

so that you only see the frame at the position of the playhead. This makes it possible for you

to see which frame passes the playhead by as you ripple the Timeline. You can toggle this

two-up display off completely by choosing View > Enable Multiview Edit Preview.

4-up display when sliding a clip

�To roll an edit point: To roll an edit, moving the Out point of the outgoing clip and the In point of

the incoming clip at the same time, drag an edit point between two clips to the left or right. (Roll

edits can also be done in Selection mode.)

Selected edit point before roll

Edit point moved farther to the right, both adjacent clips resized to prevent gap


Edit | Chapter 44 Trimming

EDIT

When rolling an edit, a 2-up display shows the changing continuity of action from the outgoing

frame of the clip to the left to the incoming frame of the clip to the right, and you will hear the audio

scrubbing of the right clip.

Two-up display when rolling an edit

�Ripple edit: To ripple the outgoing or incoming part of an edit to add or remove media to a clip

while simultaneously moving all other clips at the left in the Timeline to make room, click the

Trim tool, and drag an edit point to a new position in the Timeline.

Selected outgoing half of an edit point before ripple

Rippled clip is shorter, the rest of the Timeline has moved left to fill the gap

When rippling an edit, a 2-up display shows the continuity of action from the outgoing frame of

the clip to the left to the incoming frame of the clip to the right. Which frame updates depends on

which side of the edit you’re rippling.


Edit | Chapter 44 Trimming

EDIT

TIP: You can temporarily disable this two-up display by pressing the Shift key while you

ripple so that you only see the frame at the position of the playhead. This makes it possible

for you to see which frame passes the playhead by as you ripple the Timeline. You can toggle

this two-up display off completely by selecting View > Enable Multiview Edit Preview.

Two-up display when rippling an edit

Turning Off the Heads Up Display While You Trim

If you press the Shift key while performing most drag and trim operations, you can suspend the

multi-frame heads up displays that appear in the Timeline window in order to focus on the frame that

intersects the playhead.

To toggle the two- and four-frame heads up displays off or on:

�Choose View > Enable Multiview Edit Preview.