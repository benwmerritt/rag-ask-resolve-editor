---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 499
---

# Inspector

The Camera Shake Controls tab

Controls Tab

The Controls tab includes parameters for adjusting the offsets, strength, speed, and frequency of the

simulated camera shake movement.

Deviation X and Y

These controls determine the amount of shake applied to the image along the horizontal (X) and

vertical (Y) axes. Values between 0.0 and 1.0 are permitted. A value of 1.0 generates shake positions

anywhere within the boundaries of the image.

Rotation Deviation

This determines the amount of shake that is applied to the rotational axis. Values between 0.0 and 1.0

are permitted.

Randomness

Higher values in this control cause the movement of the shake to be more irregular or random. Smaller

values cause the movement to be more predictable.

Overall Strength

This adjusts the general amplitude of all the parameters and blends that affect in and out. A value of

1.0 applies the effect as described by the remainder of the controls.

Speed

Speed controls the frequency, or rate, of the shake.

Frequency Method

This selects the overall shape of the shake. Available frequencies are Sine, Rectified Sine, and Square

Wave. A Square Wave generates a much more mechanical-looking motion than a Sine.

Filter Method

When rescaling a pixel, surrounding pixels are often used to give a more realistic result. There are

various algorithms for combining these pixels, called filters. More complex filters can give better

results but are usually slower to calculate.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

The best filter for the job often depends on the amount of scaling and on the contents of the

image itself.

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

Some filters, such as Sinc and Bessel, require an infinite number of pixels to calculate exactly. To

speed up this operation, a windowing function is used to approximate the filter and limit the number of

pixels required. This control appears when a filter that requires windowing is selected.

�Hanning: This is a simple tapered window.

�Hamming: Hamming is a slightly tweaked version of Hanning that does not taper all the way

down to zero.

�Blackman: A window with a more sharply tapered falloff.

�Kaiser: A more complex window with results between Hamming and Blackman.

Most of these filters are useful only when making an image larger. When shrinking images, it is

common to use the Bi-Linear filter, however, the Catmull-Rom filter will apply some sharpening

to the results and may be useful for preserving detail when scaling down an image.

Example

Resize filters. From left to right: Nearest Neighbor, Box, Linear, Quadratic, Cubic, Catmull-Rom,

Gaussian, Mitchell, Lanczos, Sinc, and Bessel.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Edges

This menu determines how the Edges of the image are treated.

�Canvas: This causes the edges that are revealed by the shake to be the canvas color—usually

transparent or black.

�Wrap: This causes the edges to wrap around (the top is wrapped to the bottom, the left is

wrapped to the right, and so on).

�Duplicate: This causes the Edges to be duplicated, causing a slight smearing effect at the edges.

�Mirror: Image pixels are mirrored to fill to the edge of the frame.

Invert Transform

Select this control to Invert any position, rotation, or scaling transformation. This option might be useful

for exactly removing the motion produced in an upstream Camera Shake.

Flatten Transform

The Flatten Transform option prevents this node from concatenating its transformation with adjacent

nodes. The node may still concatenate transforms from its input, but it will not concatenate its

transformation with the node at its output.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Transform nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.

Crop [CRP]

The Crop node

Crop Node Introduction

The Crop node can be used to cut out a portion of an image or to offset the image into a larger image

area. However, unlike using a mask, this node actually changes the resolution of the image.

TIP: You can crop an image in the viewer by activating the Allow Box Selection in the upper-

left corner of the viewer while the Crop node is selected and viewed. Then, drag a crop

rectangle around the area of interest to perform the operation.

NOTE: Because this node changes the physical resolution of the image, animating the

parameters is not advised.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Inputs

The single input on the Crop node is used to connect a 2D image for cropping.

Input: The orange input is used for the primary 2D image you want to crop.

Basic Node Setup

Below, the Crop node is inserted between the MediaIn1 node and the background input of the

Merge. Unlike using a mask tool, cropping the MediaIn1 changes the resolution of the clip. The

cropped MediaIn1 node connected to the orange background input also sets the resolution of the

Merge output.

The Crop node can be used to cut out a portion of an image.

Inspector

The Crop Controls tab

Controls Tab

The Controls tab provides XY Offset and XY Size methods for cropping the image.

Offset X and Y

These controls position the image off the screen by pushing it left/right or up/down. The cropped

image disappears off the edges of the output image. The values of these controls are measured

in pixels.

Size X and Y

Use these controls to set the vertical and horizontal resolution of the image output by the Crop node.

The values of these controls are measured in pixels.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Keep Aspect

When toggled on, the Crop node maintains the aspect of the input image.

Keep Centered

When toggled on, the Crop node automatically adjusts the X and Y Offset controls to keep the image

centered. The XY Offset sliders are automatically adjusted, and control over the cropping is done with

the Size sliders or the Allow Box Selection button in the viewer.

Reset Size

This resets the image dimensions to the size of the input image.

Reset Offset

This resets the X and Y Offsets to their defaults.

Change Pixel Aspect

Enable this checkbox to reveal a Pixel Aspect control that can be used to change the image’s pixel aspect.

Clipping Mode

This option sets the mode used to handle the edges of the image when performing domain of

definition (DoD) rendering. This is profoundly important for nodes like Blur, which may require samples

from portions of the image outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition to

use the full frame of the image, effectively ignoring the current domain of definition. If the upstream

DoD is smaller than the frame, the remaining area in the frame will be treated as black/transparent.

�Domain: Setting this option to Domain will respect the upstream DoD when applying the node’s

effect. This can have adverse clipping effects in situations where the node employs a large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that would normally be outside the upstream

DoD is treated as black/transparent.

Auto Crop Tab

Auto Crop tab analyzes the selected channel and crops the image based on that channel’s

boundaries. The adjustments from auto crop are seen in the Crop tab parameters.

The Auto Crop tab

RGBA Color Channels

Select which channels are examined for an Auto Crop. This is useful for auto cropping images with

non-solid backgrounds in a specific color channel, like a blue color gradient. Toggling the channel off

causes Auto Crop to ignore it when evaluating the image.

Auto Crop

This evaluates the image and attempts to determine the background color. It then crops each side of

the image to the first pixel that is not that color.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Transform nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.