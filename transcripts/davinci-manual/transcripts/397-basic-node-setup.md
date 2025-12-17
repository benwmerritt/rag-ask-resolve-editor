---
title: "Basic Node Setup"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 397
---

# Basic Node Setup

The dHoldout node receives the background media containing the deep image data. It then lets you

refine the depth boundaries of the foreground deep image to occlude the background.

dHoldout accepts deep image data from two sources and uses

the foreground source to occlude the background.

Inspector

dHolodout controls

Controls Tab

The Controls tab includes parameters for adjusting the amount of depth information to include or

exclude from occluding the background deep image.

�Compute Occluded Samples: Use this checkbox to remove samples from a semi-transparent

foreground input. Visible background pixels will be recolored as if they were seen through a

partially transparent foreground.

�Holdout Z Offset: This slider allows you to reposition the holdout depth samples forward or

backwards. Decreasing this value will push the holdout forward, whereas increasing the value will

have the opposite effect.

�Sample: Click and drag from the sample button into the viewer to choose a value.

�Holdout Center: This allows you to reposition the holdout along the the X and Y axis.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Image nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

dMerge [dMg]

The dMerge node

dMerge Node Introduction

This tool combines multiple data streams, merging their depth samples for seamless compositing.

This tool has numerous inputs similar to the merge 3D tool.

Inputs

The dMerge tool uses one background input and multiple foreground inputs.

Background: This orange input is connected from a node with deep image data that you want to use

for the background.

Foreground: The white foreground input is for connecting other deep image nodes that you want to

combine with the background. There can be multiple foreground inputs to this tool just by dragging

additional connections between the nodes.

Basic Node Setup

The dMerge node receives the background containing the deep image data. It then lets you merge

additional deep image nodes to combine the data.

dMerge accepts deep image data from multiple sources and combines them.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Image nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

dRecolor [dRc]

The dRecolor node

dRecolor Node Introduction

This tool combines Deep Image data with an RGB (multi-layer) image. This node has two inputs,

one for Deep/depth and the other for Color. Use this node to recolor Deep Image samples with 2D

RGB values

Inputs

The dRecolor tool uses two inputs, one for deep color images and the other for RGB images.

Depth: This orange input is connected from a node with deep image data that you want to recolor.

Color: The green input is for the RGB image that you want to use to combine the Depth input with.

Basic Node Setup

The dRecolor node receives media containing deep image data. It then lets you combine it with a

normal 2D image using the RGB input.

dRecolor accepts deep image data and lets you combine it with a 2D RGB image.

Inspector

dRecolor controls


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Controls Tab

The Controls tab includes parameters for blending the 2D RGB image into the background

deep image.

�Center X/Y: Reposition the 2D RGB image over the deep image.

�Target Input Alpha: Select this checkbox to enable the Alpha channel from the Color input,

influencing the transparency of deep samples. When this option is turned off, only RGB will be

used to recolor the deep image.

�Drop Input Zero Alpha: When this is enabled, pixels in the RGBA source with zero alpha are

ignored and won’t influence the deep image.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Image nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.

dResize [dRz]

The dResize node

dResize Node Introduction

This tool resizes a Deep Image’s width and height.

Inputs

The dResize tool uses a single input.

Image: This orange input is connected from a node with deep image data that you want to resize.

Basic Node Setup

The dResize node receives media containing deep image data. It then lets you resize it before passing

it onto the rest of the node tree..

dResize accepts deep image data and lets you resize it.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Inspector

dResize controls

Controls Tab

The Controls tab includes parameters for resizing the deep image.

�Width: Scales the image’s width.

�Height: Scales the image’s height.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Image nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.

dTransform [dXf]

The dTransform node

dTransform Node Introduction

This tool allows you to adjust spatial positioning of deep image data while preserving its depth

samples. You can scale and translate Deep Images, including the sample Z values.

Inputs

The dTransform tool uses a single input and an effect mask.

Image: This orange input is connected from a node with deep image data that you want to transform.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools.

Basic Node Setup

The dTransform node receives media containing deep image data. It then lets you transform it before

passing it onto the rest of the node tree.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

dTransform accepts deep image data and lets you transform it.