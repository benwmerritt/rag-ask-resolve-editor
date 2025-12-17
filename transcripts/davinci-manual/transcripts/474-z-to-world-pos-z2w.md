---
title: "Z to World Pos [Z2W]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 474
---

# Z to World Pos [Z2W]

The Z to World Position node

Z to World Pos Node Introduction

The Z to World Pos node is used to either generate a World Position Pass from a Z channel and a 3D

Camera or a Z channel from a World Position Pass and a 3D Camera.

Creating a World Position Pass from Z-depth can be useful when your 3D application is not capable of

creating a WPP.

It can also be used when a 3D-tracking software outputs a per-pixel Z-depth together with the 3D

Camera. Thus, the Volume Mask and Volume Fog could be applied to real-world scenes. The quality of

the resulting WPP depends mainly on the quality of the incoming Z channel.

See the “WPP Concept” section for further explanation on how this technology works and to learn

about the required imagery.

Inputs

The following inputs appear on the node tile in the Node Editor:

Image: The orange image input accepts an image containing a World Position Pass or a Z-depth pass,

depending on the desired operation.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the World Position Pass to

certain areas.

Scene Input: The magenta scene input accepts a 3D scene input containing a 3D Camera.

Basic Node Setup

Below, a MediaIn labeled RGBA contains the main rendered image from a 3D scene. A Z-depth pass

from a 3D-rendered scene is labeled Z_PASS. The Channel Booleans node is used to map the Aux Z

channel into either the red, green, or blue channel. The Z to World Position node is placed after the

Channel Booleans node, and an imported 3D camera that matches the RGBA image is connected to

the 3D camera input on the Z to World Position node. A Channel Booleans node is placed after the

Z to World Position node, which can remap the X, Y, and Z positions for use in other nodes.


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

A Z to World Position node creates a World Position Pass from a Z-depth pass

Inspector

The Z to World Position Controls tab

Controls Tab

The Controls tab determines whether you are creating a World Position Pass or a Z channel. If there is

more than one camera in the connected scene, this tab also selects the camera to use for the calculation.

Mode

This menu switches between creating a Z channel from a World Position Pass or vice versa.

Camera

If multiple cameras are available in the connected Scene input, this drop-down menu allows you to

choose the correct camera needed to evaluate the image.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Position nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.

WPP Concept

The Position nodes in Fusion offer an entirely new way of working with masks and Volumetrics for

footage containing XYZ Position channels. Z to World offers the option to create those channels out of

a Z channel and 3D Camera information. For this overview, we refer to the World Position Pass as WPP.

What Is a WPP?

The WPP interprets each pixel’s XYZ position in 3D space as an RGB color value.


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

For instance, if a pixel sits at 0/0/0, the resulting pixel has an RGB value of 0/0/0 and thus will be black.

If the pixel sits at 1/0/0 in the 3D scene, the resulting pixel is entirely red. Of course, if the coordinates

of the pixel are something like -60/75/123, WPP interprets those values as RGB color values as well.

Due to the potentially enormous size of a 3D scene, the WPP channel should always be rendered in

32-bit floating point to provide the accuracy needed. The image below shows a 3D rendering of a

scene with its center sitting at 0/0/0 in 3D Space and the related WPP. For better visibility, the WPP is

normalized in this example.

Different Coordinate Spaces

Rendering WPPs can occur in different Coordinate Spaces. These include World Space, Eye Space,

and Object Space. The image below depicts how those different spaces look, although the nodes in

Fusion require the WPP rendering to occur in World Space.

The Scene Input

The nodes offer a Scene input, which can either be a 3D camera or a 3D scene containing a camera.

While the camera is vital for the Z to World node, Volume Mask and Volume Fog can generate their

output without any camera attached or with the camera position set to 0/0/0.

However, connecting a camera that lines up with the original camera the WPP has been rendered

from, or setting the camera’s position manually, dramatically improves the accuracy and look of the

resulting fog or mask.


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

The “Invisible Sphere”

The example scene shown so far has an empty background, meaning there is nothing in the scene

apart from the ground plane and the cubes.

If applying fog to a scene like that, which is larger than the ground plane, the result will look similar to

the “w/o Sphere” example shown below because, with no WPP information outside the ground plane,

the resulting value is 0/0/0, and the fog fills that area as well.

To get around that, you can add an invisible bounding sphere to your scene to create “dummy” WPP

values to help the Fog node to create the correct volume as shown in the “with Sphere” example below.

The Common Controls

Nodes that handle Position operations share several identical controls in the Inspector. This section

describes controls that are common among Position nodes.

Inspector

Position nodes Common Settings tab


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Position category. The controls are

consistent and work the same way for each tool.

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image.

Normally, this will cause the tool to skip processing entirely, copying the input straight to the output.

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This can be useful if the node is scripted to

trigger a task, but the node’s value is set to 0.0.

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

format supports Object and Material ID channels, which can be used as a mask for the effect. These

checkboxes determine whether the channels will be used if present. The specific Material ID or Object

ID affected is chosen using the next set of controls.

Correct Edges

This checkbox appears only when the Use Object or Use Material checkboxes are selected. It toggles

the method used to deal with overlapping edges of objects in a multi-object image. When enabled,

the Coverage and Background Color channels are used to separate and improve the effect around

the edge of the object. If this option is disabled (or no Coverage or Background Color channels are

available), aliasing may occur on the edge of the mask.

For more information on the Coverage and Background Color channels, see Chapter 78,

"Understanding Image Channels," in the DaVinci Resolve Reference Manual, or Chapter 18

in the Fusion Reference Manual


Fusion Page Effects | Chapter 115 Position Nodes

FUSION

Object ID/Material ID (Sliders)

Use these sliders to select which ID will be used to create a mask from the object or material channels

of an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the viewer. The image or sequence must have been rendered from a 3D software

package with those channels included.

Motion Blur

�Motion Blur: This toggles the rendering of Motion Blur on the tool. When this control is toggled

on, the tool’s predicted motion is used to produce the motion blur caused by the virtual camera’s

shutter. When the control is toggled off, no motion blur is created.

�Quality: Quality determines the number of samples used to create the blur. A quality setting of 2

will cause Fusion to create two samples to either side of an object’s actual motion. Larger values

produce smoother results but increase the render time.

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


Fusion Page Effects | Chapter 115 Position Nodes

FUSION