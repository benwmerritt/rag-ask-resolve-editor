---
title: "Chapter 119"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 490
---

# Chapter 119

Tracking Nodes

This chapter details the Tracking nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Camera Tracker [CTra]��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2733

Camera Tab������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2736

Solve Tab������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2738

Track Filtering���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2741

Operations on Selected Tracks��������������������������������������������������������������������������������������������������������������������������������������������������� 2742

Export������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2743

3D Scene Transform�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2744

Options����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2746

Understanding Camera Tracking������������������������������������������������������������������������������������������������������������������������������������������������ 2747

Planar Tracker Node [PTRA]���������������������������������������������������������������������������������������������������������������������������������������������������������� 2749

What the Planar Tracker Saves���������������������������������������������������������������������������������������������������������������������������������������������������� 2749

A Typical Planar Tracker Workflow�������������������������������������������������������������������������������������������������������������������������������������������� 2750

Track Mode������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2753

Steady Mode���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2755

Corner Pin Mode�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2755

Merge Mode����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2756

Options Tab������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2758

Surface Tracker [SFt]������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2759

Tracker [TRA]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2768

IntelliTrack AI Point Tracker���������������������������������������������������������������������������������������������������������������������������������������������������������� 2770

Legacy Point Tracker Onscreen Controls������������������������������������������������������������������������������������������������������������������������������ 2770

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2785


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Camera Tracker [CTra]

The Camera Tracker node

Camera tracking is match moving, and a vital link between 2D and 3D, allowing compositors to

integrate 3D renders into live-action scenes. The Camera Tracker node is used to calculate the path

of a live-action camera and generate a virtual camera in 3D space. This virtual camera’s motion is

intended to be identical to the motion of the actual camera that shot the scene. Using the calculated

position and movement of the virtual camera provides the flexibility to add 3D elements to a live-

action scene. Also, the Camera Tracker creates a point cloud in 3D space that can be used to align

objects and other 3D models to the live-action scene.

For more information about how to use the Camera Tracker, see Chapter 86, "3D

Camera Tracking," in the DaVinci Resolve Reference Manual, or Chapter 26 in the Fusion

Reference Manual.

The original video clip

3D objects composited on to the video clip that use the camera tracker

to remain aligned with the objects in the frame as the image moves


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Inputs

The Camera Tracker has two inputs:

Background: The orange image input accepts a 2D image you want tracked.

Occlusion Mask: The white occlusion mask input is used to mask out regions that do not need to be

tracked. Regions where this mask is white will not be tracked. For example, a person moving in front

of and occluding bits of the scene may be confusing to the tracker, and a quickly-created rough mask

around the person can be used to tell the tracker to ignore the masked-out bits.

Basic Node Setup

The Camera Tracker background input is used to connect the image you want tracked. Polygon masks

can be connected into the occlusion mask input to identify areas the tracker should ignore.

The Camera Tracker with occlusion masks

Inspector

The Camera Tracker tab

Track Tab

The Track tab contains the controls you need to set up an initial analysis of the scene.

Auto Track

Automatically detects trackable features and tracks them through the source footage. Tracks will

be automatically terminated when the track error becomes too high, and new tracks are created as

needed. The values of the Detection Threshold and Minimum Feature Separation sliders can be used

to control the number and distribution of auto tracks.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Reset

Deletes all the data internal to the Camera Tracker node, including the tracking data and the solve

data (camera motion path and point cloud). To delete only the solve data, use the Delete button on the

Solve tab.

Preview AutoTrack Locations

Turning this checkbox on will show where the auto tracks will be distributed within the shot. This

is helpful for determining if the Detection Threshold and Minimum Feature Separation need to be

adjusted to get an even spread of trackers.

Detection Threshold

Determines the sensitivity to detect features. Automatically generated tracks will be assigned to

the shot, and the Detection Threshold will force them to be either in locations of high contrast or

low contrast.

Minimum Feature Separation

Determines the spacing between the automatically generated tracking points. Decreasing this slider

causes more auto tracks to be generated. Keep in mind that a large number of tracking points will also

result in a lengthier solve.

Track Channel

Used to nominate a color channel to track: red, green, blue, or luminance. When nominating a channel,

choose one that has a high level of contrast and detail.

Track Range

Used to determine which frames are tracked:

�Global: The global range, which is the full duration of the Timeline.

�Render: The render duration set on the Timeline.

�Valid: The valid range is the duration of the source media.

�Custom: A user-determined range. When this is selected, a separate range slider appears to set

the start and end of the track range.

Bidirectional Tracking

Enabling this will force the tracker to track backward after the initial forward tracking. When tracking

backward, new tracks are not started but rather existing tracks are extended backward in time.

It is recommended to leave this option on, as long tracks help give better solved cameras and

point clouds.

Gutter Size

Trackers can become unstable when they get close to the edge of the image and either drift or jitter or

completely lose their pattern. The Camera Tracker will automatically terminate any tracks that enter the

gutter region. Gutter size is given as a percentage of pattern size. By default, it’s 100% of pattern size,

so a 0.04 pattern means a 0.04 gutter.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

New Track Defaults

There are three methods in which the Camera Tracker node can analyze the scene, and each has its

own strengths when dealing with certain types of camera movement.

�Tracker: Internally, all the Trackers use the Optical Flow Tracker to follow features over time and

then further refine the tracks with the trusted Fusion Tracker or Planar Tracker. The Planar Tracker

method allows the pattern to warp over time by various types of transforms to find the best fit.

These transforms are:

�Translation

�Translation and Rotation Translation, Rotation, and Scale Affine

�Perspective

It is recommended to use the default TRS setting when using the Planar Tracker. The Affine and

Perspective settings need large patterns in order to track accurately.

�Close Tracks When Track Error Exceeds: Tracks will be automatically terminated when the

tracking error gets too high. When tracking a feature, a snapshot of the pixels around a feature are

taken at the reference time of the track. This is called a pattern, and that same pattern of pixels is

searched for at future times. The difference between the current time pattern and the reference

time pattern is called the track error. Setting this option higher produces longer but increasingly

less accurate tracks.

�Solve Weight: By default, each track is weighted evenly in the solve process. Increasing a track’s

weight means it has a stronger effect on the solved camera path. This is an advanced option that

should be rarely changed.

Auto Track Defaults

Set a custom prefix name and/or color for the automatically generated tracks. This custom color will be

visible when Track Colors in the Options tab is set to User Assigned.

Camera Tab

The Camera Tracker Camera tab

The controls of the Camera tab let you specify the physical aspects of the live-action camera, which

will be used as a starting point when searching for solve parameters that match the real-world camera.

The more accurate the information provided in this section, the more accurate the camera solve.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

The Camera tab includes controls relating to the lens and gate aspects of the camera being solved for.

Focal Length

Specify the known constant focal length used to shoot the scene or provide a guess if the Refine

Focal Length option is activated in the Solve tab.

Film Gate

Choose a film gate preset from the drop-down menu or manually enter the film back size in the

Aperture Width and Aperture Height inputs. Note that these values are in inches.

Aperture Width

In the event that the camera used to shoot the scene is not in the preset drop-down menu, manually

enter the aperture width (inches).

Aperture Height

In the event that the camera used to shoot the scene is not in the preset drop-down menu, manually

enter the aperture height (inches).

Resolution Gate Fit

This defines how the image fits the sensor size. Often, film sensors are sized to cover a number of

formats, and only a portion of the sensor area is recorded into an image.

For example, a 16:9 image is saved out of a full aperture-sized sensor.

Typically, fit to Width or Height is the best setting. The other fit modes are Inside, Outside, or

Stretched.

Center Point

This is where the camera lens is aligned to the camera. The default is (0.5, 0.5), which is the middle of

the sensor.

Use Source Pixel Aspect

This will use the squeeze aspect of the pixels that is loaded in the image. HD is square pixels, but

NTSC has a pixel aspect ratio of 0.9:1, and Anamorphic CinemaScope is 2:1 aspect. Disabling this

option exposes Pixel X and Y number fields where you can customize the source pixel aspect.

Auto Camera Planes

When enabled, the camera’s image plane and far plane are automatically moved to enclose the point

cloud whenever a solve completes. Sometimes, though, the solver can atypically fling points off really

deep into the scene, consequently pushing the image plane very far out. This makes the resulting

scene unwieldy to work with in the 3D views. In these cases, disable this option to override this default

behavior (or delete the offending tracks).


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION