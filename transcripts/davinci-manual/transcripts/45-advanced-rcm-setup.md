---
title: "Advanced RCM Setup"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 45
---

# Advanced RCM Setup

Advanced users who need more detailed control over every aspect of RCM can choose Custom from

the Resolve Color Management preset menu. This exposes every control that’s available, which opens

a world of workflow possibilities for advanced users and post production facilities.

Because each of the settings encompasses a significant amount of functionality, the following sections

cover each particular parameter in detail.

NOTE: Older projects using RCM will have Color science set to Legacy, to preserve the

older color management settings and color transformations effect on your work. For more

information on how the previous generation of RCM works, see the September 2020 version

of the DaVinci Resolve 16 Manual.

Custom Color Management settings of Resolve Color Management, as updated in DaVinci Resolve 17

Single Setting vs. Dual Setting RCM

There are two ways you can set up RCM. When the “Use Separate Color Space and Gamma”

checkbox is turned off, the Color Management panel of the Project Settings exposes one drop-down

each for the Input, Timeline, and Output Color Space settings. Each setting lets you simultaneously


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

transform the gamut and gamma, depending on which option you choose. This makes it a bit simpler

to set up the transform you need.

Single setting Resolve Color Management

If you turn the “Use Separate Color Space and Gamma” checkbox on, then the Color Management

panel changes so that the Input, Timeline, and Output Color Space settings each display two pop-ups.

The first drop-down lets you explicitly set the gamut, while the second drop-down lets you explicitly

set the gamma. This makes it easier to see exactly which pair of transforms is being used at each

stage of RCM.

Dual setting Resolve Color Management

Additionally, Dual Setting RCM enables you to assign separate gamut and gamma transforms to clips in

the Media Pool.

Dual setting Resolve Color Management

assignments for Media Pool clips

Setting the Input Color Space

This setting is the default color space that all otherwise unidentified clips in the Media Pool will default

to, unless you manually identify the color space of these clips by right-clicking them and choosing an

Input Color Space (and optionally Input Gamma) from the contextual menu.

This setting does not affect media in camera raw formats, or media with embedded

color space metadata.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Choosing a Timeline Color Space

The Timeline Color Space is the “working” color space that determines how each clip’s contrast and

color are mapped for adjustment, which in turn has an impact on how sensitive the effects and grading

controls are as you work. Some colorists prefer to work in the classic “video” color space of Rec. 709,

since the controls feel comfortable and familiar, particularly if you’re mastering SDR content. On the

other hand, colorists who are used to working with log-encoded media (likely using the Log controls)

often prefer to work in a more film-oriented workflow using Cineon, LogC, or other wide gamut,

logarithmically encoded formats.

If you’re outputting an SDR deliverable, any color space that you’re comfortable will produce good

results. However, if you’re outputting an HDR deliverable, it’s in your best interest to choose a wide

gamut Color Space (and Gamma) to obtain the best results on output. In this instance, DaVinci Wide

Gamut is a great choice (see below for more information).

No matter which Timeline Color Space you choose to work in, all clips in an edit are transformed from

the Input Color Space that’s either automatically or manually assigned to them, to the Timeline Color

Space setting to provide the final output. This is how you can grade within a Log-encoded timeline

color space and yet view a normalized or de-logged image.

IMPORTANT: Once you choose a Timeline Color Space and begin grading, do not change

your Timeline Color Space, or you’ll end up changing all of the grades that are built using

the mathematics it defines. You can always change the Output Color Space to create a new

deliverable, but all of your grades depend on the Timeline Color Space to render correctly.

DaVinci Wide Gamut Color Space and DaVinci Intermediate Gamma

DaVinci Wide Gamut (DaVinci WG) and DaVinci Intermediate are Timeline Color Space and Gamma

settings developed by Blackmagic Design that provide a reliable universal internal working color

space, which encompasses a practical maximum of what image data any given camera can capture.

The DaVinci Wide Gamut color space is greater than BT.2020, ARRI Wide Gamut, and even ACES, so

you don’t ever lose image data, no matter where your media is coming from.

The DaVinci Wide Gamut color space


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Furthermore, the primary color values of the DaVinci WG color space are set such that the process of

automatically mapping source media from different cameras into this gamut is extremely accurate as

part of the Input to Timeline Color Space conversion, and tone and saturation mapping from one color

space to another can be done more accurately in the Timeline to Output Color Space conversion.

This also helps to produce greater consistency among media from different cameras when making

manual grading adjustments (though some variations due to differences in camera and lens systems

will remain).

The DaVinci Intermediate OETF gamma setting has been designed to work with DaVinci Wide Gamut

to provide a suitable internal luminance mapping of high precision image data, in preparation for

mastering to either HDR or SDR standards, as your needs require, without losing image data.

The DaVinci Intermediate OETF seen encoding HDR levels

The DaVinci Intermediate OETF encoding SDR levels


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Resolve Color Management is extremely flexible, so you don’t have to use DaVinci Wide Gamut/

DaVinci Intermediate as your Timeline color space if you don’t want. However, it presents many

advantages and is worth trying out to see if it can improve your workflow.

For more information, see the “DaVinci Resolve Wide Gamut Intermediate” document at

https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion.

Timeline Working Luminance

This control is only visible while the Resolve Color Management presets menu is set to Custom

Settings. The Timeline Working Luminance drop-down menu lets you choose how the Input DRT

(described below) maps the maximum level of a source image to the currently selected Timeline Color

Space. This setting also defines the maximum highlight level that’s possible to output into the currently

selected Output Color Space using the Output DRT.

While it’s typical to set this according to the mastering standard you’re grading to via a collection of

SDR and HDR labeled settings, there are additional settings available that make it possible to add

more automatic compression of highlights as you grade.

SDR 100: The conventional setting for grading SDR material with a maximum level of 100 nits.

HDR 500-4000: Conventional settings for grading HDR material at a variety of maximum

mastering levels. So long as output DRT isn’t set to None, there will be some manner of rolloff

in the highlights, unless inverse DRT is enabled, in which case there will be no rolloff.

SDR and HDR ER settings: These “extended range” settings each specify two values and

provide more headroom for aggressive grading of highlights by enabling DaVinci Resolve to

compress a greater range of out-of-bounds image data without clipping, which can result in a

smoother look.

Here’s how it works. Suppose you choose the setting “HDR ER 1000/2000.” In this case,

the Input DRT is used to map the maximum brightness of each source image to the range

specified by the first value, which is 1000 nits. Then, when you grade, the signal isn’t clipped

until it reaches the maximum range specified by the second value, which is 2000 nits. This

provides an additional 1000 nits of out-of-bounds headroom before the image data is hard

clipped by RCM’s image processing pipeline. The Output DRT is then used to map from the

maximum brightness specified by the second number (2000 nits) to the output value defined

by the currently selected Output Color Space, in the process compressing this out-of-bounds

headroom to preserve as much highlight detail as is possible given the range you’ve selected.

Custom: Exposes a field where you can enter a specific nit value.

203 Nit Support for SDR to HDR

This control is only visible while the Resolve Color Management presets menu is set to Custom

Settings. Resolve Color Management has support for remapping SDR content to HDR by mapping

100 nits to 203 nits (defined as the diffuse white level) according to the BT.2100 recommendation.

This enables the peak highlights of SDR material to compete more favorably against the significantly

brighter highlights of HDR content in programs that combine both (such as documentaries), so that

SDR whites continue to appear white, rather than gray, when compared to diffuse white in HDR.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

The checkbox that enables this is hidden by default. Whenever you set the Output to an HDR standard

while the Timeline is set to an SDR standard, the “Use 203 nits reference for Rec.2100 HDR” checkbox

for remapping SDR highlights to HDR appears in both the RCM settings of the Color Management

panel of the Project Settings and in the Color Space Transform Resolve FX plugin.

The “Use 203 nits reference for Rec.2100 HDR” checkbox in Resolve Color

Management for scaling SDR levels appropriately into HDR color space