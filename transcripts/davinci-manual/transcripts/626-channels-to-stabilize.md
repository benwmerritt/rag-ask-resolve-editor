---
title: "Channels to Stabilize"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 626
---

# Channels to Stabilize

Once you’ve analyzed the frame that represents the best contrast and color for that clip, the Channels

to Stabilize controls let you choose how to make the correction. The What to Stabilize pop-up menu

lets you choose between stabilizing White Balance and Brightness, or R, G, B Channels Separately.

�If you choose White Balance and Brightness, two checkboxes let you choose whether or not you

want to include Stabilize White Balance and Stabilize Brightness independently from one another.

�If you choose R, G, B channels separately, three checkboxes appear letting for Stabilize Red,

Green, and Blue Channel, so you can pick which particular channels you want to correct.

The Stabilize drop-down menu lets you choose how to make the correction, with the options Levels

and Contrast, Offset, and Gain, each of which uses a different method to make the necessary

correction, so if one method doesn’t work for the particular problem your clip is exhibiting, you can try

the other methods to try and get a better result.

Captured Analysis Values

Once you’ve analyzed the frame, another set of parameters appear showing the captured analysis

values upon which the automated correction is based, so that you can make manual adjustments

if necessary to improve the result. The parameters that are shown depend on the option you chose

from the What to Stabilize pop-up menu.

�If you chose White Balance and Brightness, then you’ll have a Normalized White Balance color

control, and Low Level and High Level sliders.

�If you chose R, G, B Channels Separately, then you’ll have Red, Green, and Blue High and

Low Level sliders.

Contrast Pop (Studio Version Only)

A more extreme and selective version of the Midtone Detail control found in the Color Wheels palette,

designed to add either sharp high-contrast looks, or soft low-contrast looks to a selective portion of

the tonal range of the image.

�Detail Amount: Lets you choose how much of this effect to apply. At 0, no effect is applied. At

positive values progressively sharper contrast is added, while at negative values progressively

softer low-contrast is applied.

�Detail size: Lets you choose which structures of the image are affected by this localized contrast

adjustment, from smaller to larger.

�Low and High Threshold: These values let you define what range of image tonality is affected by

this filter, allowing you to omit either shadows or highlights from this operation.

�Softness: Lets you soften the transition between the affected and unaffected areas of the image.


Resolve FX Overview | Chapter 156 Resolve FX Color

COLOR

DCTL (Studio Version Only)

Lets you apply a DCTL wherever you can apply ResolveFX plugins.

For more information on DCTLs and where they’re installed, see Chapter 200, “Creating

DCTL LUTs.”

�DCTL List: A pop-up that lets you choose from the available DCTLs installed on your

workstation location.

On Mac OS X: Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/

On Windows: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT

On Linux: /home/resolve/LUT

�Reload DCTL: Allows users to refresh the currently loaded DCTL file content. This lets the user

make changes in the DCTL using a text editor, then reload it to see the results. It does not refresh

the DCTL list; to do so, you must restart the DaVinci Resolve application.

Dehaze (Studio Version Only)

Designed to let you make adjustments to color and contrast to reduce the visible effects of Aerial

Perspective (i.e., smog, airlight, and haze) in an image. This filter automatically generates a simulated

depth map, which is used to apply more of this corrective color adjustment to faraway parts of the

image that would be more affected by haze effects and less color adjustment to closeup parts of the

image. It estimates haze and has options for guiding that estimate and controlling the processing.

�Dehaze Strength: This slider applies a simultaneous color and contrast adjustment. Raising

Dehaze Strength subtly increases contrast (especially in the shadows) while rebalancing color

toward the complement of the currently selected Haze Color and selectively intensifying

saturation. Lowering Dehaze Strength decreases contrast and rebalances color toward the

selected Haze Color itself while selectively lowering saturation.

�Haze Color: A color control that lets you choose or sample the color of smog, airlight, or haze in an

image that you want to minimize.

�Display Depth: Lets you view the simulated depth matte that’s being generated. Turn this on

before adjusting the Shadow and Highlight controls below.

�Shadow: This slider raises or lowers darkest parts of the simulated depth map that defines the

parts of the image that are estimated to be farthest away.

�Highlight: This slider lets you raise or lower the lightest parts of the simulated depth map that

defines the parts of the image that are estimated to be closest to us.

Despill

Removes the color cast on a subject caused by the reflection of light off the green or blue screen.

This color cast can remain after the green screen has been keyed out. This Despill filter is useful for

reducing spill after keying, or with externally generated keys or masks.


Resolve FX Overview | Chapter 156 Resolve FX Color

COLOR

The Despill FX removing a green color cast from the subject’s arms and hair. Above is no despill and below is full despill.

�Key Color: Sets the color to be removed from the subject, either Red, Green, or Blue.

�Strength: The amount of Despill to apply. 1.000 is equal to despill “on” in the previous version

of the 3D Keyer checkbox. Variable strength comes in handy as you can preserve more of the

original color information if the context allows it. For example, less despill is appropriate if the new

composited background will also be green.


Resolve FX Overview | Chapter 156 Resolve FX Color

COLOR

False Color (Studio Version Only)

False Color is designed to replicate exactly the false color readout of a Blackmagic Design camera but

can also be used as a creative effect that can be used for replicating camera HUDs, infrared sensors,

and custom posterization looks by remapping pixel brightness to customizable color bands and

gradients. The color set can either match the False Color setting in a specific Blackmagic Design camera

or be customized with a list of creative style presets provided for use or inspiration. The presets can be

modified by setting the number of colors used and defining the tonal range each color represents.

Resolve FX False Color Camera preset and legend

Resolve FX False Color thermal creative preset and legend

General

�Plugin Mode: This menu is used to switch between matching a specific Blackmagic Design

Camera’s False Color setting or accessing creative presets. When Specific Camera Model is

chosen, the Camera Model section is displayed for selecting the camera and settings you want to

use. When Creative is chosen, the Color bands section is displayed for choosing and customizing

the preset.


Resolve FX Overview | Chapter 156 Resolve FX Color

COLOR

Camera Model

The Camera Model controls are displayed when Specific Camera Model is chosen from the Plugin

Model menu. These menus allow you to match the False Color from a camera configuration.

�Camera: Selects the exact Blackmagic Design camera sensor.

�Camera Mode: Selects the dynamic range setting.

�ISO Level: Sets the ISO or light sensitivity setting.

Color Bands

These controls are displayed when Creative is chosen from the Plugin Model menu. The Color Bands

group of controls are used to select and modify the appearance of the False Color presets.

�Creative Style: Selects one of the built-in style presets for the effect.

�Number of Bands: Lets you choose how many different colors are in the scale.

�Show Sliders: Exposes the Top and Bottom controls letting you select the specific range of a color

in percentage values. For example, setting a Red color value between Bottom 45 and Top 55

will tint red anything in the image between 45 and 55% brightness on the waveform monitor.

�Color: Provides either a color swatch or picker to choose the color for the band.

Preprocessing

This group of controls is used to apply tonal and blur processing to the image.

�Blur: Applies a blur filter to the image before analysis.

�Black Level: Increases or decreases the shadow range assigned to colors that fall lower on the

False Color legend.

�White Level: Increases or decreases the highlight range assigned to colors that fall higher on the

False Color legend.

�Gamma: Shifts the mid-tone range towards colors that fall lower or higher on the False Color legend.

Scale/Legend

This section is used to control the visibility and appearance of the False Color legend shown at the left

of the frame. The Legend shows how dark to light inputs get mapped to new colors. It is burned in to

the image.

�Show Scale: Shows or hides the Legend.

�Show Values: Shows or hides numeric values on the Legend. These numeric values represent

different scales based on the Value Style menu.

�Show Labels: Shows or hides data point labels on the Legend. The labels identify important data

points along the tonal range, such as black clipping, white clipping, and middle gray.

�Contrast: Increases or decreases the transparency of the Legend’s background underlay.

�Value Detail: Increases or decreases the number of axis value labels displayed on the Legend.

�Value Style: This menu includes three options for the scale used for the Legend’s numeric values.

Percentage: Uses a percentage scale for the Legend, going from 0% at

the bottom to 100% at the top.

Hundredths: Uses a Hundredths scale for the Legend, going from 0 at

the bottom to 100 at the top with no “%” symbol.

Normalized: Uses a Normalized scale for the Legend, going from 0.0 at

the bottom to 1.0 at the top.


Resolve FX Overview | Chapter 156 Resolve FX Color

COLOR