---
title: "Chroma Warp Stroke"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 563
---

# Chroma Warp Stroke

The Chroma Warp stroke tools modify and refine any selection you’ve made.

�Chroma Range: Adjust this slider to set the amount of adjacent colors included in the range.

Lower ranges make the color selection more specific, while higher ranges encompass more of the

adjacent colors.

�Exposure: Adjusting this slider darkens or brightens the selection in the ending circle only

(the orange dot). Negative values darken, while positive values brighten.

�Tonal Range Low: Adjusting this slider lets you primarily affect the darker regions of the initially

selected color for change, leaving the brighter regions unchanged. This adjustment is global and

applies to all strokes in the chromaticity diagram.

�Tonal Range High: Adjusting this slider lets you primarily affect the brighter regions of the initially

selected color for change, leaving the darker regions unchanged. This adjustment is global and

applies to all strokes in the chromaticity diagram.

�Tonal Range Pivot: This slider lets you set the initial point between Tonal Range Low and Tonal

Range High that those tools diverge from.

�Normal/Point to Point Toggle: Clicking on either of these icons changes a Normal selection to a

Point to Point or vice versa.

Hue-Saturation/Chroma-Luma Mode

The Color Warper Hue-Saturation and Chroma-Luma palettes are a mesh-based warping tool that,

instead of warping the spatial location of pixels, warps one set of colors into another. Better yet, unlike

the HSL curves, they let you simultaneously adjust two color parameters at the same time, within user-

selectable regions of specific hues. These adjustments, made using a grid of draggable control points,

automatically have a smooth falloff from the colors you’re warping to other colors that are locked into

place. The smoothness of this falloff depends on the distance between the warp points that are being

adjusted and other warp points that are locked in place to prevent change.

The Color Warper, located in the center palette area

There are two ways you can use this tool. You can drag the control points in the grid to make highly

specific image adjustments. More intuitively, you can click to sample the image, which selects the

closest grid point that affects that color, and then drag to make an adjustment with that control point.


Color | Chapter 136 Color Warper

COLOR

Clicking and dragging to sample skin tone in the Viewer to adjust that

color’s control point on the Hue-Saturation warping grid

You can use this tool to make extremely specific adjustments to colors in an image, similar to what

you might do with a Qualifier key or with the HSL curves. However, by warping the points using a grid,

you can manipulate two color characteristics at the same time, adjusting both hue and saturation,

or chroma and luma. In the following example, specific adjustments are being made to refine the

woman’s shirt, to adjust her skin tone, and to manipulate the greens of the foliage in the shot. All three

of these naturalistic adjustments are smooth and artifact-free by virtue of the Color Warper’s method

of cleanly remapping color.

(Top) The original image, (Bottom) Manipulating the hue and saturation of the grass using the Chroma-Luma controls

You can also use this tool to create wide-ranging stylistic looks for the overall image, bending the color

in creative ways that other controls don’t. In the following image, the less saturated and neutral colors

of the image are all warped towards a bluish-cyan, while the more saturated oranges are warped

towards a saturated orange-red, to quickly create a stylistic treatment of the image.


Color | Chapter 136 Color Warper

COLOR

(Top) The original image, (Bottom) Stylizing the overall image using the Hue-Saturation controls

The Color Warper Interface

You can either use the Color Warper as it appears docked into the middle palette area, or you can

click the Expand button to open the Color Warper into a floating window that you can make as large

as you like, giving you more detailed control of dense grids of control points. For convenience, the

examples in this chapter show the Color Warper side-by-side with the Viewer, in a floating window.

While the Color Warper is open in its own window, clicking the Close button puts the palette back in

the palette area below.

Clicking the Expand button opens the

Color Warper into a floating window,

clicking the Close button in the floating

window puts the palette back.

There are two overall regions of the Color Warper palette. At the left, the grid area has the actual

warping grid with points you manipulate to make adjustments, while controls underneath let you

choose the resolution of the grid and the color space in which it works. At the right, the control area

provides all the tools, range controls, and feathering controls that are available for manipulating the

warping grid in a variety of highly specific ways.


Color | Chapter 136 Color Warper

COLOR

Using the Grid Controls to Manipulate Color

This palette has two modes; each lets you manipulate the colors of the image in different ways, and

each has a different style of grid used for warping the different color channels that are affected.

Learning how to manipulate the color warping points of each of these grids is central to understanding

how this palette works.

(Left) The radial grid in Hue-Saturation mode,

(Right) The two rectangular grids in Chroma-Luma mode

Dragging to Warp Colors

Despite the different shapes, each of these grids are manipulated in similar ways. Dragging a control

point alters whatever color corresponds to that point, while the colors that surround this dragged point

are also adjusted proportionally according to their location between the point being dragged and

surrounding points that either (a) aren’t affected, or (b) are locked into place. Locked points prevent the

colors at those points from being changed. By locking some parts of a grid and dragging other parts,

you can create sophisticated hue-specific adjustments.

The orange control point has

been selected and dragged

to make an adjustment.

Control points with black outlines

are locked in place and help

prevent control points on the

opposite side from being moved.

All other control points between

the selected and locked

control points are stretched or

squished depending on the

selected point’s adjustment.


Color | Chapter 136 Color Warper

COLOR

The image above shows the three states of control points in the grid:

�Orange: Selected points appear orange. You can select multiple points by Command-clicking

multiple points, by dragging a bounding box over multiple points, or by using the draw selection

tool to click and draw over any points you want to select. Once you’ve selected and moved a

control point, it becomes locked to keep that adjustment in place.

Selected points appear

orange; in this example

four points are selected to

move them all together.

�Outlined: White control points with a black outline are locked. Locked points do not move

automatically when nearby points are dragged, so locked points are important for preventing

specific colors you don’t want altered from being changed, as well as for saving changes to points

that you’ve adjusted. All adjusted points become locked. The outer corners of the Chroma-Luma

grid are locked, as is the outer ring and center point of the Hue-Saturation web.

Locked points with black

outlines keeping other

colors in the image from being

adjusted by the selected point

�White: White control points are neither selected nor locked, and will be stretched or squished

when adjacent control points are moved.

Unlocked control points

between a selected point and

locked points (in this case the

corners of the grid) will squish

and stretch to warp an entire

range of color as you drag.


Color | Chapter 136 Color Warper

COLOR

While control points work much the same in either the Hue-Saturation or Choma-Luma modes,

there are some important differences. The radial “spokes” of the Hue-Saturation wheel don’t

influence neighboring spokes, so any adjustment you make to a control point on one spoke only

affects the colors that fall between it and the two neighboring spokes that surround it. This means

it’s not necessary to lock control points on neighboring spokes of this wheel-shaped grid to

prevent them from changing.

Adjustments made to control

points on one “spoke” of the

Hue-Saturation wheel grid don’t

affect those on neighboring

spokes, which act as if they’re

locked, even though they’re not.

Both the Hue-Saturation and Chroma-Luma warper grids lock the outer boundary of the grid.

You can still drag these points to adjust them, but they can’t be unlocked and they won’t

move automatically when you adjust other control points. The Hue-Saturation grid has an

additional point locked right in the center, which keeps the neutral colors (black through gray

and white) neutral.

TIP: Dragging the locked center point of the Hue-Saturation grid lets you alter the color

of the white point, while proportionally warping all other colors in the image to smoothly

accommodate this change. This can be the starting point of a lot of different looks.