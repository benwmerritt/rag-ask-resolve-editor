---
title: "Using the Lightbox"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 543
---

# Using the Lightbox

The Lightbox shows you all clips in the Timeline as a grid of thumbnails, arranged in rows from left to

right and top to bottom. This lets you quickly evaluate, compare, and search for clips you want to use

when making selections, creating groups, flagging clips, or when scanning for a particular scene or

looking for an individual clip.

The Color page Lightbox displays all the clips in the Timeline.


Color | Chapter 128 Color Page Timeline and Lightbox

COLOR

At the right of the Lightbox is a vertically oriented Timeline Ruler letting you know the timecode value

at the beginning of each row of clips. At the top right is a Zoom slider that lets you change the size of

the thumbnails.

Selecting a clip in the Lightbox is the same as selecting a clip in the Timeline, and right-clicking a

clip in the Lightbox shows the same contextual menu items you’d see if you right-clicked a clip in the

Timeline. Furthermore, you can also grade the current clip in the Lightbox using a control panel, or by

exposing the color controls to grade the current clip using a mouse or other input device.

Methods of using the Lightbox:

To show or hide the Lightbox: Click the Lightbox button in the toolbar.

To show color controls in the Lightbox: Click the Show Color Controls button in the UI control

bar above the Lightbox.

The Color Controls button, with the

sidebar and Thumbnail Info buttons below

To show thumbnail info in the Lightbox: Click the Clip Info button, which is the second control

at the upper left-hand corner of the Lightbox, to turn each clip’s thumbnail Info off and on.

To resize clips in the Lightbox: Drag the Zoom slider to the right to increase thumbnail size, or

to the left to decrease thumbnail size.

The Lightbox button, Zoom slider,

and Monitor Output buttons

The contents of the Lightbox can be filtered using the same options that are available for

filtering the Thumbnail timeline.

To filter the Lightbox:

•	 Click the Show sidebar button at the upper left-hand corner of the Lightbox. This reveals

all of the filtering options that are available in the Lightbox, including custom Smart Filters

you’ve created.

•	 Click one of the options appearing in the sidebar. The Lightbox should immediately update

to show just those clips that match the selected criteria.

•	 To go back to seeing every clip in the Timeline, click All Clips. The Lightbox can also be

output to video, in order to see its contents on a broadcast display or projector.


Color | Chapter 128 Color Page Timeline and Lightbox

COLOR

For more information about clip

selections, groups, and grade

management, see Chapter 142, “Grade

Management.”

The Lightbox sidebar, with

controls for filtering the Lightbox

To output the contents of the Lightbox to video:

Click the Output Lightbox to Video button at the upper right-hand corner of the Lightbox.

The button for outputting

the Lightbox to video


Color | Chapter 128 Color Page Timeline and Lightbox

COLOR

Chapter 129

Automated Grading

Commands and

Imported Grades

While DaVinci Resolve has a wide variety of manual grading controls that afford you

control over just about every component of digital imagery, DaVinci has spent a lot

of time investigating ways of increasing colorist efficiency by creating automated

grading tools.

Furthermore, with integrated editing bringing professional editors into the world of editing, grading,

and finishing in DaVinci Resolve, the same automated tools being developed to help colorists go

home earlier can also be used to give non‑colorists a hand in taking care of simple grading tasks.

Contents

Color Match Palette������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3039

Tips for Properly Shooting a Color Chart������������������������������������������������������������������������������������������������������������������������������� 3040

How to Use Color Match����������������������������������������������������������������������������������������������������������������������������������������������������������������� 3041

Configuration Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3043

Reset Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3043

Automatic Adjustments in the Primaries Palette�������������������������������������������������������������������������������������������������������������� 3044

White Balance Eyedropper����������������������������������������������������������������������������������������������������������������������������������������������������������� 3044

Pick Black Point and Pick White Point������������������������������������������������������������������������������������������������������������������������������������� 3044

Auto Color��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3045

Shot Match�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3047

Shot Match Guidelines�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3048

How to Use Shot Match������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3048

Suggestions for Using Shot Match�������������������������������������������������������������������������������������������������������������������������������������������� 3049

Broadcast Safe����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3050

Using CDL Grades ���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3051

Using ARRI Looks ����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3051


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

Color Match Palette

If the camera and lighting departments had the foresight to shoot a color test chart for each of the

major lighting setups in the project you’re grading, DaVinci Resolve lets you superimpose a sampling

grid over a chart in a clip and mathematically analyze the sampled colors to generate an automatic

correction. Using controls in the Color Match palette, you can specify the Source Gamma, Target

Gamma, and Target Color Space to make sure that the resulting correction is correct for the camera

you used, and the project you’ve set up.

The Color Match palette works with several standardized color charts:

�Datacolor SpyderCheckr 24

�DSC Labs ChromaDumonde 24+4

�DSC Labs SMPTE OneShot

�X-Rite ColorChecker Classic

�X-Rite ColorChecker Classic - Legacy

�X-Rite ColorChecker Video

�X-Rite ColorChecker Passport Video

The X-Rite ColorChecker, Datacolor SpyderCheckr,

and DSC Labs SMPTE OneShot charts compared,

all of which are supported by the Color Match palette

The result is analyzed to generate an automatic color correction to use to create a neutral

grade for the image, to use as a starting point for the rest of your grade.


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR