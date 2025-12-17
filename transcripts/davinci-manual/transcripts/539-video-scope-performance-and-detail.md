---
title: "Video Scope Performance and Detail"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 539
---

# Video Scope Performance and Detail

All video scopes were updated for DaVinci Resolve 16 to show more detail with faster performance

than in previous versions. While they’re GPU-accelerated, the video scopes require a certain amount

of video processing power to operate. Depending on which combination of video scopes and scope

options you have selected, you may notice your real time processing capabilities ever so slightly

affected. Closing the video scopes frees up all processing for color correction and effects. On

high‑powered workstations, you probably won’t notice a difference, but on less powerful computers,

closing the scopes might make a small difference.

Two global settings in the Video Scope option menu affect the performance and detail of all video

scopes equally.

�On slower workstations, a quality submenu lets you choose High, Medium, or Low quality scope

drawing, to trade off legibility for performance. High quality shows you the most information about

the video signal, while an Auto option makes a selection based on your workstation’s capabilities.

The Quality setting in the Video Scope option menu


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

�All video scopes have a Low Pass Filter setting in the Video Scope option menu that filters out a

signal’s noise to make the scope graphs clearer to read. While this can act as an “x-ray” to better

see detail in the scope graph interiors, it can make the highlight and shadow excursions on the

graph seem a bit shy of where they actually are, so it’s recommended to enable the “Extents”

option of whichever scope you’re using to get an unambiguous look at the maximum excursions in

your scopes. Extents draws an outline highlighting all graph excursions to show you the true level

of all overshoots and undershoots in the video signal, even when the Low Pass Filter is on.

The Waveform scope with Low Pass Filter turned off

The Waveform scope with Low Pass Filter turned on


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Display Qualifier Focus in Video Scope Graphs

The Display Qualifier Focus setting in the Video Scope option menu helps you identify which features

in the video image correspond to which parts of the video scopes. With Display Qualifier Focus turned

on, choosing the Qualifier mode of the Viewer and moving the eyedropper around the image draws

circles around the sampled pixels as they appear in the currently visible video scope graph. If multiple

video scopes are visible, each scope will have an indication of the location of the sampled pixels that’s

specific to each scope.

Hovering the eyedropper over a feature in the Viewer

The regional analysis of those pixels

shown in the overlaid red, blue, and green

waveforms of the Waveform scope.

Explanation of Each Video Scope

There are five available video scopes, each of which shows a different analysis of the video signal

you’re adjusting.

Waveform Monitor

Overlays waveform analyses of the Y (luma/luminance), CBCR (the color difference channels of

Y’CBCR), or RGB (red, green, and blue) channels over one another so that you can see how they align.

The Waveform scope showing Y’ (luma) only, with colorization and extents enabled


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

The Y option presents a true Luma scope that can have Colorize enabled to show false color, which

lets you see which colors in the Viewer image are where in the video scope graph.

For the RGB scopes, the relative heights of the red, green, and blue graphs indicate is identical to the

description seen for the Parade scope below, and with color enabled the red, green, and blue graphs

are tinted with the color they represent. This makes it easy to see where all three graphs align, by

looking for where parts of the waveform monitor appear in white, which is the result of the red, green,

and blue graphs lining up and adding their color together.

Parade

The Parade scope shows separate waveforms side by side that analyze the strength of individual

video signal components. The Parade scope can be set to analyze RGB, YRGB, and Y’CBCR.

By showing a comparison of the intensity of the luma, red, green, and blue channels, the Parade scope

makes it possible to detect and compare imbalances by comparing the relative heights of the RGB

graphs in the highlights (the top of the R, G, and B graphs), shadows (the bottom of the R, G, and B

graphs), and midtones (the middle of the R, G, and B graphs) for the purposes of identifying color casts

and performing scene-by-scene correction.

When the YRGB channels are taken altogether, the bottom of all graphs indicates the black point

of the image, while the tops of all graphs indicate the white point. It then follows that the difference

between the height of the bottom and top of all graphs indicates the overall contrast ratio of the image

you’re evaluating. Tall parade graphs indicate a wide contrast ratio, while short parade graphs indicate

a narrow contrast ratio.

The Parade scope showing YRGB waveforms, with colorization and extents enabled


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Vectorscope

Measures the overall range of hue and saturation within an image. Measurements are relative to

a centered graticule that you can enable that’s overlaid on the scope, which provides a frame of

reference via crosshairs. DaVinci Resolve has a traditional vectorscope, the graph of which emulates

a trace-drawn graph, with 75 percent color bar targets indicating the angle of each of the primary

and secondary colors around the edge of the graph, and an optional skin tone reference graticule

(otherwise known as the In-phase reference).

The Vectorscope can have Colorize enabled to show false color which lets you see which colors in the

Viewer image are where in the video scope graph.

More saturated colors in the frame stretch those parts of the graph farther toward the edge, while

less saturated colors remain closer to the center of the vectorscope, which represents 0 saturation.

By judging how many parts of the vectorscope graph stick out at different angles, you can see how

many hues there are in the image, with the specific angle of each part of the graph showing you which

hues they are. Furthermore, by judging how well centered the middle of the vectorscope graph is

relative to the crosshairs, you can get an idea of whether there’s a color imbalance in the image. If the

vectorscope graph is off-centered, the direction in which it leans lets you know that there’s a color cast

(tint) in the image.

The Vectorscope shown in 2x mode, with combined highlights, mid-tones, and shadows extents


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR