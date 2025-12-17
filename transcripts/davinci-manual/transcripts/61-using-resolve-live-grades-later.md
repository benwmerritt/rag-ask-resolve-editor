---
title: "Using Resolve Live Grades Later"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 61
---

# Using Resolve Live Grades Later

Since each Snapshot you capture during a Resolve Live session contains timecode that was captured

from the camera, grades from snapshots with timecode that overlaps recorded camera original media

can be synced using ColorTrace when the time comes to start making dailies.

Keep in mind that snapshot grades correspond to the monitored output of the camera during the

shoot. If you shot using a raw format, you’ll need to use whatever in-camera debayering settings

were used for monitoring during the shoot if you want the grades from your snapshots to produce the

same result.

For more information on using ColorTrace, see Chapter 149, “Copying and Importing Grades

Using ColorTrace.”

Using LUTs in Resolve Live Workflows

Many on-set workflows use Lookup Tables (LUTs) to calibrate displays, normalize log-encoded media

for monitoring, and preview looks in the video village to test how the current lighting scheme will work

with the intended grade. You can apply LUTs using the Lookup Tables section of the Project Setting’s

Color Management panel, or within a grade as part of a node tree.

However, you can also export LUTs, if necessary for monitor previewing, that you can apply by loading

them into a compatible LUT box of some kind, connected in-between the camera’s video output and a

display, or using a display capable of  loading LUTs internally.

If you’re exporting LUTs using the Generate 3D LUT command of the Thumbnail timeline’s contextual

menu, you should limit yourself to using only Primaries palette and Custom Curves palette controls

within a single node. These are the only grading controls that can be mathematically converted

into a LUT.

When exporting a LUT, any nodes that use Windows or OpenFX will be ignored along with all

corrections made within these nodes. All other nodes with Primaries palette and Custom Curves

palette adjustments that can be translated into a LUT will have their combined result translated

into a LUT. For any nodes that mix supported and unsupported adjustments for LUT export (such as

sharpening or blur filtering operations), the unsupported adjustments will simply be ignored.

For more information on exporting LUTs, in “Exporting Grades and LUTs” see Chapter 142,

“Grade Management.”

NOTE: DaVinci Resolve exports LUTs in the .cube format, which is a DaVinci-developed

LUT format, with no relation to the Adobe SpeedGrade.cube format.


Setup and Workflows | Chapter 14 Resolve Live

MEDIA

Chapter 15

Stereoscopic

Workflows

DaVinci Resolve has robust support for a wide variety of stereoscopic workflows.

Using the built-in tools of the Studio version of DaVinci Resolve, you can edit using

stereoscopic clips, grade the resulting program, adjust each clip’s stereo‑specific

properties such as convergence and floating windows, and master stereoscopic

output, all within DaVinci Resolve.

Contents

Stereoscopic Workflows�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 321

Hardware Requirements for Working in Stereo 3D������������������������������������������������������������������������������������������������������������� 321

Setting Up to Display Stereo 3D via SDI����������������������������������������������������������������������������������������������������������������������������������� 322

Setting Up to Display Stereo 3D via HDMI������������������������������������������������������������������������������������������������������������������������������� 322

Supported Stereo 3D Media����������������������������������������������������������������������������������������������������������������������������������������������������������� 323

Using Dual Sets of Media in Any Supported Format����������������������������������������������������������������������������������������������������������� 323

Using Stereoscopic OpenEXR Media����������������������������������������������������������������������������������������������������������������������������������������� 323

Using Stereoscopic CineForm Media����������������������������������������������������������������������������������������������������������������������������������������� 323

Creating Stereo 3D Clips From Separate Files��������������������������������������������������������������������������������������������������������������������� 324

Step 1 – Import and Organize Your Media�������������������������������������������������������������������������������������������������������������������������������� 324

Step 2 – Generate 3D Stereo Clips���������������������������������������������������������������������������������������������������������������������������������������������� 324

Step 3 – (Optional) Create Optimized Media��������������������������������������������������������������������������������������������������������������������������� 326

Monitoring Stereoscopic 3D in the Edit Page����������������������������������������������������������������������������������������������������������������������� 326

Converting Clips Between Stereo and Mono������������������������������������������������������������������������������������������������������������������������ 326

Converting Stereo Clips Back to Mono�������������������������������������������������������������������������������������������������������������������������������������� 326

Converting Mono Clips or an Entire Timeline to Stereo���������������������������������������������������������������������������������������������������� 327

Attaching Mattes to Stereo 3D Clips������������������������������������������������������������������������������������������������������������������������������������������ 327

Organizing and Grading Stereo 3D Dailies����������������������������������������������������������������������������������������������������������������������������� 328

Step 1 – Create 3D Stereo Clips���������������������������������������������������������������������������������������������������������������������������������������������������� 328

Step 2 – Edit the New Stereo Clips Into One or More Timelines for Grading��������������������������������������������������������� 328

Step 3 – Align Your Media���������������������������������������������������������������������������������������������������������������������������������������������������������������� 328


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Step 4 – Grading Stereo Media����������������������������������������������������������������������������������������������������������������������������������������������������� 328

Step 5 – Output Offline or Online Media for Editing����������������������������������������������������������������������������������������������������������� 330

Conforming Projects to Stereo 3D Media�������������������������������������������������������������������������������������������������������������������������������� 331

Grading Mastered Stereoscopic Media From Tape�������������������������������������������������������������������������������������������������������������� 331

Adjusting Clips Using the Stereo 3D Palette�������������������������������������������������������������������������������������������������������������������������� 331

Stereo Eye Selection��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 332

Stereo 3D Geometry Controls�������������������������������������������������������������������������������������������������������������������������������������������������������� 333

Swap and Copy Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 334

Automatic Image Processing for Stereo 3D����������������������������������������������������������������������������������������������������������������������������� 335

Stereo 3D Monitoring Controls������������������������������������������������������������������������������������������������������������������������������������������������������ 337

Floating Windows��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 338

Outputting Stereo 3D Media in the Deliver Page���������������������������������������������������������������������������������������������������������������� 340

Rendering Frame-Compatible Media����������������������������������������������������������������������������������������������������������������������������������������� 340

Rendering Individual Left- and Right-Eye Clips��������������������������������������������������������������������������������������������������������������������� 340

Apple Spatial Video (MacOS only)������������������������������������������������������������������������������������������������������������������������������������������������ 341

Using Apple Spatial Video in DaVinci Resolve����������������������������������������������������������������������������������������������������������������������� 341

Stereoscopic Workflows

Creating a stereo 3D project is a multi-step process that benefits from careful media organization.

This chapter covers how to set up for working on stereoscopic projects, how to import stereoscopic

projects, and how to export stereoscopic media.

First, stereoscopic pairs of clips, i.e., the individual left- and right-eye media files, are imported into the

Media Pool, organized, and then linked together using the “Stereo 3D Sync” command to create a new

set of linked stereo clips. Then, these clips stereo clips can be either edited or conformed to imported

project data using a single Timeline. DaVinci Resolve lets you manage left- and right-eye grades and

sizing in the Color page using the controls found in the shortcut menu of the Thumbnail timeline, and in

the Stereo 3D palette.

If you’re using stereoscopic CineForm media, which contains muxed left-eye and right-eye image data

that can be decoded by DaVinci Resolve, you still need to go through this process, although you’ll be

using duplicate clips to populate Left and Right folders with matching sets of clips.

Hardware Requirements for

Working in Stereo 3D

With DaVinci Resolve on Mac systems, dual 4:2:2 Y’CbCr stereoscopic video streams are output via

SDI from a compatible Blackmagic Design video interface. You can select either Side-by-Side or Line

Mesh output to be fed to your stereo 3D-capable display, depending on its compatibility. Alternately,

if you turn on the “Enable Dual SDI 3D Monitoring” checkbox in the Video Monitoring group of the

Master Settings panel of the Project Settings, your compatible Blackmagic Design video interface

outputs full resolution 4:2:2 Y’CbCr for each eye to compatible displays.

When setting up a 3D-capable DaVinci Resolve workstation, keep in mind that the dual video streams

of 3D projects make greater demands on disk bandwidth, media decoding via your workstation’s CPU,

and effects processing via your workstation’s available GPU cards.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Setting Up to Display Stereo 3D via SDI

All DaVinci Resolve systems can output a side-by-side frame-compatible signal that can be viewed on

a stereo 3D-capable display via a single SDI connection, output from a DeckLink HD Extreme card or

better. For higher-quality monitoring, two SDI signals can be used to output the left-eye and right-eye

images separately at full resolution using one of the following Blackmagic Design video interfaces:

�DeckLink HD Extreme 3D+

�DeckLink 4K Extreme

�DeckLink 4K Extreme 12G

�DeckLink 8K Pro

�UltraStudio 4K

�UltraStudio 4K Extreme

�UltraStudio 4K Extreme 3

Very old legacy systems accomplish this via NVIDIA dual SDI monitoring outputs.

NOTE: If your stereo display is not capable of multiplexing the two incoming SDI signals by

itself, you can accomplish this using an external device to multiplex both SDI signals into

a single stereo 3G signal that will be compatible. Check with your display manufacturer in

advance to see if this is necessary.

The following procedures describe how to set up stereo 3D monitoring in two different ways.

Monitoring via dual SDI to dual SDI:


Open the Master Settings panel of the Project Settings, then do the following:

�Make sure the Use 4:4:4 SDI checkbox is unchecked.

�Turn on the “Use dual outputs on SDI” checkbox.


Open the Stereo 3D palette in the Color page, and do the following:

�Set Vision to Stereo.

�Set the Out pop-up menu to None.

NOTE: When “Enable dual SDI 3D monitoring” is turned on, split-screen wipes and cursors

will not be visible on the grading monitor, nor will you be able to view image resizing.

Setting Up to Display Stereo 3D via HDMI

If your stereo-capable display only has HDMI input, you’ll need to use the HDMI output of a compatible

Blackmagic Design video interface that has HDMI 1.4 or better to output stereo 3D signals; see the

documentation accompanying your video interface for more information.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Supported Stereo 3D Media

When importing stereo 3D media from other applications, there are two types of media that are

compatible with DaVinci Resolve stereoscopic workflows.

Using Dual Sets of Media in Any Supported Format

When originally shot, the media corresponding to stereo 3D workflows consists of two directories, one

for the left-eye media, and one for the right-eye media. For the most automated workflow possible,

this media must be tightly organized. Each pair of left-eye and right-eye media files in both directories

should have matching timecode, and reel numbers that clearly indicate which are the left-eye shots,

and which are the right-eye shots. When organized in this way, it’s relatively easy to use DaVinci

Resolve to convert each matching pair of clips into the stereo 3D clips that you’ll need to work in

DaVinci Resolve. This process is covered in detail in a subsequent section.

Using Stereoscopic OpenEXR Media

DaVinci Resolve is compatible with stereo OpenEXR files to accommodate professional cinema and

specialty workflows. Stereo OpenEXR clips include the media for both eyes stored as separate parts

so that a single OpenEXR file may output either a single image or stereo 3D images when used with

an application that supports it, such as DaVinci Resolve. This means you can edit stereo OpenEXR

media, grade it, and make all of the stereoscopic adjustments that the Stereo palette of the Color

page supports.

If you import stereo OpenEXR clips to the Media Pool, they will at first appear to be regular non-stereo

clips that output a single image. However, these can easily be converted to stereo 3D clips using the

following procedure.

To set stereo OpenEXR clips to be usable as stereo clips:


Import the OpenEXR media to the Media Pool as you would any other clips.


Select one or more OpenEXR clips, then right-click the selection and choose “Convert to Stereo”

from the contextual menu. Those clips will now appear with a stereo 3D badge to indicate that

they’re stereo.

Using Stereoscopic CineForm Media

DaVinci Resolve is also compatible with CineForm stereo QuickTime files. CineForm clips encode

the media corresponding to both eyes and mux (multiplex) it together in such a way so that CineForm

files may output either a single frame of image data, if used in an application that is not capable of

stereoscopic processing, or stereo 3D media when used with an application that is, such as DaVinci

Resolve. This means that you can edit CineForm media using nearly any NLE, export a project via

whatever workflow is convenient, and end up with a stereoscopic project that can be graded in

DaVinci Resolve.

There are two ways of creating CineForm files. One is by using a camera or recording system that

processes dual synchronized video signals to create a single set of CineForm media. The other is to

use the CineForm conversion tools that come with GoPro CineForm Studio to reprocess dual sets of

stereo 3D assets into the CineForm format.

The CineForm codec itself encodes full-frame image data using wavelet compression, at any

resolution, at up to 12-bits, in a choice of RGB, Y’CbCr, or RAW color spaces. DaVinci Resolve is

compatible with CineForm in a QuickTime wrapper using any supported color space, allowing access

to the dual streams of image data that are provided.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

When the time comes to output your program, keep in mind that while DaVinci Resolve can read

CineForm files, CineForm files cannot be rendered out of DaVinci Resolve unless you’ve purchased

an encoding license for OS X or Windows from GoPro. Furthermore, DaVinci Resolve cannot render

Stereoscopic CineForm files.

If you import stereo CineForm clips to the Media Pool, they will at first appear to be regular non-stereo

clips that output a single image. However, these can easily be converted to stereo 3D clips using the

following procedure.

To set stereo CineForm clips to be usable as stereo clips:


Import the CineForm media to the Media Pool as you would any other clips.


Select the CineForm media you need to convert, then right-click the selection and choose

“Convert to Stereo” from the contextual menu. Those clips will now appear with a stereo 3D badge

to indicate that they’re stereo.