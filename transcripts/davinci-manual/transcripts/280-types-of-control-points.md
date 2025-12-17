---
title: "Types of Control Points"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 280
---

# Types of Control Points

The control points along an XY path in the viewer are locked to the control points on the X and Y

curve in the Spline Editor. The number of points are identical, and adding a control point in one place

adds it to the other. That is not the case with a Polyline path. Polyline paths are composed of locked

and unlocked points. Whether a point is locked is determined by how it was added to the Polyline.

Locked points on the motion path in the viewer will have an associated point on the Displacement

spline in the Spline Editor; unlocked points will not have corresponding points. Each has a distinct

behavior, as described below.

Locked Points

Locked points are the motion path equivalents of keyframes. They are created by changing the

playhead position and moving the animated control. These points indicate that the animated control

must be in the specified position at the specified frame.

The locked points are displayed as larger-sized hollow squares in the viewer. Each locked key has an

associated point on the path’s Displacement curve in the Spline Editor.

Locked points on a path in the viewer

Deleting a locked point from the motion path will change the overall timing of the motion.

To change the duration of a path using locked points:


Connect an object to a Transform node.


Position the where you want to start the motion path.


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION

A graphic placed on the right side of the frame


Set the playhead at frame 0.


Select the Transform node and in the Inspector, click the Keyframe button

to the right of the Center X/Y parameter.

This adds the path modifier and creates the first locked point of the path.


Position the playhead at frame 45.


Move the object’s center to the lower center of the screen.

Moving the playhead and repositioning the bee adds a second locked point


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION

This sets the second locked point.


View the Spline Editor and display Path1’s Displacement spline.

The path’s Displacement spline with locked keyframes

At a value of 0.0, the control will be located at the beginning of the path. When the value of the

Displacement spline is 1.0, the control is located at the end of the path.


Select the keyframe at frame 45 in the Displacement spline and drag it to frame 50.

The motion path is now 50 frames long, without making any changes to the motion path’s shape.

If you try to change this point’s value from 1.0 to 0.75, it cannot be done because the point is the

last in the animation, so the value must be 1.0 in the Displacement spline.


Position the playhead on frame 100 and move the bee center to the upper-left corner of

the screen.

Moving locked points changes the duration of a motion path without changing its shape


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION

This will create an additional locked point and set a new ending for the path.

Unlocked Points

Unlocked points are created when additional points are added to the motion path while in Insert and

Modify modes. These points are used to adjust the overall shape of the motion path, without directly

affecting the timing of the motion. This means you can add whatever unlocked points you want to

reshape a motion path, without that having any effect on the timing of the animation on that path.

This makes it vastly easier to fine-tune a motion path spatially after you’ve perfected the timing of the

animation temporally.

Unlocked points do not have corresponding points on the path’s Displacement spline. They appear in

the viewer as smaller, solid square points.

To add unlocked points to a motion path, do the following:


Select a motion path spline by using the Tab key to cycle controls until the path is selected.


To insert points along a path, click the Insert and Modify button in the toolbar.


Click on the path and create two new points: one half-way between the first and the second

points, and the other half-way between the second and the third points.

The two points just added are not present in the motion path’s Displacement spline. These are

unlocked points, used to shape the motion but unrelated to the timing of the path.

Unlocked points added to the motion path are not displayed on the Displacement spline

You can add unlocked points to the Displacement spline as well. Additional unlocked points in the

Spline Editor can be used to make the object’s motion pause briefly.


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION

To pause motion along a motion path using an unlocked point:

Select a locked point on the Displacement spline and then hold down the Command key while

dragging the point horizontally to another frame. The point is copied as an unlocked point to

the new frame.

Create a pause in the motion by copying locked points

Knowing the difference between locked and unlocked points gives you independent control

over the spatial and temporal aspects of motion paths.

Locking and Unlocking Points

You can change an unlocked point into a locked point, and vice versa, by selecting the point(s) and

choosing the Lock Point option from the contextual menu.

Tips for Manipulating Motion Paths

There are a variety of ways you can create and edit motion paths in the viewer.

Compound Motion Paths Using Path Centers

Every motion path has a defined center represented by a crosshair. Path centers allow paths to be

connected to other controls and behave in a hierarchical manner, which is an exceptionally powerful

way of creating complex motion by combining relatively simple paths.

A useful example of this technique would be animating the path of a bee in flight. A bee often flies

in a constant figure eight pattern while simultaneously moving forward. The easy way of making this

happen involves two paths working together.

In the following example, the bee would be connected to a first path in a Transform node, which

would be a figure eight of the bee moving in place. This first path’s center would then be connected to

another path defining the forward motion of the bee through the scene via a second Transform node.

To create a compound motion path:


Create a figure-eight motion path by keyframing an object or drawing a polyline mask.

(If using a polygon mask, you’ll need to remove the auto-keyframing and publish the mask prior to

the next step.)


Add a polyline mask and create a smooth curve spline that travels across the screen.


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION


At the bottom of the Inspector, right-click over the “Right-click here for shape animation” label and

choose Remove Polygon Polyline to remove the auto-animation behavior.


Right-click over the label again and choose Publish.


Select the object’s Transform node and click the Modifiers tab.


Right-click over the Path1 Center X/Y parameter and choose Path.


At the bottom of Path2, choose Connect To > Polygon: Polyline.


Keyframe the Path2 Displacement to move the object along the second path.

Two motion paths working together