---
title: "Path Modifier"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 279
---

# Path Modifier

In terms of functionality, it makes no difference which method you use to generate the path modifier.

All the above methods are just different ways to get to the same point. Whichever way you decide to

add the path modifier, the Modifiers tab contains controls for the path.

Creating a path adds controls to the

Modifiers tab in the Inspector.

You can use the path modifier controls in the Inspector to change the position, size, and rotation of the

entire path shape. The Displacement parameter is represented as a spline in the Spline Editor, which

determines the object’s position along the path and the Heading Offset is used for the orientation

along the path.

Controlling Speed and Orientation along a Path

Every Polyline path has an associated Displacement spline in the Spline Editor. The Displacement

spline represents acceleration, or the position of the animated object along its path, represented as a

value between 0.0 and 1.0.

The Displacement curve of a Poly path represents the acceleration of an object on a path.


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION

Smaller values are closer to the beginning of a path, while larger values are increasingly closer to the

end of the path.

For instance, let’s say you have a bumblebee that bobs up and down as it moves across the screen.

To have the bee accelerate as it moves up and down but slow down as it reaches its peaks and valleys

you use the Displacement curve.

A curvy path defined by a spline shape

The curved shape path does not define how fast the bee moves. The speed of the bee at any

point along the path is a function of the Displacement parameter. You can control the Displacement

parameter either in the Modifiers tab or in the Spline Editor.

To use the Displacement parameter to control the speed of an object on a path, do the following.


Position the playhead at the start of the animation.


In the Modifiers tab, drag the Displacement parameter to 0.0. This positions the object at the start

of the path.


Click the Keyframe button to the right of the Displacement parameter.


Position the playhead somewhere further into the comp and drag the Displacement parameter

until the object is where you want it to be based on the current frame.


Continue updating the playhead and the Displacement parameters at key points in the comp until

you have reached the end of the path.

After the initial animation is set, you can use the Displacement curve in the Spline Editor to adjust

the timing.

To adjust the timing of an object along a path:


Open the Spline Editor and enable the Displacement spline in the header.


Move control points horizontally closer together to increase the speed between the two points

while maintaining the location of the object along the path.

A longer, flatter curve between two points indicates a slower rate of change.


Drag a control point up or down to change its location on the path while maintaining the timing

between two points.


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION

A Displacement curve in the Spline Editor

TIP: Holding down the Option key while clicking on the spline path in the viewer will add a

new point to the spline path without adding a Displacement keyframe in the Spline Editor.

This allows you to refine the shape of the path without changing the speed along the path.

Using a Path Modifier to Adjust Orientation

The Heading parameter is used to adjust the orientation of the object along the path. For instance, if

you want the bee in our animation to auto-orient based on the direction of the path, you can connect

the bee’s angle to the Heading parameter.

To connect the Heading to an object’s angle:


Right-click over an object’s angle parameter in a Transform node.


Choose Connect To > Path > Heading.

In our example comp, the bee now auto-orients as the path descends and rises.

The Transform’s angle parameter connected to the path modifier’s Heading parameter


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION

XY Path

Unlike a Polyline path, the XY path modifier uses separate splines in the Spline Editor to calculate

position along the X-axis and along the Y-axis.

To animate a coordinate control using an XY path modifier:

�Right-click on the center coordinate control in the viewer or the Center X/ Y parameter in the

Inspector, and then choose Modify With > XY Path from the contextual menu.

Adding the XY Path modifier to a Center parameter in the Inspector

At first glance, XY paths work like Polyline paths. To create the path once the modifier is

applied, position the playhead and drag the onscreen control where you want it. Position the

playhead again and move the onscreen control to its new position. The difference is that the

control points are only there for spatial positioning. There is no Displacement parameter for

controlling temporal positioning.

XY path modifier controls in the

Modifiers tab of the Inspector


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION

Instead of dragging in the viewer, you can use the controls in the Modifiers tab to create a motion path,

while using the object’s original Inspector controls as an offset to this motion path. You can use the

XYZ parameters to position the object, the Center X/Y parameters to position the entire path, the Size

and Angle to scale and rotate the path, and the Heading Offset control to adjust the orientation.

Using an XY path modifier to animate a piece of text

Using the XY Paths in the Spline Editor

The Spline Editor for the XY path displays the X and Y channel splines. Changes to the path in the

viewer or the Inspector will be displayed as keyframes on these splines in the Spline Editor. Unlike a

Polyline path, XY paths do not include a Displacement curve. The speed of the object along the path

is tied to the path itself and cannot be separated from the timing of the keyframes that define that path.

TIP: XY path and Poly path can be converted between each other from the contextual menu.

This gives you the ability to change methods to suit your current needs without having to

redo animation.

The advantage of the XY path modifier is that you can explicitly set an XY coordinate at a specific time

for more control.

XY Path displays X and Y curves in the Spline Editor but does not include a Displacement control.

Switching Default Paths

If you want to change the default path type to XY path, you can choose Fusion > Preferences >

Globals in Fusion Studio or Fusion > Fusion Settings in DaVinci Resolve. In the Settings window, select

the Defaults category and choose XY Path for the Point With drop-down menu. The next time you

keyframe the Center X/Y parameter or choose Animate from CenterX/Y’s contextual menu, an XY path

modifier will be used instead of a Polyline path.


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION