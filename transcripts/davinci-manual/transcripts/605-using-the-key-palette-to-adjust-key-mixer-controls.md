---
title: "Using the Key Palette to Adjust Key Mixer Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 605
---

# Using the Key Palette to Adjust Key Mixer Controls

When you open the Key palette for a selected Key Mixer node, you can adjust the following controls:

Key palette showing controls when a Key Mixer is selected


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

�Input list: A list of every input that’s connected to the Key Mixer. Each entry on the list has the

following controls:

Input name: The name of each node connection attached to that key mixer, such as Input Link 1,

Input Link 2, and so on.

Input invert: Inverts the key being fed into this particular input. Off by default.

Input mask: Lets you switch the key input between Matte and Mask modes. In Matte mode (on) the

key input combines via intersection with other inputs connected to the Key mixer. In Mask mode

(off by default), the key input is added to the other key inputs connected to the Key mixer.

Gain parameter: Decreases or increases the intensity of that input matte’s contribution to the

resulting output matte.

Offset parameter: Adjusts the contrast of that input matte’s contribution to the resulting

output matte.

�Output invert: Inverts the overall result of the various Input Link interactions.

�Gain: This parameter increases or reduces the strength of the resulting output key. Setting Gain

to 0 results in all inputs being set to black, while the default setting of 1.00 outputs the combined

mattes at full strength. The maximum setting of 2.00 increases the intensity of any part of the

key output that’s less than 100 percent white, which can have the practical effect of “growing”

soft edges. You can also use this parameter to keyframe the key output to fade that node’s

contribution in or out with one set of keyframes.

�Offset: Lets you adjust the contrast of the Output key.

The Many Uses of Key Output Gain

Several of the techniques discussed in here and in “Secondary Qualifiers,” can be further customized

using the Key Output Gain parameter, which makes it easy to control the strength of a node’s effect on

your grade with a single adjustment. In the following example, two simple Serial nodes are applied to a

clip, with the first one expanding image contrast, and the second one using a variety of controls to add

some extreme warmth to the highlights.

A tint applied only to the highlights of the image

If you decided that you want to reduce the amount of warmth added by the second node

without readjusting the controls you used to create the effect, you could open the Key palette

and lower the Key Output Gain parameter to fade the effect with a single adjustment.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

Four versions of this grade shown using the Versions option of the Split Screen

controls, with Output Gain set to 1, .75, .5, and.25 for comparison

This principle also works for controlling the strength of individual nodes that are being combined in

parallel, that are combined using the Layer node, or for simply fading out the effect of any node in the

node tree you want to “turn down” a bit.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

Chapter 147

Channel Splitting

and Image

Compositing

This chapter begins by showing node structures you can use to isolate, split apart,

convert, and recombine the image channels of clip in different ways. This includes

ways of using the additional image channels that are provided in some types

of media.

The second part of the chapter shows ways that you can do image compositing right in the

Color page, with techniques for using external mattes for compositing, and using qualifier keys to do

green- and blue-screen compositing against other layers in the Timeline.

Contents

Isolating, Splitting, and Converting Color Channels������������������������������������������������������������������������������������������������������ 3366

Enabling, Disabling, and Converting Node Channels���������������������������������������������������������������������������������������������������� 3366

Splitting Channels with the Splitter/Combiner Nodes��������������������������������������������������������������������������������������������������� 3368

Multi-Channel RED HDRx Support������������������������������������������������������������������������������������������������������������������������������������������� 3370

Introduction to Compositing Using the Alpha Output���������������������������������������������������������������������������������������������������� 3373

Using a Qualifier Key to Create Transparency�������������������������������������������������������������������������������������������������������������������� 3373

Using a Matte to Create Transparency����������������������������������������������������������������������������������������������������������������������������������� 3377

Setting the Composite Mode in a Corrector Node����������������������������������������������������������������������������������������������������������� 3378

Using OFX Alpha Channels (Legacy)�������������������������������������������������������������������������������������������������������������������������������������� 3379


Color | Chapter 147 Channel Splitting and Image Compositing

COLOR

Isolating, Splitting, and

Converting Color Channels

DaVinci Resolve provides two different methods of making channel-specific adjustments,

depending on whether you need to apply an adjustment to just one channel within a single node,

or apply separate adjustments to all three channels across several nodes.

Enabling, Disabling, and

Converting Node Channels

Within the contextual menu of each node in the Node Editor is a series of four options:

Expanded choices for choosing a color space and gamma for image

processing within a node, and for disabling channels

While the ability to change the color space in which a particular node’s operations work from the

RGB default has been available for many versions, the list of available color spaces was greatly

expanded in DaVinci Resolve 15 (all the previous options such as Lab (CIE), HSL, and YUV are still

there). Additionally, you have the option of choosing the gamma that node works with as well, with a

similarly long list of options.

Choosing a node-specific color space and gamma does not directly alter the image, as with the Color

Space Transform ResolveFX plugin. Instead, changing a node’s color space and gamma alters what

type of image channels the red, green, and blue controls affect, and how the adjustments you make

within that node are applied. For example, this lets you make a temperature adjustment with a node’s

gamma set to Linear, which in some instances may be mathematically advantageous.

Additionally, three checked Enable Channel 1–3 options let you turn individual channels off or on,

limiting which channel that node’s adjustments will actually affect.

In the following example, you’ll see how to use these features to selectively sharpen just the Y’ (luma)

of an image without affecting the chroma, which can be a more subtle effect than simply sharpening

the entire image.


Color | Chapter 147 Channel Splitting and Image Compositing

COLOR

To use channel disabling and color space conversion to sharpen luma only:


Add a node with which to apply the sharpening you want to the current clip.


Right-click the new node, and choose YUV from the Color Space submenu of the contextual menu.


Apply sharpening by doing one of the following:

�Using that node’s contextual menu, uncheck Enable Channel 2 and Enable Channel 3, which

correspond to the U (Cb) and V (Cr) channels, leaving only Channel 1 (Y) enabled. Then, open the

Blur palette, and drag the ganged Radius sliders down to sharpen the Y channel.

�You can also just open the Blur palette, ungang the Radius sliders, and drag the red slider down

to sharpen the Y channel, since any control with three gangable sliders will automatically assign

those sliders to whichever channels are used by the currently selected Color Space.

(Before) The original image, (After) Sharpening

applied to only the Y’ channel of the image

As you can see, while the Blur palette ordinarily provides separate R, G, and B controls that can be

unganged from one another, the Color Space submenu lets you apply sharpening to the channel

definitions of other colorspaces, providing many other corrective and creative possibilities with the

same controls.


Color | Chapter 147 Channel Splitting and Image Compositing

COLOR