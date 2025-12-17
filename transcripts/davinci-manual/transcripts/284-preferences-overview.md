---
title: "Preferences Overview"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 284
---

# Preferences Overview

The Preferences window provides a wide variety of optional settings available for you to configure

Fusion’s behavior to better suit your working environment. These settings are accessed via the

Preferences window. The Preferences window can be opened from a menu at the top of the interface.

In DaVinci Resolve, to open the Fusion Preferences window, do one of the following:

•	 On macOS, switch to the Fusion page and choose Fusion > Fusion Settings.

•	 On Windows, switch to the Fusion page and choose Fusion > Fusion Settings.

•	 On Linux, switch to the Fusion page and choose Fusion > Fusion Settings.

In Fusion Studio, to open the Fusion Preferences window, do one of the following:

•	 On macOS, choose Fusion Studio > Preferences.

•	 On Windows, choose File > Preferences.

•	 On Linux, choose File > Preferences.

The Preferences window includes composition settings.

Global and Composition Preferences

The Preferences window is divided into a category sidebar on the left and the settings panel on the

right. In Fusion Studio, there are two levels of preferences: Global and Composition. The Fusion page

in DaVinci Resolve uses just a single Global preference that affects every project, new and existing.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

The Global preferences are used to set options specific to Fusion’s overall behavior as well as defaults

for each new composition. The Composition preferences in Fusion Studio can further modify the

currently open composition without affecting the Global preferences or any other composition that is

open but not displayed.

Categories of Preferences

The first entry in the Preferences sidebar is assigned to the Global preferences. Clicking the Global

and Default Settings disclosure arrow reveals the following sections.

Fusion Studio Global and Default settings

3D View

The 3D View preferences offer control over various parameters of the 3D Viewers, including grids,

default ambient light setup, and Stereoscopic views.

AVI (Windows Fusion Studio Only)

The AVI preferences configure the default compression options when creating AVI files from a

Saver node. These settings can be overridden on a case-by-case basis using the Format tab in the

Saver’s Inspector.

Defaults

The Defaults preferences are used to select default behavior for a variety of options, such as

animation, global range, timecode display, and automatic tool merging.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Flow

You use the Flow preferences to set many of the same options found in the Node Editor’s contextual

menu, like settings for Tile picture, the Navigator, and pipe style.

Frame Format

The Frame Format preferences are used to create new frame formats as well as select the default

image height and width when adding new creator tools like Background and Text+. You also set the

frame rate for playback.

General

The General preferences contain options for the general operation, such as auto save, and gamma

settings for color controls.

GPU (Fusion Studio Only)

The GPU preferences include options for selecting specific GPU acceleration methods based on your

computer platform and hardware capabilities. It is also used for enabling caching, and debugging GPU

devices and tools.

Layout (Fusion Studio Only)

You can use the Layout preferences to save the exact layout of Fusion’s windows.

Loader (Fusion Studio Only)

Using the Loader preferences, you can set options for the default Loader’s depth and aspect ratio as

well as define the local and network LoaderCache settings.

Memory (Fusion Studio Only)

Memory management for multi-frame and simultaneous branch rendering is configured in the Memory

preferences.

Network (Fusion Studio Only)

The Network rendering preferences are used to configure options such as selecting a render master,

email notification, and whether the machine can be used as a render slave.

Path Map

Path Map preferences are used to configure virtual file path names used by Loaders and

Savers as well as the folders used by Fusion to locate comps, macros, scripts, tool settings, disk

caches, and more.

Preview (Fusion Studio Only)

The Preview preferences is where you configure the Preview creation and playback options.

QuickTime (macOS Fusion Studio Only)

This section lets you preconfigure the QuickTime codec used for rendering.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Script

The Script preferences include a field for passwords used to execute scripts externally, programs to

use for editing scripts, and the default Python version to use.

Spline Editor

The Spline Editor preferences allow you to set various spline options for Autosnap behavior, handles,

markers, and more.

Splines

Options for the handling and smoothing of animation splines, Tracker path defaults, onion-skinning,

roto assist, and more are found in the Splines preference.

Timeline

The Timeline preferences is where you create and edit Timeline/Spline filters and set default options

for the Keyframes Editor.

Tweaks

The Tweaks preferences handle miscellaneous settings for modifying the behavior when loading

frames over the network and queue/network rendering.

User Interface

These preferences set the appearance of the user interface window and how the Inspector is

displayed.

Video Monitoring (Fusion Studio Only)

The Video Monitoring preferences is where you can configure your Blackmagic video display

hardware for monitoring on an HD, Ultra HD, or DCI 4K display.

View

The View preferences are used to manage settings for viewers, including default control colors,

Z-depth channel viewing ranges, default LUTs, padding for fit, zoom, and more.

VR Headsets

The VR Headsets preferences allow configuration of any connected Virtual Reality headsets, including

how stereo and 3D scenes are viewed.

Bins (Fusion Studio Only)

There are three panels as part of the Bins preferences: a Security panel where you set users and

passwords for serving the local bins; a Servers panel used to select which remote Bin servers are

connected; and a Settings panel for stamp rendering.

Import

The Import settings contain options for EDL Import that affect how flows are built using the data

from an EDL.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Preferences In Depth

Within each category is a deep set of controls for configuring Fusion so that it better fits your working

environment. The preferences contain both software and hardware options that affect all newly

created comps. The following section explains every option located in the preferences categories.

3D View

The 3D View preferences contain settings for various defaults in the 3D Viewers, including grids,

default ambient light setup, and Stereoscopic views.

The 3D View preferences

Grid

The Grid section of the 3D View preferences configures how the grid in 3D Viewers are drawn.

�Grid Antialiasing: Some graphics hardware and drivers do not support antialiased grid

lines, causing them to sort incorrectly in the 3D Viewer. Disabling this checkbox will disable

antialiasing of the grid lines. To turn off the grid completely, right-click in a 3D Viewer and choose

3D Options > Grid.

�Size: Increasing the Size value will increase the number of grid lines drawn. The units used for the

spacing between grid lines are not defined in Fusion. A “unit” is whatever you want it to be.

�Scale: Adjusting the overall scaling factor for the grid is useful, for example, if the area of the grid

appears too small compared to the size of your geometry.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Perspective Views

The Perspective Views section handles the appearance of the perspective view in both a normal and

stereoscopic project.

�Near Plane/Far Plane: These values set the nearest and furthest point any object can get to or

from the camera before it is clipped. The minimum setting is 0.05. Setting Near Plane too low and

Far Plane too far results in loss of depth precision in the viewer.

�Eye Separation/Convergence/Stereo Mode: This group of settings defines the defaults when

stereo is turned on in the 3D Viewer.

Orthographic Views

Similar to the Perspective Views, the Orthographic Views (front, top, right, and left views) section sets

the nearest and furthest point any object can get to or from the viewer before clipping occurs.

Fit to View

The Fit to View section has two value fields that manage how much empty space is left around objects

in the viewer when the F key is pressed.

�Fit Selection: Fit Selection determines the empty space when one or more objects are selected

and the F key is pressed.

�Fit All: Fit All determines the empty space when you press F with no objects selected.

Default Lights

These three settings control the default light setup in the 3D Viewer.

The default ambient light is used when lighting is turned on and you have not added a light to the

scene. The directional light moves with the camera, so if the directional light is set to “upper left,” the

light appears to come from the upper-left side of the image/camera.