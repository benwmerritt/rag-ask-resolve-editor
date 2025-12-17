---
title: "Clearing Viewers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 245
---

# Clearing Viewers

Whenever you load a node into a viewer, you prompt that node, all upstream nodes, and other related

nodes to be rendered. If you load nodes into both viewers, this is doubly true. If you want to prevent

your computer from processing views that aren’t currently necessary, you can clear each viewer.

Methods of clearing viewers:

�Press 1 or 2 to empty the left or right viewers if they’re filled.

�Press ` (the Accent key) to empty both viewers.

Create/Play Preview

You can right-click a node, and choose an option from the Create/Preview Play On submenu of the

contextual menu to render and play a preview of any node’s output on one of the available viewers.

The Render Settings dialog is displayed, and after accepting the settings, the tool will be rendered and

the resulting frames stored in RAM for fast playback on that view.

TIP: Hold the Shift key when selecting the viewer from the menu to bypass the Render dialog

and to start creating the preview immediately using the default settings or the last settings

used to create a preview.

Connecting and Disconnecting Nodes

Once you’ve started to add nodes to your composition, you need to connect them to perform their

intended operations.

Node Basics

Each node displays small colored knots around the edges. One or more arrows represent inputs, and

the square represent the tool’s processed output, of which there is always only one. Outputs are white

if they’re connected properly, gray if they’re disconnected, or red to let you know that something’s

wrong and the node cannot process properly.

A Blur node with a Foreground

Input, Mask Input, and Output.

Each node takes as its input the output of the node before it. By connecting a MediaIn node’s output

to a Blur node, you move image data from the MediaIn node to the Blur node, which does something

to process the image before the Blur node’s output is in turn passed to the next node in the tree.

Two nodes connected together.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

How to Connect Nodes

To manually connect one node to another, click on one node’s output and drag a connection line

out to drop on another node’s input. The order in which you drag node connections is not important;

you can just as easily drag a connection from one node’s input to another node’s output and get the

same results.

Before (top), and after (bottom) dragging a connection

line and dropping it to connect two nodes.

Dropping Connections on Top of Nodes

To make your life a bit easier, you can also drag a connection line and drop it directly on top of the

tile of a node to automatically connect to the default input of that node, which is usually labeled

“background” or “input.” In the following example, a connection is dragged from the output of a

MediaIn node and dropped onto the tile of a Blur1 node, and the background input is connected first.

Before (top), and after (bottom) dragging a connection

line and dropping it on top of a node.

If you drop a connection on top of a node that already has the background input connected, then the

second most important connection will be attached, which for multi-input nodes is the foreground

input, and for other single-use nodes may be the Effects Mask input.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Before (previous page), and after (above) dragging a connection line and

dropping it on top of a node that has the background input already connected.

Some multi-input nodes are capable of adding inputs to accommodate many connections, such as the

Merge3D node. These nodes simply add another input whenever you drop a connection onto them.

After dragging a connection line and dropping

it on top of a Merge3D node.

Attaching Connections to Specific Inputs

If you want to make sure you don’t attach a connection to the default input of a node, then you need to

drop it right on top of the specific node input you want to attach it to. If you can see the input’s label in

the tooltip bar, then you know you’re correctly positioned to make a good connection.

However, there’s an alternate method of connecting nodes together in instances where there are

several inputs to choose from and you want to make sure you’re choosing the correct one. Hold down

the Option key while dragging a connection from one node’s output and dropping it onto the body of

another node. This opens a pop-up menu from which you can choose the specific input you want to

connect to, by name. Please note that this menu only appears after you’ve dropped the connection on

the node and released your pointing device’s button.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Option-dragging a node connection to drop onto

another node exposes a node input menu.

Automatically and Manually Attaching Mask Nodes

Mask nodes, such as the Polygon, B-Spline, Ellipse, or Rectangle, have a different automatic behavior

when you connect them to other nodes. If you drag a connection from a Mask node onto the body of

another node, it will automatically connect itself to the default mask input, which is usually the effect

mask input. The assumption is that you’re using the mask to limit the node’s effect somehow. However,

this isn’t always the case, so you’ll need to be careful of this behavior to make sure you’re attaching

your mask to the input that will actually create the effect you need.

Before (left) and after (right) dragging a connection from a

Mask node and dropping it on top of a MatteControl node.

Identifying Node Inputs

While you are still figuring out all the nodes and their inputs, hovering the pointer over any knot will

display a node tip with the knot’s name.

TIP: Rather than remembering the different knot types, press the right mouse button, hold

Option, and drag from the output of a node to the center of another tool. When you release

the mouse, a tooltip will appear allowing you to select the knot you want to connect to.

Node Order Matters

The order in which nodes are attached defines the order in which each image-processing operation is

applied to the image.

In the following example, a MediaIn node adds a clip to the composition, while a Defocus node

blurs the image, and then a TV node adds scanlines and vertical distortion. Those effect nodes are

then connected to the MediaOut node in the Fusion page in DaVinci Resolve or a Saver node in

Fusion Studio.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Adding a Defocus effect first, then the TV node second.

As you can see above, connecting the Defocus node first, followed by the TV node, means that while

the initial image is softened, the TV effect is sharp. However, if you reverse the order of these two

nodes, then the TV effect distorts the image, but the Defocus node now blurs the overall result, so

that the TV effect is just as soft as the image it’s applied to. The explicit order of operations you apply

makes a big difference.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Adding a TV effect first, and a Defocus second.

As you can see, the node tree that comprises each composition is a schematic of operations with

tremendous flexibility. Additionally, the node tree structure facilitates compositing by giving you the

ability to direct each node’s output into separate branches, which can be independently processed

and later recombined in many different ways, to create increasingly complex composites while

eliminating the need to precompose, nest, or otherwise compound layers together, which would impair

the legibility of your composition.

In the following example, several graphics layers are individually transformed and combined with a

series of Merge nodes. The result of the last Merge node is then transformed, allowing you to move

the entire collection of previous layers around at once. Because each of these operations is clearly

represented via the node tree, it’s easy to see everything that’s happening, and why.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

The output of five Text nodes being combined using Merge

nodes is modified by a single Transform node.