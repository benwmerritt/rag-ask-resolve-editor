---
title: "Introduction to the RGB Mixer Palette"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 556
---

# Introduction to the RGB Mixer Palette

The RGB Mixer palette lets you remix different amounts of image data from one channel to another,

and has a wide variety of creative and utilitarian uses. Furthermore, the RGB Mixer can be used

either to remix the color channels, or to add different proportions of each color channel into a

monochrome image.

RGB Mixer palette

By default, the RGB Mixer palette is set to mix any amount of the Red, Green, and Blue color channels

into any of the other channels. Each color channel has a dedicated control group of Red, Green,

and Blue sliders that you use to do the mixing, and the default values of these can be seen in the

screenshot above.

Each slider has an overall range of –2.00 to +2.00. This means that you also have the option of

subtracting any combination of color channel values from a particular channel. For example, you can

lower the Red control group’s Green slider to –.24 to subtract 24 percent of the Green channel from

the Red channel.

The Auto Normalize control on

the Red cµhannel of the RGB Mixer

The RGB Mixer has an additional Auto Normalize control for each channel. These per-channel

normalize controls allow for users to adjust channel mixes without affecting overall luminance. When

you adjust one color channel, the others will automatically compensate for the change.


Color | Chapter 133 Primary Grading Controls

COLOR

Example

The Original image has a cyclist with a green stripe on his helmet:

The normal Green channel for the RGB Mixer

Normally reducing the Green channel in the green output adds a magenta

cast to the entire image

When Auto Normalize is active, the other two channels compensate for the

change in green. Showing the hue change mainly in the green helmet stripe

(now turned cyan), with minimal changes to the rest of the image.


Color | Chapter 133 Primary Grading Controls

COLOR

Preserve Luminance

With the “Preserve Luminance” checkbox turned on, any channel adjustment you make is prevented

from altering the luma of the image by automatically raising or lowering the other two channels to

compensate. In the following example, you can see that when “Preserve Luminance” is turned on,

lowering the Green control group’s Green slider results in the Red and Blue channels being raised by

the same amount (as seen in the Parade scope). Conversely, raising a color channel’s slider ends up

lowering the other two channels by the same amount to keep overall image luminosity the same.

The result of an RGB Mixer adjustment with “With luminance level preserved” turned on.

You can see that lowering the green channel slider also raises red and blue.

Resetting the RGB Mixer

Clicking the Reset button at the top right-hand corner of the RGB Mixer resets each slider to its default

position, where Red = 1.00 for Red output, Green = 1.00 for Green output, Blue = 1.00 for Blue output,

and all other sliders = 0.

Swap Channels Buttons

A set of three buttons at the bottom of the RGB Mixer lets you easily swap two channels with one

another. This can be useful as part of a creative look, or corrective in instances where two channels

are accidentally reversed.

�Swap Red and Green: Swaps these two color channels.

�Swap Green and Blue: Swaps these two color channels.

�Swap Red and Blue: Swaps these two color channels.


Color | Chapter 133 Primary Grading Controls

COLOR

Using the RGB Mixer in Monochrome Mode

When you turn on the Monochrome checkbox, two of the sliders within each Output group are

disabled. This leaves the Red > Red slider, the Green > Green slider, and the Blue > Blue slider as the

only available controls.

Keeping in mind that each of the color channels that makes up an image is itself a grayscale channel,

the RGB sliders in Monochrome mode let you add different proportions of the Red, Green, and Blue

color channels together to create custom grayscale versions of a shot.

Sliders at their default values when Monochrome mode is enabled

To understand why this is useful, let’s consider the default values of the Red, Green, and Blue sliders.

To emulate the human eye’s sensitivity to the wavelengths of light, the Rec. 709 video standard

defines an isolated Luma (Y’) component as consisting of 0.2126 of the Red channel, 0.7152 of the

Green channel, and 0.0722 of the Blue channels added together. This can be seen in the default

values (rounded to the nearest integer percentage) of 21, 71, and 7.

This is the standard method of deriving a black and white version of a color image, and in fact

produces identical results to those obtained by setting the Saturation parameter to 0.

However, there have traditionally been other ways of mixing the colors of life into different grayscale

interpretations. For example, photographers often use colored filters in conjunction with black & white

film stocks, such as a yellow/green filter to emphasize pleasing skin tone for lightly complexioned

people. A much older example is the use of black & white film stocks with different sensitivities

(old orthochromatic stocks were not sensitive to red wavelengths, recording only blue and green to

create an image).

Using the RGB Mixer with Monochrome mode turned on gives you the ability to mix your own

custom blends of all three color channels to emphasize the creative characteristics you require. For

instance, increasing the mix of blue and decreasing red and green can give skin tones a darker,

metallic sheen. The following screenshots show multiple versions of the same image with different

monochrome mixes.


Color | Chapter 133 Primary Grading Controls

COLOR

Three monochrome mixes of the same image.

The top image is the result of setting saturation to 0.

Like the parameters in Color mode, you can use the RGB Mixer’s Monochrome mode to

subtract one color channel from the others, for even more creative effects.


Color | Chapter 133 Primary Grading Controls

COLOR