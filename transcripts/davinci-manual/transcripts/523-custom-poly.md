---
title: "Custom Poly"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 523
---

# Custom Poly

The Custom Poly modifier can be added to Polygon masks or paths. Similar in function to the Custom

and pCustom tools, existing points can be repositioned in the polyline, or replaced completely with a

new set of points. The expressions are evaluated for each point on the output polygon. The modifier

can be applied by right-clicking on the “Right-click here for shape animation” text at the bottom of the

Polygon controls, and selecting Insert > Custom Poly from the contextual menu.

Selecting the Custom Poly modifier

Inspector

The Custom Poly Controls tab


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Controls Tab

The Custom Poly Controls tab are available once you select the modifiers tab on the Polygon’s

inspector. It has a single point input, and number variables to use in animating the expressions.

The default is one point and four numbers, but they can be expanded to a maximum of nine. Additional

points and numbers can be added from the Config tab.

The Custom Poly Polyline tab

Polyline Tab

The polyline tab exposes the controls to connect and modify the polyline.

Connect Source Polyline here

Allows you to connect other polylines to the modifier.

Show View Controls

This checkbox toggles the polyline controls visibility in the viewer.

Number of Points

The number of output points can be set, controlling the amount of custom subdivision of the polyline.

A value of zero uses the number of original source points.

Poly Expression X/Y

Fields for entering the mathematical expressions. For example, px*(1-n1)+n1*get2x(disp) and py*(1-n1)+

n1*get2y(disp).

It uses most of the same expression variables as the Expression modifier below (i.e., n1..n9, p1x..p9x,

p1y..p9y, math functions, etc.), and it adds:

�px,py for the current point on the source polygon

�disp for the point’s displacement on the polyline (0.0 is start, 1.0 is end)

�index for the current point’s index (zero-based)

�num for the number of output points

�getx(disp), gety(disp) to get values from anywhere on the polyline

�getx_at(disp, time), gety_at(disp, time) to get values from polylines at other times

�Similarly, get2x/y(), get3x/y(), get2x/y_at(), get3x/y_at() for the second and third source polys


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Config Tab

The config tab allows you to select the amount of Points and Numbers shown in the modifier (to a

maximum of 9), and to give them custom names for easier organization.

Expression

An expression is a variable or a mathematical calculation added to a parameter, rather than a straight

numeric value. You can add an expression to any parameter in Fusion, or you can add the Expression

modifier, which adds several tabs to the modifier Inspector. Adding this modifier to a parameter adds

the ability to manipulate that parameter based on any number of controls, either positional or value-

based. This modifier offers exceptional flexibility compared to the more limited Calculation or Offset

modifiers, but it is unable to access values from frames other than the current time.

The Expression modifier accepts nine value inputs and nine position inputs that are used as part of a

user-defined mathematical expression to output a value.

To add the Expression modifier to a parameter, right-click the parameter in the Inspector and choose

Modify With > Expression from the contextual menu. The type of value returned by the Expression

depends entirely on the type of control it is modifying.

When used with a value control (like a slider), the Expression in the Number Out tab is evaluated to

create the result. When used to modify a positional control (like Center), the Point Out tab controls

the result.

The Inspector’s Modifiers tab contains the controls for the Expression modifier, described below.

Inspector

Expressions modifier controls


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Controls Tab

This tab provides nine number controls and nine point controls. The values of the number controls

can be referred to in an expression as n1 through n9. The X-coordinate of each point control can be

referred to as p1x through p9x, while the Y-coordinate is p1y through p9y.

These values can be set manually, connected to other parameters, animated, and even connected to

other Expressions or Calculations.

The Number Out tab

Number Out Tab

Mathematical formulas are entered using the Number In and Point In values from the Controls tab.

The output modifies the control in which the Expression was applied. See below for the syntax to use

in this field.

The Point Out tab

Point Out Tab

The two text boxes in this tab use mathematical formulas, accessing the Number In and Point In values

from the Controls tab. The output value modifies the control in which the Expression was applied. The

Expression in the top text box control is used to calculate the X-axis value, and the bottom text box is

used to calculate the Y-axis control. See below for the syntax to use in this field.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

The Expressions modifier Config tab

Config Tab

A good expression is reused over and over again. As a result, it can be useful to provide more

descriptive names for each parameter or control and to hide the unused ones. The Config Tab

of the Expressions modifier can customize the visibility and name for each of the nine point and

number controls.

Random Seed

The Random Seed control sets the starting number for the Rand() function. The rand(x, y) function

produces a random value between X and Y, producing a new value for every frame. As long as the

setting of this Random Seed slider remains the same, the values produced at frame x are always the

same. Adjust the Seed slider to a new value to get a different value for that frame.

Show Number or Point X

There are eighteen of these checkbox controls, one for each of the nine Number and nine Point

inputs. Enable this checkbox to display the control for Number x or Point x in the Controls tab.

Name for Number or Point X

There are eighteen of these edit controls, one for each of the nine Number and nine Point inputs.

Type a new name for the input into this edit control to assign a new name for the Input’s label in the

Controls tab.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Expression Syntax Formulas

Formulas are entered into the Number Out or Point Out tabs as part of an expression. They can be

made up of the following functions:

n1...n9

The value of Number Input 1..9.

p1x...p9x

The X of Positional Control 1..9.

p1y...p9y

The Y of Positional Control 1..9.

time

The current time (frame number).

pi

The value of pi.

e

The value of e.

log(x)

The base-10 log of x.

ln(x)

The natural (base-e) log of x.

sin(x)

The sine of x (x is degrees).

cos(x)

The cosine of x (x is degrees).

tan(x)

The tangent of x (x is degrees).

asin(x)

The arcsine of x, in degrees.

acos(x)

The arccosine of x, in degrees.

atan(x)

The arctangent of x, in degrees.

atan2(x, y)

The arctangent of x,y, in degrees.

abs(x)

The absolute (positive) value of x.

int(x)

The integer (whole) value of x.

frac(x)

The fractional value of x.

sqrt(x)

The Square Root of x.

rand(x, y)

A random value between x and y.

rands(x, y, s)

A random value between x and y, based on seed s.

min(x, y)

The minimum (lowest) of x and y.

max(x, y)

The maximum (highest) of x and y.

dist(x1, y1, x2, y2)

The distance between point x1,y2 and x2,y2.

dist3d(x1,y1,z1,x2,y2,z2)

The distance between 3D points x1,y2,z1 and x2,y2,z2

noise(x)

A smoothly varying Perlin noise value based on x

noise2(x, y)

A smoothly varying Perlin noise value based on x and y

noise3(x, y, z)

A smoothly varying Perlin noise value based on x, y and z

if(c, x, y)

Returns x if c not 0, otherwise y.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Expression Syntax Operators

Operators are used to evaluate statements. They are combined with functions to perform logical and

mathematical calculations in the Number Out and Point Out tabs.

x + y

x plus y.

x - y

x minus y.

x > = y

1.0 if x is less than y, otherwise 0.0.

x > y

1.0 if x is greater than y, otherwise 0.0.

!x

1.0 if x = 0, otherwise 0.0.

-x

(0.0 - x).

+x

(0.0 + x) (effectively does nothing).

x ^ y

x raised to the power of y.

x y

x multiplied by y.

x y

x divided by y.

x % y

x modulo y, (remainder of (x divided by y)).

x > = y

1.0 if x is less than or equal to y, otherwise 0.0.

x > = y

1.0 if x is greater than or equal to y, otherwise 0.0.

x = y

1.0 if x is exactly equal to y, otherwise 0.0.

x == y

1.0 if x is exactly equal to y, otherwise 0.0 (identical to above).

x < > y

1.0 if x is not equal to y, otherwise 0.0.

x != y

1.0 if x is not equal to y, otherwise 0.0 (identical to above).

x & y

1.0 if both x and y are not 0.0, otherwise 0.0.

x && y

1.0 if both x and y are not 0.0, otherwise 0.0 (identical to above).

x | y

1.0 if either x or y (or both) are not 0.0, otherwise 0.0.

x || y

1.0 if either x or y (or both) are not 0.0, otherwise 0.0 (identical to above).

Example 1

To make a numeric control equal to the Y value of a motion path, add an expression to the

desired target control and connect the Path to Point In 1. Enter the formula:

p1y

into the Number Out field.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Example 2

To make the result of the Expression’s Number Out be the largest of Number In 1 and Number

In 2, multiplied by the cosine of Number In 3, plus the X coordinate of Point In 1, enter

the formula:

max(n1, n2) * cos(n3) + p1x

into the Number Out field.

Example 3

Add a Background node set to solid black and a Hotspot node. Set the Hotspot size to 0.08

and set the Strength to maximum. Modify the Hotspot center with an expression. Change the

current frame to 0.

Set n1 to 0.0 and add a Bézier Spline. At frame 29, set the value of n1 to 1.0. Select both points

and loop the spline using the Spline Editor. Now enter the following equations into the Point

Out tab of the expression.

X-Axis Expression

n1

Y-Axis Expression

0.5 + sin(time*50) 4

Render out a preview and look at the results. (Try this one with motion blur.)