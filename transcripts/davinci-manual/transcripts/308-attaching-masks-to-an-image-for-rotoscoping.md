---
title: "Attaching Masks to an Image for Rotoscoping"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 308
---

# Attaching Masks to an Image for Rotoscoping

There are two ways you’ll typically attach a Mask node, such as a Polygon node, so that it adds an

alpha channel to an image for compositing later in the node tree.

Using a MatteControl Node

The MatteControl node is the main node used for combining masks in different ways and inserting the

result into an image stream. The MatteControl node is attached downstream of the node outputting

the image you want to rotoscope. You’ll typically attach a Polygon or B-Spline node to the Garbage

Matte input of the MatteControl node to use the spline as an alpha channel.

Feeding a Polygon node to a MatteControl node to perform rotoscoping

To use this setup, you’ll load the MatteControl node into the viewer and select the Polygon node to

expose its controls so you can draw and modify a spline while viewing the image you’re rotoscoping.

The MatteControl node’s Garbage Matte > Invert checkbox lets you choose which part of the image

becomes transparent.

Connecting a Mask to a MediaIn or Loader Node’s Input

This method is a bit simpler but requires you to know that you can view one node while adjusting

another node, even if that other node is disconnected. If you add an unattached Mask node such as

a Polygon or B-Spline node, and then place a MediaIn or Loader node directly into the viewer while

selecting the Mask node, you can draw a spline to rotoscope the image.

Rotoscoping a MediaIn node using

a disconnected Polygon node

When you’re finished rotoscoping, you simply connect the Polygon node’s output to the Loader node’s

input, and an alpha channel is automatically added to that node.

Connecting a Polygon node to a MediaIn node

to use a spline as an alpha channel


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

TIP: If you connect a Mask node to a MediaIn or Loader node’s effect input without any

shapes drawn, that mask outputs full transparency, so the immediate result is that the image

output by the MediaIn or Loader node becomes completely blank. This is why when you want

to rotoscope by connecting a mask to the input of a MediaIn or Loader node, you need to

work within a disconnected Mask node first. Once the shape you’re drawing has been closed,

connect the Mask node to the MediaIn or Loader’s input, and you’re good to go.

Combining Multiple Masks

Masks are designed to be added one after the other, with each Mask node acting as an additional

layer of masking.

Combining multiple Polygon nodes

one after the other in the node tree

When a Mask node’s input is attached to another mask, a Paint Mode drop-down menu appears, which

allows you to choose how you want to combine the two masks.

The Paint Mode parµameter in the Polygon node Inspector parameters


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

The default option is Merge, but you can also choose Subtract, Minimum, Maximum, Multiply, or

any other operation that will give you the mask boolean interaction you need. Additionally, a pair of

Invert and Solid checkboxes let you further customize how to combine the current mask with the one

before it.

The Invert and Solid options

Mask Inputs on Other Nodes

Masks can be used for a variety of reasons, so there are several categories of mask inputs that

different nodes include to accommodate these different uses. Incidentally, in most cases you can

connect either masks or mattes to a mask input to take advantage of that input’s functionality.

TIP: If you select a node with an empty effect mask input, adding a Mask node automatically

connects to the open effect mask input.

Effects Mask Inputs

Almost every node in Fusion has an Effect mask input (colored blue), which lets you choose which

parts of the image will or will not be affected by that node.

A Blur node with a Polygon

node masking its effect

While masks (or mattes) are connected via an input, they are actually applied “post effect,” which

means the node first applies its effect to the entire image, and then the mask is used to limit the result

by copying over unaffected image data from the input.

Although many nodes support effects masking, there are a few where this type of mask does not

apply—notably Savers, Time nodes, and Resize, Scale, and Crop nodes.

TIP: Effects masks define the domain of definition (DoD) for that effect,

making it more efficient.


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

A Polygon node used as a mask to limit the Blur node’s effect

Pre-Masking Inputs

Unlike effect masks, a pre-mask input (the name of which is usually specific to each node using them)

is used by the node before the effect is applied. This usually causes the node to render more quickly

and to produce a more realistic result. In the case of the Highlight and the Glow nodes, a pre-mask

restricts the effect to certain areas of the image but allows the result of that effect to extend beyond

the limits of the mask.

The advantage to pre-masking is that the behavior of glows and highlights in the real world can be

more closely mimicked. For example, if an actor is filmed in front of a bright light, the light will cause

a glow in the camera lens. Because the glow happens in the lens, the luminance of the actor will be

affected even though the source of the glow is only from the light.

In the case of the DVE node, a pre-mask is used to apply a transformation to a selected portion of

the image, without affecting portions of the image outside of the mask. This is useful for applying

transformations to only a region of the image.

Garbage Matte Inputs

Garbage Matte inputs (usually colored gray) are used to exclude light stands, rigging, and boom

microphones that intrude upon masks being pulled via blue-screen and green-screen keys. In the

following example, a lighting stand to the left is removed from the image via a B-Spline node’s mask

connected to the Garbage Matte input of the DeltaKeyer node.

A B-Spline node is connected to the Garbage Matte input

of a DeltaKeyer node to eliminate a light stand at the left of frame


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION

TIP: You can quickly add a mask node to the Effect/Solid/Garbage Matte inputs of a keyer

node by right-clicking the header bar of that node in the Inspector and choosing whichever

mask node you want to use from the Effect Mask, SolidMatte, and GarbageMatte submenus.

You choose whether a garbage matte is applied to a keying node as opaque or transparent in the

Inspector for the node to which it’s connected.

Solid Matte

Solid Matte inputs (colored white) are intended to fill unwanted holes in a matte, often with a less

carefully pulled key producing a dense matte with eroded edges, although you could also use a

polygon or mask paint to serve this purpose. In the example below, a gentle key designed to preserve

the soft edges of the talent’s hair leaves holes in the mask of the woman’s face, but using another

DeltaKeyer to create a solid matte for the interior of the key that can be eroded to be smaller than the

original matte lets you fill the holes while leaving the soft edges alone. This is also sometimes known

as a hold-out matte.

Filling in holes in the mask pulled by the DeltaKeyer1 node (left) with another, harder but eroded

key in DeltaKeyer2 that’s connected to the SolidMatte input of DeltaKeyer1 (right)


Fusion Fundamentals | Chapter 80 Rotoscoping with Masks

FUSION