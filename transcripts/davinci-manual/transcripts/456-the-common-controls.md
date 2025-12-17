---
title: "The Common Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 456
---

# The Common Controls

Nodes that handle miscellaneous operations share a number of identical controls in the Inspector. This

section describes controls that are common among miscellaneous nodes.

Inspector

The Common Miscellaneous Settings tab

Settings Tab

The Settings tab in the Inspector can be found on every tool in the miscellaneous nodes. The controls

are consistent and work the same way for each tool.

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image.

Normally, this will cause the tool to skip processing entirely, copying the input straight to the output.

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This can be useful if processing of this node

is scripted to trigger another task, but the value of the node is set to 0.0.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Red/Green/Blue/Alpha Channel Selector

These four buttons are used to limit the effect of the tool to specified color channels. This filter is often

applied after the tool has been processed.

For example, if the Red button on a Blur tool is deselected, the blur will first be applied to the image,

and then the red channel from the original input will be copied back over the red channel of the result.

There are some exceptions, such as tools for which deselecting these channels causes the tool to

skip processing that channel entirely. Tools that do this will generally possess a set of identical RGBA

buttons on the Controls tab in the tool. In this case, the buttons in the Settings and the Controls

tabs are identical.

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

This checkbox appears only when the Use Object or Use Material checkboxes are selected. It toggles

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

displayed in the view. The image or sequence must have been rendered from a 3D software package

with those channels included.

Use GPU

The Use GPU menu has three settings. Setting the menu to Disable turns off GPU hardware-

accelerated rendering. Enabled uses the GPU hardware for rendering the node. Auto uses a capable

GPU if one is available and falls back to software rendering when a capable GPU is not available.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Motion Blur

�Motion Blur: This toggles the rendering of Motion Blur on the tool. When this control is toggled

on, the tool’s predicted motion is used to produce the motion blur caused by the virtual camera’s

shutter. When the control is toggled off, no motion blur is created.

�Quality: Quality determines the number of samples used to create the blur. A quality setting of 2

will cause Fusion to create two samples to either side of an object’s actual motion. Larger values

produce smoother results but increase the render time.

�Shutter Angle: Shutter Angle controls the angle of the virtual shutter used to produce the motion

blur effect. Larger angles create more blur but increase the render times. A value of 360 is the

equivalent of having the shutter open for one whole frame exposure. Higher values are possible

and can be used to create interesting effects.

�Center Bias: Center Bias modifies the position of the center of the motion blur. This allows for the

creation of motion trail effects.

�Sample Spread: Adjusting this control modifies the weighting given to each sample. This affects

the brightness of the samples.

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


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Chapter 112

Optical Flow

This chapter details the Optical Flow nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Optical Flow [OF]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2546

Repair Frame [REP]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2550

Smooth Motion [SM]������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2552

Tween [Tw]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2554

Vector Warping Toolset (Studio Version Only)�������������������������������������������������������������������������������������������������������������������� 2557

Vector Denoise [VDn]���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2557

Vector Transform [VXf]������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2558

Vector Warp [VWp]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2560

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2562


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Optical Flow [OF]

The OpticalFlow node

Optical Flow Node Introduction

This node analyzes a clip connected to its input using an Optical Flow algorithm. Think of optical flow

as a per-pixel motion vector that matches up features over several frames.

The computed optical flow is stored within the Vector and Back Vector aux channels of the output.

These channels can be used in other nodes like the Vector Motion Blur or Vector Distort. However,

Optical Flow must render twice when connecting it to a Time Stretcher or Time Speed node. These

nodes require the channels A. FwdVec and B. BackVec in that order, but Optical Flow generates A.

BackVec and A. FwdVec when it processes.

If you find that optical flow is too slow, consider rendering it out into OpenEXR files using a

Saver node.

TIP: If the footage input flickers on a frame-by-frame basis, it is a good idea to deflicker the

footage beforehand.

Inputs

The Optical Flow node includes a single orange image input.

Input: The orange background input accepts a 2D image. This is the sequence of frames for which

you want to compute optical flow. The output of the Optical Flow node includes the image and vector

channels. The vector channels can be displayed by right-clicking in the viewer and choosing Channel

> Vectors and then Options > Normalize Color Range.

Basic Node Setup

The Optical Flow node analyzes the frames connected to the background input. Trimming a Loader or

MediaIn to only the range you need prevents analyzing unnecessary frames. The output of the node

can then be connected to any node that takes advantage of vector channels, such as a Time Stretcher.

TIP: When analyzing Optical Flow vectors, consider adding a Smooth Motion node afterward

with smoothing for forward/ backward vectors enabled.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

An Optical Flow node generating motion vectors on-the-fly.

Alternatively, if you find the Optical Flow node too slow to analyze the frames, consider

rendering it out to an OpenEXR format using a Saver node. Then import the rendered EXR file

as your new image with embedded vector channels.

An Optical Flow node rendered out through a Saver node.