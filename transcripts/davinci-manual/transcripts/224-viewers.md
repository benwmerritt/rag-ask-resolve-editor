---
title: "Viewers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 224
---

# Viewers

The viewer area displays either one or two viewers at the top of the Fusion page, and this is

determined via the Viewer button at the far right of the Viewer title bar. Each viewer can show a single

node’s output from anywhere in the node tree. You assign which node is displayed in which viewer.

This makes it easy to load separate nodes into each viewer for comparison. For example, you can

load a Keyer node into the left viewer and the final composite into the right viewer, so you can see the

image you’re adjusting and the final result at the same time.

Dual viewers let you edit an upstream node in one while seeing its effect on the overall composition in the other.

Ordinarily, each viewer shows 2D nodes from your composition as a single image. However, when

you’re viewing a 3D node, you have the option to set that viewer to one of several 3D views.

A perspective view gives you a repositionable stage on which to arrange the elements of the world

you’re creating. Alternatively, a quad view lets you see your composition from four angles, making

it easier to arrange and edit objects and layers within the XYZ axes of the 3D space in which

you’re working.

Loading a 3D node into a viewer switches on a Perspective view


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

TIP: In Perspective view, you can hold down the middle and right mouse buttons, then drag

in the viewer to pivot the view around the center of the world. All other methods of navigating

viewers work the same.

The viewers have a variety of capabilities you can use to compare and evaluate images. This section

provides a short overview of viewer capabilities to get you started.

Zooming and Panning into Viewers

There are standardized methods of zooming into and panning around viewers when you need

a closer look at the situation. These methods also work with the Node Editor, Spline Editor, and

Keyframes Editor.

Methods of panning viewers:

�Middle-click and drag to pan around the viewer.

�Hold down Shift and Command and drag the viewer to pan.

�Drag with two fingers on a track pad to pan.

Methods of scaling viewers:

�Click a viewer, and press the equals key (=) to zoom in, and the minus key (-) to zoom out.

�Press the middle and left mouse buttons simultaneously and drag left or right to resize the viewer.

�Hold down the Command key and use your pointer’s scroll control to zoom in and out of the viewer.

�Hold down the middle mouse button, and then click the left mouse button to zoom in, or click the

right button to zoom out. The scaling uses a fixed amount, centered on the position of the cursor.

�Click a viewer and press Command-1 to resize the image in the viewer to 100 percent.

�Click a viewer and press Command-2 to resize the image in the viewer to 200 percent.

�Click a viewer and press F to reset the image in the viewer to fit the viewer.

�Click the Scale viewer menu and choose Fit or a percentage.

�Right-click on a viewer and choose an option from the Scale submenu of the contextual menu.

This includes a Custom Scale command that lets you type your own scale percentage.

�Hold down the Command key and drag with two fingers on a track pad to zoom in and out

of the viewer.

Methods of spinning 3D viewers:

�In 3D Perspective view, hold down the middle and right mouse button, then drag to

spin the stage around.

�In 3D Perspective view, hold down the Shift key and drag with two fingers on a track pad to

spin the stage around.

Loading Nodes Into Viewers

When you first open the Fusion page in DaVinci Resolve, the output of the current empty composition

(the MediaOut1 node) is usually showing in viewer 2. If you’re in Dual-viewer mode, viewer 1 remains

empty until you assign a node to one of them.

When using Fusion Studio, nothing is loaded into either of the viewers until you assign a node to

one of them.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

To load specific nodes into specific viewers:

�Hover the pointer over a node, and click one of two buttons that appear at the bottom

left of the node.

�Click once to select a node, and press 1 (for the left viewer) or 2 (for the right viewer).

�Right-click a node and choose View On > None/Left View/Right View in the contextual menu.

�Right-click the control header of a node in the Inspector, and choose View On > None/Left View/

Right View from the contextual menu.

�Drag a node and drop it over the viewer you’d like to load it into (this is great for tablet users).

When a node is being viewed, a View Indicator button appears at the bottom left. This is the same

control that appears when you hover the pointer over a node. Not only does this control let you know

which nodes are loaded into which viewer, but they also expose little round buttons for switching

between viewers.

Viewer assignment buttons at the bottom of

nodes indicate when they’re being viewed.

Clearing Viewers

To clear an image from a viewer, click in the viewer to make it active; a thin red highlight is displayed at

the top of the active viewer. With the viewer active, press the ` (accent) key. This key is usually found to

the left of the 1 key on U.S. keyboards. The fastest way to remove all the images from all the viewers is

to make sure none of the viewers is the active panel, and then press the Tilde key.

You can also select the node that is currently showing in the viewer, and press the viewer number

again (1 or 2 respectively) to clear the viewer.

Viewer Controls

A series of buttons and pop-up menus in the viewer’s title bar provides several quick ways of

customizing the viewer display.

Controls in the viewer title bar

�Zoom menu: Lets you zoom in on the image in the viewer to get a closer look, or zoom out to get

more room around the edges of the frame for rotoscoping or positioning different layers. Choose

Fit to automatically fit the overall image to the available dimensions of the viewer.

�Split Wipe button and A/B Buffer menu: You can actually load two nodes into a single viewer

using that viewer’s A/B buffers by choosing a buffer from the menu and loading a node into the

viewer. Turning on the Split Wipe button (press Forward Slash) shows a split wipe between the

two buffers, which can be dragged left or right via the handle of the onscreen control, or rotated

by dragging anywhere on the dividing line on the onscreen control. Alternatively, you can switch

between each full-screen buffer to compare them (or to dismiss a split-screen) by pressing Comma

(A buffer) and Period (B buffer).


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

�SubView type: (These aren’t available in 3D viewers.) Clicking the icon itself enables or disables

the current “SubView” option you’ve selected, while using the menu lets you choose which

SubView is enabled. This menu serves one of two purposes. When displaying ordinary 2D nodes,

it lets you open up SubViews, which are viewer “accessories” within a little pane that can be used

to evaluate images in different ways. These include an Image Navigator (for navigating when

zoomed far into an image), Magnifier, 2D viewer (a mini-view of the image), 3D Histogram scope,

Color Inspector, Histogram scope, Image Info tooltip, Metadata tooltip, Vectorscope, or Waveform

scope. The Swap option (Shift-V) lets you switch what’s displayed in the viewer with what’s being

displayed in the Accessory pane. When displaying 3D nodes, this button lets you have access to

an additional mini 3D viewer.

�Node name: The name of the currently viewed node is displayed at the center of the

viewer’s title bar.

�ROI controls: Clicking the icon itself enables or disables RoI (Region of Interest) limiting in the

viewer, while using the menu lets you choose the region of the RoI. RoI lets you define the region

of the viewer in which pixels actually need to be updated. When a node renders, it intersects

the current RoI with the current Domain of Definition (DoD) to determine what pixels should be

affected. When enabled, you can position a rectangle to restrict rendering to a small region of the

image, which can significantly speed up performance when you’re working on very high resolution

or complex compositions. Auto (the default) sets the region to whatever is visible at the current

zoom/pan level in the viewer. Choosing Set lets you draw a custom region within the frame by

dragging a rectangle that defaults to the size of the viewer, which is resizable by dragging the

corners or sides of the onscreen control. Choosing Lock prevents changes from being made to

the current RoI. Choosing Reset resets the RoI to the whole viewer.

�Color controls: Lets you choose which color and/or image channels to display in the viewer.

Clicking the icon itself toggles between Color (RGB) and Alpha, the two most common things

you want to see (pressing C or A also toggles between Color and Alpha). Opening the menu

displays every possible channel that can be displayed for the currently viewed node, commonly

including RGB, Red, Green, Blue, and Alpha (available from the keyboard by pressing R, G, B, or A).

For certain media and nodes, additional auxiliary channels are available to be viewed, including

Z-depth, Object ID, Material ID, XYZ Normals, and so on.

�Viewer LUT: Clicking the icon itself toggles LUT (LookUp Table) display on or off, while the menu

lets you choose which of the many available color space conversions to apply to the viewer. The

top options let you choose Fusion controls that can be customized via the Edit item at the top of

this menu. The rest of this menu shows all LUTs installed in the LUT directory to use for viewing.

By default, when using DaVinci Resolve, the viewers in the Fusion page show you the image prior

to any grading done in the Color page, since the Fusion page comes before the Color page in

the DaVinci Resolve image processing pipeline. When you’re working on clips that have been

converted to linear color space for compositing, it is desirable to composite and make adjustments

to the image relative to a normalized version of the image that appears close to what the final will

be. Enabling the LUT display lets you do this as a preview, without permanently applying color

adjustments to the image.

�Option menu: This menu contains various settings that pertain to the viewers in Fusion.

Snap to Pixel: When drawing or adjusting a polyline mask or spline, the control points

will snap to pixel locations.

Show Controls: Toggles whatever onscreen controls are visible for the currently selected node.

Region: Provides all the settings for the Region of Interest in the viewer.

Smooth Resize: This option uses a smoother bilinear interpolated resizing method when zooming

into an image in the viewer; otherwise, scaling uses the nearest neighbor method and shows

noticeable aliasing artifacts. However, this is more useful when you zoom in at a pixel level since

there is no interpolation.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Show Square Pixels: Overrides the auto aspect correction when using formats with

non-square pixels.

Checker Underlay: Toggles a checkerboard underlay that makes it easy to see

areas of transparency.

Normalized Color Range: Allows for the visualization of brightness values outside of the normal

viewing range, particularly when working with floating-point images or auxiliary channels.

Gain/Gamma: Exposes a simple pair of Gain and Gamma sliders that let you adjust the

viewer’s brightness.

360 View: Used to properly display spherical imagery in a variety of formats, selectable

from this submenu.

Stereo: Used to properly display stereoscopic imagery in a variety of formats,

selectable from this submenu.

Time Ruler and Transport Controls

The Time Ruler, located beneath the viewer area, is based on the total duration of the composition.

What it represents depends on which version of Fusion you’re using:

•	 For DaVinci Resolve users, the duration displayed in the Time Ruler range depends on

what’s currently selected in the Edit or Cut page timeline.

•	 In Fusion Studio, the Time Ruler depends on the Global Start and End values set in the

Fusion Studio Preferences > Defaults.

The transport controls under the Time Ruler include playback controls, audio monitoring, as well as

number fields for the composition duration and playback range. Additional controls enable motion blur

and proxy settings.

Time Ruler Controls in the Fusion Page

If you’ve selected a single clip in the Edit or Cut page Timeline, then the global range shown in the

Time Ruler is based on the total source duration for that clip. You cannot move the playhead outside

the global range. The yellow lines, called the render range, identify the current In and Out points for

the clip and are the only frames visible in the Fusion page. All frames outside of this range constitute

the unused head and tail handles of that source clip.

The Time Ruler displaying ranges for a clip in the Timeline via yellow marks (the playhead is red)

If you’ve created a Fusion clip or a compound clip, then the “working range” reflects the entire

duration of that clip.

The Time Ruler displaying ranges for a Fusion clip in the Timeline


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Render Range

The render range determines the range of frames that are visible in the Fusion page and that are used

for interactive playback, disk caches, and previews. Frames outside the default render range are not

visible in the Fusion page and are not rendered or played.

You can modify the duration of the render range for preview and playback only. Making the range

shorter or longer does not trim the clip in the Edit or Cut page Timelines.

You can change the render range in the Time Ruler by doing one of the following:

�Hold down the Command key and drag a new range within the Time Ruler.

�Drag either the start or end yellow line to modify the start or end of the range.

�Right-click within the Time Ruler and choose Set Render Range from the contextual menu.

�Enter new ranges in the Range In and Out fields to the left of the transport controls.

�Drag a node from the Node Editor to the Time Ruler to set the range to the duration of that node.

You can return the render range to the In and Out points

of the timeline clip by doing one of the following.

�Right-click within the Time Ruler and choose Auto Render Range.

�Click back in the Edit or Cut page, and then return to the Fusion page.