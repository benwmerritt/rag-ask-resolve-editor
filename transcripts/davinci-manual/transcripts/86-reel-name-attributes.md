---
title: "Reel Name Attributes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 86
---

# Reel Name Attributes

The “Assist using Reel Names” checkbox in the General Options panel of the Project Settings is an

extremely important setting for controlling how the conform process works. By default it’s turned off,

and Reel Names are left blank. This is fine for conform workflows where all you need is the file path

or file name and source timecode to successfully identify which media files correspond to what clips.

However, if you need more information than that to reconform the clips in your project, you can turn

on the “Assist using Reel Names” checkbox to enable DaVinci Resolve to use one of four different

methods to automatically define reel names for every clip in the Media Pool.

Using the Clip Attributes dialog, you also have the option of manually defining how one or more

selected clips in the Media Pool have their Reel Names defined. This is useful when there are certain

clips in a project that need to use a different method of reel name extraction, or manually entered

reel names. Once you’ve used Clip Attributes to change the reel names of clips, those clips no longer

automatically update when you change the “Assist using Reel Names” options in the Project Settings.

You must first turn on “Assist using Reel Names” in the General Options of the Project Settings, and

choose a Reel Assist setting, for the reel name attributes in the Clip Attributes window to be editable.

The Reel Name panel of the Clip Attributes Window

�Source clip file pathname: Obtains the reel name by extracting it from each media file’s path.

This makes it possible to extract a reel name from all or part of the file name, or from all or part

of the name of any folder in the path that encloses that file. This extraction is defined using

the Pattern field.

�Pattern: A code that defines how a reel name should be extracted from the source clip pathname.

More information about creating patters appears later in this chapter.


Ingest and Organize Media | Chapter 22 Modifying Clips and Clip Attributes

MEDIA

�Media Pool bin name: The reel name is obtained from the name of the bin in the Media Pool that

encloses that clip. For example, in a stereoscopic workflow you might want to export offline stereo

media with the “Left” and “Right” bin names in which they’re organized as reel names. Another

example would be organizing VFX being incrementally processed in individually named bins, such

as “VFX_Tuesday_10-12.”

�Embedding in Source clip file: Useful for file formats where the reel name is embedded within the

media file itself. CinemaDNG and other digital cinema cameras, QuickTime files created by Final

Cut Pro, and DPX frame files are formats that can contain reel name header data.

�Source clip filename: If there is no defined reel number, often it’s easy to just use the

Source clip filename.

�User Defined: This option is only available when you manually alter the reel name for one or

more selected clips in the Media Pool using the Clip Attributes dialog. Choosing User Defined lets

you type any string of text you like to use as the reel name.

Update Timecode from Audio – LTC

Some cameras do not offer the ability to sync to an external timecode source. Their recorded

timecode may be time of day or free run timecode, but it would not be frame accurately synced to

other cameras, the dual system audio recorder or the digital slate. This makes multi-cam or dual sound

system syncing a time consuming manual operation.

DaVinci Resolve offers a solution to this problem if, by connecting an externally generated timecode to

the camera audio input, the video that’s recorded by the camera has a timecode reference recorded

on the audio track during the shoot.

Select this clip, or clips, in the media pool, then right-click on one of the highlighted clips and select

“Update timecode from audio - LTC.” DaVinci Resolve automatically and instantly updates the clip

timecode using the LTC it finds on the audio tracks. You can now use the clips as though they were

synced on set.

Changing Clip Thumbnails

in the Media Pool

When the Media Pool is in Thumbnail mode, each clip is represented by a small image that defaults to

the first frame of that clip. You can scrub the thumbnail of any clip to view its contents using the pointer

after hovering over it for a moment. However, when you’re done scrubbing, moving the pointer away

from any clip returns its thumbnail to the first frame of media, which may or may not be representative

of its contents. You can change this, if you like.

To customize the thumbnail of any clip:


Move the pointer over a clip you want to customize the thumbnail of.


Hover for a moment, then scrub to a representative frame.


Right-click that clip, and choose Set Poster Frame, or press Command-P.

To clear the custom poster frame of any clip:

�Right-click a clip, and choose Clear Poster Frame, or press Option-P.


Ingest and Organize Media | Chapter 22 Modifying Clips and Clip Attributes

MEDIA

Creating Subclips

Subclips give you another way of organizing media in the Media Pool, letting you break excessively

long clips into shorter ones. For example, if the director of a project is fond of “rolling takes” where

multiple takes are all recorded within a single clip, you can break these takes up by making them

into subclips.

To create a subclip:


Select any clip in the Media Pool to open it into the Viewer.


Set In and Out points to define the section you want to turn into a subclip.


Do one of the following:

�Right-click the jog bar and choose Make Subclip.

�Drag a clip from the Viewer or Source Viewer into the Media Pool.


A new subclip dialog appears, allowing you to name the subclip and decide to use its full extents

by turning on the checkbox.

The New SubClip dialog

Once created, subclips appear and work like any other clip in DaVinci Resolve. You can also create

subclips in the Media page while performing other organizational tasks there.

Removing or Changing Subclip Limits

Once created, you can right-click any subclip in the Media Pool or a timeline and choose Edit Subclip

to open a dialog in which you can turn on a checkbox to use the subclip’s full extents, or to change the

start or end timecode of the subclip via timecode fields, before clicking Update to modify the subclip.

The Edit Subclip dialog


Ingest and Organize Media | Chapter 22 Modifying Clips and Clip Attributes

MEDIA

Organizing Stereo 3D Media

When working with stereo media in DaVinci Resolve, one of the first tasks you must perform is that of

syncing each stereo pair of clips to act as a single clip. This is easily accomplished so long as you’re

careful about how you organize your media in the Media Pool.

Each set of right- and left-eye media should always be organized into separate left-eye bins and right-

eye bins, to facilitate later syncing of these clips using the Stereo 3D Sync command in the Media Pool

contextual menu.

For more information about setting up media for stereo workflows, “see Chapter 15,

“Stereoscopic Workflows.” In section called “Stereoscopic Workflows”

Camera Raw Decoding

Camera raw media formats are so named because they capture raw color space data directly from the

sensor of whatever digital cinema camera did the recording. Raw image data is not human readable,

and must be debayered or demosaiced to convert the original raw data into image data that can be

handed off to DaVinci Resolve’s image processing pipeline.

There are four ways you can control how camera raw media is debayered into a useful, “normalized”

image for adjustment or output:

�The Camera Raw panel of the Project Settings contain groups of parameters that correspond to

every camera raw media format that’s supported by DaVinci Resolve. Using these parameters

in the Camera Raw panel, you can override the original camera metadata that was written at

the time of recording, and make simultaneous adjustments to all camera raw media throughout

your project.

�The Image Panel in the Inspector also contains the controls for every raw media format

that’s supported by DaVinci Resolve. Allowing you to select all, some, or individual clips

for raw debayering.

�The Camera Raw palette in the Color page lets you individually adjust Camera Raw parameters

for individual clips in the Timeline.

�When you use Resolve Color Management (RCM) in a project that uses Camera Raw formats,

color science data from each camera manufacturer is used to debayer or demosaic each camera

raw file to specific color primaries with linear gamma, so that all image data from the source is

preserved and made available to DaVinci Resolve’s color managed image processing pipeline.

As a result, the Camera Raw project settings and Camera Raw palette of the Color page are

disabled, because RCM is controlling the debayering of all camera raw clips, and all image data

from the raw file is available for conversion to the Timeline Color Space you choose to work with

as you grade.

For more information about each of the Camera Raw formats that can be adjusted in

DaVinci Resolve, see Chapter 7, “Camera Raw Settings.”


Ingest and Organize Media | Chapter 22 Modifying Clips and Clip Attributes

MEDIA

Chapter 23

Using

Scene Detection

If you have a program that someone has delivered as a single media file, with no

accompanying EDL with which to split it up, you can use DaVinci Resolve’s Scene

Detect window to automatically find the cut points and split it into individual clips,

ready for grading.

Contents

Scene Cut Detection on the Timeline (Studio Version Only)������������������������������������������������������������������������������������������ 458

Scene Detection in the Media Page������������������������������������������������������������������������������������������������������������������������������������������� 459

The Scene Detect Window Interface������������������������������������������������������������������������������������������������������������������������������������������ 459

The Scene Detect Viewers�������������������������������������������������������������������������������������������������������������������������������������������������������������� 459

The Scene Detect Graph�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 461

Cut List������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 462

The Scene Detect Options Drop-down Menu������������������������������������������������������������������������������������������������������������������������ 463

An Example Scene Detect Workflow����������������������������������������������������������������������������������������������������������������������������������������� 463


Ingest and Organize Media | Chapter 23 Using Scene Detection

MEDIA