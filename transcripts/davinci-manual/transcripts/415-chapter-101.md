---
title: "Chapter 101"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 415
---

# Chapter 101

Flow Nodes

This chapter details the Sticky Note and Underlay features available in Fusion.

The abbreviations next to each feature name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Sticky Note [Nte]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2287

Sticky Note Introduction����������������������������������������������������������������������������������������������������������������������������������������������������������������� 2287

Usage������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2287

Underlay [Und]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2288

Underlay Introduction���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2288

Usage������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2288


Fusion Page Effects | Chapter 101 Flow Nodes

FUSION

Sticky Note [Nte]

The Sticky Note

Sticky Note Introduction

A Sticky Note is not a node at all. It is a useful way of attaching notes, comments, and history to a

specific area of a comp. By changing their size and color, they can provide unobtrusive comments or

important notices, as required. Sticky Notes make an excellent complement to the Comments tab in

the Inspector.

Usage

A Sticky Note added to a node tree can provide a description

for other people or as a reminder to yourself

To create a Sticky Note, click in an empty area of the Node Editor where you want a Sticky Note to

appear. Then, from the Effects Library, click the Sticky Note effect located in the Tools > Flow category

or press Shift-Spacebar and search for the Sticky Note in the Select Tool window.

Like Groups, Sticky Notes are created in a smaller, collapsed form. They can be expanded by double-

clicking on them. Once expanded, they can be resized using any side or corner of the note or

moved by dragging on the name header. To collapse the Sticky Note again, click the icon in the top-

left corner.

To rename, delete, copy, or change the color of the note, right-click over the note and choose from the

contextual menu. Using this menu, you can also lock the note to prevent editing.

To edit the text in a Sticky Note, first expand it by double-clicking anywhere on the note, and then click

below its title bar. If the note is not locked, you can edit the text.


Fusion Page Effects | Chapter 101 Flow Nodes

FUSION

Underlay [Und]

The Underlay

Underlay Introduction

Underlays are a convenient method of visually organizing areas of a composition. As with Groups,

Underlays can improve the readability of a comp by separating it into labeled functional blocks. While

Groups are designed to streamline the look of a comp by collapsing complex layers down to single

nodes, Underlays highlight, rather than hide, and do not restrict outside connections.

Usage

Underlay node structure

As with Sticky Notes , an Underlay can be added to a comp by selecting it from the Flow category in

the Effects Library or searching for it in the Select Tool window. The Underlay to the Node Editor with

its title bar is centered on the last-clicked position.

Underlays can be resized using any side or corner. This will not affect any nodes.

Underlays can also be used as simple selection groups. Activating an Underlay, by clicking its title, will

select all the tools contained wholly within it as well, allowing the entire set to be moved, duplicated,

passed through, and so on.

To rename an Underlay, first ensure that nodes contained within the Underlay are not selected.

Then, Option-click on the Underlay title to select the Underlay without selecting the nodes it contains.

Once selected, right-click over the title and choose Rename. Underlays can be assigned a color using

the same right-click contextual menu.


Fusion Page Effects | Chapter 101 Flow Nodes

FUSION

Chapter 102

Flow Organizational

Nodes

This chapter details the Groups, Macro, and Pipe Router nodes, which are

designed to help organize your compositions, making the node tree easier

to see and understand.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Groups����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2290

Groups Introduction�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2290

Usage������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2290

Macro�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2291

Macro Introduction����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2291

Usage�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2291

Macro Editor������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2291

The Final Macro���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2292

Pipe Router������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2292

Router Introduction��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2292

Usage������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2293

Router������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2293


Fusion Page Effects | Chapter 102 Flow Organizational Nodes

FUSION

Groups

The Group node

Groups Introduction

Groups are used to keep complex node trees organized. You can select any number of nodes in the

node tree and then group them to create a single node icon in the Node Editor. Groups are non-

destructive and can be opened at any time.

Usage

�To group nodes, select them in the Node Editor, and then right-click over any of the selected

nodes and choose Group from the contextual menu.

Selecting nodes to group

�To edit the individual nodes in a group, right-click and choose Expand Group from the contextual

menu. All individual nodes contained in the group are displayed in a floating node tree window.

When opened, groups hover over existing elements, allowing editing of the enclosed nodes.

An opened node group

�To remove or decompose a group and retain the individual nodes, right-click the group and

choose Ungroup.


Fusion Page Effects | Chapter 102 Flow Organizational Nodes

FUSION