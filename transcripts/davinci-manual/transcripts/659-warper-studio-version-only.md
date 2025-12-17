---
title: "Warper (Studio Version Only)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 659
---

# Warper (Studio Version Only)

The Warper is a free-form image warper that uses points or curves to push and stretch features in an

image as if they were on a sheet of rubber. While the Warper has a lot of options and settings, getting

started is really easy.

Warp Mode Points

To warp a feature of the image, just select Points as the Warp mode, click anywhere in the image

to add a warp point, and drag to push that part of the image in the direction you want it to go. Warp

points are gray. By default, warp points influence the entire image, which is pinned down at the

corners. This system makes it simple to warp large regions of the image, such as when you want to

warp an edge of the image to get rid of a boom dip.

(Left) The original image, (Right) The image warped with a single control point

To “pin down” parts of the image you don’t want to warp, Shift-click to place limiter points (which are

red). By combining warp points with limiter points, you can quickly create extremely specific warp

effects to squish and stretch features in an image in any way you want.

(Left) The original image, (Right) The image warped with control (gray) and limiter (red) points

As you work, you can Option-click any unwanted warp or limiter point to delete it. To start from scratch,

you can click the Reset Warp control in the Inspector. Warp and limiter points can be keyframed via the

Positions and Warp Strength parameters.

Warp Mode Curves

The Curves mode of the Warper lets you generate the warp around a curve or shape, instead of

simple points on a grid. This lets you get more specific with your selection and make a more organic-

looking warp on the image. The Curves mode adds more drawing tools and keyboard shortcuts to

the Viewer.


Resolve FX Overview | Chapter 169 Resolve FX Warp

COLOR

To draw a curve, first select Warp Mode Curves, then click in the Viewer where you want the curve to

start, then drag the line to where you want the next point in the curve and click again. Then continue

dragging lines and clicking points until you have the rough line or shape you need. Curves can be

used open or closed into shapes.

Add, Adjust, and Warp modes

When creating a curve, initially you will be in Add mode; this allows you to create your initial curve or

shape, however once you’ve closed the shape or pressed Esc to stop drawing, by default the Warper

will automatically shift you to Adjust mode, which allows you to manipulate your curve without adding

more points to it. You then switch to Warp mode to move the initial curve points to another location,

which actually performs the warp. You can have as many curves or shapes as you can draw, and if one

curve intersects another, a point will automatically be placed at the intersection.

You can manually toggle back and forth between Add, Adjust, and Warp modes as needed.

Curve Drawing Commands

Most of the curve editing is done intuitively by clicking and dragging in the Viewer, while there are also

some additional keyboard commands.

�Esc: Stops drawing.

�Enter: Closes the curve connecting the last point to the first point, or simply click on the first point

again to close the shape.

�Click: Anywhere in the image to start a new curve.

�Click: Anywhere on an existing curve to add another point.

�Click and Drag: To set a point and drag out its spline handles to adjust its curvature.

�Shift-Click: Anywhere in the image to start a limiter curve. A limiter curve lets you define a shape

or area where no warping will take place. A limiter curve will be in red.

�Option-Click: Creates a new line in Add mode, regardless of if you are currently in Adjust or

Warp modes.

�Delete: Removes a selected point or points.

Drawing curves in the Warper


Resolve FX Overview | Chapter 169 Resolve FX Warp

COLOR

In the above example, the limiter (red) shape around the 1 ball prevents it from being warped. The

straight line on the left is warping the table downward and to the left along its edge, as seen by the

origin reference (dotted lines) showing where the warp began and the solid line showing where the

warp is. The curve over the group of balls to the right is showing the spline handles of the currently

selected point.

Editing Splines

By default, your “curves” will look more like sharp lines rather than graceful flowing curves. You can

manipulate the smoothness of the curve by adjusting a point’s spline handles.

A point’s spline handle is seen by clicking directly on the point. If the handles don’t appear, hold down

the Command key and drag the handles out of the point. By default spline handles are paired, as you

move one, the other moves in the opposite direction. You can also manipulate one spline handle at a

time by holding the Command key and clicking on the single spline handle you want to manipulate.

Selection

To select curves and points for modification, you can click directly on them in viewer. Click on the

shape again to enclose them in a bounding box. You can select either the whole shape, a point,

or drag to draw a selection box around certain points. Holding shift and drag to creates a freeform

selection lasso instead of a box.

Once the box is in place, you can scale the points by dragging the bounding box from it’s edges. You

can rotate the selection by hovering the mouse near the edge of the box until the rotate tool appears,

then click and drag to rotate. Holding Option and dragging scales the shape around the geometric

center of the box.

Drawing a bounding box around a curve, lets you scale and rotate it.


Resolve FX Overview | Chapter 169 Resolve FX Warp

COLOR

Warper Settings

Warp Mode: Choose which control mode to apply the warp, either using Curves or Points.

Curves

�Add: With this mode selected, you can add points to create a curve or shape to warp around.

�Adjust: With this mode selected, you can adjust the curve or shape that you’ve created isolated

from the warp.

�Warp: With this mode selected, the image will warp around the curves or shapes that you’ve

created and update in real time as you move them.

�Render a Reference Grid: Check this box to add a reference grid over the image, so you can see

just how much the warp is affecting each area of the frame.

�Origin Reference: Adjusting this slider will adjust the visible intensity of the original curve

and point locations. Slide to the right to increase the intensity, slide to the left to make them

transparent.

�Position Keyframing: Keyframes the positions of the curve points.

�Warp Keyframing: Keyframes the warps of the curve points.

�Warp Strength: Adjust this slider to magnify or reduce the distortion effect of the warp.

Selected Points

�Symmetric: Makes the selected point or all points on selected curve symmetric to the selected

control point.

�Corner: Makes the selected point or all points on selected curve hard corners.

�Rounded: Makes the selected point or all points on selected curve rounded corners with

spline controls.

�Reset Handle Adjustments (Warp mode): Click this button to reset the spline curve adjustments

of a point back to neutral.

�Reset Warp (Warp mode): Click this button to reset the warp back to its original neutral state.

Selected Curve

�Show All Handles: This checkbox toggles on or off all the spline handles for all the points

on a curve.

�Open/Close: Click this button to toggle closing a curve (connecting the last point to the first point)

or opening a curve (removing the connection).

�Warper/Limiter: Click this button to toggle a curve between a warper or limiter curve. A limiter

curve prevents warping in its defined area.

�Delete: Deletes an entire curve.

Points

�Render a Reference Grid: Check this box to add a reference grid over the image, so you can see

just how much the warp is affecting each area of the frame.

�Positions: Keyframes the positions of the points in the Viewer.

�Show Origin Locations: Shows the original location of each point in the Warper.

�Clear All Points: Deletes all added points and returns the Warper to its neutral state.

�Reset Warp: Resets the Warper to its neutral state but retains all added points at their

origin position.

�Warp Strength: Adjust this slider to magnify or reduce the distortion effect of the warp.


Resolve FX Overview | Chapter 169 Resolve FX Warp

COLOR

On-Screen Controls

�Show: Shows the on-screen controls in the Viewer.

�Auto Hide: Shows the on-screen controls in the Viewer but hides them only as they are adjusted,

letting you see the final image while making adjustments.

�Hide: Hides the on-screen controls in the Viewer.

�Warp Boundaries (Points Only): This pop-up menu has three choices for letting you see which

areas of the image will be locked off by limiter points you place in the image.

None: Hides this information and is the default setting.

As Border: Shows a red line at the boundary where warping becomes locked off.

As Mask: Dims the area that’s protected from warping by limiter points.

�Scale Controls: This slider lets you shrink or grow the control points or warp vector handles to the

most convenient size for the task at hand.

Advanced Options

�Limits: A pop-up menu lets you choose how to treat the edges of the image when you’re

warping it.

Pin at Corners: Locks the four corners of the image in place, but allows the sides to bulge in or out

as you warp and allows blanking to creep in.

Around the Edges: Locks the full width and height of all four edges in place as you warp,

preventing blanking.

Distant: Locks parts of the image that are n pixels away, but the default setting is very permissive.

Manual (Free-Floating): Allows the entire image to be warped without locking any part of it,

allowing for extreme warps all along an entire edge of the image, but requiring you to place at

least one limiter point prior to adding a warp point.

�Elasticity: A pop-up menu lets you choose one of three methods of interpolating how the image

bends around a Warp point: Fabric, Rubber (the default), and Jelly. Fabric produces the “most

pointy” warps, while Jelly produces the most gently curved warps. Rubber strikes a balance

between the two extremes..

Fabric


Resolve FX Overview | Chapter 169 Resolve FX Warp

COLOR

Rubber

Jelly

�Edge Behavior: A pop-up menu eliminates any blanking caused by warping that affects the edge

of the image by filling black areas in one of several user-defined ways; options include Black (do

nothing and leave the blanking), Reflect, Wrap-Around, and Replicate.

�Warp Detail: A pop-up menu lets you choose from among three methods of calculating the

warping effect you’re creating: Faster, Default, and Better. Each choice is an obvious trade-off

between image smoothness and performance.

�Effect Follows: Allows you to choose whether the points stick to the scaled content (Input and Edit

Sizing) or the original frame in the timeline (Timeline Frame).

�Auto Advance to Adjust Mode: When this box is checked, after adding a point or curve,

automatically switch to Adjust mode to edit it.