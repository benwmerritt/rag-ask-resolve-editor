---
title: "Upstream and Downstream Nodes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 246
---

# Upstream and Downstream Nodes

Since nodes can be positioned anywhere in the Node Editor, and added in any direction, nodes are

referred to as being upstream and downstream of one another. Once you select a node, all other

nodes that directly or indirectly connect to its input are considered to be upstream. Any other nodes

that are directly or indirectly connected to the output are said to be downstream.

This is an important distinction to make because, unlike layer-based systems, the visual positioning of

nodes in your node tree has no bearing on the order of operations in that composition. The only thing

that matters is whether nodes are upstream or downstream of each other.

Tools upstream (left) and downstream (right) of the Merge node.

TIP: To help you stay organized, there are Select > Upstream/Downstream commands in the

Node Editor contextual menu for selecting all upstream or downstream nodes to move them,

group them, or perform other organizational tasks.

Disconnecting and Reconnecting Nodes

Node trees are a continuous work in progress, requiring constant revision and rearrangement as

you discover new details that need to be finessed, or things that you can do better once the overall

composition has taken shape. To facilitate quick changes, each connection between two nodes is

divided into two halves: the output half (connected to the upstream node’s output) and the input half

(connected to the downstream node’s input). This can only be seen when you hover the pointer over a

connection. The half your pointer is over is highlighted in blue.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

The two halves of a connection line that are

revealed when you hover your pointer over it.

By clicking and/or dragging these two halves, it’s possible to quickly disconnect, reconnect, and

overwrite node connections, which is essential to rearranging your node tree quickly and efficiently.

To disconnect two nodes, do one of the following:

�Click once on the input half of the connection between two nodes.

�Click on the input arrow to which a connection is attached, then drag to pull the connection away

from the tool and drop it anywhere in an empty area of the Node Editor.

To overwrite a current connection:

�Drag the output or input half of a connection, and drop it directly onto another node’s input

or output. This simultaneously disconnects the previous connection and connects the one

you’re dragging.

To reconnect a connection from one node to another:

�Drag the output or input half of a connection to disconnect it from one node, and drop the

connection directly on another node’s input or output.

Tracing Connections Through the Node Tree

Positioning the pointer over a node causes the connections attached to that node to become

highlighted, which makes it easier to see which nodes it’s attached to. Additionally, highlighted

connections display the color of the input they’re connected to, which makes it easy to see if they’re

connected to a foreground, a background, or a particular kind of mask.

Hovering the pointer over a node highlights

the color of all connections, telling you

what kinds of inputs are connected.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Additionally, positioning the pointer over a connection causes a tooltip to appear that displays the

output and input that connection is attached to.

Hovering the pointer over a node highlights the

connection between it and other nodes.

Branching

A node’s input can only have one connection attached to it. However, a tool’s output can be

connected to inputs on as many nodes as you require. Splitting a node’s output to inputs on multiple

nodes is called branching. There are innumerable reasons why you might want to branch a node’s

output. A simple example is to process an image in several different ways before recombining these

results later on in the node tree.

A MediaIn node branched to two node operations

and then recombined using a Merge node.

Alternatively, it lets you use one image in several different ways—for example, feeding the RGB to one

branch for keying and compositing, while feeding the A channel to the Effects Mask input of another

node to limit its effect, or feeding RGB to a tracker to extract motion information.

A MediaIn node branched to two different kinds of inputs, used separately.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Connecting Merge Nodes

The Merge node is the primary tool available for compositing images together. Each Merge node

is capable of combining two inputs to create a third, using standard compositing methods and

composite modes.

For more extensive information about the Merge node, see Chapter 105, “I/O Nodes,” in the

DaVinci Resolve Reference Manual or Chapter 45 in the Fusion Reference Manual.

For this chapter, all you need to know is that if you attach a background image to the

Background input (such as a landscape), and a foreground image with an alpha channel to

the Foreground input (such as a graphic with an alpha channel), the Merge node will combine

them into a single image for further compositing.

Two MediaIn nodes and a DeltaKeyer node attached to a Merge node, creating a composite.

Each Merge node has three inputs:

�Background (orange): The default input. Whichever image is connected to this input defines the

output resolution of the Merge node.

�Foreground (green): The secondary input, meant for whichever image you want to be “on top.”

�Effect Mask (blue): An optional input you can use to attach a mask or matte with which to limit the

effect of the Merge node.

It’s important to make sure you’re attaching the correct nodes to the correct inputs to ensure

you’re getting the result you want, and it’s important to keep these inputs in mind when you

connect to a Merge node. Of course, you can always drag a connection to a specific input to make

sure you’re connecting things the way you need. However, if you’re in a hurry and you simply drag

connections right on top of a Merge node:

�The first connection will be made to the background input.

�The second connection will be made to the foreground input.

�The third connection will be made to the effect mask input.

TIP: When you add a Merge node after a selected node by clicking the Merge button on the

toolbar, by clicking on the Merge icon in the Effects Library, or by right-clicking a node in the

node tree and choosing Insert Tool > Composite > Merge from the contextual menu, the new

Merge node is always added with the background connected to the upstream node coming

before it.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Automatically Creating a Merge Node When Adding Nodes

There’s a nice shortcut for connecting Merge nodes if you want to connect the incoming clip

immediately to your node tree as the top layer of a composite, and that’s to drag a clip from an

Operating System window or a Generator from the Effects Library right on top of any connection line.

When you drop the resulting node, this automatically creates a Merge node, the background input

of which is connected to the next node to the left of the connection you dropped the clip onto, and

the foreground input of which is connected to the new node that represents the clip or Generator

you’ve just added.

Dragging a node from the Media Pool onto a connection (top), and

dropping it to create a Merge node composite (bottom).

Additionally, If you drag two or more nodes from an OS window into the Node Editor at the same

time, Merge nodes will be automatically created to connect them all, making this a fast way to initially

build a composite.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

By dragging three nodes from an OS window to the Node Editor (top),

Merge nodes are automatically created to connect them all (bottom).