---
title: "Master Settings"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 27
---

# Master Settings

This panel is project specific and lets you set up and adjust the most essential properties of the

timelines in your project, including the timeline format, video monitoring method, and conform options.

In many workflows, you’ll want to adjust these settings before getting started with your project.

By default, all timelines use these project-wide settings. However, beginning with DaVinci Resolve

16, you can optionally create timelines with individual Format, Monitoring, and Output Sizing settings.

However, if you change a timeline to use “Basic Settings,” then that timeline will mirror the project-wide

options that are selected in the Project Settings.

Timeline Format

This group of settings affects the geometry and image processing of the current project.

�Timeline resolution: A drop-down menu that lets you choose a frame resolution preset to use

for image processing while grading. DaVinci Resolve is resolution independent, so you can

change the resolution at any time and all windows, tracks, sizing changes, and keyframe data will

be automatically recalculated to fit the new size. For example, you can work on a 4K project while

monitoring at HD resolutions if your room is only set up with an HD monitor, and then render the

finished project at 4K resolution for final delivery. Alternately, you can downsize an HD project to

an SD resolution to create another set of deliverables.

For more information on Resolve’s resolution independence, see Chapter 152, “Sizing and

Image Stabilization.””

�Frame size (Labeled “For X x Y processing”): Lets you set resolutions not found in the

“Timeline resolution” drop-down menu.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

�Use vertical resolution: This checkbox swaps the horizontal and vertical pixels of the Timeline

resolution. This lets you format your timeline vertically for display on smart phones, tablets, or

televisions that are in an upright configuration for digital signage.

�Pixel aspect ratio: Used to select PAR settings for image formats that don’t use the default

square pixel format. You can apply a 16:9 anamorphic PAR, a 4:3 PAR for SD projects, or a

Cinemascope ratio.

�Timeline frame rate: Determines the primary frame rate used by the project. A variety of standard

and high frame rate (HFR) settings are available. If you’re importing an AAF or XML file, this setting

is automatically set via an option in the Project Import dialog. Ideally, you should choose a frame

rate before importing media into the Media Pool. However, the first time you import media into an

empty Media Pool, you’re prompted if the incoming media frame rate doesn’t match the Timeline

frame rate set here, and you have the option of automatically updating this setting to match that

of the media you’re importing. Once one or more files have been added to the Media Pool, this

setting cannot be changed.

�Use drop frame timecode: Enables or disables drop frame timecode for the current project.

Off by default.

�Enable interlace processing: Interlaced media is supported throughout DaVinci Resolve. The

“Enable interlace processing” checkbox forces DaVinci Resolve to process all operations internally

using separated fields, in order to properly maintain the field integrity of interlaced clips in your

program. In addition, each clip in the Media Pool has a Field Dominance drop-down menu in the

Video panel of the Clip Attributes window that lets you specify whether clips are upper- or lower-

field dominant; an Auto setting makes this choice by default.

There is also a corresponding checkbox in the Render Settings panel of the Deliver page,

named “Field rendering,” that lets you enable and disable field rendering when you’re rendering

file‑based output.

There are two instances where you want to leave this setting turned off:

•	 If you’re working with progressive-frame media, it is not necessary to turn this checkbox

on. Doing so will unnecessarily increase processing time.

•	 If you’re using interlaced clips in a progressive-frame project and you’re intending to

deinterlace those clips using the Enable Deinterlacing checkbox in the Clip Attributes

window, then you must keep “Enable video field processing” off. Otherwise, the Enable

Deinterlacing checkbox will be disabled for all clips.

For more information about deinterlacing clips, see Chapter 22, “Modifying Clips and Clip

Attributes.”

If you’re working on a project with interlaced media that you intend to keep interlaced, then

whether or not it’s necessary to turn field processing on depends on what types of corrections

you’re applying to your clips. If you’re mastering your program to an interlaced format, and you’re

applying any adjustments that would cause pixels from one field to move or bleed into adjacent

fields, then field processing should be enabled; effects requiring field processing include filtering

operations such as blur, sharpen, and OpenFX operations, as well as sizing transforms that include

pan, tilt, zoom, rotate, pitch, and yaw.

On the other hand, regardless of whether you’re outputting interlaced or progressive-frame media,

if you’re not filtering or resizing your clips, and you’re only applying adjustments to color and

contrast, it’s not necessary to turn on field processing for interlaced material, and in fact, leaving it

off may somewhat shorten your project’s rendering time.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

�Align Clips to Frame Boundaries: When working with interlaced material, you can chose whether

to perform edits at the field or frame boundaries. When checked this means all editing actions

and playhead stepping will occur at full frame boundaries. This works independently of the audio

subframe controls, so it’s still possible to get perfect audio sync while working with video at the

frame level. When unchecked, all editing actions and playhead stepping will be performed at the

field boundary instead.

�Playback frame rate: Usually mirrors the frame rate selected in the “Video format” setting (in the

Video Monitoring section below), which is typically based on the frame rate of the external display

that’s connected to your video interface, given the “Timeline Frame Rate” setting. For example,

a 50Hz monitor requires a 25 fps playback frame rate for synchronous display without dropped

frames. If you want to monitor playback at a slower frame rate, type the frame rate of your choice

in this field and DaVinci Resolve will make the appropriate calculations to drop or repeat frames as

necessary to match it. This can be useful for temporarily seeing how clips look in slow motion.

Video Monitoring

The settings available in this group control the signal that’s output by the video output interface that’s

connected to your workstation, and let you specify what standard of signal is output, and via which

signal path.

By default the frame size and frame rate match those in the Timeline resolution and Playback frame

rate options. However, if necessary you can change these settings to match those of the external

display you’re using to monitor your work. For example, if you’re working with 2K files for 2K output,

but you’re color correcting using a high definition monitor set to 1080 resolution, you can select the

appropriate HD standard for that monitor without changing the Timeline Resolution settings.

�Video Resolution: Lets you choose a standard video frame size to be output via your connected

video output interface.

�Format: Lets you choose a standard video frame rate to be output via your connected video

output interface.

�Video connection checkboxes: Lets you choose the signal standard to output from your

connected video output interface to the video monitor. Make sure to choose a standard that’s

supported by both your video interface and your monitor.

The options are:

Use 1080PsF: Output progressive video in 1080i format for older HDTV sets.

Use 4:4:4 SDI: A signal path for monitoring image data to monitors that supports 4:4:4

chroma sampling, typically over SDI connections.

Use Level A for 3Gb SDI output: A signal path for monitoring image data via a

single 3 Gb/s SDI connection.

Use dual outputs on SDI output: All DaVinci Resolve systems can generate a side-by-side

display that can be sent to a Stereoscopic monitor via the HD-SDI output of an UltraStudio 4K

or DeckLink card. When dual SDI 3D monitoring is enabled, each eye is output separately at full

resolution. In this mode, split-screen wipes and cursors will not be visible on the grading monitor.

�SDI Configuration: Lets you choose from among Single Link, Dual Link, and Quad Link SDI,

depending on what your display supports.

�Data Levels: This setting only affects the data levels being output via the video interface that

connects the DaVinci Resolve workstation to your external display. It has no effect on the data

that’s processed internally by DaVinci Resolve, or on the files written when you render in the

Deliver page. It is imperative that the option you choose in DaVinci Resolve matches the data

range to which your external display is set. Otherwise, the video signal will appear to be incorrect,

even though the internal data is being processed accurately by DaVinci Resolve.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

There are two options:

Video: This is the correct option to use when using a broadcast display set to the

Rec. 709 video standard.

Full: If your monitor or projector is capable of displaying “full range” video signals, and you wish to

monitor the full 10-bit data range (0–1023) while you work, this is the correct option to use.

For more information about data levels, see Chapter 9, “Data Levels, Color

Management, and ACES.”

�Retain sub-black and super-white data: Turning this checkbox on lets DaVinci Resolve output the

undershoots (sub-black) and overshoots (super-white) within the headroom of video encoded data

levels to video. When this is turned off, these out-of-bounds values are clipped in video output.

�Video bit depth: Choose the bit depth that corresponds to the capability of your display. You can

choose between 8-bit and 10-bit. Monitoring in 10-bit is more processor intensive, but preferable

to avoid the appearance of banding that may not in fact be in the image data being processed by

DaVinci Resolve.

�Monitor scaling: Defaults to basic, and is only enabled to smooth the edges of video being viewed

on a projector with very large screens. These settings minimize high frequency artifacts that may

be seen. This may also be noticeable if you have a 2K or HD project but are monitoring on an SD

monitor. The other option, Bilinear, has different effects on the monitored image depending on

your display device, so you may need to check to verify that it’s appropriate for your environment.

�Use Rec601 Matrix for 4:2:2 SDI output: Don’t use this checkbox unless you know what it does.

You know who you are.

�Enable HDR metadata: (only available in Studio version) Turning on this checkbox outputs the

metadata necessary to send High Dynamic Range signals over HDMI 2.0a and have it be correctly

decoded by an HDR-aware video display. When this checkbox is enabled, it’s recommended to

also enable the “HDR mastering is for X nits” checkbox in the Color Management page, and set

the “nit” level (slang for cd/m2) to whatever peak luminance level your HDMI connected HDR

display is capable of.

Optimized Media and Render Cache

These settings govern the resolution and codec of optimized media that DaVinci Resolve can

generate in order to facilitate greater real time performance, as well as cached media that’s generated

by the Smart and User Cache.

�Proxy media resolution: A drop-down list lets you choose whether to generate proxy media

at each clip’s Original size, or at Half, Quarter, One-Eighth, or One-Sixteenth the resolution of

the original media, or allow DaVinci Resolve to choose this automatically for you based on your

timeline settings.

�Proxy media format: Specifies the format in which proxy media files will be written. You can

choose from among a variety of Uncompressed, ProRes, and DNxHD formats, depending on

your requirements.

�Optimized media resolution: A drop-down list lets you choose whether to generate optimized

media at each clip’s Original size, or at Half, Quarter, One-Eighth, or One-Sixteenth the resolution

of the original media, or allow DaVinci Resolve to choose this automatically for you based on your

timeline settings.

�Optimized media format: Specifies the format in which optimized media files will be written.

You can choose from among a variety of Uncompressed, ProRes, and DNxHD formats, depending

on your requirements.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

�Render cache format: Specifies the format in which render cache files will be written. You

can choose from among a variety of Uncompressed, ProRes, and DNxHD formats, depending

on your requirements.

�Enable background caching after X seconds: Specifies the duration of inactivity after which

automatic background caching will begin.

A series of checkboxes let you force specific types of effects to be cached when you use the

User Cache, which is a more selective manner of caching than the Smart Cache. These include:

Automatically cache transitions in user mode: If you’re using User mode and you find that your

workstation does not have adequate performance to play transition effects in real time, you can

force these categories of effects to be automatically included in the Sequence Cache and cached

when you’re using the User mode of caching.

Automatically cache composites in user mode: If you’re using User mode and you find that your

workstation does not have adequate performance to play composite mode or opacity effects in

real time, you can force these categories of effects to be automatically included in the Sequence

Cache and cached when you’re using the User mode of caching.

Automatically cache Fusion effects in user mode: If you’ve created effects for a clip in the Fusion

page and you find that your workstation does not have adequate performance to play that clip in

real time, you can force these categories of effects to be automatically included in the Sequence

Cache and cached when you’re using the User mode of caching.

Working Folders

These fields let you specify to which folders cache and gallery files are written.

�	Project media location: Lets you choose a specific folder on your system to hold all generated

media created for that project. Generated media includes things like new audio files created from

the Voiceover tool and Voice Convert, or essentially any type of new media created by DaVinci

Resolve itself. This allows you to make sure all the media for a project is in one common location,

making it easier to hand off, move or relink media, rather than have some media in DaVinci

Resolve’s internal file structure and some on a media drive. DaVinci Resolve will automatically

create new subfolders at your chosen media location based on media type, which makes it easy to

send some or all generated media to another location.

You can also set this location in the Create New Project dialog when creating a new project.

Inside the project media location,

DaVinci Resolve will create subfolders

automatically to organize any media

generated from within the program.

�Proxy generation location: All proxy media files that you create are saved in the directory path

specified by this field.

�Cache files location: All render cache files that you create are saved in the directory path

specified by this field. This path defaults to a hidden “CacheClip” directory that’s created at the

location of the first Media Storage Volume you specify in the DaVinci Resolve Preferences window.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

�Gallery stills location: By default, all stills you save are saved in the DPX format, and are placed

in the directory path specified by this field. This path defaults to a hidden “.gallery” directory

that’s created at the location of the first Media Storage Volume you specify in the DaVinci Resolve

Preferences window.

NOTE: If the volume you’ve selected to use for the cache becomes unavailable, DaVinci

Resolve will warn you with a dialog.