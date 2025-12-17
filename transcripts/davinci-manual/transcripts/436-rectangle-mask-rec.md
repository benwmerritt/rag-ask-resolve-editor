---
title: "Rectangle Mask [Rec]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 436
---

# Rectangle Mask [Rec]

The Rectangle node

Rectangle Mask Node Introduction

The Rectangle mask creates simple square or rectangular masks. By default, it creates a rectangle

in the same aspect ratio as the comp, but independent control is offered over the width, height, and

angle, providing for a wide variety of rectangular shapes.

Inputs

The Rectangle mask node includes a single effect mask input.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input combines the masks. How

masks are combined is handled in the Paint mode menu in the Inspector.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Basic Node Setup

The Rectangle mask node is useful for generating rectangular shapes. Below, the Rectangle mask is

used to generate a colored square by cutting a square shape from a background node.

A Rectangle mask node creating a colored

square by masking a Background node

Inspector

Rectangle Mask controls

Controls Tab

The Controls tab is used to refine how the rectangle appears after drawing it in the viewer.

Show View Controls

The Show View Controls checkbox is used to enable/disable the display of the mask’s onscreen

controls in the viewer. Onscreen controls, including center position, polylines, angles, and others, do

not appear when this checkbox is disabled, even when the node is selected.

Level

The Level control sets the transparency level of the pixels in the mask channel. When the value is 1.0,

the mask is completely opaque (unless it has a soft edge). Lower values cause the mask to be partially

transparent. The result is identical to lowering the Blend control of an effect.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

NOTE: Lowering the level of a mask lowers the values of all pixels covered by the mask in

the mask channel. For example, if a Circle mask is placed over a Rectangle mask, lowering

the level of the Circle mask lowers the values of all the pixels in the mask channel, even

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

�Invert: Areas of the input mask that are covered by the new mask are inverted: white becomes

black and vice versa. Gray areas in the new mask are partially inverted.

�Copy: This mode completely discards the input mask and uses the new mask for all values.

�Ignore: This mode completely discards the new mask and uses the input mask for all values.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Invert

Selecting this checkbox inverts the entire mask. Unlike the Invert Paint mode, this checkbox affects all

pixels, regardless of whether the new mask covers them.

Solid

When the Solid checkbox is enabled, the mask is filled to be transparent (white) unless inverted.

When disabled, the spline is drawn as just an outline whose thickness is determined by the Border

Width slider.

Center X and Y

These controls adjust the position of the Rectangle mask.

Width and Height

Use these controls to change the X or Y scale of the rectangular effect mask independently of each

other. Alternatively, drag the edges of the rectangle in the viewer to interactively adjust its size.

Corner Radius

Corner Radius allows the corners of the Rectangle mask to be rounded. A value of 0.0 is not rounding

at all, which means that the rectangle has sharp corners. A value of 1.0 applies the maximum amount of

rounding to the corners.

Angle

Change the rotation angle of an effect mask by moving the Angle control left or right. Values can be

entered in the provided input boxes. Alternatively, use the onscreen controls by dragging the little

circle at the end of the dashed angle line to interactively adjust the rotation of the ellipse.

Common Controls

Image and Settings Tabs

The Image and Settings tabs in the Inspector are also duplicated in other mask nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.

Triangle Mask [Tri]

The Triangle node

Triangle Mask Node Introduction

The Triangle mask creates simple triangular masks. It is unique in that it has no Center, Size, or Angle

control. Unlike most other types of masks, all three points of the triangle can attach to a tracker or

motion path.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Inputs

The Triangle mask node includes a single effect mask input.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input combines the masks. How

masks are combined is handled in the Paint mode menu in the Inspector.

Basic Node Setup

The Triangle mask node is useful for generating triangular shapes. Below, the Triangle mask is used to

generate a colored triangle by cutting a triangular shape from a background node.

A Triangle mask node creating

a colored Triangle shape by

masking a Background node

Inspector

Triangle Mask controls

Controls Tab

The Controls tab is used to refine how the triangle appears after drawing it in the viewer.

Show View Controls

The Show View Controls checkbox is used to enable/disable the display of the mask’s onscreen

controls in the viewer. Onscreen controls, including center position, polylines, angles, and others, do

not appear when this checkbox is disabled, even when the node is selected.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Level

The Level control sets the transparency level of the pixels in the mask channel. When the value is 1.0,

the mask is completely opaque (unless it has a soft edge). Lower values cause the mask to be partially

transparent. The result is identical to lowering the Blend control of an effect.

NOTE: Lowering the level of a mask lowers the values of all pixels covered by the mask in

the mask channel. For example, if a Circle mask is placed over a Rectangle mask, lowering

the level of the Circle mask lowers the values of all the pixels in the mask channel, even

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


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

�Replace: The new mask completely replaces the input mask wherever they intersect. Areas that

are zero (completely black) in the new mask do not affect the input mask.

�Invert: Areas of the input mask that are covered by the new mask are inverted: white becomes

black and vice versa. Gray areas in the new mask are partially inverted.

�Copy: This mode completely discards the input mask and uses the new mask for all values.

�Ignore: This mode completely discards the new mask and uses the input mask for all values.

Invert

Selecting this checkbox inverts the entire mask. Unlike the Invert Paint mode, this checkbox affects all

pixels, regardless of whether the new mask covers them.

Solid

When the Solid checkbox is enabled, the mask is filled to be transparent (white) unless inverted.

When disabled, the spline is drawn as just an outline whose thickness is determined by the Border

Width slider.

Point 1, Point 2, Point 3

These controls show the position coordinates of the three corners of the triangle. Each point can be

published, connected to other controls, animated with a path, or attached to trackers. These tasks are

performed by right-clicking the Position control or directly on the point in the viewer.

Common Controls

Image and Settings Tabs

The Image and Settings tabs in the Inspector are also duplicated in other mask nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.