---
title: "Image Processing Within Grades"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 599
---

# Image Processing Within Grades

For Pre-Clip, Clip, Post-Clip, and Timeline grades on the Color page, most Color page operations are

available within each Corrector node you add to the Node Editor. Within each node, these operations

take place in the following specific order.

The order of image processing operations that takes place within each Corrector node in the Color page

Thanks to the modular operation of the Node Editor, if a pair of image processing operations you need

to use isn’t in the ideal order for what you’re trying to do, you can apply each operation using two

different nodes in order to force those operations into the order you want. Similarly, when using Layer,

Parallel, or Key mixer nodes, the order of operations can be seen in the visible arrangement of nodes

in your node graph.

That said, most colorists tend to spread different operations across multiple nodes, whether they need

to or not, for organizational purposes or to “sandbox” certain volatile decisions that might need to be

independently revised later. However, nothing’s keeping you from using multiple operations within a

single node if you prefer a simpler node structure for your grading. Thanks to the flexibility of the Color

page, it’s your choice.


Color | Chapter 144 Image Processing Order of Operations

COLOR

Chapter 145

Serial, Parallel,

and Layer Nodes

This chapter covers the four fundamental node structures you can use to combine

Color page adjustments in even more detailed ways. These methods let you

control your order of operations and re-combine multiple versions of the graded

image in much more specific ways.

Contents

Serial, Parallel, and Layer Node Tree Structures�������������������������������������������������������������������������������������������������������������� 3333

Serial Node Structures������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3333

Controlling What Feeds a Node’s RGB Input����������������������������������������������������������������������������������������������������������������������� 3333

Parallel Node Structures��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3334

Layer Mixer Node Structures������������������������������������������������������������������������������������������������������������������������������������������������������ 3336

Layer Mixer Prioritization���������������������������������������������������������������������������������������������������������������������������������������������������������������� 3336

Using Composite Modes With the Layer Mixer�������������������������������������������������������������������������������������������������������������������� 3337

Adjusting Layer Node Strength Using Key Output Gain������������������������������������������������������������������������������������������������ 3338

Converting Layer Mixers to Parallel Mixers�������������������������������������������������������������������������������������������������������������������������� 3339


Color | Chapter 145 Serial, Parallel, and Layer Nodes

COLOR

Serial, Parallel, and

Layer Node Tree Structures

There are several ways you can organize nodes in a tree. Each method lets you control a group of

image processing operations in different ways to achieve specific results. This section covers how to

use Serial nodes, Parallel nodes, and Layer nodes, as well as how to use LUTs, work with HDR media

that lets you combine two different exposures using two different Source inputs, and apply additional

project-wide adjustments using the Timeline grade.

Serial Node Structures

The simplest, and most common node structure is a serial cascade of nodes, where a linear series of

nodes is connected, one after another.

Serial nodes, where the output of one node feeds an altered image to the next

Much of the time, this method of constructing a tree of multiple operations is all you need to do. It’s a

simple and intuitive way of organizing your adjustments, similar in principle to the stacks of layers used

in other grading and compositing applications to apply multiple operations to a clip.

Controlling What Feeds a Node’s RGB Input

When you create a grade using serially arranged nodes, each node’s output is used as the

next node’s input, so the order in which the nodes are arranged determines the order of image

processing operations.

In the following screenshot, the node tree shows a series of three operations that are applied to a

log-exposed, low-contrast clip. The first node expands clip contrast and increases saturation. The

second node isolates the sky to intensify its color. The third desaturates and warms the image.

At right, you can see the result of this node tree.

Node 2 pulls a clean key from the image data fed it by Node 1

If, instead, we reversed the order of Nodes 2 and 3, the result will be a less effective key.


Color | Chapter 145 Serial, Parallel, and Layer Nodes

COLOR

By comparison, Node 3 pulls a less then optimal key

from the image data fed it by Node 2

Because the secondary operation is sampling the desaturated image, rather than the source, the HSL

Qualifier’s key has less image data to work with, and thus you may get an inferior result.

Parallel Node Structures

Another way to organize your corrections is to use a Parallel node structure, which lets you apply

two or more overlapping adjustments at a single stage of a node tree. You can use the Parallel

node structure for organizational reasons when there is a group of secondary corrections that you

want to apply all at once. You can also use this structure for the unique way it blends overlapping

image adjustments.

The Parallel Mixer node that makes this possible has multiple RGB inputs and a single RGB output.

This lets the Parallel Mixer mix together multiple Corrector nodes, outputting a single image

as a result.

When you add a Parallel node to an existing node, DaVinci Resolve automatically adds one Corrector

node below the current node, and adds a Parallel Mixer node to its output.

Adding a Parallel node to Node 2 automatically adds the Parallel Mixer

TIP: If you want to create a series of Parallel nodes that connect to the output of the currently

selected node, create a Serial node before you create your first Parallel node.

If you’re manually connecting another node to a Parallel Mixer node, you can drag from the output of

the node to the Parallel Mixer node, and it will automatically add an input for you.


Color | Chapter 145 Serial, Parallel, and Layer Nodes

COLOR

To create an additional, unconnected input on a Parallel Mixer node:

�Right-click a Parallel Mixer node and choose Add One Input.

Ordinarily, the RGB input of every Corrector node that’s connected to a Parallel node is

connected to the output of the same node. This results in a stack of nodes that take the same

state of the image as their input. This makes it easy to apply multiple secondary operations

without worrying about whether or not a change to one will affect the keys of the others.

Further Parallel nodes can be added as

you wish with each using a common source

If you add another node in parallel, the Parallel Mixer automatically adds another input. You can have

as many nodes in parallel as you need.

The adjustments made by all nodes that are connected to a Parallel Mixer are combined equally,

regardless of which nodes are highest. In the following example, a separate overlapping window is

applied by each of three nodes in parallel.

The Parallel Mixer blends all input nodes together

As you can see in the image at right, the three tints created by the overlapping windows are all mixed

together equally; the colors blend with one another as if they are optically mixed. Most of the time, this

is exactly what you want when you’re blending overlapping naturalistic color adjustments.


Color | Chapter 145 Serial, Parallel, and Layer Nodes

COLOR

Converting Parallel Mixers to Layer Mixers

On the other hand, if you need your overlapping color adjustments to have priority over one another,

or if you want to combine multiple adjustments using composite modes, then you may want to use the

Layer Mixer node instead. If you’ve created a Parallel Mixer structure and you want to convert it to a

Layer Mixer, you can.

To change a Parallel Mixer node into a Layer Mixer node:

�Right-click a Parallel Mixer node and choose Morph Into Layer Mixer Node.