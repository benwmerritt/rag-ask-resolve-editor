---
title: "Sphere Map [3SpM]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 374
---

# Sphere Map [3SpM]

The SphereMap node

Sphere Map Node Overview

The Sphere Map node can be used to create simulated environment mapping, also called reflection

mapping. Ray trace rendering a reflective scene can be very time consuming, but sphere map-

based reflection mapping can generate 360-degree reflections faster with little loss of accuracy. For

example, when creating a reflective environment, a sphere map is created, large enough to surround

the 3D object in your scene. The sphere is mapped with the environment you want reflected and

connected to the Reflection Color input on a Reflect node.

Inputs

The single image input on the Sphere Map node accepts a 2D image texture in an equirectangular

format (where the X-axis represents 0–360 degrees longitude, and the Y-axis represents –90 to +90

degrees latitude.)

ImageInput: The orange Image input accepts a 2D RGBA image. Preferably, this is an equirectangular

image that shows the entire vertical and horizontal angle of view up to 360 degrees.

Basic Node Setup

The Sphere Map node below is mapped with a spherical image to generate the environment reflected

on the Shape 3D. It is connected to the Reflection Color input on a Reflect node.

A Sphere Map node generates a reflective environment when connected to a Reflect node Reflection Color input.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Inspector

Sphere Map controls

Controls Tab

The Controls tab in the Inspector modifies the mapping of the image input to the sphere map.

Angular Mapping

Adjusts the texture coordinate mapping so the poles are less squashed and areas in the texture get

mapped to equal areas on the sphere. It turns the mapping of the latitude lines from a hemispherical

fisheye to an angular fisheye. This mapping attempts to preserve area and makes it easier to paint on

or modify a sphere map since the image is not as compressed at the poles.

Rotation

Offers controls to rotate the texture map.

Material ID

This slider sets the numeric identifier assigned to this material. This value is rendered into the MatID

auxiliary channel if the corresponding option is enabled in the renderer.

The node expects an image with an aspect ratio of 2:1. Otherwise, the image is clamped according to

the following rules:

�2 * width > height: The width is fitted onto the sphere, and the poles display clamped edges.

�2 * width < height: The height is fitted onto the sphere, and there is clamping about the 0-degree

longitude line.

Common Controls

Settings tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Sphere Map vs. Connecting the Texture to a Sphere Directly

You can connect an equirectangular texture map directly to a sphere instead of piping it through the

Sphere Map node first. This results in a different rendering if you set the start/end angle and latitude

to less than 360°/180°. In the first case, the texture is squashed. When using the Sphere Map node, the

texture is cropped. Compare:

Spherical mapping differences

NOTE: If you pipe the texture directly into the sphere, it is also mirrored horizontally. You can

change this by using a Transform node first.

Texture 2D [3Tx]

The Texture 2D node

Texture Node Overview

The Texture 2D node sets metadata of an image being used for a texture map. By default, an image

will be (0,0) to (1,1) UV, but that can be changed. The Texture node relies on the presence of U and V

Map channels in 3D rendered images. If these channels are not present, this node has no effect.

NOTE: Background pixels may have U and V values of 0.0, which set those pixels to the color

of the texture’s corner pixel. To restrict texturing to specific objects, use an effect mask based

on the Alpha of the object, or its Object or Material ID channel.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

For more information, see Chapter 78, “Understanding Image Channels,” in the DaVinci

Resolve Reference Manual, or Chapter 18 in the Fusion Reference Manual.

Inputs

Image Input: The orange image input expects a 2D image.

Basic Node Setup

The Texture 2D node below takes a 2D gradient from the Background node and sets the UV metadata

for it. The texture is then applied to the FBX geometry based on that metadata. If you have the option

to use the UV Map tool, it is recommended because it may be faster and has onscreen controls.

A Texture 2D node is used to set the 3D texture metadata for the input image.

Inspector

Texture 2D controls

Controls Tab

The Controls tab of the Inspector includes the following options.

U/V Offset

These sliders can be used to offset the texture along the U and V coordinates.

U/V Scale

These sliders can be used to scale the texture along the U and V coordinates.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Wrap Mode

If a texture is transformed in the texture space (using the controls below or the UV Map node), then

it’s possible that areas beyond the image borders will be mapped on the object. The Wrap Mode

determines how the image is applied in these areas.

�Wrap: This wraps the edges of the image around the borders of the image.

�Clamp: The color at the edges of the images is used for texturing. This mode is similar to the

Duplicate mode in the Transform node.

�Black: The image is clipped along its edges. A black color with Alpha = 0 is used instead.

�Mirror: The image is mirrored in both X and Y.

Texture Filtering Mode

The texture can be filtered differently depending on whether you are using the Software Renderer or

OpenGL renderer in the Renderer 3D node. Within the two render engines, you can choose between

high-quality anti-aliasing or low quality. The texture filtering mode provides different filtering options

for the two render engines and the two anti-aliasing settings.

�Nearest: The simplest filtering technique is very fast but can cause artifacts when scaling textures.

�Bilinear: A standard isotropic filtering technique for scaling textures into multiple resolutions.

Works well for magnification of textures.

�Trilinear: An extension of Bilinear filtering. Trilinear tends to be a better option when

scaling down textures

�Anisotropic: The highest-quality filtering method that takes the camera orientation and polygon

perspective into account.

�SAT: SAT (Summed Area Table) is a method of performing high-quality filtering, but it can require

more memory than other options. Works very well on smaller bitmaps.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Texture Transform [3TT]

The Texture Transform node

Texture Transform Node Overview

The Texture Transform node can be used to translate, rotate, and scale the UVW texture coordinates

of a 3D object. While the input can also be an image, the output is always a material.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION