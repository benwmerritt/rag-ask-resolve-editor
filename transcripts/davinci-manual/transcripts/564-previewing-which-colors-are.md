---
title: "Previewing Which Colors Are"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 564
---

# Previewing Which Colors Are

Warped By Each Control Point

If you press and hold the Option key while you click on a control point in the warp grid, you get a

preview in the Viewer of which colors that control point will affect. Affected pixels appear in color

against black, which represents all pixels that will remain unaffected by that control point.

Holding the Option key down while clicking a Color Warper control point

shows a preview of affected pixels against black.


Color | Chapter 136 Color Warper

COLOR

Sampling to Warp Colors

While it’s important to learn how control points in the grid are manipulated, the most intuitive way of

working with this control is to use the pointer to click within the Viewer to sample a color you want to

adjust, hold the pointer button down, and then drag to adjust the color.

When moving the pointer in the Viewer, you’ll see a crosshairs moving around the warping grid that

shows you the exact color on the vectorscope graph, while a yellow box indicates the control point

that’s closest to the color you’re sampling that will be selected if you click. In the following example,

positioning the eyedropper over the sky shows that clicking will select a control point close to the

center of the grid.

Moving the pointer in the Viewer shows a preview in the warping grid

of which control point you’ll select were you to click.

Clicking and dragging selects and then moves the control point corresponding to that color in the

Viewer. As you drag the pointer, you’ll see the selected control point move in the same direction as

the mouse while the colors of the image update in real time to show the adjustment you’re making.

Meanwhile, an arrow in the grid shows you the delta of the current adjustment. Moving a selected

control point to another hue in the grid warps the original color to the new color.

Clicking and dragging moves the control point corresponding to that color

in the grid to adjust the color and locks it into place.

You can also lock control points by sampling the image. Hold the Command and Shift keys down, and

then click on the color or colors you want to lock in the warp grid to prevent them from being changed.

This makes it easy to work directly in the Viewer to lock colors you don’t want to change, before

adjusting other colors that you do want to change.

In the following example, Command-Shift-clicking on the woman’s shoulder locks the yellowish

highlights falling on her uniform in place. Then, clicking and dragging a highlight on her face lets us

push the highlights towards teal without losing the warmer highlights on her shoulder, all by sampling

directly in the Viewer.


Color | Chapter 136 Color Warper

COLOR

(Top) Command-Shift-clicking to lock the closest control point to a color on the warping grid you don’t want to change,

(Bottom) Warping a neighboring color while the control point you just locked keeps that part of the image from changing

Resetting Grid Points

If, at any point, you adjust a point that you want to reset, simply right-click on that point to de-lock

and reset it.

Grid Resolution Affects The Specificity

and Quality of Adjustments

You can change the resolution of the grids in either Hue-Saturation or Chroma-Luma modes, using

the controls at the bottom of the Color Warper palette, underneath the grid itself. Separate drop-down

menus let you choose the resolution of control points for hue and saturation, or for chroma and luma

separately, although by default they’re linked together.

The two resolution controls found underneath the grid controls

By default, the Hue-Saturation grid has a resolution of 6x6, which is the lowest resolution available.

The Chroma-Luma grid defaults to 6x6, but can be set lower, to 4x4. Low resolution warping grids

make it easy to create broad color adjustments affecting large ranges of analogous color with

smooth results. Additionally, lower quality media that’s 8-bit, with 4:2:0 chroma subsampling, and/

or highly compressed benefits from lower resolution warping grids to avoid artifacts and keep color

adjustments smooth.


Color | Chapter 136 Color Warper

COLOR

(Left) The Hue-Saturation grid set to a resolution of 6x6,

(Right) The Hue-Saturation grid set to a resolution of 24x16

On the other hand, higher resolution grids let you make more specific adjustments to tighter ranges

of color. However, this approach is more useful in projects using high quality media (10- or 12-bit, 4:2:2

or 4:4:4 chroma subsampling, and minimally compressed) to avoid unwanted artifacts. If you’re using

high-quality media, you’ll find you can use the Color Warper to make incredibly specific adjustments.

You can set the default Hue and Saturation grid resolutions in the Color Warper’s Option menu by

choosing Default Hue Resolution or Default Saturation Resolution and selecting your preferred

resolution from the drop-down menu.

The Chroma-Luma grid set to a resolution of 6x6


Color | Chapter 136 Color Warper

COLOR

The Chroma-Luma grid set to a resolution of 24x24

NOTE: If you make adjustments with the grid at one resolution, it’s possible to change the

grid to a higher or lower resolution, and your adjustment will be interpolated to fit the new

grid resolution, although the resulting adjustment may change a bit.

You Can Warp Color in Different Color Spaces

A drop-down menu at the bottom right of the warping grid lets you choose which color space to use

for manipulating the colors of the image. Different color spaces project the colors of the image into

the two-dimensional warping grid in different ways, and some may make it easier to manipulate a

particular image in the way you want by spreading out different ranges of color more widely.

The color space found underneath the grid controls

The available color spaces are:

•	 HSV

•	 HSL

•	 HSY

•	 HSP


Color | Chapter 136 Color Warper

COLOR