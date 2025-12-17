---
title: "Planar Tracker Node [PTRA]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 493
---

# Planar Tracker Node [PTRA]

The Planar Tracker node

The Planar Tracker node is designed to solve a match-moving problem that commonly comes up

during post-production. As an example, live-action footage can often contain a planar surface such as

a license plate or a road sign that needs new numbers in the license plate or a new city’s name on the

road sign. Often, the problem is that the camera is moving in the shot, so the license plate or road sign

is continuously changing perspective. You cannot just merge a new license plate over the existing one

without accounting for the perspective distortions. A time-intensive way to solve this problem would

be to use a Corner Pin node and manually keyframe the four corners. The Planar Tracker automates

this keyframing process and tracks the perspective distortions of a planar surface over time. That

tracking data is then applied with those same perspective distortions to a different foreground.

For more information on using the Planar Tracker, see Chapter 83, "Planar Tracking," in the

DaVinci Resolve Reference Manual, or Chapter 23 in the Fusion Reference Manual.

TIP: Part of using a Planar Tracker is also knowing when to give up and fall back to using

Fusion’s Tracker node or to manual keyframing. Some shots are simply not trackable, or the

resulting track suffers from too much jitter or drift. The Planar Tracker is a useful time-saving

node in the artist’s toolbox, but while it may track most shots, it is not a 100% solution.

What the Planar Tracker Saves

While the Planar Tracker does save the resulting final track in the composition on disk, it does not

save temporary tracking information, such as the individual point trackers (compared with the Camera

Tracker, which does save the individual point trackers). Some consequences of this include:

�The point trackers no longer appear in the viewer when a comp containing a Planar Tracker node

is saved and reloaded.

�Tracking may not be resumed after a comp containing a Planar Tracker node has been saved and

reloaded. In particular, this also applies to auto saves. For this reason, it is good to complete all

planar tracking within one session.

�The size of composition files is kept reasonable (in some situations, a Planar Tracker can produce

hundreds of megabytes of temporary tracking data).

�Saving and loading of compositions is faster and more interactive.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Inputs

The Planar Tracker has four inputs:

Background: The orange background image input accepts a 2D image with the planar

surface to be tracked.

Corner Pin 1: The green corner pin 1 input accepts a 2D image to be pinned on top of the background.

There may be multiple corner pin inputs, named Corner Pin 1, Corner Pin 2, etc.

Occlusion Mask: The white occlusion mask input is used to mask out regions that do not need to be

tracked. Regions where this mask is white will not be tracked. For example, a person moving in front of

and occluding bits of the pattern may be confusing the tracker, and a quickly-created rough rotomask

around the person can be used to tell the tracker to ignore the masked-out bits.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the output of the Planar

Tracker to certain areas.

Basic Node Setup

A basic Planar Tracker setup consists of just two nodes: a MediaIn connects to the background input

and the Planar Tracker can be used as a separate branch from the rest of the node tree. Once the

tracking is completed, a Planar Transform node should be generated to use the planar tracking data.

A Planar Tracker can be isolated on its own branch of a node tree.

A Typical Planar Tracker Workflow

The following steps outline the workflow with the Planar Tracker:


Remove lens distortion: The more lens distortion in the footage, the more the resulting track will

slide and wobble.


Connect footage: Connect a Loader or MediaIn node that contains a planar surface to the orange

background input and view the Planar Tracker node in a viewer.


Select a reference frame: Move to a frame where the planar surface to be tracked is not occluded

and click the Set button to set this as a reference frame.


Choose the pattern: In the viewer, make sure the onscreen controls are visible, and draw a

polygon around the planar surface you want to track. This is called the “pattern.” In most cases,

this will probably be a rectangle, but an arbitrary closed polygon can be used. The pixels

enclosed by this region will serve as the pattern that will be searched for on other frames. Note

that it is important that the pattern is drawn on the reference frame. Do not confuse the pattern

with the region to corner pin (which always has four corners and is separately specified in Corner

Pin mode).


Adjust render range: In the Keyframes Editor, adjust the render range to match the range of frames

where the planar surface is visible.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION


Adjust track options: Frequently changed options include Tracker, Motion Type, and

Track Channel.


Mask out occluders: If moving objects partially cover up the planar surface, you may wish to

connect an occlusion mask to the Planar Tracker. When using the Hybrid tracker, providing a

mask to deal with occluding objects is strongly recommended, while with the Point tracker it is

recommended to try tracking without a mask.


Track: Click the Go button to return to the reference frame. Press the Track To End button and wait

for the track to complete. Click the Go button to return to the reference frame again. Press the

Track To Start button and wait for the track to complete. Note that the tracks in the viewer are not

selectable or deletable as they are in a Camera Tracker.


Check track quality: Visually inspect the track to see how accurate it is. Does it stick to the

surface? Switching to Steady mode can help here.

10	  Use the track: At this point, in most cases, you will create a Planar Transform node from the

Inspector and use it to apply the tracked perspective distortion onto masked images. If the image

you are applying the tracking data to is a full frame unmasked clip, you can use the Steady, Corner

Pin, and Stabilize operation modes in the Planar Tracker.

Inspector

The Planar Tracker Controls tab

Controls tab

The Controls tab contains controls for determining how the Planar Tracker will be used, setting the

reference frame, and initiating the track.

Operation Mode

The Operation Mode menu selects the purpose of the Planar Tracker node. The Planar Tracker has

four modes of operation:

�Track: Used to isolate a planar surface and track its movement over time. Then, you can create a

Planar Transform node that uses this data to match move another clip in various ways.

�Steady: After analyzing a planar surface, this mode removes all motion and distortions from the

planar surface, usually in preparation for some kind of paint or roto task, prior to “unsteadying” the

clip to restore the motion.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

�Corner Pin: After analyzing a planar surface, this mode computes and applies a matching

perspective distortion to a foreground image you connect to the foreground input of the Planar

Tracker node and merges it on top of the tracked footage.

�Stabilize: After analyzing a planar surface, this mode allows smoothing of a clip’s translation,

rotation, and scale over time. This is good for getting unwanted vibrations out of a clip while

retaining the overall camera motion that was intended.

The last three modes (Steady, Corner Pin, and Stabilize) use the tracking data produced in Track mode.

NOTE: None of the operations can be combined together. For example, both Corner Pin

and Stabilize cannot be done at the same time, nor can a track be done while in corner

pinning mode.

Reference Time

The Reference Time determines the frame where the pattern is outlined. It is also the time from which

tracking begins. The reference frame cannot be changed once it has been set without destroying all

pre-existing tracking information, so scrub through the footage to be tracked and choose carefully.

The reference frame must be chosen carefully to give the best possible quality track.

You choose a reference frame by moving the playhead to an appropriate frame and then clicking the

Set button to choose that frame.

Pattern Polygon

You specify which region of the image you want to track by drawing a polygon on the reference frame.

Typically, when you first add a Planar Tracker node, you are immediately ready to start drawing a

polygon in the viewer, so it’s best to do this right away. When choosing where to draw a polygon, make

sure the region selected belongs to a physically planar surface in the shot. In a pinch, a region that is

only approximately planar can be used, but the less planar the surface, the poorer the quality of the

resulting track.

As a rule of thumb, the more pixels in the pattern, the better the quality of the track. In particular, this

means the reference frame pattern should be:

�As large as possible.

�As much in frame as possible.

�As unoccluded as possible by any moving foreground objects.

�At its maximal size (e.g., when tracking an approaching road sign, it is good to pick a later frame

where it is 400 x 200 pixels big rather than 80 x 40 pixels).

�Relatively undistorted (e.g., when the camera orbits around a flat stop sign, it is better to pick a

frame where the sign is face-on parallel to the camera rather than a frame where it is at a highly

oblique angle).

If the pattern contains too few pixels or not enough trackable features, this can cause problems with

the resulting track, such as jitter, wobble, and slippage. Sometimes dropping down to a simpler motion

type can help in this situation.

After you’ve drawn a pattern, a set of Pattern parameters lets you transform and invert the resulting

polygon, if necessary.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Track Mode

Track mode is unlike the other three options in the Operation menu in that is the only option that

initiates the planar tracking. The other modes use the tracking data generated by the Track mode.

Tracker

There are two available trackers to pick from:

�Point: Tracks points from frame to frame. Internally, this tracker does not actually track points-per-

se but rather small patterns like Fusion’s Tracker node. The point tracker possesses the ability

to automatically create its internal occlusion mask to detect and reject outlier tracks that do not

belong to the dominant motion. Tracks are colored green or red in the viewer, depending on

whether the point tracker thinks they belong to the dominant motion or they have been rejected.

The user can optionally supply an external occlusion mask to further guide the Point tracker.

�Hybrid Point/Area: Uses an Area tracker to track all the pixels in the pattern. Unlike the Point

tracker, the Area tracker does not possess the ability to automatically reject parts of the pattern

that do not belong to the dominant motion, so you must manually provide it with an occlusion

mask. Note that for performance reasons, the Hybrid tracker internally first runs the Point tracker,

which is why the point tracks can still be seen in the viewer.

There is no best tracker. They each have their advantages and disadvantages:

Artist Effort (occlusion masks): The Point tracker will automatically create its internal occlusion

mask. However, with the Hybrid tracker, you need to spend more time manually creating occlusion

masks.

Accuracy: The Hybrid tracker is more accurate and less prone to wobble, jitter, and drift since it

tracks all the pixels in the pattern rather than a few salient feature points.

Speed: The Hybrid tracker is slower than the Point tracker.

In general, it is recommended to first quickly track the shot with the Point tracker and examine the

results. If the results are not good enough, then try the Hybrid tracker.

Motion Type

Determines how the Planar Tracker internally models the distortion of the planar surface being tracked.

The five distortion models are:

�Translation.

�Translation, Rotation (rigid motions).

�Translation, Rotation, Scale (takes squares to squares, scale is uniform in x and y).

�Affine - includes translation, rotation, scale, skew (maps squares to parallelograms).

�Perspective (maps squares to generic quadrilaterals).

Each successive model is more general and includes all previous models as a special case.

When in doubt, choose Perspective for the initial track attempt. If the footage being tracked has

perspective distortions in it, and the Planar Tracker is forced to work with a simpler motion type, this

can end up causing the track to slide and wobble.

Sometimes with troublesome shots, it can help to drop down to a simpler motion model—for example,

when many track points are clustered on one side of the tracked region or when tracking a small

region where there are not many trackable pixels.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Output

Controls what is output from the Planar Tracker node while in the Track operation mode.

�Background: Outputs the input image unchanged.

�Background - Preprocessed: The Planar Tracker does various types of preprocessing on the

input image (e.g., converting it to luma) before tracking. It can be useful to see this when deciding

which track channel to choose.

�Mask: Outputs the pattern as a black and white mask.

�Mask Over Background: Outputs the pattern mask merged over the background.

Track Channel

Determines which image channel in the background image is tracked. It is good to pick a channel

with high contrast, lots of trackable features, and low noise. Allowed values are red, green, blue,

and luminance.

Tracking Controls

These controls are used to control the Tracker. Note that while tracking, only track to a new frame if

the current frame is already tracked or it is the reference frame.

�Track to start: Tracks from the current frame backward in time to the start (as determined by the

current render range).

�Step tracker to previous frame: Tracks from the current frame to the previous frame.

�Stop tracking: Stops any ongoing tracking operations.

�Step tracker to next frame: Tracks from the current frame to the next frame.

�Track to end: Tracks from the current frame forward in time to the end (as determined by the

current render range).

�Trim to start: Removes all tracking data before the current frame.

�Delete: Deletes all tracking data at all times. Use this to destroy all current results and start

tracking from scratch.

�Trim to end: Removes all tracking data after the current frame. This can be useful, for example, to

trim the end of a track that has become inaccurate when the pattern starts to move off frame.

Show Splines

This button to the right of the “Trim to end” button opens the Spline Editor and shows the splines

associated with the Planar Tracker node. This can be useful for manually deleting points from the Track

and Stable Track splines.

Right-Click Here for Track Spline

While tracking, a spline containing 4 x 4 matrices at each keypoint is created. This is known as the

“Track spline” or just “Track” for short. These matrices completely describe the distortions of the

tracked pattern.

Create Planar Transform

After tracking footage, this button can be pressed to create a Planar Transform node on the Node

Editor. The current tracking data is embedded in the Planar Transform node so that it can replicate

the planar distortions tracked by the Planar Tracker node. Unless you are compositing a full frame

foreground that matches the same dimensions as the raster, it is best to create a Planar Transform and

use it to apply motion to the foreground.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION