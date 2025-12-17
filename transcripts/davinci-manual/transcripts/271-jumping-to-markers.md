---
title: "Jumping to Markers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 271
---

# Jumping to Markers

Double-clicking a marker jumps the playhead to that marker’s position.

Renaming Markers

By default, a marker uses the frame number in its name, but you can give it a more descriptive name to go

along with the frame number, making it easier to identify. To rename a marker in Fusion, right-click over

the marker and choose Rename Guide from the contextual menu. Enter a name in the dialog and click OK.

The Marker contextual menu is accessed by right-

clicking over a marker or Keyframe Editor Time Ruler.

Show Marker List

Markers can be used to jump to specific locations in a composition using the Marker List. If you right-

click over a marker or within the Keyframe Editor Time Ruler to bring up the contextual menu, you

can choose Show Marker List, or press Shift-G, to display the Marker List dialog. The Marker List is a

floating dialog that will remain on top of the main window until closed.

The Marker List shows all the current markers in the composition, listed according to their position in

time along with any custom name you’ve given them. If you double-click a marker’s name from the list,

the playhead jumps to the marker’s location.

The Marker List dialog allows you to navigate through a composition using markers.

There is a pair of checkboxes beside the names of each marker. One is for the Spline Editor, and one

is for the Keyframes Editor. By default, markers are shown in both the Spline Editor and Keyframes

Editor, but you can deselect the appropriate checkbox to hide the markers in that view.

Deleting Markers

You can delete a marker by dragging it up beyond the Time Ruler and releasing the mouse. You can

also use the marker’s contextual menu to choose Delete Marker.


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

Autosnap

To help with precisely positioning keyframes and the start and end of segments as you drag in the

Timeline, you can have them snap to a field, a frame, or to markers. The Autosnap option is accessed

through the Options section in the Keyframes Editor’s contextual menu. There are two submenu

options for autosnapping. One option controls the snapping behavior when you drag keyframes,

control points, or the starting and ending edges of segments. The other option controls the snapping

behavior of markers.

Autosnap Points

When you drag keyframes or the edges of segments, often you want them to fall on a specific frame.

Autosnap restricts the placement of keyframes and segment edges to frame boundaries by default,

but you have other options found in the contextual menu. To configure autosnapping on keyframes

and segment edges, right-click anywhere within the Keyframes Editor and choose Options > Autosnap

Points from the contextual menu. This will display the Autosnap Points submenu with options for the

snapping behavior. The options are:

None: None allows free positioning of keyframes and segment edges with subframe accuracy.

Frame: Frame forces keyframes and segment edges to snap to the nearest frame.

Field: Field forces keyframes and segment edges to snap to the nearest field,

which is 0.5 of a frame.

Guides: When enabled, the keyframes and segment edges snap to markers.

Autosnap Markers

When you click to create a new marker, the default behavior is that it will snap to the closest frame.

If you reposition the marker, it also snaps to the nearest frame as you drag. This behavior can be

changed in the Keyframes Editor’s contextual menu by choosing from the Options > Autosnap Markers

submenu. The options are:

None: Markers can be placed anywhere with subframe accuracy.

Frame: Frame forces all markers to snap to the nearest frame.

Field: Field forces all markers to snap to the nearest field.

The Spreadsheet Editor

The Spreadsheet Editor is a separate panel that can be displayed beneath the Keyframes Editor.

It is used to compactly show the numeric values of the keyframes for selected parameters in the

Keyframes Editor’s header, via a table with rows and columns, showing time and value.

To reveal the Spreadsheet Editor, click on the Spreadsheet button in the toolbar. The Spreadsheet will

split the Work Area panel and appear below the Keyframes Editor’s interface.


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

The Spreadsheet Editor showing editable data for six keyframes

Selecting a Node to Edit

To display a node’s timing in the Spreadsheet, select the node’s name in the Keyframes Editor header.

The Start and End points of the selected node will appear in the keyframe’s line of the Spreadsheet.

To edit an animation parameter in the Spreadsheet Editor, select the parameter in the Keyframes

Editor header. The keyframe row includes a box for each frame number that contains a keyframe.

The value of the keyframe is displayed in the cell below the frame number. Clicking on a cell allows

you to change the frame number the keyframe is on or the parameter’s value for that keyframe.

Clicking on the parameter’s keyframe

value allows you to change it

TIP: Entering a frame number using a decimal point (e.g., 10.25 or 15.75) allows you to set

keyframes on a subframe level to create more natural animations.

Inserting Keyframes

You can also add new keyframes to an animation by clicking in an empty keyframe cell and entering

the desired time for the new keyframe. Using the cell under the new keyframe, you can enter a value

for the parameter.

Selecting Multiple Nodes to Edit

Multiple splines and nodes can be edited together in the Spreadsheet. By default, selecting a new

parameter in the Timeline header will replace the parameter and keyframes currently listed in the

Spreadsheet Editor. Holding down Command, you can click on additional parameters on different

nodes to add them to the Spreadsheet.


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

Customizing the Keyframes Editor

There are a few ways you can change the appearance of the Keyframes Editor to better fit your needs.

All these options are found by right-clicking anywhere within the Keyframes Editor and choosing an

option from the contextual menu that appears.

Line Size

The Line Size option controls the height of each Timeline segment individually. It is often useful to

increase the height of a Timeline bar, especially when editing or manipulating complex splines.

Methods of increasing or decreasing the height of segments:

To change the hight of just one segment: Right-click anywhere within the Keyframes Editor

and choose a size from the Line Size submenu. The options are Minimum, Small, Medium,

Large, and Huge.

To change the height of all segments: Right-click anywhere within the Keyframes Editor

and choose a size from the All Line Size submenu. The options are Minimum, Small, Medium,

Large, and Huge.

Display Point Values

A more traditional view of keyframes is to view them as control points instead of vertical bars, making

them easier to select for some people. From the Timeline contextual menu, you can right-click

anywhere within the Keyframes Editor and choose Options > Display Point Values to change how

keyframes look.

The Options submenu for changing Display Point Values

Here are the two options, compared.

Keyframes displayed as bars (left), and keyframes displayed as Point Values (right).


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

Displaying Audio Waveforms

You can display a MediaIn node’s audio waveform in the Keyframes Editor and use it as a guide as you

add and move keyframes.

Waveforms are displayed in the Keyframes Editor for all MediaIn nodes

To display the audio waveform in the Keyframes Editor:


Open the Keyframes Editor.


Click the disclosure arrow next to the MediaIn node to view the audio waveform for that clip.

To change the size of an audio waveform display:


Open the Keyframes Editor.


In the Keyframes Editor, select the audio track of the waveform you want to modify.


Right-click over the audio waveform and choose Line Size > Minimum/Small/Medium/Large/Huge.


When using Fusion Studio, you can view the audio waveforms in the Keyframes Editor by

displaying the Saver node.

To view the Audio Waveform in Fusion Studio, do the following:


Open the Keyframes Editor.


Expand the Saver track to view the audio waveform.

When you want to find the precise location of an audio beat, transient, or cue, you can slowly drag

over the audio waveform to hear the audio. If you need to see more resolution in the waveform

display, you can increase the size.

To change the size of an audio waveform display:


Open the Keyframes Editor.


Right-click over the audio waveform and choose Line Size > Minimum/Small/Medium/Large/Huge.

TIP: Right-clicking a track in the Keyframes Editor and choosing All Line Size >

Minimum/Small/Medium/Large/Huge changes all the tracks and audio waveforms in the

Keyframes Editor.


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION