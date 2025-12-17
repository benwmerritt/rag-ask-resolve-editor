---
title: "Motion Tracking Windows"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 580
---

# Motion Tracking Windows

The Tracker palette has three modes, available from the Palette menu.

�In Window mode, the tracking controls let you match the motion of a window to that of a moving

feature in the frame.

�In Stabilizer mode, the same underlying technology is used to smooth or stabilize the motion

within the entire frame.

�In FX mode a Point Tracker can be used to animate ResolveFX or OFX plugins with

positioning controls.

For more information about the FX and Stabilizer modes,

see Chapter 152, “Sizing and Image Stabilization.”

DaVinci Resolve has an incredibly simple, yet powerful, 3D cloud tracker that allows you to track

quickly and accurately any Power Window (Circular, Linear, Polygonal, Curve, or Gradient) to

follow any moving feature. This avoids the need to use dynamic keyframes to manually animate a

window’s position.

In particular, you can use the tracker to match a window’s position, size, rotation, and its pitch and yaw

in 3D space to either foreground or background elements that move within the frame.

A Power Window tracking a woman’s face

Rotoscoping Window Shapes After Tracking���������������������������������������������������������������������������������������������������������������������� 3199

Rotoscoping Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3200

Keyframing in Frame Mode���������������������������������������������������������������������������������������������������������������������������������������������������������� 3200

A Rotoscoping Workflow����������������������������������������������������������������������������������������������������������������������������������������������������������������� 3201

Viewing a Window’s Motion Path���������������������������������������������������������������������������������������������������������������������������������������������� 3204


Color | Chapter 140 Motion Tracking Windows

COLOR

Simple Tracking Using the Tracker Menu

The simplest way to track a feature using a Power Window is to use the commands found in the

Color > Tracker menu. These commands include:

Track Forward (Command-T): Tracks a window to a feature from the current position of the

playhead forward, ending at the last frame of a clip.

Track Reverse (Option-T): Tracks a window to a feature from the current position of the

playhead backward, ending at the first frame of a clip.

Track Stop (Command-Option-T): Interrupts any track. This is useful for letting you cancel a

long track that goes wrong (the Stop button of a control panel stops tracking as well).

One Frame Forward (Option-Right Arrow): Tracks a window to a feature one frame forward

from the current position.

One Frame Reverse (Option-Left Arrow): Tracks a window to a feature one frame backward

from the current position.

Most window tracks are easy to accomplish using these three commands.

To track any Power Window to match a moving feature within the frame:


Move the playhead to the frame of the current shot where you want to begin (you don’t have to

start tracking at the first frame of a shot).


Turn on any window, and adjust it to surround the feature you want to track.

Typically, you’ll have done this anyway, for example, framing someone’s moving face with a

Circular window to lighten their highlights.


To initiate tracking, do one of the following:

�Choose Color > Tracker > Track Forward (press Command-T).

�Choose Color > Tracker > Track Reverse (Option-T).

DaVinci Resolve automatically opens the Viewer page, places a series of tracking points within the

window you’ve created, and performs the track from the current frame; forward to the last frame or

backward to the first frame.

DaVinci Resolve analyzes a cloud of tracking points that follow the vectors of every trackable group

of pixels within the window you’ve created, and the results are fast and accurate. After tracking, the

window you’ve placed automatically moves, resizes, rotates, and skews to match the motion of the

feature you’re tracking.

Once a clip has tracking data applied to one of its windows, a small tracking icon appears

within that clip’s icon in the Thumbnail timeline.


Color | Chapter 140 Motion Tracking Windows

COLOR

Object tracking in progress. Tracking points are automatically

placed over trackable features of the image

A tracking icon in the top

left corner of the Thumbnail

timeline shows that clip

has been tracked

If the track you’ve performed is unsuitable, you can reposition the window to cover a different area

of the subject you’re trying to track, and initiate tracking again. New tracking data overwrites any

previous tracking data applied to that window.

Once you’re satisfied with your track, you can continue to resize, reposition, or reshape the window

being tracked. Tracking data is separate from the window transform parameters (which can be

keyframed), so changes you make to a window offset it from the originally tracked path.

Tracking Windows Across Transitions

When you track a window that crosses a transition boundary (for example, a dissolve from one clip

to another), DaVinci Resolve will automatically continue the track for the full extent of the video

under the transition.

Tracking Windows When You’ll

Be Exporting Media With Handles

When you track windows to match moving features in a clip, the windows are only transformed on

frames with tracking data. In Round Trip workflows where you add handles to the graded clips you

render for editorial flexibility in the footage you deliver, you need to make sure that you track all

windows from the beginning to the end of these handles to make sure that, if an editor actually trims

any of the clips you give them to use the handles, all windows are doing what they should.

An easy way to do this is to choose View > Show Current Clips With Handles to display each clip

you select in the Timeline with handles defined by the “Default handles length” setting in the Editing

panel of the User Preferences. Make sure that the “Default handles length” is equal to the handles

you export using the “Add X Frame handles” option in the Render Settings list of the Deliver page.

With each clip’s handles made visible in this way, you can easily track windows along every frame

you’ll be rendering.

Simple Ways of Working With Existing Tracking Data

If there’s a portion of a shot that you haven’t tracked (for example, you started tracking at a later frame,

or you ended tracking before the end of the shot), then the window you’re tracking remains wherever it

was at the first or last frame that was tracked. If you want to fill in these gaps, you can always move the

playhead to the first or last frame that was tracked, and then use the Track Backward or Track Forward

command to track the rest of the frames in that shot.


Color | Chapter 140 Motion Tracking Windows

COLOR

Tips for Better Tracking

In situations where a feature changes shape in such a way as to confuse the tracker, you can try

tracking a smaller part of the feature by using a smaller window. Once you’ve achieved a successful

track, you can resize the window as necessary, and it will have no effect on the track that’s already

been made.

Also, if you’re tracking a feature that moves behind something onscreen and disappears for the rest of

the shot, there’s an easy way to avoid having an awkward window sitting in the middle of the scene.

You can use dynamic keyframes to animate the Key Output Gain parameter (in the Key tab of the Color

page) to fade from the correction’s full strength of 1.0 down to 0, the value at which the correction

disappears, along with the window itself.

Tracking One Frame at a Time

You can click the “track one frame forward” or “track one frame backward” buttons in the Tracker

palette to track a moving feature one frame at a time, making it easier to make adjustments to follow a

difficult track when you’ve set tracking to Frame mode (by clicking the Frame button).

In Frame mode, you can keyframe window transformations to more faithfully conform to troublesome

motion as you’re moving one frame at a time through the track; manual changes to a window’s

position will be keyframed to create frame-specific transformations, rather than used to offset the

entire tracked motion path as in Clip mode. When you add multiple keyframes in the Tracker graph,

animation will be automatically interpolated from keyframe to keyframe.

Copying and Pasting Tracking

There will be plenty of times you’ll apply multiple windows to a single moving subject, such as a car,

when you can use a single motion track for all the windows. Commands in the Option menu let you

copy and paste track data from one window to another within the same node, saving time when you

want several windows tracking together as one.

To copy track data from one window to another:


Open the Window palette, then select a window that has tracking applied to it (indicated

by a tracking badge in the corner of the shape icon), and choose Copy Track Data from the

Option pop-up.


Select another window, and choose Paste Track Data from the Option pop-up. Once you’ve

copied track data from one window, you can paste it to as many other windows as you like.

You can also copy tracking from the FX mode of the Tracker palette and paste it to a window, in

case you want to use the same tracking data for both an effect and a window.

To copy track data from an FX track to a window:


Open the Tracker palette, choose the FX mode that contains the tracking data you want to copy,

and choose Copy Track Data from the Option pop-up.


Open the Window palette, select a window, and choose Paste Track Data from the Option pop‑up.

Once you’ve copied track data from one window, you can paste it to as many other windows

as you like.


Color | Chapter 140 Motion Tracking Windows

COLOR

Tracker Palette Controls in More Detail

You can easily combine object tracking and keyframing to animate windows. For example, you’ll

typically use object tracking to make a window follow the position and orientation of a moving feature,

but you can add dynamic marks to the window track of the correction in the Color page with which to

alter its size and shape to better conform to a feature’s changing form.

Controls in the Window Tracker Palette

Occasionally, you’ll run into a shot that doesn’t quite track well enough using the Tracker menu’s

simple controls. In these cases, the Viewer page provides the complete set of object tracking controls

that can be used to modify tracking operations in different situations.

The Tracker palette

The object tracking controls are divided into seven groups.

Tracker Palette Modes

The Tracker palette’s Option drop-down menu lets you choose between Window mode (for

matching a window to the motion of a feature in the frame), Stabilizer mode (for subduing

unwanted camera motion; for more information on Stabilizer mode, see Chapter 152, “Sizing

and Image Stabilization.”), and FX mode (for tracking position to be used with Resolve FX or

Open FX plugins).

Types of Tracking

A pop-up menu below the Tracker graph lets you choose whether to use the Cloud Tracker or the

Point Tracker. There are three options:

The tracker type pop-up


Color | Chapter 140 Motion Tracking Windows

COLOR

The Cloud Tracker: Automatically analyzes all parts of the image for trackable points, and

uses these to automatically figure out the motion in the shot that you want to use to move a

Power Window or stabilize a shot. This tracker type is great for quickly tracking a window to

match the movement of almost any feature, with a minimum of work.

The Point Tracker: Lets you create one or more tracker crosshairs that you can manually

position in order to track specific features in the shot. The more crosshairs you create and

position, the more accurate the track can be. The Point Tracker is incredibly useful in situations

where you need to follow the motion of a very specific feature in the frame. It can also be

useful in cases where you want to stabilize a shot that has many subjects moving in different

directions, and it’s difficult to obtain a good result with the Cloud Tracker.

IntelliTrack: Is a AI tool that doesn’t use predetermined rulesets or heuristics. Instead, it is

trained on real world examples. This makes it less likely to fail in scenarios like tracking a

subject behind brief occlusions. For most cases it will be more precise and more robust than

the normal Point Tracker.

Object Tracking

The object tracking controls provide the most basic tracking functions, some of which are mirrored

within the Color > Tracker menu.

Choose which type of transform you want to track before tracking

A series of five checkboxes let you turn on and off which transforms you’d like motion tracking to apply

automatically to the window. These checkboxes must be selected before you perform a track in order

to restrict the transforms that are used.

Pan and Tilt: Enables tracking of horizontal and vertical position, when you want to transform

a window to follow the location of a tracked subject.

Zoom: Enables tracking of size, when you want to transform a window to resize to follow a

tracked subject.

Rotate: Enables tracking of orientation, when you want to transform a window to rotate with a

tracked subject.

Perspective 3D: Enables tracking of pitch and yaw in 3D space, when you want a window to

skew to follow the orientation of a tracked subject within the scene. Good when you want the

window to “stick” to a surface.

NOTE: Once tracking or stabilization has been done, disabling these checkboxes does

nothing to alter the result. To make changes, you need to enable or disable the necessary

checkboxes first, and then reanalyze the clip.


Color | Chapter 140 Motion Tracking Windows

COLOR

After you’ve defined the transforms you want to use for the track, the analyze controls let you proceed

with the analysis of the subject being tracked.

Track One Frame Reverse button: Motion tracks a single frame in reverse. Useful for slow

tracking of difficult subjects that may require frequent correction.

Track Reverse button: Initiates tracking from the current frame backward, ending at the first

frame of the clip. Good for tracking backward when your best starting point is somewhere

within the middle of the shot.

Pause button: Stops tracking (if you’re fast enough to click this button before

tracking is finished).

Track Forward button: Initiates tracking from the current frame forward,

ending at the last frame of the clip.

Track Forward and Back button: Initiates tracking from the current frame forward, then when

finished, tracks backward from the original selected frame. This allows you a one button

process when tracking from the middle of a shot.

Track One Frame Forward button: Motion tracks a single frame forward. Useful for slow

tracking of difficult subjects that may require frequent correction.

Clip/Frame Controls

Two buttons let you set how manual adjustments to the position of tracked windows affect the

overall track.

Selecting clip or frame to apply adjustments

�Clip: The default mode, in which changes you make to the position of a window are globally

applied to the entire track. For example, if you track a feature, and then move the window, the

window moves along a motion path that’s consistently offset from the original track for the duration

of the clip. Use this mode if you’re happy with the track, but you want to modify the window’s

overall shape and position relative to the motion path it’s following.

�Frame: In this mode, changes you make to the position or shape of a window create a keyframe at

the frame at the position of the playhead. Multiple keyframes are interpolated to create animation

with which you can manually transform a window to solve a variety of problems. This mode is

useful for rotoscoping the shape and position of windows to match a subject that’s tough to

automatically track. Frame mode is also useful for making corrections to individual frames that

were badly tracked, for animating windows to go all the way out of frame along with a subject, or

for making manual, frame-by-frame adjustments to window position to cover untrackable≈sections.

The Tracker Graph

The Tracker graph provides a visual display of the tracking data that’s being analyzed. Each of the

transform controls that can be tracked has an individual curve, which lets you evaluate each tracked

parameter on its own, and each curve is color-coded to match the corresponding label of the tracking

transforms listed above.


Color | Chapter 140 Motion Tracking Windows

COLOR

The Tracker graph showing a curve for each transform control

A vertical slider to the right of the Tracker graph lets you scale the height of the curve data within to

make it easier to see it all within the graph. A horizontal slider at the bottom of the graph allows you to

zoom in and out of the tracker curves, allowing you to see finer detail of the tracking paths. Above the

Tracker graph, a Timeline ruler contains a playhead that’s locked to the playheads in the Viewer and

Keyframe Editor.

You can draw a bounding box in the Tracker graph with which to select a portion of one or more

curves to delete sections of low-quality tracking data using the Clear Selected Keyframes command

found in the Tracker Options menu. To eliminate the current bounding box from the Tracker graph,

click once anywhere within the graph.

Interactive Mode Controls

The Interactive controls, at the bottom-left of the Tracker palette, let you make manual changes

to the automatically generated tracking point cloud that DaVinci Resolve creates when you’re

tracking with the Cloud Tracker, so you can try different ways of obtaining better tracking results in

challenging situations.

Interactive mode controls

�Interactive Mode checkbox: Turns the Interactive tracking mode on and off. When you enter

Interactive mode, you can manually alter the point cloud that DaVinci Resolve uses to track the

feature within the current window. You’ll then make your track while in Interactive mode.

�Insert: Lets you add tracking points to whatever trackable features exist within a bounding box

that you’ve drawn in the Viewer. Inserted tracking points are automatically placed based on

trackable pixels in the image.

�Set Point: Lets you use the cursor (using the DaVinci Resolve Advanced control panel), to

manually place individual tracking points, one by one, with which to track a feature. If there is no

trackable pixel group at the coordinates where you placed the cursor, a tracking point will be

placed at the nearest trackable pixel group.

You must place at least two tracking points at different pixel groups to track rotation, and at least

three to track zoom.

�Delete: Eliminates all tracking points within a bounding box that you’ve drawn in the Viewer.


Color | Chapter 140 Motion Tracking Windows

COLOR

Point Tracker Controls

If you’re using the Point Tracker, then the Interactive Mode controls disappear, replaced by the two

controls of the Point Tracker.

Point Tracker controls

�Add Tracker: Click to create a new tracker that’s automatically positioned in the center of the

frame. Once created, you can drag it using the pointer to line up with the feature you want to track.

You can create as many trackers as you like. Multiple trackers are all tracked at once.

�Delete Tracker: Select any tracker (selected trackers are red, deselected trackers are blue), and

click this button to remove it.

Additional Commands in the Tracker Options Menu

There are some additional commands located in the Tracker Options pop-up menu.

Reset Track Data on Active Window: Lets you delete the tracking data corresponding to the

currently selected window.

Clear Selected Track Data: When you drag a bounding box over parts of one or more curves

in the Tracker graph, this command lets you delete that part of the graph. This is useful when

you want to eliminate sections of low-quality track data. Portions of curves that are cleared

in this way have linear interpolation automatically applied to them, similar to if you used the

Keyframes Interpolation controls.

Delete Keyframe: Deletes tracker graph keyframes at the current position of the playhead.

Clear All Tracking Points: Clears the tracking points in the Power Window at the frame

you are on.

Show Track: Turn this checkbox on to show the motion path produced by the tracking

you’ve done.

Copy Track Data: Lets you copy track data from the currently selected window. Windows can

be selected directly in the Viewer while the Tracker palette is open.

Paste Track Data: Pastes copied track data to the currently selected window. Windows can

be selected directly in the Viewer while the Tracker palette is open.