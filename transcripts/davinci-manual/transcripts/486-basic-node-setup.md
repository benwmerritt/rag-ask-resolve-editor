---
title: "Basic Node Setup"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 486
---

# Basic Node Setup

Disparity To Z takes a 3D camera and stereo images containing a disparity channel as inputs. The

output is an image with a newly computed Z channel.

A Disparity to Z node creates an image with a Z channel.

Inspector

The Disparity To Z Controls tab

Controls Tab

In addition to outputting Z values in the Z channel, this tab promotes the color channels to float32 and

outputs the Z values into the color channels as {z, z, z, 1}. This option is useful to get a quick look at the

Z channel.

NOTE: Z values are negative, becoming more negative the further you are from the camera.

The viewers only show 0.0 to 1.0 color, so to visualize other data it has to be converted via

a normalization method to fit in a display 0-1 range. To do this, right-click in the viewer and

choose Options > Show Full Color Range.

Output Z to RGB

Rather than keeping the Z values within the associated aux channel only, they will be copied into the

RGB channels for further modification with any of Fusion’s nodes.

Refine Z

The Enable checkbox refines the depth map based upon the RGB channels. The refinement causes

edges in the flow to align more closely with edges in the color channels. The downside is that

unwanted details in the color channels start to show up in the flow. You may want to experiment with

using this option to soften out harsh edges for Z-channel post effects like depth of field or fogging.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

HiQ Only

Activating this checkbox causes the Refine Z option to process only when rendering is set to High

Quality. You can ensure High Quality is enabled by right-clicking to the left or right of the transport

controls in the main toolbar.

Strength

Increasing this slider does two things. It smooths out the depth in constant color regions and moves

edges in the Z channel to correlate with edges in the RGB channels.

Increasing the refinement has the undesirable effect of causing texture in the color channel to show up

in the Z channel. You will want to find a balance between the two.

Radius

This is the radius of the smoothing algorithm.

Stack Mode

This menu determines how the input images are stacked.

When set to Separate, the Right Input and Output will appear, and separate left and right images must

be connected.

Swap Eyes

Enabling this checkbox causes left and right images to be swapped.

The Disparity To Z Camera tab

Camera Tab

If you need correct real-world Z values because you are trying to match some effect to an existing

scene, you should use the External Camera options to get precise Z values back. If any Z-buffer will

suffice and you are not that particular about the exact details of how it is offset and scaled, or if there is

no camera available, the Artistic option might be helpful.

�External Mode: An input is available on the node to connect an existing stereo Camera 3D. This

can either be a single stereo Camera 3D (i.e., its eye separation is set to non-zero), or a pair of

(tracked) Camera 3Ds connected via the Camera 3D > Stereo > Right Camera input.

�Artistic Mode: If you do not have a camera, you can adjust these controls to produce an “artistic”

Z channel whose values will not be physically correct but will still be useful. To reconstruct the

Disparity > Z Curve, pick (D, Z) values for a point in the foreground and a point in the background.

TIP: If artistic mode is a little too “artistic” for you and you want more physically‑based

parameters to adjust (e.g., convergence and eye separation), create a dummy

Camera 3D, connect it into the Disparity To Z > Camera input, and then fiddle with the

Camera 3D’s controls.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

Foreground Disparity (Pick from Left Eye)

When the camera Mode is set to Artistic, a Foreground Disparity slider is available. This is the

disparity for the closest foreground object. It will get mapped to the depth value specified by the

Foreground Depth control. Any objects with disparity outside of the range [ForegroundDisparity,

BackgroundDisparity] will have their disparity values clipped to this range leading to flat areas in the

Z channel, so make sure that you pick values that enclose the actual disparity range.

Background Disparity (Pick from Left Eye)

When the camera Mode is set to Artistic, a Background Disparity is available. This is the disparity for

the furthest background object. It will get mapped to the depth value specified by the Background

Depth control. One way to think of this input is as the upper limit to disparity values for objects at

-infinity. This value should be for the left eye. The corresponding value in the right eye will be the same

in magnitude but negative.

Foreground Depth

This is the depth to which Foreground Disparity will be mapped. Think of this as the depth of the

nearest object. Note that values here are positive depth.

Background Depth

This is the depth to which Background Disparity will be mapped. Think of this as the depth of the most

distant object.

Falloff

Falloff controls the shape of the depth curve between the requested foreground and background

depths. When set to Hyperbolic, the disparity-depth curve behaves roughly like depth = constant/

disparity. When set to Linear, the curve behaves like depth = constant * disparity. Hyperbolic tends

to emphasize Z features in the foreground, while linear gives foreground/background features in the

Z channel equal weighting.

Unless there’s a specific reason, choose Hyperbolic, as it is more physically accurate, while Linear

does not correspond to nature and is purely for artistic effect.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Stereo nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

Global Align [GA]

The GlobalAlign node

NOTE: The Global Align node is available only in Fusion Studio and DaVinci Resolve Studio.

Global Align Node Introduction

As opposed to Stereo Align, this node does not utilize optical flow at all. It’s meant as a fast and

convenient way to do simple stereo alignment for both X and Y as well as rotation.

Global Align comes in handy at the beginning of the node chain to visually correct major differences

between the left and right eye before calculating Disparity.

Manual correction of large discrepancies between left and right, as well as applying an initial color

matching, helps Disparity generate more accurate results.

Inputs

The two inputs on the Global Align node are used to connect the left and right images.

Left Input: The orange input is used to connect either the left eye image or the stack image.

Right Input: The green input is used to connect the right eye image. This input is available only when

the Stack Mode menu is set to Separate.

Outputs

Unlike most nodes in Fusion, Global Align has two outputs for the left and right eye.

Left Output: This outputs the newly aligned left eye image.

Right Output: This outputs the newly aligned right eye image.

Basic Node Setup

Global Align is typically placed at the beginning of the node tree. Below it is inserted between the left

and right eye images and the Disparity node to visually correct major differences.

A Global Align node used to manually correct left and right eye discrepancies


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

Inspector

The Global Align Controls tab

Controls Tab

The Controls tab includes translation and rotation controls to align the stereo images manually.

Translation X and Y

�Balance: Determines how the global offset is applied to the stereo footage.

�None: No translation is applied.

�Left Only: The left eye is shifted, while the right eye remains unaltered.

�Right Only: The right eye is shifted, while the left eye remains unaltered.

�Split Both: Left and right eyes are shifted in opposite directions.

Snap to Nearest Pixel

While adjusting the X or Y shift dial, this option ensures that the image is shifted in full pixel amounts only to

maintain optimum quality. This avoids sub-pixel rendering of the image, which could result in subtle blurring.

Rotation

�Balance: Determines how the global rotation is applied to the stereo footage.

�None: No rotation is applied.

�Left Only: The left eye is rotated, while the right eye remains unaltered.

�Right Only: The right eye is rotated, while the left eye remains unaltered.

�Split Both: Left and right eyes are rotated in opposite directions.

Angle

This dial adjusts the angle of the rotation. Keep in mind that the result depends on the Balance

settings. If only rotating one eye by, for example, 10 degrees, a full 10-degree rotation will be applied

to that eye.

When applying rotation in Split mode, one eye will receive a -5 degree and the other eye a

+5 degree rotation.


Fusion Page Effects | Chapter 118 Stereo Nodes

FUSION

Translation Filter Method

This menu chooses the filter method that delivers the best results depending on the content

of your footage.

Visualization

This control allows for different color encodings of the left and right eye to conveniently examine the

results of the above controls without needing to add an extra Anaglyph or Combiner node.

Set this to None for final output.

Stack Mode

Determines how the input images are stacked.

When set to Separate, the right input and output will appear, and separate left and right images

must be connected.

Swap Eyes

With Stacked Mode, image stereo pairs’ left and right images can be swapped.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Stereo nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.