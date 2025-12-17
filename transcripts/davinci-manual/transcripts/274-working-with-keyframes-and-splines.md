---
title: "Working with Keyframes and Splines"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 274
---

# Working with Keyframes and Splines

Once you animate a parameter and display the Spline Editor, you can manipulate the spline’s

keyframes (and thus the animation) in a variety of ways. By selecting Keyframe control points, you can

move, copy, and change the interpolation of your animation.

Adding Keyframes

Once you create one keyframe, additional keyframes are automatically added to a spline whenever

you move the playhead and change the value of that spline’s parameter. For example, if you change

the strength of an animated glow at frame 15, a keyframe with the new value occurs on frame 15.

In the Spline Editor, control points can also be added directly to a spline by clicking on the spline

where you want to add the new keyframe.

Adding Keyframes at the Playhead

If you want to add a new keyframe at the current playhead location, pressing Command-K

on the keyboard or right-clicking in the graph and choosing Set Key adds a keyframe under

the playhead.

Adding Equal Keyframes

If you want to hold a value over several frames, right-clicking in the graph area and choosing

Set Key Equal To displays a submenu to add a new keyframe with a value equal to the next or

the previous keyframe.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

To hold a value between two keyframes choose from the Set Key Equal To submenu

Locked and Unlocked Controls Points

When animating the Center X/Y or Pivot X/Y parameters on any tool, you create a displacement spline

in the Spline Editor. The displacement spline represents the relative offset position of the animated

object along its path. Since the displacement spline is relative, keyframes use a value between

0.0 and 1.0. A displacement value of 0.0 in the Spline Editor indicates that the object is at the very

beginning of a path. A value of 1.0 indicates that the object is positioned at the end of the path.

The displacement spline represents the relative position along a motion path

Displacement paths are composed of locked and unlocked points. Whether a point is locked is

determined by how you added it to the polyline. Locked points on the spline have an associated point

in the viewer’s motion path; unlocked points do not have a corresponding point in the viewer’s motion

path. Each has a distinct behavior, as described below.

TIP: You can convert displacement splines to X and Y coordinates by right-clicking over the

motion path in the viewer and choosing Path#: Polyline > Convert to X/Y Path.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Locked Points

Locked points are the motion path equivalents of keyframes. They are created by moving the

playhead position and changing the parameter value. These points indicate that the animated object

must be in a specified position on a specified frame. Since these keyframes are only related to

position along the path, they can only be moved horizontally along the spline’s time axis.

The locked points appear as larger-sized lock icons in the Spline Editor. Each locked key has an

associated point on the motion path in the viewer.

Deleting a locked point changes the overall timing of the motion.

Unlocked Points

Unlocked points are created by clicking directly on the spline in the Spline Editor. These points

give additional control over the acceleration along the motion path without adjusting the path itself.

Conversely, you can add unlocked points in the viewer to control the shape of the motion path without

changing the timing.

You can change an unlocked point into a locked point, and vice versa, by selecting the point(s),

right‑clicking, and choosing Lock Point from the contextual menu.

For more information on motion paths and locked keyframes, see Chapters 71 and 73 in the

DaVinci Resolve manual or Chapters 8 and 10 in the Fusion Studio manual.

Selecting, Moving, and Deleting Keyframes

The placement of keyframes greatly affects the style of the animation. Using the graph, you can select

keyframes and move them up or down to change their value or move them left and right to change the

timing. Keyframes can be copied and pasted between splines and parameters.

Methods of selecting keyframes:

�Click directly on a keyframe on the spline, or drag a bounding box around the keyframe.

�Drag a bounding box that encompasses multiple keyframes to select more than one.

�To add or remove a keyframe from the current selection, hold down the Command key while

selecting the keyframes. This will remove currently selected keyframes and add currently

unselected keyframes.

�Press Command-A or right-click in the graph area and choose Select Points > Select All from the

contextual menu to select all keyframes from the active splines.

Moving Keyframes

You can freely move keyframes with the mouse, keyboard, or the edit point controls. Keyframes can

even pass over existing points as you move them. For instance, if a keyframe exists on frame 5 and

frame 10, the keyframe at frame 5 can be repositioned to frame 15.

To move keyframes with the mouse:

�Drag the selected keyframe to its new position in the graph. If more than one keyframe is

selected, all selected keyframes will be moved simultaneously.

�Hold down the Option key before dragging the keyframe to constrain its motion to a single axis.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

To move keyframes with the keyboard:

�The Up and Down Arrow keys will adjust the value of the keyframes by a small amount.

�The current scale of the graph determines the degree of vertical movement applied to the value

with each key press. The closer the zoom in the spline, the finer the adjustment.

�Hold down the Shift key while pressing the Up or Down Arrow keys to increase the value

adjustment in larger increments.

To move keyframes using edit fields:

�The Value and Time Editors are found on the far right of the toolbar. These number fields allow

explicit values to be entered for selected keyframes. These controls are explained in more depth

later in this chapter.

To delete one or more keyframes:

�Select one or more keyframes and press the Delete or Backspace key on the keyboard. This only

removes the keyframes; it does not remove the spline, even if there are no keyframes on the

spline. To remove the spline, right-click over the parameter in the Inspector and choose Remove

[parameter name].

Showing Key Markers

You can adjust the position of the keyframes in time, without worrying about manipulating splines, by

using the key markers. The horizontal time axis can show markers that indicate the position of each

keyframe. The display of these markers is enabled by right-clicking in the graph and choosing Show >

Key Markers from the contextual menu, or by clicking on the Show Key Markers button in the toolbar.

The key markers show keyframes in the horizontal axis using the same color as the splines

Copying and Pasting Keyframes

To precisely match animation, Keyframes can be copied to a new location on the same spline or onto

completely different splines and different tools.

There are two options in the graph’s contextual menu for copying keyframes. Choosing Copy Points

(Command-C) copies all selected points. Choosing Copy Value copies a single point identified by the

pointer from multiple selected points. This does not deselect your selection set, and you can pick out

numbers as needed.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

To copy and paste points to a new location on the same spline:


Select the desired keyframes on the spline.


Right-click over the spline and choose Copy Points from the contextual menu or press

Command-C.


Click in an empty area of the graph to deselect all the copied points.


Move the playhead to the area of the spline where you want the points pasted and press

Command-V.

Or, move the pointer over the spline where you want the points pasted, and when the spline

highlights, right-click and choose Paste Points/Value.

Alternatively, you can copy and paste keyframes by dragging them with the mouse. After you

select the points, hold down the Command key and drag the points along the spline to where

you want them pasted.

To copy and paste keyframes from one spline to another:


Make one spline the active visible spline and select the desired keyframes on the spline.


Right-click over the spline and choose Copy Points from the contextual menu or press

Command-C.


Set the spline to viewed or disabled using the status checkbox next to the spline’s name in

the header.


Make the destination spline the active visible spline and select the keyframe on the spline where

the new keyframes should be pasted.


Right-click and choose Paste Points/Value or press Command-V.

You can copy a single point’s value from a group of selected points. Since this process does

not deselect the selected set, you can continue picking out values as needed without having to

reselect points.

To copy and paste a keyframe value:


Make one spline the active visible spline and select all the keyframes on the spline.


Right-click over a single point and choose Copy Value from the contextual menu.


Set the spline to viewed or disabled using the status checkbox next to the spline’s name in

the header.


Make the destination spline the active visible spline and select the keyframe on the spline where

the new keyframe should be pasted.


Right-click and choose Paste Points/Value or press Command-V.

Keyframes can also be pasted with an offset, allowing you to duplicate a spline shape but increase the

values or shift the timing using an offset to X or Y.

To paste keyframes points and values with an X or Y offset:


Make one spline the active visible spline and select the desired keyframes on the spline.


Right-click over the spline and choose Copy Points from the contextual menu or press

Command-C.


Set the spline to viewed or disabled using the status checkbox next to the spline’s name in

the header.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION


Make the destination spline the active visible spline and select the keyframe on the spline where

the new keyframes should be pasted.


Right-click and choose Paste with Offset. In the Offset dialog, enter the Y value, which will be

added to the values of the pasted keyframes.

TIP: You cannot copy and paste between different spline types. For instance, you cannot

copy from a Bézier spline and paste into a B-spline.