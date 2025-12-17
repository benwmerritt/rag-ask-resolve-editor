---
title: "Marker Overlays and Navigation"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 538
---

# Marker Overlays and Navigation

If you part the playhead on top of a marker in the Timeline of the Color page, that marker’s information

appears in a Viewer overlay, just as in the Edit page, making it easier to read notes and see what

information is available. These overlays can be easily hidden by clicking the Viewer option menu and

turning off “Show marker overlays.”

Timeline Marker List Available in

Color Page Viewer Option Menu

The option menu of the Color page Viewer has a submenu that lists all Timeline Markers in the

currently open timeline. This makes it easy to run down client notes.

Timeline markers list available for quick access in the Viewer’s option menu


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Using Video Scopes

While not directly tied to use of the Viewers, video scopes nonetheless work hand in hand to help

you evaluate the images you’re working on. DaVinci Resolve has a set of five real-time video scopes

that you can use to monitor the internal data levels of clips in your project as you work. Each scope

provides an unambiguous graphical analysis of different characteristics of the video signal, showing

you the relative strength and range of individual color components including luma, chroma, saturation,

hue, gamut, white point, and the red, green, and blue channels that, together, comprise the color and

contrast of the images in your program.

Video Scope Location

By default, you can view any one of these scopes at a time at the bottom right corner of the Color

page, by clicking the Video Scope button in the palette button bar.

The video scope, docked next to the other palettes at the bottom of the Color page

Optionally, you can click the Expand button at the top right of the video scope to open the video

scopes into a floating window, within which you can display all four video scopes together, or

individually, on any monitor connected to your workstation.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Video scopes in a floating window in HDR (ST.2084/HLG) mode

Additionally, the video scopes can appear docked on a second display as part of many of the dual-

screen layouts available in DaVinci Resolve. However, if you have three computer displays and you’re

using dual screen layouts, you still have the option to open the floating Scopes window and place it on

your third display, as large as you need.

The video scopes aren’t just available in the Color page. They’re also available in the Media and

Deliver pages for whenever you need to evaluate the video signal more objectively, such as when

you’re setting up to capture from tape or scan from film, or when you’re setting up for output.

To open video scopes from the Media, Color, or Deliver pages, do one of the following:

Choose Workspace > Video Scopes > On/Off (Command-Shift-W) to open video scopes into a

floating window.

Choose Workspace > Dual Screen > On to open video scopes as part of a dual screen layout.

Video Scope Measurement Using Scales

Because you’re evaluating the internal state of the image data, by default the numeric scales of the

WFM and Parade scopes always reflect 10-bit full range data from 0–1023, regardless of the Video/

Data Level setting you’ve selected in the Master Settings panel of the Project Settings. This gives you

a window into how the image is being processed by DaVinci Resolve prior to being output via your

computer’s video I/O interface.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

If you’re working on an HDR (High Dynamic Range) grade, you can choose HDR (ST.2084/HLG) from

the Video Scopes option menu (this feature is only available in Studio version). This replaces the

10-bit scale of the Waveform, Parade, and Histogram video scopes with a scale based on nit values

(or cd/m2) instead.

The Parade scope

showing the data

range scale

The Parade scope

showing the HDR

“nit” scale

Changing Waveform Scales

A Waveform Scale Style submenu in the Video Scopes option menu (the three dots menu) lets you

choose how you want the numeric scale at the left of Waveform and Parade scopes to be represented.

There are options for 10-bit display (the default), 12-bit display, Percentage (0 to 100), millivolt (mV), and

HDR (ST.2084/HLG). Aside from the added flexibility this gives you, this also means that it’s no longer

necessary to go to the Preferences to change the scope to have an HDR scale shown in nits (cd/m2).

Waveform scale options

IMPORTANT: If you are working in a non-DaVinci Resolve Color managed workflow and

activate the HDR (ST.2084/HLG) scopes, the waveform will always reflect HDR levels, even if

you’ve manually selected the output color space as Rec.709, and thus not be 100% accurate.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Changing Vectorscope Scales

A Vectorscope Scale Style submenu in the Video Scopes option menu (the three dots menu)

lets you choose how you want the hue reference indicators to be displayed.

Vectorscope scale options

There are four available graticule options:

Off: Disables all graticule overlays in the Vectorscope, giving you a clean view of the

Vectorscope graph against black.

Standard: The default layout. Cross hairs indicate the center of the scope, while boxes

indicate the center target of each primary and secondary hue (red, magenta, blue, cyan,

green, yellow). An outer circle provides a general frame of reference for the angle that any part

of the graph might fall along.

Simplified: Shows a crosshairs to indicate the center of the scope and smaller crosshairs

to indicate each primary and secondary hue. Useful when you want references without

extra complications.

Hue Vectors: A graticule designed to provide a more useful colorist reference for creative

decisions and image comparison. This isn’t simply decorative. Graticule lines stretch along

the reference angle of each primary and secondary hue from the hue targets to the center,

providing a more immediately useful frame of reference when comparing different vector

scope graphs to one another. These reference lines fade out within the region of average

saturation in most images, so they don’t get in the way of discerning faint details. The center

crosshairs are aligned with the red‑cyan and yellow-blue axes, indicating the naturalistic warm

to cool axis that lies between them. Tic marks indicate both the 75% and 100% levels of image

saturation for each hue.

You also have the option of choosing whether or not the primary and secondary hue targets

are shown for 75% image saturation, 100% image saturation, or both, and whether or not you

want to show the text labels for each hue.

Displaying Scopes With Data or Video Levels

For projects being worked on at video levels, a setting in the Video Scope option menu’s Waveform

Scale Style submenu lets you toggle between displaying video scopes scaled to either Data Levels

(the default) or Video Levels (by turning on Video Level Scopes). This only affects how your scopes are

displayed; it has no effect on monitored or rendered output.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

The Waveform scope shown at default Data Levels,

The same waveform shown with Video Level Scopes turned on