---
title: "Solve Tab"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 491
---

# Solve Tab

The Camera Tracker Solve tab

The Solve tab is where the tracking data is used to reconstruct the camera’s motion path along with

the point cloud. It is also where clean up of bad or false tracks is done, and other operations on the

tracks can be performed, such as defining which marks are exported in the Point Cloud 3D. The

markers can also have their weight set to affect the solve calculations.

For example, a good camera solve may have already been generated, but there are not

enough locators in the point cloud in an area where an object needs to be placed, so adding

more tracks and setting their Solve Weight to zero will not affect the solved camera but will

give more points in the point cloud.

Solve

Pressing Solve will launch the solver, which uses the tracking information and the camera

specifications to generate a virtual camera path and point cloud, approximating the motion of the

physical camera in the live-action footage. The console will automatically open, displaying the

progress of the solver.

Delete

Delete will remove any solved information, such as the camera and the point cloud but will keep all the

tracking data.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Average Solve Error

Once the camera has been solved, a summary of the solve calculation is displayed at the top of the

Inspector. Chief among those details is the Average Solve Error. This number is a good indicator

of whether the camera solve was successful. It can be thought of as the difference (measured in

pixels) between tracks in the 2D image and the reconstructed 3D locators reprojected back onto

the image through the reconstructed camera. Ultimately, in trying to achieve a low solve error, any

value less than 1.0 pixels will generally result in a good track. A value between 0.6 and 0.8 pixels is

considered excellent.

Clean Tracks by Filter

Clicking this button selects tracks based on the Track Filtering options. If the Auto Delete Tracks By

Filter checkbox is activated, the selected tracks will be deleted as well.

Clean Foreground Tracks

Clicking this button makes a selection of the tracks on fast-moving objects that would otherwise cause

a high solve error. The selection is determined by the Foreground Threshold slider.

Foreground Threshold

This slider sets the detection threshold for finding the tracks on fast-moving objects. The higher the

value, the more forgiving.

Auto Delete Tracks by Filter

With this checkbox enabled, tracks that are selected by the Clean Tracks By Filter button will be

deleted. Enable the checkbox, and then press Clean Tracks By Filter. Any track that meets the filtering

options is then selected and deleted.

Auto Delete Foreground Tracks

With this checkbox enabled, tracks that are selected by the Clean Foreground Tracks button will be

deleted. Enable the checkbox, and then press Clean Foreground Tracks. Any track that meets the

foreground threshold criteria is deleted.

Accept Solve Error

This slider sets an acceptable maximum threshold level for the solve error. If the solve error is greater

than this value, the Camera Tracker will sweep the focal length setting in an attempt to bring the solve

error under the Accept Solve Error value. If the solver cannot find a solution, the Camera Tracker

will display a message in the console that the solver failed. If a solution cannot be found, ideally

you should try to input the correct focal length or alternatively manually clean some noisy tracks

then re-solve.

Auto Select Seed Frames

With this enabled, the Camera Tracker nominates two frames that will be used as a reference for

initiating the solve. These two frames are initially solved for and a camera is reconstructed, and then

gradually more frames are added in, and the solution is "grown" outward from the seed frames. The

choice of seed frames strongly affects the entire solve and can easily cause the solve to fail. Seed

frames can be found automatically or defined manually.

Disabling this will allow the user to select their own two frames. Manual choice of seed frames is

an option for advanced users. When choosing seed frames, it is important to satisfy two conflicting

desires: the seed frames should have lots of tracks in common yet be far apart in perspective (i.e., the

baseline distance between the two associated cameras is long).


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Refine Focal Length

Enabling this will allow the solver to adjust the focal length of the lens to match the tracking points. You

can prevent the focal length being adjusted by setting the Focal Length parameter in the Camera tab.

Enable Lens Parameter

When enabled, lens distortion parameters are exposed to help in correcting lens distortion

when solving.

�Refine Center Point: Normally disabled, camera lenses are typically centered in the middle of

the film gate, but this may differ on some cameras. For example, a cine camera may be set up for

Academy 1.85, which has a sound stripe on the left, and shooting super35, the lens is offset to

the right.

�Refine Lens Parameters: This will refine the lens distortion or curvature of the lens. There tends to

be larger distortion on wide angle cameras.

NOTE: When solving for the camera’s motion path, a simulated lens is internally created to

model lens distortion in the source footage. This simulated lens model is much simpler than

real-world lenses but captures the lens distortion characteristics important for getting an

accurate camera solve. Two types of distortion are modeled by Camera Tracker:

Radial Distortion: The strength of this type of distortion varies depending on the distance

from the center of the lens. Examples of this include pincushion, barrel, and mustache

distortion. Larger values correspond to larger lens curvatures. Modeling radial distortion

is especially important for wide angle lenses and fisheye lenses (which will have a lot of

distortion because they capture 180 degrees of an environment and then optically squeeze it

onto a flat rectangular sensor).

Tangential Distortion: This kind of distortion is produced when the camera’s imaging sensor

and physical lens are not parallel to each other. It tends to produce skew distortions in the

footage similar to distortions that can be produced by dragging the corners of a corner

pin within Fusion. This kind of distortion occurs in very cheap consumer cameras and is

practically non-existent in film cameras, DSLRs, and pretty much any kind of camera used in

film or broadcast. It is recommended that it be left disabled.

Enable Lens Parameters

When disabled, the Camera Tracker does not do any lens curvature simulations. This is the default

setting and should remain disabled if there is a very low distortion lens or the lens distortion has

already been removed from the source clip. Activating the Enable Lens Parameters checkbox

determines which lens parameters will be modeled and solved for. Parameters that are not enabled

will be left at their default values. The following options are available:

�Radial Quadratic: Model only Quadratic radial lens curvature, which is either barrel or pincushion

distortion. This is the most common type of distortion. Selecting this option causes the low and

high order distortion values to be solved for.

�Radial Quartic: Model only Quartic radial lens curvature, which combines barrel and pincushion

distortion. This causes the low and high order distortion values to be solved for.

�Radial & Tangential: Model and solve for both radial and tangential distortion. Tangential relates to

misaligned elements in a lens.

�Division Quadratic: Provides a more accurate simulation of Quadratic radial lens curvature. This

causes the low and high order distortion values to be solved for.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

�Division Quartic: Provides a more accurate simulation of Quartic radial lens curvature. This causes

the low and high order distortion values to be solved for.

Lower Order Radial Distortion: This slider is available for all simulations. It determines the

quadratic lens curvature.

Higher Order Radial Distortion: This slider is available only for Quartic simulations. Determines

the quartic lens curvature.

Tangential Distortion X/Y: These sliders are available only for Tangential simulations. Determines

skew distortion.

Track Filtering

The Camera Tracker can produce a large number of automatically generated tracks. Rather than

spending a lot of time individually examining the quality of each track, it is useful to have some less

time-intensive ways to filter out large swaths of potentially bad tracks. The following input sliders are

useful for selecting large amounts of tracks based on certain quality metrics, and then a number of

different possible operations can be made on them. For example, weaker tracks can be selected

and deleted, yielding a stronger set of tracks to solve from. Each filter can be individually enabled

or disabled.

Minimum Track Length (Number of Markers)

Selects tracks that have a duration shorter than the slider’s value. Short tracks usually don’t get a

chance to move very far and thus provide less perspective information to the solver than a longer

track, yet both short and long tracks are weighted evenly in the solve process, making long tracks

more valuable to the solver. Locators corresponding to shorter tracks are also less accurately

positioned in 3D space than those corresponding to longer tracks. If the shot has a lot of long tracks,

it can be helpful to delete the short tracks. For typical shots, using a value in the range of 5 to 10 is

suggested. If there are not a lot of long tracks (e.g., the camera is quickly rotating, causing tracks to

start and move off frame quickly), using a value closer to 3 is recommended.

Maximum Track Error

Selects tracks that have an average track error greater than the slider’s value. When tracking, tracks

are automatically terminated when their track error exceeds some threshold. This auto termination

controls the maximum track error, while this slider controls the average track error. For example, tracks

following the foliage in a tree tend to be inaccurate and sometimes may be detected by their high

average error.

Maximum Solve Error

Selects tracks that have a solve error greater than the slider’s value. One of the easiest ways to

increase the accuracy of a camera solve is to select the 20% of the tracks with the highest solve error

and simply delete them (although this can sometimes make things worse).

Select Tracks Satisfying Filters

Selects the tracks within the scene that meet the above Track Filtering values. Note that when this

button is pressed, the tracks that satisfy the filter values are displayed in the Selected Tracks area

of the Solve tab and are colored in the viewer. This button is useful when Auto Select Tracks While

Dragging Sliders is turned off or if the selection, for example, was accidentally lost by mis-clicking in

the viewer.

Auto Select Tracks While Dragging Sliders

When this is ticked on, dragging the above sliders (Minimum Track Length, Maximum Track Error,

Maximum Solve Error) will cause the corresponding tracks to be interactively selected in the viewer.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Operations on Selected Tracks

Tracks selected directly in the viewer with the mouse or selected via track filtering can have the

following operations applied:

Delete

Removes the tracks from the set. When there are bad tracks, the simplest

and easiest option is to simply delete them.

Trim Previous

Cuts the tracked frames from the current frame to the start of the track.

Sometimes it can be more useful to trim a track than to delete it. For example,

high-quality long tracks that become inaccurate when the feature they are

tracking starts to become occluded or when the tracked feature moves too

close to the edge of the image.

Trim Next

Cuts the tracked frames from the current frame to the end of the track.

Rename

Replaces the current auto generated name with a new name.

Set Color

Allows for user-assigned color of the tracking points.

Export Flag

This controls whether the locators corresponding to the selected tracks

will be exported in the point cloud. By default, all locators are flagged as

exportable.

Solve Weight

By default, all the tracks are used and equally weighted when solving for the

camera’s motion path. The most common use of this option is to set a track’s

weight to zero, so it does not influence the camera’s motion path but still has

a reconstructed 3D locator. Setting a track’s weight to values other than 1.0

or 0.0 should only be done by advanced users.

Onscreen display of track names and values are controlled by these

functions:

None

Clears/hides the selected tracks.

Toggle

Swaps the selected tracks and unselected sets.

All

Selects all tracks.

Show Names

Displays the track name. By default, these are numbers.

Show Frame Range

Displays the start and end frame of a track.

Show Solve Error

Displays the amount of solve error of each selected track.

Selected Tracks

This area displays the properties of a track point or group of points. It has options to:

�Clear: Deselects all tracks and clears this area.

�Invert: Deselects the current selected tracks and selects the other tracks.

�Visible: Selects all the trackers at the current frame.

�All: Selects all trackers on all frames.

�Search: Selects tracks whose names contain a substring.

TIP: Also select tracks directly in the 2D viewer using the mouse or in the 3D viewer by

selecting their corresponding locators in the point cloud.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION