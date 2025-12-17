---
title: "Chapter 154"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 623
---

# Chapter 154

Resolve FX

This section provides detailed explanations for each Resolve FX filter that’s

available on the Cut, Edit, Fusion, and Color pages.

For more information on how to apply and adjust Resolve FX on the Cut page,

see Chapter 31, “Video and Audio Effects in the Cut Page.”

For more information on how to apply and adjust Resolve FX on the Edit page,

see Chapter 47, “Editing, Adding, and Copying Effects and Filters.”

For more information on how to apply and adjust Resolve FX on the Fusion page,

see Chapter 84, “Using Open FX, Resolve FX, and Fuse Plugins.”

For more information on how to apply and adjust Resolve FX on the Color page,

see Chapter 151, “Using Open FX and Resolve FX.”

Contents

Catalogue of Resolve FX Filters������������������������������������������������������������������������������������������������������������������������������������������������ 3459

Show Legacy Resolve FX�������������������������������������������������������������������������������������������������������������������������������������������������������������� 3460

Aperture Diffraction (Studio Version Only)���������������������������������������������������������������������������������������������������������������������������� 3510


Resolve FX Overview | Chapter 154 Resolve FX

COLOR

Catalogue of Resolve FX Filters

DaVinci Resolve comes with a set of Resolve FX filters, many of which have been optimized for real

time playback. These are located within their own category in the Effects Library of the Cut, Edit, and

Fusion pages, and in the Open FX browser of the Color page. These effects (or filters) work just like

any other Open FX plugin.

Resolve FX are shown as icons depicting each specific filter. Hovering the mouse pointer

over the icon previews the filter in the Viewer, and moving the mouse pointer along the icon

previews the filter over the length of the clip.

Icons showing categorized Resolve FX filters

In addition to the different parameters built into each filter, every single Resolve FX filter has a Blend

parameter that mixes that filter’s effect against the original image. Each filter’s Blend parameter

appears at the bottom of that filter’s settings.

The Blend slider found in the parameters of every Resolve FX filter


Resolve FX Overview | Chapter 154 Resolve FX

COLOR

Show Legacy Resolve FX

Over time some Resolve FX are depreciated for various reasons, such as their functionality being

absorbed into another effect or being re-written completely. However, for working on projects

that may have used these older effects extensively, or if you’re just feeling nostalgic, you still have

access to them.

To show the Legacy Resolve FX:

Open the Effects tab and click on the Effects (3-dot) option menu. Then select

Show Legacy Resolve FX.

You can remove these effects from the list again by unchecking this setting.


Resolve FX Overview | Chapter 154 Resolve FX

COLOR

Chapter 155

Resolve FX Blur

The plugins in this category offer a wider variety of different blur methods than

those found in the Blur palette.

Contents

Box Blur�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3462

Directional Blur����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3462

Gaussian Blur�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3463

Lens Blur (Studio Version Only)��������������������������������������������������������������������������������������������������������������������������������������������������� 3463

Shape������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3463

Speed������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3464

Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3464

Mosaic Blur������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3465

Radial Blur��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3465

Zoom Blur���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3466


Resolve FX Overview | Chapter 155 Resolve FX Blur

COLOR

Box Blur

A variable quality blur that ranges from very low quality to very soft.

�Horizontal and Vertical Strength: These sliders let you adjust the width and height of blur.

�Same Horizontal/Vertical: This checkbox lets you adjust these parameters together or separately.

�Horizontal and Vertical Channel Adjustment: These sliders let you adjust the per channel

settings of the blur.

Red: Adjusts the blur of the Red channel relative to the overall blur.

Green: Adjusts the blur of the Green channel relative to the overall blur.

Blue: Adjusts the blur of the Blue channel relative to the overall blur.

Alpha: Adjusts the blur of the Alpha channel relative to the overall blur.

�Number of Iterations: Controls how smooth the resulting blur is, with 1 being the lowest and most

“boxy” level of quality and 6 being the highest and smoothest level of quality. At low iteration

values, box blurs can appear somewhat similar to lens blurs.

�Border Type: Lets you choose how the edges of the image are affected by this blur, options

include Black, Replicate, Reflect, and Wrap Around.

�Blur Alpha: Check this box to blur the Alpha channel along with the image’s content.

Directional Blur

A blur that’s constrained to a single angle.

�Blur Strength: How much blur you want.

�Blur Angle: The direction of blur.

�Blur Type: When Blur Type is set to Realistic, the blur effect emulates a photographic motion blur.

When set to Stylized, the blur effect is a simple and smooth digital blur.

�Symmetric Blur: When the Symmetric checkbox is turned on, the blur effect appears to be created

from both directions, with the result being more of a double-image that’s blurring along the blur

angle, simulating motion blur in a camera. When off, the blur effect appears to be moving in a

single direction, from the original position out along the blur angle.

�Channel Adjustment: Allows you to now set the strength of a blur in a specific channel, relative

to the strength of the overall blur.

Red: Adjusts the blur of the Red channel relative to the overall blur.

Green: Adjusts the blur of the Green channel relative to the overall blur.

Blue: Adjusts the blur of the Blue channel relative to the overall blur.

Alpha: Adjusts the blur of the Alpha channel relative to the overall blur.

�Border Type: Lets you choose how the edges of the image are affected by this blur; options

include Black, Replicate, Reflect, and Wrap Around.

�Blur Alpha: Check this box to blur the alpha channel along with the image’s content.


Resolve FX Overview | Chapter 155 Resolve FX Blur

COLOR