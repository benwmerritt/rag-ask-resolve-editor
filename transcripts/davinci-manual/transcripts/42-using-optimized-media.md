---
title: "Using Optimized Media,"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 42
---

# Using Optimized Media,

Proxy Media, and Caching Together

How you use DaVinci Resolve’s various performance-enhancing features together is entirely up to you,

but you should know that they’re not an either/or proposition. For example, you can create optimized

media from the camera raw original clips in your project, then enable Timeline Proxy Mode playback

to enhance the performance of your 4K timeline, and turn on Smart Cache to speed up your work in

the Color page as you add Fusion effects, noise reduction, and Resolve FX or OFX to every clip. All of

these optimization methods work happily and seamlessly together to improve your performance while

keeping the image quality of your project as high as the Optimized, Proxy, and Cache formats you’ve

selected in the Master Settings panel of the Project Settings.

Which Playback Optimization

Method Should I Use?

DaVinci Resolve’s various playback optimization features are designed to specifically increase

performance to make up for hardware, storage, and bandwidth deficiencies, but knowing when to use

each method is essential to proper functionality. Included below is a quick reference.

�Timeline Proxy Mode: My timeline is playing back, just a little bit too slowly.

�Cache Clip: I need help playing back a few clips in real time that have heavy effects applied.

�Optimized Media: I need help playing back all my source media in real time, and I will only be

editing on this computer.

�Proxy Media: I need help playing back all my source media in real time, and I need to collaborate

and share this media with other users, programs, or outside storage locations.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Other Project Settings

That Improve Performance

In addition to working with proxies, using reduced raw decoding quality, generating optimized media,

and enabling the Smart and User caches, there are five additional options in the Project Settings

window and one setting in the UI Settings panel of the User Preferences that you can use to further

improve real time performance if you’re working on an underpowered computer, at the expense of

lower image quality while you work. These settings can then be changed back to higher quality modes

prior to rendering.

�Set timeline resolution to: (Master Project Settings, Timeline Format) DaVinci Resolve is resolution

independent, so you can change the resolution at any time and all windows, tracks, sizing

changes, and keyframe data will be automatically recalculated to fit the new size. Lowering the

Timeline resolution while you’re grading will improve real time performance by reducing the

amount of data being processed, but you’ll want to increase Timeline resolution to the desired size

prior to rendering. This is effectively the same as using the Proxy command, but you get to choose

exactly what resolution you want to work at.

�Enable video field processing: (Master Project Settings, Timeline Format) You can leave this

option turned off even if you’re working on interlaced material to improve real time performance.

When you’re finished, you can turn this setting back on prior to rendering. However, whether or

not it’s necessary to turn field processing on depends on what kinds of corrections you’re making.

If you’re applying any filtering or sizing operations such as blur, sharpen, pan, tilt, zoom, or rotate,

then field processing should be on for rendering. If you’re only applying adjustments to color and

contrast, field processing is not necessary.

�Video bit depth: (Master Project Settings, Video Monitoring) Monitoring at 8-bit improves real time

performance, at the expense of possibly introducing banding to the monitored image.

�Monitor scaling: (Master Project Settings, Video Monitoring) Lets you choose which transform

filter to use when scaling video to fit into the Video format resolution you’ve specified. Options are

Bilinear and Basic.

�Resize Filter: (Image Scaling) A drop-down menu that lets you choose an alternate image

transform filter (such as Bilinear) that is lower quality but less processor intensive. A “Force sizing

highest quality” checkbox in the Render Settings list of the Deliver page helps make sure you

don’t accidentally render your final media at this lower quality setting, however.

�Hide UI overlays: (User Preferences, Playback Settings) Off by default. When using a single GPU

for both display and CUDA or OpenCL processing, or if your display GPU is underpowered, or

if you lack the PCIe bandwidth required for the currently specified resolution or frame rate, you

may be able to improve real time performance by turning this option on. When enabled, onscreen

controls such as the cursor, Power Window outlines, and split-screen views are disabled and

hidden during playback. When playback is paused, all onscreen controls reappear.

�Minimize interface updates during playback: (User Preferences, Playback Settings) On by default.

While enabled, this setting improves real time performance by hiding on-screen controls that

appear in the Viewer, such as the cursor, Power Window outlines, and split-screen views during

playback. When playback is stopped, onscreen controls reappear.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Chapter 9

Data Levels,

Color Management,

and ACES

This chapter covers operational details that affect how color is managed for media

that is imported into and exported from DaVinci Resolve. If color accuracy is

important to you, then it’s a good idea to learn more about how Resolve handles

the data levels of each clip, how DaVinci Resolve Color Management helps you to

work with different formats, and how to use ACES.

Contents

Data Levels Settings and Conversions������������������������������������������������������������������������������������������������������������������������������������� 220

Converting Between Ranges and Clipping������������������������������������������������������������������������������������������������������������������������������� 221

Internal Image Processing and Clip Data Levels�������������������������������������������������������������������������������������������������������������������� 221

Assigning Clip Levels in the Media Pool����������������������������������������������������������������������������������������������������������������������������������� 222

Video Monitoring Data Levels�������������������������������������������������������������������������������������������������������������������������������������������������������� 222

Deck Capture and Playback Data Level������������������������������������������������������������������������������������������������������������������������������������ 223

Output Data Level Settings in the Deliver Page�������������������������������������������������������������������������������������������������������������������� 224

So, What’s the “Proper” Data Range for Output?������������������������������������������������������������������������������������������������������������������ 224

Introduction to DaVinci Resolve Color Management�������������������������������������������������������������������������������������������������������� 224

Display Referred vs. Scene Referred Color Management������������������������������������������������������������������������������������������������ 225

Updated RCM In DaVinci Resolve 17������������������������������������������������������������������������������������������������������������������������������������������� 225

Resolve Color Management for Editors������������������������������������������������������������������������������������������������������������������������������������� 226

The Input, Timeline, and Output Color Space������������������������������������������������������������������������������������������������������������������������ 226

The RCM Image Processing Pipeline������������������������������������������������������������������������������������������������������������������������������������������ 228

Identifying the Input Color Space of Different Clips������������������������������������������������������������������������������������������������������������ 228

Simple RCM Setup������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 230

Automatic Color Management������������������������������������������������������������������������������������������������������������������������������������������������������� 230

Resolve Color Management Presets�������������������������������������������������������������������������������������������������������������������������������������������� 231

Output Color Space����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 232


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Advanced RCM Setup������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 234

Single Setting vs. Dual Setting RCM������������������������������������������������������������������������������������������������������������������������������������������� 234

Setting the Input Color Space�������������������������������������������������������������������������������������������������������������������������������������������������������� 235

Choosing a Timeline Color Space������������������������������������������������������������������������������������������������������������������������������������������������ 236

Timeline Working Luminance���������������������������������������������������������������������������������������������������������������������������������������������������������� 238

203 Nit Support for SDR to HDR��������������������������������������������������������������������������������������������������������������������������������������������������� 238

Gamut Limiting, Restricting Values Within a Larger Gamut��������������������������������������������������������������������������������������������� 239

Input DRT Tone Mapping������������������������������������������������������������������������������������������������������������������������������������������������������������������ 239

Output DRT Tone Mapping�������������������������������������������������������������������������������������������������������������������������������������������������������������� 240

Use Inverse DRT for SDR to HDR Conversion������������������������������������������������������������������������������������������������������������������������ 242

Use White Point Adaptation������������������������������������������������������������������������������������������������������������������������������������������������������������� 242

Color Space Aware Grading Tools����������������������������������������������������������������������������������������������������������������������������������������������� 243

Apply Resize Transformations In��������������������������������������������������������������������������������������������������������������������������������������������������� 243

Graphics White Level�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 243

Display HDR On Viewers If Available������������������������������������������������������������������������������������������������������������������������������������������ 244

HDR Mastering Is For (Studio Version Only)����������������������������������������������������������������������������������������������������������������������������� 244

Resolve Color Management and the Fusion Page��������������������������������������������������������������������������������������������������������������� 244

Ability to Bypass Color Management Per Clip����������������������������������������������������������������������������������������������������������������������� 245

Exporting Color Space Information to QuickTime Files����������������������������������������������������������������������������������������������������� 245

Color Management Using ACES�������������������������������������������������������������������������������������������������������������������������������������������������� 246

Setting Up ACES in the Project Settings Window����������������������������������������������������������������������������������������������������������������� 247

ACES AMF 2.0���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 250

The Timeline Color Space in ACES Workflows is Fixed����������������������������������������������������������������������������������������������������� 252

Tips for Rendering Out of an ACES Project����������������������������������������������������������������������������������������������������������������������������� 252

Data Levels Settings and Conversions

Different media formats use different ranges of values to represent image data. Since these data

formats often correspond to different output workflows (cinema vs. broadcast), it helps to know where

your project’s media files are coming from, and where they’re going, in order to define the various data

range settings in DaVinci Resolve and preserve your program’s data integrity.

To generalize, with 10-bit image values (with a numeric range of 0–1023), there are two different data

levels (or ranges) that can be used to store image data when writing to media file formats such as

QuickTime, MXF, or DPX. These ranges are:

•	 Video: Typically used by Y’CBCR video data. All image data from 0 to 100 percent must fit

into the numeric range of 64–940. Specifically, the Y’ component’s range is 64–940, while

the numeric range of the CB and CR components is 64–960. The lower range of 4–63 is

reserved for “blacker-than-black,” and the higher ranges of 941/961–1019 are reserved for

“super-white.” These “out of bounds” ranges are recorded in source media as undershoots

and overshoots, but they’re not acceptable for broadcast output.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

•	 Full: Typical for RGB 444 data acquired from digital cinema cameras, or film scanned to DPX

image sequences. All image data from 0 to 100 percent is simply fit into the full numeric

range of 4 to 1023.

Keep in mind that every digital image, no matter what its format, has absolute minimum and

maximum levels, referred to in this section as 0–100 percent. Whenever media using one data

range is converted into another data range, each color component’s minimum and maximum

data levels are remapped so that the old minimum value is scaled to the new data level

minimum, and the old maximum value is scaled to the new data level maximum;

•	 (minimum Video Level) 64 = 4 (Data Level minimum)

•	 (maximum Video Level) 940 or 960 = 1023 (Data Level maximum)

Converting Between Ranges and Clipping

Simply converting an image from one data range to another should result in a seamless change. All

“legal” data from 0–100 percent is always preserved and is linearly scaled from the previous data

range to fit into the new data range.

The exceptions to this are undershoots and overshoots that you’ve deliberately set, also referred to

as out-of-bounds levels. The overshoots and undershoots that are allowable in “Video Levels” media

(known as sub-black or super-black and super-white) are usually clipped when converted to full-range

“Full Levels.” However, DaVinci Resolve preserves this data internally, and these clipped pixels of

detail in the undershoots and overshoots are still retrievable by making suitable adjustments in the

Color page to bring them back into the “legal” range.

The out-of-bounds image data that’s preserved within the headroom of Video Levels by DaVinci

Resolve while working is usually clipped, however, when you either output to video or render your

output. There are two settings that let you get around this for instances where you want to preserve

these levels:

A checkbox in the Video Monitoring group of the Master settings, “Retain sub-black and

super-white data,” lets DaVinci Resolve output undershoots (sub-black) and overshoots

(super-white) to video when Data Level is set to Video. When this is turned off, these out-of-

bounds values are clipped on output.

A checkbox in the Advanced settings of the Render settings in the Deliver page, “Retain

sub-black and super-white data,” lets DaVinci Resolve render undershoots (sub-black) and

overshoots (super-white) to exported media when Data Level is set to Video.

Internal Image Processing and Clip Data Levels

It’s useful to know that, internally to DaVinci Resolve, all image data is processed as full range,

uncompressed, 32-bit floating point data. What this means is that each clip in the Media Pool,

whatever its original bit-depth or data range, is scaled into full-range 32-bit data. How each clip is

scaled depends on its Levels setting in the Clip Attributes window, available from the Media Pool

contextual menu.

Selecting Auto, Video,

or Full levels


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

By converting all clips to uncompressed, full-range, 32-bit floating point data, Resolve guarantees the

highest quality image processing that’s possible. As always, the quality of your output is dependent

on the quality of the source media you’re using, but you can be sure that Resolve is preserving all the

data that was present in the original media.