---
title: "Color Matrix [CMx]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 386
---

# Color Matrix [CMx]

The Color Matrix node

Color Matrix Node Introduction

The ColorMatrix allows a vast number of operations to modify values individually in the different

color channels.

Inputs

The Color Matrix node includes two inputs: one for the main image and the other for an effect mask.

Input: This orange input is the only required connection. It connects a 2D image that is adjusted by the

color matrix.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

color matrix adjustment to only those pixels within the mask. An effect mask is applied to the tool after

it is processed.

Basic Node Setup

The Color Matrix node, like many 2D image-processing nodes, receives a 2D image like a Loader

node or the MediaIn1 shown below. The output continues the node tree by connecting to another 2D

image-processing node or a Merge node.

A Color Matrix node applied to a MediaIn1 node

Inspector

Color Matrix controls


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Controls Tab

Color Matrix multiplies the RGBA channels based on the values entered in a 4 x 4 grid. The fifth

column/row is an Add column.

Update Lock

When this control is selected, Fusion does not render the node. This is useful for setting up each value

of the node, and then turning off Update Lock to render it.

Matrix

This defines what type of operation actually takes place. The horizontal rows define the output values

of the node. From left to right, they are R, G, B, A, and Add. The vertical columns define the input

values. From top to bottom, they are R, G, B, A, and Add. The Add column allows simple adding of

values to the individual color channels.

By default, the output values are identical to the input values.

�1.0 means 100% of the Red channel input is copied to the Red channel output.

�1.0 means 100% of the Green channel input is copied to the Green channel output.

�1.0 means 100% of the Blue channel input is copied to the Blue channel output.

�1.0 means 100% of the Alpha channel input is copied to the Alpha channel output.

Written as mathematical equations, the default settings of the matrix would appear as follows:

[R out] = 1 * [R in] + 0 * [G in] + 0 * [B in] + 0 * [A in] + 0

[G out] = 0 * [R in] + 1 * [G in] + 0 * [B in] + 0 * [A in] + 0

[B out] = 0 * [R in] + 0 * [G in] + 1 * [B in] + 0 * [A in] + 0

[A out] = 0 * [R in] + 0 * [G in] + 0 * [B in] + 1 * [A in] + 0

Invert

Enabling this option inverts the Matrix. Think of swapping channels around, doing other operations

with different nodes, and then copying and pasting the original ColorMatrix and setting it to Invert to

get your channels back to the original.

Example 1: Invert

If you want to do a simple invert or negative of the color values, but leave the Alpha channel

untouched, the matrix would look like this:

Color Matrix example

Observe the fact that we have to add 1 to each channel to push the inverted values back into the

positive numbers.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Let’s follow this example step by step by viewing the waveform of a 32-bit grayscale gradient.


The original grayscale.

Original Grayscale


RGB set to -1. The values get inverted but fall below 0.

RGB set to -1


Adding 1 to each channel keeps the inversion but moves the values back into a positive range.

Adding 1 to each channel


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Example 2: Brightness per Channel

This example influences the brightness of each channel individually. This subtracts 0.2 from the

red channel, adds 0.314 to the green channel, and adds 0.75 to the blue channel, while keeping

Alpha as it is.

Brightness per channel example

Example 3: Copying Values

You can also copy color values back and forth between individual channels. In this example, the red

channel contains the luminance values of the image based on thirds, and the green channel contains

the luminance values based on the proper black-and-white conversion method, whereas the blue

channel uses a third method based on getting more information from red and less from blue. The

blue channel’s brightness is also lowered by 0.1, and the Alpha channel is replaced with the original

blue channel.

Copying Values example

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Color Space [CS]

The Color Space node

Color Space Node Introduction

The Color Space node provides the ability to work on an image in a variety of alternate color space

formats. By default, Fusion uses the RGB color space, and most nodes and displays interpret the

primary channels of an image as Red, Green, and Blue.

Changing the color space from RGB causes most images to look odd, as Fusion’s viewers still interpret

the primary channels as Red, Green, and Blue. For example, viewing an image converted to YUV in

one of the viewers shows the Y channel as Red, the U channel as Green, and the V channel as Blue.

Several common elements of the Fusion interface refer to the RGB channels directly. The four buttons

commonly found on the Inspector’s Settings tab to restrict the effect of the node to a single color

channel are one example. When a conversion is applied to an image, the labels of these buttons

remain R, G, and B, but the values they represent are from the current color space. (For example,

Red is Hue, Green is Luminance, and Blue is Saturation for an RGB to HLS conversion. The Alpha value

is never changed by the color space conversion.)

Inputs

The Color Space node includes two inputs: one for the main image and the other for an effect mask.

Input: This orange input is the only required connection. It connects a 2D image that is converted by

the color space operation.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

color space adjustment to only those pixels within the mask. An effect mask is applied to the tool after

it is processed.

Basic Node Setup

The Color Space node, like many 2D image-processing nodes, receives a 2D image like a Loader or

the MediaIn1 shown below, processes the image, and then extends the node tree by connecting to

another 2D image-processing node or a Merge node.

A Color Space node applies a

conversion to a MediaIn1 node


Fusion Page Effects | Chapter 94 Color Nodes

FUSION