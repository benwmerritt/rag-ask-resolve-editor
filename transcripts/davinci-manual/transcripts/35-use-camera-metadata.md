---
title: "Use Camera Metadata"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 35
---

# Use Camera Metadata

The most elemental camera metadata settings for exposure and color that are available.

�Color Temp: Only available when White Balance is set to something other than As Shot. Designed

to alter the “warmth” of the image. Adjustable in Kelvin. Lower values correct for “warmer” lighting,

while higher values correct for “cool” lighting. +6500 is unity. The range is +2000 to +50,000.

�Tint: Only available when White Balance is set to something other than As Shot. Designed to alter

the green to magenta balance of the image, for images with fluorescent tinting. Lower values add

green to compensate for magenta lighting, while higher values add magenta to compensate for

green lighting. 0 is unity. The range is –150 to +150.

Phantom Cine

The Phantom line of high-speed digital cinema cameras record wide latitude, high-gamut media

using the Cine Raw format.

Master Settings

These parameters let you choose the decode quality, white balance, color space, and gamma that raw

Phantom Cine clips will be transformed to use when debayered.

�Decode Using: The option you select determines whether all Phantom Cine media throughout

the project is decoded using the original Camera Metadata settings (the default selection), using

Project settings in which you choose custom settings to be applied to all clips, or using the Cine

default settings.

�Timecode: There are four types of timecode that Phantom Cine files can be set to use:

Set to zero: Camera timecode is ignored, instead using a simple frame count with

the first frame considered 0.

Time of day (Local): Time of day timecode recording.

Time of day (GMT): Time of day timecode recording based on Greenwich Mean Time.

SMPTE: Standard SMPTE timecode.

Project Settings

The following settings for exposure, color, and sharpness are available.

�Gamma: Three options are available for setting the gamma of the debayered output:

�Rec. 709

�Log 1

�Log 2


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

�Lift: Adjusts the black point of the media, raising it or lowering it while scaling all midtone values

between it and the white point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. The range is –100 to +100.

�Gain: Adjusts the white point of the media, raising or lowing it while scaling all midtone values

between it and the black point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

�Contrast: Raising contrast reduces shadows and raises highlights, while leaving midtones at

50 percent unaffected. Regardless of how you adjust this control, all image data is preserved and

can be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

�Sharpness: A debayer-specific sharpness filter applied to provide the appearance of enhanced

image detail. 20 is unity. The range is 0 to 100.

�Highlights: Makes it easy to selectively retrieve blown-out highlight detail in high-dynamic-range

media by lowering this parameter and achieves a smooth blend between the retrieved highlights

and the unadjusted midtones for a naturalistic result. 0 is unity. The range is –100 (minimum)

through +100 (maximum).

�Shadows: Lets you selectively lighten or darken shadow detail. Raising this value retrieves

shadow detail recorded below 0 percent, while leaving the midtones alone. 0 is unity.

The range is –100 (minimum) through +100 (very high).

�Color Boost: Lets you naturalistically raise the saturation of regions of low saturation, sometimes

referred to as a vibrance operation. Can be used also to lower the saturation of regions of low

saturation. 0 is unity. The range is –100 (minimum) through +100 (very high).

�Saturation: Adjusts the color intensity of the image. 0 is unity. The range is –100 (minimum)

through +100 (very high).

�Midtone Detail: When this parameter is raised, the contrast of regions of the image with high edge

detail is raised to increase the perception of image sharpness, sometimes referred to as definition.

When this parameter is lowered to a negative value, regions of the image with low amounts of

detail are softened while areas of high detail are left alone. 0 is unity. The range is –100 (minimum)

through +100 (very high).

RED

R3D source media, recorded by the various models of RED DIGITAL CINEMA cameras, contains one

of the most elaborate sets of raw parameters of any of the camera formats. These settings are divided

into four different groups.

Master RED Settings

The Master RED settings are the most important, handling decode quality and the control governing

whether the original camera metadata is used, or if you’re overriding the camera metadata project-

wide with custom settings.

These settings also contain the drop-down menus that let you choose the color space and gamma

curve used to transform the raw image data into image data for processing in DaVinci Resolve when

debayering R3D clips. Which Color Space and Gamma Curve settings you use are solely a matter of

preference; there is no absolute requirement to use one or the other for any given type of workflow.

You’re simply looking for settings that provide the best starting point for the media you have, given the

type of grading you’re looking to do.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

For example, in many cases combining the REDcolor3 Color Space setting and REDlog Film gamma

curve will offer a starting point that retains the most image detail with the greatest latitude for

adjustment. On the other hand, if you’re working in a hurry, for example to generate dailies for offline

editing, using one of the REDcolor Color Space settings with one of the REDgamma settings can

offer an image that’s more immediately pleasing and that requires fewer adjustments to achieve

an acceptable result. These are not recommendations, they’re only examples. As always, the ideal

settings for your project depend heavily on the quality of the source media, so you should experiment

with media from your own projects to find the most suitable results to your eye.

Master

These top settings determine the image quality that you’re choosing to extract from the R3D source

media. The tradeoff is that higher quality media at higher resolution will be more processor-intensive

to debayer, depending on your workstation’s capabilities.

�Decode Quality: Determines the image quality of the decoded R3D data that’s handed off to

the DaVinci Resolve image processing pipeline. The Decode Quality you select has a direct

impact on real time performance. Decoding performance depends entirely on the hardware

capabilities of your system.

On the most modern systems, R3D files can be decoded using accelerated GPU-based

debayering if you set the Use GPU for R3D drop-down menu to Debayer in the Decode Options

panel of the DaVinci Resolve System Settings. DaVinci Resolve 16.1.2 introduced the latest RED

API-enabling 8K-accelerated debayering using Cuda. Otherwise, R3D files can be decoded with

high performance using multi-core CPU processing if your workstation has fast enough CPUs.

If necessary, you can also choose a lower quality setting that provides better real time playback

on systems with limited performance while you work, and then switch to a higher quality when

rendering the final output. A “Force debayer res to highest quality” checkbox in the Render

Settings list of the Deliver page makes it easy to follow this workflow.

�Bit Depth: DaVinci Resolve can decode R3D files with 8-, 10-, or 16-bit image data for processing.

Choosing 16-bit for maximum quality may impact playback performance on some hardware.

�Timecode: The timecode recorded for R3D media depends on the camera setting in use when it

was shot. There are three choices:

Camera: This setting automatically selects between Absolute and Edge depending on what was

chosen as the default timecode mode on the camera. This setting needs to be selected before

you add R3D media to the Media Pool. If you’re browsing R3D media when you change this

setting, you should refresh the folder in the Library of the Media Pool before adding media to the

Media Pool.

Absolute: The default. Records “time of day” timecode. If an external timecode source was

connected and the camera was put into Jam Sync mode, the external timecode would have been

recorded instead.

Edge: The first recorded clip for each magazine starts at 01:00:00:00, and the timecode of each

subsequent clip is recorded sequentially and continuously.

�Decode Using: The option you select determines whether all R3D media throughout the project is

decoded using the original Camera Metadata settings (the default selection), using Project settings

in which you choose custom settings to be applied to all clips, or using the RED default settings.

Project Settings

These settings control the fundamental methods used to debayer R3D media. The selections you

make to these settings determine the basic color and contrast that you’re choosing to extract from the

camera raw image data.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

�Color Science: The options are Original, which was the color science used by early builds of the

REDone camera, Version 2, and IPP2, which is the current version of color science used by the

entire RED camera line. Unless you need to match the look of older projects using the older color

science, the newest color science is generally preferable.

�Color Space: Because RED cameras record R3D data which uses a raw color space, debayering

the native R3D data requires choosing a color space to convert the raw signal into. Bear in mind

that the color space you choose is merely a starting point for further correction. There is no

requirement that you choose one or the other color space for any given workflow. You should

choose the color space that provides the most pleasing starting point for your particular project.

DragonColor2: A further optimized version of DragonColor that is especially recommended for

underwater footage.

REDcolor4: A further optimized version of REDcolor3 that is especially recommended

for underwater footage.

REDWideGamutRGB: Part of RED’s IPP2 (image processing pipeline 2) initiative; this is a camera

color space designed to encompass all colors that can be recorded by RED cameras without

clipping, and is meant to provide a single common starting point for all models of RED cameras, for

convenient grading to HDR or SDR workflows.

Rec. 2020: Decodes into the standard color space specified by the Rec. 2020 standard for high

definition video, UHD video, and beyond. While you may find this option useful, it is not required

for programs being output to video.

Rec. 709: Decodes into the standard color space specified by the Rec. 709 standard for high

definition video. While you may find this option useful, it is not required for programs being

output to video.

sRGB: Decodes into the standard color space defined by the sRGB standard, typically used for

computer display.

Adobe1998: Decodes into Adobe’s unique version of the sRGB standard.

DCI-P3: Decodes to an RGB-encoded image data with a D61 white point, intended for use when

outputting media for DCI mastering.

DCI-P3 D65: Decodes RGB-encoded image data with a D65 white point, intended for monitoring

with a P3-compatible display.

ProPhoto RGB: A color space developed by Kodak that offers a large gamut intended for

photography. An idiosyncrasy of this color space is that the green and blue primary points are

outside the boundaries of visible color, meaning this gamut encompasses “imaginary” colors in

order to achieve an extremely large gamut.

CameraRGB: Outputs the original, unmodified sensor data. Not a recommended setting.

REDspace: Fits the raw R3D image data into a color space thatʼs larger than that of Rec. 709.

Appropriate for digital cinema mastering and film output. REDspace was the predecessor to the

REDcolor setting.

REDcolor: A color space thatʼs similar to the Rec. 709 option, but modified to balance accuracy

with pleasing color rendition, emphasizing accurate skin tones.

REDcolor2: Similar, but less saturated than, REDcolor.

REDcolor3: Similar saturation to REDcolor, but with additional modifications to improve the

color rendition of skin tone. Introduced as the optimum color space for Epic cameras, but also

appropriate for previous generations of RED cameras.

DragonColor: A color space optimized for cameras with the RED Dragon sensor, although this

color space can be used for previous generations of RED cameras as well.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

�Gamma Curve: There are several options available for choosing a gamma profile to be used when

debayering the raw R3D data:

REDgamma4: The latest iteration of the REDgamma curve, designed to give a good in-camera

look without the need for grading, while retaining great dynamic range and highlight handling.

REDgamma4 is suitable for all RED cameras.

REDlog Film: An improved logarithmic gamma setting that’s designed to remap the original 12-bit

R3D data to the standard Cineon gamma curve. This setting produces flat-contrast image data that

preserves image detail with a wide latitude for adjustment, and is compatible with log workflows,

including those intended for film output.

Linear: No gamma adjustment is made, this is a linear-to-light representation of data from the RED

camera’s sensor.

Rec. 709: A gamma curve typical for Rec. 709 display. Does not provide an abundance of latitude

for grading.

Gamma 2.4: A simple power-function gamma setting commonly used for broadcast.

Gamma 2.6: A simple power-function gamma setting commonly used for digital cinema projection.

sRGB: Similar gamma setting to that employed by Rec. 709.

HDR ST.2084: The standardized gamma curve for high-dynamic-range (HDR) video. Also referred

to as the PQ curve.

Hybrid Log Gamma: The standardized gamma curve for the HLG standard of high-dynamic-range

(HDR) video jointly developed by the BBC and NHK.

BT.1886: The standardized gamma curve for standard-dynamic-range HD and UHD display. Does

not provide an abundance of latitude for grading.

Log3G12: An expanded option for RED’s IPP2 (image processing pipeline 2) initiative, this is a wide

dynamic range log space designed to encode camera data from all RED models to a common

starting point in RWG color space for convenient grading to HDR or SDR workflows. Log3G12

provides 12 stops of dynamic range above mid gray, 2 more stops than Log3G10. However, this is

at the expense of a slight loss of precision.

Log3G10: Part of RED’s IPP2 (image processing pipeline 2) initiative, this is a wide dynamic range

log space designed to encode camera data from all RED models to a common starting point in

RWG color space for convenient grading to HDR or SDR workflows. 3G represents the mapping of

18% mid gray to 1/3, and 10 represents the 10 stops of dynamic range above mid gray this supports.

PDlog 685: A logarithmic gamma setting that maps the native 12-bit RED image data into the linear

portion of a Cineon or film transfer curve.

PDlog 985: A logarithmic gamma setting with different mappings.

Custom PDlog: A logarithmic gamma setting that exposes user adjustable Black Point, White

Point, and Gamma PDlog parameters so you can customize your own log gamma curve.

REDspace: Similar to Rec. 709, but slightly altered to be more appealing, primarily through higher

contrast and lighter midtones. The predecessor to the REDgamma curve.

REDlog: A logarithmic gamma setting that maps the original 12-bit R3D image data to a 10-bit

curve. The blacks and midtones occupying the lowest 8 bits of the video signal maintain the

same precision as in the original 12-bit data, while the highlights that occupy the highest 4 bits

are compressed. While reducing the precision of highlight detail, the tradeoff is that there’s an

abundance of precision throughout the rest of the signal. This is a good setting for maintaining

maximum latitude.

REDgamma: An improved gamma curve designed to be perceptually appealing on displays

calibrated for Rec. 709, with an improved soft roll-off in the highlights to maintain highlight detail

while grading.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

REDgamma2: Similar to REDgamma, with higher contrast.

REDgamma3: The most recent iteration of the REDgamma curve. Based on a log starting

point, but with a pleasing “ready to view” contrast curve applied, designed to be a visually

pleasing starting point that maintains excellent dynamic range. REDgamma3 is also designed to

work with REDcolor3.

�Blend Type: Works to control how RED HDRX media is used. When using either Simple or Magic

Motion to blend HDRX exposures, there’s no need to use the second output in the Node Editor.

You can choose from three options:

None: Only the regular exposure is used.

Simple: Blends the two HDRX exposures to achieve a pleasing middle ground.

Magic Motion: Uses a proprietary algorithm to combine the dual exposures to combine

overexposed and well-exposed regions of the picture in a more targeted fashion, while blending

the sharpness of the regularly exposed source with the motion blur of the underexposed source.

�Blend Bias: Lets you adjust how much of the regular exposure and how much of the

underexposure are combined.

�Apply Metadata Curves: If the R3D media files were preprocessed in REDCINE X Pro, and saved

with color curve metadata, you can use this setting to either use or discard that metadata.

�D.E.B. (Dragon Enhanced Blacks): A checkbox that enables the elimination of red noise in RED

cameras using the Dragon sensor.

�Embedded Audio: Enables embedded audio in R3D media.