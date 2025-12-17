---
title: "The Common Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 516
---

# The Common Controls

Nodes that handle VR operations share a number of identical controls in the Inspector. This section

describes controls that are common among VR nodes.

Inspector

The VR Common controls

Settings Tab

The Settings tab in the Inspector can be found on every tool in the VR category. The controls are

consistent and work the same way for each tool.

Apply Mask Inverted

Enabling the Apply Mask Inverted option inverts the complete mask channel for the tool. The mask

channel is the combined result of all masks connected to or generated in a node.

Use GPU

The Use GPU menu has three settings. Setting the menu to Disable turns off hardware-accelerated

rendering using the graphics card in your computer. Auto uses a capable GPU if one is available and

falls back to software rendering when a capable GPU is not available.


Fusion Page Effects | Chapter 122 VR Nodes

FUSION

Hide Incoming Connections

Enabling this checkbox can hide connection lines from incoming nodes, making a node tree appear

cleaner and easier to read. When enabled, empty fields for each input on a node are displayed in the

Inspector. Dragging a connected node from the node tree into the empty field hides that incoming

connection line as long as the node is not selected in the node tree. When the node is selected in the

node tree, the line reappears.

Comments

The Comments field is used to add notes to a tool. Click in the empty field and type the text. When a

note is added to a tool, a small red square appears in the lower-left corner of the node when the full

tile is displayed, or a small text bubble icon appears on the right when nodes are collapsed. To see the

note in the Node Editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more details on scripting

nodes, please consult the Fusion scripting documentation.


Fusion Page Effects | Chapter 122 VR Nodes

FUSION

Chapter 123

Warp Nodes

This chapter details the Warp nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Coordinate Space [CdS]������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2881

Corner Positioner [CPn]������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2883

Dent [Dnt]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2885

Displace [Dsp]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2886

Drip [DRP]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2889

Grid Warp [Grd]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2891

Lens Distort [Lens]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2898

Perspective Positioner [PPn]��������������������������������������������������������������������������������������������������������������������������������������������������������� 2901

Vector Distortion [Dst]��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2902

Vortex [Vtx]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2905

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2907


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Coordinate Space [CdS]

The Coordinate Space node

Coordinate Space Node Introduction

The Coordinate Space node changes the coordinate space of the image from rectangular to polar or

from polar to rectangular.

Inputs

The two inputs on the Coordinate Space node are used to connect a 2D image and an effect mask,

which can be used to limit the distorted area.

Input: The orange input is used for the primary 2D image that is distorted.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the distortion to only those

pixels within the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Coordinate Space node is used below to make a circular pattern based on a Fast Noise, Mosaic

Blur (DaVinci Resolve Resolve FX only), and a Transform node. The Crop node at the end is used to set

the desired resolution.

The Coordinate Space node can help create motion graphics backgrounds


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Example

To demonstrate a basic tunnel effect that can be achieved with this node:

1.	 Add a Text+ node with some text, and then animate it to move along a path from the top of

the frame to the bottom.

2.	 Connect the output of the Text+ node to a Coordinate Space node.

3.	 Select Polar to Rectangular from the Shape menu.

As the text moves from top to bottom along the original path, it appears to move from an

infinite distance in the Coordinate Space node. It may be necessary to flip the text using a

Transform node to make it appear the correct way in the Coordinate Space node. Another

common use for the Coordinate Space node is to use it in pairs: two of them set to different

Shape settings with a Drip or Transform node in between. When used in this way, the effect

gets modified while the image remains the same.

Inspector

The Coordinate Space Controls tab

Controls Tab

The Controls tab Shape menu switches between Rectangular to Polar and Polar to Rectangular.

Consider the following example to demonstrate the two coordinate spaces.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Warp nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION