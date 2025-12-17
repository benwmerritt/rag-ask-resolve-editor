---
title: "The Common Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 426
---

# The Common Controls

I/O nodes share a number of identical controls in the Inspector. This section describes controls that

are common among I/O nodes.

Inspector

Common Saver settings inspector


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

Settings Tab

The Settings tab in the Inspector can be found on the Loader, Saver, MediaIn, and MediaOut nodes.

The controls are consistent and work the same way for each tool, although some parameters are only

available on individual nodes but are covered here.

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image.

Normally, this causes the tool to skip processing entirely, copying the input straight to the output.

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This can be useful if processing of this node

is scripted to trigger another task, but the value of the node is set to 0.0.

Red/Green/Blue/Alpha Channel Selector

These four buttons are used to limit the effect of the tool to specified color channels. This filter is often

applied after the tool has been processed.

For example, if the red button on a Blur tool is deselected, the blur is first applied to the image, and

then the red channel from the original input is copied back over the red channel of the result.

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

format supports Object and Material ID channels, which can be used as a mask for the effect. These

checkboxes determine whether the channels are used, if present. The specific Material ID or Object ID

affected is chosen using the next set of controls.

Correct Edges

This checkbox appears only when the Use Object or Use Material checkboxes are selected. It toggles

the method used to deal with overlapping edges of objects in a multi-object image. When enabled,

the Coverage and Background Color channels are used to separate and improve the effect around

the edge of the object. If this option disabled (or no Coverage or Background Color channels are

available), aliasing may occur on the edge of the mask.

For more information on Coverage and Background Color channels, see Chapter 78,

"Understanding Image Channels," in the DaVinci Resolve Reference Manual, or Chapter 18

in the Fusion Reference Manual.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

Object ID/Material ID (Sliders)

Use these sliders to select which ID is used to create a mask from the object or material channels of

an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the view. The image or sequence must have been rendered from a 3D software package

with those channels included.

Hide Incoming Connections

Enabling this checkbox can hide connection lines from incoming nodes, making a node tree appear

cleaner and easier to read. When enabled, empty fields for each input on a node are displayed in

the Inspector. Dragging a connected node from the node tree into the field hides that incoming

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


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

Chapter 106

Layer Nodes

This chapter details the use and modification of multilayer

images in your compositions.

The abbreviations next to each node name can be used in the Select Tool dialog when searching for

tools and in scripting references.

Contents

Layer Muxer [LMx]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2364

Layer Regex  [LRx]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2365

Layer Remover  [LRm]���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2368

Swizzler [Swz]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2370

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2376


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION

Layer Muxer [LMx]

The Layer Muxer node

Layer Muxer Node Introduction

This tool allows layers from one source to be combined with another source. The tool has two inputs;

when multilayer sources are connected, layers from one source are combined with the other.

Inputs

The Layer Muxer tool uses two inputs.

Image 1: This orange input is connected from a node with multilayer data that you want to combine.

Image 2: This green input is connected from a node with multilayer data that you want to combine.

Basic Node Setup

The Layer Muxer node receives two nodes with multilayer data and combines them in various ways

based on which layers you want to keep and which you want to ignore.

Layer Muxer combines two multi layer images.

Inspector

Layer Muxer controls


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION

Controls Tab

The Controls tab includes parameters for selecting layers to be used.

�Layer: Elect layers from the clip connected to the Image 2 input to combine with the clip

connected to Image 1. The pulldown control allows you nominate which layer(s) you’d like to

combine.  If any option other than All Layers is selected, a small layer icon will appear in the Layer

Muxer node to remind you that only certain layers are being passed through.

Default Layer: If a default layer is used in the Input 2 multilayer media file, it will combine that layer.

All Layers: Combines all the layers of the Input 2 multilayer image together.

Custom: Presents a check list off all layers in Input 2 that allows you to turn on and off the

multiple layers.

�Conflicts: Use this control to switch between either Image 1 or Image 2, the two inputs on this tool;

the selected Image will be output as the tool’s Default/[Main] layer.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Layer nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.