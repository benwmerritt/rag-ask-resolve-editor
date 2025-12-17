---
title: "Decoder Settings"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 36
---

# Decoder Settings

This second group of settings contains additional controls for finessing the debayering of RED

raw image data. Which controls are exposed depends on which Color Science setting is selected

above. Many of the settings in this group are color correction adjustments, some of which resemble

analogous controls in the Color page. However, the FLUT and DRX controls manage the exposure of

the debayered media being fed to the DaVinci Resolve image processing pipeline, and so can be used

to retrieve image detail from R3D source media in cases where the default settings are clipping or

crushing detail in the highlights or shadows that would be unavailable to DaVinci Resolve as a result.

�De-noise: Applies image-wide noise reduction. There are seven settings available, from mild to

maximum, that you can use to balance noise reduction against any possible image degradation.

�OLPF Compensation: (color science versions 1 and 2) OLPF compensation applies a low pass filter

to reduce color moiré. There are four options: Off (the default), Low, Medium, and High.

�Image Detail: (color science versions 1 and 2) Controls the demosaicing algorithm that’s used for

the software decoding of R3D media. You can choose a level of sensor detail extraction: Low,

Medium, and High (recommended). If you’re using a RED ROCKET card, this setting is ignored as

there is a fixed algorithm that’s used.

�FLUT: (color science versions 1 and 2) A gain operation that lets you boost or attenuate the ISO in

smaller increments. 0 is unity. The range is –8 to +8.

�Contrast: Raising contrast reduces shadows and raises highlights, while leaving midtones at

50 percent unaffected. The image is compressed rather than clipped at the limits of 100 and 0

percent. 0 is unity. The range is –1 to +1.

�Saturation: (color science versions 1 and 2) Adjusts the color intensity of the image. 1 is unity.

The range is 0 (minimum) through 5.0 (very high).

�DRX: (color science versions 1 and 2) A Dynamic Range control (X) that lets you recover highlights

while taking into account Color Temperature (degrees Kelvin) and Tint. 0 is unity, and 1.0 is the

maximum value.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

�Shadow: (color science version 1 and 2) Provides control over the toe (low range) of the

FLUT adjustment. 0 is unity. The range is –2 to +2.

�Brightness: Adjusts image lightness. Image data is compressed rather then clipped at

100 and 0 percent. 0 is unity. The range is –10 to +10.

�Flashing pixel adjust: A setting to apply noise reduction for removing or minimizing any flashing

pixels recorded from the sensor. Levels are: None, Low, Medium, and High.

Three additional parameters are available for IPP2 workflows, but they only function when DaVinci

Resolve is set to use DaVinci YRGB Color Managed color science and the Timeline to Output Gamut

Mapping in the Color Management panel of the Project Settings is set to RED IPP2 Gamut Mapping.

These controls (which are also mirrored in the Color Management panel when enabled) are designed

to let you tone map wide gamut media that’s being graded to a smaller gamut, such as Rec. 709.

The RED IPP2 Gamut Mapping controls that appear in the Color Management tab of the Project Settings

�Output Tone Map: (color science IPP2) Provides an easy setting for setting the resulting contract

when tone mapping wide dynamic range images to standard dynamic range (SDR) output. Settings

are: None, Low, Medium, and High. Low results in less contrast; High results in more contrast.

�Highlight Roll Off: (color science IPP2) Five settings let you adjust how much to roll off the

highlights to fit within the current gamut. These are: None, Hard, Medium, Soft, and Very Soft. Hard

provides a minimum of roll-off; Very Soft provides a maximum of roll-off. This setting interacts with

the HDR Peak Nits slider below.

�HDR Peak Nits: (color science IPP2) Adjusts the amount of highlight compression that’s done by

Highlight Roll Off.

Use Camera Metadata

The most elemental camera metadata settings for exposure and color that are available.

�ISO: A gain operation that keeps the black point at 0 while raising or lowering the white point

of the image, linearly scaling everything in between. Raising the ISO results only in boosted

highlights being more compressed; no clipping will occur. 320 is unity. The range is 50–6400.

�Exposure Adjust: Increases or lowers image lightness in units relative to ƒ-stops. Using exposure

to boost the image beyond 100 or to lower it below 0 will clip, not compress, the image data that’s

passed along to the DaVinci Resolve image processing pipeline. 0 is unity. The range is –7 to +7.

�Color Temp: Designed to alter the “warmth” of the image while keeping white elements of the

scene looking neutral. Adjustable in degrees Kelvin. Lower values correct for “warmer” lighting,

while higher values correct for “cool” lighting. This parameter is designed specifically to adjust

RED linear light image data to make the most photometrically accurate correction. 5600 is unity.

The range is 1700 to 10,000.

�Tint: Color balance correction for images with a green or magenta color cast, such as fluorescent

or sodium vapor bulbs. This parameter is designed specifically to adjust RED linear light image

data to make the most photometrically accurate correction. 0 is unity. The range is –100 to +100.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

Sony RAW

Sony makes several digital cinema cameras, such as the F65 and F55, that record wide latitude, high-

gamut media either using Sony’s 12-bit SR codec, or as 16-bit raw media files. Since Sony’s cameras do

not use a traditional Bayer pattern, special debayering is necessary when working with F65 raw media,

and the image data is demosaiced using the following raw controls and parameters.

Master Settings

These parameters let you choose the decode quality, white balance, color space, and gamma that

Sony raw clips will be transformed to use when debayered.

�Decode Quality: Determines the image quality of the decoded Sony raw data that’s handed off to

the DaVinci Resolve image processing pipeline regardless of the Play Quality setting. The Decode

Resolution you select has a direct impact on real time performance, and decoding performance

depends entirely on the hardware capabilities of your system.

If necessary, you can choose a lower resolution setting that provides better real time playback

on systems with limited performance while you work, and then switch to a higher quality when

rendering the final output. A “Force debayer res to highest quality” checkbox in the Render

Settings list of the Deliver page makes it easy to follow this workflow.

�Decode Using: The option you select determines whether all F65 media throughout the project is

decoded using the original Camera Metadata settings (the default selection), using Project settings

in which you choose custom settings to be applied to all clips, or using the Sony default settings.

Project Settings

These settings control the fundamental methods used to debayer Sony raw media. The selections you

make to these settings determine the basic color and contrast that you’re choosing to extract from the

camera raw image data.

�White Balance: The first seven options offer White Balance presets, which automatically

adjust the Color Temp and Tint parameters. These options include: Daylight, Cloudy, Shade,

Tungsten, Fluorescent, and Flash. An eighth option, Custom, makes the Color Temp and Tint

parameters user-adjustable.

�Color Space: Multiple color spaces are adjustable, depending on your intended workflow:

Rec. 709: Decodes into the standard color space specified by the Rec. 709 standard for high

definition video.

P3 D60: Decodes RGB-encoded image data with a D60 white point, intended for monitoring with

a P3-compatible display.

SGamut: Decodes into Sony’s wider S-gamut color space, designed to provide the widest range

of image data for adjustment.

SGamut3: The gamut is identical to SGamut, but color reproduction is more accurate, according to

Sony’s “Technical Summary for S-Gamut3Cine/S-Log3 and S-Gamut3/S-Log3” whitepaper.

SGamut3.Cine: According to Sony’s “Technical Summary for S-Gamut3Cine/S-Log3 and

S-Gamut3/S-Log3” whitepaper, S-Gamut3.Cine is designed to provide a more traditionally log-

encoded workflow with color reproduction that is slightly wider than the P3 gamut.

P3: Decodes to an RGB-encoded image data with a D61 white point, intended for use when

outputting media for DCI mastering.

ACES: Decodes to image data that maps to the ACES profile for the camera that was used.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

�Gamma: Five gamma settings are available, depending on what starting point you want to

use for further grading.

Gamma 2.4: A simple power-function gamma setting commonly used for broadcast.

Gamma 2.6: A simple power-function gamma setting commonly used for digital cinema projection.

Rec. 709: A gamma curve typical for Rec. 709 display.

SLog: Not designed for viewing, Sony’s SLog gammas are designed to provide a wide latitude for

grading; 14-stops according to Sony. 18% gray is at 38%.

SLog2: This version has a half stop offset from SLog to allow for a higher dynamic range.

18% gray is at 32%.

SLog3: An “easier to grade” version of SLog. 18% gray is at 40%. According to Sony’s

“Technical Summary for S-Gamut3Cine/S-Log3 and S-Gamut3/S-Log3,” SLog3 is designed to

provide a more traditionally log-encoded workflow, with a gamma curve that is similar, but not

identical, to Cineon workflows.

Linear: A simple linear gamma setting.

�Lift: Adjusts the black point of the media, raising it or lowering it while scaling all midtone values

between it and the white point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. The range is –100 to +100.

�Gain: Adjusts the white point of the media, raising or lowering it while scaling all midtone values

between it and the black point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

�Contrast: Raising contrast reduces shadows and raises highlights, while leaving midtones at 50

percent unaffected. Regardless of how you adjust this control, all image data is preserved and can

be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

�Sharpness: A debayer-specific sharpness filter applied to provide the appearance of enhanced

image detail. 20 is unity. The range is 0 to 100.

�Highlights: Makes it easy to selectively retrieve blown-out highlight detail in high-dynamic-range

media by lowering this parameter, and achieves a smooth blend between the retrieved highlights

and the unadjusted midtones for a naturalistic result. 0 is unity. The range is –100 (minimum)

through +100 (maximum).

�Shadows: Lets you selectively lighten or darken shadow detail. Raising this value retrieves shadow

detail recorded below 0 percent, while leaving the midtones alone. 0 is unity. The range is –100

(minimum) through +100 (very high).

�Color Boost: Lets you naturalistically raise the saturation of regions of low saturation, sometimes

referred to as a vibrance operation. Can be used also to lower the saturation of regions of low

saturation. 0 is unity. The range is –100 (minimum) through +100 (very high).

�Saturation: Adjusts the color intensity of the image. 0 is unity. The range is –100 (minimum)

through +100 (very high).

�Midtone Detail: When this parameter is raised, the contrast of regions of the image with high edge

detail is raised to increase the perception of image sharpness, sometimes referred to as definition.

When this parameter is lowered to a negative value, regions of the image with low amounts of

detail are softened while areas of high-detail are left alone. 0 is unity. The range is –100 (minimum)

through +100 (very high).

�Enable ICVFX: While VFX shooting in a virtual production workflow, the LED wall lighting in the

background is mixed with normal lighting for people in the foreground. Checking this box lets you

correct for that mixed lighting.

LED Wall Kelvin: Dial in the color temperature of the LED wall.

Light Blend: Specifies the mixing ratio of the normal lighting and LED wall lighting. A value of 100 is

normal lighting only (equivalent to ICVFX mode disabled). A value of 0 is the LED wall lighting only.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

Use Camera Metadata

The most elemental camera metadata settings for exposure and color that are available.

�Exposure: Increases or lowers image lightness in units relative to ASA values. If your

intended exposure adjustment lifts image data above the maximum white level, don’t worry;

all image data is preserved and can be retrieved in subsequent adjustments. +800 is unity.

The range is +1 to +65,535.

�Color Temp: Designed to alter the “warmth” of the image. Adjustable in degrees Kelvin. Lower

values correct for “warmer” lighting, while higher values correct for “cool” lighting. +6500 is unity.

The range is +2000 to +50,000.

�Tint: Only available when White Balance is set to something other than As Shot. Designed to

alter the green to magenta balance of the image, for images with fluorescent tinting. Lower values

add green to compensate for magenta lighting, while higher values add magenta to compensate

for green lighting. 0 is unity. The range is –150 to +150.

Sony Media and SLog

Sony’s proprietary SLog gamma setting, which produces flat-contrast, wide-gamut image

data that preserves image detail with a wide latitude for adjustment, is also available on some

other Sony cameras. Similarly to working with clips using the ARRI ALEXA’s Log-C gamma,

you need to normalize SLog clips by using Resolve Color Management (RCM), by making a

manual adjustment to color and contrast, or by applying a LUT, using the same techniques

discussed previously.

When applying a LUT, there are two methods that Sony recommends. A 1D LUT can be used

to transform SLog clips into the standard Cineon (or Log-C) curve if your ultimate goal is to

output Log media for film printing. If you’re planning to output to a normalized format, you can

use a dedicated LUT to make this transformation.

For more information, search the web for Sony’s document “SLog: A new LUT for digital

production mastering and interchange applications.”


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA