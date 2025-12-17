---
title: "Check the Composition"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 242
---

# Check the Composition

The Render Manager’s Status field in the render log indicates if a composition fails to render. Some

possible causes of this are as follows:

�No Render Nodes Could Be Found: On the Preferences Network tab, make sure that there is at

least one Render node available, running and enabled. If all Render nodes are listed as Offline

when they are not, check the network.

�The Composition Could Not Be Loaded: Some Render nodes may not be able to load a

composition while others can. This could be because the Render node could not find the

composition (check that the path name of the composition is valid for that Render node) or

because the composition uses plugins that the Render node does not recognize.

�The Render Nodes Stop Responding: If a network link fails, or a Render node goes down

for some reason, the Render node will be removed from the active list and its frames will be

reassigned. If no more Render nodes are available, the composition will fail after a short delay

(configurable in network preferences). If this happens, check the render log for clues as to which

Render nodes failed and why.

�The Render Nodes Failed to Render a Frame: Sometimes a Render node simply cannot render

a particular frame. This could be because the Render node could not find all the source frames

it needed, or the disk it was saving to become full or because of any other reason for which Fusion

might normally be unable to render a frame. In this case, the Render Manager will attempt to

reassign that failed frame to a different Render node. If no Render node can render the frame, the

render will fail. Try manually rendering that frame on a single machine and observe what happens.

�Check the Render Nodes: Fusion’s Render Manager incorporates a number of methods to

ensure the reliability of network renders. Periodically, the Render Manager will send signals called

Heartbeats, generated at regular intervals, to detect network or machine failures. In this event, a

failed Render node’s outstanding frames are reassigned to other Render nodes where possible.

In rare cases, a Render node may fail in a way that the heartbeat continues even though the

Render node is no longer processing. If a Render node failed (although the Render Master may

not have detected it) and you do not want to wait for the Frame Timeout, simply restart the Fusion

workstation or Fusion Render Node that has hung. This triggers the heartbeat check, reassigns

the frames on which that Render node was working, and the render should continue. Heartbeats

may fail if the system that is performing the render is making extremely heavy use of the Swap

file or is spending an extraordinary amount of time waiting for images to become available over a

badly lagged network. The solution is to provide the Render node with more RAM, adjust memory

settings for that node, or upgrade the network bandwidth.

�Check the Network: At the Render Master, bring up the Network tab of the Preferences dialog

box and click Scan. If a Render node is not listed as running, the Render Master will not be able to

contact it for network rendering. Alternatively, bring up a command prompt and ping the Render

nodes manually. If the remote systems do not respond when they are up and running, the network

is not functioning and should be examined further.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Chapter 67

Working in the

Node Editor

This chapter discusses how to work in the Node Editor, including multiple ways to

add, connect, rearrange, and remove nodes to create any effect you can think of.

Contents

Learning to Use the Node Editor������������������������������������������������������������������������������������������������������������������������������������������������� 1318

Navigating within the Node Editor��������������������������������������������������������������������������������������������������������������������������������������������� 1319

Automatic Node Editor Navigation���������������������������������������������������������������������������������������������������������������������������������������������� 1319

Using the Node Navigator��������������������������������������������������������������������������������������������������������������������������������������������������������������� 1319

Node View Bookmarks�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1320

Adding Nodes to a Composition������������������������������������������������������������������������������������������������������������������������������������������������ 1322

Adding, Inserting, and Replacing Nodes Using the Toolbar����������������������������������������������������������������������������������������� 1322

Adding Nodes Quickly Using the Select Tool Window���������������������������������������������������������������������������������������������������� 1323

Adding Nodes from the Effects Library������������������������������������������������������������������������������������������������������������������������������������ 1324

Adding, Inserting, and Replacing Nodes Using the Contextual Menu���������������������������������������������������������������������� 1327

Deleting Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1328

Disconnected Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1328

Selecting and Deselecting Nodes��������������������������������������������������������������������������������������������������������������������������������������������� 1328

Loading Nodes into Viewers�������������������������������������������������������������������������������������������������������������������������������������������������������� 1329

Viewed Nodes When You First Open Fusion������������������������������������������������������������������������������������������������������������������������ 1330

Node View Indicators������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1331

Drag and Drop Nodes into a Viewer������������������������������������������������������������������������������������������������������������������������������������������ 1331

Using the Contextual Menu������������������������������������������������������������������������������������������������������������������������������������������������������������ 1331

Clearing Viewers��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1332

Create/Play Preview�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1332

Connecting and Disconnecting Nodes����������������������������������������������������������������������������������������������������������������������������������� 1332

Node Basics������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1332

How to Connect Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1333

Dropping Connections on Top of Nodes�������������������������������������������������������������������������������������������������������������������������������� 1333

Identifying Node Inputs������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1335

Node Order Matters�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1335


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Upstream and Downstream Nodes ������������������������������������������������������������������������������������������������������������������������������������������ 1338

Disconnecting and Reconnecting Nodes������������������������������������������������������������������������������������������������������������������������������� 1338

Tracing Connections Through the Node Tree ��������������������������������������������������������������������������������������������������������������������� 1339

Branching������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1340

Connecting Merge Nodes��������������������������������������������������������������������������������������������������������������������������������������������������������������� 1341

Automatically Creating a Merge Node When Adding Nodes��������������������������������������������������������������������������������������� 1342

Automatically Creating a Merge Node by Connecting Two Outputs������������������������������������������������������������������������ 1343

Connection Options and Routers���������������������������������������������������������������������������������������������������������������������������������������������� 1344

Using Routers to Reshape and Branch Connections�������������������������������������������������������������������������������������������������������� 1345

Swapping Node Inputs ������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1346

Extracting and Inserting Nodes��������������������������������������������������������������������������������������������������������������������������������������������������� 1347

Cut, Copy, and Paste Nodes��������������������������������������������������������������������������������������������������������������������������������������������������������� 1348

Cut, Copy, and Paste in the Node Editor��������������������������������������������������������������������������������������������������������������������������������� 1348

Pasting Node Settings���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1349

Copying and Pasting Nodes to and from Any Text Editor���������������������������������������������������������������������������������������������� 1349

Using Multilayer Nodes (Studio Version Only)��������������������������������������������������������������������������������������������������������������������� 1350

Viewer������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1350

Nodes and Inspector��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1351

Input Layer Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1352

Instancing Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1352

Using Instanced Nodes�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1353

De-Instancing and Re-Instancing Specific Parameters��������������������������������������������������������������������������������������������������� 1354

Keeping Node Trees Organized������������������������������������������������������������������������������������������������������������������������������������������������� 1354

Moving Nodes�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1354

Renaming Nodes��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1355

Changing Node Colors�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1356

Using Sticky Notes����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1356

Using Underlay Boxes����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1357

Node Thumbnails������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1358

Choosing Which Nodes Show Thumbnails���������������������������������������������������������������������������������������������������������������������������� 1359

Switching Thumbnails between Images and Icons������������������������������������������������������������������������������������������������������������ 1360

Finding Nodes�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1360

Performing Simple Searches���������������������������������������������������������������������������������������������������������������������������������������������������������� 1361

Using Regular Expressions������������������������������������������������������������������������������������������������������������������������������������������������������������� 1361

Custom Node Settings�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1362

Managing Saved Settings��������������������������������������������������������������������������������������������������������������������������������������������������������������� 1362

Resetting Defaults������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1363

Saving and Loading Alternate Node Settings���������������������������������������������������������������������������������������������������������������������� 1363

Adding Saved Settings from the File System������������������������������������������������������������������������������������������������������������������������ 1363

Node Modes Including Disable and Lock������������������������������������������������������������������������������������������������������������������������������ 1364

Node Editor Options������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1364

Node Tooltips and the Status Bar���������������������������������������������������������������������������������������������������������������������������������������������� 1365


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Learning to Use the Node Editor

The Node Editor (formerly called the Flow or Flow Editor) is the heart of Fusion’s compositing interface.

It uses a flowchart structure called a node tree that lets you build a composition out of interconnected

nodes, as opposed to using layers in a layer list. Each clip you add to the composition, and each

image-processing operation you apply to those clips, is added as a node, all of which are joined

together with connections that propagate image data from one node to the next. Each individual node

performs a relatively simple operation, but collectively they combine to let you create wonderfully

complex results.

The Node Editor.

This chapter discusses how to work in the Node Editor in greater detail, showing you how to add,

connect, rearrange, and remove nodes to create any effect you can think of.

To display the Node Editor:

�Click the Nodes button on the UI toolbar.

The Nodes button in the UI toolbar.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Navigating within the Node Editor

The Node Editor is the place where everything relating to nodes and the construction of your

composites happens. The more you learn about how to navigate within the Node Editor, the faster

you’ll be able to work. There are a variety of standard methods of panning and zooming around the

Node Editor, many of which are shared with other panels in Fusion.

Methods of panning the Node Editor:

�Middle-click and drag to pan around the Node Editor.

�Hold down Shift and Command, and then click and drag within the Node Editor to pan.

�Drag with two fingers on a track pad to pan in the Node Editor

Methods of zooming the Nod4e Editor:

�Press the Middle and Left buttons simultaneously and drag to resize the Node Editor.

�Hold down the Command key and use your pointer’s scroll control to resize the Node Editor.

�Right-click the Node Editor and choose an option from the Scale submenu of the contextual menu.

�Press Command-1 to reset the Node Editor to its default size.

�Hold down the Command key and drag with two fingers on a track pad to resize the Node Editor.

Automatic Node Editor Navigation

If a node that is not visible in the Node Editor becomes selected, either by using the Find command

or by selecting a node’s header in the Inspector, the Node Editor will automatically pan to display the

node in the visible area.

Using the Node Navigator

Another useful way to pan around the Node Editor is to use the Node Navigator. The Node Navigator

is a small rectangular overview in the upper-right corner of the Node Editor. It gives a bird’s eye view of

the entire composition, with an inner outline that indicates the portion of the composition that is visible

in the panel. You can use the Node Navigator when you are zoomed in on a node tree and want to

pan around a composition.

The Node Navigator.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

To display or hide the Node Navigator, do one of the following:

�Right-click in an empty area of the Node Editor, and then choose Options > Show Navigator.

�Press the V key.

To have the Node Navigator resume displaying automatically when needed after you’ve closed it:

�Right-click in an empty area of the Node Editor, and then choose Options > Auto Navigator.

To change the size of Node Navigator, do the following:

�Drag the lower-left corner of the Navigator to resize it.

Drag the corner to resize the Navigator.

To return to the default Node Navigator size, do the following:

�Right-click anywhere within the Node Navigator and choose Reset Size.

To pan the Node Editor using the Node Navigator, do the following:

�Drag within the Node Navigator to move around different parts of your node tree.

�Within the Navigator, drag with two fingers on a track pad to move around different

parts of your node tree.