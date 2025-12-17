---
title: "Z To Disparity [Z2D]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 489
---

# Z To Disparity [Z2D]

The Z To Disparity node

NOTE: The Z To Disparity node is available only in Fusion Studio and DaVinci Resolve Studio.

Z To Disparity Node Introduction

Z To Disparity takes a stereo camera and an image containing a Z channel and outputs the same

image but with disparity channels in it. This is useful for constructing a Disparity map from CG renders,

which will be more accurate than the Disparity map created from the Disparity node.

Inputs

The three inputs on the Z To Disparity node are used to connect the left and right images and a

camera node.

Left Input: The orange input is used to connect either the left eye image or the stack image.

Right Input: The green input is used to connect the right eye image. This input is available only when

the Stack Mode menu is set to Separate.

Stereo Camera: The magenta input is used to connect a stereo perspective camera, which may be

either a Camera 3D with eye separation, or a tracked L/R Camera 3D.

Outputs

Unlike most nodes in Fusion, Z To Disparity has two outputs for the left and right eye.

Left Output: This outputs the left eye image containing a new disparity channel, or a Stacked Mode

image with a new disparity channel.

Right Output: This outputs the right eye image with a new disparity channel. This output is visible only

if Stack Mode is set to Separate.

Basic Node Setup

Below, a stereo camera and an image containing a Z channel is connected to a Z To Disparity node.

The same image is output with disparity channels.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

A Z To Disparity node takes an image with a Z channel and creates a disparity channel

Inspector

The Z To Disparity Controls tab

Controls Tab

The Controls tab includes settings that refine the conversion algorithm.

Output Disparity To RGB

In addition to outputting disparity values into the disparity channel, activating this checkbox causes Z

To Disparity to also output the disparity values into the color channels as {x, y, 0, 1}.

When activated, this option will automatically promote the RGBA color channels to float32. This option

is useful for a quick look to see what the disparity channel looks like.

Refine Disparity

This refines the Disparity map based on the RGB channels.

Strength

Increasing this slider does two things. It smooths out the depth in constant color regions and moves

edges in the Z channel to correlate with edges in the RGB channels. Increasing the refinement has the

undesirable effect of causing texture in the color channel to show up in the Z channel. You will want to

find a balance between the two.

Radius

This is the pixel-radius of the smoothing algorithm.

Stack Mode

In Stack Mode, L and R outputs will output the same image.

If HiQ is off, the interpolations are done using nearest-neighbor sampling, leading to a more

“noisy” result.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

Swap Eyes

This allows you to easily swap the left and right eye outputs.

The Z To Disparity Camera tab

Camera Tab

The Camera tab includes settings for selecting a camera and setting its conversion point if necessary.

Camera Mode

If you need correct real-world disparity values because you are trying to match some effect to an

existing scene, you should use the External setting to get precise disparity values back. When External

is selected, a magenta camera input is available on the node to connect an existing stereo Camera 3D

node, and use the Camera settings to determine the Disparity settings.

If you just want any disparity and do not particularly care about the exact details of how it is offset and

scaled, or if there is no camera available, then the Artistic setting might be helpful.

Camera

If you connect a Merge 3D node that contains multiple cameras to the camera input, the Camera menu

allows you to select the camera to use.

Artistic Camera mode

If you do not have a camera, you can adjust the artistic controls to produce a custom disparity channel

whose values will not be physically correct but will be good enough for compositing hacks. There are

two controls to adjust:

Convergence Point

This is the Z value of the convergence plane. This corresponds to the negative of the Convergence

Distance control that appears in Camera 3D. At this distance, objects in the left and right eyes are at

exactly the same position (i.e., have zero disparity).

Objects that are closer appear to pop out of the screen, and objects that are further appear behind

the screen.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

Background Disparity (Sample from Left Eye)

This is the disparity of objects in the distant background. You can think of this as the upper limit to

disparity values for objects at infinity. This value should be for the left eye. The corresponding value in

the right eye will be the same in magnitude but negative.

Settings Tab

The Settings tab in the Inspector is also duplicated in other Stereo nodes. These common controls are

described in detail in the following “The Common Controls” section.

The Common Controls

The Common Settings tab can be found on virtually every tool found in Fusion. The following controls

are specific settings for Stereo nodes.

Settings Tab

The Common Settings Stereo 3D Settings tab

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image.

Normally, this will cause the tool to skip processing entirely, copying the input straight to the output.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

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


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

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


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION