---
title: "The Common Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 498
---

# The Common Controls

Nodes that handle tracking operations share several identical controls in the Inspector. This section

describes controls that are common among Tracking nodes.

Inspector

The Common Tracking Controls Settings tab

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Tracking category. The controls are

consistent and work the same way for each tool.

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image.

Normally, this will cause the tool to skip processing entirely, copying the input straight to the output.

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This can be useful if the node is scripted to

trigger a task, but the node’s value is set to 0.0.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Red/Green/Blue/Alpha Channel Selector

These four buttons are used to limit the effect of the tool to specified color channels. This filter is often

applied after the tool has been processed.

For example, if the Red button on a Blur tool is deselected, the blur will first be applied to the image,

and then the red channel from the original input will be copied back over the red channel of the result.

There are some exceptions, such as tools for which deselecting these channels causes the tool to

skip processing that channel entirely. Tools that do this will generally possess a set of identical RGBA

buttons on the Controls tab in the tool. In this case, the buttons in the Settings and the Controls tabs

are identical.

Apply Mask Inverted

Enabling the Apply Mask Inverted option inverts the complete mask channel for the tool. The mask

channel is the combined result of all masks connected to or generated in a node.

Multiply by Mask

Selecting this option will cause the RGB values of the masked image to be multiplied by the mask

channel’s values. This will cause all pixels of the image not included in the mask (i.e., set to 0) to

become black/transparent.

Use Object/Use Material (Checkboxes)

Some 3D software can render to file formats that support additional channels. Notably, the EXR file

format supports Object ID and Material ID channels, which can be used as a mask for the effect.

These checkboxes determine whether the channels will be used, if present. The specific Material ID or

Object ID affected is chosen using the next set of controls.

Correct Edges

This checkbox appears only when the Use Object or Use Material checkboxes are selected. It toggles

the method used to deal with overlapping edges of objects in a multi-object image. When enabled,

the Coverage and Background Color channels are used to separate and improve the effect around

the edge of the object. If this option is disabled (or no Coverage or Background Color channels are

available), aliasing may occur on the edge of the mask.

For more information on the Coverage and Background Color channels, see Chapter 78,

"Understanding Image Channels," in the DaVinci Resolve Reference Manual, or Chapter 18

in the Fusion Reference Manual.

Object ID/Material ID (Sliders)

Use these sliders to select which ID will be used to create a mask from the object or material channels

of an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the viewer. The image or sequence must have been rendered from a 3D software

package with those channels included.

Motion Blur

�Motion Blur: This toggles the rendering of Motion Blur on the tool. When this control is toggled

on, the tool’s predicted motion is used to produce the motion blur caused by the virtual camera’s

shutter. When the control is toggled off, no motion blur is created.

�Quality: Quality determines the number of samples used to create the blur. A quality setting of

2 will cause Fusion to create two samples to either side of an object’s actual motion. Larger values

produce smoother results but increase the render time.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

�Shutter Angle: Shutter Angle controls the angle of the virtual shutter used to produce the motion

blur effect. Larger angles create more blur but increase the render times. A value of 360 is the

equivalent of having the shutter open for one full frame exposure. Higher values are possible and

can be used to create interesting effects.

�Center Bias: Center Bias modifies the position of the center of the motion blur. This allows for the

creation of motion trail effects.

�Sample Spread: Adjusting this control modifies the weighting given to each sample. This affects

the brightness of the samples.

Use GPU

The Use GPU menu has three settings. Setting the menu to Disable turns off GPU hardware-

accelerated rendering. Enabled uses the GPU hardware for rendering the node. Auto uses a capable

GPU if one is available and falls back to software rendering when a capable GPU is not available.

Hide Incoming Connections

Enabling this checkbox can hide connection lines from incoming nodes, making a node tree appear

cleaner and easier to read. When enabled, empty fields for each input on a node will be displayed

in the Inspector. Dragging a connected node from the node tree into the field will hide that incoming

connection line as long as the node is not selected in the node tree. When the node is selected in the

node tree, the line will reappear.

Comments

The Comments field is used to add notes to a tool. Click in the empty field and type the text. When a

note is added to a tool, a small red square appears in the lower-left corner of the node when the full

tile is displayed, or a small text bubble icon appears on the right when nodes are collapsed. To see the

note in the Node Editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more details on scripting

nodes, please consult the Fusion scripting documentation.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Chapter 120

Transform Nodes

This chapter details the Transform nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Camera Shake [CSh]������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2789

Crop [CRP]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2792

DVE [DVE]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2795

Letterbox [LBX]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2798

Planar Transform [Pxf]���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2801

Resize [RSZ]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2803

Scale [SCL]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2806

Transform [XF]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2809

The Common Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2813


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Camera Shake [CSh]

The Camera Shake node

Camera Shake Node Introduction

This node can simulate a variety of camera shake-style motions from organic to mechanical. It is not

the same as the Shake Modifier, which generates random number values for parameters.

For more information on the Shake modifier, see Chapter 124, "Modifiers," in the DaVinci

Resolve Reference Manual, or Chapter 64 in the Fusion Reference Manual.

The Camera Shake node concatenates its result with adjacent transformation nodes for

higher-quality processing.

Inputs

The two inputs on the Camera Shake node are used to connect a 2D image and an effect mask, which

can be used to limit the camera shake area.

Input: The orange input is used for the primary 2D image that shakes.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the camera shake area to

only those pixels within the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Camera Shake background input is used to connect the image you want to transform. Polygon

masks can be connected into the occlusion mask input to identify areas the camera shake

should ignore.

The Camera Shake node can be connected directly after

a MediaIn node or any node providing a 2D output.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION