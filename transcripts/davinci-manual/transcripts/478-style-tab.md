---
title: "Style Tab"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 478
---

# Style Tab

The sEllipse Style tab

Style

The Style tab is used to assign a color to the shape and control its transparency.

Color

The color controls determine the color of the fill and border. To choose a shape color, you can click the

color disclosure arrow, use the color swatch, or drag the eyedropper into the viewer to select a color

from an image. The RGBA sliders or number fields can be used to enter each color channel’s value or

the strength of the Alpha channel.

Allow Combining

When this checkbox is enabled, the Alpha channel value is maintained even when passing through

other nodes downstream that may cause the shape to overlap with copies of itself. When disabled, the

Alpha channel value may increase when the shape overlaps itself.

For instance, if an ellipse’s Alpha channel is set to .5, enabling the Allow Combining checkbox

maintains that value even if the shape passes through a Duplicate or Grid node that causes the shape

to overlap. Disabling the checkbox causes the Alpha channel values to be compounded at each

overlapping area.

Allow Combining Enabled (left), Allow Combining Disabled (right)


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

sExpand

The sExpand node

The sExpand node is used to dilate or erode shapes. Like almost all Shape nodes, you can only view

the sExpand node’s results through a sRender node.

External Inputs

The following input appears on the node’s tile in the Node Editor.

Input1: [orange, required] This input accepts the output of another shape node. This shape or

compound shape connected to this input is either eroded or dilated.

Basic Node Setup

The sExpand node takes a single input that is most often from a compound shape. However, it can

be used on single shapes like sStars and sNgons. The output of the sExpand can then be output to

another shape node or to a sRender node for viewing or compositing into the greater node tree.

Star and ellipse shapes combined in an sBoolean node, then output to an sExpand for dilating or eroding

Inspector

The sExpand Controls tab


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Controls

The Controls tab includes all of the parameters for the sExpand node.

Amount

A positive value dilates the shape while a negative value erodes it.

Border Style

The border style controls how the expanded or contracted shapes join at the corners. There are four

styles provided as options. Bevel squares off the corners. Round creates rounded corners. Miter and

Miter Clip maintain pointed edges, until a certain threshold. The Threshold is set by the Miter limit slider.

Miter Limit

The Miter parameter is only displayed when the Miter or Miter Clip border style is selected. The miter

limit determines when the pointed edges become beveled based on the shape’s thickness.

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

sGrid

The sGrid node

The sGrid node replicates the shape on an X and Y grid and adds the ability to offset the rows

and columns. Like almost all Shape nodes, you can only view the sGrid node’s results through a

sRender node.

External Inputs

The following input appears on the node’s tile in the Node Editor.

Input1: [orange, required] This input accepts the output of another Shape node. The shape connected

to this input is replicated on a custom grid.

Basic Node Setup

The sGrid node takes a single input from a single or compound shape from am sMerge or sBoolean

node. The sGrid node places the incoming shape on a grid of rows and columns. The output of the

sGrid can then be output to another Shape node or a sRender node for viewing or compositing into

the greater node tree.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

An sEllipse shape connected to an sGrid and then output to an sRender

for viewing and combining with other elements

Inspector

The sGrid Controls tab

Controls

The Controls tab is used to determine the number of grid cells and their offset position.

Grid Cells X and Y

These parameters set the number of cells on the grid, both horizontally and vertically. For instance,

entering 5 in the X and Y number field creates five rows of the shape and five columns.

X and Y Offset

Sets the X and Y distance between the rows and columns. An offset value of 0.0 will have all the rows

and columns on top of each other. Entering X Offset at 1.0 would spread the columns the width to

the frame.

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

sJitter

The sJitter node

The sJitter node is most often used to randomly position an array of shapes generated from a sGrid or

sDuplicate node. However, it includes an auto-animating random mode that can be used to distort and

randomly jitter single shapes.

Like almost all Shape nodes, you can only view the sJitter node’s results through a sRender node.

External Inputs

The following input appears on the node’s tile in the Node Editor.

Input1: [orange, required] This input accepts the output of another Shape node. The shape connected

to this input is offset, distorted, and animated based on the sJitter node settings.

Basic Node Setup

The sJitter node takes an array of shapes from a sGrid or sDuplicate node and randomly changes their

position, size, and rotation. The output of the sExpand can then be output to another Shape node or to

a sRender node for viewing or compositing into the greater node tree.

An array of shapes created by the sGrid node input into an sJitter node to randomly offset or scale the shapes

Inspector

The sJitter Controls tab


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Controls

The Controls tab offers range sliders that determine the variation amount for offset, size, and rotation.

The Point Jitter parameters are used to offset the invisible points that create the vector shapes.

Jitter Mode

The Jitter Mode menu allows you to choose between static position and size offsets or enabling

an auto-animation mode. Leaving the default Fixed selection allows you to offset a grid of shapes,

animating with keyframes or modifiers if needed. The Random menu selection auto-animates the

parameters based on the range you define using the range sliders. If all the range sliders are left in

the default position, no random animation is created. Increasing the range on any given parameter will

randomly animate that parameter between the range slider values.

Shape X and Y Offset

These parameters set the horizontal and vertical offset from the shape array’s original position. This is

done randomly, so not all shapes in the array will offset by the same amount.

Shape X and Y Size

These parameters set the horizontal and vertical scaling for each shape in an array. The left range

value decreases the scale, and the right range value increases the scale. This is done randomly, so not

all shapes in the array will scale by the same amount.

Shape Rotate

This parameter rotates each shape in an array.

Point Jitter

The X and Y Point Jitter parameters use the vector control points to distort the shape. This can be

used to give a distressed appearance to ellipses or wobbly animation to other shapes.

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.