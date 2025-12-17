---
title: "Node Colors Tell You Which Nodes Go Together"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 298
---

# Node Colors Tell You Which Nodes Go Together

Each node in Fusion accomplishes a single type of effect or operation. These single-purpose nodes

make it easier to decipher a complex composition when examining its node tree. Single-purpose

nodes also make it easier to focus on fine-tuning specific adjustments, one at a time, when assembling

an ever-growing tree.

Because each Fusion node has a specific function, they’re categorized by type to make it easier to

keep track of which nodes require what types of image channels as input, and what image data you

can expect each node to output. These general types are described here.

A node tree showing the main categories of node colors

Blue MediaIn and Loader Nodes, and Green Generator Nodes

Blue MediaIn nodes and blue Loader nodes add clips to a composite, and green Generator nodes

create images. Both types of nodes output RGBA channels (depending on the source and generator),

and may optionally output auxiliary channels for doing advanced compositing operations.


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

Because these are sources of images, both kinds of nodes can be attached to a wide variety of

other nodes for effects creation besides just 2D nodes. For example, you can also connect MediaIn

nodes to Image Plane 3D nodes for 3D compositing, or to pEmitter nodes set to “Bitmap” for creating

different particle systems. Green Generator nodes can be similarly attached to many different kinds of

nodes, for example, attaching a FastNoise node to a Displace 3D node to impose undulating effects to

3D shapes.

Shape nodes are also green, although they must be attached to a specialized set of gray modifier

and render nodes (all of which begin with the letter “s” and appear in the Shape category of the

Effects Library).

2D Processing Nodes, Color Coded by Type

These encompass most 2D processing and compositing operations in Fusion, all of which process

RGBA channels and pass along auxiliary channels. These include:

�Orange Blur nodes

�Olive Color Adjustment nodes (color adjustment nodes additionally concatenate with one another)

�Pink Paint nodes

�Dark orange Tracking nodes

�Tan Transform node (transform nodes additionally concatenate with one another)

�Teal VR nodes

�Dark brown Warp nodes

�Gray, which includes Compositing nodes as well as many other types.

Additionally, some 2D nodes such as Fog and Depth Blur (in the Deep Pixel category) accept and use

auxiliary channels such as Z-Depth to create different perspective effects in 2D.

TIP: Two 2D nodes that specifically don’t process alpha channel data are the Color Corrector

node and the Gamut node. The Color Correction node lets you color correct a foreground

layer to match a background layer without affecting an alpha channel. The Gamut node

lets you perform color space conversions to RGB data from one gamut to another without

affecting the alpha channel.

Purple Particle System Nodes

These are nodes that connect to create different particle systems, and they’re incompatible with other

kinds of nodes until you add a pRender node that outputs 2D RGBA and auxiliary data that can be

composited with other 2D nodes and operations.

Dark Blue 3D Nodes

These are 3D operations, which generate and manipulate 3D data (including auxiliary channels)

that are incompatible with other kinds of nodes until processed via a Renderer 3D node, which then

outputs RGBA and auxiliary data.

Brown Mask Nodes

Masks output single-channel images that can only be connected to one another (to combine masks)

or to specified Mask inputs. Masks are useful for defining transparency (Alpha masks), defining which

parts of an image should be cropped out (Garbage masks), or defining which parts of an image should

be affected by a particular node operation (Effects masks).


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

Using Channels in a Composition

When you connect one node’s Output to another node’s Input, you feed all of the channels that are

output from the upstream node to the downstream node. 2D nodes, which constitute most simple

image processing operations in Fusion, propagate all channel data from node to node, including

RGB, alpha, and auxiliary channels, regardless of whether or not that node actually uses or affects a

particular channel.

2D nodes also typically operate upon all channel data routed through that node. For example,

if you connect a node’s output with RGBA and XYZ Normals channels to the input of a Vortex node,

all channels are equally transformed by the Size, Center, and Angle parameters of this operation,

including the alpha and XYZ normals channels, as seen in the following screenshot.

(Top) The Normal Z channel output by a rendered torus, (Bottom) The Normal Z channel after the output is

connected to a Vortex node; note how this auxiliary channel warps along with the RGB and A channels


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

This is appropriate because in most cases, you want to make sure that all channels are transformed,

warped, or adjusted together. You wouldn’t want to shrink the image without also shrinking the alpha

channel along with it, and the same is true for most other operations.

On the other hand, some nodes deliberately ignore specific channels when it makes sense.

For example, the Color Corrector and Gamut nodes, both of which are designed to alter RGB

data specifically, do not affect auxiliary channels. This makes them convenient for color-matching

foreground and background layers you’re compositing, without worrying that you’re altering the depth

information accompanying that layer.

TIP: If you’re doing something exotic and you actually want to operate on a channel that’s

usually unaffected by a particular node, you can always use the Channel Booleans node to

reassign the channel. When doing this to a single image, it’s important to connect that image

to the background input of the Channel Booleans node, so the alpha and auxiliary channels

are properly handled.

Channel Limiting

Most nodes have a set of Red, Green, Blue, and Alpha buttons in the Settings tab of that node’s Inspector.

These buttons let you exclude any combination of these channels from being affected by that node.

The channel limiting buttons in the Settings panel of

a Transform node, so only the Green channel is affected

For example, if you wanted to use the Transform node to affect only the green channel of an image,

you can turn off the Red, Blue, and Alpha buttons. As a result, the green channel is processed by

this operation, and the red, blue, and alpha channels are copied straight from the node’s input to the

node’s output, skipping that node’s processing to remain unaffected.

Transforming only the green color channel of the image with a Transform effect


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

Skipping Channel Processing

Under the hood, most nodes process all channels first, but afterward copy the input image to the

output for channels that have been enabled. Modern workstations are so fast that this isn’t usually

noticeable, but there are some nodes where deselecting a channel actually causes that node to skip

processing that channel entirely. Nodes that operate this way have a linked set of Red, Green, Blue,

and Alpha buttons on another tab in the node. In these cases, the Common Control channel buttons

are instanced to the channel buttons found elsewhere in the node.

Blur, Brightness/Contrast, Erode/Dilate, and Filter are examples of nodes that all have RGBA buttons in

the main Controls tab of the Inspector, in addition to the Settings tab.

Adding Alpha Channels

Much of visual effects compositing has to do with placing a foreground subject over a background.

Possibly the most fundamental method is through the use of an alpha or matte channel. If an alpha

channel is not contained within the clip, you add one via keying or rotoscoping. While more specific

methods are covered in detail in later chapters, here’s an example of how this is handled within Fusion.

In the case of extracting an alpha matte from a green screen image, you typically connect the image’s

RGB output to the “Input” input of a Keyer node such as the Delta Keyer, and you then use the keyer’s

controls to extract the matte. The Keyer node automatically inserts the alpha channel that’s generated

alongside the RGB channels, so the output is automatically RGBA. Then, when you connect the keyer’s

output to a Merge node to composite it over another image, the Merge node automatically knows to

use the embedded alpha channel coming into the foreground input to create the desired composite,

as seen in the following screenshot.

A simple node tree for keying; note that only one connection links the DeltaKeyer to the Merge node

Rotoscoping, or manually drawing a mask shape using a Polygon or other Mask node is another

technique used to create the matte channel. There are many ways to configure the node tree for this

task, but the simplest setup is just to connect a Polygon or B-Spline mask node to the Effect Mask

input of a MediaIn or Loader node.

TIP: When rotoscoping, it is best to leave the Mask node disconnected from the image while

you draw the shape. This allows you to view the MediaIn node while drawing. Connect the

Matte node once you have finished drawing the shape.

A simple rotoscoping setup using a

Polygon node directly connected to

the Effect Mask input of a MediaIn.


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

In both cases, you can see how the node tree’s ability to carry a single channel or multiple

channels of image data over a single connection line simplifies the compositing process.