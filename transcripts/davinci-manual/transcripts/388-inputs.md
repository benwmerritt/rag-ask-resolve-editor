---
title: "Inputs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 388
---

# Inputs

The Gamut node includes two inputs: one for the main image and the other for an effect mask to limit

the conversion area.

Input: This orange input is the only required connection. It connects a 2D image output that is the

source of the gamut conversion.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

Gamut operation to only those pixels within the mask. An effect mask is applied to the tool after the

tool is processed.

Basic Node Setup

A Gamut node is most often placed directly after the MediaIn node in DaVinci Resolve or a Loader

node in Fusion Studio. Another Gamut node is usually placed at the end of a node tree before a

MediaOut node in DaVinci Resolve or a Saver node in Fusion Studio.

A Gamut node applied to a MediaIn1 node

Inspector

Gamut controls


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Controls Tab

The Controls tab is where all the conversion operations take place. It has a section for incoming

images and a section for the node’s output. Which section you use depends on whether you are

stripping an image of a gamma curve to make it linear or converting a linear image to a specific color

space and gamma curve for output.

Source Space

Source Space determines the input color space of the image. When placed directly after a Loader

node in Fusion or a MediaIn node in DaVinci Resolve, you would select the applicable color space

based on how the image was created and check the Remove Gamma checkbox. The output of the

node would be a linearized image. You leave this setting at No Change when you are adding gamma

using the Output Space control and placing the node directly before the Saver node in Fusion or a

MediaOut node in DaVinci Resolve.

DCI-P3

The DCI-P3 color space is most commonly used in association with DLP projectors. It is frequently

provided as a color space available with DLP projectors and as an emulation mode for 10-bit LCD

monitors such as the HP Dreamcolor and Apple’s Pro Display XDR. This color space is defined in the

SMPTE-431-2 standard.

Custom

The Custom gamut allows you to describe the color space according to CIE 1931 primaries and white

point, which are expressed as XY coordinates, as well as by gamma, limit, and slope. For example,

the DCI-P3 gamut mentioned above would have the following values if described as a Custom

color space.

Red Primary

0.68

0.32

Green Primary

0.265

0.69

Blue Primary

0.15

0.06

White Point

0.314

0.351

Gamma

2.6

–

Linear Limit

0.0313

–

To understand how these controls work, you could view the node attached to a gradient background

in Waveform mode and observe how different adjustments modify the output.

Output Space

Output Space converts the gamut to the desired color space. For instance, when working with

linearized images in a composite, you place the Gamut node just before the Saver node and use the

Output Space to convert to the gamut of your final output file. You leave this setting at No Change

when you want to remove gamma using the Source Space control.

NOTE: When outputting to HD specification Rec. 709, Fusion uses the term Scene to refer to

a gamma of 2.4 and the term Display for a gamma of 2.2.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Remove/Add Gamma

Select these checkboxes to do the gamut conversion in a linear or nonlinear gamma, or simply remove

or add the applicable gamma values without changing the color space.

Pre-Divide/Post-Multiply

Selecting this checkbox causes the image’s pixel values to be divided by the Alpha values prior to

the color correction, and then re-multiplied by the Alpha value after the correction. This helps to avoid

the creation of illegally additive images, particularly around the edges of a blue/green key or when

working with 3D-rendered objects.

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Hue Curves [HCv]

The Hue Curves node

Hue Curves Node Introduction

The Hue Curves node allows you to adjust the color in an image using a series of spline curves.

Splines are provided to control the image’s hue, saturation, and luminance as well as each individual

color channel. An additional set of curves allows you to apply suppression to individual color channels.

The advantage of the Hue Curves node over other color correction nodes in Fusion is that the splines

can be manipulated to restrict the node’s effect to a very narrow portion of the image, or expanded

to include a wide-ranging portion of the image. Additionally, these curves can be animated to follow

changes in the image over time. Since the primary axis of the spline is defined by the image’s hue, it is

much easier to isolate a specific color from the image for adjustment.

Inputs

The Hue Curves node includes two inputs: one for the main image and the other for an effect mask to

limit the color correction area.

Input: This orange input is the only required connection. It connects a 2D image for the Hue Curves

color correction.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

Hue Curves operation to only those pixels within the mask. An effect mask is applied to the tool after it

is processed.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Basic Node Setup

The Hue Curves node, like many 2D image-processing nodes, receives a 2D image like a Loader

node or the MediaIn1 shown below. The output continues the node tree by connecting to another 2D

image-processing node or a Merge node.

A Hue Curves node applied to a Loader node in Fusion Studio

Inspector

Hue Curves controls

Controls Tab

The Controls tab consists of color attribute checkboxes that determine which splines are displayed

in the Spline window. The spline graph runs horizontally across with control points placed

horizontally at each of the primary colors. You can manipulate these control points to change the

selected color attribute.

Mode

The Mode options change between No Animation and Animated Points modes. The default mode is

No Animation, where adjustments to the curves are applied consistently over time. Setting the Mode

to Animated Points or Dissolve allows the color curve to be animated over time.

Dissolve mode is essentially obsolete and is included for compatibility reasons only.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Color Channel Checkboxes

These checkboxes define which splines are editable and are included when using the Eyedropper to

pick a color in the image.

Any number of activated splines can be edited simultaneously; however it’s more convenient to have

only the currently modified spline active to avoid unwanted changes to other splines.

When using the Eyedropper icon, a point is created on all active splines, representing the

selected color.

Spline Window

This graph display is the main interface element of the Hue Curves node, which hosts the various

splines. In appearance, the node is very similar to the Color Curves node, but here the horizontal axis

represents the image’s hue, while the vertical axis represents the degree of adjustment. The Spline

window shows the curves for the individual channels. It is a miniature Spline Editor. In fact, the curves

shown in this window can also be found and edited in the Spline Editor.

The spline curves for all components are initially flat, with control points placed horizontally at each of

the primary colors. From left to right, these are: Red, Yellow, Green, Cyan, Blue, and Magenta. Because

of the cyclical design of the hue gradient, the leftmost control point in each curve is connected to the

rightmost control point of the curve.

Right-clicking in the graph displays a contextual menu containing options for resetting the curves,

importing external curves, adjusting the smoothness of the selected control points, and more.

In and Out

Use the In and Out controls to manipulate the precise values of a selected point. To change a value,

select a point and enter the In/Out values desired.

Eyedropper

Left-clicking and dragging from the Eyedropper icon changes the current mouse cursor to an

Eyedropper. While still holding down the mouse button, drag the cursor to a viewer to pick a pixel

from a displayed image. This causes control points, which are locked on the horizontal axis, to appear

on the currently active curves. The control points represent the position of the selected color on the

curve. Use the contextual menu’s Lock Selected Points toggle to unlock points and restore the option

of horizontal movement.

Points are only added to enabled splines. To add points only on a specific channel, disable the other

channels before making the selection.

Pre-Divide/Post-Multiply

Selecting this checkbox causes the image’s pixel values to be divided by the Alpha values prior to the

color correction, and then re-multiplied by the Alpha value after the correction. This helps when color

correcting images that include a premultiplied Alpha channel.

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION