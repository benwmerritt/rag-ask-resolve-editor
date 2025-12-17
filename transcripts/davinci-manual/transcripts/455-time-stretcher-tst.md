---
title: "Time Stretcher [TSt]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 455
---

# Time Stretcher [TSt]

The Time Stretcher node

Time Stretcher Node Introduction

The Time Stretcher node is similar to the Time Speed node but permits the speed of the clip to be

animated. Full spline control of the effect is provided, including smoothing. As a result, the Time

Stretcher can be used to animate a single clip to 200, back to normal speed, pause for a second, and

then play backward (like a VCR rewinding).

Image interpolation offers smooth, high-quality results, all using a spline curve to adjust time

nonlinearly. To apply constant time changes such as frame rate changes, use a Time Speed instead.

When operating in Flow mode, Optical Flow data is required. This node does not generate optical flow

directly; you must create it manually upstream using an Optical Flow node or by loading the forward/

reverse vector channels from disk.

Flow Stretcher does not interpolate the aux channels but instead destroys them. In particular, the

Vector/BackVector channels are consumed/destroyed. Add an Optical Flow after the Flow Stretcher if

you want to generate flow vectors for the retimed footage.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Inputs

The single input on the Time Stretcher node is used to connect a 2D image that will be time stretched.

Input: The orange input is used for the primary 2D image that will be time stretched.

Basic Node Setup

Like the Time Speed node, the Time Stretcher setup is as simple as connecting a 2D image into the

orange background input of the node.

A MediaIn node having its time ramped to various

speeds in the Time Stretcher node.

Inspector

The Time Stretcher controls

Source Time

This control designates from which frame in the original sequence to begin sampling.

When a Time Stretcher node is added to the node tree, the Source Time control already contains a

Bézier spline with a single keyframe set to 0.0. The keyframe position is determined by the current

time when the node is added to the node tree.

NOTE: The Source Time spline may not be immediately visible until Edit is selected from the

Source Time’s contextual menu, or Display all Splines is selected from the Spline Window’s

contextual menu.

Interpolate Mode

This menu determines the how the time speed is processed in order to improve its visual playback

quality, especially in the case of clips that are slowed down.

There are three choices in the menu.

�Nearest: The most processor efficient and least sophisticated method of processing; frames are

either dropped for fast motion or duplicated for slow motion.

�Blend: Also processor efficient but can produce smoother results; adjacent duplicated frames are

dissolved together to smooth out slow or fast motion effects.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

�Flow: The most processor intensive but highest quality method of speed effect processing.

Using vector channels pre-generated from an Optical Flow node, new frames are generated to

create slow or fast motion effects. The result can be exceptionally smooth when motion in a clip

is linear. However, two moving elements crossing in different directions or unpredictable camera

movement can cause unwanted artifacts.

Sample Spread

This slider is displayed only when Interpolation is set to Blend. The slider controls the strength of the

interpolated frames on the current frame. A value of 0.5 blends 50% of the frame before and 50% of

the frame ahead and 0% of the current frame.

Depth Ordering

This menu is displayed only when Interpolation is set to Flow. The Depth Ordering is used to

determine which parts of the image should be rendered on top. This is best explained by example.

In a locked-off camera shot where a car is moving through the frame, the background does not move,

so it produces small, or slow, vectors. The car produces larger, or faster, vectors.

The Depth Ordering in this case is Fastest on Top, since the car draws over the background.

In a shot where the camera pans to follow the car, the background has faster vectors, and the car has

slower vectors, so the Depth ordering method would be Slowest on Top.

Clamp Edges

This checkbox is displayed only when Interpolation is set to Flow. Under certain circumstances, this

option can remove the transparent gaps that may appear on the edges of interpolated frames. Clamp

Edges can cause a stretching artifact near the edges of the frame that is especially visible with objects

moving through it or when the camera is moving.

Because of these artifacts, it is a good idea to use clamp edges only to correct small gaps around the

edges of an interpolated frame.

Edge Softness

This slider is displayed only when Interpolation is set to Flow and Clamp Edges is enabled. It helps to

reduce the stretchy artifacts that might be introduced by Clamp Edges.

If you have more than one of the Source Frame and Warp Direction checkboxes turned on, this

can lead to doubling up of the stretching effect near the edges. In this case, you’ll want to keep the

softness rather small at around 0.01. If you have only one checkbox enabled, you can use a larger

softness at around 0.03.

Source Frame and Warp Direction

These checkboxes are displayed only when Interpolation is set to Flow. These controls determine

which frames and which vectors are used to create the in-between frames. Each method ticked on will

be blended into the result.

�Prev Forward: Takes the previous frame and uses the Forward vector to

interpolate the new frame.

�Next Forward: Takes the next frame in the sequence and uses the Forward vector to

interpolate the new frame.

�Prev Backward: Takes the previous frame and uses the Back Forward vector to

interpolate the new frame.

�Next Backward: Takes the next frame in the sequence and uses the Back vector to

interpolate the new frame.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Example

Make sure that the current time is either the first or last frame of the clip to be affected in the

project. Add the Time Stretcher node to the node tree. This will create a single point on the

Source Time spline at the current frame. The value of the Source Time will be set to zero for

the entire Global Range.

Set the value of the Source Time to the frame number to be displayed from the original source,

at the frame in time it will be displayed in during the project.

To shrink a 100-frame sequence to 25 frames, follow these steps:

1.

Change the Current Time to frame 0.

2.

Change the Source Time control to 0.0.

3.

Advance to frame 24.

4.

Change the Source Time to 99.

5.

Check that the spline result is linear.

6.

Fusion will render 25 frames by interpolating down the 100 frames to a length of 25.

7.

Hold the last frame for 30 frames, and then play the clip backward at regular speed.

Continue the example from above and follow the steps below.

8.

Advance to frame 129.

9.

Right-click on the Source Time control and select Set Key from the menu.

10.	 Advance to frame 229 (129 + 100).

11.	 Set the Source time to 0.0.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other miscellaneous nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Wireless Link [Wire]

The Wireless Link node

Wireless Link Node Introduction

The Wireless Link node helps manage the tangle of connection lines in a node tree by wirelessly

connecting one 2D node to another 2D node.

Although Wireless Links can be helpful, try to keep as much of a node tree as visible as possible;

otherwise, you lose one of the main benefits of a node tree.

Inputs

There are no inputs on this node.

Basic Node Setup

There is no setup for this node. It is a free-standing node that connects “wirelessly” using the control

in the Inspector.

Inspector

The Wireless Link Controls tab

Controls Tab

The Controls tab in the Wireless Link node contains a single Input field for the linked node.

Input

To use the Wireless Link node, in the Node Editor, drag the 2D node into the Input field of the Wireless

Link node. Any change you make to the original node is wirelessly replicated in the Wireless Link

node. You can use the output from the Wireless Link node to connect to a nearby node.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other miscellaneous nodes. These common

controls are described in detail in the following “The Common Controls” section.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION