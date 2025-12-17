---
title: "The Common Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 460
---

# The Common Controls

Nodes that handle optical flow operations share a number of identical controls in the Inspector.

This section describes controls that are common among Optical Flow nodes.

Inspector

The Common Optical Flow Settings tab

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Optical Flow category. The controls

are consistent and work the same way for each tool.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image.

Normally, this causes the tool to skip processing entirely, copying the input straight to the output.

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This can be useful when this node process is

scripted to trigger another task, but the value of the node is set to 0.0.

Red/Green/Blue/Alpha Channel Selector

These four buttons are used to limit the effect of the tool to specified color channels. This filter is often

applied after the tool has been processed.

For example, if the Red button on a Blur tool is deselected, the blur is first applied to the image, and

then the red channel from the original input will be copied back over the red channel of the result.

There are some exceptions, such as tools for which deselecting these channels causes the tool to

skip processing that channel entirely. Tools that do this generally possess a set of identical RGBA

buttons on the Controls tab in the tool. In this case, the buttons in the Settings and the Controls tabs

are identical.

Apply Mask Inverted

Enabling the Apply Mask Inverted option inverts the complete mask channel for the tool. The mask

channel is the combined result of all masks connected to or generated in a node.

Multiply by Mask

Selecting this option causes the RGB values of the masked image to be multiplied by the mask

channel’s values. This causes all pixels of the image not included in the mask (i.e., set to 0) to become

black/transparent.

Use Object/Use Material (Checkboxes)

Some 3D software can render to file formats that support additional channels. Notably, the EXR file

format supports Object ID and Material ID channels, which can be used as a mask for the effect. These

checkboxes determine whether the channels are used, if present. The specific Material ID or Object ID

affected is chosen using the next set of controls.

Correct Edges

This checkbox appears only when the Use Object or Use Material checkboxes are selected. It toggles

the method used to deal with overlapping edges of objects in a multi-object image. When enabled,

the Coverage and Background Color channels are used to separate and improve the effect around

the edge of the object. If this option disabled (or no Coverage or Background Color channels are

available), aliasing may occur on the edge of the mask.

For more information see Chapter 78, "Understanding Image Channels," in the

DaVinci Resolve Reference Manual, or Chapter 18 in the Fusion Reference Manual.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Object ID/Material ID (Sliders)

Use these sliders to select which ID is used to create a mask from the object or material channels of

an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the view. The image or sequence must have been rendered from a 3D software package

with those channels included.

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

edit boxes used to add scripts that process when the tool is rendering.

For more details on scripting nodes, see the Fusion scripting documentation.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

FUSION

Chapter 113

Paint Node

This chapter details the Paint node available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Paint��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2566

Paint Node Introduction����������������������������������������������������������������������������������������������������������������������������������������������������������������� 2566

Inputs������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2566

Basic Node Setup������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2566

Types of Paint Strokes��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2567

Editing Options Toolbar������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2568

Inspector������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2570

Paint Node Modifiers����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2573

Keyboard Shortcuts�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2574


Fusion Page Effects | Chapter 113 Paint Node

FUSION

Paint

The Paint node

Paint Node Introduction

Paint is an extremely flexible, stroke-based tool for wire and rig removal, image cloning, or to create

custom masks and mattes rapidly. Fusion’s paint can even be used to create new images and artistic

elements from scratch.

Each Paint node is made up of a series of brush strokes. These strokes are vector shapes with

editable brush, size, and effect. A wide range of apply modes and brush types are available.

Most Brushstrokes styles are editable polylines for fine control. They can be animated to change

shape, length, and size over time. The opacity and size of a stroke can be affected by velocity and

pressure when used with a supported tablet.

Unlimited undo and redo of paint provides the ability to experiment before committing changes to an

image sequence. Paint strokes can be reordered, deleted, and modified with virtually infinite flexibility.

Inputs

The two inputs on the Paint node are used to connect a 2D image and an effect mask which can be

used to limit the painted area.

Input: It is required to connect the orange input with a 2D image that creates the size of the “canvas”

on which you paint.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the Paint to only those

pixels within the mask.

Basic Node Setup

The Paint node always needs an input connection. The simplest setup is to paint directly on the

incoming MediaIn node.

A MediaIn node connected directly to the Paint input


Fusion Page Effects | Chapter 113 Paint Node

FUSION

A more flexible setup is to use a Background node to set the size that matches the image you are

painting on. In the Inspector, the background would be set to be fully transparent. Then, the Paint tool

can be merged as the foreground over the actual image you want to paint on.

A Paint node merged over the top of a MediaIn for more flexibility