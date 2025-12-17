---
title: "Printer Light Step Project Settings"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 551
---

# Printer Light Step Project Settings

The increments used by the Printer Point buttons are defined by the Printer Light Step Calibration

parameters, found in the Color panel of the User Preferences. The default settings are designed to

emulate traditional film printer adjustments, but these settings can be customized to align DaVinci

Resolve’s printer points adjustments with those of a particular film lab’s equipment. However,

if you’re not working with a lab, you can change the Step and Density settings to alter how much of an

adjustment each printer point makes according to your own preferences.

For more information, see Chapter 4, “System and User Preferences.”

Controls in the Color panel of the User Preferences

to adjust Printer Point functionality

TIP: If you’re feeling left out because all the cool kids are using printer points and you’re

unfamiliar with them, making the Parade scope visible is a great way to learn how these

adjustments work while seeing their specific effects on the red, green, and blue channels of

the video signal.


Color | Chapter 131 Primaries Palette

COLOR

Chapter 132

HDR Palette

This chapter focuses on the global and zone-based adjustments found in the

HDR palette, which is DaVinci’s newest primary grading tool. Despite its name,

this palette can be used, as you might the Lift/Gamma/Gain mode of the Primaries

palette, to create the foundational adjustment for any SDR or HDR grade.

However, its zone‑based nature gives it the power and specificity of curve-based adjustments,

making the HDR palette suitable for a multitude of creative and corrective tasks. Furthermore,

this palette’s color space awareness, as well as the perceptually uniform color space in which it’s

adjustments are made, make this palette uniquely suited for controlling the saturation and highlights of

HDR mastered images.

Contents

Introduction to the HDR Palette������������������������������������������������������������������������������������������������������������������������������������������������ 3078

What Makes the HDR Palette Special?����������������������������������������������������������������������������������������������������������������������������������� 3079

The HDR Palette Interface������������������������������������������������������������������������������������������������������������������������������������������������������������� 3081

Navigating Multiple Zones in the Controls Panel���������������������������������������������������������������������������������������������������������������� 3081

Making Global Adjustments�������������������������������������������������������������������������������������������������������������������������������������������������������� 3083

Black Offset Explained������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3087

Making Zone-Based Adjustments�������������������������������������������������������������������������������������������������������������������������������������������� 3088

Zone-Based Color Adjustments������������������������������������������������������������������������������������������������������������������������������������������������� 3089

Zone-Based Exposure Adjustments����������������������������������������������������������������������������������������������������������������������������������������� 3092

An Example of Zone-Based Exposure Adjustment����������������������������������������������������������������������������������������������������������� 3093

Zone Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3095

Customizing Zones Using the Zone Panel��������������������������������������������������������������������������������������������������������������������������� 3097

The Zone Sidebar������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3097

Zones Graph����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3098

Customizing and Saving Presets������������������������������������������������������������������������������������������������������������������������������������������������ 3099

Resetting Color and Zone Adjustments��������������������������������������������������������������������������������������������������������������������������������� 3100


Color | Chapter 132 HDR Palette

COLOR

Introduction to the HDR Palette

The HDR palette is specifically designed to enable fast and flexible primary grading of wide-latitude

media for either SDR or HDR output. It’s “color space aware” in that it works with Resolve Color

Management to fit the known mapping of source image data within the HDR palette’s own perceptually

uniform operational color space. Using advanced color processing algorithms, this enables more

efficient color and contrast adjustments, and perceptually uniform controls that make it easier to adjust

all colors equally across the spectrum, while maintaining careful control of image saturation.

The HDR palette

A set of global controls, at the right of the palette, let you make foundational adjustments to the overall

image, along with a set of Hue, Midtone Detail, Contrast/Pivot, and Black Offset controls at the bottom.

Additionally, a set of overlapping zone-specific controls let you make color and contrast adjustments

to specific ranges of image tonality. Altogether, the HDR palette lets you make primary grading

adjustments that are both photographically naturalistic and as tonally broad or specific as you require,

while minimizing unwanted artifacts.

Despite its sophistication, the HDR palette uses color balance and slider controls that should be

familiar to any colorist or editor familiar with the more conventional Lift/Gamma/Gain controls. Whether

you’re a grading professional or just getting started with color, the HDR palette will enable great

results with less hassle once you learn how to harness its power.

The controls panel of the HDR palette

TIP: Due to the increasing ubiquity of HDR-capable media and HDR streaming distribution

workflows, the node HDR mode and HDR palette are both available without restriction in the

free downloadable version of DaVinci Resolve.


Color | Chapter 132 HDR Palette

COLOR

What Makes the HDR Palette Special?

Before diving into the detailed use of the HDR palette’s controls, it’s important to understand a

bit more about how the HDR palette processes image data, so you can better understand what

advantages this tool presents.

Using the HDR Palette Without Color Management

While the HDR palette has been designed to work hand in hand with color management, you can use

it in non-color managed workflows so long as you set it up correctly. The HDR palette option menu

has Color Space and Gamma submenus that let you specify how you want to work. By default, both

submenus are set to “Timeline” to reflect the color space you’re choosing to work within in display-

referred workflows.

Color Space Aware Controls When Using Color Management

The HDR palette really shines when you enable Resolve Color Management or ACES, because it’s a

color space aware palette that uses color management to full advantage. Being color space aware

means that the color and contrast controls of the HDR palette conform themselves to the range of

each clip’s image data as mapped from the Input Color Space assigned to the source clip to the

Timeline Color Space your program is working within. Practically, this provides two benefits:

�The controls of the HDR palette work and feel virtually identical no matter what type of source clip

you’re adjusting, and no matter which timeline color space you’re choosing to work within.

�HDR palette adjustments made to one type of media will have a similar result when copied to

other types of media. This makes makes matching shots and copying looks from one type of

media to another easier than with previous tools.

NOTE: Because the HDR palette is color space aware, it’s not necessary to enable the HDR

setting on nodes for controls to work intuitively while working within a wide gamut Timeline

Color Space, or delivering to an HDR format like ST.2084. The HDR palette takes care of this

for you, automatically.

Perceptually Uniform Adjustments

Furthermore, the image data of each clip is converted from the Timeline Color Space to an operational

color space used by the HDR palette, where the image is adjusted and then converted back to the

Timeline Color Space again, ready for the next operation. The operational color space that’s used by

the HDR palette is perceptually uniform, which means that the range of values corresponding to each

visible hue are distributed evenly throughout this color space.

While the HDR palette works well grading standard dynamic range (SDR) material, the underlying color

science used by this palette also addresses issues that have inconvenienced colorists grading high

dynamic range programs using traditional controls. These benefits include:

�Since the controls of this palette calculate all color transformations within a perceptually uniform

color space, you will experience finer control over color adjustments in a more photographically

intuitive way. For example, you may find that yellow hues are easier to grade within this palette,

since there’s a more even distribution of hues around the circumference of the color wheels.

�The HDR palette lets you make contrast adjustments without altering image saturation, meaning

that unlike when you use the master wheels of the Lift, Gamma, and Gain panel, the HDR palette

lets you raise image contrast without increasing image saturation, and lower image contrast

without decreasing image saturation. You’ll find this is particularly useful while boosting highlights


Color | Chapter 132 HDR Palette

COLOR

in HDR grades, since you can now do so without causing extreme saturation increases in

your highlights. In fact, all adjustments you make to contrast with these controls will adjust the

image while keeping saturation unerringly constant (that is to say, perceptually speaking; you

will in fact notice small saturation changes in the Vectorscope). This, of course, excludes the

saturation controls.

�The HDR palette’s deep integration with Resolve Color Management also makes matching shots

and copying looks from one type of media to another easier than with previous tools. Whether

you’re a professional, or just getting started with color, the HDR palette will enable better results

with less hassle.

Superior Temp and Tint Controls

Because the HDR palette is color space aware, the Temperature and Tint adjustments in this palette

are themselves made using the same kind of XYZ to LMS color space transform used by the Chromatic

Adaptation Resolve FX plugin. The result is that Temp adjustments are photometrically accurate and

create visual results similar to how the human vision system perceives changes to a scene due to a

change in the color temperature of lighting.

Customizable Zones

Another unique aspect of the HDR palette is how it can be customized to suit a wide variety of working

styles, specific tasks, and colorist preferences. Switching to the Zones panel reveals an interface for

adjusting the Range and Falloff of each currently defined zone, using graphical controls overlaid onto a

histogram of the current image, while a curve shows the user how the contrast and color adjustments

they’ve made mathematically affect the RGB channels of the image within each zone. While the default

zones preset provides an efficient starting point for many kinds of scenes, the varying tonal range of

image data in different scenes, whether daytime, nighttime, interior, or exterior, will often require you

to customize these zones to get the best results from adjustments using these controls.

The Zones panel lets you customize the tonal ranges that each set of zone controls affect.

Additionally, the sidebar at the left provides controls for adding and removing zones, so users can

customize this palette to work exactly the way they want. Any customized preset can be saved for

easy recall. This way, users have the freedom to work in whatever way suits them.

The Option menu provides fast access to additional ways of customizing this palette’s operation,

including the selection and management of presets, a choice of methods for numerically editing Color

Balance adjustments, and a setting that determines whether or not the Global controls are always

exposed, or should be banked to like the other zone controls.


Color | Chapter 132 HDR Palette

COLOR