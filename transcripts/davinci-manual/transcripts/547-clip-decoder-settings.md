---
title: "Clip Decoder Settings"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 547
---

# Clip Decoder Settings

There’s much more information on the various format-specific Master settings, as well as the

occasionally format-specific Clip Decoder settings, in Chapter 7, “Camera Raw Settings.” However, with

the exception of the RED Clip Decoder settings that appear for R3D clips, most other formats share a

set of DaVinci Resolve-specific controls that provide wide-latitude access to the raw image data for

purposes of making different kinds of adjustments.

Camera Raw Clip Decoder settings for BRAW media

While specific raw formats have individual controls, the standard controls include:

�Color Temp: Designed to alter the “warmth” of the image. Adjustable in degrees Kelvin. Lower

values correct for “warmer” lighting, while higher values correct for “cool” lighting. +6500 is unity.

The range is +2000 to +50,000.

�Tint: Color balance correction for images with a green or magenta color cast, such as fluorescent

or sodium vapor bulbs. 0 is unity. The range is –150 to +150.

�Exposure: Increases or lowers image lightness in units relative to ƒ-stops. If your intended

exposure adjustment lifts image data above the maximum white level, don’t worry; all image data

is preserved and can be retrieved in subsequent adjustments. 0 is unity. The range is –5 to +5.

�Sharpness: A debayer-specific sharpness filter applied to provide the appearance of enhanced

image detail. 20 is unity. The range is 0 to 100.

�Highlights: Makes it easy to selectively retrieve blown-out highlight detail in high-dynamic-range

media by lowering this parameter, and achieves a smooth blend between the retrieved highlights

and the unadjusted midtones for a naturalistic result. 0 is unity. The range is –100 through +100.

�Shadows: Lets you selectively lighten or darken shadow detail. Raising this value retrieves

shadow detail recorded below 0 percent, while leaving the midtones alone. 0 is unity. The range is

–100 through +100.

�Color Boost: A non-uniform saturation operation that affects regions of low saturation more

than regions of high saturation. This is sometimes referred to as a vibrance operation. 0 is unity,

showing the original color values. Raising color boost from 0-100 increases color intensity, but low-

saturation parts of the image are raised more aggressively. Lowering Color Boost from 0 to -100

decreases color intensity, but low-saturation parts of the image are lowered more aggressively.

0 is unity, showing unaltered saturation. The range is –100  through +100.


Color | Chapter 130 Camera Raw Palette

COLOR

�Saturation: A uniform saturation operation that raises (above 50) or lowers (below 50) the

color intensity of every color value within the image. 50 is unity, showing unaltered saturation.

The range is -100 (completely desaturated) through +100 (saturation is doubled).

�Midtone Detail: When this parameter is raised, the contrast of regions of the image with high

edge detail is raised to increase the perception of image sharpness, sometimes referred to as

definition. When this parameter is lowered to a negative value, regions of the image with low

amounts of detail are softened while areas of high-detail are left alone. 0 is unity. The range is

–100 through +100.

�Lift: Adjusts the black point of the media, raising it or lowering it while scaling all midtone values

between it and the white point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. The range is –100 to +100.

�Gain: Adjusts the white point of the media, raising or lowering it while scaling all midtone values

between it and the black point. Regardless of how you adjust this control, all image data is

preserved and can be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

�Contrast: Raising contrast reduces shadows and raises highlights, while leaving midtones at

50 percent unaffected. Regardless of how you adjust this control, all image data is preserved and

can be retrieved in subsequent adjustments. 0 is unity. The range is –100 to +100.

Resetting Camera Raw Settings

If you’ve made changes to the parameters of the Camera Raw palette and you decide you need to

reset them, there are two options, found in the Options menu.

�Reset: Resets all parameters in the Camera Raw palette to their default settings.

�Revert: Similar to the “Original Memory” command, Revert changes all camera raw parameters

back to the state they were at when you first selected the current clip.

Updating Sidecar Settings for

Blackmagic RAW (BRAW) Clips

Blackmagic RAW clips support both embedded look metadata within the .braw media clip and external

look metadata in .sidecar files. Ordinarily, these files travel in pairs whenever you manage BRAW

media, and whenever a .sidecar file is present, its settings override those of the embedded metadata

within the actual .braw clip. Since the .sidecar metadata is in human-readable JSON formatted text, it’s

easy to edit and accommodates a wide variety of onset to post-production workflows.

The .braw and .sidecar files as seen in the file system

If you like, you can make changes to the raw look metadata of a .braw clip and upgrade the .sidecar

metadata from within the Color page of DaVinci Resolve, so the media on disk reflects these changes

in any other BRAW compatible application.


Color | Chapter 130 Camera Raw Palette

COLOR

To update the .sidecar raw look metadata:


Open the Color page, select a .braw clip in the Thumbnail timeline, and open

the Camera Raw palette.


Set Decode Using to Clip to enable the palette controls.


Make whatever adjustments you want to make using the controls of the Camera Raw palette.


When you’re done, click the Update Sidecar button.

The Update Sidecar button in the

Camera Raw palette for .braw media


Color | Chapter 130 Camera Raw Palette

COLOR

Chapter 131

Primaries Palette

This chapter focuses on the core color adjustments that you’ll be making to

create “primary” corrections that alter the overall color and contrast of the image

using both the Lift/Gamma/Gain adjustments in the Wheels and Bars modes of

the Primaries palette, and the Shadow/Midtone/Highlight/Offset controls in the

Log mode, both of which have traditionally formed the foundation of most grades.

Contents

Introduction to the Primaries Palette�������������������������������������������������������������������������������������������������������������������������������������� 3059

HDR Grading With the Primaries Palette�������������������������������������������������������������������������������������������������������������������������������� 3060

Which Do I Start With, the Primaries or HDR Palette?������������������������������������������������������������������������������������������������������ 3060

Shared Controls in the Primaries Palette������������������������������������������������������������������������������������������������������������������������������ 3060

Switching Between Primaries Tools����������������������������������������������������������������������������������������������������������������������������������������� 3060

Color Balance Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3061

Master Wheels�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3061

Numeric Parameters������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3062

Shared Adjustment Controls�������������������������������������������������������������������������������������������������������������������������������������������������������� 3062

Auto Correction���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3064

Reset Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3064

Color Wheels and Bars������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3065

3-Way Master Wheel Adjustments�������������������������������������������������������������������������������������������������������������������������������������������� 3066

Offset Color and Master Controls���������������������������������������������������������������������������������������������������������������������������������������������� 3067

Color Bars Mode�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3068

Log Wheels Mode����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3068

Using the Log Mode Controls to Grade Log-Encoded Media������������������������������������������������������������������������������������� 3069

Using the Log Mode Controls to Stylize Normalized Media������������������������������������������������������������������������������������������ 3071

Adjusting the Default Tone Ranges in Log Mode�������������������������������������������������������������������������������������������������������������� 3073

Adjusting Contrast in Log Mode������������������������������������������������������������������������������������������������������������������������������������������������� 3073

Log Offset Color and Master Controls������������������������������������������������������������������������������������������������������������������������������������� 3073

Offset and Printer Points���������������������������������������������������������������������������������������������������������������������������������������������������������������� 3074

Adjusting Printer Points in the Bars Mode������������������������������������������������������������������������������������������������������������������������������ 3074

Adjusting Printer Points Via Keyboard Shortcuts�������������������������������������������������������������������������������������������������������������� 3075

Printer Light Step Project Settings�������������������������������������������������������������������������������������������������������������������������������������������� 3076


Color | Chapter 131 Primaries Palette

COLOR

Introduction to the Primaries Palette

If you’ve had any exposure to color correction tools in any application, the Lift/Gamma/Gain controls

found within the Wheels mode of the Primaries palette should look familiar. These controls correspond

to the most traditional and basic color correction functionality available in DaVinci Resolve and are

designed to let users without control panels have easy access to color balance and YRGB contrast

manipulation using a mouse, tablet, or trackpad.

Color Balance controls for primary grading, in Wheels mode

As the name implies, the Primaries palette has been designed for the kind of overall “primary”

color adjustments to the image that typically serve as the foundation of any grade. “Secondary”

adjustments then refer to more specific adjustments made to isolated subjects within the image.

However, it’s a time-tested practice that you do everything you can to get the overall image right

using one or more primary corrections before moving on to more specific detail work built on top

of these initial adjustments. For one thing, it’s a more structured, organized way to work. However,

it’s also the most efficient way to make sure you’re tackling the image in a holistic way, that

maximizes improvements while minimizing stress on the video signal.

The Primaries palette has three distinct modes of operation:

•	 Wheels mode contains the traditional DaVinci YRGB Lift/Gamma/Gain controls that allow

tonally specific yet widely overlapping regions of adjustment. Wheels mode also provides

access to the RGB Offset/Printer Points color balance and master controls.

•	 Bars mode gives access to the same YRGB Lift/Gamma/Gain and Offset controls as

the Primaries Wheels mode, but the Bars interface lets you make vertical slider-driven

adjustments to individual YRGB lift, YRGB gamma, and YRGB gain channels, as well as

providing a slider and button-driven interface for the RGB Offset/Printer Points controls.

•	 Log mode is the home of the RGB Offset/Printer Points color balance and master controls

that adjust the overall signal in a linear, film-oriented way. Log mode provides Shadow/

Midtone/Highlight/Offset controls that offer more restrictive yet customizable regions of

adjustment intended for making adjustments to log-encoded image data.

Which mode you use depends entirely on how you like to work, and what kinds of adjustments you

need to make.


Color | Chapter 131 Primaries Palette

COLOR