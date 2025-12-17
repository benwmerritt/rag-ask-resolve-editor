---
title: "Introduction to Tracking"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 323
---

# Introduction to Tracking

Fusion includes three different Tracking nodes that let you analyze different kinds of motion. Once you

have tracked motion on a clip, you can then use the resulting data for stabilization, motion smoothing,

matching the motion of one object to that of another, and a host of other essential tasks. Each tracker

type has its own chapter in this manual. This chapter covers the tracking techniques with the Planar

Tracker node.

Using the Planar Tracker

The Planar Tracker node is designed to deal with match moving issues on flat, unvarying surfaces that

commonly arise during post-production. Examples of flat, unvarying surfaces include clips containing

a license plate, a road sign, or a brick wall that often need images merged on top of them, such as

replacing the numbers in the license plate, changing the city’s name in the road sign, or placing a

billboard poster on the empty brick wall.

The Planar Tracker automates this process by analyzing the perspective distortions of a planar surface

on a background plate over time, and then re-applying those same perspective distortions to a

different foreground.

TIP: Part of using the Planar Tracker is also knowing when to give up and fall back to using

Fusion’s Tracker node or to manual keyframing. Some shots are simply not trackable, or the

resulting track suffers from too much jitter or drift. The Planar Tracker is a time-saving node in

the artist’s toolbox and, while it can track most shots, no tracker is a 100% solution.

Different Ways of Using the Planar Tracker Node

Like the other tracking nodes found in Fusion, the Planar Tracker can both analyze and contain the

resulting image tracking data interior to the node, and it can also use that tracking data to transform

either another image, paint strokes, or a polygon mask shape.

The Planar Tracker provides four modes of operation:

�Track: Used to isolate a planar surface and track its movement over time. Then, you can create a

Planar Transform node that uses this data to match move another clip in various ways.

�Steady: After analyzing a planar surface, this mode removes all motion and distortions from the

planar surface, usually in preparation for some kind of paint or roto task, prior to “unsteadying” the

clip to add the motion back.

�Corner Pin: After analyzing a planar surface, this mode computes and applies a matching

perspective distortion to a foreground image you connect to the foreground input of the Planar

Tracker node, and merges it on top of the tracked footage.

�Stabilize: After analyzing a planar surface, allows smoothing of a clip’s translation, rotation, and

scale over time. Good for getting unwanted vibrations out of a clip while retaining the overall

camera motion that was intended.


Fusion Fundamentals | Chapter 83 Planar Tracking

FUSION

Setting Up to Use the Planar Tracker

Similar to the Tracker node, to do a planar track, you need to connect the output of the image you

want to track to the background input of a Planar Tracker node.

Connecting an image to the background input of a PlanarTracker node

Check for Lens Distortion

If the image has barrel distortion, or any other kinds of lens distortion, it can adversely affect your

track. The more lens distortion in the footage, the more the resulting track will slide and wobble. If you

can see distortion in the image or you’re having problems with the track, you’ll want to try inserting the

Lens Distort node between the image and the Planar Tracker to eliminate this problem.

Fusion’s Lens Distort node can be used to remove or add lens distortion in an image. Connecting

the MediaIn or Loader node to the Lens Distort node displays controls for manually correcting lens

distortion. If you use Synth Eyes, PFTrack or 3D Equalizer software, you can also import lens data from

those applications to make the adjustments more automatic.

A Lens Distort node inserted between a MediaIn1 and

Planar Tracker to remove lens distortion

For more information about using the Lens Distort node, see Chapter 123, “Warp Nodes,”

in the DaVinci Resolve Reference Manual or Chapter 63 in the Fusion Reference Manual.

If you are using DaVinci Resolve, you can use the Lens Corrections control in the Cut page or

Edit page. This adjustment carries over into the Fusion page. Lens correction in DaVinci Resolve

automatically analyzes the frame in the Timeline viewer for edges that are being distorted by a wide

angle lens. Clicking the Analyze button moves the Distortion slider to provide an automatic correction.

From there, the MediaIn node in the Fusion page will have the correction applied, and you can begin

planar tracking.


Fusion Fundamentals | Chapter 83 Planar Tracking

FUSION

A Basic Planar Tracker

Match Move Workflow

Using the Planar Tracker is a process, but it’s straightforward once you’ve learned how to use it. The

following procedure tries to make this process as clear as possible.

To track a surface using the Planar Tracker:


Make sure the Operation Mode is set to Track, as you need to analyze an image to track a surface

before you do anything else.


With the background input of the Planar Tracker connected to an image, and the Planar Tracker

open in a viewer, move the playhead to a frame of video where the planar surface you want to

track is at its largest, is unoccluded, and is clearly a plane, and then click the Set button in the

Track panel of the Inspector to make this the reference frame that will be used to guide the track.

Clicking the Set button to set the reference

frame to use for analysis


Next, you’ll need to identify the specific pattern within the image that you want to track. In most

cases, this will probably be a rectangle, but any arbitrary closed polygon can be used. The pixels

enclosed by this region will serve as the pattern that will be searched for on other frames. Please

note that it is important that the pattern is drawn on the reference frame. In this example, we want

to track the wall behind the man, so we draw a polygon around part of the wall that the man won’t

pass over as he moves during the shot.

Drawing a polygon to identify the part of the image you want

to track, which should be a flat, trackable plane

TIP: Do not confuse the pattern you’re identifying with the region you’re planning to

corner pin (which always has four corners and is separately specified in Corner Pin mode.


Fusion Fundamentals | Chapter 83 Planar Tracking

FUSION


(Optional) If moving objects partially cover up or occlude the planar surface, you may wish to

connect a mask that surrounds and identifies these occlusions to the white “occlusion mask” input

of the Planar Tracker. This lets the Planar Tracker ignore details that will cause problems.

When using the Hybrid Tracker, providing a mask to deal with occluding objects is nearly

mandatory, while with the Point Tracker it is recommended to try tracking without a mask.


If necessary, move the playhead back to the reference frame, which in this case was the first

frame. Then, click the Track To End button and wait for the track to complete.

The Analyze buttons of the Planar Tracker

As the clip tracks, you can see track markers and trails (if they’re enabled in the Options tab of the

Inspector) that let you see how much detail is contributing to the track, and the direction of motion

that’s being analyzed.

During tracking, you can see track markers and trails

to follow how well the track is going


Once the track is complete, play through the clip to visually inspect the track so you can evaluate

how accurate it is. Does it stick to the surface? Switching to Steady mode can help here, as

scrubbing through the clip in Steady mode will help you immediately see unwanted motion in

the track.


Since we’re doing a match move, click the Create Planar Transform button to export a Planar

Transform node that will automatically transform either images or masks to follow the analyzed

motion of the plane you tracked.

Clicking Create Planar Transform to create a node to

use to transform other images or masks

In this case, the Planar Transform node will be inserted after a pair of Background and Paint nodes

that are being used to put some irritatingly trendy tech jargon graffiti on the wall. The Planar

Transform will automatically transform the Paint node’s output connected to its background input

to match the movement of the wall.


Fusion Fundamentals | Chapter 83 Planar Tracking

FUSION

Adding the PlanarTransform node after a Paint node to match move it to

the background image, combining it via a Merge node

The result is a seamless match move of the fake graffiti married to the wall in the original clip.

The final result; the paint layer is match moved to the background successfully


Fusion Fundamentals | Chapter 83 Planar Tracking

FUSION

TIP: If you want to composite semi-transparent paint strokes on the wall, or use Apply modes

with paint stroke, you can attach a Paint node to a Background node set to 100 transparency.

The resulting image will be whatever paint strokes you make against transparency and is easy

to composite.