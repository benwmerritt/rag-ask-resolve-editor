---
title: "Automatically Creating a Merge"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 247
---

# Automatically Creating a Merge

Node by Connecting Two Outputs

Here’s an endlessly useful shortcut for when you have a disconnected node that you want to

composite over another node. Drag a connection from the output of the node you want to be the

foreground layer, and drop it on top of the output of the node you want to be the background layer,

and a Merge node will be automatically created to build that composite.

Dragging a connection from a disconnected node to another node’s output

(top), and dropping it to create a Merge node composite (bottom).


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Connection Options and Routers

By default, the Node Editor uses linear connections that are drawn straight between any two

connected nodes. While efficient, this sometimes causes connection lines to overlap nodes, which

some people feel interferes with the view of the Node Editor.

Linear connections between nodes.

If you like, you can change how connections are drawn by enabling orthogonal connections, which

automatically draws lines with right angles to avoid having connections overlap nodes.

Optional orthogonal connections between nodes.

Functionally, there’s no difference to your composition; this only affects how your node tree appears.

To change how connections are drawn in the Node Editor:

�Right-click the Node Editor background and choose one of the following from the

contextual menu.

�Options > Direct Pipes

�Options > Orthogonal Pipes


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Using Routers to Reshape and Branch Connections

If you want to force a particular connection to be drawn at an angle to keep your node tree tidy,

you can add a router to either linear or orthogonal connections to force an angle so it will be drawn

however you like.

A router added to force a connection to be drawn at an angle.

Routers are tiny nodes with a single input and an output, but with no parameters except for a

comments field (available in the Inspector), which you can use to add notes about what’s happening in

that part of the composition.

Even more usefully, you can branch a router’s output to multiple nodes, which makes routers even

more useful for keeping node trees neat in situations where you want to branch the output of a node

in one part of your node tree to other nodes that are all the way on the opposite end of that same

node tree.

A router branching its output to multiple nodes.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Methods of using routers:

�To add a router to a connection: Option-click anywhere on a connection.

�To move a router: Drag the router to a new location, and the connection will reshape

itself as necessary.

�To branch a router’s output: Drag a connection from the router output to the input of another

node. You can branch a router’s output as many times as you need to.

�To remove a router: Select any router and press the Delete key, or right-click a router and choose

Delete from the contextual menu.

Swapping Node Inputs

For multiple-input nodes such as the Merge, Merge 3D, and Dissolve nodes, there’s a quick method

of swapping the Primary and Secondary inputs, such as the foreground and background inputs of a

Merge tool, when you find you’ve accidentally connected them in the wrong order. If a node has more

than two of its inputs connected, only the foreground and background inputs will be swapped.

To swap the primary inputs of a multi-input node, do one of the following:

�Select a node and press Command-T to reverse its inputs.

�Right-click a node and choose Swap Inputs from the contextual menu.

Before swapping node inputs (top), and after swapping node inputs

(bottom), the connections don’t move but the colors change.

Inputs can move freely around the node, so swapping two inputs doesn’t move the connection

lines; instead, the inputs change color to indicate you’ve reversed the background (orange) and

foreground (green) connections.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Extracting and Inserting Nodes

When building a composition, you’ll often find that you need to rearrange nodes that you’ve already

added, in order to connect them in different ways to obtain a better result. Happily, this is easy to do

by extracting one or more nodes from one part of a node tree and inserting them at another part of

the node tree.

To extract one or more nodes from their position in the node tree:

�To extract a single node: Hold down the Shift key, drag a node from the node tree up or down to

disconnect it, and then drop the node before releasing the Shift key. That node is now detached,

and the output of the next upstream node is automatically connected to the input of the next

downstream node to fill the gap in the node tree.

�To extract multiple nodes: Select the nodes you want to extract, hold down the Shift key, drag

one of the selected nodes up or down to disconnect them, and then drop the node before

releasing the Shift key. Those nodes are now detached (although they remain connected to one

another), and the output of the next upstream node is automatically connected to the input of the

next downstream node to fill the gap in the node tree.

Before extracting a pair of nodes (left), and after extracting a pair of nodes (right).

After you’ve extracted a node, you can re-insert it into another connection somewhere else.

You can only insert one node at a time.

To insert a disconnected node in the Node Editor between two compatible nodes:


Hold down the Shift key and drag a disconnected node directly over a connection between two

other nodes.


Once the connection highlights, drop the node, and then release the Shift key. That node is now

attached to the nodes coming before and after it.

Before inserting a node (left), and after inserting a node (right).


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

TIP: If you hold down the Shift key, you can extract a node and re-insert it somewhere else

with a single drag.