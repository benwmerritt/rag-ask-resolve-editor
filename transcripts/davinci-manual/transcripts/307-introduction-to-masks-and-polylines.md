---
title: "Introduction to Masks and Polylines"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 307
---

# Introduction to Masks and Polylines

Polylines are splines that are used whenever a control is animated with a motion path or when a

node’s effect is masked with a drawn shape. They are also used in the Paint and Grid Warp nodes. In

a more basic form, polylines are used to control the animation in the Spline Editor. Since these splines

are used for just about everything, they are extremely flexible, with a considerable amount of controls,

modes, and options. This chapter offers an overview of polylines and their operation, with specific

information on how to use them for masks.

Mask Nodes

Mask nodes create an image that is used to define transparency in another image. Unlike other image

creation nodes in Fusion, mask nodes create a single channel image rather than a full RGBA image.

The most used mask tool, the Polygon mask tool, is located in the toolbar.

For more information on these mask tools, see Chapter 108, “Mask Nodes,” in the

DaVinci Resolve Reference Manual or Chapter 48 in the Fusion Reference Manual.

Editing Bézier Handles��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1688

Point Editor��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1688

Reduce Points��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1689

Shape Box���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1689

Showing and Hiding Onscreen Polyline Controls�������������������������������������������������������������������������������������������������������������� 1690

Stop Rendering������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1691

Roto Assist����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1691

Creating Softness Using Double Polylines���������������������������������������������������������������������������������������������������������������������������� 1691

Converting a Single Polyline to a Double Polyline ������������������������������������������������������������������������������������������������������������ 1692

Adding Softness to a Segment���������������������������������������������������������������������������������������������������������������������������������������������������� 1693

Adding Additional Points to the Shape������������������������������������������������������������������������������������������������������������������������������������ 1693

Locking/Unlocking Point Pairs����������������������������������������������������������������������������������������������������������������������������������������������������� 1693

Animating Polyline Masks������������������������������������������������������������������������������������������������������������������������������������������������������������� 1694

Removing Animation from a Polyline Mask���������������������������������������������������������������������������������������������������������������������������� 1694

Adding and Removing Points from an Animated Mask���������������������������������������������������������������������������������������������������� 1694

Publishing Specific Control Points��������������������������������������������������������������������������������������������������������������������������������������������� 1694


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

The available nodes in the Mask bin of the Effects Library

Polygon Mask

Polygon masks are user-created Bézier shapes. This is the most common type of polyline and the

basic workhorse of rotoscoping. Polygon mask tools are automatically set to animate as soon as you

add them to the Node Editor.

B-Spline Masks

B-Spline masks are user-created shapes made with polylines that are drawn using the B-Splines.

They behave identically to polyline shapes when linear, but when smoothed the control points

influence the shape through tension and weight. This generally produces smoother shapes while

requiring fewer control points. B-Spline mask tools are automatically set to animate as soon as you add

them to the Node Editor.

Bitmap Masks

The Bitmap mask allows images from the Node Editor to act as masks for nodes and effects. Bitmap

masks can be based on values from any of the color, alpha, hue, saturation, luminance, and the

auxiliary coverage channels of the image. The mask can also be created from the Object or Material ID

channels contained in certain 3D-rendered image formats.

Mask Paint

Mask Paint allows a mask to be painted using Fusion’s built-in vector paint nodes.

Wand Mask

A Wand mask provides a crosshair that can be positioned in the image. The color of the pixel under

the crosshair is used to create a mask, where every contiguous pixel of a similar color is also included

in the mask. This type of mask is ideal for isolating color adjustments.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

Ellipse, Rectangle, and Triangle Masks

These are primitive shape masks.

For more information on these mask tools, see Chapter 108, “Mask Nodes,” in the

DaVinci Resolve Reference Manual or Chapter 48 in the Fusion Reference Manual.

Ranges Mask

Similar to the Bitmap mask, the Ranges mask allows images from the Node Editor to act as masks for

nodes and effects. Instead of creating a simple luminance-based mask from a given channel, Ranges

allows spline-based selection of low, mid, and high ranges, similar to to the Color Corrector node.

Polyline Types

You can draw polylines using either B-Spline or Bézier spline types. Which you choose depends on

the shape you want to make and your comfort with each spline style.

Bézier Polylines

Bézier polylines are shapes composed of control points and handles. Several points together are used

to form the overall shape of a polyline.

Bézier control point with direction handles

extended to create a smooth curve

Each control point has a pair of handles used to define the exact shape of the polyline segments

passing through each control point. Adjusting the angle or length of the direction handles will affect

whether that segment of the polyline is smooth or linear.

Bézier control point with direction handles

aligned to create a linear segment

If you’re familiar with applications such as Adobe Photoshop or Illustrator, you’ll already be familiar with

many of the basic concepts of editing Bézier polylines.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

B-Spline Polylines

A B-Spline polyline is similar to a Bézier spline; however, these polylines excel at creating smooth

shapes. Instead of using a control point and direction handles for smoothness, the B-Spline polyline

uses points without direction handles to define a bounding box for the shape. The smoothness of the

polyline is determined by the tension of the point, which can be adjusted as needed.

B-Splines excel at creating smooth curves

Converting Polylines from One Type to Another

Just because you created a shape using a B-Spline or polyline, that doesn’t mean you’re stuck with

the controls you started with. You can convert any shape from B-Spline to Bézier, or Bézier to B-Spline,

as needed.

To switch a shape between Polyline and B-Spline controls:

Right-click a shape in the viewer and choose Convert Bézier Spline to B-Spline or

Convert B-Spline to Bézier from the spline’s contextual menu (only the appropriate option

will be displayed).

When converting from one type to another, the original shape is preserved. The new polyline

generally has twice as many control points as the original shape to ensure the minimum

change to the shape. While animation is also preserved, this conversion process will not

always yield perfect results. It’s a good idea to review the animation after you convert

spline types.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

How to Use Masks with Other Nodes

Typically, a node applies its effect to every pixel of an image. However, many nodes have mask inputs

that can be used to limit the effect that node has on the image.

A Blur node with a Polygon

node masking its effect

Masks are single-channel images that can be used to define which regions of an image you want to

affect. Masks can be created using primitive shapes (such as circles and rectangles), complex polyline

shapes that are useful for rotoscoping, or by extracting channels from another image.

A Polygon node’s mask seen in the viewer

Each mask node is capable of creating a single shape. However, Mask nodes are designed to be

added one after the other, so you can combine multiple masks of different kinds to create complex

shapes. For example, two masks can be subtracted from a third mask to cut holes into the resulting

mask channel.

Fusion offers several different ways you can use masks to accomplish different tasks. You can attach

Mask nodes after other nodes in which you want to create transparency, or you can attach Mask nodes

directly to the specialized inputs of other nodes to limit or create different kinds of effects.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION