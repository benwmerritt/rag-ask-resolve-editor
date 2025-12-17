---
title: "Chapter 8"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 37
---

# Chapter 8

Improving

Performance,

Proxies, and

the Render Cache

DaVinci Resolve is a high-performance piece of software designed to enable

real time effects on a variety of workstations.

This section describes the various ways you can monitor your performance to make sure you’re

maintaining real time playback, along with different methods of optimizing real time performance,

including using on-the-fly proxies and the background Render Cache.

Contents

Understanding the GPU Status Display������������������������������������������������������������������������������������������������������������������������������������ 193

Prioritizing Audio or Video Playback in the Edit Page������������������������������������������������������������������������������������������������������� 193

Performance Mode Improves Overall Performance����������������������������������������������������������������������������������������������������������� 194

Adjusting Performance Mode���������������������������������������������������������������������������������������������������������������������������������������������������������� 194

Timeline Proxy Mode Improves Effects Performance�������������������������������������������������������������������������������������������������������� 194

Reducing Decode Quality Improves Raw Media Performance������������������������������������������������������������������������������������� 195

Optimized Media Improves Overall Performance���������������������������������������������������������������������������������������������������������������� 196

Creating Optimized Media���������������������������������������������������������������������������������������������������������������������������������������������������������������� 196

Optimized Media for Raw Source Clips��������������������������������������������������������������������������������������������������������������������������������������� 197

Customizing the Type of Optimized Media You Create������������������������������������������������������������������������������������������������������ 197

Switching Between Optimized and Original Media�������������������������������������������������������������������������������������������������������������� 198

Sharing Optimized Media Between Projects��������������������������������������������������������������������������������������������������������������������������� 199

Rediscovering Lost Optimized Media������������������������������������������������������������������������������������������������������������������������������������������ 199

Deleting Optimized Media����������������������������������������������������������������������������������������������������������������������������������������������������������������� 199

Using Optimized Media for Delivery�������������������������������������������������������������������������������������������������������������������������������������������� 199


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Using the Smart or User Cache Improves Effects Performance���������������������������������������������������������������������������������� 199

How Cached Media Is Organized������������������������������������������������������������������������������������������������������������������������������������������������� 200

Choosing a Cache Format and Location����������������������������������������������������������������������������������������������������������������������������������� 202

When Caching Happens������������������������������������������������������������������������������������������������������������������������������������������������������������������� 202

The Difference Between the Smart Cache and User Cache Modes��������������������������������������������������������������������������� 203

Manually Controlling the Cache��������������������������������������������������������������������������������������������������������������������������������������������������� 204

Controlling Fusion Output Caching��������������������������������������������������������������������������������������������������������������������������������������������� 204

Controlling Node Caching���������������������������������������������������������������������������������������������������������������������������������������������������������������� 205

Controlling Color Output Caching������������������������������������������������������������������������������������������������������������������������������������������������ 205

Controlling Edit Page Filter Caching������������������������������������������������������������������������������������������������������������������������������������������� 205

Using Cached Media When Rendering in the Deliver Page�������������������������������������������������������������������������������������������� 205

Clearing Cached Media��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 205

The Cache Manager���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 206

Automatic Cache Deletion�������������������������������������������������������������������������������������������������������������������������������������������������������������� 207

Using Proxy Media������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 207

Creating and Using Proxy Media�������������������������������������������������������������������������������������������������������������������������������������������������� 207

Proxy Handling Display���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 208

Creating Proxy Files with the Blackmagic Proxy Generator�������������������������������������������������������������������������������������������� 209

Generating Proxy Media in Other Applications���������������������������������������������������������������������������������������������������������������������� 212

Managing Proxy Media����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 213

Switching Between Proxy Media and Original Media���������������������������������������������������������������������������������������������������������� 214

Using Proxy Files for Delivery���������������������������������������������������������������������������������������������������������������������������������������������������������� 214

Moving Proxies Using a DaVinci Resolve Archive (.dra)������������������������������������������������������������������������������������������������������ 215

Working Remotely Using Proxy Media���������������������������������������������������������������������������������������������������������������������������������������� 215

Proxy Media vs. Other Playback Optimizations in DaVinci Resolve����������������������������������������������������������������������������� 216

Using Optimized Media, Proxy Media, and Caching Together������������������������������������������������������������������������������������� 217

Which Playback Optimization Method Should I Use?�������������������������������������������������������������������������������������������������������� 217

Other Project Settings That Improve Performance������������������������������������������������������������������������������������������������������������� 218


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Understanding the GPU Status Display

Every viewer in DaVInci Resolve exposes a GPU status indicator and a frame-per-second (FPS) meter,

which appears in the Viewer’s title bar, which shows you your workstation’s performance whenever

playback is initiated. Since DaVinci Resolve uses one or more GPUs (graphics processing units) to

handle all image processing and effects, the GPU status display shows you how much processing

power is being used by whichever clip is playing.

Frame rate and GPU indication,

green is good

A green status indicator shows there is plenty of GPU processing headroom available. As the

GPU resources is increasingly taxed, this green graph eventually turns red to show that the

available GPU power is insufficient for consistent real time playback.

Red indicates that playback is at

slower than real time

Eventually, as you add more and more effects and corrections, you’ll reach the limits of available

performance, forcing DaVinci Resolve to either drop frames, or play video at a slower speed in

order to maintain high image quality, shown by the red FPS indicator.

When real time performance falls short, DaVinci Resolve provides a variety of controls and options

that let you enhance real time playback and effects. Each is useful for different situations, and all

can work together so you can choose the best trade-off between image quality and performance

while you work. All of these methods can be set up to have no effect on your delivered output.

Prioritizing Audio or Video

Playback in the Edit Page

When available processing power is insufficient to play the clip or clips at the position of the playhead

due to the grade, transforms, or effects that are applied at that moment in the Timeline, you have the

ability to choose exactly how performance in DaVinci Resolve degrades, by turning the “Show All

Video Frames” on or off in the Option menu of the Edit page Viewers.

�Show All Video Frames off: The default setting, ideal for video editing. Prioritizes audio playback

at the expense of dropping video frames when processing power is tight, resulting in a more

conventional playback experience.

�Show All Video Frames on: An alternate setting that’s ideal when you’re doing effects work, for

which you need to see every single frame play back, sequentially. Audio quality is compromised

while every frame of video plays in slower-than-real-time, if necessary, to maintain playback.

Keep in mind that this setting only affects playback when GPU performance is lacking.

In areas of the Timeline where performance is adequate, playback remains uncompromised.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Performance Mode Improves

Overall Performance

Performance Mode, which is found in the Playback Settings of the User Preferences, analyzes your

computer’s configuration, the CPU, GPU, connected video interface, and so on, and automatically

tunes DaVinci Resolve’s under-the-hood image processing settings to provide the best interactivity on

your machine. It’s set to Automatic by default, although you can choose to adjust its effect manually,

or disable it altogether. When enabled, Performance Mode dramatically improves the experience of

editing, mixing, and grading on less powerful computers.

While Performance Mode is turned on, DaVinci Resolve still outputs to video, renders in the Delivery

page, and processes via the Media Management command at the highest quality. As a result, using

Performance Mode makes no compromise in the quality of your output, so creative editors and audio

mixers can leave this setting on always.

Finishing editors and colorists might notice subtle differences between the image on your computer

monitor on less powerful computers when Performance Mode is on versus when it’s off, which is

why this setting can be disabled, either entirely or in part using checkboxes in the Playback Settings

panel of the User Preferences for instances where GUI interactivity is less important than your

onscreen display.

Adjusting Performance Mode

A pair of radio buttons in the Playback Settings panel of the User Preferences let you choose between

Automatic (default) and Manual behaviors when you turn on Performance Mode in DaVinci Resolve.

Set to Automatic, Performance mode automatically optimizes a variety of operations in a bid to balance

performance with the necessary level of image quality, for fast onscreen performance while always

maintaining the highest level of quality for video output.

Set to Manual, there are three different settings you can choose to disable for instances where a

particular performance tradeoff results in an undesirably noticeable reduction in image quality in

Performance Mode:

Optimized Sizing: Relates to how image resizing is handled.

Optimized Decode Quality: Relates to how clip resolution vs. timeline resolution is handled.

Optimized Image Processing: Relates to how image processing operations are handled.

Timeline Proxy Mode

Improves Effects Performance

If you don’t want to either drop frames or play at slower than real time speed whenever the GPU Status

indicator is in the red, an immediate way of improving performance is to turn on the Use Timeline

Proxies option in the Playback menu. Using timeline proxies reduces processing demands by taking

advantage of the resolution independence of DaVinci Resolve to lower the resolution of your clips

on-the-fly, thereby increasing real time playback performance without the need to spend time caching

part or all of the timeline, or create optimized media (both discussed later).


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

To turn Use Timeline Proxies on and off:

Choose Playback > Timeline Proxy Resolution > Half Resolution, Quarter Resolution, or None.

Turning on one of the proxy resolutions reduces the working resolution by either half or a quarter

of whatever the current Timeline resolution is for your project. Working at a temporarily reduced

resolution increases your workstation’s real time performance, while the resolution independence of

Resolve guarantees that every window you draw and sizing operation you make scales correctly to

the actual resolution of your project.

Proxy Resolution

Width

Height

Full 8K UHD


Full UHD/Half 8K UHD


Full-HD/Half UHD/Quarter 8K UHD


Half-HD/Quarter UHD/Eighth 8K UHD


Quarter-HD/Eighth UHD/Sixteenth 8K UHD


Table of half and quarter proxy resolutions for different television frame sizes

IMPORTANT: Timeline Proxy Mode is entirely different and independent of the creation of

Proxy Media as described later in this chapter. The two functions, Timeline Proxy Mode and

Proxy Media, have no relation to each other.

Reducing Decode Quality

Improves Raw Media Performance

The Use Proxy command will improve performance when grades and effects are responsible for your

project’s slower than real time playback, but Use Proxy won’t help when real time performance is

being used up by the need to debayer raw media. While you could improve playback performance by

taking the time to either generate optimized media (see below) or render to the Fusion Output Cache

by enabling the Smart Cache (see later in this chapter), the fastest solution is to open the Camera Raw

panel of the Project Settings and reduce the Decode Quality of the raw media formats you’re using:

Decode Quality: Camera raw formats such as R3D and F65 can be debayered at different

levels of quality. For higher real time performance, you can choose a lower quality setting

while you work, and then switch to a higher quality when rendering the final output.

Options for reducing resolution vary by each raw format’s differing capabilities, but at the very

least include full, half, and quarter resolution (R3D and Sony Raw have options for full, half,

quarter, eighth, and sixteenth). Exceptions include the Canon RAW, Panasonic Varicam RAW,

and Phantom Cine formats, which only decode to full resolution.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

If you reduce the decode quality of raw media formats in your project to improve performance,

you can use the “Force debayer res to highest quality” checkbox in the Render Settings list of

the Deliver page to ensure that DaVinci Resolve renders all raw formats at the highest quality

available, so you don’t have to worry about forgetting to change the decode quality back

when it’s time to render your deliverables.