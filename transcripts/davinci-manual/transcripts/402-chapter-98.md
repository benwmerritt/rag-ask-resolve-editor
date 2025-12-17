---
title: "Chapter 98"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 402
---

# Chapter 98

Effect Nodes

This chapter details the Effect nodes in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Duplicate [Dup]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2214

Highlight [HIL]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2220

Hot Spot [Hot]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2223

Object Removal [ORm]�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2229

Pseudo Color [PsCl]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2233

Rays [CIR]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2235

Shadow [SH]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2236

Trails [TRLS]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2239

TV [TV]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2244

The Common Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2247


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Duplicate [Dup]

The Duplicate node

Duplicate Node Introduction

Similar to the Duplicate 3D node, the Duplicate node can be used to quickly duplicate any 2D image,

applying a successive transformation to each, and creating repeating patterns and complex arrays

of objects. The options in the Jitter tab allow for non-uniform transformations, such as random

positioning or sizes.

Inputs

The two inputs on the Duplicate node are used to connect a 2D image and an effect mask, which can

be used to limit the area where duplicated objects appear.

Input: The orange input is used for the primary 2D image that is duplicated.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes,

paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the duplicated

objects to appear only those pixels within the mask. An effects mask is applied to the tool after the

tool is processed.

Basic Node Setup

The Duplicate node can be used in a variety of different ways and with a variety of different inputs.

Below, to create motion graphics, a masked Background node creates a circular shape that is

duplicated in the Duplicate node.

A Duplicate node used to create a repeating circular object


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Inspector

Duplicate controls

Controls Tab

The Controls tab includes all the parameters you can use to create, offset, and scale copies of the

object connected to the input on the node.

Copies

Use this slider to set the number of copies made. Each copy is a copy of the last copy. So, when set

to 5, the parent is copied, then the copy is copied, then the copy of the copy is copied, and so on.

This allows for some interesting effects when transformations are applied to each copy using the

following controls.

Time Offset

Use the Time Offset slider to offset any animations that are applied to the original image by a set

amount per copy. For example, set the value to -1.0 and use a square set to rotate on the Y-axis as the

source. The first copy shows the animation from a frame earlier. The second copy shows animation

from a frame before that, and so forth. This can be used with great effect on textured planes, for

example, where successive frames of a clip can be shown.

Center

The X and Y Center controls set the offset position applied to each copy. An X offset of 1 would offset

each copy 1 unit along the X-axis from the last copy.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Pivot

The Pivot controls determine the position of the pivot point used when changing the size, position, or

angle of each copy. The pivot does not move with the original object or the duplicated array. To have

the pivot follow the army, you must modify the pivot controls.

Size

The Size control determines how much scaling to apply to each copy.

Angle

The Angle control sets the amount of Z rotation applied to each copy. The angle adjustment is linear

based on the location of the pivot point.

Angle adjustment with centered pivot

Angle adjustment with offset pivot

Apply Mode

The Apply Mode setting determines the math used when blending or combining duplicated objects

that overlap.

�Normal: The default mode uses the foreground object’s Alpha channel as a mask to determine

which pixels are transparent and which are not. When this is active, another menu shows possible

operations, including Over, In, Held Out, Atop, and XOr.

�Screen: Screen blends the objects based on a multiplication of their color values. The Alpha

channel is ignored, and layer order becomes irrelevant. The resulting color is always lighter.

Screening with black leaves the color unchanged, whereas screening with white always produces

white. This effect creates a similar look to projecting several film frames onto the same surface.

When this is active, another menu shows possible operations, including Over, In, Held Out,

Atop, and XOr.

�Dissolve: Dissolve mixes overlapping objects. It uses a calculated average of the objects to

perform the mixture.

�Multiply: Multiplies the values of a color channel. This gives the appearance of darkening the

object as the values are scaled from 0 to 1. White has a value of 1, so the result would be the

same. Gray has a value of 0.5, so the result would be a darker object or, in other words, an object

half as bright.

�Overlay: Overlay multiplies or screens the color values of the foreground object, depending

on the color values of the object behind. Patterns or colors overlay the existing pixels while

preserving the highlights and shadows of the color values of the objects behind the foreground

objects. Objects behind other objects are not replaced but mixed with the front objects to reflect

the original lightness or darkness of the objects behind.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

�Soft Light: Soft Light darkens or lightens the foreground object, depending on the color values of

the objects behind them. The effect is similar to shining a diffused spotlight on the image.

�Hard Light: Hard Light multiplies or screens the color values of the foreground object, depending

on the color values of the objects behind them. The effect is similar to shining a harsh spotlight on

the image.

�Color Dodge: Color Dodge uses the foreground object’s color values to brighten the objects

behind them. This is similar to the photographic practice of dodging by reducing the exposure of

an area of a print.

�Color Burn: Color Burn uses the foreground object’s color values to darken the objects behind

them. This is similar to the photographic practice of burning by increasing the exposure of an area

of a print.

�Darken: Darken looks at the color information in each channel and selects the object’s foreground

or background’s color value, whichever is darker, as the result color. Pixels lighter than the

blended colors are replaced, and pixels darker than the blended color do not change.

�Lighten: Lighten looks at the color information in each channel and selects the object’s foreground

or background’s color values, whichever is lighter, as the result color value. Pixels darker than the

blended color are replaced, and pixels lighter than the blended color do not change.

�Difference: Difference looks at the color information in each channel and subtracts the foreground

object’s color values from the background object’s color values or the behind object’s values from

the foreground object’s values, depending on which has the higher brightness value. Blending

with white inverts the color. Blending with black produces no change.

�Exclusion: Exclusion creates an effect similar to but lower in contrast than the Difference mode.

Blending with white inverts the base color values. Blending with black produces no change.

�Hue: Hue creates a result color with the luminance and saturation of the background objects color

values and the hue of the foreground object’s color values.

�Saturation: Saturation creates a result color with the luminance and hue of the base color and the

saturation of the blend color.

�Color: Color creates a result color with the luminance of the background object’s color value

and the hue and saturation of the objects in the foreground. This preserves the gray levels in the

image and is useful for colorizing monochrome objects.

�Luminosity: Luminosity creates a color using the hue and saturation of the background object

and the luminance of the foreground object. This mode creates an inverse effect from that of the

Color mode.

Operator

This menu is used to select the Operation mode used when the duplicate objects overlap. Changing

the Operation mode changes how the overlapping objects are combined. This drop-down menu is

visible only when the Apply mode is set to Normal.

The formula used to combine pixels in the Duplicate node is always (fg object * x) + (bg object * y).

The different operations determine what x and y are, as shown in the description for each mode.

The Operator Modes are as follows:

�Over: The Over mode adds the foreground object to the background object by replacing the

pixels in the background with the pixels from the Z wherever the foreground object’s Alpha

channel is greater than 1.

x = 1, y = 1 - [foreground object Alpha]

�In: The In mode multiplies the Alpha channel of the background object against the pixels in the

foreground object. The color channels of the foreground object are ignored. Only pixels from the


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

foreground object are seen in the final output. This essentially clips the foreground object using

the mask from the background object.

x = [background Alpha], y = 0

�Held Out: Held Out is essentially the opposite of the In operation. The pixels in the foreground

object are multiplied against the inverted Alpha channel of the background object.

x = 1 - [background Alpha], y = 0

�Atop: Atop places the foreground object over the background object only where the background

object has a matte.

x = [background Alpha], y = 1 - [foreground Alpha]

�XOr: XOr combines the foreground object with the background object wherever either the

foreground or the background have a matte, but never where both have a matte.

x = 1 - [background Alpha], y = 1-[foreground Alpha]

Subtractive/Additive

This slider controls whether Fusion performs an Additive composite, a Subtractive composite, or

a blend of both when the duplicate objects overlap. This slider defaults to Additive assuming the

input image’s Alpha channel is premultiplied (which is usually the case). If you don’t understand the

difference between Additive and Subtractive compositing, here’s a quick explanation.

An Additive blend operation is necessary when the foreground image is premultiplied, meaning that

the pixels in the color channels have been multiplied by the pixels in the Alpha channel. The result

is that transparent pixels are always black since any number multiplied by 0 always equals 0. This

obscures the background (by multiplying with the inverse of the foreground Alpha), and then adds the

pixels from the foreground.

A Subtractive blend operation is necessary if the foreground image is not premultiplied. The

compositing method is similar to an additive composite, but the foreground image is first multiplied by

its Alpha, to eliminate any background pixels outside the Alpha area.

While the Additive/Subtractive option is often an either/or mode in most other applications, the

Duplicate node lets you blend between the Additive and Subtractive versions of the compositing

operation. This can be useful for dealing with problem composites with bright or dark edges.

For example, using Subtractive merging on a premultiplied image may result in darker edges, whereas

using Additive merging with a non-premultiplied image causes any non-black area outside the

foreground’s Alpha to be added to the result, thereby lightening the edges. By blending between

Additive and Subtractive, you can tweak the edge brightness to be just right for your situation.

Gain

The Gain RGB controls multiply the values of the image channel linearly. All pixels are multiplied by

the same factor, but the effect is larger on bright pixels and smaller on dark pixels. Black pixels are not

changed since multiplying any number times 0 always equals 0.

Alpha Gain linearly scales the Alpha channel values of objects in front. This effectively reduces the

amount that the objects in the background are obscured, thus brightening the overall result. When

the Subtractive/Additive slider is set to Additive with Alpha Gain set to 0.0, the foreground pixels are

simply added to the background.

When Subtractive/Additive slider is set to Subtractive, this controls the density of the composite,

similarly to Blend.

All Gain values will compound based on the number of duplications.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Blur

Adds a blurring effect to the duplicated layers.

�Lock Blur: Locks the X and Y Blur sliders together for symmetrical blurring. This is enabled by

default. When the Lock Blur control is deselected, independent control over each axis is provided.

�Blur: Sets the amount of blur applied to the duplicated layers in the tool. The Blur amount will not

compound based on the number of duplications.

�Glow: Adds a glow effect to the blur of the duplicated layers.

�Blend: The Blend slider determines the percentage of the affected image that is mixed with

original image. It blends in more of the original image as the value gets closer to 0.

�RGBA Scale: Allows adjusting the strength of the individual Red, Green, Blue, and Alpha channels

to the blur of the duplicated layers.

Burn In

The Burn In control adjusts the amount of Alpha used to darken the objects that fall behind other

objects, without affecting the amount of foreground objects added. At 0.0, the blending behaves like a

straight Alpha blend, in contrast to a setting of 1.0 where the objects in the front are effectively added

on to the objects in the back (after Alpha multiplication if in Subtractive mode). This gives the effect

of the foreground objects brightening the objects in the back, as with Alpha Gain. In fact, for Additive

blends, increasing the Burn In gives an identical result to decreasing Alpha Gain.

Blend

This blend control is different from the Blend slider in the Common Settings tab. Changes made to this

control apply the blend between objects. The Blend slider fades the results of the last object first, the

penultimate after that, and so on. The blending is divided between 0 and 1, with 1 being all objects are

fully opaque and 0 being only the original object showing.

Merge Under

This checkbox reverses the layer order of the duplicated elements, making the last copy the

bottommost layer and the first copy the topmost layer.

Jitter Tab

The options in the Jitter tab allow you to randomize the position, rotation, size, and color of all the

copies created in the Controls tab.

r

Duplicate Jitter tab


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Random Seed

The Random Seed slider and Reseed button are used to generate a random starting point for the

amount of jitter applied to the duplicated objects. Two Duplicate nodes with identical settings but

different random seeds produce two completely different results.

Center X and Y

Use these two controls to adjust the amount of variation in the X and Y position of the duplicated objects.

Axis X and Y

Use these two controls to adjust the amount of variation in the rotational pivot center of the duplicated

objects. This affects only the additional jitter rotation, not the rotation produced by the Rotation

settings in the Controls tab.

X Size

Use this control to adjust the amount of variation in the Scale of the duplicated objects.

Angle

Use this dial to adjust the amount of variation in the Z rotation of the duplicated objects.

Gain

The Gain RGBA controls randomly multiply the values of the image channel linearly.

Blend

Changes made to this control randomize the blend between objects.

Common Controls

Settings Tab

The Settings tab controls are common to all Effect nodes, so their descriptions can be found in

“The Common Controls” section at the end of this chapter.