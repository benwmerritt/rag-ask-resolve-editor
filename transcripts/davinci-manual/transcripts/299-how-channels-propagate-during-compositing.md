---
title: "How Channels Propagate During Compositing"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 299
---

# How Channels Propagate During Compositing

Images are combined or composited together using the Merge node. The Merge node takes two

RGBA inputs labeled “Foreground” (green) and “Background” (orange) and combines them into a

single RGB output (or RGBA if both the foreground and background input images have alpha), where

the foreground image is in front (or on top, depending on what you’re working on), and the background

image is, you guessed it, in back.

A simple Merge node composite

Auxiliary channels, on the other hand, are handled in a much more specific way. When you composite

two image layers using the Merge node, auxiliary channels only propagate through the image

that’s connected to the background input. The rationale for this is that in most CGI composites, the

background is most often the CG layer that contains auxiliary channels, and the foreground is a live-

action green screen plate.

Since most compositions use multiple Merge nodes, it pays to be careful about how you connect

the background and foreground inputs of each Merge node to make sure that the correct channels

flow properly.

TIP: Merge nodes are also capable of combining the foreground and background inputs

using Z-Depth channels using the “Perform Depth Merge” checkbox, in which case every

pair of pixels are compared. Which one is in front depends on its Z-Depth and not the

connected input.

Rearranging or Combining Channels

Last, but certainly not least, it’s also possible to rearrange and re-combine channels in any way you

need, using one of four different node operations. For example, you might want to combine the red

channel from one image with the blue and green channels of a second image to create a completely

different channel mix. Alternatively, you might want to take the alpha channel from one image and

merge it with the alpha channel of a second image in different ways, adding, subtracting, or using

other intersection operations to create a very specific blend of the two.

The following nodes are used to re-combine channels in different ways:


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

�Channel Boolean: This is a 3D node used to remap and modify channels of 3D materials using a

variety of simple pre-defined math operations.

�Channel Booleans: Used to shuffle or rearrange RGBA and auxiliary channels within a single input

image, or among two input images, to create a single output image. If you only connect a single

image to this node, it must be connected to the background input to make sure everything works.

�Copy Aux: The Copy Aux node is used to remap channels between RGBA channels and

auxiliary data channels in a single 2D image. The Copy Aux node is mostly a convenience

node, as the copying can also be accomplished with more effort (and flexibility) using a

Channel Booleans node.

�Matte Control: Designed to do any combination of the following: (a) re-combining mattes, masks,

and alpha channels in various ways, (b) modifying alpha channels using dedicated matte controls,

and (c) copying alpha channels into the RGB stream of the image connected to the background

input in preparation for compositing. You can copy specific channels from the foreground input to

the background input to use as an alpha channel, or you can attach masks to the garbage matte

input to use as alpha channels as well.

Understanding Premultiplication

Now that you understand how to direct and recombine RGB images and alpha channels in Fusion,

it’s time to go more deeply into alpha channels to make sure you always combine RGB and alpha

channels correctly for each operation you perform in your composite. This might seem simple, but

small mistakes are easy to make and can result in unsightly artifacts. This is arguably one of the most

confusing areas of visual effects compositing, so don’t skip this section.

When alpha channel and RGB pixels are both contained within a media file, such as a 3D rendered

animation that contains RGB and transparency, or a motion graphics movie file with transparency

baked in, there are two different ways they might be combined, and it’s important to know which

is in use.

�Unpremultipled (Straight): An RGB image unaltered by the semi-transparency information in a

fourth channel (alpha channel)

�Premultiplied: An RGB image that has each channel multiplied by its alpha

channel before compositing.

The term Premultiplied alpha is a term that has historically been used by editors, visual effects

artists, and motion graphics designers, but it’s imprecise. The alpha channel itself is not multiplied.

The R, G, and B channels are multiplied by the alpha. In the end, the alpha channel stays the same, but

the values contained in the R, G, and B channels are modified.

A RGB image (left) and its alpha channel (right)


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

Non-premultiplied images, sometimes called “straight” alpha channels, have RGB channels that are

unaltered (not multiplied) by the alpha channel. The result is that the RGB image has no anti-aliased

edges and no semi-transparency. It’s usually obvious where the RGB image ends and the alpha matte

begins. The image below is an example of the ragged edges seen in the RGB channels when using a

non-premultiplied alpha channel. But notice the smooth semi-transparent edges found in the alpha.

A detailed view of a non-premultiplied RGB image (left) and its alpha channel (right)

A premultiplied alpha channel means the RGB pixels are multiplied by the alpha channel. This method

guarantees that the RGB image pixels include semi-transparency where needed, like anti-aliased

edges. Most computer-generated images are premultiplied for convenience, because they’re easier to

review smoothly without actually being placed inside of a composite.

A detailed view of a premultiplied image (left) and its alpha channel (right)

What does this mean for compositing? The edges of a premultiplied image look much smoother,

making them the preferred choice when compositing foreground over the background in a merge.

Consequently, all alpha channels are made to be premultiplied in compositing operations if they

weren’t already.

On the other hand, it is always preferred to color correct a non-premultiplied RGBA image, because

you don’t want to alter the pixel values of an image after the RGB channels have been multiplied by

the alpha channel.

If you think of this from a mathematical perspective:

�RGB pixel value x 0 = 0: The black transparent areas of an alpha channel have a pixel value

of 0. When you take the value of an RGB pixel and multiply it by 0 (n x 0 = 0) then by the laws of

multiplication, the RGB value becomes 0, or fully transparent.

�RGB Pixel value x 1 = RGB Pixel: The solid or opaque white areas have a value of 1.0. When you

take the value of an RGB pixel and multiply it by 1 (n x 1 = n), then the RGB value stays the same,

fully opaque.


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

�RGB Pixel value x 0.3 = A different color: Along the edges of an alpha channel are gray pixels,

indicating semi-transparency. These semi-transparent pixels have a value falling somewhere

between 1.0 and 0.0. To apply the alpha channel’s anti-aliased edges to the RGB channels, you

multiply the pixel values. The multiplication process mixes some percentage of the transparent

pixels (black) with the RGB pixels. Although this is desired to get good anti-aliased edges, you

can not color correct the image because it alters the smooth semi-transparency you created

once it is done.

RGB pixels are multiplied by varying degrees of

transparency and the result is a different RGB value.

The Rules of Premultiplication

Following from the information presented above, when you’re compositing multiple images together

and one or more has a built-in alpha channel, you want to make sure you follow these general rules to

avoid problems:

�Always use premultiplied images with a Merge node.

�Only color-correct images that are not premultiplied.

�Always filter and transform images that are premultiplied.

�Never double premultiply an image.

Premultiplication and the Merge Node

The foreground input of a Merge node expects a premultiplied RGBA image. It is an additive

merge, meaning the semi-transparent areas of the foreground are added over the background.

However, if the image is not premultiplied, the pixels that should be transparent are still added, which

typically results in an unwanted bright fringe around the edges of your foreground subject.

If you are compositing with a non-premultiplied alpha, you can fix these bright edges by changing the

Merge to perform a Subtractive merge in the Inspector.

Nonpremultiplied edges in an additive Merge (left) and

premultiplied edges in an additive Merge (right)


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

TIP: When an RGB image and a Mask node are combined using, for instance, a Matte

Control node, if the RGB image is not multiplied by the mask in the Matte control, the

checkerboard background pattern in the viewer will appear only semi-transparent when it

should be fully transparent.

Color Correcting Premultiplied RGBA Images

When you premultiply an image, you tie any changes made to the brightness of the RGB pixels to

the alpha channel pixels as well. If, for example, you raise the brightness of the foreground image in

any way, you’ll also raise the brightness of the alpha channel, which will likely not be desirable as this

will change the transparency the alpha channel creates. The visible result of this when viewing the

Merge node is that the entire background will become brighter (or darker if you’d lowered the RGB

brightness) based on your color adjustment.

For this reason, the rule is always to divide the semi-transparent pixels before performing any color

correction on an image with an alpha channel. You can do this turning on the Pre-Divide/Post Multiply

checkbox in any node that performs color correction. Alternatively, you can use the Alpha Divide and

Alpha Multiply nodes to do the same thing. These methods are covered in more detail later in this chapter.

Color correcting a premultiplied foreground incorrectly alters the background (left).

Color correcting a nonpremultiplied foreground works correctly (right).

Double Premultiplied RGBA Means Double Trouble

A common mistake made by many artists is to over-compensate for premultiplication. As important as

it is to premultiply the alpha before compositing in a Merge node, it’s just as important not to double

premultiply the alpha. Performing a premultiply operation two times in a row can create a darken halo

effect around your images. You are effectively multiplying by the gray semi-transparent pixels twice;

this is not optimal.

Double premultiplied image displays dark edges (left);

premultiplied image with correct edges (right)


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

Premultiplied Alpha Channels and Filtering

When dealing with filtering, the state of the RGBA channels shouldn’t matter for most

composites. However, an exception might be if the filter algorithm you choose includes color

modification. For instance, if a filter attempts to simulate a defocus by blooming highlights like

a real light source, that filter might over-brighten pixels near a transparent edge, which will

result in some manner of artifact when that image is composited.