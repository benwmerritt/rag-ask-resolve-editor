---
title: "Lens Distort [Lens]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 519
---

# Lens Distort [Lens]

The Lens Distort node

Lens Distort Node Introduction

This node can be used to remove or add lens distortion in an image. The lens distortion in an image

depends on the lens, quality, number of elements, and many other factors.

One reason to remove lens distortion is to composite with an undistorted layer. For example,

compositing a 3D element over a distorted live-action layer will cause unwanted effects like straight

lines not matching up on the foreground and background. The resulting composite will not look

believable.

Inputs

The two inputs on the Lens Distort node are used to connect a 2D image and an effect mask, which

can be used to limit the distorted area.

Input: The orange input is used for the primary 2D image that is distorted.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the distortion to only those

pixels within the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

A simplified example below applies the Lens Distort in Undistort mode to the MediaIn1 live-action

layer, composites the 3D elements, and finally applies the Lens Distort at the end with the same

settings, but this time in Distort mode to get the original look and distortion back into the image.

Lens Distort applied on the live-action media at the beginning of the node tree, and once again at the end


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Inspector

The Lens Distort Controls tab

Controls Tab

The Controls tab presents various ways to customize or build the lens distortion model you want.

Camera Settings allow you to specify the camera used to capture the content.

Mode

Undistort removes the lens distortion to create a flattened image. Distort brings the original lens

distortion back into the image.

Edges

Determines how samples that fall outside the frame are treated.

�Canvas: Pixels outside the frame are set to the default canvas color. In most cases, this is black

with no alpha.

�Duplicate: Pixels outside the frame are duplicated. This results in “smeared” edges but is useful

when, for example, applying a blur because in that case black pixels would result in the unwanted

blurring between the actual image and the black canvas.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Clipping Mode

�Domain: Retains all pixels that might be moved out of the frame for later re-distorting.

�Frame: Pixels moved outside the frame are discarded.

Output Distortion Map

Outputs the location of pixels as a warped screen-coordinate map.

Camera Settings

The options known from the Camera 3D are duplicated here. They can either be set manually or

connected to an already existing Camera 3D.

Lens Distortion Model

Select the appropriate 3D Equalizer Lens Distortion model here: 3DE Classic Model, 3DE4

Anamorphic, 3DE4 Radial Fisheye, or 3DE4 Radial. Please consult the 3D Equalizer manual for further

explanation. The sliders in the 3DE Classic LD Model are most likely best suited for manually applying

(un)distortion, without having imported lens data.

Supersampling [HiQ]

Sets the number of samples used to determine each destination pixel. As always, higher

supersampling leads to higher render times. 1×1 bilinear is usually of sufficient quality, but with high

lens distortion near the edges of the lens, there are noticeable differences to higher settings.

Supersampling Mode [HiQ]

The type of sample done for each supersample. Nearest leads to a crisper but more aliased image.

Bi-Linear gives a blurrier result.

Load Distortion Data

Allows the user to load a Lens Distortion profile created, for example, by the 3D Equalizer.

How to Manually Determine Lens Distortion

In an ideal world, one would have exact lens parameters from each lens that was used during

the shoot, and one could use those values to undistort the image. However, in the real world,

those parameters have not been taken on set or don’t match. Another approach is to use

software like 3D Equalizer, which analyzes the footage and delivers a dataset that can be

imported into the Lens Distort node right away.

And finally, one could try to manually eyeball the amount of lens distortion using the control

sliders. To do that, one could either look for horizontal or vertical lines in the footage that

are supposed to be straight and straighten them out using the controls, or shoot a full-frame

checkerboard pattern on set as a reference.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Warp nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Perspective Positioner [PPn]

The Perspective Positioner node

Perspective Positioner Node Introduction

The Perspective Positioner is the complementary node to the Corner Positioner node. It “unpins” an

image by positioning corner points on a perspective distorted area, thereby removing the perspective

from the image. This function can also be used to wobble and warp the image by animating the points

over time.

Inputs

The two inputs on the Perspective Positioner node are used to connect a 2D image and an effect

mask, which can be used to limit the transformed area.

Input: The orange input is used for the primary 2D image that is transformed.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the transform to only those

pixels within the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

In the example below, the Perspective Positioner is used to unpin a perspective distorted area of the

MedianIn2 in order to paint on the flat texture. The MediaIn2 is then corner pinned back into place.

The Perspective Positioner and Corner Positioner do not concatenate, so some softness is introduced

with these nodes.

The Perspective Positioner unpins an image to paint on a texture map.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Inspector

The Perspective Positioner Controls tab

Controls Tab

The Controls tab contains parameters for selecting vector channels and controlling how much

distortion they apply to an image.

Mapping Type

The Mapping Type menu is used to select the type of transform used to distort the image. Bi-Linear

is available for support of older projects. Leaving this on Perspective is strongly suggested since the

Perspective setting maps the real world more accurately.

Corners X and Y

There are the four control points of the Perspective Positioner. Interactively drag these in the viewers

to position each corner of the image. You can refine their position using the Top, Bottom, Left, and

Right controls in the Inspector.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Warp nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Vector Distortion [Dst]

The Vector Distortion node

Vector Distortion Node Introduction

The Vector Distortion node distorts the main source image along the X- and Y-axis separately, based

on the vector channel data in the source image or vector channels from a second reference image.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION