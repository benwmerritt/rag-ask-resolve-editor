---
title: "3D View"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 336
---

# 3D View

The second output of the Camera Tracker node displays a 3D scene. To view this, connect this 3D

output to a 3D Transform or Merge 3D node and view that tool.

After solving, connecting the second output of the Camera Tracker

node to a Merge 3D displays the point cloud in 3D

After an initial solve, the 3D output displays the point cloud and the camera, along with the image

connected to it. Selecting points displays the Camera Tracker toolbar above the viewer, which gives

control of various functions, such as renaming, deleting, and changing the colors of points in the

point cloud.

3D output of a point cloud and a solved camera path


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION

Auto-Tracking in the Camera Tracker

Tracking is the term used to describe the task of observing or analyzing a sequence of frames (or clip).

The Camera Tracker node must take into account the movement of the source footage before it can

determine the location and movement of the virtual camera. The Camera Tracker tool automatically

searches for features that are high-contrast patterns within the clip and assigns trackers to those

features. Having a wide distribution of tracking points across the frame and having points with long

durations results in the best track.

Increasing Auto-Generated Tracking Points

Unlike the Tracker node, setting tracking points is entirely automatic in the Camera Tracker, but the

Detection Threshold and Minimum Feature Separation sliders let you adjust the criteria by which

tracking points are found. Lowering these parameters lets you increase the number of tracking points

that will be found. This can be useful if the scene has too few points, which will prevent the solver from

generating an accurate camera and point cloud. However, make these adjustments with care, since

adding too many points may generate redundant trackers that slow down the entire process with

minimal benefit.

Previewing Tracking Points

You can view the tracking points currently generated on the clip by viewing the Camera Tracker node

and turning on the Preview AutoTrack Locations checkbox. This causes green tracking points to be

displayed in the viewer as you play through the clip. Using this preview, you can decide whether you

need to make adjustments to the Detection Threshold or Minimum Feature Separation to increase or

decrease the number of tracking points that are found automatically.

Green tracker marks are added automatically to the features in an image

Bi-Directional Tracking

When performing a track, you can enable the Bidirectional Tracking checkbox, which first tracks

forward from the start of the clip, and then tracks a second pass in reverse. This two-pass approach

can potentially extend the duration of any given point by re-analyzing points initially identified in

the forward pass. There is very little reason not to have this enabled unless you are very short on

time. Bidirectional tracking takes longer, but it’s usually worth it, and the process is reasonably quick

considering the benefit.


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION

Choosing a Tracking Algorithm

There are three available choices for the algorithm to use when tracking. The three options in the

New Track Defaults section of the Inspector include:

�Optical Flow: Usually your best choice, unless you have a great deal of criss-crossing

objects in a clip.

�Tracker: A good second choice when Optical Flow can’t be used due to motion estimation errors

like criss-crossing objects.

�Planar: Mostly used in simpler clips, where the majority of the image consists of planar surfaces

such as the facades of buildings.

Masking Out Objects

When tracking a clip, the Camera Tracker automatically generates trackers on feature details.

However, not all features that stand out in a clip are appropriate for camera tracking. You only want

to track features that are “nailed to the set.” In other words, objects that move independently of the

camera motion, like moving cars and people, cause inaccuracies when camera tracking. You must

eliminate these types of objects from the analysis.

The primary way of avoiding these problem areas is by masking. You connect a mask to the Camera

Tracker node’s Track Mask input to identify areas of a scene that the Camera Tracker can analyze. For

example, if you have a clip of an airport runway along a shoreline, the waves of the water and moving

clouds in the sky must be masked since they move independently of the camera.

When creating a mask, the fixed areas of the image to be analyzed for tracking should be

encompassed in the white portion of the mask. All moving objects that need to be ignored should be

encompassed in the black portion. The mask should then be attached to the Camera Tracker Track

Mask input.

Masks used to omit the moving clouds and waves from being tracked by the Camera Tracker


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION

By doing this, the tracker ignores the waves of the water and moving clouds. Unlike drawing a mask

for an effect, the mask in this case does not have to be perfect. You are just trying to identify the rough

area to occlude from the tracking analysis.

The original image to be tracked (left), and the occlusion mask of the clouds and water (right)

TIP: If there’s a lot of motion in a shot, you can use the Tracker or Planar Tracker nodes to

make your occlusion mask follow the area you want to track. Just remember that, after using

the PlanarTracker or PlanarTransform node to transform your mask, you need to use a Bitmap

node to turn it back into a mask that can be connected to the Camera Tracker node’s Track

Mask input.

Matching the Live-Action Camera

Once you have completed tracking, the next stage of this workflow requires the controls in the

Camera tab. This is where you define the actual camera used on set, primarily the film gate size

and focal length. This information should have been logged on the set to make available for post-

production. When using camera-original media, you can sometimes locate this information in the file

metadata.

To locate camera metadata, do the following:

�If you are using DaVinci Resolve, select the MediaIn node with the camera clip, open the Metadata

Editor, and view the Camera metadata preset.

�If you are using Fusion Studio, display the metadata subview from the viewer toolbar.

The Camera tab in the Camera Tracker tool


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION

If the actual values are not known, try a best guess. The solver attempts to find a camera near these

parameters, and it helps the solver by giving parameters as close to the live action as possible. The

more accurate the information you provide, the more accurate the solver calculation. At a minimum, try

to at least choose the correct camera model from the Film Gate menu. If the film gate is incorrect, the

chances that the Camera Tracker correctly calculates the lens focal length become very low.

Unlike the Track and Solve tabs, the Camera tab does not include a button at the top of the Inspector

that executes the process. There is no process to perform on the Camera tab once you configure the

camera settings. After you set the camera settings to match the live-action camera, you move to the

Solve tab.

Running the Solver

The next step in this workflow involves the controls found in the Solve tab. Solving is a

compute‑intensive process in which the Camera Tracker analyzes the currently existing tracks

to create a 3D scene. It generates a virtual camera that matches the live action and a point cloud

consisting of 3D locators that recreate the tracked features in 3D space. The analysis is based on

parallax in the frame, which is the perception that features closer to the camera move quicker than

features further away. This is much like when you look out the side window of a car and can see

objects in the distance move more slowly than items near the roadside.

The trackers found in the Track phase of this workflow have a great deal to do with the success or

failure of the solver, making it critical to deliver the best set of tracking points from the very start.

Although the masking you create to occlude objects from being tracked helps to omit problematic

tracking points, you almost always need to further filter and delete poor quality tracks in the

Solver tab. That’s why, from a user’s point of view, solving should be thought of as an iterative process.

To solve a camera’s motion:


Click the Solve button to run the solver.


Filter out and delete poor tracks.


Rerun the solver.

The Solver tab after it has run and produced

an average solve error of 04367 pixels


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION