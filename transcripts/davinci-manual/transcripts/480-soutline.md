---
title: "sOutline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 480
---

# sOutline

The sOutline node

The sOutline node is used to create outlines from merged or boolean compound shapes. The

individual shapes retain their own style, color, size, position, and other characteristics. The only

difference is the border thickness, border style, position, and length are applied to all incoming shapes

uniformly in the sOutline node.

Like almost all shape nodes, you can only view the sOutline node’s results through a sRender node.

External Inputs

The following input appears on the node’s tile in the Node Editor:

Input1: [orange, required] This input accepts the another shape node’s output, but more likely a

compound shape from a sMerge or sBoolean. An outline is created from the compound shape

connected to this input.

Basic Node Setup

The sOutline node takes a single input that is most often from a compound shape, however, it can

sometimes be useful on single shapes to create double outlines. The output of the sOutline can then

be output to another Shape node or to a sRender node for viewing or compositing into the greater

node tree.

A compound shape from an sBoolean node is connected

to an sOutline for creating a complex outlined shape

Inspector

The sOutline Controls tab


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Controls

The Controls tab is used to define the outline thickness, border and cap style, position, and length that

is applied to the compound shape connected to the input.

Thickness

This parameter controls the width of the outline.

Border Style

The Border Style parameter controls how the outline joins at the corners. There are three styles

provided as options. Bevel squares off the corners. Round creates rounded corners. Miter maintains

pointed corners.

Cap style

Three Cap Style options are used to create lines with flat, rounded, or squared ends. Flat caps have

flat, squared ends, while rounded caps have semi-circular ends. Squared caps have projecting ends

that extend half the line width beyond the end of the line.

The caps are not visible unless the length is below 1.0.

Position

The Position parameter allows you to position the starting point of the shape. When used in

conjunction with the Length parameter, it positions the gap in the outline.

Length

The Length parameter controls the end position of the outline. A length of 1.0 is a closed shape.

Setting the length below 1.0 creates an opening or gap in the outline. Keyframing the Length

parameters allows you to create write-on style animations.

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

sPolygon [sPly]

The sPolygon node

The sPolygon tool allows users to draw custom shapes. Through intuitive point manipulation, this tool

allows users to effortlessly generate intricate forms, curves, and lines, which tie in with the existing

shape tools in Fusion. It provides the freedom to design custom elements, making it a valuable tool in

motion graphics design.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Inputs

This node generates shapes and does not have any inputs.

Basic Node Setup

The sPolygon node is a shape generator, meaning it generates a shape and therefore has no inputs.

The output of the sPolygon can go into a sRender for viewing and further compositing or, more likely,

connect to another Shape node like sGrid or sDuplicate.

An sPolygon node connecting to an sDuplicate node, and then viewed using an sRender node

Inspector

The sPolygon Controls tab

Controls

The Controls tab is used to define the polygon characteristics, including fill, border, size, and position.

Solid

When enabled, the Solid checkbox fills the rectangle shape with the color defined in the Style tab.

When disabled, an outline created by the Border Width control is displayed, and the center is made

transparent.

Border Width

This parameter expands or contracts the border around the shape. Although it can be used when the

Solid checkbox is enabled, it is primarily used to determine the outline thickness when the checkbox

is disabled.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Border Style

The Border Style parameter controls how the sides of the rectangle join at the corners. There are

three styles provided as options. Bevel squares off the corners. Round creates rounded corners. Miter

maintains pointed corners.

Cap style

The cap styles can create lines with flat, rounded, or squared ends. Flat caps have flat, squared ends,

while rounded caps have semi-circular ends. Squared caps have projecting ends that extend half the

line width beyond the end of the line.

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

Z Offset [3D]

If used with the 3D toolset, you can offset the polygon in back and forth along the Z-axis by adjusting

these controls.

Size

Use the Size control to adjust the scale of the polygon shape, without affecting the relative behavior of

the points that compose the shape or setting a keyframe in the shape animation.

X,Y,Z Rotation

Use these three controls to adjust the rotation angle of the shape along any axis.

Fill Method [3D]

The Fill Method menu offers two different techniques for dealing with overlapping regions of a

polyline. If overlapping segments in a shape are causing undesirable holes to appear, try switching the

setting of this control from Alternate to Non Zero Winding.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Style Tab

The sPolygon Style tab

Style

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

Alpha channel is set to .5, enabling the Allow Combining checkbox maintains that value even if the

shape passes through a duplicate or grid node that causes the shape and Alpha channel to overlap.

Disabling the checkbox causes the Alpha channel values to be compounded at each overlapping area.

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in "The Common Controls” section.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION