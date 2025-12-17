---
title: "Resetting Defaults"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 251
---

# Resetting Defaults

Even if you’ve created new default settings for new nodes, you can always reset individual parameters

to the original default setting. In addition, it’s easy to restore the original default settings for new nodes

you create.

To reset a single parameter to the original default settings:


Create a new node.


Open the Inspector and customize a parameter to the new default value you want it to have.


Right-click that parameter in the Inspector, and choose Set to Default from the contextual menu.

To reset every parameter in a node to the original defaults, do one of the following:

�Right-click on the node and choose Settings > Reset Default.

�Right-click that node’s control header in the Inspector, and choose Settings > Reset Default.

�Delete the .setting file from the Defaults folder.

NOTE: When you use the Settings > Reset Default command, the default .setting file is

deleted. If you want to save a node’s settings as alternate settings, you should use the

Settings > Save As command.

Saving and Loading Alternate Node Settings

Once you change parameter values for a node using the Inspector, those values can also be saved as

an alternate setting for that node, which can be reused at a later time.

To save alternate settings for a node:


Right-click on a tool, and then choose Settings > Save As from the contextual menu.


When the Save File dialog appears, enter a name for the Setting and save it to your hard drive.

Unlike saved defaults, the .settings files can be saved anywhere on the file system. They do not

need to be in the Default Settings folder.

To load a saved setting for one or more nodes:


Right-click a node and choose Settings > Load from the contextual menu.


Use the Open File dialog to select the settings you want to load into that node, and then click

Open. Those settings are now applied to that node.

Adding Saved Settings from the File System

Saved settings in your File system can also be used to create new nodes by dragging the .setting file

into the Node Editor from a standard file browser. Once dropped, that setting turns into a new node.

TIP: If you drop a setting directly onto a connection line, the new node will be inserted onto

that connection.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Node Modes Including Disable and Lock

Right-clicking one or more nodes and opening the contextual menu reveals a series of commands in

the Modes submenu, some with accompanying keyboard shortcuts, that let you set control visibility,

disable, lock, update, and cache nodes.

�Show Controls: Sets whether that node reveals its parameters in the Inspector when it’s selected

and whether its onscreen controls appear in viewers. On by default.

�Pass Through: (Command-P) Identical to the toggle switch in the Inspector that turns nodes off

and on. Disabled nodes are ignored as image data is passed from the next previous upstream

node to the next downstream node. On by default.

�Locked: (Command-L) Identical to the lock button in the Inspector that prevents a node from being

edited in the Inspector. Off by default.

�Update: (Command-U) On by default. While this option is enabled, all changes to the node will

cause it to re-render. When Update is disabled, you can still change the node’s parameters, but

those changes will not process or update the image until Update is re-enabled. While disabled,

the last processed image for that node will be displayed as a freeze frame. One example of when

this is useful is when you have a large or processor-intensive composition (such as a particularly

intense particle system), and disabling this option temporarily will let you quickly make several

quick parameter adjustments to different nodes without forcing you to wait for the node tree to

re-render after every adjustment. Another example of when this is useful is when you want to

quickly see the effect of animated downstream nodes while keeping upstream nodes that are too

processor-intensive to play in real time from rendering additional frames.

�Force Cache: When enabled, this node’s output for the current frame has an extremely high cache

priority, essentially forcing it to stay cached in memory. Off by default.

Toggling any one of these node modes displays a badge within that node indicating its state.

Node Editor Options

Right-clicking in an empty area of the Node Editor will bring up the contextual menu and the Options

submenu. The Options submenu contains several choices that can be used to customize how the

Node Editor looks and behaves.

�Pipes Always Visible: Enabling this option causes a connection to cross over a node instead of

beneath it, sometimes making it easier to follow the connection’s path.

�Show Hidden Pipes: When enabled, the Inspector option to Hide Incoming Connections in every

node is overridden and all connections are displayed in the Node Editor.

�Aspect Correct Tile Pictures: Aspect Correct Tile Pictures forces the display of thumbnails to be

aspect corrected, which is slower but visually more accurate. This option is enabled by default.

�Full Tile Render Indicators: Enabling this option causes the thumbnail to flash green

when rendering, which makes it easier to identify which node is processing in a large,

complex node tree.

�Show Grid: This option can be used to enable or disable the Node Editor’s background grid.

�Show Instance Links: When enabled, the Node Editor draws a green connection between an

instanced node and its parent.

�Auto Remove Routers: If routers are disconnected from a tool, they are automatically deleted

from the Node Editor. This option is enabled by default to eliminate the need to delete

orphaned routers.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

�Show Navigator: Enabling this option displays a small overview window of the entire node tree in

the Node Editor’s top-right corner. For more information, see the Navigator section in this chapter.

�Auto Navigator: The Navigator only appears when one or more nodes is outside the visible area

of the Node Editor. For more information, see the Navigator section in this chapter.

�Build Flow Vertically/Horizontally: Node trees can be built either horizontally from left to right or

vertically from top to bottom. Enabling one of these options determines whether new nodes are

added beneath the current node or to the right of the current tool.

�Orthogonal/Direct Pipes: Use these two options to decide whether connections between nodes

are drawn as Direct (straight) lines or Orthogonal (bent) lines.

Node Tooltips and the Status Bar

Even in simple node trees, it’s easy to forget some essential detail about the nodes in your comp.

To help you figure out what everything’s for, you can hover the pointer over any node in the Node

Editor to display information in the Status bar at the bottom of the Node Editor consisting of that node’s

name, frame size, pixel aspect, resolution, and color depth.

The Status bar located beneath the Node Editor.

If you wait a few moments later, a more elaborate presentation of the same information appears within

a floating tooltip in the Inspector. This tooltip gives you additional information about the Domain (Image

and DoD) and the data range used by that clip.

The floating tooltip showing node information

that appears within the Node Editor.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Chapter 68

Node Groups,

Macros, and

Fusion Templates

This chapter reveals how to use groups, macros, and templates in Fusion so

working with complex effects becomes more organized, more efficient, and easier.

Contents

Groups������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1367

Creating Groups����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1367

Deleting Groups���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1368

Expanding and Collapsing Groups�������������������������������������������������������������������������������������������������������������������������������������������� 1368

Panning and Scaling within Open Group Windows����������������������������������������������������������������������������������������������������������� 1368

Ungrouping Nodes ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1368

Saving and Reusing Groups ��������������������������������������������������������������������������������������������������������������������������������������������������������� 1369

Macros������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1369

Creating Macros����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1370

Using Macros������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1371

Re-Editing Macros�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1371

Other Macro Examples���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1372

Creating Fusion Templates������������������������������������������������������������������������������������������������������������������������������������������������������������ 1372

Getting Started with a Fusion Title Template������������������������������������������������������������������������������������������������������������������������� 1372

Saving a Title Macro��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1372

Using Your New Title Template����������������������������������������������������������������������������������������������������������������������������������������������������� 1376

Getting Started with a Fusion Transition Template������������������������������������������������������������������������������������������������������������� 1377

Creating a Fusion Transition Template�������������������������������������������������������������������������������������������������������������������������������������� 1377

Using Your New Transition Template���������������������������������������������������������������������������������������������������������������������������������������� 1380

Getting Started with a Fusion Generator Template������������������������������������������������������������������������������������������������������������ 1381

Creating a Fusion Generator Template������������������������������������������������������������������������������������������������������������������������������������� 1381


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

Groups

When you work on complex visual effects, node trees can become sprawling and unwieldy, so

grouping tools together can help you better organize all the nodes and connections. Groups are

containers in your node tree that can hold multiple nodes, similar to the way a folder on your Desktop

holds multiple files. There is no limit to the number of nodes that can be contained within a group, and

you can even create subgroups within a group.

Creating Groups

Creating a group is as simple as selecting the nodes you want to group together and using the

Group command.

To create a group:


Select the nodes you want grouped together.


Right-click one of the selected nodes and choose Group from the contextual menu (Command-G).

Several nodes selected in preparation for making

a group (top), and the resulting group (bottom).

Using Your New Generator Template��������������������������������������������������������������������������������������������������������������������������������������� 1384

Creating a Fusion Effect Template��������������������������������������������������������������������������������������������������������������������������������������������� 1384

Changing Durations of a Template��������������������������������������������������������������������������������������������������������������������������������������������� 1385

Creating Media Drop Zones in Templates������������������������������������������������������������������������������������������������������������������������������ 1386

Creating a Custom Template Icon����������������������������������������������������������������������������������������������������������������������������������������������� 1387

Using Fusion Template Bundles��������������������������������������������������������������������������������������������������������������������������������������������������� 1387


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

The selected nodes are collapsed into a group, which is displayed as a single node in the Node

Editor. The Group node can have inputs and outputs, depending on the connections of the nodes

within the group. The Group node only displays inputs for nodes that are already connected to nodes

outside the group. Unconnected inputs inside the group will not have an Input knot displayed on the

Group node.