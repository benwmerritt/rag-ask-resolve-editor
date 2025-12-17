---
title: "Chapter 111"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 450
---

# Chapter 111

Miscellaneous

Nodes

This chapter details miscellaneous nodes within Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Auto Domain [ADoD]������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2507

Change Depth [CD]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2509

Custom Tool [CT]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2510

Fields [FLDs]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2522

Frame Average [Avg]������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2524

Keyframe Stretcher [KfS]���������������������������������������������������������������������������������������������������������������������������������������������������������������� 2525

Run Command [Run]������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2528

Set Domain [DOD]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2531

Switch [Swi]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2533

Time Speed [TSpd]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2534

Time Stretcher [TSt]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2537

Wireless Link [Wire]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2541

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2542


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Auto Domain [ADoD]

The Auto Domain node

Auto Domain Node Introduction

The Auto Domain node automatically sets the image’s domain of definition (DoD) based on bounds

of the input image’s background Canvas color. It does not change the image’s physical dimensions.

Some EXR images come with optimized DoDs already set, but other formats do not. For formats other

than EXR, this node can speed up compositions by optimizing the DoD based on the content rather

than the frame’s dimensions.

For example, a CG character rarely takes up the entire frame of an image. With this type of image, the

Auto Domain node sets the DoD to a rectangular region by comparing image pixels with the Canvas

color. The Canvas color indicates what color the pixels are outside the DoD. By default, unless a

Canvas color is set using the Set Canvas Color node, the color is set to black. This default works well

when an image has a premultiplied alpha channel. The result is a DoD that encompasses the portion

of the clip that contains only the character. The DoD is updated on each frame to accommodate

changes, such as a character walking closer to the camera. However, if a clip does not contain an

alpha channel, the Set Canvas Color node can be used to define the Canvas color as solid alpha with

a color that matches the solid background.

For more detail on the Set Canvas Color node, see Chapter 94, "Color Nodes," in the

DaVinci Resolve Reference Manual, or Chapter 34 in the Fusion Reference Manual.

NOTE: The Domain of Definition is a bounding box that encompasses pixels that

have a nonzero value. The DoD is used to limit image-processing calculations and

speeds up rendering.

Inputs

The single input on the Auto Domain node is used to connect a 2D image and an effect mask, which

can be used to limit the blurred area.

Input: The orange input is used for the primary 2D image that is blurred.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the blur to only those pixels

within the mask.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Basic Node Setup

The example below assumes that the image does not contain an alpha channel but a CG character

rendered against a black background. This is common for different render passes like specular or

shadows, for example. The image is connected to a Set Canvas Color node, which sets the Canvas

color to black with a solid alpha. The Set Canvas Color then connects to the Auto Domain node, which

detects the pixels and sets the DoD. If the original image contained a premultiplied alpha channel,

the Set Canvas Color would not be needed, and the image could be connected directly into the Auto

Domain node.

An Auto Domain node automatically limits the area of image processing.

Inspector

The Auto Domain Controls tab

Controls Tab

In most cases, the Auto Domain node automatically calculates the DoD bounding box; however,

the rectangular shape can be modified using the Controls tab in the Inspector.

Left

Defines the left border of the search area of the ADoD. Higher values on this slider move the left

border toward the right, excluding more data from the left margin.

1 represents the right border of the image; 0 represents the left border. The slider defaults

to 0 (left border).

Bottom

Defines the bottom border of the search area of the ADoD. Higher values on this slider move the

bottom border toward the top, excluding more data from the bottom margin.

1 represents the top border of the image; 0 represents the bottom border. The slider defaults

to 0 (bottom border).

Right

Defines the right border of the search area of the ADoD. Higher values on this slider move the right

border toward the left, excluding more data from the right margin.

1 represents the right border of the image; 0 represents the left border. The slider defaults

to 1 (right border).


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Top

Defines the top border of the search area of the ADoD. Higher values on this slider move the top

border toward the bottom, excluding more data from the top margin.

1 represents the top border of the image; 0 represents the bottom border. The slider defaults

to 1 (top border).

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other miscellaneous nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.

Change Depth [CD]

The Change Depth node

Change Depth Node Introduction

The Change Depth node has one simple use, and that is to change the bits per color channel used

to process a node. This node is often used after color correcting 32-bit floating-point image files,

converting them from float processing to 16-bit per channel to preserve memory and performance.

It can also be useful if, from a certain point in your node tree, you feel the need to process your images

in a higher bit depth than their original one or to reduce the bit depth to save memory.

Inputs

The single input on the Change Depth node is used to connect a 2D image and an effect mask, which

can be used to limit the blurred area.

Input: The orange input is used for the primary 2D image to be converted.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes or bitmaps from other tools. Connecting a mask to this input limits the blur to only those pixels

within the mask.

Basic Node Setup

Below, a Loader node in Fusion Studio is color corrected and then down converted from a floating-

point image to a 16-bit image to save image-processing time and memory.

A Change Depth node placed after color correction is done on a floating-point image.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Inspector

The Change Depth Controls tab

Controls Tab

The two controls for this node are the Depth menu and the Dither menu. These two menus are used to

convert and adjust the color depth of the image.

Depth

The Keep setting doesn‘t do anything to the image but instead keeps the input depth. The other

options change the bit depth of the image to the respective value.

Dither

When down converting from a higher bit depth, it can be useful to add Error Diffusion or Additive

Noise to camouflage artifacts that result from problematic (high-contrast) areas.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other miscellaneous nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.

Custom Tool [CT]

The Custom Tool node

Custom Tool Node Introduction

The Custom Tool node is the most complex and the most powerful node in Fusion. It is used to create

custom expressions and filters to modify an image. In addition to providing three image inputs, the

Custom Tool node allows for the connection of up to eight numeric inputs and as many as four XY

position values from other controls and parameters in the node tree.

Per-pixel calculations can be performed on the Red, Green, Blue, Alpha, Z, Z-Coverage, UV texture

coords, XYZ Normals, RGBA background color, and XY motion vector channels of the images.

You should be moderately experienced with scripting, or C++ programming, to understand the

structure and terminology used by the Custom Tool node.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION