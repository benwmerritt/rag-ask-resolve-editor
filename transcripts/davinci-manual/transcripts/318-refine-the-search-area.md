---
title: "Refine the Search Area"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 318
---

# Refine the Search Area

A second rectangle with a dotted border surrounds the pattern box. This is the search area. When

progressing from one frame to another while tracking, the Tracker analyzes the region defined by the

search area, which surrounds the last known tracker position in an attempt to relocate the pattern. The

larger the search area, the better chance you have of successfully tracking fast moving objects, but

the longer the track will take. However, there are some ways to optimize tracking for specific content.

For example, tracking a pattern that is moving quickly across the screen from left to right requires a

wide search area but does not require a very tall one, since all movement is horizontal. If the search

area is smaller than the movement of the pattern from one frame to the next, the Tracker will likely fail

and start tracking the wrong pixels, so it’s important to take the speed and direction of the motion into

consideration when setting the search area.

You can resize the search area by dragging

the edges of the dotted outline

Perform the Track Analysis

Before you begin analyzing, you’ll need to make sure you’ve set a render range in the Time Ruler that

corresponds to the range of frames during which the pattern is visible. This may be an entire clip or

only a small portion of that clip. Depending on the type of motion you’re tracking, you may want to use

the Adaptive Mode option to aid the analysis (see below for more details).

Once your options are set, you can use any of the tracking transport buttons at the top of the Inspector

to start tracking. Once tracking has started, you cannot work in the Node Editor until it has completed.

The tracking transport buttons and analysis parameters


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

To begin tracking, do one of the following:

�Click the Track Reverse button to track from the very end of the render range.

�Click the Track Backward from Current Frame button to track backward from the

current playhead position.

�Click the Track Forward button to track from the very start of the render range.

�Click the Track Forward from Current Frame button to track forward from the current

playhead position.

Pattern tracking will stop automatically when it reaches the end of the render range (or the start when

tracking backward), but you can also interrupt it and stop tracking at any time.

To stop tracking, do one of the following:

�Click the Stop Tracking button in the tracker transports.

�Click Stop Render at the bottom of the Fusion window.

�Press the Escape key.

When tracking is complete, the path will be connected to the pattern. The path from that pattern

can now be connected to another node or used for more advanced operations like stabilization

and corner positioning.

Once the track is complete, assuming it’s good, you can use the various techniques in this chapter to

use the track in your composition.

Tips for Choosing a Good Pattern

The Tracker works by searching each frame for the pixels contained in the pattern. In order for a track

to be successful, a fairly high contrast and unique region of the image must be located in the footage.

This process is known as pattern selection.

The first step in pattern selection is to review the footage to be tracked several times. Watch for

candidate patterns that are visible through the entire range of frames, where the contrast is high and

the shape of the pattern does not change over time. The more unique the pattern, the more likely the

track is to be successful.

In addition to locating high contrast, defined patterns, watch for the frames where the pattern moves

the most. Identifying the maximum range of a pattern’s motion will help to determine the correct size

for the pattern search area.

It is not uncommon to have a scene that requires the use of several different patterns to generate a

single path. This most often occurs because the pattern moves out of frame or is temporarily obscured

by another scene element. Combining patterns into a single pattern is described later in the chapter.

Selecting the Pattern’s Image Channels

When a pattern of pixels is selected, the Tracker automatically selects the color channel used

for tracking the pattern based on an analysis of each channel for contrast, clarity, and reliability.

The channels selected are highlighted in the bars to the right of the Pattern display window in the

node controls.


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Highlighted channel bars indicate which

channel is selected for tracking

You can override the automatic channel selection by clicking the buttons beneath the bars for each

channel to determine the channel used for tracking.

You can choose any one of the color channels, the luminance channels, or the alpha channel

to track a pattern.

When choosing a channel, the goal is to choose the cleanest, highest contrast channel for use in the

track. Channels that contain large amounts of grain or noise should be avoided. Bright objects against

dark backgrounds often track best using the luminance channel.

Selecting Patterns for Stabilization

Selecting patterns for stabilization can be a tricky business. The location of the pattern, when it is

selected, is used to determine precisely how the image will be stabilized. At least two patterns are

required to correct for rotation; using three patterns will correct for scaling, and more will usually

improve the quality of the solution.

Try not to select just any potentially valid pattern in the sequence, as some patterns will make the

solution worse rather than better. To help with your selection, use the following guidelines when

selecting patterns for stabilization.

�Locate patterns at the same relative depth in the image. Objects further in the background will

move in greater amounts compared to objects in the foreground due to perspective distortion.

This can confuse the stabilization calculations, which do not compensate for depth.

�Locate patterns that are fixed in position relative to each other. Patterns should not be capable of

moving with reference to each other. The four corners of a sign would be excellent candidates,

while the faces of two different people in the scene would be extremely poor choices for patterns.

Using the Pattern Flipbooks

Each pattern has a pair of thumbnail windows shown in the Inspector. The left window shows the

selected pattern, while the right window is updated during the track to show the actual pattern that has

been acquired for each frame.

The Tracker Pattern Selection and Flipbook thumbnails


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Each pattern that’s stored is added to a Flipbook. Once the render is complete, you can play this

Pattern Flipbook to help you evaluate the accuracy of the tracked path. If you notice any jumps in the

frames, then you know something probably went wrong.

Using Adaptive Pattern Tracking

Even the most ideal pattern will usually undergo shifts in profile, lighting conditions, and other

variables. These can adversely affect pattern recognition to the point that a pattern becomes

unusable. The Tracker offers three modes of pattern acquisition during tracking that can help to

correct these conditions. The modes can be set using the Adaptive Mode options in the Inspector.

The Adaptive Mode options

None

When the Adaptive mode is set to None, the pattern within the rectangle is acquired when the pattern

is selected, and that becomes the only pattern used during the track.

Every Frame

When Every Frame is chosen, the pattern within the rectangle is acquired when the pattern is

selected, and then reacquired at each frame. The pattern found at frame 1 is used in the search on

frame 2, the pattern found on frame 2 is used to search frame 3, and so on. This method helps the

Tracker adapt to changing conditions in the pattern.

Every Frame tracking is slower and can be prone to drifting from sub-pixel shifts in the pattern from

frame to frame. Its use is therefore not recommended unless other methods fail.

Best Match Tracking

Best Match tracking works in much the same way as Every Frame tracking; however, it will not

reacquire the pattern if the difference between the original pattern and the new one is too great. This

helps to prevent cases where transient changes in the image cause the Tracker to become confused.

As a comparison between the two Adaptive modes, if a shadow passes over the tracker point, the

Every Frame tracking mode may start tracking the shadow instead of the desired pattern. The Best

Match mode would detect that the change from the previous frame’s pattern was too extreme and

would not grab a new pattern from that frame.

The Adaptive mode is applied to all active patterns while tracking. If you only want some patterns to

use the Adaptive mode, disable all other patterns in the list before tracking.


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Dealing with Obscured Patterns

Often, an otherwise ideal pattern can be temporarily obscured (occluded) or blocked from tracking—

for example, when tracking a car that passes behind a telephone pole.

In these situations, you divide the render range up into two ranges, the range before the pattern

is obscured and the range after the pattern becomes visible again. After tracking the two ranges

individually, the Tracker will automatically interpolate between the end of the first range and the start

of the second.

If you need to edit the resulting motion path to account for any non-linear motion that takes place

between the two tracked ranges, you can select the track path to expose a Node toolbar with controls

for adjusting the control points on this path. For example, you can choose Insert and Modify mode to

insert points in the non-tracked range to compensate for any nonlinear motion in the tracked pattern.

Tools for modifying tracker paths in the Node toolbar of the viewer

Dealing with Patterns That Leave the Frame

There are two options when a tracker leaves the frame. If the pattern re-enters the frame, you can treat

it like an obscured pattern. If the pattern does not re-enter the frame, or it is undesirable to hand track

portions of the movement, you can use the Track Center (Append) mode to select a new pattern.

The Track Center (Append) mode pop-up menu

The Track Center (Append) mode selects a new pattern that will continue to add keyframes to the

existing path. The offset between the old pattern and the new pattern is automatically calculated to

create one continuous path.

To use the Track Center (Append) mode, do the following:


When the pattern has become untrackable for some reason, stop analysis and move the playhead

to the last frame that tracked successfully.


Choose Track Center (Append) from the Path Center pop-up menu in the Inspector.


Now, drag the Pattern selector to a new pattern that can be tracked from that point onward.


Restart tracking from the current frame.


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

When selecting a pattern to use in appending to an existing path, a pattern that is close to the old

pattern and at the same apparent depth in the frame generates the best results. The further away

the new pattern is, the more likely it is that the difference in perspective and axial rotation will reduce

accuracy of the tracked result.