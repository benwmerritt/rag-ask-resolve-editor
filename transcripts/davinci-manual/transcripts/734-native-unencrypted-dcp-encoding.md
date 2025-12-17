---
title: "Native Unencrypted DCP Encoding"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 734
---

# Native Unencrypted DCP Encoding

and Decoding (Studio Version Only)

DaVinci Resolve also has native DCP encoding and decoding support built-in, for unencrypted

DCP files only. That means that you can output and import (for test playback) unencrypted DCP files

without needing to purchase a license of EasyDCP. If you have a license, a setting in the Configuration

panel of the System Preferences enables you to choose whether to use EasyDCP (for creating

encrypted DCP output), or the native DaVinci Resolve encoding.

Native DCP Encoding Parameters

When you choose DCP from the Format dropdown menu, the following additional parameters

are exposed:

�HDR: (DCP, IMF) Specifies the package as having HDR content.

�Use interop packaging: (DCP only, located under Type parameter) Lets you create an Interop

DCP package, based on an earlier standard of DCP delivery that is not forward compatible with

SMPTE DCP packages.

�Maximum bit rate: (DCP, IMF) Lets you choose how much to compress the result.

�Lossless Compression: (IMF) Lets you choose to encode using lossless compression.

�Slope-Rate Control: (DCP, IMF) A checkbox lets you specify lossless compression.

�Quality: (DCP, IMF) Lets you choose either automatic or manually specified DCP quantization

levels at which to compress the video signal when using the Kakadu JPEG 2000 encoder.

Native DCP settings in DaVinci Resolve


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER

If you’ve selected DCP from the Format dropdown menu, a Composition Settings group appears with

the following parameters when you click the disclosure control, which let you populate standard DCP

composition metadata:

�Composition name: The name of the exported composition. DCPs use specific naming

conventions for the composition name that include metadata about the file itself for DCP

projectors and playback equipment. DaVinci Resolve has a tool called the Composition Name

Generator to generate these names properly for you; it is accessed by pressing the “Edit” button

next to this field. Simply fill out the fields and press OK, and DaVinci Resolve will rename your

composition in line with these standards.

The Composition Name Generator will pass a standards

compliant name for you to the Composition Name field.

�Issuer: The organization providing the composition.

�Use current date: A checkbox that lets the current date be used as the Issue date automatically.

�Issue date: The date the composition is issued.

�Content kind: A dropdown provides a list of acceptable choices for defining the content.

�Content version label: Meant to identify the version of the content being provided.

�Annotate xml using composition name: Auto-populates Asset Map, Composition Playlist, and

Packing List with data from the project. Otherwise these three fields are manually editable.

�Annotate reel index as suffix: Auto-populates Reel Annotation with data from the project.

Otherwise this is manually editable.

�Annotate media using filename: Auto-populates Main Video Track and Audio Track 1 with data

from the project. Otherwise these three fields are manually editable.


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER

Parameters for adding composition metadata

Rendering IMF Segments and DCP Reels

DaVinci Resolve supports splitting IMF and DCP projects into separate segments and reels, in addition

to rendering media as a single file. This can be useful for breaking up your timeline to fit within allowed

file sizes on legacy file systems, separating marketing and studio assets from the final film, or just

being able to replace certain sections of the film without having to re-encode the entire file.

To Render an IMF Segment or DCP Reel:


Choose IMF or DCP from the format settings in the Video tab of the Render Settings panel.


Navigate to the “Segment list” or “Reel list” section of the composition settings.


Choose from the following options:

Single segment/reel: Encodes the Timeline into a single file (default setting).

Regular intervals of: Encodes the Timeline into multiple segments/reels, each one the duration of

the value set in the “mins” field.

Align to clips on the first video track: Encodes the Timeline into multiple segments/reels; each

individual clip on the V1 track of the Timeline becomes its own separate file.

Keep audio as single segment (IMF only): Select this checkbox to keep the audio portion of the

IMF as a single file, regardless of the segment options selected above.


Press the Add to Render Queue button.

IMF Segment options


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER

Creating DCP/IMF Supplemental Packages

Once created, DaVinci Resolve has the ability to reimport a DCP or IMF so that you can overwrite

parts that need to be updated with new media, in order to export a “Supplemental Package,” which is

effectively a new version of the program that combines the new overwritten parts of the program with

the old version, such that you can deliver just the changes.

NOTE: Supplemental packages are only supported using the Kakadu encoder and decoder;

this is not compatible with DCP or IMF packages created using EasyDCP. To avoid issues,

disable “Use easyDCP decoder” in the Decode Options panel of the DaVinci Resolve

System Preferences.

Importing a DCP or IMF Into a Timeline


Using the Media Storage browser in the Media page, find and select the DCP or IMF, and check

the header of the Metadata Editor to verify that your media is suitable for creating a supplemental

package. Supported IMF profiles will be displayed in the Metadata Viewer.

The header in the Metadata Editor showing an IMF that’s

compatible with the creation of a supplemental package


Create a new project and add the DCP/IMF package you need to modify to the Media Pool. If a

dialog appears asking if you want to change your timeline frame rate to match the incoming media,

click Change to make your project match the media.


Create a timeline from the composition playlist (XML) within the imported DCP or IMF by right

clicking the imported package in the media pool and choosing “Create New Timeline Using

Composition Playlist” from the contextual menu.

Right-clicking an imported IMF or DCP clip in the Media

Pool reveals a command to make a new timeline using

the composition playlist in the contextual menu


The New Timeline dialog has an “Import Dolby Vision Project Settings” checkbox. When it’s turned

on, clicking Create will do the following:

a)	 Dolby Vision will be enabled in the Color Management panel of the Project Settings, and the

Mastering Display menu will be set to match that of the IMF package.

b)	 If Resolve Color Management (RCM) is not active, the Timeline Color Space will be set to

match the Dolby Vision metadata. However, if RCM is already enabled, the user must manually

set this by turning on “Use Separate Color Space and Gamma,” and changing the Timeline

settings to P3-D65” and “ST.2084” respectively.


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER


Creating the Timeline will import Dolby Vision metadata (if applicable). This will allow a

Tone Mapping preview to be seen on the Color page that uses the original metadata.

Dolby Vision metadata will be imported if present when importing an IMF

Once import is complete, all video and audio clips from the DCP or IMF appear within a new

bin with the name of the package. The resulting timeline will be identified via its icon as a

DCP/IMF timeline.

The imported media and timeline when you import an IMF

Editing the Resulting Timeline

At this point, you can edit the program in the Timeline as necessary.

�You can overwrite sections of the Timeline with new clips. All modifications will be automatically

included into the supplemental package.

�You can use the Blade tool or Insert Edit command to cut sections of the existing program to

which you want to add Fusion effects, audio grading, or color correction. When you do this,

you must right click that section and choose “Include in Supplemental Package” to make sure it

exports correctly.

Right-clicking a section of the program and choosing

Include In Supplemental Package

For IMF Dolby Vision packages, please ensure all modifications are on the first video track (V1).

NOTE: If RCM is being used, please ensure the input color space and gamma of the inserts

are correct.


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER