---
title: "Rays [CIR]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 405
---

# Rays [CIR]

The Rays node

Rays Node Introduction

Rays is a modified zoom blur effect that radiates through an object from a specified point.

Inputs

There are two inputs on the Rays node: one for the image and one for the effects mask.

Input: The orange input is used for the primary 2D image that gets the rays applied to it.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input restricts the rays to be within the

pixels of the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Rays node works best when the image or graphic connected to the orange input includes an

Alpha channel from which the rays emit.

Rays node set up to emit from a line of text

Inspector

Rays node controls

Controls Tab

The Controls tab contains all the primary controls necessary for customizing the rays.

Center X and Y

This coordinate control and related viewer crosshair set the center point for the light source.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Blend

Sets the percentage of the original image that’s blended with the light rays.

Decay

Sets the length of the light rays.

Weight

Sets the falloff of the light rays.

Exposure

Sets the intensity level of the light rays.

Threshold

Sets the luminance limit at which the light rays are produced.

Common Controls

Settings Tab

The Settings tab controls are common to all Effect nodes, so their descriptions can be found in the

“The Common Controls” section at the end of this chapter.

Shadow [SH]

The Shadow node

Shadow Node Introduction

Shadow is a versatile node used in the creation of a drop shadow, based on the Alpha channel in an

image. Optionally, a second image can be used as a depth matte to distort the shadow based on the

varying depth in a background image.

Input

The three inputs on the Shadow node are used to connect a 2D image that causes the shadow.

A depth map input and an effect mask can be used to limit the area where trails appear. Typically, the

output of the shadow is then merged over the actual background in the composite.

Input: The orange input is used for the primary 2D image with Alpha channel that is the source

of the shadow.

Depth: The green Depth map input takes a 2D image as its input and extracts a depth matte from a

selected channel. The light Position and Distance controls can then be used to modify the appearance

of the shadow based on depth.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the area where the shadow

appears. An effects mask is applied to the tool after the tool is processed.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

NOTE: The Shadow node is designed to create simple 2D drop shadows. Use a Spot Light

node and an Image Plane 3D node for full 3D shadow casting.

Basic Node Setup

Below, the Shadow node uses the output of an image with Alpha and connects to the foreground of a

Merge. The shadow is shown over the background input to the Merge.

A Shadow node is generated from the

MediaIn2 and shown over MediaIn1

Inspector

Shadow node controls


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Controls Tab

The Controls tab contains all the primary controls necessary for customizing the shadow appearance.

Shadow Offset

This control sets the X and Y position of the shadow. When the Shadow node is selected, you can also

adjust the position of the Shadow Offset using the crosshair in the viewer.

Softness

Softness controls how blurry the shadow’s edges appear.

Shadow Color

Use this control to select the color of the shadow. The most realistic shadows are usually not totally

black and razor sharp.

Light Position

This control sets the position of the light relative to the shadow-casting object. The Light Position is

only taken into consideration when the Light Distance slider is not set to infinity (1.0).

Light Distance

This slider varies the apparent distance of the light between infinity (1.0) and zero distance from the

shadow-casting object. The advantage of setting the Light Distance is that the resulting shadow is

more realistic-looking, with the further parts of the shadow being longer than those that are closer.

Minimum Depth Map Light Distance

This control is active when an image is connected to the shadow’s Depth Map input. The slider is used

to control the amount that the depth map contributes to the Light Distance. Dark areas of a depth map

make the shadow deeper. White areas bring it closer to the camera.

Z Map Channel

This menu is used to select which color channel of the image connected to the node’s Depth Map

input is used to create the shadow’s depth map. Selections exist for the RGB and A, Luminance, and

Z-buffer channels.

Output

This menu determines if the output image contains the image with shadow applied or the shadow only.

The shadow only method is useful when color correction, perspective, or other effects need to be

applied to the resulting shadow before it is merged back with the object.

Common Controls

Settings Tab

The Settings tab controls are common to all Effect nodes, so their descriptions can be found in “The

Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Trails [TRLS]

The Trails node

Trails Node Introduction

The Trails node is used to create a ghost-like after-trail of the image. This creates an interesting effect

when applied to moving images with an Alpha channel. Unlike a directional blur, only the preceding

motion of an image is displayed as part of the effect. Since the trail effect is based on an image buffer,

it requires you to play or activate the pre-roll for some number of frames before you see the effect.

Input

The two inputs on the Trails node are used to connect a 2D image and an effect mask that can be

used to limit the area where trails appear.

Input: The orange input is used for the primary 2D image that receives the trails applied.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the area where the trails

effect appears. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The output of an animated Text node is connected to the input of the Trails node. Trails are generated

based on the motion of the text. The Reset button must be pressed in the Inspector between each

preview, or the trails will accumulate.

A Trails node generates trails for the animation in the Text node


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION