---
title: "Cut, Copy, and Paste Nodes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 248
---

# Cut, Copy, and Paste Nodes

The standard operations of cut, copy, and paste are also available in the Node Editor. You can use

them to temporarily remove nodes from the Node Editor, create duplicate nodes, or even copy the

settings from one node and paste those settings into another node with compatible settings.

Cut, Copy, and Paste in the Node Editor

The standard commands all work, but with some special features specific to the Node Editor.

To copy one or more selected nodes, do one of the following:

�Right-click a node and choose Copy from the contextual menu.

�Choose Edit > Copy from the Edit menu (Command-C).

To cut one or more selected nodes, do one of the following:

�Right-click over the node and choose Cut from the contextual menu.

�Choose Edit > Cut from the Edit menu (Command-X).

When you paste into the Node Editor, you create a copy of the last node or nodes you’ve cut

or copied. When pasting, there are a few different things you can do to control where pasted

nodes appear.

To paste one or more selected nodes, do one of the following:

�To paste nodes to be inserted after another node: Select the node in the node tree you want to

insert the pasted node(s) to, and choose Edit > Paste (Command-V).

�To paste nodes to be disconnected from the rest of the node tree: Deselect all nodes, and then

choose Edit > Paste (Command-V), or right-click anywhere in the Node Editor and choose Paste

from the contextual menu.

�To paste disconnected nodes in a specific area of the Node Editor: Deselect all nodes, and

then click the place in the Node Editor where you want pasted node(s) to appear, and choose

Edit > Paste (Command-V), or right-click anywhere in the Node Editor and choose Paste from the

contextual menu.

�To paste a node to replace an existing node in the Node Editor: Right-click a node in the Node

Editor that you want to replace, choose Paste from the contextual menu, and when a dialog

appears asking if you want to replace that node, click OK. This only works when you use the

contextual menu command.

TIP: When you paste a MediaIn, Loader, or Generator node so it will be inserted after a

selected node in the node tree, a Merge tool is automatically created and used to composite

the pasted node by connecting it to the foreground input. While this can save you a few

steps, some artists may prefer to perform these sorts of merges manually, so this can be

changed using the Defaults panel in the Auto tools section of the Fusion > Fusion Settings.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Pasting Node Settings

Instead of pasting a node, you can choose to paste just the parameter settings that you copied from

another node. This can be useful if you’ve carefully set or animated parameters in one node that you

want to also use in another node.

Note that you can paste settings between two nodes of the same type, or between two entirely

different kinds of nodes that happen to have one or more of the same parameters in the Inspector.

When copying settings from one type of node to another, only the settings that match between two

nodes will be copied. A common example is to copy an animated Center parameter from a Transform

node to the Center parameter of a Mask node.

To Paste settings from one node to another:


Select a node that has settings you want to copy, and choose Copy from the

Edit menu (Command-C).


Right-click a node you want to paste those settings to, and choose Paste Settings

from the contextual menu.

Copying and Pasting Nodes to and from Any Text Editor

The format of nodes in the Node Editor is not binary, but is in fact a simple text format. The implications

of that may not be obvious, but one example benefit is clear when you start dealing with nodes.

One or more nodes can be copied from the Node Editor and pasted directly into a text editor or email.

This pastes the selection in text format, just as it’s saved internally in Fusion. For example, if you copy

the following set of three nodes:

A set of three nodes being copied.

And you then paste into a new text editing document, you get the following:

The same three nodes pasted into a text editor.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

At this point, you have the option of editing the text (if you know what you’re doing), emailing it to

colleagues, or storing it in a digital notepad of some sort for future use. To use this script in Fusion

again, you need only copy it and paste it back into the Node Editor.

TIP: This is a very easy way to pass specific node settings back and forth between artists

who may not be in the same room, city, or country.

Using Multilayer Nodes

(Studio Version Only)

Fusion can intelligently handle multilayer image workflows with support for EXR, Stereoscopic 3D,

and PSD assets. Users can see a list of layers on the Fusion viewers and interact with layers in each

node in the Settings tab in the Inspector. As this layer structure is retained throughout the toolset, this

means you can isolate a tool to work on an individual layer, while still passing through the other layers

unmodified.

Viewer

When loading a multilayer file, you can preview specific layers in the Viewer and select a layer

from the drop-down list. Files without layer support will show only a ‘default’ option from the

drop-down menu.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Using the Layer drop-down in the Viewer to select just the Asteroids layer from a multilayer file for viewing

Nodes and Inspector

In the Settings tab you’ll find a Layer category where you have access to a number of controls to affect

certain layers and to control layers from each tool input.

�Process Layers: Select the layer to process for effects from:

Default Layer (default): To apply the effect on the base/unnamed layer, not affecting other layers.

All Layers: To apply the effect on all available layers.

Custom: Choice of other available layers to apply the effect on, not affecting other layers.

�Input Layer: The Input Layer lists all layers available from the upstream node of the default input.

The selected layer can be used by the current tool or further down the node tree in isolation.

�Effect Mask Layer: If the tool has an Effect Mask input, this control lists the available layers that

can provide mattes for the tool.

Connecting the multilayer file, both directly to the BrightnessContrast

Effect Mask (blue arrow) in addition to its input, allows you

to quickly create perfect masks of any layer in the file.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Tools with other named inputs (like Image) can show additional layer controls with a

corresponding name (like Image Layer).

Input Layer Controls

For optimal performance, Fusion tools request only the processed layers from each input. The Input

Layer, Effect Mask Layer, Image Layer and other input layer controls allow the user to customize this

behavior. In each input control, you can select Auto or Match or select an explicit layer value to map:

�Auto (Default): Requests the layer selected in the Process Layers selection. If the layer does not

exist, the tool falls back to the default layer.

�Match: Requests the layer selected in the Process Layers selection. If the layer does not exist,

the tool shows a failure.

�Explicit Layer Selection: Requests the explicit layer selection from one of the listed layers.

This isolates the specific layer for use in the current tool or further down the node tree.

For Fusion plugins, the Process Layer and Input Layer controls are automatically generated in

the Inspector’s Settings tab. Creators of plugins can decide to define and place the controls

explicitly in another place, similar to how the MultiMerge places the controls in the main

controls section.

Some Fusion tools include controls to handle additional layer-based decisions.

For example:

•	 The Renderer3D shows a new Eye control > Layers option when using a stereoscopic

camera, allowing the left and right eyes to be output as individual layers.

•	 When combining multilayered sources using composite nodes (e.g., MultiMerge),

Channel Booleans, or a MatteControl, the Settings tab has additional controls to select

Background or Foreground options to isolate and combine the selected layers.

•	 The Combiner tool can be used to create custom layers. Set the Mode to Layer.

This exposes layer name fields allowing you to name the new layers.

Instancing Nodes

Normally, when you use copy and paste to create a duplicate of a node, the new node is completely

independent from the original node, so that changes made to one aren’t rippled to the other. However,

there are times when two nodes must have identical settings at all times. For example, when you’re

making identical color corrections to two or more images, you don’t want to constantly have to adjust

one color correction node and then manually adjust the other to match. It’s a hassle, and you risk

forgetting to keep them in sync if you’re working in a hurry.

While there are ways to publish controls in one node and connect them to matching controls in

another node, this becomes prohibitively complex and time consuming for nodes in which you’re

making adjustments to several controls. In these cases, creating “instanced” nodes is a real time-saver,

as well as an obvious visual cue in your node tree as to what’s going on.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION