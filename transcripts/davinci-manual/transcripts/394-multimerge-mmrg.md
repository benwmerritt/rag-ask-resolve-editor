---
title: "MultiMerge [MMrg]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 394
---

# MultiMerge [MMrg]

The MultiMerge node

MultiMerge Node Introduction

The MultiMerge node allows you to combine several sources together in a layer-based structure.

Unlike the standard Merge tool, which only accepts one foreground input, MultiMerge creates a new

consecutive foreground input each time a new source is dragged to the tool.

These inputs are added to the Layer List in the Inspector and are displayed in a hierarchy from top

to bottom as a stack. The layers are arranged so the layer closest to the foreground is at the top of

the list, and the one closest to the background is at the bottom. Each layer has its own separate and

independent Merge controls (see the Merge node above) that appear in the lower half of the Inspector,

allowing you to individually adjust the position, size, composite modes, etc., for each source input.

As your composite increases in complexity, you can end up with a large amount of standard Merge

nodes scattered throughout the node tree. MultiMerge can be used to combine these Merge nodes

together, both as an organizational tool and allowing you to control the order of operations in a

layer-based, rather than a node-based environment. You could conceivably composite and organize

hundreds of separate layers using one MultiMerge node on your node tree.

A sky replacement composite requiring three separate Merge nodes (previous page) is

replaced by one single Multi Merge node (above). The pipe of the currently selected layer

in the Layer List has a slight glow applied (Actors node to MultiMerge node).


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

Inputs

The MultiMerge node provides these image inputs:

Background: The orange background input is for the first of the images you want to composite

together. You should connect the background input before connecting the foreground input.

Foreground: The foreground inputs are for each subsequent image you want to composite together,

which is typically a foreground subject that should be in front of the background. Connecting a pipe

from a new source onto the MultiMerge node automatically creates a new foreground input on the

node and a new layer in the Layer List. Foreground inputs are all colored white.

Effect Mask: (Optional) The effect mask input lets you mask a limited area of the output image to be

merged where the mask is white (where the foreground image shows in front of the background),

letting the background image show through by itself where the mask is black.

Basic Node Setup

MultiMerge nodes are typically connected in the following way, with multiple input images connected

to the foreground inputs, a background input, and the output connected to the next node in the

composition. In this example, the effect mask input is not used, as this is not typical.

A typical MultiMerge node structure in DaVinci Resolve

Resolution Handling

While you can connect images of any resolution to the background and foreground inputs of the

MultiMerge node, the image that’s connected to the background input determines the resolution

of the output.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

Inspector

The Layer List of the MultiMerge node. The input to

Layer 4 has been disconnected (strike through the

name) and disabled (unchecked). The Luma Key layer

is having its name changed, the Sky layer is disabled

(unchecked), while the Actors layer is enabled (checked).

Layer List

For each foreground input connected to the MultiMerge node, a new layer is created sequentially in

the Layer List. The Layer List is hierarchically sorted from top to bottom, with layers on top being above

any layers below them in the image. You can customize this layer structure in several ways.

To Select a Layer:

Click on the layer in the Layer List to make that layer active. The active layer’s Merge controls will

appear at the bottom of the Inspector, and the pipe connecting to the layer’s input on the MultiMerge

node will glow slightly in the node tree.

You can multi-select layers by holding the Shift key down while clicking to select a range of layers, or

the Command key to select multiple non-adjacent layers.

Right-clicking on any layer opens up a contextual menu with the following options:

�Go To Source: Selects the tool that is connected to the layer’s input on the MultiMerge node and

opens the tool’s parameters in the Inspector.

�Split Here: Automatically creates another connected MultiMerge node and splits the existing

layers between the two. The layer that was selected for the split, and all layers above it, will be

spun off into a new MultiMerge node. The original MultiMerge node will be connected to the

background input of the new MultiMerge node.

�Rename Layer X: Opens up a dialog box allowing you to rename the selected layer.

�Rename Layer to Match Source: Automatically changes the name of the layer to the name of the

tool it’s connected to.

�Set Layer X to Default: This resets the layer’s merge settings below, back to the default.

�Delete Layer: This deletes the layer entirely from the Layer List and disconnects the pipe from the

original tool. It does not delete the original tool.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

To Move a Layer up or down the List:

Click and drag on the Layer name and move it up or down the list. A grey line will highlight where in

the list the layer will now be placed. Let go of the mouse button to make the change.

To Rename a Layer:

By default each layer is named based in the input tool’s name. To change the Layer’s name to

something more meaningful, double-click on the Layer’s name and type a new name in the text field.

You can also right-click on a Layer’s name and select Rename Layer from the contextual menu.

To Disable/Enable a Layer:

Checking or unchecking the box next to the Layer’s name will enable or disable that layer respectively.

Disabling the layer turns off that input’s contribution to the overall composite in the MultiMerge but

does not delete it.

To Replace a Layer:

By design, if you disconnect the pipe from a the MultiMerge’s input, the layer will still remain in its

place in the Layer List but with a strike-through its name to let you know that nothing is currently

connected. This allows you to quickly iterate and audition several input sources (clips, graphics, etc.) to

the same layer without having to constantly rearrange the order of your Layer List.

Keyframing the Layer List:

The Layer List itself is keyframable, using the standard keyframe controls to the right of the list.

Parameters that can be keyframed are layer order, and layer enable and disable.

Merge Controls

Each layer has a separate and independent set of Merge controls that appear here when the layer is

selected. For detailed information on how the Merge controls work, see the previous section in this

chapter titled Merge [Mrg].


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

The Common Controls

The Merge, MultiMerge, and Dissolve nodes share several identical controls in the Inspector.

This section describes controls that are common among those two nodes.

Inspector

Merge Setting Inspector

Settings Tab

The Settings tab in the Inspector can be found on both tools in the Composite category. The Settings

controls are even found on third-party color type plugin tools. The controls are consistent and work

the same way for each tool, although some tools do include one or two individual options that are also

covered here.

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image.

Normally, this will cause the tool to skip processing entirely, copying the input straight to the output.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This can be useful if processing of this node

is scripted to trigger another task, but the value of the node is set to 0.0.

Red/Green/Blue/Alpha Channel Selector

These four buttons are used to limit the effect of the tool to specified color channels. This filter is often

applied after the tool has been processed.

For example, if the red button on a blur tool is deselected, the blur will first be applied to the image,

then the red channel from the original input will be copied back over the red channel of the result.

There are some exceptions, such as tools for which deselecting these channels causes the tool to

skip processing that channel entirely. Tools that do this will generally possess a set of identical RGBA

buttons on the Controls tab in the tool. In this case, the buttons in the Settings and the Controls

tabs are identical.

Apply Mask Inverted

Enabling the Apply Mask Inverted option inverts the complete mask channel for the tool. The mask

channel is the combined result of all masks connected to or generated in a node.

Multiply by Mask

Selecting this option will cause the RGB values of the masked image to be multiplied by the mask

channel’s values. This will cause all pixels of the image not in the mask (i.e., set to 0) to become

black/transparent.

Use Object/Use Material (Checkboxes)

Some 3D software can render to file formats that support additional channels. Notably, the EXR file

format supports Object and Material ID channels, which can be used as a mask for the effect. These

checkboxes determine whether the channels will be used, if present. The specific Material ID or

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

Use these sliders to select which ID will be used to create a mask from the object or material channels

of an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the view. The image or sequence must have been rendered from a 3D software package

with those channels included.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

Use GPU

The Use GPU menu has three settings. Setting the menu to Disable turns off hardware-accelerated

rendering using the graphics card in your computer. Enabled uses the hardware. Auto uses a capable

GPU if one is available and falls back to software rendering when a capable GPU is not available

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

�Center Bias: Center Bias modifies the position of the center of the motion blur. This allows the

creation of motion trail effects.

�Sample Spread: Adjusting this control modifies the weighting given to each sample. This affects

the brightness of the samples.

Layers

�Process Layers: Select the layer to process for effects from:

�Default Layer (default) - To apply the effect on the base/unnamed layer,

not affecting other layers.

�All Layers - To apply the effect on all available layers.

�Custom - Choice of other available layers to apply the effect on, not affecting other layers.

�Input Layer: The Input Layer lists all layers available from the upstream node of the default input.

The selected layer can be used by the current tool or farther down the node tree in isolation.

�Effect Mask Layer: If the tool has an Effect Mask input, this control lists the available layers that

can provide mattes for the tool.

Comments

The Comments field is used to add notes to a tool. Click in the field and type the text. When a note

is added to a tool, a small red square appears in the lower left corner of the node when the full tile is

displayed or a small text bubble icon appears on the right when nodes are collapsed. To see the note

in the node editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more details on scripting

nodes, please consult the Fusion scripting documentation.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION