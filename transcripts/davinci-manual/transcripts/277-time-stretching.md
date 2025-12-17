---
title: "Time Stretching"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 277
---

# Time Stretching

Time Stretching allows for a selected group of keyframes to be proportionally stretched or squashed.

This allows you to change the duration of the animation while keeping the relative distance between

each keyframe. To enable spline stretching, select the group of keyframes that you want to time

stretch, and then choose Modes > Time Stretching from the graph’s contextual menu or click the Time

Stretch button in the toolbar.

The Time Stretch button in the toolbar


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

When you have more than one keyframe selected on the spline, enabling Time Stretch surrounds the

outer keyframes with two vertical white bars. Drag on the white vertical bars to stretch or shrink the

timing of the spline segments within the bars. Drag these bars back and forth to stretch or squash the

spline segment.

The Time Stretch bars in the graph

TIP: If no keyframes are selected when you enable Time Stretch, drag a rectangle to set the

boundaries of the Time Stretch.

To disable the Time Stretching mode:

�Click on the Time Stretch button in the toolbar again or reselect Modes > Time Stretching from the

contextual menu.

Shape Box

The Shape Box transform mode is similar to Time Stretching; however, it can adjust the vertical scaling

of keyframe values as well as time.

To enable the Shape Box, do one of the following:

�Select a group of keyframes, and then choose Modes > Shape Box from the contextual menu.

�Select a group of keyframes, and then click the Shape Box button in the toolbar.

�Select a group of keyframes, and then press Shift-B to enable or disable the Shape Box mode.

The Shape Box button in the toolbar


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

A white rectangle outlines the selected points when the mode is enabled. To scale, skew, or stretch

the spline, drag on any of the control points located around the box. To move all the keyframes, drag

on the box edges.

The Shape Box in the graph

TIP: If no points are selected, or if you want to select a new group of keyframes, you can

drag out a new rectangle at any time.

Ease In/Out

For a more precise way to adjust the length of Bézier direction handles attached to selected

keyframes, you can use the Spline Ease dialog. To show the dialog, select a keyframe in the graph,

and then choose Edit > Ease In/Out from the graph’s contextual menu or press T on the keyboard.

The Ease In/Out controls appear above the graph area. You can drag over the number fields to adjust

the length of the direction handles or enter a value in the fields.

The Ease In/Out controls above the graph area

Clicking the Lock In/Out button will collapse the two sliders into one, so any adjustments apply to both

direction handles.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Importing and Exporting Splines

Spline shapes can be imported and exported from or to an ASCII text file. This makes it easier to

save complex spline curves for later reuse, or to transfer tracking, path, and animation data from one

application to another. Exported splines are assigned the file extension .spl for easy identification.

To export a spline:


Select the active spline in the Spline Editor.


Right-click on the spline in the graph area to display the contextual menu and select Export.


Choose from three format options in the submenu.


Enter a name and location in the file browser dialog, and then click Save.

Exporting a spline gives you three options. You can export the Samples, Key Points, or All Points.

Samples adds a control point at every frame to create an accurate representation of the spline.

Key Points replicates the control point positions and values on the spline using linear interpolation.

All Points exports the spline as you see it in the Spline Editor, using the same position, value, and

interpolation.

To import a spline:


Add an animation spline for the parameter.


In the Spline Editor, right-click on the animation spline and select Import Spline from the

contextual menu.


In the File Browser dialog, select the spline curve .spl file, and then click Open.

Importing a new curve will replace any existing animation on the selected spline.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Chapter 73

Animating with

Motion Paths

Layers and 3D objects can move along a designated spline shape to create motion

path animations. This chapter discusses how you can create, edit, and use motion

paths in Fusion.

Contents

Animating Using Motion Paths��������������������������������������������������������������������������������������������������������������������������������������������������� 1509

Types of Motion Paths����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1510

Polyline Path������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1510

Path Modifier������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1514

Controlling Speed and Orientation along a Path������������������������������������������������������������������������������������������������������������������ 1514

XY Path������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1517

Types of Control Points�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1519

Locked Points���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1519

Unlocked Points����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1522

Locking and Unlocking Points������������������������������������������������������������������������������������������������������������������������������������������������������ 1523

Tips for Manipulating Motion Paths������������������������������������������������������������������������������������������������������������������������������������������ 1523

Compound Motion Paths Using Path Centers���������������������������������������������������������������������������������������������������������������������� 1523

Copying and Pasting Motion Paths�������������������������������������������������������������������������������������������������������������������������������������������� 1524

Removing Motion Paths������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1524

Recording Motion Paths������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1525

Importing and Exporting Polylines�������������������������������������������������������������������������������������������������������������������������������������������� 1525

Native Format��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1525


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION