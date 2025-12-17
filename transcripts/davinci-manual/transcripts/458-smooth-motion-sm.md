---
title: "Smooth Motion [SM]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 458
---

# Smooth Motion [SM]

The Smooth Motion node

Smooth Motion Node Introduction

The Smooth Motion node smooths various AOV (Arbitrary Output Variables) channels in a clip using

optical flow to look at neighboring frames. It can be used for smoothing the Disparity channel in a

stereo 3D clip, where it helps reduce temporal edge/fringing artifacts, but it can also smooth a wide

range of channels like vectors, normals, and Z.

It is required that the image connected to the input on the node have precomputed Vector and Back

Vector channels; otherwise, this tool prints error messages in the Console window.

Check on the channels you want to temporally smooth. Be aware that if a channel selected for

smoothing is not present, Smooth Motion will not fail, nor will it print any error messages.

It can also be used to smooth the Vector and Back Vector channels; however, sometimes, this can

make the interpolated results worse if there are conflicting motions or objects in the shot that move

around erratically, jitter, or bounce rapidly.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

TIP: You can use two or more Smooth Motion nodes in sequence to get additional

smoothing. With one Smooth Motion node, the previous, current, and next frames are

examined for a total of 3; with two Smooth Motion nodes, 5 frames are examined; and with

three Smooth Motion nodes, 7 frames are examined.

Another technique using two Smooth Motion nodes is to use the first Smooth Motion node to smooth

the Vector and Back Vector channels. Use the second Smooth Motion to smooth the channels you

want to smooth (e.g., Disparity). This way, you use the smoothed vector channels to smooth Disparity.

You can also try using the smoothed motion channels to smooth the motion channels.

Inputs

The Smooth Motion node includes a single orange image input.

Input: The orange image input accepts a 2D image. This is the sequence of images for which you want

to compute smooth motion. This image must have precomputed Vector and Back Vector channels

either generated from an Optical Flow node or saved in EXR format with vector channels.

Basic Node Setup

The Smooth Motion node takes the output of the Optical Flow node for the required Vector and

Back Vector channels. The Smooth Motion node can then be used to smooth those channels or

AO channels.

A Smooth Motion node using Vector and Back Vector channels from the Optical Flow node.

Inspector

The Smooth Motion Controls tab


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Controls Tab

The Controls tab includes checkboxes for the channels you want to smooth. If a channel selected

for smoothing is not available in the input image, Smooth Motion will not fail, nor will it print any error

messages to the Console.

Channel

Smooth Motion can be applied to more than just the RGBA channels. It can also be applied to the

other AOV channels.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Optical Flow nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.

Tween [Tw]

The Tween node

Tween Node Introduction

Tween reconstructs a missing frame by interpolating between two neighboring frames using

the optical flow. Tween is nearly identical in functionality to Time Speed and Time Stretcher.

The major difference is that it works on two images that are not serial members of a sequence. As a

consequence, it cannot use the Vector or Back Vector aux channels stored in the images. The Tween

node manually generates the optical flow, so there is no need to add an Optical Flow node before the

Tween node. The generated optical flow is thrown away and is not stored back into the output frames.

Since optical flow is based on color matching, it is a good idea to color correct your images to match

ahead of time. Also, if you are having trouble with noisy images, it may also help to remove some of

the noise ahead of time.

Tween destroys any input aux channels. See the Optical Flow node for controls and settings information.

Inputs

There are two image inputs on the Tween node and an effects mask input.

Input 0: The orange input, labeled input 0, is the previous frame to the one you are generating.

Input 1: The green input, labeled input 1, is the next frame after the one you are generating.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the Tween to certain areas.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Basic Node Setup

The Tween node receives two inputs for the two neighboring frames to the one you are generating.

Below, the previous frame, frame 01, is connected to the orange input 0. The next frame, frame 03, is

connected to the green input 1. The Tween node will generate frame 02 and output the sequence.

The Tween node receives two neighboring frames and generates the middle one.

Inspector

The Tween Controls tab

Controls Tab

The Controls tab includes options for how to tween frames. It also includes controls for adjusting the

optical flow analysis, identical to those controls in the Optical Flow node.

Interpolation Parameter

This option determines where the frame you are interpolating is, relative to the two source frames A

and B. An Interpolation Parameter of 0.0 will result in frame A, a parameter of 1.0 will result in frame B,

and a parameter of 0.5 will yield a result halfway between A and B.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Depth Ordering

The Depth Ordering determines which parts of the image should be rendered on top by selecting

either Fastest On Top or Slowest On Top. The examples below best explain these options.

In a locked-off camera shot where a car is moving through the frame, the background does not move,

so it produces small, or slow, vectors, while the car produces larger, or faster, vectors.

The Depth Ordering in this case is Fastest On Top since the car draws over the background.

In a shot where the camera pans to follow the car, the background has faster vectors, and the car has

slower vectors, so the Depth Ordering method is Slowest On Top.

Clamp Edges

Under certain circumstances, this option can remove the transparent gaps that may appear on the

edges of interpolated frames. Clamp Edges causes a stretching artifact near the edges of the frame

that is especially visible with objects moving through it or when the camera is moving.

Because of these artifacts, it is a good idea to use Clamp Edges only to correct small gaps around the

edges of an interpolated frame.

Edge Softness

This slider is displayed only when Clamp Edges is enabled. The slider helps to reduce the stretchy

artifacts that might be introduced by Clamp Edges.

If you have more than one of the Source Frame and Warp Direction checkboxes turned on, this

can lead to doubling up of the stretching effect near the edges. In this case, you‘ll want to keep the

softness rather small at around 0.01. If you have only one checkbox enabled, you can use a larger

softness at around 0.03.

Source Frame and Warp Direction

These checkboxes allow you to choose which frames and vectors create the in-between frames.

Each method ticked on will be blended into the result.

�Prev Forward: Takes the previous frame and uses the Forward vector to interpolate

the new frame.

�Next Forward: Takes the next frame in the sequence and uses the Forward vector to interpolate

the new frame.

�Prev Backward: Takes the previous frame and uses the Back Forward vector to interpolate

the new frame.

�Next Backward: Takes the next frame in the sequence and uses the Back vector to interpolate

the new frame.

Optical Flow Options

These settings tweak the optical flow analysis. See the Class and Advanced Controls section for the

Optical Flow node earlier in this chapter.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Optical Flow nodes. These common

controls are described in detail in the following “The Common Controls” section.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION