---
title: "Bump Map [3Bu]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 371
---

# Bump Map [3Bu]

The Bump Map node

Bump Map Node Overview

The Bump Map node is used to convert a grayscale (height map) image into a bump map and takes an

input directly from a bump map created by the Create Bump Map node. The node outputs a material.

Inputs

The Bump Map node includes a single orange input for connecting a 2D image you want to use as the

bump map texture, or it can accept the output of the Create Bump Map node.

ImageInput: The orange Image input is used to connect a 2D RGBA image for the bump calculation or

an existing bump map from the Create Bump map node.

Basic Node Setup

The Bump Map node is connected to the Bump Map material input on any one of the material shader

nodes. Below, the example uses a Fast Noise node to generate an image that connects to the

Bump Map node. The output of the Bump Map node connects to the Bump Map material input on a

Ward node.

A Bump Map is connected to the Bump Map material input on a material node.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Inspector

Bump Map controls

Controls Tab

The Controls tab contains all parameters for modifying the input source and the appearance of

the bump map.

Source Image Type

Toggle between Height Map, which creates a bump map similar to the Create Bump Map node, and

Bump Map, which expects a bump map created by the Create Bump Map node.

Filter Size

A custom filter generates the bump information. The drop-down menu sets the filter size.

Height Channel

Sets the channel from which to extract the grayscale information.

Clamp Z Normal

Clips the lower values of the blue channel in the resulting bump texture.

Height Scale

Changes the contrast of the resulting values in the bump map. Increasing this value yields a more

visible bump map.

Texture Depth

Optionally converts the resulting bump map texture into the desired bit depth.

Wrap Mode

Wraps the image at the borders, so the filter produces correct result when using seamless tile textures.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Notes on Bump Maps

There is some confusion of terminology with bump mapping, depending on where you get your

information. Here are Fusion conventions:

Height Map

A grayscale image containing a height value per pixel

Bump Map

An image containing normals stored in the RGB channels used for

modifying the existing normals (usually given in tangent space)

Normals Map

An image containing normals stored in the RGB channels used for

replacing the existing normals (usually given in tangent or object space)


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Catcher [3Ca]

The Catcher node

Catcher Node Overview

The Catcher material is used to “catch” texture-mode projections cast from Projector 3D and Camera

3D nodes. The intercepted projections are converted into a texture map and applied by the Catcher

material to the geometry to which it is connected.

To understand the Catcher node, it helps to understand the difference between light-based

projections and texture-based projections. Choosing Light from the projection mode menu on the

Projector 3D or Camera 3D nodes simply adds the values of the RGB channels in the projected image

to the diffuse texture of any geometry that lies within the projection cone. This makes it impossible to

clip away geometry based on the Alpha channel of an image when using light mode projections.

Imagine a scenario where you want to project an image of a building onto an image plane as part of a

set extension shot. You first rotoscope the image to mask out the windows. This makes it possible to

see the geometry of the rooms behind the wall in the final composite. When this image is projected as

light, the Alpha channel is ignored, so the masked windows remain opaque.

By connecting the Catcher to the diffuse texture map of the material applied to the image plane,

and then switching the projection mode menu in the Projector 3D or Camera 3D node from Light or

Ambient Light mode to Texture mode, the projected image is applied as a texture map. When using

this technique for the example above, the windows would become transparent, and it would be

possible to see the geometry behind the window.

The main advantages of this approach over light projection are that the Catcher can be used to

project Alpha onto an object, and it doesn‘t require lighting to be enabled. Another advantage is that

the Catcher is not restricted to the diffuse input of a material, making it possible to project specular

intensity maps, or even reflection and refraction maps.

NOTE: The Catcher material requires a Projector 3D or Camera 3D node in the scene, set to

project an image in Texture mode on the object to which the Catcher is connected. Without

a projection, or if the projection is not set to Texture mode, the Catcher simply makes the

object transparent and invisible.

Inputs

The Catcher node has no inputs. The output of the node is connected to the diffuse color material

input of the Blinn, Cook Torrance, or other material node applied to the 3D geometry.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Basic Node Setup

The output of a Catcher node should be connected to the material input of your 3D geometry node.

A camera is set up as a proctor with an image connected to the camera’s image input. When the

camera is set to texture projection mode, the Catcher node is used to determine which geometry

receives the texture.

A Catcher node output is connected to the input of the geometry node that receives the texture projection

Inspector

Catcher controls

Controls Tab

The Options in the Controls tab determine how the Catcher handles the accumulation

of multiple projections.

Enable

Use this checkbox to enable or disable the node. This is not the same as the red switch in the upper-

left corner of the Inspector. The red switch disables the tool altogether and passes the image on

without any modification. The Enable checkbox is limited to the effect part of the tool. Other parts, like

scripts in the Settings tab, still process as normal.

Color Mode

The Color mode menu is used to control how the Catcher combines the light from multiple projectors.

It has no effect on the results when only one projector is in the scene. This control is designed

to work with the software renderer in the Renderer 3D node and has no effect when using the

OpenGL renderer.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Alpha Mode

The Alpha mode is used to control how the Catcher combines the Alpha channels from multiple

projectors. It has no effect on the results when only one projector is in the scene. This control is

designed to work with the software renderer in the Renderer 3D node and has no effect when using

the OpenGL renderer.

Threshold

The Threshold can be used to exclude certain low values from the accumulation calculation.

For example, when using the Median Accumulation mode, a threshold of 0.01 would exclude any pixel

with a value of less than 0.01 from the median calculation.

Restrict by Projector ID

When active, the Catcher only receives light from projectors with a matching ID. Projectors with a

different ID are ignored.

Material ID

This slider sets the numeric identifier assigned to this material. This value is rendered into the

MatID auxiliary channel if the corresponding option is enabled in the Renderer 3D node.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.