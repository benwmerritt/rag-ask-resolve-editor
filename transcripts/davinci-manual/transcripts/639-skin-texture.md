---
title: "Skin Texture"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 639
---

# Skin Texture

The Skin Texture controls have three operating modes that let you choose the method you want to use

to control skin texture. Beauty Automatic and Beauty Advanced provide the texture controls available

in the Beauty plugin, while Smoothing provides the previously available texture adjustment controls.

Beauty Automatic Controls

Automatic mode reveals easy-to-use controls for smoothing or coarsening detail.

�Amount: Lets you choose how much smoothing or coarsening to apply.

�Scale: Lets you reduce or increase the amount of smoothing or coarsening that’s accomplished

with the range of the Amount slider.

Smoothing Controls

�Smoothing: This slider removes detail from the areas isolated by the Skin Mask controls,

smoothing the complexion. Its operation depends on the settings of the Detail Size and Detail

sliders below. You may find you can increase Smoothing more dramatically as you increase Detail

using the Detail Size and Detail sliders described below.

�Detail Size and Detail: Once you’ve used the Smoothing slider, you can then use these sliders to

selectively put subtle skin details back into the image; Detail Size determines the maximum size of

details you want to put back into the face, and Detail is a sharpening operation that lets you adjust

how visible these small details are. By combining smoothing and subtle preservation of small

details, you can get a much more naturalistic result than were you to simply leave the entire face

unnaturally smooth.

(Top Left) The original image, (Top Right)

Only smoothing complexion, (Bottom Left)

Using Detail Size and Detail to put

natural texture back into the smoothed

result (results exaggerated for print)


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

Beauty Advanced

These controls are identical to the Advanced controls of the Beauty plugin, covered previously in

this chapter.

Color Grading

These controls let you make color adjustments to the overall face.

�Contrast: This slider lets you lighten the face in a natural way by keeping the shadows dark, even

while you brighten the face, making it easy to bring actors out of the background.

�Midtone: Lets you add a more luminous quality to the skin tone.

�Color boost: Specifically boosts saturation in the lowest saturated parts of the face.

�Tint: Provides a limited range of naturalistic hues emphasizing orange through red (but extending

to green and magenta) with which to tweak complexion.

�Desaturate shadow: This slider lets you selectively desaturate the darkest shadows on the face

to keep things looking natural, or to desaturate more aggressively in order to stylize the face in a

different way. Also useful when using the other adjustments of this plugin makes the shadows too

colorful. Moving this slider into negative values will add saturation.

�Shine Removal: This slider is an inverse contrast adjustment designed to ameliorate sweat

and shine on a person’s face, although moving this slider into negative values will also

accentuate shine.

Side Lighting

These controls allow you to fill in or accentuate shadows and balance the light between the sides

of the face.

�Lift Left/Right: Adjusts the dark parts of the image for a side of the face.

�Gamma Left/Right: Adjusts the midtone parts of the image for a side of the face.

�Gain Left/Right: Adjusts the bright parts of the image for a side of the face.

�Area Size: This control lets you adjust the size of the area of influence of the side lighting.

�Bias Left/Right: Normally the left and right sides of the face are split right down the nose. You can

use this control to manually adjust the center of the effect, if necessary.

�Area Softness: This control adjusts the softness of the effect around the side of the face.

Eye Shadow

These controls give extensive control of the eyelids and sockets, without manipulating the eyes

themselves. Used subtly, it can easily remove bags under the eyes, or accentuate makeup details.

Used aggressively, you can create realistic eye makeup effects from nothing. There are separate

controls for the upper and lower eyelid areas.

�Temp Upper/Lower: Adjusts the color temperature of the eyelid.

�Tint Upper/Lower: Adjusts the tint of the eyelid.

�Hue Upper/Lower: Adjusts the color of the eyelid.

�Saturation Upper/Lower: Adjusts the saturation of the eyelid.

�Gamma Upper/Lower: Adjusts the gamma of the eyelid.

�Size Upper/Lower: Adjusts the size of the area of the eyelid modifications.

�Softness Upper/Lower: Adjusts how soft the blending is between the eyelids and the face.

�Strength Left/Right: Lets you set different strengths for the left or right eye to compensate for

lighting differences between the sides of the face.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

(Left) The original image, (Right) using the Eyeshadow tools to change

the model’s upper eyeshadow color to purple and increase the intensity

Eye

These controls target just the eyes and surrounding area of the face.

�Sharpening: This slider lets you selectively add sharpening just to the eyes and eyelashes, which

lets you instantly add focus to any performer.

�Brightening: This slider lets you whiten the eyeballs.

�Eye Light: This slider lets you brighten the region of the face around the eyes that’s often thrown

into shadow by the subject’s forehead in situations with imprudent lighting.

�Eyebag Removal: This slider uses a variety of techniques to smooth, color-adjust, and brighten the

area under the eyes most susceptible to eye bags with tired talent.

(Left) Eyes with no special adjustment, (Right) eyes with adjustment

Lips

These controls target just the lips and surrounding area of the mouth.

�Hue Shift: This slider lets you adjust the color of a subject’s lips or lipstick.

�Saturation: This slider lets you adjust the intensity of lip color.

�Gamma: This slider lets you adjust the lip brightness using a gamma curve.

�Upper Lip Smooth: Lets you smooth out fine age lines that can appear above lips.

�Mouth Corners Inner/Outer: Adjusts the side corners of the mouth.

�Top Inner/Outer: Adjusts the top boundary of the lips.

�Bottom Inner/Outer: Adjusts the bottom boundary of the lips.

�Softness: The softness of the blend between the mouth area and the rest of the face.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

Teeth

A smile can hide a thousand lies, but just these three controls can accentuate the teeth.

�Blue Gain: This control is used to color balance the teeth, making them whiter or yellower

as desired.

�Gamma: This manipulates a gamma curve allowing you to set how bright a smile the subject has.

�Mask Softness: The softness of the blend between the teeth and the rest of the face.

Blush

The parameters in this group let you modify the hue of the blush region of a subject’s cheek, letting

you correct an unwise makeup choice, or push a subject’s blush color around to add makeup that

wasn’t there.

�Hue: This slider lets you adjust the hue of the cheeks.

�Saturation: This slider then lets you intensify or remove blush color.

�Size: This slider lets you adjust the size of the blush area of the cheeks.

About Forehead, Cheeks, and Chin Retouching

The next three groups of controls borrow a technique from portrait painters, who’ve long taken

advantage of the “traffic light” approach to rendering skin hues that observes that foreheads are often

a bit yellow, the middle of the face is usually a bit red, and chins can be a bit green. A combination of

unequal sun exposure, capillary distribution, and follicle growth account for this, but the bottom line

is that faces are seldom a single unified hue. This means that there may be a region of the face that

would benefit from individual adjustment (cheeks that have gotten too much sun, for example). But it

also means that when you allow a bit of hue variation into your face grade, you can achieve a more

naturalistic result.

(Left) A face graded with a single hue, (Right) a face graded with slight variation in the forehead, blush area, and chin


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

TIP: For a variety of reasons, people are extremely sensitive to the hues of skin tone, so

tiny variations that can be difficult to identify nevertheless have a significant impact on the

resulting visuals. Unless you’re aiming to create a special effect, these controls are meant to

be used sparingly.

Forehead

As the name implies, adjusts color and texture on the forehead.

�Hue and Saturation: These sliders let you adjust forehead color.

�Gamma: This manipulates a gamma curve allowing you to set how bright the forehead is.

�Smooth: This slider lets you apply a specific smoothing operation to the forehead to ameliorate

wrinkles and worry-lines.

Cheeks

Simple color adjustment controls affecting the entire cheek area, and not just the blush area.

Hue and Saturation: These sliders let you adjust the color of the cheek, eye, and nose area.

Chin

Simple color adjustment controls over the chin of the face.

Hue and Saturation: These sliders let you adjust the color of the chin, running up alongside the

sides of the face (the beard area).

Relight (Studio Version Only)

Relight allows you to add light sources to your scene, realistically illuminating the objects within it.

Unlike a Power Window whose shape is fixed on screen, Relight analyzes the shapes of people and

objects to create a Surface Map and uses that map to reflect light appropriately. When dialed-in

properly, this effect can provide the illusion of light following the curves of an object, reflecting off

highlights, and disappearing into shadows.

Relight is useful in situations when you wished you had another light in the scene, want to accentuate

an existing light to match another shot, or increase the realism of day-for-night grading.

NOTE: The Relight effect creates the illusion of depth with its analysis of the surfaces in

a scene, but it does not calculate 3D relationships between objects in the scene. Shapes

cannot be made to cast shadows, and depth information cannot be produced.

Setting up Relight

Analyzing the image to create a Surface Map is very computationally intensive. Calculating the effects

of light sources to an existing analysis is comparatively very fast. By default, adding Relight to a node

will create the map and add a light in one step. This is convenient, but adjusting the light position

re-runs the effect, and hence re-runs the analysis. So it can be slow to work with unless you have an

extremely powerful computer. Fortunately it is possible to split the work across two nodes, caching

the analysis in the first node and adjusting the light positions in the second node. This is described in

detail below.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

Note that you can add multiple light sources reusing the same analysis. If you have, say, three separate

lights in the same scene, reusing one analysis, then this will run three times faster than repeating the

analysis for each light.

And as an advanced option, the split approach allows you to use a Surface Map which has been

saved out to file, or a Surface Map from other software. Computer graphics software can often

render “surface normals” of 3D models along with the images they create and these can be made

compatible with Relight. In this context a “normal” is a geometric term describing which way a surface

is oriented. There is no universal format for surface normals; see the External Map settings for some

options which can help with using these as Surface Maps in the plugin.

Here is a sample node graph splitting the Relight in two:

How to set up a dual Relight Node Tree with two separate Relight nodes, configured as above.

These have been labeled Surface Map and Lighting for clarity.

In the above example, you have the source video

and two Relight nodes. This is how they’re set up:

•	 The source video is connected to the first RGB input (top green triangle) of both nodes.

•	 The first Relight Node ((RLT) Surface Map) creates the Surface Map for the image by

selecting “Output Surface Map” checkbox in the Relight effect’s settings. When checked,

the plugin goes into analysis-only mode and other options disappear. You can enable Node

Caching to automatically generate the Surface Map in the background when you aren’t

using DaVinci Resolve. The RGB output of this node is connected to the second RGB input

(bottom green triangle) of the second Relight Node.

•	 In the second Relight Node ((RLT) Lighting), set the first option “Surface Map” from its default

(“Use Internal”) to “Use Input 2.” The other settings all remain visible; this node is where you

will adjust the light properties.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

You can add Power Windows, Qualifiers, or masks to either node, or to separate nodes and

connect them via the first Alpha channel (top blue triangle) of either node. For example, you

could select a person using the magic mask and use it to limit the lighting to just that person

and not the background.

The output of the Relight Surface Map.

This goes into the input of the Relight Lighting node.