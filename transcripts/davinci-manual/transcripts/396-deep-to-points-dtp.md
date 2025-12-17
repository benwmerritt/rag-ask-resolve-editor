---
title: "Deep to Points [DtP]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 396
---

# Deep to Points [DtP]

The Deep to Points node

Deep to Points Node Introduction

This tool converts Deep images into a 3D point cloud. This tool is useful for visualizing depth samples

and offers a way to see elements in Z when incorporating elements.

Inputs

The Deep to Points tool uses one input.

Input: This orange input is the only required connection. It is connected from a node with

deep image data.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Camera: Connecting a scene’s camera to the green camera input precisely positions the point cloud

relative to the original 3D scene. The camera’s perspective is taken into account so that points are

accurately placed within the 3D Viewer.

Basic Node Setup

The Deep to Points node receives the media in containing the deep image data. It then creates a 3D

point cloud from the image to make it easier to visualize elements in Z space.

Deep to Points accepts deep image data and creates a Point Cloud

before passing that visualization off to the rest of the node tree.

Inspector

Deep to Points controls

Controls Tab

The Controls tab includes parameters for adjusting the point cloud.

�Style: Style allows you to display the points as cross hairs or points in the viewer.

�Size: This slider can be used to increase the size of the onscreen crosshairs or points

�Antialiasing: When enabled, points will appear rounded and smooth, resulting in softer edges.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

�Density: This slider allows you to control the overall concentration of points in the viewer.

Increasing the value will build up the intensity of points whereas decreasing this value will have

the opposite effect.

�Default Color: When unchecking the Use Per-Point Colors checkbox, each point will inherit a color

specified in this control.

�Use Per-Point Colors: When enabled, each point will inherit its color from the connected

source clip.

�Make Renderable: Determines whether the point cloud visible in the 3D viewer will be renderable

in a Renderer3D node. Enabling this checkbox will allow the point cloud to be rendered out into a

flat 2D image.

�Unseen by Camera: This checkbox control appears when the Make Renderable option is

selected. If the Unseen by Cameras checkbox is selected, the point cloud is visible in the viewers

but not rendered into the output image by the Renderer 3D node.

�Scale: This slider allows you to increase or decrease the overall size of the point cloud.

�Depth Scale: The slider allows you to expand or contract the overall depth of the point cloud.

Increasing the depth scale will amplify the overall distance of depth; spacing out the points giving

you a fuller representation of the point cloud.

�Flip Depth: Use this checkbox to invert the depth data, flipping the position of the points from

negative to positive

Transform Tab

The controls in this tab are used to set the position and scaling parameters of the point cloud.

The Deep to Points Transform tab


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Translation

X, Y, Z Offset

These controls can be used to position the point cloud.

Rotation

Rotation Order

Use these buttons to select which order is used to apply rotation along each axis of the object. For

example, XYZ would apply the rotation to the X axis first, followed by the Y axis and then finally

the Z axis.

X, Y, Z Rotation

Use these controls to rotate the object around its pivot point. If the Use Target checkbox is selected,

then the rotation is relative to the position of the target; otherwise, the global axis is used.

Pivot

X, Y, Z Pivot

A Pivot point is the point around which an object rotates. Normally, an object rotates around its own

center, which is considered to be a pivot of 0,0,0. These controls can be used to offset the pivot from

the center.

Scale

X, Y, Z Scale

If the Lock X/Y/Z checkbox is checked, a single Scale slider is shown. This adjusts the overall size of

the object. If the Lock checkbox is unchecked, individual X, Y, and Z sliders are displayed to allow

individual scaling in each dimension. Note: If the Lock checkbox is checked, scaling of individual

dimensions is not possible, even when dragging specific axes of the Transformation Widget in

scale mode.

Use Target

Selecting the Use Target checkbox enables a set of controls for positioning an XYZ target. When

target is enabled, the object always rotates to face the target. The rotation of the object becomes

relative to the target.

Import Transform

Opens a file browser where you can select a scene file saved or exported by your 3D application. It

supports the following file types:

LightWave Scene

.lws

Max Scene

.ase

Maya Ascii Scene

.ma

The Import Transform button imports only transformation data. For 3D geometry, lights, and cameras,

consider using the File > FBX Import option.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Onscreen Transformation Controls

Most of the controls in the Transform tab are represented in the viewer with onscreen controls for

transformation, rotation, and scaling. To change the mode of the onscreen controls, select one of the

three buttons in the toolbar in the upper left of the viewer. The modes can also be toggled using the

keyboard shortcut Q for translation, W for rotation, and E for scaling. In all three modes, individual axes

of the control may be dragged to affect just that axis, or the center of the control may be dragged to

affect all three axes.

The scale sliders for most 3D tools default to locked, which causes uniform scaling of all three

axes. Unlock the Lock X/Y/Z Scale checkbox to scale an object on a single axis only.

Viewer Transform controls

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Image nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.

dHoldout [dHld]

The dHoldout node

dHoldout Node Introduction

This tool uses a foreground Deep Image to occlude background Deep Image samples, either by

removing them or computing the value after occlusion

Inputs

The dHoldout tool uses one background input and a foreground input.

Background: This orange input is connected from a node with deep image data that you want to use

for the background.

Foreground: The white foreground input is for the second of two deep images which is typically a

foreground subject that should be used to occlude the background.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION