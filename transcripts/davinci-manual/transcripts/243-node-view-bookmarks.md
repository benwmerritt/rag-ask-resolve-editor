---
title: "Node View Bookmarks"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 243
---

# Node View Bookmarks

Bookmarks are another way of navigating the Node Editor. Bookmarks save the position and

scale of the Node Editor, so you can quickly and precisely jump from viewing one group of nodes

to viewing another.

To add a bookmark, do the following:


Pan and scale in the Node Editor to view a group of nodes you are interested in.


From the Options menu in the upper right of the Node Editor, choose Add Bookmark, or

press Cmd-D.


In the Manage Bookmarks dialog that opens, enter a name for the bookmark and click the

Add button.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

The first nine saved bookmarks are given keyboard shortcuts and listed in the Options menu.

They are also listed in the Go To Bookmarks dialog along with any saved bookmarks beyond

the initial nine.

The Node Editor Options menu

with nine bookmarks added

TIP: You can return the Node Editor to the default scale by right-clicking in the Node Editor

and choosing Scale > Default Scale or pressing Cmd-1.

If your Node Tree changes and you want to update Bookmark names or delete bookmarks, those

tasks can be done in the Manage Bookmarks dialog.

To rename or delete a bookmark, do the following:


From the Options menu in the upper right of the Node Editor, choose Manage Bookmarks.


In the Manage Bookmarks dialog that opens, right-click over the bookmark and

choose Rename or Remove.


Click OK to close the Manage Bookmarks dialog.

Using Bookmarks

You can jump to a Bookmark view by selecting a bookmark listed in the Options menu or choosing

Go To Bookmarks to open the Go To Bookmarks dialog. The Go To Bookmarks dialog has all the

bookmarks listed in the order they were created in the current composition. Double-clicking on any

entry in the dialog will update the Node Editor to that view and close the Go To Bookmarks dialog.

If you have a long list of bookmarks, you can use the search field at the bottom of the dialog to enter

the name of the bookmark you want to find.

Changing the Sort Order and Assigning Keyboard Shortcuts

Bookmarks appear in the Options menu and in the Go To Bookmarks dialog in the order they were

created. The top nine bookmarks listed are assigned keyboard short cuts. If you want to change the


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

sort order of the list you can do that in the Manage Bookmarks dialog. This can be useful if you want

some bookmarks to have specific keyboard shortcuts, or you want a bookmark you made early in the

process to not have a keyboard shortcut assigned to it.

To change the order of the listed bookmarks, do the following:


From the Options menu in the upper right of the Node Editor, choose  Manage Bookmarks.


In the Manage Bookmarks dialog drag a bookmark up or down in the list.


An insert line appears where the bookmark will be inserted. Release the mouse button when the

insert line is where you want the bookmark to be listed.

The keyboard short cuts will update to reflect the new order.

TIP: You can hold down the Shift key to select multiple bookmarks and move them

simultaneously up or down in the Manage Bookmark list.

Using Underlays as Bookmarks

Underlays added to the Node Editor are automatically added as bookmarks. They are listed in the

Options menu below the list of your custom bookmarks. You can omit Underlays from showing in

the list of bookmarks by opening the Go To Bookmarks dialog and disabling the checkbox to Show

Underlays. When the checkbox is disabled, Underlays will not show in the Go To Bookmarks dialog,

and they will not appear in the Options menu.

Adding Nodes to a Composition

You can add nodes to the Node Editor in a variety of ways, depending on the type of node you’re

adding, and how much guidance you need to find what you’re looking for. Additionally, the way you

add nodes to a composition may also be dictated by how you need to attach that node to the current

node tree.

Make Sure You’re Adding Compatible Nodes

It’s a good rule of thumb to make sure that whenever you’re adding or inserting new nodes

to the node tree, that you’re adding nodes that are compatible with the nodes you’re trying to

attach to. For example, you’ll have no problem inserting a Blur, Color, Filter, Paint, or Position

node after almost any 2D operation. However, if you try to add a Merge3D node after a Glow

node, it won’t automatically connect, because those two nodes cannot be connected directly.

Adding, Inserting, and Replacing Nodes Using the Toolbar

The Fusion toolbar, located above the Node Editor, displays a selection of frequently-used nodes,

displayed as buttons with distinct icons. These buttons make it fast to add Merge, Background, Paint,

Mask, Transform, and many other commonly used nodes with the click of a button, or the drag of

your pointer.

The Fusion page toolbar.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

TIP: If you don’t know which node a particular icon corresponds to, just hover your pointer

over any toolbar button and a tooltip will display the full name of that tool.

Methods of adding nodes by clicking toolbar buttons:

�To add a node after a selected node: Select a node in the Node Editor and then click a

toolbar button.

�To add a disconnected node to the Node Editor: Deselect all nodes in the Node Editor and then

click a toolbar button.

Methods of adding nodes by dragging toolbar buttons:

�To insert a new node into the node tree: Drag a toolbar button into the Node Editor and onto the

connection line between any two compatible nodes. When the connection highlights as the node

is over it, drop the node and it’ll be inserted.

�To create a disconnected node: Drag a toolbar button into an empty part of the Node Editor.

Dragging a toolbar button into the Inspector also creates a disconnected node.

�To insert a new node after a node loaded into a viewer: Drag a toolbar button onto a viewer to

insert a new node after whichever node is viewed, regardless of whether any nodes are selected.

To replace a node in the Node Editor with a node from the toolbar:


Drag a button from the toolbar so that it’s directly over the node in the Node Editor that you want

replaced. When the node underneath is highlighted, drop the node.

Dragging a node from the toolbar

to replace an existing tool.


Click OK in the dialog to confirm the replacement.

TIP: When you replace one node with another, any settings that are identical between the

two nodes are copied into the new node. For example, replacing a Transform node with a

Merge will copy the existing center and angle values from the Transform to the Merge.

Adding Nodes Quickly Using the Select Tool Window

The next fastest way of adding or inserting nodes to the Node Editor is using the Select Tool window,

which lets you search for any node available to Fusion by typing a few characters. Once you learn this

method, it’ll probably become one of your most frequently-used ways of adding nodes.

To use the Select Tool window to add nodes:


Do one of the following to determine if you want to insert a node or create a disconnected node:

�If you want to insert a node, select a node that’s compatible with the one you’ll be creating, and

the new node will be inserted after it.

�If you want to create a disconnected node, deselect all nodes.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION


Press Shift-Spacebar to open the Select Tool dialog.


When the window appears, type characters corresponding to the name of the node you’re looking

for. A list automatically appears with likely candidates, and you can use the Up and Down arrow

keys to select the correct node (if it’s not selected already). If you don’t know the name of the

exact tool you’re looking for, you can also type in common keywords and categories (i.e., keyer,

materials, etc.) to get a selection of tools based on your input.


When you’ve selected the correct node, press the Return key (or click OK), and that node will be

either inserted or added.

The Select Tool dialog lets you find any

node quickly if you know its name.

TIP: Whenever you use the Select Tool window, the text you entered is remembered the

next time you open it, so if you want to add another node of the same kind—for example, if

you want to add two Blur nodes in a row—you can just press Shift-Spacebar and then press

Return to add the second Blur node.

Adding Nodes from the Effects Library

While the toolbar shows many of the most common nodes you’ll be using in any composition, the

Effects Library contains every single tool available in Fusion, organized by category, with each node

ready to be quickly added to the Node Editor. If you need more guidance to find the node you’re

looking for, or if you just want to browse around and see what’s available, the Effects Library is the

perfect place to start.

To open the Effects Library:

�Click the Effects Library button in the UI toolbar at the top of the Fusion window.

The Effects Library appears at the upper-left corner of the Fusion window, and consists of two panels.

A category list at the left shows all categories of nodes and presets that are available, and a list at the

right shows the full contents of each selected category.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

The Tools bin of the Effects Library exposing 3D nodes.

By default, the category list shows the primary sets of effects: Tools, Open FX, Templates, and LUTs;

with disclosure controls to the left that hierarchically show all subcategories within each category.

The categories are:

�Tools: Tools consist of all the effects nodes that you use to build compositions, organized by

categories such as 3D, Blur, Filter, Mask, Particles, and so on.

�Open FX: All Resolve FX and any installed third party Open FX plugins will appear here.

�Templates: When using the Fusion page in DaVinci Resolve, templates consist of presets, macros,

and utilities that have been created to get you started quickly. For example, Backgrounds consists

of a variety of customizable generators that have been created using a combination of Fusion

tools. Lens flares presents a wide variety of multi-element lens flares that you can add to any

composition. Particles has a selection of pre-made particle systems that you can customize for

your own use. Shaders has a variety of materials that you can use as texture maps for 3D text and

geometry that you create in Fusion. And there are many, many other categories’ worth of useful

presets and macros that you can learn from and use in your own projects.

�LUTs: An assortment of pre-installed Look Up Tables for gamma, gamut, and colorspace

conversions can be found here. Inserting a LUT into the Node Editor creates a new FileLUT (FLUT)

node with the selected LUT file preloaded.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

For more information on adding your own LUTs to this list, see Chapter 150, “Using LUTs.”

Adding, Inserting, and Replacing Tools Using the Effects Library

Adding nodes to the Node Editor from the Tools category of the Effects Library is very similar to

adding nodes from the toolbar.

Methods of adding nodes by clicking in the Effects Library:

�To add a node after a selected node: Select a node in the Node Editor and then click a node in

the browser of the Effects Library.

�To add a disconnected node to the Node Editor: Deselect all nodes in the Node Editor and then

click a node in the browser of the Effects Library.

Methods of adding nodes by dragging from the Effects Library:

�To insert a new node into the node tree: Drag a node from the browser of the Effects Library

into the Node Editor and onto the connection line between any two compatible nodes. When the

connection highlights as the node is over it, drop the node and it’ll be inserted.

�To create a disconnected node: Drag a node from the browser of the Effects Library into an

empty part of the Node Editor. Dragging a toolbar button into the Inspector also creates a

disconnected node.

�To insert a new node after a node loaded into a viewer: Drag a node from the browser of the

Effects Library onto a viewer to insert a new node after whichever node is viewed, regardless of

whether any nodes are selected.

To replace a node in the Node Editor with a node from the Effects Library:


Drag a node from the browser of the Effects Library so it’s directly over the node in the Node

Editor that you want replaced. When that node is highlighted, drop it.


Click OK in the dialog to confirm the replacement.

Adding, Inserting, and Replacing Templates Using the Effects Library

Adding items from DaVinci Resolve’s Fusion page Templates category is often a bit different.

Sometimes, as when adding a Lens Flare, a single node can be added or inserted into the Node

Editor. When this is the case, adding nodes works the same as when adding from the Tools category.

Adding a Lens Flare effect.

Other times, such as when adding an item from the “How to” category, dragging a single item from the

Node Editor results in a whole node tree being added to the Node Editor. Fortunately, all nodes of the

incoming node tree are automatically selected when you do this, so it’s easy to drag the entire node

tree to another location in the Node Editor where there’s more room. When this happens, the nodes of

the incoming effect are exposed so you can reconnect and reconfigure it as necessary to integrate the

effect with the rest of your composition.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Adding a LightWrap effect from the “How to” bin of the Templates category of the Effects Library.