---
title: "The Common Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 503
---

# The Common Controls

Nodes that handle Transform operations share several identical controls in the Inspector. This section

describes controls that are common among Transform nodes.

Inspector

The Transform Common controls

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Transform category. The Settings

controls are even found on third-party Transform-type plugin tools. The controls are consistent and

work the same way for each tool.

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


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

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


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

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


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Chapter 121

USD Nodes

This chapter details the Universal Scene Descriptor (USD) nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve

are interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Universal Scene Descriptor (USD) Files����������� 2817

USD Scene Tree Dialog for Object

Selection in USD Files��������������������������������������������� 2818

uCamera [uCa]�������������������������������������������������������������� 2819

uDuplicate [uDp]��������������������������������������������������������� 2822

uExport [uEx]����������������������������������������������������������������� 2827

uImage Plane [uIm]���������������������������������������������������� 2828

uLoader [uLd]��������������������������������������������������������������� 2830

uMaterialX [uMX]���������������������������������������������������������� 2831

uMerge [uMg]���������������������������������������������������������������� 2833

uRenderer [uRn]����������������������������������������������������������� 2834

uReplaceMaterial [uRM]������������������������������������������� 2837

uShape [uSh]����������������������������������������������������������������� 2840

uSwitch [uSw]���������������������������������������������������������������� 2843

uTransform [uXf]��������������������������������������������������������� 2845

uVariant [uVa]���������������������������������������������������������������� 2847

uVisibility [uVis]����������������������������������������������������������� 2848

uVolume [uVo]�������������������������������������������������������������� 2850

USD Lights

uCylinder Light [uCL]������������������������������������������������ 2852

uDisk Light [uDi]���������������������������������������������������������� 2853

uDistant Light [uDL]�������������������������������������������������� 2855

uDome Light [uDo]����������������������������������������������������� 2856

uRectangle Light [uRL]�������������������������������������������� 2858

uSphere Light [uSL]��������������������������������������������������� 2860

USD Material

uNormalMap [uNm]��������������������������������������������������� 2862

uShader [uSd]�������������������������������������������������������������� 2863

uTexture [uTx]��������������������������������������������������������������� 2866

uTextureTransform [uTXf]���������������������������������������� 2867

The Common Controls������������������������������������������� 2868


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Universal Scene Descriptor (USD) Files

The Universal Scene Descriptor USD framework is a set of open standards for describing, composing,

and simulating a 3D environment. The USD file format is more than just a simple format - it's an open

source 3D scene description used for creating and sharing 3D content across various applications.

DaVinci Resolve and Fusion can import USD (.usdc, .usdz, and .usda) 3D information including

geometry, lighting, cameras, materials, and animation. A new collection of USD tools has been added

to Fusion, allowing users to manipulate, re-light, and render these USD files.

The USD Loader

The uLoader allows you to import USD files and adjust its options.

The uLoader node

To Import a USD file:


Add a uLoader tool to your Fusion Composition.


Select the USD file you want to load in the File Browser. If you wish to change this file in the future,

you can do so in the uLoader Inspector without disrupting your node tree.


Connect the output of the uLoader to a uMerge tool.


Connect any other USD tools, like uCamera or any of the uLights, to manipulate the scene.


Connect the output of the uMerge tool to a uRenderer.


Connect the output of the uRenderer to the MediaOut tool.

A very simple USD import node tree


Fusion Page Effects | Chapter 121 USD Nodes

FUSION