---
title: "Preview"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 288
---

# Preview

Preview is only available in Fusion Studio. Previews in DaVinci Resolve use the Scratch Disk setting in

the Media Storage preferences.

In the Preview preferences, you configure the creation and playback options for preview renders.

The Preview preferences


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Options

�Render Previews Using Proxy Scaling: When checked, this option scales down the images to the

preview size for the Loader and Creator tools. This causes much faster rendering. If this option is

disabled, frames will be rendered at full size and are then scaled down.

�Skip Frames to Maintain Apparent Framerate: When checked, frames are skipped during

playback of Flipbooks and file sequences to maintain the frame rate setting.

�Show Previews for Active Loaders: This setting determines whether the preview playback

controls are shown below the Inspector when a Loader with a valid file is activated.

�Show Previews for Active Savers: This setting determines whether the preview playback controls

below the Inspector are shown when a Saver with a valid file is activated.

�Display File Sequences On: This setting determines which viewer or external monitor is used for

the interactive and file sequence playbacks as well as for the scrubbing function in the bins.

QuickTime

The QuickTime preferences are only available in Fusion Studio on macOS. These settings configure

the default QuickTime codec settings when you select QuickTime as the rendering file format in the

Saver node.

The QuickTime preferences

�Compressor: This drop-down menu displays the QuickTime codecs available from your computer.

Fusion tests each codec when the program is started; therefore, some codecs may not be

available if the tests indicate that they are unsuitable for use within Fusion.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

�Quality: This slider is used to determine the amount of compression to be used by the codec.

Higher values produce clearer images but larger files. Not all codecs support the Quality setting.

�Key Frame Every X Frames: When checked, the codec will create key frames at specified

intervals. Key frames are not compressed in conjunction with previous frames and are, therefore,

quicker to seek within the resulting movie. Not all codecs support the key frame setting.

�Limit Data Rate To X KB/Second: When checked, the data rates of the rendered file will be limited

to the amount specified. Not all codecs support this option. Enter the data rate used to limit the

QuickTime in kilobytes (kB) per second, if applicable. This control will have no effect if the Limit

Data Rate To option is not selected.

Script

The preferences for Scripting include a field for passwords used to execute scripts from the command

line and applications for use when editing scripts.

The Script preferences

Login

There are three login options for running scripts outside of the Fusion application.

�No Login Required to Execute Script: When enabled, scripts executed from the command line, or

scripts that attempt to control remote copies of Fusion, do not need to log in to the workstation in

order to run.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

�Specify Custom Login: If a username and password are assigned, Fusion will refuse to process

incoming external script commands (from FusionScript, for example), unless the Script first logs in

to the workstation. This only affects scripts that are executed from the command line, or scripts

that attempt to control remote copies of Fusion. Scripts executed from within the interface do not

need to log in regardless of this setting. For more information, see the Scripting documentation.

�Use Windows Login Validation: When using Fusion on Windows, enabling this option verifies

the user name and password (also known as credentials) with the operating system before running

the script.

Options

Script Editor: Use this preference to select an external editor for scripts. This preference is used

when selecting Scripts > Edit.

Python Version

Two options are presented here for selecting the version of Python that you plan on using

for your scripts.

Spline Editor

The Spline Editor preferences allow you to set various spline options for Autosnap behavior, handles,

markers, and more. This only affects splines displayed in the Spline Editor, not splines created in the

viewer using the polygon tool or paths.

The Spine Editor preferences


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Spline Editor Options

These settings control the spline behavior in the Spline Editor, as well as the appearance of the graph area.

�Independent Handles: Enabling this option allows the In or Out direction handle on newly created

key frames to be moved independently without affecting the other. This option is also available via

the Options submenu when right-clicking in the Spline Editor graph.

�Follow Active: The Spline Editor focuses on the currently active tool. This option is also available

via the Options submenu when right-clicking in the Spline Editor graph.

�Show Key Markers: Small colored triangles will be displayed at the top of the Spline Editor

Time Ruler to indicate key frames on active splines. The colors of the triangles match the colors of

the splines. This option is also available via the Show submenu when right-clicking in the Spline

Editor graph.

�Show Tips: Toggles if tooltips are displayed or not. This option is also available via the Show

submenu when right-clicking in the Spline Editor graph.

�Autosnap Points: When moving points in the Spline Editor, these will snap to the fields or frames

or can be moved freely. This option is also available via the Options submenu when right-clicking

in the Spline Editor graph.

�Guides: When moving points in the Spline Editor, these will snap to guides as well. This option is

also available via the Options submenu when right-clicking in the Spline Editor graph.

�Autosnap Guides: When moving or creating guides, these will snap to the fields or frames or can

be moved freely. This option is also available via the Options submenu when right-clicking in the

Spline Editor graph.

�Autoscale: Keeps the Spline Editor scales intact on changing the editable spline content of the graph.

This scale is also available via the Options submenu when right-clicking in the Spline Editor graph.

�Scroll: Scrolls horizontally and vertically to show all or most of the spline points. This option is also

available via the Scale submenu when right-clicking in the Spline Editor graph.

�Fit: Zooms to fit all points within the spline graph, if necessary. This option is also available via the

Scale submenu when right-clicking in the Spline Editor graph.

LUT View Options

These settings let you control how the LUT view is displayed.

�Independent Handles: Enabling this option allows the In or Out direction handle on newly created

key frames to be moved independently without affecting the other.

�Show Key Markers: Small colored triangles will be displayed at the top of the Spline Editor Time Ruler

to indicate key frames on active splines. The colors of the triangles match the colors of the splines.

�Show Tips: Toggles whether tooltips are displayed.

Splines

Options for the handling and smoothing of animation splines, tracker path defaults, and rotoscoping

are found in the Splines preferences.

�Autosmooth: Automatically smooths out any newly created points or key frames on the splines

selected in this section. You can choose to automatically smooth animation splines, B-Splines,

polyline matte shapes, LUTs, paths, and meshes.

�B-Spline Modifier Degree: This setting determines the degree to which the line segments

influence the resulting curvature when B-Splines are used in animation. Cubic B-Splines determine

a segment through two control points between the anchor points, and Quadratic B-Splines

determine a segment through one control point between the anchor points.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

�B-Spline Polyline Degree: This setting is like the one above but applies to B-Splines

used for masks.

The Splines preferences

�Tracker Path Points Visibility: This setting determines the visibility of the control points on tracker

paths. You can show them, hide them, or show them when your cursor hovers over the path, which

is the default behavior.

�Tracker Path: The default tracker creates Bézier-style spline paths. Two other options in this

setting allow you to choose B-Spline or XY Spline paths.

�Polyline Edit Mode on Done: This setting determines the state of the Polyline tool after you

complete the drawing of a polyline. It can either be set to modify the existing control points on the

spline or modify and add new control points to the spline.

�Onion Skinning: The Onion Skinning settings determine the number of frames displayed while

rotoscoping, allowing you to preview and compare a range of frames. You can also adjust if the

preview frames only from the frame prior to the current frame, after the current frames, or split

between the two.


Fusion Fundamentals | Chapter 75 Preferences

FUSION