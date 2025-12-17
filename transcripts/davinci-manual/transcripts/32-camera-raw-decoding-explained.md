---
title: "Camera Raw Decoding Explained"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 32
---

# Camera Raw Decoding Explained

Camera raw media formats are so named because they capture raw color space data directly from the

sensor of whatever digital cinema camera did the recording. Raw image data is not human readable,

and must be debayered or demosaiced to convert the original raw data into image data that can be

handed off to DaVinci Resolve’s image processing pipeline.

Raw

Image

Data

Color Page

Image Processing

Camera Raw

Decoding

Deliver

Page Output

Raw decoding is the very first image processing operation that takes place, and it takes place before

all other operations in the Color page, before even the Source bar in the Node Editor. For this reason,

it’s important to understand that the ideal transformation of raw image data to DaVinci Resolve-friendly

image data is one that preserves the maximum amount of image data for continued processing.

Since the 32-bit floating point accuracy of DaVinci Resolve’s image processing pipeline preserves all

transformed raw data with exceptional fidelity, the Camera Raw parameters are primarily useful for

making whatever initial adjustments will produce the most optimum starting point for grading.

Each group of Camera Raw settings is available from the Raw Profile menu. This description covers the

settings that are available for each of the camera raw media formats supported by DaVinci Resolve.

Camera Raw Project Settings

The Camera Raw panel of the Project Settings contain groups of parameters that correspond to every

camera raw media format that’s supported by DaVinci Resolve. Using these parameters in the Camera

Raw panel, you can override the original camera metadata that was written at the time of recording,

and make simultaneous adjustments to all camera raw media throughout your project.

Camera Raw project settings


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

Each supported camera format has different controls that are specific to that format. These controls

are also mirrored in the Camera Raw palette in the Color page, which lets you individually adjust the

Camera Raw parameters for individual clips in a Timeline when you set Decode Using to Clip.

Camera Raw project palette in the Color page

Camera Raw Image Inspector

The Image panel in the Inspector exposes the Camera Raw parameters. If the video clip is in a Raw

format, the specific camera’s Raw controls will be exposed for user manipulation. Raw still images from

Nikon (NEF) and Canon (CR2) cameras can also be adjusted in this panel.

The Image Inspector for a Blackmagic RAW file


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

ARRI

The ARRI ALEXA can record ProRes, DNxHD, or raw image data. When shooting raw, image data is

recorded straight from the Bayer sensor, and must be debayered by DaVinci Resolve.

Master Settings

ARRI ALEXA media is extremely simple to debayer. There are only three Master settings.

�Decode Quality: Lets you debayer ARRI ALEXA raw files at Full, Half, or Quarter resolution to

improve performance on slower systems. Lower resolution media is lower quality, but faster to

work with and process. If necessary, you can choose a lower resolution setting that provides

better real time playback on systems with limited performance while you work, and then switch

to a higher quality when rendering the final output. A “Force debayer res to highest quality”

checkbox in the Render Settings list of the Deliver page makes it easy to follow this workflow.

�Decode Using: The option you select determines whether all ARRI ALEXA media throughout

the project is decoded using the original Camera Metadata settings (the default selection), using

Project settings in which you choose custom settings to be applied to all clips, or using the

ARRI default settings.

�Import Media at Open Gate Resolution: Enables DaVinci Resolve to access the “open gate” area

of clips from ALEXA cameras capable of shooting in this mode, which produces a 3.4K image with

extra area for stabilization and repositioning.

Project Settings

The following decoder settings let you adjust the color and exposure of ALEXA clips.

�Lift: Adjusts the black point of the media, raising it or lowering it while scaling all midtone values

between it and the white point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. The range is –100 to +100.

�Gain: Adjusts the white point of the media, raising or lowering it while scaling all midtone values

between it and the black point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

�Contrast: Raising contrast reduces shadows and raises highlights, while leaving midtones at 50

percent unaffected. Regardless of how you adjust this control, all image data is preserved and can

be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

�Tint: Adjusts color balance to push the image between magenta and green; useful for balancing

images with a green or magenta color cast, such as fluorescent or sodium vapor bulbs. 0 is unity.

The range is –150 to +150.

�Sharpness: A debayer-specific sharpness filter applied to provide the appearance of enhanced

image detail. 0 is unity, and 10 is the default. The range is 0 to 100.

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


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

�Saturation: Adjusts the color intensity of the image. 0 is unity. The range is –100 (minimum)

through +100 (very high).

�Midtone Detail: When this parameter is raised, the contrast of regions of the image with high edge

detail is raised to increase the perception of image sharpness, sometimes referred to as definition.

When this parameter is lowered to a negative value, regions of the image with low amounts of

detail are softened while areas of high detail are left alone. 0 is unity. The range is –100 (minimum)

through +100 (very high).

�Decode as monochrome: When this box is checked the ArriRaw footage will be decoded in black

and white only. This setting is designed to work with the Alexa Monochrome range of cameras. If

applied to normal ARRI Raw, it will simply discard the color information. RAW controls that affect

color, such as saturation and color temp, will have no effect.

Use Camera Metadata

The most elemental camera metadata settings for exposure and color that are available.

�Color Temp: Adjusts color balance to alter the “warmth” of the image. Adjustable in Kelvin. Lower

values correct for “warmer” lighting, while higher values correct for “cool” lighting. +2000 is unity.

The range is +2000 to +11,000.

�Tint: Only available when White Balance is set to something other than As Shot. Designed to alter

the green to magenta balance of the image, for images with fluorescent tinting. Lower values add

green to compensate for magenta lighting, while higher values add magenta to compensate for

green lighting. 0 is unity. The range is –12 to +12.

�Exposure: Increases or lowers image lightness in units relative to ASA values. If your

intended exposure adjustment lifts image data above the maximum white level, don’t worry;

all image data is preserved and can be retrieved in subsequent adjustments. 160 is unity.

The range is +160 to +3200.

�Finetune Red: Advanced debayer setting.

�Finetune Green: Advanced debayer setting.

�Finetune Blue: Advanced debayer setting.

ARRI Media and Log-C

ALEXA media is usually recorded using Log-C gamma and color processing, which is very

similar to the Cineon Log gamma curve, developed by Kodak to produce flat-contrast, wide-

gamut image data that preserves image detail with a wide latitude for adjustment. There is no

ALEXA raw parameter to adjust this, so for Rec. 709 monitoring and deliverables you need to

“normalize” Log-C clips in one of three ways.

You can use Resolve Color Management (RCM) to automatically normalize log-encoded media

according to the type of media it is.

You can create your own adjustment to normalize Log-C clips as part of the grading process,

using the parameters of the Color page. This approach gives you the most flexibility, as you’ll

be making custom settings that maximize the image data that’s available in every scene.

Alternately, you can use a LUT to normalize Log-C clips to obtain a fast starting point for

additional grading. Used in this way, LUTs can be applied either as an output LUT, if the entire

Timeline is nothing but ALEXA raw media, or as a LUT that’s applied to an individual node of

a grade, if you’re mixing ALEXA raw media with other formats. This provides a fast and easy

solution to linearizing ALEXA media that can be useful for creating dailies for offline editing.

However, one LUT may not be suitable for all clips. If you’re applying individual LUTs to each


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

clip, you can create multiple LUTs, each with differing contrast settings, in order to gain the

speed benefits of using LUTs, while taking into account the individual differences among clips.

ARRI has a LUT generator available online that you can use to create custom LUTs for use with

a variety of color correction applications at: https://www.arri.com/en/learn-help/learn-help-

camera-system/tools/lut-generator

Blackmagic RAW

A raw format developed by Blackmagic Design and used by a variety of Blackmagic cameras.

This format relies on the increased processing capabilities of modern cameras to perform a certain

amount of in-camera pre-processing (including noise management, sensor profiling, and edge

reconstruction) to partially de-mosaic the image and then re-encode the result, factoring in the

characteristics of the originating image sensor. The image is encoded in such a way as to later enable

typical raw controls but with efficiently compressed files (using a custom non-linear 12-bit space)

that are not computationally challenging to decode and use. BRAW media can be encoded at either

a Constant Bitrate (with variable compression of 3:1, 5:1, 8:1, and 12:1) or at Constant Quality (with a

variable bitrate).

BRAW Sidecar Metadata Files

BRAW files have been designed to accommodate descriptive metadata that enables look

management from on-set through post. This metadata is both embedded in the .braw files and

included within .sidecar files that are saved alongside the media. Metadata .sidecar files that are

present always takes precedence over the embedded metadata for purposes of decoding. However, if

there’s no .sidecar file, decoding of the .braw file falls back on the embedded metadata.

Modifying Sidecar Files

You can use the Camera Raw palette of the Color page to Update a BRAW clip’s sidecar file with

changes made to the Camera Raw settings. Click Update Sidecar to save changes, and click Export

Frame to export a one-frame image for reference.

Master Settings

These parameters let you choose the decode quality and method that raw clips will be transformed to

use when debayered.

�Decode Quality: Lets you debayer .braw files at Full, Half, Quarter, or Eighth resolution to improve

performance on slower systems. Lower resolution media is lower quality but faster to work with

and process. If necessary, you can choose a lower resolution setting that provides better real time

playback on systems with limited performance while you work, and then switch to a higher quality

when rendering the final output. A “Force debayer res to highest quality” checkbox in the Render

Settings list of the Deliver page makes it easy to follow this workflow.

�Decode Using: The option you select determines whether all .braw media throughout the project

is decoded using the original Camera Metadata settings (the default selection), using Project

settings in which you choose custom settings to be applied to all clips, or using the Blackmagic

Raw default settings.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA