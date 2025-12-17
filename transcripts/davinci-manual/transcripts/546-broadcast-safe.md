---
title: "Broadcast Safe"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 546
---

# Broadcast Safe

If you regularly deliver to restrictive QC standards, then you can enable Broadcast Safe in the

Color Management panel of the Project Settings while you grade to limit both the luma and chroma of

the video signal to one of three levels of acceptable overshoots and undershoots.

The Broadcast Safe parameters in the Color

Management panel of the Project Settings

Broadcast safe IRE (mV) levels: A drop-down menu for choosing one of three levels

of aggressiveness when limiting the signal. Choose the range that corresponds to your

QC requirements. The options are “–20 - 120” (permissive), “–10 - 110” (conservative), and

“0 - 100” (very conservative).

Make Broadcast Safe: A checkbox that turns broadcast safe limiting on and off.

NOTE: The clipping imposed by Broadcast Safe itself does not have an inherently soft roll-

off. For best results, Broadcast Safe should be used in conjunction with the Soft Clip controls

in the Color page, or a Soft Clip LUT.

For more information see Chapter 4, “System and User Preferences.”


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

Using CDL Grades

There are two instances where primary grading adjustments may be applied to a clip outside

of adjustments that you make within the Node Editor of the Color page. If you import a CDL

(Color Decision List), then the CDL adjustment for each clip is made available to you via a contextual

menu command in the Thumbnail timeline of the Color page.

For more information, see Chapter 149, “Copying and Importing Grades Using ColorTrace.”

Using ARRI Looks

If you’ve ingested ARRIRAW media or QuickTime-wrapped Apple ProRes from an Amira, Alexa SXT

or Alexa LF, or MXF-wrapped Apple ProRes from Alexa Mini LF with embedded ARRI Look metadata

(CDL + LUT), the embedded look can be copied to the currently selected node in the Color page.

To copy an ARRI look from the source media to the current node:


Select a node in the Node Editor to which you want to apply the look data.


Right-click that clip’s thumbnail and choose Apply ARRI CDL and LUT. A LUT and Color Wheels

adjustment will be applied to the selected node.

Using the Apply ARRI CDL and LUT

command copies a look from the source

media to a node in the Node Editor


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

Chapter 130

Camera Raw Palette

The Camera Raw palette lets you make clip-specific adjustments to the

parameters that are used to debayer a raw clip into an image that can be graded in

DaVinci Resolve.

Contents

Introduction to the Camera Raw Palette������������������������������������������������������������������������������������������������������������������������������� 3053

Copying, Versioning, and Protecting Camera Raw Settings�������������������������������������������������������������������������������������� 3053

Making Changes to Clip Camera Raw Settings����������������������������������������������������������������������������������������������������������������� 3054

Clip Decoder Settings��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3055

Resetting Camera Raw Settings������������������������������������������������������������������������������������������������������������������������������������������������� 3056

Updating Sidecar Settings for Blackmagic RAW (BRAW) Clips��������������������������������������������������������������������������������� 3056


Color | Chapter 130 Camera Raw Palette

COLOR

Introduction to the Camera Raw Palette

When a timeline uses clips that are linked to camera raw source media recorded from cameras from

Blackmagic Design, RED, ARRI, Sony, and Vision Research, all clips in raw media formats are initially

debayered using the settings found in the Camera Raw panel of the Project Settings.

However, if there are individual clips that you want to apply different raw settings to, for example

altering the ISO to pull more detail out of the highlights or shadows, then you can use the controls

found in the Camera Raw palette to individually alter the parameters found within.

The Camera Raw palette showing the available parameters for Blackmagic RAW media.

The Camera Raw palette is automatically set to the mode (seen within the Mode drop-down menu)

that is appropriate to the clip that’s currently selected. If the current clip is not in a raw format, then the

parameters within the Camera Raw palette are disabled.

This section covers general use of the Camera Raw palette. For in-depth documentation

about specific camera raw parameters, see Chapter 7, “Camera Raw Settings.”

Copying, Versioning, and

Protecting Camera Raw Settings

Ordinarily, a clip’s camera raw settings are copied along with its grade, or saved inside stills grabbed

from that clip, when you use the various grade management techniques covered in later Chapter,

see Chapter 142, “Grade Management.”

When you create new versions, you copy the current Camera Raw settings to the new version, but

any changes you make are specific to that version, so each version can have individual Camera Raw

adjustments. For example, you could compare the results of two different camera raw adjustments on

the same clip.


Color | Chapter 130 Camera Raw Palette

COLOR

Camera Raw master settings for BRAW media

If you’re copying and rippling grades among multiple clips, you can also protect each clip’s camera raw

settings from being overwritten using the “Copy Grade: Preserve Camera Raw Settings” option found

in the contextual menu of the Gallery.

For more information on the Copy Grade settings, see Chapter 142, “Grade Management.”

Making Changes to Clip

Camera Raw Settings

If you want to make individual adjustments to a particular clip’s camera raw settings, choose “Clip” from

the Decode Using drop-down menu in the Camera Raw palette. This makes all the parameters in the

Camera Raw palette editable, and changes you make override the project-wide camera raw settings.

Changes to the parameters in the Camera Raw palette can also be rippled across multiple

clips at once.

To ripple camera raw adjustments across multiple clips:


First, you must select a range of clips in the Color page timeline.


Open the Camera Raw palette, and make whatever adjustments are necessary to the current clip.

The name of each parameter you adjust changes to amber, showing you which parameters have

been modified, and which have not.


To ripple your changes, do one of the following:

�Click the Use Changes button to ripple only the altered parameters (in amber) to the other clips

you’ve selected in the Timeline. This preserves differences between clips in the parameters you

haven’t adjusted (in gray).

�Click the Use Settings button to ripple every parameter of the current clip to the other clips

you’ve selected, overwriting all the camera raw settings at once.

The Use Changes and Use Settings

buttons in the Camera Raw palette


Color | Chapter 130 Camera Raw Palette

COLOR