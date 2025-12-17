---
title: "Erode Dilate Node [ErDl]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 413
---

# Erode Dilate Node [ErDl]

The Erode Dilate node

Erode Dilate Node Introduction

The Erode Dilate node contracts or expands the image, depending on whether the Amount slider is

set to a negative or positive value.

Inputs

The Erode Dilate node includes two inputs: one for the main image and the other for an effect mask to

limit the area where the erode or dilate is applied.

Input: The orange input takes the RGBA channels from an image to calculate the custom filter.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

erode or dilate to only those pixels within the mask. An effects mask is applied to the tool after the tool

is processed.


Fusion Page Effects | Chapter 100 Filter Nodes

FUSION

Basic Node Setup

The Erode Dilate node is commonly used to contract or expand mattes. Below, a Luma Keyer is

connected to the Erode Dilate and passes the modified key to a Matte Control where it is embedded

into the image.

An Erode Dilate node placed after a Luma

Keyer to operate on a Matte Control

Inspector

Erode Dilate controls

Controls Tab

The Controls tab includes the main Amount slider that determines whether you are performing an

erode by entering a negative value or a dilate by entering a positive value.

Color Channels (RGBA)

The Erode Dilate node defaults to operating on R, G, B, and A channels. Selective channel editing is

possible by enabling or disabling the checkboxes beside each channel.

This is not the same as the RGBA checkboxes found under the Common Controls. The node takes

these controls into account before it processes. Deselecting a channel causes the node to skip that

channel when processing, speeding up the rendering of the effect. In contrast, the channel controls

under the Common Controls tab are applied after the node has processed.


Fusion Page Effects | Chapter 100 Filter Nodes

FUSION

Lock X/Y

The Lock X/Y checkbox is used to separate the Amount slider into amount X and amount Y, allowing a

different value for the effect on each axis.

Amount

A negative value for Amount causes the image to erode. Eroding simulates the effect of an

underexposed frame, shrinking the image by growing darker areas of the image so that they eat away

at brighter regions.

A positive value for Amount causes the image to dilate, similar to the effect of overexposing a camera.

Regions of high luminance and brightness grow, eating away at the darker regions of the image. Both

techniques eradicate fine detail in the image and tend to posterize fine gradients.

The Amount slider scale is based on the input image width. An amount value of 1 = image width. So, if

you want to erode or dilate by exactly 1 pixel on an HD image, you would enter 1/1920, or 0.00052083.

Common Controls

Settings Tab

The Settings tab controls are common to all Filter nodes, so their descriptions can be found in “The

Common Controls” section at the end of this chapter.

Filter Node [Fltr]

The Filter node

Filter Node Introduction

The Filter node contains several standard convolution filters, easily selectable from a list. This node

enables a variety of effects, from radically changing the look of an image to adding subtle randomly-

generated film grain. The Sobel and Laplacian settings are often used for edge detection.

Inputs

The Filter node includes two inputs: one for the main image and the other for an effect mask to limit

the area where the filter is applied.

Input: The orange input is used for the primary 2D image that gets the filter applied.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines,

basic primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input

limits the filter to only those pixels within the mask. An effects mask is applied to the tool after the

tool is processed.


Fusion Page Effects | Chapter 100 Filter Nodes

FUSION

Basic Node Setup

The Filter node can be inserted after an image, mask, or any node that needs a filter applied.

Below, it is used to create an edge matte, which is then used to mask the soft glow around the

keyed foreground.

A Filter node using the Sobel setting to extract an edge matte

Inspector

Filter controls

Controls Tab

The Controls tab is used to set the filter type, the channels the filter is applied to, and the amount it

blends with the original image.

Filter Type

The Filter Type menu provides a selection of filter types described below.

�Relief: This appears to press the image into metal, such as an image on a coin. The image appears

to be bumped and overlaid on gray.

�Emboss Over: Embosses the image over the top of itself, with adjustable highlight and shadow

height and direction.


Fusion Page Effects | Chapter 100 Filter Nodes

FUSION

�Noise: Uniformly adds noise to images. This is often useful for 3D computer-generated images

that need to be composited with live action, as it reduces the squeaky-clean look that is inherent

in rendered images. The frame number acts as the random generator seed. Therefore, the effect

is different on each frame and is repeatable.

�Defocus: This filter type blurs the image.

�Sobel: Sobel is an advanced edge detection filter. Used in conjunction with a Glow filter, it creates

impressive neon light effects from live-action or 3D-rendered images.

�Laplacian: Laplacian is a very sensitive edge detection filter that produces a finer edge than the

Sobel filter.

�Grain: Adds noise to images similar to the grain of film (mostly in the midrange). This is useful for

3D computer-generated images that need to be composited with live action as it reduces the

squeaky-clean look that is inherent in rendered images. The frame number acts as the random

generator seed. Therefore, the effect is different on each frame and is repeatable.

Color Channels (RGBA)

The Filter node defaults to operating on R, G, B, and A channels. Selective channel editing is possible

by enabling or disabling the checkboxes beside each channel.

Power

Values range from 1 to 10. Power proportionately increases the amount by which the selected filter

affects the image. This does not apply to the Sobel or Laplacian filter type.

Angle

This control has a range from 0 to 315 degrees and changes the effect in increments of 45 degrees.

This applies only to the Relief and Emboss filters.

Median

Depending on which Filter Type is selected, the Median control may appear. It varies the Median

filter’s effect. A value of 0.5 produces the true median result, as it finds the middle values. A value of

0.0 finds the minimums, and 1.0 finds the maximums. This applies to the Median setting only.

Seed

This control is visible only when applying the Grain or Noise filter types. The Seed slider can be used

to ensure that the random elements of the effect are seeded with a consistent value. The randomizer

always produces the same result, given the same seed value.

Animated

This control is visible only when applying the Grain or Noise filter types. Select the checkbox to cause

the noise or grain to change from frame to frame. To produce static noise, deselect this checkbox.

Common Controls

Settings Tab

The Settings tab controls are common to all Filter nodes, so their descriptions can be found in “The

Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 100 Filter Nodes

FUSION