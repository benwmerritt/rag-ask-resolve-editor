---
title: "DVE [DVE]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 500
---

# DVE [DVE]

The DVE node

DVE Node Introduction

The DVE (Digital Video Effects) node is a 3D-image transformation similar to nodes found in old, tape-

based online editing suites. The node encompasses image rotations, perspective changes, and Z

moves. The axis can be defined for all transformations.

Inputs

The three inputs on the DVE node are used to connect a 2D image, DVE mask, and an effect mask,

which can be used to limit the DVE area.

Input: The orange input is used for the primary 2D image that is transformed by the DVE.

DVE Mask: The white DVE mask input is used to mask the image prior to the DVE transform being

applied. This has the effect of modifying both the image and the mask.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input causes the DVE to modify only

the image within the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

In the example below, the DVE node is inserted between the MediaIn2 node and the foreground input

of the Merge. The MediaIn1 node is manipulated in the DVE node and composited over the top of the

MediaIn1 node.

The DVE node modifying the foreground input of a Merge node


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Inspector

The DVE Controls tab

Controls Tab

The Controls tab includes all the transform parameters for the DVE.

Pivot X, Y, and Z

Positions the axis of rotation and scaling. The default is 0.5, 0.5 for X and Y, which is in the center of

the image, and 0 for Z, which is at the center of Z space.

Rotation Order

Use these buttons to determine in what order rotations are applied to the image.

XYZ Rotation

These controls are used to rotate the image around the pivot along the X-, Y- and Z-axis.

Center X and Y

This positions the center of the DVE image onscreen. The default is 0.5, 0.5, which positions the DVE

in the center of the image.

Z Move

This zooms the image in and out along the Z-axis. Visually, when this control is animated, the effect is

similar to watching an object approach from a distance.

Perspective

This adds additional perspective to an image rotated along the X- or Y-axis, similar to changing the

Field of View and zoom of a camera.

Masking Tab

The DVE node allows pre-masking of its input image. This offers the ability to create transformations

from the masked area of the image while leaving the remainder of the image unaffected.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

The DVE Masking tab

Unlike regular effect masks, the masking process occurs before the transformation. All the usual mask

types can be applied to the DVE mask.

Black Background

Toggle this on to erase the area outside the mask from the transformed image.

Fill Black

Toggle this on to erase the area within the mask (before transformation) from the DVE’s input,

effectively cutting the masked area out of the image. Enabling both Black Background and Fill Black

will show only the masked, transformed area.

Alpha Mode

This determines how the DVE will handle the alpha channel of the image when merging the

transformed image areas over the untransformed image.

�Ignore Alpha: This causes the input image’s alpha channel to be ignored, so all masked

areas will be opaque.

�Subtractive/Additive: These cause the internal merge of the pre-masked DVE image over the

input image to be either Subtractive or Additive.

An Additive setting is necessary when the foreground DVE image is premultiplied, meaning that

the pixels in the color channels have been multiplied by the pixels in the alpha channel. The result

is that transparent pixels are always black, since any number multiplied by 0 always equals 0.

This obscures the background (by multiplying with the inverse of the foreground alpha), and then

simply adds the pixels from the foreground.

A Subtractive setting is necessary if the foreground DVE image is not premultiplied. The

compositing method is similar to an Additive merge, but the foreground DVE image is first

multiplied by its own alpha, to eliminate any background pixels outside the alpha area.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Transform nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Letterbox [LBX]

The Letterbox node

Letterbox Node Introduction

Use the Letterbox node to adapt existing images to the frame size and aspect ratios of any other

format. The most common use of this node is to convert film resolution images to HD-sized frames

for viewing on an external television monitor. Horizontal or vertical black edges are automatically

added where necessary to compensate for aspect ratio differences. This node actually changes the

resolution of the image.

NOTE: Because this node changes the physical resolution of the image, animating the

controls is not recommended.

Inputs

The single input on the Letterbox node is used to connect a 2D image for letterbox/cropping.

Input: The orange input is used for the primary 2D image you want to letterbox/crop.

Basic Node Setup

The Letterbox node is used in the example below to change the resolution of the Merge node’s

output. Depending on how the resolution is modified, side pillars, or a horizontal letterbox mask, is

applied to “fill in” the frame area, which the Merge node output does not cover.

The Letterbox node converting the Merge output resolution and adding letterbox masking where needed.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Inspector

The Letterbox Controls tab

Controls Tab

The Controls tab includes parameters for adjusting the resolution and pixel aspect of the image. It also

has the option of letterboxing or pan-and-scan formatting.

Width and Height

The values of these controls determine the size of the output image as measured in pixels.

TIP: You can use the formatting contextual menu to quickly select a resolution from a

list. Place the pointer over the Width or Height controls, and then right-click to display the

contextual menu. The bottom of the menu displays a Select Frame Format submenu with

available frame formats. Select any one of the choices from the menu to set the Height,

Width, and Aspect controls automatically.

Auto Resolution

Activating this checkbox automatically sets the Width and Height sliders to the Frame Format settings

found in the Preferences window for Fusion Studio or to the resolution of the DaVinci Resolve Timeline.

Pixel Aspect X and Y

These controls determine the pixel aspect ratio of the output image.

Center X and Y

This Center control repositions the image window when used in conjunction with Pan-and-Scan mode.

It has no effect on the image when the node is set to Letterbox mode.

Mode

This control is used to determine the Letterbox node’s mode of operation.

�Letterbox/Envelope: This corrects the aspect of the input image and resizes it to match the

specified width.

�Pan-and-Scan: This corrects the aspect of the input image and resizes it to match the specified

height. If the resized input image is wider than the specified width, the Center control can be used

to animate the visible portion of the resized input.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Filter Method

When rescaling a pixel, surrounding pixels are often used to give a more realistic result. There are

various algorithms for combining these pixels, called filters. More complex filters can give better

results but are usually slower to calculate. The best filter for the job often depends on the amount of

scaling and on the contents of the image itself.

�Box: This is a simple interpolation resize of the image.

�Linear: This uses a simplistic filter, which produces relatively clean and fast results.

�Quadratic: This filter produces a nominal result. It offers a good compromise between

speed and quality.

�Cubic: This produces better results with continuous-tone images. If the images have fine detail in

them, the results may be blurrier than desired.

�Catmull-Rom: This produces good results with continuous-tone images that are resized down.

This produces sharp results with finely detailed images.

�Gaussian: This is very similar in speed and quality to Bi-Cubic.

�Mitchell: This is similar to Catmull-Rom but produces better results with finely detailed images. It is

slower than Catmull-Rom.

�Lanczos: This is very similar to Mitchell and Catmull-Rom but is a little cleaner and also slower.

�Sinc: This is an advanced filter that produces very sharp, detailed results; however, it may produce

visible “ringing” in some situations.

�Bessel: This is similar to the Sinc filter but may be slightly faster.

Window Method (Sinc and Bessel Only)

Some filters, such as Sinc and Bessel, require an infinite number of pixels to calculate exactly.

To speed up this operation, a windowing function is used to approximate the filter and limit the number

of pixels required. This control appears when a filter that requires windowing is selected.

�Hanning: This is a simple tapered window.

�Hamming: Hamming is a slightly tweaked version of Hanning that does not taper all the way

down to zero.

�Blackman: A window with a more sharply tapered falloff.

�Kaiser: A more complex window with results between Hamming and Blackman.

Most of these filters are useful only when making an image larger. When shrinking images, it is

common to use the Bi-Linear filter; however, the Catmull-Rom filter will apply some sharpening

to the results and may be useful for preserving detail when scaling down an image.

Example

Different resize filters. From left to right: Nearest Neighbor, Box, Linear, Quadratic, Cubic,

Catmull-Rom, Gaussian, Mitchell, Lanczos, Sinc, and Bessel.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Transform nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.