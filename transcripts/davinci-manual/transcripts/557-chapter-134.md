---
title: "Chapter 134"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 557
---

# Chapter 134

Curves

The Color page has a powerful curves interface that provides controls for adjusting

color and contrast with the Custom Curves, as well as a variety of “Hue” or “HSL”

curves that let you make more targeted adjustments to hue, saturation, and

luminance in a variety of ways.

Contents

Introduction to Curves��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3108

Adjusting Curves Using the Mouse������������������������������������������������������������������������������������������������������������������������������������������� 3108

Sampling Images to Place Control Points on Curves��������������������������������������������������������������������������������������������������������� 3110

Showing Picker RGB Values����������������������������������������������������������������������������������������������������������������������������������������������������������� 3110

Curves Histograms������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3110

Custom Curves������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3112

Editing the Top and Bottom Control Points of Curves������������������������������������������������������������������������������������������������������� 3113

HDR Grading Using Curves������������������������������������������������������������������������������������������������������������������������������������������������������������ 3114

Enabling Editable Splines in the Custom Curves����������������������������������������������������������������������������������������������������������������� 3114

Adding Default Anchors to the Custom Curves�������������������������������������������������������������������������������������������������������������������� 3115

Ganging and Unganging Custom Curves�������������������������������������������������������������������������������������������������������������������������������� 3115

Copying Custom Curves From One Color Channel to Another������������������������������������������������������������������������������������ 3116

Curve Intensity Sliders���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3116

YSFX Sliders�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3117

Soft Clip����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3117

Ganging and Unganging Soft Clip Controls��������������������������������������������������������������������������������������������������������������������������� 3118

Soft Clip Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3118

The HSL Curves����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3121

Image Sampling for Hue and Sat Curves�������������������������������������������������������������������������������������������������������������������������������� 3122

Additional Controls in the Hue and Sat Curves������������������������������������������������������������������������������������������������������������������� 3123

Hue vs. Hue������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3123

Hue vs. Sat���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3124

Hue vs. Lum�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3124

Lum vs. Sat��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3125

Sat vs. Sat����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3125

Sat vs. Lum Curve������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3126


Color | Chapter 134 Curves

COLOR

Introduction to Curves

The Curves palette, selectable via one of the toolbar buttons above the Center Palette panel of the

Color page, has six modes that provide different curve-based methods of manipulating the color and

contrast of an image. Each curve lets you adjust a customizable region of the image based either on

image tonality (zones of lightness or darkness), hue (specific colors), or saturation (intensity of color).

All curves can be adjusted using either the pointer, or knobs on the DaVinci Resolve Mini or Advanced

control panel.

The Curves palette is color-space-aware when you’re using Resolve Color Management (RCM) or

ACES. What this means is that the overall range of each curve better fits the overall data range of the

current clip no matter what Timeline Color Space you’re using, for both SDR and HDR mastering. This

makes curves adjustments easier, more specific, and a more consistent experience, no matter what

your workflow happens to be.

TIP: All curves in DaVinci Resolve can be used to affect the overall image, or limited to

affect only a specific portion of the image as a part of a secondary operation using qualifiers,

windows, imported mattes, or any combination of the three.

Adjusting Curves Using the Mouse

All Color curves in DaVinci Resolve use the following controls for basic on-screen adjustment using

the pointer, controlled either with your mouse, pen, or other input device of choice.

Methods of adjusting curves using the on-screen interface:

�To add a control point: Click anywhere on a curve. A control point is added at the position of

the mouse where you clicked, and the curve is altered, if necessary, to match the new control

point’s position.

�To add a control point without altering the curve: Hold the Shift key down, and click anywhere on

or around a curve. A control point is added to the curve at the position of the pointer where you

clicked, but the curve is not altered.

�To snap a control point to the neutral diagonal of the curve: (Custom curve only) Hold the Option

key down while dragging any control point on the curve. A diagonal line appears indicating the

neutral state of the image, and the control point will snap to it. When you release the Option key

and then press the Option key again after releasing, the diagonal guide line disappears.

Snapping a curve’s control point back to its neutral position by holding down the Option key


Color | Chapter 134 Curves

COLOR

�To remove a control point: Right-click any control point to make it disappear.

�To reset a single color channel curve to a completely neutral setting: Click the reset button to

the right of that color channel’s intensity slider.

�To reset all color channel curves: Click the Reset Custom Curve button at the upper right-hand

corner of the Curves palette.

By default, a control point influences the portion of each curve that falls between its neighboring

two control points.

Control point adjustments affect the entire portion of a curve between adjacent control points.

In the top screenshot, you can see that the control point at the position of the pointer is affecting the

larger part of the curve that falls between the lower left-hand control point (which is there by default),

and a user-created control point placed up within the highlights of the curve.

In the bottom screenshot, an additional control point to the left of the one being adjusted limits the

area of the curve that is adjusted. By careful placement of additional control points, you can make

extremely targeted adjustments to images using the Custom curves.


Color | Chapter 134 Curves

COLOR

This example highlights the importance of using control points to “lock off” portions of a curve

at a neutral or nearly neutral position to prevent changes to specific portions of an image,

even while using other control points to make changes.

NOTE: The HSL curves also have an optional adjustment mode using Bezier curves that will

be covered in those sections.

Sampling Images to Place Control Points on Curves

Another way you can add control points to curves is to move the pointer to the Viewer, and click

to sample a color value and place a control point at the position on the currently open curve that

corresponds to that value. This works with Custom, Hue, and HSL curves.

Clicking on a feature

of the image

Creates a control point on

the currently open curve

Showing Picker RGB Values

While you’re dragging the pointer over the Viewer and looking for a feature to sample, you can enable

a tooltip that shows you the RGB Value of the pixel under the pointer by right-clicking the Viewer and

choosing Show Picker RGB Value to toggle this feature on and off. When you turn this feature on, the

Show RGB Picker Values In submenu in the Viewer’s option menu has options for displaying either 8-

or 10-bit tristimulus values.

The color picker tooltip that appears when

you turn on Show RGB Picker Values

Curves Histograms

The Custom curves and HSL curves all show a histogram that represents the input of the currently

selected Correction node, which you can use to guide your adjustments. The Histograms submenu

of the Curves palette’s Option menu lets you choose to disable these histograms, or to switch

the histograms between showing the input or the output of the node. If you switch to Output, the

histograms will update to show you the result of your adjustments, at the expense of seeing the image

data that the curve is actually working upon.


Color | Chapter 134 Curves

COLOR

The Custom curves show a YRGB histogram:

The histogram appearing underneath the Custom Curves shows a YRGB histogram analysis

Each Hue or HSL curve shows a histogram analysis of the two color channels that

Curve acts upon: hue against saturation level, luminance against saturation level, or

saturation level against saturation level, to give three different examples. In the case of Hue

or HSL curves, these histograms make it easy to see which parts of the Curve controls will

actually affect image data.

The histogram appearing underneath the Hue vs Sat

curve plots all saturation levels at each value of hue


Color | Chapter 134 Curves

COLOR