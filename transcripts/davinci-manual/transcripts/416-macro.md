---
title: "Macro"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 416
---

# Macro

Macros are not technically a node. Instead, they are a group of nodes that act as a single node.

Macro Introduction

Macros can be used to combine multiple nodes and expose a user-definable set of controls.

They are meant as a fast and convenient way of building custom nodes.

Usage

To create a Macro, select the nodes intended for the macro. The order in which the nodes are

selected becomes the order in which they are displayed in the Macro Editor. Right-click on any of the

selected nodes and choose Macro > Create Macro from the contextual menu.

Select the nodes to include in the macro

Macro Editor

The Macro Editor allows you to specify and rename the controls that are exposed in the final

macro tool.

In the example below, the tool is named Light_Wrap at the top. The Blur slider for Matte Control 1 is

enabled and renamed to Softness, as it will appear in the Inspector.

The Macro Editor


Fusion Page Effects | Chapter 102 Flow Organizational Nodes

FUSION

After setting up the macro to your liking, click the Close button in the lower-right corner of the dialog.

Then, in the Save dialog, click Yes to save the macro, click No to leave Macro Editor without saving the

changes, or click Cancel to return to the Macro Editor.

The Macro Editor save dialog

To add the macro to your node tree, right-click anywhere on the node tree and select Macro >

[NameOfYourMacro] from the contextual menu.

Saving a Macro as a Title Template in the Edit Page (DaVinci Resolve)

When using DaVinci Resolve, macros are available only in the Fusion page. However, if the macro

is a title animation, you can save it to the Titles Templates folder and have it appear in the Edit page

Effects Library.

To save a title macro so it appears in the Edit page Effects Library, save the macro to:

macOS: Users > UserName > Library > Application Support > Blackmagic Design >

DaVinci Resolve > Fusion > Templates > Edit > Titles

Windows: C Drive > Users > UserName > AppData > Roaming > Blackmagic Design >

DaVinci Resolve > Support > Fusion > Templates > Edit > Titles

The Final Macro

The final macro looks and behaves just like any other node in Fusion.

As another example, you could take a single Channel Boolean, set it to Add mode, and make it into a

macro exposing no controls at all, thus creating the equivalent of an Add Mix node like the one that

can be found in programs like Nuke.

Pipe Router

Pipe Routers are another type of organizational tool you use to improve the layout and appearance of

the node tree.

Router Introduction

Routers can be used to neatly organize your comps by creating “elbows” in your node tree, so the

connection lines do not overlap nodes, making them easier to understand. Routers do not have any

influence on render times.


Fusion Page Effects | Chapter 102 Flow Organizational Nodes

FUSION

Usage

A Pipe Router usage example

Router

To insert a router along a connection line, Option- or Alt-click on the line. The router can then be

repositioned to arrange the connections as needed.

Although routers have no actual controls, they still can be used to add comments to a comp.

An example comment in a Router node


Fusion Page Effects | Chapter 102 Flow Organizational Nodes

FUSION

Chapter 103

Fuses

This chapter introduces Fuses, which are scriptable plugins that can

be used within Fusion.

Contents

Fuses [Fus]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2295

Fuses Introduction����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2295

Installing Fuses����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2295

Working with Fuses in a Composition������������������������������������������������������������������������������������������������������������������������������������� 2295


Fusion Page Effects | Chapter 103 Fuses

FUSION

Fuses [Fus]

A Fuse node

Fuses Introduction

Fuses are plugins. The difference between a Fuse and an Open FX plugin is that a Fuse is created

using a Lua script. Fuses can be edited within Fusion or DaVinci Resolve, and the changes you make

compile on-the-fly.

Using a Lua script makes it easy for even non-programmers to prototype and develop custom nodes.

A new Fuse can be added to a composition, edited and reloaded, all without having to close the

current composition. They can also be used as modifiers to manipulate parameters, curves, and text

very quickly. ViewShader Fuses can make use of the GPU for faster performance. This makes Fuses

much more convenient than an Open FX plugin that uses Fusion’s OFX SDK. However, this flexibility

comes at a cost. Since a Fuse is compiled on-the-fly, it can be significantly slower than the identical

node created using the Open FX SDK.

As an example, Fuses could generate a mask from the over-exposed areas of an image, or create

initial particle positions based on the XYZ position stored within a text file.

Please contact Blackmagic Design for access to the SDK (Software Developer Kit) documentation.

Installing Fuses

Fuses are installed in the Fusion:\Fuses path map. By default this folder is located at

Users/ User_Name/Library Application Support/Blackmagic Design/Fusion (or DaVinci Resolve)/Fuses

on macOS or C:\Users\User_Name\AppData\Roaming\Blackmagic Design\Fusion (or DaVinci Resolve)\

Fuses, on Windows. Files must use the extension .fuse, or they will be ignored by Fusion.

Working with Fuses in a Composition

Fuses can be designed to appear in any category in the Effects Library. Once installed, they are added

to a composition exactly as any native or third-party plugin node. However, since a Fuse is just a text

document, it can be edited by clicking the Edit button that appears at the top of the Inspector when

the Fuse node is selected. This will open the Fuse in the default script editor specified in the Global

Preferences/Scripting panel.

NOTE: Any changes made to a Fuse’s script do not immediately affect other copies of the

same Fuse node already added to a composition. To use the updated Fuse script on all

similar Fuses in the composition, either close and reopen the composition, or click on the

Reload button in each Fuse’s Inspector.

When a composition containing a Fuse node is opened, the currently saved version of the Fuse script

is used. The easiest way to ensure that a composition is running the current version of a Fuse is to

close and reopen the composition.


Fusion Page Effects | Chapter 103 Fuses

FUSION