---
title: "Chapter 117"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 476
---

# Chapter 117

Shape Nodes

This chapter details the Shape nodes available in Fusion.

Contents

sBoolean������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2661

sBSpline [sBSp]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2664

sChangeStyle [sCs]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2665

sDuplicate��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2667

sEllipse���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2669

sExpand�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2672

sGrid��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2673

sJitter������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2675

sMerge���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2676

sNGon������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2678

sOutline��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2681

sPolygon [sPly]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2682

Adding Points��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2686

sRectangle�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2687

sRender�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2690

sStar��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2693

sText [sTxt]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2696

sTransform��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2697

Common Controls����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2698


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

sBoolean

The sBoolean node

The sBoolean node combines or excludes overlapping areas of two shapes based on a menu of

boolean operations.

Like almost all shape nodes, you can only view the sBoolean node’s results through a sRender node.

External Inputs

The following inputs appear on the node’s tile in the Node Editor. Except when using the subtract

boolean operation, which shape you connect into which input does not matter.

Input1: [orange, required] This input accepts the output of another shape node. This input is used as

the base shape when the subtract boolean operation is chosen.

Input2: [green, optional] This input accepts the output of another shape node. This input is used to cut

the base shape hole when the subtract boolean operation is chosen.

Basic Node Setup

The sBoolean node is used to combine two shape nodes. The output of the sBoolean can then be

output to another shape node or a sRender node for viewing.

Star and ellipse shapes combined in an sBoolean node, then output

to an sRender for viewing and further processing

Inspector

The sBoolean Controls tab


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Controls

The Controls tab is primarily used to select the boolean operation that determines how the two shapes

are combined.

Operation

The operation menu includes four boolean operations:

Intersection: Sometimes called an AND operation, this setting will only show areas where the

two shapes overlap. The result is only where input 1 AND input 2 overlap.

Star and ellipse shapes with an sBoolean node set to intersection

Union: Sometimes called an OR operation, this setting will only show areas where either of

the two shapes exists. The result is where either input 1 OR input 2 exists. The Union setting is

similar to the result of the sMerge node.

Star and ellipse shapes with an sBoolean node set to union

Subtract: Sometimes called a NOT operation, this setting outputs the shape of input 1 but

eliminates the areas where input 2 overlaps. The result is input 1 minus input 2.

Star and ellipse shapes with an sBoolean node set to subtract


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Xor: Sometimes called an AND NOT operation, this setting outputs the shape of input 1 or

input 2 but eliminates the areas where they overlap. The result is (input 1 minus input 2) +

(input 2 minus input 1).

Star and ellipse shapes with an sBoolean node set to xor

Style Mode

The Style mode menu only includes one option. The Replace setting replaces the color and alpha

level of the incoming shapes with the color set in the Style tab.

Style Tab

The sBoolean Style tab

Style

Any color assigned to the individual shape nodes is replaced by the color set using the Style

tab controls.

Color

The color controls determine the color of the output shape from the sBoolean node. To choose a

shape color, you can click the color disclosure arrow, use the color swatch, or drag the eyedropper

into the viewer to select a color from an image. The RGBA sliders or number fields can be used to

enter each color channel’s value or the strength of the Alpha channel.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Allow Combining

When this checkbox is enabled, the Alpha channel value is maintained even when passing through

other nodes downstream that may cause the shape to overlap with copies of itself. When disabled, the

Alpha channel value may increase when the shape overlaps itself.

For instance, if an ellipse’s Alpha channel is set to .5, enabling the Allow Combining checkbox

maintains that value even if the shape passes through a duplicate or grid node that causes the shape

to overlap. Disabling the checkbox causes the Alpha channel values to be compounded at each

overlapping area. When using the sBoolean node, the individual shape node checkboxes are ignored,

and the sBoolean node’s checkbox determines the Alpha channel's behavior.

Allow Combining Enabled (left), Allow Combining Disabled (right)

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

sBSpline [sBSp]

The sBSpline node

Introduction

sBSpline is identical to a sPolygon in all respects except one. Where sPolygon use Bézier splines, this

node uses B-Splines. Where Bézier splines employ a central point and two handles to manage the

smoothing of the spline segment, a B-Spline requires only a single point. This means that a sBSpline

shape requires far fewer control points to create a nicely smoothed shape.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION