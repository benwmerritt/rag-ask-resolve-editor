---
title: "Patch Replacer (Studio Version Only)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 645
---

# Patch Replacer (Studio Version Only)

The Patch Replacer is a quick fix when you need to “paint out” an unwanted feature from the image.

For those of you who’ve been using windows and Node Sizing to do small digital paint jobs, this plugin

offers more options and a streamlined workflow.

On adding the plugin, an onscreen control consisting of two patches appears, with an arrow

connecting them indicating which patch is being copied into the other. The patch behind the arrow is

the “source” patch, used to sample part of the image, and the patch in front of the arrow is the “target”

patch, used to cover up the unwanted feature using pixels from the source patch.

To use the Patch Replacer, simply drag the target patch over the feature you want to obscure, resize it

to fit using the corner controls (the source patch is automatically resized to match), and then drag the

source patch to an area of the image that can convincingly be used to fill the target patch.

(Top) Original image, (Botom) Removing the thermostat with the Patch Replacer

The source and target patches can be motion tracked using the FX tracker, so this tool is effective

even if the subject or camera is moving.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

Main Controls

The Fill-in Method pop-up menu is arguably the most important, as it defines what method to use to

fill the destination patch with whatever is in the source patch. The rest of the primary controls work

differently depending on which Fill-in method you choose.

�Clone: Simply copies the source patch into the target patch. When Clone is selected, the

Replacement Detail slider (which defaults to 1) lets you fade out the source patch, while Region

Shape lets you choose a different kind of shape to use, and Blur Shape Edges lets you feather the

edge of this operation, to more convincingly blend the source with the target area.

�Blend Clone: A much more sophisticated method of obscuring the target area using pixels from

the source patch, and in many cases will yield better results more quickly than cloning. The source

patch is copied into the target patch in such a way as to combine the source detail with the lighting

found inside of the target area, creating in most instances a fast, seamless match. The Keep

Original Detail checkbox, when turned on, merges detail from the source and target patches to

create a composite, rather than a fill. The Variability slider lets you adjust how solid the center of

the patch is. The Blur Shape Edges slider works a bit differently with Blend Clone selected, but

the idea is the same, feathering the effect from the outside in to obscure instances where there’s a

noticeable border around the target area.

�Fast Mask: Eliminates the source patch, doing instead a quick neighboring pixel blend that works

well with small patches but can betray a grid pattern on larger patches. Region Shape and Blur

Shape Edges are both adjustable.

�Blend Mask: Eliminates the source patch, and essentially does the Blend Clone operation but

without the source. Works well on small patches, but can become too blurred on larger patch

sizes. Gives you access to the Variability slider of the Blend Clone.

Patch Positions

Source X and Y, Target X and Y, and Target Width and Height are provided as explicit controls both for

numeric adjustment, should that be necessary, and also to allow for keyframing in case you need to

change the position and/or size of the source and fill patches over time.

Keep in mind that the source and target patches can be motion tracked using the FX tracker, although

two checkboxes, Source Follows Track and Target Follows Track, let you disable FX tracker match

moving when necessary.

The Align Source to Target button moves the source patch directly over the target patch, allowing you

to quickly reset and iterate the location of the source patch.

Onscreen Controls

The Control Visibility pop-up menu lets you choose whether the source and target onscreen controls

are visible as you work. Show (the default) leaves all onscreen controls visible all the time. Auto Hide

hides all onscreen controls whenever you’re dragging one, letting you see the image as you adjust it

without having these controls in the way. Hide makes all onscreen controls invisible, so you can see a

clean version of the image with the effect, however you can still edit the effect if you remember where

the controls are.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

Chapter 164

Resolve FX Sharpen

These plugins offer a newer and more detailed method of sharpening specific

details in images than the sharpen operation found in the Blur palette.

Three different plugins offer different ways of using the same fundamental algorithm to perform

different tasks.

Contents

Sharpen (Studio Version Only)����������������������������������������������������������������������������������������������������������������������������������������������������� 3573

Main Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3573

Detail Levels����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3573

Chroma���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3573

Sharpen Edges (Studio Version Only)��������������������������������������������������������������������������������������������������������������������������������������� 3574

Main Controls���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3574

Edge Detection Controls����������������������������������������������������������������������������������������������������������������������������������������������������������������� 3574

Soften and Sharpen (Studio Version Only)����������������������������������������������������������������������������������������������������������������������������� 3574

Main Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3575

Adjust Small Skin Texture Granularity������������������������������������������������������������������������������������������������������������������������������������� 3575


Resolve FX Overview | Chapter 164 Resolve FX Sharpen

COLOR

Sharpen (Studio Version Only)

The Sharpen filter functions by separating the image into four levels of detail, the underlying

structure, the fine scale details, the medium scale details, and the large scale details, each of which

encompasses differently sized structures that comprise the overall image. In this way, the Sharpen

filter lets you apply different amounts of sharpening to each of the fine, medium, and large structures

of the image, giving you enormous control over how these different structures of image detail

are affected.

Main Controls

Controls the overall sharpening effect.

�Sharpen Amount: The primary global control that lets you add sharpening to the image. To refine

the result, use the controls in Detail Levels to choose how much sharpness to apply to each size

of structure this plugin can operate upon. 1.800 is the default value. 0 is no sharpening, 5.000 is

maximum sharpening.

Detail Levels

Lets you customize the sharpen effect in a variety of highly specific ways.

�Fine Detail Size: This slider adjusts the threshold of what is considered to be a fine detail,

although this also alters which image structures are affected by the Medium and Large Details

sliders as well. Lowering this slider omits larger structures of the image from sharpening. The

default is 0.050.

�Fine Detail: At its default setting, the Fine Details slider governs the sharpness of extremely

fine detail such as skin pores and strands of hair, or small speckles on textured surfaces. Lower

settings apply less sharpening to these structures, while higher settings apply more sharpening.

�Medium Details: This slider governs the sharpness of coarser detail such as freckles, wrinkles,

clusters of hair, and surface details with greater edge definition. Lower settings apply less

sharpening to these structures, while higher settings apply more sharpening.

�Large Details: This slider governs the sharpness of the largest details in the image, such as

eyelids, the shadows at the edges of lips and noses, and the edges where hair meets the face,

and the most contrasty edge details throughout the image. Lower settings apply less sharpening

to these structures, while higher settings apply more sharpening.

Chroma

A special purpose control that you want to handle with care.

�Sharpen Chroma: Selectively sharpens the chroma of the image while leaving the luma (Y) alone.


Resolve FX Overview | Chapter 164 Resolve FX Sharpen

COLOR

Sharpen Edges (Studio Version Only)

A variation of the Sharpen filter that’s streamlined for detecting edges to create a key used to limit

sharpening to the selected edge details of an image. This is a good filter to use when attempting to

make mildly soft-focus clips less objectionable.

Main Controls

Controls the overall sharpening effect accomplished with this plugin.

�Sharpen Amount: The primary global control for adding sharpening to the edges

detected by this filter.

�Sharpen Radius: Controls the granularity of the detail that’s added using Sharpen Amount.

Edge Detection Controls

These controls let you customize the sharpen effect in very specific ways.

�Display Edges: This checkbox lets you see a grayscale preview of the edges that are being

detected for sharpening while you use the other controls in this group. If you turn this checkbox

on, you can see precisely the effect that the four other controls in this section have on the key that

determines which parts of the image are sharpened.

�Pre Denoise: Smooths the matte to remove individual pixels of noise. Reducing Pre Denoise lets

you minimize edges from the key that you don’t want to sharpen and soften edges that are jagged

because of excessive noise. Raising Pre Denoise adds more edges to the sharpening operation

and strengthens the edges that are already there.

�Edge Detect Threshold: Lets you adjust how strong edge detail needs to be in order to be

included in the key. Reducing this parameter includes more edges in the operation, while raising it

excludes edges from the operation.

�Edge Mask Strength: Lets you increase the intensity of the edges in the key. Reducing Edge Mask

Strength diminishes the edges and reduces the intensity of sharpening in those areas. Raising

Edge Mask Strength intensifies the edges and adds more of the image within the region of each

detected edge to the sharpening operation.

�Edge Blur: Lets you control the softness of the edges in the key. Reducing Edge Blur sharpens the

key and narrows the edges that are affected by sharpening. Increasing Edge Blur softens the key

and potentially includes a wider area of image detail in the sharpening operation.

Soften and Sharpen (Studio Version Only)

A variation of the Sharpen filter that’s streamlined for letting you both smooth some details and add

sharpness to other details of the image based on the size of the structures. It can be used with any

image for which you want to smooth some features while sharpening others, but this is an operation

that’s often used for minimizing unwanted blemishes, wrinkles, or scarring when used within a window

or qualifier that’s isolating the skin.

The advantage of using Soften and Sharpen is that you can use the Small Texture slider to leave a

bit of natural skin detail intact, such as pores and other small naturalistic details, while you use the

Medium and Large Texture controls to smooth out unwanted details in whatever proportion gives you

a naturalistic result.


Resolve FX Overview | Chapter 164 Resolve FX Sharpen

COLOR

TIP: The best way to achieve a more natural result is to leave Small Texture at 0 or just

above, while reducing Medium Texture just enough to minimize whatever details merit

minimizing and reducing Large Texture by somewhat less to minimize larger blemishes, while

leaving overall face detail intact. This is the logic behind the default values of Small 0.000,

Medium –0.800, and Large –0.300.