---
title: "Natural Cubic Spline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 525
---

# Natural Cubic Spline

The Natural Cubic Spline is one of the animation modifiers in Fusion and normally is applied to

numerical values rather than point values. It can be applied by right-clicking a numerical control and

selecting Modify With > Natural Cubic Spline.

NOTE: Unlike other spline types, Cubic splines have no control handles. They attempt to

automatically provide a smooth curve through the control points.

Usage

Being an animation spline, this modifier has no actual Controls tab. However, its effect can be seen

and influenced in the Spline Editor.

Natural Cubic Spline Editor


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Offset (Angle, Distance, Position)

There are three Offset modifiers used to create variances between values. Depending on the modifier,

these values relate to controls, paths, and points. The three types of Offset modifiers available in

Fusion are:

�Offset Angle

�Offset Distance

�Offset Position

Offset Angle

The Offset Angle modifier outputs a value between 0 and 360 that is based on the angle between

two positional controls. The Position and Offset parameters may be static, connected to other

positional parameters, or connected to paths of their own. All offsets use the same set of controls,

which behave differently depending on the offset type used. These controls are described below.

Offset Distance

The Offset Distance modifier outputs a value that is based on the distance between two positional

controls. This modifier is capable of outputting a value based on a mathematical expression applied to

a position.

Offset Position

The Offset Position modifier generates a position (X and Y coordinates) that is based on the

relationship between positional controls. This modifier is the equivalent of a calculation control except

that it outputs X and Y coordinates instead of a value.

It can be applied by right-clicking a control and selecting Modify With > Offset.

Inspector

The Offset Position modifier controls

Offset Tab

The Inspector for all three Offset modifiers is identical. The Offset tab includes Position and

Offset values as well as a Mode menu for selecting the mathematical operation performed by the

offset control.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Position X and Y

The X and Y values are used by the Position to generate the calculation.

Offset X and Y

The X and Y values are used by the Offset to generate the calculation.

Flip Position Horizontal and Vertical

When these controls are selected, the Position is mirrored along the vertical or horizontal axis of

the image.

Flip Offset Horizontal and Vertical

When these controls are selected, the Offset position is mirrored along the vertical or horizontal axis

of the image.

Mode

The Mode menu includes mathematical operations performed by the Offset control. Available

options include:

�Offset

�Difference (Position - Offset)

�Difference (Offset - Position)

�Average

�Use Position Only

�Use Offset Only

�Maximum

�Minimum

�Invert Position

�Invert Offset

�Invert Sugar

�Random Offset

Image Aspect

Adjust the modifier’s output to compensate for the image aspect (not pixel aspect) of the project. A

square image of 500 x 500 would use an Image Aspect value of 1, and a rectangular image of 500 x

1000 would use an Aspect Value of 2. The default value is always based on the current frame format

selected in the preferences. To calculate image aspect, divide the width by the height. This control can

also be used to create the illusion of aspect.

The Offset Time tab

Time Tab

Position Time Scale

This returns the value of the Position at the Time Scale specified (for example, 0.5 is the value at half

the current frame time).

Position Time Offset

This returns the value of the Position at the Time Offset specified (for example, 10 is 10 frames back).


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Offset Time Scale

This returns the value of the Offset at the Time Scale specified.

Offset Time Offset

This returns the value of the Offset at the Time Offset specified.

Example

This is a simple comp to illustrate one potential use of offsets.

•	 Create a new Comp 100 frames long.

•	 Create a node tree consisting of a black background and a Text node foreground connected

to a Merge.

•	 In the Text Layout tab, use the Center X control to animate the text from the left side of the

screen to the right.

•	 Move to frame 0.

•	 In the Text tab in the Inspector, right-click the Size control and select Modify With > Offset

Distance from the contextual menu.

•	 This adds two onscreen controls: a crosshair for the position and an X control for the

offset. These onscreen controls represent the Position and Offset controls displayed in the

Modifiers tab.

The size of the text is now determined by the distance, or offset, between the two

onscreen controls.

•	 Drag the X onscreen control in the viewer to see how the distance from the crosshair

changes the size of the merge and by association the text.

•	 Both the crosshair and the X onscreen controls are animatable and can be connected to

other controls.

•	 Position the X centered at the bottom of the viewer.

•	 In the Inspector, select the Modifiers tab.

•	 In the Offset on Text size section, right-click over Position and choose Connect To >

PathConnect the position value of the Offset to the existing path by right-clicking the

Position control and selecting Connect To > Path1 Position.

•	 Play the comp to view the animation.

Now, the text shrinks near the center of the path (when the distance between the offset and

the path is at its minimum) and grows at its ends (where the distance between the offset and

the path is at its maximum).


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Path

The Path modifier uses two splines to control the animation of points: an onscreen motion path

(spacial) and a Time spline visible in the Spline Editor (temporal). To animate an object’s position

control using a Path, right-click the Position control either in the Inspector or in the viewer and select

Path from the contextual menu. This adds a keyframe at the current position. You can begin creating a

path by moving the playhead and dragging the center position control in the viewer. The Spline Editor

shows a displacement spline for editing the temporal value, or “acceleration,” of the path.

Inspector

The Path modifier Controls tab

Controls Tab

The Controls tab for the path allows you to scale, reposition, and rotate the path. It also provides the

Displacement parameter, allowing you to control the acceleration of an object attached to the path.

Center

The actual center of the path. This can be modified and animated as well to move the entire

path around.

Size

The size of the path. Again, this allows for later modification of the animation.

X Y Z Rotation

The path can be rotated in all three dimensions to allow for sophisticated controls.

Displacement

Every motion path has an associated Displacement spline in the Spline Editor. The Displacement

spline represents the position of the animated element along its path, represented as a value between

0.0 and 1.0. Displacement splines are used to control the speed or acceleration of an object’s

movement along the path.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

To slow down, speed up, stop, or even reverse the motion of the control along the path, adjust the

values of the points for the path’s displacement in the Spline Editor or in the Inspector.

�A Displacement value of 0.0 in the Spline Editor indicates that the control is at the very beginning

of a path.

�A value of 1.0 indicates that the control is positioned at the end of the path.

�Each locked point on the motion path in the viewer has an associated point on the

Displacement spline.

�Unlocked points have a control point in the viewer but do not have a corresponding point on the

Displacement spline.

Heading Offset

Connecting to the Heading adjusts the auto orientation of the object along the path. For instance,

if a mask’s angle is connected to the path’s heading, the mask’s angle will adjust to follow the angle

of the path.

Right-Click Here for Shape Animation

It’s possible to animate the shape of the path as well or to connect it to other path controls like Polyline

Masks or Paint Strokes.

TIP: Switching Default Paths

You can change the default path type used when animating a position or center control to

a path (if this is the preferred type of animation). Open the Preferences window and select

the Global Settings. In the Default category, select the Point With menu and choose Path.

The next time Animate is selected from a Position or Center control’s contextual menu,

a path is used.