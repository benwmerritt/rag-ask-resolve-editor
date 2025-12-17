---
title: "Safe Area Overlays in the Viewer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 536
---

# Safe Area Overlays in the Viewer

You can show or hide a series of safe area overlays in the Viewer. All safe area overlay options are

found in the View > Safe Area menu. Each safe area overlay option can be individually enabled or

disabled from this menu.

Viewer displaying extents, center, safe, action and title area overlays

On/Off: Turns all currently selected safe area marker options on or off at once.

Extents: An outline showing the exact outer edge of the frame. Especially useful when the

safe markers are set to an aspect ratio other than that currently used by the Viewer.

Action: An outline showing the outer 90% action safe area of the frame.

Title: An outline showing the outer 80% title safe area of the frame.

Center: A crosshairs showing the center of the frame.

Aspect: Enables use of the View > Select Aspect Ratio submenu to change the aspect ratio of

the safe area markers. You can choose among the following aspect ratios: 1.33 (a.k.a. 4:3), 1.66,

1.77 (a.k.a. 16:9), 1.85, and 2.35.

Use Gray Background

Checking the “Use gray background in viewers” box in the User Preference’s UI Settings sets the

empty area of the Viewer (if there is any) to a lighter gray, making it easier to see which parts of the

Viewer are black because of blanking, and which parts are simply empty because of the way the

image is zoomed or panned.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Monitor Calibration

If you use Light Illusion’s LightSpace CMS or SpectraCal’s Calman for display calibration, you can now

use DaVinci Resolve as a sync-able pattern generator. This means you can use DaVinci Resolve to

output color patches, synchronized by LightSpace, to your display through whichever video interface

is connected to your computer. These synchronized color patches will be analyzed by a monitor probe

that’s also controlled by LightSpace, which stores the probe data and compares it to the original color

values of the output color values in order to characterize that display.

To use this feature, you must first have a licensed copy of LightSpace CMS, which is a Windows

application. Synchronization depends on a wired or wireless LAN being available to connect the

LightSpace application with DaVinci Resolve.

To synchronize LightSpace CMS to DaVinci Resolve as a pattern generator client:


Open LightSpace on the Windows computer that’s running it.


When LightSpace is open, click the Network Manager button. A window appears displaying the

two network IP addresses used by LightSpace. Note these, and click the Enable button.

The Network Manager dialog

in LightSpace CMS


In DaVinci Resolve, choose Workspace > Monitor Calibration > LightSpace.


When the LightSpace dialog opens, enter the second of the two network IP addresses LightSpace

lists into the Remote Machine field, and make sure the Port number matches. Then click the

Connect button.

The Calibration dialog in DaVinci Resolve,

connected to LightSpace CMS via WiFi


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

If everything is working correctly, the LightSpace dialog in DaVinci Resolve should show the

word “Connected,” and the Network Manager dialog in LightSpace should show that there is 1

available client/s.

You can now close the Network Manager dialog in LightSpace and follow the procedures outlined

in the LightSpace CMS documentation for characterizing your display and building and exporting a

display LUT (in the .cube format) that you can use as a display LUT in DaVinci Resolve. Alternately,

you can export a display LUT from LightSpace that can be loaded onto an outboard video

processing device.


When you’re finished, click Disconnect in the LightSpace dialog, and then click Cancel to close

the window.

Viewing Broadcast Safe Exceptions

Choosing View > Display Broadcast Safe Exceptions sets the Color page Viewer to show a false-color

overlay that indicates in blue the regions of the picture that violate the currently selected broadcast

safe level in the Color Management panel of the Project Settings.

Areas of the image that violate broadcast safe are highlighted in blue

More information about broadcast safe limiting in the Color Management panel of the Project

Settings see Chapter 127, “Automated Grading Commands and Imported Grades.”

Comparing Clips in the Viewer

The ability to compare different clips to one another is an important part of the color correction

process. DaVinci Resolve provides three different ways of doing so. You can use the Gallery to display

two clips for split screen comparison. You can also use different reference modes to see a timeline clip

or reference movie directly as part of a split screen comparison. Finally, you can use the Split Screen

controls to display multi-frame arrangements in the Viewer.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Saving and Wiping Stills in the Gallery and Timeline

The Gallery on the Color page provides fast access to stills that you’ve saved from various clips in the

Timeline. While the dedicated Gallery page provides a more comprehensive interface for browsing

presaved “looks,” as well as for importing stills from other projects, you can save, organize, and

browse stills directly within the Gallery of the Color page.

Stills are saved in the DPX file format. Once you’ve saved one or more stills, you can set up split

screen wipes in the Viewer, which will be mirrored to your external display.

Stills from the Gallery can be compared to the current shot, making it easier to match grades.

This section provides an abbreviated summary of still store and split screen functionality to get you

started quickly.

To save a still, do one of the following:

�Choose Color > Stills > Grab Still (Option-Command-G).

�Right-click on the Viewer and choose Grab Still.

To wipe a still, do one of the following:

�Select a still in the Gallery, and click the Image Wipe button on the top Viewer toolbar.

�Choose Color > Stills > Play Still (Command-W), or right-click in the Viewer and choose Toggle Wipe.

�Double-click a still in the Gallery.

To adjust a wipe in the Viewer, do one of the following:

�Drag the pointer within the Viewer to move the wipe.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

The different wipe customization modes

To customize a wipe in the Viewer:

Click one of the Wipe mode buttons in the Viewer toolbar. There are the following modes:

Horizontal: Lets you compare both halves of the wipe to either side of a vertical

border. Dragging the pointer moves the wipe border left and right.

Vertical: Lets you compare both halves of the wipe above and below a horizontal

border. Dragging the pointer moves the wipe border up and down.

Diagonal: Lets you compare both halves of the wipe via an adjustable diagonal border.

Dragging the pointer repositions the wipe to the left and right. Hold the Option key

down and drag while moving the pointer around in a circle to rotate the border of the

wipe to any angle you like.

Mix: Lets you blend both images together to compare them. Dragging the pointer

controls the fade percentage from one image to the other.

Alpha: Lets you use a qualifier to define transparency in the image of the current clip

while comparing it to a Gallery still used as the background. Add a node to the grade

and use the qualifier to key a particular color you want to turn transparent (the green

of a green screen, for example). Then, connect that node’s KEY output to the Alpha

Output that appears in the Node Editor. The part of the foreground image isolated

by the key becomes transparent, allowing the Gallery still in the background to show

through. This can be useful for previewing how the lighting or grade of a foreground

VFX plate looks when the image is composited against a particular background image

stored in the Gallery.

Difference (A/B): Lets you view only the pixels that change due to an operation on the

node. For example, if you select this highlight and adjust the gain, only the pixels that

the gain modified would be visible in the Viewer.

Box: Lets you view the current clip as a picture-in-picture effect against the still in

the background. Dragging the pointer resizes the crop box around the outside of the

reference image.

Venetian Blind: Lets you compare both images being wiped via alternating horizontal

strips. Drag the pointer up or down to change the size of the alternating strips. Good

for quickly comparing vertical color uniformity, focusing on color and contrast changes

that occur from top to bottom.

Checkerboard: Lets you compare both images being wiped via an alternating

checkerboard. Drag the mouse left or right to alternate between images by squeezing

each check horizontally. Good for comparing color uniformity across the width and

height of two images.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Choose one of the following from the Wipe Style submenu in the Viewer’s option menu.

Wipe Style: Cycles among the Horizontal, Vertical, Diagonal, Mix, Alpha, Difference, Box,

Venetian Blind, and Checkerboard modes.

Invert Wipe: Reverses each half of the wipe (Option-W).

Hover Scrub in the Gallery

When Live Preview is enabled in the Gallery option menu, the Hover Scrub Preview submenu lets you

choose how you want Live Preview to be shown by a thumbnail in the Gallery and in the Viewer when

you hover the pointer over a still or LUT in the LUT Browser:

�You can choose to scrub both the thumbnail you’re hovering over and the Viewer, letting you

preview the current still’s grade or a LUT over the duration of the current clip in both the thumbnail

and Viewer.

�You can choose to scrub just the thumbnail, leaving the Viewer to show just the grade or LUT over

the frame at the position of the playhead.

�You can disable scrubbing altogether, in which case both the thumbnail and the Viewer will only

show the grade or LUT over the frame at the position of the playhead.

Copying Grades from Stills in the Gallery

Stills also store the grade from the clip they came from, and can be used to copy grades from one clip

to another, or to store grades that you might want to use later.

To copy a grade from a still to a clip, do one of the following:

�Select one or more clips in the Timeline, then right-click a still in the Gallery

and choose Apply Grade.

�Select one or more clips in the Timeline, then middle-click a still in the Gallery.

When you copy a still in this way, the saved grade completely overwrites the grade in the target

clip, unless you’ve used the “Preserve number of nodes” option, found in the contextual menu of

the Gallery.

For more detailed information on using the Gallery, including options for organizing the

Gallery browser, instructions for using Albums, Power Grades, and Memories, as well as other

methods of copying grades and performing advanced grade management tasks, see Chapter

141, “Using the Gallery.” and see Chapter 142, “Grade Management.”