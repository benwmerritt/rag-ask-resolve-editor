---
title: "Subtracting One Key from Another"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 604
---

# Subtracting One Key from Another

The way multiple keys are combined within the Key Mixer depends on a pair of Key Input buttons you

can toggle using the Key palette. In the following example, a partial green tint is washed throughout

the midtones of the image using a qualifier, but you want to exclude the man’s skin tone from this

operation. Using the Key Mixer, you can subtract one key from another to accomplish this with ease.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

A selective blue tint added to the midtones

of the image includes the red sign.

To change the Key Input settings for a node connected to a Key Mixer:


In this example, Node 2 is isolating part of the midtones of the image, and feeding its key through

the Key Mixer to Node 4, which is using it to apply a partial blue tint. However, in preparation for

subtracting the skin tone from this operation, Node 3 is isolating the man’s skin tone.

A node setup in preparation of subtracting the Bar sign from the

midtone isolation being used to add a partial blue tint


To reveal the controls you’ll use to change how the key from Node 3 interacts with the key from

Node 2, double-click the Key Mixer node to select it.


Open the Key palette; a list of all input links that are connected to the Key Mixer appears at

the right.

The input list of the Key Mixer node


Color | Chapter 146 Combining Keys and Using Mattes

COLOR


Within each list entry is the input name (Input Link 1, Input Link 2, etc.), a Matte control,

a Mask control, a gain parameter, and an offset parameter.

To subtract Node 3’s key from that of Node 2: Turn on both

the Key Input Matte button and the Key Input Invert button for

Input Link 2.

Turning on Matte and Invert for Input Link 2

to Output Node 3 subtracted from Node 2

To subtract Node 2’s key from that of Node 3: Turn on both

the Key Input Matte button and the Key Input Invert button for

Input Link 1.

Turning on Matte and Invert for Input Link 1

to Output Node 2 subtracted from Node 3

To limit the output to the intersection of both keys: Turn on

the Key Input Matte button for either Input Link 1 or Input Link 2.

Turning on Matte for Input Link 1 to output

the intersection of two mattes


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

To invert the resulting matte you’ve created: Turn on the Output Link Invert button.

When you’re finished, if you choose to subtract Node 3’s key from that of Node 2, the result should

resemble the following screenshot.

The result of subtracting a key of the man’s face from a key of the overall

midtones of the image, and using that to add a selective green tint

Adding Inputs to Key Mixer Nodes

New Key Mixer nodes have two key inputs by default. If necessary, additional inputs can be added in

order to combine even more keys with one another.

To add inputs to the Key Mixer:

�Drag the Key Output from a corrector node to the Key Mixer.

�Right-click a Key Mixer node, and choose Add One Input.

When combining three or more keys, the interaction of keys using the Key palette controls becomes

even more complex, but the rules outlined above still apply.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

Using the Key Palette

For example, the Key Input Invert control is always enabled when you add an Outside node, which is

why the Outside node applies adjustments to the inverse area of the previous node. If you turn this

control off, that node’s key will exactly mirror the original key being fed to it from the previous node.

The controls that are available in the Key palette vary depending on what kind of node you

have selected:

Corrector Nodes: Have three sets of parameters. Key Input parameters let you make

adjustments to keys being fed through a node’s Key Input connection. The Key Output

parameters let you make adjustments to the key data being output by a node’s Key Output

connection, and includes the incredibly powerful Offset Gain parameter that governs the

strength of that node’s contribution to the overall grade. Finally, the Qualifier parameters let

you make adjustments to the internal key created with the HSL Qualifier or Window controls.

This functionality is covered more extensively in the next section.

Ext Mattes: Have two sets of parameters. Transform parameters let you make geometric

transformations to a matte so it fits the clip it’s being applied to better. An Offset control

lets you slip the sync between an external matte and the clip to which it’s applied. This

functionality is covered in the section on external mattes.

Key Mixer Nodes: Have two sets of parameters that are dependent on which of the

connections attached to a Key Mixer’s key inputs is selected. Input parameters let you adjust

how much of a contribution a key makes to the total key mix, and whether the contribution is

additive or subtractive.

The Output parameters let you adjust the inversion and strength of the key that’s output by the Key

Mixer. This functionality is described more extensively in the Key Mixer section.

Layer Mixer and Parallel Mixer nodes have no adjustable controls in the Key palette.

Using the Key Palette to Affect Corrector Nodes

When you open the Key palette for a selected Corrector node, you can adjust the

following parameters:

Key palette showing controls when a node is selected


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

Key Input Controls

�Input invert: Inverts the key being fed into the key input. Off by default.

�Input matte: Lets you switch the key input between Matte and Mask modes. In Matte mode (on by

default) the key input combines via intersection with keys generated internally using the Qualifier

or Windows palette. In Mask mode, the key input is added to the internal key instead.

�Gain: Controls the strength of the key connected to the key input.

�Offset: Controls the contrast of the key connected to the key input.

�Blur Radius: Blurs the key connected to the key input

�Blur H/V Ratio: Alters the horizontal/vertical ratio of the blur that’s being applied to the key input.

Key Output Controls

�Qualifier invert: Inverts the overall key.

�Gain: Using the key output, this parameter governs the strength of that node’s contribution to the

overall grade. Setting Gain to 0 results in that node having no effect at all, while the default setting

of 1.00 applies the full strength of any adjustments made with that node. The maximum setting of

2.00 increases the intensity of any part of the key output that’s less than 100 percent white. You

can also use this parameter to keyframe the key output to fade that node’s contribution in or out

with one set of keyframes.

�Offset: Lets you adjust the contrast of the Output key. This has no effect if the entire key is 100

percent white (a solid key).

Qualifier Controls

�Qualifier invert: Inverts the key created by that node’s Qualifier palette.

�Qualifier matte: Lets you switch the interaction of the keys generated by the Qualifier and Window

palettes between Matte and Mask modes. In Matte mode (the default), the Qualifier and Windows

palettes combine via intersection. In Mask mode, they’re added together instead.

�Gain: Lets you raise or lower the strength of the key generated by the Qualifier palette.

�Offset: Lets you adjust the contrast of the key generated by the Qualifier palette.