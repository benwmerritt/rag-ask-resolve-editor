---
title: "Color"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 383
---

# Color

A sub category of the Color tools in Fusion that gives you access to various color

processing tools.

Auto Gain [AG]

The Auto Gain node

Auto Gain Node Introduction

The Auto Gain node automatically adjusts the tonal range of an image, setting the darkest and

brightest pixels to user-selected values. By default, the darkest pixels get pushed to black, the

brightest pixels get pushed to white, and pixels in between get stretched to cover the tonal

range evenly.

This can be useful when compensating for variations in lighting, dealing with low-contrast images, or

visualizing the full color range of float images (although the viewer’s View Normalized Image option is

generally more suitable for this).

Inputs

The two inputs on the Auto Gain node are the input and effect mask.

Input: The orange input connects the primary 2D image for the auto gain.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the auto gain adjustment to

only those pixels within the mask. An effect mask is applied to the tool after the tool is processed.

Basic Node Setup

The Auto Gain node, like many 2D image-processing nodes, receives a 2D image like a Loader node

or the MediaIn1 shown below. The output continues the node tree by connecting to another 2D image-

processing node or a Merge node.

An Auto Gain node applied to a MediaIn1 node


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Inspector

Auto Gain controls

Controls Tab

The Controls tab contains the few primary controls necessary for customizing the AutoGain operation.

NOTE: Variations over time in the input image can cause corresponding variations in the

levels of the result. For example, if a bright object moves out of an otherwise dark shot, the

remaining scene gets suddenly brighter, as the remaining darker values get stretched to

white. This also applies to sudden depth changes when Do Z is applied; existing objects may

be pushed forward or backward when a near or far object enters or leaves the scene.

Do Z

Select the Do Z checkbox to apply the Auto Gain effect to the Z or Depth channels. This can be useful

for matching the ranges of one Z-channel to another, or to view a float Z-channel in the RGB values.

Range

This Range control sets the black point and white point in the image. All tonal values in the image

rescale to fit within this range.

EXAMPLE Create a horizontal gradient with the Background node. Set one color to dark gray

(RGB Values 0.2). Set the other color to light gray (RGB Values 0.8).

Add an Auto Gain node and set the Low value to 0.0 and the High value to 0.5. This causes

the brightest pixels to be pushed down to 0.5, and the darkest pixels get pushed to black.

The remainder of the pixel values scale between those limits.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Brightness Contrast [BC]

The Brightness Contrast node

Brightness Contrast Node Introduction

The Brightness Contrast node adjusts the gain, brightness, contrast, gamma, and saturation of

an image. The order of the controls represents the order in which the operations are applied. For

example, gamma gets applied before contrast but after gain. The Brightness Contrast is also reversible

using the Forward and Reverse buttons. So color corrections, once applied, can be reversed further

downstream.

For this to work best, image processing should operate in 32-bit floating point.

Inputs

The two inputs on the Brightness Contrast node are the input and effect mask.

Input: The orange input connects the primary 2D image for the brightness contrast.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the Brightness Contrast

adjustment to only those pixels within the mask. An effect mask is applied to the tool after the tool is

processed.

Basic Node Setup

The Brightness Contrast node, like many 2D image-processing nodes, receives a 2D image like a

Loader node or the MediaIn1 shown below. The output continues the node tree by connecting to

another 2D image-processing node or a Merge node.

A Brightness Contrast node applied to a MediaIn1 node


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Inspector

Brightness Control controls

Controls Tab

The Controls tab contains all the primary controls necessary for customizing the brightness, contrast

operations.

Color Channels (RGBA)

The filter defaults to operating on R, G, B, and A channels. Selective channel filtering is possible by

clicking each channel button to make them active or inactive.

NOTE: This is not the same as the RGBA checkboxes found under the common controls.

The node takes these selections into account before it processes the image, so deselecting a

channel causes the node to skip that channel when processing, speeding up the rendering of

the effect. In contrast, the channel controls under the Common Controls tab get applied after

the node has processed.

Gain

The gain slider is a multiplier of the pixel value. A Gain of 1.2 makes a pixel that is R0.5 G0.5 B0.4 into

R0.6 G0.6, B0.48 (i.e., 0.4 * 1.2 = 0.48) while leaving black pixels unaffected. Gain affects higher values

more than it affects lower values, so the effect is most influential in the midrange and top range of

the image.

Lift

While Gain scales the color values around black, Lift scales the color values around white. The pixel

values get multiplied by the value of this control. A Lift of 0.5 makes a pixel that is R0.0 G0.0 B0.0 into

R0.5 G0.5, B0.5 while leaving white pixels unaffected. Lift affects lower values more than it affects

higher values, so the effect is most influential in the midrange and low range of the image.

Gamma

Values higher than 1.0 raise the Gamma (mid-gray), whereas lower values decrease it. The effect of

this node is not linear, and existing black or white points are not affected at all. Pure gray colors are

affected the most.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Contrast

Contrast is the range of difference between the light to dark areas. Increasing the value of this slider

increases the contrast, pushing color from the midrange toward black and white. Reducing the contrast

causes the colors in the image to move toward midrange, reducing the difference between the darkest

and brightest pixels in the image.

Brightness

The value of the Brightness slider gets added to the value of each pixel in the image. This control’s

effect on an image is linear, so the effect is applied identically to all pixels regardless of value.

Saturation

Use this control to increase or decrease the amount of Saturation in the image. A saturation of 0 has

no color, reducing the image to grayscale.

Low and High

This range control is similar to the Gain control in some respects. If Low gets anchored at 0.0

and the High value gets reduced from 1.0, the effect is identical to increasing the gain. High values

get multiplied by the inverse of the high value. (e.g., if high is 0.75, each pixel is multiplied by

1/0.75, or 1.3333).

Leaving the high anchored at 1.0 and increasing the low is the same as inverting the image colors and

increasing the gain and inverting it back again. This pushes more of the image toward black without

affecting the whites at all.

Direction

Forward applies all values normally. Reverse effectively inverts all values.

Clip Black/White

The Clip Black and Clip White checkboxes clip out-of-range color values that can appear in an image

when processing in floating-point color depth. Out-of-range colors are below black (0.0) or above

white (1.0). These checkboxes have no effect on images processed at 8-bit or 16-bit per channel, as

such images cannot have out-of-range values.

Pre-Divide/Post-Multiply

Selecting the Pre-Divide/Post-Multiply checkbox causes the image pixel values to be divided

by the Alpha values before the color correction, and then re-multiplied by the Alpha value after

the correction.

This helps to prevent the creation of illegally additive images when color correcting images with

premultiplied Alpha channels.

Common Controls

Settings Tab

The Settings tab in the Inspector appears in other Color nodes. These common controls are described

in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION