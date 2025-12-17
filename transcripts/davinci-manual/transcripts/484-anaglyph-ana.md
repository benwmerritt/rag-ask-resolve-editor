---
title: "Anaglyph [Ana]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 484
---

# Anaglyph [Ana]

The Anaglyph node

NOTE: The Anaglyph node is available only in Fusion Studio and DaVinci Resolve Studio.

Anaglyph Node Introduction

The Anaglyph node is used to create stereoscopic images by combining separate left eye and right

eye images. It is most commonly used at the end of a stereoscopic workflow to display or deliver the

final result.

Inputs

The three inputs on the Anaglyph node are the left eye input, right eye input, and effect mask.

Left Eye Input: The orange input is used to connect the 2D image representing the left eye in the

stereo comp.

Right Eye Input: The green input is used to connect the 2D image representing the right eye in the

stereo comp.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the stereoscopic creation to

only those pixels within the mask.

Basic Node Setup

The Anaglyph node is usually placed at the end of a stereoscopic node tree to display the final result.

When using separate images for the left and right eye, the left eye image is connected to the orange

input, and the right eye image is connected to the green input of the node. When using either

horizontally or vertically stacked images containing both left eye and right eye information, these only

connect to the orange input.

An Anaglyph node using separate left and right eye inputs


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

Inspector

The Anaglyph Controls tab

Controls Tab

Using the parameters in the Controls tab, the separate images are combined to create a

stereoscopic output.

Color Type Menu

The Color Type menu allows you to choose between different color encodings to fit your preferred

display device. To match your stereo glasses, you can choose between Red/Cyan, Red/Green, Red/

Blue, Amber/Blue, and Green/Magenta encoding; Red/Cyan is the most commonly used.

The Anaglyph Color Type menu

Method

In addition to the color used for encoding the image, you can also choose five different methods

from the Method menu: Monochrome, Half-color, Color, Optimized, and Dubois. These methods are

described below.

The Anaglyph Method menu


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

�Monochrome: Assuming you are using a Red/Cyan Color Type, the left eye contains the

luminance of the left image and is placed in the output of the red channel. The right eye contains

the luminance of the right image and is placed in the output green and blue channels.

�Half-Color: Assuming you are using a Red/Cyan Color Type, the left eye contains the luminance

of the left image and is placed in the output of the red channel. The right eye contains the color

channels from the right image that match the glasses’ color for that eye.

Monochrome

Half-Color

�Color: The left eye contains the color channels from the left image that match the glasses’ color

for that eye. The right eye contains the color channels from the right image that match the glasses’

color for that eye.

�Optimized: Used with red/cyan glasses, for example, the resulting brightness of what shows

through the left eye is substantially less than the brightness of the right eye. Using typical ITU-R

601 ratios for luminance as a guide, the red eye would give 0.299 brightness, while the cyan

eye would give 0.587+0.114=0.701 brightness—over twice as bright. The difference in brightness

between the eyes can produce what are referred to as retinal rivalry or binocular rivalry, which

can destroy the stereo effect. The Optimized method generates the right eye in the same fashion

as the Color method. The left eye also uses the green and blue channels but in combination with

increased brightness that reduces retinal rivalry. Since it uses the same two channels from each

of the source images, it doesn’t reproduce the remaining one. For example, 1.05× the green and

0.45× the blue channels of the left image is placed in the red output channel, and the green and

blue channels of the right image are placed in the output green and blue channels. Red from both

the left and right images is not used.

Color

Optimized


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

�Dubois: Images with fairly saturated colors can produce retinal rivalry with the Half-color, Color,

and Optimized methods because the color is visible in only one eye. For example, with red/

cyan glasses, a saturated green object looks black in the red eye, and green in the cyan eye.

The Dubois method uses the spectral characteristics of (specifically) red/cyan glasses and CRT

(Trinitron) phosphors to produce a better anaglyph and in the end, tends to reduce retinal rivalry

caused by such color differences in each eye. It also tends to reduce ghosting produced when

one eye ‘leaks’ into the other eye. The particular calculated matrix in Fusion is designed for red/

cyan glasses and isn’t available for other glasses types. Since it is also derived from CRT color

primaries, it may not give the best results with a common LCD (though it’ll still likely produce less

retinal rivalry and ghosting than the other methods).

Dubois

Swap Eyes

Allows you to swap the left and right eye inputs easily.

Horiz Stack

Takes an image that contains both left and right eye information stacked horizontally. These images

are often referred to as “crosseyed” or “straight stereo” images. You only need to connect that one

image to the orange input of the node. It then creates an image half the width of the original input,

using the left half of the original image for the left eye and the right half of the original image for the

right eye. Color encoding takes place using the specified color type and method.

Vert Stack

Takes an image that contains both left and right eye information stacked vertically. You only need to

connect that one image to the orange input of the node. It then creates an image half the height of the

original input, using the bottom half of the original image for the left eye and the top half of the original

image for the right eye. Color encoding takes place using the specified color type and method.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Stereo nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

Combiner [Com]

The Combiner node

NOTE: The Combiner node is available only in Fusion Studio and DaVinci Resolve Studio.

Combiner Node Introduction

The Combiner node takes two stereoscopic inputs and creates so-called “stacked images” with the

left and right eye, either side by side or on top of each other. Stereoscopic nodes are available only in

Fusion Studio and DaVinci Resolve Studio.

Inputs

The two inputs on the Combiner node are used to connect the two images that get combined in a

stacked stereo image.

Image 1 Input: The orange input is used to connect the 2D image representing the left eye in the

stereo comp.

Image 2 Input: The green input is used to connect the 2D image representing the right eye in the

stereo comp.

Basic Node Setup

Below, a left eye image and right eye image are connected to the Combiner node to create a single

stacked stereo image. It can be more efficient to render out the stacked stereo images as EXR files

than to generate the disparity on-the-fly.

Left and right eye images are connected into a Combiner node to generate a stacked stereo image.

Inspector

The Combiner Controls tab


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

Controls Tab

To stack the images, the left eye image is connected to the orange input, and the right eye image is

connected to the green input of the node.

Combine

The Combine menu provides three options for how the two images are made into a stacked

stereo image.

�None: No operation will take place. The output image is identical to the left eye input.

�Horiz: Both images will be stacked horizontally, or side-by-side, with the image connected to the

left eye input on the left. This will result in an output image double the width of the input image.

�Vert: Both images will be stacked vertically, or on top of each other, with the image connected

to the left eye input on the bottom. This will result in an output image double the height of the

input image.

�Layers: This exposes layer name fields, allowing you to rename the layers.

Swap Eyes

Allows you to easily swap the left and right eye input.

Add Metadata

Metadata is carried along with the images and can be added to the existing metadata using this

checkbox. To view Metadata, use the viewer’s SubView menu set to Metadata.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Stereo nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.