---
title: "Layer Mixer Node Structures"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 600
---

# Layer Mixer Node Structures

The Layer Mixer is structurally quite similar to the layout used by the Parallel Mixer. However, there are

two key differences. First, the Layer Mixer node combines multiple adjustments with priority given to

the image adjustment in the lowest overlapping node input. Second, you have the option of combining

all of the Corrector nodes that are connected to a Layer Mixer using one of several different composite

modes, to create a wide variety of visual effects.

Because of their similarities, layering nodes with the Layer Mixer works in much the same way as

creating a Parallel node structure.

Layer Mixer Prioritization

In the following example, the same node structure from the Parallel Mixer example is shown, this time

with the three overlapping color adjustments mixed together using the Layer Mixer.

The Layer Mixer prioritizes nodes connected to lower inputs

such that each node’s output completely obscures whatever is behind it

Now, instead of the three adjusted color tints being blended, you can see that the blue tint, which is

connected to the lowest input of the Layer Mixer, is dominant and covers the overlapping regions of

the two other adjustments. Meanwhile, the green tint, which is connected to the middle input of the

Layer Mixer, covers the overlapping portion of the orange tint, which is connected to the highest input

of the Layer Mixer.

Rearranging which connections are attached to which Layer Mixer inputs changes each node’s priority,

and like the Parallel Mixer, you can add more inputs manually, or by dragging the output of a node to

the Layer Mixer.


Color | Chapter 145 Serial, Parallel, and Layer Nodes

COLOR

The Layer Mixer’s prioritization is most useful when you have an overlapping adjustment that you need

to override any other adjustments happening on that stack. In the following example, two nodes are

connected to the Layer Mixer node. Node 2 is applying a high-contrast, cool look to the entire clip.

Node 3 isolates the skin tone, which is unflattering with the background stylization, and applies a

different, more naturalistic adjustment.

Using the layer mixer, grades on Node 3 will have a greater

priority over Node 2, so the final grade combinµes the high

contrast from Node 2 with the adjusted skin tone from Node 4

Because of the Layer Mixer’s prioritization, the adjustment made to the woman’s skin tone

completely covers the adjustment made to the node that comes above it, providing the best of

both worlds with one simple adjustment.

Using Composite Modes With the Layer Mixer

You have the option of combining the adjustments made by all nodes connected to a Layer Mixer

node using the same Composite modes that are available when compositing clips in the Timeline. This

lets you combine different overlapping image adjustments using compositing math to achieve creative

effects or utilitarian fixes.

The following simple example shows two overlapping Corrector nodes connected to a Layer Mixer

node that’s set to the Add composite mode. Node 3 has no adjustment, but Node 5 has an extremely

high-contrast curve adjustment applied, along with a blur, that effectively isolates the highlights of the

image and feathers them out.


Color | Chapter 145 Serial, Parallel, and Layer Nodes

COLOR

Combining two nodes using the Layer Mixer

set to Add to create a glowing effect

By adding both treatments together, a hot glow has been created, blowing out the highlights

of the image. Many, many other effects are possible using the different composite modes that

are available.

For more information on composite modes, see Chapter 50, “Compositing and Transforms in

the Timeline.”

Adjusting Layer Node Strength Using Key Output Gain

Whether you’re combining overlapping corrections, or mixing different adjustments using Composite

modes, you’ll run into situations where you want to reduce the influence of one overlapping

adjustment relative to the other nodes that are connected to the Layer Mixer node. This can be

accomplished using each overlapping node’s Key Output Gain parameter, located in the Key palette.

Using the Output Gain parameter in the Key palette


Color | Chapter 145 Serial, Parallel, and Layer Nodes

COLOR

Key Output Gain defaults to 1.00, but lowering this value reduces the strength of that node’s

contribution to the Layer Mixer. Using the previous example, selecting Node 4 (the high‑contrast

image used to create the glow), opening the Key palette, and reducing the Key Output Gain parameter

to 0.50 reduces the intensity of the Glow effect by half.

You can use Key Output Gain to mix the proportion of any number of overlapping adjustments in order

to create the perfect combination for your purposes.

TIP: You can also use the Key Output Gain parameter to mix the proportion of adjustments

being combined using the Parallel Mixer node.

Converting Layer Mixers to Parallel Mixers

You can easily convert a Layer Mixer to a Parallel Mixer should you discover that you need to mix your

overlapping corrections evenly rather than combine them with priority. Keep in mind that you’ll lose the

ability to use Composite modes.

To change a Layer Mixer node into a Parallel Mixer node:

�Right-click a Parallel Mixer node and choose Morph Into Parallel Node.


Color | Chapter 145 Serial, Parallel, and Layer Nodes

COLOR

Chapter 146

Combining Keys

and Using Mattes

A key is the actual image channel that’s generated by different secondary

operations to isolate specific portions of images to work on.

This chapter covers different ways you can manipulate and combine keys from multiple nodes, or

propagate keys among nodes. It also shows different ways you can use mattes that are imported from

other applications, as well as how to use the Key palette to further manipulate keys in different ways.

Contents

Introduction to Manipulating and Combining Keys���������������������������������������������������������������������������������������������������������� 3341

Outside Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3341

Feeding Keys From One Node to Another��������������������������������������������������������������������������������������������������������������������������� 3342

Connecting Key Outputs to RGB Inputs, and Vice Versa�������������������������������������������������������������������������������������������� 3344

Using External Mattes��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3346

External Mattes to Limit Adjustments��������������������������������������������������������������������������������������������������������������������������������������� 3347

Extracting External Mattes from OpenEXR Layers����������������������������������������������������������������������������������������������������������� 3349

Using External Mattes to Add Texture������������������������������������������������������������������������������������������������������������������������������������� 3350

Using External Mattes to Create Transparency������������������������������������������������������������������������������������������������������������������ 3352

Key Palette Controls for the External Matte Node������������������������������������������������������������������������������������������������������������ 3353

Using Mattes From the Fusion Page��������������������������������������������������������������������������������������������������������������������������������������� 3353

Using the Key Mixer������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3356

Adding Two Keys Together����������������������������������������������������������������������������������������������������������������������������������������������������������� 3356

Subtracting One Key from Another������������������������������������������������������������������������������������������������������������������������������������������� 3357

Adding Inputs to Key Mixer Nodes�������������������������������������������������������������������������������������������������������������������������������������������� 3360

Using the Key Palette����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3361

Using the Key Palette to Affect Corrector Nodes��������������������������������������������������������������������������������������������������������������� 3361

Using the Key Palette to Adjust Key Mixer Controls��������������������������������������������������������������������������������������������������������� 3362

The Many Uses of Key Output Gain������������������������������������������������������������������������������������������������������������������������������������������ 3363


Color | Chapter 146 Combining Keys and Using Mattes

COLOR