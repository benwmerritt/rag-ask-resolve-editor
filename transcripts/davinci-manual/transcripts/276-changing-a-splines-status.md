---
title: "Changing a Spline’s Status"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 276
---

# Changing a Spline’s Status

The Spline header is a hierarchical list of animated parameters and their parent nodes. Clicking

the disclosure arrow next to a tool’s name reveals all the names of the animated parameters on

that tool. Clicking directly on the parameter name in the Spline header activates that spline for

display and editing.

The Spline header with the Brightness

Contrast tool and its animated

Gain and Gamma parameters

Tool Status Checkbox

Next to the name of each spline is a checkbox that indicates the spline’s status. When you select a

parameter name, the checkbox becomes active, allowing you to see and edit the spline in the graph.

There are three selection modes for each checkbox: active, viewed, and disabled. Clicking directly

on the checkbox will toggle it between these three states. Changing the state of the parent node

checkbox sets the state for all splines for that node.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Active: When the checkbox is enabled with a check

mark, the spline is displayed in the graph and can

be edited.

Viewed: When the checkbox is enabled with a

solid gray box, the spline is visible in the graph but

cannot be edited. It is read-only.

Disabled: When the checkbox is clear, the spline is

not visible in the graph and cannot be edited.

Checkboxes determine which

splines are visible and editable

Selection States

There are three selection options, labeled Select All Tools, Deselect All Tools, and Select One Tool,

that determine how the items in the Spline Editor header behave when a checkbox or label is selected

to activate a spline. These states are located in the Options menu in the upper-right corner of the

Spline Editor.

Select All Tools: Choosing this option activates all

splines for editing.

Deselect All Tools: Choosing this option sets all spline

checkboxes to disabled.

Select One Tool: This option is a toggle. When Select

One Tool is chosen from the menu, only one spline in

the header is active and visible at a time. Clicking on

any spline’s checkbox will set it to active, and all other

splines will be cleared. When disabled, multiple splines

can be active in the header.

The Options menu selection states

make it easier to select and deselect

all parameters in the header

Selection Groups

It is possible to save the current selection state of the splines in the header, making selection groups

that can easily be reapplied when needed. To create a selection group, right-click over any parameter

in the header or in an empty area of the graph and choose Save Current Selection from the contextual

menu. A dialog will appear to name the new selection.

To reapply the selection group, choose the selection group by name from the Set Selection menu

in the same contextual menu. Other context menu options allow selection groups to be renamed

or deleted.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Reshaping Splines Using the Toolbar

There are several ways to manipulate the shape of a spline, thereby altering the animation that spline

generates. Other than manually adjusting Bézier handles, you can quickly squish, stretch, loop,

and reverse a spline. You can also quickly change the interpolation between keyframes from the

default linear motion to more natural smooth motion. All these options are provided at the bottom of

the Spline Editor in the toolbar. The toolbar is divided into different groups for setting interpolation,

reversing splines, looping splines, time stretching, and reshaping splines.

Interpolation

Keyframes are specific frames in an animation where control points are set to exact values on a given

parameter. Interpolation is the method used to fill in the unknown values between two keyframes.

Fusion automatically interpolates between two keyframes. However, you may want to modify the

interpolation to achieve a specific style of animation. The Spline Editor includes several interpolation

methods you can choose from using the toolbar.

Interpolation buttons in the toolbar: Smooth,

Linear, Invert, Step In, and Step Out

Smooth

A smoothed segment provides a gentle keyframe transition in and out of the keyframe by slightly

extending the direction handles on the curve. This slows down the animation as you pass through the

keyframe. To smooth the selected keyframe(s), press Shift-S or click the toolbar’s Smooth button.

Smooth interpolation between keyframes

Linear

A linear segment effectively takes the shortest route between two control points, which is a straight

line. To make the selected keyframe(s) linear, press Shift-L or click the Linear button in the toolbar.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Linear interpolation between keyframes

TIP: Invert is used only for non-animated LUT splines, which are currently only available in

the LUT Editor window.

Step In/Step Out

On occasion, it is not desirable to have any interpolation between two keyframes. Instead, the value of

one keyframe may hold its value until another keyframe changes it. For these cases, use the Step In or

Step Out mode.

Step In causes the value of the previous keyframe to hold, then jump straight to the value of

the next keyframe.

Step In holds a value until the next

keyframe is reached in the comp

Step Out causes the value of the selected keyframe to hold right up to the next keyframe.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Step Out switches immediately to the

next keyframe value in a comp

Step In and Step Out modes can be set for selected keyframes by clicking on the toolbar buttons for

each mode, or by right-clicking and choosing the appropriate option from the contextual menu. The

keyboard shortcuts I and O can also be used to enable Step In and Step Out on selected keyframes.

Reversing Splines

Reverse inverts the horizontal direction of a segment of an animation spline. To apply reverse, choose

a group of points in a spline and click the Reverse button, or right-click and choose Reverse from the

contextual menu, or press the V key. The group of points is immediately mirrored horizontally in the

graph. Points surrounding the reversed selection may also be affected.

The Reverse button in the toolbar

Looping Splines

It is often useful to repeat an animated section, either infinitely or for a specified number of times, such

as is required to create a strobing light or a spinning wheel. Fusion offers a variety of ways to repeat a

selected segment.

The various Loop buttons in the toolbar

Set Loop

To repeat or loop a selected spline segment, select the keyframes to be looped. Select Set Loop

from the contextual menu or click on the Set Loop button in the toolbar. The selected section of the

spline repeats forward in time until the end of the global range, or until another keyframe ends the

repeating segment.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

A looped section in the graph

Changing and Removing the Loop

You can change the looped segment by modifying any of the keyframes or control points originally

used to create the loop. Simply select one of the originating key points, make any necessary

modifications, and the looped segment updates. To remove the loop, select the keyframes you used

to create the loop, and then click the Loop button in the toolbar.

Ping-Pong

The Ping-Pong Loop mode repeats the selected segment, reverses each successive loop, and then

repeats. Ping-pong looping can be enabled on the selected segments from the context menu or

the toolbar.

A ping-pong section in the graph

Relative Loop

The Relative Loop mode repeats the segment like the Loop, but each repetition adds upon the last

point of the previous loop so that the values increase steadily over time.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

A Relative Loop section in the graph

Looping Backward

You can choose Set Pre-Loop by right-clicking in the graph area and choosing it from the contextual

menu. This option contains the same options for looping as the Loop option buttons in the toolbar,

except that the selected segment is repeated backward in time rather than forward.

Repeating Splines X Number of Times

You can duplicate splines and repeat them a set number of times by right-clicking in the graph area

and choosing Duplicate from the contextual menu. Duplicated splines are like looped splines, except

that the selected segment repeats only a specified number of times, and each repetition is a copy

rather than an instance. Adjustments to the original segment do not alter the shape of its repetitions.

The Duplicate modes are only accessed from the Duplicate contextual menu, which reveals a

submenu with all the looping modes described above. Selecting any of these modes opens a dialog in

which the number of repetitions can be entered.

The Duplicate contextual submenu


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Gradient Extrapolation

You can choose Gradient Extrapolation by right-clicking in the graph area and choosing it from the

contextual menu. This option continues the trajectory of the last two keyframes.

The Gradient Extrapolation applied to the spline