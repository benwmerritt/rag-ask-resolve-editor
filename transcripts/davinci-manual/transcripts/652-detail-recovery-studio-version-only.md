---
title: "Detail Recovery (Studio Version Only)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 652
---

# Detail Recovery (Studio Version Only)

Detail Recovery is a utilitarian effect that lets you extract image detail from the second input, in order

to re-add it to the image coming in the first input. In this way, you can selectively add detail back to an

image in which it’s been removed. Because of how it works, this is an effect that’s intended to be used

on the Color page.

To use Detail Recovery, you must add it to the node tree as a Resolve FX node (dragging it directly

from the Open FX library into the node tree as its own node), in order to expose both of the RGB

inputs that appear on the node when you do this. By default, the first RGB input is for the image you

want to add detail to, and the second RGB input is for the image you’re extracting image detail from.

In the following example, Node 1 is the base grade, and Node 2 is a grade in which the

highlights are being blown out for stylistic effect. The Detail Recovery node is then being

added to add specific image detail from Node 1 back to the output of Node 2.

Setting up the Detail Recovery effect to add image

detail from Node 1 to the image coming from Node 2

The result, compared with the image in Node 2, is an image that’s still harshly exposed, but

that has traces of fine image detail so it doesn’t look so clipped.


Resolve FX Overview | Chapter 167 Resolve FX Texture

COLOR

(Top) The image with highlights compressed harshly, (Bottom)

The image with high-frequency detail added back

Detail Recovery has the following parameters.

Detail Recovery

�Transfer Direction: This drop-down menu lets you choose which input provides the detail and

which input the detail is combined with.

Details Extraction

�Frequency Cutoff: A slider that lets you choose how much detail you want to extract for recovery.

Lower values isolate finer details; higher values include progressively larger details.

�Detail/Edge Balance: This lets you choose between recovering all details or from the stronger

edges only.

�Strength: This slider lets you exaggerate or attenuate the detail that’s extracted for recovery.

�Detail Mix: At a value of 1.000, this slider blends the extracted detail with the image you’re adding

it to so that both layers blend together. At a value of 0.000, the extracted detail replaces whatever

overlapping pixels are in the image you’re adding it to. Using this slider, you can choose the best

blend for your purposes.

�Preview Detail checkbox: Turning this checkbox on lets you see the detail that’s being extracted

using the Frequency Cutoff and Strength sliders.


Resolve FX Overview | Chapter 167 Resolve FX Texture

COLOR

Fast Noise

Fast Noise creates computer-generated noise patterns that can be composited on, or used to warp a

video clip for a variety of special effects, such as smoke, haze, or water ripples.

Original image

The image with Fast Noise’s Smoke preset applied.

The onscreen controls for position and rotation are visible.


Resolve FX Overview | Chapter 167 Resolve FX Texture

COLOR

Appearance

Controls for what noise pattern is generated. All parameters are keyframeable for changing the noise

pattern over time.

�Preset: Select from some common noise pattern use cases: Mist, Smoke, Water Surface, River, and

Heat Haze. Default is the standard noise pattern, and Custom is auto-selected if you change any

of the parameters below.

�Scale: The size of the noise pattern.

�H/V Ratio: Controls the horizontal/vertical spread ratio.

�Detail Level: How many levels of fine detail to generate.

�Detail Balance: Applies weighting to the different scales of detail. The slider lets you choose

between stronger large detail or stronger fine detail. A value of 0.000 removes fine detail entirely.

�Evolution: Changes the noise pattern gradually. This slider controls the “progress” of the noise

pattern over time, rather than just modifying its current state.

Adjustment

Controls for adjusting the parameters of the noise pattern once it’s been generated. Especially useful

for modifying the noise pattern’s Alpha channel for compositing. All parameters are keyframeable for

changing the noise pattern over time.

�Brightness: Increases or decreases the gain of the noise pattern.

�Contrast: Moving this slider to the right makes the light areas lighter and dark areas darker in the

noise pattern, increasing the contrast. Moving it to the left reduces the contrast.

�Saturation: This slider controls the scale between a grayscale and color noise pattern.

A value of 0.000 is completely grayscale, and a value of 1.000 is fully color.

�Color Tint: Sets the overall color of the effect.

�Invert Dark Regions: Check this box to invert the dark regions to white and darken the edges in

the noise pattern.

�Invert Pattern: Check this box to invert the color of the noise.

�Allow Negative Values: Check this box to apply negative values to the Output section below.

Position

Controls that adjust the center and direction of the noise pattern.

�Position X/Y: Location of the center of the noise pattern.

�Rotation: Rotates the noise pattern around its center.

�Position Reference: Controls how to position the effect when a clip is re-sized or

moved in the Timeline.

Sizing and FX Tracker: The noise pattern follows Sizing and FX Tracker adjustments in the Color

page. For example, if you used the FX Tracker to track a camera pan, the noise pattern would

move with the pan, rather than stay in one place as the shot panned underneath it.

Keyframed Positions: The noise pattern position can be adjusted as normal using keyframes.

The position and rotation controls can also be adjusted directly in the Viewer when the Open FX

Overlay mode is selected from the drop-down menu in the bottom left of the Viewer. Dragging the

star in the Viewer adjusts the X/Y position. Dragging the circle clockwise or counterclockwise sets

the rotation.


Resolve FX Overview | Chapter 167 Resolve FX Texture

COLOR

Auto-Animation

These controls allow you to adjust the animation of the noise pattern.

�Velocity X/Y: How far to automatically advance each frame from the start position. You can

keyframe these controls to change the noise pattern’s direction, without adjusting its actual X/Y

position. This lets you mimic motions like smoke changing direction in the wind.

�Seethe: Controls how far to automatically evolve each frame from the starting Evolution value.

�Randomize Start Frame: Aligns the skipping cycle to the current frame. This allows you to re-use a

favorite effect in multiple clips without it looking exactly identical in each instance.

�Start Frame: Lets you set the reference frame for the skip pattern. This allows you to control the

sequence of noise you get, just in case you need to match it to the same noise pattern on another

clip. This frame will be repeated.

Output

These controls allow you to choose how to adjust the output of the noise pattern.

�Preview Noise: Checking this box shows the noise pattern alone.

�Output: Choose how to use the noise pattern.

Composite Onto Clip: The noise pattern is placed on top of or mixed into the video clip.

Composite Type: Selects composite mode for the noise pattern.

Put Into Alpha Channel: The noise is inserted into the node’s Alpha channel, allowing you to use

the noise pattern for compositing purposes. Please note, you will also need to right click on the

node and select “Use OFX Alpha” to activate this setting. Alternatively, you can drag the Fast

Noise effect directly into the Node Graph as an FX Node instead of applying it to a corrector node,

and you can use the Alpha without additional settings.

Use to Warp Image: The noise pattern is used to distort the image.

Input Alpha: Controls what to do with the input Alpha channel.

�Limits Warping Effect: Limits the warp to certain areas as defined by the Alpha channel. For

example, when you want to have a water ripple or heat shimmer on only certain part of the clip.

�Gets Warped as Well: The warp affects the Alpha channel in addition to the RGB channels. For

example, when warping a logo with a transparent background.

JPEG Damage

Simulates the kinds of minor or major artifacts you get when doing JPEG compression; useful for

simulating compression damage.

�Quality: Lets you lower the bit depth of the image.

�Resolution: Lets you increase the size of macroblocking artifacts that appear.

�Block Aspect Ratio: Lets you adjust the macroblocks to be more square or rectangular.

�Frequency Scale: Sharpens the effect.

�Scale Component: Lets you base this effect on All Frequencies, the X-Frequency, or the

Y-Frequency.


Resolve FX Overview | Chapter 167 Resolve FX Texture

COLOR