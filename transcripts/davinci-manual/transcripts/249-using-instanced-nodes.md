---
title: "Using Instanced Nodes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 249
---

# Using Instanced Nodes

Instanced nodes are nodes that have been created using the Paste Instance command, and

which share settings with the original node so that a change made to one instanced node is also

automatically applied to all other instances of that node (as well as the original node you copied).

To create an Instance, do the following:


Select a node you want to instance, and copy it (Command-C).


Do one of the following:

�To create a disconnected instance of a node: Right-click in the background of the Node Editor,

and choose Paste Instance from the contextual menu (Command-Shift-V).

�To insert an instanced node between two other nodes: Select a node that’s upstream of where

you want to insert the instanced node, and press Command-Shift-V. Alternatively, you can right-

click directly on a connection line, and choose Paste Instance from the contextual menu.

However you paste an instance, the name of that instanced node takes the form

"Instance_NameOfNode." If you paste multiple instances, each instance is numbered

"Instance_NameOfNode_01."

A green link line shows an instanced Blur node’s relationship to the original Blur node it was copied from.

When a node tree contains instanced nodes, a green line shows the link between the original node

and its instances. You have the option to hide these green link lines to reduce visual clutter in the

Node Editor.

To toggle the visibility of green instance link lines in the Node Editor:


Right-click anywhere in the background of the Node Editor.


Choose Options > Show Instance Links from the contextual menu.

If you’ve been using an instance of a node and you later discover you need to use it to apply separate

adjustments, you can “de-instance” the node.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

To de-instance a node, making it independent:


Right-click an instanced node.


Choose Deinstance from the contextual menu. That node is now independent from the original

node. Once you de-instance a node, you cannot re-instance it, but you can undo the operation.

NOTE: If you’ve de-instanced a node and you cannot undo the operation because you’ve

restarted DaVinci Resolve, you can only recreate an instance by copying the original and

pasting an instance again.

De-Instancing and Re-Instancing Specific Parameters

By default, every parameter in an instanced node is linked to the original node, so that any change

you make is rippled across. However, from time to time you’ll find the need to independently adjust

just one or two parameters while keeping the rest of that node’s parameters linked. For this reason,

instead of de-instancing the entire tool, you can de-instance individual parameters.

To de-instance a single parameter:

�Right-click on a parameter’s name or value in the Inspector, and choose Deinstance from the

contextual menu.

If you’ve only de-instanced individual parameters, you can re-instance those parameters later on if you

change your mind.

To re-instance a single parameter:

Right-click on a parameter’s name or value in the Inspector, and choose Reinstance from the

contextual menu. That parameter immediately inherits the setting of the original node.

Keeping Node Trees Organized

Similar to working with files on your desktop, even the simplest of composites require you to do some

amount of organization. In this section we’ll look at some basic node operations, some of which you

may already be familiar with just from using your computer’s operating system or other applications.

Moving Nodes

Selecting one or more nodes and dragging them moves them to a new location, which is one of the

simplest ways of organizing a node tree, by grouping nodes spatially according to the role they play in

the overall composition.

Keep in mind that the location of nodes in the Node Editor is purely aesthetic, and does nothing to

impact the output of a composition. Node tree organization is purely for your own peace of mind, as

well as that of your collaborators.

TIP: Once you’ve arranged the nodes in a composition in some rational way, you can use

the Sticky Note and Underlay tools to add information about what’s going on and to visually

associate collections of nodes more definitively. These tools are covered later in this section.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Snapping Nodes to the Grid

By default, you can position nodes freely wherever you want them to be. However, keeping nodes and

connection lines straight and aligned can make them easier to read. To help keep them aligned, you

can have nodes you’re dragging automatically snap to the grid.

To have nodes snap to the grid as they’re dragged:

�Right-click over an empty area of the Node Editor, and choose Arrange Tools > To Grid from the

contextual menu. All nodes you drag now snap to the nearest grid coordinate.

�Right-click over an empty area of the Node Editor, and choose Arrange Tools > To Connected

from the contextual menu. All nodes you drag now snap to the horizontal or vertical position of the

nodes they’re attached to.

TIP: You can set “Arrange to Grid” or “Arrange to Connected” as the default for new

compositions by choosing Fusion > Fusion Settings in DaVinci Resolve or File > Preferences

in Fusion Studio, and turning the Fusion > Node Editor > Arrange To Grid or Arrange to

Connected checkboxes on.

Commands to “Clean Up” a Node Tree

The grid in the background of the Node Editor can be used to align nodes, either by eye

or automatically.

To “clean up” an unruly node tree:

Right-click in an empty section of the Node Editor, and choose Line Up All Tools to Grid from

the contextual menu. All nodes in the Node Editor will move to align and center themselves

along the nearest grid lines.

To “clean up” only one or more selected nodes:

Right-click one of the selected nodes and choose Line Up to Grid from the contextual menu.

All selected nodes will move to align and center themselves along the nearest grid lines, while

all unselected nodes will be left as they are.

Renaming Nodes

Each node that’s created is automatically assigned a name (based on its function) and a number

(based on how many of that type of node have been created already). For example, the first Blur

node added to a composition will be called Blur1, the second will be Blur2, and so on. Although

initially helpful, larger compositions may benefit from important nodes having more descriptive

names to make it easier to identify what they’re actually doing, or to make it easier to reference those

nodes in expressions.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

To rename a node:


Do one of the following:

�Right-click a node and choose Rename from the contextual menu.

�Select a node and press F2.


When the Rename dialog appears, type a new name, and then click OK or press Return.

NOTE: If multiple nodes are selected, multiple dialogs will appear asking for a

name for each tool.

Since Fusion can be scripted and use expressions, the names of nodes must adhere to a scriptable

syntax. Only use alphanumeric characters (no special characters), and do not use any spaces.

Also, you cannot start a node name with a number. If you accidentally create a name that doesn’t

exactly follow the guidelines, spaces and invalid characters will be automatically deleted.

If you want to see the original node types instead of the node names, press and hold

Command-Shift-E.

Changing Node Colors

You can change the color of any node by selecting it, opening the Inspector, and choosing a new color

from the Node Color pop-up in the Inspector header for that node. Alternatively, you can right-click a

node and choose a color from the Set Color submenu.

To return a node to its regular color, right-click it and choose Set Color > Clear Color from the

contextual menu, or open the Node Color pop-up for a node in the Inspector, and choose Clear Color.

Using Sticky Notes

A good way to add notes about different parts of a composition, client feedback about various details,

and other information you want to keep track of, is to add Sticky Notes to the Node Editor.

A Sticky Note in the Node Editor.

Sticky Notes are yellow boxes in which you can type whatever text you want. They can be resized,

moved, and collapsed when they’re not being edited, but once created they remain attached to the

background of the Node Editor where you placed them until you either move them or delete them.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Methods of working with Sticky Notes:

�To create a Sticky Note: Click somewhere in the Node Editor where you want a Sticky Note to

appear. Then, press Shift-Spacebar, type sticky, and press the Return key when the Sticky Note

appears in the Select Tool window. Alternatively, you can open the Effects Library, open the Tools

> Node Editor category, and click or drag the Sticky Notes node to create a new one.

�To open a Sticky Note to full size: Double-click a minimized Sticky Note and it expands to a larger,

resizable yellow box.

�To edit a Sticky Note: If necessary, double-click a Sticky Note to open it to full size, and then click

once in the body of the note to place a text cursor. You can edit text within the Sticky Note just like

any other text editor.

�To rename a Sticky Note: Right-click a Sticky Note, choose Rename, type a new name into the

Rename dialog, and click OK. Alternatively, you can select a Sticky Note, press F2 to open the

Rename dialog, and press Return to close it when you’re done.

�To resize a Sticky Note: Double-click a Sticky Note to open it to full size, and then drag any of the

edges or corners to make it larger or smaller.

�To minimize a Sticky Note: Click the close box at the upper left-hand corner of the Sticky Note,

and it collapses to a small tile.

�To delete a Sticky Note: Right-click any Sticky Note and choose Delete from the contextual menu

or select the Sticky note in the Node Editor and press the Delete key.

Using Underlay Boxes

Underlay Boxes are a good way of associating a collection of nodes that work together to perform a

specific task in your composition. They’re simply colored rectangles that you can put nodes inside of.

Once you place nodes inside an Underlay, you can move the Underlay, and all the nodes within move

along with it.

An Underlay in the Node Editor.

Underlay Boxes can be named to identify the purpose of that collection of nodes, and they can

be colored to be distinct from other Underlay Boxes or to adhere to some sort of color code for

your compositions.

Methods of working with Underlay Boxes:

�To create an Underlay Box: Click somewhere in the Node Editor where you want the Underlay

Box to appear. Then, press Shift-Spacebar, type under, and press the Return key when the

Underlay Box appears in the Select Tool window. Alternatively, you can open the Effects Library,

open the Tools > Node Editor category, and click or drag the Underlay Box node to create

a new one.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

�To create an Underlay Box around specific nodes: Select the nodes in the Node Editor that you

want surrounded by an Underlay Box. Then, press Shift-Spacebar, type under, and press the

Return key when the Underlay Box appears in the Select Tool window. Alternatively, you can open

the Effects Library, open the Tools > Node Editor category, and click the Underlay Box node to

have it added and sized to encompass all the selected nodes.

�To resize an Underlay Box: Drag any of the edges or corners to make it larger or smaller.

�To rename an Underlay Box: Option-click the Underlay Box to select just the box and not the

contents, and then right-click it and choose Rename (or press F2). Type a new name into the

Rename dialog and click OK or press Return.

�To change the color of an Underlay Box: Option-click the Underlay Box to select just the box and

not the contents, and then right-click it and choose a color from the Set Color submenu.

�To put nodes inside of an Underlay Box: Select the nodes you want to place inside an

Underlay Box, and then drag them to fit inside. The Underlay Box must be big enough to fit all the

nodes. Alternatively, you can place an Underlay Box near a collection of nodes you want to put

inside it, and then resize the Underlay Box to encompass all those nodes.

�To move an Underlay Box and all its nodes: Once nodes have been placed inside an Underlay

Box and have been deselected, you can move the entire collection of nodes together by dragging

the Underlay Box by its title bar.

�To remove nodes from an Underlay Box: There are two ways you can remove nodes from an

Underlay Box.

With both the Underlay Box and nodes deselected, drag a bounding box or Command-click to

select all nodes in the box you want to remove, and drag them out.

Resize the Underlay Box so that it’s smaller than the collection of nodes it originally encompassed.

Once an Underlay Box is so small that even the last node sticks out beyond its edge, those nodes

are automatically removed from the Underlay Box, and you can move or delete the Underlay Box

without moving those nodes.

�To delete an Underlay Box and all nodes within: Select an Underlay Box and press the Delete

key to delete both the Underlay Box and all nodes found inside it. If you don’t also want to delete

the nodes, first drag the nodes out of the box.

�To delete an Underlay Box but keep all nodes within: Option-click the Underlay Box to select it

and not the nodes, and then press the Delete key. The nodes within remain where they were.