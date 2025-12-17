---
title: "Gamut Limiting, Restricting Values Within a Larger Gamut"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 46
---

# Gamut Limiting, Restricting Values Within a Larger Gamut

This control is only visible while the Resolve Color Management presets menu is set to Custom

Settings. In the emerging world of larger gamuts for distribution, it’s increasingly common for delivery

specifications to specify output to a large gamut, such as Rec. 2020, yet require that image values

be restricted to a smaller gamut, such as P3. This is to allow delivery to “future-proofed” delivery

standards, while preventing saturation values that are too high to be displayed on consumer displays

that aren’t capable of implementing the full scope of those standards.

In this case, you’ll choose a larger gamut in Output Color Space, but you’ll then choose a smaller

gamut in “Limit Output Gamut To.” When you do this, all image values falling outside the “Limit Output

Gamut To” standard specified will be hard clipped. This setting defaults to None.

Choose a setting from the Limit Output Gamut To menu to limit image values within a larger gamut

Input DRT Tone Mapping

This control is only visible while the Resolve Color Management presets menu is set to Custom

Settings. RCM has always transformed the color primaries of different media formats to match one

another within the shared Timeline Color Space. In this updated version, the Input DRT (Display

Rendering Transform) drop-down menu provides a variety of different options to enable DaVinci

Resolve to automatically tone map the image data of SDR and HDR clips to better match one another

when they’re fit into the currently selected Timeline Color Space. While each option varies in the

details, they are all automated input-to-timeline color transforms that do the following:


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

�Log-encoded media, or media using a 2.4 gamma transfer function, is mapped so the black point,

midtones at 18% gray, and white levels match those of HDR media. Highlight data will be carefully

stretched as necessary so that the highlights of all clips in the Timeline, whether SDR or HDR,

are treated similarly.

�Raw formats such as BRAW, RED, and ARRI RAW, and media using HDR transfer functions are

minimally mapped along an HDR range of tonality.

�All color transforms into the Timeline Color Space are done without clipping.

The idea is to distribute the image data of each clip in the Timeline, be it SDR or HDR media, along

a similar histogram, with shadows, midtones, and highlights spread out in such a way as to create an

easier starting point for grading. One result of this is that grades made for one type of media mostly

work well with other types of media.

Different options are provided governing the details of how this Input to Timeline Color Space

transform is achieved. They all do the same thing but have different advantages.

�None: This setting disables Input DRT Tone Mapping. No tone mapping is applied to the

Input to Timeline Color Space conversion at all, resulting in a simple 1:1 mapping to the

Timeline Color Space.

�Simple: A good mapping for color transforms from HDR to SDR.

�Luminance Mapping: Same as DaVinci, but more accurate when the Input Color Space of all your

media is in a single standards-based color space, such as Rec. 709 or Rec. 2020.

�DaVinci: This option tone maps the transform with a smooth luminance roll-off in the shadows and

highlights, and controlled desaturation of image values in the very brightest and darkest parts of

the image. This setting is particularly useful for wide-gamut camera media and is a good setting to

use when mixing media from different cameras.

�Saturation Preserving: This option has a smooth luminance roll-off in the shadows and highlights,

but does so without desaturating dark shadows and bright highlights, so this is an effective option

for colorists who like to push color harder. However, because over-saturation in the highlights

of the image can look unnatural, two parameters are exposed to provide some user-adjustable

automated desaturation.

Sat. Rolloff Start: Lets you set a threshold, in nits (cd/m2), at which saturation will roll off along with

highlight luminance. Beginning of the rolloff.

Sat. Rolloff Limit: Lets you set a threshold, in nits (cd/m2), at which the image will be totally

desaturated. End of the rolloff.

Output DRT Tone Mapping

This control is only visible while the Resolve Color Management presets menu is set to Custom

Settings. To accommodate workflows where you need to transform one color space into another that

has a dramatically larger or smaller gamut, an additional group of settings have been added that can

help to automate the expansion or contraction of image data necessary to give a pleasing result.

Using the available options in the Output DRT drop-down menu will compress or expand your image

data as necessary during the Timeline to Output Color Space transformation that RCM performs when

monitoring or rendering a timeline, in order to make sure that the final result is either not clipping, or to

ensure that it’s taking better advantage of the new color space. This is not meant to provide your final

grade. Rather, it’s meant to give you a faster starting point, when you need it, for proceeding with your

own more detailed grade of the result.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Here are some examples of what the Gamut Mapping controls of RCM can be used for:


If you’re working with high-dynamic-range log-encoded media and you’re outputting to Rec. 709

as you work, turning on Gamut Mapping lets RCM use saturation and tone mapping to give you a

more immediately pleasing image with highlight detail that’s not clipped.


If you’re working with standard-dynamic-range log-encoded media and you’re outputting to an

HDR format as you work, turning on Gamut Mapping lets RCM use saturation and tone mapping

to expand the highlights of the image to HDR strength to give you an image with more immediate

visual impact on HDR screens.

(Before/After) Gamut Mapping used to automatically fit

high‑dynamic-range media into the Rec. 709 color space

The Output DRT (Display Rendering Transform) drop-down menu provides the following options.

�None: No tone mapping is applied to the Timeline to Output Color Space conversion at all,

resulting in a simple 1:1 output with no softness or rolloff applied. All image data outside of gamut

will be clipped.

�Simple: A good mapping for color transforms from HDR to SDR.

�Luminance Mapping: Same as DaVinci, but more accurate when all your media is in a single

standards-based color space, such as Rec. 709 or Rec. 2020, set to the Timeline and Output.

�DaVinci: This option tone maps your output with a smooth luminance roll-off in the shadows and

highlights, and controlled desaturation of image values in the very brightest and darkest parts

of the image. It’s been designed to give smooth, naturalistic highlights and shadows as you

push and pull the values of your images, without the need for additional settings. This setting is

particularly useful for wide-gamut camera media and is a good setting to use when mixing media

from different cameras.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

�Saturation Preserving: This option has a smooth luminance roll-off in the shadows and highlights

to prevent clipping. It does so without desaturating dark shadows and bright highlights, so this

is an effective option for colorists who like to push color a bit harder. However, because over

saturation in the highlights of the image can look unnatural, two parameters are exposed to

provide some user-adjustable automated desaturation.

Sat. Rolloff Start: Lets you set a threshold, in nits (cd/m2), at which saturation will roll off along with

highlight luminance. Beginning of the rolloff.

Sat. Rolloff Limit: Lets you set a threshold, in nits (cd/m2), at which the image will be totally

desaturated. End of the rolloff.

�RED IPP2: This setting lets you use RED IPP2 tone mapping to output to an SDR format, such as

Rec. 709; two settings are exposed with which to choose how your output will be shaped.

Output Tone Map: Lets you choose what kind of tone mapping you want to use for your output.

Options include: None, Low, Medium, and High.

Highlight Roll Off: Lets you choose what kind of highlight rolloff you want to use to prevent

clipping. Options include: None, Hard, Medium, Soft, and Very Soft.

HDR peak nits: A slider lets you choose the peak nit level you want to tone map to.

Defaults to 10,000 nits.

Use Inverse DRT for SDR to HDR Conversion

This control is only visible while the Resolve Color Management presets menu is set to Custom

Settings. A device rendering transform (DRT) is typically used when converting high dynamic range

media to a lower dynamic range color space/mastering standard. Thus, setting up a color transform

from SDR to HDR is an “inverse” operation to expand the dynamic range of SDR media to HDR

standards. The way this works is that levels at 100 nits are mapped to the maximum value set for the

Timeline Working Luminance parameter, and all other image levels are strategically tone mapped in

order to give yourself a good starting point for grading SDR media into an HDR program.

This setting also has a secondary use. With this setting turned on, you can output Rec. 709 clips with

color that’s identical to the input, with no compression in the highlights.

NOTE: Turning on “Use Inverse DRT for SDR to HDR Conversion” may exaggerate noise in

imported SDR media with large flat expanses of bright colors.

Use White Point Adaptation

This control applies a chromatic adaptation transform to account for different white points between

color spaces.

�Uncheck this box if you simply want to view the input color space’s white point unaltered in the

output color space. For example, wanting to use a P3-D60 mastered clip inside a P3-D65 timeline

for reference purposes.

�Check this box to apply the chromatic adaptation transform to convert the input white point to

match the output color space’s white point.  For example, wanting a P3-D60 mastered clip to cut in

with other clips mastered in a P3-D65 timeline.

NOTE: This control is only visible while the Resolve Color Management presets menu is set

to Custom Settings.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Color Space Aware Grading Tools

In DaVinci Resolve version 17, both Resolve Color Management and ACES enables “color space aware”

palettes, such as the new HDR palette, to have controls that feel consistent, no matter what color

space the original media is from, or what Timeline Color Space you’re using.

Other palettes, such as the Qualifier and Curves palettes, become color space aware when you turn

on the “Use Color Space Aware Grading Tools” checkbox in the Color Management panel of the

Project Settings (this is turned on by default). When you’re using color space aware grading tools, you

should not turn on HDR Mode for the node you’re working on.

�In the case of the Qualifier palette, this enables Qualifiers to create high-quality keys as you would

expect, no matter what the color space of the original media is, or what Timeline Color Space

you’re using.

�In the case of the Curves palette, this makes the overall range of each curve better fit the overall

data range of the current clip, making curves adjustments easier and more specific.

NOTE: This control is only visible while the Resolve Color Management presets menu is set

to Custom Settings.

Apply Resize Transformations In

When you’re using Resolve Color Management, a new “Apply Resize Transformations In” Project

Setting is available in the Color Management panel while the Resolve Color Management presets

menu is set to Custom Settings. This setting lets you choose which color space is used for resizing

operations. Ordinarily, resizing is done in Linear, but certain specialty workflows benefit from doing

resizing in other color spaces, so this option lets you choose which is best. The available options are:

Timeline: Uses the Timeline Color Space to perform all resizing operations.

Log: Uses a Log Color Space for resizing. Good for avoiding artifacts in certain high-contrast

images, such as titles and star fields.

Linear: Usually provides the best results with most SDR media.

Linear Mapped: Usually provides the best results with most HDR media.

Gamma: Provided in case you find a need for this option.

Gamma Mapped: Usually provides best results when mixing SDR media with

wide gamut and log-encoded media on the same timeline.

Graphics White Level

The “Graphics white level” setting lets you define a shared maximum level in nits (cd/m2) for titles,

generators, and selected effects that generate color. Changing this setting lets you change the

maximum level of all DaVinci Resolve-generated titles, generator graphics, and effects at once to

accommodate different mastering and output requirements.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA