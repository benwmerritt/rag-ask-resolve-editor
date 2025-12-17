---
title: "The Common Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 448
---

# The Common Controls

Nodes that handle matte operations share a number of identical controls in the Inspector. This section

describes controls that are common among matte nodes.

Inspector

Common Matte settings Inspector

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Matte category. The controls are

consistent and work the same way for each tool.

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image.

Usually, this causes the tool to skip processing entirely, copying the input straight to the output.

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This can be useful if this node is scripted to

trigger another task, but the value is set to 0.0.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Red/Green/Blue/Alpha Channel Selector

These four buttons are used to limit the effect of the tool to specified color channels. This filter is often

applied after the tool has been processed.

For example, if the Red button on a Blur tool is deselected, the blur is first applied to the image, and

then the red channel from the original input is copied back over the red channel of the result.

There are some exceptions, such as tools where deselecting these channels causes the tool to skip

processing that channel entirely. In that case, there are a set of RGBA buttons on the Controls tab in

the tool. The buttons in the Settings and the Controls tabs are identical.

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

For more information on the Coverage and Background Color channels, see Chapter 78,

"Understanding Image Channels," in the DaVinci Resolve Reference Manual, or Chapter 18

in the Fusion Reference Manual.

Object ID/Material ID (Sliders)

Use these sliders to select which ID is used to create a mask from the object or material channels of

an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the view. The image or sequence must have been rendered from a 3D software package

with those channels included.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Clipping Mode

This option determines how edges are handled when performing domain of definition rendering.

This is profoundly important when blurring the matte, which may require samples from portions of the

image outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition.

If the upstream DoD is smaller than the frame, the remaining area in the frame is treated as

black/transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that would normally be outside the upstream

DoD is treated as black/transparent.

Use GPU

The Use GPU menu has three settings. Setting the menu to Disable turns off GPU hardware-

accelerated rendering. Enabled uses the GPU hardware for rendering the node. Auto uses a capable

GPU if one is available, and falls back to software rendering when a capable GPU is not available

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


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Chapter 110

Metadata Nodes

This chapter details the Metadata nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Copy Metadata [Meta]��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2499

Set Metadata [SMeta]����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2500

Set Timecode [TcMeta]�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2502

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2504


Fusion Page Effects | Chapter 110 Metadata Nodes

FUSION

Copy Metadata [Meta]

The Copy Metadata node

Copy Metadata Node Introduction

Copy Metadata combines, replaces, or clears the metadata in your image. Metadata can be viewed in

a subview of the viewer.

Inputs

The two inputs on the Copy Metadata node are used to connect two 2D images.

Background Input: The orange background input is used for the primary 2D image that is output from

the node.

Foreground Input: The green foreground input is used for the secondary 2D image that contains

metadata you want merge or overwrite onto the background image.

Basic Node Setup

The Copy Metadata node takes metadata from the foreground input (green) and copies it into the

background input (orange). The output is the background input with modified metadata.

A Copy Metadata node copies metadata from the

foreground and embeds it into the background clip

Inspector

The Copy Metadata Controls tab


Fusion Page Effects | Chapter 110 Metadata Nodes

FUSION

Controls Tab

The Controls tab configures how metadata coming from the foreground input image gets added to the

background input image.

Operation

The Operation menu determines how the metadata of the foreground and background inputs

are treated.

�Merge (Replace Duplicates): All values are merged, but values with duplicate names are taken

from the foreground input.

�Merge (Preserve Duplicates): All values are merged, but values with duplicate names are taken

from the background input.

�Replace:  The metadata in the foreground replaces the entire metadata in the background.

�Clear: All metadata is discarded.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Metadata nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.