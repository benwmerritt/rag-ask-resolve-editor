---
title: "Monitoring and Grading to ST.2084 in DaVinci Resolve"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 52
---

# Monitoring and Grading to ST.2084 in DaVinci Resolve

Monitoring an ST.2084 image is as simple as obtaining a ST.2084-compatible HDR display and

connecting it to the output of your DeckLink 8K, DeckLink 4K Extreme 12G, or UltraStudio 4K Extreme.

Setting up Resolve Color Management to grade for ST.2084 is identical to setting up to grade for

Dolby Vision. You’ll also monitor the video scopes identically, and output a master identically, given

that both standards rely upon the same PQ curve.

TIP: If you’re monitoring with the built-in video scopes in DaVInci Resolve, you can turn

on “HDR (ST.2084/HLG)” in the Waveform Scale Style settings in the Scopes option menu,

which will replace the 10-bit scale of the video scopes with a scale based on nit values

(cd/m2) instead.

Connecting to HDR-Capable Displays using HDMI 2.0a

If you have a DeckLink 4K Extreme 12G or an UltraStudio 4K Extreme video interface, then DaVinci

Resolve 12.5 and above can output the metadata necessary to correctly display HDR video signals to

display devices using HDMI 2.0a when you turn on the “Enable HDR metadata over HDMI” checkbox

in the Master Settings panel of the Project Settings.

The Enable HDR metadata over HDMI option in

the Master Settings panel of the Project Settings

lets you output HDR via HDMI 2.0a

When you do so, a setting in the Color Management panel of the Project Settings, “HDR mastering

is for X” lets you specify the output, in nits, to be inserted as metadata into the HDMI stream being

output, so that the display you’re connecting to correctly interprets it. The output you specify should

match what your display is expecting.

The “HDR mastering is for” setting lets you insert

metadata for HDR output via HDMI 2.0a


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

HDR10+™

DaVinci Resolve supports the new HDR10+ HDR format by Samsung. Please note that this support is

a work in progress as this is a new standard. When enabled, an HDR10+ palette shows the results of

the trimming analysis that make an automated downconversion of HDR to SDR, creating metadata to

control how HDR-strength highlights look on a variety of supported televisions and displays. This is

enabled and set up in the Color Management panel of the Project Settings with the Enable HDR10+

checkbox. Turning HDR10+ on enables the HDR 10+ palette in the Color page.

HDR 10+ settings in the Color Management panel of the Project Settings

Monitoring and Grading to ST.2084 for HDR10+

When you’re grading a program for HDR10+ output, you’ll need to monitor an ST.2084 image, which

is as simple as obtaining a ST.2084-compatible HDR display and connecting it to the output of your

DeckLink 8K, DeckLink 4K Extreme 12G, or UltraStudio 4K Extreme.

Setting up Resolve Color Management to grade for ST.2084 is identical to setting up to grade for

Dolby Vision or regular HDR10. You’ll also monitor the video scopes identically, and output a master

identically, given that each of these standards rely upon the same PQ curve.

TIP: If you’re monitoring with the built-in video scopes in DaVinci Resolve, you can turn

on “HDR (ST.2084/HLG)” in the Waveform Scale Style settings in the Scopes option menu,

which will replace the 10-bit scale of the video scopes with a scale based on nit values

(cd/m2) instead.

HDR10+ Grading Workflow

The idea behind the HDR10+ workflow is that you’ll grade the HDR version of each clip in your

program first, and then use the automatic analysis to create a downconverted tone mapped version

of each shot that’s controlled by metadata. Once the HDR10+ trim pass is complete, you’ll deliver the

rendered HDR output along with a set of HDR10+ JSON metadata files to a facility for final mastering.

Simultaneous Master and Target Display Output for HDR10+

When mastering HDR and trimming versions for more limited displays, it’s extremely useful to be able

to evaluate your HDR grade and tone mapped trim pass side by side. Starting in DaVinci Resolve 15,

it’s possible to output both the Master Display output and the Target Display output simultaneously

when you’re grading with either Dolby Vision or HDR10+ enabled.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

Necessary Hardware

To work in this manner, you must have the following equipment:

�Your DaVinci Resolve grading workstation must output via a DeckLink 8K, DeckLink 4K

Extreme 12G, UltraStudio 4K Extreme video interface, or better.

�Your Mastering Display must be capable of HDR nit levels suitable for the deliverable you’re

required to produce.

�An HDR target display that can be set to the appropriate tone mapped output.

Enabling Simultaneous Monitoring

When you set up your display hardware, the HDR Master Display must be connected to output A,

and the Target Display must be connected to output B of whichever BMD video output device you’re

using. Then, you need to turn on the “Use dual outputs on SDI” checkbox in the Master Settings of the

Project Settings. At this point, assuming all of your connections are compatible with one another, you

should see an HDR image output to your HDR display and a trimmed image output to your SDR display.

HDR10+ Auto Analysis Commands

After you’ve graded an HDR version of each clip in your program, a set of HDR10+ specific commands

let you auto-analyze each clip to create custom HDR to SDR downconversion metadata that give you

a starting point for the SDR trim pass you need to do. These commands are available in the Color >

HDR10+ submenu:

Analyze All Shots: Automatically analyzes each clip in the Timeline and

stores the results individually.

Analyze Selected Shot(s): Only analyzes selected shots in the Timeline.

Analyze Selected and Blend: Analyzed multiple selected shots and averages the result,

which is saved to each clip. Useful to save time when analyzing multiple clips that have

identical content.

Analyze Current Frame: A fast way to analyze clips where a single frame is

representative of the entire shot.

Delivering HDR10+

Once you’re finished grading the HDR and trimming the SDR downconversion, you need to output

your program correctly in the Deliver page.

Rendering an HDR10+ Master

To deliver an HDR10+ master after you’ve finished grading, you want make sure that the Output Color

Space of the Color Management panel of the Project Settings is set to the appropriate HDR ST.2084

setting based on the peak output you want to deliver (any values above will be clipped). Then, you

want to set your render up to use the highest quality Format/Codec combination that can be delivered

to whomever is doing the final mastering.

The HDR10+ analysis and manual trim metadata you generated while trimming is saved per clip,

in a series of JSON sidecar files, which should then be exported by right-clicking that timeline in the

Media Pool, and choosing Timelines > Export > HDR10+JSON.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

These two sets of files are then delivered to a facility that’s capable of creating an HDR10+ Mezzanine

File (this cannot be done in DaVinci Resolve).

NOTE: The HDR10+ mastering workflow is still a work in progress. More information will be

provided as it becomes available.

HDR Vivid

HDR Vivid is the HDR video technology standard released by the UHD World Association (UWA).

Mastering in this format assures wide compatibility with HDR televisions, phones, computers, and other

devices adhering to this standard.

HDR Vivid settings in the Color Management panel of the Project Settings

Monitoring and Grading to ST.2084 for HDR Vivid

When you’re grading a program for HD Vivid output, you’ll need to monitor an ST.2084 image, which

is as simple as obtaining a ST.2084-compatible HDR display and connecting it to the output of your

DeckLink 8K, DeckLink 4K Extreme 12G, or UltraStudio 4K Extreme.

Setting up Resolve Color Management to grade for ST.2084 is identical to setting up to grade for

Dolby Vision or regular HDR10. You’ll also monitor the video scopes identically, and output a master

identically, given that each of these standards rely upon the same PQ curve.

TIP: If you’re monitoring with the built-in video scopes in DaVinci Resolve, you can turn

on “HDR (ST.2084/HLG)” in the Waveform Scale Style settings in the Scopes option menu,

which will replace the 10-bit scale of the video scopes with a scale based on nit values

(cd/m2) instead.

HDR Vivid Grading Workflow

The idea behind the HDR Vivid workflow is that you’ll grade the HDR version of each clip in your

program first, and then use the automatic analysis to create a downconverted tone mapped version of

each shot that’s controlled by metadata. Once the HDR Vivid trim pass is complete, you’ll deliver the

rendered HDR output with embedded HDR Vivid metadata.

Simultaneous Master and Target Display Output for HDR Vivid

When mastering HDR and trimming versions for more limited displays, it’s extremely useful to be able

to evaluate your HDR grade and tone mapped trim pass side by side. Starting in DaVinci Resolve 15,

it’s possible to output both the Master Display output and the Target Display output simultaneously

when you’re grading with HDR Vivid enabled.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

Necessary Hardware

To work in this manner, you must have the following equipment:

�Your DaVinci Resolve grading workstation must output via a DeckLink 8K, DeckLink 4K Extreme

12G, UltraStudio 4K Extreme video interface, or better.

�Your Mastering Display must be capable of HDR nit levels suitable for the deliverable you’re

required to produce.

�An HDR target display that can be set to the appropriate tone mapped output.

Enabling Simultaneous Monitoring

When you set up your display hardware, the HDR Master Display must be connected to output A,

and the Target Display must be connected to output B of whichever BMD video output device you’re

using. Then, you need to turn on the “Use dual outputs on SDI” checkbox in the Master Settings of

the Project Settings. At this point, assuming all of your connections are compatible with one another,

you should see an HDR image output to your HDR display and a trimmed image output to your

SDR display.

HDR Vivid Trim Controls in DaVinci Resolve

The latest version of the HDR Vivid palette exposes three sets of controls. The first are the

main controls:

�Target Display Output: This drop-down specifies what parameters are used to display the

tone mapped image. This menu lets you choose specific display properties to obtain a preview

of what the trimmed image will look like on different displays with different gamuts and peak

luminance capabilities.

�Trim Mode: Determines the toolset used to create the trims, either Curve or Statistical modes.

�Analyze controls: The commands governing HDR Vivid auto-analysis are available as buttons,

which perform the same functions as their similarly named counterparts in the Color > HDR Vivid

submenu. Please note that most trim controls are disabled until you perform an analysis, which is a

necessary first step.

All: Automatically analyzes each clip in the current Timeline and stores the results individually.

Selected: Only analyzes selected shots in the Timeline.

Frame: Useful in situations where part of a clip has an extreme level of color or lightness that’s

not typical of the rest of the clip, that incorrectly biases the analysis and produces a poor result.

Placing the playhead on a frame that’s representative of how the clip is supposed to look, and

using the Frame option, bases the analysis on only that frame. This is also a fast way to analyze

clips where a single frame is representative of the entire shot.

�Enable Tone Mapping Preview: Lets you see the target display output in the Color page Viewer

and video output, so you can evaluate how the tone mapped version looks on your HDR display.

�The next set of controls activate based on which Trim Mode you have selected.

�Curve: The Curve trim mode exposes a variety of controls that lets the colorist adjust the trim

metadata manually at the clip or frame level. Offset, Brightness, and Detail settings are available

for the Dark and Bright parts of the curve. Midtones have a brightness control. Highlight Crop

lets you bring any highlights back into range that may have exceeded the display’s maximum

brightness, thus blowing out. Separate Global and Highlight saturation settings are also possible.

�Statistical: The Statistical trim mode exposes controls that let you fine tune the automatic tone

mapping algorithm used in the Analyze step.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

HDR Vivid controls in the Color page