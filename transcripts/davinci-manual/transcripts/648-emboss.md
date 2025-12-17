---
title: "Emboss"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 648
---

# Emboss

An emboss effect with several options to create different kinds of outline and emboss effects.

�Emboss Style: This pop-up lets you choose from among Relief, Emboss Over, Sobel, and

Laplacian types of embossing.

�Power: Lets you adjust how pronounced the emboss effect is.

�Angle: Lets you choose the apparent angle at which the emboss effect is rendered.

Channels

Three checkboxes let you choose to use the Red, Green, and Blue channels to create this effect.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Mirrors

An effect that lets you reflect part of the image in any direction you like. At its simplest, this can create

a split mirror effect like that found at the end of Prince’s “When Doves Cry.” At its most complicated,

multiple reflections can be set up, to create whirling Kaleidoscope patterns in the image.

Main Controls

These controls let you choose what kind of effect this plugin has.

�Mirror Placement: Lets you choose different types of mirror effects including Individual

(a simple reflection), Rosette, and Kaleidoscope.

�Reflect at Borders: Lets you add another reflection of the image whenever the angle and position

of your reflection would result in offscreen black coming into the frame.

Individual Controls

When Mirror Placement is set to Individual, a series of six sets of Mirror parameters lets you add

multiple mirrored edges in different combinations; by default only one is on, but you can turn more

edges on to create more complicated mirror effects. Each group of Mirror parameters has the

following parameters:

�Enable Mirror: Turns that mirror reflection on.

�X and Y Position: Positions the center of the mirror split reflection.

�Angle: Lets you adjust the angle of the seam along which a reflection will run.

�Flip: Flips which side of the image is reflected.

Rosette Controls

When Mirror Placement is set to Rosette, a single set of parameters creates a variety of

circular patterns.

�X and Y Position: Positions the center of the circular rosette reflection.

�Angle: Lets you adjust the orientation of the rosette pattern about its center.

�Wedge Width: Lets you adjust the thickness of the wedges around the outside of the rosette

pattern, and by extension how many wedges there will be. Thicker wedges results in fewer

reflections around the rosette pattern and thinner wedges result in more reflections around the

rosette pattern.

Kaleidoscope Controls

When Mirror Placement is set to Kaleidoscope, a single set of parameters lets you create a variety of

kaleidoscopic images:

�X and Y Position: Positions the center of the mirror split reflection.

�Center Size: Lets you shrink or expand the cells comprising the kaleidoscopic image.

�Angle: Lets you adjust the angle of the seam along which a reflection will run.

�Number of Sides: Three sides produce a triangular pattern, while four sides produce a rectalinear

pattern aligned with the currently selected angle.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Pencil Sketch in DaVinci Resolve

(Studio Version Only)

A plugin with highly customizable controls for making an image look like it was drawn.

�Color Sketch: Check this box to toggle between a color or grayscale sketch.

�Sketch Stroke Controls: Parameters to control the thickness of outlines, the threshold at which

they appear around objects in the frame, and their length.

�Sketch Tone Controls: Parameters to control how many levels of tonality are in the rendered

result, and contrast controls to influence how much of the image falls into shadows, mid-tones,

and highlights.

�Sketch Texture Controls: Parameters to apply a customizable stippled texture over the image,

with a checkbox to auto animate it.

(Top) The original image, (Bottom) The image with Pencil Sketch applied


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Prism Blur

Simulates flat chromatic aberration and a vignetted lens.

�X and Y Position: Let you change the center of the effect within the frame about which chromatic

aberration is created.

�Blur Strength: Lets you blur the primary image.

�Aberration Distance: Adjusts how far the aberration effect appears from the source image.

�Aberration Strength: Intensifies the zoom blur used to create the chromatic aberration

effect to intensify it.

�Vignette Size: Lets you add edge vignetting to the image; setting this to 0 removes the vignette,

while 1 is the maximum size of a vignette using this filter.

�Vignette Sharpness: Lets you adjust the feathering of the vignette effect; lowering this value

softens the edge, while raising this value sharpens, but never fully eliminates the softness

from this edge. The Vignette effect is designed to fall off in a way that simulates how a lens

would exhibit vignetting.

Scanlines

Simulates television scanlines, or any effect where you want alternating lines to darken the image.

A variety of parameters makes this an extremely flexible effect that can be applied in numerous ways.

Appearance

Let you customize the type of scanline effect you want.

�Line Frequency: Lets you choose how many or few lines are superimposed on the image;

fewer lines automatically space themselves to be thicker as they’re uniformly distributed

across the image.

�Line Sharpness: Lets you blur the border between each line, softening the effect.

�Line Angle: Lets you rotate the lines to appear at any angle; the default is 0 which results in

horizontal lines.

�Line Width: Lets you increase or decrease the width of the blanking lines that obscure the image

(which default to black but are tinted by the Color 2 parameter), thus increasing or decreasing the

amount of image showing through.

�Line Shift: Lets you offset the lines being overlaid on the image. Animating Line Shift lets you

create a rolling scanlines effect.

Color

Lets you tint and shift channels of the alternating scanlines created by this filter. Exaggerated, this can

create numerous other stylistic effects.

�Color 1 and Color 2: Color picker and eyedropper controls that let you tint each alternating set of

lines (eyedroppers let you sample a color from the RGB image being input into the current node).

�Red, Green, and Blue Offset: Lets you offset individual channels.

�Scanlines Only: Lets you see just the scanlines in isolation while you adjust them.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Composite

Lets you choose how to composite the scanlines effect against the original image.

�Scanlines Only: Lets you output an image consisting only of the scanlines patter you’ve created.

Good for creating different kinds of patterned textures and mattes.

�Composite Type: Lets you choose which composite mode is used to blend the scanline effect into

the image.

Sky Replacement

Replacing a drab, colorless sky with a more vibrant one or matching skies shot on different days are

common colorist tasks that are made more efficient with the Sky Replacement effect. The benefits

of using Sky Replacement instead of traditional compositing methods are a focused specific toolset

allowing you to:

�Dynamically match the foreground to the brightness and color cast of the sky.

�Use Tracking options to move the sky along with the clip’s camera movement.

�Add realistic computer generated sky elements, like sky color, horizon haze, clouds,

and light sources.

(Top) The original bland sky, (Bottom) The image with a new better looking sky.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR