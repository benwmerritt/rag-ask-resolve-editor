---
title: "Basic Node Setup"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 418
---

# Basic Node Setup

The Day Sky node is a generator, so it typically starts the branch of a node tree and connects to some

other node, like a Merge node.

A Day Sky connected as the background to a Merge node

Inspector

Day Sky controls

Controls Tab

The Controls tab is used to set the location and time of the daylight simulation. This will determine the

overall look that is generated.

Location

The Latitude and Longitude sliders are used to specify the location used to create the Day Sky

simulation.

Date and Time

The Day, Month, and Time controls are used to select the specific time for the Day Sky simulation.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Turbidity

Turbidity causes light to be scattered and absorbed instead of transmitted in straight lines through

the simulation. Increasing the turbidity will give the sky simulation a murky feeling, as if smoke or

atmospheric haze were present.

Do Tone Mapping

Since the simulation is calculated in 32-bit floating-point color space, it generates color values well

above 1.0 and well below 0.0. Tone mapping is a process that takes the full dynamic range of the

resulting simulation and compresses the data into the desired exposure range while attempting to

preserve as much detail from the highlights and shadows as possible. Deselect this checkbox to

disable any tone mapping applied to the simulation.

Generally, this option should be deselected only if the resulting image will later be color corrected as

part of a floating-point color pipeline.

Exposure

Use this control to select the exposure used for tone mapping.

Day sky Advance tab controls

Advanced Tab

The Advanced tad provides more specific controls over the brightness and width of the different

ranges in the generated sky.

Horizon Brightness

Use this control to adjust the brightness of the horizon relative to the sky.

Luminance Gradient

Use this control to adjust the width of the gradient separating the horizon from the sky.

Circumsolar Region Intensity

Use this control to adjust the intensity or brightness of the sky nearest to the sun.

Circumsolar Region Width

Use this control to adjust the width or size of the area in the sky affected by the sun.

Backscattered Light

Use this control to increase or decrease the backscatter light in the simulation.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Common Controls

Image and Settings Tabs

The Image and Settings tabs in the Inspector are duplicated in many Generator nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.

Fast Noise [FN]

The Fast Noise node

Fast Noise Node Introduction

The Fast Noise node is a very fast and flexible Perlin Noise generator. It can be useful for a wide

range of effects, from clouds, to swirling fog, waves, water caustics, stylized fire, and smoke, and

other organic textures. It is also invaluable as a noise source for other effects, such as heat shimmers,

particle systems, and dirtiness maps.

Inputs

The two map inputs on the Fast Noise node allow you to use masks to control the value of the noise

detail and brightness controls for each pixel. These two optional inputs can allow some interesting and

creative effects. There is also a standard effect mask input for limiting the Fast Noise size.

Noise Detail Map: A soft-edged mask connected to the gray Noise Detail Map input will give a flat

noise map (zero detail) where the mask is black, and full detail where it is white, with intermediate

values smoothly reducing in detail. It is applied before any gradient color mapping. This can be very

helpful for applying maximum noise detail in a specific area, while smoothly falling off elsewhere.

Noise Brightness Map: A mask connected to this white input can be used to control the noise map

completely, such as boosting it in certain areas, combining it with other textures, or if Detail is set to 0,

replacing the Perlin Noise map altogether.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

Fast Noise to only those pixels within the mask.

Basic Node Setup

The Fast Noise node is used to generate images for other nodes to take advantage of. For example,

below the Fast Noise node is used as a bitmap source in the Particle Emitter.

A Fast Noise node used as a bitmap source for a Particle Emitter


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Inspector

Fast Noise controls

Noise Tab

The Noise tab controls the shape and pattern of the noise for the Fast Noise node.

Discontinuous

Normally, the noise function interpolates between values to create a smooth continuous gradient of

results. Enable this checkbox to create hard discontinuity lines along some of the noise contours. The

result will be a dramatically different effect.

Inverted

Select this checkbox to invert the noise, creating a negative image of the original pattern. This is most

effective when Discontinuous is also enabled.

Center

Use the Center coordinate control to pan and move the noise pattern.

Detail

Increase the value of this slider to produce a greater level of detail in the noise result. Larger values

add more layers of increasingly detailed noise without affecting the overall pattern. High values take

longer to render but can produce a more natural result.

Brightness

This control adjusts the overall brightness of the noise map, before any gradient color mapping is

applied. In Gradient mode, this has a similar effect to the Offset control.

Contrast

This control increases or decreases the overall contrast of the noise map, prior to any gradient

color mapping. It can exaggerate the effect of the noise and widen the range of colors applied in

Gradient mode.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Lock and Scale X/Y

The size of the noise map can be adjusted using the Scale slider, changing it from gentle variations

over the whole image to a tighter overall texture effect. The Scale slider can be separated into

independent X- and Y-axis scale sliders by clicking on the Lock X/Y checkbox immediately above,

which can be useful for a brushed-metal effect.

Angle

Use the Angle control to rotate the noise pattern.

Seethe

Adjust this thumbwheel control to interpolate the noise map against a different noise map.

This will cause a crawling shift in the noise, as if it was drifting or flowing. This control must be

animated to affect the gradient over time, or you can use the Seethe Rate control below.

Seethe Rate

As with the Seethe control above, the Seethe Rate also causes the noise map to evolve and change.

The Seethe Rate defines the rate at which the noise changes each frame, causing an animated drift in

the noise automatically, without the need for spline animation.

Fast Noise node Color tab


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Color Tab

The Color tab allows you to adjust the gradient colors used in the generated noise pattern.

Two Color

A simple two-color gradient is used to color the noise map. The noise function will smoothly transition

from the first color into the second.

Gradient

The Advanced Gradient control in Fusion is used to provide more control over the color gradient used

with the noise map.

Common Controls

Image and Settings Tabs

The Image and Settings tabs in the Inspector are duplicated in many Generator nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.