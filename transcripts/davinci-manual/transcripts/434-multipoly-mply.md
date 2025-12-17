---
title: "MultiPoly [MPly]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 434
---

# MultiPoly [MPly]

The MultiPoly node

Introduction

The MultiPoly tool makes rotoscoping more efficient by allowing you to create multiple masks in a

single node. The list of polygon shapes in the inspector allows you to easily modify, organize, and

animate shapes through one simple interface.

With the multiple masks presented in a scrolling list format, akin to the convenience offered by MultiMerge,

you can effortlessly organize, edit, and animate individual shapes. This intuitive interface streamlines

the process of drawing intricate masks, empowering you to create polished compositions with ease.

Furthermore, all these advantages are available within this List view, facilitating swift selection and

modification of specific shapes, toggling their visibility, and precise adjustment of their parameters.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Usage

After adding the MultiPoly, the tool is ready for you to start drawing your first mask.

To create a mask, use the tools at the top of the viewer to create polygons, splines, and points (these

points will make up segments of the polyline). You can close the mask by clicking the initial point again.

The MutliPoly tool showing three creation of masks on the viewer

Inspector

Multipoly controls


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

In the Inspector, pressing the Polygon or BSpline button will create a new mask type. Each new mask

is added to the List view located in the Inspector.

Within the List view, you can rename or reorder any of the masks you’ve just added. Modify specific

shapes by selecting them in the layer list and changing their properties in the lower portion of the

Inspector.

To animate any of the drawn masks, select the animation diamond next to the text “Right-click

here for shape animation,” at the bottom of the Inspector or you can right-click on this text and

select Animate.

Within the layer list, right clicking on a mask offers a few options.

Duplicate: Makes a copy of the selected mask and adds a new entry in the layer list.

Split here: Splits the selected mask and any mask below it, copying them to a new fresh

MultiPoly node.

Rename: Allows you to rename the selected mask.

Reset to default: Keeps the mask entry in the layer list but removes the mask shape and

resets all the controls for that mask.

Delete: Deletes the mask.

Polygon Mask [Ply]

The Polygon node

Polygon Mask Node Introduction

The Polygon mask is most useful for masking objects that do not have a regular shape. When first

added to a node, the Polygon mask consists of only Center and Angle controls, which are visible

onscreen. Points are added to the polyline by clicking in the viewer. Each new point is connected to

the last one created.

Like the B-Spline mask tool, the Polygon mask auto-animates. Adding this node to the Node Editor

adds a keyframe to the current frame. Moving to a new frame and changing the shape creates a new

keyframe and interpolate between the two defined shapes.

Inputs

The Polygon mask node includes a single effect mask input.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input combines the masks. How

masks are combined is handled in the Paint mode menu in the Inspector.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Basic Node Setup

The Polygon node can be used to generate a detailed spline shape or combined with other masks for

even more complex shapes. In the node tree below, the Polygon mask is used to generate detailed

shape as a solid matte on the Delta Keyer.

A Polygon node generates a detailed shape as a Solid matte.

Inspector

Polygon Mask controls

Controls Tab

The Controls tab is used to refine how the polyline appears after drawing it in the viewer.

Show View Controls

The Show View Controls checkbox is used to enable/disable the display of the mask’s onscreen

controls in the viewer. Onscreen controls, including center position, polylines, angles, and others, do

not appear when this checkbox is disabled, even when the node is selected.

Level

The Level control sets the transparency level of the pixels in the mask channel. When the value is 1.0,

the mask is completely opaque (unless it has a soft edge). Lower values cause the mask to be partially

transparent. The result is identical to lowering the blend control of an effect.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

NOTE: Lowering the level of a mask lowers the values of all pixels covered by the mask in

the mask channel. For example, if a Circle mask is placed over a Rectangle mask, lowering

the level of the Circle mask lowers the values of all of the pixels in the mask channel, even

though the Rectangle mask beneath it is still opaque.

Filter

This control selects the filtering algorithm used when applying Soft Edge to the mask.

�Box: This is the fastest method but at reduced quality. Box is best suited for minimal

amounts of blur.

�Bartlett: Otherwise known as a Pyramid filter, Bartlett makes a good compromise between speed

and quality.

�Multi-box: When selecting this filter, the Num Passes slider appears and lets you control the

quality. At 1 and 2 passes, results are identical to Box and Bartlett, respectively. At 4 passes and

above, results are usually as good as Gaussian, in less time and with no edge “ringing.”

�Gaussian: The Gaussian filter uses a true Gaussian approximation and gives excellent results, but

it is a little slower than the other filters. In some cases, it can produce an extremely slight edge

“ringing” on floating-point pixels.

Soft Edge

Use the Soft Edge slider to blur (feather) the mask, using the selected filter. Higher values cause

the edge to fade off well beyond the boundaries of the mask. A value of 0.0 creates a crisp, well-

defined edge.

Border Width

The Border Width control adjusts the thickness of the mask’s edge. When the solid checkbox is

toggled on, the border thickens or narrows the mask. When the mask is not solid, the mask shape

draws as an outline, and the width uses the Border Width setting.

Paint Mode

Connecting a mask to the effect mask input displays the Paint mode menu. The Paint mode is used

to determine how the incoming mask for the effect mask input and the mask created in the node

are combined.

�Merge: Merge is the default for all masks. The new mask is merged with the input mask.

�Add: The mask’s values add to the input mask’s values.

�Subtract: In the intersecting areas, the new mask values subtract from the input mask’s values.

�Minimum: Comparing the input mask’s values and the new mask, this displays the lowest

(minimum) value.

�Maximum: Comparing the input mask’s values and the new mask, this displays the highest

(maximum) value.

�Average: This calculates the average (half the sum) of the new mask and the input mask.

�Multiply: This multiplies the values of the input mask by the new mask’s values.

�Replace: The new mask completely replaces the input mask wherever they intersect. Areas that

are zero (completely black) in the new mask do not affect the input mask.

�Invert: Areas of the input mask that are covered by the new mask are inverted; white becomes

black and vice versa. Gray areas in the new mask are partially inverted.

�Copy: This mode completely discards the input mask and uses the new mask for all values.

�Ignore: This mode completely discards the new mask and uses the input mask for all values.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Invert

Selecting this checkbox inverts the entire mask. Unlike the Invert Paint mode, the checkbox affects all

pixels, regardless of whether the new mask covers them or not.

Solid

When the Solid checkbox is enabled, the mask is filled to be transparent (white) unless inverted.

When disabled, the spline is drawn as just an outline whose thickness is determined by the Border

Width slider.

Center X and Y

These controls adjust the position of the polygon spline mask.

Size

Use the Size control to adjust the scale of the polygon spline effect mask, without affecting the relative

behavior of the points that compose the mask or setting a keyframe in the mask animation.

X, Y, and Z Rotation

Use these three controls to adjust the rotation angle of the mask along any axis.

Fill Method

The Fill Method menu offers two different techniques for dealing with overlapping regions of a

polyline. If overlapping segments in a mask are causing undesirable holes to appear, try switching the

setting of this control from Alternate to Non Zero Winding.

Right-Click Here for Shape Animation

By default, all polygon spline masks are animated when they are created. The initial keyframe is set to

the current time, and any changes to the shape at different times create new keys.

Right-clicking on this label displays a contextual menu that offers options for removing or re-adding

animation to the mask, or publishing and connecting the masks together.

Common Controls

Image and Settings Tabs

The Image and Settings tabs in the Inspector are also duplicated in other mask nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.