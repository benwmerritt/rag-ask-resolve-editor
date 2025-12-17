---
title: "Basic Node Setup"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 377
---

# Basic Node Setup

The Glow node receives a 2D image like the MediaIn1 shown below. The output continues the node

tree by connecting to another 2D image-processing node or a Merge node.

A Glow node applied to a MediaIn1 node in DaVinci Resolve

Inspector

Glow controls

Controls Tab

The Controls tab contains all the primary controls necessary for customizing the glow operation.

A Color Scale section at the bottom of the Inspector can be used for tinting the glow.

Filter

Use this menu to select the method of Blur used in the filter. The selections are described below.

�Box: A simple but very fast Box filter.

�Bartlett: Bartlett adds a softer, subtler glow with a smoother drop-off but may take longer to

render than Box.

�Multi-box: Multi-box uses a Box filter layered in multiple passes to approximate a Gaussian shape.

With a moderate number of passes (e.g., four), a high-quality blur can be obtained, often faster

than the Gaussian filter, and without any ringing.

�Gaussian: Gaussian adds a soft glow, blurred by the Gaussian algorithm.

�Fast Gaussian: Fast Gaussian adds a soft glow, blurred by the Gaussian algorithm. This is the

default method.

�Blend: Blend adds a nonlinear glow that is evenly visible in the whites and blacks.

�Hilight: Hilight adds a glow without creating a halo in the surrounding pixels.

�Solarize: Solarize adds a glow and solarizes the image.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Color Channels (RGBA)

This filter defaults to operating on R, G, B, and A channels. Selective channel filtering is possible by

clicking each channel to make them active or inactive.

NOTE: This is not the same as the RGBA checkboxes found under the common controls. The

node takes these selections into account before it processes the image, so deselecting a

channel causes the node to skip that channel when processing, speeding up the rendering of

the effect. In contrast, the channel controls under the Common Controls tab are applied after

the node has processed.

Lock X/Y

When Lock X/Y is checked, both the horizontal and vertical glow amounts are locked. Otherwise,

separate amounts of glow may be applied to each axis.

Glow Size

Glow Size determines the size of the glow effect. Larger values expand the size of the glowing

highlights of the image.

Num Passes

Only available in Multi-box mode. Larger values lead to a smoother distribution of the effect, but also

increase render times. It’s good to find the line between desired quality and acceptable render times.

Glow

The Glow slider determines the intensity of the glow effect. Larger values tend to completely blow the

image out to white.

Clipping Mode

This option determines how edges are handled when performing domain-of-definition rendering.

This is profoundly important for nodes like Blur, which may require samples from portions of the image

outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition. If

the upstream DoD is smaller than the frame, the remaining area in the frame is treated as

black/transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that would normally be outside the upstream

DoD is treated as black/transparent.

Blend

The Blend slider determines the percentage of the affected image that is mixed with original image. It

blends in more of the original image as the value gets closer to 0.

This control is a cloned instance of the Blend slider in the Common Controls tab. Changes made to this

control are simultaneously made to the one in the common controls.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Apply Mode

Three Apply Modes are available when it comes to applying the glow to the image.

�Normal: Default. This mode simply adds the glow directly over top of the original image.

�Merge Under: Merge Under places the glow beneath the image, based on the Alpha channel.

Threshold mode permits clipping of the threshold values.

�Threshold: This control clips the effect of the glow. A new range slider appears. Pixels in the

glowed areas with values below the low value are pushed to black. Pixels with values greater than

high are pushed to white.

�High-Low Range Control: Available only in Threshold mode. Pixels in the glowed areas with

values below the low value are pushed to black. Pixels with values greater than high are

pushed to white.

Color Scale (RGBA)

These Scale sliders can be used to adjust the amount of glow applied to each color channel

individually, by tinting the glow.

By click and holding on the Pick button, then dragging the pointer over the viewer, you can select a

specific color from the image.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Blur nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Sharpen [Shrp]

The Sharpen node

Sharpen Node Introduction

The Sharpen node uses a convolution filter to enhance detail in an image overall or to an

individual channel.

Inputs

The two inputs on the Sharpen node are used to connect a 2D image and an effect mask that can limit

the area affected by the sharpen.

Input: The orange input is used for the primary 2D image for sharpening.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the sharpen to only those

pixels within the mask. An effect mask is applied to the tool after it is processed.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Basic Node Setup

The Sharpen node receives a 2D image like the MediaIn1 shown below. The output continues the

node tree by connecting to another 2D image-processing node or a Merge node.

A Sharpen node applied to a MediaIn1 node in DaVinci Resolve

Inspector

Sharpen controls

Controls Tab

The Controls tab contains all the primary controls necessary for customizing the sharpen operation.

Color Channels (RGBA)

This filter defaults to operating on R, G, B, and A channels. Selective channel filtering is possible by

clicking the channel buttons to make them active or inactive.

NOTE: This is not the same as the RGBA checkboxes found under the common controls. The

node takes these selections into account before it processes the image, so deselecting a

channel causes the node to skip that channel when processing, speeding up the rendering of

the effect. In contrast, the channel controls under the Common Controls tab are applied after

the node has processed.

Lock X/Y

This locks the X and Y Sharpen sliders together for symmetrical sharpening. This is checked

by default.

Amount

This slider sets the amount of sharpening applied to the image. When the Lock X/Y control is

deselected, independent control over each axis is provided.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Clipping Mode

This option determines how edges are handled when performing domain-of-definition rendering. This

is profoundly important for nodes like Blur, which may require samples from portions of the image

outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition. If the

upstream DoD is smaller than the frame, the remaining area in the frame is treated as black/

transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that would normally be outside the upstream

DoD is treated as black/transparent.

Blend

The Blend slider determines the percentage of the affected image that is mixed with original image. It

blends in more of the original image as the value gets closer to 0.

This control is a cloned instance of the Blend slider in the Common Controls tab. Changes made to this

control are simultaneously made to the one in the common controls.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Blur nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Soft Glow [SGlo]

The Soft Glow node

Soft Glow Node Introduction

The Soft Glow node is similar to the Glow node but performs additional processing of the image to

create a much softer, more natural glow.

This node is perfect for atmospheric haze around planets, skin tones, and simulating dream

like environments.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION