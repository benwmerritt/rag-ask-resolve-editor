---
title: "Setting up DaVinci Resolve for Resolve Live"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 60
---

# Setting up DaVinci Resolve for Resolve Live

Once the hardware is set up, you will need to check the configuration of DaVinci Resolve to be able to

make use of the live grading features of Resolve Live.

The first setting is to select the appropriate video input hardware in the Video I/O settings.

The Video I/O panel of the System Preferences provides two sets of options for configuring video

interfaces connected to your computer, one for capture, and one for monitoring. Resolve Live uses the

video hardware input selected in the capture device. You will need to restart DaVinci Resolve if you

modify these settings.

Video input/output options in the System Preferences

Next, you should begin with a new empty project. You should set up the new project’s Timeline and

Video Monitoring settings to match the format and frame rate coming out of your camera.


Setup and Workflows | Chapter 14 Resolve Live

MEDIA

IMPORTANT: You must set up the resolution and frame rate in your new project’s

Timeline format and Video Monitoring format in the project’s Master Settings to match the

resolution and frame rate of the video coming out of the camera.

Make sure your Timeline format and Video Monitoring size and frame rate

match your camera’s video output in the Master Settings

Then add a new empty timeline, since the live grading workflow involves capturing live graded

snapshots to an otherwise unoccupied timeline. One recommended way of organizing the live

grades of a shoot is to create one new project per day of shooting. This way, snapshots captured

during shoots using all 24 hours of time-of-day timecode won’t conflict with one another. Also,

separate projects can make it easier to use ColorTrace to copy grades from your live grade

snapshots to the camera original media you’ll be creating dailies from, eventually.

TIP: Having an empty Media Pool and Timeline doesn’t mean you can’t install useful

LUTs and pre-import reference stills and saved grades to the Gallery, as these can be

valuable tools for expediting your on-set grading.

Once you’ve created your new project, you also need to choose the disk where all snapshots you

take will be saved. By default, snapshots are saved on the scratch disk at the top of the Scratch

Disks list in the Media Storage panel of the System Preferences. They’re automatically saved in a

folder named identically to the current project, inside a folder called Resolve Live.


Setup and Workflows | Chapter 14 Resolve Live

MEDIA

Resolve Live software checklist:

•	 Choose the Capture Device for inputting the video signal from the Video Input/Output

options in the System Preferences.

•	 Create a New Project.

•	 Make sure your Timeline format and Video Monitoring size and frame rate match your

camera’s video output in the project’s Master Settings.

•	 Create a New Timeline.

Grading Live

Once your camera and computer are appropriately connected and configured, using Resolve Live

is straightforward. This section describes the live grading workflow as it was designed to be used.

Once you’re familiar with the capabilities of Resolve Live, you may find your own ways of working that

are more in tune to the needs of your particular project.

Going Live

Once you’ve created your day’s project, you need to turn on Resolve Live to begin work.

To turn on Resolve Live:


Open the Color page.


Choose Color > Resolve Live (Command-R).

A red Resolve Live badge at the top of the Viewer indicates that Resolve Live is turned on,

and the transport controls are replaced by the Freeze and Snapshot buttons.

A red badge shows that Resolve Live is active and showing incoming video from the camera


Setup and Workflows | Chapter 14 Resolve Live

MEDIA

At this point, the video from the connected camera should become visible within the Viewer, the

camera timecode should be displayed in the Viewer’s timecode window, and you can begin using all

of the capabilities of the Color page to begin grading whatever is onscreen, including Gallery split-

screens for matching and comparing. The current color adjustments in all palettes are automatically

applied to both the image in the Viewer and the video output to an external display (if there is one).

While Resolve Live is on, much of DaVinci Resolve’s non-grading functionality is disabled, so when

you’re finished, be sure to turn Resolve Live off.

To turn off Resolve Live, do one of the following:

�Click the Exit button at the bottom left-hand corner of the Viewer.

�Choose Color > Resolve Live (Command-R).

Using Freeze

In Resolve Live mode, the Freeze button (it looks like a snowflake) freezes the current incoming video

frame, so you can grade it without being distracted by motion occurring during the shoot. When you’ve

made the adjustment you need, you can unfreeze playback in preparation for grabbing a snapshot.

To freeze incoming video:

�Click the Freeze button (that looks like a snowflake).

�Choose Color > Resolve Live Freeze (Shift-Command-R).

The snowflake button freezes the image

so you can grade a particular frame

Using Snapshot

Once you’re happy with a grade, clicking the Snapshot button saves a snapshot of the current still in

the Viewer,  the incoming timecode value, and your grade into the Timeline. Snapshots are simply

one-frame clips. They use grades and versions just like any other clip. In fact, ultimately there’s no

difference between the timeline created by a Resolve Live session and any other timeline, other than

that the Resolve Live timeline only has a series of one frame clips, which appear in the Timeline of the

Edit page as a series of 1-frame stills.

To save a snapshot, do one of the following:

�Click the snapshot button (with a camera icon).

�Choose Color > Resolve Live Snapshot (Command-Option-R).

The snapshot button saves a frame

and the grade for future use


Setup and Workflows | Chapter 14 Resolve Live

MEDIA

For example, you may begin the process of building and refining a grade for a particular scene

during an unrecorded run-through. Then, once shooting starts, you may take snapshots of

each shot’s slate, and then of significant takes that follow, tweaking where necessary and in

conjunction with the DP’s feedback once things get going. New camera setups may require

further tweaks, which you’ll save as snapshots for those shots, and as you work in this way

you’ll find yourself building up a timeline of snapshots that correspond to that day’s shoot.

As you work, keep in mind that you must temporarily turn Resolve Live off in order to open a

grade from a previous snapshot in the Timeline, in order to use it as a starting point for another

shot. You can also save grades into the Gallery.

Resolve Live Audio Monitoring

When using Resolve Live, you can now hear the audio signal from the camera coming into the

Decklink or Ultrastudio device as you grade. You can toggle this behavior on or off by clicking on the

speaker icon underneath the Viewer.

Clicking on the speaker icon toggles the audio on and off during a Resolve Live session.


Setup and Workflows | Chapter 14 Resolve Live

MEDIA