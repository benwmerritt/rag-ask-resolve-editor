---
title: "The Window Palette Interface"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 572
---

# The Window Palette Interface

Once you’ve created a node with which to apply a Power Window correction, you need to open the

Window palette if it hasn’t been opened already.

To open the Window palette:

Click the Window palette button.

The majority of the Window palette is occupied by the Window list, within which you can create as

many windows as you need for the task at hand. There are five types of windows you can create, each

of which has a different geometry. You can use these windows individually, or you can combine them

to create even more complex shapes and interactions. The Window palette has four groups of controls

that let you use these windows in different ways.

The Window palette with the Window list

�Window list: A row of buttons at the top of this list lets you add new windows, which you can then

customize as necessary. Each window in the list exposes an On/Off button that shows the shape

type, a Layer Name field (blank until you add some text) that you can use to identify what each

window is for, an Invert button, and a Mask button that governs how that window interacts with the

other windows that are currently enabled (adding to other windows by default, or subtracting from

other windows in Mask mode).

�Transform parameters: Controls the overall size, aspect ratio, position, and rotation of the

currently selected window.

�Softness parameters: Controls the edge softness of the currently selected window. Different

window shapes have different softness options.

�Option drop-down menu: The Option drop-down menu has commands for creating and modifying

custom window presets for easy recall later, resetting windows, deleting windows, saving and

managing window presets, and copying and pasting track data.


Color | Chapter 138 Secondary Windows

COLOR

Using buttons along the top of the Window palette, there are five types of windows you can create:

�Linear: A four-point shape that can be edited into any kind of rectangle or trapezoid you might

need. In addition to the center and corner controls, you can also drag any of the four sides to

change the shape.

�Circular: An oval that can be shaped, sized, and feathered to solve an amazing number

of problems.

�Polygonal: A four-point shape that can be expanded with additional control points to create

complex sharp-cornered polygonal shapes.

�Curve: A Bezier drawing tool that you can use to create any kind of shape, curved, polygonal, or

mixed, that you require.

�Gradient: A simple two-handled control for dividing the screen into two halves, with options for

the center, angle, and feathering of the shape. Good for fast sky adjustments.

Managing Windows

To manipulate a window, first you need to create the type of window you want to use, or if you’ve got a

group of windows created already, you need to select the window you want to work on.

Methods of creating and selecting windows:

�To create a new window: Click the Shape icon button or click the Create Window button (at the

top of the Window list) that corresponds to the window you want to create.

�To select a window using the onscreen controls: Click anywhere within a window to select it in

the Viewer.

�To select a window from the Window list: Click the Shape icon button corresponding to the

window you want to select.

To delete a window you no longer want:

�Select a window, then click the Delete button.

To reset a window:

�To reset one window to its default shape: Select a window, then choose Reset Selected Window

from the Option drop-down.

Showing and Hiding Onscreen Window Controls

When you open the Window palette, the Viewer goes into Power Window mode. Enabling a window

makes that window’s onscreen controls appear within the Viewer, and are mirrored to video out so you

can see the window controls on your external display. If you like, you can change how and where the

onscreen controls appear.

To choose whether onscreen controls are mirrored to video out,

or disabled, do one of the following:

Choose an option from the Window Outline submenu in the Viewer’s option menu.

There are three options:

Off: Hides the window outline on both the external display and the Viewer.

On: The default, shows the window outline on both the external display and the Viewer.

Only UI: Hides the window outline on your external display, but leaves it in the Viewer.

Press Option-H to toggle among all three of the above modes.


Color | Chapter 138 Secondary Windows

COLOR

This command is a three-way toggle. The first use of this command hides the window outline on your

external display, but leaves it in the Viewer. The second use of this command hides the window outline

on both the external display and Viewer. The third use of this command shows the window outline on

both the external display and Viewer.

TIP: If you leave the onscreen controls visible in the Viewer, you may find that as you work

you want to temporarily hide or show the onscreen controls in the Viewer so you can get an

uncluttered look at the image you’re adjusting. You can quickly toggle any set of onscreen

controls off and on without selecting Off in the menu by pressing Shift-` (tilde).

Using the High-Visibility Power Window Outline Option

Ordinarily, Power Window outlines are white (for the center shape) and gray (for the softness

shapes). However, sometimes this color scheme can be difficult to see, so the Color panel of the

User Preferences has an option in the General Settings section called “High visibility Power Window

outlines.” Turning this on sets Power Window outlines to be drawn as green (for the center shape) and

yellow (for the softness shapes), to make these windows easier to see in certain circumstances.

(Left) Default window outlines, (Right) High Visibility window

outlines enabled in the Color panel of the User Preferences

Window Transform Controls

Windows have transform parameters that are similar to those found in the Sizing palette.

These parameters let you alter the window, affecting all of its control points together.

Window transform controls


Color | Chapter 138 Secondary Windows

COLOR

Size: Scales the entire window up or down. 50.00 is the default size.

Aspect: Alters the aspect ratio of the window. 50.00 is the default value, larger values make

the window wider, and smaller values make the window taller.

Pan: Repositions the window along the X axis. 50.00 is the default position, larger values

move the window to the right, smaller values move the window to the left.

Tilt: Repositions the window along the Y axis. 50.00 is the default position, larger values move

the window up, smaller values move the window down.

Rotate: The default value is 0. Increasing this parameter rotates the shape clockwise,

decreasing this parameter rotates the shape counterclockwise.

Opacity: Lets you vary the transparency of an individual window’s contribution to a

node’s key.

Convergence: When “Apply stereoscopic convergence to windows and effects” is

enabled in the General Options of the Project Settings, this additional Transform parameter

appears that lets you create properly aligned convergence for a window placed onto a

stereoscopic 3D clip.

For more information about working with Stereoscopic 3D projects, see Chapter 15,

“Stereoscopic Workflows.”

The transform parameters also correspond to onscreen controls found in the Viewer, which can be

manipulated directly using the pointer.

Manipulating the window position on the Viewer

While many of the onscreen controls correspond to parameters within the Window palette, some

onscreen controls, such as the control points that govern reshaping linear, polygonal, and Curve

windows, are only adjustable via the pointer.

Onscreen controls for window transforms:

�To select any window: Click on one of an arrangement of many windows to select it, making that

window’s controls active.

�To reposition any window: Drag anywhere within the window’s onscreen control. Window position

corresponds to the Window palette’s Pan and Tilt parameters. For a gradient window, drag the

center control point.


Color | Chapter 138 Secondary Windows

COLOR

�To resize a circular window while locking its aspect ratio: Drag one of the four blue corner points

out to enlarge, or inwards to shrink. This corresponds to the Window palette’s Size parameter.

�To squish or stretch a circular window, altering its aspect ratio: Drag one of the blue top,

bottom, left, or right control points. These adjustments correspond to the Window palette’s

Aspect parameter.

�To rotate a window: Drag the top inner white rotate handle, in the middle of the window.

For a gradient, drag the bottom arrow handle.

�To alter window softness: Drag any one of the magenta softness handles. Different window

shapes have different sets of handles, which correspond to the Softness parameters.

�To reshape a linear window: Drag any of the white corner handles to corner pin the window,

or drag one of the white top, bottom, or side handles to move an entire side segment of the

window around.

�To reshape a polygonal window: Turning on a polygonal window reveals a simple white rectangle

with four corner control points. Click anywhere on the surface of the rectangle to add additional

control points with which to reshape the polygon, and drag any control point to alter its shape.

Polygonal windows are limited to a maximum of 128 control points.

�To change the size and aspect of a curve: Shift-drag a bounding box around the control

points you want to transform, and then adjust the corners of the box to resize the points while

maintaining the aspect ratio of the shape, or adjust the top, bottom, left, or right points to squish or

stretch the shape.

�To remove control points from polygonal or Curve windows: Middle-click the control point you

want to remove.

NOTE: Removing a control point from a polygonal window that’s already been animated

using the Keyframe Editor results in that point abruptly popping on and off at the keyframes

creating the animation.

Window Softness

Each type of window has different Softness parameters, depending on how adjustable that window is.

�Circular: A single parameter, Soft 1, lets you adjust the uniform softness of the oval’s edge.

�Linear: Four parameters, Soft 1–4, let you adjust the softness of each of the four sides of the linear

window independently. Magenta softness control points on the top, bottom, left, and right let you

adjust the softness of each side of the linear shape independently.

�Polygon: Two parameters, Inside Softness and Outside Softness, let you adjust the overall

softness of a polygonal window. There are no onscreen softness control points.

�Curve: Two parameters, Inside Softness and Outside Softness, let you adjust the overall softness

of a curve. Using the onscreen controls, you can adjust the magenta inside and outside softness

control points independently, creating any softness shape you need.

�Gradient: A single parameter, Soft 1, lets you adjust the uniform softness of the

gradient window’s edge.


Color | Chapter 138 Secondary Windows

COLOR