---
title: "Examples"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 452
---

# Examples

The following examples are intended to help you understand the various components of the Custom

Tool node.

Rotation

To rotate an image, we need the standard equations for 2D rotation:

x’ = x * cos(theta) - y * sin(theta) y’ = x * sin(theta) + y *

cos(theta)

Using the n1 slider for the angle theta, and a sample function, we get (for the red channel):

getr1b(x * cos(n1) - y * sin(n1), x * sin(n1) + y * cos(n1))

This calculates the current pixel’s (x,y) position rotated around the origin at (0,0) (the bottom-

left corner), and then fetches the red component from the source pixel at this rotated position.

For centered rotation, we need to subtract 0.5 from our x and y coordinates before we rotate

them, and add 0.5 back to them afterward:

getr1b((x-.5) * cos(n1) - (y-.5) * sin(n1) + .5, (x-.5) * sin(n1) + (y-.5)

* cos(n1) + .5)

Which brings us to the next lesson: Setup and Intermediate Expressions. These are useful for

speeding things up by minimizing the work that gets done in the Channel expressions. The

Setup expressions are executed only once, and their results don‘t change for any pixel, so you

can use these for s1 and s2, respectively.

cos(n1) sin(n1)

Intermediate expressions are executed once for each pixel, so you can use these for i1 and i2:

(x-.5) * s1 - (y-.5) * s2 + .5

(x-.5) * s2 + (y-.5) * s1 + .5


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

These are the x and y parameters for the getr1b() function from above, but with the Setup

results, s1 and s2, substituted so that the trig functions are executed only once per frame, not

every pixel. Now you can use these intermediate results in your Channel expressions:

getr1b(i1, i2)

getg1b(i1, i2)

getb1b(i1, i2)

geta1b(i1, i2)

With the Intermediate expressions substituted in, we only have to do all the additions,

subtractions, and multiplications once per pixel, instead of four times. As a rule of thumb, if it

doesn‘t change, do it only once.

This is a simple rotation that doesn’t take into account the image aspect at all. It is left as an

exercise for you to include this (sorry). Another improvement could be to allow rotation around

points other than the center.

Filtering

Our second example duplicates the functionality of a 3 x 3 Custom Filter node set to average

the current pixel together with the eight pixels surrounding it. To duplicate it with a Custom

Tool node, add a Custom Tool node to the node tree, and enter the following expressions into

the Setup tab.

(Leave the node disconnected to prevent it from updating until we are ready.)

S1

1.0/w1

S2

1.0/h1

These two expressions are evaluated at the beginning of each frame. S1 divides 1.0 by the

current width of the frame, and S2 divides 1.0 by the height. This provides a floating-point

value between 0.0 and 1.0 that represents the distance from the current pixel to the next pixel

along each axis.

Now enter the following expression into the first text control of the Channel tab (r).

(getr1w(x-s1, y-s2) + getr1w(x, y-s2) + getr1w(x+s1, y-s2) + getr1w(x+s1,

y) + getr1w(x-s1, y) + r1 +getr1w(x-s1, y+s2) + getr1w(x, y+s2) +

getr1w(x+s1, y+s2)) / 9

This expression adds together the nine pixels above the current pixel by calling the getr1w()

function nine times and providing it with values relative to the current position. Note that we

referred to the pixels by using x+s1, y+s2, rather than using x+1, y+1.

Fusion refers to pixels as floating-point values between 0.0 and 1.0, which is why we created

the expressions we used in the Setup tab. If we had used x+1, y+1 instead, the expression

would have sampled the same pixel over and over again. (The function we used wraps the

pixel position around the image if the offset values are out of range.)

That took care of the red channel; now use the following expressions for the green, blue, and

alpha channels.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

(getg1w(x-s1, y-s2) + getg1w(x, y-s2) + getg1w(x+s1, y-s2) + getg1w(x+s1,

y) + getg1w(x-s1, y) + g1 +getg1w(x-s1, y+s2) + getg1w(x, y+s2) +

getg1w(x+s1, y+s2)) / 9

(getb1w(x-s1, y-s2) + getb1w(x, y-s2) + getb1w(x+s1, y-s2) + getb1w(x+s1,

y) + getb1w(x-s1, y) + b1 +getb1w(x-s1, y+s2) + getb1w(x, y+s2) +

getb1w(x+s1, y+s2)) / 9

(geta1w(x-s1, y-s2) + geta1w(x, y-s2) + geta1w(x+s1, y-s2) + geta1w(x+s1,

y) + geta1w(x-s1, y) + a1 + geta1w(x-s1, y+s2) + geta1w(x, y+s2) +

geta1w(x+s1, y+s2)) / 9

It’s time to view the results. Add a Background node set to a solid color and change the color

to a pure red. Add a hard-edged Rectangular effects mask and connect it to the expression

just created.

For comparison, add a Custom Filter node and duplicate the settings from the image above.

Connect a pipe to this node from the background to the node and view the results. Alternate

between viewing the Custom Tool node and the Custom Filter while zoomed in close to the

top corners of the effects mask.

Of course, the Custom Filter node renders a lot faster than the Custom Tool node we created,

but the flexibility of the Custom Tool node is its primary advantage. For example, you could

use an image connected to input 2 to control the median applied to input one by changing all

instances of getr1w, getg1w, and getb1w in the expression to getr2w, getg2w, and getb2w, but

leaving the r1, g1, and b1s as they are.

This is just one example; the possibilities of the Custom Tool node are limitless.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other miscellaneous nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Fields [FLDs]

The Fields node

Fields Node Introduction

The Fields node is a robust multipurpose utility offering several functions related to interlaced video

frames. It interpolates video fields into frames or video frames into fields. Although the interlace

preference and method type is defined in the MediaIn or Loader, and generators, this node can be

used to assist in the standards conversion of PAL to NTSC and provides the ability to process fields

and frames for specific portions of a node tree.

This node can also interlace two separate images together into a single interlace image.

The background input is the dominate field 1 and the foreground is field 2.

Inputs

The single input on the Fields node is used to connect a 2D image and an effect mask, which can be

used to limit the blurred area.

Stream1 Input: The orange background input is used for the primary 2D image that is

interpolated or converted.

Stream2 Input: The optional green foreground input is only used when merging two

interlaced images together.

Basic Node Setup

The Fields node below is used to convert the background image from a PAL interlaced format to

progressive frames.

The background image can be modified to various interlaced formats.

Inspector

The Fields Controls tab


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Controls Tab

The Controls tab includes two menus. The Operation menu is used to select the type of field

conversion performed. The Process Mode menu is used to select the field’s format for the

output image.

Operatiion Controls

Operation Menu

�Do Nothing: This causes the images to be affected by the Process Mode selection exclusively.

�Strip Field 2: This removes field 2 from the input image stream, which shortens the image to half

of the original height.

�Strip Field 1: This removes field 1 from the input image stream, which shortens the image to half of

the original height.

�Strip Field 2 and Interpolate: This removes field 2 from the input image stream and inserts a

field interpolated from field 1 so that image height is maintained. Should be supplied with frames,

not fields.

�Strip Field 1 and Interpolate: This removes field 1 from the input image stream and inserts a

field interpolated from field 2 so that image height is maintained. Should be supplied with frames,

not fields.

�Interlace: This combines fields from the input image stream(s). If supplied with one image

stream, each pair of frames are combined to form half of the number of double-height frames.

If supplied with two image streams, single frames from each stream are combined to form

double-height images.

�De-Interlace: This separates fields from one input image stream. This will produce double the

amount of half-height frames.

Reverse Field Dominance

When selected, the Field Order or Dominance of the image will be swapped.

Process Mode


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Process Mode Menu

�Full Frames: This forces Frame Processing. Useful for processing frames in a part of a node tree

that is otherwise field processing.

�NTSC Fields: This forces NTSC Field Processing. Useful for processing fields in a part of a node

tree that is otherwise frame processing.

�PAL Fields: This forces PAL Field Processing. Useful for processing fields in a part of a node tree

that is otherwise frame processing.

�PAL Fields (Reversed): This forces PAL-swapped Field Processing.

�NTSC Fields (Reversed): This forces NTSC-swapped Field Processing.

�Auto: This attempts to match the mode of its input images. Fields are used if the input

types are mixed.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other miscellaneous nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.