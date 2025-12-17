---
title: "Track"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 655
---

# Track

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


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Command-Drag will allow you to lasso multiple mesh points,

and scale, rotate, and stretch them, as needed.

Manually editing the mesh points at a frame only affects that frame directly; it does not affect

neighboring tracking data. However, it does affect neighboring interpolated positions, which

makes it good for tracking from that point onwards. For example:

�Tracking is good until frame 150 when a few points separate from the rest, disturbed by a lighting

change. At frame 150 they can be manually moved back into place, then if tracking is resumed

they will continue with their corrected positions.

�Tracking exists until frame 150, after which there is no data for a few frames until it resumes at 160.

Editing the points at either frames 150 or 160 will cause the intermediate frames to be interpolated

with these changes applied.

�Tracking exists up to frame 150 and at frame 160 onwards, frames 151-159 are interpolated.

At frame 155 some points are adjusted. This creates tracking data at this frame, and now frames

151‑154 interpolate from the last tracked frame to this current one, and then frames 156-159 from

the current to the next tracked frame.

If an object in the frame occludes the tracked surface, for example tracking a mesh on a shirt, and the

person’s arm moves down through the mesh, breaking the track. You may be able to fix this issue by

using an Alpha channel, as described in the Tracking Using a Mask section below.

Tracking data is also visible as keyframes in the Keyframe Editor in the FX node’s Surface Tracker

keyframing data, and it is also accessible as the last control at the bottom of the Track section where

the data at a frame can be created or deleted directly.

�Go to Start: This button will snap the playhead to the first frame that has been tracked, or the

frame where the boundary was created.

�Go To End: This button will snap the playhead to the last frame that has been tracked.

�Tracking Direction Controls: These controls perform the tracking analysis in the direction

indicated. They are from left to right: Track Backwards, Track Backward One Frame, Pause

Tracking, Track Forwards Then Reverse, Track Forwards One Frame, Track Forwards. Using these

controls, you can set the track across the whole clip or limit the tracking to just a section of it.

�Tracking Data Controls: These controls allow you to manipulate the track data after it’s been run.

Remove Tracking Data Before This Frame: Clears all the tracking data before the current frame.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Track From Last Known Match: This button will match the tracking data to the current frame

and connect it to the last frame where tracking data exists. If there has been too much motion

between those times, you can move the points approximately into place and try matching again.

For example, the tracking occurs without issue until frame 150, but something moving across the

scene causes an error in the track for six frames (151-157). The tracking data can be paused before

it hits these frames, or these frame’s tracking data can be deleted after the fact. Then at frame 158

you can press this button to continue the track from the last known good track at frame 150.

Remove Tracking Data At This Frame: Clears the tracking data at the current frame.

Remove Tracking Data After This Frame: Clears all the tracking data after the current frame.

�Interaction Overlays: These buttons control the visibility of the mesh overlays on the Viewer.

Show: Shows the mesh at all times.

Hide on Drag: Shows the mesh until a point is dragged, then it is hidden, allowing you to see the

surface underneath for fine adjustments.

Hide: Hides the mesh at all times.

�Tracking Behavior: These options allow you adjust the way the tracking operates.

Motion Range: Controls how far to search for matches. Increase this slider if the surface is moving

too quickly and the tracking fails to find it.

Mesh Rigidity: Controls how flexible the mesh is. Reduce this slider to make the mesh points more

flexible. This gives you best results if the clip is noise-free and warping smoothly. Increase this

slider to get a “stiffer” tracked surface with less internal warping.

Quality: The tracker can be very computationally intensive; it is recommended to use the Faster

setting while making adjustments to the mesh, then use Better for the final track once all the

parameters have been set correctly.

Tracking Keyframes: Controls the Surface Tracker in the standard Keyframe Editor. You can insert,

delete, and navigate different keyframes from this option.

NOTE: The Surface Tracker creates data at each frame of the source clip. If the source clip is

not at the same frame rate as the timeline, tracking may seem to stutter or skip frames. You

can “bake” retiming into a clip by right-clicking on it on the Edit page and choosing “Render In

Place” to create a result with exactly one frame for every timeline frame.

Result

Once the tracking data is complete, the Result section lets you determine what and how to composite

a video layer on top of the moving surface.

�Output: There are six options for what to do with the resulting tracking data.

Warp Input 2 Onto 1: Warps the Surface Tracker’s second RGB input to the shape and position of

the tracked mesh and composites it onto the clip.

Warp Input 2 Onto Blank: Warps the Surface Tracker’s second RGB input to the shape and

position of the tracked mesh and passes the Alpha channel information, allowing you to perform

the actual composite in another node or effect.

Warp Input 1’s Alpha: Applies the results of the Surface Tracker to the first Key input (the second RGB

and Key inputs are ignored). If the first Key input receives an Alpha channel from another node with,

say, a drawn shape, or a key, or other Alpha data, it can be warped from the first frame to others.

Create Mesh Alpha Mask: Produces an Alpha mask, which follows the position and shape of the

outline of the mesh. All inputs and alphas are ignored.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Stabilize-Warp Input 1: Performs an inverse warp to the Reference Frame (again, this should be

a frame that ideally is as close to and flat-on to the camera as possible). The result is a stationary

image within the boundary with all the lighting changes and details of the surface’s motion shown

on it. This now stabilized image can be modified with any of DaVinci Resolve’s existing tools,

bypassing any issues caused by this area’s motion in the original video clip. Once modified, you

warp the result back onto the original footage by using a copy of the original Surface Tracker node

but with the Rewarp Stabilized Clip setting here instead.

Rewarp Stabilized Clip: Composites the output of the Stabilize-Warp Input 1 selection back onto

the original video clip, after it’s been modified. This option is designed to be used in conjunction

with a copy of a Surface node using Stabilize-Warp Input 1. It seamlessly blends whatever

additional modifications that were made between the two Surface Trackers back together.

�Overlay/Alpha Source: Allows you to select which frames of the overlay or alpha are used to

create the result.

First Frame: Useful for freezing content from an overlay clip to use a still frame as a static texture.

In DaVinci Resolve’s External Matte controls the offset can be chosen, but also you can use the

same frame as the texture reference with Reference Frame.

Reference Frame: Starts at the currently defined reference frame (see below), instead of at frame

0. The reference frame is the frame which the mesh overlay is initially positioned in its “un-warped”

state, and the positioning controls are active.

Each Frame: Treats the overlay or alpha as a clip, warping each frame in turn. This is necessary for

animated overlays or re-warping stabilized content. It should be noted that in the Key controls on

the Color page, when an External Matte is selected, options appear to control the lifetime of the

external clip.

�Expand/Contract: Allows you to add or remove pixels from the edges of the overlay or alpha. It is

important to note that the expanded area is not tracked and will not be stabilized to the content.

�Softness: Blurs the edge of the Expand/Contract tool to blend more realistically into the scene.

�Motion Blur: This slider lets you add motion blur to the overlay to preserve the illusion that it was

actually captured with the scene.

�Overlay Placement: These controls let you set the initial transform options for the image you want

to overlay on the mesh.

Go To Reference: Moves the playhead to the selected reference frame.

Set to Current: Sets the current frame under the playhead as the reference frame.

Reference Frame: Shows the frame number at which the overlay is originally positioned and un-

warped (the point from which the warp to every other frame is calculated). The positioning controls

appear on screen when the clip is at the reference frame. A frame where the surface’s view is

largest and least warped is the best starting point for rendering onto other frames.

Positioning: Lets you choose how to adjust the overlay position.

�Sliders: Choosing this option exposes a set of transform sliders (X/Y position, zoom, rotate, etc.)

that let you manipulate the overlay’s initial position.

�Interactive Canvas: Choosing this option exposes draggable frame controls in the Viewer,

allowing you to transform the overlay using mouse controls. The Viewers shows a large grid with

9 regions; you can drag in any of them to move, skew, or warp the overlay.

�Interactive Pins: Adjusting the image in this mode is done by manually placing control points,

called pins, in the Timeline Viewer. Adding one pin only gives you position control. At least

two points are required for scaling and rotation. Dragging on one of the pins scales or rotates

the image around the other pin. Using three pins, you can create perspective distortions by

dragging any one of the pins. You can add up to four pins for unique corner pinning distortions.

Reset Position: Resets the on-screen overlay back to its default state.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

�Interaction Overlays: These buttons control the visibility of the mesh overlays on the Viewer.

Show: Shows the mesh at all times.

Hide on Drag: Shows the mesh until a point is dragged, then it is hidden, allowing you to see the

surface underneath for fine adjustments.

Hide: Hides the mesh at all times.

�Compositing: Lets you set the composite blend mode for the overlay operation. For more detailed

information on each blend mode, see Chapter 50, “Compositing and Transforms in the Timeline.”

Composite Type: A drop-down menu of all the possible composite operations.

Opacity: This slider controls the transparency of the overlay.

Using the Surface Tracker

The Surface Tracker is a deep and versatile tool that can be used to realistically isolate a moving

surface for a variety of effects. The examples below can get you started on discovering its uses.

Using the Surface Tracker to Composite a Logo onto a Fabric Surface

One of the more common use cases of the Surface Tracker is to overlay a still graphic on top of a

moving surface and have the graphic behave realistically as the surface deforms and warps. In this

example, we will add a simple logo to the back of a jacket.

The first step is to define the boundary of where we want the surface analyzed. For best results, you

need to place the boundary on the surface to be tracked, not around it, and try to find a frame where

the surface is flat on to the camera and as large in the frame as possible.

The next step is to define the Mesh within the

surface to be warped. In this case, we will leave

the Point Locations setting at Automatic to have

the effect apply the mesh points. Ideally, there will

be more than five mesh points for a good track.

Unfortunately, this surface doesn’t have enough

detail to make a good mesh, so we will temporarily

add a Contrast Pop node before the Surface

Tracker in order to artificially enhance its details.

Creating the initial boundary to

isolate the surface of the jacket

where the logo will be applied


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

By adding the Contrast Pop FX

before the Surface Tracker input,

we can artificially increase the detail

inside the boundary, giving it a

better surface to form the mesh.

Next, we will track the Mesh’s motion using the

Track Forward button and leave the rest of the

controls at their defaults. Note that the track

continues to warp and fold correctly, even when

the subject leans back in his chair.

The Tracker analyzes the

Mesh movement throughout

the rest of the video clip.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

With the surface now correctly analyzed, we no longer need the Contrast Pop node, so we can

disconnect it at this point. Next, we will drag the logo (a .png file with transparency) from the Media

Pool, over into the node tree, where it comes in as a matte. We then add a corrector node after the

matte, so we can adjust the color/saturation/brightness, etc. of the logo. Next, we set the RGB and Key

connections of the nodes through the matte and corrector nodes, and into the second RGB and Key

inputs of the Surface Tracker. This is shown on the node tree below:

The node tree, showing the layout of the RGB and Key inputs to composite the logo over the jacket

Now, moving to the Result section, we set the following parameter:

Output: Warp Input 2 onto 1

This will take the second RGB and Key input (logo) and deform it over the original image coming in to

RGB input 1.

Then we will click on the Go To Reference button to take the clip to its reference frame, and in

Positioning, use the Interactive - Canvas tool to reframe the logo to look like it’s on the same plane as

the jacket.

Adjusting the logo in the

Interactive Canvas mode

to transform it to make it

appear it’s in the same

plane as the jacket


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

For the last step, we change the Composite Type from Normal to Overlay to make the logo blend in

better to the surface of the jacket. Notice how the logo is deformed by the mesh to wrap around the

curves and folds of the jacket, and it tracks along with the man as he leans back in his chair.

The finished Surface Tracker

composite; the logo now adheres

to the curves and folds of the

jacket and tracks along with the man

as he shifts positions in his chair.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Tracking Using a Mask in the Surface Tracker

If there is an object occluding the surface to be tracked, then an input key can be used as a tracking

mask to exclude the blocking object from the track. Areas of full alpha (completely white) in the Alpha

channel are analyzed for tracking, while other areas are excluded. Any appropriate effect, window, or

qualifier can be used as the Alpha channel generator. For example, in the shot below, the path has

the surface mesh applied to it, however the woman walking over the path breaks the mesh tracking.

By connecting a node’s key output with a Magic Mask applied to it that picks out the shape of the

walking woman, then inverting that mask (so the woman is black, while her surroundings are white),

the mesh ignores her legs and feet as they pass through it and only tracks points in the white areas

(everything other than the woman).

A problem trying to track the path’s surface; as the woman walks through the mesh, the points attach

themselves to her feet instead of the path, breaking the tracking on the right side of the path.

By connecting an inverted key from a Magic Mask node of just the woman, the tracking ignores the woman

walking through the mesh (anything black), and only tracks points in the white part of the Alpha channel.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

The resulting mesh is now properly attached to the path’s right side and tracks correctly as she walks through it.

In the final step of the Surface Tracker, the overlay with alpha is composited over the original clip with

alpha, so if using a tracking mask, it is recommended to disconnect it from the Surface Tracker’s key

input after the tracking is complete.

Using the Surface Tracker’s Stabilize Warp

The Surface Tracker’s Stabilize Warp operation allows you to use the mesh to freeze a section of video

in place to make it easier to use with certain other operations. This is useful when the surface you

are modifying is difficult to isolate with other tools due to its movement. Using the Surface Tracker to

stabilize areas is a bit different to set up.

�Initially you want to set the Surface Tracker’s mesh tracking on a surface you want to work on, as

explained earlier in this chapter.

�Once complete, in the Result section you use the Output mode called Stabilize-Warp Input 1, and

then feed that RGB output to a new corrector or FX node.

�This will isolate just the mesh surface and freeze it in place, allowing you to make any adjustments

needed. This method is different than, say, a window qualifier, which sticks to the video and moves

with it. In Stabilize Warp, the “window” (actually the mesh defined boundary) is frozen in place

instead, and the video moves and warps within it.

�Once your adjustments are finished, you then feed the RGB output of the corrector node back into

an exact copy of the first Surface Tracker node. The copied Surface Tracker node’s Output then

needs to be set to Rewarp Stabilized Clip instead. This re-lays the adjusted mesh back on to the

original video clip. Directly copying an FX node like the Surface Tracker is not currently supported.

To copy the Surface Tracker, you must grab a still into your Gallery, then right-click on it and

append the still’s node graph back into your same clip, deleting the excess duplicate nodes other

than the Surface Tracker.

For example, in the clip below we will use the Surface Tracker to remove a small mole from

the woman’s chin. Normally, we could use a Patch Replacer FX to put a smooth area of skin

nearby over the mole. This shot is tricky to use effectively in the Patch Replacer because the

subject cocks her head while she’s talking, as the camera trucks around her.

This movement on all axes means that the area of skin underneath the source patch is

changing angle and lighting all the time, ruining the effect. While the patch replacer does


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

support tracking, the mole is on her chin and her talking also causes the skin around her

cheek to deform, making it unsuitable for a simple track.

In this case, we can use the Surface Tracker’s Stabilize Warp function to “hold” those face area

pixels in place under the source and target patches, patch them, and then make a Rewarp

Stabilized Clip version of the Surface Tracker to lay those corrected pixels back onto the

original image.

We want to remove this mole from the woman’s chin. Because of camera movement,

combined with her chin and cheek deforming as she talks, this is difficult to achieve with

the Patch Replacer alone.

First we will create a mesh on her face and track it as described above. Making holes for the

eyes and mouth so their rapid movement does not disturb the mesh on her face.

We apply the mesh to her face and track it, leaving

holes in the mesh for her eyes and mouth.

Once the tracking is complete, in Result we will choose the Output mode Stabilize-Warp

Input 1. This will freeze the mesh in place and give us the resulting output, which we will feed

into a Patch Replacer node. Now we can simply use the Patch replacer statically to hide the

mole using another area of skin. No tracking is required. Because the mesh is static, and the

video warps within it, this area now perfectly matches the angles, lighting changes, and skin

stretching of the area as she talks.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

The frozen mesh stays in place (the face) and the video warps inside it. This allows us to

use a static Patch Replacer to replace the mole area, with a smooth area on her cheek. No

additional tracking is required.

At this point, we will then make an exact copy the Surface Tracker node, and place it after the Patch

Replacer. To copy the Surface Tracker node, we must grab a still of the current clip, and then right-click

on the still in the Gallery and select Append Node Graph to duplicate it back into our node tree. We

want to delete any excess nodes added, and keep only the copy of the Surface Tracker. Then in the

copied Surface Tracker, we need to select “Rewarp Stabilized Clip” from the Result tab’s Output mode.

Then connect the original clip to RGB input 1, and the output from the Patch Replacer to RGB input 2,

as shown in the node graph below:

The node tree showing the correct setup for Warp Stabilizing the mesh. The first Surface Tracker node has

its Result Output set to “Stabilize-Warp Input 1.” The second copy of the Surface Tracker node has its Result

Output set to “Rewarp Stabilized Clip.” The actual mole removal will take place in the Patch Replacer FX node.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Our finished effect now shows that the mole has been replaced, and regardless of her jaw movement

or the camera position, the source patch always matches perfectly to the lighting and position changes

over time. This makes for a much more seamless and convincing effect.

The resulting shot perfectly hides the mole (above),

no matter her facial position or camera movement.