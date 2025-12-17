---
title: "Tracker [TRA]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 496
---

# Tracker [TRA]

The Tracker node

Tracker Node Introduction

The Tracker is used to detect and follow one or more pixel patterns across frames in moving video.

The tracking data can then be used to control the position or values of other nodes in the composition

(for example, the center of a Light Rays node). Additionally, trackers can be used to stabilize an image

or to apply destabilization to one image based on the motion of another.

For more information, see Chapter 82, "Using the Tracker Node," in the DaVinci Resolve

Reference Manual or Chapter 22 in the Fusion Reference Manual.

Inputs

The Tracker has three inputs:


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Background: The orange image input accepts the main 2D image to be tracked.

Foreground: The optional green foreground accepts a 2D image to be merged on top of the

background as a corner pin or match move.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes,

paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the tracking

to certain areas.

Basic Node Setup

Tracker nodes can be applied inline with other nodes or as a branch from the clip you want to track.

When used inline, an image can be stabilized by connecting it to the orange background input. After

the image is tracked, setting the Tracker’s Operation menu to Match Move will apply a stabilization to

the connected image.

A Tracker node connected inline to an image for stabilization

When used as an offshoot from the node tree, an image can be tracked and then that tracking data is

published for use on another node somewhere else in the node tree. The output of the Tracker does

not need to connect to another node. The tracking data is published and can be used via the Connect

To contextual menu.

A Tracker node branched from the node tree

The Tracker can also work as a replacement for a Merge tool in match-moving setups. Below, the

Tracker tracks the image connected to the orange background input and applies the tracking data

to the image connected to the foreground input. The same foreground-over-background merge

capabilities are available in the Tracker node.

A Tracker node set up to apply a match move to the foreground input


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

IntelliTrack AI Point Tracker

The Fusion Tracker node now defaults to using IntelliTrack, the new DaVinci Neural Engine tracker.

Using AI makes tracking easier and more precise, especially when tracking many points.

IntelliTrack, like other AI tools, doesn’t use predetermined rulesets or heuristics. Instead, it is trained

on real world examples. This makes it less likely to fail in scenarios like tracking a subject behind brief

occlusions. For most cases it will be more precise and more robust than the normal point tracker.

All the IntelliTrack analysis happens behind the scenes, and there is no additional user input required,

other than to choose the IntelliTrack setting, set the tracking crosshairs over high contrast areas on the

same moving subject, and then press one of the tracker direction controls.

Adding a Tracking Point in the IntelliTrack mode in the Fusion Tracker

NOTE: The original Point tracker is still available to use by choosing the Point button.

Legacy Point Tracker Onscreen Controls

Though Fusion now defaults to IntelliTrack, if you wish to continue to use the old Point tracker, it is

still available by clicking the Point button. Each pattern in the tracker has its own set of onscreen

controls used to select the pixels in the image to be tracked. These controls are visible in the viewers

whenever you select a tracker in the node tree.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Tracker onscreen controls

Pattern Rectangle

In the viewer, the tracker displays a solid-line red rectangle called the pattern rectangle. Every pixel

within the rectangle makes up the pattern used for tracking. You can resize the pattern if necessary by

dragging on the rectangle’s borders.

A pattern rectangle identifies the area to track

Search Rectangle

Whenever the mouse moves over the pattern rectangle, a second rectangle with a dashed outline

appears. The dashed outline represents the search area, which determines how far away from the

current pattern the Tracker looks in the next frame. The search area should always be larger than the

pattern, and it should be large enough to encompass the largest frame-to-frame movement in the

scene. Faster moving objects require larger search areas, and slower moving objects can get away

with smaller search areas. The larger the search area, the longer it takes to track, so try not to make

the search area larger than necessary. If the selected Tracker has a custom name, the name of that

Tracker is displayed as a label at the bottom right of the search area rectangle.

The search rectangle is the area searched

from frame to frame to locate the pattern.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Repositioning the Tracker

The pattern rectangle has a small handle in the upper-left corner. Dragging on the handle repositions

the pattern. An enlarged view of the pattern is displayed under your mouse pointer to assist with the

precise positioning of the pattern. This thumbnail disappears when the mouse button is released. You

can adjust the magnification ratio in the Inspector’s Options tab.

Dragging the handle magnifies the pattern

rectangle for precise placement.

TIP: There is no limit to the number of trackers that can be used in one composition, or

the number of objects that use the tracking data. There is also no limit to the number of

patterns that can be tracked by a single Tracker node. This chapter serves as a reference

for the various controls in the Tracker, but we strongly suggest you read the more general

information see Chapter 82, "Using the Tracker Node," in the DaVinci Resolve Reference

Manual or Chapter 22 in the Fusion Reference Manual.

The Tracker can be employed in two forms: as a node in the Node Editor or as a modifier

attached to a parameter. When used as a node in the Node Editor, the image tracked comes

from the input to the Tracker node. When used as a modifier, controls appear in the Modifiers

tab for the node with the connected control. Tracker Modifiers can track only one pattern,

but the image source can come from anywhere in the composition. Use this technique when

tracking a quick position for an element.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION