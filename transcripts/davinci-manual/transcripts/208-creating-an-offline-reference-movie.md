---
title: "Creating an Offline Reference Movie"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 208
---

# Creating an Offline Reference Movie

Even though the colorist in any given workflow is likely to be building new grades from scratch,

it can be valuable to have a reference movie showing any color corrections, filters, or effects that

the offline editor applied during the editing process. This offline reference can be imported into a

DaVinci Resolve project, and used as a split-screen reference whenever there’s some question about

a look or effect from the offline edit.

Offline reference movies also serve as a useful tool when conforming a project in the Edit page.

After project conform, you can compare the project as seen in the Record Viewer with the

synchronized offline movie as seen in the Source Viewer set to Offline mode. This makes it easy to

scrub through a project to make sure that each clip has imported correctly and is in sync.

More information about using offline reference movies appears later in this chapter.

Mixed Frame Sizes and Mixed Codecs

Most NLEs can freely mix media using different frame sizes, different codecs, and different frame rates.

DaVinci Resolve deals with these combinations in different ways, depending on what settings you’ve

selected in the Project Settings.

Mixing Frame Sizes: Mixed frame sizes are easily handled. The Set Timeline Resolution To

parameter in the Project Settings panel of the Project Settings dictates the current resolution

of the project. Any clips with a frame size that doesn’t match the project is resized according

to the option selected in the Image Scaling panel of the Project Settings. You can, of course,

always manually readjust the sizing of any clip if you want to make a specific adjustment.

All resizing is done using the optical-quality resizing algorithms in DaVinci Resolve.

For more information, see Chapter 152, “Sizing and Image Stabilization.”

Mixing Codecs: Mixed codecs are also not a problem, as long as the different codecs used

by the media in the project you’re importing are compatible with the list of codecs and formats

that DaVinci Resolve supports. For more information about the currently supported list of

codecs and formats, check the Blackmagic Design support page for DaVinci Resolve. This list

is updated often with newly supported formats.

Mixed Frame Rates

DaVinci Resolve also supports mixed frame rates, although there is a setting you must choose to

ensure the best results for the NLE you’re importing from. By default, mixed clip frame rate support

is enabled via the “Mixed frame rate format” pop-up menu that appears either in the Master Project

Settings, or in the Import AAF or XML dialog.

The different options available in the “Mixed frame rate format” pop-up are available to let you conform

projects using the method of mixed frame rate calculation used by the NLE a project was originally

edited in; different NLEs have different ways of mixing frame rates, and that used by Final Cut Pro 7 is

different from that used by Final Cut Pro X or Avid Media Composer. If you need to change this setting,

you must do so before you import any media into the Media Pool; once the Media Pool is populated,

this setting can no longer be changed.


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT

Mixed frame rate format selection

This Mixed frame rate format pop-up menu is also found in the Load AAF and Load XML dialogs.

DaVinci Resolve automatically chooses a setting from the “Mixed frame rate format” pop-up menu

that corresponds to the project file you’re importing, but in some cases you can override this

setting if necessary. For projects sent from Final Cut Pro, you can choose either “Final Cut Pro 7” or

“Final Cut Pro X” to match the type of project you’re importing. On the other hand, you should choose

“Resolve” for projects imported from Premiere Pro, Smoke, Media Composer, or other NLEs.

When “Mixed frame rate format” is set to anything but None, DaVinci Resolve conforms and processes

all clips in the Timeline to play at the project’s frame rate. For example, 23.98, 29.97, 30, 50, 59.94,

and 60 fps clips will all play at 24 fps if that’s what “Timeline frame rate” is set to in the Master Project

Settings. Clips with different source frame rates will be retimed to match the Timeline conform frame rate.

The Retime process that’s used to render clips with differing frame rates can be changed for individual

clips via the Retime Process parameter in the Edit page Inspector, or it can be changed project-wide

using the Retime Process parameter found in the Frame Interpolation panel of the Master Project

Settings.

For more information on how each of the three available options work, see the

“Frame Interpolation” section see Chapter 4, “System and User Preferences.”

If you choose “None,” then clips with frame rates that aren’t equal to the Timeline frame rate will ignore

their original frame rate and will play at the Timeline rate, resulting in either faster or slower motion,

depending on the difference between the original and Timeline frame rates.

NOTE: Because DPX files often either lack or have incorrect frame rate information in

the header data, you may need to select None when conforming a project using image

sequences to make sure your media is not incorrectly interpreted.


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT

How clips in mixed frame rate timelines are rendered depends on whether the Render Settings are set

to render individual source clips or one single clip. When you render the Timeline as ”Individual Source

Clips,” then all clips are rendered individually at their original frame rate. If you select ”Single Clip,”

then all clips are converted to the “Timeline frame rate” frame rate setting, and rendered as a single

media file.

Importing Effects when Conforming Edits

DaVinci Resolve is capable of translating a subset of the effects exported within XML, AAF, and EDL

project files into their DaVinci Resolve equivalents. The following chart illustrates which effects are

supported, and for which project import formats.

Unsupported effects are neither imported nor displayed in DaVinci Resolve. However, the majority of

unsupported effects are preserved internally, and are reinserted into exported XML or AAF files so

that those effects will reappear in your NLE once the project is reimported.

EDL

FCP 7 XML

FCP X XML

AAF

Color Corrections

No

No

Yes

No

Composite Modes

No

Yes

Yes

Overlay only

Multiple Tracks

No

Yes

Yes

Yes

Video Transitions

Yes

Yes

Yes

Yes

Audio Transitions

No

No

No

Yes

Opacity Settings

No

Yes

Yes

Yes, via 3D Warp

or Superimpose

Position, Scale, Rotation

No

Yes

Yes

Yes, via 3D Warp

Flip and Flop

No

No

No

Yes, via Flip, Flop, or

Flip‑Flop effects

Pitch and Yaw

No

No

No

Yes, via 3D Warp

Linear Speed Effects

Yes

Yes

Yes

Yes

Variable Speed Effects

No

Yes

Yes

Yes

Still Image Clips

No

All supported formats

in Resolve

All supported formats

in Resolve

All supported

formats in Resolve

Freeze Frames

No

No

No

Yes

Nested Sequences

No

Yes

Yes

No

Linked Clip Audio

Yes

Yes

Yes

Yes

Mixed Frame Rates

No

Yes

Yes

Yes

Text Generators

No

Yes

Yes

No

Effects supported with imported AAF, XML, and EDL


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT

About Supported Color Corrections

At the time of this writing, only Final Cut Pro X XML projects are capable of exporting color correction

data that can be imported as primary grades in DaVinci Resolve. For obvious reasons, color correction

import is a one-way street, and imported color corrections cannot be output back to Final Cut Pro.

Imported Final Cut Pro X color adjustments appear in the Color page as primary corrections.

Other workflows for importing color correction information from other applications are available

using ColorTrace to import grade data from CDLs (Color Decision Lists). For more information,

see the “Copying Grades Using ColorTrace” section in Chapter 186, “Copying and Importing Grades

Using ColorTrace.”

About Supported Transitions

EDLs are the most restrictive when it comes to transition support in DaVinci Resolve, as only Cross

Dissolves will be read. Any other transitions appearing in an EDL will be automatically converted to a

Cross Dissolve of the same duration when it’s imported into DaVinci Resolve.

On the other hand, DaVinci Resolve supports the import of ten different transitions when importing

XML project files from Final Cut Pro X and legacy Final Cut Pro 7, or nine different transitions when

importing AAF files from Avid Media Composer or Symphony.

EDL

FCP XML

AAF

Clock Wipe

No

Yes

Yes

Center Wipe

No

Yes

Yes

Cross Dissolve

Yes

Yes

Yes

Additive Dissolve

No

Yes

No

Dip to Color Dissolve

No

Yes

Yes

Edge Wipe

No

Yes

Yes

Venetian Blind Wipe

No

Yes

Yes

Cross Iris

No

Yes

Yes

Diamond Iris

No

Yes

Yes

Oval Iris

No

Yes

Yes

Supported transitions for imported EDL, XML, and AAF


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT

Transition Names

To help you prepare projects for export, note that the names of transitions vary between XML

and AAF project files. Here are the supported transitions as they appear in Avid Media Composer

and Symphony.

Dip to Color Dissolve

Dip to Color effect in the Blend category

Edge Wipe

Horizontal/Vertical/Lower Left/Lower Right/Upper Left/Upper Right Diagonal

effects in the Edge Wipe category

Center Wipe

Horizontal Open and Vertical Open effects in the Edge Wipe category

Clock Wipe

Clock effect in the Shape Wipe category

Venetian Blind Wipe

Vertical Blinds and Horizontal Blinds effects in the Shape Wipe category

Cross Iris

4 Corners effect in the Shape Wipe category

Diamond Iris

Diamond effect in the Shape Wipe category

Oval Iris

Circle effect in the Shape Wipe category

About Supported Opacity, Position, Scale, and Rotation Settings

When importing XML project files from Final Cut Pro X, Premiere Pro, or legacy Final Cut Pro 7, DaVinci

Resolve supports the import of Opacity, Position, Scale, and Rotation settings. Imported Composite

and Transform settings for any given clip appear in the Inspector of the Edit page, or in the Edit Sizing

mode of the Sizing palette in the Color page. If these settings have been keyframed, the animation will

appear in DaVinci Resolve.

When importing AAF files from Media Composer or Symphony, DaVinci Resolve supports the

import of Opacity, Resize, and 3D Warp effects, which are converted into Pan, Tilt, Zoom, and Rotate

settings in DaVinci Resolve, located in the Edit page Inspector or the Edit Sizing mode of the Sizing

palette in the Color page.

About Flip and Flop Support

When importing AAF project files from Media Composer or Symphony, Flip, Flop, and Flip-Flop effects

are converted into the equivalent horizontal and vertical Flip toggles in DaVinci Resolve, located in the

Edit page Inspector or the Edit Sizing mode of the Sizing palette in the Color page.

Pitch and Yaw

When importing AAF files from Media Composer or Symphony, DaVinci Resolve supports the

import of Pitch and Yaw 3D Warp effects, which are converted into equivalent Pitch and Yaw settings

in DaVinci Resolve, located in the Edit page Inspector or the Edit Sizing mode of the Sizing palette

in the Color page.


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT