---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 387
---

# Inspector

Color Space controls

Controls Tab

The Controls tab in the Color Space node consists of two menus. The top Conversion menu

determines whether you are converting an image to RGB or from RGB. The bottom menu selects the

alternative color space you are either converting to or from.

Conversion

This menu has three options. The None option has no effect on the image. When To Color is selected,

the input image is converted to the color space selected in the Color Type control found below. When

To RGB is selected, the input image is converted back to the RGB color space from the type selected

in the Color Type menu (for example, YUV to RGB).

Color Type

This menu is used to select the color space conversion applied when the To Color conversion is

selected. When the To RGB option is selected in the Conversion menu, the Color Type option should

reflect the input image’s current color space. There are eight color space options to choose from.

�HSV (Hue, Saturation, and Value): Each pixel in the HSV color space is described in terms of its

Hue, Saturation, and Value components. Value is defined as the quality by which we distinguish

a light color from a dark one or brightness. Decreasing saturation roughly corresponds to adding

white to a paint chip on a palette. Increasing Value is roughly similar to adding black.

�YUV (Luma, Blue Chroma, and Red Chroma): The YUV color space is used in the analog

broadcast of PAL video. Historically, this format was often used to color correct images because

of its familiarity to a large percentage of video engineers. Each pixel is described in terms of its

Luminance, Blue Chroma, and Red Chroma components.

�YIQ (Luma, In Phase, and Quadrature): The YIQ color space is used in the analog broadcast of

NTSC video. This format is much rarer than YUV and almost never seen in production. Each pixel

is described in terms of its Luminance, Chroma (in-phase or red-cyan channel), and Quadrature

(magenta-green) components.

�CMY (Cyan, Magenta, and Yellow): Although more common in print, the CMY format is often

found in computer graphics from other software packages. Each pixel is described in terms of its

Cyan, Magenta, and Yellow components. CMY is nonlinear.

�HLS (Hue, Luminance, and Saturation): Each pixel in the HLS color space is described in terms

of its Hue, Luminance, and Saturation components. The differences between HLS and HSV color

spaces are minor.

�XYZ (CIE Format): This mode is used to convert a CIE XYZ image to and from RGB color spaces.

CIE XYZ is a weighted space, instead of a nonlinear one, unlike the other available color spaces.

Nonlinear in this context means that equal changes in value at different positions in the color

space may not necessarily produce the same magnitude of change visually to the eye.

Expressed simply, the CIE color space is a perceptual color system, with weighted values obtained

from experiments where subjects were asked to match an existing light source using three primary

light sources.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

This color space is most often used to perform gamut conversion and color space matching

between image display formats because it contains the entire gamut of perceivable colors.

�Negative: The color channels are inverted. The color space remains RGBA.

�BW: The image is converted to black and white. The contribution of each channel to the luminance

of the image is adjustable via slider controls that appear when this option is selected. The default

values of these sliders represent the usual perceptual contribution of each channel to an image’s

luminance. The color space of the image remains RGBA.

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Copy Aux [CpA]

The Copy Aux node

Copy Aux Node Introduction

The Copy Aux node is used to shuffle channels between visible channels and auxiliary data channels

in a single 2D image. Typically, these auxiliary channels are rendered from 3D applications. Auxiliary

channels supported in the Copy Aux node include background color, z-depth, texture coordinates,

coverage, object ID, material ID, normals, vectors, back vectors, and world position.

The Copy Aux node is mostly a convenience node, as the copying can also be accomplished with

more effort using a Channel Booleans node. Where Channel Booleans deals with individual channels,

Copy Aux deals with channel groups. By default, the Copy Aux node automatically promotes the depth

of its output to match the depth of the aux channel.

Copy Aux also supports static normalization ranges. The advantage of static normalization versus

the dynamic normalization that Fusion’s viewers do is that colors remain constant over time. For

example, if you are viewing Z or WorldPos values for a ball, you see a smooth gradient from white to

black. Now imagine that some other 3D object is introduced into the background at a certain time.

Dynamic normalization turns the ball almost completely white while the background object is now the

new black. Dynamic normalization also causes flicker problems while viewing vector/disparity channels,

which can make it difficult to compare the aux channels of two frames at different times visually.

Inputs

The Copy Aux node includes two inputs: one for the main image and the other for an effect mask.

Input: This orange input is the only required connection. It connects a 2D image for the Copy Aux

node operation.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

Copy Aux operation to only those pixels within the mask. An effect mask is applied to the tool after the

tool is processed.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Basic Node Setup

The Copy Aux node, like many 2D image-processing nodes, receives a 2D image like a Loader node

or the MediaIn1 shown below. The output continues the node tree by connecting to another 2D image-

processing node or a Merge node.

A Copy Aux node applied to a MediaIn1 node

Inspector

Copy Aux controls

Controls Tab

The Controls tab is used to copy auxiliary channel groups into RGBA channels. Although Copy

Aux has quite a few options, most of the time you select only the channel to copy and ignore the

remaining functionality.

Mode

The Mode menu determines whether the auxiliary channel is copied into the RGBA color channel

(Aux to Color) or vice versa (Color to Aux). Using this option, you can use one Copy Aux node to bring

an auxiliary channel into color, do some compositing operations on it, and then use another Copy Aux

node to write the color back into the auxiliary channel. When the Mode is set to Color to Aux, all the

options in the Controls tab except the Aux Channel menu are hidden.

Aux Channel

The Aux Channel menu selects the auxiliary channel to be copied from or written to depending on

the current mode. When the aux channel abcd has one valid component, it is copied as aaa1, two valid

components as ab01, three valid components as abc1, and four components as abcd. For example, the

Z-channel is copied as zzz1, texture coordinates as uv01, and normals as nxnynz1.

Out Color Depth

Out Color Depth controls the color depth of the output image. Most aux channels contain float values

or, if they are integer valued, they can contain values beyond 255. When you copy float values into an

int8 or int16 image, this can be a problem since negative values and values over 1.0 can get clipped.

In addition, precision can be lost. This option determines what happens if the depth of RGBA channels

of the input image is insufficient to contain the copied aux channel.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Be careful when copying float channels into integer image formats, as they can get clipped if you do

not set up Copy Aux correctly. For this node, all aux channels are considered to be float32 except

ObjectID or MaterialID, which are considered to be int16.

�Match Aux Channel Depth: The bit depth of the RGBA channels of the output image is increased

to match the depth of the aux channel. Specifically, this means that the RGBA channels of the

output image are either int16 or float32. Be careful when using this option because, for example,

if you normally have int8 color channels, you are now using 2x or 4x more memory for the

color channels. Particularly, the Z, Coverage, TextureCoordinate, Normal, Vector, BackVector,

WorldPosition, and Disparity channels are always output as float, and the Material/ObjectID

channels are output as int16.

�Match Source Color Depth: The bit depth of the RGBA channels of the output image is the same

as the input image. This can have some unexpected consequences. For example, if your input

image is int8, the XYZ components of normals that are floating-point numbers in the [-1, 1] range

are clipped to non-negative numbers [0, 1] range. As a more extreme example, consider what

happens to Z values. Z values are floating-point numbers stored in the [-1e30, 0] range, and they

all get truncated to the [0, 1] range, which means your Z-channel is full of zeroes.

�Force Float32: The bit depth of the RGBA channels of the output image is always float32.

Channel Missing

Channel Missing determines what happens if a channel is not present. For example, this determines

what happens if you chose to copy Disparity to Color and your input image does not have a Disparity

aux channel.

�Fail: The node fails and prints an error message to the console.

�Use Default Value: This fills the RGBA channels with the default value of zero for everything

except Z, which is -1e30.

Kill Aux Channels

When this is checked, Copy Aux copies the requested channel to RGBA and then outputs a resulting

image that is purely RGBA with other channels being killed. This is useful if you want to increase the

number of frames of Copy Aux that can be cached for playback—for example, to play back a long

sequence of disparity. A handy tip is that you can use the Kill Aux feature also with just Color to Aux >

Color for a longer color playback.

Kill Aux channels


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Enable Remapping

When remapping is enabled, the currently selected aux channel is rescaled, linearly mapping the

range according to the From and To slider selections as explained below. The Remapping options are

applied before the conversion operation. This means you could set the From > Min-Max values to -1,

1 to rescale your normals into the [0, 1] range, or set them to [-1000, 0] to rescale your Z values from

[-1000, 0] into the [0, 1] range before the clipping occurs.

Note that the Remapping options are per channel options. That means the default scale for normals

can be set to [-1, +1] > [0, 1] and for Z it can be set [-1000, 0] > [0, 1]. When you flip between normals and

Z, both options are remembered. One way this could be useful is that you can set up the remapping

ranges and save this as a setting that you can reuse. The remapping can be useful to squash the aux

channels into a static [0, 1] range for viewing or, for example, if you wish to compress normals into the

[0, 1] range to store them in an int8 image.

�From > Min: This is the value of the aux channel that corresponds to To > Min.

�From > Max: This is the value of the aux channel that corresponds to To > Max. It is possible to set

the max value less than the min value to achieve a flip/inversion of the values.

�Detect Range: This scans the current image to detect the min/max values and then sets the

From > Min/ From > Max Value controls to these values.

�Update Range: This scans the current image to detect the min/max values and then enlarges the

current [From > Min, From > Max] region so that it contains the min/max values from the scan.

�To > Min: This is the minimum output value, which defaults to 0.

�To > Max: This is the maximum output value, which defaults to 1.

�Invert: After the values have been rescaled into the [To > Min, To > Max] range, this

inverts/flips the range.

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Gamut [Gmt]

The Gamut node

Gamut Node Introduction

The Gamut node has controls to transform one color space to another and remove/add gamma curves.

This node, along with the Cineon Log node, is primarily used to linearize incoming images and then

reapply the applicable output gamma curve at the end of a node tree.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION