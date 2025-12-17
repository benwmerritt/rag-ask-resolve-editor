---
title: "Merge 3D [3Mg]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 350
---

# Merge 3D [3Mg]

The Merge 3D node

Merge 3D Introduction

The Merge 3D node is the primary node in Fusion that you use to combine separate 3D elements into

the same 3D environment.

For example, in a scene created with an image plane, a camera, and a light, the camera would not be

able to see the image plane and the light would not affect the image plane until all three objects are

introduced into the same environment using the Merge 3D node.

The Merge provides the standard transformation controls found on most nodes in Fusion’s

3D suite. Unlike those nodes, changes made to the translation, rotation, or scale of the Merge

affect all the objects connected to the Merge. This behavior forms the basis for all parenting in

Fusion’s 3D environment.

Inputs

The Merge node displays only two inputs initially, but as each input is connected a new input appears

on the node, assuring there is always one free to add a new element into the scene.

SceneInput[#]: These multicolored inputs are used to connect image planes, 3D cameras, lights,

entire 3D scenes, as well as other Merge 3D nodes. There is no limit to the number of inputs this node

can accept. The node dynamically adds more inputs as needed, ensuring that there is always at least

one input available for connection.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Basic Node Setup

The Merge 3D is the hub of a 3D composite. All elements in a 3D scene connect into a Merge 3D.

Multiple Merge 3D nodes can be strung together to control lighting or for neater organization. The last

Merge 3D in a string must connect to a Renderer 3D to be output as a 2D image.

Merge 3D with a connected Image Plane, FBX Mesh object, SpotLight, and camera

Inspector

Merge 3D controls

Controls Tab

The Controls tab is used only to pass through any lights connected to the Merge 3D node.

Pass Through Lights

When the Pass Through Lights checkbox is selected, lights are passed through the Merge into its

output to affect downstream elements. Normally, the lights are not passed downstream to affect the

rest of the scene. This is frequently used to ensure projections are not applied to geometry introduced

later in the scene.

Common Controls

Transform and Settings Tabs

The remaining controls for the Transform and Settings tabs are common to most 3D nodes. Their

descriptions can be found in “The Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Override 3D [3Ov]

The Override 3D node

Override 3D Node Introduction

The Override node lets you change object-specific options for every object in a 3D scene

simultaneously. This is useful, for example, when you wish to set every object in the input scene to

render as a wireframe. Additionally, this node is the only way to set the wireframe, visibility, lighting,

matte, and ID options for 3D particle systems and the Text 3D node.

Inputs

SceneInput: The orange Scene input accepts the output of a Merge 3D node or any node creating a

3D scene.

Basic Node Setup

The Override 3D node is frequently used in conjunction with the Replace Material node to produce

isolated passes. For example, in the node tree below, a scene branches out to an Override node that

turns off the Affected by Lights property of each node, then connects to a Replace Material node that

applies a Falloff shader to produce a falloff pass of the scene.

Override 3D connected to a Replace Material node


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Inspector

Override 3D controls

Controls Tab

The function of the controls found in the Controls tab is straightforward. First, you select the option

to override using the Do [Option] checkbox. That reveals a control that can be used to set the value

of the option itself. The individual options are not documented here; a full description of each can be

found in any geometry creation node in this chapter, such as the Image Plane, Cube, or Shape nodes.

Do [Option]

Enables the override for this option.

[Option]

If the Do [Option] checkbox is enabled, then the control for the property itself becomes visible.

The control values of the properties for all upstream objects are overridden by the new value.

Common Controls

Settings Tabs

The Settings tab includes controls common to most 3D nodes. Their descriptions can be found in “The

Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Point Cloud 3D [3PC]

The PointCloud 3D node

Point Cloud 3D Node Introduction

A Point Cloud is generally many null objects created by 3D tracking or modeling software.

When produced by 3D tracking software, the points typically represent each of the patterns tracked

to create the 3D camera path. These point clouds can be used to identify a ground plane and to orient

other 3D elements with the tracked image. The Point Cloud 3D node creates a point cloud either by

importing a file from a 3D tracking application or generating it when you use the Camera Tracker node.

NOTE: A null object is an invisible 3D object that has all the same transform properties of a

visible 3D object.

Inputs

The Point Cloud has only a single input for a 3D scene.

SceneInput: This orange input accepts a 3D scene.

Basic Node Setup

The Point Cloud 3D node is viewed and connected through a Merge 3D node, integrating it into the

larger 3D scene.

Point Cloud 3D connected and viewed through a Merge 3D


Fusion Page Effects | Chapter 89 3D Nodes

FUSION