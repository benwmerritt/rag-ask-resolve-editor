---
title: "Channel Booleans [Bol]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 384
---

# Channel Booleans [Bol]

The Channel Booleans node

Channel Booleans Node Introduction

The Channel Booleans node applies a variety of mathematical and logical operations on the channels

in an image. This node works by using one image’s channels to modify another image’s channels. If a

foreground input is not available, selecting options that use color channels from the foreground ends

up using the background input’s color channels instead.

NOTE: Be aware of another similarly named Channel Boolean (3Bol), which is a 3D node

used to remap and modify channels of 3D materials. When modifying 2D channels, use the

Channel Booleans (with an “s”) node (Bol).

Inputs

There are four inputs on the Channel Booleans node in the Node Editor, but only the orange

Background input is required.

Background: This orange input connects a 2D image that gets adjusted by the foreground input image.

Effect Mask: The blue effect mask input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the channel

booleans adjustment to only those pixels within the mask.

Foreground: The green foreground input connects a 2D image that is used to adjust the background

input image.

Matte: The white matte input can be used to combine external mattes with the foreground and

background operations.

Basic Node Setup

The Channel Booleans node is an extremely flexible tool used in many different ways. The example

below copies the z-depth channel from the foreground input (green) into the background image (orange).

A Channel Booleans set to copy from foreground to background


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Inspector

Channel Booleans controls

Color Channel Tab

On the Color Channels tab, the controls are divided into two columns.

On the left side are target channels for the image connected into the orange background input.

The drop-down menu to the right lets you choose whether you want to modify the BG image with

its channels (suffix BG after list name) or with the channels from an image connected into the green

foreground input on the node (suffix FG in the drop-down list).

Operation

This menu selects the mathematical operation applied to the selected channels.

The options are as follows:

Copy

Copy the value from one color channel to another. For example, copy the foreground red channel into

the background’s Alpha channel to create a matte.

�Add: Add the color values from one color channel to another channel.

�Subtract: Subtract the color values of one color channel from another color channel.

�And: Perform a logical AND on the color values from color channel to color channel. The

foreground image generally removes bits from the color channel of the background image.

�Or: Perform a logical OR on the color values from color channel to color channel. The foreground

image generally adds bits from the color channel of the background image.

�Exclusive Or: Perform a logical XOR on the color values from color channel to color channel. The

foreground image generally flips bits from the color channel of the background image.

�Multiply: Multiply the values of a color channel. This gives the appearance of darkening the image

as the values scale from 0 to 1. White has a value of 1, so the result would be the same. Gray has a

value of 0.5, so the result would be a darker image or, in other words, an image half as bright.

�Divide: Divide the values of a color channel. This gives the appearance of lightening the image as

the values scale from 0 to 1.

�Maximum: Compare the two images and take the maximum, or brightest, values from each image.

�Minimum: Compare the two images and take the minimum, or darkest, values from each image.

�Negative: Invert the FG input to make a negative version of the image.

�Solid: Solid sets a channel to a full value of 255. This is useful for setting the Alpha to full value.

�Clear: Clear sets a channel to a value of zero. This is useful for clearing the Alpha.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

�Difference: Difference subtracts the greater color values of one color channel from the lesser

values of another color channel.

�Signed Add: Signed Add subtracts areas that are lower than mid-gray and adds areas that are

higher than mid-gray, which is useful for creating effects with embossed gray images.

To Red, To Green, To Blue, To Alpha

These menus represent the four color channels of the output image. Use the drop-down menu to

select which channel from the source images produces the output channel.

The default setting copies the channels from the foreground channel. Select any one of the four color

channels, as well as several auxiliary channels like Z-buffer, saturation, luminance, and hue.

Inspector

Aux Channel Inspector

Aux Channel Tab

This tab includes a series of menus where you select a source for the auxiliary channels of the

output image.

Enable Extra Channels

When the Enable Extra Channels checkbox is selected, the Channel Booleans node can output

images with channels beyond the usual RGBA. Once enabled, the remaining controls in the

Aux Channels tab can copy data into the auxiliary channels.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

EXAMPLES To copy the Alpha channel of one image to its color channels, set the red, green,

and blue channels to Alpha BG. Set the Operation to Copy.

To copy the Alpha channel from another image, set operation type to Alpha FG.

To replace the existing Alpha channel of an image with the Alpha of another image, choose

“Do Nothing” for To Red, To Green, and To Blue and “Alpha FG” for To Alpha. Pipe the image

containing the Alpha into the foreground input on the Channel Booleans node. Set Operation:

“Copy.” The same operation is available in the Matte Control node.

To combine any mask into an Alpha channel of an image, choose “Do Nothing” for To Red,

To Green, and To Blue and “Matte” for To Alpha. Pipe the mask into the foreground input on

the Channel Booleans node. Set Operation: “Copy.”

To subtract the red channel’s pixels of another image from the blue channel, choose

“Do Nothing” for To Red and To Green and “Red FG” for To Blue. Pipe the image containing

the red channel to subtract into the foreground input on the Channel Booleans node. Set

Operation: “Subtract.”

Common Controls

Settings Tab

The Settings tab in the Inspector appears in other Color nodes. These common controls are described

in detail at the end of this chapter in “The Common Controls” section.

Color Corrector [CC]

The Color Corrector node

Color Corrector Node Introduction

The Color Corrector node is a comprehensive color node with histogram matching, and equalization,

hue shifting, tinting, and color suppression.

Controls in the Color Corrector node are separated into four tabs: Correction, Ranges, Options,

and Settings.

Inputs

The Color Corrector node includes four inputs in the Node Editor.

Input: This orange input is the only required connection. It connects a 2D image for color correction.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the color

corrector adjustment to only those pixels within the mask. An effect mask is applied to the tool after

the tool is processed.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Match Reference: The green input is used to connect an image that can be a reference for histogram

matching.

Match Mask: This optional white input accepts any mask much like an effect mask. However, this mask

defines of the area to match during a Histogram Match. It offers more flexibility in terms of shape than

the built-in Match rectangle in the Inspector.

Basic Node Setup

The Color Corrector node, like many 2D image-processing nodes, receives a 2D image like a Loader

node or the MediaIn1 shown below. The output continues the node tree by connecting to another 2D

image-processing node or a Merge node.

A Color Corrector node applied to a MediaIn1 node

Inspector

Color Corrector controls

Correction Tab Colors Menu

The main Correction tab is further separated into four types of correction methods: colors, levels,

histogram, and suppress. Selecting one from the menu at the top of the Correction tab causes that

method’s controls to appear. The Color method is described in detail below.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Range

This menu determines the tonal range affected by the color correction controls in this tab. The menu

can be set to Shadows, Midtones, Highlights, and Master, where Master is the default affecting the

entire image.

The selected range is maintained throughout the Colors, Levels, and Suppress sections of the

Color Corrector node.

Adjustments made to the image in the Master channel are applied to the image after any changes

made to the Highlight, Midtone, and Shadow ranges.

NOTE: The controls are independent for each color range. For example, adjusting the

Gamma control while in Shadows mode does not change or affect the value of the Gamma

control for the Highlights mode. Each control is independent and applied separately.

Color Wheel

The color wheel provides a visual representation of adjustments made to Hue and Saturation, as well

as any tinting applied to the image. Adjustments can be made directly by dragging the color indicator,

or by entering values in the numeric boxes under the color wheel.

The tinting is represented in the color wheel color indicator that shows the color and strength of the

tint. The Highlight setting uses a black outline for the color indicator. The Midtones and Shadows use

gray color indicators. The Master color indicator is also black, but it has a white M in the center to

distinguish it from the others.

The mouse can position the color indicator for each range only when the applicable range is selected.

For example, the Highlight color indicator cannot be moved when the Master range is selected.

Holding down the Command or Ctrl key while dragging this indicator allows you to make finer

adjustments by reducing the control’s sensitivity to mouse movements. Holding down the Shift key

limits the movement of the color indicator to a single axis, allowing you to restrict the effect to either

tint or strength.

Tint Mode

This menu is used to select the speed and quality of the algorithm used to apply the hue and

saturation adjustments. The default is Better, but for working with larger images, it may be desirable to

use a faster method.

Hue

This slider is a clone of the Hue control located under the color wheel. The slider makes it easier to

make small adjustments to the value with the mouse. The Hue control provides a method of shifting

the hue of the image (or selected color range) through the color spectrum. The control value has an

effective range between -0.1 and 1.0, which represents the angle of rotation in a clockwise direction.

A value of 0.25 would be 90 degrees (90/360) and would have the effect of shifting red toward blue,

green to red, and so on.

Hue shifting can be done by dragging the slider, entering a value directly into the text control, or by

placing the mouse above the outer ring of the color wheel and dragging the mouse up or down. The

outer ring always shows the shifted colors compared to the original colors shown in the center of

the wheel.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Saturation

This slider is a clone of the Saturation control located under the color wheel. The slider makes it easier

to make small adjustments to the value with the mouse. The Saturation control is used to adjust the

intensity of the color values. A saturation of 0 produces gray pixels without any color component,

whereas a value of 1.0 produces no change in the chroma component of the input image. Higher

values generate oversaturated values with a high color component.

Saturation values can be set by dragging the slider, entering a value directly into the text control, or by

dragging the mouse to the left and right on the outer ring of the color wheel control.

Channel

This menu is set for the Histogram, Color, and Levels sections of the Color Corrector node. When the

red channel is selected, the controls in each mode affect the red channel only, and so on.

The controls are independent, so switching to blue does not remove or eliminate any changes made

to red, green, or Master. The animation and adjustments made to each channel are separate. This

menu simply determines what controls to display.

Contrast

Contrast is the range of difference between the light to dark areas. Increasing the value of this slider

increases the contrast, pushing color from the midrange toward black and white. Reducing the contrast

causes the colors in the image to move toward midrange, reducing the difference between the darkest

and brightest pixels in the image.

Gain

The Gain slider is a multiplier of the pixel value. A gain of 1.2 makes a pixel that is R0.5 G0.5 B0.4 into

R0.6 G0.6, B0.48 (i.e., 0.4 * 1.2 = 0.48), while leaving black pixels totally unaffected. Gain affects higher

values more than it affects lower values, so the effect is strongest in the midrange and top range of

the image.

Lift

While Gain scales the color values around black, Lift scales the color values around white. The pixel

values are multiplied by the value of this control. A Lift of 0.5 makes a pixel that is R0.0 G0.0 B0.0 into

R0.5 G0.5, B0.5, while leaving white pixels totally unaffected. Lift affects lower values more than it

affects higher values, so the effect is strongest in the midrange and low range of the image.

Gamma

Values higher than 1.0 raise the Gamma (mid gray), whereas lower values decrease it. The effect of

this node is not linear, and existing black or white points are not affected at all. Pure gray colors are

affected the most.

Brightness

The value of the Brightness slider is added to the value of each pixel in your image. This control’s

effect on an image is linear, so the effect is applied identically to all pixels despite value.

Reset All Color Changes

Selecting this button returns all color controls in this section to their default values.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Correction Tab Levels Menu

The main Correction tab is further separated into four types of correction methods: colors, levels,

histogram, and suppress. When Levels is selected from the menu, you can remap the white and

black points of an image, with a Gamma control to adjust midtones. A histogram provides a view of

the tonal distribution in the image to help guide your adjustments. The Level method is described in

detail below.

Color Corrector Levels controls

Range

Identical to the Range menu when Color is selected in the Menu, the Range menu determines the

tonal range affected by the color correction controls in this tab. The menu can be set to Shadows,

Midtones, Highlights, and Master, where Master is the default affecting the entire image.

The selected range is maintained throughout the Colors, Levels, and Suppress sections of the Color

Corrector node.

Adjustments made to the image in the Master channel are applied to the image after any changes

made to the Highlights, Midtones, and Shadows ranges.

NOTE: The controls are independent for each color range. For example, adjusting the

Gamma control while in Shadows mode does not change or affect the value of the Gamma

control for the Highlights mode. Each control is independent and applied separately.

Channel

This menu is used to select and display the histogram for each color channel or for the Master channel.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Histogram Display

A histogram is a chart that represents the distribution of color values in the scene. The chart reads

from left to right, with the leftmost values representing the darkest colors in the scene and the

rightmost values representing the brightest. The more pixels in an image with the same or similar

value, the higher that portion of the chart is.

Luminance is calculated per channel; therefore, the red, green, and blue channels all have their own

histogram, and the combined result of these comprises the Master Histogram.

To scale the histogram vertically, place the mouse pointer inside the control and drag the pointer up to

zoom in or down to zoom out.

Display Selector Toolbar

The Display Selector toolbar at the top of the histogram provides a method of enabling and disabling

components of the histogram display. Hold the mouse pointer over the button to display a tooltip that

describes the button’s function.

�Input Histogram: This enables or disables the display of the input image’s histogram.

�Reference Histogram: This enables or disables the display of the reference image’s histogram.

�Output Histogram: This enables or disables the display of the histogram from the post-color-

corrected image.

�Corrective Curve: This toggles the display of a spline used to visualize exactly how auto color

corrections applied using a reference image are affecting the image. This can be useful when

equalizing luminance between the input and reference images.

Histogram Controls

These controls along the bottom of the histogram display are used to adjust the input image’s

histogram, compressing or shifting the ranges of the selected color channel.

The controls can be adjusted by dragging the triangles beneath the histogram display to the left

and right.

Shifting the High value toward the left (decreasing the value) causes the histogram to slant toward

white, shifting the image distribution toward white. The Low value has a similar effect in the opposite

direction, pushing the image distribution toward black.

Output Level

The Output Level control can apply clipping to the image, compressing the histogram. Decreasing the

High control reduces the value of pixels in the image, sliding white pixels down toward gray and gray

pixels toward black.

Adjusting the Low control toward High does the opposite, sliding the darkest pixels toward white.

If the low value were set to 0.1, pixels with a value of 0.0 would be set to 0.1 instead, and other values

would increase to accommodate the change. The best way to visualize the effect is to observe the

change to the output histogram displayed above.

Reset All Levels

Clicking this button resets all the controls in the Levels section to their defaults.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Correction Tab Histogram Menu

When the menu is set to Histogram, a histogram display is produced of the input image. If a reference

image is also provided, the histogram for the reference image is also displayed. The controls in this

tab are primarily used to match one image to another, using either the Equalize or Match modes of

the Color Corrector.

Color Correction in Histogram mode

Channel

This menu is used to select and display the histogram for each color channel or for the Master channel.

Histogram Display

A histogram is a chart that represents the distribution of color values in the scene. The chart reads

from left to right, with the leftmost values representing the darkest colors in the scene and the

rightmost values representing the brightest. The more pixels in an image with the same or similar

value, the higher that portion of the chart is.

Luminance is calculated per channel; therefore, the red, green, and blue channels all have their own

histogram, and the combined result of these comprises the Master Histogram.

To scale the histogram vertically, place the mouse pointer inside the control and drag the pointer up to

zoom in or down to zoom out.

Display Selector Toolbar

The Display Selector toolbar at the top of the histogram provides a method of enabling and disabling

components of the histogram display. Hold the mouse pointer over the button to display a tooltip that

describes the button’s function.

�Input Histogram: This enables or disables the display of the input image’s histogram.

�Reference Histogram: This enables or disables the display of the reference image’s histogram.

�Output Histogram: This enables or disables the display of the histogram from the post-color-

corrected image.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

�Corrective Curve: This toggles the display of a spline used to visualize exactly how auto color

corrections applied using a reference image are affecting the image. This can be useful when

equalizing luminance between the input and reference images.

Float Images and Histogram Equalization or Matching

By using the Histogram Match or Equalize methods on a float image, the color depth of the output

image is converted to 16-bit integer. Two-dimensional histograms are not well suited to working

with the extreme dynamic range of float images, so these operations always revert to 16-bit integer

processing.

Histogram Type

Each of these menu options enables a different type of color correction operation.

�Keep: Keep produces no change to the image, and the reference histogram is ignored.

�Equalize: Selecting Equalize adjusts the source image so that all the color values in the image are

equally represented—in essence, flattening the histogram so that the distribution of colors in the

image becomes more even.

�Match: The Match mode modifies the source image based on the histogram from the reference

image. It is used to match two shots with different lighting conditions and exposures so that they

appear similar.

When selected, the Equalize and Match modes reveal the following controls.

�Match/Equalize Luminance: This slider affects the degree that the Color Corrector node attempts

to affect the image based on its luminance distribution. When this control is zero (the default),

matching and equalization are applied to each color channel independently, and the luminance, or

combined value of the three color channels, is not affected.

If this control has a positive value when equalizing the image, the input image’s luminance

distribution is flattened before any color equalization is applied.

If this control has a positive value when the correction mode is set to Match, the luminance

values of the input are matched to the reference before any correction is applied to the R, G, and

B channels.

The Luminance and RGB controls can have a cumulative effect, and generally they are not both

set to full (1.0) simultaneously.

�Lock R/G/B: When this checkbox is selected, color matching is applied to all color channels

equally. When the checkbox is not selected, individual controls for each channel appear.

Equalize/Match R/G/B

The name of this control changes depending on whether the Equalize or Match modes have been

selected. The slider can be used to reduce the correction applied to the image to equalize or match it.

A value of 1.0 causes the full effect of the Equalize or Match to be applied, whereas lower values

moderate the result.

Precision

This menu determines the color fidelity used when sampling the image to produce the histogram.

10-bit produces higher fidelity than 8-bit, and 16-bit produces higher fidelity than 10-bit.

Smooth Correction

Often, color equalization and matching operations introduce posterization in an image, which

occurs because gradients in the image have been expanded or compressed so that the dynamic

range between colors is not sufficient to display a smooth transition. This control can be used to

smooth the correction curve, blending some of the original histogram back into the result for a more

even transition.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Snapshot Match Time

Click this button to take a freeze snapshot of the current reference histogram, storing its current

state as a snapshot in memory. If the reference histogram is not snapshot, the reference histogram is

updated from frame to frame. This can cause flickering and phasing of the correction as the node tries

to match a changing source to a changing reference.

Release Match

Click this button to release the current snapshot of the histogram and return to using the live

reference input.

Reset All Histogram Changes

Selecting this button removes all changes made to the histogram, returning the controls to default and

setting the mode back to Keep.

Correction Tab Suppress Menu

Color Suppression provides a mechanism for removing an unwanted color component from the image.

The Color Wheel control is similar to that shown in the Colors section of the node, but this one is

surrounded by six controls, each representing a specific color along the wheel.

To suppress a color in the selected range, drag the control that represents that color toward the center

of the color wheel. The closer the control is to the center, the more that color is suppressed from

the image.

Color Corrector Suppression controls

Suppression Angle

Use the Suppression Angle control to rotate the controls on the suppression wheel and zero in on a

specific color.

Reset All Suppression

Clicking this control resets the suppression colors to 1.0, the default value.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Ranges Tab

The Ranges tab contains the controls used to specify which pixels in an image are considered to be

shadows and which are considered to be highlights. The midrange is always calculated as pixels not

already included in the shadows or the highlights.

Color Corrector Luminance controls

Range

This menu is used to select the tonal range displayed in the viewers. They help to visualize the pixels

in the range. When the Result menu option is selected, the image displayed by the color corrector in

the viewers is that of the color corrected image. This is the default.

Selecting one of the other menu options switches the display to a grayscale image showing which

pixels are part of the selected range. White pixels represent pixels that are considered to be part of

the range, and black pixels are not in the range. For example, choosing Shadows would show pixels

considered to be shadows as white and pixels that are not shadows as black. Mid gray pixels are only

partly in the range and do not receive the full effect of any color adjustments to that range.

Channel

The Channel menu in this tab can be used to examine the range of a specific color channel. By default,

Fusion displays the luminance channel when the color ranges are examined.

Spline Display

The ranges are selected by manipulating the spline handles. There are four spline points, each with

one Bézier handle. The two handles at the top represent the start of the shadow and highlight ranges,

whereas the two at the bottom represent the end of the range. The Bézier handles are used to control

the falloff.

The midtones range has no specific controls since its range is understood to be the space between

the shadow and the highlight ranges.

The X and Y text controls below the spline display can be used to enter precise positions for the

selected Bézier point or handle.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Output the Range You See Now as Final Render

Selecting this checkbox causes the monochrome display of the range shown in the viewers to be

output as the final render. Normally, the Color node outputs the full RGBA image, even if the node

were left to display one of the color ranges in the view instead. This control makes it possible to use

the Color Corrector node to generate a range’s matte for use as an effect mask in other nodes.

Preset Simple/Smooth Ranges

These two buttons can be used to return the spline ranges to either Smooth (default) or Simple

(linear) settings.

Options Tab

The Options tab includes a few very important processing operations including a simple solution when

color correcting premultiplied Alpha channels.

Color Corrector controls

Pre-Divide/Post-Multiply

Selecting this option divides the color channels by the value of the Alpha before applying the color

correction. After the color correction, the color values are re-multiplied by the Alpha to produce a

properly additive image. This is crucial when performing an additive merge or when working with CG

images generated with premultiplied Alpha channels.

Histogram Proxy Scale

The Histogram Proxy Scale determines the precision used when creating and calculating histograms.

Lower values represent higher precision, and higher values produce a rougher, generalized histogram.

Process Order

This menu is used to select whether adjustments to the image’s gamma are applied before or after any

changes made to the images levels.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION