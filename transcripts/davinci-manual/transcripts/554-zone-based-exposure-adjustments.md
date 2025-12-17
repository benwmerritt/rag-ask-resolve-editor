---
title: "Zone-Based Exposure Adjustments"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 554
---

# Zone-Based Exposure Adjustments

Each zone has its own Exposure control that allows you to stretch image contrast from that zone’s Min

or Max range boundary either down towards the shadows, or up towards the highlights. As seen on

the Zone graph (found on the Zone panel), exposure adjustments are made on a scale measured in

stops, to provide a more photographic experience when grading wide dynamic range material.

The scale of the Zone graph shows you the shadow and highlight ranges,

in stops, relative to 0 representing 18 percent photographic gray

On this scale, 0 stops corresponds to photographic 18% gray, at the center of each image’s tonal

range. Shadows then fall to the left over -8 stops, while highlights fall to the right over +8 stops,

where each stop represents either twice the amount of light (stopping up) or half the amount of light

(stopping down).

In conjunction with Resolve Color Management, this range is designed to accommodate any SDR or

HDR range you’ll be mastering to. All HDR palette controls are designed to accommodate up to 16

stops of exposure. By comparison, most modern digital cinema cameras claim to be able to capture

somewhere between 13-19 stops of dynamic range, while a white paper from the ASC states that

modern film negatives are capable of capturing 14 stops of dynamic range.

Unlike the Lift/Gamma/Gain or Log master level controls, the Exposure adjustment of each zone

starts at a specific boundary of image tonality, and stretches all the way out through the highlights

or shadows, through the maximum or minimum signal level allowable. Since Shadow and Light are

the two zones that are centered on the midtones of the image, they’re the best zones for seeing how

this works. Because of this, these are also probably the first two zones you’ll want to adjust if you’re

making more specific exposure changes to the image.

Using the default preset, Shadow exposure adjustments affects everything in the image from stop 1

down through absolute black.

(Left) The original image, (Right) Darkening all shadows by lowering the Shadow exposure adjustment


Color | Chapter 132 HDR Palette

COLOR

Meanwhile, Light exposure adjustments affect everything in the image from -1 stops all the way

through maximum white.

(Left) The original image, (Right) Lightening all highlights by raising the Light exposure adjustment

This ability to make open-ended adjustments to image contrast in different overlapping ranges of

shadow and highlight tonality makes these controls uniquely suitable for HDR grading, while also

being completely suitable when grading at SDR levels. Also, keep in mind that all contrast adjustments

in the HDR palette keep saturation constant as contrast increases or decreases.

This is particularly useful when making large contrast adjustments to HDR images, for which a 300

nit expansion of highlight contrast using the Lift/Gamma/Gain or Log controls would create a huge

saturation increase. Using the HDR palette to expand highlight contrast keeps image saturation

perceptually the same, while offering zone-specific saturation controls that let you choose whether to

increase or decrease the saturation falling within that zone.

Exposure adjustments to zones that overlap other zones are smoothly combined to allow targeted

contrast adjustments, while making it relatively easy to avoid unwanted artifacts, like contouring or

solarizing due to overzealous inversion of the curves caused by these operations.

An Example of Zone-Based Exposure Adjustment

To see this in action, let’s see what happens when we make some overlapping adjustments to the

Light, Highlight, and Specular zones in order to grade some HDR highlights, focusing our attention

on the Waveform scope, since it’s difficult to see HDR grades in print. Keep in mind that you won’t

usually be making Zone-based Exposure adjustments by themselves. This example image has had

a Contrast/Pivot adjustment to push the midtones and shadows down, to give the shadows greater

definition. Then, Black Offset is raised to lift the darkest shadows up just a little bit, so they can

breathe. This leaves us with an image that’s mostly under 200 nits to begin with. A perfect starting

point for us to begin sculpting those highlights.

(Left) The original image; (Right) After changing Contrast/Pivot and raising Black Offset

Using the default preset, making an exposure adjustment to the Light zone smoothly raises everything

in the source image above -1 stops on the Zone graph. Practically, it’s stretching up all levels above 10

nits on the HDR scope. This smoothly boosts the brighter part of the image, while leaving the shadows

down where we put them.


Color | Chapter 132 HDR Palette

COLOR

(Left) The previous adjustment; (Right) After raising Light Exposure

At this point, making an exposure adjustment to the Highlight zone boosts all levels above 1.5 stops on

the Zone graph. Again, practically speaking, all levels above 100 nits are being boosted, brightening

the top highlights. In the image, you can see that we’re creating a greater differentiation between

dimmer and brighter highlights in the image, creating highlight contrast with greater detail where once

there were simply flat pools of light.

(Left) The previous adjustment; (Right) After raising Highlight Exposure

Now, this might be a fine place to stop, but since we’re interested in turning the HDR in this image up

to 11, we can put the highlights over the top by making one more Exposure adjustment, to the Specular

zone. The Specular zone starts at 4 stops and is designed to let you boost or attenuate only the very

brightest, hardest highlights, likely corresponding to specular details such as chrome reflections, eye

glints, and directly photographed light sources. You won’t always use this control, but it’s useful to

know about.

In this example, the default Specular Zone Min Range control is outside of the available image data

in the image (seen as the right edge of the histogram in the Zone graph), so making adjustments with

this control won’t do anything. However, dragging the Min Range control to intersect the end of the

histogram will allow these controls to affect the very brightest pixels in the image.

(Left) The original distribution of zones in the Zone Graph; (Right) Dragging the Specular Min Range handle to intersect

the brightest highlights in the image histogram, to allow the Specular controls to affect that part of the image


Color | Chapter 132 HDR Palette

COLOR

Now, the Specular Exposure control lets us push the very brightest pixels of our image up,

further differentiating them from the other highlights, and widening the audience’s sensation of

highlight contrast.

(Left) The previous adjustment; (Right) After raising Specular Exposure to bring the very brightest highlights to 1000 nits

Now, having selectively boosted the Highlight and Specular zones, you might decide that you like

the differentiation that’s been created among different brightnesses of highlights, but the overall

highlights are too bright. This is easily fixed by lowering the Light zone’s Exposure adjustment. As a

result of this one adjustment, all of the highlights are scaled down, while the adjustments you’ve made

to the Highlight and Specular zones maintain a relative influence on the parts of the image they’re

brightening. The Shadow, Dark, and Black controls work similarly, but for the shadows.

(Left) The previous adjustment; (Right) After lowering Light Exposure, all levels smoothly scale down to reduce the

brightness of the highlights while keeping the differentiation you’ve created with the Highlight and Specular controls.

Now that you’ve seen how all overlapping Zone adjustments work together to create a seamless

adjustment, it’s time to look at the Zone controls in more detail.

Zone Controls

Each individual zone also has controls for Color Balance and Saturation, which let you make focused

adjustments that fall within specific ranges of image tonality, all without needing to use a qualifier.

Using all of these zones together, you can make fast, precise, and smooth adjustments to the image

that feel incredibly natural. Despite the name of the palette, this allows careful adjustment of SDR

images, as well as creative adjustment of the spectacular range of highlights that HDR enables. There

are also Range and Falloff controls to the left and right of each cluster of controls that let you redefine

each zone’s area of influence, even if the Zone graph is hidden.


Color | Chapter 132 HDR Palette

COLOR

The Shadow and Light zone controls next to one another; you

can see the Min and Max indicators, along with the Range

value (in stops) at the upper left of each group of controls.

�Range indicator: An icon and value at the upper-right-hand corner of each zone control cluster

shows that zone’s range. A numeric value shows the range value, which is the Luminance level

of image tonality at which that zone’s adjustment begins. This value is expressed in stops, while

an icon shows you whether it’s a maximum range (affecting shadows) or a minimum range

(affecting highlights).

Clicking the icon shows a temporary preview in the Viewer of which parts of the image will

be affected by the controls of that zone. Affected areas appear in full color, while unaffected

areas appear black.

�Zone-specific Color Balance: A color balance control lets you readjust the relative strength of the

red, green, and blue channels within the current zone of image tonality.

�Zone-specific Exposure: Zone-specific Exposure controls work in conjunction with an

adjustable pivot that defines the Luminance level that each exposure adjustment starts from.

To accommodate both shadow and highlight adjustments, there are two kinds of pivots, labeled

Maximum and Minimum range, and indicated using an icon. Max Range controls, such as the

Shadow control, start at a maximum value with exposure adjustments stretching image contrast

downward towards the shadows. Min Range controls, such as Light, start at a minimum value with

exposure adjustments stretching contrast upwards towards the highlights. Each zone also has a

falloff that specifies how much of that zone overlaps neighboring zones (starting at the pivot level)

in order to blend overlapping adjustments softly enough to prevent contouring.

�Zone-specific Saturation: Adjusts the intensity of color within the current zone of image tonality.

�Min/Max Range: Defines the level of image tonality at which that zone’s adjustment starts.

This value is expressed in stops. Identical to the Min or Max Range slider in the Zone panel.

Useful for tweaking Range while the Zones graph is hidden.

�Zone Falloff: Defines how softly this zone fades into all overlapping zones. Identical to the

Falloff slider in the Zone panel, the value is visible in the virtual slider below. Useful for tweaking

Falloff while the Zones graph is hidden.

�Zone-specific Color Balance Values: Two values expose the current color balance operation

numerically. The option menu lets you choose between representing these as X and Y,

or as Angle and Strength.


Color | Chapter 132 HDR Palette

COLOR