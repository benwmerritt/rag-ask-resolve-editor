---
title: "The Fusion Page"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 7
---

# The Fusion Page

The Fusion page is intended, eventually, to be a feature-complete integration of Blackmagic Design

Fusion, a powerful 2D and 3D compositing application with over thirty years of evolution serving

the film and broadcast industry, creating effects that have been seen in countless films and

television series.

Merged right into DaVinci Resolve with a newly updated user interface, the Fusion page makes it

possible to jump immediately from editing right into compositing, with no need to export media, relink

files, or launch another application to get your work done. Everything you need now lives right inside

DaVinci Resolve.

The Fusion page showing Viewers, the Node Editor, and the Inspector

For more information on using the Fusion page, see Chapter 63, “Introduction to Compositing

in Fusion.”

The Work Area

You’ll probably not see this term used much, in favor of the specific panels within the work area that

you’ll be using, but the area referred to as the Work Area is the region at the bottom half of the Fusion

page UI, within which you can expose the three main panels used to construct compositions and edit

animations in the Fusion page. These are the Node Editor, the Spline Editor, and the Keyframes Editor.

By default, the Node Editor is the first thing you’ll see, and the main area you’ll be working within, but it

can sit side by side with the Spline Editor and Keyframes Editor as necessary, and you can make more

horizontal room on your display for these three panels by putting the Effects Library and Inspector into

half-height mode, if necessary.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

The Work Area showing the Node Editor, the Spline Editor, and Keyframes Editor

Viewers

The Viewer Area area encompasses the Time Ruler and transport controls. The Time Ruler is the

principal “timeline” of the Fusion page, which focuses exclusively on the current composition you’re

working on and may consist of one clip or several. This area can be set to display either one or two

viewers at the top of the Fusion page, chosen via the Viewer button at the far right of the Viewer title

bar. Each viewer can show a single node’s output from anywhere in the node tree. You assign which

node is displayed in which viewer. This makes it easy to load separate nodes into each viewer for

comparison. For example, you can load a Keyer node into the left Viewer and the final composite into

the right Viewer, so you can see the image you’re adjusting and the final result at the same time.

Dual viewers let you edit an upstream node in one while seeing its effect on the overall composition in the other

Ordinarily, each viewer shows 2D nodes from your composition as a single image. However, when

you’re viewing a 3D node, you have the option to set that viewer to one of several 3D views, including

a perspective view that gives you a repositionable stage on which to arrange the elements of the

world you’re creating, or a quad view that lets you see your composition from four angles, making

it easier to arrange and edit objects and layers within the XYZ axes of the 3D space in which

you’re working.

Toolbar

The toolbar, located underneath the Time Ruler, contains buttons that let you quickly add commonly

used nodes to the Node Editor. Clicking any of these buttons adds that node after the currently

selected node in the node tree, or adds an unconnected instance of that node if no nodes

are selected.

The toolbar has buttons for adding commonly used nodes to the Node Editor


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

The toolbar is divided into six sections that group commonly used nodes together.

As you hover the pointer over any button, a tooltip shows you that node’s name.

Effects Library

The Effects Library on the Fusion page shows all of the nodes and effects that are available in the

Fusion page, including effects that come with DaVinci Resolve and third-party OFX, if available. While

the toolbar shows many of the most common nodes you’ll be using in any composite, the Effects

Library contains every single tool available in the Fusion page, organized by category, with each node

ready to be quickly added to the Node Editor. Suffice it to say there are many, many more nodes

available in the Effects Library than on the toolbar, spanning a wide range of uses.

The Effects Library with Tools open

Node Editor

The Node Editor is the heart of the Fusion page, because it’s where you build the tree of nodes that

makes up each composition. Each node you add to the node tree adds a specific operation that

creates one effect, whether it’s blurring the image, adjusting color, painting strokes, drawing and

adding a mask, extracting a key, creating text, or compositing two images into one.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

The Node Editor displaying a node tree creating a composition

Inspector

The Inspector is a panel on the right side of the Fusion page that you use to display and manipulate

the parameters of one or more selected nodes. When a node is selected in the Node Editor, its

parameters and settings appear in the Inspector, ready for you to modify. The Fusion Inspector is

divided into two panels. The Tools panel shows you the parameters of selected nodes.

The Modifiers panel shows you different things for different nodes. For all nodes, it shows you

the controls for Modifiers, or adjustable expressions, that you’ve added to specific parameters to

automatically animate them in different ways.

The Inspector shows parameters

from one or more selected nodes

Nodes with different tabs expand the Controls,

Transform, and Settings parameters


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Additionally, many nodes expose multiple tabs’ worth of controls in the Inspector,

seen as icons at the top of the parameter section for each node. Click any tab to

expose that set of controls.

Thumbnail Timeline

Hidden by default, the Thumbnail timeline can be opened by clicking the Clips button in the UI Toolbar

and appears underneath the Node Editor when it’s open. The Thumbnail timeline shows you every

clip in the current Timeline, giving you a way to navigate from one clip to another when working on

multiple compositions in your project and providing an interface for creating and switching among

multiple versions of compositions and resetting the current composition, when necessary.

The Thumbnail timeline lets you navigate the Timeline and manage versions of compositions

Media Pool

In the Fusion page, the Media Pool continues to serve its purpose as the repository of all media you’ve

imported into your project. This makes it easy to add additional clips to your compositions simply by

dragging the clip you want from the Media Pool into the Node Editor. The media you add appears as a

new MediaIn node in your composition, ready to be integrated into your node tree however you need.

The Media Pool in Thumbnail mode showing video clips


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO