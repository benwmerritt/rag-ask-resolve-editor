---
title: "Defocus [Dfo]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 376
---

# Defocus [Dfo]

The Defocus node

Defocus Node Introduction

The Defocus node simulates the effects of an out-of-focus camera lens, including blooming and image

flaring. It provides a fast Gaussian mode, as well as a more realistic but slower Lens mode.

Inputs

The two inputs on the Defocus node are for connecting a 2D image and an effect mask that can be

used to limit the simulated defocused area.

Input: The orange input is used for the primary 2D image for defocusing.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the defocus to only those

pixels within the mask. An effect mask is applied to the tool after it is processed.

Basic Node Setup

The Defocus node receives a 2D image like the MediaIn1 shown below. The output continues the

node tree by connecting to another 2D image-processing node or a Merge node.

A Defocus node applied to a MediaIn1 node

Inspector

Defocus controls


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Controls Tab

The Controls tab contains all the primary controls necessary for customizing the defocus operation.

Filter

Use this menu to select the exact method applied to create the defocus. Gaussian applies a simplistic

effect, while Lens mode creates a more realistic defocus. Lens mode takes significantly longer

than Gaussian.

Lock X/Y

When Lock X/Y is selected, this performs the same amount of defocusing to both the X- and Y-axis of

the image. Deselect to obtain individual control.

Defocus Size

The Defocus Size control sets the size of the defocus effect. Higher values blur the image by greater

amounts and produce larger blooms.

Bloom Level

The Bloom Level control determines the intensity and size of the blooming applied to pixels that are

above the bloom threshold.

Bloom Threshold

Pixels with values above the set Bloom Threshold are defocused and have a glow applied (blooming).

Pixels below that value are only defocused.

The following four lens options are available only when the Filter is set to Lens.

�Lens Type: The basic shape used to create the “bad bokeh” effect. This can be refined further

with the Angle, Sides, and Shape sliders.

�Lens Angle: Defines the rotation of the shape. Best visible with NGon lens types. Because of the

round nature of a circle, this slider has no visible effect when the Lens Type is set to Circle.

�Lens Sides: Defines how many sides the NGon shapes have. Best visible with NGon lens

types. Because of the round nature of a circle, this slider has no visible effect when the Lens

Type is set to Circle.

�Lens Shape: Defines how pointed the NGons are. Higher values create a more pointed, starry

look. Lower values create smoother NGons. Best visible with NGon lens types and Lens Sides

between 5 and 10. Because of the round nature of a circle, this slider has no visible effect when

the Lens Type is set to Circle.

Clipping Mode

This option determines how edges are handled when performing domain-of-definition rendering. This

is profoundly important for nodes like Blur, which may require samples from portions of the image

outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition. If the

upstream DoD is smaller than the frame, the remaining area in the frame is treated as black/

transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that would normally be outside the upstream

DoD is treated as black/transparent.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Blur nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Directional Blur [DrBl]

The Directional Blur node

Directional Blur Node Introduction

This node is used to create Directional and Radial blurs. It is useful for creating simulated motion blur

and light ray-type effects. Directional Blur affects all channels (RGBA).

Inputs

The two inputs on the Directional Blur node are used to connect a 2D image and an effect mask which

can be used to limit the blurred area.

Input: The orange input is used for the primary 2D image that has the directional blur applied.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the directional blur to only

those pixels within the mask. An effect mask is applied to the tool after it is processed.

Basic Node Setup

The Directional Blur node receives a 2D image like the MediaIn1 shown below. The output continues

the node tree by connecting to another 2D image-processing node or a Merge node.

A Directional Blur node applied to a MediaIn1 node


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Inspector

Directional Blur controls

Controls Tab

The Controls tab contains all the primary controls necessary for customizing the

directional blur operation.

Type

This menu is used to select the type of directional blur to be applied to the image.

�Linear: Linear distorts the image in a straight line, resembling the scenery that appears in the

window of a speeding train.

�Radial: Radial creates a distortion that originates at some arbitrary center, radiating outward the

way that a view would appear if one were at the head of the train looking forward.

�Centered: The Centered button produces a similar result to linear, but the blur effect is equally

distributed on both sides of the original.

�Zoom: Zoom creates a distortion in the scale of the image smear to simulate the zoom streaking of

a camera filming with a slow shutter speed.

Center X and Y

This coordinate control and related viewer crosshair affects the Radial and Zoom Motion Blur types

only. It is used to position where the blurring effect starts.

Length

Length adjusts the strength and heading of the effect. Values lower than zero cause blurs to

head opposite the angle control. Values greater than the slider maximum may be typed into the

slider’s edit box.

Angle

In both Linear and Center modes, this control modifies the direction of the directional blur. In the

Radial and Zoom modes, the effect is similar to the camera spinning while looking at the same spot. If

the setting of the length slider is other than zero, the effect creates a whirlpool effect.

Glow

This adds a Glow to the directional blur, which can be used to duplicate the effect of increased camera

exposure to light caused by longer shutter speeds.

Clipping Mode

This option determines how edges are handled when performing domain-of-definition rendering.

This is profoundly important for nodes like Blur, which may require samples from portions of the image

outside the current domain.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

�Frame: The default option is Frame, which automatically sets the node’s domain of definition to use

the full frame of the image, effectively ignoring the current domain of definition. If the upstream

DoD is smaller than the frame, the remaining area in the frame is treated as black/transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that would normally be outside the upstream

DoD is treated as black/transparent.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Blur nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Glow [Glo]

The Glow nozzde

Glow Node Introduction

A Glow is created by blurring an image, and then brightening the blurred result and mixing it back with

the original. The Glow node provides a variety of variations on this theme. For example, a Bartlett glow

is a high-quality glow with a smoother drop-off; however, it is more processor-intensive at larger sizes.

Inputs

The Glow node has three inputs: an orange one for the primary 2D image input, a blue one for an

effect mask, and a third white input for a Glow mask.

Input: The orange input is used for the primary 2D image that has the glow applied.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input restricts the source of the glow to

only those pixels within the mask. An effect mask is applied to the tool after it is processed.

Glow Mask: The Glow node supports pre-masking using the white glow mask input. A Glow pre-mask

filters the image before applying the glow. The glow is then merged back over the original image. This

is different from a regular effect mask that clips the rendered result.

The Glow mask allows the glow to extend beyond the borders of the mask, while restricting the source

of the glow to only those pixels within the mask.

Glow masks are identical to Effect masks in every other respect.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION