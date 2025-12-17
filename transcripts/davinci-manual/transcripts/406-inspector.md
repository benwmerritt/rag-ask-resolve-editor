---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 406
---

# Inspector

Trails node controls

Controls Tab

The Controls tab contains all the primary controls necessary for customizing the trails.

Restart

This control clears the image buffer and displays a clean frame, without any of the ghosting effects.

Preroll

This makes the Trails node pre-render the effect by the number of frames on the slider.

Reset/Preroll on Render

When this checkbox is enabled, the Trails node resets itself when a preview or final render is initiated.

It pre-rolls the designated number of frames.

This Time Only

Selecting this checkbox makes the pre-roll use this current frame only and not the previous frames.

Preroll Frames

This determines the number of frames to pre-roll.

Lock RGBA

When selected, this checkbox allows the Gain of the color channels to be controlled independently.

This allows for tinting of the Trails effect.

Gain

The Gain control affects the overall intensity and brightness of the image in the buffer. Lower values in

this parameter create a much shorter, fainter trail, whereas higher values create a longer, more solid trail.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Rotate

The Rotate control rotates the image in the buffer before the current frame is merged into the effect.

The offset is compounded between each element of the trail. This is different than each element of the

trail rotating on its pivot point. The pivot remains over the original object.

Offset X/Y

These controls offset the image in the buffer before the current frame is merged into the effect.

Control is given over each axis independently. The offset is compounded between each element of

the trail.

Lock Scale X/Y

When selected, this checkbox allows the X- and Y-axis scaling of the image buffer to be manipulated

separately for each axis.

Scale

The Scale control resizes the image in the buffer before the current frame is merged into the effect.

The size is compounded between each element of the trail.

Lock Blur X/Y

When selected, this checkbox allows the blurring of the image buffer to be controlled separately for

each axis.

Blur Size

The Blur Size control applies a blur to the trails in the buffer before the current frame is merged into

the effect. The blur is compounded between each element of the trail.

Apply Mode

The Apply Mode setting determines the math used when blending or combining the trailing objects

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

�Overlay: Overlay multiplies or screens the color values of the foreground object, depending on

the color values of the background object. Patterns or colors overlay the existing pixels while

preserving the highlights and shadows of the color values of the objects behind the foreground

objects. The objects behind the foreground objects are not replaced but mixed with the

foreground objects to reflect the original lightness or darkness of the background objects.

�Soft Light: Soft Light darkens or lightens the foreground object, depending on the color values of

the objects behind them. The effect is similar to shining a diffused spotlight on the image.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

�Hard Light: Hard Light multiplies or screens the color values of the foreground object, depending

on the color values of the objects behind them. The effect is similar to shining a harsh spotlight on

the image.

�Color Dodge: Color Dodge uses the foreground object’s color values to brighten the objects

behind them. This is similar to the photographic practice of dodging by reducing the exposure of

an area of a print.

�Color Burn: Color Burn uses the foreground object’s color values to darken the objects behind

them. This is similar to the photographic practice of burning by increasing the exposure of an area

of a print.

�Darken: Darken looks at the color information in each channel and selects the color value from the

object in front or behind, whichever is darker. Pixels lighter than the blended colors are replaced,

and pixels darker than the blended color do not change.

�Lighten: Lighten looks at the color information in each channel and selects the color value

from the object in front or behind, whichever is lighter. Pixels darker than the blended color are

replaced, and pixels lighter than the blended color do not change.

�Difference: Difference looks at the color information in each channel and subtracts the foreground

object’s color values from the background object’s color values or vice versa, depending on

which has the higher brightness value. Blending with white inverts the color. Blending with black

produces no change.

�Exclusion: Exclusion creates an effect similar to but lower in contrast than the Difference mode.

Blending with white inverts the base color values. Blending with black produces no change.

�Hue: Hue creates color with the luminance and saturation of the background object’s color and

the hue of the foreground object’s color.

�Saturation: Saturation creates color with the luminance and hue of the base color and the

saturation of the blend color.

�Color: Color creates color with the luminance of the background object’s color and the hue and

saturation of the object in front. This preserves the gray levels in the image and is useful for

colorizing monochrome objects.

�Luminosity: Luminosity creates color with the hue and saturation of the background object’s color

and the luminance of the foreground object’s color. This mode creates an inverse effect from that

of the Color mode.

Operator

This menu is used to select the Operation mode used when the trailing objects overlap. Changing the

Operation mode changes how the overlapping objects are combined to produce a result. This drop-

down menu is visible only when the Apply mode is set to Normal.

The formula used to combine pixels in the trails node is always (fg object * x) + (bg object * y).

The different operations determine what x and y are, as shown in the description for each mode.

The Operator Modes are as follows:

�Over: The Over mode adds the foreground object to the background object by replacing the

pixels in the background with the pixels from the Z wherever the foreground object’s Alpha

channel is greater than 1.

x = 1, y = 1 - [foreground object Alpha]

�In: The In mode multiplies the Alpha channel of the background object against the pixels in the

foreground object. The color channels of the foreground object are ignored. Only pixels from the

foreground object are seen in the final output. This essentially clips the foreground object using

the mask from the background object.

x = [background Alpha], y = 0


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

�Held Out: Held Out is essentially the opposite of the In operation. The pixels in the foreground

object are multiplied against the inverted Alpha channel of the background object.

x = 1 - [background Alpha], y = 0

�Atop: Atop places the foreground object over the background object only where the background

object has a matte.

x = [background Alpha], y = 1 - [foreground Alpha]

�XOr: XOr combines the foreground object with the background object wherever either the

foreground or the background have a matte, but never where both have a matte.

x = 1 - [background Alpha], y = 1 - [foreground Alpha]

Subtractive/Additive

This slider controls whether Fusion performs an Additive composite, a Subtractive composite, or

a blend of both when the trailing objects overlap. This slider defaults to Additive assuming the

input image’s Alpha channel is premultiplied (which is usually the case). If you don’t understand the

difference between Additive and Subtractive compositing, below is a quick explanation.

NOTE: An Additive blend operation is necessary when the foreground image is

premultiplied, meaning that the pixels in the color channels have been multiplied by the pixels

in the Alpha channel. The result is that transparent pixels are always black since any number

multiplied by 0 always equals 0. This obscures the background (by multiplying with the

inverse of the foreground Alpha), and then adds the pixels from the foreground.

A Subtractive blend operation is necessary if the foreground image is not premultiplied.

The compositing method is similar to an additive composite, but the foreground image is first

multiplied by its Alpha, to eliminate any background pixels outside the Alpha area.

Although the Additive/Subtractive option is often an either/or checkbox in other software, the

Trails node lets you blend between the Additive and Subtractive versions of the compositing

operation. This can be useful when dealing with problem edges that are too bright or too dark.

For example, using Subtractive merging on a premultiplied image may result in darker edges, whereas

using Additive merging with a non-premultiplied image causes any non-black area outside the

foreground’s Alpha to be added to the result, thereby lightening the edges. By blending between

Additive and Subtractive, you can tweak the edge brightness to be just right for your situation.

Alpha Gain

Alpha Gain linearly scales the Alpha channel values of the trailing objects in front. This effectively

reduces the amount that the trailing objects in the background are obscured, thus brightening the

overall result. When the Subtractive/Additive slider is set to Additive with Alpha Gain set to 0.0, the

foreground pixels are added to the background.

When the Subtractive/Additive slider is set to Subtractive, this controls the density of the composite,

similar to Blend.

Burn In

The Burn In control adjusts the amount of Alpha used to darken the objects that trail under other

objects, without affecting the amount of foreground objects added. At 0.0, the blending behaves like

a straight Alpha blend. At 1.0, the objects in the front are effectively added onto the objects in the

back (after Alpha multiplication if in Subtractive mode). This gives the effect of the foreground objects


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

brightening the objects in the back, as with Alpha Gain. In fact, for Additive blends, increasing the

Burn In gives an identical result to decreasing Alpha Gain.

Merge Under

When enabled, the current image is placed under the generated trail, rather than the usual, over

top operation. The layer order of the trailing elements is also reversed, making the last trail the

topmost layer.

Common Controls

Settings Tab

The Settings tab controls are common to all Effect nodes, so their descriptions can be found in “The

Common Controls” section at the end of this chapter.

TV [TV]

The TV node

TV Node Introduction

The TV node is a simple node designed to mimic some of the typical flaws seen in analog television

broadcasts and screens. This Fusion-specific node is mostly obsolete when using DaVinci Resolve

because of the more advanced Analog Damage ResolveFX.

Input

The two inputs on the TV node are used to connect a 2D image and an effect mask, which can be

used to limit the area where the TV effect appears.

Input: The orange input is used for the primary 2D image that gets the TV distortion applied.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the area where the TV

effect to appears. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The output of an image is connected to the input of the TV node. The style of TV interference is then

customized using the controls in the Inspector.

The TV node simulates TV-style flaws in the

image connected to the orange input


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION