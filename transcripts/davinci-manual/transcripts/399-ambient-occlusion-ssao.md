---
title: "Ambient Occlusion [SSAO]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 399
---

# Ambient Occlusion [SSAO]

The Ambient Occlusion node

Ambient Occlusion Node Introduction

Ambient Occlusion (AO) is the lighting caused when a scene is surrounded by a uniform diffuse

spherical light source. Think of the scene as being surrounded by a humongous sphere that uniformly

emits light from its surface. AO captures the low frequency lighting. It does not capture sharp shadows

or Diffuse or Specular lighting. So, AO is usually combined with Diffuse and Specular lighting to create

a full lighting solution.

The Ambient Occlusion node generates global lighting effects in 3D-rendered scenes as a post effect.

It quickly approximates computationally expensive ray-traced global illumination. Being a post effect, it

exposes similar aliasing issues like the Shader, Texture, and Volume Fog nodes. Hence, artifacts may

appear in certain situations.

Usage

The AO node rarely works out of the box, and requires some tweaking. The setup process involves

adjusting the Kernel Radius and Number Of Samples to get the desired affect.

The Kernel Radius depends on the natural “scale” of the scene. Initially, there might appear to be no

AO at all. In most cases, the Kernel Radius is too small or too big, and working values must be found.

Inputs

There are three inputs on the AO node. The standard effect mask is used to limit the AO effect. The

Input and Camera connections are required. If either of these is not supplied, the node does not

render an image on output.

Input: This orange input accepts a 2D RGBA image, Z-Depth, and Normals.

Camera: The green camera input can take either a 3D Scene or a 3D Camera that

rendered the 2D image.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

Ambient Occlusion to only those pixels within the mask. An effects mask is applied to the tool after the

tool is processed.

Basic Node Setup

The Ambient Occlusion node is typically placed after a Renderer 3D node. The Renderer 3D node

must have Z-Depth and Normals enabled in its output channels. The Camera3D that is rendered by the

Renderer3D node is then connected to the camera input on the AO node.


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Ambient occlusion as a 2D post process

Inspector

Ambient Occlusion controls

Controls Tab

The controls tab includes all the main controls for compositing with AO. It controls the quality and

appearance of the effect.

Output Mode

�Color: Using the Color menu option combines the incoming image with Ambient Occlusion applied.

�AO: This option outputs the pure Ambient Occlusion as a grayscale image. White corresponds

to regions in the image that should be bright, while black correspond to regions that should be

darker. This allows you to create a lighting equation by combining separate ambient/diffuse/

specular passes. Having the AO as a separate buffer allows creative freedom to combine the

passes in various ways.


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Kernal Type

To determine the AO, rays are cast from a point on the surface being shaded, outward to a large

enclosed sphere.

The AO factor is determined by the unoccluded rays that reach the sphere.

�Hemisphere: Rays are cast toward a hemisphere oriented to the surfaces normal. This option

is more realistic than Sphere and should be used unless there is a good reason otherwise. Flat

surfaces receive 100% ambient intensity, while other parts are darkened.

�Sphere: Rays are cast toward a sphere centered about the point being shaded. This option is

provided to produce a stylistic effect. Flat surfaces receive 50% ambient intensity, while other

parts are made darker or brighter.

Number of Samples

Increase the samples until artifacts in the AO pass disappear. Higher values can generate better

results but also increase render time.

Kernel Radius

The Kernel Radius controls the size of the filter kernel in 3D space. For each pixel, it controls how

far one searches in 3D space for occluders. The Filter Kernel should be adjusted manually for each

individual scene.

If made too small, nearby occluders can be missed. If made too large, the quality of the AO decreases

and the samples must be increased dramatically to get the quality back.

This value is dependent on the scene Z-depth. That means with huge Z values in the scene, the kernel

size must be large as well. With tiny Z values, a small kernel size like 0.1 should be sufficient.

Lift/Gamma/Tint

You can use the lift, gamma, and tint controls to adjust the AO for artistic effects.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Pixel nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.

TIP: Combining multiple AO passes with different kernel radii can produce better effects.


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

AO Tips and Limitations

Transparency/Translucency: AO is designed to work with opaque objects. There are known

limitations with transparent receivers and those with transparent occluders. You can work

around some of these limitations by splitting out the transparent/translucent objects into

separate scenes and only computing AO on the opaque objects.

Particles: Because of the transparency/translucency limitations, do not use AO on particles,

unless the particles are solid opaque geometry. Anti-aliased edges are another form of

transparency, so they also cause problems with AO.

Supersampling: To render anti-aliasing with Ambient Occlusion, enable HiQ for the Z and

Normals pass in the Renderer 3D.

Viewer Dependence: AO methods work in viewer space, and the results are viewer

dependent. This means the amount of darkening can vary depending on the view location,

when in reality it should be constant. If at a point on an object the AO is 0.5, moving the

camera could change it to 0.4.

Baking of AO: The OpenGL UV renderer can be used to bake AO into the textures on models.

Depth Blur [DBl]

The Depth Blur node

Depth Blur Node Introduction

The Depth Blur node is primarily used to create focal length or depth-of-field effects. It blurs

3D-rendered images based on included Z-channel values, and can also be used for general per-pixel

blurring effects through the Blur Channel controls.

Inputs

The Depth Blur node includes three inputs: one for the main image, one for a blur image, and another

for an effect mask to limit the area where the depth blur is applied.

Input: This orange input is the only required connection. It accepts a 2D image that includes

a Z channel. The Z channel is used to determine the blur amount in different regions of the image.

Blur Image: If the Blur Image input is connected, channels from the image are used to control the blur.

This allows general 2D per-pixel blurring effects.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines,

basic primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input

limits the depth blur to only those pixels within the mask. An effects mask is applied to the tool after

the tool is processed.


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Basic Node Setup

The Depth Blur node receives the image containing the Z channel. Below, the Z depth channel is

provided in a separate image file and combined with the RGB (beauty) image using a Channels

Booleans tool. Channel Booleans sets the Z buffer channel to copy into the luminance foreground.

Depth Blur is applied to the beauty image based on a Z depth channel

Inspector

Depth Blur controls

Controls Tab

The Controls tab includes parameters for adjusting the amount of blur applied and the depth of the

blurred area. It also includes options for selecting channels other than the Z channel for the blur map.

Filter

This menu selects the filter used for the blur.

�Box: This applies a basic depth-based box blur effect to the image.

�Soften: This applies a depth-based general softening filter effect.

�Super Soften: This applies a depth-based high-quality softening filter effect.

Blur Channel

Select one of these options to determine the channel used to control the level of blur applied to each

pixel. The channel from the main image input is used, unless an image is connected to the node’s

green Blur Image input.

Lock X/Y

When toggled on, this control locks the X and Y Blur sliders together for symmetrical blurring.


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Blur Size

This slider is used to set the strength of the horizontal and vertical blurring.

Focal Point

This control is visible only when the Blur channel menu is set to use the Z channel.

Use this control to select the distance of the simulated point of focus. Lowering the value causes the

Focal Point to be closer to the camera; raising the value causes the Focal Point to be farther away.

Depth of Field

This control is used to determine the depth of the area in focus. The focal point is positioned in the

middle of the region, and all pixels with a Z-value within the region stay in focus. For example, if the

focal point were selected from the image and set to a value of 300, and the depth of field is set to 200,

any pixel with a Z-value between 200 and 400 would remain in focus.

Z Scale

Scales the Z-buffer value by the selected amount. Raising the value causes the distances in the

Z-channel to expand. Lowering the value causes them to contract. This is useful for exaggerating the

depth effect. It can also be used to soften the boundaries of the blur. Some images with small depth

values may require the Z-scale to be set quite low, below 1.0.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Pixel nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.