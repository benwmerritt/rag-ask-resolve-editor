---
title: "Set Metadata [SMeta]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 449
---

# Set Metadata [SMeta]

The Set Metadata node

Set Metadata Node Introduction

Set Metadata allows you to create new Name = Value pairs in the metadata.  Metadata can be viewed

in a subview of the viewer.

Inputs

The single input on the Set Metadata node is used to connect a 2D image that gets metadata added.

Background Input: The orange background input is used for the primary 2D image that is output from

the node with the new metadata.


Fusion Page Effects | Chapter 110 Metadata Nodes

FUSION

Basic Node Setup

The Set Metadata node embeds new metadata into the background input (orange). The output is the

background input with new metadata.

A Set Metadata node creates new metadata and

embeds it into the background clip.

Inspector

The Set Metadata Controls tab

Controls Tab

The Controls tab is where you set up the name of the metadata field and the value or information

regarding the metadata.

Field Name

The name of the metadata value. Do not use spaces.

Field Value

The value assigned to the name above.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Metadata nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 110 Metadata Nodes

FUSION

Set Timecode [TcMeta]

The Set Timecode node

Set Timecode Node Introduction

Set Timecode inserts dynamic timecode values into the metadata table based on the FPS settings.

Inputs

The single input on the Set Timecode node is used to connect a 2D image that gets timecode added.

Background Input: The orange background input is used for the primary 2D image that is output from

the node with the new timecode.

Basic Node Setup

The Set Timecode node embeds new timecode metadata into the background input (orange). The

output is the background input with updated timecode.

A Set Timecode node inserts new timecode metadata into the background clip.

Inspector

The Set Timecode Controls tab

Controls Tab

The Controls tab sets the clip’s starting timecode metadata based on FPS, hours, minutes, seconds,

and frames.


Fusion Page Effects | Chapter 110 Metadata Nodes

FUSION

FPS

You can choose from a variety of settings for frames per second.

Since this is a Fuse, you can easily adapt the settings to your needs by editing the appropriate piece of

code for the buttons:

MBTNC_StretchToFit = true,

{ MBTNC_AddButton = "24" },

{ MBTNC_AddButton = "25" },

{ MBTNC_AddButton = "30" },

{ MBTNC_AddButton = "48" },

{ MBTNC_AddButton = "50" },

{ MBTNC_AddButton = "60" },

})

as well as for the actual values:

local rates = { 24, 25, 30, 48, 50, 60 }

Hours/Minutes/Seconds/Frames Sliders

Define an offset from the starting frame of the current comp.

Print to Console

Verbose output of the Timecode/Frame value in the Console.

The Timecode/Frames conversion is done according to the FPS settings.

The result might look like this:

TimeCode:	00:00:08:15

Frames:


Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Metadata nodes. These common controls

are described in detail in the following “The Common Controls” section.


Fusion Page Effects | Chapter 110 Metadata Nodes

FUSION

The Common Controls

Nodes that handle metadata operations share several identical controls in the Inspector. This section

describes controls that are common among Metadata nodes.

Inspector

The Common Metadata Settings tab

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Metadata category. The controls

are consistent and work the same way for each tool.

Use Object/Use Material (Checkboxes)

Some 3D software can render to file formats that support additional channels. Notably, the EXR file

format supports Object ID and material ID channels, which can be used as a mask for the effect. These

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


Fusion Page Effects | Chapter 110 Metadata Nodes

FUSION

Object ID/Material ID (Sliders)

Use these sliders to select which ID is used to create a mask from the object or material channels of

an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the view. The image or sequence must have been rendered from a 3D software package

with those channels included.

Comments

The Comments field is used to add notes to a tool. Click in the empty field and type the text. When a

note is added to a tool, a small red square appears in the lower-left corner of the node when the full

tile is displayed, or a small text bubble icon appears on the right when nodes are collapsed. To see the

note in the Node Editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are  available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more details on scripting

nodes, please consult the Fusion scripting documentation.


Fusion Page Effects | Chapter 110 Metadata Nodes

FUSION