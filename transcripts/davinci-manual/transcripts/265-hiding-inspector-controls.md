---
title: "Hiding Inspector Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 265
---

# Hiding Inspector Controls

If you like, Inspector parameters for specific nodes can be hidden so they never appear, even

when that node is selected. This can be useful for preventing accidental changes by you or

other compositors who may be working on a composition in situations where you don’t want to

lock the node.

To Toggle the Inspector controls for a node or or off:

Right-click on the node in the Node Editor, or on the Inspector header, and choose Modes >

Show Controls from the contextual menu.

Using the Inspector Header

When you select a node, it populates the Inspector with a title bar, or Inspector header, that displays

that node’s name as well as other controls that govern that node. A node’s Inspector header itself

has a variety of controls, but clicking (or double-clicking) on an Inspector header also exposes that

node’s parameters.

A node’s Inspector header

When you select multiple nodes at once, you’ll see multiple headers in the Inspector. By default, only

the parameters for the active node (highlighted orange in the Node Editor) can be opened at any

given time, although you can change this behavior in Fusion’s Preferences.

Selecting and Viewing Nodes in the Inspector

Inspector headers are click targets for selecting nodes, opening and closing node parameters, and

other things.

Methods of using headers:

�To select a node using the Inspector header: When multiple nodes are selected, you can make

a node the active node by clicking its Inspector header in the Inspector. As the actively selected

node, the Inspector header and the corresponding node in the Node Editor are highlighted

orange, and its parameters are exposed.

�To load a node into the viewer using the Inspector header: You can view a node by dragging its

header into one of the viewers.

�To view a node’s splines with the control header: If you want to view the animated curves

of a node in the Spline Editor, you can add them by dragging the Inspector header into the

Spline Editor. All animated splines for the parameters of that node will automatically be displayed.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Using Header Controls

The controls found in each node’s Inspector header makes it fast to do simple things.

To turn nodes off and on: Each Inspector header has a toggle switch to the left

of its name, which can be used to enable or disable that node. Disabled nodes

pass image data from the previous upstream node to the next downstream node

without alteration.

To change the Inspector header name: The name of the node corresponding to

that Inspector header is displayed next. You can change the name by right-clicking

the Inspector header to expose contextual menu commands similar to those found

when you right-click a node in the Node Editor and choosing Rename. Alternatively,

you can click an Inspector header and press F2 to edit its name. A Rename dialog

appears, where you can enter a new name and click OK (or press Return).

To color-code nodes: A color pop-up menu lets you color code with one of 16 colors.

Choose Clear Color if you want to return that node to the default color.

To version nodes: Turning on the Versions button displays a Version bar

with six buttons. Versioning is described in the following section.

To pin Inspector controls: Clicking the Pin button “pins” that node’s parameters

in the Inspector so they remain in place, even if you deselect that node. You can

have as many pinned nodes as you like in the Inspector, but the more you have,

the more likely you’ll be scrolling up and down the Inspector to navigate all the

available parameters.

To lock nodes: Clicking the Lock button locks that node so no changes

can be made to it.

To reset Inspector controls: The rightmost button in the Inspector header is a Reset

button that resets the entire node to the default settings for that node.

Versioning Nodes

Each button is capable of containing separate parameter settings for that node, making it easy to save

and compare up to six different versions of settings for each node. All versions are saved along with

the node in the Node Editor for future use.

The Version bar, underneath an Inspector

header, with versions enabled

An orange underline indicates the currently selected version, which is the version that’s currently

being used by your composition. To clear a version you don’t want to use any more, right-click that

version number and choose Clear from the contextual menu.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Parameter Tabs

Underneath the Inspector header is a series of panel tabs, displayed as thematic icons. Clicking one of

these icons opens a separate tab of parameters, which are usually grouped by function. Simple nodes,

such as the Blur node, consist of two tabs where the first contains all of the parameters relating to

blurring the image, and the second is the Settings tab.

The parameter tabs of the Blur node

More complicated nodes have more tabs containing more groups of parameters. For example, the Delta

Keyer has seven tabs: separating Key, Pre-Matte, Matte, Fringe, Tuning, and Mask parameters, along

with the obligatory Settings tab. These tabs keep the Delta Keyer from being a giant scrolling list of

settings and make it easy to keep track of which part of the keying process you’re finessing as you work.

The parameter tabs of the Delta Keyer node

The Settings Tab

Every node that comes with Fusion has a Settings tab. This tab includes a set of standard controls

that appear for nearly every node, although some nodes have special Settings tab controls that

others lack.

The Settings tab in the Inspector


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

The following controls are common to most nodes, although some are node-specific. For example,

Motion Blur settings have no purpose in a Color Space node.

Blend

The Blend control is found in all nodes, except the Loader, MediaIn, and Generator nodes. It is used

to blend between the node’s unaltered image input and the node’s final processed output. When the

blend value is 0.0, the outgoing image is identical to the incoming image. Ordinarily, this will cause

the node to skip processing entirely, copying the input straight to the output. The default for this node

is 1.0, meaning the node will output the modified image 100%.

Process When Blend is 0.0

This checkbox forces the node to process even when the input value is zero and the image output

is identical to the image input. This can be useful on certain nodes or third-party plugins that store

values from one frame to the next. If this checkbox is disabled on nodes that operate in this manner,

the node will skip being processed when the Blend is set to 0, producing incorrect results on

subsequent frames.

Red/Green/Blue/Alpha Channel Checkboxes

Most nodes have a set of RGBA boxes in the Settings tab. These selectable boxes let you exclude any

combination of these channels from being affected by that node.

The channel limiting boxes in the Settings panel of a Transform

node set so that only the green channel is affected.

For example, if you wanted to use the Transform node to affect only the green channel of an

image, you can turn off the Red, Blue, and Alpha checkboxes. As a result, the green channel

is processed by this operation, and the red, blue, and alpha channels are copied straight from

the node’s input to the node’s output, skipping that node’s processing to remain unaffected.

Transforming only the green color channel of the image with a Transform effect


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Skipping Channel Processing

Under the hood, most nodes actually process all channels first, but afterward copy the input image

to the output for channels that have been unchecked. Modern workstations are so fast that this isn’t

usually noticeable, but there are some nodes where deselecting a channel actually causes that node

to skip processing that channel entirely. Nodes that operate this way have a linked set of Red, Green,

Blue, and Alpha boxes on another tab in the node.

Channel boxes on the Controls tab of the Blur node indicate that

disabled channels won’t be processed at all, to save rendering time..

In these cases, the Common Control channel boxes are instanced to the channel boxes found

elsewhere in the node. Blur, Brightness/Contrast, Erode/Dilate, and Filter are examples of nodes that

all have RGBY checkboxes in the main Controls tab of the Inspector, in addition to the Settings tab.

Apply Mask Inverted

When the Apply Mask Inverted checkbox is enabled, masks attached to the Effect Mask input of that

node are inverted.

TIP: The Apply Mask Inverted checkbox option operates only on effects masks, not on

garbage masks.

Multiply By Mask

Selecting this option will cause the RGB values of the masked image to be multiplied by the Mask

channel’s values. This will cause all pixels of the image not included in the mask (i.e., those set to 0) to

become black. This creates a premultiplied image.

Use Object/Use Material (For Masking)

Some 3D animation and rendering software can output to file formats that support auxiliary channels.

Notably, the OpenEXR file format supports Object ID and Material ID channels, either of which can be

used as a mask for an effect. This checkbox determines whether the channels will be used if they are

available. The specific Material ID or Object ID affected is chosen using the next set of controls.

�Sample Controls: The Sample Controls are only displayed once the Use Object or Use Material

checkbox is enabled. These controls select which ID is used to create a mask from the Object

or Material channels saved in the image. You use the Sample button to grab IDs from the image

in the viewer, the same way you use the Color Picker to select a color, by holding down the left

mouse button on the Sample button, then dragging over to the viewer to the part of the image you

want to select. The image or sequence must have been rendered from a 3D software package

with those channels included.

�Correct Edges: The Correct Edges checkbox is only displayed once the Use Object or Use

Material checkbox is enabled. When the Correct Edges checkbox is enabled, the Coverage and


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Background Color channels are used to separate and improve the effect around the edge of the

object. When disabled (or no Coverage or Background Color channels are available), aliasing may

occur on the edge of the mask.

Motion Blur

For nodes that are capable of introducing motion, such as Transform nodes, Warp nodes, and so

on, the Motion Blur checkbox toggles the rendering of motion blur on or off for that node. When this

checkbox is enabled, the node’s predicted motion is used to produce the blur caused by a virtual

camera shutter. When the control is disabled, no motion blur is created.

When Motion Blur is disabled, no additional controls are displayed. However, turning on Motion Blur

reveals four additional sliders with which you can customize the look of the motion blur you’re adding

to that node.

�Quality: Determines the number of samples used to create the blur. The default quality setting

of 2 will create two samples on either side of an object’s actual motion. Larger values produce

smoother results but will increase the render time.

�Shutter Angle: Controls the angle of the virtual shutter used to produce the Motion Blur effect.

Larger angles create more blur but increase the render times. A value of 360 is the equivalent of

having the shutter open for one whole frame exposure. Higher values are possible and can be

used to create interesting effects. The default value for this slider is 100.

�Center Bias: Modifies the position of the center of the motion blur. Adjusting the value allows for

the creation of trail-type effects.

�Sample Spread: Adjusting Sample Spread modifies the weight given to each sample. This affects

the brightness of the samples set with the Quality slider.

Scripting

Scripting fields are present on every node and contain one or more editable text fields that can be

used to add scripts that process when that node is rendering. For more information on the contents of

this tab, please consult the Scripting documentation.

Comments

A Comments field is found on every node and contains a single text field that is used to add comments

and notes to that node. To enter text, simply click within the field to place a cursor, and begin typing.

When a note is added to a node, the comments icon appears in the Control Header and can be seen

in a node’s tooltip when the cursor is placed over the node in the Node Editor. The contents of the

Comments tab can be animated over time, if required.

Additional controls appear under this tab if the node is a Loader. For more information, see

Chapter 104, “Generator Nodes.” In the DaVinci Resolve Reference Manual or Chapter 44 in

the Fusion Reference Manual.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION