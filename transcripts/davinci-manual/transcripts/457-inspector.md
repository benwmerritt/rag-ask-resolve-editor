---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 457
---

# Inspector

Optical Flow advanced controls

Controls Tab (Advanced)

When you add an Optical Flow, Repair Frame, or Tween node to a Comp, a Method drop-down menu

in the Inspector allows you to choose between an Advanced GPU-based algorithm or a Classic CPU-

based algorithm. This Advanced method is the same Optical Flow algorithm used in other DaVinci

Resolve pages.

Warp Count

Decreasing this slider makes the optical flow computations faster. To understand what this option

does, you must understand that the optical flow algorithm progressively warps one image until it

matches with the other image. After some point, convergence is reached, and additional warps

become a waste of computational time. You can tweak this value to speed up the computations, but it

is good to watch what the optical flow is doing at the same time.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Iteration Count

Decreasing this slider makes the computations faster. In particular, just like adjusting the Warp Count,

adjusting this option higher will eventually yield diminishing returns and not produce significantly

better results. By default, this value is set to something that should converge for all possible shots and

can be tweaked lower fairly often without reducing the disparity’s quality.

Smoothness

This controls the smoothness of the optical flow. Higher smoothness helps deal with noise, while lower

smoothness brings out more detail.

Half Resolution

The Half Resolution checkbox is used purely to speed up the calculation of the optical flow. The input

images are resized down and tracked to produce the optical flow.

Controls Tab (Classic)

By choosing Classic from the Method drop-down menu in the Inspector, you can use the older CPU-

based algorithm to maintain compatibility with Comps created in previous versions. This method may

also be better suited for some Stereo3D processing.

When using the Classic method, a single slider at the top of the Inspector improves performance

by generating proxies. The remaining Advanced section parameters tune the Optical Flow vector

calculations. The default settings serve as a good standard. In most cases, tweaking of the advanced

settings is not needed. Many deliver small or diminishing returns. However, depending on the settings,

rendering time can easily vary by 10x. If you’re interested in reducing process time, it is best to start by

experimenting with the Proxy, Number of Iterations, and Number of Warps sliders and changing the

filtering to Bilinear.

Proxy (for Tracking)

The Proxy slider is used purely to speed up the calculation of the optical flow. The input images are

resized down by the proxy scale and tracked to produce the optical flow. The computational time is

roughly proportional to the number of pixels in the image. This means a proxy scale of 2 will give a

4x speedup, and a proxy scale of 3 will give a 9x speedup.

Smoothness

This controls the smoothness of the optical flow. Higher smoothness helps deal with noise, while lower

smoothness brings out more detail.

Edges

This slider is another control for smoothness but applies it based on the color channel. It tends to have

the effect of determining how edges in the flow follow edges in the color images. When it is set to a

low value, the optical flow becomes smoother and tends to overshoot edges. When it is set to a high

value, details from the color images start to slip into the optical flow, which is not desirable. Edges in

the flow end up more tightly aligning with the edges in the color images. This can result in streaked-

out edges when the optical flow is used for interpolation. As a rough guideline, if you are using the

disparity to produce a Z-channel for post effects like Depth of Field, then set it lower in value. If you are

using the disparity to perform interpolation, you might want it to be higher in value.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Match Weight

This control sets a threshold for how neighboring groups of foreground/background pixels are

matched over several frames. When set to a low value, large structural color features are matched.

When set to higher values, small sharp variations in the color are matched. Typically, a good value for

this slider is in the [0.7, 0.9] range. When dealing with stereo 3D, setting this option higher tends to

improve the matching results in the presence of differences due to smoothly varying shadows or local

lighting variations between the left and right images. The user should still perform a color match or

deflickering on the initial images, if necessary, so they are as similar as possible. This option also helps

with local variations like lighting differences due to light passing through a mirror rig.

Mismatch Penalty

This option controls how the penalty for mismatched regions grows as they become more dissimilar.

The slider provides a choice between a balance of Quadratic and Linear penalties. Quadratic strongly

penalizes large dissimilarities, while Linear is more robust to dissimilar matches. Moving this slider

toward Quadratic tends to give a disparity with more small random variations in it, while Linear

produces smoother, more visually pleasing results.

Warp Count

Decreasing this slider makes the optical flow computations faster. In particular, the computational time

depends linearly upon this option. To understand what this option does, you must understand that the

optical flow algorithm progressively warps one image until it matches with the other image. After some

point, convergence is reached, and additional warps become a waste of computational time. The

default value in Fusion is set high enough that convergence should always be reached. You can tweak

this value to speed up the computations, but it is good to watch what the optical flow is doing at the

same time.

Iteration Count

Decreasing this slider makes the computations faster. In particular, the computational time depends

linearly upon this option. Just like adjusting the Warp Count, adjusting this option higher will eventually

yield diminishing returns and not produce significantly better results. By default, this value is set to

something that should converge for all possible shots and can be tweaked lower fairly often without

reducing the disparity’s quality.

Filtering

This option controls filtering operations used during flow generation. Catmull-Rom filtering will

produce better results, but at the same time, turning on Catmull-Rom will increase the computation

time steeply.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Optical Flow nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Repair Frame [REP]

The Repair Frame node

Repair Frame Node Introduction

Repair Frame replaces damaged or missing frames or portions of frames with scratches or other

temporally transient artifacts. It requires three frames: the repair frame and two neighboring frames.

An Optical Flow node is not required for generating motion vectors since the Repair Frame node

computes the optical flow. However, this can make it slow to process.

Repair Frame will not pass through, but rather destroys, any aux channels after the

computation is done.

See the Optical Flow node for controls and settings information.

TIP: If your footage varies in color from frame to frame, sometimes the repair can be

noticeable because, to fill in the hole, Repair Frame must pull color values from adjacent

frames. Consider using deflickering, color correction, or using a soft-edged mask to help

reduce these kinds of artifacts.

Inputs

There are two inputs on the Repair Frame node. One is used to connect a 2D image that will be

repaired and the other is for an effect mask.

Input: The orange input is used for the primary 2D image that will be repaired.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the repairs to certain areas.

Basic Node Setup

The Repair Frame node analyzes the incoming MediaIn node and repairs single frame issues

like dust or scratches.

A Repair Frame node set up to analyze a MediaIn

node using internal optical flow analysis.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Inspector

The Repair Frame Controls tab

Controls Tab

The Controls tab includes options for how to repair the frames. It also includes controls for adjusting

the optical flow analysis, identical to those controls in the Optical Flow node.

Depth Ordering

The Depth Ordering determines which parts of the image should be rendered on top by selecting

either Fastest On Top or Slowest On Top. The examples below best explain these options.

In a locked-off camera shot where a car is moving through the frame, the background does not move,

so it produces small, or slow, vectors, while the car produces larger, or faster, vectors.

The depth ordering in this case is Fastest On Top since the car draws over the background.

In a shot where the camera pans to follow the car, the background has faster vectors, and the car has

slower vectors, so the Depth Ordering method is Slowest On Top.

Clamp Edges

Under certain circumstances, this option can remove the transparent gaps that may appear on the

edges of interpolated frames. Clamp Edges causes a stretching artifact near the edges of the frame

that is especially visible with objects moving through it or when the camera is moving.

Because of these artifacts, it is a good idea to use clamp edges only to correct small gaps around the

edges of an interpolated frame.

Edge Softness

This slider is displayed only when Clamp Edges is enabled. The slider helps to reduce the stretchy

artifacts that might be introduced by Clamp Edges.

If you have more than one of the Source Frame and Warp Direction checkboxes turned on, this

can lead to doubling up of the stretching effect near the edges. In this case, you’ll want to keep the

softness rather small at around 0.01. If you have only one checkbox enabled, you can use a larger

softness at around 0.03.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

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

These settings tweak the optical flow analysis. See the Classic and Advanced Controls section for the

Optical Flow node earlier in this chapter.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Optical Flow nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.