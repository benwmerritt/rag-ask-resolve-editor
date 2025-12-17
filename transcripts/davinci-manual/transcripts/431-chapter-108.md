---
title: "Chapter 108"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 431
---

# Chapter 108

Mask Nodes

This chapter details the Mask nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Bitmap Mask [Bmp]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2387

B-Spline Mask [BSp]������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2392

Ellipse Mask [Elp]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2396

Mask Paint [PnM]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2399

MultiPoly [MPly]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2402

Polygon Mask [Ply]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2404

Ranges Mask [RNG]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2409

Rectangle Mask [Rec]������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2414

Triangle Mask [Tri]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2417

Wand Mask [Wnd]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2420

The Common Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2424


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Bitmap Mask [Bmp]

The Bitmap node

Bitmap Mask Node Introduction

The Bitmap mask node allows images from the node tree to act as masks for nodes and effects.

Bitmap masks can be based on values from any of the color, Alpha, hue, saturation, luminance,

and auxiliary coverage channels of the image. Nodes can also be masked based on the Object ID

or Material ID of a 3D-rendered image (provided those channels were included when the file was

rendered).

The Bitmap mask node is not required for effect masks. For effects masks, the Common Settings

tab for the masked node displays controls to select which channel of the mask image is used to

create the mask.

However, Bitmap mask nodes may still be required to connect to other mask inputs on some nodes,

such as Garbage Mattes and Pre-Masks. Also, using a Bitmap mask node between the mask source

and the target node provides additional options that would not be available when connecting directly,

such as combining masks, blurring the mask, or clipping its threshold.

Inputs

The Bitmap mask node includes two inputs in the Node Editor.

Input: The orange input accepts a 2D image from which the mask will be created.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input combines the masks. How

masks are combined is handled in the Paint mode menu in the Inspector.

Basic Node Setup

The Bitmap mask node is not required for connecting an image into the effect mask input, but it does

provide options that are otherwise unavailable. It allows for selecting channels other than RGBA for the

mask, as well as softness and clipping. In the node tree below, the two Bitmap masks are combined

using a Paint menu located in the second Bitmap mask node, which allows you to add, subtract,

multiply, and perform other operations on the combined mask.

Bitmap nodes can be chained together for more advanced matte operations.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Inspector

Bitmap Mask controls

Controls Tab

The Controls tab is used to refine how the image connected to the orange input converts into the

Bitmap mask.

Show View Controls

The Show View Controls checkbox is used to enable/disable the display of the mask’s onscreen

controls in the viewer. Onscreen controls, including center position, polylines, angles, and others, do

not appear when this checkbox is disabled, even when the node is selected.

Level

The Level control sets the transparency level of the pixels in the mask channel. When the value is 1.0,

the mask is completely opaque (unless it has a soft edge). Lower values cause the mask to be partially

transparent. The result is identical to lowering the Blend control of an effect.

NOTE: Lowering the level of a mask lowers the values of all pixels covered by the mask in

the mask channel. For example, if a Circle mask is placed over a Rectangle mask, lowering

the level of the Circle mask lowers the values of all the pixels in the mask channel, even

though the Rectangle mask beneath it is still opaque.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Filter

This control selects the filtering algorithm used when applying Soft Edge to the mask.

�Box: This is the fastest method but at reduced quality. Box is best suited for minimal

amounts of blur.

�Bartlett: Otherwise known as a Pyramid filter, Bartlett makes a good compromise between speed

and quality.

�Multi-box: When selecting this filter, the Num Passes slider appears and lets you control the

quality. At 1 and 2 passes, results are identical to Box and Bartlett, respectively. At 4 passes and

above, results are usually as good as Gaussian, in less time and with no edge “ringing.”

�Gaussian: The Gaussian filter uses a true Gaussian approximation and gives excellent results, but

it is a little slower than the other filters. In some cases, it can produce an extremely slight edge

“ringing” on floating-point pixels.

Soft Edge

Use the Soft Edge slider to blur (feather) the mask, using the selected filter. Higher values cause

the edge to fade off well beyond the boundaries of the mask. A value of 0.0 creates a crisp, well-

defined edge.

Paint Mode

Connecting a mask to the effect mask input displays the Paint mode menu. The Paint mode is used

to determine how the incoming mask for the effect mask input and the mask created in the node

are combined.

�Merge: Merge is the default for all masks. The new mask is merged with the input mask.

�Add: The mask’s values add to the input mask’s values.

�Subtract: In the intersecting areas, the new mask values subtract from the input mask’s values.

�Minimum: Comparing the input mask’s values and the new mask, this displays the lowest

(minimum) value.

�Maximum: Comparing the input mask’s values and the new mask, this displays the highest

(maximum) value.

�Average: This calculates the average (half the sum) of the new mask and the input mask.

�Multiply: This multiplies the values of the input mask by the new mask’s values.

�Replace: The new mask completely replaces the input mask wherever they intersect. Areas that

are zero (completely black) in the new mask do not affect the input mask.

�Invert: Areas of the input mask that are covered by the new mask are inverted; white becomes

black and vice versa. Gray areas in the new mask are partially inverted.

�Copy: This mode completely discards the input mask and uses the new mask for all values.

�Ignore: This mode completely discards the new mask and uses the input mask for all values.

Invert

Selecting this checkbox inverts the entire mask. Unlike the Invert Paint mode, this checkbox affects all

pixels, regardless of whether the new mask covers them.

Fit Input

This menu is used to select how the image source is treated if it does not fit the dimensions of the

generated mask.

In the example below, a 720 x 576 image source (yellow) is used to generate a 1920 x 1080

mask (gray).


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Crop: If the image source is smaller than the generated mask, it will be placed according to

the X/Y controls, masking off only a portion of the mask. If the image source is larger than the

generated mask, it will be placed according to the X/Y controls and cropped off at the borders

of the mask.

Stretch: The image source will be stretched in X and Y to accommodate the full dimensions of

the generated mask. This might lead to visible distortions of the image source.

Inside: The image source will be scaled uniformly until one of its dimensions (X or Y) fits the

inside dimensions of the mask. Depending on the relative dimensions of the image source

and mask background, either the image source’s width or height may be cropped to fit the

respective dimensions of the mask.

Width: The image source will be scaled uniformly until its width (X) fits the width of the mask.

Depending on the relative dimensions of the image source and mask, the image source’s

Y dimension might not fit the mask’s Y dimension, resulting in either cropping of the image

source in Y or the image source not covering the mask’s height entirely.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Height: The image source will be scaled uniformly until its height (Y) fits the height of the

mask. Depending on the relative dimensions of the image source and mask, the image

source’s X-dimension might not fit the mask’s X-dimension, resulting in either cropping of the

image source in X or the image source not covering the mask’s width entirely.

Outside: The image source will be scaled uniformly until one of its dimensions (X or Y) fits the

outside dimensions of the mask. Depending on the relative dimensions of the image source

and mask, either the image source’s width or height may be cropped or not fit the respective

dimension of the mask.

Center X and Y

These controls adjust the position of the Bitmap mask.

Channel

The Channel menu determines the Channel of the input image used to create the mask. Choices

include the red, green, blue, and alpha channels, the hue, luminance, or saturation values, or the

auxiliary coverage channel of the input image (if one is provided).

Threshold Low/High

The Threshold range control can be used to clip the bitmap image. Increasing the low range control

will clip pixels below the specified value to black (0.0). Decreasing the high range control will force

pixels higher than the specified value to white (1.0).

Use Object/Use Material

This control has no effect unless the input image contains a Material or Object ID channel. When

toggled on, the Object ID and Material ID are used to create a mask based on the selected object or

material. When toggled off, the regular color channels will generate the mask.

Common Controls

Image and Settings Tabs

The Image and Settings tabs in the Inspector are also duplicated in other Mask nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION