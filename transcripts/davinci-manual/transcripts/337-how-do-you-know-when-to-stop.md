---
title: "How Do You Know When to Stop?"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 337
---

# How Do You Know When to Stop?

At the end of the solve process, an Average Solve Error (sometimes called a reprojection error)

appears at the top of the Inspector. This is the crucial value that tells you how well the calculation has

gone. A good Average Solve Error for HD content is below 1.0.

You can interpret a value of 1.0 as a pixel offset; at any given time, the track could be offset by 1 pixel.

The higher the resolution, the lower the solve error should be. If you are working with 4K material, your

goal should be to achieve a solve error below 0.5.

Tips for Solving Camera Motion

When solving camera movement, it’s important to provide accurate live-action camera

information, such as focal length and film gate size, which can significantly improve the

accuracy of the camera solve. For example, if the provided focal length is too far away from

the correct physical value, the solver can fail to converge, resulting in a useless solution.

Additionally, for the solver to accurately triangulate and reconstruct the camera and point

cloud, it is important to have:

•	 A good balance of tracks across objects at different depths, with not too many tracks

in the distant background or sky (these do not provide any additional perspective

information to the solver).

•	 Tracks distributed evenly over the image and not highly clustered on a few objects or

one side of the image.

•	 The track starts and ends staggered over time, with not too many tracks ending on

the same frame.

Using Seed Frames

The solver works by first constructing a partial solution between two seed frames. These seed

frames are selected automatically. However, automatic selection adds time to the process. The time is

reported in the solve summary at the top of the Inspector once you run the solver. You can select your

own seed frames to speed the process and potentially get a better solve on trickier clips. The solver

uses these seed frames to create an intermediate solution and then extends this forward and

backward for the duration of the clip.

Selecting appropriate seed frames is not necessarily recommended unless you have some experience

with camera tracking. Keeping the default Auto Select Seed Frames checkbox enabled in the Solve

Options section of the Solver tab selects the best frames in most cases. However, you can disable the

checkbox and use the Seed Frame 1 and Seed Frame 2 slider to select frames you believe achieve

better results.

When choosing seed frames, it is important to satisfy two main characteristics:

�Seed frames should have lots of tracks in common.

�Seed frames should be far apart in perspective.

Sometimes There’s Nothing You Can Do

Some shots that do not have enough camera motion to triangulate feature locations cannot

be reconstructed with any useful accuracy. Ensuring that a shot is camera-trackable begins

on set, with proper usage of track markers, and by ensuring that camera moves have enough

perspective shifts for the solver to glean useful data from.


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION

Cleaning Up Camera Solves

Sometimes the first solve will be good enough. Other times, it may take a few hours of cleaning

up tracks to get a good solve, and sometimes it is impossible. With experience, one gets a feel for

which tracks should be deleted and which should be kept, and which shots will be easy, difficult, or

impossible to solve.

Be aware that deleting too many tracks can cause the Average Solve Error to increase, as the solver

has too little information to work with. In particular, if there are fewer than eight tracks on any frame,

mathematically there is not enough information to solve the clip. However, it is strongly recommended

to use a lot more than eight tracks to get a robust and accurate solve.

IMPORTANT: If you are not familiar with camera tracking, it may be tempting to try to directly

edit the resulting 3D splines in the Spline Editor in order to improve a solved camera’s motion

path. This option should be used as an absolute last resort. It’s preferable, instead, to modify

the 2D tracks being fed into the solver.

How to Judge Track Accuracy

The automatic color coding of tracking markers makes deleting false or poor tracks easier. After the

solver runs, each tracker is assigned a solve error color that indicates which 3D locators match their

2D tracking points well, and which match up poorly.

Green: Good. Tracked very well.

Yellow: Moderate confidence. Usually an acceptable track.

Orange: Low Confidence. May be acceptable in some situations.

Red: No Confidence. The tracks have not solved well.

Hovering the pointer over any tracking point displays a large metadata tooltip that includes the solve

error for the point. For a more visual representation of the accuracy, you can enable the display of

3D locators in the viewer by clicking the Reprojection Locators button in the viewer toolbar.

After a solve, the Camera Tracker toolbar can display Reprojection locators

When the tracking points are converted into a point cloud by the solver, it creates 3D reprojection

locators for each tracking point. These Reprojection locators appear as small X marks near the

corresponding tracking point. The more the two objects overlap, the lower the solve error.


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION

Reprojection locators displayed with tracking points, and tooltip

The goal when filtering the trackers is to remove all red tracker marks and keep all the green marks.

Whether you decide to keep both the yellow and orange or just the yellow is more a question of

how many marks you have in the clip. You produce a better solve if you retain only the yellow marks;

however, if you do not have enough marks to calculate the 3D scene, you will have to keep some of

the better orange marks as well.

Tips for What to Keep and What to Delete

Understanding what false tracks look like, and then manually cleaning the track data to

reduce it to a precise set of clear tracks, will result in a more accurate solve. When cleaning up

any track—particularly yellow and orange color coded tracks—keep the following in mind:

•	 Keep all tracks with motion that’s completely determined by the motion of the

live‑action camera.

•	 Delete tracks on moving objects or people and tracks that have parallax issues.

•	 Delete tracks that are reflected in windows or water.

•	 Delete tracks of highlights that move over a surface.

•	 Delete tracks that do not do a good job of following a feature.

•	 Delete tracks that follow false corners created by the superposition of

foreground and background layers.

•	 Consider deleting tracks that correspond to locators that the solver has reconstructed

at an incorrect Z-depth.

Deleting Tracks

You can manually delete tracks in the viewer or use filters to select groups of tracks. When deleting

tracks in the viewer, it is best to modify the viewer just a bit to see the tracks more clearly. From

the Camera Tracker toolbar above the viewer, clicking the Track Trails button hides the trails of the

tracking points. This cleans up the viewer to show points only, making it easier to make selections.

At the right end of the toolbar, clicking the Darken Image button slightly darkens the image, again

making the points stand out a bit more in the viewer.

Hiding trails and darkening the viewer can make

it easier to see and select poor tracks


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION

To begin deleting poor-quality tracks, you can drag a selection box around a group of tracks you

want to remove and then either click the Delete Tracks button in the Camera Tracker toolbar or press

Command-Delete.

You can hold down the Command key to select discontiguous tracking marks that are not near each

other. If you accidentally select tracks you want to keep, continue holding the Command key and drag

over the selected tracks to deselect them.

When deleting tracks, take note of the current Average Solve Error at the top of the Inspector and

then rerun the solver. It is better to delete small groups of tracks and then rerun the solver than to

delete one or two large sections. As mentioned previously, deleting too many tracks can have adverse

effects and increase the Average Solve Error.

Using Filters to Delete Problem Tracks

The Solve tab includes filters that can be used to select groups of similar tracks by track length, track

error, and solve error. These can be used to quickly select and delete poorly performing tracks that

may be misleading to the resulting camera, leaving a concise list of accurate tracks.

Tracks can be selected using filters and deleted

using the Operations On Selected Tracks buttons

For instance, it is generally best to run the solver using tracks with longer durations. Since shorter

tracks tend to be less accurate when calculating the camera, you can remove them using the Filter

section in the Inspector.

Increasing the Minimum Track Length parameter sets a threshold that each tracker must meet. Tracks

falling below the threshold appear red. You can then click the Select Tracks Satisfying Filters button to

select the shorter tracks and click Delete from the Options section in the Inspector.

Exporting a 3D Scene for Efficiency

The Camera Tracker saves all its 2D tracks into the composition, sometimes resulting in a rather large

file on disk. If you are dealing with a large clip with many 2D tracks over a long duration, the saved

composition can reach over a gigabyte in size. Using a Camera Tracker node in a composition can

make it cumbersome to load and operate. While it is possible to use the Camera Tracker node directly

to composite via the 3D output, you’ll achieve better performance by exporting. Once the quality

of the solve is satisfactory, the Export tab can generate a “low memory” alternative by producing

individual Camera 3D, Point Cloud, Ground Plane, and 3D Renderer nodes.

Before you can export the 3D scene, you must provide a bit more information about it. You’ll do this

using controls found in the Export tab. Cameras do not include tiltmeters, so clips do not contain

metadata that indicates how the camera is tilted or oriented. This is critical information when recreating

the virtual camera. It is also useful to determine the location for the center of this 3D scene. The Export

tab provides various translation, rotation, and scale controls to set these options.


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION

Unalign the 3D Scene Transforms

By default, the Export tab is set to Aligned in the 3D Scene Transform section. The Aligned setting

locks the orientation and scale of the 3D scene to prevent accidentally changing it. So, before you can

set the ground plane and origin location, you must change the Camera Tracker to be unaligned using

the 3D Scene Transform menu in the Export tab. After you have gone through the Export settings and

configured them how you want, you must set the menu back to Aligned before exporting.

Set the 3D Scene Transform menu to Unaligned

before setting the ground plane

Setting the Ground Plane

The Camera Tracker has no idea if the camera is on its side or tilted in some way. So, it is up to you to

indicate where the ground plane is in a clip. After choosing Unaligned from the 3D Scene Transform

menu, you can begin identifying the ground plane.

Drag a selection box around marks that represent the ground


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION

To set the ground plane, do the following:


Move to a frame with lots of green 3D locators where you can see a large part of the ground.


In the viewer, drag a selection box around the marks located on the ground in the clip.


In the Inspector Orientation section, click the Set from Selection button.

TIP: In some cases, the clip you are tracking may not have the ground in the frame.

If necessary, you can set the Selection menu to XY, which indicates you are selecting points

on a wall.