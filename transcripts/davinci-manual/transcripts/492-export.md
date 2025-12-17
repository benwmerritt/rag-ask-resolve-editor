---
title: "Export"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 492
---

# Export

The Export tab lets you turn the tracked and solved data this node has generated into a form that can

be used for compositing.

The Camera Tracker Export tab

Export

The Export button will create a basic setup that can be used for 3D match moving:

�A Camera 3D with animated translation and rotation that matches the motion of the live-action

camera and an attached image plane.

�A Point Cloud 3D containing the reconstructed 3D positions of the tracks.

�A Shape 3D set to generate a ground plane.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

�A Merge 3D merging together the camera, point cloud, and ground plane. When the Merge 3D is

viewed through the camera in a 3D viewer, the 3D locators should follow the tracked footage.

�A Renderer 3D set to match the input footage.

The export of individual nodes can be enabled/disabled in the Export Options tab.

Update Previous Export

When this button is clicked, the previously exported nodes are updated with any new data generated.

These previously exported nodes are remembered in the Previous Export section at the bottom of this

section. Here’s an example of how this is handy:


Solve the camera and export.


Construct a complex Node Editor based around the exported nodes for use in set extension.


The camera is not as accurate as preferred or perhaps the solver is rerun to add additional tracks

to generate a denser point cloud. Rather than re-exporting the Camera 3D and Point Cloud 3D

nodes and connecting them back in, just press the Update Previous Export button to “overwrite”

the existing nodes in place.

Automatically Update Previous Export After Solves

This will cause the already exported nodes (Camera 3D, Point Cloud 3D, Lens Distort, Renderer 3D,

and the ground plane) to auto update on each solve.

3D Scene Transform

Although the camera is solved, it has no idea where the ground plane or center of the scene is

located. By default, the solver will always place the camera in Fusion’s 3D virtual environment so

that on the first frame it is located at the origin (0, 0, 0) and is looking down the Z-axis. You have the

choice to export this raw scene without giving the Camera Tracker any more information, or you can

set the ground plane and origin to simplify your job when you begin working in the 3D scene. The 3D

Scene Transform controls provide a mechanism to correctly orient the physical ground plane in the

footage with the virtual ground plane in the 3D viewer. Adjusting the 3D Scene Transform does not

modify the camera solve but simply repositions the 3D scene to best represent the position of the live-

action camera.

NOTE: If you export the scene and then make changes in the 3D Scene Transform, it is

important to manually click Update Previous Export to see the results in the exported nodes.

Aligned/Unaligned

The Aligned/Unaligned menu locks or unlocks the origin and ground plane settings. When set to

Unaligned, you can select the ground plane and origin either manually or by selecting locators

in the viewer. When in unaligned mode, a 3D Transform control in the 3D viewer can be manually

manipulated to adjust the origin.

Once alignment of the ground plane and origin has been completed, the section is locked by

switching the menu to Aligned.

Set from Selection

When set to unaligned, buttons labeled Set from Selection are displayed under the Origin, Orientation,

and Scale sections. Clicking these buttons takes the selecting locators in the viewer and aligns the

ground plane or origin based on the selection.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

For instance, to set the ground plane, do the following:


After solving, set the 3D Scene Transform menu to Unaligned.


Find a frame where the ground plane is at its largest and clearest point.


In the viewer, drag a selection rectangle around all the ground plane locators.


Hold Shift and drag again to add to the selection.


In the Orientation section, make sure the Selection Is menu correctly matches the orientation of

the selected locators.


Click the Set from Selection button located under the Orientation parameters.


Set the 3D Scene Transform menu back to Aligned.

To get the best result when setting the ground plane, try to select as many points as possible

belonging to the ground and having a wide separation.

TIP: When selecting points for the ground plane, it is helpful to have the Camera Tracker

node viewed in side-by-side 2D and 3D views. It may be easier to select tracks belonging to

the ground by selecting tracks from multiple frames in the 2D viewer rather than trying to box

select locators in the 3D viewer.

Setting the origin can help you place 3D objects in the scene with more precision. To set the origin,

you can follow similar steps, but only one locator is required for the origin to be set. When selecting a

locator for the origin, select one that has a very low solve error.

Ground Plane Options

These controls let you adjust the ground plane for the scene, which is a crucial step in making sure the

composite looks correct.

Color

Sets the color of the ground plane.

Size

Controls how big the ground plane can be set.

Subdivision Level

Shows how many polygons are in the ground plane.

Wireframe

Sets whether the ground plane is set as wireframe or solid surface when

displayed in 3D.

Line Thickness

Adjusts how wide the lines will draw in the viewer.

Offset

By default, the center of the ground plane is placed at the origin (0, 0, 0).

This can be used to shift the ground plane up and down along the Y-axis.

Export Options

Provides a checkbox list of what will be exported as nodes when the Export button is pressed. These

options are: Camera, Point Cloud, Ground Plane, Renderer, Lens Distortion, and Enable Image Plane in

the camera.

The Animation menu allows you to choose between animating the camera and animating the point

cloud. Animating the camera leaves the point cloud in a locked position while the camera is keyframed

to match the live-action shot. Animating the point cloud does the opposite. The camera is locked in

position while the entire point cloud is keyframed to match the live-action shot.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Previous Export

When the Update Previous Export button is clicked, the previously exported nodes listed here are

updated with any new data generated (this includes the camera path and attributes, the point cloud,

and the renderer).

Options

The Options tab lets you customize the Camera Tracker’s onscreen controls so you can work most

effectively with the scene material you have.

The Camera Tracker Options tab

Trail Length

Displays trail lines of the tracks overlaid on the viewer. The amount of frames forward and back from

the current frame is set by length.

Location Size

In the 3D viewer, the point cloud locators can be sized by this control.

Track Colors, Locator Colors, and Export Colors each have options for setting their color to one of the

following: User Assigned, Solve Error, Take From Image, and White.

Track Colors

The onscreen tracks in the 2D viewer.

Locator Colors

The point cloud locators in the 3D viewer.

Export Colors

The colors of the locators that get exported within the Point Cloud node.

Darken Image

Dims the brightness of the image in viewers to better see the overlaid tracks. This affects both the 2D

and 3D viewers.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Visibility

Toggles which overlays will be displayed in the 2D and 3D viewers. The options are: Tracker Markers,

Trails, Tooltips in the 2D viewer, Tooltips in the 3D viewer, Reprojected Locators, and Tracker Patterns.

Colors

Sets the color of the overlays.

�Selection Color: Controls the color of selected tracks/locators.

�Preview New Tracks Color: Controls the color of the points displayed in the viewer when the

Preview AutoTrack Locations option is enabled.

�Solve Error Gradient: By default, tracks and locators are colored by a green-yellow-red gradient

to indicate their solve error. This gradient is completely user adjustable.

Reporting

Outputs various parameters and information to the Console.

Understanding Camera Tracking

On large productions, camera tracking or 3D match moving is often handed over to experts who have

experience with the process of tracking and solving difficult shots. There is rarely a shot where you

can press a couple of buttons and have it work perfectly. It does take an understanding of the whole

process and what is essential to get a good solved track.

The Camera Tracker must solve for hundreds of thousands of unknown variables, which is a complex

task. For the process to work, it is essential to get good tracking data that exists in the shot for a long

time. False or bad tracks will skew the result. This section explains how to clean up false tracks and

other techniques to get a good solve.

Workflow

Getting a good solve is a repeated process.

Track > Solve > Refine Filters > Solve > Cleanup tracks > Solve > Cleanup from point cloud >

Solve > Repeat.

Initially, there are numerous tracks, and not all are good, so a process of filtering and cleaning up

unwanted tracks to get to the best set is required. At the end of each cleanup stage, pressing Solve

ideally gives you a progressively lower solve error. This needs to be below 1.0 for it to be good for use

with full HD content, and even lower for higher resolutions. Refining the tracks often but not always

results in a better solve.

False Tracks

False tracks are caused by a number of conditions, such as moving objects in a shot, or reflections and

highlights from a car. There are other types of false tracks like parallax errors where two objects are at

different depths, and the intersection gets tracked. These moiré effects can cause the track to creep.

Recognizing these False tracks and eliminating them is the most important step in the solve process.

Track Lengths

Getting a good set of long tracks is essential; the longer the tracks are, the better the solve. The Bi-

Directional tracking option in the Tracker tab is used to extend the beginning of tracks in time. The

longer in time a track exists and the more tracks that overlap in time of a shot, the more consistent and

accurate the solve.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Seed Frames

Two seed frames are used in the solve process. The algorithm chooses two frames that are as far

apart in time yet share the same tracks. That is why longer tracks make a more significant difference in

the selection of seed frames.

The two Seed frames are used as the reference frames, which should be from different angles of the

same scene. The solve process will use these as a master starting point to fit the rest of the tracks in

the sequence.

There is an option in the Solve tab to Auto Detect Seed Frames, which is the default setting and most

often a good idea. However, auto detecting seed frames can make for a longer solve. When refining

the Trackers and re-solving, disable the checkbox and use the Seed 1 and Seed 2 sliders to enter the

previous solve’s seed frames. These seed frames can be found in the Solve Summary at the top of the

Inspector after the initial solve.

Refine Filters

After the first solve, all the Trackers will have extra data generated. These are solve errors and

tracking errors.

Use the refine filters to reduce unwanted tracks, like setting minimum tracker length to eight frames.

As the value for each filter is adjusted, the Solve dialog will indicate how many tracks are affected by

the filter. Then Solve again.

Onscreen Culling

Under the Options tab, set the track to 20. This will display each track on footage with +-20 frame trail.

When scrubbing/playing through the footage, false tracks can be seen and selected onscreen, and

deleted by pressing the Delete key. This process takes an experienced eye to spot tracks that go bad.

Then Solve again.

You can view the exported scene in a 3D perspective viewer. The point cloud will be visible. Move and

pan around the point cloud, select and delete points that seem to have no inline with the image and

the scene space. Then Solve again.

Repeat the process until the solve error is below 1.0 before exporting.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Tracking nodes. These common controls

are described in detail in the following “The Common Controls” section.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION