---
title: "Tile Animation"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 658
---

# Tile Animation

These controls appear in Tiles mode. They make it easy to create simple intro/outro animations

to bring all or some tiles onscreen, and to push all or some tiles offscreen, in different ways. The

Animate drop-down menu determines whether this animation will be automatic or manually created

using keyframes.

�Apply to All Tiles: When enabled, any animation that’s set up will be applied to all tiles in the

layout simultaneously.

�Animate: This drop-down menu lets you choose between Manually Keyframing intro or outdo

animations or automatically creating animations to introduce or conclude a tile. The options are:

Manually Keyframe: In this mode, you must manually keyframe the four progress sliders below to

create animated Intro and Outro animations.

Intro Only: Animation is automatically created to bring each tile onscreen according to the types of

animation you choose from four checkboxes below. Options include: Fly, Shrink, Rotate, and Fade,

in any combination. A Duration slider appears that lets you choose how long the Intro will be.

Outro Only: Animation is automatically created to send each tile offscreen according to the types of

animation you choose from four checkboxes below. Options include: Fly, Shrink, Rotate, and Fade,

in any combination. A Duration slider appears that lets you choose how long the Outro will be.

Intro & Outro: Animation is automatically created to bring each tile onscreen and then send each

tile offscreen, according to the types of animation you choose from four checkboxes below.

Options include: Fly, Shrink, Rotate, and Fade, in any combination. A Duration slider appears that

lets you choose how long the Intro and Outro will be.

Fly Animation: Lets you choose a direction for tiles to fly in from and fly out to.

Shrink Animation: Lets you choose a method of shrinking out or in when the Fly Progress

slider is animated.

Fly Progress: (manual key framing only) A slider that, when animated, lets you fly a tile into

or out of the frame. A value of 0.000 positions the tile in its default grid position. A value of

1.000 positions the tile entirely off screen.

Shrink Progress: (manual key framing only) A slider that, when animated, lets you shrink a tile

down to nothing or up to the current size. A value of 0.000 sizes the tile at its largest state.

A value of 1.000 shrinks the tile to nothing.

Rotate Progress: (manual key framing only) A slider that, when animated, lets you fly a tile into

or out of the frame. A value of 0.000 positions the tile in its default grid position. A value of

1.000 positions the tile entirely off screen.

Fade Progress: (manual key framing only) A slider that, when animated, lets you fly a tile into

or out of the frame. A value of 0.000 positions the tile in its default grid position. A value of

1.000 positions the tile entirely off screen.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Easing & Blur

These controls appear in Tiles mode. They let you adjust the easing of the tile animation created in the

previous group of controls.

�Motion and Size Ease: These controls set the curve used for simulated momentum in animating

the Tile Position and Size keyframes of the tiles.

None: No curves are applied. The animation snaps immediately from keyframe to keyframe.

Linear: No easing curves are applied; motion is neither accelerated or decelerated.

In: The animation curve starts slower and ends faster.

Out: The animation curve starts faster and ends slower.

In & Out: The animation curve starts slower, accelerates in the middle, and slows down at the end.

�Animation Effects Ease: These controls set the curve used for simulated momentum in animating

the Tile Animation keyframes of the tiles.

None: No curves are applied. The animation snaps immediately from keyframe to keyframe.

In: The animation curve starts slower and ends faster.

Out: The animation curve starts faster and ends slower.

In & Out: The animation curve starts slower, accelerates in the middle, and slows down again at

the end.

�Ease Amount: The relative strength of the animation curve in speeding up and slowing down.

The values range from 0.000 to 1.000.

�Motion Blur: This slider controls the amount of motion blur added to the animation, in order to

make it smoother and more organic looking. The values range from 0.000 (no motion blur), to

1.000 (maximum motion blur).

Global Blend

�Blend: This slider controls the overall opacity of the entire Video Collage effect. The values range

from 0.000 (completely transparent) to 1.000 (completely opaque).


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Chapter 169

Resolve FX Warp

The filters in this category let you warp the image in different ways, creating

procedural or custom distortion effects, some of which can be automatically

animated. The Warper plugin is a point-based free‑form Warp tool.

Contents

Dent���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3654

Lens Distortion (Studio Version Only)�������������������������������������������������������������������������������������������������������������������������������������� 3654

Ripples���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3655

Main Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3655

Ripple Controls����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3655

Vortex������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3655

Warper (Studio Version Only)������������������������������������������������������������������������������������������������������������������������������������������������������� 3656

Warp Mode Points����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3656

Warp Mode Curves��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3656

Warper Settings���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3659

Waviness������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3661


Resolve FX Overview | Chapter 169 Resolve FX Warp

COLOR

Dent

A warp effect that creates different types of circular bowing and folding effects.

�DentType: This lets you choose from six different types of “dent” warping effects. The options are

Type 1, Type 2, Type 3, Sine, Cosine, and Black Hole.

�X and Y: Position sliders let you offset the center of the warp.

�Size: This lets you adjust the diameter of the warp.

�Strength: This lets you adjust the extent and direction of the warp, lowering this below zero “pulls”

the image into the center of the effect, while raising this above zero “pushes” the image outward

to buckle according to the DentType you’ve chosen.

�Edge Behavior: This eliminates any blanking caused by negative distortion by filling black areas

in one of several user-defined ways; options include Black (do nothing and leave the blanking),

Reflect, Wrap-Around, and Replicate.

Lens Distortion (Studio Version Only)

Lets you add convex or concave lens distortion to an image, to make it warp by bulging outward or

bulging inward, similar to a poorly made lens. This filter could also be used in a corrective manner,

to compensate for images exhibiting barrel distortion. Additionally, the amount of distortion applied

to each color channel can be varied, in order to create the effect of chromatic aberration using the

curvature of the distortion you’re adding for a more accurate effect.

�Red, Green, and Blue Distortion: These sliders are ordinarily locked together by the Gang

checkbox. When adjusted as ganged, moving these sliders to the left (negative values) increases

“fisheye” distortion, while moving these sliders to the right (positive values) creates an inverted

“fisheye” effect that bows the image inward rather than outward. Turning Gang off lets you set the

Red, Green, and Blue Distortion sliders to different values, introducing more accurately simulated

chromatic aberration to the image.

�Fine Adjustment: This checkbox results in the distortion sliders operating within a much smaller

range, enabling more precise adjustments.

�X and Y Position: These sliders let you change the center of the distortion effect.

�Edge Behavior: The options available in this pop-up eliminate blanking caused by negative

distortion by filling black areas in one of several user-defined ways; options include Black (do

nothing and leave the blanking), Reflect, Wrap-Around, and Replicate.

TIP: To resize a clip with an extreme distortion effect that introduces blanking around the

edges of the frame, you’ll need to use the Zoom control found in the Node Sizing mode

of the Sizing palette. Edit and Input sizing will only zoom the image within the border

created by blanking.


Resolve FX Overview | Chapter 169 Resolve FX Warp

COLOR

Ripples

A warp effect that creates different types of ripples.

Main Controls

These controls govern the type of ripple and the quality of optional ripple shine that you want.

�Ripple Shape: Lets you choose from Circular, Square, Horizontal, Vertical, Exponential, Star, and

Radial ripples.

�Wave Shape: Lets you choose from Sinusoidal, Triangular, Fresnel In, Fresnel Out, and Natural waves.

A set of Shine parameters lets you overlay a simulated shine on top of these ripples.

�Shine: A checkbox lets you turn this shine on and off.

�Shine Direction: Lets you add a light shine to the peaks of the ripples. Works best at low shine strength.

�Vertical Shine Height: Lets you adjust the thickness of the highlights running along the ripples.

�Shine Size: Lets you adjust the length of the highlights running along the ripples.

�Shine Strength: Lets you adjust the overall appearance of the shine.

�Animate: This checkbox, if checked, reveals a Speed slider that lets you set how quickly the

ripple effect auto-animates the phase of the currently configured ripple effect, without the need

to use keyframes.

Ripple Controls

A separate set of Ripple parameters lets you enable up to five overlapping ripples.

�Enable Ripple: A keyframable checkbox that will turn a particular ripple on or off.

�X and Y Position: Lets you change the center position of each set of ripples.

�Amplitude: Lets you adjust the “height” of each ripple caused by this effect.

�Frequency: Lets you choose how many ripples are being created.

�Decay: Lets you adjust the falloff of the ripple effect, where ripples gradually diminish as they

reach the point of decay.

�Phase: Lets you adjust the phase of the ripple effect relative to the center origination point. If you

want to animate a ripple simply, you can also choose to keyframe the Phase parameter to create

the same effect created by the Animate checkbox above.

Vortex

Vortex begins as an S shaped warp effect, but you can adjust the parameters to create many types of

warping effects.

�X and Y position: Two sliders let you offset the center of the warp.

�Size: Adjusts the diameter of the warp.

�Angle: Adjusts the direction and intensity of the warp effect; setting Angle below 0 twists the

image to the left, while raising Angle over 0 twists the image to the right.

�Power: Rotates the area that’s affected to create a harder border between what is warped and what isn’t.

�Swirl: Intensifies the effect, twisting the image into an even tighter swirling effect.

�Edge Behavior: The options available in this pop-up eliminate blanking caused by negative

distortion by filling black areas in one of several user-defined ways; options include Black (do

nothing and leave the blanking), Reflect, Wrap-Around, and Replicate.


Resolve FX Overview | Chapter 169 Resolve FX Warp

COLOR