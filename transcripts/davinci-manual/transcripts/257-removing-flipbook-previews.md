---
title: "Removing Flipbook Previews"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 257
---

# Removing Flipbook Previews

Once you create a Flipbook Preview, you need to know how to clear it from RAM.

To eliminate a Flipbook you’ve created:

�Right-click within a viewer containing a Flipbook Preview, and choose Remove Preview.

Flipbook Preview Render Settings

This section covers all the settings available for rendering Flipbook Previews to RAM.

Settings

The Settings section of the Preview Render dialog includes three buttons that determine the overall

quality and appearance of your Flipbook Preview. These buttons also have a significant impact on

render times.

HiQ: When enabled, this setting renders the preview in full image quality. If you need to see

what the final output of a node would look like, then you would enable the HiQ setting. If you are

producing a rough preview to test animation, you can save yourself time by disabling this setting.

MB: The MB in this setting stands for Motion Blur. When enabled, this setting renders with motion

blur applied if any node is set to produce motion blur. If you are generating a rough preview and

you aren’t concerned with the motion blur for animated elements, then you can save yourself time

by disabling this setting.

Some: When Some is enabled, only the nodes specifically needed to produce the image of the

node you’re previewing are rendered.

Size

Since RAM Flipbook Previews use RAM, it’s helpful to know how many frames you can render into

RAM before you run out of memory. The Flipbook Preview dialog calculates the currently available

memory and displays how many frames will fit into RAM. If you have a small amount of RAM in your

computer and you cannot render the entire range of frames you want, you can choose to lower the

resolution to a setting that delivers the best quality/duration ratio for your preview.

Network

Network rendering is only available in Fusion Studio.

For more information on network rendering, see Chapter 66, “Rendering Using Saver Nodes,”

in the DaVinci Resolve Reference Manual or Chapter 4 in the Fusion Reference Manual.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Shoot On

Sometimes you may not want to render every single frame, but instead every second, third, or fourth

frame to save render time and get faster feedback. You can use the Step parameter to determine the

interval at which frames are rendered.

Frame Range

This field defaults to the current Render Range In/Out set in the Time Ruler to determine the start and

end frames for rendering. You can modify the range to render more or fewer frames.

Configurations

Once you’ve created a useful preview configuration, you can save it for later use by clicking the

Add button, giving it a name, and clicking OK.

Updating a Preview

This option is designed for the interactive frame-by-frame work of rotoscoping and painting. Right-click

over a preview in the viewer and choose Update from its contextual menu. When active, any frames

that are modified on the previewed node are automatically updated in the preview’s playback. This

lets you reserve the RAM for playback. You can keep it playing on a loop or ping-pong while you work

in another viewer.

Onscreen Controls

When it comes to adjusting images, the Control Panel provides very precise numerical values, but

sometimes visually positioning an element using onscreen controls can get you where you want to go

with less tweaking.

The Angle preview control

The viewers show onscreen controls for manipulating the parameters of the currently selected node.

Common onscreen controls include crosshairs, angle indicators, polylines, and paint strokes. Each of

these controls can be manipulated directly in the viewer using the mouse or keyboard.

The controls shown in viewers are determined by which nodes are selected, not by the node

displayed in the viewer. For example, a downstream blur is easily viewed while manipulating the

controls for a selected polygon mask or merge. If multiple nodes are selected, the controls for every

selected node are shown simultaneously.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Showing and Hiding Onscreen Controls

The onscreen controls for a viewer can be hidden so they don’t interfere with viewing the image.

To toggle the visibility of onscreen controls, do one of the following:

�Click a viewer’s Option menu and choose Show Controls to toggle the controls on or off.

�Right-click in a viewer and choose Options > Show Controls from the contextual menu.

�Select a viewer and press Command-K.

Enabling/Disabling Onscreen Controls in Specific Nodes

Some nodes, like masks, allow disabling of their onscreen controls on a per-node basis, since you

often use multiple Polygon nodes to organize and animate masks.

You can disable some nodes, like the

Polygon node, on a per-node basis.

Making Fine Adjustments to Onscreen Controls

If you want the visual guidance of onscreen controls with the precision of the Inspector, you can use

different keyboard modifiers.

�Up and Down Arrow keys can be used to adjust the vertical position of an onscreen

control by small steps.

�Holding down the Command key while using the Up and Down Arrow keys reduces the scale of

each step by a factor of ten. Holding Shift increases the scale of each step by a factor of ten.

Toolbars

There are two toolbars in the viewer: a viewer toolbar, which always appears at the top of each

viewer and gives you control over what that viewer shows, and an optional node toolbar that appears

underneath that gives you contextual controls based on the node you’ve selected in the Node Editor.

Viewer Toolbar

A viewer toolbar runs across the top of each viewer, providing access to many of the most commonly

used viewer-related settings, as well as an indication of the status of many of the most important

settings. Most of the menus and buttons found on this toolbar are described in detail throughout

this chapter.

The viewer toolbar


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Node Toolbars

In addition to the viewer toolbar, a node toolbar is displayed underneath, at the top of the viewer

display area, whenever you select a node that exposes special nodes. Examples of nodes that expose

a toolbar include the text, masks, paths, paint strokes, and the 3D environment.

The node toolbar shown for the Paint node

Customizing the Node Toolbar

If you want to change the size of the buttons that appear in the Node toolbar, or turn on text names

for each node, you can right-click anywhere in the empty area of the toolbar and choose new settings

from the Icon Size and Button Style submenus in the contextual menu.

The contextual menu for the node toolbar

A/B Buffers

Each viewer has two buffers, each of which can contain images from different nodes, enabling easy

comparison of two different nodes within the same viewer by either toggling between buffers, or

via an adjustable split-wipe. Each buffer can be considered a complete and separate viewer within

the same viewer pane. The A buffer is always shown by default, so when you first load a node into a

viewer, the image loads into the A buffer.

Flipping between Buffers

Switching between buffers is easy, either to view a different image while keeping another image

handy, or to flip between the original image and the affected image for comparison.

To switch between buffers, do one of the following:

�Select a viewer and press comma (,) to select the A buffer or press period (.) to select the B buffer.

�Click the Buffer menu and choose either Switch to A View or Switch to B View.

The Buffer menu lets you switch between buffers


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

TIP: Each buffer can be set to different display settings—for example, showing different

channels or different viewing LUTs, either applied to different nodes or applied to two

buffered versions of the same node.

Split Wipes between Buffers

You can also wipe between both buffers, providing a more direct means of comparison.

To wipe between buffers, do one of the following:


Prepare to wipe between two images by loading different nodes into each buffer, or load the same

node with different viewer options into each buffer.


To toggle the split wipe on or off, do one of the following:

a)	 Click the Switch to Split Wipe View button.

b)	 Press Forward Slash (/).


To adjust the wipe, do one of the following:

a)	 Move the center of the wipe by dragging the center handle of the wipe divider.

b)	 Press Command-Option and click anywhere in the viewer to jump the wipe divider to

that location.

c)	 Change the angle or the wipe by dragging the wipe divider. Dragging the wipe divider while

holding the Shift key snaps it to the nearest 45-degree angle.

d)	 Panning or zooming the viewer pans and zooms both buffers together.


(Optional) If you want to change the image that’s displayed on that side of the split, you can drag

new nodes onto either half of the viewer.


To turn off the wipe, click the Switch to Split Wipe View button again (or press /).

The wipe divider can be adjusted for comparing different areas of the A and B images


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Even when you wipe, you can choose different display channels, view LUTs, or other display options

for each buffer individually by clicking on the half of the wipe you want to alter, and then choosing the

options you want that buffer to use. This allows easy comparison of different channels, LUTs, or other

viewer settings while wiping the same image, or different images.