---
title: "Basic Node Setup"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 379
---

# Basic Node Setup

The Vari Blur node receives a 2D image like the MediaIn1 shown below. A gradient Background tool

connects to the Blur image input to control the areas affected by the blur. The output continues the

node tree by connecting to another 2D image-processing node or a Merge node.

A Vari Blur node applied to a MediaIn1 node and a

gradient background directing the blurred regions

Inspector

Vari Blur controls

Controls Tab

The Controls tab contains all the primary controls necessary for customizing the Vari Blur operation.

Method

Use this menu to select the method of Blur used in the filter. The selections are described below.

�Soften: This method varies from a simple Box shape to a Bartlett triangle to a decent-looking

Smooth blur as Quality is increased. It is a little better at preserving detail in less-blurred areas

than Multi-box.

�Multi-box: Similar to Soften, this gives a better Gaussian approximation at higher Quality settings.

�Defocus: Produces a flat, circular shape to blurred pixels that can approximate the

look of a defocus.

Quality

Increasing Quality gives smoother blurs, at the expense of speed. Quality set to 1 uses a very fast

but simple Box blur for all Method settings. A Quality of 2 is usually sufficient for low Blur Size values.

A Quality of 4 is generally good enough for most jobs unless Blur Size is particularly high.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Blur Channel

This selects which channel of the Blur Image controls the amount of blurring applied to each pixel.

Lock X/Y

When selected, only a Blur Size control is shown, and changes to the amount of blur are applied to

both axes equally. If the checkbox is cleared, individual controls appear for both X and Y Blur Size.

Blur Size

Increasing this control increases the overall amount of blur applied to each pixel. Those pixels where

the Blur image is black or nonexistent are blurred, despite the Blur Size.

Blur Limit

This slider limits the useable range from the Blur image.  Some Z-depth images can have values that

go to infinity, which skew blur size. The Blur Limit is a way to keep values within range.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Blur nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Vector Motion Blur [VMB]

The Vector Motion Blur node

Vector Motion Blur Introduction

This node is used to create directional blurs based on a Motion Vector map or AOV (Arbitrary Output

Variable) channels exported from 3D-rendering software like Arnold, Renderman, or VRay. You can

also generate motion vectors using the Optical Flow node in Fusion.

The vector map is typically two floating-point images: one channel specifies how far the pixel

is moving in X, and the other specifies how far the pixel is moving in Y. These channels may be

embedded in OpenEXR or RLA/RPF images, or may be provided as separate images using the node’s

Vectors input.

The vector channels should use a float16 or float32 color depth, to provide + and – values.

A value of 1 in the X channel would indicate that pixel has moved one pixel to the right, while a value of

–10 indicates ten pixels of movement to the left.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Inputs

The Vector Motion Blur node has three inputs for a 2D image, a motion vector pass, and an

effect mask.

Input: The required orange input is for a 2D image that receives the motion blur.

Vectors: The green input is also required. This is where you connect a motion vector AOV rendered

from a 3D application or an EXR file generated from the Optical Flow node in Fusion.

Vector Mask: The white Vector Mask input is an optional input that masks the image before

processing.

Effect Mask: The common blue input is used for a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input restricts the source

of the motion blur to only those pixels within the mask. An effect mask is applied to the tool after it is

processed.

Basic Node Setup

The Vector Motion Blur node receives a 2D image like the IMAGE shown below. A MediaIn or Loader

node containing motion vectors is connected to the Vector’s input. The output continues the node

tree by connecting to another 2D image-processing node or a Merge node.

A Vector Motion Blur node applied to a MediaIn or Loader

node with motion vectors connected to the Vectors input

Inspector

Vector Motion Blur node

Controls Tab

The Controls tab contains all the primary controls necessary for customizing the Vector Motion

Blur operation.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

X Channel

Use this menu to select which channel of the image provides the vectors for the movement of the

pixels along the X-axis.

Y Channel

Use this menu to select which channel of the image provides the vectors for the movement of the

pixels along the Y-axis.

Flip Channel

These checkboxes can be used to flip, or invert, the X and Y vectors. For instance, a value of 5 for a

pixel in the X-vector channel would become –5 when the X checkbox is enabled.

Lock Scale X/Y

Selecting this checkbox provides access to separate sliders for X and Y Scale. By default, only a single

Scale slider is provided.

Scale

The X and Y vector channel values for a pixel are multiplied by the value of this slider. For example,

given a scale of 2 and a vector value of 10, the result would be 20. This slider splits to show Scale X

and Scale Y if the Lock Scale X/Y checkbox is not enabled.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Blur nodes. These common controls are

described in the following “The Common Controls” section.

The Common Controls

Nodes that handle blur operations share several identical controls in the Inspector. This section

describes controls that are common among Blur nodes.

Inspector

Common Blur settings


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Blur category. The Settings controls

are even found on third-party Blur-type plugin tools. The controls are consistent and work the same

way for each tool.

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

For example, if the Red button on a Blur tool is deselected, the blur is first applied to the image, and

then the red channel from the original input is copied back over the red channel of the result.

There are some exceptions, such as tools where deselecting these channels causes the tool to

skip processing that channel entirely. Tools that do this generally possess a set of identical RGBA

buttons on the Controls tab in the tool. In this case, the buttons in the Settings and the Controls tabs

are identical.

Apply Mask Inverted

Enabling the Apply Mask Inverted option inverts the complete mask channel for the tool. The mask

channel is the combined result of all masks connected to or generated in a node.

Multiply by Mask

Selecting this option causes the RGB values of the masked image to be multiplied by the mask

channel’s values. This causes all pixels of the image not in the mask (i.e. set to 0) to become

black/transparent.

Use Object/Use Material (Checkboxes)

Some 3D software can render to file formats that support additional channels. Notably, the EXR file

format supports object and material ID channels, which can be used as a mask for the effect. These

checkboxes determine whether the channels are used, if present. The specific material ID or object ID

affected is chosen using the next set of controls.

Correct Edges

This checkbox appears only when the Use Object or Use Material checkboxes are selected. It toggles

the method used to deal with overlapping edges of objects in a multi-object image. When enabled,

the Coverage and Background Color channels are used to separate and improve the effect around

the edge of the object. If this option disabled (or no Coverage or Background Color channels are

available), aliasing may occur on the edge of the mask.

For more information on the Coverage and Background Color channels, see Chapter 78,

“Understanding Image Channels,” in the DaVinci Resolve Reference Manual, or Chapter 18

in the Fusion Reference Manual.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Object ID/Material ID (Sliders)

Use these sliders to select which ID is used to create a mask from the object or material channels

of an image. Use the Sample button in the same way as the Color Picker to grab IDs from the image

displayed in the viewer. The image or sequence must have been rendered from a 3D software

package with those channels included.

Use GPU

The GPU menu has three settings. Disable turns off GPU hardware accelerated rendering. Enabled

uses the GPU hardware for rendering the node. Auto uses a capable GPU if one is available and falls

back to software rendering when a capable GPU is not available.

Motion Blur

�Motion Blur: This toggles the rendering of Motion Blur on the tool. When this control is toggled

on, the tool’s predicted motion is used to produce the motion blur caused by the virtual camera’s

shutter. When the control is toggled off, no motion blur is created.

�Quality: Quality determines the number of samples used to create the blur. A Quality setting of

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


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION