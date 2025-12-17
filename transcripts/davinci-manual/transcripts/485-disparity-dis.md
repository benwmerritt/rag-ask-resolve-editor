---
title: "Disparity [Dis]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 485
---

# Disparity [Dis]

The Disparity node

NOTE: The Disparity node is available only in Fusion Studio and DaVinci Resolve Studio.

Disparity Node Introduction

Disparity generates the left/right shift between the frames in a stereo pair. It also generates the vertical

disparity between the left/right images, which is usually a lot smaller than the horizontal disparity and

ideally should be 0 to minimize viewing discomfort. When viewing the output of the Disparity node in

the views, the human eye can distinguish quality/detail in the Disparity map better by looking at either

the grayscale X disparity or Y disparity rather than looking at the combined XY disparity as a Red/

Green color image.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

The generated disparity is stored in the output image’s Disparity aux channel, where the left image

contains the left > right disparity, and the right image contains the right > left disparity. Because

disparity works based on matching regions in the left eye to regions in the right eye by comparing

colors and gradients of colors, colors in the two eyes must be as similar as possible. Thus, it is a good

idea to color correct ahead of time. It is also a good idea to crop away any black borders around the

frames, as this confuses the disparity tracking (and also causes problems if you are using the Color

Corrector’s histogram match ability to do the color matching).

In Stack mode, left and right outputs deliver the same image. If the left and right images have a global

vertical offset larger than a few pixels, it can help the disparity tracking algorithm if you vertically align

features in the left/right eyes ahead of time using a Transform node. Small details tend to get lost in the

tracking process when you have a large vertical offset between left/right eyes.

Consider using a SmoothMotion node to smooth your disparity channel. This can help reduce time-

dependent flickering when warping an eye. Also, think about whether you want to remove lens

distortion before computing disparity. If you do not, your Disparity map becomes a combined Disparity

and Lens Distortion map. This can have advantages and disadvantages.

One disadvantage is that if you then do a vertical alignment, you are also removing lens distortion

effects. When trying to reduce the computation time, start first with adjusting the Proxy and Number of

Iterations sliders.

The Disparity node does not support RoI or DoD.

Inputs

The two inputs on the Disparity node are used to connect the left and right images.

Left Input: The orange input is used to connect either the left eye image or the stacked image.

Right Input: The green input is used to connect the right eye image. This input is available only when

the Stack Mode menu is set to Separate.

Outputs

Unlike most nodes in Fusion, Disparity has two outputs for the left and right eye.

Left Output: This holds the left eye image with a new disparity channel, or a Stacked Mode image with

a new disparity channel.

Right Output: This holds the right eye image with a new disparity channel. This output is visible only if

Stack Mode is set to Separate.

Basic Node Setup

Below, a left eye image and right eye image are connected to the Disparity node. The Disparity node

then outputs each eye to Saver nodes. It can be more efficient to render out the stereo images as EXR

files than to generate the disparity on-the-fly.

Left and right eye images are connected into a Disparity node

to generate and render out a stereo image


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

Inspector

The Disparity Controls tab

Proxy (for Tracking)

The input images are resized down by the proxy scale, tracked to produce the disparity, and then

the resulting disparities are scaled back up. This option is purely to speed up the calculation of

the disparity, which can be slow. The computational time is roughly proportional to the number of

pixels in the image. This means a proxy scale of 2 gives a 4x speedup, and a proxy scale of 3 gives

a 9x speedup. In general, 1:1 proxy will give the most detailed flow, but keep in mind that this is

highly dependent on the amount of noise and film grain. If noise is present in large quantities, it can

completely obliterate any gains moving from 2:1 to 1:1 proxy. In some situations, it can even make

things worse. You can think of the Proxy setting as acting as a simplistic low-pass filter for removing

noise/grain.

Advanced

The Advanced settings section has parameter controls to tune the Disparity map calculations.

The default settings have been chosen to be the best default values from experimentation with

many different shots and should serve as a good standard. In most cases, tweaking of the Advanced

settings is not needed.

Smoothness

This controls the smoothness of the disparity. Higher values help deal with noise, while lower values

bring out more detail.

Edges

This slider is another control for smoothness but applies it based on the color channel. It tends to have

the effect of determining how edges in the disparity follow edges in the color images. When it is set

to a lower value, the disparity becomes smoother and tends to overshoot edges. When it is set to a

higher value, edges in the disparity align more tightly with the edges in the color images, and details

from the color channels start to slip into the disparity, which is not usually desirable.

As a rough guideline, if you are using the disparity to produce a Z channel for post effects like depth

of field, experiment with higher values, but if you are using the disparity to do interpolation, you might

want to keep the values lower.

In general, if the Edges slider is set is too high, there can be problems with streaked out edges when

the disparity is used for interpolation.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

Match Weight

This controls how matching is done between neighboring pixels in the left image and neighboring

pixels in the right image. When a lower value is used, large structural color features are matched.

When higher values are used, small sharp variations in the color are matched. Typically, a good value

for this slider is in the [0.7, 0.9] range. Setting this option higher tends to improve the matching results

in the presence of differences due to smoothly varying shadows or local lighting variations between

the left and right images. You should still color match the initial images so they are as similar as

possible; this option tends to help with local variations (e.g., lighting differences due to light passing

through a mirror rig).

Mismatch Penalty

This controls how the penalty for mismatched regions grows as they become more dissimilar. The

slider provides a choice between a balance of Quadratic (lower values) and Linear (higher values)

penalties. Lower value Quadratic settings strongly penalize large dissimilarities, while higher value

Linear settings are more robust to dissimilar matches. Moving this slider toward lower tends to give a

disparity with more small random variations in it, while higher values produce smoother, more visually

pleasing results.

Warp Count

Turning down the Warp Count makes the disparity computations faster. In particular, the computational

time depends linearly upon this option. To understand what this option does, you need to understand

that the Disparity algorithm progressively warps the left image until it matches with the right image.

After some point, convergence is reached, and additional warps are just a waste of computational

time. The default value in Fusion is set high enough that convergence should always be reached.

You can tweak this value to speed up the computations, but it is good to watch how the disparity is

degrading in quality at the same time.

Iteration Count

Turning down the Iteration Count makes the disparity computations faster. In particular, the

computational time depends linearly upon this option. Just like adjusting Warp Count, at some point

adjusting this option higher will yield diminishing returns and will not produce significantly better

results. By default, this value is set to something that should converge for all possible shots and can be

tweaked lower fairly often without reducing the disparity’s quality.

Filtering

This menu determines the filtering operations used during flow generation. Catmull-Rom filtering will

produce better results, but at the same time, it increases the computation time steeply.

Stack Mode

This menu determines how the input images are stacked.

When set to Separate, the Right Input and Output will appear, and separate left and right images must

be connected.

Swap Eyes

Enabling this checkbox causes the left and right images to swap.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Stereo nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

Disparity To Z [D2Z]

The DisparityToZ node

NOTE: The Disparity to Z node is available only in Fusion Studio and DaVinci Resolve Studio.

Disparity to Z Node Introduction

Disparity To Z takes a 3D camera and an image containing a disparity channel as inputs, and outputs

the same image but with a newly computed Z channel.

Optionally, this node can output Z into the RGB channels. Ideally, either a stereo Camera 3D or a

tracked stereo camera is connected into Disparity To Z. However, if no camera is connected, the node

provides artistic controls for determining a Z channel. The depth created by this node can be used for

post effects like fogging or depth of field (DoF).

The Z values produced become more incorrect the larger (negative) they get. The reason is that

disparity approaches a constant value as Z approaches -infinity. So Z = -1000 and Z = -10000 and Z

= -100000 may map to D=142. 4563 and D=142. 4712 and D=142. 4713. As you can see, there is only

0.0001 in D to distinguish between 10,000 and 100,000 in Z. The maps produced by disparity are not

accurate enough to make distinctions like this.

Inputs

The three inputs on the Disparity To Z node are used to connect the left and right images and a

camera node.

Left Input: The orange input is used to connect either the left eye image or the stack image.

Right Input: The green input is used to connect the right eye image. This input is available only when

the Stack Mode menu is set to Separate.

Stereo Camera: The magenta input is used to connect a stereo camera node.

Outputs

Unlike most nodes in Fusion, Disparity To Z has two outputs for the left and right eye.

Left Output: This holds the left eye image with a new Z channel, or a Stacked Mode image with a new

disparity channel.

Right Output: This holds the right eye image with a new Z channel. This output is visible only if Stack

Mode is set to Separate.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION