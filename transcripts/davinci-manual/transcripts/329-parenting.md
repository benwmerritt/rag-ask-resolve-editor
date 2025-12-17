---
title: "Parenting"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 329
---

# Parenting

One of the many advantages of the node-based approach to 3D compositing is that parenting

between objects becomes implicit in the structure of a 3D node tree. The basis for all parenting is the

Merge3D node. If you’re careful about how you connect the different 3D objects you create for your

scene, you can use multiple Merge3D nodes to control which combinations of objects are transformed

and animated together, and which are transformed and animated separately.

For example, picture a scene with two spheres that are both connected to a Merge3D. The

Merge3D can be used to rotate one sphere around the other, like the moon around the earth. Then

the Merge3D can be connected to another Merge3D to create the earth and the moon orbiting

around the sun.

One Merge3D with two spheres parented to another

Merge3D and parenting using three connected spheres


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Here are the two simple rules of transforming parented Merge3D nodes:

�Transforms and animation applied to a Merge3D are also applied to all 3D objects connected

to that Merge3D node, including cameras, lights, geometry, and other merge nodes

connected upstream.

�Transforms and animation applied to upstream merge nodes don’t affect downstream

merge nodes.

Cameras

When setting up and animating a 3D scene, the metaphor of a camera is one of the most

comprehensible ways of framing how you want that scene to be rendered out, as well as animating

your way through the scene. Additionally, compositing artists are frequently tasked with matching

cameras from live-action clips, or matching cameras from 3D applications.

To accommodate all these tasks, Fusion provides a flexible Camera3D node with common camera

controls such as Angle of View, Focal Length, Aperture, and Clipping planes, to either set up your own

camera or to import camera data from other applications. The Camera3D node is a virtual camera

through which the 3D environment can be viewed.

A camera displayed with onscreen Transform controls in the viewer; the Focal Plane indicator is enabled in green

Cameras are typically connected and viewed via a Merge3D node; however, you can also connect

cameras upstream of other 3D objects if you want that camera to transform along with that object

when it moves.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Quickly Viewing a Scene Through a Camera

When you’ve added a camera to a scene, you can quickly view the scene “through the camera”

by setting up the following.

To view the scene through the camera:


Select the Merge3D node that the camera is connected to, or any node downstream of

that Merge3D.


Load the selected Merge3D or downstream node into a viewer.


Right-click on the axis label in the bottom corner of the viewer and choose the camera name.

The viewer’s frame may be different from the camera frame, so it may not match the true boundaries

of the image that will be rendered by the Renderer3D node. If there is no Renderer3D node added to

your scene yet, you can use Guides that represent the camera’s framing.

For more information about Guides, see Chapter 69, “Using Viewers.” in the DaVinci Resolve

Reference Manual or Chapter 7 in the Fusion Reference Manual.

Plane of Focus and Depth of Field

Cameras have a plane of focus, for when depth of field rendering is available. Here’s the procedure for

enabling depth of field rendering in your scenes.

To render depth of field in a 3D scene:


You must add a Renderer3D node at the end of your 3D scene.


Select the Renderer3D node, and set the Renderer Type to OpenGL Renderer.


Open the Accumulation Effects disclosure control that appears, and turn on the Enable

Accumulation Effects checkbox in the OpenGL render.

Turning on Enable Accumulation Effects enables additional depth of field controls

Turning on “Enable Accumulation Effects” exposes a Depth of Field checkbox along with Quality

and Amount of DoF Blur sliders that let you adjust the depth of field effect. These controls affect

only the perceived quality of the depth of field that is rendered. The actual depth of field that’s

generated depends solely on the setup of the camera and its position relative to the other 3D

objects in your scene.

When you select your scene’s Camera3D node to view its controls in the Inspector, a new Focal

Plane checkbox appears in the Control Visibility group. Turning this on lets you see the green focal

plane indicator in the 3D Viewer that lets you visualize the effect of the Focal Plane slider, which is

located in the top group of parameters in the Camera3D node’s Controls tab.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Turning on the Focal Plane checkbox in the Camera3D node

For more information about these specific camera controls, see Chapter 89, “3D Nodes,” in

the DaVinci Resolve Reference Manual or Chapter 29 in the Fusion Reference Manual.

Importing Cameras

If you want to match cameras between applications, you can import camera paths and positions

from a variety of popular 3D applications. Fusion is able to import animation splines from Maya and

XSI directly with their own native spline formats. Animation applied to cameras from 3ds Max and

LightWave are sampled and keyframed on each frame.

To import a camera from another application, do the following:


Select the camera in the Node Editor.


At the bottom of the Inspector, click the Import Camera button.


In the file browser, navigate to and select the scene that contains the camera you want to import.

A dialog box with several options will appear. When the Force Sampling checkbox is enabled,

Fusion will sample each frame of the motion, regardless of the format.

The Select Camera dialog

TIP: When importing parented or rigged cameras, baking the camera animation in the 3D

application before importing it into Fusion often produces more reliable results.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Lighting and Shadows

You can add light sources to a scene to create very detailed lighting environments and atmosphere.

There are four different types of lights you can use in 3D scenes: ambient, directional, point,

and spotlights.

Enabling Lighting in the Viewer

A scene without lights uses a default directional light, but this automatically disappears once you add a

3D light object. However, even when you add light objects to your scene, lighting and shadows won’t

be visible in the viewer unless you first enable lighting in the viewer contextual menu by right-clicking

anywhere within a viewer and choosing 3D Options > Lighting or Shadows to turn on one or both.

Enabling Lighting to Be Rendered

Lighting effects won’t be rendered in the Renderer3D node until the Enable Lighting and/or Shadows

checkboxes are checked in the Inspector.

The Lighting button under the viewer

NOTE: When lighting is disabled in either the viewer or final renders, the image will appear to

be lit by a 100% ambient light.

Cotrolling Lighting within Each 3D Object

All nodes that create or merge geometry also include lighting options that are used to choose how

each object is affected by light:

�Merge3D nodes have a Pass Through Lights checkbox that determines whether lights attached to

an upstream Merge3D node also illuminate objects attached to downstream Merge3D nodes.

�ImagePlane3D, Cube3D, Shape3D, Text3D, and FBXMesh3D nodes have a set of Lighting

controls that let you turn three controls on and off: Affected by Lights, Shadow Caster, and

Shadow Receiver.

3D objects have individual lighting controls that let you

control how each object interacts with light and shadows


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION