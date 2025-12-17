---
title: "Drawing Curves"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 573
---

# Drawing Curves

The Curve window is the only window that doesn’t display any onscreen controls when it’s first turned

on. Instead, you must click within the Viewer to add control points, drawing your own custom shape to

isolate whatever region you want.

Curve window to isolate a car

TIP: Turning on the Viewer’s full-screen mode can make it easier to draw detailed shapes.

You can also zoom into and out of the Viewer while you’re drawing, using either the scroll

wheel of a mouse or by pressing Command-Plus or Command-Minus.

To draw a curve:


Turn on the Curve window style control.


Click anywhere in the Viewer to start adding control points and drawing the shape you need.


Click and drag to add and shape Bezier curves, or just click and release to add a hard angle.


To finish drawing and close the shape, click the first control point you created to create a corner, or

click and drag on the first control point you created to create a Bezier curve.

Once you’ve drawn a curve, there are many ways of manipulating it.

Simple methods of modifying a curve:

�To add points: Click anywhere on a curve to add control points.

�To reshape a curve: Drag any control point to a new location. You can drag control points even

while you’re drawing a new curve, selecting previously drawn points to move them, to adjust their

spline handles, or to delete previously added points, without the need to finish the window first.

�To move a curve: Drag anywhere within or just outside a curve to move it.

�To symmetrically alter a Bezier curve: Drag any Bezier handle. The opposite handle automatically

moves in the other direction.

�To asymmetrically alter a Bezier curve: Option-drag any Bezier handle. The opposite handle

stays in place while you drag the current handle. Once you’ve created an asymmetric pair of

Bezier handles, they move together as one if you simply drag a handle. You need to Option-drag

to change the angle.

�To change a curve into a corner: Option-double-click any Bezier curve control point to change it

to a sharp-angled corner point.

�To change a corner into a curve: Option-click any corner point and drag to pull out a Bezier

handle, changing it to a curve.

�To remove points: Middle-click the control point you want to remove.


Color | Chapter 138 Secondary Windows

COLOR

NOTE: Removing a control point from a polygonal window that’s already been animated

using the Keyframe Editor results in that point abruptly popping on and off at the keyframes

creating the animation.

You can also Shift-drag a bounding box to select multiple control points on a curve to move, delete, or

transform them all at once.

You can Shift-drag a bounding box over multiple control

points to manipulate them all at once.

To select multiple control points on a curve:


Hold the Shift key down and drag a bounding box around the control points you want to

manipulate or delete. All included control points will become highlighted.


Do one of the following:

�To move the control points: Drag anywhere within the bounding box.

�To transform the control points: Drag one of the outer corners to resize all control points

symmetrically, drag the top, bottom, or side handles to squish or stretch the control points

relative to one another, or move the pointer to one of the corners until the rotate cursor appears,

and then drag to rotate the control points.

�To delete the control points: Press the Backspace key.


When you’re finished, press the Escape key to deselect the control points.

Converting Linear, Circular, and Polygon

Windows into Bezier Curves

If you start out isolating a subject using one of the simple Linear, Circular, or Polygon shape windows

and you realize that you need a more complex shape to accomplish the task at hand, you can easily

convert them to a more complex Bezier curve by choosing Convert to Bezier from the Window palette

Option menu.


Color | Chapter 138 Secondary Windows

COLOR

Before and after converting a circular window to a Bezier curve and

adjusting the result, before adding softness to the edge

Once you’ve converted a simple shape to a Bezier window, you can add control points and manipulate

the shape in any way you need to make it better conform to the subject, just as you would with

any curve.

Resetting the Window Palette

The entire Window palette can be reset using the Option menu’s Reset command.

Combining Power Windows

with the Mask Control

Adding multiple windows to a single node is an easy way to create composite keys. When combining

windows, the Mask control defines whether one window adds to another window, or subtracts from

that window.

In the following example, Circular and Curve windows have both been created, and each window’s

Mask control is also turned on (by default), resulting in both masks being added together so that the

sunset look correction affects both the sky and the woman’s face.

The two images show the combination of the key mattes.

By turning the Mask control of the circular window off, the circular window is subtracted from the curve.


Color | Chapter 138 Secondary Windows

COLOR

Turning off the Mask control of the circular window

Now, the woman’s face is being protected from the aggressive sky treatment.

The two images show the result of subtracting the circular window

Since windows can be individually tracked and keyframed, you can quickly set up complex

interactions of windows to solve common problems you’ll encounter. For example, when you’re

tracking a window to follow a moving subject that moves behind something in the frame, you can use

a second window with Mask turned off to cover the object in front. Now, when the tracked window

intersects the subtractive window, the correction will disappear along with the subject.

You can also use the Mask control to create more complex shapes than you can with a single window.

Mattes and mask used together to make complex shapes

Furthermore, once you reach the limits of what shapes you can create using the four available

windows, you can combine multiple nodes containing multiple shapes and qualifiers using the

Key Mixer.


Color | Chapter 138 Secondary Windows

COLOR

Copying and Pasting Windows

If there’s a particular window you’ve created that you want to either duplicate within the current node,

or apply to another node, you can copy and paste an individual window’s shape from one item in the

Window list to another.

Methods of copying and pasting windows:

�To copy a window: Click any enabled window in the Window list, then click the Window palette

option menu and choose Copy Window.

�To duplicate a window: After copying a window, create another window of the same type that you

copied, and then click the Window palette option menu and choose Paste Window.

�To paste a window to another node: Double-click or otherwise select another node, open the

Window palette, choose the same type of window that you copied in the Window list, and then

click the Window palette option menu and choose Paste Window.

�To paste a window to the same node: Click any enabled window in the Window list, then click the

Window palette option menu and choose Copy Window, then click Paste Append Window in the

Window Option menu.

Saving Window Presets

If you find there’s a particular window shape or combination of windows that you use frequently, you

can save one or more windows as a preset for easy recall whenever needed. For example, if you’re

working on a documentary within which you find you need to do a lot of face brightening, you can

create preset face ovals for close-up, medium, and wide shots, to save you from having to customize

a stock circular window for every single new shot. You can also save groups of windows together as a

single preset, in order to reuse complicated multi-window shapes.

Window presets are available from a group of Presets controls in the option menu in the upper right-

hand corner of the Window palette.

Controls for saving, applying,

and deleting window presets


Color | Chapter 138 Secondary Windows

COLOR

Methods of working with Power Window presets:

�To save a window preset: Once you’ve created one or more windows you want to save, click the

Save as New Preset option in the Window palette’s option menu. Type a name into the resulting

dialog, and click OK. That preset is now available in the Preset section of the option menu.

�To recall a window preset: Click to open the Window palette’s option menu, and choose a preset

from the list. Loaded window presets overwrite whatever other windows were set up in that node.

�To update an already saved preset: Recall a preset, change the resulting window(s), then click to

open the Window palette’s option menu. Select Update Preset, then select the preset name. This

will overwrite the selected preset with the altered window arrangement.

�To delete a window preset: Click to open the Window palette’s option menu, and choose Delete

Preset, then choose a preset from the list. Make sure you chose the correct preset name; there is

no warning before the deletion, and you cannot undo the deletion once it’s done.

Once recalled, windows created by presets can be modified and tracked just like any other window.