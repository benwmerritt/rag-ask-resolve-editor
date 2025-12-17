---
title: "Black Offset Explained"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 553
---

# Black Offset Explained

Of all the Global controls, the Black Offset control is one of the most deceptively important. Black

Offset lets you define the darkest pixels of the image. Adjustments made to Black Offset do not offset

the entire signal, they only affect the very darkest portion of the signal, letting you raise or lower the

black point of the image while smoothly blending the resulting adjustment into the unadjusted portion

of the image. The result is that you can compress or expand the bottom of your signal.

If you raise Black Offset, you can add “flaring” to the image, similarly to how light flaring within a lens

might lighten the darkest part of the image.

(Left) The original image, (Right) Raising Black Offset in order to add flaring to the darkest pixels of the image

Alternately, you can lower Black Offset to lower the very darkest pixels in the image. If the source

image is dark enough, this control can lower the darkest pixels below 0, however this image detail is

preserved in the color image processing pipeline

The most important thing to understand about this control is that level to which you set Black Offset

becomes the new level at which Global exposure adjustments are made. In the following example, the

first image shows the original color of a clip that was exposed to be dark. In the second image, Black

Offset is adjusted to raise the darkest parts of the image, compressing them relative to the midtones

and introducing a pleasing flaring effect to the shadows.

(Left) The original image; (Right) The image with Black Offset raised

In the following image, Global Exposure is raised, and you can see in the Waveform scope that the

exposure change stretches the contrast of the image up, with the darkest pixels “locked” to the Black

Offset you set.

(Left) Before, (Right) After raising Global Exposure to stretch image contrast out from the Black Offset level;

notice that the bottom of the signal continues “touching” the same level after global exposure is raised.


Color | Chapter 132 HDR Palette

COLOR

The Black Offset level you set also becomes the minimum picture level when you lower exposure,

either using the Global Exposure changes, or when you use any of the “darkening” zone controls

such as Shadow, Dark, and Black. The following image shows the result of lowering Global Exposure;

the shadows of the image are compressed more heavily than the highlights as exposure is lowered,

with the result that the minimum value of the image remains at the Black Offset level you set. With

shadow detail impressively preserved, this compression rolls off smoothly and nonlinearly through the

midtones so that the image continues to look as natural as possible.

(Left) Before, (Right) After lowering Global Exposure to compress image contrast down to the

Black Offset level; notice the signal never goes lower than the Black Offset level

This is also true when using other darkening zone exposure controls, such as the Shadow control,

which selectively pushes the exposure of the darker part of the image down, while leaving the

highlights alone. While reducing Shadow exposure, the darkest pixels still compress so that nothing

goes beneath the Black Offset level you set.

Bottom line, you can adjust Black Offset at any time, either before or after any other Global or Zone

adjustments, to fine tune the image as necessary.

Making Zone-Based Adjustments

After you’ve made whatever initial global adjustments you want, you can optionally make more

tonally‑specific adjustments to the image via the Zone-based color and contrast controls to the left.

These divide the image into multiple overlapping “zones,” which are somewhat similar in principal

to Ansel Adams’ zone system, which divides images into tonally-specific regions based on image

luminance, from pure black, through progressively lighter shadows, to 18% gray as the middle value

centering the midtones of most images, and then up through progressively lighter highlights on the

way to the last zone of pure white.

Simplified illustration of Ansel Adams’ zone system

While Adams’ zone system was meant to teach people how to think about using the available range

of the photographic medium when exposing images, the zones of the HDR palette let you put this

concept into practice by allowing you to make tonally-specific Color Balance, Saturation, and Exposure

adjustments that only affect the range of shadows or highlights that fall within that zone.


Color | Chapter 132 HDR Palette

COLOR

Using the default preset, the shadows of your image are divided into overlapping Shadow, Dark, and

Black zones, while the highlights of your image are divided into separate overlapping zones for Light,

Highlight, and Specular ranges. The chart below illustrates the relationship of these zones to one another.

Approximation of the overlapping zones in the HDR palette that can be individually adjusted

NOTE: All of the examples in this section have Timeline to Output Tone Mapping set to None,

to keep the ramp gradient linear for purposes of this explanation.

Zone-Based Color Adjustments

Understanding how adjustments made using these overlapping zones interact with one another is key

to knowing what you can do using the HDR palette. Keep in mind that every zone is customizable, but

here’s how the default zone definitions work to let you make detailed image adjustments. For clarity,

Zone adjustments are shown made to a linear ramp gradient image, to demonstrate exactly what tonal

portion of each image is affected by each control.

�The Light and Shadow zones are the most broadly defined zones. Together, they cover the entire

tonal range of your image. They softly overlap one another by two stops at the center of the

tonal range (50% gray or 18% exposure); this is where adjustments made to Light mix together

with adjustments made to Shadow, resulting in both adjustments softly blending together.

Making exposure adjustments to these two zones lets you manipulate overall image contrast

by selectively compressing/expanding contrast in the shadows and/or highlights relative to one

another. Using the color controls lets you make broad color adjustments to the upper (highlights)

and/or lower (shadows) range of image tonality.

Color adjustments to a ramp gradient show the Light

(tinted green) and Shadow (tinted orange) zones


Color | Chapter 132 HDR Palette

COLOR

�The Dark and Black zones overlap two progressively lower luminance ranges of the Shadow zone.

Dark is useful for adjusting the color or contrast of the deeper shadows, while Black is useful as

a trim that lets you manipulate the very darkest parts of an image. All adjustments you make to

Dark are mixed with any adjustments made to Shadow, and all adjustments made to Black are

mixed with the adjustments made to Dark and Shadow. In this way, all color adjustments you make

to overlapping Shadow zones mix smoothly together to produce the final result, as seen in the

following ramp gradient.

Color adjustments to a ramp gradient show the Dark

(tinted blue) overlapping the Shadow (tinted orange) zone

�The Highlight and Specular zones overlap two progressively brighter luminance ranges of the

Light zone. Highlight lets you adjust the color and/or contrast of the brightest highlights, while

Specular is useful as a trim that lets you manipulate the very brightest highlights of an image.

All adjustments you make to Highlight are mixed with any adjustments made to Light, and all

adjustments made to Specular are mixed with the adjustments made to Highlight and Light. In

this way, all color adjustments you make to overlapping Highlight zones mix smoothly together to

produce the final result, as seen in the following ramp gradient.

Color adjustments to a ramp gradient show the Highlight

(tinted yellow) overlapping the Light (tinted green) zone.

As you can see, each one of these zones allow the specific adjustment of whichever parts of the

image fall within the luminance range of that zone (as defined on the Zones panel), while providing

control over how smoothly one adjustment fades into the next, to prevent unwanted contouring.

As you make adjustments to the Range and Falloff of each zone using the different sets of zone

controls, they work together to smoothly manipulate the contrast and color of the image, similarly

to if you were using a more precise and constrained version of the Custom Curves. In fact, you can

see the actual adjustment you’re making by exposing the Zone graph.


Color | Chapter 132 HDR Palette

COLOR

(Left) Raising the Range of the Light zone to expand the Shadow zone’s range of

influence, (Right) The same adjustment seen in the Zone graph

Working this way allows a tremendous specificity of adjustment, without the need to use curves or

qualifiers. For example, zone-specific Color Balance controls allow you to grade the highlights and

shadows separately using the Shadow and Light zone controls to quickly create a warm/cool split

lighting effect. This makes the creation of dynamic grades more efficient and more creative.

(Left) The original image, (Right) Using the HDR palette to warm the

highlights and cool the shadows (exaggerated for print)

In this next example, the Dark zone’s Color Balance control is used to add a splash of green to the

darker shadows of the image, while the Black control is used to neutralize this green in the very

blackest shadows.

(Left) The original image, (Right) Using the HDR palette

to add green to a narrow range of shadows


Color | Chapter 132 HDR Palette

COLOR