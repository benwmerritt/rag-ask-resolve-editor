---
title: "Project Settings"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 34
---

# Project Settings

CinemaDNG has a variety of settings that can be adjusted to alter the image quality of the debayered

result. The Color Temp and Tint parameters are only available if the White Balance drop-down menu is

set to Custom.

�Color Science: Lets you choose what version of camera color science you want to use

to decode CinemaDNG media.

Camera Metadata: Chooses whichever version of color science was selected by

the camera at the time of shooting.

Gen 4: The original version of color science available for recording and decoding

CinemaDNG media.

�White Balance: The first seven options offer White Balance presets, which automatically

adjust the Color Temp and Tint parameters. These options include: Daylight, Cloudy, Shade,

Tungsten, Fluorescent, and Flash. An eighth option, Custom, makes the Color Temp and Tint

parameters user-adjustable.

�Color Space: Multiple color spaces are adjustable, depending on your intended workflow:

Rec. 709: Decodes into the standard color space specified by the Rec. 709 standard for high

definition video.

P3 D60: Decodes into the standard P3 color space specified by the DCI standard for digital

cinema projection.

Blackmagic Design: Decodes into a log-encoded color space that remaps the raw data into an

approximation of the Log-C standard. Choosing Blackmagic Design Film also forces the Gamma

setting to Blackmagic Design Film. This setting produces flat-contrast image data that preserves

image detail with a wide latitude for adjustment, which is suitable as a starting point for detailed

grading and is also compatible with log workflows intended for film output.

�Gamma: Five gamma settings are available, depending on what starting point you want to use for

further grading.

2.4: A simple power-function gamma setting commonly used for broadcast.

2.6: A simple power-function gamma setting commonly used for digital cinema projection.

Rec. 709: A gamma of 2.35, with a linear segment near black, approximating the EBU

recommended gamma for broadcast.

sRGB: A gamma of 2.2, with a linear segment near black, intended for reproduction on computer

displays alongside the sRGB color space.

Linear: A simple linear gamma setting.

Blackmagic Design Film: A log-encoded gamma setting that approximates Cineon encoding, the

main difference being that more data is encoded in the darkest portion of the Blackmagic Design

Film signal. When you choose this setting, the appropriate variation of gamma will be applied

based on your particular sensor, be it 4K or 4.6K.

Blackmagic Design Video: A normalized gamma setting that provides a fast starting point for

grading if you don’t want to begin with a log-encoded image.

�Highlight Recovery: A checkbox that lets you include additional highlight sensor data that’s

usually clipped by the standard decoding matrix. In cases where you have extremely clipped

highlights, you may obtain additional image detail this way, although it may contain unusual

color artifacts.

�Sharpness: A debayer-specific sharpness filter applied to provide the appearance of enhanced

image detail. 20 is unity. The range is 0 to 100.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

�Highlights: Makes it easy to selectively retrieve blown-out highlight detail in high-dynamic-range

media by lowering this parameter and achieves a smooth blend between the retrieved highlights

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

�Lift: Adjusts the black point of the media, raising it or lowering it while scaling all midtone values

between it and the white point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. The range is –100 to +100.

�Gain: Adjusts the white point of the media, raising or lowering it while scaling all midtone values

between it and the black point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

�Contrast: Raising contrast reduces shadows and raises highlights, while leaving midtones at

50 percent unaffected. Regardless of how you adjust this control, all image data is preserved and

can be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

Use Camera Metadata

The most elemental camera metadata settings for exposure and color that are available.

�Exposure: Increases or lowers image lightness in units relative to ƒ-stops. If your intended

exposure adjustment lifts image data above the maximum white level, don’t worry; all image data

is preserved and can be retrieved in subsequent adjustments. 0 is unity. The range is –5 to +5.

�Color Temp: Only available when White Balance is set to something other than As Shot. Designed

to alter the “warmth” of the image. Adjustable in Kelvin. Lower values correct for “warmer” lighting,

while higher values correct for “cool” lighting. +6500 is unity. The range is +2000 to +50,000.

�Tint: Only available when White Balance is set to something other than As Shot. Designed to alter

the green to magenta balance of the image, for images with fluorescent tinting. Lower values add

green to compensate for magenta lighting, while higher values add magenta to compensate for

green lighting. 0 is unity. The range is –150 to +150.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

CinemaDNG Files and Blackmagic Design Film

Blackmagic Design’s logarithmically encoded Blackmagic Design Film gamma setting,

which produces flat-contrast, wide-gamut image data that preserves image detail with a

wide latitude for adjustment, is a modified version of the standard Cineon curve. However,

the modifications are designed to emphasize the strengths of the sensors used by the

Blackmagic Design cameras. Similarly to working with clips using Cineon, the ARRI ALEXA’s

Log-C gamma, or Sony’s proprietary S-Log or S-Log2 formats, you need to normalize clips

using Blackmagic Design Film by using Resolve Color Management (RCM), by making a

manual adjustment to color and contrast, or by applying a LUT, using the same techniques

discussed previously.

Nikon RAW

Nikon RAW (NEF) is produced by a variety of Nikon cameras.

Master Settings

These parameters let you choose the decode quality and method that raw clips will be transformed to

use when debayered.

�Decode Quality: Lets you debayer Nikon RAW files at Full, Half, or Quarter resolution to improve

performance on slower systems. Lower resolution media is lower quality but faster to work with

and process. If necessary, you can choose a lower resolution setting that provides better real time

playback on systems with limited performance while you work, and then switch to a higher quality

when rendering the final output. A “Force debayer res to highest quality” checkbox in the Render

Settings list of the Deliver page makes it easy to follow this workflow.

�Decode Using: The option you select determines whether all Nikon RAW media throughout the

project is decoded using the original Camera Metadata settings (the default selection), using

Project settings in which you choose custom settings to be applied to all clips, or using the Nikon

RAW default settings.

Project Settings

Nikon RAW has a variety of settings that can be adjusted to alter the image quality of the debayered

result. The Color Temp and Tint parameters are only available if the White Balance drop-down menu is

set to Custom.

�White Balance: The first seven options offer White Balance presets, which automatically adjust

the Color Temp and Tint parameters. These options include Daylight, Cloudy, Shade, Tungsten,

Fluorescent, and Flash. An eighth option, Custom, makes the Color Temp and Tint parameters user

adjustable.

�Color Space: Choose one of the common video colorspaces.

�Gamma: Choose N-Log or one of the common video colorspaces.

�Sharpness: A debayer-specific sharpness filter applied to provide the appearance of enhanced

image detail. 20 is unity. The range is 0 to 100.

�Highlights: Makes it easy to selectively retrieve blown-out highlight detail in high-dynamic-range

media by lowering this parameter and achieves a smooth blend between the retrieved highlights

and the unadjusted midtones for a naturalistic result. 0 is unity. The range is –100 (minimum)

through +100 (maximum).


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

�Shadows: Lets you selectively lºighten or darken shadow detail. Raising this value retrieves

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

detail are softened, while areas of high detail are left alone. 0 is unity. The range is –100 (minimum)

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

�Lens Distortion: Check this box to apply automatic Lens Distortion Correction.

�Lens Vignette: Adjusts the correction strength to control vignetting.

�Exposure: Increases or lowers image lightness in units relative to ƒ-stops. If your intended

exposure adjustment lifts image data above the maximum white level, don’t worry; all image data

is preserved and can be retrieved in subsequent adjustments. 0 is unity. The range is –5 to +5.

�Color Temp: Only available when White Balance is set to something other than As Shot. Designed

to alter the “warmth” of the image. Adjustable in Kelvin. Lower values correct for “warmer” lighting,

while higher values correct for “cool” lighting. +6500 is unity. The range is +2000 to +50,000.

�Tint: Only available when White Balance is set to something other than As Shot. Designed to alter

the green to magenta balance of the image for images with fluorescent tinting. Lower values add

green to compensate for magenta lighting, while higher values add magenta to compensate for

green lighting. 0 is unity. The range is –150 to +150.


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

Panasonic Varicam RAW

Panasonic Varicam RAW (CRW) is produced by a variety of Panasonic cameras (such as the VariCam

35 and VariCam Pure 4K) recording to Codex VRAW recorders.

Master Settings

These parameters let you choose the decode quality, white balance, color space, and gamma that raw

clips will be transformed to use when debayered.

�Decode Quality: Lets you debayer Varicam RAW files at Full, Half, or Quarter resolution to improve

performance on slower systems. Lower resolution media is lower quality but faster to work with

and process. If necessary, you can choose a lower resolution setting that provides better real time

playback on systems with limited performance while you work, and then switch to a higher quality

when rendering the final output. A “Force debayer res to highest quality” checkbox in the Render

Settings list of the Deliver page makes it easy to follow this workflow.

�Decode Using: The option you select determines whether all Varicam RAW media throughout

the project is decoded using the original Camera Metadata settings (the default selection), using

Project settings in which you choose custom settings to be applied to all clips, or using the

Varicam RAW default settings.

Project Settings

Panasonic Varicam RAW has a variety of settings that can be adjusted to alter the image quality of the

debayered result. The Color Temp and Tint parameters are only available if the White Balance drop-

down menu is set to Custom.

�White Balance: The first seven options offer White Balance presets, which automatically adjust

the Color Temp and Tint parameters. These options include: Daylight, Cloudy, Shade, Tungsten,

Fluorescent, and Flash. An eighth option, Custom, makes the Color Temp and Tint parameters

user-adjustable.

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

detail are softened while areas of high-detail are left alone. 0 is unity. The range is –100 (minimum)

through +100 (very high).


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA

�Lift: Adjusts the black point of the media, raising it or lowering it while scaling all midtone values

between it and the white point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. The range is –100 to +100.

�Gain: Adjusts the white point of the media, raising or lowering it while scaling all midtone values

between it and the black point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

�Contrast: Raising contrast reduces shadows and raises highlights, while leaving midtones at 50

percent unaffected. Regardless of how you adjust this control, all image data is preserved and can

be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.