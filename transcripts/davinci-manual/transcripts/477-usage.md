---
title: "Usage"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 477
---

# Usage

The sBSpline controls

When first added to a Node Editor, the sBSpline shape consists of only Center control, which is

visible onscreen.

Points are added to the sBSpline by clicking in the viewer. Each new point is connected to the last

one created, but instead of the spline going directly through each control point, sBSpline control

points only influence the spline shape. The control point pulls the spline in its direction to create a

smooth curve.

Like the sPolygon shape tool, the sBSpline shape auto-animates. Adding this node to the Node Editor

adds a keyframe to the current frame. Moving to a new frame and changing the shape creates a new

keyframe and interpolate between the two defined shapes.

sChangeStyle [sCs]

The sChangeStyle node

sChangeStyle Node Introduction

The sChangeStyle node assigns a new style to the combined shape tree, overriding the style (color

and Allow Combining settings) set in the upstream shape tools.

Inputs

The single input on the sChangeStyle tool is used to connect the Shape node you want to change

the style of.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Basic Node Setup

Connect the shape output that you wish change the style of to the input. The output of the node then

gets passed to the remainder of the shape node tree.

A simple node tree showing the sChangeShape node taking the output of an sEllipse

shape, performing the style change, and passing it to the sRender node.

Inspector

The sChangeStyle controls

Controls

The Style tab is used to assign color to the shape and control its transparency.

Color

The Color parameter controls determine the color of the fill and border from the sPolygon node. To

choose a shape color, you can click the color disclosure arrow and use the color swatch, or drag the

eye dropper into the viewer to select a color from an image. The RGBA sliders or number fields can be

used to enter the value of each color channel or the strength of the Alpha channel.

Allow Combining

When this checkbox is enabled, the Alpha channel value is maintained, even when passing through

other nodes downstream that may cause the shape to overlap with copies of itself. When disabled,

the Alpha channel value may increase when the shape overlaps itself. For instance, if a rectangle

Alpha channel is set to .5, enabling the Allow Combining checkbox maintains that value, even if the

shape passes through a duplicate or grid node that causes the shape and Alpha channel to overlap.

Disabling the checkbox causes the Alpha channel values to be compounded at each overlapping area.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Allow Combining enabled (left), Allow Combining disabled (right)

sDuplicate

The sDuplicate node

The sDuplicate node creates copies of the input shape, offsetting each copy’s position, size, and

rotation. Like almost all shape nodes, you can only view the sDuplicate node’s results through a

sRender node.

External Inputs

The following input appears on the node’s tile in the Node Editor:

Input1: [orange, required] This input accepts the output of another Shape node. The shape connected

to this input is copied and offset based on the controls in the Inspector.

Basic Node Setup

The sDuplicate node takes a single input that is most often from a single or compound shape from a

sMerge or sBoolean node. The sDuplicate node creates copies of the incoming shape and offsets

them to create a pattern. The output of the sDuplicate can then be output to another shape node or to

a sRender node for viewing or compositing into the greater node tree.

An sEllipse shape connected to an sDuplicate and then output to an

sRender for viewing and combining with other elements


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Inspector

The sDuplicate Controls tab

Controls

The Controls tab is used to determine the number of copies and set their position, size, and rotation offset.

Copies

This slider determines the number of copies created by the node. The number does not include the

original shape, so entering a value of five will produce five copies plus the original.

X and Y Offset

These sliders set the X and Y distance between each of the copies. Each copy is offset from the

previous copy by the value entered in the X and Y number fields. The copies all start at 0, the center of

the original shape, and are offset from there. Using Fusion’s normalized coordinate system, entering X

Offset at 0.5 would move each copy half the frame’s width to the right. Entering -1.0 would move each

copy to the left by the width of the frame.

X and Y Size

Sets the X and Y size offset based on the previous shape size. For instance, an X and Y value of 1.0

creates copies identical in size to the original but. Entering a value of X and Y of 0.5 will cause each

copy to be half the size of the copy before it.

Axis Mode

The Axis mode menu provides four options for determining how each copy determines its

rotational pivot point.

�Absolute: Allows you to set an X and Y position for the axis of rotation based on the original

shape’s location. The axis of rotation is then copied and offset with each duplicated shape.

�Origin Relative: Each copy uses its center point as its axis of rotation.

�Origin Absolute: Each copy uses the center of the original shape as its axis of rotation.

�Progressive: Compounds each shape copy by progressively transforming each copy based on the

previous shape’s position, rotation, and scale.

X and Y Pivot

The X and Y pivot controls are displayed when the Axis mode is set to Absolute. You can use these

position controls to place the axis of rotation.

Rotation

Determines an offset rotation applied to each copy. The rotation is calculated from the offset rotation

of the previous copy. To rotate all copies identically, use the Angle parameter on the original shape or

use a sTransform node.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

sEllipse

The sEllipse node

The sEllipse node is used to create circular shapes. Like almost all shape nodes, you can only view the

sEllipse node’s results through a sRender node.

External Inputs

This node generates shapes and does not have any inputs.

Basic Node Setup

The sEllipse node is a shape generator, meaning it generates a shape and therefore has no input.

The output of the sEllipse can go into a sRender for viewing and further compositing or, more likely,

connect to another shape node like sGrid or sDuplicate.

An sEllipse node connecting to an sGrid node, and then viewed using an sRender node

Inspector

The sEllipse Controls tab


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Controls

The Controls tab is used to define the elliptical shape characteristics, including fill, border, size,

and position.

Solid

When enabled, the Solid checkbox fills the elliptical shape with the color defined in the Style tab.

When disabled, an outline created by the Border Width control is displayed, and the center is made

transparent.

Border Width

This parameter expands or contracts the border around the shape. Although it can be used when the

Solid checkbox is enabled, it is primarily used to determine the outline thickness when the checkbox

is disabled.

Cap style

When the Solid checkbox is disabled, three cap style options are displayed. The cap styles can create

lines with flat, rounded, or squared ends. Flat caps have flat, squared ends, while rounded caps have

semi-circular ends. Squared caps have projecting ends that extend half the line width beyond the end

of the line.

The caps are not visible unless the length is below 1.0.

Position

The position parameter is only displayed when the Solid checkbox is disabled. It allows you to position

the starting point of the shape. When used in conjunction with the length parameter, it positions the

gap in the ellipse outline.

Length

The length parameter is only displayed when the Solid checkbox is disabled. A length of 1.0 is a

closed shape. Setting the length below 1.0 creates an opening or gap in the outline. Keyframing the

length parameters allows you to create write-on style animations.

X and Y Offset

These parameters are used to position the shape left, right, up, and down in the frame. The shape

starts in the center of the frame, and the parameters are used to offset the position. The offset

coordinates are normalized based on the width of the frame. An X offset of 0.0 is centered, and a

value of 0.5 places the center of the shape directly on the right edge of the frame.

Width/Height

The width and height determine the vertical and horizontal size of the ellipse. If the values are

identical, then you have a perfect circle.

Angle

The angle rotates the shape, which on a perfect circle doesn’t change the image all that much, but if

you create an oval or an outline with a short length, you can rotate the shape based on the center axis.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION