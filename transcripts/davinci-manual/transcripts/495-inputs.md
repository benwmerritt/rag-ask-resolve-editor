---
title: "Inputs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 495
---

# Inputs

There are four inputs to the Surface Tracker node.

Input: The yellow input accepts the media with the surface that you want to track and composite onto.

Overlay: The green input accepts still graphics, video, or the output of a node tree. This is the image

that you want to overlay onto the surface.

Occlusion Mask: The pink occlusion mask input is used to mask out regions that do not need to be

tracked. Regions where this mask is white will not be tracked. For example, a person moving in front

of and occluding bits of the scene may be confusing to the tracker, and a quickly-created rough mask

around the person can be used to tell the tracker to ignore the masked-out bits.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines,

basic primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input

limits the filter to only those pixels within the mask. An effects mask is applied to the tool after the

tool is processed.

Basic Node Setup

Connect the media with the surface you want to composite onto to the main yellow input. Connect the

media with the graphic or video that you want to overlay onto the surface to the green overlay input.

Optionally, connect effect or occlusion masks to their respective inputs, if needed.

A simple node tree showing video clip of a guitar player, using the surface

tracker to overlay a small graphic of a bee on his shirt.

Inspector

The Bounds tab in the Surface Tracker controls

Bounds

This is where you are prompted to draw an area on the image that you want to apply the texture to.

Ideally, you want to choose a frame in the clip that has the surface you want to track as close and

as flat-on to the camera as possible. This frame becomes the default reference frame for the effect.

Simply click on the image to make multiple points around the area you want to define (a minimum

of three points are required), and the effect will connect them automatically as a polygon. Boundary

points should be on the surface for tracking, not around it. If points are accidentally placed on object

edges or the background instead, it will cause errors in the tracking.

You may add multiple boundaries and multiple holes to the same image, and all boundaries will join

together into one shape before subtracting the holes. The purpose of multiple boundaries and holes

are to allow you to mask out complex surfaces with regions not for tracking. For example, you can


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

make a boundary around someone’s face, but use multiple holes to exclude the eyes and mouth

as those change appearance quickly as the subject blinks and talks, making them exceptionally

difficult to track.

Multiple boundaries are designed to work on the same surface; using multiple boundaries on different

surfaces within the image will cause poor results. Separate surfaces are best tracked by using multiple

instances of the Surface Tracker instead.

The boundary is not useful for rotoscoping objects, only for analyzing the motion of a surface.

Rotoscoping of foreground objects can be done as described in the Tracking Using a Mask

section below.

�Click to Add Points: These are the controls used to make boundary areas on the image.

Boundary: The currently selected boundary area on the image. You can change the current

boundary or hole by using the drop-down menu. If there are issues with the boundary

(i.e., crossed edges, too few points, etc.), an error message will appear next to the boundary name.

+ Bound: Adds a boundary polygon to the image. You can have multiple boundaries defined for

the same surface, and they will be joined together into one shape.

+ Hole: Adds an area to exclude tracking from the surface. Used to remove overly complex and

changing parts of a surface from the effect’s calculations.

Delete: Lets you delete the boundary or hole selected in the Boundary field. Currently, this

operation can not be undone, so be careful around this button.

Clear All: Lets you delete all boundaries and holes in the effect.

A simple boundary drawn on his shirt in the viewer


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

The Mesh tab in the Surface Tracker controls

Mesh

With the boundaries now defined, you can establish the mesh over the surface to be tracked. The

initial mesh serves as the starting point for tracking, so for best results, the mesh should be placed

when your surface is as flat-on and closest to the camera as possible.

The mesh can be manually adjusted by dragging current points (multiple points can be moved by

holding command and dragging an area around the points) or clicking on an area to place new ones.

Option-clicking a point will remove it from the mesh. Manually adding mesh points can be useful if

there are flexible portions of the surface known to be a point where the texture should fold but which

is not initially identified when placing the mesh. For example, an extended arm may not have a mesh

point active at the elbow, but with a mouse click (and a basic knowledge of human anatomy), you can

manually add one there. Another use case would be to add points to an area with little detail, but

you know will develop detail as it rotates into view. Placing mesh points in blank areas that show little

detail will not improve results and may actually degrade them, so very few points on smooth areas is

desirable. A good rule of thumb is that if more than five points are created inside the boundaries, the

mesh may be good enough for tracking. Points cannot be added or deleted after tracking.

A good mesh is a sign of good tracking as they go hand in hand. If your mesh has few points detected

and the results don’t track tightly, you can artificially improve your results. For example, make sure that

the content is clearly visible. Tracking and point detection can fail if the surface is too bright (HDR), too

dark, or low contrast due to working in log. To improve results, you can temporarily add a brightness/

contrast node before the Surface Tracker to adjust contrast manually, then run the Surface Tracker.

Simply disable the brightness/contrast node again after the tracking has finished.

�Regenerate Mesh: This button recreates the mesh at the current frame and settings and discards

any manual changes that have been made.

Point Locations: These controls determine which mode is used to generate the mesh points.

Automatic: The Surface Tracker automatically locates the best details for tracking, and places

mesh points on those details. In most cases, Automatic will give you the best results.

Point Number Limit: Lets you set the maximum amount of mesh points to place. The number of

mesh points affects how the overlay will flex and fold, and should be set by the expected flexibility

of the surface. They do not directly affect tracking speed.

Minimum Point Spacing: Lets you set the minimum distance between mesh points. This prevents

mesh points from bunching together too tightly in highly detailed areas and interfering with each other.

Uniform: Creates a regular grid of points in the boundary and relies on internal shape models to

deform the grid during tracking. This may give better results than Automatic mode, if your surface

is highly detailed.

�Horizontal Spacing: Adjusts the horizontal distance between adjacent points in the uniform mesh.

�Vertical Spacing: Adjusts the vertical distance between adjacent points in the uniform mesh.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

The automatic mesh applied to the boundary. The bee is now composited

onto the shirt, but it does not look very realistic yet.

The Track tab in the Surface Tracker controls

Track

This section of the effect tracks the motion of the mesh points over time. Use the Tracking Direction

controls to complete the tracking procedure across the clip. After the tracking is complete, the effect

does no more analysis, and any additional contrast assistance from previous nodes can be discarded

after this step. For simple cases, the tracking may run completely without user intervention, but for

more complex cases, a number of additional controls are used to refine the track.

Fixing a broken track will require some manual adjustments to both the mesh and the tracking data.

At any time while tracking, mesh points can be adjusted either one by one, or with the lasso selection

tool (Command - Drag) around the entire mesh or just parts of it. The lasso selection tool also has the

ability to stretch, scale, and rotate the mesh points, making it easier to manually deform and place

the mesh exactly where you want it to be, if for some reason the automatic tracking fails. However,

additional mesh points cannot be added or deleted at this stage, without first resetting the tracking.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Manually editing the mesh points at a frame only affects that frame directly; it does not affect

neighboring tracking data. However, it does affect neighboring interpolated positions, which makes it

good for tracking from that point onwards. For example:

•	 Tracking is good until frame 150 when a few points separate from the rest, disturbed by a

lighting change. At frame 150 they can be manually moved back into place, then if tracking is

resumed they will continue with their corrected positions.

•	 Tracking exists until frame 150, after which there is no data for a few frames until it resumes

at 160. Editing the points at either frames 150 or 160 will cause the intermediate frames to be

interpolated with these changes applied.

•	 Tracking exists up to frame 150 and at frame 160 onwards, frames 151-159 are interpolated.

At frame 155 some points are adjusted. This creates tracking data at this frame, and now

frames 151-154 interpolate from the last tracked frame to this current one, and then frames

156-159 from the current to the next tracked frame.

Go to Start: This button will snap the playhead to the first frame that has been tracked, or the frame

where the boundary was created.

Go To End: This button will snap the playhead to the last frame that has been tracked.

Tracking Direction Controls: These controls perform the tracking analysis in the direction indicated.

They are from left to right: Track Backwards, Track Backwards One Frame, Pause Tracking, Track

Forwards Then Reverse, Track Forwards One Frame, Track Forwards. Using these controls, you can

set the track across the whole clip or limit the tracking to just a section of it.

Trimming: These controls allow you to manipulate the track data after it’s been run.

�Remove Tracking Data Before This Frame: Clears all the tracking data before the current frame.

�Track From Last Known Match: This button will match the tracking data to the current frame

and connect it to the last frame where tracking data exists. If there has been too much motion

between those times, you can move the points approximately into place and try matching again.

For example, the tracking occurs without issue until frame 150, but something moving across the

scene causes an error in the track for six frames (151-157). The tracking data can be paused before

it hits these frames, or these frame’s tracking data can be deleted after the fact. Then at frame 158

you can press this button to continue the track from the last known good track at frame 150.

�Remove Tracking Data At This Frame: Clears the tracking data at the current frame.

�Remove Tracking Data After This Frame: Clears all the tracking data after the current frame.

Tracking Behavior: These options allow you adjust the way the tracking operates.

�Motion Range: Controls how far to search for matches. Increase this slider if the surface is moving

too quickly and the tracking fails to find it.

�Mesh Rigidity: Controls how flexible the mesh is. Reduce this slider to make the mesh points more

flexible. This gives you best results if the clip is noise-free and warping smoothly. Increase this

slider to get a “stiffer” tracked surface with less internal warping.

�Quality: The tracker can be very computationally intensive; it is recommended to use the Faster

setting while making adjustments to the mesh, then use Better for the final track once all the

parameters have been set correctly.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Interaction Overlays: These buttons control the visibility of the mesh overlays on the Viewer.

�Show: Shows the mesh at all times.

�Hide on Drag: Shows the mesh until a point is dragged, then it is hidden, allowing you to see the

surface underneath for fine adjustments.

�Hide: Hides the mesh at all times.

NOTE: The Surface Tracker creates data at each frame of the source clip. If the source clip is

not at the same frame rate as the timeline, tracking may seem to stutter or skip frames. You

can “bake” retiming into a clip by right-clicking on it on the Edit page and choosing “Render In

Place” to create a result with exactly one frame for every timeline frame.

The Result tab in the Surface Tracker controls

Result

Once the tracking data is complete, the Result section lets you determine what and how to composite

a video layer on top of the moving surface.

Output: There are six options for what to do with the resulting tracking data.

�Warp Input 2 Onto 1: Warps the Surface Tracker’s overlay input to the shape and position of the

tracked mesh and composites it onto the clip.

�Warp Input 2 Onto Blank: Warps the Surface Tracker’s overlay input to the shape and position of

the tracked mesh and passes the Alpha channel information, allowing you to perform the actual

composite in another node or effect.

�Warp Input 1’s Alpha: Applies the results of the Surface Tracker to the Effect Mask input.

�Create Mesh Alpha Mask: Produces an Alpha mask, which follows the position and shape of the

outline of the mesh. All inputs and alphas are ignored.

�Stabilize-Warp Input 1: Performs an inverse warp to the Reference Frame (again, this should be

a frame that ideally is as close to and flat-on to the camera as possible). The result is a stationary

image within the boundary with all the lighting changes and details of the surface’s motion shown

on it. This now stabilized image can be modified with any of DaVinci Resolve’s existing tools,

bypassing any issues caused by this area’s motion in the original video clip. Once modified, you

warp the result back onto the original footage by using a copy of the original Surface Tracker node

but with the Rewarp Stabilized Clip setting here instead.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

�Rewarp Stabilized Clip: Composites the output of the Stabilize-Warp Input 1 selection back onto

the original video clip, after it’s been modified. This option is designed to be used in conjunction

with a copy of a Surface node using Stabilize-Warp Input 1. It seamlessly blends whatever

additional modifications that were made between the two Surface Trackers back together.

Overlay/Alpha Source: Allows you to select which frames of the overlay or alpha are used to create

the result.

�First Frame: Useful for freezing content from an overlay clip to use a still frame as a static texture.

�Reference Frame: Starts at the currently defined reference frame (see below), instead of at frame

0. The reference frame is the frame which the mesh overlay is initially positioned in its “un-warped”

state, and the positioning controls are active.

�Each Frame: Treats the overlay or alpha as a clip, warping each frame in turn. This is necessary for

animated overlays or re-warping stabilized content.

Contract/Expand: Allows you to add or remove pixels from the edges of the overlay or alpha. It is

important to note that the expanded area is not tracked and will not be stabilized to the content.

Softness: Blurs the edge of the Expand/Contract tool to blend more realistically into the scene.

Motion Blur: This slider lets you add motion blur to the overlay to preserve the illusion that it was

actually captured with the scene.

Overlay Placement: These controls let you set the initial transform options for the image you want to

overlay on the mesh.

�Go To Reference: Moves the playhead to the selected reference frame.

�Set to Current: Sets the current frame under the playhead as the reference frame.

�Reference Frame: Shows the frame number at which the overlay is originally positioned and un-

warped (the point from which the warp to every other frame is calculated). The positioning controls

appear on screen when the clip is at the reference frame. A frame where the surface’s view is

largest and least warped is the best starting point for rendering onto other frames.

�Positioning: Lets you choose how to adjust the overlay position.

Sliders: Choosing this option exposes a set of transform sliders (X/Y position, zoom, rotate, etc.)

that let you manipulate the overlay's initial position.

Interactive Canvas: Choosing this option exposes draggable frame controls in the Viewer,

allowing you to transform the overlay using mouse controls. The Viewers shows a large grid with 9

regions; you can drag in any of them to move, skew, or warp the overlay.

Interactive Pins: Adjusting the image in this mode is done by manually placing control points,

called pins, in the Timeline Viewer. Adding one pin only gives you position control. At least two

points are required for scaling and rotation. Dragging on one of the pins scales or rotates the

image around the other pin. Using three pins, you can create perspective distortions by dragging

any one of the pins. You can add up to four pins for unique corner pinning distortions.

�Reset Position: Resets the on-screen overlay back to its default state.

Interaction Overlays: These buttons control the visibility of the mesh overlays on the Viewer.

�Show: Shows the mesh at all times.

�Hide on Drag: Shows the mesh until a point is dragged, then it is hidden, allowing you to see the

surface underneath for fine adjustments.

�Hide: Hides the mesh at all times.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Compositing: Lets you set the composite blend mode for the overlay operation. For more detailed

information on each blend mode, see Chapter 50, “Compositing and Transforms in the Timeline.”

�Composite Type: A drop-down menu of all the possible composite operations.

�Opacity: This slider controls the transparency of the overlay.

The completed surface tracking composites the bee graphic onto his shirt. The composite type was screen, and

the opacity reduced to blend into the shirt. The bee moves realistically as the shirt folds and deforms as he plays.