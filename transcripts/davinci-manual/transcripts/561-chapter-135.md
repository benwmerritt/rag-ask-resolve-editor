---
title: "Chapter 135"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 561
---

# Chapter 135

ColorSlice

This chapter focuses on using the ColorSlice tool, allowing you to make

targeted changes to specific color ranges that seamlessly integrate with the rest

of the image.

Contents

ColorSlice����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3129

Vectorspace ColorSlice Controls������������������������������������������������������������������������������������������������������������������������������������������������ 3130

Global ColorSlice Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������� 3131

Using Color Slice���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3131


Color | Chapter 135 ColorSlice

COLOR

ColorSlice

ColorSlice is a fixed vector grading tool that allows you to qualify a range or ranges of colors that all

blend smoothly together, making a more seamless image than using the HSL qualifier.

The ColorSlice vector-based grading tool

You can use ColorSlice to set overall density, saturation, and hue parameters to replicate different

CMY print processes and to change brightness and saturation for each vectorspace slice. To achieve

deep filmic colors and looks, brightness is controlled in a subtractive way when adjusting saturation,

so saturated colors are not unnaturally bright and do not need luminance adjustments.

Increasing the Saturation (left) creates a brighter red,

while using the ColorSlice tool (right) creates a deeper red.


Color | Chapter 135 ColorSlice

COLOR

Vectorspace ColorSlice Controls

The ColorSlice tool is comprised of seven different vectorspace slices. Each vectorspace slice controls

a range of colors based on the conventional vectors on the Vectorscope: Red, Green, Blue, Cyan,

Magenta, and Yellow. In addition, a seventh vector has been added for skin tones.

The Red ColorSlice

vectorspace slice controls

Each vectorspace slice is composed of the following controls:

Highlight: Click and holding on this icon will enable a highlight view as long as you hold the

button down, showing the areas of the image that will be modified by the control. You can also

switch between each vectorspace’s highlight permanently by activating a highlight view in the

Viewer first to make it easier to refine the parameters below.

Slice Color: A name that represents the color of the area controlled (Red, Green, Blue, etc.).

Reset: Resets the all the vectorspace slice controls back to the default levels.

Color Wheel: A visual representation of the vectorspace slice. All colors within the brightened

wedge are what will be adjusted by the controls.

Center: This is the only adjustable qualifying control. Sliding this bright line back and forth

will move the center of the color range, letting you slightly change which colors are weighted

more in the qualifier. You cannot move the center out of its range. Use this tool in conjunction

with the highlight view to make sure that the specific colors you want to adjust are qualified.

Hue: Changes the hue of all the colors within the vectorspace slice. Adjusting this control

does not affect the qualification of the original color.

Density: Adjusts the density of the colors inside the vectorspace slice by adjusting the

luminance of more saturated colors to emulate a subtractive color film process.

Saturation: Adjusts the saturation of colors qualified by this slice using a subtractive color

model that prevents highly saturated colors from becoming unnaturally bright.


Color | Chapter 135 ColorSlice

COLOR

Global ColorSlice Controls

In addition to the individual vectorspace slice controls, there are a set of global controls along the top

of the tool. These will change the values of the entire image.

The ColorSlice Global controls

Density: Adjusts the luminance of more saturated colors to emulate a subtractive

color film process.

Den.Depth: Controls the effect of density adjustments on brighter areas of the image.

Saturation: Adjusts saturation using a subtractive color model that prevents highly saturated

colors from becoming unnaturally bright.

Sat.Balance: Adjusts how saturation changes effect the luminance balance in colors with

medium saturation levels.

Sat.Depth: Controls the effect of saturation adjustments on brighter areas of the image.

Hue: Changes the hue of all the colors within the image.

Reset: Resets all ColorSlice adjustments.

Using the Numeric Parameters

In addition to the Global controls above, Each vectorspace slice has a set of four number fields that

display the values of the Center, Hue, Density, and Saturation controls. These fields can be edited like

any other parameter on the Color page.

To edit values directly:

�You can double-click on a field to edit its value numerically.

�You can insert the text cursor next to a value in this field and use the Up and Down Arrow keys to

adjust the value one digit at a time.

�You can cut, copy, and paste values among fields.

�You can click on the field and drag left or right to adjust its value with a virtual slider.

Using Color Slice

Each vectorspace slice has a center line, which is the color where most of the weight of the

adjustments will be made. By sliding the Center control back and forth, you can select which color

to qualify the most of. The Center control is the only control used to qualify colors; all the other tools

make adjustments to that qualification.

The Cyan color slice center is

marked by a bright white line,

while its color range is bounded

by white lines on either side

clockwise and counterclockwise.


Color | Chapter 135 ColorSlice

COLOR

As you adjust the Center control, you will want to take a look at the qualified colors, either by click and

holding on the highlight icon in the upper left of the vectorspace slice, or by turning on the highlight in

the Viewer.

Once you have the range of colors selected, you simply adjust the Hue, Density, and Saturation

controls for the vectorspace slice until you get the results you’re looking for. Note that pulling a

perfectly clean matte is not necessary; you just want to make sure that the range of colors you want to

enhance is mostly selected.

For this example, we will quickly qualify and adjust both the sky and ocean, as well as the cycler’s skin

tone all in the same node, at the same time using just the ColorSlice tool.

This is the initial balanced image, and we want to make the sky and ocean more vibrant, as well as

accentuate the sunset light falling on the cyclist.

The original balanced shot we want to enhance

First, we open the ColorSlice tool and set our Viewer to B/W Highlight.

Using the Cyan vectorspace slice, we first adjust the Center control until we have the maximum

amount of sky and ocean qualified (white). Next we will turn off our highlight and adjust the density and

saturation sliders to get a nice vibrant sky and ocean.

Adjusting the Cyan center control to maximize

the amount of sky and ocean qualified (white)

The center, density, and

saturation adjustments

for Cyan (sky and ocean)


Color | Chapter 135 ColorSlice

COLOR

Next we will use the Skin vectorspace slice, and again turn on the highlight and adjust the center until

we have the maximum amount of the cyclist qualified. However, note we also end up qualifying quite

a bit of the hills behind him, which we don’t want. We then turn off the highlight and adjust the density

and saturation sliders until we have a rich warm glow falling on him (and the hills).

Adjusting the Skin center control to maximize the amount of the cyclist

qualified (white). Note quite a bit of the hills behind him are qualified too.

The center, density, and

saturation adjustments for

Skin, accentuating the late

afternoon sun on the cyclist

Now we will go over to the next vectorspace slice, Yellow. Turning on the highlight, we will now adjust

the center control to maximize the amount of the hills behind him that are qualified. Note that his skin

tones are not qualified using this vectorspace slice, only the hills. Now we will turn off the highlight and

dial back the density and saturation of the hills again that we had qualified in the previous slice.

Adjusting the Yellow center control to pick out just the hills (white).

Note his skin tones are not qualified.

The center, density, and

saturation adjustments for

Yellow, desaturating just

the hills back to normal that

were inadvertently picked

up in the Skin vectorspace

slice previously.


Color | Chapter 135 ColorSlice

COLOR

The final image and result from those three fast ColorSlice operations.

The final ColorSlice image; three different operations in one node with one tool

You may have noticed that the qualification mattes pulled by these operations were full of

small holes and expect to have to do a lot of tedious matte finesse operations to smooth them

out. With ColorSlice, all the qualifiers blend seamlessly into the others, so there is no matte

flickering or distracting speckles popping in and out as the video plays back. Of course, for

tricker shots you can still limit the ColorSlice effect using Power Windows, and even other

qualifiers, to direct the effect to just the areas of the frame you want it to apply to.


Color | Chapter 135 ColorSlice

COLOR