---
title: "Adding Points"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 435
---

# Adding Points

Adding Points to a polygonal effect mask is relatively simple. Immediately after adding the node to the

Node Editor, there are no points, but the tool will be in Click Append mode. Click once in the viewer

wherever a point is required for the mask. Continue clicking to draw the shape of the mask. When the

shape is complete, click on the initial point again to close the mask.

When the shape is closed, the mode of the polyline will change to Insert and Modify. This allows for

the adjusting and adding of additional points to the mask by clicking on segments of the polyline. To

lock down the mask’s shape and prevent accidental changes, switch the Polyline mode to Done using

the Polyline toolbar or contextual menu.

B-Spline Mask Polygon toolbar


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

When a Polygon (or B-Spline) mask is added to a node, a toolbar appears above the viewer, offering

easy access to modes. Hold the pointer over any button in the toolbar to display a tooltip that

describes that button’s function.

�Click: Click is the default option when creating a polyline (or B-Spline) mask. It is a Bézier style

drawing tool. Clicking sets a control point and appends the next control point when you click again

in a different location.

�Draw: Draw is a freehand drawing tool. It creates a mask similar to drawing with a pencil on paper.

You can create a new mask using the Draw tool, or you can extend an existing open spline by

clicking the Draw tool and starting to draw from the last control point.

�Insert: Insert adds a new control point along the spline.

�Modify: Modify allows you to safely move or smooth any exiting point along a spline without

worrying about adding new points accidentally.

�Done: Prevents any point along the spline from being moved or modified. Also, new points cannot

be added. You can, however, move and rotate the entire spline.

�Closed: Closes an open spline.

�Smooth: Changes the selected control point from a linear to a smooth curve.

�Linear: Changes the selected control point from a smooth curve to linear.

�Select All: Selects all the control points on the spline.

�Keys: Shows or hides the control points along the spline.

�Handles: Shows or hides the Bézier handles along the polyline.

�Shape: Places a reshape rectangle around the selected spline shape. Using the reshape

rectangle, you can deform groups of control points or entire shapes much easier than modifying

each point.

�Delete: Deletes the selected control point(s).

�Reduce: Opens a Freehand precision window that can be used to reduce the number of controls

points on a spline. This can make the paint stroke easier to modify, especially if it has been

created using the Draw tool.

�Publish menu: You can use the publish menu to select between publishing the control points or

the path. Publishing is a form of parameter linking, it makes the selected item available for use by

other controls. It also allows you to attach a control point to a tracker.

�Follow Points: Allows a selected point to follow the path of a published point. The point follows

the published point using an offset position.

�Double Poly: Allows softening part of the spline curve while keeping other portions of the curve

sharp. The double polyline is composed of two shapes, an inner and outer shape. The inner shape

is the original shape from the single polyline, whereas the outer shape is used to determine the

spread of the softness. The further the outer shape gets from the inner shape, the softer that

segment of the shape becomes. Both polylines start with exactly the same shape as the original

single polyline, keeping the mask sharp to start. Any animation already applied to the shape

remains. To select the outer shape, press the Tab key to cycle between the onscreen controls

until the dashed outline is visible, or you can select the outer polyline using the contextual menu’s

Controls > Outer Polygon menu.

�Multiframe: Multiframe is a method of adjusting control points across multiple keyframes. The

default setting of none only adjusts the control point of a spline on the current keyframe. Setting

the menu to All adjusts the controls point for all keyframes. Prev settings adjust the current and

previous keyframe while Next adjusts the current and next keyframe.

�Onion Skinning: Enabling onion skinning displays a mix in the viewer of the spline animation. It is

useful when aligning spline animation and motion. Selecting Onion Skin Settings from the drop

down menu allows you to set the number of overlapping frames.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

�Roto Assist: Enable the Roto Assist button when you begin painting with the Polyline Stroke

tool. The polyline points snap to the closest edge as you click to add points to the shape. A cyan

outline indicates the points that have snapped to an edge. There are three main Roto Assist

options selectable through the drop down menu:

Multiple Points: When enabled, a single click on a high contrast edge adds multiple points to

define the entire edge, instead of having to add each point individually. This is a one time only

click. The second click reverts to single point edge detection.

Distance 8: Opens a dialog where you can set the pixel range within which searching for an edge

takes place.

Reset: Used for resetting the snap attribute of all snapped points. After resetting, the points

become unavailable for tracking.

Change the way the toolbar is displayed by right-clicking on the toolbar and selecting from

the options displayed in the toolbar’s contextual menu. The functions of the buttons in this

toolbar are explained in depth in the Polylines chapter.

Ranges Mask [RNG]

The Ranges node

Ranges Mask Node Introduction

Similar to Bitmap mask, the Ranges mask allows images from the node tree to act as masks for nodes

and effects. Instead of creating a simple luminance-based mask from a given channel, Ranges allows

spline-based selection of low, mid and high ranges, akin to Color Corrector.

Inputs

The Ranges mask node includes two inputs in the Node Editor.

Input: The orange input accepts a 2D image from which the mask will be created.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input combines the masks. How

masks are combined is handled in the Paint mode menu in the Inspector.

Basic Node Setup

The Ranges node is not required for connecting an image into the effect mask input, but like the

Bitmap node, it does provide options that are otherwise unavailable. It allows for selecting channels

other than RGBA for the mask, as well as softness and clipping. In the node tree below, the Ranges

node takes the composite out of the merge, creating a mask for the color correction.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

A Ranges node selects a specific range in the image to create a mask.

Inspector

Rangers Mask controls

Controls Tab

The Controls tab is used to refine how the image connected to the orange input converts into the

ranges mask.

Show View Controls

The Show View Controls checkbox is used to enable/disable the display of the mask’s onscreen

controls in the viewer. Onscreen controls, including center position, polylines, angles, and others, do

not appear when this checkbox is disabled, even when the node is selected.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Level

The Level control sets the transparency level of the pixels in the mask channel. When the value is 1.0,

the mask is completely opaque (unless it has a soft edge). Lower values cause the mask to be partially

transparent. The result is identical to lowering the blend control of an effect.

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

Center X and Y

These controls adjust the position of the ranges mask.

Fit Input

This menu is used to select how the image source is treated if it does not fit the dimensions of the

generated mask.

For example, below, a 720 x 576 image source (yellow) is used to generate a 1920 x 1080

mask (gray).

Crop: If the image source is smaller than the generated mask, it is placed according to the

X/Y controls, masking off only a portion of the mask. If the image source is larger than the

generated mask it is placed according to the X/Y controls and cropped off at the borders

of the mask.

Stretch: The image source is stretched in X and Y to accommodate the full dimensions of the

generated mask. This might lead to visible distortions of the image source.

Inside: The image source is scaled uniformly until one of its dimensions (X or Y) fits the inside

dimensions of the mask. Depending on the relative dimensions of the image source and mask

background, either the image source’s width or height may be cropped to fit the respective

dimension of the mask.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Width: The image source is scaled uniformly until its width (X) fits the width of the mask.

Depending on the relative dimensions of the image source and mask, the image source’s

Y dimension might not fit the mask’s Y dimension, resulting in either cropping of the image

source in Y or the image source not covering the mask’s height entirely.

Height: The image source is scaled uniformly until its height (Y) fits the height of the mask.

Depending on the relative dimensions of the image source and mask, the image source’s

X dimension might not fit the mask’s X dimension, resulting in either cropping of the image

source in X or the image source not covering the mask’s width entirely.

Outside: The image source is scaled uniformly until one of its dimensions (X or Y) fits the

outside dimensions of the mask. Depending on the relative dimensions of the image source

and mask, either the image source’s width or height may be cropped or not fit the respective

dimension of the mask.

Channel

The Channel menu determines the Channel of the input image used to create the mask. Choices

include the red, green, blue, and alpha channels; the hue, luminance, or saturation values; or the

auxiliary coverage channel of the input image (if one is provided).

Shadows/Midtones/Highlights

These buttons are used to select which range is output by the node as a mask. White pixels represent

pixels that are considered to be part of the range, and black pixels are not included in the range. For

example, choosing Shadows would show pixels considered to be shadows as white, and pixels that

are not shadows as black. Mid gray pixels are only partly in the range and do not receive the full effect

of any color adjustments to that range.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Channel

The Channel selection buttons shown in this tab can be used to extract a mask from the range

of a specific color channel. By default, Fusion uses the luminance channel when the color ranges

are examined.

Mini Spline Editor

The extent of the ranges is selected by manipulating the spline handles. There are four spline points,

each with one Bézier handle. The two handles at the top represent the start of the shadow and

highlight ranges; the two handles at the bottom represent the end of the range. The Bézier handles

are used to control the falloff.

The midtones range has no specific control, since its range is understood to be the space between

the shadow and highlight ranges. In other words, after low and high masks have been applied,

midtones are everything else.

The X and Y text controls below the Mini Spline Editor can be used to enter precise positions for the

selected Bézier point or handle.

Presets

This sets the splines to two commonly-used configurations. The Simple button gives a straightforward

linear-weighted selection, while the Smooth button uses a more natural falloff.

Common Controls

Image and Settings Tabs

The Image and Settings tabs in the Inspector are also duplicated in other mask nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.