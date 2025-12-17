---
title: "Custom Curves"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 558
---

# Custom Curves

DaVinci’s Custom curves provide smooth adjustment of each clip’s Y, R, G, and B channels.

The Custom curve mode of the Curves palette is divided into two areas, the Curve Editor to the left,

and the Curve controls to the right. The editor contains the actual Curve controls you use to adjust the

image. The controls at the right let you choose which curves you’re adjusting, and adjust their intensity.

The Custom curves seen used to create a gentle “S” curve

adjustment with four additional control points added

The Custom curves are useful for making more tonally specific, channel-by-channel adjustments to

an image than can be accomplished using the Color Balance controls. They’re also useful for making

strange and wonderful stylistic adjustments through unusual alterations to different combinations of

color channels.

Although the ganged Custom curves appear to be a single curve control, the Custom curve editor

is actually presented as a series of overlaid curves, and the YRGB curves all appear within a single

editor. The default, neutral position of the Custom curves is a diagonal line that runs from the lower-left

black point of the image through the upper-right white point.

The neutral diagonal position of the curve at which no adjustment is made


Color | Chapter 134 Curves

COLOR

The horizontal axis represents the range of image tonality in the original image, from black (at the

left) to white (at the right), while the vertical axis represents the range of alteration you can make.

By adding control points to the surface of the curve and raising or lowering it at different regions, you

are actually remapping the original horizontal “input” value of a color channel to an “output” value of

your choosing.

Additional controls appear to the right of the curve editor itself. A top row of buttons let you

select the curve corresponding to an individual color channel for isolated adjustment, while a

vertical stack of four sliders let you adjust the intensity of each color channel’s curve.

The channel-editing buttons and curve intensity

sliders appear to the right of the curve editor

Editing the Top and Bottom Control Points of Curves

You can also edit curves using the default two control points that the curve control starts out with in

the Curve Editor. The Black Point control (at the lower-left) and the White Point control (at the upper-

right) let you expand and compress the video signal similarly to using the Lift and Gain Master Wheel

controls in the Color Wheels palette.

The Curve control at its original state

The Black and White Point controls dragged

to the right and left to expand the signal

You can use the Black and White Point controls in the following ways:

Using the Black Point control: Dragging this control up makes a lift adjustment to raise the

black point of the signal. Dragging this control to the right makes a lift adjustment to lower the

black point of the signal.

Using the White Point control: Dragging this control down makes a gain adjustment to lower

the white point of the signal. Dragging this control to the left makes a gain adjustment to raise

the white point of the signal.


Color | Chapter 134 Curves

COLOR

HDR Grading Using Curves

When using various grading controls in the Color page to grade wide-latitude images for HDR output,

you may find it useful to enable the HDR mode of the node you’re working on by right-clicking

that node in the Node Editor and choosing HDR mode from the contextual menu (only available in

Resolve Studio).

Using a node’s contextual menu to

put that node into HDR mode

This setting adapts that node’s controls to work within an expanded HDR range. Practically speaking,

this makes it easier to work with wide-latitude signals using controls that operate by letting you make

adjustments at different tonal ranges such as Lift/Gamma/Gain, Custom Curves, Soft Clip, and so on.

Enabling Editable Splines in the Custom Curves

When the Curve palette is in Custom mode, you can choose Editable Splines from the option menu to

expose Bezier spline handles on any selected control point, which let you make more precise curve

adjustments whenever necessary.

Custom curve with editable splines enabled

NOTE: Beware of making curve adjustments that are too sharp, or with control points that

are too close together, as they can introduce unwanted contouring within the image, causing

flattening or solarization in parts of the image that you may not want.


Color | Chapter 134 Curves

COLOR

Adding Default Anchors to the Custom Curves

You can also choose Default Anchors from the option menu of the Curve palette in Custom mode to

place three additional control points on the curve, dividing the curve into five segments that affect the

shadows, low midtones, medium midtones, high midtones, and highlights of the image.

Custom curve with Default Anchors exposed

Ganging and Unganging Custom Curves

By default, the Custom curves are ganged, so that curve adjustments affect a clip’s YRGB channels all

together, resulting in an adjustment to image contrast that’s similar to using the Master Wheels in the

Color Wheels palette. When making this type of adjustment, increasing contrast also increases image

saturation, while reducing contrast also reduces image saturation. Since curves can be manipulated

with greater specificity than the three Master Wheels, you can make much finer contrast adjustments

using the YRGB curves than when using the Master Wheels only.

Turning ganging off lets you use the full power of Custom curves to alter the image. Unlike the Color

Balance controls, each of which adjust all three color channels simultaneously, the Curve controls let

you adjust each channel individually when Gang Custom Curves is turned off.

To disable Custom curve ganging:

Click the Curve Edit button that corresponds to the curve channel you want to edit. Clicking

any Curve Edit button highlights that curve to make it easy for editing when curves overlap

one another. Once one or more curves is offset from the others, you can freely edit any curve

by dragging its control points.

Custom Curve Edit buttons

are to the left, the Gang

button is to the right


Color | Chapter 134 Curves

COLOR

To re-enable Custom curve ganging:

Click the Gang button to the left of the Curve Edit buttons.

Editing color channels via individual curve adjustments lets you make smooth color-channel

specific corrections, or you can make radically individual adjustments to create a wide number

of creative effects.

Turning off curve ganging lets you independently adjust each curve

TIP: When curve ganging is disabled, the Luma curve allows you to adjust the Y channel

by itself, which is similar to using the Y-only Lift/Gamma/Gain knobs of the DaVinci Resolve

Micro, Mini, or Advanced Control Panels. When making this type of adjustment, increasing

luma contrast results in a perceptual decrease of image saturation.

Copying Custom Curves From One Color Channel to Another

Even if you’ve unganged the Custom curves, you can still mirror one curve’s adjustments to another by

copying it using the “Copy to Red/Green/Blue” commands in the Curve palette’s option menu.

Curve Intensity Sliders

Four Curve Intensity sliders to the right of the Curve Editor, one for each channel, let you mix between

the current curve’s effect on the clip, and the original state of the image before you altered the curve.

The default Intensity of 100 results in that curve exerting its full effect on the image, while an intensity

of 0 results in that curve having no effect on the image. The Intensity sliders provide an easy way to

“split the difference” between a curve adjustment and the previous state of the image.

Lowering the Curve Mix slider reduces the

effect of that curve’s adjustment on the image.


Color | Chapter 134 Curves

COLOR