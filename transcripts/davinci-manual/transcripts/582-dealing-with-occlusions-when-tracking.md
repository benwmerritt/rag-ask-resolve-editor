---
title: "Dealing With Occlusions When Tracking"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 582
---

# Dealing With Occlusions When Tracking

Sometimes you’ll find that you need to deal with a gap in the useful tracking data. For example,

objects in the frame that pass in front of the feature you’re trying to track cause gaps in the tracking

information for a clip.

In situations where a subject being tracked becomes totally occluded by another object in the

frame, there’s an easy method of interpolating to cover holes in the available tracking data.

In the following example, the woman walks behind another fence post, this time one that’s

taller than she is. The window tracking her face will become completely lost at this point, but

interpolation will help to salvage this shot.

Original clip

Interpolating between two sets of tracking data to track past an occlusion:


Move the playhead to the first trackable frame of the moving feature you’re correcting,

and create a Power Window that surrounds it.

Adding the Power Window


Use Track Forward to track the feature as far as you can before it becomes obscured behind

something else in the frame.


When the Power Window stops tracking the feature reliably, stop the track.


Color | Chapter 140 Motion Tracking Windows

COLOR

The Power Window is obscured by the post


Open the Tracker palette.


Click the Frame button to put the Tracker controls into frame-by-frame adjustment mode. This is an

important step.

Selecting Frame mode


Move the playhead to the frame where the feature you’re tracking reappears from behind the

occlusion, then drag the window so that it again overlaps the feature.

Moving the playhead and position the window


Use Track Forward to continue tracking the feature until the end of the clip. Alternately, you

could have started from the end of the clip and used Track Reverse to track the feature as far as

possible, if that’s easier.

Now that you’ve identified the gap in reliable tracking data for this clip, it’s

time to set up the interpolation.

Notice the gap in the tracking data where

the window was behind the post


Color | Chapter 140 Motion Tracking Windows

COLOR


Drag a bounding box over the portion of the curves in the Tracker graph that fall between the

good tracking data at the beginning and end of the shot.


Click the Tracker palette option pop-up menu, and choose Clear Selected Track Data.

The portions of curves that you selected are deleted, and have linear interpolation automatically

applied to them so that there’s no hole in the track data or the motion of the window, which now

moves smoothly from the last outgoing frame of reliable tracking data to the first incoming frame of

new reliable tracking data.

Point Tracker Workflows

As advanced as the Cloud Tracking that is the default in DaVinci Resolve is, there are times when

it may be simpler to track using good old-fashioned crosshairs. The Point Tracker makes it easy to

track very specific features of a subject with motion you need to follow. Unlike the Cloud Tracker,

which automatically looks for all trackable points within a region of the image that you identify using

a window, the Point Tracker lets you create one or more crosshairs that you must manually position

to overlap with whatever high-contrast features you want to track. This section covers the three main

workflows you need to know to use the Point Tracker.

Tracking a Window Using the Point Tracker

The following procedure describes, in a general way, how to use the Point Tracker to track a moving

subject and apply that motion to a Power Window.


Move the playhead to the frame of the current shot where you want to begin (you don’t have to

start tracking at the first frame of a shot, since you can always track backward).


Turn on any window, and adjust it to surround the feature you want to track. Typically, you’ll have

done this anyway, for example, framing someone’s moving face with a Circular window to lighten


Color | Chapter 140 Motion Tracking Windows

COLOR

their highlights. You want to make sure that the window you want to apply the tracked motion to is

selected before you begin tracking. In this example, we’ll be tracking a Circular window to follow

the woman’s face.

Setting up to track a window over a woman’s face


Open the Tracker palette, and choose Point Tracker from the bottom right pop-up.

Choosing the Point Tracker


Before you start tracking, choose what types of motion you want to track and apply to the window

you’re working on. You can choose from among Pan, Tilt, Zoom, Rotate or Perspective 3D. Which

methods of transformation can be applied depend on how many points you add to track.

Choosing what type of motion to analyze


Click the Add Tracker Point icon. A new tracker crosshairs appears in the Viewer in the center of

the frame.

Clicking the

Add Tracker Point icon


Color | Chapter 140 Motion Tracking Windows

COLOR


Move the pointer directly over the tracker crosshairs, and when it turns into the move cursor, click

and drag to move the crosshairs to line up on top of the feature you want to track. For the best

results, this should be a high-contrast detail such as a corner, the end of a line, a small shape like

a pebble, or a jagged detail. Unlike other point trackers, there is no inside or outside region to

separately adjust, there’s only the one crosshairs that you need to align. In this example, this first

crosshairs is placed at the inside of her stage left eyebrow (the corner of her eye would introduce

too much jitter as the tracker will pick up her blinks).

Lining up the tracker crosshairs with the feature you need to track


If you want to improve the accuracy of your track, you can create more tracker crosshairs and

position them on top of other details within the subject you’re tracking. For the best results, make

sure that all crosshairs are placed onto details that are in the same plane of motion. In other words,

don’t put some crosshairs on a person’s face in the foreground, and other crosshairs on a tree

that’s far in the background, since both these features will have very different vectors of motion.

In this example, trackers are placed at her inside eyebrows and at the corner of her lips.

Setting up four trackers to follow the corners of her eyebrows and mouth


Color | Chapter 140 Motion Tracking Windows

COLOR

The final track, accomplished with four point trackers,

with the track path turned on


When you’re done placing crosshairs, click the Track Forward or Track Backward buttons to

initiate tracking. The clip will be analyzed, and the Tracker graph will update with the tracking

data, and the window you had selected automatically moves to match the motion of the feature

you’re tracking.