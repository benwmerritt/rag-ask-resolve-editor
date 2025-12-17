---
title: "Keyboard Shortcuts in This Chapter"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 139
---

# Keyboard Shortcuts in This Chapter

Here’s a list of of keyboard shortcuts you might find helpful that relate to topics found in this chapter.

Key Shortcut

Function

V

Select nearest edit to playhead

Shift-V

Select clip intersecting playhead

U

Select incoming, outgoing, or centered part of edit

Option-U

Toggle selection among video+audio, video only, and

audio only

Option-Y

Select clips forward (of the playhead) on all tracks

Command-Option-Y

Select clips backward (of the playhead) on all tracks

Y

Select clips forward (of the playhead) on current track

Command-Y

Select clips backward (of the playhead) on current track

Up, Down Arrow Keys

Move selection to previous/next edit or clip

Delete

Delete clip and leave gap (lift edit)

Forward Delete

Ripple delete; deletes a clip and moves the rest of the timeline

left to fill the gap

Command-Backslash (\)

Insert edit; adds a cut to the clip(s) at the position of

the playhead


Edit | Chapter 36 Editing Basics

EDIT

Key Shortcut

Function

N

Toggle timeline snapping off and on

Command-Shift-L

Toggle linked selection off and on

Option-1 through 8

Set video destination control to that track number; press again

to enable/disable

Command-Option-1 thorugh 8

Set audio destination control to that track number; press again

to enable/disable

Option-Shift-1 through 8

Toggle lock for individual video tracks

Option-Shift-9

Toggle lock for all video tracks

Option-Shift-F1 through F8

Toggle lock for individual audio tracks

Option-Shift-F9

Toggle lock for all audio tracks

F9

Insert Edit selected clip(s) from Media Pool or Source Viewer

to the Timeline

F10

Overwrite Edit selected clip(s) from Media Pool or Source

Viewer to the Timeline

F11

Replace Edit the first of selected clip(s) from Media Pool or

Source Viewer to the Timeline

F12

Place On Top Edit from Media Pool or Source Viewer to

the Timeline

Shift-F10

Ripple Overwrite from Media Pool or Source Viewer to

the Timeline

Shift-F11

Fit to Fill from Media Pool or Source Viewer to the Timeline

Shift-F12

Append To End Edit from Media Pool or Source Viewer to

the Timeline

Undo

Command-Z

Redo

Command-Shift-Z

Drag and Drop Editing

If you’ve already used other editing programs, the procedures in this section will almost certainly be

remedial, but if you’re new to editing, this section covers the most basic methods of editing a series of

clips into the Timeline to get you started. The absolute simplest method of editing is to drag clips from

the Media Pool and drop them into the Timeline. You can do this with individual clips, or with selected

groups of clips.


Edit | Chapter 36 Editing Basics

EDIT

Drag and Drop Editing of Individual Clips Into the Timeline

If you’re just editing one clip at a time to create an edited sequence in a timeline, this is how that works.


If you need to edit specific ranges of the clips you’re editing, you can set In and Out points in

source clips first by doing one of the following:

Setting In and Out points while skimming a thumbnail in the Metadata View: As you’re skimming

over a clip’s thumbnail in the Viewer, press I and O to set In and Out points to encompass the

part of that clip you’re going to want to use. If you’ve turned on Live Media Preview in the Source

Viewer, then the Source Viewer will show what you’re skimming so you can get a closer look.

If you don’t like the current In and Out points, you can press Option-X to clear them both.

Setting In and Out points while skimming a thumbnail in the Media Pool: As you’re skimming

over a clip’s thumbnail in the Viewer, press I and O to set In and Out points to encompass the

part of that clip you’re going to want to use. If you’ve turned on Live Media Preview in the Source

Viewer, then the Source Viewer will show what you’re skimming so you can get a closer look.

When you’re finished, that clip’s thumbnail will show a range indicator at the bottom to show how

much of the clip you’ve selected. If you don’t like the current In and Out points, you can press

Option-X to clear them both.

Using the Media Pool Filmstrip in the Media Pool’s List view: Set the Media Pool to List view,

select Show Filmstrip in the option menu, then select a clip to expose it in the Filmstrip at the top

of the Media Pool, drag the pointer through the Filmstrip to watch it play and press I and O to set

In and Out points to the appropriate range. The Filmstrip will dim the heads and tails to let you see

the range of media you’ve marked. If you’ve turned on Live Media Preview in the Source Viewer,

then the Source Viewer will show what you’re skimming so you can get a closer look. If you don’t

like the current In and Out points, you can press Option-X to clear them both.

Using the Source Viewer: Open a clip in the Viewer by double-clicking it in the Media Pool, or

by selecting it in the Media Pool and pressing the Return or Enter key. Then use the transport

controls, jog bar, control panel buttons, Spacebar, or JKL commands to move the playhead, and

place In and Out points using the In and Out buttons to the right of the transport controls, or by

pressing the I or O keys. If you don’t like the current In and Out points, you can press Option-X to

clear them both.


Drag the clip you want to edit from either the Media Pool or the Source Viewer, and drop it onto

the desired position in the Timeline to perform an overwrite edit. If you drag a clip on top of

another clip that’s already in the Timeline, the clip you’re dragging will overwrite the part of the clip

that it overlaps.

Dragging a clip from the Media Pool to overwrite a clip in the Timeline

TIP: If you drag a clip into the blank area above an existing video track or below an existing

audio track, a new track will automatically be created.


Edit | Chapter 36 Editing Basics

EDIT

Drag and Drop Editing of Several

Clips Into the Timeline At Once

The procedure above also works when you want to edit several clips into the Timeline at once by

dragging them from the Media Pool.


Change the sort order of the Media Pool’s browser area to put the clips into the order in which you

want them to appear. In Thumbnail view you can use the Sort Order menu, but in List view you can

click the header of any metadata column to sort by that column’s data. If you’ve used the Metadata

Editor to add Scene, Shot, Take, or other information to identify each clip, you can sort by these

metadata criteria.


Use the Media Pool thumbnails, the Media Pool List view Filmstrip, or the Source Viewer to set In

and Out points to define the part of each clip that you want to edit into the Timeline.


Select the Media Pool clips you want to edit into the Timeline by dragging a bounding box,

Command-dragging multiple bounding boxes over different sets of clips, by Shift-clicking a range

of clips, or by Command-clicking individual non-contiguous clips.


Drag any of the selected clips to the desired position in the Timeline to perform an overwrite edit.

Using the Sort Order menu to change the sort order of clips in the Media Pool

Dragging multiple clips into the Timeline in the sort order of the Media Pool


Edit | Chapter 36 Editing Basics

EDIT

The clip(s) you drag overwrite whatever other clips they overlap in the Timeline. Multiple clips

dragged from the Media Pool will be edited in the order in which they’re sorted in the Media

Pool, using each clip’s In and Out points.

Drag and Drop Editing of Video-Only or Audio-Only Edits

While it’s easy to edit just the video or just the audio of a clip by disabling the audio or video

destination control in the Timeline prior to doing any sort of edit (described later in Chapter 39,

“Three- and Four-Point Editing”), there’s also a pair of keyboard modifiers you can use to do the very

same thing while you’re dragging.

To edit only the video of a clip from the Media Pool: Option-drag clips from the Media Pool/

Filmstrip, Source Viewer, or Finder into the Timeline.

To edit only the audio of a clip from the Media Pool: Shift-drag clips from the Media Pool/

Filmstrip, Source Viewer, or Finder into the Timeline.

To edit only the video or audio of a clip from the Source Viewer: Open a clip into the Source

Viewer, then move the pointer over the Source Viewer and drag from either the Video-only or

Audio-only overlays that appear over the bottom of the image.

Video and Audio-only overlay controls appear in the

Source Viewer that let you drag just the video or just

the audio into the Timeline

Drag and Drop Insert Editing

You can also drag multiple clips from the Timeline, or a single clip from the Source Viewer, at any

frame of the current timeline to either insert the selection between any two clips or to insert it in the

middle of an existing clip, moving (actually rippling) all media to the right of the new edit point you

create to make room for the new incoming media.

To shuffle insert multiple clips from the Media Pool or Source Viewer into the Timeline:


Select one or more clips in the Media Pool (the sort order dictates the final order of the edited

clips), or open a clip in the Source Viewer.


Press and hold the Command and Shift keys, and drag the selection from the Media Pool or

Source Viewer into the Timeline.


As you drag, the clips you’re dragging will be inserted into the Timeline at the pointer location.

Release the mouse to finish making the edit.


Edit | Chapter 36 Editing Basics

EDIT

Making an Insert Edit while dragging clips from the Media Pool

Dragging Clips From the File System Into the Timeline

You can also drag a clip directly from your file system to the Timeline on supported platforms.

Dragging multiple clips into the Timeline from the macOS Finder


Edit | Chapter 36 Editing Basics

EDIT