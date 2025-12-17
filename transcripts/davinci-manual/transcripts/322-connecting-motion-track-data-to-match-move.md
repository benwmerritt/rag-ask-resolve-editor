---
title: "Connecting Motion Track Data to Match Move"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 322
---

# Connecting Motion Track Data to Match Move

Now that we have a successful analysis, it’s time to use it to create the Match Move effect. To make

this process easier, we’ll double-click the tracker’s name in the Tracker List of the Inspector, and enter

a new name that’s easier to keep track of (heh). Adding your own names make that tracker easier to

find in subsequent contextual menus and lets you keep track of which trackers are following which

subjects as you work on increasingly complex compositions.

Renaming a tracker to make it easier to find

Now it’s time to connect the track we’ve just made to the text in order to start it in motion. After loading

the Merge1 node into the viewer to see the text in context with the overall composite we’re creating,

we’ll select the Text1 node to open its parameters in the Inspector, and click the Layout panel icon

(second button from the left) to expose the Layout controls, which are the text-specific transform

controls used to position the text object in the frame. These are the controls that are manipulated

when you use the Text node onscreen controls for repositioning or rotating text.


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

The Layout controls for a Text node,

in the Layout panel

The Center X and Y parameters, while individually adjustable, also function as a single target for

purposes of connecting to tracking to quickly set up match moving animation. You set this up via the

contextual menu that appears when you right-click any parameter in the Inspector, which contains a

variety of commands for adding keyframing, modifiers, expressions, and other automated methods of

animation including connecting to motion tracking.

If we right-click anywhere on the line of controls for Center X and Y, we can choose Connect To >

Tracker1 > Bridge Track: Offset position from the contextual menu, which connects this parameter to

the tracking data we analyzed earlier.

Connecting the Center X and Y parameter to the Bridge Track: Offset position motion path we analyzed

Immediately, the text moves so that the center position coincides with the center of the tracked

motion path at that frame. This lets us know the center of the text is being match moved to the motion

track path.


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

The text now aligns with the motion track coordinate

Offsetting the Position of a Match Moved Image

In fact, we want to offset the match-moved text, so it’s higher up in the frame. To do this, we select the

Tracker1 node again and use the Y Offset 1 dial control to move the text up, since now any changes we

make to the Bridge Track dataset now apply to the center of the text that’s connected to it.

Using the X and Y Offset controls in the Tracker1 node to

offset the text layer’s position from the tracked motion path

The offset we create is shown as a dotted red line that lets us see the actual offset being created

by the X and Y Offset controls. In fact, this is why we connected to the Bridge Track: Offset position

option earlier.

The text offset from the tracked motion path; the offset can be seen as a dotted red line in the viewer


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Now, if we play through this clip, we can see the text moving along with the bridge.

Two frames of the text being match moved to follow the bridge in the shot


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Chapter 83

Planar Tracking

This chapter provides an overview of how to use the Planar Tracker node, and how

to use it to make match moves simple.

For more information about the Planar Tracker node, see Chapter 119, “Tracking Nodes,” in the

DaVinci Resolve Reference Manual or Chapter 59 in the Fusion Reference Manual.

Contents

Introduction to Tracking������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1761

Using the Planar Tracker������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1761

Different Ways of Using the Planar Tracker Node���������������������������������������������������������������������������������������������������������������� 1761

Setting Up to Use the Planar Tracker��������������������������������������������������������������������������������������������������������������������������������������� 1762

Check for Lens Distortion���������������������������������������������������������������������������������������������������������������������������������������������������������������� 1762

A Basic Planar Tracker Match Move Workflow�������������������������������������������������������������������������������������������������������������������� 1763

Tips for Choosing Good Planes to Track�������������������������������������������������������������������������������������������������������������������������������� 1766


Fusion Fundamentals | Chapter 83 Planar Tracking

FUSION