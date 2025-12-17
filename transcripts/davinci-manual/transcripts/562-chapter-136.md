---
title: "Chapter 136"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 562
---

# Chapter 136

Color Warper

The Color Warper is a powerful toolset for making both highly specific

adjustments to particular things in the frame, and widely general adjustments

to create unique looks.

The two modes of the Color Warper each make it easy to change hues using the Chroma Warp,

or simultaneously modify two different color attributes, either saturation and hue, or lightness and

hue. This gives the Color Warper an advantage over curves, which only let you adjust one color

characteristic at a time.

Contents

Introduction to the Color Warper����������������������������������������������������������������������������������������������������������������������������������������������� 3136

Chroma Warp���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3136

Using The Chroma Warp in Normal Mode������������������������������������������������������������������������������������������������������������������������������� 3137

Using The Chroma Warp in Point to Point Mode����������������������������������������������������������������������������������������������������������������� 3138

Pin Points������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3139

Chroma Warp Tools��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3139

Chroma Warp Stroke������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3140

Hue-Saturation/Chroma-Luma Mode�������������������������������������������������������������������������������������������������������������������������������������� 3140

The Color Warper Interface���������������������������������������������������������������������������������������������������������������������������������������������������������� 3142

Using the Grid Controls to Manipulate Color������������������������������������������������������������������������������������������������������������������������ 3143

Previewing Which Colors Are Warped By Each Control Point����������������������������������������������������������������������������������� 3145

Sampling to Warp Colors���������������������������������������������������������������������������������������������������������������������������������������������������������������� 3146

Resetting Grid Points������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3147

Grid Resolution Affects The Specificity and Quality of Adjustments������������������������������������������������������������������������� 3147

You Can Warp Color in Different Color Spaces������������������������������������������������������������������������������������������������������������������� 3149

Hue – Saturation Controls������������������������������������������������������������������������������������������������������������������������������������������������������������� 3150

Tools���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3150

Modifiers��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3151

Range��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3151

Auto Lock Controls����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3152

Smoothing Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3152


Color | Chapter 136 Color Warper

COLOR

Introduction to the Color Warper

The Color Warper consists of two modes: Chroma Warp, and Hue-Saturation, Chroma-Luma.  Both

modes are designed to warp one set of colors into another with a smooth falloff that might be difficult

to achieve with qualifiers alone. However, for each node, you must choose between using the Chroma

Warp, or the Hue-Saturation and Chroma-Luma controls.

Chroma Warp

The Chroma Warp is a mode found in the Color Warper palette. Like the Color Warper hue-sat/chroma-

luma controls, its purpose is to make smooth and precise changes between color ranges. The main

difference is that the Chroma Warp uses strokes on a chromaticity diagram rather than adjusting the

points on a mesh to make its changes. Both will give you great results, but you can only use one of

these tools per node, either the traditional Color Warper or the Chroma Warp.

The Chroma Warp chromaticity diagram on the left and toolset to the right

The main interface of the Chroma Warp contains a chromaticity diagram with the range of the current

colors in the image overlayed on top in white (similar to a vectorscope representation), with the toolset

to the left. The chromaticity diagram is perceptionally uniform, meaning that the distances between

points on the diagram closely align to the visual differences seen in the image when using the

Chroma Warp. The Chroma Warp is exposure independent, meaning once you’ve set a Chroma Warp,

subsequent changes in luminance will not break your qualified selection.

The first decision to make is whether you want to use the Chroma Warp in Normal or Point to

Point modes.

Chroma – Luma Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3152

Axis Angle���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3154

Tools���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3154

Modifiers�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3155

Range�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3155

Auto Lock Controls����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3156

Smoothing Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3156


Color | Chapter 136 Color Warper

COLOR

Using The Chroma Warp in Normal Mode

Use this mode when you want to naturally transition from one color to another through the entire color

range that lies between them, for example changing the color of an entire sky to a deeper blue.

Select the color range you want to modify by:

�Clicking the original color using the qualifier eyedropper in the Viewer, then dragging towards the

direction of the new color in the chromaticity diagram. The Viewer will update as you drag through

the color ranges, allowing you to easily dial in the exact change you want.

�Clicking on the color representation inside the chromaticity diagram itself, then dragging towards

the color you wish to change it to.

In either case, the initial color selected will be represented by a blue dot on the chromaticity diagram,

and the final color will be represented by an orange dot. They will be connected by an arrow showing

the range of change. An orange outline around the vector shows the entire range of colors modified.

Dragging the points toward the white point (the small circle in the diagram) will desaturate the color,

while dragging it toward the edges will increase a color’s saturation.

The Chroma Warp in Normal mode, changing both the tonal range of the

grass to more yellow and the sky range to deeper blue.


Color | Chapter 136 Color Warper

COLOR

Using The Chroma Warp in Point to Point Mode

Use this mode to isolate and change a specific color to another color entirely, for example changing

the color of a shirt from blue to yellow without going through green.

Select the specific color you want to modify by:

�Clicking the original color using the qualifier eyedropper in the Viewer, then dragging towards the

direction of the new color in the chromaticity diagram. The Viewer will update as you drag through

the colors, allowing you to easily dial in the exact destination color you want.

�Clicking on the color representation inside the chromaticity diagram itself, then dragging towards

the color you wish to change it to.

In either case, the initial color selected will be represented by a blue dot on the chromaticity diagram,

and the final color will be represented by an orange dot. They will be connected by an arrow showing

the range of change. An orange outline around both dots shows the selection range of the original

and final colors.

Dragging the points toward the white point (the small circle in the diagram) will desaturate the color,

while dragging it toward the edges will increase a color’s saturation.

The Chroma Warp in Point to Point mode, changing just the color of the shirt from blue to yellow.

TIP: You can use multiple Normal and Point to Point selections concurrently for very

advanced color changes within the same node.


Color | Chapter 136 Color Warper

COLOR

Pin Points

This tool allows you to set a pin designating a color range to be excluded from the selected range. For

example, if you wanted to change the color of a sign from red to green, but it had yellow lettering that

fell into the range between, you could add a pin point to the yellow text to exclude it from the color

change. Another use case would be to put a pin point on the skin tones of an actor so that their skin

remained the same regardless of the color changes happening around it.

You can set a pin point just like the selection above, either by using the qualifier on a color in the

image itself in the Viewer, or by clicking on the color in the chromaticity diagram.

Placing a Pin Point around the white point to keep neutral

tones from tinting during a Chroma Warp operation

TIP: If using the tool is causing tinting issues, try placing a Pin Point on the white point

of the chromaticity diagram (the center circle). This will remove all neutral grays from the

color adjustment.

The Chroma Warp tools

Chroma Warp Tools

The Chroma Warp toolset are where you access the main color selection parameters of the Warp.

�Add Stroke (Normal): This puts the Chroma Warp in Normal mode to select a color range.

�Add Stroke (Point to Point): This puts the Chroma Warp in Point to Point mode to select a

specific color.

�Add Pin Point: This allows you to set a pin designating a color to be excluded from the

selected range.

�Select: Lets you click on an existing range and drag it around the chromaticity diagram.

�Delete Strokes or Points: This lets you delete specific strokes and points you have already set on

the Chroma Warp. Simply click on one of the points of a range, then click on the trashcan icon.


Color | Chapter 136 Color Warper

COLOR