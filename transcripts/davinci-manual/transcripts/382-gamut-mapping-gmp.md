---
title: "Gamut Mapping [GMp]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 382
---

# Gamut Mapping [GMp]

The Gamut Mapping node

Gamut Mapping Node Introduction

The Color Space Transform node provides Gamut Mapping controls to accommodate workflows

where you need to transform one color space into another that has a dramatically larger or smaller

gamut. These controls are identical to those found in the Color Space Transform node’s Gamut

Mapping group and are similar to those found in the Color Management panel of the Project Settings.

Inputs

The two inputs on the Gamut Mapping node are the input and effect mask.

Input: The orange input connects the primary 2D image for the auto gain.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the adjustment to only

those pixels within the mask. An effect mask is applied to the tool after the tool is processed.

Basic Node Setup

The Gamut Mapping node, like many 2D image-processing nodes, receives a 2D image, such as a

Loader node or the MediaIn1 shown below. The output continues the node tree by connecting to

another 2D image-processing node or a Merge node.

A Gamut Map node applied to a MediaIn1 node


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Inspector

Gamut Mapping controls

Controls Tab

The Controls tab contains the primary controls necessary for adjusting the Gamut Limiter parameters.

Gamma

A pop-up menu lets you specify what type of gamma the clip is supposed to have, so set this to

whatever matches that image (this may match the Timeline Color Space, but it depends on how

you’re working).

Tone Mapping Method

Lets you enable tone mapping to accommodate workflows where you need to transform one color

space into another with a dramatically larger or smaller dynamic range, by automating an expansion or

contraction of image contrast in such a way as to give a pleasing result with no clipping.

�None: This setting disables Input DRT Tone Mapping. No tone mapping is applied to the Input

to Timeline Color Space conversion at all, resulting in a simple 1:1 mapping to the Timeline

Color Space.

�Clip: Hard clips all out-of-bounds values.

�Simple: Uses a simple curve to perform this transformation, compressing or expanding the

highlights and/or shadows of the timeline dynamic range to better fit the output dynamic range.

Note that the “Simple” option maps between approximately 5500 nits and 100 nits, so if you’re

mapping from an HDR source with more than 5500 nits to an SDR destination there may still be

some clipping of the highlights above 5500 nits.

�Luminance Mapping: Same as DaVinci, but more accurate when the Input Color Space of all your

media is in a single standards-based color space, such as Rec. 709 or Rec. 2020.

�DaVinci: This option tone maps the transform with a smooth luminance roll-off in the shadows and

highlights, and controlled desaturation of image values in the very brightest and darkest parts of

the image. This setting is particularly useful for wide-gamut camera media and is a good setting to

use when mixing media from different cameras.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

�Saturation Preserving: This option has a smooth luminance roll-off in the shadows and highlights

but does so without desaturating dark shadows and bright highlights, so this is an effective option

for colorists who like to push color harder. However, because over-saturation in the highlights

of the image can look unnatural, two parameters are exposed to provide some user-adjustable

automated desaturation.

Sat. Rolloff Start: Lets you set a threshold, in nits (cd/m2), at which saturation will roll off along with

highlight luminance. Beginning of the rolloff.

Sat. Rolloff Limit: Lets you set a threshold, in nits (cd/m2), at which the image will be totally

desaturated. End of the rolloff.

Max Input/Output Luminance

Adjusting the sliders allows you to specify the minimum and maximum luminance of the input image

in nits. Using these two sliders together, you can set which value from the Input Gamma is mapped to

which value of the Output Gamma.

Average Input Luminance

Used to compensate for large differences in the viewer’s state of visual adaptation when viewing a

bright image on an HDR display versus seeing that same image on an SDR display. For most “average”

images this setting works best set between 0–10. However, when you’re converting very bright

images (for example, a snow scene at noon), then using a higher value will yield more image detail

within the highlights.

Gamut Mapping Method

Accommodates workflows where you need to transform one color space into another with a

dramatically larger or smaller gamut by helping to automate an expansion or contraction of image

saturation in such a way as to give a pleasing and naturalistic result with no clipping. Choosing

Saturation Mapping lets you remap the saturation values of the image. It enables the Saturation Knee

and Saturation Max. controls.

�The Saturation Knee slider sets the image level at which saturation mapping begins. Below this

level, no remapping is applied. All saturation values from this level on up are remapped according

to the Saturation Max. slider. A value of 1.0 is maximum saturation in the currently selected output

color space.

�The Saturation Max. slider sets the new maximum level to which you want to either raise or

lower all saturation values that are above the Saturation Knee setting. A value of 1.0 is maximum

saturation in the currently selected output color space.

Advanced

�Apply Forward OOTF: Check this box to convert the image from scene referred to display referred

color management.

�Apply Inverse OOTF: Check this box to convert the image from display referred to scene referred

color management.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Revival

A sub category of the Color tools in Fusion that pertains to fixing common technical

errors with programs being finished, remastered, or restored.

Chromatic Aberration Removal [CAr]

The Chromatic Aberration

Removal node

Chromatic Aberration Removal Node Introduction

A node that lets you manually correct the slight color fringing that results from chromatic aberration in

a lens. Show Estimated Fringes checkboxes for the RGB channels display an “alignment guide” that

visually isolates each of the types of fringing against gray.

Inputs

The two inputs on the Chromatic Aberration Removal node are the input and effect mask.

Input: The orange input connects the primary 2D image for the auto gain.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the adjustment to only

those pixels within the mask. An effect mask is applied to the tool after the tool is processed.

Basic Node Setup

The Chromatic Aberration Removal node, like many 2D image-processing nodes, receives a 2D

image, such as a Loader node or the MediaIn1 shown below. The output continues the node tree by

connecting to another 2D image-processing node or a Merge node.

A Chromatic Aberration Removal node applied to a MediaIn1 node


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Inspector

Chromatic Aberration Removal controls

Controls Tab

The Controls tab contains the primary controls necessary for adjusting the Chromatic Aberration

Removal parameters.

Advanced Options

Advanced Options provide additional parameters for problem shots.

�Lens Center: Center X and Y parameters let you offset the center of the lens if you’re dealing with

a reframed and re-rendered shot.

�Stronger Correction: Shows the location of image features that resemble fringing.

Estimation Options

The Estimation Options are used solely to highlight and identify areas of fringing. They do not affect

the final output of the image. They only become available when one of the Show Estimated Fringes

boxes is checked in the Aberration Correction section.

�R/C, G/P, B/Y Balance: These tools adjust the incoming balance between their respective colors

to better identify hard to see fringing.

�Brightness: Magnifies the fringe indicators that are displayed when you turn on either of the

Estimated Fringes checkboxes.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Aberration Correction

These tools let you make manual adjustments to correct aberration issues.

�R/C, G/P, B/Y Scale: Adjust these sliders to eliminate the fringing from their respective colors.

�R/C, G/P, B/Y Edge: Adjusts to compensate for the difference in fringing due to the curvature of

the lens’ edges

�Show Estimated Fringes: Checking this box will show just the estimated fringes over a gray

background. It will also activate the Estimation Options sliders, which will let you further highlight

and identify areas of fringing.

This makes it easy to make manual adjustments to correct the problem, using the Scale and Edge

controls to individually adjust Red/Cyan, Green/Purple, and Blue/Yellow fringing.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION