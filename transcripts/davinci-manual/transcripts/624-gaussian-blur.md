---
title: "Gaussian Blur"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 624
---

# Gaussian Blur

Provides a smooth blur that resembles looking at the image through semi-opaque glass, reducing

detail and noise.

�Horizontal and Vertical Strength: Two sliders let you adjust the Horizontal and Vertical Strength

independently.

�Same Horizontal/Vertical: This checkbox lets you keep the Horizontal and Vertical Strength

values ganged together.

�Horizontal and Vertical Channel Adjustment: These sliders let you adjust the per channel

settings of the blur.

Red: Adjusts the blur of the Red channel relative to the overall blur.

Green: Adjusts the blur of the Green channel relative to the overall blur.

Blue: Adjusts the blur of the Blue channel relative to the overall blur.

Alpha: Adjusts the blur of the Alpha channel relative to the overall blur.

�Border Type: Lets you choose how the edges of the image are affected by this blur; options

include Black, Replicate, Reflect, and Wrap Around.

�Blur Alpha: Check this box to blur the Alpha channel along with the image’s content.

Lens Blur (Studio Version Only)

A high-quality simulation of optical lens blurring. Adjustable parameters let you achieve different

kinds of “bokeh” effects, which are similar to those produced by different combinations of aperture

design and lens spherical aberration corrections that affect the “circle of confusion” that creates visible

shapes in areas of the picture with pinpoint highlights.

Shape

The Shape group lets you choose what shape of aperture to simulate and affects the shape of the

bokeh in this effect.

A custom shape used in a color node tree to create

custom bokeh in the Lens Blur plugin

�Shape Type: Lets you choose what type of apertures you want to use. There are three options:

Real Apertures: Lets you choose a realistic option from the Aperture Shape pop-up menu below,

with which to influence the shape of the bokeh effect. Aperture Shape options include Triangle,

Square, Pentagon, Hexagon, Heptagon, or Octagon shaped aperture.


Resolve FX Overview | Chapter 155 Resolve FX Blur

COLOR

Creative: Lets you choose a more fanciful option from the Aperture Shape pop-up menu below,

with which to influence the shape of the bokeh effect. These options simulate the kind of bokeh

you could realistically achieve by placing a blackout filter with a custom shaped hole in the center

in front of a lens. Aperture Shape options include Heart, Star, Starfish, Starburst, Petals, Lip, Eye,

Droplet, and Leaf.

External Input: Uses any arbitrary graphic with a (preferably small) white shape against a black

background to influence the shape of the bokeh effect. This shape must be a graphic or matte clip

that’s added to the Node Editor, then you can attach the image to the second RGB input of the

Lens Blur node.

�Aperture Shape: Provides different options for aperture shapes that influence the shape of this

plugin’s simulated bokeh blur effect.

�Preview Shape: This checkbox lets you see the actual shape you’ve selected to use.

Speed

The Speed Options group lets you adjust the quality/speed tradeoff of this plugin.

�Quality: Three options, Full, Half (Faster), and Quarter (Fast), let you choose a suitable tradeoff

between image quality and plugin performance.

�Blur Alpha: Check this box to blur the Alpha channel along with the image’s content.

�Horizontal and Vertical Crop: Crops the External Input shape image being used to influence the

bokeh to a smaller size, in the event the large size of the graphic is slowing things down and you

can crop out extra black from the edges. You won’t notice a change to the result until you start

cropping into the white part of the shape.

Controls

The parameters available from the Controls group change depending on the Shape Type

you’ve selected.

�Blur Size/Scale: Adjusts the overall amount of blur. At higher values, the shape of bokeh can be

more clearly seen.

�Blade Curvature: (Only available with Real and Creative Apertures) Lets you round off the edges

of the Aperture Shape you selected.

�Rotation: Lets you adjust the angle the shape appears at.

�Anamorphism: Lets you adjust the aspect ratio of this effect in order to match the lens blur

created by anamorphic lenses.

�Chroma Shift: Lets you simulate chromatic aberration within the blur effect.

�Highlights: Lets you adjust how the highlights of the image affect the blur, dilating or eroding the

image more or less depending on how high Smooth Strength is.

�Apodization: (Only available with Real and Creative Apertures) A slider that lets you adjust the

simulated “Airy disk” pattern in the defocused effect being generated. Dragging the slider to the

left toward negative values accentuate concentric rings around the bokeh pattern that simulate the

effects of optical diffraction and add a pattern to the result, while dragging this slider to the right

introduces positive values that gradually filter the edges of the simulated bokeh pattern, resulting

in a progressively smoother result.

�Catadioptric: (Only available with Real and Creative Apertures) A slider that lets you simulate

the effect of a shaped mirror element in a Catadioptric telescope to “improve” focus within

the defocused bokeh effect this plugin produces. At higher and higher values, the underlying

image becomes progressively less blurry, while still being distorted by the bokeh shape being

used which results in soft image overlays, creating a very different kind of simulated optical

defocusing effect.


Resolve FX Overview | Chapter 155 Resolve FX Blur

COLOR

Mosaic Blur

A simple, pixelated blur suitable for hiding the face of anonymous witnesses.

�Pixel Frequency: Lets you adjust the size of each pixel, thus determining the density and

resolution of the resulting grid of pixels.

�Cell Shape: Lets you adjust the base shape of the mosaic. The options are Square, Hexagon,

and Triangle.

�Aliasing: Lets you adjust how tightly each cell samples the area underneath it.

�X Offset: Shifts the grid left or right.

�Y Offset: Shifts the grid up or down.

�Aspect: Adjusts the aspect ratio of the cells.

�Antialias Result: With this box checked the effect performs extra processing to get cleaner lines

between the cells.

�Blur Alpha: Check this box to blur the Alpha channel along with the image’s content.

�Whole Cells Only: Limits the showing of cells to those cells that are completely inside of a

window only.

Radial Blur

A blur effect that simulates the motion blur that would occur were the image spinning around its

center point.

�X and Y Position: Lets you move the center of the blur.

�Smooth Strength: Adjusts how much blurring is applied.

�Blur Type: When Blur Type is set to Realistic, the blur effect emulates a photographic motion blur.

When set to Stylized, the blur effect is a simple and smooth digital blur.

�Blur Symmetry: Three options are available.

Symmetric: The blur effect appears to be created in both directions, with the result being

more of a double-image that’s blurring in an arc around the X/Y Position, simulating motion blur in

a camera.

Clockwise: The blur effect appears to be moving in a single, clockwise direction.

Anti-Clockwise: The blur effect appears to be moving in a single, counter-clockwise direction.

�Channel Adjustment: Allows you to now set the strength of a blur in a specific channel, relative to

the strength of the overall blur.

Red: Adjusts the blur of the Red channel relative to the overall blur.

Green: Adjusts the blur of the Green channel relative to the overall blur.

Blue: Adjusts the blur of the Blue channel relative to the overall blur.

Alpha: Adjusts the blur of the Alpha channel relative to the overall blur.

�Border Type: Lets you choose how the edges of the image are affected by this blur; options

include Black, Replicate, Reflect, and Wrap Around.

�Move with Sizing: Checking this box lets the blur center retain its relative position in the frame if

the Input and Editing sizing are changed.

�Blur Alpha: Check this box to blur the Alpha channel along with the image’s content.


Resolve FX Overview | Chapter 155 Resolve FX Blur

COLOR

Zoom Blur

A blur effect that simulates the motion blur that would occur were a camera moving toward the image.

�Zoom Amount: When Blur Type is set to Realistic, this slider becomes bi-directional. The center

is 0, or no blur at all. Dragging to the right expands the blur effect outward from the position.

Dragging to the left shrinks the image towards the Position, blurring outward from there.

�Blur Type: When Blur Type is set to Realistic, the blur effect emulates a photographic motion blur.

When set to Stylized, the blur effect is a simple and smooth digital blur.

�Smooth Strength: When Blur Type is set to Stylized, this slider controls the strength of the effect.

The left is 0, or no blur at all. Dragging to the right expands the blur effect outward from the

position. Dragging to the left shrinks the image towards the Position, blurring outward from there.

�Center Exclusion: Controls the distance from the XY position that the Zoom Blur begins.

�Channel Adjustment: Allows you to now set the strength of a blur in a specific channel, relative to

the strength of the overall blur.

Red: Adjusts the blur of the Red channel relative to the overall blur.

Green: Adjusts the blur of the Green channel relative to the overall blur.

Blue: Adjusts the blur of the Blue channel relative to the overall blur.

Alpha: Adjusts the blur of the Alpha channel relative to the overall blur.

�Center Position: Lets you move the center of the blur.

�Quality: Choose between Faster, Better, and Enhanced. Better and Enhanced modes are used to

improve sharp image content at low blur values. If this does not apply to your footage, Faster will

work just as well.

�Border Type: Lets you choose how the edges of the image are affected by this blur; options

include Black, Replicate, Reflect, and Wrap Around.

�Move with Sizing: Checking this box lets the blur center retain its relative position in the frame if

the Input and Editing sizing are changed.

�Blur Alpha: Check this box to blur the Alpha channel along with the image’s content.


Resolve FX Overview | Chapter 155 Resolve FX Blur

COLOR

Chapter 156

Resolve FX Color

These plugins provide color processing methods that aren’t available in any of the

Color Page palettes of the Color page and include several color management tools

that can be applied outside of Resolve Color Management (RCM).

Contents

ACES Transform��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3468

Chromatic Adaptation��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3468

Color Compressor (Studio Version Only)������������������������������������������������������������������������������������������������������������������������������� 3469

Color Space Transform�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3470

Color Space Transform��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3470

Tone Mapping��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3470

Gamut Mapping������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3471

Advanced������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3471

Color Stabilizer (Studio Version Only)��������������������������������������������������������������������������������������������������������������������������������������� 3472

Analysis Region����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3472

Channels to Stabilize������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3473

Captured Analysis Values��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3473

Contrast Pop (Studio Version Only)�������������������������������������������������������������������������������������������������������������������������������������������� 3473

DCTL (Studio Version Only)������������������������������������������������������������������������������������������������������������������������������������������������������������ 3474

Dehaze (Studio Version Only)�������������������������������������������������������������������������������������������������������������������������������������������������������� 3474

Despill ����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3474

False Color (Studio Version Only)������������������������������������������������������������������������������������������������������������������������������������������������ 3476

General���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3476

Camera Model�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3477

Color Bands������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3477

Preprocessing��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3477

Scale/Legend���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3477

Gamut Limiter��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3478

Gamut Mapping (Studio Version Only)������������������������������������������������������������������������������������������������������������������������������������� 3478

Invert Color�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3479


Resolve FX Overview | Chapter 156 Resolve FX Color

COLOR