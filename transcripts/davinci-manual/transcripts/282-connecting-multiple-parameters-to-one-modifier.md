---
title: "Connecting Multiple Parameters to One Modifier"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 282
---

# Connecting Multiple Parameters to One Modifier

A single modifier or published parameter can be applied to multiple parameters so they all act as one.

This is handled through the Connect To submenu. As with modifier assignment, the list is filtered to

show only options that are suitable for the parameter you’ve right-clicked on. When you do this, the

connection is bidirectional; editing either parameter will cause the other parameter to change.

The Connect To menu connects

modifiers to multiple parameters

Adding and Inserting Multiple Modifiers

Modifiers can be connected to each other and branched, just like nodes in the Node Editor. For

example, the Calculation modifier outputs a number, but has two Number parameters, both of which

can have modifiers added to them. If you want to insert a modifier between the existing modifier and

the modified parameter, use the Insert submenu of the parameter’s contextual menu.

Available Modifiers in Fusion:

�Anim Curves: Adds an animation curves modifier that allows you to dynamically adjust the timing,

scaling, and acceleration of an animation.

�Bézier Spline: Adds a Bézier spline to the Spline Editor for animating the selected parameter.

�B-Spline Spline: Adds a B-Spline spline to the Spline Editor for animating the selected parameter.

�Calculation: Creates an indirect link that includes a mathematical expression

between two parameters.


Fusion Fundamentals | Chapter 74 Using Modifiers, Expressions, and Custom Controls

FUSION

�CoordTransform Position: Calculates the current 3D position of a given object even after multiple

3D transforms have repositioned the object through the node tree hierarchy.

�Cubic Spline: Adds a Cubic spline to the Spline Editor for animating the selected parameter.

�Expression: Allows you to add a variable or a mathematical calculation to a parameter, rather than

a straight numeric value. The Expression modifier provides controls in the Modifiers tab, giving

you more room and parameters than the SimpleExpression

�From Image: This modifier takes color samples of an image along a user-definable line and

creates a gradient from those samples.

�Gradient Color Modifier: Creates a customized gradient and maps it into a specified time range to

animate a value.

�KeyStretcher: Used to stretch keyframes in a Fusion Title template when trimming the template in

the Edit page or Cut page timeline.

�MIDI Extractor: Modifies the value of a parameter using the values stored in a MIDI file.

�Natural Cubic Spline: Adds a Natural Cubic spline to the Spline Editor for animating

the selected parameter.

�Offset (Angle, Distance, Position): The three Offset modifiers are used to create variances,

or offsets, between two positional values. For instance, when this modifier is added to a size

parameter, you can change the size of an object using the distance between two onscreen

controls (position and offset).

�Path: Produces two splines to control the animation of of an object: An onscreen motion path

(spacial) and a Time spline visible in the Spline Editor (temporal).

�Perturb: Generates smoothly varying random animation for a given parameter.

�Probe: Auto-animates a parameter by sampling the color or luminosity of a specific pixel or

rectangular region of an image.

�Publish: The first step in linking two non-animated parameters is to use the Publish modifier to

publish a parameter. That allows other parameters to use the Connect To submenu and link to the

published parameter.

�Resolve Parameter: Allows you to modify the duration of a Fusion transition template from the Edit

page Timeline. The Resolve Parameter Modifier is applied to any animated parameter instead of

keyframing the transition.

�Shake: Similar to Perturb, Shake generates smoothly varying random animation

for a given parameter.

�Track: Attaches a single point tracker to the selected parameter. The tracker can then track an

object onscreen to animate the parameter. This is quicker and more direct than using the normal

Tracker node; however, it offers less flexibility since the resulting tracker is only a single point and

can only be used for the selected parameter.

�Vector Result: Similar to the Offset modifier, Vector Result is used to offset position parameters

using origin, distance, and angle controls to create a vector. This vector can then be used to adjust

any other parameter.

�XY Path: Produces an X and Y spline in the Spline Editor to animate the position of an object..

For more information on all modifiers available in Fusion, see Chapter 124, “Modifiers,” in the

DaVinci Resolve Reference Manual and Chapter 64 in the Fusion Reference Manual.


Fusion Fundamentals | Chapter 74 Using Modifiers, Expressions, and Custom Controls

FUSION

Performing Calculations in Parameter Fields

You can enter simple mathematical equations directly in a number field to calculate a desired

value. For example, typing 2.0 + 4.0 in most number fields will result in a value of 6.0. This can

be helpful when you want a parameter to be the sum of two other parameters or a fraction of the

screen resolution.

Using SimpleExpressions

Simple Expressions are a special type of script that can be placed alongside the parameter it is

controlling. These are useful for setting simple calculations, building unidirectional parameter

connections, or a combination of both. You add a SimpleExpression by entering an equals sign directly

in the number field of the parameter and then pressing Return.

Entering an equals sign opens the SimpleExpression

field with Pick Whip control

An empty field will appear below the parameter, and a yellow indicator will appear to the left. The

current value of the parameter will be entered into the number field. Using Simple Expressions, you

can enter a mathematical formula that drives the value of a parameter or even links two different

parameters. This helps when you want to create an animation that is too difficult or impossible to set

up with keyframing. For instance, to create a pulsating object, you can use the sine and time functions

on a Size parameter. Dividing the time function can slow down the pulsing while multiplying it can

increase the rate.

A SimpleExpression using the sine and time functions

Inside the SimpleExpression text box, you can enter one-line scripts in Lua with some Fusion-specific

shorthand. Some examples of Simple Expressions and their syntax include:

Expression

Description

time

This returns the current frame number.

Merge1.Blend

This returns the value of another input, Blend, from

another node, Merge1.

Merge1:GetValue("Blend", time-5)

This returns the value from another input, but

sampled at a different frame, in this case five

frames before the current one.

sin(time/20)/2+.5

This returns a sine wave between 0 and 1.


Fusion Fundamentals | Chapter 74 Using Modifiers, Expressions, and Custom Controls

FUSION

Expression

Description

iif(Merge1.Blend == 0, 0, 1)

This returns 0 if the Blend value is 0, and returns

1 if it is not. The iff() function is a shorthand

conditional statement, if-then-else.

iif(Input.Metadata.ColorSpaceID ==

"sRGB", 0, 1)

This returns 0 if the image connected to the

current node’s Input is tagged with the sRGB

colorspace. When no other node name is supplied,

the expression assumes the Input is coming from

the current node. It is equivalent to self.Input.

The Input in most, but not all, Fusion nodes is the

main image input shown in the Node Editor as

an orange triangle. Images have members that

you can read, such as Depth, Width, Metadata,

and so on.

Point(Text1.Center.X, Text1.

Center.Y-.1)

Unlike the previous examples, this returns a Point,

not a Number. Point inputs use two members, X

and Y. In this example, the Point returned is 1/10

of the image height below the Text1’s Center. This

can be useful for making unidirectional parameter

links, like offsetting one Text from another.

Text1.Center - Point(0,.1)

This is similar to the previous expression.

This SimpleExpression returns Text instead of a

Number or Point.

Text("Colorspace: "..(Merge1.

Background.Metadata.ColorSpaceID)

The string inside the quotes is concatenated with

the metadata string, perhaps returning:

Colorspace: sRGB

Text("Rendered "..os.date("%b %d,

%Y").. " at "..os.date("%H:%M").."\n

on the computer "..os.

getenv("COMPUTERNAME").. " running

"..os. getenv("OS").."\n from the comp

"..ToUNC(comp.Filename))

This returns a much larger Text, perhaps

something like:

Rendered Nov 12, 2019 at 15:43 on the computer

Rn309 running Windows_NT from the comp \\

SRVR\Proj\Am109\SlateGenerator_A01.comp

os.date("%H:%M")

The OS library can pull various information about

the computer. In the previous example, os.date

gets the date and time in hours:minutes.

"..os.getenv("COMPUTERNAME").. "

running "..os.

Any environment variable can be read by

os.getenv, in this case the computer name and the

operating system.

"\n from the comp

"..ToUNC(comp.Filename)

To get a new line in the Text, \n is used. Various

attributes from the comp can be accessed with

the comp variable, like the filename, expressed as

a UNC path.


Fusion Fundamentals | Chapter 74 Using Modifiers, Expressions, and Custom Controls

FUSION

TIP: When working with long SimpleExpressions, it may be helpful to drag the Inspector

panel out to make it wider or to copy/paste from a text editor or the Console.

After setting an expression that generates animation, you can open the Spline Editor to view the

values plotted out over time. This is a good way to check how your SimpleExpression evaluates

over time.

A sine wave in the Spline Editor, generated by the expression used for Text1: Size

For more information about writing Simple Expressions, see the Fusion Studio Scripting Guide, and the

official Lua documentation.

Pick Whipping to Create an Expression

With a SimpleExpression field open, a + button is displayed on the left side. Dragging the + button

onto another control, or "pick whipping," links the two parameters, similar to the Connect To menu.

However, unlike a Connect To parameter link, the pick whip allows you to modify the connection by

further editing the expression.

Pick whipping to connect one parameter to another quickly

SimpleExpressions can also be created and edited within the Spline Editor. Right-click on the

parameter in the Spline Editor and select Set SimpleExpression from the contextual menu. The

SimpleExpression will be plotted in the Spline Editor, allowing you to see the result over time.

Removing SimpleExpressions

To remove a SimpleExpression, right-click the name of the parameter, and choose Remove Expression

from the contextual menu.


Fusion Fundamentals | Chapter 74 Using Modifiers, Expressions, and Custom Controls

FUSION