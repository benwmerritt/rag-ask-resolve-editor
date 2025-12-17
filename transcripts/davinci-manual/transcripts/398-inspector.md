---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 398
---

# Inspector

dTransform controls

Controls Tab

The Controls tab includes parameters for transforming the deep image.

�Scale Z: The slider allows you to expand or contract the overall depth samples of the source.

Increasing the scale will amplify the overall distance of depth. Decreasing will compress the

depth range.

�Translate Z: Translate Z will allow you to move an object forward or backward along its depth

channel. This gives you the control to relocate an object closer or farther away from camera.

�Sample: Click and drag from the sample button into the viewer to choose a value.

�Center X/Y: Move the center position of the deep image.

�Pivot X/Y: Move the pivot point of the deep image.

�Size X/Y: Resize the deep image on the selected axis.

�Use Size and Aspect: Check this box to activate the parameters below.

�Size: Scales the image equally along both the X and Y axes

�Aspect: Lets you set the aspect ratio of the image.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Image nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Image to Deep [ItD]

The Image to Deep node

Image to Deep Node Introduction

This tool has an input for a 2D image. When connected, the image is given deep image data and can

be composited in a deep environment via the dMerge node.

Inputs

The Image to Deep tool uses one input.

Input: This orange input is the only required connection. It is connected from a node with 2D image

data that you want to use with a Deep Image.

Basic Node Setup

The Image to Deep node receives the media in containing the 2D image data. It then adds Deep

Image information to it, allowing it to be used in deep image compositing with a dMerge node.

Image to Deep accepts a 2D image (MediaIn3) then adds Deep Image data, allowing

it to be composited with Deep Image media (MediaIn1) via a dMerge node.

Inspector

Image to Deep controls


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Controls Tab

The Controls tab includes parameters for adjusting the depth information.

�Specify Z: Check this box to specify the current Z depth. If unchecked, you can adjust it using the

Z Scale control below.

�Z Scale: The slider allows you to expand or contract the overall depth samples of the source.

Increasing the scale will amplify the overall distance of depth. Decreasing will compress the

depth range.

�Z Offset: Will allow you to move an object forward or backward along its depth channel. This gives

you the control to relocate an object closer or farther away from camera.

�Sample: Click and drag from the sample button into the viewer to choose a value.

�Center X/Y: Reposition the 2D image along the X/Y axes.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Image nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.

The Common Controls

Settings Tab

The Common Settings tab can be found on most tools in Fusion. The following controls are specific

settings for Deep Image nodes.

The Deep Image Settings tab


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Hide Incoming Connections

Enabling this checkbox can hide connection lines from incoming nodes, making a node tree appear

cleaner and easier to read. When enabled, empty fields for each input on a node are displayed in

the Inspector. Dragging a connected node from the node tree into the field hides that incoming

connection line as long as the node is not selected in the node tree. When the node is selected in the

node tree, the line reappears.

Comments Tab

The Comments tab contains a single text control that is used to add comments and notes to the tool.

When a note is added to a tool, a small red dot icon appears next to the setting’s tab icon and a text

bubble appears on the node. To see the note in the Node Editor, hold the mouse pointer over the

node for a moment. The contents of the Comments tab can be animated over time, if required.

Scripting Tabs

The Scripting tab is present on every tool in Fusion. It contains several edit boxes used to add scripts

that process when the tool is rendering. For more details on the contents of this tab, please consult the

scripting documentation.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Chapter 97

Deep Pixel Nodes

This chapter details Deep Pixel nodes found in Fusion. Deep Pixel nodes are

capable of handling AOVs (Arbitrary Output Variables) from 3D-rendered files.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Ambient Occlusion [SSAO]������������������������������������������������������������������������������������������������������������������������������������������������������������ 2198

Depth Blur [DBl]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2201

Fog [Fog]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2203

Shader [Shd]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2205

Texture [Txr]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2208

The Common Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2210


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION