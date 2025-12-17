---
title: "Selecting the Sky to be Replaced"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 649
---

# Selecting the Sky to be Replaced

It should be noted that the Sky Replacement effect does not do any sky selection itself, but rather

takes that selection from other tools and focuses on blending the selection seamlessly with either a

background plate of another sky or its own artificial sky generator. The benefit of separating the sky

selection and the replacement tools is deliberate, as qualifying a sky is usually trivial, while getting a

good mask at the horizon is not. This allows the colorist to use the right qualifier (HSL, Window, Magic

Mask, etc.) for the particular scene, and then pass that on to the Sky Replacement effect. Another

benefit of this arrangement is that the Sky Replacement effect can be applied to the same node as

your qualifier, letting you select and replace the sky all in one node, and both tools can be updated

concurrently as you use them.

To select the sky to be replaced and connect it to the Sky Replacement FX:


In a color node, use any Qualifier (Power Window, HSL, 3D, Magic Mask, etc.) to get a clean key of

the sky and horizon.


Then drag the Sky Replacement effect from the Effects Library onto the same node.


Or create a new color node, drag the alpha output from the previous node (blue square), to the

alpha input of the new node (blue triangle), and drag the Sky replacement effect from the Effects

Library to the new node.

Selecting the Replacement Sky

Once your original sky is qualified, you have two choices on what to replace the sky with, either an

artificially generated sky (created in the Sky Replacement Parameters below), or new footage of a

previously shot sky as a background plate.

To connect a sky background plate to the Sky Replacement FX:


In a color node, qualify the sky and add the Sky Replacement FX.


Right-click on the node with the Sky Replacement FX, and select Add OFX Input from the

drop‑down menu. An additional color and alpha input appear on the node.


Drag the clip of the sky background plate from the Media Pool into the Node tree to make a new

external matte of the clip.


Add a serial node off the external matte to make a new color node, so you can reposition and

grade the sky background plate as necessary.


Connect the color output of the new color node (green square) to the Sky Replacement color input

(the lower green triangle on the node). This will now use the video of the background plate for the

sky replacement.

The node tree showing

how to add your own sky

background plate footage to

the Sky Replacement effect.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Sky Mask Adjustments

These options let you make final adjustments to the source mask from whatever qualifier you’ve used.

�Preview Mask: Check this box to see the mask as a black and white matte; white is where the new

sky will come through.

�Shift Edge: Shifts the mask boundary into, or away from, the horizon.

�Refine: Adjusts the mask boundary to the image edges.

�Black Level: Adjusts the transparency level of the mask.

�White Level: Adjusts the opacity level of the mask.

Source Sky Appearance

These tools let you customize the look of the new incoming sky. They have no effect on the artificial

sky, but only on a video clip used as a sky background plate.

�Color Space: Lets you adjust the incoming sky’s color space. Defaults to timeline settings.

�Gamma: Lets you adjust the incoming sky’s gamma. Defaults to timeline settings.

�Detail: Lets you adjust the incoming sky’s midtone detail.

�Brightness: Lets you adjust the incoming sky’s brightness.

�Saturation: Lets you adjust the incoming sky’s saturation.

�Temperature: Lets you adjust the incoming sky’s color temperature.

�Tint: Lets you adjust the incoming sky’s tint.

�Opacity: Lets you adjust the incoming sky’s opacity, if you want to blend it in with the sky from the

original footage.

The same car shot with a more dramatic storm footage used as the

replacement sky, adjusted with the Source Sky Appearance tools.

Artificial Sky

These options let you generate realistic looking artificial sky elements. They are broken into three

categories: Sky, Cloud, and Hotspot (stand in for the sun or moon). By default, the opacities for these

elements are all set to zero (off). In order to see them, you must increase the opacity for each category

to a positive number.

�Preview Artificial Sky: Checking this box shows all the Artificial Sky categories alone, without

being composited with the foreground plate.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

�Sky Opacity: Lets you adjust the opacity of the sky. Zero is totally off, and one is completely

opaque. Any value in between is used to blend the artificial sky in with the source sky.

�Sky Color: Lets you set the color of the sky.

�Horizon Color: Lets you set the color of the horizon haze that blends with the sky color.

�Horizon Softness: Lets you adjust how soft the horizon blends into the sky.

�Horizon Height: Lets you set how high the horizon reaches in the frame.

�Horizon Angle: Lets you adjust the angle of the horizon.

�Cloud Opacity: Lets you adjust the opacity of the clouds in regards to the sky. Lower values blend

the clouds in more; higher values make them stand out.

�Cloud Color: Lets you set the color of the clouds.

�Cloud Scale: Lets you set the size of the noise pattern that creates the clouds, letting you choose

how close the clouds are to the foreground.

�Cloud Shape: Lets you adjust the horizontal/vertical ratio of the clouds. Lower values equal puffier

(cumulus) clouds, while higher values make them more lengthened (cirrus).

�Cloud Tilt: Lets you adjust the angle of the sky relative to the ground, to match the

foreground angle.

�Cloud Detail: Lets you determine the ratio of large to fine detail in the clouds.

�Cloud Fill: Lets you adjust the amount of cloud cover in the sky.

�Cloud Contrast: Lets you adjust how contrasty the cloud cover is compared to the sky.

�Cloud Time: Lets you change the noise pattern of the clouds. Using this control with keyframes

will let you change the cloud pattern over time.

�Hotspot Brightness: Lets you adjust the intensity of the hotspot. Zero is no hotspot. There is an

on-screen control for this option in the Viewer.

�Hotspot Color: Lets you adjust the color of the hotspot.

�Hotspot Position: Lets you adjust the position of the hotspot. There is an on-screen control for this

option in the Viewer.

�Hotspot Size: Lets you adjust the size of the hotspot.

�Hotspot Sharpness: Lets you adjust the sharpness of the edges of the hotspot.

Sky Position

These tools let you track the motion in the foreground clip, in order to realistically move the sky along

with any camera movement.

�Match Motion: Lets you choose which tracking method to use.

Keyframing Only: Lets you manually adjust the sky movement by keyframing the position controls.

Track Foreground: Automatically performs a track based on the foreground

elements in the composite.

Track Original Sky: Automatically performs a track based on the sky in the original clip.

Only works when the sky has existing details like clouds. This is the best and most reliable

tracking method to use if your footage allows.

Use FX tracker: Links to the track generated by the FX tracker in the tracker controls.

�Adjust Size: Lets you adjust the size of the sky, so that it can cover the range of motion

defined in the tracker.

�Adjust Position: Lets you manually adjust the X and Y positions of the sky.

�Auto-Size for Motion: Analyzes the track and automatically sets the size and position of the sky to

encompass the track’s extents.

�Flip Horizontal: Flips the sky on its horizontal axis.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Sky Integration

These controls help you match the attributes of the final sky to the foreground footage.

�Preview Final Sky: Check this box to view only the final sky output, including motion and any

keyframed parameters.

�Lens Distortion: Adjust this to warp the sky to match the curvature of the original camera lens.

�Lens Defocus: Adjust this to move the sky out of focus and match the depth of field of the

original lens.

�Exposure: Lets you adjust the overall brightness of the sky.

�Add Grain: These controls are a simplified set of tools to emulate the grain patterns found on

motion picture film. Check this box to turn the grain pattern on or off.

Grain: Determines the amount of grain to add in the sky.

Size: Determines the size of the grain in the sky.

Softness: Determines how crisp the individual grains are.

Saturation: Adds color to the grain. 0 is monochromatic.

Foreground Appearance

Turning on these controls automatically attempts to adjust the overall look of the foreground, based on

an analysis of parameters of the final sky.

�Adjust Foreground: Check this box to activate the Foreground Appearance tools below.

�Auto Adaptation: Selects the method by which the Foreground Appearance analysis is generated.

None: No automatic settings are applied. You can manually adjust the parameters below.

Globally Applied: The color cast is calculated from the visible sky and then applied globally to the

foreground, with no variations in brightness. However, the color cast will update dynamically if the

sky changes over time.

Match Horizon: The color cast is calculated from the visible sky but is weighted towards the

horizon, its distance set with the Localization control. This will make brighter/darker areas of the

sky apply bright/darker changes to the foreground. For example, if you have a dark sky but a

moon on the horizon, the foreground will be brighter around the moon than elsewhere. This also

updates dynamically over time.

�Adaptation Amount: Lets you select how much adaptive color adjustment to make.

�Localization (Match Horizon only): Lets you determine how far or near the color

cast reaches from the horizon.

�Brightness: Lets you adjust the foreground’s gain or brightness.

�Saturation: Lets you adjust the foreground’s saturation.

�Temperature: Lets you adjust the foreground’s color temperature.

�Tint: Lets you adjust the foreground’s tint.

Sky Replacement Workflow

Here’s a sample workflow for replacing the sky with one generated by the artificial sky tools.

This is the original clip, with the sky we want to replace. To start with, we simply make a new

color node.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

The original shot we want to replace the sky on.

Next we need to qualify the sky. For this clip, we can apply the Magic Mask (object) tool to the node

to select just the sky we want to replace. You could also use the HSL qualifier, 3D qualifier, or even a

power window to do the same thing.

The sky qualified using the Magic Mask tool.

Now that the sky is selected, we can drag and drop the Sky Replacement effect from the

Effects Library onto the same node that our Magic Mask is on.

The black area is where we will create our new sky.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Now that both toolsets are active on the same node, we can adjust both the Magic Mask and the

Sky Replacement parameters at the same time. This makes the complete sky replacement a one

node process.

You can use both the Magic Mask (or any qualifier) and the Sky Replacement tools on the same node.

Using the Artificial Sky Controls, we can create a new, more interesting sky. Then, using the Sky

position tools, we can track the sky to the camera movement of the original clip. Finally, adding the

Foreground Appearance toolset, we can seamlessly blend the foreground and sky together.

The final replaced sky that tracks with the camera movement.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR