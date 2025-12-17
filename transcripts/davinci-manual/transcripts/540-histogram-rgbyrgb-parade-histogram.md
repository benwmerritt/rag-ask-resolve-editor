---
title: "Histogram (RGB/YRGB parade histogram)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 540
---

# Histogram (RGB/YRGB parade histogram)

Displays a statistical analysis of how many pixels of each color channel lie at each percentage of

tonality, plotted along a digital scale from 0 percent (black) to 100 percent (white). Comparing the left,

middle, and right parts of the Y, R, G, and B graphs (Y is optional) lets you evaluate the color balance in

the shadows, midtones, and highlights of the image.

The Histogram scope set to YRGB

Taken altogether, the left of all graphs indicates the black point of the image, while the right of all

graphs indicate the white point. It then follows that the difference between the width of the left and

right of all graphs indicates the overall contrast ratio of the image you’re evaluating. Wide histogram

graphs indicate a wide contrast ratio, while narrow histogram graphs indicate a narrow contrast ratio.

CIE Chromaticity Scope

DaVinci Resolve contains CIE 1931 xy and CIE 1976 uv scopes, which let you see the current image

analysis as a graph superimposed against a triangle that represents the tristimulus values of the color

gamut you’re working within, along with an indication of the current white point. A label shows the

currently selected gamut, with the specific coordinates of these Red, Green, and Blue values as well

as the White point, while the overall “horseshoe” shape represents the entire range of visible light, all

plotted against an xy graph.

The white point ordinarily appears atop a curve along the center of the shape. This curve indicates

the black body locus, along which the various color temperatures of an image’s white point correlate,

from orange-ish warm to blue-ish cool. This black body locus corresponds to the color temperatures

obtained by progressively heating carbon to different temperatures.

You also have the option of showing a second gamut triangle, in cases where you want to compare

the current analysis to two different gamuts. This can be useful when you need to create deliverables

in multiple gamuts, and you want to see which parts of the video signal are safe in all gamuts and

which parts are exceeding the smaller of the two. When you do this, both gamuts are labeled, and the

coordinates of the Red, Green, and Blue values of both gamuts are listed to the side.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

The CIE 1931 xy scope showing both P3 and Rec. 709 gamuts

In a way, the Chromaticity scope is a 3D scope, but it’s drawn as if you’re looking down at the top of a

3D shape that plots every color value in an image in X, Y, Z space, but you can only perceive the 2D

outline around the widest parts of this shape drawn on an X, Y plot. The graph does indeed represent

every single value found within a 3D plot of the image data, but the triangle only indicates the widest

“slice” of the current gamut and of this 3D shape within the mid-tones.

What this means is that while the Chromaticity scope’s graph gives you a rough idea of whether or not

the current image is within gamut relative to your delivery spec, it’s not exact and it’s not foolproof,

as part of the image data could fall within this wide triangle and yet overshoot the required gamut

elsewhere in the highlights at the top or the shadows near the bottom of the 3D shape you’re looking

down on. On the other hand, if any part of the graph does extend past the boundaries of the gamut

triangle, then that definitely indicates a gamut violation.

You can add an additional gamut triangle in the scope settings in order to compare the color space

you’re working in to another color space, for reference.

Most people who’ve had any exposure to color grading concepts are familiar with the traditional CIE

1931 horseshoe graph, which plots the portion of the spectrum visible to the human eye according

to studies done in the late 1920s (subsequent studies have confirmed this analysis). The optional CIE

1976 uv graph is based on an updated color space (CIELUV) that was an attempt by the International

Commission on Illumination (CIE) to create a more perceptually uniform graph of color. Whereas the

CIE 1931 analysis visually exaggerates certain parts of a color graph, the CIE 1976 graph draws all parts

of a color graph more or less proportionally to one another. Overall, neither analysis is more “correct”

than the other, it’s simply a matter of what you prefer to look at.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

The CIE 1976 scope showing both P3 and Rec. 709 gamuts

Panning and Zooming the Video Scopes

If you want to examine any part of a video scope’s graph in more detail, you can do the following:

To zoom into a graph: Hold the Option key down, and roll the scroll control.

To pan around a graph: Click and drag with the middle pointer button.

Customizing the Video Scopes

Once you’ve opened the video scopes, there are a variety of ways you can customize how the scopes

look, and expose additional onscreen graticule information to help you measure what you need.

Methods of customizing the Scopes window:

�To change the size of the Scopes window: Drag the lower right-hand corner to resize the Scopes

window to the desired size.

�To change how many scopes are displayed at once: Click one of the buttons in the upper right-

hand corner of the Scopes window to set 1, 2, 4, or 9 up arrangements of the video scopes. You

can also choose how many scopes are simultaneously displayed by choosing Workspace > Video

Scopes > 1-Up, 2-Up, or 4-Up.

�To change which scopes appear in which pane: Click the Name drop-down at the upper left

corner of each scope’s pane, and choose a different scope. If you like, you can instantiate more

than one of each kind of video scope in multi-scope layouts, for instances where you want to

view variations on a particular type of scope with different settings. For example, you might want

to expose three Vectorscopes, setting each to a different tonal range so you can simultaneously

view Vectorscope analyses of Low (shadows), Mid (midtones), and High (highlights).


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Different layout options in the Scope window

Once open, you can resize the Scopes window to make it as large or small as you require,

positioning on a second display if you want to make it even larger.

To customize each video scope’s display options:


Click the Option button to the right of the Scope drop-down menu to expose the current scope’s

Custom Controls window.

Clicking to open the current scope’s custom controls


Adjust any of the available controls to customize the look of that particular scope.


Click anywhere outside of the Custom Controls window to make it disappear.

Parade Scope Display Options

The Parade scope has the following options:

�RGB, YRGB, and YCbCr modes, allowing you to evaluate more channels than before.

�A colorize checkbox lets you view graphs in monochrome or false-color (indicating red,

green, and blue).

�An Extents checkbox draws an outline highlighting all graph excursions, to unambiguously show

you all overshoots and undershoots in each waveform.

�The Parade slider makes that scope’s graph brighter or dimmer. Brighter graphs make it easier to

see fine detail, but harder to see which parts of the graph are stronger and weaker.

�The Graticule slider makes that scope’s scale brighter or dimmer, making it more or less visible

(or distracting) relative to the graph.

�The Show Reference Levels checkbox lets you turn on adjustable Low and High

reference level markers by setting the low and high sliders to something other than their

defaults. This is especially useful for HDR grading where you’re working within a specific peak

luminance threshold.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Options in the Parade scope

Options in the Waveform scope

Waveform Scope Display Options

The Waveform scope has the following options:

�Y (luma) and CbCr (chrominance) modes to show you the true luma or chroma signals in isolation,

and RGB to show you only an RGB analysis.

�In RGB mode, R, G, and B buttons that can be individually toggled on and off to see any

combination of graphs.

�A colorize checkbox lets you view overlaid graphs in monochrome or false-color (indicating red,

green, and blue). If you’re only enabling the Y or C scopes, the different areas of these graphs are

drawn with color taken from the image being analyzed, which makes it easier to see which part of

the scope graph corresponds to which part of the image.

�An Extents checkbox draws an outline highlighting all graph excursions, to unambiguously show

you all overshoots and undershoots in each waveform.

�The Waveform slider makes that scope’s graph brighter or dimmer. Brighter graphs make it easier

to see fine detail, but harder to see which parts of the graph are stronger and weaker.

�The Graticule slider makes that scope’s scale brighter or dimmer, making it more or less visible (or

distracting) relative to the graph.

�The Show Reference Levels checkbox lets you turn on adjustable Low and High reference

level markers by setting the low and high sliders to something other than their defaults.

This is especially useful for HDR grading where you’re working within a specific peak

luminance threshold.

Vectorscope Display Options

The Vectorscope has the following options:

�Choose ALL to view the entire tonal range of the image as a Vectorscope graph analysis, or to

selectively view just the shadows (Low), mid-tones (Mid), or highlights (High) of the image as a

vectorscope graph analysis.

�A Colorize checkbox draws the different areas of these graphs with color taken from the image

being analyzed, which makes it easier to see which part of the scope graph corresponds to which

part of the image. With colorize turned off, graphs only appear white.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

�An Extents checkbox draws an outline highlighting all graph excursions to unambiguously show

you all overshoots and undershoots.

�A Combine checkbox lets you see simultaneous overlapping extents for the highlights, mid-tones,

and shadows overlaid on one another.

�The Vectorscope slider makes that scope’s graph brighter or dimmer. Brighter graphs make it

easier to see fine detail, but harder to see which parts of the graph are stronger and weaker.

�The Graticule slider makes that scope’s scale brighter or dimmer, making it more or less visible (or

distracting) relative to the graph.

�Low Range and High Range sliders let you manually define the boundaries separating shadows

from mid-tones and highlights. Low Range defaults to 0.30, and High Range defaults to 0.70.

�Show 2X Zoom zooms the vectorscope graph by 200%, making it easier to see fine detail and use

the vectorscope with charts.

�Show Skin Tone Indicator checkbox shows a line at the traditional Inphase angle that is useful as a

general guidepost for average skin tone hue.

�Show Graticule checkbox lets you show or hide the circular degrees indicator surrounding the

outer edge and the cross hairs that indicate the center of the vectorscope.

Options in the Vectorscope

Options in the Histogram scope

Options in the Chromaticity scope

Histogram Display Options

The Histogram has the following options:

�You can view either RGB or YRGB histograms.

�Gain slider scales that scope’s graph taller or shorter. Taller graphs expand to show greater detail

in the histogram’s peaks, shorter graphs reduce the apparent detail.

�Graticule slider makes that scope’s scale brighter or dimmer, making it more or less visible

(or distracting) relative to the graph.

�The Show Reference Levels checkbox lets you enable adjustable Low and High reference

level markers by setting the Low and High sliders to something other than their defaults. These

reference markers are especially useful for HDR grading where you’re working within a specific

peak luminance threshold.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

CIE Chromaticity Display Options

The CIE Chromaticity scope has the following options:

�You can view a chromaticity analysis in either a CIE 1931 xy graph, or a CIE 1976 uv graph.

�CIE Chromaticity slider makes that scope’s graph brighter or dimmer. Brighter graphs make it

easier to see fine detail, but harder to see which parts of the graph are stronger and weaker.

�Graticule slider makes that scope’s scale brighter or dimmer, making it more or less visible (or

distracting) relative to the graph.

�Additional Gamut drop-down menu lets you expose a second gamut triangle, for instances where

you want to compare how an image fits into two different gamut ranges.

�Show 2X Zoom zooms the CIE graph and graticule by 200%, making it easier to see fine detail and

use the vectorscope with the charts.

�Show Graticule checkbox lets you show or hide the circular degrees indicator surrounding the

outer edge and the cross hairs that indicate the center of the vectorscope.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR