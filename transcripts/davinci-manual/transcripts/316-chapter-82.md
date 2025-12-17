---
title: "Chapter 82"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 316
---

# Chapter 82

Using the

Tracker Node

This chapter shows the many capabilities of the Tracker node in Fusion, starting

with how trackers can be connected in your node trees, and finishing with the

different tasks that can be performed.

Contents

Introduction to Tracking����������������������������������������������������������������������������������������������������������������������������������������������������������������� 1725

Tracker Node Overview������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1726

Modes of the Tracker Node����������������������������������������������������������������������������������������������������������������������������������������������������������� 1726

Basic Tracker Node Operation����������������������������������������������������������������������������������������������������������������������������������������������������� 1727

Connect to a Tracker’s Background Input������������������������������������������������������������������������������������������������������������������������������� 1727

Analyze the Image to be Tracked������������������������������������������������������������������������������������������������������������������������������������������������ 1727

Apply the Tracking Data������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1728

Viewing Tracking Data in the Spline Editor���������������������������������������������������������������������������������������������������������������������������� 1731

Tracker Inspector Controls������������������������������������������������������������������������������������������������������������������������������������������������������������� 1732

Motion Tracking Workflow In Depth������������������������������������������������������������������������������������������������������������������������������������������ 1733

Connect the Image to Track����������������������������������������������������������������������������������������������������������������������������������������������������������� 1733

Add Trackers������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1733

Refine the Search Area�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1736

Perform the Track Analysis������������������������������������������������������������������������������������������������������������������������������������������������������������ 1736

Tips for Choosing a Good Pattern����������������������������������������������������������������������������������������������������������������������������������������������� 1737

Using the Pattern Flipbooks���������������������������������������������������������������������������������������������������������������������������������������������������������� 1738

Using Adaptive Pattern Tracking������������������������������������������������������������������������������������������������������������������������������������������������� 1739

Dealing with Obscured Patterns������������������������������������������������������������������������������������������������������������������������������������������������� 1740

Dealing with Patterns That Leave the Frame������������������������������������������������������������������������������������������������������������������������� 1740

Setting Up Tracker Offsets��������������������������������������������������������������������������������������������������������������������������������������������������������������� 1741

Stabilizing with the Tracker Node����������������������������������������������������������������������������������������������������������������������������������������������� 1742

Stabilization Using the Tracker Match Move Mode������������������������������������������������������������������������������������������������������������� 1742


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Introduction to Tracking

Tracking is one of the most useful and essential techniques available to a compositor. It can be

roughly defined as the creation of a motion path from analyzing a specific area in a clip over time.

Fusion includes a variety of different tracking nodes that let you analyze different kinds of motion.

Once you have tracked motion on a clip, you can then use the resulting data for stabilization, motion

smoothing, matching the motion of one object to that of another, and a host of other essential tasks.

Types of tracking nodes in Fusion:

Tracker: Follows a relatively small, identifiable feature or pattern in a clip to derive a

2D motion path. This is sometimes referred to as point tracking.

Planar Tracker: Follows a flat, unvarying surface area in a clip to derive a 2 ½D motion path

including perspective. A planar tracker is also more tolerant than a point tracker when some

tracked pixels move offscreen or become obscured.

Camera Tracker: Tracks multiple points or patterns in a clip and performs a more

sophisticated analysis by comparing those moving patterns. The result is a precise recreation

of the live-action camera in virtual 3D space.

Each tracker type has its own chapter in this manual. This chapter covers the tracking

techniques with the Tracker node.

Smoothing Motion������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1743

Using the Tracker Node for Match Moving���������������������������������������������������������������������������������������������������������������������������� 1744

Simple Match Moving������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1744

Corner Positioning Operations����������������������������������������������������������������������������������������������������������������������������������������������������� 1745

Perspective Positioning Operations������������������������������������������������������������������������������������������������������������������������������������������� 1745

Connecting to Trackers’ Operations����������������������������������������������������������������������������������������������������������������������������������������� 1745

Steady Position������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1745

Steady Angle������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1745

Offset Position��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1746

Unsteady Position�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1746

Steady Size���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1746

Using the Outputs of a Tracker����������������������������������������������������������������������������������������������������������������������������������������������������� 1746

Using the Tracker as a Modifier��������������������������������������������������������������������������������������������������������������������������������������������������� 1748

Match Moving Text Example���������������������������������������������������������������������������������������������������������������������������������������������������������� 1751

Adding a Layer to Match Move������������������������������������������������������������������������������������������������������������������������������������������������������ 1751

Setting Up Motion Tracking������������������������������������������������������������������������������������������������������������������������������������������������������������� 1751

A Simple Tracking Workflow����������������������������������������������������������������������������������������������������������������������������������������������������������� 1753

Connecting Motion Track Data to Match Move�������������������������������������������������������������������������������������������������������������������� 1756

Offsetting the Position of a Match Moved Image���������������������������������������������������������������������������������������������������������������� 1758


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Tracker Node Overview

The Tracker node is a single node that actually performs tracking, stabilizing, matching moving, and

corner-pinning operations. Since the Tracker node can transform the foreground input, it can be used

to generate tracks and then operate as a Merge in a match move or corner-pin setup. Or you can

use it to produce tracking data only and then publish that data to other nodes in the Node Editor.

Modes of the Tracker Node

The Tracker node is an incredibly flexible tool often used multiple times in a composite to help with

dozens of tasks. However, most of those tasks can be boiled down into just a few operations. The

Tracker node has four operation modes that cover the majority of tracking situations.

Stabilizing

You can use one or more tracked patterns to remove all the motion from the sequence or to smooth

out vibration and shakiness. When you use a single tracker pattern to stabilize, you stabilize only

the X and Y position. Using multiple patterns together, you are able to stabilize position, rotation,

and scaling.

Match Moving

The reverse of stabilizing is match moving, which detects position, rotation, and scaling in a clip using

one or more patterns. Instead of removing that motion, it is applied to another image so that the two

images can be composited together.

Corner Positioning

Corner positioning tracks four patterns that are then used to map the four corners of a new foreground

into the background. This technique is generally used to replace signs or mobile phone screens.

The Planar Tracker node is often a better first choice for these types of tracking tasks.

Perspective Positioning

Perspective positioning again tracks four patterns to identify the four corners of a rectangle.

Each corner is then mapped to a corner of the image, rescaling and warping the image to remove all

apparent perspective. The Planar Tracker node is often a better first choice for removing perspective

from a clip.


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Basic Tracker Node Operation

All tracking workflows consist of three fundamental steps.


Attach an image you want to track to the yellow background input of the Tracker node.


Set the tracking pattern and analyze the clip to create a path.


Apply the tracking data to stabilize, match move, corner pin, or remove perspective.

Connect to a Tracker’s Background Input

You start by connecting the output of the image you want to track to a Tracker node’s background

input. The Tracker node analyzes the image that’s attached to its background input.

You can insert the Tracker node serially with other nodes if you intend to use the Tracker node itself to

do a simple stabilization operation or if you want to use it to perform the function of a Merge node in a

match move or corner-pin operation.

Tracker node connected serially so it can both

track and transform the input images

However, if you’re just using a Tracker node to analyze data for use with multiple nodes elsewhere in

the comp, you could choose to branch it and leave its output disconnected to indicate that Tracker

node is a data repository. Please note that this is not necessary; serially connected Tracker nodes can

be linked to multiple other nodes as well.

Tracker connected as a branch to indicate it is linked

to other nodes and not used directly

Analyze the Image to be Tracked

After constructing the node tree and inserting the Tracker where you want, you can set up the tracker

in the viewer. You identify one or more features in the image that you wish to track (referred to as

patterns) by adding trackers (there’s one by default) and positioning them using the onscreen controls

in the viewer. After the Tracker node analyzes the clip, the resulting tracking data is stored within that

Tracker node. Keyframes, one per frame, indicate the Tracked Center X and Y data that has been

saved, while a motion path shows the path of tracked data in the viewer.


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

A motion path that indicates the tracked motion, and tic

marks that indicate tracking data keyframes

Apply the Tracking Data

The resulting tracking data stored within the Tracker node is used to stabilize, match move, corner pin,

or remove perspective in one of two ways.

Method 1: Use the Tracker node to match move and merge

You can connect a foreground image to the Tracker node and apply the motion from the analyzed

background image.

Using a Tracker node in line for a match move


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Setting the Operation parameter in the Operation tab in the Inspector to Match Move, Corner Position,

or Perspective Position always applies the motion to the foreground input (if one is connected). This

is an easy workflow for simple situations. In this scenario, you can use the Tracker node to replace a

Merge node since Tracker nodes include all the same functionality as a Merge.

Using a Tracker node to do a match move and merge, all in one

Method 2: Connect specific parameters to the Tracker Node

Alternatively, you can connect the tracking data from the Tracker node to the specific parameters of

other nodes that will actually do the work, for instances where setting up a match move isn’t just a

matter of transforming a foreground image. Each Tracker node and each pattern within the Tracker

node publishes its data for other nodes to use without directly linking to them in the node tree.

For example, in the following node tree, an Ellipse node is being used to isolate a glow effect for the

ray gun prop.

The Tracker set up as a branch and connected using the Connect To menu

The ellipse needs to follow the motion of the ray gun, so a Tracker node is used to analyze the

movement of the gun tip so that tracking data can be used to animate the ellipse. The ellipse is not

connected to the tracker directly via the foreground input but indirectly through the Connect To

contextual menu.


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Applying the light of a ray gun by connecting

tracking data to the center position of an Ellipse node

This is made easier by renaming the Tracker you created to something descriptive of what’s

being tracked.

You can rename trackers in the Tracker List by

double-clicking them and typing descriptive text

Once the tip of the ray gun has been tracked, this tracking data is then connected to the Center

parameter of an Ellipse node that’s limiting a Glow effect by right-clicking the label of the Center

parameter in the Inspector, and choosing Tracker1 > Ray Gun Glow: Offset position from the Connect

to submenu of the contextual menu. All the data from every Tracker node in your node tree and every

tracking pattern appears within this submenu, and since we named the Tracker, it’s easy to find.

Choosing Offset position because it will place the center of the ellipse directly over the path. However,

it also gives us the flexibly to offset the ellipse if need be, using the offset controls in the Inspector.

Right-clicking a parameter’s label lets you connect tracking data to it to animate it

You can connect the data from a Tracker node to any other node’s parameter; however, you’ll most

typically connect track data to center, pivot, or corner X/Y style parameters. When you use tracking

data this way, it’s not necessary to connect the output of the Tracker node itself to anything else in

your node tree; the data is passed from the Tracker to the Center parameter by linking it with the

Connect To submenu.


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION