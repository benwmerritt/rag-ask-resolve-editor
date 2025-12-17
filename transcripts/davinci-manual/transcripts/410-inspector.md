---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 410
---

# Inspector

Grain controls

Controls Tab

The Controls tab includes all the parameters for modifying the appearance of the grain.

Power

This slider determines the strength of the grain. A higher value increases visibility, making the grain

more prevalent.

RGB Difference

Separate Red, Green, and Blue sliders are used to modify the strength of the effect on a per

channel basis.

Grain Softness

This slider controls the blurriness or fuzziness of the grain. Smaller values cause the grain to be more

sharp or coarse.

Grain Size

This slider determines the size of the grain particles. Higher values increase the grain size.

Grain Spacing

This slider determines the density or amount of grain per area. Higher values cause the grain to

appear more spaced out.

Aspect Ratio

This slider adjusts the aspect of the grain so that it can be matched with anamorphic images.

Alpha-Multiply

When enabled, this checkbox multiplies the image by the Alpha, clearing the black areas of any

grain effect.


Fusion Page Effects | Chapter 99 Film Nodes

FUSION

Grain Spread controls

Spread Tab

The Spread tab uses curves for the red, green, and blue channels to control the amount of grain over

each channel’s tonal range.

RGB Checkboxes

The red, green, and blue checkboxes enable each channel’s custom curve, allowing you to control

how much grain appears in each channel. To mimic usual film responses, more grain would appear

in the blue channel than the red, and the green channel would receive the least. Right-clicking in the

spline area displays a contextual menu containing options related to modifying spline curves.

For more information on the LUT Editor’s controls see Chapter 107, “LUT Nodes,” in the DaVinci

Resolve Reference Manual, or Chapter 47 in the Fusion Reference Manual.

In and Out

This control provides direct editing of points on the curve by setting In/Out point values.

Examples

Default Spread

In the default setting, the grain is applied evenly to the entire image, as shown here. However,

film often shows a different amount of grain in the blacks, mids, and whites.


Fusion Page Effects | Chapter 99 Film Nodes

FUSION

Bell-Shaped Spread

Setting a bell shape is often a good starting point to create a more realistic-looking grain.

Here we have a non-uniform distribution with different amounts of grain in the red, green, and

blue channels.

In both examples, the grain’s power has been exaggerated to show the effect a bit better.

Common Controls

Setting Tab

The Settings tab controls are common to all Film nodes, so their descriptions can be found in

“The Common Controls” section at the end of this chapter.

Light Trim [LT]

The Light Trim node

Light Trim Node Introduction

This node emulates film scanner light trims. By design, this node works best with logarithmic data,

such as the images stored by Cineon, Arri, or Blackmagic RAW files. When logarithmic data is

provided, the Light Trim node can be used to increase or decrease the apparent exposure level of

the image.


Fusion Page Effects | Chapter 99 Film Nodes

FUSION

Inputs

There are two Inputs on the Light Trim node: one for the 2D image and one for the effects mask.

Input: The orange input is used for the primary Log 2D image that gets its exposure adjusted.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the exposure change to be

within the pixels of the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Light Trim node is placed after a LOG clip but before the Log clip is converted by a

Cineon LOG node.

A Light Trim node used to adjust exposure on a LOG clip

Inspector

Light Trim controls

Controls Tab

The Controls tab includes a single slider that adjusts the exposure of the image.

Lock RGBA

When selected, the Lock RGBA control collapses control of all image channels into one slider.

This selection is on by default. To manipulate the various color channels independently, deselect

this checkbox.

Trim

This slider shifts the color in film, optical printing, and lab printing points. 8 points equals one stop

of exposure.

Common Controls

Settings Tab

The Settings tab controls are common to all Film nodes, so their descriptions can be found in “The

Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 99 Film Nodes

FUSION

Remove Noise [RN]

The Remove Noise node

Remove Noise Node Introduction

The Remove Noise node provides simple noise management. The basic operation is that the node

blurs the image channels, and then compares the blurred image to the original to extract the noise.

A sharpness is then applied to the image, except where noise was detected.

To use this node, view the image and look at the red channel. Then increase the Red Softness until the

grain appears to be gone. Next, increase the sharpness until the detail reappears, but stop before the

grain reappears. Repeat for the green and blue channels.

Inputs

There are two inputs on the Remove Noise node: one for the 2D image and one for the effects mask.

Input: The orange input is used for the primary 2D image that gets noise removed.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the noise removal change

to be within the pixels of the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Remove Noise node can be used on any clip with noise. For example, it is used below to remove

noise prior to keying the clip using the DeltaKeyer.

A Remove Noise node used to remove noise prior to keying

Inspector

Remove Noise controls


Fusion Page Effects | Chapter 99 Film Nodes

FUSION

Controls Tab

The Controls tab switches the noise removal between two methods: Color and Chroma. When the

Method is set to Color, the Controls tab adjusts the amount of blur and sharpness individually for each

RGB channel. When the Method is set to Chroma, the blur and sharpness is adjusted based on Luma

and Chroma controls.

Method

This menu is used to choose whether the node processes color using the Color or Chroma method.

This also gives you a different set of control sliders.

Lock

This checkbox links the Softness and Detail sliders of each channel together.

Softness Red, Green, and Blue

The Softness sliders determine the amount of blur applied to each channel of the image. In Chroma

mode, you have sliders for the softness in the Luminance and Chrominance channels, respectively.

Detail Red, Green, and Blue

The Sharpness sliders determine how much detail is reintroduced into each channel after

each channel is softened. In Chroma mode, you have sliders for Luminance and Chrominance

channels, respectively.

Chroma Method controls

Common Controls

Settings Tab

The Settings tab controls are common to all Film nodes, so their descriptions can be found in the

following “The Common Controls” section.


Fusion Page Effects | Chapter 99 Film Nodes

FUSION