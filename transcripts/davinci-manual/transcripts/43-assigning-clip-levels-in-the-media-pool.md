---
title: "Assigning Clip Levels in the Media Pool"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 43
---

# Assigning Clip Levels in the Media Pool

When you first import media into the Media Pool, either manually in the Media page or automatically

by importing an AAF or XML project in the Edit page, Resolve automatically assigns the “Auto” Levels

setting. When a clip is set to Auto, the Levels setting used is determined based on the codec of the

source media.

DaVinci Resolve generally does a good job of figuring out the appropriate Levels setting of each

clip on its own. However, in certain circumstances, such as when you’re working with media that was

originated in one format but transcoded into another, you may find that you need to manually choose

the appropriate settings so that the levels of each clip are interpreted correctly. This can be done

using each clip’s Levels setting in the Clip Attributes window, available from the Media Pool contextual

menu in either the Media or Edit pages.

To change a clip’s Data Level setting:


Open the Media or Edit page.


Select one or more clips, then right-click one of them and choose Clip Attributes.


Click the Levels ratio button corresponding to the data level setting you want to assign,

then click OK.

TIP: If you need to change the Levels setting of a range of clips that share a unique property

such as reel name, resolution, frame rate, or file path, you can view the Media Pool by column,

and sort by the particular column that will best isolate the range of media to which you need

to make a data level assignment.

Once you change a clip’s Levels setting, that clip will automatically be reconverted based on the new

assignment. If it appears to be correct, then you’re ready to work. If it doesn’t, then you may want to

reconsider the Levels assignment you’ve made, and you should check with the person who provided

the media to find out how it was generated, captured, and exported.

So long as the Levels settings used by your clips are accurate, you should be ready to work. However,

problems can still occur based on what external video hardware you’re using with your workstation,

and how you need to deliver the finished media to your client. For this reason, there are three

additional data level settings that you can use to maintain data integrity, while at the same time seeing

the proper image as you work.

Video Monitoring Data Levels

Superficial problems may result if the settings used by your external display differ from the settings

you’re using to process data levels in Resolve. Accordingly, there is a Video/Full Level setting in the

Master Settings panel of the Project Settings (in the Video Monitoring section).

When you change this setting, the image being output to your external display should change, but the

image you see in your Viewer will not. That’s because this setting only affects the data levels being

output via the video interface connecting the Resolve workstation to your external display. It has no

effect on the data that’s processed internally by Resolve, or on the files written when you render in the

Deliver page.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

There are two options:

Video: This is the correct option to use when using a broadcast display set to the

Rec. 709 video standard (10-bit 64–940).

Full: If your monitor or projector is capable of displaying “full range” video signals, and you

wish to monitor the full 10-bit data range (4–1023) while you work, then this is the correct

option to use.

It is imperative that the option you choose in DaVinci Resolve matches the data range the

external display is set to. Otherwise, the video signal will appear to be incorrect, even though

the internal data is being processed accurately by DaVinci Resolve.

Auto/Video/Full Level

selection for monitoring

Deck Capture and Playback Data Level

There is a separate “Video/Data Level” setting that is specific to when you’re capturing from or

outputting to VTRs. This setting also affects the video signal that is output via the video interface

connecting the Resolve workstation to your VTR (which is usually also in the signal chain used for

monitoring). However, it only takes effect when you’re capturing from tape in the Media page, or

editing to tape in the Deliver page. If you never capture or output to tape, this setting will never

take effect.

This setting is found in the Deck Capture and Playback panel of the Project Settings.

The reason for a separate option for tape capture and output is that often you’d want to monitor in one

format (normally scaled Rec. 709), but output to tape in another (full range RGB 444). This way, you can

set up Resolve to accommodate this workflow, and then not have to worry about manually switching

your video interface back and forth.

There are two options:

Video: This is the correct option to use when you want to output conventional

Rec. 709 video to a compatible tape format.

Full: This is the correct option to use when you want to output “full range” RGB 444 video

to a compatible tape format.

Once tape ingest or output has finished, your video interface goes back to outputting using

the setting specified by the “Colorspace conversion uses” setting in the Master Settings panel

of the Project Settings (in the Video Monitoring section).


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Output Data Level Settings in the Deliver Page

Finally, there’s one last set of data level settings, available in the Render Settings list, within the Format

group. It’s the “Set to video or data level” drop-down menu. It’s there to give you the ability to convert

the data level of your rendered output, if necessary.

All media is output using a single data level, depending on your selection.

There are three options:

Automatic: The output data level of all clips is set automatically based on the codec you

select to render to in the “Render to” drop-down menu.

Video: All clips are rendered as normally scaled for video (10-bit 64–940).

Full: All clips are rendered as full range (10-bit 4–1019).

For most projects, leaving this setting on “Automatic” will yield the appropriate results.

However, if you’re rendering media for use by another image processing application (such as

a compositing application) that is capable of handling “full range” data, then full range output

is preferable for media exchange as it provides the greatest data fidelity. For example, when

outputting media for VFX work as a DPX image sequence, or as a ProRes 4444 encoded

QuickTime file, choosing “Unscaled full range data” guarantees the maximum available image

quality. However, it is essential that the application you use to process this media is set to read

it as “full range” data, otherwise the images will not look correct.

So, What’s the “Proper” Data Range for Output?

Strictly speaking, there is no absolutely “proper” data range to use when outputting image data.

As long as the Levels setting of each clip in the Media Pool is set to reflect how each clip was created,

your primary consideration is which data range is compatible with the media format or application

you’re delivering to. If the media format you’re exporting to supports either normally scaled or full

range, and the application that media will be imported into supports either normally scaled or full

range, then it’s really your choice, as long as everyone involved with the project understands how the

data range of the media is meant to be interpreted once they receive it.

Outputting to hardware is a bit trickier, in that you need to make sure that the external display or VTR

you’re outputting to is set up to receive a signal using the data range you’ve chosen. If the device is

limited to only one data range, then you need to be sure that you’re outputting to it using that data

range, or the levels of the image will appear to be incorrect, even though the image data being

processed by Resolve is actually fine.

Introduction to DaVinci Resolve

Color Management

How color is managed in DaVinci Resolve depends on the “Color Science” setting at the top of the

Color Management panel of the Project Settings. There are four options: DaVinci YRGB, DaVinci

YRGB Color Managed, DaVinci ACEScc, and DaVinci ACEScct. This section discusses the second

setting, DaVinci YRGB Color Managed. ACEScc and ACEScct is discussed in the following section in

this chapter.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Display Referred vs. Scene Referred Color Management

The default DaVinci YRGB color science setting, which is what DaVinci Resolve has always used,

relies on what is called “Display Referred” color management. This means that Resolve has no

information about how the source media used in the Timeline is supposed to look; you can only

judge color accuracy via the calibrated broadcast display you’re outputting to. Essentially, you are

the color management, in conjunction with a trustworthy broadcast display that’s been calibrated to

ensure accuracy.

DaVinci Resolve 12 introduced a color science option called “DaVinci YRGB Color Managed,” or

more simply “Resolve Color Management” (RCM). This introduced a so-called “Scene Referred” color

management scheme, in which you have the option of matching each type of media you’ve imported

into your project with a color profile that informs DaVinci Resolve how to represent each specific color

from each clip’s native color space within the common working color space of the timeline in which

you’re editing, grading, and finishing.

This is important, because two clips that contain the same RGB value for a given pixel may in actuality

be representing different colors at that pixel, depending on the color space that was originally

associated with each captured clip. This is the case when you compare raw clips shot with different

cameras made by different manufacturers, and it’s especially true if you compare clips recorded using

the differing log-encoded color spaces that are unique to each camera.

This Scene Referred component of color management via RCM doesn’t do your grading for you, but

it does try to ensure that the color and contrast from each different media format you’ve imported

into your project are represented accurately in your timeline. For example, if you use two different

manufacturer’s cameras to shoot green trees, recording Blackmagic Film color space on one, and

recording to the Sony SGamut3.Cine/SLog3 color space on the other, you can now use RCM to make

sure that the green of the trees in one set of clips match the green of the trees in the other, within the

shared color space of the Timeline.

It should be mentioned that this sort of thing can also be done manually in a more conventional

Display Referred workflow, by assigning LUTs that are specific to each type of media, or using

Color Space Transform Resolve FX in order to transform each clip from the source color space to

the destination color space that you require. However, RCM’s automation can make this process

faster by freeing you from the need to locate and maintain a large number of LUTs to accommodate

your various workflows. Also, the matrix math used by RCM (as well as the Color Space Transform

operation) extracts high-precision, wide-latitude image data from each supported camera format,

preserving high-quality image data from acquisition, through editing, color grading, and output. These

are all advantages when compared to lookup tables, which can have plenty of precision, but can clip

out‑of‑bounds image data and introduce issues when differing lookup table interpolation methods

cause minor inconsistencies with color space transformations from application to application.

The preservation of wide-latitude image data deserves elaboration. LUTs clip image detail that goes

outside of the numeric range they’re designed to handle, so this often requires the colorist to make a pre-

LUT adjustment to “pull back” image data in the highlights that you want to retrieve. Using RCM eliminates

this two-step process, since the input color space matrix operations used to transform the source

preserves all wide-latitude image data, making highlights easily retrievable without any extra steps.

Updated RCM In DaVinci Resolve 17

In version 17, DaVinci Resolve introduced the biggest improvements to Resolve Color Management

(RCM) since it was originally introduced, adding numerous features to simplify setup, improve image

quality, and make the “feel” of your grading controls more consistent. Specific improvements include

improved metadata management for incoming media files that support color metadata, a new wide

gamut color space suitable for using as your default Timeline working color space for any program,

a new Input Tone Mapping option (Input DRT) that makes it easier to mix media formats for SDR and

HDR grading, improved Timeline to Output Tone Mapping (Output DRT) that offers improved shadow


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

and highlight handling, and select color space-aware grading palettes that make controls feel and

perform well no matter what you’re grading.

This updated Resolve Color Management has the same name as the previous version. However, older

projects using the previous version of RCM will have Color science set to Legacy, to preserve the

older color management settings and color transformations effect on your work. For more information

on how the previous generation of RCM works, see the September 2020 version of the DaVinci

Resolve 16 Manual.

How Is DaVinci Resolve Color Management Different from ACES?

This is a common question, but the answer is pretty simple. Resolve Color Management

(RCM) and ACES are both Scene Referred color management schemes designed to solve the

same problem. However, if you’re not in a specific ACES-driven cinema workflow, DaVinci

Resolve Color Management can be simpler to use, and will give you all of the benefits of color

management, while approximating the “feel” that the DaVinci Resolve Color page controls

have always had.

Resolve Color Management for Editors

RCM isn’t just for Colorists. RCM can be easier for editors to use in situations where the source

material is log-encoded. Log-encoded media preserves highlight and shadow detail, which is great for

grading and finishing, but it looks flat and unpleasant, which is terrible for editing.

Even if you have no idea how to do color correction, it’s simple to turn RCM on in the Color

Management panel of the Project Settings, and then use the Media Pool to assign the particular

Input Color Space that corresponds to the source clips from each camera. Once that’s done, each

log-encoded clip is automatically normalized to the default Timeline Color Space of Rec. 709

Gamma 2.4. So, without even having to open the Color page, editors can be working with pleasantly

normalized clips in the Edit page.

The Input, Timeline, and Output Color Space

The foundation of Resolve Color Management rests on three core settings. Not only do you have the

ability to either automatically or manually identify the color science of each individual source clip (the

Input Color Space), but you also have explicit control over the working color space within which all

color adjustments and operations are made (the Timeline Color Space), and you have separate control

over the Output Color Space that defines how your graded image will be monitored and output.

This means that, basically, Resolve Color Management consists of two color transforms working

together, converting each source clip via its Input Color Space definition into the Timeline Color Space

in which you work, and then converting the adjusted image from the Timeline Color Space to whatever

Output Color Space you require to deliver the project.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Input Color Space

Timeline Color Space

Output Color Space

Resolve Color Management consists of three color transforms working together.

This means that, as a colorist, you can set the Timeline Color Space that you’re working in to whatever

you prefer. If you prefer grading wide-gamut log media because you like the way the grading controls

behave in that color space, you can set the Timeline Color Space in the Color Management panel of

the Project Settings to DaVinci Wide Gamut (more on this below), or any of the available log formats,

including ARRI Log C, REDWideGamutRGB/Log3G10, and Cineon Film Log. If you instead prefer

grading in the Rec. 709 color space because you’re mastering a standard dynamic range (SDR)

program to Rec. 709 and you’re more comfortable with how the controls in DaVinci Resolve have

always felt in that color space, you can choose that instead. Whatever Timeline Color Space you

assign is what all source clips will be transformed to for purposes of making grading adjustments in the

Color page, so you can make this choice using a single setting.

A key benefit of the color space conversions that RCM applies is that no image data is ever clipped

during the Input to Timeline color space conversion. For example, even if your source is log‑encoded

or in a camera raw format, grading with a Rec. 709 Timeline Color Space does nothing to clip or

otherwise limit the image data available to the RCM image processing pipeline. All image values

greater than 1.0 or less than 0.0 are preserved and made available to the next stage of RCM

processing, the Timeline to Output color space conversion.

Consequently, if you’re grading in a color space other than the one you need to output to, you don’t

have to worry about data loss during the color transformation back to the color space you actually

want to output to. The Output Color Space setting gives you the freedom to work using whatever

Timeline Color Space you like while grading, with Resolve automatically converting your output to the

specific color space you want to monitor with and deliver to. And thanks to the precision of the image

processing in DaVinci Resolve, you can convert from a larger color space to a smaller one and back

again without clipping or a loss of quality. Of course, if you apply a LUT or use Soft Clip within a grade,

then clipping will occur, but that’s a consequence of using those particular operations.

TIP: If you want to use Resolve Color Management, but you want the Input and Output Color

Spaces to match whatever you set the Timeline Color Space to, you can choose “Bypass” in

the “Input Colorspace” and “Output Colorspace” drop-down menus.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Finally, it is the Output Color Space that determines the final color space of your rendered result. While

no image data is clipped during the Source to Timeline color space conversion, image data will be

clipped during the Timeline to Output color space conversion in order for the final image to conform to

the color space being rendered and output, unless you use the Gamut Mapping options to compress

image data during the Timeline to Output Color Space conversion.