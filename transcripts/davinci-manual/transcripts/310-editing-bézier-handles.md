---
title: "Editing Bézier Handles"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 310
---

# Editing Bézier Handles

For Bézier polylines, each control point has two direction handles that adjust the slope of a curve

through the control point. These direction handles appear only when the point is selected.

Dragging a direction handle makes adjustments to the curve of the segment that emerges from the

control point. The direction handle on the opposing side of the control point will also move to maintain

the relationship between these two handles.

To break the relationship between direction handles and adjust one independently, hold Command

while dragging a handle. Subsequent changes will maintain the relationship, unless Command is held

during each adjustment.

Hold Command to adjust one handle independently

If you want to adjust the length of a handle without changing the angle, hold Shift while moving a

direction handle.

Point Editor

The Point Editor dialog can be used to reposition control points using precise X and Y coordinates.

Pressing the E key on the keyboard will bring up the Point Editor dialog and allow you to reposition

one or more selected control points.

The Point Editor dialog can be used to position control points

The dialog box contains the X- and Y-axis values for that point. Entering new values in those boxes

repositions the control point. When multiple control points are selected, all the points move to the

same position. This is useful for aligning control points along the X- or Y-axis.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

If more than one point is selected, a pair of radio buttons at the top of the dialog box determines

whether adjustments are made to all selected points or to just one. If the Individual option is selected,

the affected point is displayed in the viewer with a larger box. If the selected point is incorrect, you can

use the Next and Previous buttons that appear at the bottom of the dialog to change the selection.

In addition to absolute values for the X- and Y-axis, you can adjust points using relative values from

their current position. Clicking once on the label for the axis will change the value to an offset value.

The label will change from X to X-offset or from Y to Y-offset.

The Point Editor dialog with Offset values

If you are not sure of the exact value, you can also perform mathematical equations in the dialog box.

For example, typing 1.0-5 will move the point to 0.5 along the given axis.

Reduce Points

When freehand drawing a polyline or an editable paint stroke, the spline is often created using more

control points than you need to efficiently make the shape. If you choose Reduce Points from the

polyline’s contextual menu or toolbar, a dialog box will open allowing you to decrease the number of

points used to create the polyline.

The Reduce Points button in the toolbar

The overall shape will be maintained while eliminating redundant control points from the path. When

the value is 100, no points are removed from the spline. As you drag the slider to the left, you reduce

the number of points in the path.

Shape Box

If you have a polyline shape or a group of control points you want to scale, stretch, squish, skew, or

move, you can use the shape box to easily perform these operations.

To enable the shape box, do one of the following:

�Click the Shape Box toolbar button.

�Choose Shape Box from the contextual menu.

�Press Shift-B.

The Shape Box button in the Polyline toolbar


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

If there are selected points on the polyline when the Shape Box mode is enabled, the shape box is

drawn around those points. Otherwise, you can drag the shape box around the area of control points

you want to include.

If you want to freely resize the shape box horizontally and vertically, you can drag a corner handle.

Dragging a handle on the side of the shape box resizes the polyline along a specific axis.

Dragging a side handle resizes along a specific axis

Holding Command while dragging a shape box handle will apply adjustments from the center

of the shape box, constraining the transformation to the existing proportions of the shape box.

Holding Shift while dragging a corner handle affects only that handle, allowing skewed and non-

uniform transformations.

Hold Shift while dragging a corner to perform non-uniform transformations

Showing and Hiding Onscreen Polyline Controls

It is often difficult to identify individual points when they are placed closely together. You can choose

to display both points and their direction handles, just points, or just handles. These display mode

options are selected using the Show Key Points and Show Handles toolbar buttons, or from the

polyline’s context menu.

The Show Key Points and Show

Handles buttons in the toolbar


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

You use these options to simplify the screen display when adjusting control points placed closely

together and to avoid accidentally modifying controls and handles that are adjacent to the

intended target.

Stop Rendering

While points along the polyline are being moved, the results are rendered to the viewer to provide

constant interactive feedback. Although extremely useful, there are situations where this can be

distracting and can slow down performance on a complex effect. To disable this behavior so renders

happen only when the points stop moving, you can toggle the Stop Rendering button in the toolbar or

select this option from the polyline contextual menu.

Roto Assist

You can enable the Roto Assist button in the toolbar when you begin drawing your shape to have

points snap to the closest high-contrast edge as you draw the shape. The points that have snapped to

an edge are indicated by a cyan outline.

There are three main Roto Assist options.

�Multiple Points: Allows adding multiple points along an entire edge with a single click instead of

having to add each point individually.

�Distance: Defines the pixel range within which searching for an edge will take place.

�Reset: Used for resetting the snap attribute of the snapped points. After resetting, the points will

become unavailable for tracking.

The Roto Assist options in the toolbar

Creating Softness Using Double Polylines

The standard soft edge control available in all Mask nodes softens the entire mask equally. However,

there are times, particularly with a lot of motion blur, when softening part of the curve while keeping

other portions of the curve sharp is required.

This form of softness is called non-uniform softness, which is accomplished by converting

the shape from a single polyline to a double polyline. The double polyline is composed of

two shapes: an inner and an outer shape. The inner shape is the original shape from the

single polyline, whereas the outer shape is used to determine the spread of the softness.

The further the outer shape gets from the inner shape, the softer that segment of the

shape becomes.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

A double polyline uses an inner and outer shape for non-uniform softness

Converting a Single Polyline to a Double Polyline

To convert a mask into a double polyline, click the Double Polyline button in the Polyline toolbar or

right-click in the viewer and select Make Outer Polyline from the mask’s contextual menu.

The shape will be converted into an inner and an outer polyline spline. Both polylines start with exactly

the same shape as the original single polyline. This keeps the mask sharp to start with and allows any

animation that may have already been applied to the shape to remain.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

Make Double Polyline button

The control points on the outer shape are automatically parented to their matching points on the

inner shape. This means that any changes made to the inner shape will also be made to the outer

shape. The relationship is one-way; adjustments to the outer shape can be made without affecting the

inner shape.

A dashed line drawn between the points indicates the relationship between the points on the inner

and outer shapes.