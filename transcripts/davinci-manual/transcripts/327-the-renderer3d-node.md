---
title: "The Renderer3D Node"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 327
---

# The Renderer3D Node

Every 3D node you add outputs a complete 3D scene. This is unlike most traditional 3D modeling and

animation programs, where all objects reside within a global scene environment. This means that the

scenes created by a Camera 3D node and an image plane are separate until they’re combined into the

same scene via a Merge3D node, which itself outputs a complete 3D scene. However, this 3D scene

data can neither be composited with other 2D images in your composition nor rendered out without

first being rendered within the node tree using a Renderer3D node.

To be more specific, 3D nodes that output 3D scenes cannot be connected directly to inputs that

require 2D images. For example, the output of an ImagePlane3D node cannot be connected directly

to the input of a Blur node, nor can the output of a Merge3D node be directly connected to a regular

Merge node. First, a Renderer3D node must be placed at the end of your 3D scene to render it into

2D images, which may then be composited and adjusted like any other 2D image in your composition.

Output of a Merge3D connected to a Renderer3D node to output 2D image data


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

The Renderer3D uses one of the cameras in the scene (typically connected to a Merge3D node) to

produce an image. If no camera is found, a default perspective view is used. Since this default view

rarely provides a useful angle, most people build 3D scenes that include at least one camera.

The image produced by the Renderer3D can be any resolution with options for fields processing,

color depth, and pixel aspect.

Software vs. GPU Rendering

The Renderer3D node lets you choose between using a software renderer or an OpenGL renderer,

trading off certain aspects of rendered image quality for speed, and trading off depth of field rendering

for soft shadow rendering, depending on the needs of a particular element of your composition. To

choose which method of rendering to use, there’s a Renderer Type pop-up menu in the Controls tab of

each Renderer3D node’s parameters in the Inspector. The default is Software Renderer.

The Renderer Type option in the Controls tab of a Renderer3D node

Software Renderer

The software renderer is generally used to produce the final output. While the software renderer is not

the fastest method of rendering, it has twin advantages. First, the software renderer can easily handle

textures much larger than one half of your GPU’s maximum texture size, so if you’re working with

texture images larger than 8K you should choose the software renderer to obtain maximum quality.

Second, the software renderer is required to enable the rendering of “constant” and “variable” soft

shadows with adjustable Spread, which is not supported by the OpenGL renderer. Soft shadows

are more natural, and they’re enabled in the Shadows parameters of the Controls tab of light nodes;

you can choose Sampling Quality and Softness type, and adjust Spread, Min Softness, and Filter

Size sliders. Additionally, the software renderer supports alpha channels in shadow maps, allowing

transparency to alter shadow density.

When the Renderer3D node “Renderer Type” drop-down is set to OpenGL Renderer, you cannot render

soft shadows or excessively large textures (left). When the Renderer3D node “Renderer Type” drop-

down is set to Software Renderer, you can render higher-quality textures and soft shadows (right).

OpenGL Renderer

The OpenGL renderer takes advantage of the GPU in your computer to render the image; the textures

and geometry are uploaded to the graphics hardware, and OpenGL shaders are used to produce the

result. This can produce high-quality images that can be perfect for final rendering, and can also be

potentially orders of magnitude faster than the software renderer, but it does pose some limitations


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

on some rendering effects, as soft shadows cannot be rendered, and the OpenGL renderer also

ignores alpha channels during shadow rendering, resulting in a shadow always being cast from the

entire object.

On the other hand, because of its speed, the OpenGL renderer exposes additional controls for

Accumulation Effects that let you enable depth of field rendering for creating shallow-focus effects.

Unfortunately, you can’t have both soft shadow rendering and depth of field rendering, so you’ll need

to choose which is more important for any given 3D scene you render.

Don’t Forget That You Can Combine Rendered Scenes in 2D

While it may seem like an insurmountable limitation that you can’t output both soft shadows

and depth of field using the same renderer, don’t forget that you can create multiple

3D scenes each using different renderers and composite them in 2D later on. Furthermore,

you can also render out auxiliary channels that can be used by 2D image processing nodes

such as AmbientOcclusion, DepthBlur, and Fog to create pseudo-3D effects using the

rendered images.

OpenGL UV Renderer

When you choose the OpenGL UV Renderer option, a Renderer3D node outputs an “unwrapped”

version of the textures applied to upstream objects, at the resolution specified within the Image tab of

that Renderer3D node.

A normally rendered 3D scene (left), and the same scene rendered

using the OpenGL UV Renderer mode of the Renderer3D node (right)

This specially output image is used for baking out texture projections or materials to a texture map for

one of two reasons:

�Baking out projections can speed up a render.

�Baking out projections lets you modify the texture using other 2D nodes within your composition,

or even using third-party paint applications (if you output this image in isolation as a graphics file)

prior to applying it back onto the geometry.

Suppose, for instance, that you have a scene on a street corner, and there’s a shop sign with a phone

number on it, but you want to change the numbers. If you track the scene and have standing geometry

for the sign, you can project the footage onto it, do a UV render, switch the numbers around with a

Paint node, and then apply that back to the mesh with a Texture2D.

The UV renderer can also be used for retouching textures. You can combine multiple DSLR still shots

of a location, project all those onto the mesh, UV render it out, and then retouch the seams and apply

it back to the mesh.

You could project tracked footage of a road with cars on it, UV render out the projection from the

geometry, do a temporal median filter on the frames, and then map a “clean” roadway back down.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Loading 3D Nodes into the Viewer

When you load a 3D node into the viewer, it switches to a 3D Viewer, which lets you pan, zoom, and

rotate the scene in 3D, making it easy to make adjustments in three dimensions.

The 3D Viewer

The interactive 3D Viewer is highly dependent on the computer’s graphics hardware, relying on

support from OpenGL. The amount of onboard memory, as well as the speed and features of your

workstation’s GPU, make a huge difference in the speed and capabilities of the 3D Viewer.

Displaying a node with a 3D output in any viewer will switch the display type to a 3D Viewer.

Initially, the contents of the scene will be displayed through a default perspective view.

A 3D Viewer’s default perspective view

To change the viewpoint, right-click in the viewer and choose the desired viewpoint from the ones

listed in the Camera submenu. A shortcut to the Camera submenu is to right-click on the axis label

displayed in the bottom corner of the viewer.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Right-click the Axis label of the viewer

to change the viewpoint

In addition to the usual Perspective, Front, Top, Left, and Right viewpoints, if there are cameras

and lights present in the scene as potential viewpoints, those are shown as well. It’s even possible

to display the scene from the viewpoint of a Merge3D or Transform3D by selecting it from the

contextual menu’s Camera > Other submenu. Being able to move around the scene and see it from

different viewpoints can help with the positioning, alignment, and lighting, as well as other aspects of

your composite.

The Perspective drop-down menu also shows cameras, lights,

and Merge3D and Transform3D nodes you can switch to.

Navigating the 3D View

For the most part, panning and scaling of the 3D Viewer uses the same controls as the 2D Viewer.

For more information about the options available in the 3D Viewer, see Chapter 69,

“Using Viewers.” in the DaVinci Resolve Reference Manual or Chapter 7 in the Fusion

Reference Manual.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

To pan in a 3D Viewer, do the following:

�Hold the middle mouse button and drag in the viewer.

To dolly (zoom) in the 3D Viewer, do one of the following:

�Hold down the middle and left mouse buttons and drag left or right in the viewer.

�Hold down the Command key and use your pointing device’s scroll control.

To rotate around the 3D Viewer, do the following:

�Hold down the Option key and middle-button-drag left and right in the viewer.

If you want to frame certain objects in the viewer:


Select the viewer you want to work in.


Do one of the following:

�Press Shift-F to Fit all objects in the viewer.

�Press F to Fit to selection (or Fit All if nothing is selected).

�Press D to Rotate the viewer to look at the center of the currently selected object without

moving the viewer’s position.

Furthermore, selecting a 3D node in the Node Editor also selects the associated object in the

3D Viewer.