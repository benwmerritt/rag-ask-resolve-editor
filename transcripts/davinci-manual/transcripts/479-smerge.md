---
title: "sMerge"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 479
---

# sMerge

The sMerge node

The sMerge node combines shapes similar to a standard Merge node, except the sMerge node can

accept more than two shape inputs.

Like almost all Shape nodes, you can only view the sMerge node’s results through a sRender node.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

External Inputs

The node displays only two inputs first, but as each shape node is connected, a new input appears on

the node, assuring there is always one free to add a new shape into the composite.

Input[#]: These multi-colored inputs are used to connect multiple Shape node. There is no limit to the

number of inputs this node can accept. The node dynamically adds more inputs as needed, ensuring

that there is always at least one input available.

Basic Node Setup

The sMerge node is used to combine two Shape nodes. In terms of layering, each subsequent input

is placed over the previous input. For instance, the first shape connected to the orange input is the

bottom-most shape, the green input is layered over it, and if a third shape is connected to the pink

input, that is the topmost layer.

Three shapes are combined in an sMerge node, then output to an sRender for viewing and further processing.

Inspector

The sMerge Controls tab

Controls

The only control for the sMerge node is the Override Axis checkbox, which overrides the shape’s axis.

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

sNGon

The sNGon node

The sNGon node is used to create multi-sided shapes like triangles, pentagons, and octagons.

Like almost all Shape nodes, you can only view the sNGon node’s results through a sRender node.

External Inputs

This node generates shapes and does not have any inputs.

Basic Node Setup

The sNGon node is a shape generator, meaning it generates a shape and therefore has no inputs.

The output of the sNGon can go into a sRender for viewing and further compositing or, more likely,

connect to another Shape node like sGrid or sDuplicate.

An sNGon node connecting to an sDuplicate node, and then viewed using an sRender node.

Inspector

The sNGon Controls tab

Controls

The Controls tab is used to define multi-sided shape characteristics, including fill, border, size,

and position.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Solid

When enabled, the Solid checkbox fills the NGon shape with the color defined in the Style tab.

When disabled, an outline created by the Border Width control is displayed, and the center is made

transparent.

Border Width

This parameter expands or contracts the border around the shape. Although it can be used when the

Solid checkbox is enabled, it is primarily used to determine the outline thickness when the checkbox

is disabled.

Border Style

The Border Style parameter controls how the sides of the NGon join at the corners. There are three

styles provided as options. Bevel squares off the corners. Round creates rounded corners. Miter

maintains pointed corners.

Cap style

When the Solid checkbox is disabled, three cap style options are displayed. The cap styles can create

lines with flat, rounded, or squared ends. Flat caps have flat, squared ends, while rounded caps have

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

coordinates are normalized based on the width of the frame. So, an X offset of 0.0 is centered and a

value of 0.5 places the center of the shape directly on the right edge of the frame.

Width/Height

The Width and Height parameters determine the vertical and horizontal size of the ellipse. If the values

are identical, then all sides are of equal length.

Angle

The Angle parameter rotates the shape based on the center axis.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Style Tab

The sNGon Style tab

Style

The Style tab is used to assign a color to the shape and control its transparency.

Color

The Color controls determine the color of the fill and border. To choose a shape color, you can click

the color disclosure arrow, use the color swatch, or drag the eyedropper into the viewer to select a

color from an image. The RGBA sliders or number fields can be used to enter each color channel’s

value or the strength of the Alpha channel.

Allow Combining

When this checkbox is enabled, the Alpha channel value is maintained even when passing through

other nodes downstream that may cause the shape to overlap with copies of itself. When disabled, the

Alpha channel value may increase when the shape overlaps itself.

For instance, if a NGon Alpha channel is set to .5, enabling the Allow Combining checkbox maintains

that value even if the shape passes through a duplicate or grid node that causes the shape to overlap.

Disabling the checkbox causes the Alpha channel values to be compounded at each overlapping area.

Allow Combining Enabled (left), Allow Combining Disabled (right)

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION