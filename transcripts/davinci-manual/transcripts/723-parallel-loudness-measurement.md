---
title: "Parallel Loudness Measurement"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 723
---

# Parallel Loudness Measurement

A parallel 5.1 down-mix can be performed during the render as a source for a 5.1 loudness

measurement. Certain delivery specifications (such as for Netflix) require that the loudness

measurement of Atmos Masters be performed at 5.1. You can enable this parallel 5.1 (or stereo) render

for the loudness measurement and monitor in the room’s native format.

Selecting a Downmix option

Low-latency Rendering

Previous versions of the Dolby Atmos Renderer were able to run at a specific latency of 10.67 ms.

This restriction has been removed, allowing selection of lower latency engine processing block sizes,

and thus lower monitoring latency through the Dolby Atmos renderer. However, the larger block size

is enforced by the renderer during certain operations, such as Binaural renderer, or when a parallel

loudness down-mix is enabled.

Surround Buses in Fairlight (Studio Version Only)

The FlexBus structure in Fairlight enables user-definable buses. Atmos mixes call for several bus

formats that are available in DaVinci Resolve 17 and later.

�9.1.6

�22.2

Object-Based Format Support (Studio Version Only)

�Dolby Atmos with support for 7.1.2 and 7.1.4

�MPEG-H with support for 5.1.4, 7.1.4, and 7.2.3

�SMPTE ST.2098 with support for 9.1 OH, 9.1 HT, 11.1 HT, 13.1 HT, and 15.1 HT

Auro-3D Support (Studio Version Only)

�Auro-3D with support for 9.1, 10.1, 11.1 (7+4), 13.1


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

Dolby Atmos Configuration Controls

The Video and Audio I/O panel of the Resolve System Preferences lets you enable and configure

the use of a Dolby RMU for doing Dolby Atmos mixing. You can enter the IP address of the RMU, and

choose the base audio output.

Configuring Dolby Atmos in the Resolve System Preferences

Atmos Re-Renders

In order to provide parity with the external renderer, you can create presets that let you define a

PCM output format and a set of sources using the bed, object, and group definitions (such as 5.1).

Bounce Mix to Track accommodate these re-render presets in Dolby Atmos timelines, allowing

you to generate multiple deliverables in a single pass. These render presets are stored and

recalled as part of the timeline.

Bounce Mix to Track Dolby Atmos re-render options

In addition to render format, you can select the source from a combination of beds, objects, or

defined VCA groups.

Dolby Atmos Render Preset options


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

MPEG-H Authoring

DaVinci Resolve enables MPEG-H authoring. This includes Native MPEG-H track and bus formats

and monitoring, including the ability to define basic track-level meta-data for export into an MPEG- H

scene, and export of a MPEG-H Master file. Once enabled, the formats become available for selection

as a bus, track, or monitoring format, in the Bus Format window.

The MPEG-H format options in the Bus Format window

These formats also become available for multi-channel track assignment.


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

The MPEG-H format options in the Track Format submenu

Tracks are mixed natively in a similar manner to most immersive content, with the creation of a bed mix

consisting of a set of immersive object tracks that use dynamic panning. These are combined onto the

main bus to form the immersive mix.

Track Configuration

In addition to this process, once the format is enabled, a set of MPEG-H meta-data columns become

enabled in the DaVinci Resolve Track index, including Track Type, Kind, Language, SW Group,

and Preset.

For more information about these columns and how to configure them, see Chapter 170,

“Using the Fairlight Page.”

When MPEG-H is enabled in the Project Settings, the Tracks panel shows additional

columns of information for defining each track in the Timeline


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

Export

Once everything is configured, and your project is mixed, you export a master file. In order to do this,

you must select a range In and Out point on the Timeline to define an export range. Additionally, you

must define whichever busses are designated for rendering by defining their Kind, and you can select

tracks you want to export additionally.

Selecting tracks and busses to export

NOTE: An MPEG-H master file can only contain a maximum of fifteen channels total.

If the selected track and bus stems exceeds this, then the export will fail, issuing a warning.

The same will occur if a range is not selected.

To export an MPEG-H mix:


Choose Fairlight > Immersive Audio > Generate MPEG-H Audio File.


Choose a save location and name, and click Save.

At this point, all defined buses are rendered. Then, track loudness is measured for compliance. Lastly,

the source audio is exported and the metadata embedded into the deliverable MPEG-H wav file.

There are several error conditions, which are deleted during the export process, that will all cause the

export to fail. For example, all tracks must contain audio. Audio within switch groups must be within a

specific loudness tolerance of one another. If any of these conditions occur, a dialog will appear.

Warning dialog during MPEG-H export


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT