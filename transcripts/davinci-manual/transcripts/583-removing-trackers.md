---
title: "Removing Trackers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 583
---

# Removing Trackers

If you find that a particular tracker is causing problems, you can remove it by selecting it in the Viewer,

and clicking the Delete Tracker icon, before retracking the subject.

Clicking the Delete Tracker icon

Using Frame Mode to Offset Track

A common issue when point tracking is how to deal with occlusions and times when the tracked

feature moves off screen. In DaVinci Resolve, the solution is to use the Tracker palette’s Frame mode

to move the tracker crosshairs onto another feature to track, while offsetting the resulting motion so

that it continues to follow the original motion path.


In this example, a point tracker crosshairs has been positioned at a corner of a window of a

building that’s being separately adjusted using a Power Window. The window is being used

because, as the woman turns to leave, she covers up most of the other trackable outer edges of

the building, which would ruin the track.

Setting up to track a building moving off screen


Color | Chapter 140 Motion Tracking Windows

COLOR


As the camera pans, the feature being tracked is about to go off frame, which is about to ruin the

track. As this happens, click the Stop Track button.

Stopping the track on the last good frame

of the track, before the tracker goes off screen


Move the playhead back to the last good frame of tracking, and then click the Frame button in the

Tracker palette to go into Frame mode.

Turning on Frame mode, to prepare to offset the track


In Frame mode, you can now drag the tracker to another feature of the building, this time the outer

edge of the roof, that will be better to follow as the building goes out of frame to the left, since the

Power Window will go out of frame before the rightmost corner of the building’s roof does.

Dragging the tracker to another feature

that’s better to track


Now, click the Track Forward button again, and the crosshairs will begin tracking the new feature,

but the motion will be offset, so the movement of the Power Window continues to follow the

original motion path.


Color | Chapter 140 Motion Tracking Windows

COLOR

Tracking an offset feature lets the

window go all the way off screen

The tracker path before and after moving the

tracker crosshairs in Frame mode is smooth and continuous


If you turn on the track path (in the Tracker Option menu), and move the playhead to the frame

where you moved the tracker, you can see that the motion before you moved the tracker and

the motion after continues smoothly along the same path, with no sudden breaks. When you’re

finished, click the Clip button to get out of Frame mode.

Rotoscoping Window Shapes After Tracking

While the DaVinci Resolve trackers are pretty miraculous when it comes to making a window follow

moving subjects, or elements within a moving scene, there will be plenty of times when the final track

isn’t quite perfect.

For example, if you’re trying to isolate someone’s face with a very specific window, and the person

turns their head, then the resulting change of shape is almost certainly going to require you to make

animated adjustments to the window in order to continue making such a specific isolation.

Before and after a window tracking a turning head, the window doesn’t quite

follow the edge of the woman’s face as her head turns


Color | Chapter 140 Motion Tracking Windows

COLOR

Fortunately, the Tracker palette’s Frame mode makes it easy to animate shape changes you make

to windows in order to better follow a moving subject, a task often referred to as rotoscoping.

By following the motion of a moving subject, and making a series of automatically keyframed

adjustments to the window at every point the subject changes speed or direction, you can make a

window isolate a moving target with surprising precision.

Using Frame mode to rotoscope the window to better

follow the edges of her face and the contours of the jaw

Furthermore, you can also use Frame mode to repair imprecise tracks where the window is veering

off course because of quickly or irregularly moving features. In these cases, you have the option of

manually tracking the window in Frame mode to fit the trajectory of the feature, frame by frame.

Lastly, you don’t even have to have performed a track to use the Tracker graph in Frame mode

to keyframe animated changes to a window. In fact, using the Tracker graph in Frame mode can

sometimes be more convenient than using the Keyframe Editor in Auto Keyframe mode, depending on

what you’re doing.

Rotoscoping Controls

The Clip/Frame buttons determine whether or not you’re rotoscoping a shape.

In Clip mode: Any changes you make to a window transform it over the entire duration of

that clip. In other words, you can track a window to a moving feature, and in Clip mode any

changes you make to the size, rotation, position, or shape of the window occur equally from

the beginning to the end of that clip.

In Frame mode: Changes you make to a window automatically create a keyframe at the

bottom of the ruler in the Tracker graph. Making two or more changes to a window in

Frame mode results in automatically interpolated animation from one keyframed window

transformation to the next.

You can freely move back and forth between Clip to Frame modes to make changes to a window.

Even if you’ve keyframed a window to change shape, you can turn on Clip mode and make an overall

change to the window, enlarging it for example, that results in the window being equally enlarged at

every keyframe.

Keyframing in Frame Mode

Once you’ve added keyframes to the Tracker palette, there are a number of ways you can edit them.


Color | Chapter 140 Motion Tracking Windows

COLOR

Methods of working with keyframes in the Tracker graph:

�To add a keyframe: Click the Add Keyframe icon at the upper right-hand corner of the Tracker

graph. It looks similar to the Keyframe icons found in the Edit page Inspector. This is useful for

adding a keyframe to a frame where the window fits the subject well, prior to moving forward

a few frames and making an alteration to the window to follow the subject that will generate

another keyframe.

�To move the playhead from one keyframe to another: Click the Previous Keyframe and Next

Keyframe icons at the upper right-hand corner of the Tracker graph. These controls look similar to

those found in the Edit page Inspector.

�To delete a keyframe: With the playhead on the same frame as the keyframe you want to delete,

open the Tracker option menu, and choose Delete Keyframe.

The Previous Keyframe, New Keyframe,

and Next Keyframe buttons in the Tracker graph

A Rotoscoping Workflow

The following procedure demonstrates how to use a window to rotoscope an onscreen feature that

you want to isolate. In the process, it shows how to set up a window for rotoscoping using the Tracker

palette, and discusses some best practices for rotoscoping efficiently.

To rotoscope or manually track a window using automatic keyframing:


Create a window to isolate the feature you’re wanting to adjust, and use the tracker to make

it follow the motion of the subject. If the window doesn’t follow the contours of the subject as

precisely as you require, then you can begin manually keyframing its shape on top of the tracking

you’ve done to rotoscope the subject.


With the Tracker palette open, click Frame to change the tracking mode.

Clicking the Frame button to

begin keyframing your shape

The best way to use Frame mode for tracking is to either start at the last successfully tracked

frame and work your way forward, or start at the first successfully tracked frame and work your

way backward. This takes the best advantage of the automatic keyframing and interpolation

between keyframes to animate the window you’re transforming smoothly.


With the playhead at either the first or last frame where the window fits the subject you’re

isolating, you can either click the Add Keyframe button at the upper right-hand corner of the

Tracker graph, or wiggle any control point by a pixel or two, to add a keyframe at that frame.

Clicking the Add Keyframe icon

in the Tracker graph


Color | Chapter 140 Motion Tracking Windows

COLOR

Adding a keyframe at the last frame where the window follows the subject’s motion well means

that any future animated changes you make interpolate from this frame forward, rather than from

previous frames where there’s no need for alterations.

Adjusting the window in Frame mode adds a keyframe

While you’re in Frame mode, the changes you make to the window automatically generate a

keyframe in the Tracker palette, which appears at the bottom of the Tracker graph’s timeline.

Keyframes appear in the

Tracker graph ruler

It’s frequently essential to add a keyframe at the last frame where a window conforms well to

the subject you’re trying to isolate, in order to limit window animation from that frame to the next

keyframed transformation, rather than accidentally animating from the beginning of the clip, or

from the next or previous keyframe in the Tracker graph.


Next, move the playhead to the next frame where the window requires adjustment to better fit the

moving subject, and adjust the position of the window, the control points of the window, or both to

isolate the subject as necessary.

Readjusting the window in Frame mode

to follow the subject’s motion

This results in a second keyframe being placed in the ruler of the Tracker graph.


Color | Chapter 140 Motion Tracking Windows

COLOR

Two keyframes creating rotoscoped animation

in addition to any motion tracking that’s applied


With your first two keyframes placed, scrub the playhead back and forth between them to

evaluate how well the window’s animation is automatically interpolating to fit the motion of the

subject you’re isolating. If the window doesn’t follow the motion of your subject well enough,

move the playhead to the frame where the window divergence is the most pronounced and make

another adjustment to correct the shape.

This creates another keyframe.

A frame between the two keyframes you’ve

rotoscoped that needs further adjustment

After adjusting the

in-between frame


When you’re finished making adjustments between your first two keyframes, move the playhead

farther along and add keyframes as necessary to make the window follow the motion of

your subject.

In general, look for the frames where your subject’s motion starts, stops, speeds up, slows down,

or changes direction. As you work, it’s good to try and add the fewest number of keyframes

you can to ensure smooth motion from one to another. Too many keyframed adjustments

made too close together for a smoothly moving subject risks adding jerky motion if you’re not

careful. On the other hand, if you have an erratically moving subject, you may have to add more

keyframes, possibly frame by frame, to achieve the desired result.

TIP: If you’re isolating a subject with a complex shape that moves quite a lot, you might

consider using multiple simple overlapping shapes to track and rotoscope it, rather than a

single complicated one, to make the task easier.


When you’re finished rotoscoping the window, be sure to click the Clip button to switch back

to Clip mode, so you can trim the window’s shape across every keyframe you’ve just created,

if necessary. This will also prevent you from accidentally adding more keyframes if you select

other shapes.


Color | Chapter 140 Motion Tracking Windows

COLOR

This technique requires a bit more work then simply using the Tracker, but it’ll let you quickly

adjust the animation of a window to more tightly conform to a moving subject when you

need an adjustment to be specific to that subject alone. You can also use this technique to

reposition specific motion path points in the middle of an otherwise successful track to make

them fit better, or to add keyframes to the beginning or end of a track when the subject moves

offscreen but the window does not.