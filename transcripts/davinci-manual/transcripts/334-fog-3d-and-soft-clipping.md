---
title: "Fog 3D and Soft Clipping"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 334
---

# Fog 3D and Soft Clipping

The Fog3D node helps to create atmospheric depth cues.

Split screen with and without fog

The Fog3D node works well with depth of field and antialiasing supported by the OpenGL renderer.

Since it is not a post-processing node (like the VolumeFog node found in the Nodes > Position menu

or Fog node in Nodes > Deep Pixel), it does not need additional channels like Position or Z-channel

color. Furthermore, it supports transparent objects.

The SoftClip node uses the distance of a pixel from the viewpoint to affect opacity, allowing objects

to gradually fade away when too close to the camera. This prevents objects from “popping off”

should the camera pass through them. This is especially useful with particles that the camera may be

passing through.

Geometry nodes such as the Shape3D node use a Matte Objects checkbox to enable masking out

parts of the 3D scene. Effectively, everything that falls behind a matte object doesn’t get rendered.

However, matte objects can contribute information into the Z-channel and the Object ID channel,

leaving all other channels at their default values. They do not remove or change any geometry; they

can be thought of as a 3D garbage matte for the renderer.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Circle shape used as a Matte

object to see the floor

Matte Object Parameters

Opening the Matte disclosure control reveals the Is Matte option, which when turned on enables two

more options.

Matte parameters in the Shape3D node; enabling

Is Matte reveals additional options

�Is Matte

Located in the Controls tab for the geometry, this is the main checkbox for matte objects. When

enabled, objects whose pixels fall behind the matte object’s pixels in Z do not get rendered.

�Opaque Alpha

When the Is Matte checkbox is enabled, the Opaque Alpha checkbox is displayed. Enabling

this checkbox sets the alpha value of the matte object to 1. Otherwise the alpha, like the RGB,

will be 0.

�Infinite Z

When the Is Matte checkbox is enabled, the Infinite Z checkbox is displayed. Enabling this

checkbox sets the value in the Z-channel to infinite. Otherwise, the mesh will contribute normally

to the Z-channel.

Matte objects cannot be selected in the viewer unless you right-click in the viewer and choose

3D Options > Show Matte Objects in the contextual menu. However, it’s always possible to select

the matte object by selecting its node in the node tree.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Material and Object IDs

Most nodes in Fusion that support effect masking can use Object ID and Material ID auxiliary channels

to generate a mask. The parameters used to accomplish this are found in the Common Controls tab of

each node.

Material ID parameters in a Shape3D node’s Inspector controls

The Material ID is a value assigned to identify what material is used on an object. The Object ID is

roughly comparable to the Material ID, except it identifies objects and not materials.

Both the Object ID and Material ID are assigned automatically in numerical order, beginning with 1. It

is possible to set the IDs to the same value for multiple objects or materials even if they are different.

Override 3D offers an easy way to change the IDs for several objects. The Renderer will write the

assigned values into the frame buffers during rendering, when the output channel options for these

buffers are enabled. It is possible to use a value range from 0 to 65534. Empty pixels have an ID of

0, so although it is possible to assign a value of 0 manually to an object or material, it is not advisable

because a value of 0 tells Fusion to set an unused ID when it renders.

Object ID for ground plane and object

set to the same numeric value

World Position Pass

The World Position Pass, or WPP, is a render pass generated from 3D applications. Each pixel is

assigned the XYZ position where the pixel was generated in the world coordinates. So if the face from

which the pixel was derived in the scene sits at (0,0,0), the resulting pixel will have a Position value of

(0,0,0). If we visualize this as RGB, the pixel will be black. If a face sits at (1,0,0) in the original scene,

the resulting RGB pixel will be red. Due to the huge range of possible positions in a typical 3D scene,

and 7⁄8 of those possible positions containing negative coordinates, the Position channel is always

rendered in 32-bit float.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

A World Position Pass rendering of a scene with its center at (0,0,0) The actual image is on the left

3D Scene Input

Nodes that utilize the World Position channel are located under the Position category. VolumeFog and

Z to WorldPos require a camera input matching the camera that rendered the Position channels, which

can either be a Camera3D or a 3D scene containing a camera. Just as in the Renderer3D, you can

choose which camera to use if more than one are in the scene. The VolumeFog can render without

a camera input from the Node Editor if the world space Camera Position inputs are set to the correct

value. VolumeMask does not use a camera input. Nodes that support the World Position Pass, located

under the Position category, offer a Scene input, which can be either a 3D Camera or a 3D scene

containing a camera.

There are three Position nodes that can take advantage of World Position Pass data.

�Nodes > Position > Volume Fog

�Nodes > Position > Volume Mask

�Nodes > Position > Z to World

�The “Dark Box”

Empty regions of the render will have the Position channel incorrectly initialized to (0,0,0). To get the

correct Position data, add a bounding sphere or box to your scene to create distant values and allow

the Position nodes to render correctly.

Without a bounding mesh to generate Position values, the fog fills in the background incorrectly


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Point Clouds

The Point Cloud node is designed to work with locator clouds generated from 3D tracking software.

3D camera tracking software, such as SynthEyes and PF Track, will often generate hundreds or even

thousands of tracking points. Seeing these points in the scene and referencing their position in 3D and

screen space is important to assist with lining up live action and CG, but bringing each point in as an

individual Locator3D would impact performance dramatically and clutter the node tree.

Point cloud in the viewer

The Point Cloud node can import point clouds written into scene files from match moving or 3D

scanning software.

To import a point cloud, do the following:


Add the PointCloud3D node to your composition.


Click the Import Point Cloud button in the Control panel.


Browse to the scene file and select a cloud to import from the scene.

The entire point cloud is imported as one object, which is a significantly faster approach.

Finding, Naming, and Publishing Points

Many 3D trackers allow for the naming of individual tracking points, as well as setting tracking points

on points of interest. The Point Cloud 3D will quickly find these points and publish them. A published

point in the cloud can be used to drive the animation of other parameters.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

To find a point in the point cloud, do the following:


Right-click anywhere within a viewer.


Choose Find from the Point Cloud’s submenu in the contextual menu.


Type the name of the point and click OK.

Finding a point cloud using the viewer contextual menu

If a point that matches the name you entered is found, it will be selected in the point cloud and

highlighted yellow.

TIP: The Point Cloud Find function is a case-sensitive search. A point named “tracker15” will

not be found if the search is for “Tracker15”.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Renaming a Point in the Cloud

You can use the Point Cloud contextual menu to rename a selected point. This works only for a single

point. A group of points cannot be renamed.

Publishing a Point

If you want to use a point’s XYZ positions for connections to other controls in the scene, you can

publish the point. This is useful for connecting objects to the motion of an individual tracker. To publish

a point, right-click it and choose Publish from the contextual menu.

Publishing a point using the viewer contextual menu


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION