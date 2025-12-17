---
title: "Creating and Editing Polylines In‑Depth"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 309
---

# Creating and Editing Polylines In‑Depth

This section covers the Polygon node’s capabilities in depth.

The Polyline Toolbar

Whenever a node that contains one or more polylines is selected, the polyline is shown on all viewers

and the Polyline toolbar is displayed along the side of each viewer. The toolbar contains several

buttons that make switching polyline modes and options easy to access.

The Polyline toolbar

If you hover the pointer over any of the Polyline toolbar buttons, a tooltip that describes the button’s

function appears. Clicking on a button will affect the currently active polyline or the selected polyline

points, depending on the button.

You can change the size of the toolbar icons, add labels to the buttons, or make other adjustments

to the toolbar’s appearance in order to make polylines easier to use. All the options can by found by

right-clicking on the toolbar and selecting from the options displayed in the contextual menu.

Selecting a Specific Polyline

It is possible to have several polylines in the viewer at once if you select multiple Mask nodes in the

Node Editor, so it’s important to be able to switch between polylines easily.

To make a polyline active, do one of the following:

�Click one of the polyline’s control points or segments.

�Press Tab and Shift-Tab to cycle between available polylines.

�Right-click in the viewer and choose the desired polyline by name from the Controls > Select menu.

Polyline Creation Modes

There are several different modes available from the toolbar for creating and modifying polylines.

The specific mode used when a polyline is first added will depend on whether it is used as a path

or a mask.

Each of the modes is described in more detail below.

Click Append

This mode is the default mode for mask creation. It’s used to quickly define the rough shape of the

mask, after which you switch to Insert and Modify mode to refine the mask further.

The Click Append toolbar button (Shift-C)


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

To create a mask using the Click Append mode, do the following:


Select Click Append from the toolbar or press Shift-C.


Click the pointer where you want to start the shape.


Move and click the pointer to append a point to the last one.


To close the shape, place the mouse pointer over the first point created and click when the pointer

changes shape.

When a shape is closed, the polyline is automatically switched to Insert and Modify mode.

Although the Click Append mode is rarely used with paths, it can be helpful when you know the

overall shape of a motion path, but you don’t yet know the timing.

TIP: Holding Shift while you draw a mask constrains subsequent points to 45-degree angles

relative to the previous point. This can be very helpful when drawing regular geometry.

Insert and Modify

Masks, which are created in Click Append mode, automatically switch to Insert and Modify mode when

the mask shape is closed. You can also manually switch to this mode by clicking the Insert and Modify

button in the toolbar or using the Shift-I keyboard shortcut. This mode makes it easier to add additional

points and refine the shape of the mask. Dragging the control points or direction handles modifies

existing points on the polyline.

The Insert Modify toolbar button (Shift-I)

Insert and Modify mode is also the default mode for creating motion paths. A new control point is

automatically added to the end of the polyline, extending or refining the path, any time a parameter

that is animated with a motion path is moved.

Draw Append

The Draw Append mode creates a freehand polyline shape directly on the viewer, like drawing with

a pencil or a paintbrush. This mode is ideal to use in conjunction with a tablet and for the creation of

garbage mattes and effect masks around complex shapes.

The Draw Append toolbar button (Shift-D)


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

Protection Modes

In addition to the modes used to create a polyline, two other modes are used to protect the points

from further changes after they have been created.

Modify Only

Modify Only mode allows existing points on the polyline to be modified, but new points may not be

added to the shape.

The Modify Only toolbar button (Shift-M)

TIP: Even with Modify Only selected, it is still possible to delete points from a polyline.

Done

The Done mode prohibits the creation of any new points, as well as further modification of any existing

points on the polyline.

The Done toolbar button (Shift-N)

Closing Polylines

There are several ways to close a polyline, which will connect the last point to the first.

To close a polyline, do one of the following:

�Hover the pointer over the first point created, and then click on the point.

�Press Shift-O on the keyboard.

�Click the Close button on the polyline toolbar.

�Draw a polyline until you are ready to close the shape, and then right-click and choose

Polygon:Polyline > Closed.

The Close toolbar button (Shift-O)

All these options are toggles that can also be used to open a closed polygon.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

Selecting and Adjusting Polylines

To create the shape you need for a mask or a motion path, you need to know how to manipulate the

splines. Fusion provides a number of simple techniques for selecting, moving, and smoothing a spline,

but also includes more complex adjustment techniques for scale, skewing, and twisting a spline.

Polyline Points Selection

To select one or more control points on a polyline, do one of the following:

�Click directly on the control points.

�Lasso around the points.

To add or remove points from the current selection, do one of the following:

�Hold the Shift key to select a continuous range of points.

�Hold Command and click each control point you want to add or remove.

�Press Command-A to select all the points on the active polyline.

TIP: Once a control point is selected, you can press Page Down or Page Up on the keyboard

to select the next control point in a clockwise or counterclockwise rotation. This can be very

helpful when control points are very close to each other.

Moving Polyline Points

The selected polyline points can be moved using either the keyboard or the mouse.

To move selected control points using the pointer, do one of the following:

�Drag on the selected points anywhere in the viewer.

�Hold Shift while dragging to restrict movement to a single axis.

�Hold Option and drag anywhere in the viewer to move the selected control point.

To move selected control points using the keyboard, do one of the following:

�Press the Up or Down Arrow keys on the keyboard to nudge a point up or down in the viewer.

�Hold Command-Up or Down Arrow keys to move in smaller increments.

�Hold Shift-Up or Down Arrow keys to move in larger increments.

Smoothing a Polyline Segment

If you want to shape the polyline and control its slope, you can choose to smooth a spline segment by

adjusting the Bézier direction handles.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

To smooth the selected points on an active polyline, do one of the following:

�Press Shift-S.

�Click the Smooth button on the Polyline toolbar.

�Choose Smooth from the polyline’s contextual menu.

The Smooth button in the toolbar (Shift-S)

Linearizing a Polyline Segment

To make certain that a polyline segment is perfectly straight, that segment must be linearized. A linear

segment aligns the Bézier direction handles with the segment and therefore has no curvatures. The

segment is always drawn in a straight line between two points on the polyline.

To linearize the selected points on an active polyline, do one of the following:

�Press Shift-L.

�Click the Linear button on the polyline’s toolbar.

�Choose Linear from the polyline’s contextual menu.

The Linear button in the toolbar (Shift-L)

Transforming Individual or Multiple Points

Select the points to be transformed, and then do one of the following:

�Hold T and drag to twist.

�Hold S and drag to scale.

�Hold X and drag to scale horizontally only.

�Hold Y and drag to scale vertically only.

�Hold O and drag to offset the points perpendicular to the tangent.

The position of the pointer when the transformation begins becomes the center used for the

transformation.

Deleting Selected Points

You can delete a selected point or group of points by pressing Delete or Backspace, choosing Delete

from the contextual menu, or by clicking the Delete Point button in the toolbar. The shape of the

polyline changes to reflect the removal of these points.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

TIP: Deleting all the points in a polyline does not delete the polyline itself. To delete a

polyline, you must delete the node or modifier that created the polyline.