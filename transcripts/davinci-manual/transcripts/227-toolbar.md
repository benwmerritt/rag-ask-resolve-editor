---
title: "Toolbar"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 227
---

# Toolbar

The toolbar, located underneath the Time Ruler, contains buttons that let you quickly add commonly

used nodes to the Node Editor. Clicking any of these buttons adds that node after the currently

selected node in the node tree, or adds an unconnected instance of that node if no nodes are

selected. The Toolbar can be customized and saved for specific tasks.

The toolbar has buttons for adding commonly used nodes to the Node Editor.

The default toolbar is divided into sections that group commonly used nodes together. As you hover

the pointer over any button, a tooltip shows you that node’s name.

�Loader/Saver nodes (Fusion Studio Only): The Loader node is the primary node used to

select and load clips from the hard drive. The Saver node is used to write or render your

composition to disk.

�Generator/Title/Paint nodes: The Background and FastNoise generators are commonly used to

create all kinds of effects, and the Title generator is obviously a ubiquitous tool, as is Paint.

�Color/Blur nodes: ColorCorrector, ColorCurves, HueCurves, and BrightnessContrast are the four

most commonly used color adjustment nodes, while the Blur node is ubiquitous.

�Compositing/Transform nodes: The Merge node is the primary node used to composite one

image against another. ChannelBooleans and MatteControl are both essential for reassigning

channels from one node to another. Resize alters the resolution of the image, permanently altering

the available resolution, while Transform applies pan/tilt/rotate/zoom effects in a resolution-

independent fashion that traces back to the original resolution available to the source image.

�Mask nodes: Rectangle, Ellipse, Polygon, and BSpline mask nodes let you create shapes to use

for rotoscoping, creating garbage masks, or other uses.

�Particle system nodes: Three particle nodes let you create complete particle systems when you

click them from left to right. pEmitter emits particles in 3D space, while pMerge lets you merge

multiple emitters and particle effects to create more complex systems. pRender renders a 2D

result that can be composited against other 2D images.

�3D nodes: Seven 3D nodes let you build sophisticated 3D scenes. These nodes auto attach to

one another to create a quick 3D template when you click from left to right. ImagePlane3D lets you

connect 2D stills and movies for compositing into 3D scenes. Shape3D lets you create geometric

primitives of different kinds. Text3D lets you build 3D text objects. Merge3D lets you composite

multiple 3D image planes, primitive shapes, and 3D text together to create complex scenes, while

Camera3D lets you frame the scene in whatever ways you like. SpotLight lets you light the scenes

in different ways and Renderer3D renders the final scene and outputs 2D images and auxiliary

channels that can be used to composite 3D output against other 2D layers.

When you’re first learning to use Fusion, these nodes are really all you need to build most common

composites. Once you’ve become a more advanced user, you’ll still find that these are truly the most

common operations you’ll use.

Customizing the Toolbar

You can add and remove tools from the Fusion toolbar and then save the custom toolbar as a preset.

New tools can be added by dragging them from the Effects Library or the Node Editor, and dividers

can be added to group tool sets together.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

To create a new toolbar, do the following:


Right click in an empty area of the toolbar and choose Customize > Create Toolbar from the

contextual menu.


Enter a name for the toolbar in the dialog box, and click OK.

To rearrange the tools in the toolbar, do the following:


Create a new custom toolbar or select an existing custom toolbar.


Drag a node in the toolbar to a new location.

To add a tool to the toolbar:


Create a new custom toolbar or select an existing custom toolbar.


Do one of the following:

�Drag a node from the Effects Library to the location on the toolbar where you want it added.

�Drag a node from the Node Editor to the location on the toolbar where you want it added.

To add a divider to a toolbar, do the following:


Create a new custom toolbar or select an existing custom toolbar.


Right-click over any tool and choose Customize > Add Divider. A divider is

added to the right of the tool.

To remove a tool from a toolbar, do the following:


Create a new custom toolbar or select an existing custom toolbar.


Right-click over any tool and choose Remove [name of tool].

To remove a group of tools between two dividers, do the following:


Create a new custom toolbar or select an existing custom toolbar.


Right-click over any tool in a group and choose Remove Group.

To prevent a custom toolbar from being modified:

Right-click over the toolbar and choose Lock from the contextual menu.

To switch between toolbars:

Right-click over the toolbar and choose the custom toolbar name or choose Default to return to

Fusion’s default toolbar.

To rename a custom toolbar, do the following:


Right-click over the toolbar and choose the name of the custom toolbar you want to rename.


Right-click over the toolbar again and choose Customize > Rename [toolbar name].


Enter a new name for the toolbar.

To delete a custom toolbar, do the following:


Right-click over the toolbar and choose the name of the custom toolbar you want to delete.


Right-click over the toolbar again and choose Customize > Remove [toolbar name].

TIP: Adding and deleting tools from a custom toolbar is not undoable. If you are creating a

complex toolset, make a new custom toolbar based on your current toolbar in between major

changes and work off that. That way if you make an error, you can revert back to the last

known good toolbar. Once you have the final toolbar the way you want it, you can go back

and remove all the interim custom toolbars you made.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Node Editor

The Node Editor is the heart of Fusion because it’s where you build the tree of nodes that makes up

each composition. Each node you add to the node tree adds a specific operation that creates one

effect, whether it’s blurring the image, adjusting color, painting strokes, drawing and adding a mask,

extracting a key, creating text, or compositing two images into one.

The Node Editor displaying a node tree creating a composition

You can think of each node as a layer in an effects stack, except that you have the freedom to route

image data in any direction to branch and merge different segments of your composite in completely

nonlinear ways. This makes it easy to build complex effects, but it also makes it easy to see what’s

happening, since the node tree doubles as a flowchart that clearly shows you everything that’s

happening, once you learn to read it.

Adding Nodes to Your Composition

Depending on your mood, there are a few ways you can add nodes from the Effects Library to your

composition. For most of these methods, if there’s a single selected node in the Node Editor, new

nodes are automatically added after it, but if there are no selected nodes or multiple selected nodes,

then new nodes are added as disconnected from anything else.

Methods of adding nodes include:

�Click a button in the toolbar.

�Open the Effects Library, find the node you want in the relevant category, and click once on a

node you’d like to add.

�Right-click on a node and choose Insert Tool from the drop-down menu to add it after the node

you’ve right-clicked on. Or, you can right-click on the background of the Node Editor to use that

submenu to add a disconnected node.

�Press Shift-Spacebar to open a Select Tool dialog, type characters corresponding to the name of

the node you’re looking for, and press the Return key (or click OK) when it’s found. Once you learn

this method, it’ll probably become one of your most frequently used ways of adding nodes.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

The Select Tool dialog lets you find

any node quickly if you know its name.

Removing Nodes from Your Composition

Removing nodes is as simple as selecting one or more nodes, and then pressing the Delete or

Backspace keys.

Identifying Node Inputs and Node Outputs

Each node displays small colored connections around the edges. One or more arrows represent

inputs, and the square connection represents the tool’s processed output, of which there is always

only one. If you hover the pointer over any of a node’s inputs or output, the name of that input or

output immediately appears in the Status bar. If you wait for a few more moments, a floating tooltip

displays the same name right over the node.

Node Editing Essentials

Each node has inputs and outputs that are “wired together” using connections. The inputs are

represented by arrows that indicate the flow of image data from one node to the next, as each node

applies its effect and feeds the result (via the square output) to the next node in the tree. In this way,

you can quickly build complex results from a series of relatively simple operations.

Three nodes connected together


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

You can connect a single node’s output to the inputs of multiple nodes (called “branching”).

One node branching to two to split the image to two operations

You can then composite images together by connecting the output from multiple nodes to certain

nodes such as the Merge node that combines multiple inputs into a single output.

Two nodes being merged together into one to create a composite

By default, new nodes are added from left to right in the Node Editor, but they can also flow from top

to bottom, right to left, bottom to top, or in all directions simultaneously. Connections automatically

reorient themselves along all four sides of each node to maintain the cleanest possible presentation as

you rearrange other connected nodes.

Nodes can be oriented in any direction; the input arrows let you follow the flow of image data.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION