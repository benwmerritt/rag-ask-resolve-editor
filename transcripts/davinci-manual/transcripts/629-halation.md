---
title: "Halation"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 629
---

# Halation

These controls are a simplified way of adding soft glows to the edges of the subjects in your frame, to

mimic this characteristic of motion picture film. If you want more control, you can disable this setting

and use the Halation effect instead.

�Enable Halation: Turns the Halation effect on or off.

�Highlights Only: Limits the Halation effect only to the edges of highlights.

�Amount: Lets you set the intensity of the halation.

�Radius: Lets you set the spread size of the glow from the edges.

�Saturation: Lets you adjust the color intensity of the halation.

�Hue: Lets you tint the glow a selected color.

Bloom

These controls lets you introduce a subtle glow around the edges of highlights.

�Enable Bloom: Turns the Bloom effect on or off.

�Amount: Lets you set the intensity of the bloom.

�Radius: Lets you set the spread size of the bloom from the edges.

Grain

These controls are a simplified set of tools to emulate the grain patterns found on motion picture film.

For more detailed control you can disable this setting and use the Film Grain effect instead.

�Enable Grain: Turns the grain pattern on or off.

�Preset: Provides some starting points for grain, based on film stock standards.

�Amount: Determines the amount of grain in the image.

�Size: Determines the size of the grain in the image.

�Softness: Determines how crisp the individual grains are.

�Saturation: Adds color to the grain. 0 is monochromatic.

�Image Defocus: Affects the overall resolution of the image, defocusing more as you reduce the

control towards 0. At 1.000 the resolution is untouched. This control does not affect the grain.

Flicker

These controls add a gentle pulse to the image exposure, mimicking the flicker of motion picture

projection. For more detailed controls you can disable this setting and use the Flicker Addition

effect instead.

�Enable Flicker: Turns the Flicker effect on or off.

�Amount: Sets how much flicker to add to the image. Low settings will be barely visible,

while high settings can be useful for more extreme looks like the Nostalgic preset.

�Rate: The rate at which the flicker pulses.


Resolve FX Overview | Chapter 157 Resolve FX Film Emulation

COLOR

Gate Weave

These controls mimic the slight horizontal and vertical shift of the image as the film is

mechanically pulled through the camera’s gate.

�Enable Gate Weave: Turns the Gate Weave on or off.

�Amount: Determines the amount of motion to the weave.

�Rate: The rate at which the weave moves.

Film Gate

These controls will add blanking to the edges of the image that mimic film projection or telecine

alignment controls.

�Enable Film Gate: Turns the Film Gate on or off.

�Preset: Select an aspect ratio from different common film standards.

�Ratio H/V: You can set a custom ratio for the image here.

�Enable Curvature: Turning this on slightly rounds the corners of the image to mimic how the shape

of an actual film frame is exposed.

�Padding: This will zoom the image in and out of the blanking, allowing you to see the entire

exposed “frame” of film if desired. Similar to a telecine control.

NOTE: It is possible to get unexpected results using Film Gate with video that is not

scaled to fill the entire frame. If this is the case, use the sizing controls to fill the frame with

your image first.

Flicker Addition

Why remove flicker with the Resolve FX Flicker Removal plugin when you can add it instead? The

Flicker Addition plugin adds rapidly animated exposure changes to make the image appear to flicker,

creating animated effects that would be difficult to keyframe manually. When applied to an image in

different ways, this plugin can be used to simulate torchlight, firelight, light fixtures with old ballasts or

frayed wiring, or any temporally unstable light source. For example, you could key only the highlights

of a night-time image and use Flicker Addition to affect those isolated highlights.

Two groups of controls let you control the quality of this flickering.

Main Controls

These controls let you choose how to apply the flicker and its overall speed and intensity.

�Flicker Type: This pop-up menu lets you apply the flicker as a Lift, Gamma, Gain, Vignette, or

Alpha adjustment.

�Range slider: This lets you set how widely the flickering will vary.

�Speed: This lets you adjust how quickly the flickering is animated.

�Smoothness: This slider lets you adjust the temporal quality of the flickering, whether it changes

abruptly from one value to another (at lower settings) or whether it makes more continuous

transitions from one value to another (at higher settings).

�Flicker R, G, B Channels: Three checkboxes let you choose which color channels are affected by

this flickering.


Resolve FX Overview | Chapter 157 Resolve FX Film Emulation

COLOR

Flicker Quality

These controls let you adjust the details of how the flickering animates.

�Randomness Scale: This slider lets you introduce irregularity to the Horizontal, Vertical,

and Rotational motion of the camera shake. The greater this value, the more irregularity

will be introduced.

�Pause Length: This slider lets you adjust the frequency of intermittent pauses that break up the

random motion added by this filter.

�Pause Interval: This slider lets you adjust the duration of intermittent pauses that break up the

random motion added by this filter.

�Pause Randomness: This lets you add a degree of randomness to the intervals that happen.

�Random Seed: This slider lets you alter the value that sets what random values are being

produced. Identical values result in identical randomness.

Halation (Studio Version Only)

An effect that mimics the subtile light scatters, reflections, and analog blooms of light reflecting back

through the dye layers of motion picture film. This usually presents itself as a fine red/orange tinted

glow around high contrast bright regions, like lights or reflections. Halation can also be caused by light

reflections within processing and development equipment, or in the camera itself. These minor flaws

can add a subtle organic and analog look to digital files.

The Halation effect can add an organic and analog look to your digital files. Original (L), Halation (R).

There are a variety of tools and controls to give you fine detail on exactly how the halation

will appear.


Resolve FX Overview | Chapter 157 Resolve FX Film Emulation

COLOR

The shot before the Halation effect

The Halation effect on the same image; note the

halation in the water reflections and the woman in the white t-shirt.

Processing Color Space

Lets you chose the color space for the Halation effect. The default is the same as the current timeline.

Isolation

The Isolation controls define which regions of your clips will form halation halos.

�Threshold: The level low clip level for the Halation effect.

�Normalization: The high clip level for the Halation effect.


Resolve FX Overview | Chapter 157 Resolve FX Film Emulation

COLOR

�Film Saturation Level: The level above which all color is suppressed and saturated to white.

Especially useful in HDR workflows, so the resulting Halation effects are visible at HDR

brightness levels.

�View Isolated Regions: Shows only the regions isolated for generating the Halation effect.

The View Isolated Regions checkbox shows you

the areas that will be affected by the halation.

Dye Layer Reflections

The Dye Layer Reflections controls give you the ability to fine tune the physical characteristics of the

halation glow.

�Strength: Controls the brightness of the reflection.

�Gamma: Controls the how the glow spreads out.

�Saturation: Controls the intensity of the color of the glow.

�Spread: Defines the extent of the dye reflection.

�Fine Tune Relative Spread: Checking this box allows you to manually adjust the red, green, and

blue reflection distances.

Secondary Glow

The Secondary Glow controls add additional halation characteristics.

�Strength: Controls the brightness of the secondary glow.

�Gamma: Controls how the glow spreads out.

�Spread: Defines the extent of the glow around bright detail.

�Filter: Limits the color of the glow in the selected color.


Resolve FX Overview | Chapter 157 Resolve FX Film Emulation

COLOR