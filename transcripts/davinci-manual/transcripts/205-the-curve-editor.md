---
title: "The Curve Editor"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 205
---

# The Curve Editor

If you want to work with keyframes in even more detail, you can use the Curve Editor. When clicked,

the the Curve Editor expands to accommodate a large graph in which you can freely adjust both the

timing and value of selected keyframes, while also providing optional Bezier spline controls used

to create smooth curves with which to adjust the acceleration of animated changes from one value

to another.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

The Curve Editor showing the timing and values of selected parameters.

To open the Curve Editor:

Click on the Curve icon in the upper left of the Keyframe Editor.

When opened, any track that has keyframes will appear as a colored line on the graph, with

control points along the line at the keyframe position. You can hover the pointer over a line

to display its track name (and its current value) in a pop up. The line color will also match

the track color in the Keyframe Editor. You can open and close multiple parameters into the

Curve Editor using the Parameters menu that lets you choose which tracks are exposed via

checkboxes. At the bottom of the Curve Editor is a keyframe track identical to the Keyframe

Editor that displays the keyframes for the selected curve.

While you can only work on one curve at a time, you can choose which is selected for editing

by clicking any dimmed curve in the Curve Editor. Using the control points exposed by each

curve, you can edit parameters, alter keyframe timing, and change each control point’s

interpolation to create custom easing effects affecting the acceleration of change from one

keyframe to the next.

Methods of adding and selecting keyframes in the Curve Editor:

�To change which curve you’re editing: Click the Parameters menu and choose which curves you

want to expose to work on. If multiple curves are open in the Curve Editor, click any dimmed curve

in the background to highlight it for editing.

�To add new keyframes to a curve: Option-click anywhere on a curve to add a new control point.

You can also select the Add Keyframes icon at the top of the toolbar, which will let you add

multiple keyframes to a curve, just by clicking on it.

�To duplicate one or more keyframes: Make a selection of keyframes, then press Command-C to

copy, move the playhead to where you want to paste them and press Command-V. This can be a

good way to quickly loop a repetitive animated effect you’ve created.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

�To select a single keyframe: Click a single control point to select it. You can perform the same

operation on the keyframe track at the very bottom of the Curve Editor.

�To select multiple discontiguous keyframes: Command-click all control points you want to select,

whether they’re next to one another or not. You can perform the same operation on the keyframe

track at the very bottom of the Curve Editor.

�To select multiple contiguous keyframes: Click the first keyframe you want to select, and then

shift-click the last keyframe you want to select, and all keyframes between will also be selected, or

drag a bounding box within the Curve Editor around multiple keyframes to select them all at once.

You can perform the same operation on the keyframe track at the very bottom of the Curve Editor.

�To select all keyframes: If the Keyframe Editor is open and it has focus (by clicking anywhere

within it), then pressing Command-A will select all keyframes within that Keyframe Editor.

Methods of adjusting keyframes in the Curve Editor:

�To drag one or more keyframes freely on a curve: Select one or more control points and drag left

or right to retime them, and up or down to change their value. A popup will display the track name

and the updated value as you move it.

�To drag one or more keyframes on a curve in only one direction: Select one or more control

points, then hold the Shift key while dragging either vertically or horizontally to constrain keyframe

adjustment within that single direction.

Methods of changing keyframe interpolation/easing/smoothing:

�To change one or more Linear keyframe to Ease In or Ease Out: Eased keyframes create

animated changes that begin slowly and accelerate to full speed, or slow down gradually to

decelerate to a stop. This only works when you have two or more keyframes creating an animated

effect. Select one or more keyframes, then choose Ease In, Ease Out, or Ease In and Out from the

toolbar, depending on which keyframe you’re editing and the effect you want to create.

�To change one or more eased keyframes to Linear: Select one or more keyframes, then choose

Linear from the toolbar.

�To change the interpolation of multiple keyframes: Select multiple keyframes by Command-

clicking or dragging a bounding box, and then click one of the four Bezier interpolation buttons in

the Curve Editor title bar to simultaneously change the interpolation of all of them.

�To adjust a Bezier handle: Drag the Bezier handle in any direction to alter the curve.

Methods of Cutting, Copying, Pasting, and Deleting keyframes:

�To cut or copy, and paste one or more keyframes: Make a selection of keyframes and use the Cut

(Command-X) or Copy (Command-C) key shortcuts. Then, move the playhead to where you want

the first of the copied keyframes to start, and press Paste (Command-V).

�To delete one or more keyframes from a curve: Select the keyframe(s) you want to delete and

press Delete.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

Curve Editor Controls

The Curve Editor controls (L-R): Curves Editor, Keyframe Editor, Parameters, Selection, Hand, Add Keyframe,

Linear, Ease in, Ease out, Ease in and Out, Detail Zoom, Full Extend Zoom, Zoom Slider, Expand, Option Menu.

Curves Editor: Click this icon to open the Curves Editor.

Keyframe Editor: Click this icon to open the Keyframe Editor.

Parameters: Opens a checkbox to turn on or off individual curve visibility. In addition,

if you’ve added a keyframable Open FX or Resolve FX to the clip, you can select those

parameters here.

Pointer Mode: Returns to the standard mode where clicking on things with the pointer

selects them.

Hand Mode: Lets you click and drag to navigate through the Curve Editor when zoomed

in. Useful in highly detailed and complicated animations.

Add Keyframes: Turns the pointer into an Add Keyframe tool that will add a keyframe on

any curve in the Curve Editor, simply by clicking it.

Show Handle: Toggles the Bezier handle controls on or off.

Linear: Sets the curve to a direct linear progression from keyframe to keyframe.

Ease In: Sets the curve to gradually intensify the curve from the starting keyframe.

Ease In and Out: Sets the curve to gradually intensify the curve from the starting

keyframe and gradually intensify the curve towards the ending keyframe.

Ease Out: Sets the curve to gradually intensify the curve towards the ending keyframe.

Detail Zoom: Zooms the Keyframe Editor in around the playhead position.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

Full Extend Zoom: Zooms the Keyframe Editor out to show the range of the whole clip.

Zoom Slider: Lets you choose a custom zoom level for the Keyframe Editor.

Expand: Opens the Keyframe and Curves Editor in its own resizable window.

Option Menu:

�Display Time Ruler in Seconds: Shows the time ruler in HH:MM:SS:FF timecode

format based on the timeline.

�Display Time Ruler in Frames: Shows the time ruler as number of frames since the

timeline start.

�Snap Keyframes to Grid: When enabled in the Curve Editor, this snaps keyframe

control points to the playhead position.

�Show Curve Tooltips: When enabled in the Curve Editor, placing the pointer over a

curve will show its track name and value at the given point.

Keyframable Open FX and Resolve FX

Keyframes added to Resolve FX parameters appear in both the Keyframe and Curve Editor. Using the

Display Selected Parameters menu in the 3-dot option menu,  you can expose individual keyframe

tracks and curves for each keyframed parameter of an effect applied to a clip, for smoothing, retiming,

or editing.

The Open FX and Resolve FX can be adjusted in the Keyframe and

Curves Editor by selecting it in Display Selected Parameters.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT