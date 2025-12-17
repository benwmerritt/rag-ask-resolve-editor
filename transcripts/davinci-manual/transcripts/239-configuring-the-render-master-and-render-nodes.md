---
title: "Configuring the Render Master and Render nodes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 239
---

# Configuring the Render Master and Render nodes

There are two roles played by computers involved in network rendering.

�The Render Master manages the list of compositions to be rendered (the queue) and allocates

frames to Render nodes for rendering. Metaphorically speaking, the Render Master is the traffic

cop of this process.

�The Render nodes are the main computers used for the rendering process. All computers involved

in network rendering must be on the same network subnet, and they all must have access to the

various files (including Fonts and third-party plugins) used to create the composite. The path to the

files must be the same for each computer involved in rendering.

Preparing the Render Master

The Render Master manages the list of compositions to be rendered (the queue) and allocates frames

to Render nodes for rendering. The Render Master is also used to maintain the Render node list and

to push updates to the various Render nodes when needed. At least one computer in the render farm

must be configured to act as the Render Master.

Any copy of Fusion can act as a Render Master by setting up the Fusion Network Preferences.

The Network panel sets up computers as Render Masters.

Acting as a Render Master has no significant impact on render performance. The system resources

consumed are insignificant. However, there are specific steps you must take to make one of your

computers a Render Master.

To set up the Render Master:


Install a copy of Fusion Studio on the computer you want to be the Render Master.


In Fusion Studio, choose Fusion Studio > Preferences on macOS or File > Preferences on

Windows and Linux


In the Preferences dialog, select the Global > Network Preferences panel.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION


Enter the name of the Render Master in the Name field and enter the IP address.


Enable the Make This Machine a Render Master checkbox.


If you want to use this computer as part of the render farm, enable the Allow This Machine to Be

Used as a Render Node checkbox as well.

To have the Render Node act as the Render Manager:

�Select a node in the Render Manager and choose Set Default Master from the contextual menu.

Once a computer is enabled to act as the master, use the Render Manager to add the Render nodes it

will manage. The Render Manager dialog is described in detail later in this chapter.

Preparing Render Nodes

Before you can begin rendering on the network, the Render nodes must be set up to accept

instructions from the Render Master.

In Fusion Studio, you can enable the computer to be used as a Render node in two ways:

�Choose File > Allow Network Renders.

�Enable the Allow This Machine to Be Used as a Network Render Node in the Global >

Network Preferences.

On a macOS Render Node computer:

�Click the Render Node icon in the menu bar and choose Allow Network Renders.

The Render Node menu

accessed in the macOS menu bar

On a Linux Render Node computer:

�Right-click the Fusion Render Node icon in the App Launcher and choose Allow Network Renders.

On a Windows Render Node computer:

�Right-click the Fusion Render Node icon in the taskbar Notification area and choose

Allow Network Renders.

Setting Up the Render Manager

The Render Manager window is used to monitor the progress of rendering. It can be used to reorder,

add, or remove compositions from a queue, and to manage the list of Render nodes used for

rendering. To open the Render Manager window in Fusion Studio, choose File > Render Manager.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

The Render Manager is used to reorder, add, and remove compositions from a render queue.

The Render Master is always listed as the first computer in the Render Node list along the right side.

This allows the Render Manager to render local queues without using the network. For the Render

Master to control additional Render nodes, the nodes must be added to the Render Node list.

Right-clicking in the Render Node list allows you to add Render nodes by entering the Render node’s

name or IP address. You can also choose Scan to have the Render Manager look for Render nodes on

the local network.

The Render Manager is used to add Render nodes.

Scanning for Render Nodes

With the Render Manager open, you can scan for Render nodes by right-clicking in the Render

Manager’s Render Node list and choosing Scan for Render Nodes from the drop-down menu.

Scanning looks through all IP addresses on the network subnet to determine whether any other

computers in the local network are actively responding on the port Fusion uses for network rendering.

A copy of the Fusion Render node must be running on the remote computer in order for it to be

detected by the scan.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Manually Adding Render Nodes

To manually add a Render node to the Render Node list, right-click in the Render Manager’s Render

Node list and choose Add Render Node from the drop-down menu.

The Add Render Node dialog allows you to

manually enter a Render Node name or IP

address to locate it on the subnet.

In the Add Render Node dialog that opens, enter the name or the IP address of the remote Render

node. The Render Manager will attempt to resolve names into IP addresses and IP addresses into

names automatically. You can use this method to add Render nodes to the list when they are not

currently available on the network.

Removing Render Nodes

To remove a computer from the Render Node list, right-click over the Render Node in the Render

Node list and choose Remove Render Node(s) from the pop-up menu. You can use Command on

macOS or Ctrl on Windows and Linux to select multiple Render nodes for removal.

Loading and Saving Render Node Lists

The list of Render nodes is automatically saved in the Documents > Blackmagic Design > Fusion >

Queue folder when you quit the Render Manager. You can save and reload alternative lists of Render

nodes by choosing Render Node > Save Render Node List and Load Render Node list from the menu.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Submitting Comps to Network Render

To submit a comp to render on the network, you can use the Render Manager, the Render Settings

dialog, or a third-party render farm application. The Render Settings dialog is quicker, while the

Render Manager and third-party render farm applications can provide more feedback and control over

the process.

Using the Render Settings Dialog for Network Rendering

When starting a preview or a final render, selecting the Use network checkbox from the Render

Settings dialog and submitting the render adds a composition to the end of the current queue in the

Render Manager. The Render Master used is based on the Fusion preferences from the workstation

submitting the comp.

The Use Network checkbox

enables network rendering from

the Render Settings dialog.

NOTE: Distributed network rendering works for image sequences like EXR, TIFF, and DPX.

You cannot use network rendering for Quicktime, H264, ProRes, or MXF files.

Using the Render Manager Window for Network Rendering

The Render Manager uses a render queue that lets you batch render comps. Compositions are

rendered in the order in which they are listed in the Render Manager, with the top entry rendered first,

followed by the next item down, and so on. Multiple comps in a queue may render simultaneously

depending on the group of Render nodes they are using and the priority assigned to each comp.

To add a comp to the queue in the Render Manager:

�Click the Add Comp button and navigate to the comp on your hard drive.

�Right-click in the queue list and select Add Comp from the drop-down menu, and then navigate to

the comp on your hard drive.

�Drag a comp file from an OS window into the Render Manager’s queue list.

The Add Comp button in the Render Manager adds a

comp to the queue for batch rendering over the network.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Removing a Composition from the Queue

To remove a composition from the queue, select the composition in the queue list and press the

Backspace/Delete key or right-click over the comp in the queue list and choose Remove Composition

from the drop-down menu.

Saving and Reloading Queue Lists

It can be useful to save a queue list to reuse at a later time. The current queue list is saved in the

Documents > Blackmagic Design > Fusion > Queue folder. To save the current queue with a new

name, choose File > Save Queue As in the Render Manager menu bar. To reload a saved Queue,

choose File > Load Queue and navigate to the saved location.

Reordering the Queue Lists

In the middle of a job, priorities for finishing a composition may change. Shifting deadlines may require

that a composition further down in the queue be rendered sooner. You can move comps to a new

position in the queue by dragging them in the queue list. If a composition with a status set to Done is

moved lower in the queue, it does not re-render. To re-render a comp, right-click on the comp in the

queue and choose Clear Completed frames from the drop-down menu.