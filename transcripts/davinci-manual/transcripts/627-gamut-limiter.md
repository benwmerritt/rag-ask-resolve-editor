---
title: "Gamut Limiter"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 627
---

# Gamut Limiter

Lets you limit the gamut to a specified standard. Useful in situations where the delivery color space is

a large gamut such as Rec. 2020, but the QC specification requires limiting to a smaller gamut such as

P3, in order to limit the amount of saturation allowable in the final output. This is a limiting operation, so

out of bounds values are hard clipped. This plugin can be used regardless of whether or not Resolve

Color Management is enabled. Because it’s a limiter, it should probably be one of the last operations in

any node tree to prevent useful image data from being clipped.

�Current Gamut: Choose the timeline gamut currently being used by the image.

�Current Gamma: Choose the timeline gamma currently being used by the image.

�Limit Gamma to: Choose the gamut you want to restrict the image to here.

These menus present the same options as the Resolve Color Management menus in the

Color Management panel.

For more information about the options available in these parameters, see Chapter 9, “Data

Levels, Color Management, and ACES.”

Gamut Mapping (Studio Version Only)

The Color Space Transform plugin provides Gamut Mapping controls to accommodate workflows

where you need to transform one color space into another that has a dramatically larger or smaller

gamut. These controls are identical to those found in the Color Space Transform plugin’s Gamut

Mapping group and are similar to those found in the Color Management panel of the Project Settings.

�Gamma: A pop-up menu lets you specify what type of gamma the clip is supposed to have, so set

this to whatever matches that image (this may match the timeline color space, but it depends on

how you’re working).

�Tone Mapping Method: Lets you enable tone mapping, to accommodate workflows where you

need to transform one color space into another with a dramatically larger or smaller dynamic range

by automating an expansion or contraction of image contrast in such a way as to give a pleasing

result with no clipping.

None: This setting disables Input DRT Tone Mapping. No tone mapping is applied to the Input

to Timeline Color Space conversion at all, resulting in a simple 1:1 mapping to the Timeline

Color Space.

Clip: Hard clips all out-of-bounds values.

Simple: Uses a simple curve to perform this transformation, compressing or expanding the

highlights and/or shadows of the timeline dynamic range to better fit the output dynamic range.

Note that the “Simple” option maps between approximately 5500 nits and 100 nits, so if you’re

mapping from an HDR source with more than 5500 nits to an SDR destination there may still be

some clipping of the highlights above 5500 nits.

Luminance Mapping: Same as DaVinci, but more accurate when the Input Color Space of all your

media is in a single standards-based color space, such as Rec. 709 or Rec. 2020.

DaVinci: This option tone maps the transform with a smooth luminance roll-off in the shadows and

highlights, and controlled desaturation of image values in the very brightest and darkest parts of

the image. This setting is particularly useful for wide-gamut camera media and is a good setting to

use when mixing media from different cameras.


Resolve FX Overview | Chapter 156 Resolve FX Color

COLOR

Saturation Preserving: This option has a smooth luminance roll-off in the shadows and highlights,

but does so without desaturating dark shadows and bright highlights, so this is an effective option

for colorists who like to push color harder. However, because over-saturation in the highlights

of the image can look unnatural, two parameters are exposed to provide some user-adjustable

automated desaturation.

�Sat. Rolloff Start: Lets you set a threshold, in nits (cd/m2), at which saturation will roll off along

with highlight luminance. Beginning of the rolloff.

�Sat. Rolloff Limit: Lets you set a threshold, in nits (cd/m2), at which the image will be totally

desaturated. End of the rolloff.

Max Input/Output Luminance: Checking these boxes and adjusting the slider below allows

you to specify the minimum and maximum luminance of the input image in nits. Using these two

sliders together, you can set which value from the Input Gamma is mapped to which value of the

Output Gamma.

Avg. Input Luminance: Used to compensate for large differences in the viewer’s state of visual

adaptation when viewing a bright image on an HDR display versus seeing that same image on an

SDR display. For most “average” images this setting works best set between 0–10. However, when

you’re converting very bright images (for example, a snow scene at noon), then using a higher

value will yield more image detail within the highlights.

�Gamut Mapping Method: Accommodates workflows where you need to transform one color

space into another with a dramatically larger or smaller gamut by helping to automate an

expansion or contraction of image saturation in such a way as to give a pleasing and naturalistic

result with no clipping. Choosing Saturation Mapping lets you remap the saturation values of the

image. It enables the Saturation Knee and Saturation Max. controls.

�The Saturation Knee slider sets the image level at which saturation mapping begins. Below

this level, no remapping is applied. All saturation values from this level on up are remapped

according to the Saturation Max. slider. A value of 1.0 is maximum saturation in the currently

selected output color space.

�The Saturation Max slider sets the new maximum level to which you want to either raise or

lower all saturation values that are above the Saturation Knee setting. A value of 1.0 is maximum

saturation in the currently selected output color space.

�Apply Forward OOTF: Check this box to convert the image from scene referred to display referred

color management.

�Apply Inverse OOTF: Check this box to convert the image from display referred to scene referred

color management.

Invert Color

A Color category plugin that lets you invert any color channel, including the Alpha channel just by

checking the appropriate box. This little plugin has 101 uses in advanced workflows, especially when

you need to invert Alpha or Key channels to do something specific. This is not a “film negative” plugin;

this is a simple inversion.


Resolve FX Overview | Chapter 156 Resolve FX Color

COLOR

Chapter 157

Resolve FX

Film Emulation

These plugins are designed to emulate motion picture film characteristics for

aesthetic and creative effects.

Contents

Camera Shake (Studio Version Only)����������������� 3481

Main Controls����������������������������������������������������������������� 3481

Shake Levels������������������������������������������������������������������ 3481

Shake Quality����������������������������������������������������������������� 3481

Blanking Handling����������������������������������������������������� 3482

Film Damage���������������������������������������������������������������� 3482

Blur and Shift Controls��������������������������������������������� 3483

Add Vignetting������������������������������������������������������������� 3483

Add Dirt���������������������������������������������������������������������������� 3483

Add Scratch������������������������������������������������������������������� 3483

Film Grain (Studio Version Only)�������������������������� 3484

Main Controls���������������������������������������������������������������� 3484

Grain Params����������������������������������������������������������������� 3484

Advanced Controls���������������������������������������������������� 3484

Film Look Creator (Studio Version Only)��������� 3485

Main Controls��������������������������������������������������������������� 3486

Color Space Overrides�������������������������������������������� 3486

Film Look������������������������������������������������������������������������ 3486

Color Settings��������������������������������������������������������������� 3487

Split Tone������������������������������������������������������������������������ 3487

Vignette��������������������������������������������������������������������������� 3487

Halation��������������������������������������������������������������������������� 3488

Bloom������������������������������������������������������������������������������� 3488

Grain��������������������������������������������������������������������������������� 3488

Flicker������������������������������������������������������������������������������ 3488

Gate Weave������������������������������������������������������������������ 3489

Film Gate������������������������������������������������������������������������ 3489

Flicker Addition���������������������������������������������������������� 3489

Main Controls��������������������������������������������������������������� 3489

Flicker Quality�������������������������������������������������������������� 3490

Halation (Studio Version Only)����������������������������� 3490

Processing Color Space������������������������������������������� 3491

Isolation���������������������������������������������������������������������������� 3491

Dye Layer Reflections����������������������������������������������� 3492

Secondary Glow���������������������������������������������������������� 3492

Basic Grain��������������������������������������������������������������������� 3493

Global Adjustments��������������������������������������������������� 3493

Vignette��������������������������������������������������������������������������� 3493


Resolve FX Overview | Chapter 157 Resolve FX Film Emulation

COLOR

Camera Shake (Studio Version Only)

This effect replicates random camera motion for Horizontal and Vertical position, Rotation, and Zoom.

A variety of parameters are provided to let you customize the quality of motion, from slow meandering

drift to abrupt, jagged jerks and pops.

Main Controls

The primary controls governing how much camera shake is added.

�Motion Scale and Speed Scale: These sliders let you adjust the overall amplitude and speed of

camera shake that’s introduced to the image.

�Motion Blur: Lets you add simulated motion blur to the image being shaken, which can add a more

realistic look to the motion. Motion blur is more visible on fast-moving motion, as DaVinci Resolve

is simulating the effect of a motion picture camera’s shutter speed on exposed subjects in motion.

Shake Levels

These controls let you adjust the intensity of camera shake.

�Pan Amplitude: Lets you set how much horizontal motion you want.

�Tilt Amplitude: This slider lets you choose how much vertical motion you want. These sliders are

completely independent of one another.

�Rotation Amplitude: Lets you introduce rotational motion to the camera shake as well.

�PTR Speed: This slider lets you choose how fast the Pan, Tilt, and Rotation camera shake is.

�Zoom Amplitude: This slider lets you add zooming to the camera motion being created.

�Zoom Speed: This slider lets you choose how fast this random zooming should occur.

�Zoom Type: This pop-up menu lets you choose how to add zooming; you can choose

Outward Only, Inward Only, or Outward and Inward. If you choose Inward Only, you don’t have to

worry about blanking appearing around the edges of the frame.

Shake Quality

These controls let you customize the type of shaking you want.

�Motion Method: This pop-up menu lets you choose from different ways of generating the motion

this plugin introduces. You can choose from SINE, Rectified SINE, Rectified SINE (Invert), and

Square Wave (good for popping or flickering motion).

�Phase: This slider lets you set the starting point of the camera shake you’re creating, based on the

Motion Method and Amplitude settings you’ve chosen.

�Randomness Scale: This slider lets you introduce irregularity to the Horizontal, Vertical, and

Rotational motion of the camera shake. The greater this value, the more irregularity will be introduced.

�Randomness Speed: This slider lets you choose between smoothly erratic motion (at lower

values) or more jagged motion (at higher values).

�Pause Length: This slider lets you adjust the frequency of intermittent pauses that break up the

random motion added by this filter.

�Pause Interval: This slider lets you adjust the duration of intermittent pauses that break up the

random motion added by this filter.

�Pause Randomness: This lets you add a degree of randomness to the intervals that happen.

�Random Seed: This slider lets you alter the value that sets what random values are being

produced. Identical values result in identical randomness.


Resolve FX Overview | Chapter 157 Resolve FX Film Emulation

COLOR

Blanking Handling

These controls let you determine what to do when camera shake causes blanking past the edge of

the image.

�Border Type: This pop-up menu lets you choose how you want to fill the empty spaces at the

edge that appear if the camera shake you create pushes the image out of the current frame size

of your project. Four options let you choose to Replicate, Reflect, or Wrap-Around the image to

fill the gap.

�Zoom to Crop: This slider lets you zoom in on the image to crop out unwanted blanking being

introduced by the Camera Shake effect.

Film Damage

Found in the Resolve FX Texture category. After you’ve used the new Resolve FX Revival plugins to fix

damage in archival footage, you can turn around and use the Film Damage plugin to make brand new

digital clips look worn, dirty, and scratched instead. When used in conjunction with the Film Grain and

Flicker Addition plugins, you can convincingly recreate the feel of poorly kept vintage archival footage.

(Top) Original image, (Bottom) Result with Film Damage


Resolve FX Overview | Chapter 157 Resolve FX Film Emulation

COLOR