---
title: "Chapter 95"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 392
---

# Chapter 95

Composite Nodes

This chapter details the Dissolve and Merge nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Dissolve [Dx]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2159

Merge [Mrg]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2162

MultiMerge [MMrg]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2171

The Common Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2175


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

Dissolve [Dx]

The Dissolve node

Dissolve Node Introduction

The Dissolve node is typically used to mix two images together, providing a gradual transition

between two clips. A Background/Foreground slider controls the mix between the foreground and

background images. Dissolves are commonly used to transition between one clip and another and are

a very common effect in editing. However, you can also use the extreme left and right positions of the

Background/Foreground slider to switch between inputs. Unlike other nodes in Fusion, the Dissolve

node does not require you to connect an image to the background but lets you output either the

background or foreground according to the setting of the Background/Foreground slider.

This quality makes it possible for you use the Dissolve node as an automatic layer switching tool when

connected to background and foreground clips with different durations. Simply connect each clip to

the background and foreground inputs, respectively, and set the Background/Foreground slider to the

input of shorter duration, to determine which is “on top.” After the last frame of that clip has ended, the

Dissolve node automatically switches to the clip that’s connected to the other input.

Besides the default dissolve, the Gradient Wipe setting of the Operation menu allows you to create

arbitrary animated dissolve patterns based on the luminance of an image connected to the optional

Gradient Wipe input. You can use this capability with images of geometric shapes or gradients of

different kinds, movie clips of fire, water ripples, or rain, the Fast Noise node, or even particle systems

you create within the Fusion page to create a variety of unique and creative transitions. Soft-edged

effect masks may also be used to add to the possible effects.

Ultimately, animating the Background/Foreground control allows you to control the transition that’s

being used to switch from the foreground input to the background, or vice versa.

Inputs

The Dissolve node provides three image inputs, all of which are optional:

Background: The first of two images you want to switch between or mix. Unlike most other nodes, it is

unnecessary to connect the background input before connecting the foreground input.

Foreground: The second of two images you want to switch between or mix. The Dissolve node works

best when both foreground and background inputs are connected to images with the same resolution.

Gradient Map: (Optional) The Gradient Map is required only when Gradient Wipe is selected.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

Basic Node Setup

Dissolve nodes are typically connected in the following way, with two input images connected to the

background and foreground inputs, and the output connected to the next node in the composition.

A typical dissolve node structure in Fusion

Resolution Handling

It is recommended to make sure that all images connected to the foreground, background, and

gradient map inputs of the Dissolve node have the same resolution and the same pixel aspect. This is

not required, however. But, the result if you mix resolutions depends on how you set the Background/

Foreground slider.

•	 If the input images are different sizes, but the Foreground/Background slider is set to full

Foreground (all the way to the right) or full Background (all the way to the left), then the

output resolution will be identical to the image resolution of the corresponding node input.

•	 If input images of different sizes are mixed by setting the Background/Foreground slider

somewhere between, the output resolution will be set to the larger of the two input

resolutions to make sure there’s enough room to contain both images. In this case, you may

experience undesirable resolution changes when the slider moves from full foreground or

background to somewhere in between.

For example, if you try to dissolve between a 4K image (connected to the background) and

an 8K image (connected to the foreground), the output of the Dissolve node will be 4K when

the slider is set to full Background, but will suddenly jump to 8K when set to full Foreground or

when mixed somewhere between the foreground and background.

Inspector

Dissolve controls

Controls Tab

These are the main controls that govern the Dissolve node’s behavior.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

�Operation Pop-Up: The Operation menu contains one of seven different methods for mixing

the Foreground and Background inputs. The two images are mixed using the value of the

Background/Foreground slider to determine the percentage each image contributes.

Dissolve: The standard Dissolve mode is the equivalent of a cross dissolve: one clip fades out as

another clip fades in.

Additive Dissolve: Similar in look to a standard film dissolve, an Additive dissolve adds the second

clip and then fades out the first one.

Erode: The Erode method transitions between the two images by growing the darkest areas of

the background image to reveal the foreground image. The effect appears similar to a filmstrip

burning out.

Random Dissolve: A randomly generated dot pattern is used to perform the mix of the images.

Random Noise Dissolve: A moving random dot pattern is used to perform the mix of the images.

Gradient Wipe: The dissolve is controlled by the luminance values of the image in the Gradient

Map input. The edges of this dissolve can be softened. The density and the color of the border

can be adjusted independently.

SMPTE Wipe: The SMPTE wipe is similar to the basic effect wipes found on many video effects

switchers. There is a horizontal wipe and a vertical wipe provided. The wipes can have soft edges

and borders added. The density and the color of the border can be adjusted independently.

�Background/Foreground Slider: Defaults to Foreground. This control determines whether the

output is the background image, the foreground image, or a mix between the two. The type of mix

is determined by the Operation control. If one of the input images is not currently available, the

other one will be output despite the setting of this slider.

Gradient/SMPTE Wipe Controls

The following controls appear only when Gradient Wipe or SMPTE Wipe are selected.

�Wipe Style: (SMPTE Wipe only) This drop-down list allows the selection of two wipe styles:

Horizontal - Left to Right and Vertical - Top to Bottom. The direction of the wipes can be reversed

by using the Invert Wipe checkbox.

�Invert Wipe: (SMPTE Wipe only) When checked, the direction of the wipe will be reversed.

�Softness: Use this control to soften the edge of the transition.

�Border: Select the Border to enable coloring of the transition’s edge and to reveal the associated

controls. The effect is to create a border around the transition edge.

�Border Softness: (Appears only when Border is turned on) The Border Softness slider controls the

width and density of the border. Higher values will create a denser border, and lower values will

create a thinner one.

�Border Color: (Appears only when Border is turned on) Use Border Color to select the color used

in the border.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in both the Dissolve and Merge nodes. These

common controls are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

Merge [Mrg]

The Merge node

Merge Node Introduction

The Merge node combines two images based on the Alpha (opacity) channel associated with the

one in front. This node takes two inputs: a background and a foreground image. The Operation mode

determines which method is used to combine the foreground and background images, supporting the

standard Over, In, Held Out, Atop, and XOr methods for compositing images. Meanwhile, an Apply

Mode pop-up lets you use different composite modes, transfer modes, or blend modes (whichever is

your preferred terminology) to combine the foreground against the background in different ways. This

includes such standard modes as screen, dissolve, multiply, overlay, as well as many others.

The Merge node can perform both additive (premultiplied) and subtractive (non-premultiplied)

compositing, depending on how your compositions and media are set up. However, you also have the

flexibility of using the Additive/Subtractive slider to blend between additive and subtractive composite

results, which has the bonus of providing solutions for problem edges in some cases.

Ordinarily, the foreground and background input connections determine the layer order of images

composited with this node. However, you can also enable Z-Depth compositing if Z-channels are

available in the input images. Z-merging compares the depth value of each pixel in each layer to

determine which pixels should be in front and which should be behind.

Inputs

The Merge node provides three image inputs, all of which are optional:

Background: The orange background input is for the first of two images you want to composite

together. You should connect the background input before connecting the foreground input. If you

connect an image to the background without connecting anything to the foreground input, the Merge

node will output the background image.

Foreground: The green foreground input is for the second of two images you want to composite

together, which is typically a foreground subject that should be in front of the background. If you

connect an image to the foreground input without connecting anything to the background input first,

the Merge node won’t output anything.

Effect Mask: (Optional) The effect mask input lets you mask a limited area of the output image to be

merged where the mask is white (where the foreground image shows in front of the background),

letting the background image show through by itself where the mask is black.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION