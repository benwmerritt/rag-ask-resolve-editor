---
title: "Copying Individual Nodes and Settings"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 591
---

# Copying Individual Nodes and Settings

Copying grades from clip to clip copies everything except for keyframes and motion tracking.

However, there is one way you can copy the motion tracking from one clip to another, and that’s by

copying and pasting individual node settings. This can save time when you’re assembling complicated

node trees by recycling specific nodes or node settings from previous grades.

Copying and Pasting All Settings From One Node to Another

The simplest thing you can do is to copy all of a node’s settings, and paste them into another node.

This makes it easy to duplicate things like windows, qualifier settings, keyframing, or motion tracking

that you want to reuse in another node as the basis for another operation. This is also a quick way to

manually ripple a change you make in a node to that same node in another clip’s grade.


Color | Chapter 142 Grade Management

COLOR

To copy a node’s settings from one clip to another, do one of the following:

�Option-drag one node onto another. When you drop it, the settings of the node you dragged

overwrite those of the node you dropped onto.

�Select a node with settings you want to copy and choose Edit > Copy (Command-C). Then, select

a node you want to paste these settings to either in the current grade or in the grade of another

clip, or create a new node, and choose Edit > Paste (Command-V) to paste the settings you

copied. These pasted node settings overwrite any other settings that node previously used.

Paste Attributes on the Color Page

You can copy the settings of one node and

paste a subset of those settings to another

selected node by choosing Edit > Paste

Attributes (Option-V). A Paste Attributes

window appears that shows you which node

you’re copying from, and which node you’re

pasting to, and provides controls for choosing

whether you want to paste keyframes and

how to align them (Start Frames or Source

Timecode), as well as a series of checkboxes

for choosing which palettes, windows, and

OFX/ResolveFX you want to apply. You can

only paste all parameters from a specified

palette; there’s no current provision for pasting

specific parameters from within a given palette,

with the exception of pasting specific windows

and their accompanying trackers.

The Paste Attributes window on the Color page

Copying from the Node Graph

of Other Clips or Gallery Stills

When constructing new grades, you may sometimes find it convenient to copy existing nodes or node

settings from the grade of another clip or gallery still. This can be easily accomplished by exposing

the node tree of any still that’s saved in the Gallery, or any clip in the Thumbnail timeline, and using the

controls found in the floating node graph to copy individual nodes or node adjustments to the current

clip’s grade shown in the Node Editor.

Copying Clip Settings Using Display Node Graph

In Clip mode, the floating Node Graph window has four sets of controls you can use to choose how to

copy nodes and adjustments:

�Clip Node Graph: By default, the Clip node graph is displayed at the left. You can drag any node

from the floating node graph to the current grade shown in the Node Editor, and drop it onto an

existing node to overwrite that node’s settings or onto a connection line to insert it as a new node.


Color | Chapter 142 Grade Management

COLOR

�Timeline Node Graph: (Only available if there is a Timeline grade) You can switch to the Timeline

grade, if there is one, by either clicking the second button in the Node Graph title bar, or by

choosing Timeline from the drop-down menu at the upper right-hand corner of the floating

Node Graph window.

�Apply Color/PTZR/Source/All buttons: With the Clip panel selected, four buttons let you

selectively copy the entire grade, the sizing, the source settings, or all settings at once to

the current clip.

Dragging a node from another clip’s node graph to the currently selected clip’s grade in the Node Editor

Copying Node Settings Using Display Node Graph

In Node mode, the floating Node Graph window displays all of the available Color Attributes found

within each node, instead of the Apply Color/PTZR/Source/All buttons:

�Node Settings: Use the checkboxes to choose which node adjustments get copied and which

do not. After you’ve checked the settings you want to selectively copy, dragging a node from the

floating node graph onto nodes in the Node Editor copies or appends the selected attributes into

the target node, leaving all other attributes alone. For Windows and OpenFX, you have the option

of also copying any motion tracking that’s available.

The Node panel open with the Color Corrector

and Blur attributes selected for copying


Color | Chapter 142 Grade Management

COLOR

Ability to Open Compound Nodes in “Display Node Graph”

When you right-click a Gallery still or a thumbnail and choose Display Node Graph for a grade that

uses compound nodes, you can right-click any compound node and choose “Show compound node,”

or Command-double-click a compound node to open it and see its individual nodes.

Opening a compound node in a floating Node Graph window

How to Copy Nodes Using Display Node Graph

The following procedures describe how to open the floating node graph in different situations.

To copy individual nodes or settings from any still in the Gallery:


Click the thumbnail in the Timeline of the clip you want to copy nodes to. Its node graph will

appear in the Node Editor.


Right-click a still in the Gallery you want to copy nodes from, and choose Display Node Graph.

A floating Node Graph window appears displaying that still’s node tree.


(Optional) While the Gallery Node Graph window is open, you can select any other still, and this

window will update to show the currently selected still’s node graph, ready for you to copy from.


In the floating Node Graph window, choose Clip if you want to copy overall clip attributes, or

choose Node to copy individual node attributes.


Do one of the following to copy nodes or settings to the Node Editor.

�In Clip mode, drag any node from the floating node graph to the current grade shown in the

Node Editor, and drop it onto an existing node to overwrite that node’s settings. If you open the

Node panel and choose specific attributes, only those attributes will be copied to the node you

drag onto.

�In Clip mode, drag any node from the floating node graph to the current grade shown in the

Node Editor, and drop it onto a connection line to insert it as a new node. If you open the

Node panel and choose specific attributes, only those attributes will be copied to the new

node that’s created.

�In Clip mode, click Apply Color to copy the entire grade from the floating node graph to

overwrite the current grade in the Node Editor.


Color | Chapter 142 Grade Management

COLOR

�In Clip mode, click Apply PTZR to copy the sizing from the floating node graph to overwrite that

of the current clip.

�In Clip mode, click Apply Source to copy the source settings from the floating node graph to

overwrite those of the current clip.

�In Clip mode, click Apply All to copy every setting from the floating node graph to the current clip.

�In Node mode, select which attributes you want to copy, and then drag any node from the

floating node graph to the current grade shown in the Node Editor, and drop it onto an existing

node to overwrite the settings of that node that you selected.

�In Node mode, select which attributes you want to copy, and then drag any node from

the floating node graph to the current grade shown in the Node Editor, and drop it onto a

connection line to insert it as a new node with only the settings that you selected.


While the floating Node Graph window is open, you can also select any clip in the Thumbnail

timeline to change the grade that’s displayed in the Node Editor, ready for you to copy to.


Click Close when you’re finished.

To copy individual nodes or settings from any clip in the Timeline:


Click the thumbnail in the Timeline of the clip you want to copy nodes to. Its node graph will

appear in the Node Editor.


Right-click the thumbnail of another clip you want to copy nodes from, and choose Display Node Graph.

NOTE: The Display Node Graph command only appears in the contextual menu of a clip

in the Thumbnail timeline that is not currently selected.


(Optional) In the floating Node Graph window, choose Clip if you want to copy overall clip

attributes, or choose Node to copy individual node attributes.


Do one of the following to copy nodes or settings to the Node Editor.

�In Clip mode, drag any node from the floating node graph to the current grade shown in the Node

Editor, and drop it onto an existing node to overwrite that node’s settings. If you open the Node

panel and choose specific attributes, only those attributes will be copied to the node you drag onto.

�In Clip mode, drag any node from the floating node graph to the current grade shown in the

Node Editor, and drop it onto a connection line to insert it as a new node. If you open the Node

panel and choose specific attributes, only those attributes will be copied to the new node

that’s created.

�In Clip mode, click Apply Color to copy the entire grade from the floating node graph to

overwrite the current grade in the Node Editor.

�In Clip mode, click Apply PTZR to copy the sizing from the floating node graph to overwrite that

of the current clip.

�In Clip mode, click Apply Source to copy the source settings from the floating node graph to

overwrite those of the current clip.

�In Clip mode, click Apply All to copy every setting from the floating node graph to

the current clip.

�In Node mode, select which attributes you want to copy, and then drag any node from the

floating node graph to the current grade shown in the Node Editor, and drop it onto an existing

node to overwrite the settings of that node that you selected.

�In Node mode, select which attributes you want to copy, and then drag any node from

the floating node graph to the current grade shown in the Node Editor, and drop it onto a

connection line to insert it as a new node with only the settings that you selected.


Color | Chapter 142 Grade Management

COLOR


(Optional) While the floating Node Graph window is open, you can also select any clip in the

Thumbnail timeline to change the grade that’s displayed in the Node Editor, ready for you

to copy to.


Click Close when you’re finished.