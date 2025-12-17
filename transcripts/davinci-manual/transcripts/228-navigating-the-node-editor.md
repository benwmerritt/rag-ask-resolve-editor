---
title: "Navigating the Node Editor"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 228
---

# Navigating the Node Editor

As your Node tree gets larger, parts inevitably go offscreen. When a portion of the node tree is

offscreen, a resizable Navigator pane appears in the upper-right corner. The Navigator is a miniature

representation of the entire node tree that you can drag within to pan to different parts of your

composition quickly. You can resize the navigator using a handle in the lower-left corner, and you can

choose to show or hide the Navigator by pressing the V key, or by right-clicking the Node Editor to

access the Options submenu of the contextual menu.

The Navigator pane for accessing offscreen parameters or tools

There are other standard methods of panning and zooming around the Node Editor.

Methods of navigating the Node Editor:

•	 Middle-click and drag to pan around the Node Editor.

•	 Hold down Shift and Command and drag the Node Editor to pan.

•	 Press the Middle and Left mouse buttons simultaneously and drag to resize the Node Editor.

•	 Hold down the Command key, and use your mouse’s scroll control to resize the Node Editor.

•	 Right-click the Node Editor and choose an option from the Scale submenu of the

contextual menu.

•	 Press Command-1 to reset the Node Editor to its default size.

•	 Drag two fingers on a track pad to pan.

•	 Hold the Command key down and drag two fingers on a track pad to resize the Node Editor.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Vertical Node Editor Layouts

Alternative Node View Layout presets located in the Fusion page allow for positioning the Node Editor

vertically, either alongside the Inspector, or along the left side of the screen. This can be very helpful

when animating in the Spline Editor or Keyframes Editor.

When in the Fusion page, you can choose the layouts from Workspace > Layout Presets. Choosing

a vertical layout allows the node tree to flow from top to bottom, leaving much more room along the

lower half of the screen for the Spline Editor or Keyframes Editor.

The Mid Flow Vertical layout preset used with the Vertical Flow direction setting.

When using the vertical layouts, enabling the Flow > Build Direction > Vertical option in the Fusion

settings will cause all new Node trees to build vertically, leaving maximum room for Fusion’s

animation tools.

You can then save alternative layouts based on these two vertical presets using the Workspace >

Layout Presets submenu.

When you want to return to the default horizontal Node Editor layout, just choose Workspace > Layout

Presets > Fusion Presets > Default.

These Layout options are not available in Fusion Studio, however, you can use the Floating Frame to

position the Node Editor wherever you like.

Keeping Organized

As you work, it’s important to keep the node trees that you create tidy to facilitate a clear

understanding of what’s happening. Fortunately, the Fusion Node Editor provides a variety of methods

and options to help you with this, found within the Options and Arrange Tools submenus of the Node

Editor contextual menu.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Status Bar

The Status bar in the lower-left corner of the Fusion window shows you a variety of up-to-date

information about things you’re selecting and what’s happening in Fusion. For example, hovering the

pointer over a node displays information about that node in the Status bar. Additionally, the currently

achieved frame rate appears whenever you initiate playback, and the percentage of the RAM cache

that’s used appears at all times. Other information, updates, and warnings appear in this area

as you work.

The Status bar under the Node Editor showing you information about a node under

the pointer, as well as a popup box with even more relevant info.

Occasionally the Status bar will display a badge to let you know there’s a message in the console you

might be interested in. The message could be a log, script message, or error.

A notification that there’s a message in the Console


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Effects Library

The Effects Library in Fusion shows all the nodes and effects available in Fusion, including third-

party OFX plugins, if installed. If you are using DaVinci Resolve, Resolve FX also appear in the OFX

category. While the toolbar shows many of the most common nodes you’ll use in any composite, the

Effects Library contains every single tool available in Fusion, organized by category, with each node

ready to be quickly added to the Node Editor. Suffice it to say that there are many, many more nodes

available in the Effects Library than on the toolbar, spanning a wide range of uses.

The Effects Library with Tools open

The Templates section of the Effects Library

The hierarchical category browser of the Effects Library is divided into several sections depending

on whether you are using Fusion Studio or the Fusion page within DaVinci Resolve. The Tools section

is the most often used since it contains every node that represents an elemental image-processing

operation in Fusion. Hovering the pointer over a specific tool will reveal a tool-tip explaining its

functionality at the bottom right of the DaVinci Resolve interface. The OpenFX section contains third-

party plugins, and if you are using the Fusion page, it also contains ResolveFX, which are included with

DaVinci Resolve. A third section, only visible when using the Fusion page in DaVinci Resolve, is the

Templates section. The Template section contains a variety of additional content including templates

for Lens Flares, Backgrounds, Generators, Particle Systems, Shaders (for texturing 3D objects), and

other resources for use in your composites.

The Effects Library’s list can be made full height or half height using a button at the far left of

the UI toolbar.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

The Inspector

The Inspector is a panel on the right side of the Fusion window that you use to display and manipulate

the parameters of one or more selected nodes. When a node is selected in the Node Editor, its

parameters and settings appear in the Inspector.


The Inspector shows parameters from

one or more selected nodes.

The Modifier panel

showing a Perturb modifier

The Tools and Modifiers Panels

The Fusion Inspector is divided into two panels. The Tools panel is the main panel that shows you

the parameters of selected nodes. The Modifiers panel shows optional extensions to the standard

parameters of a tool. In the following image, a Perturb modifier has been added to a parameter to add

random animation to that parameter, and the controls found on the Modifier panel let you customize

what kind of randomness is being added.

Other nodes display node-specific items here. For example, Paint nodes show each brush

stroke as an individual set of controls in the Modifiers panel, available for further editing

or animating.

Parameter Header Controls

A cluster of controls appears at the top of every node’s controls in the Inspector.

Common Inspector controls


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Set Color: A pop-up menu that lets you assign one of 16 colors to a node, overriding a

node’s own color.

Versions: Clicking Versions reveals another toolbar with six buttons. Each button can

hold an individual set of adjustments for that node that you can use to store multiple

versions of an effect.

Pin: The Inspector is also capable of simultaneously displaying all parameters for

multiple nodes you’ve selected in the Node Editor. Furthermore, a Pin button in the

title bar of each node’s parameters lets you “pin” that node’s parameters into the

Inspector so that they remain there even when that node is deselected, which is

valuable for key nodes that you need to adjust even while inspecting other nodes of

your composition.

Lock: Locks that node so that no changes can be made to it.

Reset: Resets all parameters within that node.