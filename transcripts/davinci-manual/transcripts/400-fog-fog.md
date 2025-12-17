---
title: "Fog [Fog]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 400
---

# Fog [Fog]

The Fog node

Fog Node Introduction

The Fog node is used to create simulated fog effects on 3D-rendered images that contain a valid

Z-buffer channel. The fog can be placed in front of or behind various elements of a rendered image

based on the selected Z-channel planes.

Inputs

The Fog node includes three inputs: one for the main image with a Z channel, one for a blur image,

and another for an effect mask to limit the area where the depth blur is applied.

Input: This orange input is the only required connection. It accepts a 2D image that includes

a Z channel. The Z channel is used to determine the fog amount in different regions of the image.


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Blur Image: The green second image input connects an image that is used as the source of the fog.

If no image is provided, the fog consists of a single color. Generally, a noise map of some sort is

connected here.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines,

basic primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input

limits the fog to only those pixels within the mask. An effects mask is applied to the tool after the

tool is processed.

Basic Node Setup

The Fog node is typically placed after a Renderer 3D node. The Renderer 3D node must have Z-Depth

enabled in its output channels.

A Fog node added as a 2D post process after the Renderer 3D node

Inspector

Fog controls


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Controls Tab

The Controls tab includes parameters for adjusting the density and color of the fog.

Z-Buffer Near Plane and Far Plane

These controls are used to select the extents of the fog within the scene. To pick a value, drag the

Pick button to an area on the image being viewed where the plane is to be located.

The Near Plane is used to select the depth where the fog thins out to nothing. The Far Plane is used to

select the depth at which the fog becomes opaque.

Z Depth Scale

This option scales the Z-buffer values by the selected amount. Raising the value causes the distances

in the Z-channel to expand, whereas lowering the value causes the distances to contract. This is useful

for exaggerating the fog effect.

Fog Color

This option displays and controls the current fog color. Alpha adjusts the fog’s transparency value.

Fog Opacity

Use this control to adjust the opacity on all channels of the fog.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Pixel nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.

Shader [Shd]

The Shader node

Shader Node Introduction

The Shader node can control the lighting, reflection mapping, and 3D shading of elements in a

rendered image. The node relies on the presence of the normal map channel in a rendered image. If

this channel is not present, this node has no effect.

Inputs

The Shader node includes three inputs: one for the main image with normal map channels, one for a

reflection map, and another for an effect mask to limit the area where the depth blur is applied.

Input: This orange input is the only required connection. It accepts a 2D image that includes a

normals channel.


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Reflection Map Image: The green reflection map image input projects an image onto all elements in

the scene or to elements selected by the Object and Material ID channels in the Common Controls.

Reflection maps work best as 32-bit floating point, equirectangular formatted images

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits

the shader to only those pixels within the mask. An effects mask is applied to the tool after the

tool is processed.

Basic Node Setup

The Shader node is inserted after a 2D image that contains a Normals channel. Below, a Renderer

3D is used to add a Normals channel to an image. The Shader node uses the normals for refining the

surface appearance with a reflection map connected.

The Shader node using normals from a Renderer 3D and a reflection input

Inspector

Shader controls

Controls Tab

The Controls tab for the Shader node includes parameters for adjusting the overall surface reaction

to light sources. You can modify the ambient, diffuse, specular, and reflection properties of the image

connected to the orange image input.

Light Tab

The Controls tab includes parameters for basic lighting brightness and reflections.

Ambient

Ambient controls the Ambient color present in the scene or the selected object. This is a base level of

light added to all pixels, even in completely shadowed areas.


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Diffuse

This option controls the Diffuse color present in the scene or for the selected object. This is the normal

color of the object, reflected equally in all directions.

Specular

This option controls the Specular color present in the scene or for the selected object. This is the color

of the glossy highlights reflected toward the eye from a light source.

Reflection

This option controls the Reflection contribution in the scene or for the selected object. High levels

make objects appear mirrored, while low levels overlay subtle reflections giving a polished effect. It

has no effect if no reflection map is connected.

Reflection Type

This menu determines the type of reflection mapping used to project the image in the second input.

Screen: Screen causes the reflection map to appear as if it were projected on to a screen behind the

point of view.

Spherical: Spherical causes the reflection map to appear as if it were projected on to a huge sphere

around the whole scene.

Refraction: Refraction causes the reflection map to appear as if it were refracting or distorting

according to the geometry in the scene.

Equator Angle

Equator Angle controls the left to right angle of the light generated and mapped by the Shader node

for the scene or the selected object.

Polar Height

Polar Height controls the top to bottom angle of the light generated and mapped by the Shader node

for the scene or the selected object.

Shader tab controls


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Shader Tab

The Shader tab is used to adjust the falloff of the Diffuse and Specular light and the tint color of the

specular highlight.

Diffuse and Specular

When enabled, these checkboxes allow you to edit the Diffuse and/or Specular Shader curves in the

Shader spline window.

In and Out

These options are used to display and edit point values on the spline.

Specular Color

Use the Diffuse curve to manipulate the diffuse shading and the Specular curve to affect the specular

shading. Drag a box over several points to group-select them. Right-clicking displays a menu with

options for adjusting the spline curves.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Pixel nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.