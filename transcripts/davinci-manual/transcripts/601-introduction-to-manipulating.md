---
title: "Introduction to Manipulating"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 601
---

# Introduction to Manipulating

and Combining Keys

Each node’s key input and key output makes it possible to route key channel data from one node to

another so you can apply isolated corrections. Furthermore, the Key Mixer lets you combine a variety

of keys from different nodes to create more detailed keys with which to tackle complex operations.

This section covers all the ways you can recombine key data, as well as how keys can be used in

conjunction with the Alpha output to create regions of transparency in a clip for compositing right

within DaVinci Resolve.

Outside Nodes

Whenever you use a Power Window or HSL Qualifier to limit a correction within one node, a special

node structure lets you automatically create a second node, called an Outside node, to apply

additional adjustments to the inverse of the region you isolated in the previous node. Outside nodes

are really just Corrector nodes with the Key Palette’s Key Input Invert control enabled, which makes it

easy to apply separate corrections to an isolated subject and to its surroundings.

The Key Input Invert button, in the Key palette, that

inverts any key fed to that node’s Key Input

In the following example, the sky has been isolated using a Power Window, and an Outside node has

been added to make an additional correction to everything else within the shot.

The Outside node automatically has its key input inverted.

To add an Outside node to a node, creating a secondary correction:


Select a node that has been limited using a Power Window or HSL Qualifier.


Do one of the following:

�Choose Nodes > Add Outside (Option-O).

�Right-click a node choose Add Outside Node.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

A new node is created immediately after the selected node, with the RGB and key outputs of the first

node automatically connected to those of the new node.

When selecting the new node and opening the Key palette, you can see that the Key Input’s Invert

control is on by default, which is what inverts the key from the previous node.

The Key Input Invert control is on by default for each node.

If, instead of using the Outside node to invert the incoming key, you want to copy the existing key

in order to perform another operation to the same isolated region, you can disable the key input’s

Invert control.

Feeding Keys From One Node to Another

One of the most powerful aspects of the Node Editor is the ability to create keys based on a specific

part of the node tree, and feed the result into a completely different correction somewhere else in the

node tree. This is one of the reasons for the separate key input and output on every Corrector node.

The key that’s created whenever you use the HSL Qualifier, create one or more windows, or use an

external matte can be output from one node’s key output and fed to the key input of any other node

in a tree. There are many reasons to do this, but the following example shows a common problem you

can solve with this technique.

Using a key from one node to make an adjustment with a different node:


Use Node 1 to apply a basic primary correction, increasing contrast and balancing the color to

achieve a pleasing ambient color temperature.


Add a Serial node (Node 2), followed by a Layer Mixer node which also adds Node 4 (as seen

in the following screenshots). Then, completely desaturate Node 4 and add contrast to make it

super-high contrast black and white, desaturate Node 2 just a bit, and right-click the Layer Mixer

node to choose the Overlay blend mode with which to combine these two layers.

A group of nodes to create a stylized image


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

The result is a highly stylized image, but the skin tone on the actor’s face and hands in the

resulting image are too monochromatic, and you want to give them some differentiation. Simply

adding another node after the Layer Mixer and keying the skin tone may not work well because

the low level of saturation will make a key difficult to pull.

The resulting stylized image may be difficult to key accurately.


Add another node after the Layer Mixer (Node 5 in the screenshot), and then right-click in the gray

background area of the Node Editor, and choose Add Node > Corrector to create an unattached

node, (Node 6).


Connect the RGB output of Node 1 to the RGB input of Node 6, and then connect the key output of

Node 6 to the key input of Node 5. Now you’re ready to pull a high-quality key from the very first

correction in Node 1, skipping all the complication coming afterwards.


Use the HSL Qualifier in Node 6 to pull a good strong skin tone key based on the primary image.

Given the way the node tree is now set up, that key is fed to Node 5, and will limit whatever

adjustments you make there.

Using Node 6 to pull a key from the image output by Node 1, and feeding that key to Node 5


Now, you can make your adjustment to Node 6’s grade, to lower the contrast, brighten, and

increase the saturation of the actor’s skin tone.As a result of this operation, the background

remains desaturated and contrasty, while the actor’s skin tone has the brighter quality we need

for the shot.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

(Left) An entire clip with a high-contrast grade, (Right) The skin tone graded

differently from the high-contrast grade using a key

This example could have been handled in a variety of different ways, but the point is that you

can add nodes that connect to the state of the image at any part of a node tree, and use them

to generate keys to feed to any other node, regardless of what’s happening to the picture

in between.

Connecting Key Outputs to

RGB Inputs, and Vice Versa

There’s another way you can manipulate a key from one node using another in the Node Editor, and

that’s to connect the key output from one node to the RGB input of another node. When you do this,

you can use any of the controls of the second node to manipulate the key, and you can then use the

result by connecting the RGB output of the second node to the key input of a third node.

Connecting a key output to an RGB input to adjust a key with a second node’s controls

In the node tree shown above, Node 2 pulls a key, Node 4 manipulates the key, and Node 3 uses the

key to make a color adjustment.

Keep in mind that a key is just a grayscale image. Setting up this kind of node structure lets you

use any of the second node’s controls, such as the Custom Curves, Noise Reduction or Motion Blur

controls, Sharpen, Midtone Contrast, Lift/Gamma/Gain, Contrast, or Log controls, to manipulate the key

in ways you couldn’t do using only the Matte Finesse controls.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

While this technique may not be necessary for conventional color isolations, it can come in very handy

when making tricky isolations with hard to key subjects, or when using one of the Qualifier modes

to pull a key to create transparency for compositing using the Node Editor’s Alpha output. In this

instance, you can connect the RGB output of a node used for key manipulation directly to the Alpha

output. In the example, Node 1 pulls a key, and the RGB is connected to Node 3 which is used to

color correct the foreground image. The key from Node 1 is connected to the RGB of Node 2, which

manipulates the key to clean it up prior to connecting it to the Alpha output block at the bottom right of

the Node Editor.

Connecting a key output to an RGB input to adjust a

key used to create transparency via the Alpha output

Furthermore, this capability also lets you create keys in other ways besides using the Qualifier palette

controls. In the following example, the Contrast and Custom Curve controls in Node 3 create a high-

contrast matte of the windows which is blurred. The RGB output of Node 3 is then connected to the

KEY input of Node 2, where the resulting key can be used for a variety of adjustments; in this case,

to tint the product within the image green. Alternately, this technique could be also be used to create

transparency via the Alpha output.

Using a high-contrast color correction as a key

You can manually connect RGB inputs and outputs to Key inputs and outputs by dragging links

between them. Alternatively, you can drag and hover a node over an RGB or Key link to insert it.

Interconnecting key and RGB inputs and outputs is a powerful capability that lets you create many

kinds of workarounds for uncommon situations.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR