---
title: "Parameter Tabs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 229
---

# Parameter Tabs

Many nodes expose multiple tabs’ worth of controls in the Inspector, seen as icons at the top of the

parameter section for each node. Click any tab to expose that set of controls.

Nodes with several tabs’ worth of parameters

Keyframes Editor

The Keyframes Editor displays each node in the current composition as a stack of layers within a

miniature timeline. The order of the layers is largely irrelevant as the order and flow of connections in

the node tree dictate the order of image-processing operations. You use the Keyframes Editor to trim,

extend, or slide Loader, MediaIn, and effects nodes, or to adjust the timing of keyframes, which appear

superimposed over each effect node unless you open them up into their editable track.

The Keyframes Editor is used to adjust the timing of clips, effects, and keyframes.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Keyframes Editor Control Summary

At the top, a series of zoom and framing controls let you adjust the work area containing the layers.

These controls let you manipulate the Keyframes Editor view.

A Horizontal zoom control lets you scale the size of the editor.

�A Zoom to Fit button fits the width of all layers to the current width of the Keyframes Editor.

�A Zoom to Rect tool lets you draw a rectangle to define an area of the Keyframes

Editor to zoom into.

�A Sort pop-up menu lets you sort or filter the tracks in various ways.

�An Option menu provides access to many other ways of filtering tracks and

controlling visible options.

A timeline ruler provides a time reference, as well as a place in which you can scrub the playhead.

At the left, a track header contains the name of each layer, as well as controls governing that layer.

�A lock button lets you prevent a particular layer from being changed.

�Nodes that have been keyframed have a disclosure control, which when opened displays a

keyframe track for each animated parameter.

In the middle, the actual editing area displays all layers and keyframe tracks available in the

current composition.

At the bottom-left, Time Stretch and Spreadsheet mode controls provide additional ways

to manipulate keyframes.

At the bottom right, the Time/TOffset/TScale drop-down menu and value fields let you numerically

alter the position of selected keyframes either absolutely, relatively, or based on their distance from

the playhead.

Adjusting Clip Timings

Each Loader or MediaIn node that represents a clip used in a composition is represented as a layer

in this miniature timeline. You can edit a layer’s In or Out points by positioning the pointer over the

beginning or end of a segment and using the resize cursor to drag that point to a new location. You

can slide a layer by dragging it to the left or right, to better line up with the timing of other elements in

your composition.

The Keyframes Editor also lets you adjust the timing of elements that you’ve added from directly

within Fusion.

Adjusting Effect Timings

Each effect node also appears as a layer, just like clips. You can resize the In and Out points of an

effect layer, and slide the entire layer forward or backward in time, just like a Loader or MediaIn

layers. If you trim an effect layer to be shorter than the duration of the composition, the effect cuts in

at whichever frame the layer begins, and cuts out after the last frame of that layer, just like a clip on

a timeline.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Adjusting Keyframe Timings

When you’ve animated an effect by adding keyframes to a parameter in the Inspector, the Keyframes

Editor is used to edit the timing of keyframes easily. By default, all keyframes applied to parameters

within a particular node’s layer appear superimposed in one flat track over the top of that layer.

To edit keyframes, you can click the disclosure control to the left of any animated layer’s name in the

track header, which opens up keyframe tracks for every keyframed parameter within that layer.

Keyframe tracks exposed

Keyframe Editing Essentials

Here’s a short list of keyframe editing methods that will get you started.

Methods of adjusting keyframes:

�You can click on a single keyframe to select it.

�You can drag a bounding box over a series of keyframes to select them all.

�You can drag keyframes left and right to reposition them in time.

�You can right-click one or more selected keyframes and use commands from the drop-down menu

to change keyframe interpolation, copy/paste keyframes, or even create new keyframes.

�You can Command-drag one or more selected keyframes to drag a duplicate of them to another

position in the keyframe track.

To change the position of a keyframe using the toolbar, do one of the following:

�Select a keyframe, and then enter a new frame number in the Time Edit box.

�Choose T Offset from the Time Editor pop-up, select one or more keyframes, and enter a

frame offset.

�Choose T Scale from the Time Editor pop-up, select one or more keyframes, and enter a multiplier

added to the current playhead frame position. For instance, if the playhead is on frame 10 and the

keyframe is on frame 30, entering the TScale value of 2 will position the keyframe on frame 50.

The distance between the playhead and original keyframe is 20, so (20 x 2) = 40, which is then

added to the playhead position.

Time Stretching Keyframes

If you select a range of keyframes in a keyframe track, you can turn on the Time Stretch tool to show

a box used to squeeze and stretch the entire range of keyframes relative to one another. The Time

Stretcher changes the overall timing of a sequence of keyframes without losing the relative timing from

one keyframe to the next. Alternatively, you can turn on Time Stretch and draw a bounding box around

the keyframes you want to adjust to create a time-stretching boundary that way. Click the Time Stretch

tool again to turn it off.

Time stretching keyframes


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

The Keyframe Spreadsheet

If you turn on the Spreadsheet and then click on the name of a layer in the keyframe track, the numeric

time position and value (or values if it’s a multi-dimensional parameter) of each keyframe appear

as entries in the cells of the Spreadsheet. Each column represents one keyframe, while each row

represents a single aspect of each keyframe.

Editing keyframes in the Spreadsheet

For example, if you’re animating a motion path, then the “Key Frame” row shows the frame each

keyframe is positioned at, and the “Path1Displacement” row shows the position along the path at each

keyframe. If you change the Key Frame value of any keyframe, you’ll move that keyframe to a new

frame of the Timeline.

Spline Editor

The Spline Editor provides a more detailed environment for editing the timing, value, and interpolation

of keyframes. Using control points at each keyframe connected by splines (also called curves), you

can adjust how animated values change over time. The Spline Editor has four main areas: the Zoom

and Framing controls at the top, the Parameter list at the left, the Graph Editor in the middle, and the

toolbar at the bottom.

The Spline Editor is divided into the Zoom controls at top,

Parameter list at left, Graph Editor, and toolbar.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Spline Editor Control Summary

At the top, a series of Zoom and Framing controls let you adjust the work area containing the curves.

�Vertical and horizontal zoom controls let you scale the size of the editor.

�A Zoom to Fit button fits the width of all curves to the current width of the Spline Editor.

�A Zoom to Rect tool lets you draw a rectangle to define an area of the Spline Editor to zoom into.

A Timeline ruler provides a time reference, as well as a place in which you can scrub the playhead.

The Parameter list at the left is where you decide which splines are visible in the Graph view. By

default, the Parameter list shows every parameter of every node in a hierarchical list. Checkboxes

beside each name are used to show or hide the curves for different keyframed parameters. Color

controls let you customize each spline’s tint to make splines easier to see in a crowded situation.

The Graph view that takes up most of this panel shows the animation spline along two axes. The

horizontal axis represents time, and the vertical axis represents the spline’s value. Selected control

points show their values in the edit fields at the bottom of the graph.

Lastly, the toolbar at the bottom of the Spline Editor provides controls to set control point interpolation,

spline looping, or choose Spline editing tools for different purposes.

Choosing Which Parameters to Show

Before you start editing splines to customize or create animation, you need to choose which

parameter’s splines you want to work on.

To show every parameter in every node:

�Click the Splines Editor Option menu and choose Expose All Controls. Toggle this control off again

to go back to viewing what you were looking at before.

To show splines for the currently selected node:

�Click the Splines Editor Option menu and choose Show Only Selected Tool.

Essential Spline Editing

The Spline Editor is a deep and sophisticated environment for keyframe and spline editing and retiming,

but the following overview will get you started using this tool for creating and refining animation.

To select one or more control points:

�Click any control point to select it.

�Command-click multiple control points to select them.

�Drag a bounding box around multiple control points to select them as a group.

To edit control points and splines:

�Click anywhere on a spline to add a control point.

�Drag one or more selected control points to reshape the spline.

�Shift-drag a control point to constrain its motion vertically or horizontally.

To edit Bézier curves:

�Select any control point to make its Bézier handles visible, and drag the Bézier handles.

�Command-drag a Bézier handle to break the angle between the left and right handles.

To delete control points:

�Select one or more control points and press the Delete or Backspace key.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION