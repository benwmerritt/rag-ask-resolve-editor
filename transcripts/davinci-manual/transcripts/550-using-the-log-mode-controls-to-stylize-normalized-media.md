---
title: "Using the Log Mode Controls to Stylize Normalized Media"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 550
---

# Using the Log Mode Controls to Stylize Normalized Media

You can also use the Log mode controls on already normalized images. Although the results you

get will be somewhat different, this can be a fast way to create interesting stylizations. Whereas the

broadly overlapping tonal ranges of the Lift, Gamma, and Gain color balance controls allow subtle

adjustments to be made very easily, the Log palette’s color balance controls affect much more

restrictive tonal zones that overlap much less when used on normalized images.

The following illustration shows an approximation of how the Shadows, Midtones, and Highlights, by

default, divide the tonal range of the image into non-overlapping thirds. As you saw in the previous

section, these divisions were originally intended to map to log-encoded media. However, with

normalized media these divisions provide a different, and potentially useful, set of ranges from the

Primaries mode controls.


Color | Chapter 131 Primaries Palette

COLOR

Shadows

Midtones

Highlights

High Range

Low Range

This graphic shows an approximation of the tonal range of each of the Log controls

with the additional low and high range to expand or contract the range.

With normalized media, the Shadows really do only affect the darkest shadows, falling off at

approximately the bottom third of image tonality. The Midtones affect only the middle third of grays,

and the Highlights affect the brightest top third of image values. However, these default ranges of

image tonality can be adjusted using the Low Range and High Range controls, which are described in

more detail later.

The following image shows the default interaction of extreme corrections made to a grayscale image

using the Log mode controls. The Shadows have been pushed toward green, the Midtones have been

pushed toward blue, and the Highlights have been pushed toward red.

Extreme adjustments showing the overlap of the Shadow,

Midtone, and Highlight color balance controls

As you can see, with normalized media the color interaction between each adjustment is very subtle.

The darkest shadows end up bright green, the midtone values are vivid blue, and the highlights are

almost pure red. This restrictiveness is useful when you want to limit a correction to a specific tonal

range within the image without needing to use a Luma qualifier. It’s also quite useful for making bold,

stylistic color adjustments when creating a non-naturalistic look.

TIP: The Highlights adjustment of the Log controls can also be extremely useful for boosting

or otherwise controlling the highlights of HDR grades. However, the multiple highlight zones

of the HDR palette afford a much higher degree of control over this kind of adjustment, using

similar control panel-friendly controls.


Color | Chapter 131 Primaries Palette

COLOR

Adjusting the Default Tone Ranges in Log Mode

When in Log mode, two additional parameters appear in the top shared controls bar that let you

modify the range of Shadows and Highlights image tonality that each Color Balance control affects,

in turn narrowing and widening the range of Midtones. Keep in mind that while the ranges can be

customized, the amount of overlap between each range cannot.

Low Range: Moves the border where the Shadows and Midtones meet. Lowering this

parameter widens the range affected by the Midffectetones, and narrows the range affected

by the Shadows. Raising this parameter narrows the Midtones and widens the Shadows.

High Range: Moves the border where the Midtones and Highlights meet. Lowering the High

Range parameter narrows the range ad by the Midtones, and widens the range affected by

the Highlights. Raising this parameter narrows the Highlights and widens the Midtones.

There are also Saturation and Hue parameters which mimic these settings found within other palettes

and modes.

Adjusting Contrast in Log Mode

When using the Log mode controls, your primary tools for adjusting image contrast will usually be the

Offset master wheel and Contrast and Pivot parameters. Using these three controls, you can set a

black point and adjust the overall contrast very quickly.

The Shadow, Midtone, and Highlight master wheels let you adjust image lightness within the same

restrictive ranges of image tonality that are defined by the Low Range, High Range, and Pivot

parameters. These adjustments should appear smooth, if somewhat narrower then the Lift/Gamma/

Gain controls, when used with log-encoded media. However, when used with normalized images,

severe adjustments made with one master wheel may not always make a smooth transition to the next

adjacent range of image lightness.

NOTE: Because these controls are so restrictive when used with normalized images, it’s

easy to create solarization effects by raising the shadows to be higher than the Midtones, or

lowering the Highlights to fall below the Midtones, to give two examples.

Log Offset Color and Master Controls

The Log controls share the same Offset color balance and Master Wheel controls that appear in the

Lift/Gamma/Gain mode of the Wheels and Bars controls. The Offset controls are in fact processed

as part of the Log controls, but for convenience they’re presented with the Wheels controls because

they’re so useful.

�The Offset color balance control: Works as a simultaneous adjustment to all three Offset sliders

located in the Primaries palette; adjustments made to the Offset color balance control also alter

the Offset sliders. Used subtly, this makes it easy to neutralize color imbalances in the darkest

part of the image, while simultaneously rebalancing every other part of the image. Used more

dramatically, this control makes it easy to add a color wash throughout the entire image.

�The Offset wheel: Acts as a global adjustment to image lightness, an operation sometimes

referred to as setup, raising or lowering all YRGB channels together.


Color | Chapter 131 Primaries Palette

COLOR

Offset and Printer Points

In Bars mode, the Offset controls are represented by three vertical sliders, which mirror the settings of

the Offset color balance controls in the Color Wheel palette, except that they provide individual control

over the Red, Green, and Blue color channels. In fact, this interface also happens to be the epicenter

of the Printer Points functionality offered by DaVinci Resolve.

When you drag one of the Offset sliders up or down, you raise or lower that color channel in its

entirety. This can be useful for adjusting color channels that are particularly problematic, but it’s also

the way you impose the kinds of traditional linear color adjustments that color timers of film have

employed for decades. In fact, many colorists consider the simplicity of these controls a virtue, and

embrace the slight shadow or highlight contamination that can result from color balancing in this linear

way as a creative hallmark of traditional cinema color adjustment.

Offset RGB and master controls

NOTE: Unlike the other Color Balance control adjustments described in this chapter, the

Offset controls do not use the Lum Mix parameter to control whether individual adjustments

to the R, G, or B channels result in automatic adjustments being made to the other two color

channels in order to maintain constant Luma levels. All Offset and printer points adjustments

made to a specific color channel affect only that color channel.

Adjusting Printer Points in the Bars Mode

Each Offset slider also has a pair of arrow buttons, one at the top and one at the bottom. These

buttons provide “Printer Point” adjustment of these values, which let you adjust each Offset channel in

discrete increments. Printer Points can be useful for projects that have tight integration with a film lab,

and are designed to emulate color adjustments made using optical printers.

The “plus” and “minus” red, green, and blue

buttons for making printer point adjustments


Color | Chapter 131 Primaries Palette

COLOR

The Offset wheel control underneath the Offset sliders lets you adjust all three sliders at once,

performing a master or setup adjustment. The Offset sliders, Printer Point buttons, and Offset wheel

can be adjusted using keyboard shortcuts.

NOTE: The DaVinci Resolve Advanced and Mini color grading panels each have support for

adjusting printer points using rotary controls for the Red, Green, and Blue channels, as well as

All channels together.

Adjusting Printer Points Via Keyboard Shortcuts

One of the best ways of using printer points if you don’t have a color control panel that supports them

is to enable the numeric keypad to use dedicated keyboard shortcuts just for printer points.

To use the Printer Lights Hotkeys:

�Choose Color > Printer Light Hotkeys, or press Option-Command-Grave Accent (`)

When you enable Printer Light Hotkeys, there are two sets of shortcuts you can use to manipulate

printer points. First, if you want to directly manipulate RGB in whole increments, there’s one set for that.

Red

Green

Blue

7 - Plus Red

8 - Plus Green

9 - Plus Blue

4 - Minus Red

5 - Minus Green

6 - Minus Blue

However, if you want to work in the classic way by manipulating cyan, magenta, and yellow in whole

increments, there’s another set of shortcuts for that, using the remaining keys on the numeric keypad.

Cyan

Magenta

Yellow

1 - Plus Cyan

2 - Plus Magenta

3 - Plus Yellow

Minus (–) - Minus Cyan

0 - Minus Magenta

Period (.) - Minus Yellow

There are also a pair of keyboard modifiers that gives you finer control over printer points adjustments

made with these special keyboard shortcuts, while retaining the coarser default adjustments that let

you make bigger changes more quickly:

�Hold down Command while using these key shortcuts to adjust printer points in

quarter‑increments.

�You can use half-increments as well, but you will need to assign the keyboard shortcuts

for these manually.


Color | Chapter 131 Primaries Palette

COLOR