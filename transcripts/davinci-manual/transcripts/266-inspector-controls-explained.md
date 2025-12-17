---
title: "Inspector Controls Explained"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 266
---

# Inspector Controls Explained

Although a few nodes use fully customized interface elements that are unique to only that node, the

vast majority of nodes use a mix of sliders, angle wheels, and checkboxes. This section explains how

to use these controls.

Fusion Slider Controls

Slider Controls are used to select a single value from a range of values. You change the value by

dragging the slider or entering a value into the edit box. This is fairly standard behavior for sliders.

However, there is additional functionality that can increase your productivity when making changes

with sliders.

Clicking on the gutter to the left or right of the handle will increase or decrease the value. Holding

Command while clicking on the gutter will adjust the values in smaller increments. Holding Shift while

clicking will adjust the value in larger increments.

Hold Command while clicking in the gutter

to move in smaller increments

While slider controls use a minimum and maximum value range, entering a value in the edit box

outside that range will often expand the range of the slider to accommodate the new value. For

example, it is possible to enter 500 in a Blur Size control, even though the Blur Size sliders default

maximum value is 100. The slider will automatically adjust its maximum displayed value to allow entry

of these larger values.

If the slider has been altered from its default value, a small circular indicator will appear below the

gutter. Clicking on this circle will reset the slider to its default.

Thumbwheel

A Thumbwheel control is identical to a slider except it does not have a maximum or minimum value.

To make an adjustment, you drag the center portion left or right or enter a value directly into the

edit box. Thumbwheel controls are typically used on angle parameters, although they do have other

uses as well.

Thumbwheel controls for X,Y, and Z rotation with

arrows on either end for fine-tuning adjustments

Once the thumbwheel has been selected, you can use the Up and Down Arrows on your keyboard

to further adjust the values. As with the slider control, the Command and Shift keys can be used to

increase or decrease the change in value in smaller or larger increments.

If the thumbwheel has been altered from its default value, a small circular indicator will appear below

above the thumbwheel. Clicking on this circle will reset the thumbwheel to its default.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Range Controls

The Range controls are actually two separate controls, one for setting the Low Range value and one

for the High Range value. To adjust the values, drag the handles on either end of the Range bar. To

slide the high and low values of the range simultaneously, drag from the center of the Range bar. You

can also expand or contract the range symmetrically by holding Command and dragging either end of

the Range bar. You find Range controls on parameters that require a high and low threshold, like the

Matte Control, Chroma Keyer, and Ultra Keyer nodes.

A Matte Threshold Range control

TIP: You can enter floating-point values in the Range controls by typing the values in using

the Low and High numeric entry boxes.

Checkboxes

Checkboxes are controls that have either an On or Off value. Clicking on the checkbox control will

toggle the state between selected and not selected. Checkboxes can be animated, with a value of 0

for Off and a value of 1.0 or greater for On.

Checkboxes used to select options for tracking

Drop-Down Menus

Drop-down menus are used to select one option from a menu. Once the menu is open, choosing one

of the items will select that entry. When the menu is closed, the selection is displayed in the Inspector.

Drop-down menu in the TimeSpeed node

Drop-down menu selections can be animated, with a value of 0 representing the first item in the list, 1

representing the second, and so forth.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Button Arrays

Button arrays are groups of buttons that allow you to select from a range of options. They are almost

identical in function to drop-down menu controls, except that in the case of a button array it is possible

to see all of the available options at a glance. Often button arrays use icons to make the options more

immediately comprehensible.

The Lens Type button array in the Defocus node

Color Chooser and Picker

The Color panel is displayed wherever a parameter requires a color as its value, such as the Fill or

Outline color in the Text+ node. The selected color is shown in a swatch with an Eyedropper to its

right, and below the swatch is the Color Chooser.

The Color panel with transparency preview

The Color panel is extremely flexible and has four different techniques for selecting and

displaying colors.

TIP: Color can be represented by 0–1, 0.255, or 0–65000 by setting the range you want in

the Preferences > General panel.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

macOS and Windows Color Nodes

Clicking on the color swatch will display the operating system’s standard Color Selection node.

Each operating system has a slightly different layout, but the general idea is the same. You can choose

a color from the swatches provided—the color wheel on macOS, or the color palette on Windows.

However you choose your color, you must click OK for the selection to be applied.

macOS Colors panel

Windows Color dialog


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

The Color Chooser

You also have access to the built-in color chooser, which includes sections for choosing grayscale

values, as well as the currently chosen hue with different ranges of saturation and value. A hue bar and

alpha bar (depending on the node) let you choose different values.

The color chooser in

the Background node

Picking Colors from an Image

If you are trying to match the color from an image in the viewer, you can hold down the cursor over

the Eyedropper, and then drag the pointer into the viewer. The pointer will change to an Eyedropper,

and a pop-up swatch will appear above the cursor with the color you are hovering over and its values.

When you are over the color you want, release the mouse button to set the color.

The Eyedropper

with color swatch

The Color Picker normally selects from a single pixel in the image, but you can adjust the size of the

selection by dragging into the viewer with the Eyedropper, and then holding Command and dragging

out a rectangle for the sample size you want. The size change applies to all Color Pickers until the size

is changed again.

Gradients

The Gradient Control bar is used to create a gradual blend between colors. The Gradient bar displays

a preview of the colors used from start to end. By default, there are two triangular color stops: one on

the left that determines the start color, and one on the right that determines the end color.

The default Gradient controls


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Gradient Type

The Gradient Type button array is used to select the form used to draw the gradient.

Linear gradient: Linear draws the gradient along a straight line from the starting color

stop to the ending color stop.

Linear gradient

Reflect gradient: Reflect draws the gradient by mirroring the linear gradient on either

side of the starting point.

Reflect gradient

Square gradient: Square draws the gradient by using a square pattern when

the starting point is at the center of the image.

Square gradient

Cross gradient: Cross draws the gradient using a cross pattern when the starting point is at

the center of the image.

Cross gradient


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Radial gradient: Radial draws the gradient in a circular pattern when the starting point is at the

center of the image.

Radial gradient

Angle gradient: Angle draws the gradient in a counter-clockwise sweep when the starting

point is at the center of the image.

Angle gradient

Start and End Position

The Start and End Position controls have a set of X and Y edit boxes that are useful for fine-tuning the

start and end position of the gradient. The position settings are also represented by two crosshair

onscreen controls in the viewer, which may be more practical for initial positioning.

Gradient Colors Bar

The Gradient Colors bar is used to select the blending colors for the gradient. The default two color

stops set the start and end colors. You can change the colors used in the gradient by selecting the

color stop, and then using the Eyedropper or color wheel to set the new color.

You can add, move, copy, and delete colors from the gradient using the Colors bar.

To add a color stop to the Gradient Colors bar:


Click anywhere along the bottom of the Gradient Colors bar.


Use the Eyedropper or color wheel to set the color for the color stop.

To move a color stop on the Colors bar:

�Drag a color stop left or right along the Gradient Color bar.

To copy a color stop on the Colors bar:

�Hold Command while you drag a color stop.

To delete a color stop from the Colors bar, do one of the following:

�Drag the color stop up past the Gradient Colors bar.

�Select the color stop, then click the red X button to delete it.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Interpolation Space

The Gradient Interpolation Method pop-up menu lets you select what color space is used to calculate

the colors between color stops.

Offset

When you adjust the Offset control, the position of the gradient is moved relative to the start and end

markers. This control is most useful when used in conjunction with the repeat and ping-pong modes

described below.

Once/Repeat/Ping-Pong

These three buttons are used to set the behavior of the gradient when the Offset control scrolls the

gradient past its start and end positions. The Once button is the default behavior, which keeps the

color continuous for offset. Repeat loops around to the start color when the offset goes beyond the

end color. Ping-pong repeats the color pattern in reverse.

1x1, 2x2, 3x3, 4x4, 5x5

These buttons control the amount of sub-pixel precision used when the edges of the gradient become

visible in Repeat mode, or when the gradient is animated. Higher settings will take significantly longer

to render but will be more precise.

Gradient Contextual Menu

Gradients have their own contextual menu that you can bring up by right-clicking on the Gradient bar.

In the Gradient contextual menu are options for animating, publishing, and connecting one gradient

to another. There is also a gradient-specific modifier that builds a custom gradient by sampling colors

from the output of a node in the Node Editor.