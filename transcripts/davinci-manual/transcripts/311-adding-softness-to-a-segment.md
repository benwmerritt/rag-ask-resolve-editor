---
title: "Adding Softness to a Segment"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 311
---

# Adding Softness to a Segment

The outer shape is drawn using a green dashed line instead of a solid line to help distinguish it from

the inner shape.

To select the outer soft edge shape, do one of the following:

�Use the Tab key to cycle between the onscreen controls until the dashed outline is visible

�Right-click over a spline in the view and choose Controls > Select > Polygon: Outer Polygon.

Once the outer polyline is selected, you can drag any of the points away from the inner polyline to add

some softness to the mask.

TIP: Press Shift-A to select all the points on a shape, and then hold O and drag to offset the

points from the inner shape. This gives you a starting point to edit the falloff.

The farther the outer shape segment is from the inner shape, the larger the falloff will be in that area.

Adding Additional Points to the Shape

It is not necessary for every point on the inner shape to have a match on the outer shape, or vice

versa. You can add additional control points to refine the shape of either shape.

Each polyline stores its animation separately; however, if a point is adjusted on the inner shape that is

parented to a point on the outer shape, a keyframe will be set for both splines. Adjusting a parented

point on the outer shape only sets a keyframe for the outer shape’s spline. If a point that is not parented

is adjusted, it will only set a keyframe on the relevant spline. You can disable this behavior entirely for

this polyline by selecting Polygon: Outer Polygon > Follow Inner Polyline from the contextual menu.

Locking/Unlocking Point Pairs

If you want to parent additional control points, you can select the points, right-click in the viewer, and

choose Lock Point Pairs from the contextual menu for either spline. This will cause the selected point

on the outer shape to become parented to the selected point on the inner shape.

Any animation already applied to either point is preserved when the points become parented.

To unlock a point so it is no longer parented, select the point, right-click in the viewer, and deselect

Lock Point Pairs from the contextual menu.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

Animating Polyline Masks

Animating masks is surprisingly easy. When Polygon or B-Spline masks are added to the Node Editor,

the spline’s control points are automatically ready to be animated. All you have to do to animate a

mask is move the playhead to a new frame and then change the shape of the mask. A new keyframe

is added in the Spline Editor and Timeline Editor. This one keyframe controls the position of all control

points for that mask at that frame. Once two or more keyframes have been created, the shape of the

polygon or B-Spline is automatically interpolated from one keyframe to the next.

TIP: The center point and rotation of a shape are not auto-animated. Only the control points

are automatically animated. To animate the center position or rotation, enable keyframes for

that parameter in the Inspector.

To adjust the overall timing of the mask animation, you edit the Keyframe horizontal position spline

using the Spline Editor or Timeline Editor. Additional points can be added to the mask at any point to

refine the shape as areas of the image become more detailed.

Removing Animation from a Polyline Mask

If you want a Polyline mask to remain static, you can remove the automatic animation setting. In the

Inspector for the mask, right-click in the bottom of the panel where it says Right Click Here For Shape

Animation. From the contextual menu, choose Remove Bézier Spline. If you decide you need to

animate the mask at a later time, right-click in the same area again and choose Animate.

Adding and Removing Points from an Animated Mask

When adding points to an animated mask, the new point is fit into the shape at all keyframes. Deleting

a point removes that point from all keyframes in the animated mask.

Publishing Specific Control Points

Although you can rapidly animate the entire shape of a polyline using a single keyframe, by default the

Spline Editor and Timeline display only one keyframe for the entire shape at any given frame.

This default keyframing behavior is convenient when quickly animating shapes from one form

to another, but it doesn’t allow for specific individual control points that need to be keyframed

independently of all other control points for a particular shape. If you’re working on a complex mask

that would benefit from more precise timing or interpolation of individual control points, you can

expose one or more specific control points on a polyline by publishing them.

Be aware that publishing a control point on a polyline removes that point from the standard animation

spline. From that point forward, that control point can only be animated via its own keyframes on its

own animation spline. Once removed, this point will not be connected to paths, modifiers, expressions,

or trackers that are connected to the main polyline spline.

To publish a selected point or points, do one of the following:

�Click on the Publish Points button in the Polyline toolbar.

�Select Publish Points from the Polyline’s contextual menu.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

A new coordinate control is added to the Polyline mask controls for each published point, named

Point 0, Point 1, and so on.

The Publish Points controls in the Inspector

The onscreen control indicates published points on the polyline by drawing that control point

much larger. Once a published point is created, it can be connected to a tracker, path, expression,

or modifier by right-clicking on this control and selecting the desired option from the point’s

contextual menu.

The published point in the viewer

Using “Publish to Path” to Preserve Animation

When a point is published, any animation already applied to that point is removed. However, if you

need to keep the animation, you can use the “Publish to Path” option. This Polyline contextual menu

option publishes the selected points and converts their existing animation to a path. You can also use

the Publish to Path button in the Polyline toolbar.

Using “Follow Published Points” to Add Points

There are times when you will need to have control points that lie between two other published

points follow the motion of the published points, while still maintaining their relative offset and shape.

For this reason, points in a Polyline mask can be set to “Follow Published Points” using the Polyline’s

contextual menu.

When a point of an effect mask is set to follow points, the point will be drawn as a diamond shape

rather than a small box.

A control point set to Follow Published Points

When this mode is enabled, the new “following” control points will maintain their position relative

to the motion of any published points in the mask, while attempting to maintain the shape of that

segment of the mask. Unlike published points, the position of the following points can still be animated

to allow for morphing of that segment’s shape over time.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

Chapter 81

Paint

This chapter describes how to use Fusion’s non-destructive Paint tool to repair

images, remove objects, and add creative elements.

Contents

Paint Overview������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1697

Types of Paint Nodes����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1697

Setting Up the Paint Node ����������������������������������������������������������������������������������������������������������������������������������������������������������� 1698

Setting the Paint Node’s Resolution ����������������������������������������������������������������������������������������������������������������������������������������� 1698

Paint Node Workflow����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1699

Select the Correct Paint Stroke Type���������������������������������������������������������������������������������������������������������������������������������������� 1699

Setting the Brush Size ��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1702

Choosing an Apply Mode �������������������������������������������������������������������������������������������������������������������������������������������������������������� 1702

Editing Paint Strokes������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1706

Editing Paint Strokes in the Modifiers Tab����������������������������������������������������������������������������������������������������������������������������� 1707

Deleting Strokes ���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1707

Animating and Tracking Paint Strokes������������������������������������������������������������������������������������������������������������������������������������ 1708

Animating with Write-On Controls���������������������������������������������������������������������������������������������������������������������������������������������� 1708

Tracking a Paint Stroke�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1708

Using the Planar Tracker with the Paint Tool���������������������������������������������������������������������������������������������������������������������������� 1711

Inverting the Steady Effect to Put the Motion Back In�������������������������������������������������������������������������������������������������������� 1717

Painting a Clean Plate ����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1719


Fusion Fundamentals | Chapter 81 Paint

FUSION

Paint Overview

The Paint node is a procedural paint tool, which means that each paint stroke is a live, editable object

that’s drawn with properties that you can mix and match to address a wide variety of painting tasks.

You can use it to paint masks, retouch images, perform beauty work, clone out objects, or even create

motion graphics. Each element of a paint stroke can be altered long after you apply it. Since strokes

are editable, you can apply, change, ignore, delete, and even reorder them in a node tree.

Types of Paint Nodes

There are two types of paint nodes in Fusion. The Paint node is a full-featured creative and retouch

vector-based paint tool that requires an input on which to paint. The Mask Paint node lets you

specifically paint an alpha channel to limit the area of an effect. It allows you to create paint strokes on

an alpha channel without needing to have an input.

�The Paint node is located in the Paint category of the Effects Library.

�The Mask Paint node is located in the Mask category of the Effects Library.

The main difference between these two Paint tools is that the Mask Paint tool only paints on the Alpha

channel, so there are no channel selector buttons. The Paint tool can paint on any or all channels.

The majority of this chapter covers the Paint node, since it shares identical parameters and settings

with the Mask Paint node.

The Paint node available in the Paint category of the Effects Library


Fusion Fundamentals | Chapter 81 Paint

FUSION