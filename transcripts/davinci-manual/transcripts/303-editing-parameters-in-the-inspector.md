---
title: "Editing Parameters in the Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 303
---

# Editing Parameters in the Inspector

To improve an effect, you can make an adjustment to a node’s parameters in the Inspector at the

right. The selected node shows its controls in the Inspector, in which most nodes have several tabs of

controls seen as little icons just underneath that node’s title bar.

The Inspector showing the parameters of the TV effect

Clicking the last panel on any node opens the Settings panel. Every node has a Settings panel, and

this is where the parameters that every node shares, such as the Blend slider and RGBA buttons, are

found. These let you choose which image channels are affected, and let you blend between the effect

and the original image.

The Settings panel, which includes channel limiting

and mask handling controls that every node shares

In the case of the TV effect, for example, the resulting image has a lot of transparency because

the scan lines being added are also being added to the alpha channel, creating alternating lines of

transparency. Turning off the Alpha checkbox results in a more solid image, while opening the Controls

tab (the first tab) and dragging the Scan Lines slider to the right to raise its value to 4 creates a more

visible television effect.

The original TV effect (left), and modifications to the TV effect to make the clip more solid (right)


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

Replacing Nodes

In the Effect category of the Effects Library, you’ll also find a Highlight node that adds glints to the

highlights of an image.

Instead of clicking the Highlight node, which would add it after the currently selected node, dragging

and dropping a node from the Effects Library on top of a node in the Node Editor replaces the node in

the Node Editor.

Dragging a node from the Effects Library

onto a node in the Node Editor to replace it

In our example, the Highlight1 node takes the TV node’s place in the node tree, and the new effect can

be seen in the viewer, which in this example consists of star highlights over the lights in the image.

It’s time to use the Inspector controls to customize this effect.

Adjusting Fusion Sliders

When you drag a slider in the Fusion Inspector—in this case, the Number of Points slider—a little

dot appears underneath it. This dot indicates the position of the default value for that slider and also

serves as a reset button if you click it.

Adjusting a slider reveals a reset button underneath it

Each slider is limited to a different range of minimum and maximum values that is particular to the

parameter you’re adjusting. In this case, the Number of Points slider maxes out at 24. However, you

can remap the range of many (but not all) sliders by entering a larger value in the number field to the

right of that slider. Doing so immediately repositions the slider’s controls to the left as the slider’s range

increases to accommodate the value you just entered.

Entering a larger value to expand the range over which a slider will operate


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

Compositing Two Clips Together

As entertaining as it is adding individual nodes to create simple effects, eventually you’ll need to

start adding additional layers of media in order to merge them together as composites. Let’s turn our

attention to another example in which we need to combine a background clip with a foreground clip

that includes a built-in alpha channel, to see simple layering in action.

Adding Additional Media to Compositions

You’ll often find that even though you start out wanting to do something relatively simple, you end up

adding additional media to create the effect that you need.

�In Fusion Studio, you do this by adding additional Loader nodes. If you add a new Loader node to

an empty area of the Node Editor, you’ll add an unconnected Loader2 node (incremented to keep

it unique) that you can then connect how you want.

�In the Fusion page, you can open the Media Pool and drag clips directly to the Node Editor to add

them to your node tree. If you drag a clip from the Media Pool to an empty area of the Node Editor,

you’ll add an unconnected MediaIn2 node (incremented to keep it unique) that you can then

connect in any way you want.

The Media Pool as seen in the Fusion page


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

Automatically Creating Merge Nodes

If you want to connect the incoming clip immediately to your node tree as the top layer, or foreground,

of a composite, in Fusion Studio select the Loader1 node and then add a second Loader node. In the

Fusion page, drag the new clip from the Media Pool right on top of any connection line.

In both cases, the new MediaIn or Loader node automatically becomes the “foreground input”.

Dragging a node from the Media Pool onto a connection (left), and dropping it to create a Merge node composite (right)

The Node Editor is filled with shortcuts like this to help you build your compositions more quickly.

Here’s one for when you have a disconnected node that you want to composite against another node

with a Merge node. Drag a connection from the output of the node you want to be the foreground

layer, and drop it on top of the output of the node you want to be the background layer. A Merge node

will be automatically created to build that composite. Remember: background inputs are orange, and

foreground inputs are green.

Dragging a connection from a disconnected node to another node’s output

(left), and dropping it to create a Merge node composite (right)

Adding Clips to a Fusion Composition From the File System

If you drag clips from the file system directly into the Node Editor, they’ll be added to

the DaVinci Resolve Media Pool automatically. So, if you have a library of stock animated

background textures and you’ve just found one you want to use using your file system’s

search tools, you can simply drag it straight into the Node Editor and it’ll be added to the

currently selected bin of the Media Pool.

Fixing Problem Edges in a Composite

Most often, the Merge node does a perfectly good job when handed a foreground image with

premultiplied alpha transparency to composite against a solid background image. However, from time

to time, you may notice a small bit of fringing at the edge of the border of a foreground element and

transparent area, such as seen in the following close-up. This slight lightening at the edge is a tell-tale

sign that the clip probably wasn’t premultiplied. The Merge node expects all foreground images with

alpha channels to be premultiplied. But this is something that’s easily fixed.


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

A bit of fringing at the edge of a foreground

element surrounded by transparency

Click to select the Merge node for that particular composite, and look for the Subtractive/

Additive slider.

The Subtractive/Additive slider, which can be used

to fix or improve fringing in composites

Drag the slider all the way to the left, to the Subtractive position, and the fringing disappears.

A clip with alpha exhibits fringing (left),

and after fixing fringing by dragging the

Subtractive/Additive slider to the left (right)

The Subtractive/Additive slider, which is only available when the Apply mode is set to Normal,

controls whether the Normal mode performs an Additive merge, a Subtractive merge, or a

blend of both. This slider defaults to Additive merging, which assumes that all input images

with alpha transparency are premultiplied (which is usually the case). If you don’t understand

the difference between Additive and Subtractive merging, here’s a quick explanation:

•	 An Additive merge, with the slider all the way to the right, is necessary when the foreground

image is premultiplied, meaning that the pixels in the color channels have been multiplied by

the pixels in the alpha channel. The result is that transparent pixels are always black, since

any number multiplied by 0 is always 0. This obscures the background (by multiplying with

the inverse of the foreground alpha), and then simply adds the pixels from the foreground.

•	 A Subtractive merge, with the slider all the way to the left, is necessary if the foreground

image is not premultiplied. The compositing method is similar to an Additive merge, but

the foreground image is first multiplied by its own alpha to eliminate any background pixels

outside the alpha area.

The Additive/Subtractive slider lets you blend between two versions of the merge operation,

one Additive and the other Subtractive, to find the best combination for the needs of your

particular composite. Blending between the two is occasionally useful for dealing with

problem composites that have edges that are calling attention to themselves as either too

bright or too dark.

For example, using Subtractive merging on a premultiplied image may result in darker edges,

whereas using Additive merging with a non-premultiplied image will cause any non-black

area outside the foreground’s alpha to be added to the result, thereby lightening the edges.

By blending between Additive and Subtractive, you can tweak the edge brightness to be just

right for your situation.


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION