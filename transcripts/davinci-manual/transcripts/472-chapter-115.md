---
title: "Chapter 115"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 472
---

# Chapter 115

Position Nodes

This chapter details the Position nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Volume Fog [VLF]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2636

Volume Mask [VLM]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2643

Z to World Pos [Z2W]����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2648

WPP Concept��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2649

The Common Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2651


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

Volume Fog [VLF]

The Volume Fog node

Volume Fog Node Introduction

The Volume Fog node is used to create sophisticated volumetric fog on images containing XYZ

Position channels.

As opposed to 3D-rendered volumetric fog, it works on 2D images and delivers much faster results

and interactive feedback when setting up the fog. See the “WPP Concept” section at the end of this

chapter for further explanation of how this technology works and to learn about the required imagery.

Basic Node Setup

The Volume Fog node takes an image input; in the example below, it is a Renderer 3D with World

Position enabled in the output channels. Another input is the 3D scene, which contains the camera.

A Fast Noise node generates the fog texture.

Volume Fog Node Structure

A 3D scene and a rendered scene connected to Volume Fog

Inputs

The following inputs appear on the Volume Fog node in the Node Editor.

Image: The orange input accepts the primary image where the fog will be applied. This image contains

a World Position Pass in the XYZ Position channels.

Fog Image: The green Fog image input is for creating volumetric fog with varying depth and extent; a

2D image can be connected here. A good starting point is to use a Fast Noise at a small resolution of

256 x 256 pixels.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the fog to certain areas.

Scene Input: The magenta scene input accepts a 3D scene containing a 3D Camera.


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

Inspector

The Volume Fog Shape tab

Shape Tab

The Shape tab defines the size and location of the fog volume. You can either use the Pick buttons to

select the location and orientation in the viewer or use the Translation, Rotation, and Scale controls.

Shape

This menu switches between a basic spherical or rectangular volume to be placed in your image.

These volumes can then be further refined using the Fog image and effect mask.

Pick

Drag the Pick button into the viewer to select the XYZ coordinates from any 3D scene or 2D image

containing XYZ values, such as a rendered World Pass, to position the center of the Volume object.

When picking from a 2D image, make sure it’s rendered in 32-bit float to get full precision.

X, Y, Z Offset

These controls can be used to position the center of the fog volume manually or can be animated or

connected to other controls in Fusion.

Rotation Pick

Drag the Pick button into the viewer to select the rotational values from any 3D Scene or 2D image

containing those values, like an XYZ-Normal-Pass, to reorient the fog volume.

When picking from a 2D image, like an XYZ Normal pass, make sure it’s rendered in 32-bit float to get

full precision and accurate rotational values.

X, Y, Z Rotation

Use these controls to rotate the fog volume around its center.


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

X, Y, Z Scale

Scale the fog volume in any direction from its center to refine further the overall Size value

specified below.

Size

The overall size of the fog volume created.

Soft Edge

Controls how much the fog volume is faded toward the center from its perimeter to achieve a

softer look.

The Volume Fog Color tab

Color Tab

The Color tab controls the detail and color of the fog.

Adaptive Samples

Volumes images consist of multiple layers, so there may be 64 layers in a volume. This checkbox

adjusts the rendering algorithm for how to best blend those layers.

Dither: Applies a form of noise to improve the blending and hide visible layer differences.

Samples

Determines how many times a “ray” shot into the volume will be evaluated before the final image is

created. Not unlike raytracing, higher values lead to more detail inside the volume but also increase

render times.


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

Z Slices

The higher the Z Slices value, the more images from the connected Fog image sequence will be used

to form the depth of the volume.

You can, for example, use a Fast Noise with a high Seethe Rate to create such a sequence of images.

Be careful with the resolution of the images. Higher resolutions can require a large amount of memory.

As a rule of thumb, a resolution of 256 x 256 pixels with 256 Z Slices (i.e., forming a 256 x 256 x 256

cubic volume, which will use up to 256 MB for full color 32-bit float data) should give you a good

starting point.

First Slice Time

Determines which frame of the Global Range is used to deliver the first slice from the connected fog

image sequence.

Make sure that both Global In and Global Out, as well as the valid range of your source node, fall

within the range of First Slice Time + Z Slices.

Color

Allows you to modify the color of the fog generated. This will multiply over any color provided by the

connected Fog image.

Gain

Increases or decreases the intensity of the fog. More Gain will lead to a stronger glow and less

transparency in the fog. Lower values let the fog appear less dense.

Subtractive/Additive Slider

Similar to the Merge node, this value controls whether the fog is composed onto the image in Additive

or Subtractive mode, leading to a brighter or dimmer appearance of the fog.

Fog Only

This option outputs the generated fog on a black background, which then can be composited

manually or used as a mask on a Color Corrector for further refinement.

The Volume Fog Noise tab

Noise Tab

The Noise tab controls the shape and pattern of the noise added to the fog.


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

Detail

Increase the value of this slider to produce a greater level of detail in the noise result. Larger values

add more layers of increasingly detailed noise without affecting the overall pattern. High values take

longer to render but can produce a more natural result.

Gain

This control increases or decreases the brightest parts of the noise map.

Brightness

This control adjusts the overall brightness of the noise map, before any gradient color mapping is

applied. In Gradient mode, this produces a similar effect to the Offset control.

Translation

Use the Translation coordinate control to pan and move the noise pattern.

Noise Rotation

Use the Rotation controls to orient the noise pattern in 3D.

Seethe

Adjust this thumbwheel control to interpolate the noise map against a different noise map. This will

cause a crawling shift in the noise, like it was drifting or flowing. This control must be animated to

affect the noise over time.

Discontinuous

Normally, the Noise function interpolates between values to create a smooth, continuous gradient of

results. Enable this checkbox to create hard discontinuity lines along some of the noise contours. The

result will be a dramatically different effect.

Inverted

Select this checkbox to invert the noise, creating a negative image of the original pattern. This is most

effective when Discontinuous is also enabled.

The Volume Fog Camera tab

Camera Tab

For a perfect evaluation of a fog volume, a camera or 3D scene can be connected to the Scene input

of the node.

Camera

If multiple cameras are available in the connected Scene input, this menu allows the selection of the

correct camera needed to evaluate the fog volume. Instead of connecting a camera, position values

can be provided manually or by connecting the XYZ values to other controls.


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

Translation Pick

Drag the Pick button into the viewer to select XYZ coordinates from any 3D scene or 2D image

containing XYZ values, like a rendered World Pass, to define the center of the camera. When picking

from a 2D image, make sure it’s rendered in 32-bit float to get full precision.

X, Y, Z Offset

These controls can be used to define the center of the camera manually or can be animated or

connected to other controls in Fusion.

The Volume Fog Light tab

Light Tab

To utilize the controls in the Light tab, you must have actual lights in your 3D scene. Connect that

scene, including Camera and Lights, to the 3D input of the node.

Do Lighting

Enables or disables lighting calculations. Keep in mind that when not using OpenCL (i.e., rendering on

the CPU), these calculations may become a bit slow.

Do In-Scattering

Enables or disables light-scattering calculations. The volume will still be lit according to the state of the

Do Lighting checkbox, but scattering will not be performed.

Light Samples

Determines how accurate the lighting is calculated. Higher values mean more accurate calculation at

the expense of longer render times.


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

Density

This is similar to scattering in that it makes the fog appear thicker. With a high amount of scattering,

though, the light will be scattered out of the volume before it has had much chance to travel through

the fog, meaning it won’t pick up a lot of the transmission color. With a high density instead, the fog still

appears thicker, but the light gets a chance to be transmitted, thus picking up the transmission color

before it gets scattered out. Scattering is affected by the light direction when Asymmetry is not 0.0.

Density is not affected by light direction at all.

Scattering

Determines how much of the light bouncing around in the volume ends up scattering the light out of

the fog. If the light scatters more, or more accurately, then there’s a higher probability of the light being

scattered out of the volume, hence less light is left to continue through the fog. This option can make

the fog seem denser.

Asymmetry

Determines in what direction the light is scattered. A value of 0 produces uniform, or isotropic,

scattering, meaning all directions have equal probability. A value greater than 0 causes “forward

scattering,” meaning the light is scattered more into the direction of the light rays. This is similar to

what happens with water droplets in clouds. A value smaller than 0 produces “back scattering,” where

the light is more scattered back toward the original light source.

Transmission

Defines the color that is transmitted through the fog. The light that doesn’t get scattered out will tend

toward this color. It is a multiplier, though, so if you have a red light, but blue transmission, you won’t

see any blue.

Reflection

Changes the intensity of the light that is scattered out. Reflection can be used to modify the overall

color before Emission is added. This will be combined with the color channels of the volume texture

and then used to scale the values. The color options and the color channels of the volume texture

are multiplied together, so if the volume texture were red, setting the Reflection color options to blue

would not make the result blue. In such a case, they will multiply together to produce black.

Emission

This adds a bit of “glowing” to the fog, adding energy/light back into the calculation. If there are no

lights in the scene, and the fog emission is set to be 1.0, the results are similar to no lighting, like

turning off the Do Lighting option. Glowing can also be done while producing a different kind of look,

by having a Transmission greater than 1. This, however, would never happen in the real world.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Position nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

Examples

In these examples, we are looking at a volume from the outside. On the left, you see how the

Volume Fog looks with straight accumulation. That means the Do Lighting option is turned off.

On the right, you see the same volume with lighting/scattering turned on, and a single

point light.

Here, we have a slightly more complex Volume.

On the left with straight accumulation; in the middle with lighting, scattering, and a single point

light; and on the right, the light in the scene has been moved, which also influences the look of

the volume.