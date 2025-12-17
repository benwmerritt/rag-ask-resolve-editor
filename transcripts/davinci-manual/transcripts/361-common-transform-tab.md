---
title: "Common Transform Tab"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 361
---

# Common Transform Tab

Common Transform 3D tab

Many tools in the 3D category include a Transform tab used to position, rotate, and scale the object

in 3D space.

Translation

X, Y, Z Offset

These controls can be used to position the 3D element.

Rotation

Rotation Order

Use these buttons to select which order is used to apply rotation along each axis of the object. For

example, XYZ would apply the rotation to the X axis first, followed by the Y axis and then finally

the Z axis.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

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

If the Lock X/Y/Z checkbox is checked, a single Scale slider is shown. This adjusts the overall size of the

object. If the Lock checkbox is unchecked, individual X, Y, and Z sliders are displayed to allow individual

scaling in each dimension. Note: If the Lock checkbox is checked, scaling of individual dimensions is not

possible, even when dragging specific axes of the Transformation Widget in scale mode.

Use Target

Selecting the Use Target checkbox enables a set of controls for positioning an XYZ target. When

target is enabled, the object always rotates to face the target. The rotation of the object becomes

relative to the target.

Import Transform

Opens a file browser where you can select a scene file saved or exported by your 3D application.

It supports the following file types:

LightWave Scene

.lws

Max Scene

.ase

Maya Ascii Scene

.ma

dotXSI

.xsi

The Import Transform button imports only transformation data. For 3D geometry, lights, and cameras,

consider using the File > FBX Import option.

Onscreen Transformation Controls

Viewer Transform controls

Most of the controls in the Transform tab are represented in the viewer with onscreen controls for

transformation, rotation, and scaling. To change the mode of the onscreen controls, select one of the

three buttons in the toolbar in the upper left of the viewer. The modes can also be toggled using the

keyboard shortcut Q for translation, W for rotation, and E for scaling. In all three modes, individual axes

of the control may be dragged to affect just that axis, or the center of the control may be dragged to

affect all three axes.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

The scale sliders for most 3D tools default to locked, which causes uniform scaling of all three axes.

Unlock the Lock X/Y/Z Scale checkbox to scale an object on a single axis only.

Settings Tab

Common Settings 3D controls

The Common Settings tab can be found on most tools in Fusion. The following controls are specific

settings for 3D nodes.

Hide Incoming Connections

Enabling this checkbox can hide connection lines from incoming nodes, making a node tree appear

cleaner and easier to read. When enabled, empty fields for each input on a node are displayed in

the Inspector. Dragging a connected node from the node tree into the field hides that incoming

connection line as long as the node is not selected in the node tree. When the node is selected in the

node tree, the line reappears.

Comment Tab

The Comment tab contains a single text control that is used to add comments and notes to the tool.

When a note is added to a tool, a small red dot icon appears next to the setting’s tab icon and a text

bubble appears on the node. To see the note in the Node Editor, hold the mouse pointer over the

node for a moment. The contents of the Comments tab can be animated over time, if required.

Scripting Tab

The Scripting tab is present on every tool in Fusion. It contains several edit boxes used to add scripts

that process when the tool is rendering. For more details on the contents of this tab, please consult the

scripting documentation.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Chapter 90

3D Light Nodes

This chapter details the 3D Light nodes available when creating 3D composites in

Fusion. The abbreviations next to each node name can be used in the Select Tool

dialog when searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Ambient Light [3AL]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1986

Directional Light [3DL]���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1988

DomeLight [3Do]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1991

Point Light [3PL]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1993

Spot Light [3SL]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1996

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2000


Fusion Page Effects | Chapter 90 3D Light Nodes

FUSION

Ambient Light [3AL]

The Ambient Light node

Ambient Light Node Introduction

An Ambient Light is a directionless light that globally illuminates a scene. It has no real position or

rotation, although an onscreen control appears in the viewer to indicate that a light is present in

the scene. Position controls for the viewer are provided to move the widget out of the way of other

geometry, if necessary.

Similar to a Camera 3D, you connect lights into a Merge 3D and view them in the scene by viewing the

Merge 3D node. Selecting a light node and loading it into the viewer does not show anything.

Inputs

The Ambient Light node includes a single optional orange input for a 3D scene or 3D geometry.

SceneInput: The orange input is an optional input that accepts a 3D scene. If a scene is provided, the

Transform controls in this node apply to the entire scene provided.

Basic Node Setup

The Ambient Light node is designed to be part of a larger 3D scene. You connect the light directly into

a Merge 3D. Separating lights into different Merge 3D nodes allows you to control which lights affect

which objects.

Ambient Light node structure


Fusion Page Effects | Chapter 90 3D Light Nodes

FUSION