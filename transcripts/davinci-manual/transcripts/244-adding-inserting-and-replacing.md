---
title: "Adding, Inserting, and Replacing"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 244
---

# Adding, Inserting, and Replacing

Nodes Using the Contextual Menu

Another way of adding, inserting, and replacing nodes is to use the Node Editor’s contextual menu,

which has dedicated submenus that let you create any kind of node available in Fusion. This can be a

convenient when the pointer is already in the Node Editor selecting, moving, or connecting nodes.

Methods of adding nodes using the contextual menu:

�To add a node: Right-click in an empty area of the Node Editor, and choose a node from the

Add Tool submenu.

�To insert a node: Right-click a node in the Node Editor, and choose a node from the Insert

Tool submenu.

�To replace a node: Right-click a node in the Node Editor, and choose a node from the

Replace Tool submenu.

TIP: When you replace one node with another, any settings that are identical between the

two nodes are copied into the new node. For example, replacing a Transform node with a

Merge will copy the existing center and angle values from the Transform to the Merge.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Deleting Nodes

To delete one or more selected nodes, press Delete (macOS) or Backspace (Windows), or right-click

one or more selected nodes and choose Delete from the contextual menu. The node is removed

from the Node Editor, and whichever nodes are connected to its primary input and output are now

connected together. Nodes connected to other inputs (such as mask inputs) become disconnected.

Before deleting a node from a node tree (top), and after upstream

and downstream nodes have automatically reconnected (bottom).

Disconnected Nodes

It’s perfectly fine to have disconnected nodes, or even entire disconnected branches of a node tree,

in the Node Editor alongside the rest of a composition. All disconnected nodes are simply ignored

while being saved for possible future use. This can be useful when you’re saving nodes that you’ve

customized but later decided you don’t need. It’s also useful for saving branches of trees that you’ve

since exported to be self-contained media that’s re-imported to take the place of the original effect,

but you want to save the original nodes just in case you need to redo your work.

Selecting and Deselecting Nodes

In order to work with nodes in the Node Editor in any way, or modify node parameters in the Inspector,

you first need to learn to select the node or nodes you want to work with.

Selecting Nodes

Selecting nodes is one of the most fundamental things you can do to move nodes or target them for

different operations. There are a variety of methods you can use.

Methods of selecting nodes:

�To select a single node: Click any node in the Node Editor.

�To select multiple nodes one at a time: Command-click each node you want to select.

�To select a whole region of nodes: Drag a bounding box around all nodes you want to select.

�To select all upstream or downstream nodes: Right-click a node and choose Select >

Upstream Nodes/Downstream Nodes from the contextual menu.

�To select all nodes in the Node Editor: Press Command-A.

�To select a node from the Keyframe Editor: Click any layer in the Keyframe Editor to select the

corresponding node in the Node Editor.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

The Active Node

When you select a single node using any of the methods described above, the selected node is

known as the active node, and is highlighted orange to indicate that its parameters are currently

editable in the Inspector (if the Inspector is open). This also indicates that node will be targeted for

specific operations (such as inserting new nodes).

While multiple nodes can be selected, only one node will be the active node. To indicate the

difference, the active node remains highlighted with orange, while all other selected nodes are

highlighted with white. Unselected nodes have simple black outlines.

The active node is highlighted orange, while other selected nodes are highlighted white.

To set the active node when there are multiple selected nodes:

�Option-click one of the selected nodes in the Node Editor to make that one the active node.

�Open the Inspector (if necessary), and click a node’s header bar to make it the active node.

Deselecting Nodes

Deselecting nodes, when necessary, works pretty much as you would expect.

Methods of deselecting nodes:

�Click once in the background of the Node Editor to deselect all nodes.

�Press Command-Shift-A to deselect all nodes.

�Command-click to deselect multiple nodes one at a time.

�Command-drag a bounding box to deselect a group of selected nodes at one time.

Loading Nodes into Viewers

Once you’ve started building a composition, the next thing you need to learn is how to view specific

nodes that you want to work on. This is important because the combination of which node is being

viewed and which node is currently selected (these aren’t always the same node) often determines

which onscreen controls are available and how they appear.

In the following example, you’re set up to rotoscope an image using a Polygon node that’s attached to

the garbage mask input of a MatteControl node which is inserting the mask as an alpha channel.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

A node tree for doing a simple rotoscoping job.

As seen in the screenshot above, you’ll want to load the upstream MediaIn or Loader node into a

viewer while the Polygon node is selected for editing in order to see the full image you’re rotoscoping

while keeping the Polygon node’s spline visible.

Viewed Nodes When You First Open Fusion

When you first open the Fusion page in DaVinci Resolve, the output of the current empty composition

(the MediaOut1 node) is usually showing in viewer 2. If you’re in Dual-viewer mode, viewer 1 remains

empty until you assign a node to one of them.

When you first open Fusion Studio with an empty comp, both viewers remain empty even after reading

in media using a Loader node. The viewers only display content when you assign a node to one of them.

There are several different ways to display a node in a viewer. Which ones you use depends on how

you like to work.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Node View Indicators

The View indicators are displayed under each node, and serve two purposes. First, they’re a clickable

interface for displaying a node’s output in one of the viewers. Second, they’re an indication of which

nodes in the Node Editor are being viewed. By default, there are two round indicators, representing

the two viewers. The left and right indicators correspond to the left and right viewers, regardless of

whether both viewers are visible or just one.

A viewer indicator enabled for the right

viewer and disabled for the left viewer.

To load a node into a viewer using the Node View indicators:

�Clicking an indicator turns it white to show that node is currently loaded in the corresponding

viewer. Clicking it again turns the indicator black and removes it from the viewer. Nodes only

display View indicators if they’re currently being viewed. If you want to view indicators, hovering

the pointer over the node makes the indicators visible and available for clicking.

�You can also use keyboard shortcuts to toggle each View indicator. The default two viewers are

assigned numeric keyboard shortcuts 1 and 2. Pressing the corresponding number once displays

the selected node in the appropriate display view, while pressing it again clears that display.

For complex compositions, you may need to open additional viewers. For example, one viewer may

be used to display the end result of the final comp, while another viewer displays the source, a third

viewer displays a mask, and a fourth viewer might be a broadcast monitor connected via a Blackmagic

DeckLink card or other display hardware. When you have more than two viewers, additional View

indicators are added and each one is assigned a consecutive number between 3 and 9.

The more viewers you add, the more you may need help remembering which viewer is represented by

which View indicator. Positioning the pointer over the View indicator in question will display a tooltip

with the name of the viewer it represents.

Drag and Drop Nodes into a Viewer

If the View indicators are too small of a target for you to click on reliably and you are not keyboard

oriented, another way to load a node into a viewer is to drag and drop it onto the viewer you want to

load it into. This offers a quick explicit way to assign a node to a viewer, especially for pen and tablet

users. Please note that as you drag, the node will appear to move at first, but it’ll snap back into its

original location once the pointer leaves the Node Editor.

Using the Contextual Menu

You can also right-click a node, and then choose View On > Left or Right to display the node on the

appropriate viewer.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION