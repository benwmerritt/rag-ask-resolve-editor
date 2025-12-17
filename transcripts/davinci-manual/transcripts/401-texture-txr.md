---
title: "Texture [Txr]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 401
---

# Texture [Txr]

The Texture node

Texture Node Introduction

The Texture node controls the texture mapping of elements in a rendered image. The Texture node

relies on the presence of U and V Map channels in a 3D-rendered image connected to the main Image

input. If these channels are not present, this node has no effect.

NOTE: Background pixels may have U and V values of 0.0, which set those pixels to the color

of the texture’s corner pixel. To restrict texturing to specific objects, use an effect mask based

on the Alpha of the object or its Object or Material ID channel.

Inputs

The Texture node includes three inputs: one for the main image with UV map channels, one for

a texture map image, and another for an effect mask to limit the area where the replace texture

is applied.


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Input: This orange input accepts a 2D image that includes UV channels. If the UV channels are not in

the images, this node has no effect.

Texture: The green texture map input provides the texture that is wrapped around objects, replacing

the current texture.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits

the texture to only those pixels within the mask. An effects mask is applied to the tool after the

tool is processed.

Basic Node Setup

The Texture node is inserted after a 2D image that contains a Texture UV channel. Below, a Renderer

3D is used to add texture coordinates to 3D text. The Texture node can then be used to manipulate

those coordinates using a new texture connected to the green texture input.

A Texture node used to manipulate the texture coordinates and add texture to a Text 3D node

Inspector

Texture controls

Texture Tab

The Texture tab controls allow you to flip, swap, scale, and offset the UV texture image connected to

the texture input.

Flip Horizontal and Vertical

Use these two buttons to flip the texture image horizontally and/or vertically.

Swap UV

When this checkbox is selected, the U and V channels of the source image are swapped.


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Rotate 90

The texture map image is rotated 90 degrees when this checkbox is enabled.

U and V Scale

These controls change the scaling of the U and V coordinates used to map the texture. Changing

these values effectively enlarges and shrinks the texture map as it is applied.

U and V Offset

Adjust these controls to offset the U and V coordinates. Changing the values causes the texture to

appear to move along the geometry of the object.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Pixel nodes. These common controls

are described in the following “The Common Controls” section.

The Common Controls

Nodes that handle Deep Pixel compositing operations share several identical controls in the Inspector.

This section describes controls that are common among Deep Pixel nodes.

Inspector

Common Settings tab in Deep Pixel Nodes


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Deep Pixel category. The Settings

controls are even found on third-party Deep Pixel-type plugin tools. The controls are consistent and

work the same way for each tool although some tools do include one or two individual options that are

also covered here.

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

channel’s values. This causes all pixels of the image not in the mask (i.e., set to 0) to become black/

transparent.

Use Object/Use Material (Checkboxes)

Some 3D software can render to file formats that support additional channels. Notably, the EXR file

format supports Object and Material ID channels, which can be used as a mask for the effect. These

checkboxes determine whether the channels are used if present. The specific Material ID or Object ID

affected is chosen using the next set of controls.

Correct Edges

This checkbox appears only when the Use Object or Use Material checkboxes are selected. It toggles

the method used to deal with overlapping edges of objects in a multi-object image. When enabled,

the Coverage and Background Color channels are used to separate and improve the effect around

the edge of the object. If this option is disabled (or no Coverage or Background Color channels are

available), aliasing may occur on the edge of the mask.

For more information, see Chapter 78, “Understanding Image Channels,” in the

DaVinci Resolve Reference Manual, or Chapter 18 in the Fusion Reference Manual.


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION

Object ID/Material ID (Sliders)

Use these sliders to select which ID is used to create a mask from the object or material channels of

an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the viewer. The image or sequence must have been rendered from a 3D software

package with those channels included.

Use GPU

The Use GPU menu has three settings. Setting the menu to Disable turns off hardware-accelerated

rendering using the graphics card in your computer. Enabled uses the hardware. Auto uses a capable

GPU if one is available, but falls back to software rendering when a capable GPU is not available.

Motion Blur

�Motion Blur: This toggles the rendering of Motion Blur on the tool. When this control is toggled

on, the tool’s predicted motion is used to produce the motion blur caused by the virtual camera’s

shutter. When the control is toggled off, no motion blur is created.

�Quality: Quality determines the number of samples used to create the blur. A quality setting of

2 causes Fusion to create two samples to either side of an object’s actual motion. Larger values

produce smoother results but increase the render time.

�Shutter Angle: Shutter Angle controls the angle of the virtual shutter used to produce the motion

blur effect. Larger angles create more blur but increase the render times. A value of 360 is the

equivalent of having the shutter open for one whole frame exposure. Higher values are possible

and can be used to create interesting effects.

�Center Bias: Center Bias modifies the position of the center of the motion blur. This allows the

creation of motion trail effects.

�Sample Spread: Adjusting this control modifies the weighting given to each sample. This affects

the brightness of the samples.

Comments

The Comments field is used to add notes to a tool. Click in the field and type the text. When a note

is added to a tool, a small red square appears in the lower-left corner of the node when the full tile is

displayed, or a small text bubble icon appears on the right when nodes are collapsed. To see the note

in the Node Editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more details on scripting

nodes, please consult the Fusion scripting documentation.


Fusion Page Effects | Chapter 97 Deep Pixel Nodes

FUSION