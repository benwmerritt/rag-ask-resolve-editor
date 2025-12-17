---
title: "Output"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 633
---

# Output

The Output controls let you choose how the image is output, composited, and displayed in the Viewer.

�Output: This menu offers three options for which channels are output from the effect.

Alpha Highlight: Displays the transparent part of an Alpha channel as gray and the solid part of an

alpha channel in full color.

Alpha Highlight B/W: Displays the black and white Alpha channel, which is often helpful when

sampling additional areas to key.

Final Composite: The keyed image is displayed composited over any video track below it.

�Use Alpha: A common control in many Resolve FX and 3rd party Open FX plugins; this checkbox

determines if the Alpha channel is used when compositing over another video track. It can be

used instead of choosing RGB Only (Blank Alpha) from the Output menu.

To use the Luma Keyer in the Edit page to key a subject:


Apply the Luma Keyer to a clip on video track 2 or higher.


From the Viewer Overlay menu in the lower-left corner of the Timeline Viewer choose

Open FX Overlays.


Either click a pixel in a bright or dark part of the image you want to key out, or click and drag

across a range of pixels within that subject.


The transparency immediately takes effect, showing the keyed subject against whatever clip

appears on the video track underneath it in the Timeline as a composite. To see the matte you

created for further adjustment, choose Alpha Highlight or Alpha Highlight B/W from the Output

drop-down menu.


To add or subtract from the matte, click the plus or minus Luma Range buttons, and then click or

drag across the portion of the keyed image.


To add softness to the outer range of the key you’re creating, click the plus Softness button and

then click or drag across the portion of the image you’d like to include as a soft edge.


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR

Chapter 160

Resolve FX Light

The plugins in this category all replicate different optical and lighting effects.

While most have been designed to quickly give you realistic results, all can be

pushed harder to provide many artistic effects.

Contents

Aperture Diffraction (Studio Version Only)����� 3510

Output��������������������������������������������������������������������������������� 3511

Isolation Controls��������������������������������������������������������� 3512

Aperture Controls�������������������������������������������������������� 3512

Diffraction Controls����������������������������������������������������� 3512

Compositing Controls������������������������������������������������ 3512

Glow����������������������������������������������������������������������������������� 3513

Shape and Spread������������������������������������������������������� 3513

Color and Composite������������������������������������������������� 3513

Lens Flare (Studio Version Only) ������������������������� 3514

Lens Flare Preset��������������������������������������������������������� 3514

Select Output����������������������������������������������������������������� 3514

Light Source Masking������������������������������������������������ 3514

Position����������������������������������������������������������������������������� 3514

Global Corrections������������������������������������������������������ 3515

Aperture��������������������������������������������������������������������������� 3515

Elements��������������������������������������������������������������������������� 3515

Lens Reflections (Studio Version Only)������������� 3517

Output�������������������������������������������������������������������������������� 3518

Isolation Controls��������������������������������������������������������� 3518

Global Controls������������������������������������������������������������� 3519

Presets������������������������������������������������������������������������������ 3519

Reflecting Elements���������������������������������������������������� 3519

Light Rays���������������������������������������������������������������������� 3520

Main Controls��������������������������������������������������������������� 3520

Position��������������������������������������������������������������������������� 3520

Appearance������������������������������������������������������������������ 3520


Resolve FX Overview | Chapter 160 Resolve FX Light

COLOR

Aperture Diffraction (Studio Version Only)

Found in the ResolveFX Light category, Aperture Diffraction models the starburst effect usually seen

when shooting bright lights with small apertures, the physical cause of which is light-diffraction on

the aperture blades of a lens. This plugin simulates this, with the result being automatically applied to

scene highlights that you can isolate and refine, with customizable virtual apertures.

Small regions of brightness exhibit a star pattern glow, as seen in the following image.

(Top) Original image, (Bottom) Applying Aperture Diffraction

Large regions of brightness exhibit a more even glow with shaping and texture that look like a natural

optical effect. It can be used to create a different type of glow effect with a more realistic look in some

situations than the Glow plugin, though it’s more processor intensive. In other situations, this plugin

opens up many different stylistic possibilities for glowing effects.


Resolve FX Overview | Chapter 160 Resolve FX Light

COLOR

(Top) Original image, (Bottom) Applying Aperture Diffraction

Output

These controls let you choose what image is output by this plugin.

�Select Output: Lets you preview the image with different stages of the Aperture Diffraction

effect applied.

Isolated Source: Used to help when adjusting the Isolation controls.

Preview Aperture: Used to help when adjusting the Aperture controls.

Preview Diffraction Pattern: Shows you the resulting diffraction pattern based

on the aperture control settings.

Diffraction Patterns Alone: Shows you the glow effect that will be applied to the image by itself.

Final Composite: Shows you the final output of the effect.

�Alpha Masks Light Sources: Check this box to use the input Alpha channel to exclude sources in

those areas from casting light rays.

�Alpha Limits Effect: Check this box to use the input Alpha channel for compositing purposes.

Unchecking means the input Alpha is ignored.

�Quality: Lets you choose a quality setting to trade off between quality and speed. Choices are

Full, Half (Faster), Quarter (Fast). High quality gives diffraction of finer detail, but otherwise does

not change the effect. If you have no small light point sources, you can safely use half or quarter

qualities with no reduction in image quality.


Resolve FX Overview | Chapter 160 Resolve FX Light

COLOR

Isolation Controls

The Isolation controls let you choose which highlights in the scene generate visible glow and patterns.

The effect of these controls can be directly monitored by setting Select Output to Isolated Source.

�Color Mode: A pop-up menu that lets you either choose to keep the colors of the different

highlight regions that generate glow, or treat them all as grayscale brightness only (color

controls later can change the effect). Grayscale is faster to process, but Color can result in some

brilliant effects.

�Brightness: Sets the threshold at which highlights are isolated.

�Gamma: Lets you shape the isolated highlights.

�Smooth: Lets you blur details in the highlights that you don’t want to be pronounced.

�Color Filter: Lets you choose a particular color of highlight to isolate (an eyedropper lets you

select a value from the Viewer).

�Operation: Lets you adjust the resulting Isolation matte (options include Shrink, Grow, Opening,

Closing) with a slider to define how much.

Aperture Controls

The Aperture controls let you define the shape and texture of the resulting glow this plugin creates.

�Iris Shape: Lets you choose a shape that determines how many arms the star pattern will have.

Options are Triangle, Square, Pentagon, Hexagon, Heptagon, and Octagon.

�Aperture Size: Lets you alter the resulting diffraction pattern alternating between more of a star

shape at higher values and a stippled wave pattern at lower values.

�Blade Curvature and Rotation: Lets you alter the softness and orientation of the arms of each star.

�H/V Ratio: Alters the horizontal/vertical ratio of the aperture, allowing you to replicate an

anamorphic glow.

�Angle: Sets the angle of the aperture.

�Chroma Shift: Lets you introduce some RGB “bleed” into the glow.

Diffraction Controls

�Result Gamma: Lets you adjust how pronounced will be the glow that appears between the arms

of the star patterns that appear.

�Result Scale: Lets you alternate between pronounced star patterns at high values and more

diffuse glows at low values.

Compositing Controls

These controls let you adjust how to composite the glow effect against the original image.

�Normalize Brightness: This checkbox scales the brightness of the glow per frame. The Aperture

Diffraction effect will keep to a consistent overall brightness as the scene changes.

�Brightness: Lets you adjust the intensity of the glow effect.

�Colorize: Lets you tint the glow effect using the Color control that appears below.


Resolve FX Overview | Chapter 160 Resolve FX Light

COLOR