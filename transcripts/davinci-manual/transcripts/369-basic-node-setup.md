---
title: "Basic Node Setup"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 369
---

# Basic Node Setup

The Reflection node can be the main shader for an object as it is in the example below, or it can be

used to feed the diffuse material input of a Ward, Blinn, Phong, or other material node. Usually, a

Sphere Map node is used as the source of the Reflect node’s reflection color input.

A Reflect node used to create a highly reflective surface of a Shape 3D node

Inspector

Reflect controls

Controls Tab

The Controls tab contains parameters for adjusting the reflective strength based on the orientation of

the object, as well as the tint color of the Reflect shader node.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Reflection

Reflection Strength Variability

This multi-button control can be set to Constant or By Angle for varying the reflection intensity,

corresponding to the relative surface orientation to the viewer. The following three controls are visible

only when this control is set to By Angle.

Glancing Strength

[By Angle] Glancing Strength controls the intensity of the reflection for those areas of the geometry

where the reflection faces away from the camera.

Face On Strength

[By Angle] Face On Strength controls the intensity of the reflection for those parts of the geometry that

reflect directly back to the camera.

Falloff

[By Angle] Falloff controls the sharpness of the transition between the Glancing and Face On Strength

regions. It can be considered similar to applying gamma correction to a gradient between the Face On

and Glancing values.

Constant Strength

[Constant Angle] This control is visible only when the reflection strength variability is set to Constant. In

this case, the intensity of the reflection is constant despite the incidence angle of the reflection.

Refraction

If the incoming background material has a lower opacity than 1, then it is possible to use

an environment map as refraction texture, and it is possible to simulate refraction effects in

transparent objects.

Separate RGB Refraction Indices

When this checkbox is enabled, the Refraction Index slider is hidden, and three sliders for adjusting

the refraction index of the Red, Green, and Blue channels appear in its place. This allows simulation of

the spectral refraction effects commonly seen in thick imperfect glass, for example.

Refraction Index

This slider controls how strongly the environment map is deformed when viewed through a surface.

The overall deformation is based on the incidence angle. Since this is an approximation and not a

simulation, the results are not intended to model real refractions accurately.

Refraction Tint

The refraction texture is multiplied by the tint color for simulating color-filtered refractions. It can be

used to simulate the type of coloring found in tinted glass, as seen in many brands of beer bottles,

for example.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Stereo Mix [3SMM]

The Stereo Mix node

Stereo Mix Node Overview

This node is used to swap the left and right material inputs. It is often used to output to the left and

right eye of the 3D Render.

Inputs

This node has two inputs that are both required for this node to work. Both inputs accept either a

2D image or a 3D material.

LeftMaterial: The orange left material input accepts a 2D image or a 3D material to be used as the

material for the left eye rendering. If a 2D image is used, it is converted to a diffuse texture map using

the basic material type.

RightMaterial: The green right material input accepts a 2D image or a 3D material to be used as the

material for the right eye rendering. If a 2D image is used, it is converted to a diffuse texture map using

the basic material type.

While the inputs can be either 2D images or 3D materials, the output is always a material.

Basic Node Setup

The Stereo Mix node can be used with either stereo images or materials. The example below shows

two images combined in the Stereo Mix node causing the output to be a stereo anaglyph material.

A Stereo Mix node used to combine left and right images into a single stereo material

Inspector

Stereo Mix controls


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Controls Tab

The Controls tab contains a single switch that swaps the left and right material inputs.

Swap

This option swaps both inputs of the node.

Material ID

This slider sets the numeric identifier assigned to this material. This value is rendered into the MatID

auxiliary channel if the corresponding option is enabled in the renderer.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Ward [3Wd]

The Ward node

Ward Node Introduction

The Ward node is a basic illumination material that can be applied to geometry in the 3D scene.

It describes how the object responds to light and provides multiple texture map inputs to allow fine

control over the diffuse, specular, and bump map components of the material.

Specifically, the Ward node is ideal for simulating brushed metal surfaces, as the highlight can

be elongated along the U or V directions of the mapping coordinates. This is known as an

anisotropic highlight.

The Ward node outputs a 3D Material that can be connected to the material inputs on any 3D

geometry node.

Inputs

There are six inputs on the Ward node that accept 2D images or 3D materials. These inputs control

the overall color and image used for the 3D object as well as controlling the color and texture

used in the specular highlight. Each of these inputs multiplies the pixels in the texture map by the

equivalently named parameters in the node itself. This provides an effective method for scaling parts

of the material.

Diffuse Material: The orange Diffuse material input accepts a 2D image or a 3D material to be used as

a main color and texture of the object.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Specular Color Material: The green Specular Color material input accepts a 2D image or a 3D material

to be used as a highlight color and texture of the object.

Specular Intensity Material: The magenta Specular Intensity material input accepts a 2D image or a

3D material to be used as an intensity map for the material’s highlights. When the input is a 2D image,

the Alpha channel is used to create the map, while the color channels are discarded.

Spread U Material: The white Spread U material input accepts a 2D image or a 3D material. The value

of the Spread U option in the node’s controls is multiplied against the pixel values in the material’s

Alpha channel.

Spread V Material: The white Spread V material input accepts a 2D image or a 3D material. The value

of the Spread V option in the node’s controls is multiplied against the pixel values in the material’s

Alpha channel.

Bump Map Material: The white Bump Map material input accepts only a 3D material. Typically, you

connect the texture into a Bump Map node, and then connect the Bump Map node to this input. This

input uses the RGB information as texture-space normals.

When nodes have as many inputs and some using the same color as this one does, it is often difficult

to make connections with any precision. Hold down the Option or Alt key while dragging the output

from another node over the node tile, and keep holding Option or Alt when releasing the left mouse

button. A small drop-down menu listing all the inputs provided by the node appears. Click on the

desired input to complete the connection.

Basic Node Setup

The Ward node is used to make a shiny glass surface and replace the 3D text material in the example

below. A diffuse color material comes from Reflect node, and the specular color is altered by a

gradient color Fast Noise node.

A Ward node used with a diffuse connection and specular color connection


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION