---
title: "Turning Grades and/or Fusion Effects Off"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 596
---

# Turning Grades and/or Fusion Effects Off

The Bypass Color Grades and Fusion Effects button/drop-down commands in the Viewer’s title bar

are also available via View > Bypass Color and Fusion menu commands. Turning off Fusion effects in

the Color page is an easy way to improve playback performance on low power systems when you just

need to make a quick set of grading adjustments. Toggling grades off and on is also a convenient way

to quickly get a before and after look at a shot where the before goes all the way back to the source.

If you choose Toggle Bypass or click the Viewer control, you’ll turn off whatever is checked in the

optional menu, which lets you choose whether or not you want to bypass both Color and Fusion, or

just one or the other.

(Left) Menu commands for bypassing Color and Fusion,

(Right) Edit page Timeline Viewer controls

Resetting Nodes

If you’re dissatisfied with your current operations and want to start over, there are three ways you can

reset nodes in the Node Editor. These are available as items in the Color menu.

�Reset Selected Node Grade: Resets the currently selected node, eliminating all keyframes, to the

default parameter settings.

�Reset Grades and Keep Nodes: Resets every node in the current node tree, without affecting the

node tree’s structure; all nodes remain where they were. However, each node has been reset to

the default parameter settings.

�Reset All grades and Nodes: Deletes every node and keyframe, and restores a single node set to

the default parameter settings.

You can also reset nodes using the mouse, which can be a quick thing to do if you’re already working

in the Node Editor to accomplish other things.

Methods of resetting nodes with the mouse:

�To reset a selected node: Right-click that node and choose Reset Node Grade from the

contextual menu.

�To reset all grades and nodes: Right-click anywhere in the background of the Node Editor, and

choose Reset All Grades and Nodes from the contextual menu.

Methods of resetting nodes with the keyboard:

�To reset a selected node: Press (Shift-home).

�To reset all grades and nodes: Press (Command-home).

�To reset all grades and keep nodes: Press (Shift-Command-home).


Color | Chapter 143 Node Editing Basics

COLOR

Previewing and Restoring Node Trees

There are two other methods of quickly dealing with unwanted changes you’ve made to node trees,

without needing to use undo.

Preview Memory: Lets you preview the effect of any saved grade on the current clip. To

preview, choose Color > Preview Memory (Option-Shift-P), and then right-click any saved still

in the Gallery (or Memory) and choose Add Correction. In fact, you can use Add Correction

to try out as many stills as you like. If you like any still’s effect, then you can leave it be. If you

don’t like any of the stills you previewed, then choosing Color > Preview Memory again reverts

the clip to the original grade.

Original Memory: This command lets you quickly revert a clip’s grade to its original state

when you first selected that clip. It is accessed by choosing Color > Original Memory (Option-

Shift-O). This is useful for getting immediately back to a clip’s original grade if you’ve made

a series of changes that you then regret. Selecting another clip in the Timeline and then

reselecting the clip you made changes to resets what is considered to be the current grade.

Caching Specific Nodes

to Improve Performance

You can flag specific nodes to be cached, along with all nodes appearing upstream in that node tree.

By caching nodes using processor-intensive effects, you free up real time capability for the remaining

downstream nodes in a grade. Choosing Playback > Render Cache > User only caches nodes that

you’ve flagged for caching.

When you choose Playback > Render Cache > Smart mode, DaVinci Resolve automatically caches any

nodes that use Motion Blur, Noise Reduction, or OFX plugins, without you needing to do anything.

To flag a node and all corrections made in upstream nodes for caching:

Right-click any node and choose Node Cache > On from the contextual menu.

Editing Node Trees

There is no limit to the number of nodes you can create and connect to one another, and you

can make as many or as few parameter adjustments as you like within each node. The following

procedures describe the ways you can add nodes to the node graph as you build each grade’s

node tree.

Adding Nodes

The simplest thing you can do to add to the complexity of a node tree is to add additional nodes, in

order to add more adjustments to the current grade. You can add nodes so that they’re automatically

attached to nodes that are already in the node tree, for immediate adjustment, or you can add

unattached nodes to empty areas of the node tree in preparation for assembling a particularly

complicated and specific node tree to accomplish a difficult task.


Color | Chapter 143 Node Editing Basics

COLOR

Methods of adding nodes to the tree using a mouse, tablet, or trackpad:

�To add any kind of node to the node graph using the mouse: Right-click any node in the

node tree, and choose the type of node you want to add from the Add Node submenu of the

contextual menu.

�To add a disconnected node to the node graph: Right-click anywhere within the node graph’s

background, then choose Add Node > Corrector from the contextual menu. Disconnected nodes

have no effect on a node tree until they’re connected.

Methods of adding nodes to a currently selected node in the tree using the keyboard:

�To add a serial node after the currently selected node: Press Option-S key, choose Color >

Nodes > Add Serial from the menu.

�To append a serial node to the very end of the node tree: Press Option-K, choose Color > Nodes

> Append Node from the menu.

�To add a serial node before the currently selected node: Press Shift-S, or choose Color > Nodes

> Add Before Current.

�To add nodes in parallel to the currently selected node: Press Option-P, choose Color > Nodes >

Add Parallel from the menu.

�To layer nodes with the currently selected node: Press Option-L, choose Color > Nodes >

Add Layer from the menu.

�To add an outside node to the currently selected node: Press Option-O, choose Color > Nodes >

Add Outside Node from the menu.

Adding Nodes with Windows Turned On

There are also dedicated commands for adding serial nodes with Circular/Linear/Polygon/Curve

windows automatically turned on, for convenience.

To add a node to the tree with a Window automatically enabled:

Choose an item from the Nodes menu that corresponds to the following:

�Node + CPW: Circular Power window (Option-C)

�Node + LPW: Linear Power window (Option-Q)

�Node + PPW: Polygonal Power window (Option-G)

�Node + PCW: PowerCurve window (Option-B)

Whenever you add a node to a tree, it’s numbered consecutively to come after the next most recent

node you’d added, regardless of the order in which it appears in the node tree. For example, if you’ve

already added three nodes, and then you decide to add another node in between Nodes 1 and 2, the

new node will be Node 4, and the order of the nodes will be 1, 4, 2, and 3.

Deleting Nodes

If there’s a node that you no longer need, you can choose to remove it completely from the node tree

to remove its effect permanently.

To delete a node, do one of the following:

�Select a node, then press the Forward-Delete key.

�Right-click a node, and choose Delete Node.

After you’ve deleted a node, the node to the left and right of the node you deleted are automatically

connected so that the node tree is unbroken. Also, all the nodes in a tree are renumbered after

the deletion of any node, so there’s no discontinuity in node order. For example, if you have three

consecutively numbered nodes in a tree and you delete the second one, the node that was formerly

number 3 is renumbered to be 2.


Color | Chapter 143 Node Editing Basics

COLOR

Connecting and Disconnecting Nodes

For a node tree to work, every node in the Node Editor must be connected into a working node tree,

from the Source input, through each node in the tree, to the Node Tree output. Any disconnected

node will result in that clip’s grade being disabled. However, you may find the need to disconnect

some parts of a node tree in order to reconnect them in different ways.

To connect two disconnected nodes:

�Click and drag a connection from the RGB or key output of one node to the corresponding

RGB or key input of another, and when the line highlights, release the mouse button.

To change the connection from one node to another:

�Move the pointer over the second half of any connection line between two nodes until it highlights

blue, then click and drag it to reconnect it to another input, on that node or another.

To disconnect two nodes, do one of the following:

�Position the pointer over the right-hand side of a node connection so it highlights,

and click it to delete it.

�Click a link to select it (selected links turn orange), and then press the

Delete or Forward-Delete key.

�Right-click a link and choose Delete Link.

To overwrite a node’s previous connection:

�You can drag a connection to a node input or output that’s already connected, which will overwrite

the previous connection with the new one you’re dragging. When you do this, the connection

that’s about to be overwritten appears highlighted in orange.

�You can connect any node’s RGB or Key output to as many inputs as you want, but you can

only have one connection going to a node’s input. The exception to this is a node with multiple

inputs, designed to combine the output of multiple nodes. These include the Parallel, Mixer,

and Key Mixer nodes.

Extracting a Node

Sometimes you need to remove a node from its current position in the node tree, such that the nodes

to the left and right of it automatically reconnect to one another, saving you from having to reconnect

them manually. This is called extracting a node.

To extract a node, do one of the following:

�Select a node, and choose Color > Nodes > Extract Current Node.

�Select a node, and press E.

Keep in mind that disconnected nodes in the node tree suspend grading altogether, so you’ll want

to either reconnect that node to another part of the node tree, or delete it; you cannot leave it

disconnected in the Node Editor.

Inserting a Node

If there’s a disconnected node in the Node Editor, there’s a simple way you can insert it into the node

tree between any two other nodes. This also works for nodes that you’re dragging into a node tree

from another source, for example, from the exposed node tree of a still in the Gallery.

To insert a disconnected node between two other nodes:

�Drag a disconnected node, or a node from another node tree, onto the connection between any

two other nodes in a node tree; when a plus icon appears over the node you’re dragging, drop it

to insert the node.


Color | Chapter 143 Node Editing Basics

COLOR

Rearranging Node Order

The order in which nodes are connected in your tree affects the result of a grade. For example, if you

boost the highlights in the first node, and then you try to isolate a portion of the picture in a second

node that you now realize has been clipped, you may to need to change your order of operations to

optimize your corrections.

To swap the contents of two nodes:

�Command-drag any node and drop it onto another node to swap the operations within each node.

The nodes won’t appear to have moved, but you should be able to tell from the node badges

underneath that the operations have been reversed.

To move a node to any other position in the node tree:


Double-click any node in the node tree and press E to extract it, removing it from the tree so that it

becomes unattached.


Drag the now-unattached node to the connection line between any two other nodes in the tree,

and when a small plus icon appears, drop it to automatically connect that node at that position in

the node tree.

Copying and Pasting All Settings From One Node to Another

The simplest thing you can do is to copy all of a node’s settings and paste them into another node.

This makes it easy to duplicate things like windows, qualifier settings, keyframing, or motion tracking

that you want to reuse in another node as the basis for another operation. This is also a quick way to

manually ripple a change you make in a node to that same node in another clip’s grade.

To copy a node’s settings from one clip to another, do one of the following:

�Option-drag one node onto another. When you drop it, the settings of the node you dragged

overwrite those of the node you dropped onto.

�Select a node with settings you want to copy and choose Edit > Copy (Command-C). Then, select

a node you want to paste these settings to either in the current grade or in the grade of another

clip, or create a new node, and choose Edit > Paste (Command-V) to paste the settings you

copied. These pasted node settings overwrite any other settings that node previously used.

NOTE: There are additional methods of copying nodes and individual node settings.

For more information, see Chapter 142, “Grade Management.”

Node Context Menu Actions Can Have Assigned Shortcut Keys

You can assign shortcut keys to common Node Context menu actions like Lock Node, HDR Mode,

Clean Up Selected Node Graph, etc. Go to Keyboard Customization > Commands > Panels > Color

Nodes to assign the shortcuts.


Color | Chapter 143 Node Editing Basics

COLOR