---
title: "Viewer Overview"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 256
---

# Viewer Overview

Viewers in Fusion display the current frame of the current composition in a variety of ways to help you

see what you’re doing and evaluate the final result of your compositing artistry. Viewers display 2D

images, but they can also display a 3D environment using a 3D View as well as a special Quad viewer

to help you effectively work in three dimensions.

Side-by-side dual viewers: a 3D viewer (left), and a 2D viewer (right)

Additionally, you can expose “subviews” including color inspectors, magnifiers, waveforms,

histograms, and vectorscopes to help you analyze the image as you work.

Viewer with a 3D Histogram subview at the upper left-hand corner

Single vs. Dual Viewers

By default, there are two viewers positioned side by side across the top of the window. However, you

can use the Single/Dual Viewer button to toggle between displaying a single viewer or two viewers

displayed side by side.

The Single/Dual Viewer toggle button


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Floating Viewers in Fusion Studio

In addition to the dual views above the Node Editor, Fusion Studio provides the option to use an

unlimited number of floating viewers. These floating viewers are excellent for taking full advantage of a

dual monitor configuration. Floating viewers can also be set to full-screen mode to make the best use

of screen real estate.

To create a new floating display view, select Window > New View from the menu bar at the top of the

screen. The position and configuration of the new view can be saved in the layout preferences, if required.

Video Output

When using DaVinci Resolve or Fusion Studio, if Blackmagic video hardware is present in the

computer, then you can select a node to preview directly on that display. While video output can’t be

used for manipulating onscreen controls such as center crosshairs or spline control points, they’re

extremely valuable for evaluating your composition via the output format, and for determining image

accuracy using a properly calibrated display.

The video hardware is configured from the DaVinci Resolve and Fusion Studio preferences.

Clean Feed

When using DaVinci Resolve with dual computer monitors, a full-screen viewer can be displayed on

the secondary monitor from the Fusion page. This displays a third view indicator button under each

node to control what is shown on the second display. To activate this monitor, make sure you do not

have Dual Screen enabled under the Workspace menu and then select Workspace > Video Clean

Feed and select your second computer display from the submenu.

Loading Nodes into Viewers

The Fusion page in DaVinci Resolve and Fusion Studio show two different things when you first open

each application. When you first open the Fusion page, the output of the current empty composition

(the MediaOut1 node) is usually showing in viewer 2. If you’re in dual-viewer mode, viewer 1 remains

empty until you assign a node to one of them. In Fusion Studio, because there are no nodes when you

first begin a comp, nothing is displayed in the viewers.

To load specific nodes into specific viewers, do one of the following:

�Hover the pointer over a node, and click one of two buttons that appear at the bottom-left of the node.

�Click once to select a node, and press 1 (for the left viewer) or 2 (for the right viewer).

�Right-click a node and choose View On > None/Left View/Right View in the contextual menu.

�Right-click the control header of a node in the Inspector, and choose View On > None/Left View/

Right View from the contextual menu.

�Drag a node and drop it over the viewer you’d like to load it into (this is great for tablet users).

When a node is being viewed, a View Indicator button appears at the bottom left. This is the same

control that appears when you hover the pointer over a node. Not only does this control let you know

which nodes are loaded into which viewer, but they also expose little round buttons for changing

which viewer they appear in.

Viewer assignment buttons at the

bottom left of nodes indicate when

they’re being viewed, and which

dot is highlighted indicates which

viewer that node is loaded into.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Clearing Viewers

To clear an image from a viewer, click in the viewer to make it active; a light purple outline is displayed

around the active panel. With the viewer active, press the ` (accent) key. This key is usually found to the

left of the 1 key on U.S. keyboards. The fastest way to remove all images from all viewers is to make

sure none of the viewers is the active panel, and then press the accent key.

Position and Layout

In Fusion Studio, when you resize and change the layout of viewers in the composition, that

configuration is always saved with the composition. So each time you open the composition, the size

and layout is remembered. You can prevent this behavior by disabling the Recall Layout checkbox in

the Fusion Global Layout preferences.

If you want all new compositions to open with a certain viewer layout, you can configure the layout

of the two primary viewers, and then use the Grab Document Layout button in the Fusion Global

Layout preferences to remember the layout for any new compositions. To save the position and size

of floating viewers, you use the Grab Program Layout button. Finally, if you want to have the floating

viewers opened automatically when you open Fusion, enable the Create Floating Views checkbox.

The Viewer Divider

You can change the relative sizes of the left and right viewers using the horizontal viewer divider that

runs between them. Drag the viewer divider to increase or decrease the amount of space used by one

viewer. The adjacent viewer will adjust to accommodate the new layout.

The amount of vertical space available for both viewers can be adjusted by dragging the horizontal

scrollbar between the viewers and the work area below them.

The viewer divider bar


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Zooming and Panning into Viewers

There are standardized methods of zooming into and panning around viewers when you need

a closer look at the situation. These methods also work with the Node Editor, Spline Editor, and

Keyframes Editor.

Methods of panning viewers:

�Middle-click and drag to pan around the viewer.

�Hold down Shift and Command and drag the viewer to pan.

�Drag two fingers on a track pad to pan.

Methods of scaling viewers:

�Click a viewer and press the Equals key (=) to zoom in, and the Minus key (-) to zoom out.

�Press the middle and left mouse buttons simultaneously and drag left or right to resize the viewer.

�Hold down the Command key and use your pointer’s scroll control to resize the viewer.

�Hold down the Command key and drag two fingers on a track pad to resize the viewer.

�Hold down the middle mouse button, and then click the left mouse button to zoom in, or click the

right button to zoom out. The scaling uses a fixed amount, centered on the position of the cursor.

�Click a viewer and press Command-1 to resize the image in the viewer to 100 percent.

�Click a viewer and press Command-2 to resize the image in the viewer to 200 percent.

�Click a viewer and press Command-F or Command-1 to reset the image in the viewer

to fit the viewer.

�Click the Scale Viewer menu and choose Fit or a percentage.

�Right-click on a viewer and choose an option from the Scale submenu of the contextual menu.

This includes a Custom Scale command that lets you type your own scale percentage

Methods of spinning 3D viewers:

�In 3D Perspective view, hold down the middle mouse button and the right mouse button and drag

to spin the stage around.

Flipbook Previews

As you build increasingly complex compositions, and you find yourself needing to preview specific

branches of your node tree to get a sense of how various details you’re working on are looking, you

may find it useful to create targeted RAM previews at various levels of quality right in the viewer by

creating a RAM Flipbook. RAM Flipbook Previews are preview renders that exist entirely within RAM

and allow you to render a node’s output at differing levels of quality for quick processing in order to

watch a real-time preview.

Creating Flipbook Previews

Creating a Flipbook Preview is relatively fast, once you know where to look.

To create a Flipbook Preview:


Choose the node in your node tree that you want to preview by doing one of the following:

�Hold down the Option key while dragging a node into the viewer.

�Right-click a node and choose an option from the Create/Play Preview submenu in the

contextual menu.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION


When the Preview Render dialog opens, choose the quality, resolution, and motion blur settings

you want to use for the Flipbook Preview.

The Flipbook Preview Render dialog


When you’ve chosen the settings you want to use, click Start Render.

The current frame range of the Time Ruler is rendered using the settings you’ve selected, and the

result is viewable in the viewer you selected or dragged into.

Once you’ve created a Flipbook Preview within a particular viewer, right-clicking that viewer presents

Flipbook-specific commands and options to Play, Loop, or Ping-Pong the Flipbook, to open it Full

Screen, to Show Frame Numbers, and to eliminate it.

TIP: If you want to create a Flipbook Preview and bypass the Render Settings dialog by just

using either the default setting or the settings that were chosen last, hold down Shift-Option

while you drag a node into the viewer. The Settings dialog will not appear, and rendering the

preview will start right away.

Playing Flipbook Previews

While the Flipbook Preview is loaded into a viewer, or open in full-screen mode, you can play or scrub

through it using the mouse and the keyboard.

To play back a Flipbook using the mouse, do the following:

�Double-click in the viewer to start playback.

To scrub through a Flipbook using the mouse, do the following:

�Hold down the right mouse button down and drag left or right to scrub through frames.

To play back a Flipbook using the keyboard, do one of the following:

�Press the Spacebar to start or stop playback.

�Hold Shift and press the Spacebar to play in reverse.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

To scrub through a Flipbook frame-by-frame using the keyboard, do one of the following:

�Press the Left or Right Arrow keys to move to the previous or next frame.

�Hold Shift and press the Left or Right Arrow keys to jump back or forward 10 frames.

�Press Command-Left Arrow to jump to the first frame.

�Press Command-Right Arrow to jump to the last frame.

TIP: The mouse and keyboard shortcuts work in full-screen mode as well.