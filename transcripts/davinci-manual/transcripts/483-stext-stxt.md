---
title: "sText [sTxt]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 483
---

# sText [sTxt]

The sText node

Introduction

Designed for the Fusion Shape environment, the sText node is an advanced character generator

capable of multiple styles, 3D transformations, and several layers of shading. The sText node is a

“Shape” version of the 2D Text+ node. The controls for this node are mostly identical to the controls for

the 2D version in almost all respects, except sText doesn’t support gradient colors.

The sText controls


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

sTransform

The sTransform node

The sTransform node is used to add an additional set of transform controls to the existing controls

that are contained in Shape nodes. These additional transforms can be used to create hierarchical

animations. For instance, you can use a sStar’s built-in Angle control to spin the star around. The star

can then be output to an sTransform node. The rotation control in the sTransform can be used to orbit

the star around the frame.

Like almost all Shape nodes, you can only view the sStar node’s results through a sRender node.

External Inputs

The following input appears on the node’s tile in the Node Editor:

Input1: [orange, required] This input accepts the output of another Shape node. The shape connected

to this input is moved, scaled, and rotated based on the sTransform settings.

Basic Node Setup

The sTransform node takes the input from another Shape node and adds another set of transforms

or hierarchical animation. The output of the sTransform can go into a sRender for viewing and

further compositing.

An sStar node connecting to an sTransform node, and then viewed using an sRender node

Inspector

The sTransform Controls tab

Controls

The Controls tab is used to define the add a set of transform controls to the incoming shape.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

X and Y Offset

These parameters are used to position the shape left, right, up, and down in the frame. The shape

starts in the center of the frame, and the parameters are used to offset the position. The offset

coordinates are normalized based on the width of the frame. So an X offset of 0.0 is centered and a

value of 0.5 places the center of the shape directly on the right edge of the frame.

X and Y Size

The X and Y Size determine the vertical and horizontal scaling of the incoming shape. If the values are

different then the shape will be skewed from its original design.

Rotation

The dial rotates the shape based on the pivot controls.

X and Y Pivot

These parameters position the axis of rotation for the incoming shape. The pivot point is visible in the

viewer as a red X. The X can be dragged in the viewer for positioning.

Transform Axis

Check this box to apply the transform to the shape’s axis.

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Common Controls

Nodes that handle Shape operations share a number of identical controls in the Inspector. This section

describes controls that are common amongst Shape nodes.

Settings Tab

The Settings tab in the Inspector can be found on every Shape node. Most of the controls listed here

are only found in the sRender node but a few are common to all Shape nodes.

Blend (sRender only)

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming. Normally,

this causes the tool to skip processing entirely, copying the input straight to the output.

Process When Blend Is 0.0 (sRender only)

The tool is processed even when the input value is zero. This can be useful if processing of this node

is scripted to trigger another task but the value of the node is set to 0.0.

Red/Green/Blue/Alpha Channel Selector (sRender only)

These four buttons are used to limit the effect of the tool to specified color channels. This filter is often

applied after the tool has been processed.

For example, if the red button on a Blur tool is deselected, the blur is first applied to the image, then

the red channel from the original input is copied back over the red channel of the result.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

There are some exceptions, such as tools where deselecting these channels causes the tool to skip

processing that channel entirely. Tools that do this generally possess a set of identical RGBA buttons on

the Controls tab in the tool. In this case, the buttons in the Settings and the Control tabs are identical.

Apply Mask Inverted (sRender only)

Enabling the Apply Mask Inverted option inverts the complete mask channel for the tool. The mask

channel is the combined result of all masks connected to or generated in a node.

Multiply By Mask (sRender only)

Selecting this option causes the RGB values of the masked image to be multiplied by the mask

channel’s values. This causes all pixels of the image not included in the mask (i.e., set to 0) to become

black/transparent.

Motion Blur (sRender only)

�Motion Blur: This toggles the rendering of motion blur on the tool. When this control is toggled

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

Use GPU (sRender only)

The user GPU menu has three settings. Setting the menu to Disable turns off hard accelerated

rendering using the graphics card in your computer. Auto uses a capable GPU if one is available and

falls back to software rendering when a capable GPU is not available.

Hide Incoming Connections

Enabling this checkbox can hide connection lines from incoming nodes, making a node tree appear

cleaner and easier to read. When enabled, empty fields for each input on a node will be displayed

in the Inspector. Dragging a connected node from the node tree into the empty field will hide that

incoming connection line as long as the node is not selected in the node tree.. When the node is

selected in the node tree the line will reappear.

Comments

The Comments field is used to add notes to a tool. Click in the empty field and type the text. When a

note is added to a tool, a small red square appears in the lower left corner of the node when the full

tile is displayed or a small text bubble icon appears on the right when nodes are collapsed. To see the

note in the Node Editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more information on

scripting nodes, see the Fusion scripting documentation.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Chapter 118

Stereo Nodes

This chapter details the Stereo nodes available in Fusion. Stereoscopic nodes are

available only in Fusion Studio and DaVinci Resolve Studio.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Anaglyph [Ana]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2701

Combiner [Com]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2705

Disparity [Dis]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2706

Disparity To Z [D2Z]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2710

Global Align [GA]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2714

New Eye [NE]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2716

Splitter [Spl]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2719

Stereo Align [SA]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2721

Z To Disparity [Z2D]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2726

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2729


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION