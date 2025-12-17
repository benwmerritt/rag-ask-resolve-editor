---
title: "The Common Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 411
---

# The Common Controls

Film nodes share a number of identical controls in the Inspector. This section describes controls that

are common among Film nodes.

Inspector

The Common Film settings inspector

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Film category. The Settings

controls are even found on third-party Film-type plugin tools. The controls are consistent and work the

same way for each tool, although some tools do include one or two individual options, which are also

covered here.

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image.

Commonly, this causes the tool to skip processing entirely, copying the input straight to the output.

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This can be useful if processing of this node

is scripted to trigger another task, but the value of the node is set to 0.0.


Fusion Page Effects | Chapter 99 Film Nodes

FUSION

Red/Green/Blue/Alpha Channel Selector

These four buttons are used to limit the effect of the tool to specified color channels. This filter is often

applied after the tool has been processed.

For example, if the red button on a Blur tool is deselected, the blur is first applied to the image, and

then the red channel from the original input is copied back over the red channel of the result.

There are some exceptions, such as tools for which deselecting these channels causes the tool to

skip processing that channel entirely. Tools that do this generally possess a set of identical RGBA

buttons on the Controls tab in the tool. In this case, the buttons in the Settings and the Controls tabs

are identical.

Apply Mask Inverted

Enabling the Apply Mask Inverted option inverts the complete mask channel for the tool. The mask

channel is the combined result of all masks connected to or generated in a node.

Multiply by Mask

Selecting this option causes the RGB values of the masked image to be multiplied by the mask

channel’s values. This causes all pixels not included in the mask (i.e., set to 0) to become black/

transparent.

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

“Understanding Image Channels,” in the DaVinci Resolve Reference Manual, or Chapter 18

in the Fusion Reference Manual.

Object ID/Material ID (Sliders)

Use these sliders to select which ID is used to create a mask from the object or material channels of

an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the view. The image or sequence must have been rendered from a 3D software package

with those channels included.


Fusion Page Effects | Chapter 99 Film Nodes

FUSION

Clipping Mode

This option determines how edges are handled when performing domain of definition rendering. This

is mostly important for nodes like Blur, which may require samples from portions of the image outside

the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition to use

the full frame of the image, effectively ignoring the current domain of definition. If the upstream

DoD is smaller than the frame, the remaining area in the frame is treated as black/transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that would normally be outside the upstream

DoD is treated as black/transparent.

Use GPU

The Use GPU menu has three settings. Setting the menu to Disable turns off hardware-accelerated

rendering using the graphics card in your computer. Enabled uses the hardware. Auto uses a capable

GPU if one is available and falls back to software rendering when a capable GPU is not available

Comments

The Comments field is used to add notes to a tool. Click in the empty field and type the text. When a

note is added to a tool, a small red square appears in the lower-left corner of the node when the full

tile is displayed, or a small text bubble icon appears on the right when nodes are collapsed. To see the

note in the Node Editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more details on scripting

nodes, please consult the Fusion scripting documentation.


Fusion Page Effects | Chapter 99 Film Nodes

FUSION

Chapter 100

Filter Nodes

This chapter details the Filter nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Create Bump Map [CBu]����������������������������������������������������������������������������������������������������������������������������������������������������������������� 2270

Custom Filter Node [CFlt]��������������������������������������������������������������������������������������������������������������������������������������������������������������� 2272

Erode Dilate Node [ErDl]���������������������������������������������������������������������������������������������������������������������������������������������������������������� 2276

Filter Node [Fltr]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2278

Rank Filter Node [RFlt]���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2281

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2283


Fusion Page Effects | Chapter 100 Filter Nodes

FUSION

Create Bump Map [CBu]

The Create Bump Map node

Create Bump Map Node Introduction

The Create Bump Map node converts a grayscale (height map) image into a bump map. Unlike the

Bump Map node that turns an image into a 3D material, the Create Bump Map node creates bump

vector data and provides the output as an RGB image so other image-processing operations can

be applied.

Input

The Create Bump Map node includes two inputs: one for the main image and the other for an effect

mask to limit the area where the bump map is created.

Input: The orange input takes the RGBA channels from an image to calculate the bump map.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

creation of the bump map to only those pixels within the mask. An effects mask is applied to the tool

after the tool is processed.

Basic Node Setup

The Create Bump Map node accepts a 2D grayscale image like a fast noise, which can then go

through various 2D image-processing filters to create the bump map texture.

A Create Bump Map node produces a bump map as an RGB image for further image processing


Fusion Page Effects | Chapter 100 Filter Nodes

FUSION