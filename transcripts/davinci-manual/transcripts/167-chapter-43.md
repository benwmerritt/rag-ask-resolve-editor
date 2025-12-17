---
title: "Chapter 43"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 167
---

# Chapter 43

Take Selectors,

Compound Clips,

and Nested Timelines

This chapter covers a variety of different ways you can turn multiple clips into a

single object in the Timeline, to accommodate a variety of different editing tasks.

Take Selectors, compound clips, and nested timelines all appear as a single clip in the Timeline,

but they all organize multiple clips in different ways. Take Selectors let you organize multiple clips

vertically, making it easy to associate clips with one another so you can easily switch among them.

Compound clips and nested timelines let you organize multiple clips horizontally, so that you can

manage long or short sequences of clips within an edit as a single clip, when convenient.

Contents

Take Selectors��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 905

Compositing and Grading Take Selectors������������������������������������������������������������������������������������������������������������������������������� 906

Compound Clips����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 907

Individual Destination Controls with Decompose on Edit������������������������������������������������������������������������������������������������� 910

Compositing With and Grading Compound Clips������������������������������������������������������������������������������������������������������������������� 911

Nested Timelines������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 911

Re-Editing a Nested Timeline���������������������������������������������������������������������������������������������������������������������������������������������������������� 912

Swapping the Contents of the Source Viewer and Timeline������������������������������������������������������������������������������������������� 912

Editing Source Media From a Timeline or Compound Clip����������������������������������������������������������������������������������������������� 912

Marking Clips in Timelines Loaded into the Source Viewer��������������������������������������������������������������������������������������������� 912

Decomposing Nested Timelines���������������������������������������������������������������������������������������������������������������������������������������������������� 912

Compositing and Grading Nested Timelines��������������������������������������������������������������������������������������������������������������������������� 913

Audio Buses in Nested Timelines�������������������������������������������������������������������������������������������������������������������������������������������������� 914

Match Frame for Nested Timelines and Compound Clips����������������������������������������������������������������������������������������������� 914

Converting Compound Clips or Timelines to Multicam Clips���������������������������������������������������������������������������������������� 914


Edit | Chapter 43 Take Selectors, Compound Clips, and Nested Timelines

EDIT

Take Selectors

Take Selectors in DaVinci Resolve provide a way for you to manage multiple takes or versions of a

particular clip in the Timeline. They’re ideal for storing multiple useful takes for scenes where you or

the client can’t quite decide which one is the best, or for maintaining multiple versions of VFX clips that

are going through different iterations.

When you place a number of clips inside a Take Selector, only one clip appears in the Timeline, but

you can open that Take Selector and switch to any other take or version that’s stored within to switch

which clip appears in the Timeline whenever you want.

A Take Selector, shown

open, with several alternate

takes placed within

Take selectors are easy to create and use and populate. Once you’ve placed a number of clips inside

the Take Selector, you can drag any take to slip that clip’s range of media to synchronize it with the

other takes, or click a take to choose that clip within the Take Selector to appear in the Timeline,

before closing the Take Selector to confirm your change.

When closed, a Take

Selector appears as a

regular clip with a badge

When closed, multi-take clips can be edited, trimmed, composited, graded, and rendered like any

other single clip in the Timeline. A Take Selector badge appears to the left of the name of a clip to

which it’s applied to show its status; double-clicking this badge opens the Take Selector so you can

adjust its contents.


Edit | Chapter 43 Take Selectors, Compound Clips, and Nested Timelines

EDIT

Methods of using Take Selectors:

�To create a Take Selector: Right-click any clip that’s not a title or generator, and choose Take

Selector from the contextual menu. The Take Selector interface appears, disabling the rest of the

Timeline temporarily while you work with the Take Selector’s contents.

�To populate a Take Selector: Drag any clip from the Media Pool into the Take Selector, and it

appears “stacked” on top of the original clip in the Timeline.

�To choose the current take: Click any clip within the Take Selector so that it’s highlighted, and

then click the close button at the upper-left corner of the Take Selector. When next you open the

Take Selector, the current clip appears at the bottom of the stack, with a star at the upper-left

corner. Absent a choice, the current take will default to the last clip added to the Take Selector.

�To set a Take Selector to ripple the Timeline when a longer or shorter take is selected:

Click the Ripple Take button, at the upper right-hand corner of the Take Selector panel, to the

left of the trash can button. With this turned on, selecting a take that’s longer or shorter than the

current take will ripple the Timeline. With this turned off, selecting a take that’s longer or shorter

will either overwrite the next clip to the right, or leave a gap.

�To slip a clip within the Take Selector: Drag any clip to the left or right to slip the range of media

that appears within the Take Selector’s duration in the Timeline. This is useful for synchronizing

other takes to fit the same narrative beat as the first take you used.

�To remove a clip from a Take Selector: Click the clip you want to remove to select it, then

click the trash can button at the upper-right corner of the Take Selector. That take disappears from

the Take Selector.

�To close a Take Selector: Click the X close button, or press the escape key. Whichever take was

selected is now the clip that appears in the Timeline.

�To reopen a Take Selector: Double-click the Take Selector badge at the left of a clip’s name, or

right-click a multi-take clip and choose Take Selector from the contextual menu.

�To eliminate a Take Selector leaving only the take you want: Close the Take Selector, if open,

then right-click that clip in the Timeline and choose Finalize Take from the contextual menu.

Compositing and Grading Take Selectors

Since compound clips act like a single clip in the Timeline, they appear as a single MediaIn node in the

Fusion page, and you grade them as you would any other single clip in the Color page. However, for

Take Selectors, the composite or grade is applied to the Take Selector itself; when you switch to any

other take, it appears with the same composition and grade.

NOTE: Any keyframing you do is relative to the Timeline of the overall Take Selector. This

means that if you create a keyframed effect in either the Fusion or Color pages using take 1,

and you then switch to takes 2, 3, or 4, the timing might not be exactly the same and you

might need to make some adjustments.


Edit | Chapter 43 Take Selectors, Compound Clips, and Nested Timelines

EDIT

Compound Clips

You can select a series of clips in the Timeline, be they edited one after the other in serial or

superimposed and stacked in parallel, and turn them into a compound clip, which is a single clip in

the Timeline that’s actually comprised of many other audio and video clips embedded inside. This

allows you to work with a block of clips as if it were a single unit, governed by a single set of Inspector

controls, and able to be connected to another clip in your timeline by a single transition.

Editing a compound clip works the same as editing any other type of clip. They can be edited,

trimmed, and deleted using all the same methods. In addition, compound clips can be renamed, and

decomposed back into their component clips right in the Timeline.

To create a compound clip by selection:


Select a range of clips.

Selecting a range of clips to turn into a compound clip


Right-click one of the selected clips and choose New Compound Clip.


Enter an optional start timecode and a name, and click Create.

The New Compound

Clip Properties dialog

A compound clip is created which takes the place of the original clips you selected on the

Timeline. Additionally, a copy of that compound clip appears in the currently selected bin of the

Media Pool.


Edit | Chapter 43 Take Selectors, Compound Clips, and Nested Timelines

EDIT

The resulting compound clip

To create a compound clip by In-Out range:


Select a range of clips using In and Out points on the Timeline. This allows you to select partial

sections of a clip to add to the compound, rather than the whole clip. All tracks between the In-Out

range will be included, even if the track is disabled or auto select is off.

Selecting a range of clips

based on In and Out points

to turn into a compound

clip. Note that this

selection includes only

parts of the first and

last clips in the range.


Right-click on the timeline range and choose Convert In and Out to Compound Clip.

Right clicking on the

In-Out range (gray bar)

on the Timeline brings

up the context menu.


Edit | Chapter 43 Take Selectors, Compound Clips, and Nested Timelines

EDIT


Enter an optional start timecode and a name, and click Create.

The resulting bounds of the

compound clip showing

only the media included in

the exact In-Out range.

To rename a compound clip:

�Click the name of the compound clip twice in the Media Pool to select the name text. Type a new

name, and press the Return key to accept the change.

To edit a compound clip:


Right-click any compound clip and choose Open in Timeline from the contextual menu.

The Timeline updates with the contents of the compound clip, which you can re-edit at your discretion.

An open compound

clip in the Timeline


To return to the original timeline when you’re finished, double-click the name of the enclosing

timeline in the path control at the bottom left-hand corner of the Timeline.

The path control you can use to close the compound clip


Edit | Chapter 43 Take Selectors, Compound Clips, and Nested Timelines

EDIT

To decompose a compound clip into its individual clips in the Timeline:

�Right-click any compound clip and choose Decompose in Place from the contextual menu.

The compound clip is replaced by the individual clips it was made from.

To edit a compound clip from the Media Pool to the Timeline as individual clips:


Choose Edit > Decompose Compound Clips on Edit so the menu item is checked.


Use any editing command except for Fit to Fill or Place on Top to edit a compound clip

from the Media Pool or Source Viewer to the Timeline to edit it as a sequence of individual,

decomposed clips.

To change the timecode of a compound clip:

You can change the starting timecode for both multicam and compound clips. To do so, right-click

on the multicam or compound clip in the Media Pool, and select Starting Timecode from the context

menu. A Set New Start Timecode box will appear, then type in the new starting timecode you wish to

use, and click OK.