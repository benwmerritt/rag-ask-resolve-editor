---
title: "Keyframes Editor Tracks"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 269
---

# Keyframes Editor Tracks

While each clip and effect node in your composition is represented by a track, keyframed parameters

are exposed either as keyframes superimposed upon the track to which they’re applied (as seen on

the MOVEMENT track), or they can be opened up onto their own tracks for more precise editing, one

keyframe track per keyframed parameter, by clicking a disclosure control to the left of that track’s

name in the Timeline header (as seen under the “Drip1” track).

The Timeline tracks

The Timeline Header

The Timeline header area on the left side of the Timeline is a hierarchical list of all tracks in a

composition. Each track displays the name of its corresponding node, a lock button, and a disclosure

control for revealing keyframe tracks for each keyframe animation, modifier, and mask that’s

attached to it.

Collapse/Open All

A quick way to open or close all available keyframe tracks at once is to use the Expand/Collapse Tool

Controls commands in the Keyframe Timeline Option menu.


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

The Timeline header area

The Playhead

As elsewhere in Fusion, the playhead is a red vertical bar that runs through the Timeline view to

indicate the position of the current frame or time. The Keyframes Editor playhead is locked to the

viewer playhead, so the image you’re viewing is in sync.

You must click on the playhead directly to drag it, even within the Timeline ruler (clicking and

dragging anywhere else in the Timeline ruler scales the Timeline). Additionally, you can jump the

playhead to a new location by holding down the Command-Option keys and clicking in the track area

(not the Timeline ruler).

The playhead about to be

dragged by the pointer

Spreadsheet

If you turn on the Spreadsheet and then click on the name of a layer in the keyframe track, the numeric

time position and value (or values if it’s a multi-dimensional parameter) of each keyframe appear

as entries in the cells of the Spreadsheet. Each column represents one keyframe, while each row

represents a single aspect of each keyframe.

Editing keyframes in the Spreadsheet


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

For example, if you’re animating a blur, then the Key Frame row shows the frame each

keyframe is positioned at, and the Blur1BlurSize row shows the blur size at each keyframe. If

you change the Key Frame value of any keyframe, you’ll move that keyframe to a new frame of

the Timeline.

Scaling and Panning the Timeline

At the top, a series of zoom and framing controls let you adjust the work area containing the layers.

The Keyframe Editor framing controls

A Horizontal zoom control lets you scale the size of the editor.

A Zoom to Fit button fits the width of all tracks to the current width of

the Keyframes Editor.

A Zoom to Rect tool lets you draw a rectangle to define an area of

the Keyframes Editor to zoom into.

A Sort pop-up menu lets you sort or filter the tracks in various ways.

An Option menu provides access to many other ways of filtering

tracks and controlling visible options.

Working with Segments in the Timeline

Most of the work in the Timeline involves trimming and aligning clip segments.

To select a single segment in the Timeline, do one of the following:

�Click the node’s name in the header.

�Click the node’s segment in the Timeline.

To add another segment to the selection, do one of the following:

�Hold Command and click additional segments to select discontiguous selections.

�Select a segment, and then hold Shift and click another segment to make a contiguous selection

of all segments in between.

To remove a segment from the selection, do the following:

�Hold Command and click a selected segment to deselect it.


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

TIP: Selecting a node’s name from the Timeline header also selects the node’s tile in the

Node Editor, with its controls displayed in the Inspector.

Moving Segments in the Timeline

To move the position of a segment, drag on the node’s segment in the Keyframes Editor. The cursor

will resemble a bar with two arrows pointing in either direction. Moving a segment changes where that

clip begins and ends in the composition.

The Move cursor

Trimming Segments

Trimming segments has different effects on Loaders, MediaIn and Effect nodes:

�Trimming a Loader or MediaIn node is similar to trimming clips in an editing application, in that you’re

changing the in and out points of the range of media that clip makes available to your composition.

�Trimming the segments of effect nodes instead modifies the range of that node’s effect in the

composition. Outside of the trimmed region, that effect node will behave as if it were disabled.

TIP: Shortening the duration of effects nodes can optimize processing. Imagine a Loader

or MediaIn node that represents a clip that’s 100 frames long and is connected to a Defocus

node that’s animated from frames 80–100. There is little to no point in processing the defocus

node between frames 0–79, so trimming the defocus segment to start at frame 80 in the

Timeline will effectively prevent it from rendering and consuming either memory or processor

time until needed.

To trim a segment in the Timeline, do the following:

�Drag on either end of the node’s segment in the Timeline.

The cursor changes to a vertical bar with a single arrow when the cursor is in the right location to trim.

The Trim cursor

Holding the First or Last Frame

If you want to hold a Loader’s first or last frame of a clip for a certain number of frames, also called a

freeze frame, you can hold Command while you drag beyond the first or last of the segment in

the Timeline.


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

Working with Keyframes in the Timeline

Keyframes can be drawn in one of two ways. When keyframe tracks are closed, they’re drawn over the

node’s segment. Clicking on the disclosure icon to the left of the node’s name in the track header expands

the display so each keyframed parameter has its own track in the Timeline, enabling precise editing.

Furthermore, each keyframe track, whether open or closed, exposes a miniature curve overlay

that provides a visual representation of the rise and fall of keyframed values. This little overlay isn’t

directly editable.

The Drip1 segment has its keyframe tracks exposed, while the Text1 segment has

its keyframe tracks collapsed so they’re displayed within the segment.

Drag and Drop Keyframe Editing

Here are pointer-based keyframe editing methods that will get you started.

Methods of selecting keyframes:

�Click a single keyframe to select it.

�Drag a bounding box over a series of keyframes to select them all.

�Command-click to select discontiguous keyframes.

�Shift-click the first and last of a range of keyframes to select a contiguous range.

Methods of adjusting keyframes:

�You can drag keyframes left and right to reposition them in time.

�You can right-click one or more selected keyframes and use contextual menu commands to

change keyframe interpolation, copy/paste keyframes, or even create new keyframes.

Keyframe Editing Using the Time Editor

A drop-down and editing field at the bottom right of the Keyframes Editor lets you numerically edit the

timing, in frames, of any selected keyframe, making it easy to make precise adjustments.

To change the position of a keyframe using the toolbar, do one of the following:

�Select a keyframe, and then enter a new frame number in the Time Edit box.

�Choose T Offset from the Time Editor drop-down, select one or more keyframes, and

enter a frame offset.

�Choose T Scale from the Time Editor drop-down, select one or more keyframes,

and enter a frame offset.

The Time button can switch to Time Offset or Time Scale for moving keyframes.


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION