---
title: "Scale [SCL]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 502
---

# Scale [SCL]

The Scale node

Scale Node Introduction

The Scale node is almost identical to the Resize node, except that Resize uses exact dimensions,

whereas the Scale node uses relative dimensions to describe the change to the source image’s

resolution. This node actually changes the resolution of the image.

NOTE: Because this node changes the physical resolution of the image, animating the

controls is not advised.

Inputs

The single input on the Scale node is used to connect a 2D image for scaling.

Input: The orange input is used for the primary 2D image you want to scale.

Basic Node Setup

Below, the Scale node is inserted between the MediaIn1 node and the background input of the

Merge. Unlike using a Transform tool, scaling the MediaIn1 changes the resolution of the clip.

The resized MediaIn1 node connected to the orange background input also sets the resolution of the

Merge output.

The Scale node can be used to scale an image and change its resolution.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Inspector

The Scale Controls tab

Controls Tab

The Controls tab includes parameters for changing the resolution of the image. It uses a multiplier of

size to set the new resolution. An Edges menu allows you to determine how the edges of the frame

are handled if the scaling decreases.

Lock X/Y

When selected, only a Size control is shown, and changes to the image’s scale are applied to both

axes equally. If the checkbox is cleared, individual Size controls appear for both X and Y Size.

Size

The Size control is used to set the scale used to adjust the resolution of the source image. A value of

1.0 would have no affect on the image, while 2.0 would scale the image to twice its current resolution.

A value of 0.5 would halve the image’s resolution.

Only Use Filter in HiQ

The Scale node will normally use the fast Nearest Neighbor filter for any non-HiQ renders, where

speed is more important than full accuracy. Disable this checkbox to force Scale to always use the

selected filter for all renders.

Change Pixel Aspect

Enable this checkbox to reveal a Pixel Aspect control that can be used to change the image’s

pixel aspect.

Filter Method

When rescaling a pixel, surrounding pixels are often used to give a more realistic result. There are

various algorithms for combining these pixels, called filters. More complex filters can give better

results but are usually slower to calculate. The best filter for the job often depends on the amount of

scaling and on the contents of the image itself.

�Box: This is a simple interpolation resize of the image.

�Linear: This uses a simplistic filter, which produces relatively clean and fast results.

�Quadratic: This filter produces a nominal result. It offers a good compromise between

speed and quality.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

�Cubic: This produces better results with continuous-tone images. If the images have fine detail in

them, the results may be blurrier than desired.

�Catmull-Rom: This produces good results with continuous-tone images that are resized down.

This produces sharp results with finely detailed images.

�Gaussian: This is very similar in speed and quality to Bi-Cubic.

�Mitchell: This is similar to Catmull-Rom but produces better results with finely detailed images. It is

slower than Catmull-Rom.

�Lanczos: This is very similar to Mitchell and Catmull-Rom but is a little cleaner and also slower.

�Sinc: This is an advanced filter that produces very sharp, detailed results; however,

it may produce visible “ringing” in some situations.

�Bessel: This is similar to the Sinc filter but may be slightly faster.

Window Method (Sinc and Bessel Only)

Some filters, such as Sinc and Bessel, require an infinite number of pixels to calculate exactly. To

speed up this operation, a windowing function is used to approximate the filter and limit the number of

pixels required. This control appears when a filter that requires windowing is selected.

�Hanning: This is a simple tapered window.

�Hamming: Hamming is a slightly tweaked version of Hanning that does not taper all the

way down to zero.

�Blackman: A window with a more sharply tapered falloff.

�Kaiser: A more complex window with results between Hamming and Blackman.

Most of these filters are useful only when making an image larger. When shrinking images, it is

common to use the Bi-Linear filter; however, the Catmull-Rom filter will apply some sharpening

to the results and may be useful for preserving detail when scaling down an image.

Example

Different resize filters. From left to right: Nearest Neighbor, Box, Linear, Quadratic, Cubic,

Catmull-Rom, Gaussian, Mitchell, Lanczos, Sinc, and Bessel.

NOTE: Because this node changes the physical resolution of the image, animating the

controls is not advised.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Transform [XF]

The Transform node

Transform Node Introduction

The Transform node can be used for simple 2D transformations of the image, such as moving, rotating,

and scaling. The image’s aspect can also be modified using the Transform node.

The Transform node concatenates its result with adjacent Transformation nodes. The Transform node

does not change the image’s resolution.

Inputs

The two inputs on the Transform node are used to connect a 2D image and an effect mask, which can

be used to limit the transformed area.

Input: The orange input is used for the primary 2D image that gets transformed.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the transform area to only

those pixels within the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Transform node in the example below is inserted between the MediaIn2 node and the foreground

input of the Merge. Unlike using a Scale or Resize tool, transforming the MediaIn2 does not change the

resolution of the clip. For that reason, it is the tool most often used to scale, move, and rotate a clip.

The Transform node can be used to scale an image without changing its resolution.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Inspector

The Transform Controls tab

Controls Tab

The Controls tab presents multiple ways to transform, flip (vertical), flop (horizontal), scale, and rotate

an image. It also includes reference size controls that can reinterpret the coordinates used for width

and height from relative values of 0-1 into pixel values based on the image’s resolution.

Center X and Y

This sets the position of the image on the screen. The default is 0.5, 0.5, which places the image in the

center of the screen. The value shown is always the actual position multiplied by the reference size.

See below for a description of the reference size.

Pivot X and Y

This positions the axis of rotation and scaling. The default is 0.5, 0.5, which is the center of the image.

Use Size and Aspect

This checkbox determines whether the Transform node provides independent Size controls for the X

and Y scale or if Size and Aspect controls are used instead.

Size

This modifies the scale of the image. Values range from 0 to 5, but any value greater than zero can

be entered into the edit box. If the Use Size and Aspect checkbox is selected, this control will scale

the image equally along both axes. If the Use Size and Aspect option is off, independent control is

provided for X and Y.

Aspect

This control changes the aspect ratio of an image. Setting the value above 1.0 stretches the image

along the X-axis. Values between 0.0 and 1.0 stretch the image along the Y-axis. This control is

available only when the Use Size and Aspect checkbox is enabled.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Angle

This control rotates the image around the axis. Increasing the Angle rotates the image in a

counterclockwise direction. Decreasing the Angle rotates the image in a clockwise direction.

Flip Horizontally and Vertically

Toggle this control on to flip the image along the X- or Y-axis.

Edges

This menu determines how the edges of the image are treated when the edge of the raster

is exposed.

�Canvas: This causes the edges of the image that are revealed to show the current Canvas Color.

This defaults to black with no Alpha and can be set using the Set Canvas Color node.

�Wrap: This wraps the edges of the image around the borders of the image. This is useful for

seamless images to be panned, creating an endless moving background image.

�Duplicate: This causes the edges of the image to be duplicated as best as possible, continuing

the image beyond its original size.

�Mirror: Image pixels are mirrored to fill to the edge of the frame.

Filter Method

When rescaling a pixel, surrounding pixels are often used to give a more realistic result. There are

various algorithms for combining these pixels, called filters. More complex filters can give better

results but are usually slower to calculate. The best filter for the job often depends on the amount of

scaling and on the contents of the image itself.

�Box: This is a simple interpolation resize of the image.

�Linear: This uses a simplistic filter, which produces relatively clean and fast results.

�Quadratic: This filter produces a nominal result. It offers a good compromise

between speed and quality.

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


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION

Most of these filters are useful only when making an image larger. When shrinking images, it is

common to use the Bi-Linear filter; however, the Catmull-Rom filter will apply some sharpening

to the results and may be useful for preserving detail when scaling down an image.

Example

Different resize filters. From left to right: Nearest Neighbor, Box, Linear, Quadratic, Cubic,

Catmull-Rom, Gaussian, Mitchell, Lanczos, Sinc, and Bessel.

Invert Transform

Select this control to invert any position, rotation, or scaling transformation. This option is useful when

connecting the Transform to the position of a tracker for the purpose of reintroducing motion back into

a stabilized image.

Flatten Transform

The Flatten Transform option prevents this node from concatenating its transformation with adjacent

nodes. The node may still concatenate transforms from its input, but it will not concatenate its

transformation with the node at its output.

Reference Size

The controls under the Reference Size menu do not directly affect the image. Instead they allow you to

control how Fusion represents the position of the Transform node’s center.

Normally, coordinates are represented as values between 0 and 1, where 1 is a distance equal to the

full width or height of the image. This allows for resolution independence, because you can change

the size of the image without having to change the value of the center.

One disadvantage to this approach is that it complicates making pixel-accurate adjustments to an

image. To demonstrate, imagine an image that is 100 x 100 pixels in size. To move the center of

the image to the right by 5 pixels, we would change the X value of the transform center from 0.5,

0.5 to 0.55, 0.5. We know the change must be 0.05 because 5/100 = 0.05.

The Reference Size controls allow you to specify the dimensions of the image. This changes the way

the control values are displayed, so that the Center shows the actual pixel positions in the X and

Y number fields of the Center control. Extending our example, if you set the Width and Height to

100 each, the Center would now be shown as 50, 50, and we would move it 5 pixels toward the right

by entering 55, 50.

Internally, the Transform node still stores this value as a number between 0 to 1, and if you were to

query the Center controls value via scripting, or publish the Center control for use by other nodes,

then you would retrieve the original normalized value. The change is visible only in the value shown for

Transform Center in the node control.

Reference Width and Height Sliders

Set these to the width and height of the image to change the way that Fusion displays the values of

the Transform node’s Center control.

Auto Resolution

Enable this checkbox to use the current frame format settings in Fusion Studio or the timeline

resolution in DaVinci Resolve to set the Reference Width and Reference Height values.


Fusion Page Effects | Chapter 120 Transform Nodes

FUSION