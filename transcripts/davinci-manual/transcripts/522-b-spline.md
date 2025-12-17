---
title: "B-Spline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 522
---

# B-Spline

An alternative to the Bézier Spline, B-spline is another animation modifier in Fusion and is typically

applied to numerical values rather than point values. It is applied by right-clicking a parameter and

selecting Modify With > B-Spline.

Usage

B-Spline Editor

�This animation spline modifier has no actual Controls tab. However, the Spline Editor displays

the B-spline, and it can be controlled there. Notice that, though the actual value of the second

keyframe is 0, the value of the resulting spline is 0.33 due to the unique smoothing and weighing

algorithms of a B-spline.

�The weight can be modified by clicking the control point to select it, holding the W key, and

moving the mouse left and right to lower or increase the tension. This is also done with multiple

selected control points simultaneously.

Calculation

Calculations are used to create indirect connections between parameters. A Calculation can perform a

mathematical expression based on two operands, where each operand can be connected to another

parameter or set manually.

Additionally, using Time offsets and Scale controls in the Time tab, the Calculation control can access

values of a parameter at times other than the current time.

The Calculation’s most common use is for connecting two parameters when one value range or scope

is inappropriate for the other parameter.

NOTE: The Expression modifier is essentially a more flexible version of the Calculation

modifier, with a single exception. It is far easier to manipulate the timing of the operands

provided in the Calculation modifier than it is to do so with an Expression.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Inspector

Calculation Calc tab

Calc Tab

The Calc tab includes two dials used for the connected parameter and value that gets mathematically

combined. The Operator menu selects how the Second Operand value combines with the

parameter’s value.

First and Second Operand

These sliders are connected to published or animated parameters or manually set to the desired

values for the calculation.

Operator

Select from the mathematical operations listed in this menu to determine how the two operands are

combined. Clicking the drop-down arrow opens the menu with the following options:

�Add

�Subtract (First - Second)

�Multiply

�Divide (First / Second)

�Divide (Second / First)

�Subtract (Second - First)

�Minimum

�Maximum

�Average

�First only

Calculation Time tab

Time Tab

The Time tab is used to modify the time of the Calculation modifier. The controls here retime the

speed of the effect or offset it in time.

First and Second Operand Time Scale

These sliders multiply the frame number and return the value of the operands at the multiplied frame

number. A value of 1 returns the value of the operand at frame x when the composition is on frame x.

For example, if the first operand is animated with a value of 1 to 50 from frame 0 to 10, then a scale of

0.5 would cause the calculation to return a value of 25 at frame 10 (effectively slowing the animation by

half for the purposes of the calculation).


Fusion Page Effects | Chapter 124 Modifiers

FUSION

First Operand and Second Operand Time Offset

These sliders return the value of the operand at the Time Offset specified. A value of 10 would return

the value of the operand 10 frames forward in time, and -10 would return the value of the operand 10

frames back in time. See the example below for a practical example.

Example

The following example uses a calculation to apply blur to a Text node in inverse proportion to

the size of the text.

•	 Open a new composition that starts on frame 0 and ends on frame 100.

•	 At frame 0, add a Text+ node to the composition.

•	 Enter a small amount of text and set the size to 0.05

•	 Click the Keyframe button to the right of the Size slider to add a keyframe.

•	 Move to frame 100 and set the Size value to 0.50.

•	 Connect a Blur node after the Text+ node.

•	 View the Blur node in one of the viewers.

To have the blur decrease in strength as the text gets bigger, a simple “pick whip”-style

parameter linking does not work. The controls cannot be directly connected together

because the values of the Text Size control are getting bigger instead of smaller.

•	 Right-click the Blur Size and select Modify With > Calculation from the contextual menu.

This adds a Calculation modifier to the Blur node. At the top of the Inspector, a new set of

controls appears in the Modifiers tab while the Blur node is selected.

•	 At the top of the Inspector, select the Modifiers tab (F11).

•	 Right-click the First Operand slider and select Connect To > Text 1 > Size from the

contextual menu.

Although the Blur Size is now connected to the Text Size parameter, this connection isn’t

very useful. The maximum value of the Blur Size control is 0.5, which is hardly noticeable

as a blur.

•	 Set the Operator drop-down menu to Multiply.

•	 Set the Second Operand slider to 100.

•	 Now the first operand is multiplied by 100, and adjusting the dial gives you a much

blurrier blur.

•	 Switch to the Time tab of the modifier and set the First Operand Time Scale to -1.0.

Normally, the first operand gets the value of the control it is connected to from the same

frame as the current time. So at frame 10, the first operand is set to the same value as the

Text size at frame 10. By setting this value to -1, the value is read from one frame back in time

whenever the current time of the composition advances by 1 frame.

However, this means that the Calculation would be reading the value of the Text size at

frame -10 when we are at frame 10 in the composition.

•	 To correct for this, set the First Operand Time Offset slider to 100.

•	 Return to the Tools tab at the top of the Inspector and press Play (Spacebar) to watch how

the value of the Blur Size relates to the value of the Text Size.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

CoordTransform Position

Because of the hierarchical nature of 3D in Fusion, the original position of an object in a 3D scene

often fails to indicate the current position of the object. For example, an image plane might initially

have a position at 1, 2, 1, but then be scaled, offset, and rotated by other tools further downstream

in the node tree, ending up with an absolute location of 10, 20, 5. This can complicate connecting

an object further downstream in the composition directly to the position of an upstream object. The

Coordinate Transform modifier can be added to any set of the XYZ coordinate controls to calculate the

current position of a given object at any point in the scene hierarchy. To add a Coordinate Transform

modifier, right-click the numeric input on any node, and select Modify With > CoordTransform Position

from the contextual menu.

Inspector

The Coordinate Transform modifier Controls tab

Controls Tab

The Controls tab has two fields for the target and scene input. The target is for the node continuing the

original coordinates, while the scene input is used for the scene with the new coordinates.

Target Object

This control is connected to the 3D tool that produces the original coordinates to be transformed. To

connect a tool, drag the node from the Node Editor into the text edit control, or right-click the control

and select the tool from the contextual menu. It is also possible to type the tool’s name directly into

the control.

SubID

The SubID slider can be used to target an individual sub-element of certain types of geometry, such as

an individual character produced by a Text 3D tool or a specific copy created by a Duplicate 3D tool.

Scene Input

This control should be connected to the 3D tool, which outputs the scene containing the object at

the new location. To connect a tool, drag and drop a tool tile from the Node Editor into the text edit

control, or right-click the control and select an object from the Connect To pop-up menu.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Cubic Spline

The Cubic Spline is another animation modifier in Fusion that is normally applied to numerical values

rather than point values. It can be applied by right-clicking a numerical control and selecting Modify

With > Natural Cubic Spline.

Usage

Being an animation spline, this modifier has no actual Controls tab. However, its effect can be seen

and influenced in the Spline Editor.

Cubic Spline Editor


Fusion Page Effects | Chapter 124 Modifiers

FUSION