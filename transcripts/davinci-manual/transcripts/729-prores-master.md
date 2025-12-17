---
title: "ProRes Master"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 729
---

# ProRes Master

For quickly outputting ProRes Master files of a whole program. When selected, defaults to rendering in

single clip mode, with the Format set to QuickTime, the Codec set to Apple ProRes, and the Type set

to Apple ProRes 422 HQ. Audio defaults to the Codec being Linear PCM and the Bit Depth being 16.

H.264 Master

For outputting H.264 files of a whole program. When selected, defaults to rendering in single clip

mode, with the Format set to QuickTime, and the Codec set to H.264. Quality, Encoding Profile, and

Entropy Mode are set to Auto, Passes defaults to Single, and Key Frames default to Automatic with

Frame Reordering turned on. Audio defaults to the Codec being AAC with the Data Rate set to 320

Kb/s and the Bit Depth set to 16.


Deliver | Chapter 187 Rendering Media

DELIVER

H.265 Master

For outputting H.265 files of a whole program. When selected, defaults to rendering in single clip

mode, with the Format set to QuickTime, and the Codec set to H.265. Quality is set to Automatic,

Encoding Profile is set to Main, Passes defaults to Single, and Key Frames default to Automatic with

Frame Reordering turned on. Audio defaults to the Codec being AAC with the Data Rate set to 320

Kb/s and the Bit Depth set to 16.

IMF (Studio Version Only)

A dropdown menu to the right of this preset provides options for Generic, 20th Century Fox, and

Netflix-qualified presets. This preset is for facilities that deliver IMF files as digital-only deliverables.

A Preset Type dropdown lets you choose the appropriate settings to populate the various locked IMF-

specific parameters that appear.

Frame.io

A Frame.io preset at the top of the Deliver page’s Render Settings panel lets you render and upload a

program for review. All options in the Render Settings panel update to present suitable controls for this

process. At the bottom of the Render Settings list, an “Upload directly to Frame.io” checkbox lets you

choose whether or not to upload the rendered result. A Description field lets you add a description to

be uploaded along with the rendered media.

Choosing the Frame.io preset

When you choose the Frame.io preset, the Location field turns into a Frame.io field, and the

Browse button lets you choose a project and folder path to which to upload the exported result.


Deliver | Chapter 187 Rendering Media

DELIVER

Choosing a Frame.io account to deliver a program to

When you export to Frame.io, the available choices in the Resolution, Format, Video Codec, and

Type dropdown menus are limited to those that are most suitable for Frame.io file sharing. Choose

the desired export options, then click the Add to Render Queue button to add this job to the Render

Queue as you would with any other export. When that job is rendered, it automatically proceeds

to upload to Frame.io, and an upload percentage indicator appears in the job listing to show how

far along this upload is. This upload is done in the background, so you can continue working on

other things in DaVinci Resolve while the file uploads. If you want to see how long the upload will

take on any other page, you can choose Workspace > Background Activity to see the Background

Activity window.

For more information about Frame.io integration, see Chapter 13, “Frame.io and Dropbox

Replay Integration.”

Final Cut Pro 7 or X XML

A dropdown menu attached to this preset lets you choose from two different XML formats to be

exported along with the media you’re rendering:

�Selects the appropriate settings for projects that were sent from Final Cut Pro 7 to DaVinci Resolve

using XML. This is meant for situations when you’re rendering media intended for a return trip to

Final Cut Pro (by exporting an XML file from the Edit page). Renders Individual Clips, the “Codec”

setting on macOS, defaults to Apple ProRes 422 (HQ), Output Size defaults to the current Timeline

Resolution (as set in the Master Settings panel of the Project Settings), and Use Unique Filenames

is turned on.

When you choose this preset, an XML of the timeline is automatically exported along with the

media, with path names that reflect the rendered clips.


Deliver | Chapter 187 Rendering Media

DELIVER

�Selects the appropriate settings for projects that were sent from Final Cut Pro X to DaVinci

Resolve using XML. This is meant for situations when you’re rendering media intended for a return

trip to Final Cut Pro X (by exporting an FCPXML file from the Edit page). Renders Individual Clips,

the “Codec” setting on macOS, defaults to Apple ProRes 422 (HQ), Output Size defaults to the

current Timeline Resolution (as set in the Master Settings panel of the Project Settings), and Use

Unique Filenames is turned on.

When you choose this preset, an XML of the timeline is automatically exported along with the

media, with path names that reflect the rendered clips.

Premiere XML

Selects the appropriate settings for projects that were sent from Premiere Pro to DaVinci Resolve

using XML. This is meant for situations when you’re rendering media intended for a return trip to

Premiere Pro. Renders Individual Clips, the “Codec” setting on macOS defaults to Apple ProRes 422

(HQ), Output Size defaults to the current Timeline Resolution (as set in the Master Settings panel of the

Project Settings), and Use Unique Filenames is turned on.

When you choose this preset, an XML of the rendered timeline is automatically exported along with

the media, with path names that reflect the rendered clips.

Avid AAF

Selects the appropriate settings for projects that were sent from Avid Media Composer or Symphony

to DaVinci Resolve using AAF. This setting is NOT for exporting to Pro Tools. This is meant for

situations when you’re rendering media intended for a return trip to Media Composer (by exporting an

AAF file from the Edit page). The “Codec” setting defaults to DNxHR 444 12 bit, Output Size defaults

to the current Timeline Resolution (as set in the Master Settings panel of the Project Settings), and

Render Clip with Unique Filename is turned on.

When you choose this preset, an AAF of the timeline is automatically exported along with the media,

with path names that reflect the rendered clips.

Pro Tools

As of DaVinci Resolve version 16, Pro Tools export has been dramatically improved. This preset

presents the appropriate options for exporting a specifically formatted AAF project file, linked audio

files, and a linked reference video file to Pro Tools, or any application capable of importing a Pro Tools

formatted AAF file.

When exporting using the Pro Tools preset, you must use the AAF file that’s automatically created and

written to the target location, because it’s formatted specially for Pro Tools and it contains path names

reflecting the rendered clips. Do not export an AAF using the File > Export AAF/XML command, as this

will not provide the correct exchange file for Pro Tools, and it won’t work correctly.

When you use the Pro Tools preset, DaVinci Resolve outputs the following:


What you choose in the Codec dropdown menu of the Audio panel dictates whether you export

the audio from the Timeline as a collection of files that link to a separate AAF, or an AAF with

audio file embedded within as a single deliverable.

�Choose Linear PCM to export individual files linked to a separate AAF interchange file

�Choose Embedded in AAF to export an AAF with embedded Broadcast WAV audio files within it

as a single deliverable

Whether you export separate files or a single embedded AAF deliverable, each of the audio

clips in the current Timeline can be exported as individual mono or multichannel audio files.

The standard mono round trip export from DaVinci Resolve to Pro Tools is the default setting, with


Deliver | Chapter 187 Rendering Media

DELIVER

the “Render one track per channel” box checked in the Audio tab of the Pro Tools Render Setting.

With this option, a 5.1 polyphonic .wav file would be exported as six individual mono .wav files.

If the “Render one track per channel” box is unchecked, DaVinci Resolve will output multichannel

polyphonic .wav files instead. If you do this, it’s important to check in advance that Pro

Tools supports the particular multi-channel formats you want to export before committing to

this workflow.

Each exported file contains every audio channel from the source media, regardless of channels

that have been been muted in the audio panel of Clip Attributes. This means no matter how the

video editor organized the channels of audio in the Timeline, you’ll always deliver every channel of

each audio clip to whomever is doing your audio postproduction.


You can also choose to include handles using the “Add X frame handles” option in the Advanced

Settings of the Video panel to add extra frames to the beginning and end of each exported audio

clip. This will provide needed editing flexibility to whomever is refining your audio.


The type of audio file that’s exported is determined by your choice of video format in the

Video panel:

�If you choose the MXF OP-Atom video format, then MXF audio files will be exported.

�If you choose the QuickTime format, then Broadcast Wave files will be exported.


All video in your timeline will be rendered and output as a single reference movie, in the format

that’s selected in the Video panel, with all effects and titles baked in. Subtitles can also be burned

into the reference movie or exported as a file. If you want to provide a window burn, you can

enable visible metadata using the Workspace > Data Burn-In window. If you do not wish to export

a reference movie, you can uncheck the Export Video box in the Video panel.

When you output using the Pro Tools preset, an AAF of the audio tracks of the current

Timeline is exported that’s formatted for import into Pro Tools, or any other digital audio

workstation (DAW) software that’s compatible with the Pro Tools style of AAF import.

•	 Exported audio files have the file name and timecode of the source media they were

extracted from, to enable relinking to the source media in Pro Tools, if necessary. In the case

of Video+Audio files that have been synced in DaVinci Resolve, exported audio files are

given the timecode and name of the synced audio source file, not that of the video clip.

•	 Each audio track exports whatever custom name you may have given it, for use by Pro Tools.

•	 All track and clip volume automation is exported, with all keyframes.

•	 iXML metadata is also exported, including channel names when available.

IMPORTANT: When you export to Pro Tools in the Deliver page, audio effects are neither

exported nor baked in, which means that FairlightFX, EQ, Compression, Pitch, and Elastic

Wave effects will be ignored. If you are experiencing problems with imported AAF files, check

to see if there are audio effects or audio compound clips in the Timeline, and replace any you

find with duplicates of the same audio clips that have no effects.


Deliver | Chapter 187 Rendering Media

DELIVER