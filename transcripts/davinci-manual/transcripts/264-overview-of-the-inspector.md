---
title: "Overview of the Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 264
---

# Overview of the Inspector

While the creation and connection of nodes in the Node Editor determines the tools and order of

operations that make up a composition, the Inspector is where you adjust the various parameters

inside each node to do what needs to be done.

Inspector displays the Brightness Contrast controls

Animating Parameters in the Inspector���������������������������������������������������������������������������������������������������������������������������������� 1452

Removing Animation From a Parameter���������������������������������������������������������������������������������������������������������������������������������� 1453

Attaching a Parameter to an Existing Animation Curve��������������������������������������������������������������������������������������������������� 1453

Connecting Parameters������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1453

Connecting Parameters by Publishing������������������������������������������������������������������������������������������������������������������������������������� 1453

Connecting Parameters by Pick Whipping����������������������������������������������������������������������������������������������������������������������������� 1454

Contextual Menus������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1454

Customizing Node Parameters with User Controls��������������������������������������������������������������������������������������������������������� 1455

An Example of Customizing Directional Blur������������������������������������������������������������������������������������������������������������������������� 1456


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

This chapter covers methods for opening node parameters in the Inspector to edit them in

different ways according to the type of available controls.

To display the Inspector:

Click the Inspector button on the UI toolbar.

The Tools and Modifiers Panels

The Inspector is divided into two overall panels.

�The Tools panel is where the parameters of selected nodes appear so you can edit them.

�The Modifiers panel is where you edit optional extensions to the tool’s standard toolset as well as

automated expressions that you can attach to individual parameters to create animated effects.

Additionally, certain nodes such as the Paint node generate data such as Strokes, which are saved

in the Modifiers panel.

Modifiers displayed in the Modifiers panel

Customizing the Inspector

You can customize how the Inspector is presented in a variety of ways.

Inspector Height

A small arrow button at the far right of the UI toolbar lets you toggle the Inspector between full-height

and half-height views, depending on how much room you need for editing parameters.

The Maximize button on the

left side of the Inspector

In maximized height mode, the Inspector takes up up the entire right side of the UI, letting you see

every control that a node has available, or creating enough room to see the parameters of two or three

pinned nodes all at once. In half-height mode, the top of the Inspector is aligned with the tops of the

viewers, expanding the horizontal space that’s available for the Node Editor.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Inspector Display Preferences

By default, you see only selected nodes in the Inspector, and only the Active node is expanded to

show its controls. You can change this behavior by choosing Fusion > Fusion Settings in the Fusion

page or File > Preferences in Fusion Studio and opening the User Interface panel. In the User

Interface, checkboxes manage the display of controls.

Control preferences in the User Interface category

�Auto Control Open: When enabled (the default), whichever node is active automatically opens its

controls in the Inspector. When disabled, selecting an active node opens that node’s Inspector

header in the Inspector, but the parameters remain hidden unless you click the Inspector header.

�Auto Control Hide: When enabled (the default), only selected nodes are visible in the Inspector,

and all deselected nodes are automatically removed from the Inspector to reduce clutter. When

disabled, parameters from selected nodes remain in the Inspector, even when those nodes are

deselected, so that the Inspector accumulates the parameters of every node you select over time.

�Auto Control Close Tools: When enabled (the default), only the parameters for the active

node can be exposed. When disabled, you can open the parameters of multiple nodes in the

Inspector if you want.

�Auto Controls for Selected: When enabled (the default), selecting multiple nodes opens multiple

control headers for those nodes in the Inspector. When disabled, only the active node appears in

the Inspector; multi-selected nodes highlighted in white do not appear.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Opening Nodes in the Inspector

Before you can edit a node’s parameters, you need to open it in the Inspector.

To display a node’s controls in the Inspector:

Select one or more nodes from the Node Editor, Keyframes Editor, or Spline Editor.

When you select a single node so that it’s highlighted orange in the Node Editor, all of its parameters

appear in the Inspector. If you select multiple nodes at once, Inspector headers appear for each

selected node (highlighted in white in the Node Editor), but the parameters for the active node

(highlighted in orange) are exposed for editing.

Opening multiple nodes in the Inspector

Only one node’s parameters can be edited at a time, so clicking another node’s Inspector header

opens that node’s parameters and closes the parameters of the previous node you were working on.

This also makes the newly opened node the active node, highlighting it orange in the Inspector.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Pinning Multiple Nodes in the Inspector

For instances where you need to work quickly by editing the parameters of multiple nodes at the

same time, you can use the Pin button in the Inspector header of nodes in the Inspector to keep those

parameters exposed in the Inspector, regardless of whether that node is selected and active.

The Pin button of a node’s Inspector

header in the Inspector

While the Pin button is on, that node’s parameters remain open in the Inspector. If you select another

node in the Node Editor, that node’s parameters appear beneath any pinned nodes.

A pinned node on the bottom, with a selected node at the top

You can have as many pinned nodes in the Inspector as you like, but the more you have, the more

likely you’ll need to scroll up or down in the Inspector to get to all the parameters you want to edit.

To remove a pinned node from the Inspector, just turn off its Pin button in the Inspector header.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION