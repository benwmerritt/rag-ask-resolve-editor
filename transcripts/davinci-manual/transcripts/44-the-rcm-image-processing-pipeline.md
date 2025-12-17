---
title: "The RCM Image Processing Pipeline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 44
---

# The RCM Image Processing Pipeline

The previous explanation is, of course, simplified. To clarify the inner workings of Resolve Color

Management for advanced users, the following flowchart presents a rudimentary overview of how

every parameter works together to automatically manage the color of clips in your program.

Input Color

Space

Input DRT

Timeline

Color

Space

Output DRT

Your

Grade

Ouput Color

Space

Final Output

Timeline Working

Luminance

Source

Media

Manual Color

Space Tagging

or

Source Media Color

Space Metadata

or

Input Color Space

Project Setting

Affects

Input DRT

Resolve Color Management Parameters

Affects

Output DRT

Resolve Color Management’s image processing pipeline, illustrated

Identifying the Input Color Space of Different Clips

Central to the process of automated color management is knowing the color space and transfer

function used by every clip of source media in your project. There are a variety of ways DaVinci

Resolve can figure this out, in a cascading decision-tree that can be manually overridden if necessary.

Deriving the Input Color Space involved the following stages of automated decision making:


If the source media is a camera raw format like .braw, .R3D, .ari, etc., DaVinci Resolve uses

manufacturer-supplied colorimetry to automatically debayer the clip and identify its Input

Color Space.


Otherwise, if the source media has embedded color space metadata (QuickTime or .MXF make

this possible), then use that to identify the Input Color Space.


Otherwise, if there is no embedded color space metadata, use the default Input Color Space

setting of the Project Settings to assign an Input Color Space to all otherwise unidentified clips.


If necessary, you can manually set the Input Color Space of clips in the Media Pool, which

overrides both embedded color space metadata (in case it’s wrong), or the default Input Color

Space setting (if you’re dealing with multiple color spaces). You cannot override the Input Color

Space of camera raw media.

The following sections discuss each of these steps in more detail.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Using Camera Raw Formats

When you use RCM in a project that uses Camera Raw formats, color science data from each camera

manufacturer is used to debayer each camera raw file to specific color primaries with linear gamma,

so that all image data from the source is preserved and made available to DaVinci Resolve’s color

managed image processing pipeline. As a result, the Camera Raw project settings and Camera Raw

palette of the Color page are disabled, because RCM now controls the debayering of all camera

raw clips, and all image data from the raw file is available no matter which Timeline Color Space you

choose to work within.

Using Source Media Color Space Metadata

When enabled, RCM automatically identifies the color space information of imported media that’s

been either transcoded or recorded directly to supported non-raw media formats, reading the NCLC

metadata of QuickTime-wrapped files, the color space metadata of .mxf-wrapped files, and the XML

sidecar files that track color management in ACES workflows. This behavior is automatic; there are no

visible controls governing this behavior aside from the individual Input Color Space and Input Gamma

settings associated with each clip in the Media Pool.

Color Space Metadata in QuickTime

DaVinci Resolve is capable of reading the NCLC metadata found within media files wrapped within a

QuickTime container for proper color management. This metadata consists of three values formatted

as (for example) 1-1-1. From left to right, these three digits specify the Color Primary (or color space),

Transfer Function (or gamma), and Color Matrix used by that media file.

These values are standardized in the SMPTE Registered Disclosure Document RDD 36:2015. For your

information, the different codes are listed in the following table. In the previous example, the code

of 1-1-1 indicates a standard dynamic range clip that uses the BT.709 primaries, transfer function,

and color matrix.

Color Primary

Transfer Function

Color Matrix


Reserved


Reserved


GBR


ITU-R BT.709


ITU-R BT.709


BT709


Unspecified


Unspecified


Unspecified


Reserved


Reserved


Reserved


ITU-R BT.470M


Gamma 2.2 curve


FCC


ITU-R BT.470BG


Gamma 2.8 curve


BT470BG


SMPTE 170M


SMPTE 170M


SMPTE 170M


SMPTE 240M


SMPTE 240M


SMPTE 240M


FILM


Linear


YCOCG


ITU-R BT.2020


Log


BT2020 Non-

constant Luminance


SMPTE ST 428-1


Log Sqrt


BT2020

Constant Luminance


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Color Primary

Transfer Function

Color Matrix


DCI P3


IEC 61966-2-4

–

–


P3 D65


ITU-R BT.1361 Extended

Colour Gamut

–

–

–

–


IEC 61966-2-1

–

–

–

–


ITU-R BT.2020 10 bit

–

–

–

–


ITU-R BT.2020 12 bit

–

–

–

–


SMPTE ST 2084 (PQ)

–

–

–

–


SMPTE ST 428-1

–

–

–

–


ARIB STD-B67 (HLG)

–

–

The Default Input Color Space

The default Input Color Space can only be set if the “Resolve color management preset” drop-down

menu is set to Custom. Otherwise, it defaults to “Rec. 709 Gamma 2.4” for all presets. Or else, this

setting is the default color space that all otherwise unidentified clips in the Media Pool will default to.

Manually Tagging Clip Color Space

If necessary, you can manually identify the color space of one or more selected clips in the Media Pool

by right-clicking them and choosing the Input Color Space (and optionally the Input Gamma) from the

contextual menu.

Simple RCM Setup

When you first choose DaVinci YRGB Color Managed from the Color science drop-down menu of the

Color Management panel in the Project Settings, you’re presented with a simple pair of menus for

setting up how you want to work with Resolve Color Management: the “Resolve color management

preset,” and the “Output Color Space.”

Automatic Color Management

The first option when using RCM is to decide to use either Automatic Color Management or the

Manual Presets. When the Automatic Color Management box is checked, DaVinci Resolve presents

you with a simplified set of options for the most common use cases. For the Color Processing Mode,

you choose SDR or HDR, and based on the file types and codecs in the Media Pool, DaVinci Resolve

will automatically choose the appropriate input color space. Then, select from a list of common Output

color spaces for delivery. If you want specific control of these parameters, uncheck Automatic Color

Management box and select from the Color Management Presets below.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Automatic Color Management presets for fast, simple color management set up

Resolve Color Management Presets

The Resolve Color Management preset menu lets you choose how you want to use RCM to grade

your program. Each of these presets fully configures your project’s use of color management, and the

setting you select directly impacts how you’ll grade your program. Because of this, once you choose

a method of working and you grade every clip in your program, those grades rely on the preset you

used being selected in order to appear as they should.

Resolve Color Management presets for manual color management set up

When it comes to choosing a preset, a good way to think about which to use is to choose an SDR or

HDR preset that corresponds to the primary deliverable you plan on outputting. Both SDR and HDR

presets have several variations that you can choose among.

While these presets correlate to how you plan on outputting your program, they don’t lock you in,

since you can always change the Output Color Space (described below). This makes it possible to

export multiple versions of your program, each intended for different venues, no matter which color

management preset you’re using.

Whenever you choose a preset, a brief description explains the workflow that preset is intended to

facilitate. Here’s a list of the available presets, with slightly more detailed explanations.

�SDR Rec.709: (default) Sets up a Rec. 709 SDR grading environment. Your work can be converted

to HDR on output, if specified, but is limited to a Rec. 709 gamut with out-of-bounds colors

being clipped. Gamma 2.4 is not mentioned in the name because scene versus display OOTF is

managed automatically. Suitable for conventional streaming and broadcast.

�SDR P3 Broadcast: Sets up a P3-D65 SDR grading environment. Your work can be mapped

to HDR for output, if specified, but it is limited to a P3-D65 gamut with out-of-bounds colors

being clipped. Gamma 2.4 is not mentioned in the name because scene versus display OOTF is

managed automatically. Suitable for wider gamut streaming and broadcast at SDR levels.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

�SDR P3 Cinema: Sets up a P3-D60 SDR grading environment. Your work can be mapped to HDR

for output, if specified, but it is limited to a P3-D60 gamut with out-of-bounds colors being clipped.

Suitable for conventional Cinema projection.

�SDR Rec.2020: Sets up a Rec. 2020 SDR grading environment. Your work can be mapped to HDR

for output, if specified. Good for wide gamut streaming and broadcast.

�DaVinci Wide Gamut: Sets up an extra wide gamut grading environment that’s suitable for grading

either SDR or HDR. Capable of exporting with maximum image fidelity, preserving highlight details

of up to 10,000 nits. This is a log-encoded grading space for colorists wishing to work that way.

Suitable for creating mezzanine intermediates or final deliverables, or for grading HDR with high

nit levels.

�HDR P3 Broadcast: Sets up a P3-D65 HDR grading environment. Output gamut is limited to

P3‑D65, with out-of-bounds colors being clipped. Suitable for grading wide gamut SDR or HDR up

to 1000 nits.

�HDR Rec.2020: Sets up a Rec. 2020 HDR grading environment. Suitable for wide gamut SDR or

HDR deliverables up to 1000 nits.

�Custom: If none of the available presets suits how you need to work, you can choose Custom,

which exposes the full set of RCM settings for you to set up to suit your needs.

IMPORTANT: For all presets, importing media that’s in an identical or smaller gamut maps

the image data into the larger color space of the preset without transforming it. Importing

media with a wider gamut than the color space of the preset remaps the image data to fit into

the smaller color space, while preserving as much image detail as possible.

Output Color Space

For most DaVinci Resolve installations and projects, you’ll set your Output Color Space to match the

needs of your program, according to your display’s capabilities (or the capabilities your display is set to

use for the project at hand). You’ll also typically use a Resolve Color Management preset that matches

those capabilities.

However, RCM gives you the flexibility of grading in one color space and then outputting to others,

when necessary. For example, it’s easy to grade an SDR Rec. 709 version of a program for streaming

or broadcast, and then switch the Output Color Space to SDR P3 Cinema to output an additional

deliverable for theatrical exhibition.

To facilitate this, you can set the Output Color Space to any setting, independent of the Resolve Color

Management preset you’ve selected, and DaVinci Resolve will automatically convert from your Color

Management Preset to the Output Color Space of your choice. When you do so, here are the rules that

govern the resulting image transform.

When going SDR to HDR:

•	 0-50 nits (18% mid-gray) in your program is mapped to 0-50 nits on output (no change).

•	 Everything from 51-90 nits in your program is remapped from 51 to 100 nits (slightly

expanded).

•	 Everything from 91-100 nits in your program is remapped from 101 to 1000 nits

(greatly expanded).


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Original SDR grade seen within an HDR scale,

After an automatic SDR to HDR conversion

When going from HDR to SDR, the reverse is done:

•	 0-50 nits (18% mid-gray) in your program is mapped to 0-50 nits on output (no change).

•	 Everything from 51 to 100 nits in your program is remapped from 51-90 nits (slightly

compressed).

•	 Everything from 101 to 1000 nits in your program is remapped from 91-100 nits

(greatly compressed).


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

While these methods of converting between SDR and HDR provide an effective starting point for

conversion, they’re not meant to be an automatic solution. It’s critical that you do a trim pass whenever

outputting a deliverable in a new color space and EOTF, so you can check every clip and make

adjustments to improve the result when necessary.

NOTE: When converting SDR to HDR, this behavior may exaggerate noise in imported SDR

media that happens to have large flat expanses of bright colors. If you see particular clips that

show this issue, you can disable this behavior on a clip by clip basis in the Media Pool clip

contextual menu, or the Thumbnail Timeline contextual menu in the Color page, by toggling

“Inverse DRT for SDR to HDR Conversion.”