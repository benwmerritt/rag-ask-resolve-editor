---
title: "Inputs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 378
---

# Inputs

Like the Glow node, Soft Glow also has three inputs: an orange one for the primary image input, a blue

one for an effect mask, and a third white input for a Glow mask.

Input: The orange input is used for the primary 2D image for the soft glow.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the soft glow to only those

pixels within the mask. An effect mask is applied to the tool after it is processed.

Glow Mask: The Soft Glow node supports pre-masking using the white glow mask input. A Glow

pre-mask filters the image before applying the soft glow. The soft glow is then merged back over the

original image. This is different from a regular effect mask that clips the rendered result.

The Glow mask allows the soft glow to extend beyond the borders of the mask, while restricting the

source of the soft glow to only those pixels within the mask.

Glow masks are identical to effect masks in every other respect.

Basic Node Setup

The Soft Glow node receives a 2D image like the MediaIn1 shown below. The output continues the

node tree by connecting to another 2D image-processing node or a Merge node.

A Soft Glow node applied to a MediaIn1 node

Inspector

Soft Glow controls


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Controls Tab

The Controls tab contains all the primary controls necessary for customizing the soft glow operation.

A color scale section at the bottom of the Inspector can be used for tinting the soft glow.

Filter

Use this menu to select the method of Blur used in the filter. The selections are described below.

�Box: A simple but very fast Box filter.

�Bartlett: Bartlett adds a softer, subtler glow with a smoother drop-off but may take longer to

render than Box.

�Multi-box: Multi-box uses a Box filter layered in multiple passes to approximate a Gaussian shape.

With a moderate number of passes (e.g., four), a high-quality blur can be obtained, often faster

than the Gaussian filter and without any ringing.

�Gaussian: Gaussian adds a soft glow, blurred by the Gaussian algorithm. This is the

default method.

Color Channels (RGBA)

The filter defaults to operating on R, G, B, and A channels. Selective channel filtering is possible by

clicking the channel buttons to make them active or inactive.

NOTE: This is not the same as the RGBA checkboxes found under the common controls.

The node takes these selections into account before it processes the image, so deselecting a

channel causes the node to skip that channel when processing, speeding up the rendering of

the effect. In contrast, the channel controls under the Common Controls tab are applied after

the node has processed.

Threshold

This control is used to limit the effect of the soft glow. The higher the threshold, the brighter the pixel

must be before it is affected by the glow.

Gain

The Gain control defines the brightness of the glow.

Lock X/Y

When Lock X/Y is checked, both the horizontal and vertical glow amounts are locked. Otherwise,

separate amounts of glow may be applied to each axis of the image.

Glow Size

This amount determines the size of the glow effect. Larger values expand the size of the glowing

highlights of the image.

Num Passes

Available only in Multi-box mode. Larger values lead to a smoother distribution of the effect, but also

increase render times. It’s good to find the line between desired quality and acceptable render times.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Clipping Mode

This option determines how edges are handled when performing domain-of-definition rendering.

This is profoundly important for nodes like Blur, which may require samples from portions of the image

outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition.

If the upstream DoD is smaller than the frame, the remaining area in the frame is treated as

black/transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that would normally be outside the upstream

DoD is treated as black/transparent.

Blend

The Blend slider determines the percentage of the affected image that is mixed with original image.

It blends in more of the original image as the value gets closer to 0.

This control is a cloned instance of the Blend slider in the Common Controls tab. Changes made to this

control are simultaneously made to the one in the common controls.

Color Scale (RGBA)

These Scale sliders are used to adjust the amount of glow applied to each color channel individually,

by tinting the glow.

By click and holding on the Pick button, then dragging the pointer over the viewer, you can select a

specific color from the image.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Blur nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Unsharp Mask [UsM]

The Unsharp Mask node

Unsharp Mask Introduction

Unsharp masking is a technique used to sharpen only the edges within an image. This node is most

often used to correct for blurring and loss of detail in low-contrast images; for example, to extract

useful detail from long exposure shots of faraway galaxies.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

This filter extracts a range of frequencies from the image and blurs them to reduce detail. The blurred

result is then compared to the original images. Pixels with a significant difference between the original

and the blurred image are likely to be an edge detail. The pixel is then brightened to enhance it.

Inputs

The two inputs on the Unsharp Mask node are used to connect a 2D image and an effect mask for

limiting the effect.

Input: The orange input is used for the primary 2D image for the Unsharp Mask.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the Unsharp Mask to only

those pixels within the mask. An effect mask is applied to the tool after it is processed.

Basic Node Setup

The Unsharp Mask node receives a 2D image like the MediaIn1 shown below. The output continues

the node tree by connecting to another 2D image-processing node or a Merge node.

An Unsharp mask node applied to a MediaIn1 node

Inspector

Unsharp Mask controls

Controls Tab

The Controls tab contains all the primary controls necessary for customizing the

Unsharp Mask operation.

Color Channels (RGBA)

The filter defaults to operating on R, G, B, and A channels. Selective channel filtering is possible by

clicking the channel buttons to make them active or inactive.

NOTE: This is not the same as the RGBA checkboxes found under the common controls.

The node takes these selections into account before it processes the image, so deselecting a

channel causes the node to skip that channel when processing, speeding up the rendering of

the effect. In contrast, the channel controls under the Common Controls tab are applied after

the node has processed.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Lock X/Y

When Lock X/Y is checked, both the horizontal and vertical sharpen amounts are locked. Otherwise,

separate amounts of glow may be applied to each axis of the image.

Size

This control adjusts the size of blur filter applied to the extracted image. The higher this value, the

more likely it is that pixels are identified as detail.

Gain

The Gain control adjusts how much gain is applied to pixels identified as detail by the mask. Higher

values create a sharper image.

Threshold

This control determines the frequencies from the source image to be extracted. Raising the value

eliminates lower-contrast areas from having the effect applied.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Blur nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Vari Blur [VBl]

The Vari Blur node

Vari Blur Node Introduction

The Vari Blur node gives a true per-pixel variable blur, using a second image to control the amount of

blur for each pixel. It is somewhat similar in effect to the Depth Blur node but uses a different approach

for frequently cleaner results.

Inputs

There are two inputs on the Vari Blur node for the primary image: the blur map image, and an

effect mask.

Input: The gold image input is a required connection for the primary image you wish to blur.

Blur Image: The green input is also required, but it can accept a spline shape, text object, still image,

or movie file as the blur map image. Once connected, you can choose red, green, blue, Alpha, or

luminance channel to create the shape of the blur.

Effect Mask: The optional blue effect mask input expects a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

Vari Blur to only those pixels within the mask. An effect mask is applied to the tool after it is processed.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION