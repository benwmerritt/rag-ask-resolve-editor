---
title: "Adding Points"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 481
---

# Adding Points

Adding Points to a polygonal shape is relatively simple. Immediately after adding the node to the

Node Editor, there are no points, but the tool will be in Click Append mode. Click once in the viewer

wherever a point is required for the shape. Continue clicking to draw the shape. When the shape is

complete, click on the initial point again to close the shape.

When the shape is closed, the mode of the polyline will change to Insert and Modify. This allows for

the adjusting and adding of additional points to the shape by clicking on segments of the polyline. To

lock down the shape and prevent accidental changes, switch the Polyline mode to Done using the

Polyline toolbar or contextual menu.

The sPolygon toolbar

When a Polygon (or B-Spline) shape is added to a node, a toolbar appears above the viewer, offering

easy access to modes. Hold the pointer over any button in the toolbar to display a tooltip that

describes that button’s function.

�Click: Click is the default option when creating a polyline (or B-Spline) shape. It is a Bézier style

drawing tool. Clicking sets a control point and appends the next control point when you click again

in a different location.

�Draw: Draw is a freehand drawing tool. It creates a shape similar to drawing with a pencil on

paper. You can create a new shape using the Draw tool, or you can extend an existing open spline

by clicking the Draw tool and starting to draw from the last control point.

�Insert and Modify: Insert adds a new control point along the spline and lets you modify it.

�Modify Only: Modify allows you to safely move or smooth any exiting point along a spline without

worrying about adding new points accidentally.

�Done: Prevents any point along the spline from being moved or modified. Also, new points cannot

be added. You can, however, move and rotate the entire spline.

�Close: Closes an open spline.

�Smooth: Changes the selected control point from a linear to a smooth curve.

�Linear: Changes the selected control point from a smooth curve to linear.

�Select All: Selects all the control points on the spline.

�Show Key Points: Shows or hides the control points along the spline.

�Show All Handles: Shows or hides the Bézier handles along the polyline.

�Shape Box: Places a reshape rectangle around the selected spline shape. Using the reshape

rectangle, you can deform groups of control points or entire shapes much easier than modifying

each point.

�Delete Points: Deletes the selected control point(s).

�Reduce Points: Opens a Freehand precision window that can be used to reduce the number of

controls points on a spline. This can make the paint stroke easier to modify, especially if it has

been created using the Draw tool.

Change the way the toolbar is displayed by right-clicking on the toolbar and selecting from the options

displayed in the toolbar’s contextual menu.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

sRectangle

The sRectangle node

The sRectangle node is used to create rectangular shapes. Like almost all shape nodes, you can only

view the sRectangle node’s results through a sRender node.

External Inputs

This node generates shapes and does not have any inputs.

Basic Node Setup

The sRectangle node is a shape generator, meaning it generates a shape and therefore has no inputs.

The output of the sRectangle can go into a sRender for viewing and further compositing or, more likely,

connect to another Shape node like sGrid or sDuplicate.

An sRectangle node connecting to an sDuplicate node, and then viewed using an sRender node

Inspector

The sRectangle Controls tab

Controls

The Controls tab is used to define the rectangle characteristics, including fill, border, size, and position.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Solid

When enabled, the Solid checkbox fills the rectangle shape with the color defined in the Style tab.

When disabled, an outline created by the Border Width control is displayed, and the center is made

transparent.

Border Width

This parameter expands or contracts the border around the shape. Although it can be used when the

Solid checkbox is enabled, it is primarily used to determine the outline thickness when the checkbox

is disabled.

Border Style

The Border Style parameter controls how the sides of the rectangle join at the corners. There are

three styles provided as options. Bevel squares off the corners. Round creates rounded corners. Miter

maintains pointed corners.

Cap style

When the Solid checkbox is disabled, three Cap Style options are displayed. The cap styles can create

lines with flat, rounded or squared ends. Flat caps have flat, squared ends, while rounded caps have

semi-circular ends. Squared caps have projecting ends that extend half the line width beyond the end

of the line.

The caps are not visible unless the length is below 1.0.

Position

The Position parameter is only displayed when the Solid checkbox is disabled. It allows you to position

the starting point of the shape. When used in conjunction with the Length parameter, it positions the

gap in the outline.

Length

The Length parameter is only displayed when the Solid checkbox is disabled. A length of 1.0 is a

closed shape. Setting the length below 1.0 creates an opening or gap in the outline. Keyframing the

Length parameters allows you to create write-on style animations.

X and Y Offset

These parameters are used to position the shape left, right, up, and down in the frame. The shape

starts in the center of the frame, and the parameters are used to offset the position. The offset

coordinates are normalized based on the width of the frame. So an X offset of 0.0 is centered and a

value of 0.5 places the center of the shape directly on the right edge of the frame.

Width/Height

The Width and Height parameters determine the vertical and horizontal size of the rectangle. If the

values are identical, then you have a square.

Corner Radius

This parameter determines if the corners of the rectangle are sharp or rounded. A value of 0.0

produces sharp corners, while a value of 1.0 will create a circle from a staring square shape or a pill

shape from a rectangle.

Angle

The Angle parameter rotates the shape based on the center axis.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Style Tab

The sRectangle Style tab

Style

The Style tab is used to assign color to the shape and control its transparency.

Color

The Color parameter controls determine the color of the fill and border from the sRectangle node.

To choose a shape color, you can click the color disclosure arrow and use the color swatch, or drag

the eye dropper into the viewer to select a color from an image. The RGBA sliders or number fields

can be used to enter the value of each color channel or the strength of the Alpha channel.

Allow Combining

When this checkbox is enabled, the Alpha channel value is maintained even when passing through

other nodes downstream that may cause the shape to overlap with copies of itself. When disabled,

the Alpha channel value may increase when the shape overlaps itself. For instance, if a rectangle

Alpha channel is set to .5, enabling the Allow Combining checkbox maintains that value even if the

shape passes through a duplicate or grid node that causes the shape and Alpha channel to overlap.

Disabling the checkbox causes the Alpha channel values to be compounded at each overlapping area.

Allow Combining Enabled (left), Allow Combining Disabled (right)


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

sRender

The sRender node

The sRender node converts the vector shapes to an image. The output of the sRender allows the

vector shapes to be integrated with other elements in a composite.

Inputs

There is one input on the Background node for an Effect Mask input.

Input1: [orange, required] This input accepts the output of your final shape node. A rendered bitmap

image is created from the sRender node for compositing into the rest of your comp.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

displayed area to only those pixels within the mask.

Basic Node Setup

The sRender node is always placed at the end of a string of Shape nodes. The output connects to

other 2D nodes like a Soft Glow node.

Multiple Shape nodes connected to the sRender node

and then processed and composited with a title


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION