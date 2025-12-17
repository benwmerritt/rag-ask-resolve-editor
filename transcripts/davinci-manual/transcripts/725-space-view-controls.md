---
title: "Space View Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 725
---

# Space View Controls

The Space View offers the following control options, which, when used in conjunction with the track mute

and solo buttons offer very flexible options that let you focus on individual sources or groups of sources.

In the lower right corner of the workspace, you’ll find four buttons that let you view your sound sources

from different angles or perspectives.

You can freely rotate the workspace by holding down Command-Option-Shift while dragging it. If you

want to get back to a default view, click one of the perspective buttons.

Along the lower edge of the window, you’ll find the following checkboxes:

�Ambisonics Metering: This checkbox activates Ambisonics sonar-type metering when

working on Ambisonic mixes.

�Compact Meters: This option replaces the larger halo-style meters with smaller bar-graphs.

�Show Active Level Only: Clicking this option hides the names of silent sound sources.

�Show Beds: This option reveals the labels and meters for sound sources that are part of sound

beds instead of just the signals feeding your master Dolby Atmos bus.

The options in the dropdown menu to the right of the checkboxes determine which objects

appear in the virtual space:

�Show Only Selected: Shows sources based on tracks you’ve selected in the Mixer or timeline.

�Show Visible: Shows only the active audio sources for tracks that are not hidden.

�Show All: All sound sources are visible and labeled.


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

DELIVER

Deliver

CONTENTS

185	 Delivery Effects Processing���������������������������������������������������������������������������������������������������������������� 4019

186	 Using the Deliver Page������������������������������������������������������������������������������������������������������������������������ 4024

187	 Rendering Media������������������������������������������������������������������������������������������������������������������������������������ 4033

188	 Delivering DCP and IMF���������������������������������������������������������������������������������������������������������������������� 4067

189	 Delivering to Tape���������������������������������������������������������������������������������������������������������������������������������� 4082

190	 Exporting Timelines to Other Applications���������������������������������������������������������������������������������������������� 4090

Chapter 185

Delivery Effects

Processing

This chapter discusses how different video effects will be handled when you use

the controls of the Deliver page.

Contents

Delivery Effects Processing��������������������������������������������������������������������������������������������������������������������������������������������������������� 4020

When Rendering a Single Clip or When Outputting to Tape���������������������������������������������������������������������������������������� 4020

When Rendering Individual Source Clips for Round-Trip Workflows����������������������������������������������������������������������� 4020

More About Rendering Speed Effects������������������������������������������������������������������������������������������������������������������������������������� 4021

Determining the Rendered Output Resolution of Clips in Mixed Timelines���������������������������������������������������������� 4021

Rendering Edit and Input Sizing Adjustments��������������������������������������������������������������������������������������������������������������������� 4022

Rendering Mixed Frame Rate Timelines�������������������������������������������������������������������������������������������������������������������������������� 4022

Export Alpha Channels in Individual Clips Mode��������������������������������������������������������������������������������������������������������������� 4023

Export Alpha Channels in Single Clip Mode������������������������������������������������������������������������������������������������������������������������ 4023


Deliver | Chapter 185 Delivery Effects Processing

DELIVER

Delivery Effects Processing

For your final output, how effects are rendered depends on whether you’re rendering in Single Clip or

Individual Clips mode.

When Rendering a Single Clip or When Outputting to Tape

Whether you’re rendering a QuickTime or MXF master of your project as a single clip, rendering a DPX

image sequence for film output, or outputting directly to tape, all supported compositing, speed, and

transform effects are rendered by DaVinci Resolve and “baked” into the output media. Unsupported

effects are completely ignored, cannot be seen, and have no effect on media that’s rendered and output.

When Rendering Individual Source Clips

for Round-Trip Workflows

In workflows where you’re rendering individual media files to send a project back to an NLE or

finishing application for final finishing (adding titles and other effects before final delivery), DaVinci

Resolve handles different types of effects in different ways.

Unsupported effects do not appear in DaVinci Resolve. However, this effects data is internally

preserved, and when you export an XML or AAF file to send back to your NLE of choice, these effects

reappear, applied to the color corrected media that you rendered out of DaVinci Resolve and sent back.

Effects that DaVinci Resolve does support such as composite modes, opacity settings, speed effects,

and transitions are handled differently. Even though these effects are visible in DaVinci Resolve while

you work, they’re not “baked” into the final media that you render in preparation for sending back to

your NLE or finishing application. Instead, the portion of each media clip that’s used in your project is

rendered as an individual file, and the XML file that you export from DaVinci Resolve contains all of the

effects information necessary to reassemble the rendered media into a timeline that uses Final Cut Pro

effects applied to DaVinci Resolve-graded media.

EDL

FCP 7

FCP X

Premiere

Pro

Media

Composer*

Color Corrections

N/A

N/A

Rendered

N/A

N/A

Composite Modes

N/A

Sent Back

Sent Back

Sent Back

Rendered

Alpha Channels

N/A

Optionally

Rendered

Optionally

Rendered

Optionally

Rendered

Optionally

Rendered

Transitions

Sent Back

Sent Back

Sent Back

Sent Back

Sent Back

Opacity Settings

N/A

Sent Back

Sent Back

Sent Back

Sent Back

Position, Scale, Rotation

N/A

Conditional

Conditional

Conditional

Conditional

Linear Speed Effects

Sent Back

Sent Back

Sent Back

Sent Back

Sent Back

Variable Speed Effects

N/A

Sent Back

Sent Back

Sent Back

Sent Back

Long Duration Still Images

N/A

N/A

N/A

N/A

N/A

Freeze Frames

N/A

N/A

N/A

N/A

Rendered

* These effects are only sent back in AAF round trips when you’re updating an existing AAF file, rather than generating a new AAF file.

The chart shows which effects are rendered by DaVinci Resolve, and which

effects are passed back in different round trip workflows.


Deliver | Chapter 185 Delivery Effects Processing

DELIVER

After you’ve reimported your project back into your NLE or finishing application, you’re free to

readjust these effects while completing your program, without the need to re-render individual clips in

DaVinci Resolve.

IMPORTANT: One exception to the preservation of media and effects in round-trip

workflows is that nested sequences from Final Cut Pro 7 and Media Composer are not

compatible with DaVinci Resolve; XML and AAF files containing nested sequences cannot

be imported. On the other hand, Final Cut Pro X projects containing compound clips

can be imported.

More About Rendering Speed Effects

If you’re rendering a project with speed effects, you should be aware that DaVInci Resolve can

optionally render speed effects using Optical Flow processing, resulting in high-quality slow motion

and fast motion effects delivered straight out of DaVinci Resolve. If you’re satisfied with Optical Flow

processing in DaVinci Resolve, there may be no need for you to do a round-trip export if the main

reason you were doing so was to send the processing of slow motion clips to another application

for rendering, and rendering the Timeline in Single clip mode will “bake” the speed effects in using

whatever settings you’ve selected for the project, or for each clip if you’ve selected individual Retime

Process settings for different clips.

However, if you want to send unrendered speed effects to another application, rendering your project

in Individual source clips mode guarantees that the full range of each original clip of media will be

rendered, with the speed effect itself exported within the XML, AAF, or EDL file that’s exported.

NOTE: DaVinci Resolve adds three frame handles to clips with speed changes applied to

them, and to rendered clips that don’t match the project’s frame rate. This is done to facilitate

reconform in NLEs that require handles beyond the actual length of each of these clips.

Determining the Rendered Output

Resolution of Clips in Mixed Timelines

Ordinarily, rendering individual source clips results in each clip being rendered at either the project

resolution or the Resolution dropdown in the Render Settings (which overrides the project resolution),

with clips that don’t match the project resolution being resized or not according to the settings you’ve

chosen in the Image Scaling panel of the Project Settings.

However, if you’re rendering dailies for projects containing clips with mixed resolutions, you can

choose to render each clip at its original resolution by turning on the “Render at source resolution”

checkbox in the Video group of controls.


Deliver | Chapter 185 Delivery Effects Processing

DELIVER