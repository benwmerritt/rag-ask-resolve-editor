---
title: "Rank Filter Node [RFlt]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 414
---

# Rank Filter Node [RFlt]

The Rank Filter node

Rank Filter Node Introduction

The Rank Filter examines nearby pixels, sorts the pixels by value, and then replaces the color of the

examined pixels with the color of the pixel with the selected rank.

Inputs

The Rank Filter node includes two inputs: one for the main image and the other for an effect mask to

limit the area where the filter is applied.

Input: The orange input is used for the primary 2D image that gets the Rank filter applied.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

rank filter to only those pixels within the mask. An effects mask is applied to the tool after the tool is

processed.

Basic Node Setup

The Rank Filter node can be placed anywhere in a node tree to apply an effect to an image.

A Rank Filter node placed after a

MediaIn node in DaVinci Resolve

Inspector

l

Rank Filter controls


Fusion Page Effects | Chapter 100 Filter Nodes

FUSION

Controls Tab

The Controls tab is used to set the size and rank value of the filter.

Size

This control determines the size in pixels of the area sampled by the filter. A value of 1 samples 1 pixel

in each direction, adjacent to the center pixel. This produces a total of 9 pixels, including the center

sampled pixel. Larger values sample from a larger area.

Low Size settings are excellent for removing salt and pepper style noise, while larger Size settings

produce an effect similar to watercolor paintings.

Rank

The Rank slider determines which value from the sampled pixels is chosen. A value of 0 is the lowest

value (darkest pixel), and 1 is the highest value (brightest pixel).

Example

Below is a before and after example of a Rank filter with Size set to 7 and a Rank of 0.7 to

create a watercolor effect.

Before and after of a Rank Filter producing a watercolor-style effect


Fusion Page Effects | Chapter 100 Filter Nodes

FUSION

The Common Controls

Filter nodes share a number of identical controls in the Inspector. This section describes controls that

are common among Filter nodes.

Inspector

Common Filter settings Inspector

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Filter category. The Settings

controls are even found on third-party filter-type plugin tools. The controls are consistent and work the

same way for each tool, although some tools do include one or two individual options, which are also

covered here.

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image.

Normally, this causes the tool to skip processing entirely, copying the input straight to the output.

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This can be useful if processing of this node

is scripted to trigger another task, but the value of the node is set to 0.0.


Fusion Page Effects | Chapter 100 Filter Nodes

FUSION

Red/Green/Blue/Alpha Channel Selector

These four buttons are used to limit the effect of the tool to specified color channels. This filter is often

applied after the tool has been processed.

For example, if the red button on a Blur tool is deselected, the blur is first applied to the image, and

then the red channel from the original input is copied back over the red channel of the result.

There are some exceptions, such as tools for which deselecting these channels causes the tool to

skip processing that channel entirely. Tools that do this generally possess a set of identical RGBA

buttons on the Controls tab in the tool. In this case, the buttons in the Settings and the Controls

tabs are identical.

Apply Mask Inverted

Enabling the Apply Mask Inverted option inverts the complete mask channel for the tool. The mask

channel is the combined result of all masks connected to or generated in a node.

Multiply by Mask

Selecting this option causes the RGB values of the masked image to be multiplied by the mask

channel’s values. This causes all pixels of the image not included in the mask (i.e., set to 0) to become

black/transparent.

Use Object/Use Material (Checkboxes)

Some 3D software can render to file formats that support additional channels. Notably, the EXR file

format supports Object ID and Material ID channels, which can be used as a mask for the effect.

These checkboxes determine whether the channels are used, if present. The specific Material ID or

Object ID affected is chosen using the next set of controls.

Correct Edges

This checkbox appears only when the Use Object or Use Material checkboxes are selected. It toggles

the method used to deal with overlapping edges of objects in a multi-object image. When enabled,

the Coverage and Background Color channels are used to separate and improve the effect around

the edge of the object. If this option disabled (or no Coverage or Background Color channels are

available), aliasing may occur on the edge of the mask.

For more information on the Coverage and Background Color channels, see Chapter 78,

“Understanding Image Channels,” in the DaVinci Resolve Reference Manual, or Chapter 18

in the Fusion Reference Manual.

Object ID/Material ID (Sliders)

Use these sliders to select which ID is used to create a mask from the object or material channels of

an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the view. The image or sequence must have been rendered from a 3D software package

with those channels included.

Use GPU

The Use GPU menu has three settings. Setting the menu to Disable turns off hardware-accelerated

rendering using the graphics card in your computer. Enabled uses the hardware. Auto uses a capable

GPU if one is available and falls back to software rendering when a capable GPU is not available


Fusion Page Effects | Chapter 100 Filter Nodes

FUSION

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

�Center Bias: Center Bias modifies the position of the center of the motion blur. This allows for the

creation of motion trail effects.

�Sample Spread: Adjusting this control modifies the weighting given to each sample. This affects

the brightness of the samples.

Comments

The Comments field is used to add notes to a tool. Click in the empty field and type the text. When a

note is added to a tool, a small red square appears in the lower-left corner of the node when the full

tile is displayed, or a small text bubble icon appears on the right when nodes are collapsed. To see the

note in the Node Editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more details on scripting

nodes, please consult the Fusion scripting documentation.


Fusion Page Effects | Chapter 100 Filter Nodes

FUSION