---
title: "Inputs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 451
---

# Inputs

The Custom Tool node has three image inputs, a matte input, and an effect mask input.

Input: The orange, green, and magenta inputs combine 2D images to make your composite. When

entering them into the Custom Tool fields, they are referred to as c1, c2 and c3 (c standard for all three

R, G, B channels)

Matte Input: The white input is for a matte created by polylines, basic primitive shapes, paint strokes,

or bitmaps from other tools. Connecting a matte to this input allows a matte to be combined into any

equation. When entering the matte into the Custom Tool fields, it is referred to as m1.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the Custom Tool effect to

only those pixels within the mask.

Basic Node Setup

The Custom Tool below takes two image inputs and a matte input, and then combines them using

some calculation. The result can be output to a Merge or other image-processing nodes.

A Custom Tool is used to build your own effects using C++ and scripting.

Inspector

The Custom Tool Controls tab


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Controls Tab

Point in 1-4, X and Y

These four controls are 2D X and Y center controls that are available to expressions entered in the

Setup, Intermediate, and Channels tabs as variables p1x, p1y, ...., p4x, p4y. They are normal positional

controls and can be animated or connected to modifiers as any other node might.

Number in 1-8

The values of these controls are available to expressions entered in the Setup, Intermediate, and

Channels tabs as variables n1, n2, n3, ..., n8. They are normal slider controls and can be animated or

connected to modifiers exactly as any other node might.

LUT in 1-4

The Custom Tool node provides 4 LUT splines. The values of these controls are available to

expressions entered in the Setup, Intermediate, and Channels tabs using the getlut# function. For

example, setting the R, G, B, and A expressions to getlut1(r1), getlut2(g1), getlut3(b1), and getlut4(a1),

respectively, would cause the Custom Tool node to mimic the Color Curves node.

These controls can be renamed using the options in the Config tab to make their meanings more

apparent, but expressions still see the values as n1, n2, ..., n8.

The Custom Tool Setup tab

Custom Tool Setup Tab

Setup 1-4

Up to four separate expressions can be calculated in the Setup tab of the Custom Tool node. The Setup

expressions are evaluated once per frame before any other calculations are performed. The results are

then made available to the other expressions in the Custom Tool node as variables s1, s2, s3, and s4.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

NOTE: Because these expressions are evaluated once per frame only and not for each pixel,

it makes no sense to use per-pixel variables like X and Y or channel variables like r1, g1, b1.

Allowable values include constants, variables such as n1..n8, time, W and H, and functions like

sin() or getr1d().

The Custom Tool Intermediate tab

Custom Tool Intermediate Tab

Intermediate 1-4

An additional four expressions can be calculated in the Inter tab. The Inter expressions are evaluated

once per pixel after the Setup expressions are evaluated but before the Channel expressions are

evaluated. Per-pixel channel variables like r1, g1, b1, and a1 are allowable. Results are available as

variables i1, i2, i3, and i4.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

The Custom Tool Config tab

Custom Tool Config Tab

Random Seed

Use this to set the seed for the rand() and rands() functions. Click the Randomize button to set the

seed to a random value. This control may be needed if multiple Custom Tool nodes are required with

different random results for each.

Number Controls

There are eight sets of Number controls, corresponding to the eight Number In sliders in the Controls

tab. Uncheck the Show Number checkbox to hide the corresponding Number In slider, or edit the

Name for Number text field to change its name.

Point Controls

There are four sets of Point controls, corresponding to the four Point In controls in the Controls tab.

Uncheck the Show Point checkbox to hide the corresponding Point In control and its crosshair in the

viewer. Similarly, edit the Name for Point text field to change the control’s name.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

The Custom Tool Channel tab

Custom Tool Channels Tab

RGBA, Z, UV Expressions, and XYZ Normal Expressions

The Channel tab is used to set up one expression per each available channel of the image. Each

expression is evaluated once per pixel. The result creates the value for that pixel in the output of

the image.

Color Channel expressions (RGBA) should generally return floating-point values between 0.0 and 1.0.

Values beyond this are clipped if the destination image is an integer. Other expression fields should

produce values appropriate to their channel (e.g., between -1.0 and 1.0 for Vector and Normal fields,

0.0 to 1.0 for Coverage, or any value for Depth). The Channel expressions may use the results from

both the Setup expressions (as variables s1–s4) and Inter expressions (as variables i1–i4).

Custom Tool Node Syntax

Value Variables

n1..n8

Numeric Inputs

p1x..p4x

Position Values (X-axis)

p1y..p4y

Position Values (Y-axis)

s1..s4

Setup  Expression Results

i1..i4

Inter  Expression Results

time

Current Frame

x

Horizontal co-ordinate of the current pixel, between 0.0 and  1.0

y

Vertical co-ordinate of the current pixel, between 0.0 and 1.0

w (or w1..w3)

Width of Image (for image1..image3)

h (or h1..h3)

Height of Image (for image1..image3)


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Value Variables

ax (or ax1..ax3)

Image Aspect X (for image1..image3)

ay (or ay1..ay3)

Image Aspect Y (for image1..image3)

NOTE: Use w and h and ax and ay without a following number to get the dimensions and

aspect of the primary image.

Channel (Pixel) Variables

c1..c3

Current Channel (for image1..image3)

r1..r3

Red (for image1..image3)

g1..g3

Green (for image1..image3)

b1..b3

Blue (for image1..image3)

a1..a3

Alpha (for image1..image3)

z1..z3

Z-Buffer (for image1..image3)

cv1..cv3

Z Coverage (for image1..image3)

u1..u3

U Coordinate (for image1..image3)

v1..v3 nx1..nx3

V Coordinate (for image1..image3) X Normal (for image1..image3)

ny1..ny3

Y Normal (for image1..image3)

nz1..nz3

Z Normal (for image1..image3)

bgr1..bgr3

Background Red (for image1..image3)

bgg1..bgg3

Background Green (for image1..image3)

bgb1..bgb3

Background Blue (for image1..image3)

bga1..bga3

Background Alpha (for image1..image3)

vx1..vx3

X Vector (for image1..image3)

vy1..vy3

Y Vector (for image1..image3)

nz1..nz3

Z Normal (for image1..image3)

NOTE: Use c1, c2, c3 to refer to the value of a pixel in the current channel. This makes

copying and pasting expressions easier. For example, if c1/2 is typed as the red expression,

the result would be half the value of the red pixel from image 1, but if the expression is copied

to the blue channel, now it would have the value of the pixel from the blue channel.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

To refer to the red value of the current pixel in input 1, type r1. For the image in input 2, it

would be r2.

•	 get[ch][#]b(x, y) Read pixel at x,y, or 0 if out of bounds—e.g., getr1b(0,0)

•	 get[ch][#]d(x, y) Read pixel at x,y or edge pixel if out of bounds—e.g., getr1d(0,0)

•	 get[ch][#]w(x, y) Read pixel at x,y or wrap if out of bounds—e.g., getr1w(0,0)

NOTE: There are a variety of methods used to refer to pixels from locations other than the

current one in an image.

In the above description, [ch] is a letter representing the channel to access. The [#] is a number

representing the input image. So to get the red component of the current pixel (equivalent to

r), you would use getr1b(x,y). To get the alpha component of the pixel at the center of image 2,

you would use geta2b(0.5, 0.5).

•	 getr1b(x,y) Output the red value of the pixel at position x, y, if there were a valid pixel

present. It would output 0.0 if the position were beyond the boundaries of the image (all

channels).

•	 getr1d(x,y) Output the red value of the pixel at position x, y. If the position specified

were outside of the boundaries of the image, the result would be from the outer edge of the

image (RGBA only).

•	 getr1w(x,y) Output the red value of the pixel at position x, y. If the position specified were

outside of the boundaries of the image, the x and y coordinates would wrap around to the

other side of the image and continue from there (RGBA only).

To access other channel values with these functions, substitute the r in the above examples with

the correct channel variable (r, g, b, a and, for the getr1b() functions only, z, and so on), as shown

above. Substitute the 1 with either 2 or 3 in the above examples to access the images from the other

image inputs.

Mathematical Expressions

pi

The value of pi

e

The value of e

log(x)

The base-10 log of x

ln(x)

The natural (base-e) log of x

sin(x)

The sine of x (x is degrees)

cos(x)

The cosine of x (x is degrees)

tan(x)

The tangent of x (x is degrees)

asin(x)

The arcsine of x, in degrees


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Mathematical Expressions

acos(x)

The arccosine of x, in degrees

atan(x)

The arctangent of x, in degrees

atan2(x,y)

The arctangent of x,y, in degrees

abs(x)

The absolute (positive) value of x

int(x)

The integer (whole) value of x

frac(x)

The fractional value of x

sqrt(x)

The Square Root of x

rand(x,y)

A random value between x and y

rands(x,y,s)

A random value between x and y, based on seed s

min(x,y)

The minimum (lowest) of x and y

max(x,y)

The maximum (highest) of x and y

dist(x1,y1,x2,y2)

The distance between point x1,y2 and x2,y2

dist3d(x1,y1,z1,x2,y2,z2)

The distance between 3D points x1,y2,z1 and  x2,y2,z2

noise(x)

A smoothly varying Perlin noise value based on  x

noise2(x, y)

A smoothly varying Perlin noise value based on x and  y

noise3(x, y, z)

A smoothly varying Perlin noise value based on x, y and  z

if(c, x, y)

returns x if c not 0, otherwise y

Mathematical Operators

!x

1.0 if x = 0, otherwise 0.0

-x

(0.0 - x)

+x

(0.0 + x) i.e. effectively does nothing

x ^ y

x raised to the power of y

x * y

x multiplied by y

x / y

x divided by y

x % y

x modulo y, i.e. remainder of (x divided by y)

x + y

x plus y

x - y

x minus y

x < y

1.0 if x is less than y, otherwise 0.0

x > y

1.0 if x is greater than y, otherwise 0.0


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Mathematical Operators

x <= y

1.0 if x is less than or equal to y, otherwise 0.0

x >= y

1.0 if x is greater than or equal to y, otherwise 0.0

x = y

1.0 if x is exactly equal to y, otherwise  0.0

x == y

1.0 if x is exactly equal to y, otherwise 0.0, identical to above

x <> y

1.0 if x is not equal to y, otherwise 0.0

x != y

1.0 if x is not equal to y, otherwise 0.0, i.e. identical to  above

x & y

1.0 if both x and y are not 0.0, otherwise 0.0

x && y

1.0 if both x and y are not 0.0, otherwise 0.0, i.e. identical to  above

x|y

1.0 if either x or y (or both) are not 0.0, otherwise 0.0

x||y

1.0 if either x or y (or both) are not 0.0, otherwise 0.0