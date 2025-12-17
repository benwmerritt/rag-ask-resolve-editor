---
title: "Chapter 72"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 272
---

# Chapter 72

Animating in Fusion’s

Spline Editor

This chapter covers how you can keyframe effects and control animations in

Fusion’s Spline Editor.

Contents

Spline Editor Overview��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1477

Spline Editor Interface ��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1478

The Graph, Header, and Toolbar�������������������������������������������������������������������������������������������������������������������������������������������������� 1478

Renaming Splines������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1480

Changing Spline Colors������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1480

Navigating Around the Spline Editor ��������������������������������������������������������������������������������������������������������������������������������������� 1480

Markers ���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1481

Autosnap ������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1484

Creating Animation Splines ��������������������������������������������������������������������������������������������������������������������������������������������������������� 1484

Animating with Different Spline Types������������������������������������������������������������������������������������������������������������������������������������� 1485

Working with Keyframes and Splines��������������������������������������������������������������������������������������������������������������������������������������� 1487

Adding Keyframes ������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1487

Locked and Unlocked Controls Points������������������������������������������������������������������������������������������������������������������������������������� 1488

Selecting, Moving, and Deleting Keyframes ������������������������������������������������������������������������������������������������������������������������ 1489

Showing Key Markers����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1490

Copying and Pasting Keyframes ������������������������������������������������������������������������������������������������������������������������������������������������ 1490

Time and Value Editors ������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1492

Modifying Spline Handles�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1493

Reducing Points ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1494

Filtering the Spline Editor�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1495

Working with Filters��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1496

Changing a Spline’s Status ������������������������������������������������������������������������������������������������������������������������������������������������������������ 1497

Selection States ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1498


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Spline Editor Overview

The Spline Editor is the main area where animation is manipulated and refined. You primarily use the

Spline Editor to show the changing values of parameters over time in the form of splines. Whereas

Keyframes explicitly set the value of a parameter on a given frame, Splines are lines or curves

that interpolate the values between keyframes. Once you set a keyframe on a parameter, a spline

is created and can be displayed in the Spline Editor so you can make further refinements to the

animation. However, the Spline Editor is more advanced than a standard curve editor since it can

also display functions, which may not be splines, like changing characters within a text string or

mathematical expressions that drive your animations.

The Spline Editor with three animated parameters

What Are Splines?

All animation uses splines that describe the value of a parameter at any given point in time. The Spline

Editor graph shows the time of the comp along the horizontal axis and the value of the parameter

along the vertical axis.

The advantage of using splines to represent animation instead of keyframes as in the Keyframes

Editor is that splines allow you to manipulate the interpolation between keyframes. For example, if a

keyframe is set at a value of 1.0 on a parameter for frame 1, followed by a keyframe value of 10.0 for

frame 10, the values between keyframes are smoothly interpolated or calculated based on the shape

of the spline. Using the functions and controls in the Spline Editor, you have a fantastic amount of

control over that interpolation.

Reshaping Splines Using the Toolbar�������������������������������������������������������������������������������������������������������������������������������������� 1499

Interpolation������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1499

Reversing Splines ������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1501

Looping Splines ����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1501

Time Stretching ����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1504

Shape Box ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1505

Ease In/Out ������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1506

Importing and Exporting Splines ���������������������������������������������������������������������������������������������������������������������������������������������� 1507


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Spline Editor Interface

The Spline Editor is not visible by default, but you can show it at any time by clicking the Spline

button in the user interface toolbar. You can also display the Spline Editor by right-clicking on a

node in the Node Editor or a segment in the Keyframes Editor and choosing Edit Splines from the

drop‑down menu.

The Spline Editor can be open alongside the Node Editor or Keyframes Editor, or displayed separately

in order to take up the entire work area.

The Graph, Header, and Toolbar

The Spline Editor has three main working areas: the graph, header, and toolbar. On the left side of the

Spline Editor is the header, which shows a list of animated parameters. The majority of the panel is

taken up by the splines displayed in the graph area, and a toolbar runs along the bottom, providing a

variety of ways to manipulate the splines.

Graph

The graph is the largest area of the interface. It is here that you see and edit the animation splines.

There are two axes in the graph. The horizontal axis represents time, and the vertical axis represents

the spline’s value. A thin bar, called the playhead, runs vertically through the graph to represent the

current time as it does in the Timeline Editor. You can drag the playhead to change the current time,

updating the frame displayed in the viewers.

Removing a spline from a parameter removes the animation

Spline Editor Header

The header provides a mechanism for determining what splines are visible in the graph. It shows the

name of each spline in the project beneath the tool that contains that parameter. The checkbox beside

each name shows whether that spline is currently displayed in the graph and whether the spline can

be edited.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

The Spline header

Spline Editor Toolbar

The toolbar across the bottom of the Spline Editor represents the most common operations applied

to an animation spline. The various operations represented in the toolbar are all accessible from the

graph’s context menu as well, but the following buttons provide a faster shortcut.

Spline toolbar buttons

Playhead

The playhead is the thin red vertical bar that runs vertically through the Spline Editor graph and

represents the current time of the comp. You can drag the playhead to change the current time.

Status Bar

The status bar in the lower-right corner of the Fusion window regularly displays information about the

position of the pointer, along with the time and value axes.

Contextual Menus

There are two contextual menus accessible from the Spline Editor. The Spline contextual menu is

displayed by right-clicking over the graph, while the Guide contextual menu is displayed by right-

clicking on the Time Ruler above the graph.

Right-click on the horizontal axis Time

Ruler for the Guide menu


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Renaming Splines

The name of a spline in the header is based on the parameter it animates. You can change the name

of a spline by right-clicking on it in the header and choosing Rename Spline from the contextual menu.

Changing Spline Colors

Each spline in the graph is assigned a different color, making individual splines easier to identify when

multiple splines are visible at once. When the spline is active, a round color swatch is displayed next to

the spline’s name in the header.

To change the color of a spline:


Click on the color circle next to the spline name in the header.


Or right-click on the name of the spline in the header and choose Change Color from the

contextual menu.


Select the new color from the dialog box that appears and click OK.

Navigating Around the Spline Editor

It is often necessary to magnify and pan around the graph area to ensure that the splines you want

to work on are visible. In general, scaling and panning the Spline Editor works the same as in all

navigable parts of the Fusion interface. However, there are several unique functions to the Spline

Editor for controlling your view based on the height, width, and selection of multiple animation splines.

The most obvious navigation methods to use are the scale sliders and buttons located in the upper

left of the Spline Editor panel.

The Zoom Height and Zoom Width sliders, Fit button, and Zoom to Rectangle

button can be used to navigate around the graph

To scale and pan using the sliders and buttons:

Zoom Height and Zoom Width sliders let you change the height and

width of the graph area.

The Fit button attempts to rescale the view so that all currently active

splines fit within the graph.

The Zoom to Rectangle button (Command-R) allows you to draw

a bounding box around the area of the graph you want centered

and scaled.

To scale using the axis labels:

�Place the mouse pointer over the rulers for the horizontal or vertical axis and drag to resize

the graph on that axis only. The view is scaled centered on the original position of the

pointer on the ruler.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Dragging in the Time Ruler

scales the graph horizontally

To scale and pan with the mouse and/or keyboard:

�With the Spline Editor active, press the + and - keys on your keyboard to zoom in and

out of the graph.

�You can also zoom to a specific control point by holding down the Command key and scrolling the

middle mouse wheel. The mouse pointer location determines the area that gets magnified.

�Position the mouse pointer over the graph, and then hold down the middle mouse button. With the

middle mouse button pressed down, click once on the left mouse button to zoom in and once on

the right button to zoom out.

To pan the graph area:

�Drag left or right using the middle mouse button or use the scroll bar along the bottom and right

side of the graph.

Using the Graph contextual menu for navigation:

There are several ways to navigate the graph area using the Spline Editor contextual menu as well.

�Choose Scale > Scale to Fit (Command-F) to fit all active splines into the graph area.

�Choose Scale > Scale to Rectangle (Command-R) to draw a bounding box around the area of the graph

you want centered and scaled. This has the same effect as clicking the Zoom to Rectangle button.

�Choose Scale > Default to reset the scaling of the graph area to default values.

�Choose Scale > Zoom In/Zoom Out to scale the graph area. This performs the same functions as

pressing the + and - keys on the keyboard.

�Choose Scale > Auto Fit to scale the graph to fit all splines dynamically as you make splines visible

and hidden. If the scaling is changed with Auto-Fit enabled, the graph area will scroll as you play

the comp to view all the keyframes.

�Choose Scale > Auto Scroll to scroll the graph area if the splines fall outside the graph horizontally

as you play.

�Choose Scale > Manual to disable all automatic attempts at showing splines in the graph.

�Choose Options > Fit Times to automatically scale along the X-axis to fit the selected spline.

All visible splines are taken into account, not just the newly selected spline. With this option off,

activating a new spline will not change the horizontal scale.

�Choose Options > Fit Values to automatically scale along the Y-axis to fit the selected spline.

All visible splines are taken into account, not just the newly selected spline. With this option off,

activating a new spline will not change the vertical scale.