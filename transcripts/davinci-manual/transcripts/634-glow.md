---
title: "Glow"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 634
---

# Glow

A sophisticated, soft glow effect that’s highly customizable with only a few key parameters.

�Select Output: Lets you preview the image with different stages of the glow effect applied,

viewing the Shiny Regions, the Glow Alone, or the Glowing Image.

�Shine Threshold: Defines the luminance level at which glow is triggered to appear on the image.

�Alpha Masks Light Sources: Check this box to use the input Alpha channel to exclude sources in

those areas from casting light rays.

�Alpha Limits Effect: Check this box to use the input Alpha channel for compositing purposes.

Unchecking means the input Alpha is ignored.

Shape and Spread

�Spread: Defines how far out shine extends from areas of the picture that trigger it.

�H/V Ratio: Lets you adjust the proportion of horizontal to vertical spread, allowing you to create

“streaky” shine that extends farther in a particular dimension.

�Relative Spread Red/Green/Blue: Lets you adjust the spread within each color channel by a

different amount, simulating a kind of chromatic aberration in the glow.

Color and Composite

�Gain: Adjusts the brightness of the glow effect.

�Gamma: Adjusts the spread of the glow effect and how it fades with distance.

�Saturation: Adjusts the intensity of the glow’s color.

�Color Filter: A color picker and eyedropper let you choose a color with which to tint the glow.

�Glow framing: Lets you choose what happens when shine hits the edge of the frame, whether it’s

amplified by “Reflect in Camera” or whether it’s moderated by a “Vignette” effect.

�Composite Type: Lets you choose a composite mode to use to blend the glow effect with the

image. Defaults to Screen, which is good for gentle glows. Add lets you create hotter, more

intense glows, while other composite modes let you create other varied effects.

�Opacity: Lets you adjust the transparency of the glow effect and is a fast way of “easing off” of a

glow that you otherwise like, but that’s too intense for the shot at hand.

�Invert Effect: Checking this box inverts the Glow parameters, so darker areas now affect brighter

regions instead of the other way around.

�Bright Region Recovery: Adjust this slider to reclaim some image detail in areas that are blown out

by the glow.


Resolve FX Overview | Chapter 160 Resolve FX Light

COLOR

Lens Flare (Studio Version Only)

Simulates different kinds of lens flares resulting from the interplay of light through an aperture of

selectable shape bouncing within layered optical elements in a lens. Four groups of controls give you

a lot of ways to customize the presets to create your own effect:

Lens Flare Preset

You can choose a type of flare from the Lens Flare Preset drop-down. If you manipulate the controls to

create your own effect, this drop-down switches to Custom.

Select Output

The Select Output drop-down lets you switch among the following viewing options:

�Final Image: (Default) Shows the lens flare composited against the current clip.

�Flare Elements Alone: Shows the isolated flare, making it easier to adjust.

�Source Mask and Magnified Source Mask: Let you see the mask used to control the

lens flare brightness.

Light Source Masking

Three additional controls at the top let you create a quick and dirty luma key to create a mask that you

can use for occluding the lens flare effect behind foreground elements in the scene. For example,

if you’re using lens flare to simulate the sun in the sky moving behind trees, these controls let you use

those tree silhouettes to shift and modify the flare source accordingly.

�Enable Light Source Masking: This checkbox enables the Mask Threshold and Virtual Light

Source Size sliders. You can then choose either Source Mask or Magnified Source Mask to see

the mask that’s created by raising the Mask Threshold slider.

�Mask Threshold: Raising this slider pulls a fast Luma Key that masks off darker foreground

elements (such as trees against the horizon) and limits the flare to areas of the picture where

the light source of the flaring can “shine through” (In this example, shining between the

trees on the horizon).

�Virtual Light Source Size: This slider determines how quickly the center of a flare will disappear

behind the luma-keyed mask you’ve created; higher values (simulating bigger light sources) cause

a flare to disappear more slowly when passing “behind” a feature of the image that’s being keyed

via the Mask Threshold slider.

Position

Position parameters let you adjust the X and Y Position of the simulated light source that’s causing the

flare. There are three ways you can adjust the flare position.

�You can Adjust the X and Y Position sliders.

�You can turn on the OpenFX Overlay in the Viewer and drag the on-screen control.

�You can motion track elements within the scene using the FX Tracker.

Checking the Move With Sizing checkbox lets the lens flare retain its relative position in the frame

if the Input and Editing sizing are changed.


Resolve FX Overview | Chapter 160 Resolve FX Light

COLOR

Global Corrections

The Global Corrections group have parameters that let you quickly adjust the overall quality of the

flare effect.

�Global Scaling: Lets you make every element of the flare effect larger or smaller at once.

�Anamorphism: Lets you stretch all flare elements horizontally to simulate an anamorphic lens’

stretching effect.

�Lens Center X and Y position: Lets you offset the center of the simulated lens that’s causing the

flaring, about which the various elements of the flare pivot.

�Global Defocus: Lets you blur the overall flaring effect being created to soften the effect.

�Global Brightness: Lets you raise and lower the overall level of flaring being produced.

�Global Saturation: Lets you adjust the overall color intensity of the flaring.

�Colorise Result: Lets you choose how much to tint the flare, if at all. At a value of 0 (the default), no

colorization is applied at all.

�Colorization Color: Lets you choose a color to use to colorize the flare via the Colorize Result

slider above. You can use either a color control or eyedropper to sample color from the source

RGB image of the current node.

Aperture

The Aperture parameters let you define the aperture of the simulated camera apparatus through which

the flare is being generated. The shape defined by these parameters affects the look of the “starburst

element” of each flare, as well as the look of any aperture-shaped “ghost elements” you’re turning on.

�Aperture Blades: Defines how many blades make up the aperture. You can choose from

3 to 16 (defaults to 6). The diffraction of the lens flares is symmetric, so an odd number of blades

will give you twice as many rays as the number of blades, while an even number of blades will give

you the same amount of rays.

�Angle: Sets the angle of the resulting Aperture shape.

Elements

The Elements drop-down is a deceptively simple set of controls that let you expose the customization

controls of each of the layers and elements that combine to create the simulated lens flare. Up to ten

levels of elements can contribute to a lens flare effect. Each element and ghost shape has a different

set of parameters unique to that type of element. Available elements in this pop-up menu include:

�Full-Screen Glare: A simulated overall flaring that covers the entire frame at its most intense.

This glare increases as the flare nears the center of the screen and decreases as the flare

moves toward the edges of the frame. Recommended for extremely big flaring effects.

Parameters include:

Glare Brightness: A slider; set this to 0 to eliminate glare.

Glare Color: A color picker and eyedropper combination that lets you tint the glare.

�Flare Spot: Simulates the central light source that’s triggering the flare. Parameters include Flare

Size (set this to 0 to eliminate the flare spot), Flare Irregularity (which lets you create a more

organic-looking, off-balance flare), Flare Softness, and Flare Color.

�Starburst: Rays of light stretching out from the center of the flare. Parameters include Starburst

Size (set this to 0 to eliminate the starburst), Starburst Softness, Starburst Split Angle (which splits

each streak of the starburst into a wider feathered pattern), Starburst Split Balance (which lets you

adjust the brightness between each half of split streaks), and Starburst Color.


Resolve FX Overview | Chapter 160 Resolve FX Light

COLOR

�Ghost elements: Seven available layers of Ghost Elements can be enabled and set to different

optional shapes for each lens element you want to simulate. Each of the Ghost element layers can

use one of five types of shapes, including:

None: Turns that particular ghost element off.

Aperture Shape: A polygonal shape defined by the number of blades in the

aperture you’ve selected.

Anamorphic Streak: A wide horizontal artifact typical of anamorphic lenses.

Disc Shape: A round ring artifact.

Bubble Shape: An oval with haze within.

Corona Rays: A ring of streaks stretching outward.

Ghost elements share many parameters in common, although specific

elements have unique parameters. These parameters are as follows:

Color: A color picker and eyedropper combination that lets you colorize that specific element.

Position: A slider lets you set that element’s position along the optical path that’s defined by

the angle from the (Flare) Position X and Y to the Lens Center X and Y parameters. A value of

0 centers that element on the Lens Position, while larger values push that element farther and

farther away from the Lens Position.

Size: Sets the size of that flaring element, or in the case of the Anamorphic Streak, the width.

Height: (Anamorphic Streak only) Sets the vertical thickness of the streak.

Center Brightness: (Aperture, Disk, and Anamorphic Streak only) Defines the brightness in

the middle of that element, filling it to appear as a solid element. Set this closer to 0 if you

want the element to appear hollow.

Edge Brightness: (All but Anamorphic Streak) Defines the brightness of the edge of that

element. Raising this value while lowering the Center Brightness lets you create outlined

element effects.

Softness: Lets you blur that element.

Bristle Density: (Corona Only) Lets you alter the number and arrangement of the optical

bristles that appear. At lower values, fewer bristles appear, at higher values, more bristles

appear. As you change the value of this parameter, the placement of bristles shifts, allowing

you to change distribution as well as density with a single control.

Bristle Scale: (Corona only) Lets you alter the thickness of the bristles that appear.

Smaller values result in thicker bristles, higher values result in smaller bristles more tightly

packed together.

Ringing: (All types but Bubble) Simulates a pattern of diffraction artifacts. Higher values

increase the number of rings or streaks comprising the element.

Chromatic shift: Simulates chromatic aberration effects.

Eclipse Position: Simulates where the outer (away from the center) or inner (toward the

center) side of a Ghost Element is missing because the light is off the edge of a lens element

or blocked by some part of the tube housing. Practically, this defines which side of the Ghost

Element is affected by the other Eclipse parameters of size, softness, and chromatic shift.

Adjusting this results in semi-circular ghost shapes of different kinds. At 0, there is no eclipse.

At positive values, the eclipse starts from within the frame and pushes out; at negative values,

the eclipse starts from the outside of the frame and pushes in.


Resolve FX Overview | Chapter 160 Resolve FX Light

COLOR

Eclipse Size: Defines the size of the eclipse region for that flare element. At higher values,

more and more of the flare element is eclipsed.

Eclipse Softness: Defines the softness at the transition from the eclipsed and

non-eclipsed regions.

Eclipse Chromatic shift: Lets you create a chromatic aberration effect at the boundary of the

eclipsed region. At 0, there is no chromatic shift. At increasingly positive values, there’s a shift

toward blue. Toward negative values, there’s a shift toward red.

Repeat: Lets you use this element to spawn many duplicates defined by the

following two parameters.

Repeat Position Seed and Repeat Size Seed: At different values, these parameters let you

pseudo-randomly redistribute the placement of repeated elements.

Lens Reflections (Studio Version Only)

Found in the ResolveFX Light category, Lens Reflections simulates intense highlights reflecting off the

various optical elements within a lens to create flaring and scattering effects based on the shape and

motion of highlights you isolate in the scene. It’s an effective simulation that works best when there are

light sources or specular reflections in the scene such as the sun, car headlights, light fixtures, fire and

flame, or other lighting elements that are plausibly bright enough to cause such flaring.

Also, this plugin really shines when these light sources move, as each layer of simulated reflections

moves according to that element’s position within the virtual lens being simulated, creating organic

motion that you don’t have to keyframe. Without intense highlights, the results of this filter are good for

more abstract light-leak effects.


Resolve FX Overview | Chapter 160 Resolve FX Light

COLOR

(Previous page) Original image, (Above) Applying Lens Reflections