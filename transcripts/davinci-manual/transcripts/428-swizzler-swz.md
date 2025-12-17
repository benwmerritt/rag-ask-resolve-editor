---
title: "Swizzler [Swz]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 428
---

# Swizzler [Swz]

The Swizzler node

Swizzler Node Introduction

This tool enables you to combine one or more image layers and/or channels into a custom-made layer

or layers. Similar to Channel Booleans, Swizzler can assign channels from a source and apply them to

a destination channel, however, the biggest point of difference is that Swizzler utilizes layers, either

targeting layers as a source or creating new layers.

To put it simply, this tool has the functionality to create new layers, push source layers or channels to a

layer, or remove channels from a source.

Inputs

The Swizzler tool uses multiple inputs.

Input 1: This orange input is connected from a node with image data that you want to combine into a

new layer.

Input X: The white inputs are connected from additional nodes with image data that you want to

combine into a new layer.

Basic Node Setup

The Swizzler node receives multiple nodes with image data and combines them into new layers.

Swizzler combines multiple images into new layers.


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION

Inspector

Swizzler controls

Controls Tab

The Controls tab includes parameters for selecting layers to be used.

�Layer List: The layer list allows you to view and select custom layers. The button below allows you

to add a new layer to this list, introducing a new custom layer. For any layer selected in this list, the

options below allow you to choose which channels to include in the layer. Additionally, you can

rename layers directly in this list.

�Add Layer: This creates a new layer, adding it to the layer list.

�Keep Main Input Layers: Checking this box preserves existing layers from the source clip

connected to Input1. Having this enabled will pass the layers from Input1 to the Swizzler output,

giving you the control to add more layers to an existing multilayer source.

�Channels: This control allows you to select which channels will be added to the selected layer in

the layer list.

�All Channels: Transfers all channels into the selected layer.

�Color/Aux: Reveals an additional "Color" and "Aux" options, separating RGBA from AUX channels.

This separation allows you to nominate a source for the RGBA and a source for the AUX channels,

ultimately combining RGBA from one input and AUX from another input. The other two options,

“RGB/A“ and “R/G/B/A,” provide even further granular controls for channels, expanding the source

options for individual channels.

�Source: Select an input from this drop-down to source layers or channels for your chosen layer.

Your chosen layer will be the one selected in the layer list above.

�Source Layer: When using a multi-layer file connected to one of the inputs, you can choose a specific

layer using this control. All the available layers from the Source Input control will be displayed.

�Source Channels (Color/Aux mode): Select which channels from the chosen layer you would like

to use for the Aux channel. If the chosen layer doesn't have Aux channels and has been rendered

with only RGB, then select the color channels (i.e., RG for UV Texture or RGB for XYZ Normal).


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION

Examples

Assigning Aux channels

In the following example we have multiple RGB sources. Each one is a pre-rendered pass

which we want to assign to an Aux channel.

Connecting multiple RGB sources to the Swizzler

Each RGB pass is connected to a new input on the Swizzler.

Creating a new layer in the Swizzler


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION

A new layer has been added to the layer list, as there is only one layer, this will become the

new ‘default layer’

Assigning sources in the channel controls for the new layer

In the channel controls for the new layer, assign the appropriate source for each

of the Aux channels.

Previewing the new channels in the viewer

Once each of the Aux channels has been assigned an input, the channels can be previewed

in the viewer.


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION

Creating a multilayer clip

In this example, we have multiple RGB sources. Each one is a pre-rendered pass that we want

to assign to a new layer, creating a multilayer clip.

Connecting multiple RGB sources to the Swizzler

Each RGB pass is connected to a new input on the Swizzler.

Creating new layers in the Swizzler

In the layer list, add a new layer for every pass and give it a custom name. Select a layer in the

layer list, and in the controls assign the appropriate source input for that layer.


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION

For example, the UV pass has been connected to Input 4; selecting the custom layer labeled

“UV-Texture” and choosing Input 4 from the Input list will push all the channels from Input 4 to

the “UV-Texture” layer.

Selecting the new layers in the viewer

Once each of the inputs has been assigned a custom layer, these can be previewed in the

viewer and used in the comp.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Layer nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION