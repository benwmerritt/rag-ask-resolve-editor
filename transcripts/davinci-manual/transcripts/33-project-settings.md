---
title: "Project Settings"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 33
---

# Project Settings

These parameters let you choose the color science, white balance color space, gamma, and other

visual settings guiding how the image will be transformed to suit your program and RCM.

�Color Science: Lets you choose what version of camera color science you want to use to

decode .braw media.

Camera Metadata: Chooses whichever version of color science was selected by

the camera at the time of shooting.

Gen 4: The original version of color science available for recording and decoding .braw media.

Gen 5: A newer more film-like curve designed for better skin tones and high

contrast/saturation color response.

�White Balance: The first seven options offer White Balance presets, which automatically adjust

the Color Temp and Tint parameters. These options include: Daylight, Cloudy, Shade, Tungsten,

Fluorescent, and Flash. An eighth option, Custom, makes the Color Temp and Tint parameters

user-adjustable. The default is As Shot.

�Color Space: Debayering .braw data requires choosing a color space to convert the raw signal

into. Bear in mind that the color space you choose is merely a starting point for further correction.

There is no requirement that you choose one or the other color space for any given workflow,

and all settings will yield high-quality image data suitable for further color correction. You should

choose the color space that provides the most pleasing starting point for your particular project.

Blackmagic Design: A wide gamut color space designed for digital cinema workflows on

Blackmagic Design cameras.

Rec. 709: Decodes into the standard color space specified by the Rec. 709 standard for high

definition video. While you may find this option useful as a starting point, it is not required for

programs being output to video.

Rec. 2020: Decodes into the standard color space specified by the Rec. 2020 standard for high

definition video, UHD video, and beyond. While you may find this option useful as a starting point,

it is not required for programs being output to video.

DCI-P3 D65: Decodes RGB-encoded image data with a D65 white point, intended for monitoring

with a P3-compatible display.

DCI-P3 Theater: A setting designed for adaptive viewing of DCI-P3 in a theater with a projector

using a D60 white point.

CIE 1931 XYZ D65: A specialty setting for outputting to an XYZ color space with a

D65 adaptive white point.

CIE 1931 XYZ D50 (PCS): A specialty setting for outputting to an XYZ color space with a

D50 adaptive white point, as used by the profile connection space of the DNG image format.

�Gamma: There are several options available for choosing a gamma profile to be used when

debayering .braw media. Which one is best really depends on how you like to work, as all will

yield high-quality image data without clipping the signal internally within DaVinci Resolve’s image

processing pipeline. Even though some of these options will produce a range of image data that

will clip on output, all of that image data is preserved “under the hood” and can be used and

retrieved in your grade.

Blackmagic Design Film: A log-encoded “film workflow” oriented option that’s specifically

designed for version 4 of the Blackmagic Design color science. This option is designed to fit the

maximum amount of information from wide latitude BMD cameras into the data range of 0–1023.

Using this setting provides all the dynamic range from the source media into a signal that can

be transcoded to other formats with no compromise. However, this is not a viewable image and

requires grading to normalize it into an image that can be delivered to audiences.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

Blackmagic Design Video:  The standardized gamma curve for standard-dynamic-range HD

and UHD display. For wide-latitude images, highlights will be clipped, but all image data will be

preserved internally for retrieval via grading as necessary.

Blackmagic Design Extended Video: An SDR-compatible gamma curve similar to the above but

with compressed highlights that preserve more highlight detail in the visible range of the image.

Intended to be a fast starting point for grading SDR images. Fewer highlights are clipped, but

nonetheless all image data is preserved internally for retrieval via grading as necessary.

Blackmagic Design Custom: For specialty workflows.

Linear: A scene linear setting, suitable for visual effects and specialty workflows.

Rec. 2100 Hybrid Log Gamma: The standardized gamma curve for the HLG standard of

high‑dynamic-range (HDR) video jointly developed by the BBC and NHK.

Rec. 2100 ST2084 (PQ): The standardized gamma curve for high-dynamic-range (HDR) video as

encoded by Dolby Vision and HDR10+. Also referred to as the PQ curve.

�Highlight Recovery: A checkbox that lets you include additional highlight sensor data that’s

usually clipped by the standard decoding matrix. In cases where you have extremely clipped

peak highlights, you may obtain additional image detail this way, although it may contain unusual

color artifacts.

�Gamut compression: Prevents monochromatic highly saturated light sources (LEDs, neon

signs, etc.) from clipping the gamut.

�Apply LUT: Applies color metadata to the BRAW file from the selected LUT source.

�LUT source: Choose the color metadata from the sidecar file, or the metadata

embedded in the clip.

�Saturation: Adjusts the color intensity of the image. 1 is unity. The range is 0 (desaturated)

through +4 (extremely high).

�Contrast: Increases contrast by raising the top of the signal and lowering the bottom of the signal

about the Midpoint slider (described below). Raising this value increases contrast, while lowering

this value lowers contrast. 1 is unity. The range is 0 (minimum contrast) to +2 (maximum contrast).

�Midpoint: The level about which contrast is either expanded or contracted. 0.41 is unity.

The range is 0 (black) to +1 (maximum white).

�Highlight Rolloff: Makes it easy to selectively retrieve blown-out highlight detail in high-dynamic-

range media by lowering this parameter and achieves a smooth blend between the retrieved

highlights and the unadjusted midtones for a naturalistic result. 1 is unity. The range is 0 (minimum)

through +2 (maximum).

�Shadow Rolloff: Lets you selectively lighten or darken shadow detail. Raising this value

retrieves shadow detail recorded below 0 percent while leaving the midtones alone. 1 is unity.

The range is 0 (minimum) through +2 (very high).

�White Level: A gain setting for adjusting the highlights.

�Black Level: A lift setting for adjusting the shadows.

�Use Video Black Level: A legacy video setting that adds pedestal to the video signal. For people

using video equipment dating from when shoulder pads were cool.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

Use Camera Metadata

The most elemental camera metadata settings for exposure and color that are available. Deselect the

Use Camera Metadata checkboxes to activate the controls.

�Exposure: Increases or lowers image lightness in units relative to ƒ-stops. If your intended

exposure adjustment lifts image data above the maximum white level, don’t worry; all image data

is preserved and can be retrieved in subsequent adjustments. 0 is unity. The range is –5 to +5.

�Color Temp: Only available when White Balance is set to something other than As Shot. Designed

to alter the “warmth” of the image. Adjustable in Kelvin. Lower values correct for “warmer” lighting,

while higher values correct for “cool” lighting. +5500 is unity. The range is +2000 to +50,000.

�Tint: Only available when White Balance is set to something other than As Shot. Designed to alter

the green to magenta balance of the image, for images with fluorescent tinting. Lower values add

green to compensate for magenta lighting, while higher values add magenta to compensate for

green lighting. 0 is unity. The range is –150 to +150.

BRAW Files and Blackmagic Design Film

Blackmagic Design’s logarithmically encoded Blackmagic Design Film gamma setting,

which produces flat-contrast, wide-gamut image data that preserves image detail with a

wide latitude for adjustment, is a modified version of the standard Cineon curve. However,

the modifications are designed to emphasize the strengths of the sensors used by the

Blackmagic Design cameras. Similarly to working with clips using Cineon, the ARRI

ALEXA’s Log-C gamma, or Sony’s proprietary S-Log or S-Log2 formats, you need to

normalize clips using Blackmagic Design Film by using Resolve Color Management (RCM), by

making a manual adjustment to color and contrast, or by applying a LUT, using techniques

discussed previously.

Canon RAW

Canon RAW (CRW) is produced by a variety of Canon cameras.

Master Settings

These parameters let you choose the decode quality and method that raw clips will be transformed to

use when debayered.

�Decode Quality: Lets you debayer Canon RAW files at Full, Half, or Quarter resolution to improve

performance on slower systems. Lower resolution media is lower quality but faster to work with

and process. If necessary, you can choose a lower resolution setting that provides better real time

playback on systems with limited performance while you work, and then switch to a higher quality

when rendering the final output. A “Force debayer res to highest quality” checkbox in the Render

Settings list of the Deliver page makes it easy to follow this workflow.

�Decode Using: The option you select determines whether all Canon RAW media throughout the

project is decoded using the original Camera Metadata settings (the default selection), using

Project settings in which you choose custom settings to be applied to all clips, or using the Canon

RAW default settings.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

Project Settings

Canon RAW has a variety of settings that can be adjusted to alter the image quality of the debayered

result. The Color Temp and Tint parameters are only available if the White Balance drop-down menu is

set to Custom.

�White Balance: The first seven options offer White Balance presets, which automatically adjust

the Color Temp and Tint parameters. These options include Daylight, Cloudy, Shade, Tungsten,

Fluorescent, and Flash. An eighth option, Custom, makes the Color Temp and Tint parameters

user-adjustable.

�Color Space: Choose Canon Cinema Gamut or other common colorspaces.

�Gamma: Choose a Canon Log version or Rec 709.

�Sharpness: A debayer-specific sharpness filter applied to provide the appearance of enhanced

image detail. 20 is unity. The range is 0 to 100.

�Highlights: Makes it easy to selectively retrieve blown-out highlight detail in high-dynamic-range

media by lowering this parameter and achieves a smooth blend between the retrieved highlights

and the unadjusted midtones for a naturalistic result. 0 is unity. The range is –100 (minimum)

through +100 (maximum).

�Shadows: Lets you selectively lighten or darken shadow detail. Raising this value retrieves

shadow detail recorded below 0 percent, while leaving the midtones alone. 0 is unity. The range is

–100 (minimum) through +100 (very high).

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

�Lift: Adjusts the black point of the media, raising it or lowering it while scaling all midtone values

between it and the white point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. The range is –100 to +100.

�Gain: Adjusts the white point of the media, raising or lowering it while scaling all midtone values

between it and the black point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

�Contrast: Raising contrast reduces shadows and raises highlights, while leaving midtones at 50

percent unaffected. Regardless of how you adjust this control, all image data is preserved and can

be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

Use Camera Metadata

The most elemental camera metadata settings for exposure and color that are available.

�Exposure: Increases or lowers image lightness in units relative to ƒ-stops. If your intended

exposure adjustment lifts image data above the maximum white level, don’t worry; all image data

is preserved and can be retrieved in subsequent adjustments. 0 is unity. The range is –5 to +5.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

�Color Temp: Only available when White Balance is set to something other than As Shot. Designed

to alter the “warmth” of the image. Adjustable in Kelvin. Lower values correct for “warmer” lighting,

while higher values correct for “cool” lighting. +6500 is unity. The range is +2000 to +50,000.

�Tint: Only available when White Balance is set to something other than As Shot. Designed to alter

the green to magenta balance of the image, for images with fluorescent tinting. Lower values add

green to compensate for magenta lighting, while higher values add magenta to compensate for

green lighting. 0 is unity. The range is –150 to +150.

CinemaDNG

CinemaDNG is an open format capable of high-resolution raw image data with a wide dynamic range

and is one of the formats recorded by the Blackmagic Design Camera when you shoot in raw mode.

CinemaDNG images are decoded with full dynamic range when the Highlight Recovery checkbox

is selected.

DaVinci Resolve version 11.2.1 introduced improved debayering for raw CinemaDNG media acquired

using any of the Blackmagic Design cameras. The “Apply Pre Tone Curve” setting controls whether

you’re using the older debayering method (when turned on) or the newer, visually improved

debayering method (when turned off).

Master Settings

These parameters let you choose the decode quality, white balance, color space, and gamma that raw

CinemaDNG clips will be transformed to use when debayered.

�Decode Quality: Lets you debayer CinemaDNG raw files at Full, Half, or Quarter resolution to

improve performance on slower systems. Lower resolution media is lower quality but faster to

work with and process. If necessary, you can choose a lower resolution setting that provides

better real time playback on systems with limited performance while you work, and then switch

to a higher quality when rendering the final output. A “Force debayer res to highest quality”

checkbox in the Render Settings list of the Deliver page makes it easy to follow this workflow.

�Decode Using: The option you select determines whether all CinemaDNG media throughout

the project is decoded using the original Camera Metadata settings (the default selection), using

Project settings in which you choose custom settings to be applied to all clips, or using the

CinemaDNG default settings.

�Apply Pre Tone Curve: When this checkbox is turned off (the default for new projects created

in DaVinci Resolve 11.2.1 or later), DaVinci Resolve debayers CinemaDNG raw media using an

improved method that delivers better-looking results, specifically for media acquired using any

of the Blackmagic Design cameras. When this checkbox is turned on (the default for projects

created in earlier versions of DaVinci Resolve), the older debayering method is reenabled for

backward compatibility. However, turning Pre Tone Curve on may also provide better results for

CinemaDNG raw files coming from other sources. If you’re importing .dng media from cameras

other than those from Blackmagic Design, you should try both settings to see which type of

debayering you prefer.

�Apply Soft Clip: This checkbox is only available when Apply Pre Tone Curve is turned off. When

turned on, high dynamic range parts of the signal (super-white highlights) are brought back into

the picture as visible image detail you can adjust, similar to using the Highlights control to retrieve

these otherwise clipped parts of the signal.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA