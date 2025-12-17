---
title: "Inputs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 520
---

# Inputs

There are three inputs on the Vector Distort node for the primary 2D image, the distort image with

vector channels and an effect mask.

Input: The orange image input is a required connection for the primary image you wish to distort. If this

image has vector channels, they are used in the distortion.

Distort: The green input is an optional distort image input used to distort the background image based

on vector channels. Once connected, it overrides vector channels in the input image.

Effect Mask: The optional blue effect mask input expects a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits

the displacement to only those pixels within the mask. An effects mask is applied to the tool after it is

processed.

Basic Node Setup

In the example below, the MediaIn1 node uses an Optical Flow node to generate the vector channels,

which are then passed on to the Vector Distort node. MediaIn2 is distorted and composited

over the background.

The Vector Distort node relies on the image having vector

channels or an Optical Flow node to generate them.

Inspector

The Vector Distortion Controls tab


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Controls Tab

The Controls tab contains parameters for selecting vector channels and controlling how much

distortion they apply to an image.

X Channel and Y Channel

These two menus are used to select which channel of the (green) distort image input is used to distort

the X and Y channels. If no distort reference image is connected, then channels from the main orange

input are used instead.

Flip Channel X and Flip Channel Y

Use these checkboxes to flip the direction of the distortion along the specified axis.

Lock Scale X/Y

Select this checkbox to separate the Scale slider into separate Scale X and Scale Y sliders.

Scale

Use the Scale slider to apply a multiplier to the values of the distortion reference image.

Lock Bias X/Y

Select this checkbox to separate the Bias slider into separate Bias X and Bias Y sliders.

Center Bias

Use the Center Bias slider to shift or nudge the distortion along a given axis.

Edges

This menu determines how the edges of the image are treated.

�Canvas: This causes the edges that are revealed by the shake to be the canvas color—usually

transparent or black.

�Duplicate: This causes the edges to be duplicated, causing a slight smearing effect at the edges.

Glow

Use this slider to add a glow to the result of the vector distortion.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Warp nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Vortex [Vtx]

The Vortex node

Vortex Node Introduction

The Vortex effect appears as a swirling whirlpool in specified regions of the image. The Vortex can be

made to move and grow by animating the various controls.

Inputs

There are two inputs on the Vortex node for the primary 2D image and the effect mask.

Input: The orange image input is a required connection for the primary image you wish to swirl.

Effect Mask: The optional blue effect mask input expects a mask shape created by polylines,

basic primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input

limits the swirling vortex to only those pixels within the mask. An effects mask is applied to the tool

after it is processed.

Basic Node Setup

Below, the Vortex is applied to text for creating motion graphics. Since the Vortex will cause the text to

swirl outside the text boundary, a Set Domain node is used to expand the text boundary, ensuring that

the text is not cropped when the Vortex is applied.

The Vortex is used to create swirling whirlpool effects.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Inspector

The Vector Distortion Controls tab

Controls Tab

The Controls tab contains parameters for adjusting the position, size, and strength of the Vortex effect.

Center X and Y

This control is used to position the center of the Vortex effect on the image. The default is 0.5, 0.5,

which positions the effect in the center of the image.

Size

Size changes the area affected by the Vortex. You can drag the circumference of the effect in the

viewer or use the Size slider.

Angle

Drag the rotation handle in the viewer or use the thumbwheel control to change the amount of rotation

in the Vortex. The higher the angle value, the greater the swirling effect.

Power

Increasing the Power slider makes the Vortex smaller but tighter. It effectively concentrates it inside

the given image area.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Warp nodes. These common controls are

described in detail in the following “The Common Controls” section.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

The Common Controls

Nodes that handle Warp operations share a number of identical controls in the Inspector. This section

describes controls that are common among Warp nodes.

Inspector

Warp Common Controls tab

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Warp category. The Settings

controls are even found on third-party Warp-type plugin tools. The controls are consistent and work

the same way for each tool.

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image.

Normally, this will cause the tool to skip processing entirely, copying the input straight to the output.

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This can be useful if the node is scripted to

trigger a task, but the node’s value is set to 0.0.


Fusion Page Effects | Chapter 123 Warp Nodes

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

Object ID affected is chosen using the Object and Material ID sliders explained below.

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


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Motion Blur

�Motion Blur: This toggles the rendering of Motion Blur on the tool. When this control is toggled

on, the tool’s predicted motion is used to produce the motion blur caused by the virtual camera’s

shutter. When the control is toggled off, no motion blur is created.

�Quality: Quality determines the number of samples used to create the blur. A quality setting of 2

will cause Fusion to create two samples to either side of an object’s actual motion. Larger values

produce smoother results but increase the render time.

�Shutter Angle:L Shutter Angle controls the angle of the virtual shutter used to produce the motion

blur effect. Larger angles create more blur but increase the render times. A value of 360 is the

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


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION