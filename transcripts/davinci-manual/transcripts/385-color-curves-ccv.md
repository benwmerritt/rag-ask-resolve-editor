---
title: "Color Curves [CCv]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 385
---

# Color Curves [CCv]

The Color Curves node

Color Curves Node Introduction

The Color Curves node is a spline-based node for performing Lookup table (LUT) color manipulations.

A separate spline is provided for each color channel. The effect can be animated or dissolved and can

be applied to the image using RGB, YUV, YIQ, CMY, or HLS color spaces.

The LUT view in the Color Corrector can be scaled using the + and - keys on the numeric keypad.

The color curves LUT fully supports out-of-range values—i.e., pixels with color values above 1.0 or

below 0.0.

The splines shown in this LUT view are also available from the Spline Editor, should greater precision

be required when adjusting the controls.

Inputs

The Color Curves node includes three inputs in the Node Editor.

Input: This orange input is the only required connection. It connects a 2D image that is adjusted by the

color curves.

Effect Mask: The optional effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

color curves adjustment to only those pixels within the mask. An effect mask is applied to the tool after

it is processed.

Reference Image: The optional green input is used to connect a second 2D image that can be used

for reference matching.

Match Mask: This optional white input accepts any mask much like an effect mask. However, this mask

defines of the area to match during a Match. It offers more flexibility in terms of shape than the built-in

Match reference rectangle in the Inspector.

Basic Node Setup

The Color Curves node, like many 2D image-processing nodes, receives a 2D image like a Loader

node or the MediaIn1 shown below. The output continues the node tree by connecting to another 2D

image-processing node or a Merge node.

A Color Curves node applied to a MediaIn1 node


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Inspector

Color Curves controls

Controls Tab

The Controls tab for the color curves is divided into two sections. The top half of the Inspector

includes the curves and LUT controls. The bottom half is dedicated primarily to matching the

reference image.

Mode

The Mode options change between Animated and Dissolve modes. The default mode is No

Animation, where adjustments to the curves are static. Setting the mode provides a change spline for

each channel, allowing the color curve to be animated over time.

Dissolve mode is essentially obsolete and is included for compatibility reasons only.

Color Space

The splines in the LUT view represent color channels from a variety of color spaces. The default is

Red, Green, and Blue. The options in this menu allow an alternate color space to be selected.

A detailed description of the color spaces available here are below:

�RGB (Red, Green, Blue): Fusion uses the RGB color space, and most nodes and displays interpret

the primary channels of an image as Red, Green, and Blue.

�YUV (Luma, Blue Chroma, and Red Chroma): The YUV color space is used in the analog

broadcast of PAL video. Historically, this format was often used to color correct images, because

of its familiarity to a large percentage of video engineers. Each pixel is described in terms of its

Luminance, Blue Chroma, and Red Chroma components.

�HLS (Hue, Luminance, and Saturation): Each pixel in the HLS color space is described in terms of

its Hue, Luminance, and Saturation components.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

�YIQ (Luma, In Phase, and Quadrature): The YIQ color space is used in the analog broadcast of

NTSC video. This format is much rarer than YUV and almost never seen in production. Each pixel

is described in terms of its Luminance, Chroma (in-phase or red-cyan channel) and Quadrature

(magenta-green) components.

�CMY (Cyan, Magenta, and Yellow): Although more common in print, the CMY format is often

found in computer graphics from other software packages. Each pixel is described in terms of its

Cyan, Magenta, and Yellow components. CMY is nonlinear.

Color Channels (RGBA)

Use the Color Channel controls to select which channel’s spline is currently active for editing.

The labels of these controls change to reflect the names of the channels for the current color space.

Normally, they are read as Red, Green, and Blue. If the Color Curves node is operating in YUV color

space, they are read as Y, U, and V instead.

These controls do not restrict the effect of the node to a specific channel. They only select whether

the spline for that channel is editable. These controls are most often used to ensure that adding or

moving points on one channel’s spline do not unintentionally affect a different channel’s spline.

Spline Window

The Spline Window displays a standard curve editor for each RGBA channel. These splines can be

edited individually or as a group, depending on the color channels selected above.

The spline defaults to a linear range, from 0 in/0 out at the bottom left to the 1 in/1 out at the top right.

At the default setting, a color processes to the same value as the output. If a point is added in the

middle at 0.5 in/0.5 out, and the point is moved up, this raises the mid color of the image brighter.

The spline curves allow precise control over color ranges, so specific adjustments can be made

without affecting other color values.

In and Out

Use the In and Out controls to manipulate the precise values of a selected point. To change a value,

select a point and enter the in/out values desired.

Eyedropper (Pick)

Click the Eyedropper icon, also called the Pick button, and select a color from an image in the display

to automatically set control points on the spline for the selected color. The new points are drawn with a

triangular shape and can only be moved vertically (if point is locked, only the Out value can change).

Points are only added to enabled splines. To add points only on a specific channel, disable the other

channels before making the selection.

One use for this technique is white balancing an image. Use the Pick control to select a pixel from the

image that should be pure gray. Adjust the points that appear so that the Out value is 0.5 to change

the pixel colors to gray.

Use the contextual menu’s Locked Pick Points option to unlock points created using the Pick option,

converting them into normal points.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Reference

The Reference section includes controls that handle matching to sample areas of the connected

reference image.

�Match Reference: The Match Reference button adds points on the curve to match an image

connected to the green reference image input. The number of points used to match the image is

based on the Number of Samples slider below.

�Sample Reference: Clicking the Sample Reference button samples the center scanline of the

background image and creates a LUT of its color values. The number of points used to match the

samples scanline is based on the Number of Samples slider below.

�Number of Samples: This slider determines how many points are used to match the curve to the

range in the reference image.

�Show Match Rectangle: Enabling this checkbox displays a rectangle in the viewer showing the

area on the reference image used during the match process. The match rectangle affects only the

result of the Match Reference operation. The Sample reference is always done from the center

scaling of the image.

�Match Center: The X and Y parameters allow you to reposition the match rectangle to sample a

different area when matching.

�Match Width: Width controls the width of the match rectangle.

�Match Height: Heigh controls the height of the match rectangle.

�Pre-Divide/Post-Multiply: Selecting this checkbox causes the image’s pixel values to be divided

by the Alpha values prior to the color correction, and then re-multiplied by the Alpha value after

the correction. This helps to avoid the creation of illegally additive images, particularly around the

edges of a blue/green key or when working with 3D-rendered objects.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Color Gain [Clr]

The Color Gain node

Color Gain Node Introduction

The Color Gain node contains options for adjusting the gain, gamma, saturation, and hue of the image.

Many controls provided by the Color Gain node are also found in the Color Corrector node, but this

simpler node may render more quickly. One feature that distinguishes the Color Gain node from the

Color Corrector is its balance tab controls. These can be used to adjust the tinting of the colors in the

highs, mids, and lows.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Inputs

The Color Gain node includes two inputs: one for the main image and the other for an effect mask.

Input: This orange input is the only required connection. It connects a 2D image that gets adjusted by

the color gain.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

color gain adjustment to only those pixels within the mask. An effect mask is applied to the tool after it

is processed.

Basic Node Setup

The Color Gain node, like many 2D image-processing nodes, receives a 2D image like a Loader node

or the MediaIn1 shown below. The output continues the node tree by connecting to another 2D-image

processing node or a Merge node.

A Color Gain node applied to a MediaIn1 node

Inspector

Color Gain controls


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Gain Tab

The Gain tab provides control of individual RGBA Lift/Gamma/Gain parameters. These controls can

quickly enable you to fix irregular color imbalances in specific channels.

Lock R/G/B

When selected, the Red, Green, and Blue channel controls for each effect are combined into one

slider. Alpha channel effects remain separate.

Gain RGBA

The Gain RGBA controls multiply the values of the image channel in a linear fashion. All pixels are

multiplied by the same factor, but the effect is larger on bright pixels and smaller on dark pixels. Black

pixels do not change because multiplying any number times 0 is always 0.

Lift RGBA

While Gain scales the color values around black, Lift scales the color values around white. The pixel

values are multiplied by the value of this control. A Lift of 0.5 makes a pixel that is R0.0 G0.0 B0.0 into

R0.5 G0.5, B0.5, while leaving white pixels totally unaffected. Lift affects lower values more than it

affects higher values, so the effect is strongest in the midrange and low range of the image.

Gamma RGBA

The Gamma RGBA controls affect the brightness of the midrange in the image. The effect of this node

is nonlinear. White and black pixels in the image are not affected when gamma is modified, whereas

pure grays are affected most by changes to this parameter. Large changes to this control tend to push

midrange pixels into black or white, depending on the value used.

Pre-Divide/Post-Multiply

Selecting this checkbox causes the image pixel values to be divided by the Alpha values prior to

the color correction, and then re-multiplied by the Alpha value after the correction. This helps when

attempting to color correct images with premultiplied Alpha channels.

Saturation Tab

This Setting tab includes controls for the intensity of the colors in the individual RGB channels.

Color Gain Saturation setting tab

RGB Saturation

When adjusting an individual channel, a value of 0.0 strips out all that channel’s color. Values greater

than one intensify the color in the scene, pushing it toward the primary color.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Balance Tab

This tab in the Color Gain node offers controls for adjusting the overall balance of a color channel.

Independent color and brightness controls are offered for the High, Mid, and Dark ranges of

the image.

Colors are grouped into opposing pairs from the two dominant color spaces. Red values can be

pushed toward Cyan, Green values toward Magenta and Blue toward Yellow. Brightness can be raised

or lowered for each of the channels.

Color Gain Balance tab

CMY Brightness Highs/Mids/Darks

By default, the Balance sliders can be adjusted by -1 to +1, but values outside this range can be

entered manually to increase the effect. A value of 0.0 for any slider indicates no change to the image

channel. Positive and negative values indicate that the balance of the image channel has been pushed

toward one color or the other in the pair.

Hue Tab

Use the Hue tab of the Color Gain node to shift the overall hue of the image, without affecting the

brightness, or saturation. Independent controls of the High, Mid, and Dark ranges are offered by

three sliders.

The following is the order of the hues in the RGB color space: Red, Yellow, Green, Cyan, Blue,

Magenta and Red.

Color Gain Hue tab


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

High/Mid/Dark Hue

Values above 0 push the hue of the image toward the right (red turns yellow). Values below 0 push the

hue toward the left (red turns magenta). At -1.0 or 1.0, the hue completes the cycle and returns to its

original value.

The default range of the hue sliders is -1.0 to +1.0. Values outside this range can be entered manually.

Ranges Tab

The Ranges tab contains the controls used to specify which pixels in an image are considered to be

shadows and which are considered to be highlights. The midrange is always calculated as pixels not

included in either the shadows or the highlights.

Color Gain Ranges tab

Spline Display

The ranges are selected by manipulating the spline handles. There are four spline points, each with

one Bézier handle. The two handles at the top represent the start of the shadow and highlight ranges,

whereas the two at the bottom represent the end of the range. The Bézier handles are used to control

the falloff.

The midtones range has no specific controls since its range is understood to be the space between

the shadow and the highlight ranges. The X and Y text controls below the Spline display can be used

to enter precise positions for the selected Bézier point or handle.

Preset Simple/Smooth Ranges

These two buttons can be used to return the spline ranges to either Smooth (default) or Simple

(linear) settings.

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION