---
title: "Hue – Saturation Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 565
---

# Hue – Saturation Controls

As the name implies, the Hue-Saturation mode lets you alter hue and saturation simultaneously.

For most people, this is likely the most intuitive mode in which to work as the range of hues and

saturation in the image is represented radially, just like the Vectorscope; in fact a Vectorscope graph of

the image appears underneath the “wheel” grid of control points used to manipulate color.

By default, dragging any point of this grid changes the colors immediately surrounding that point that

are between the point being manipulated and adjacent “spokes” of the radial grid that either aren’t

influenced by that point, or are locked into place. In fact, you can pull these radial control points well

past the boundary of adjacent spokes of the grid to warp those colors to entirely different hues.

The selected control point being adjusted doesn’t

affect points on adjacent columns of control points that

stretch from the outer ring to the center of this control, even

when the dragged point is moved all the way past.

When manipulating control points to alter color, adjustments are similar to pushing color around a

color wheel. Moving a control point radially around the circumference of the grid changes the hue of

the colors corresponding to that control point. Moving a control point closer to the center desaturates

those colors, while moving a control point closer to the edge of the grid increases the saturation of

those colors.

The following sections describe how the different tools available in this mode work to let you

manipulate these radial control points in different ways.

Tools

Each of the available tools let you manipulate control points on the warping grid in different ways when

you click on them.

�Selection Tool: The default tool mode. Selecting this tool lets you select control points either

individually (by clicking on a single point or command-clicking multiple points) or collectively by

dragging a bounding box over multiple points, and you can right-click on control points to de-

select, unlock, and reset them. You can also Shift-click with this tool to lock points into place

without moving them. This is the most useful tool to use when manipulating the image by clicking

and dragging in the Viewer to sample a color and adjust it at the same time.


Color | Chapter 136 Color Warper

COLOR

�Draw Selection: Selecting this tool lets you make a selection of control points by clicking and

dragging to draw over all the points you want to select. This is good for making large, but specific,

selections of points.

�Pin/De-Pin: Selecting this tool lets you pin multiple control points by either clicking on them or by

clicking and dragging to draw over all the points you want to pin/de-pin.

�Pull Points: Selecting this tool lets you make adjustments by clicking anywhere on the warp grid,

even between points, to pull all neighboring control points towards where you clicked. This can be

used to reduce color contrast within a specific range of colors.

�Push Points: Selecting this tool lets you make adjustments by clicking anywhere on the warp grid,

even between points, to push all neighboring control points within a particular proximity away from

where you clicked. This can be used to increase color contrast within a specific range of colors.

Modifiers

Each of the Modifier buttons let you manipulate selections and selected control points on the warping

grid in different ways immediately upon clicking each button.

�Increase Falloff/Smooth Selection: If you’ve selected one or more control points, clicking this

button expands the selection to include all adjacent control points surrounding the selection.

�Decrease Falloff/Smooth Selection: If you’ve selected a group of control points, clicking this

button shrinks the selection by deselecting the outermost ring of selected control points, leaving

the inner control points selected.

�Invert Selection: Clicking this button selects all unselected control points, and de-selects all

selected control points. This is useful when you want to make separate color adjustments to both

specifically selected halves of the warping grid.

�Convert Selection to Pin: Clicking this button pins all currently selected control points.

�Select/Pin Column: If you have one or more control points selected, clicking this button expands

the selection to include all points on every column that have at least one selected point.

�Select/Pin Ring: If you have one or more control points selected, clicking this button expands

the selection to include all points on every ring around the center that have at least one

selected point.

�Select/Pin All, Deselect/Pin All: Clicking this button toggles the selected state of the entire

warping grid on or off.

�Reset Selection/Pins: If you have one or more control points selected, clicking this button resets

their position to the original default position in the warping grid, without de-selecting them.

Range

The Range control is a fast method of selecting multiple control points corresponding to a specific

range of colors.

�Range: A gradient shows the range of hues currently being presented in the warping grid.

Dragging the left and right handles of the Range control selection box lets you automatically

select all control points corresponding to the hues that appear within the selection box. This is a

fast way of selecting all points within a range of colors for uniform manipulation.


Color | Chapter 136 Color Warper

COLOR

Auto Lock Controls

The Auto Lock controls enables DaVinci Resolve to automatically lock a border of control points

surrounding any control point you select and adjust, which makes highly-specific color adjustments

easier to accomplish.

�Auto Lock: Enables and disables this behavior.

�X Points Border: Lets you set how many points away from the control point you’re adjusting the

border of locked control points that restricts your adjustments is. How large an area this ends

up being depends on how many points you choose, and on the resolution of the warping grid.

At higher grid resolutions, the same points distance isolates a smaller region of color.

Smoothing Controls

The smoothing controls let you “ease off” an adjustment you’ve made by progressively moving one or

more selected control points towards their original default position in the warping grid.

�Smooth Chroma: Each click of this button rotates the angle of selected control points around the

circumference of the circular warping grid towards their original position, bringing the hue of the

adjusted colors closer and closer to the original hues of the image. Saturation is unaffected.

�Reset Chroma: Resets the angle of all selected control points to the original hues of those control

points. Saturation adjustments are unaffected.

�Smooth Saturation: Each click of this button moves the position of a control point closer to its

original position relative the center of the circular warping grid, thus bringing the saturation at that

point closer to the original image saturation of the node’s input. Hue is unaffected.

�Reset Saturation: Resets the distance from the center of all selected control points to the original

image saturation at those control points.

�Reset Luma: Resets luma to the original image values.

Chroma – Luma Controls

The Chroma-Luma mode lets you alter the hue and lightness of colors in the image simultaneously.

This may not feel like a particularly intuitive way of working, as the grid controls are overlaid on colors

projected as different sides of an RGB cube. However, this enables some powerful adjustments once

you get the hang of how multiple adjustments interact in this mode, as well as the power of locking

control points to limit your adjustments to specific areas of the two grids.

Whether you’re sampling the image or manipulating the control points of this grid directly, dragging

any point of this grid changes the color of the image corresponding to that point. Vertical adjustments

change lightness, where up makes that part of the image lighter, and down makes that part of the

image darker. Horizontal adjustments change hue, depending on which range of hues are shown in

the two Chroma-Luma warping controls, and which of these you’re adjusting.

By default, only the outer four corners of this control are locked, so any adjustment you make to

any control point pushes and pulls all the other colors throughout the image, depending on your

adjustment. Working this way, multiple adjustments to multiple colors gradually pins different

colors into place, with each adjustment warping the colors falling in between to maintain a smooth

transformation from one adjustment to the next. This can be a good way to make an overall stylistic

adjustment to the image.


Color | Chapter 136 Color Warper

COLOR

The original image

The result of making multiple interacting color adjustments across the entire Chroma Luma grid

Another approach to using this mode is to make more targeted corrections by manually locking

different colors in the image that you don’t want to adjust. You can do this by using the Selection tool

and Shift-clicking any value in the Viewer, or by Shift-clicking any control point on the grid control.

By locking colors you don’t want to change, you can focus on manipulating a more specific range of

colors without altering the entire image.

Alternately, this is where the Auto Lock controls really shine. When you turn these on, you can choose

the type of region you want to affect (vertical column, horizontal row, or a square region), then choose

how large a region of color you want to manipulate (one or two points away from the point that’s

selected). Keep in mind that the current resolution of the warping grid also has an effect on how large

the resulting region of color will be. Lower resolution grids will let you manipulate larger regions of

color, while higher resolution grids will let you adjust a more narrow range of color.

The Auto Lock controls let you make highly targeted

adjustments to specific sections of the warping grid.

Once these controls are enabled, simply clicking once on the image or warping grid selects a control

point and automatically locks off the region of the grid you want to focus your adjustment on. In the

following example, a medium-resolution grid is used in conjunction with the Auto Lock controls set to

lock a 2-point rectangular region. So, clicking on the skin of the woman’s face and dragging adjusts a

section of available reds within the locked-off region of the grid.


Color | Chapter 136 Color Warper

COLOR

Making a targeted color adjustment to a locked-off region of the Chroma Luma grid

The following sections describe how the different tools available in this mode work to let you

manipulate these radial control points in different ways.

Axis Angle

When you’re in Chroma-Luma mode, an additional control appears underneath the warping grids, a

slider named Axis Angle. Dragging this slider to the left or right changes the range of hues in each of

the two warping grids that’s presented, letting you manipulate different ranges of color.

Tools

Each of the available tools let you manipulate control points on the warping grid in different ways when

you click on them.

The Tools buttons

�Grid 1/Grid 2 tabs: Since the Chroma-Luma controls expose two grids representing two different

ranges of hue and luma, these two tabs let you choose which grid will be manipulated when you

sample the image in the Viewer, as well as which grid the Tools controls affect.

�Selection Tool: The default tool mode. Selecting this tool lets you select control points either

individually (by clicking on a single point or command-clicking multiple points) or collectively by

dragging a bounding box over multiple points. You can also Shift-click with this tool to lock points

into place without moving them, and you can right-click on control points to de-select, unlock,

and reset them. This is the most useful tool to use when manipulating the image by clicking and

dragging in the Viewer to sample a color and adjust it at the same time.

�Draw Selection: Selecting this tool lets you make a selection of control points by clicking and

dragging to draw over all the points you want to select. This is good for making large, but specific,

selections of points.

�Pin/De-Pin: Selecting this tool lets you pin multiple control points by either clicking on them or by

clicking and dragging to draw over all the points you want to pin/de-pin.

�Pull Points: Selecting this tool lets you make adjustments by clicking anywhere on the warp grid,

even between points, to pull all neighboring control points towards where you clicked. This can be

used to reduce color contrast within a specific range of colors.

�Push Points: Selecting this tool lets you make adjustments by clicking anywhere on the warp grid,

even between points, to push all neighboring control points within a particular proximity away from

where you clicked. This can be used to increase color contrast within a specific range of colors.


Color | Chapter 136 Color Warper

COLOR