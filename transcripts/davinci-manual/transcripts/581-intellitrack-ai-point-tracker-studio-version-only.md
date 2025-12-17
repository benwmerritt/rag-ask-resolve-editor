---
title: "IntelliTrack AI Point Tracker (Studio Version Only)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 581
---

# IntelliTrack AI Point Tracker (Studio Version Only)

The DaVinci Neural Engine powered IntelliTrack point tracker is now available in the Color tracker,

Fusion point tracker, and the FX tracker in DaVinci Resolve Studio. The IntelliTrack setting can be used

for general tracking and stabilization tasks.

IntelliTrack, like other AI tools, doesn’t use predetermined rulesets or heuristics. Instead, it is trained

on real world examples. This makes it less likely to fail in scenarios like tracking a subject behind brief

occlusions. For most cases it will be more precise and more robust than the normal Point Tracker.


Color | Chapter 140 Motion Tracking Windows

COLOR

Using IntelliTrack: All the IntelliTrack analysis happens behind the scenes, and there is no

additional user input required other than to choose the IntelliTrack setting, set the tracking

crosshairs over high contrast areas on the same moving subject, and then press one of the

tracker direction controls.

Setting the IntelliTrack mode for the Color page window tracker

Cloud Tracker Workflows

The next few examples illustrate how to use the Tracker palette’s controls in practical situations. In

many circumstances, objects passing in front of a tracked subject, known as “occlusions,” can cause

problems. While the tracker in DaVinci Resolve is highly occlusion-resistant, the following sections

show a variety of techniques you can use when an occlusion prevents you from getting a useful track.

Using Interactive Mode to Manually Choose Tracking Features

Interactive mode lets you manually remove or add tracking points to improve tracking performance in

situations where the automatic image analysis in DaVinci Resolve provides unsatisfactory results.

For example, you can delete tracking points within a window that correspond to overlapping features

you don’t want to track. Suppose a car that you’re tracking drives by a sign that partially obscures the

car. Without intervention, the PowerCurve that’s isolating the car will deform improperly when the car

moves along and then away from the sign.

Using Interactive mode, you can delete the tracking points that will overlap the sign you don’t want to

track, improving the result.


Color | Chapter 140 Motion Tracking Windows

COLOR

To eliminate specific, unwanted tracking points from a track:


Open the Tracker palette.


Turn on the Interactive Mode checkbox.

Selecting Interactive Mode


In the Viewer, drag a box around the tracking points you want to eliminate within the window.

Dragging a box around tracking

points that need to be deleted


Click the Delete button.

Deleting tracking points

The points within the selection area are deleted.

Remaining tracking points ready to be used


Color | Chapter 140 Motion Tracking Windows

COLOR


While Interactive mode is still on, click Track Forward or Track Reverse to track the subject using

the remaining tracking points.


When you’re finished tracking, turn off the Interactive Mode checkbox.

DaVinci Resolve goes back to using automatically placed tracking points.

In another interactive tracking example, you may sometimes run into situations where you

want to eliminate all automatically placed tracking points altogether, placing your own in

specific regions of the image.

To eliminate automatic tracking points, adding your own instead:


Open the Tracker palette.


Turn on the Interactive Mode checkbox.

Selecting Interactive mode


In the Viewer, drag a box around all the tracking points in the window, and click the

Delete button to eliminate all tracking points from the image.

Selection box surrounding all tracking points


Click the Delete button to eliminate all tracking points from the image.

Deleting tracking points


Color | Chapter 140 Motion Tracking Windows

COLOR


Drag a box around the specific area where you’d like to add new tracking points. In this case,

you only want to track the top half of the woman’s face, since the bottom half is cut off by the

fence posts.


Placing the selection box over the top of the window


Now, click the Insert Track Points button.

The Insert button of Interactive mode automatically

adds tracking points within the current bounding box.

New tracking points are automatically added to whichever features are

appropriate for tracking within the box you’ve drawn.

Tracking with the remaining tracking points

NOTE: If no appropriate tracking features can be found, no points will be added.


Color | Chapter 140 Motion Tracking Windows

COLOR