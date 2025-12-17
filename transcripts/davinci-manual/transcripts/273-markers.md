---
title: "Markers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 273
---

# Markers

Markers help identify important frames in a project. They may indicate a frame where a ray gun shoots

a beam in the scene, the moment that someone passes through a portal in the image, or any other

important event in the composite.

Markers added to the Timeline in the Cut, Edit, Fairlight, or Color page will appear in the Keyframes

Editor and Spline Editor of the Fusion page. They can also be added from the Keyframes Editor or the

Spline Editor while working in Fusion Studio or the Fusion page. Markers appear along the top of the

horizontal axis Spline Editor’s Time Ruler. They are displayed as small blue shapes, and when selected,

a line extends from each guide down vertically through the graph.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

NOTE: Markers attached to clips in the Cut, Edit, Color, or Fairlight pages Timeline are not

visible in Fusion’s Spline Editor.

Unselected markers appear as blue shapes along the top, while selected

markers display a vertical line running through the graph

Working with Markers

Markers call attention to a particular frame within a comp. They can be named, displayed in a list, and

edited. After you add markers, you can easily jump the playhead between them, change their position,

or delete them altogether.

Markers can be added by right-clicking

in the horizontal time axis

To create a marker:

�Right-click in the horizontal axis Time Ruler and choose Add Marker.

To delete a marker, do one of the following:

�Drag the marker up outside the Spline Editor panel.

�Right-click on the marker and then choose Delete Marker from the menu.

�Select the marker and then press Delete or Backspace on the keyboard.

�From the Marker List, select a guide in the list and click the Del button.

To move a marker to a new frame, do one of the following:

�Drag the marker handle along the time axis.

�Right-click in the marker area and choose Options > Enable Marker Grab, and then drag the

marker’s vertical line to move the guide.

To move the Playhead to a marker:

�Right-click on a marker and choose Set Current Time To [Frame number].


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Using the Marker List

The Marker List is a list of all markers in the current comp. It can display the markers from either the

Keyframes Editor, the Spline Editor, or both panels simultaneously. Clicking on the frame number or

name of a guide causes the current time to change to that marker’s frame. Since the Marker List is a

floating window, it can remain open, allowing you to quickly jump to different markers while you work

in the Spline Editor.

To show the Marker List:

�Right-click in the horizontal axis and choose Show Marker List, or press Shift-G.

The Marker List above shows markers in the current comp.

If markers currently exist in the comp, they are automatically displayed in the Marker List, regardless

of whether they were added in the Keyframes Editor or the Spline Editor or any other page in DaVinci

Resolve. You can also add markers directly from the Marker List, which can be helpful if you have

multiple markers you need to add, and you know the rough timing.

To add a guide from the Marker List:


Click the Add button in the Marker List window.


Enter a frame number in the Time field.


Press Tab or click the Close button to close the Marker List.

To name a marker, do one of the following:

�In the Marker List, double-click in the Name column, to the right of the frame number, and enter a

name for the marker.

�Right-click over a marker in the horizontal axis and choose Rename Marker. In the dialog that

opens, enter a name for the marker.

Displaying Marker with the Timeline

The Marker List window includes checkboxes next to each marker that determines whether a marker

displays in the Spline Editor, the Keyframes Editor, both, or neither. By default, when you create

markers, they are active in both panels. To hide a marker from appearing in either panel, deselect the

appropriate checkbox.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Autosnap

To assist in precisely positioning keyframe control points along the horizontal (time) axis, you can

enable the Spline Editor’s Autosnap function. Right-clicking over a spline and choosing Options >

Autosnap Points provides a submenu with four options.

None: Allows free, sub-frame positioning of the keyframes.

Frame: Keyframes snap to the nearest frame.

Fields: Keyframes snap to the nearest field.

Markers: Keyframes snap to the nearest marker.

Autosnapping and Markers

By default, a newly-created marker snaps to the closest frame. Moving markers with the mouse also

snaps them to the current frame. You can change this behavior by selecting Options > Autosnap

Markers > None or by selecting Options > Autosnap Markers > Field from the contextual menu.

Creating Animation Splines

Animation splines are created automatically when you keyframe a parameter in the Inspector or the

Keyframes Editor. However, you can create an animation spline without first having to add a keyframe.

To create a spline:

�Right-click on the parameter to be animated in the Inspector, and choose Animate from the

contextual menu.

Choosing Animation from the menu

displays a spline in the Spline Editor

Selecting Animate from the contextual menu connects the parameter to the default spline

type. This is usually a Bézier Spline unless you change the default spline in the Defaults panel

of the Fusion Preferences.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Deleting Animation Splines

To remove an animation spline from a parameter, right-click on the control in the Inspector and select

Remove [tool parameter’s name] from the contextual menu. Removing a spline from a parameter only

deletes the spline if no other tool in the composition is connected to the same spline at that time.

Removing a spline from a parameter removes the animation

Animating with Different Spline Types

A Bézier spline is the default spline unless changed in the Preferences. However, if you want to use a

spline type other than Bézier for the animation curve, you can choose the spline type from the Modify

With contextual submenu before creating any keyframes.

Three spline types in the Modify With menu

�Bézier Spline: Bézier splines are the default curve type. Three points for each keyframe on the

spline determine the smoothness of the curve. The first point is the actual keyframe, representing

the value at a given time. The other two points represent handles that determine how smoothly


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

the curve for the segments leading in and out of the keyframe are drawn. Bézier is the most used

spline type because Bézier splines allow you to create combinations of curves and straight lines.

Bézier spline

�Modify with > B-Spline: B-splines use a single point to determine the smoothness of the curve.

Instead of using handles, a single control point determines the value as well as the smoothness

of the curve. Holding down the W key while dragging left or right on the control point adjusts the

tension of the curve.

B-spline

�Modify with > Cubic Spline: Cubic splines are similar to Bézier splines, in that the spline

passes through the control point. However, Cubic splines do not display handles and always

make the smoothest possible curve. In this way, they are similar to B-splines. This spline type

is almost never used.

Cubic spline


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

�Modify with > Natural Cubic Spline: Natural Cubic splines are similar to Cubic splines, except that

they change in a more localized area. Changing one control point does not affect other tangents

beyond the next or previous control points.

Natural Cubic spline