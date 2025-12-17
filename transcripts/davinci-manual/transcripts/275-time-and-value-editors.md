---
title: "Time and Value Editors"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 275
---

# Time and Value Editors

The Time and Value Editors in the lower-right corner of the Spline Editor are used to change the

position and parameter value of a keyframe by entering a number into the number field for each

button. Each field can switch between three modes that help modify the time and value of a keyframe

in three precise but distinct ways. The default mode for each field takes the explicit frame number or

parameter value at which you want the keyframe set. The other modes offset and scale the keyframe’s

position or value.

Use the number fields to enter in a value or a specific

time to change the selected keyframe

Time Editor

The Time Editor is used to modify the current time of the selected keyframe. You can change the Time

mode to enter a specific frame number, an offset from the current frame, or spread the keyframes

based on the distance (scale) from the playhead. You can select one of the three modes from the Time

mode drop-down menu.

Three time editing modes are selectable

from the Time mode drop-down menu

Time

The number field shows the current frame number of the selected control point. Entering a

new frame number into the field moves the selected control point to the specified frame. If

no keyframes are selected or if multiple keyframes are selected, the field is empty, and you

cannot enter a time.

Time Offset

Selecting T Offset from the drop-down menu changes the mode of the number field to Time

Offset. In this mode, the number field offsets the selected keyframes positively or negatively

in time. An offset of either positive or negative values can be entered. For example, entering

an offset of 2 moves a selected keyframe from frame 10 to 12. If multiple keyframes were

selected in the previous example, all the keyframes would move two frames forward from their

current positions.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Time Scale

Selecting T Scale from the drop-down menu changes the mode of the number field to Time

Scale. In this mode, the selected keyframes’ positions are scaled based on the position of the

playhead. For example, if a keyframe is on frame 10 and the playhead is on frame 5, entering

a scale of 2 moves the keyframe 10 frames forward from the playhead’s position, to frame 15.

Keyframes on the left side of the playhead would be scaled using negative values.

Value Editor

The Value Editor is used to modify the selected keyframe’s parameter value using one of three Value

modes. You can change the Value mode to enter a specific value for a parameter, an offset from the

value, or to spread the values. The mode is chosen from the Value mode drop-down menu.

Three value editing modes are selectable

from the Value mode drop-down menu

Value

The number field shows the value of the currently selected keyframes. Entering a new number

into the field changes the value of the selected keyframe. If more than one keyframe is

selected, the displayed value is an average of the keyframes, but entering a new value will

cause all keyframes to adopt that value.

Value Offset

Choosing Offset from the drop-down menu sets the Value Editor to the Offset mode. In this

mode, the value for the selected keyframes are offset positively or negatively. An offset of

either positive or negative values can be entered. For example, entering a value of -2 changes

a value from 10 to 8. If multiple keyframes are selected, all the keyframes have their values

modified by -2.

Value Scale

Choosing Offset from the drop-down menu sets the Value Editor to the Scale mode. Entering

a new value causes the selected keyframes’ values to be scaled or multiplied by the specified

amount. For example, entering a value of 0.5 changes a keyframe’s value from 10 to 5.

Modifying Spline Handles

All Bézier spline keyframes have a pair of control handles to shape the spline as it passes through the

key point. These handles are only displayed when the keyframe is selected. Initially, these handles

are set to linear, creating straight line changes between keyframes. However, any control point can be

made smooth by right-clicking over it and choosing Smooth or pressing Shift-S.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Bézier splines can mix linear and smooth curves

Dragging on a keyframe’s handles adjusts the slope of the segments passing through the spline.

By default, the two control handles on a control point are locked together so that if one moves, the

one on the other side moves with it. This maintains a constant tension through the keyframe. There

are situations, however, when it is desirable to modify these control handles separately for a more

pronounced curve or effect.

To temporarily break the control handles on a Bézier spline, moving one

independently of the other:


Select the control point to be modified.


Hold down the Command key and drag one of the control handles. They will now move

independently of each other, as long as the Command key is held down.

To treat all Bézier handles as independent in the Spline Editor:

Right-click in the graph and choose Independent Handles from the Options contextual menu.

Enabling this option causes all the Bézier handles to be independent. This is the same as using the

Command key when moving a handle, except it is applied to all control points until it is disabled.

Reducing Points

When there are too many control points too close together on a spline, you can choose Reduce Points

to decrease their number, making it easier to modify the remaining points. The overall shape of the

spline is maintained as closely as possible while eliminating redundant points from the path.

To reduce the number of points on a spline:


Select the range of keyframes you want to thin out.


Right-click in the graph area and choose Reduce Points from the contextual menu.


When the Reduce Points dialog appears, drag the slider to a lower value.

You can set the slider value as low as possible as long as the spline still closely resembles the shape

of your original spline.

TIP: When the value is 100, no points will be removed from the spline. Use smaller values to

eliminate more points.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Filtering the Spline Editor

The animation splines for multiple parameters can be displayed within the Spline Editor simultaneously,

and Fusion offers several ways for you to choose which spline to view and which to edit.

A complex composition can easily contain dozens, if not hundreds, of animation curves. As a

composition grows, locating a specific spline can become more difficult. There are two ways to

filter the splines shown in the Spline Editor: display selected tools only or create a filter to show only

certain tools.

The Spline Editor includes different ways to control which splines are displayed. The majority of these

options are available in the Options menu, located in the upper-right corner of the Spline Editor panel.

The Options menu is used to control

which splines are displayed in the Spline Editor

Show Only Selected Tool: You can choose to limit the splines displayed in the Spline Editor

by showing only the splines from selected tools. Choosing this option at the top of the Options

menu displays only the splines for tools currently selected in the Node Editor.

Show All/None: The default behavior of the Spline Editor displays all the splines for all the

nodes with animated parameters. You can override this by enabling Show Only Selected Tools

in the Options menu. You can also disable the Show All setting by choosing Show None, in

which case the Spline Editor remains empty.

Expose All Controls: The Expose All Controls option is a way of not filtering the parameters.

Choosing this option displays all parameters in the Spline Editor header for all nodes in the

Node Editor. It can be a fast way of activating one of the parameters and automatically adding

an animation spline for it if one does not exist.

With a large number of nodes displayed, which themselves might have a large number of

parameters, this might lead to cluttering and slowing down the interface. This option is most

effective when used in conjunction with the Show Only Selected Tool option to limit the

number of nodes and parameters displayed and yield optimum performance.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

Follow Active: The Follow Active option is located by right-clicking in the graph and choosing

Options > Follow Active. This option provides a way to filter the splines in the graph while

not filtering the header list of tools. Where the Show Only Selected Tool option hides other

tools in the header, the Follow Active option leaves the header displaying all the tools but

automatically enables only the splines of the Active tool.

Working with Filters

Filters allow you to select the specific types and classes of tools shown in the Spline Editor and

Keyframes Editor. For example, you can make a filter that shows only particle nodes or one that only

shows color correction and brightness/contrast tools.

To create a filter:


From the Options menu, choose Create/Edit Filters.


Click the New button to create a new filter and name the new filter in the dialog box.


Enable a checkbox next to the entire category or the individual tools in each category to

determine the tools included in the filter.

Enable each tool you want to keep in the Spline Editor when the filter is selected

The Invert All and Set/Reset All buttons can apply global changes to all the checkboxes, toggling

the selected states as described.

To switch the selection state of the categories when creating a filter list:


Click the Invert All button.


After configuring the custom filter, click the Save button to close the Settings dialog and save the filter.

To enable all checkboxes or disable all checkboxes:


Click the Set/Reset All button as many times as needed until all categories are either checked or

unchecked.


After configuring the custom filter, click the Save button to close the Settings dialog and save the filter.


Fusion Fundamentals | Chapter 72 Animating in Fusion’s Spline Editor

FUSION

To apply a filter to the Spline Editor:

�Choose the desired filter by name from the Options menu. The filter applies to both the Spline

Editor and the Timeline.

Each filter you create is listed

in the Options menu

To disable a filter and show all tools in the Spline Editor again:

�Choose Show All from the Options menu.