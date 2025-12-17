---
title: "Basic Node Setup"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 444
---

# Basic Node Setup

Below, the Matte Control node is set up to copy the foreground (green) input’s alpha channel into the

background (orange) input. The output of the Matte Control is then an image with an alpha channel

used as the foreground composite in the Merge node.

A Matte Control embedded an alpha from the

foreground input to the background input

Inspector

The Matte Control Matte tab

Matte Tab

The Matte tab combines and modifies alpha or color channels from an image in the foreground input

with the background image.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Combine

Use this menu to select which operation is applied. The default is set to None for no operation.

�None: This causes the foreground image to be ignored.

�Combine Red: This combines the foreground red channel to the background alpha channel.

�Combine Green: This combines the foreground green channel to the background alpha channel.

�Combine Blue: This combines the foreground blue channel with the background alpha channel.

�Combine Alpha: This combines the foreground alpha channel with the background alpha channel.

�Solid: This causes the background alpha channel to become completely opaque.

�Clear: This causes the background alpha channel to become completely transparent.

Combine Operation

Use this menu to select the method used to combine the foreground channel with the background.

�Copy: This copies the foreground source over the background alpha, overwriting any existing

alpha in the background.

�Add: This adds the foreground source to the background alpha.

�Subtract: This subtracts the foreground source from the background alpha.

�Inverse Subtract: This subtracts the background alpha from the foreground source.

�Maximum: This compares the foreground source and the background alpha and takes the value

from the pixel with the highest value.

�Minimum: This compares the foreground source and the background alpha and takes the value

from the pixel with the lowest value.

�And: This performs a logical AND on the two values.

�Or: This performs a logical OR on the values.

�Merge Over: This merges the foreground source channel over the background alpha channel.

�Merge Under: This merges the foreground source channel under the background alpha channel.

Filter

Selects the Filter that is used when blurring the matte.

�Box Blur: This option applies a Box Blur effect to the whole image. This method is faster than the

Gaussian blur but produces a lower-quality result.

�Bartlett: Bartlett applies a more subtle, anti-aliased blur filter.

�Multi-Box: Multi-Box uses a box filter layered in multiple passes to approximate a Gaussian shape.

With a moderate number of passes (e.g., four), a high-quality blur can be obtained, often faster

than the Gaussian filter and without any ringing.

�Gaussian: Gaussian applies a smooth, symmetrical blur filter, using a sophisticated constant-time

Gaussian approximation algorithm. In extreme cases, this algorithm may exhibit ringing; see below

for a discussion of this. This mode is the default filter method.

Blur

This blurs the edge of the matte using a standard, constant speed Gaussian blur. A value of zero

results in a sharp, cutout-like hard edge. The higher the value, the more blur is applied to the matte.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Clipping Mode

This option determines how edges are handled when performing domain of definition rendering.

This is profoundly important when blurring the matte, which may require samples from portions of the

image outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition. If

the upstream DoD is smaller than the frame, the remaining area in the frame is treated as

black/transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that is usually outside the upstream DoD is

treated as black/transparent.

Contract/Expand

This shrinks or grows the matte similar to an Erode Dilate node. Contracting the matte reveals more of

the foreground input, while expanding the matte reveals more of the background input. Values above

0.0 expand the matte, and values below 0.0 contract it.

Gamma

This raises or lowers the values of the matte in the semitransparent areas. Higher values cause

the gray areas to become more opaque, and lower values cause the gray areas to become more

transparent. Completely black or white regions of the matte remain unaffected.

Threshold

Any value below the lower threshold becomes black or transparent in the matte. Any value above

the upper threshold becomes white or opaque in the matte. All values within the range maintain their

relative transparency values.

Restore Fringe

This restores the edge of the matte around the keyed subject. Often when keying, the edge of the

subject where you have hair is clipped out. Restore Fringe brings back that edge while keeping the

matte solid.

Invert Matte

When this checkbox is selected, the alpha channel of the image is inverted, causing all transparent

areas to be opaque and all opaque areas to be transparent.

Solid Matte

Solid mattes are mask nodes or images connected to the solid matte input on the node. The solid

matte is applied directly to the alpha channel of the image. Generally, solid mattes are used to hold out

areas you want to remain opaque, such as someone with blue eyes against a blue screen.

Enabling Invert inverts the solid matte before it is combined with the source alpha.

Garbage Matte

Garbage mattes are mask nodes or images connected to the garbage matte input on the node.

The garbage matte is applied directly to the alpha channel of the image. Generally, garbage mattes

are used to remove unwanted elements that cannot be keyed, such as microphones and booms.

They are also used to fill in areas that contain the color being keyed but that you wish to maintain.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Garbage mattes of different modes cannot be mixed within a single tool. A Matte Control node is

often used after a Keyer node to add a garbage matte with the opposite effect of the matte applied

to the keyer.

Enabling Invert inverts the garbage matte before it is combined with the source alpha.

Post-Multiply Image

Selecting this option multiplies the color channels of the image against the alpha channel it creates for

the image. This option is usually enabled and is on by default.

Deselect this checkbox and the image can no longer be considered premultiplied for purposes

of merging it with other images. Use the Subtractive option of the Merge node instead of the

Additive option.

For more information on these Merge node settings, see Chapter 95, "Composite Nodes," in

the DaVinci Resolve Reference Manual, or Chapter 35 in the Fusion Reference Manual.

The Matte Control Spill tab

Spill Tab

The Spill tab handles spill suppression in the Matte Control. Spill suppression is a form of color

correction that attempts to remove the screen color from the fringe of the matte.

Spill is the transmission of the screen color through the semitransparent areas of the alpha channel. In

the case of blue- or green-screen keying, this usually causes the color of the background to become

apparent in the edges of the foreground subject.

Spill Color

This menu selects the color used as the base for all spill suppression techniques.

Spill Suppression

When this slider is set to 0, no spill suppression is applied to the image. Increasing the slider increases

the strength of the spill method.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Spill Method

This selects the strength of the algorithm used to apply spill suppression to the image.

�None: None is selected when no spill suppression is required.

�Rare: This removes very little of the spill color and is the lightest of all methods.

�Medium: This works best for green screens.

�Well Done: This works best for blue screens.

�Burnt: This works best for blue screen. Use this mode only for very troublesome shots.

Fringe Gamma

This control can be used to adjust the brightness of the fringe or halo that surrounds the keyed image.

Fringe Size

This expands and contracts the size of the fringe or halo surrounding the keyed image.

Fringe Shape

Fringe Shape presses the fringe toward the external edge of the image or pulls it toward the inner

edge of the fringe. Its effect is most noticeable while the Fringe Size value is large.

Cyan/Red, Magenta/Green, and Yellow/Blue

Use these three controls to color correct the fringe of the image.

This is useful for correcting semitransparent pixels that still contain color from the original background

to match the new background.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Matte nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Primatte [Pri]

The Primatte node

NOTE: Primatte is only available in Fusion Studio.

Primatte Node Introduction

Primatte is an advanced keying tool for Fusion Studio. To use Primatte effectively, you must

understand how it works. Using a series of selection buttons, Primatte assigns RGB pixels into one of

the four specific zones.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

�Zone 1: Complete background image.

�Zone 2: Foreground image with spill suppression and transparency.

�Zone 3: Foreground image with spill suppression only.

�Zone 4: Complete foreground image.

Depending on the type of blue- or green-screen content, you may find that the Delta Keyer or the

Primatte keyer handles the specific keying task better. There is no one-solution-fits-all when it comes

to keying, and in some cases, the combination of the two keyers may prove to be the best solution.

NOTE: Primatte is distributed and licensed by IMAGICA Corp. of America, Los Angeles, CA,

USA. Primatte was developed by and is a trademark of IMAGICA Corp., Tokyo, Japan.