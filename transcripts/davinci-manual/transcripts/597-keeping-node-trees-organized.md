---
title: "Keeping Node Trees Organized"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 597
---

# Keeping Node Trees Organized

It’s a good idea to keep the arrangement of your nodes in the node graph clean and neat. It’ll make it

easier to read your tree if you need to revisit a grade later on, and it will also make it easier for other

colorists working on the same project to figure out what you’re doing. The following procedures

describe how to rearrange the nodes in your tree, and the node tree working area, to help you keep

on top of your grades.

To move nodes within the Node Editor:

�Drag any node to a new position.

�Command-click or drag a bounding box around multiple nodes that you want to move, and drag

them all to a new position.

Of course, it’s easy to get carried away. If you’ve been working furiously on a complex grade and you

find yourself staring at a riot of disorganized nodes, it’s easy to quickly reorganize your node graph

using a pair of commands in the Node Editor contextual menu.

To clean up the node graph, right-click the Node Editor and choose:

�Cleanup Node Graph: Moves all nodes in the node graph so they appear in an evenly spaced

grid. Connection lines are routed around nodes to minimize clutter.

Before/after using “Cleanup Node Graph”


Color | Chapter 143 Node Editing Basics

COLOR

If your grading has gotten only slightly out of control, you can use the Cleanup Node Graph command

on multiple clips at the same time. To do so, select the clips whose node graphs you want to tidy up in

the thumbnail timeline, then right-click in on of their node graphs and choose “Cleanup Selected Node

Graphs” from the drop-down menu. This will perform a Cleanup Node Graph operation on all selected

clips at the same time.

Track Node Changes Using Color

The Color Page node graph (3-dot) option menu has an option to Track Node Changes Using Color.

This is a per system setting where the you choose the node color you want to apply to newly created

or modified nodes.

In a multi-user collaboration environment, each colorist can set their own preassigned node color.

Then, based on the node color, you can easily know who last modified a specific node. In single user

scenarios, this feature can be used to track changed nodes and grades after a particular point in time,

such as a client review session.

Selecting Track Node Changes Using Color from the Node Graph option menu will subsequently

change the color bar on a node after any modification made to that node. In this case, the

Highlights node’s color bar is now Violet after the Violet user has made a change to it.

Additionally, you can filter timeline clips by their node colors as well. To do this simply click the

Down Arrow in the Clips tab, hover over Node Color, and select the color you wish to filter by

clicking on it. You can repeat this process to filter multiple colors.

When set, only the clips that have the selected node colors will appear in the timeline.


Color | Chapter 143 Node Editing Basics

COLOR

Using Node Stack Layers

Node Stack Layers allow the management of complex grading workflows by creating multiple

sequential node graphs that let you break up grades into separate sections. This allows users to

isolate related functions like stabilization, corrections, hero grades, and display trims into individual

node layers.

Grade operations like ripple, reset, and editing can also be done on a per-layer basis. When

you grab a still to the Gallery, all of the Node Stack Layers are saved as part of that still.

Since Node Stack Layers are applied sequentially (in order from lowest to highest), you can

also use them as highly customizable re-usable filters for your grades.

The Node Stack Layers number and naming options in the Project Settings

From Project Settings > General Options > Node Stack Layer Count, users can set the

number of clip node layers. You can also add custom names to the layers such as “primaries,”

“secondaries,” “finishers,” etc.

NOTE: If for some reason you return to the settings and lower the amount of node stack

layers later, all the grades in those layers are removed across your entire project. To get them

back, simply add the layer numbers back in.

The Node Stack Layer is navigated by clicking on the dots above the node graph

or selecting the name of the active layer from the drop-down menu to the right.

Users can then select individual layers from the navigation dots above the node graph or from the

layer drop-down menu to the right.


Color | Chapter 143 Node Editing Basics

COLOR

IMPORTANT: All node layers are applied sequentially to the clip: pre-clip, L1, L2, L3, L4, post-

clip, and then Timeline.

Copying Node Stack Layers

You can copy (not just apply) the Active Node Stack layer from a Timeline Clip in the Gallery. To do so,

right-click on a Timeline Clip in the Gallery and select Copy Active Layer.

Post Group Node Stack Layer

In Project Settings under General Options > Color, there is a checkbox called Post Group Node Stack

Layer. When you enable this checkbox, the last node stack layer is processed after the Group Post-

Clip node graph. This function allows you to dedicate the last node stack layer for post group grades

and transforms.

Checking the Post Group Node Stack Layer box in Project Settings > Color

The revised node stack order now processes

Layer 3 Special Sauce after the Group Post-

Clip layer (that is automatically generated

when you group clips). Normally the

Group Post-Clip layer would be last.

Using Compound Nodes

Another node structure you can use to keep complex node trees organized is the compound

node. You can Command-click to select any number of nodes in the node tree (selected nodes are

highlighted white), and then use the “Create Compound Node” command to nest all selected nodes

inside of a single node.


Color | Chapter 143 Node Editing Basics

COLOR

Before/after creating a compound node

The resulting compound node that’s created has as many inputs and outputs as are necessary to

accommodate the connection lines that attached the nodes you selected to the rest of the node tree.

You can use compound nodes to organize complicated node trees by nesting sets of nodes that work

together to do a specific thing within a single node. You can also turn a set of nodes that you’re using

to create a specific effect into a compound node in preparation for saving to the Gallery. Creating a

library of effects in this way makes it easy to reuse them via the Append Grade command, without the

undue burden of adding lots more nodes to your grade later on.

Methods for creating and working with compound nodes:

�To create a compound node: Command-click each node you want to nest inside of a compound

node to select them with a white highlight, or drag a bounding box around a group of nodes.

Then, right-click one of the selected nodes, and choose Create Compound Node from the

contextual menu.

�To edit a compound node: Either double-click the compound node you want to open or right-click

any compound node and choose Show Compound Node from the contextual menu. The contents

of that node appear in the Node Editor, taking the place of the overall node tree.

�To exit a compound node you’re editing: To return to the top level node tree, double-click

the leftmost item in the path control at the bottom of the Node Editor, or click the name of

the compound node. You can also right-click in the compound Node Editor and choose “Exit

Compound Node” from the contextual menu.

�To label a compound node: Right-click a compound node, choose Change Label from the

contextual menu, and type a new label for that node. Press the Return key when you’re finished.

�To decompose a compound node: Right-click the compound node you want to decompose,

and choose “Decompose Compound Node” from the contextual menu. The compound node

disappears, replaced by the original nodes within. Please note, if you had applied an adjustment to

the compound node itself, that adjustment is lost when you decompose it back into its constituent

nodes. If you want to preserve the compound node adjustment itself, you can copy it, then

decompose the node, and then create a new node and paste the adjustment you’d copied.


Color | Chapter 143 Node Editing Basics

COLOR