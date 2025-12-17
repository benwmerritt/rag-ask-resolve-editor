---
title: "Fast Noise Texture [3FN]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 373
---

# Fast Noise Texture [3FN]

The Fast Noise Texture node

Fast Noise Texture Node Overview

The Fast Noise Texture node is the procedural resolution-independent version of the 2D Fast Noise

node. It creates a noise texture directly as a material for usage with 3D nodes. It offers a 3D volumetric

mode for creating seamless textures in conjunction with nodes providing UVW texture coordinates

(Similar to the UV Map 3D node set to XYZ-to-UVW or Camera).


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Inputs

The Fast Noise Texture node includes an optional input that can be used to connect a 2D image

or material.

SourceMaterial: The Source Materials input accepts a 2D image or a 3D material. The image is then

altered by the noise pattern.

Basic Node Setup

The Fast Noise Texture node below is used to generate a resolution-independent 3D texture for an

FBX imported model.

A Fast Noise Texture node generates a seamless texture, taking advantage of UVW coordinates.

Inspector

Fast Noise Texture controls

Controls Tab

The parameters of the Fast Noise Texture node control the appearance and, for 2D, the animation of

the noise.

Output Mode

�2D: Calculates the noise texture based on 2D texture coordinates (UV). This setting allows

smoothly varying the noise pattern with animation.

�3D: Calculates the noise texture based on 3D texture coordinates (UVW). Nodes like Shape 3D

automatically provide a third texture coordinate; otherwise, a 3D texture space can be created

using the UV Map node. The 3D setting does not support animation of the noise pattern.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Detail

Increase the value of this slider to produce a greater level of detail in the noise result. Larger values

add more layers of increasingly detailed noise without affecting the overall pattern. High values take

longer to render but can produce a more natural result (not all graphics cards support higher detail

levels in hardware).

Brightness

This control adjusts the overall Brightness of the noise map.

Contrast

This control increases or decreases the overall Contrast of the noise map. It can exaggerate the effect

of the noise.

Scale

The scale of the noise map can be adjusted using the Scale slider, changing it from gentle variations

over the entire image to a tighter overall texture effect. This value represents the scale along

the UV axis.

Scale Z

(3D only) The Scale Z value scales the noise texture along the W-axis in texture space. W represents a

direction perpendicular to the UV plane for a 3D texture map.

Seethe

(2D only) The Seethe control smoothly varies the 2D noise pattern.

Seethe Rate

(2D only) As with the Seethe control above, the Seethe Rate also causes the noise map to evolve

and change. The Seethe Rate defines the rate at which the noise changes each frame, causing an

animated drift in the noise automatically, without the need for spline animation.

Discontinuous

Normally, the noise function interpolates between values to create a smooth continuous gradient of

results. You can enable the Discontinuous checkbox to create hard discontinuity lines along some of

the noise contours. The result is a dramatically different effect.

Invert

Enable the Invert checkbox to invert the noise, creating a negative image of the original pattern. This is

most effective when Discontinuous is also enabled.

Material ID

This slider sets the numeric identifier assigned to this material. This value is rendered into the MatID

auxiliary channel if the corresponding option is enabled in the renderer.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Gradient 3D [3Gd]

The Gradient node

Gradient Node Overview

The Gradient 3D node is used to texture objects with a variety of gradient types. It offers many of the

same controls as the Background node. While it is not possible to transform the gradient directly in

3D space, it is orientable using the following nodes:

Texture Transform Node: The Texture Transform node can be used to adjust the mapping per pixel.

UV Map Node: The UV Map node can be used to adjust the mapping per vertex (use the XYZtoUVW

mode). This has onscreen controls, so you can see what the gradient is doing. Using this node is

recommended because it is faster to evaluate.

The gradient defaults to a linear gradient that goes from -1 to +1 along the Z-axis. All primitives in the

Shape 3D node can output a third texture coordinate for UVW mapping.

Inputs

The Gradient node has no Inputs. The output of the node is connected to a material input on

3D geometry.

Basic Node Setup

The Gradient 3D node below is used to generate a resolution-independent 3D texture for an

FBX imported model. Positioning in UVW space is easiest to do using a UV Map tool placed after

the geometry.

A Gradient 3D node generates a resolution-independent gradient texture positioned by the UV Map tool


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Inspector

Gradient 3D controls

Controls Tab

The Controls tab for the Gradient node control the pattern and colors used for the gradient texture.

Gradient Type

Determines the type or pattern used for the gradient.

Linear: A simple linear gradient.

Reflect: Based on the Linear mode, this gradient is mirrored at the middle of the

textured range.

Square: The gradient is applied using a square pattern.

Cross: Similar to the Reflect mode, but Cross uses two axes to apply the gradient.

Radial: The Radial mode uses a circular pattern to apply the gradient.

Gradient 3D modes

Gradient Bar

The Gradient control consists of a bar where it is possible to add, modify, and remove color stops of

the gradient. Each triangular color stop on the Gradient bar represents a color in the gradient. It is

possible to animate the color as well as the position of the point. Furthermore, a From Image modifier

can be applied to the gradient to evaluate it from an image.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Interpolation Space

The gradient is linearly interpolated from point to point in RGB color space by default. This can

sometimes lead to unwanted colors. Choosing another color space may provide a better result.

Scale

Allows sizing of the gradient.

Offset

Allows panning through the gradient.

Repeat

Defines how the left and right borders of the gradient are treated.

Once: When using the Gradient Offset control to shift the gradient, the border colors keep

their values. Shifting the default gradient to the left results in a white border on the left, while

shifting it to the right results in a black border on the right.

Repeat: When using the Gradient Offset control to shift the gradient, the border colors wrap

around. Shifting the default gradient to the left results in a sharp jump from white to black,

while shifting it to the right results in a sharp jump from black to white.

Ping Pong: When using the Gradient Offset control to shift the gradient, the border colors

ping-pong back and forth. Shifting the default gradient to the left results in the edge fading

from white back to black, while shifting it to the right results in the edge fading from black

back to white.

Gradients set to Once, Repeat, and Ping Pong

from top to bottom, respectively, and

shifting the gradient to the left

Sub Pixel

Determines the accuracy with which the gradient is created.

Material ID

This slider sets the numeric identifier assigned to this material. This value is rendered into the MatID

auxiliary channel if the corresponding option is enabled in the renderer.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION