---
title: "Editing Paint Strokes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 313
---

# Editing Paint Strokes

Once you’ve painted using the Stroke or Polyline stroke type, you can change the look of the stroke

by selecting it and updating the parameters in the Inspector. Selecting the stroke requires you to

switch to the selection tool in the Paint toolbar above the viewer. Using the Paint node’s selection tool,

you can either click once on a stroke or drag a bounding box around a stroke to select it for editing.

TIP: To select multiple strokes, you can Shift-click or Command-click to select and deselect

multiple specific strokes, or you can drag a selection box around all strokes you want to select.

Although you can make changes in the Tools tab in the Inspector, the Paint node uses both the Tools

tab and the Modifiers tab. In the Tools tab, you can create new brush strokes and select a stroke in the

viewer to edit. The Modifiers tab presents a list of all the strokes for the selected Paint node, which

makes it easy to modify any previously created paint stroke.

NOTE: Multistroke and Clone Multistroke each only appear as one item in the Modifiers tab

no matter how many strokes you create using those tools. Those two tools are not editable

after creating them.

The same controls you used in the Tools tab to create the strokes are located in the Modifier’s tab to

modify them. You can also animate each individual stroke.

The Stroke or Polyline Stroke

type can be edited by selecting

the stroke in the viewer


Fusion Fundamentals | Chapter 81 Paint

FUSION

Editing Paint Strokes in the Modifiers Tab

When you paint a stroke, the settings for that stroke appear in the Inspector’s Modifiers tab. You can

then change the settings in the Tools tab for the next stroke you are about to paint. Each time you

click, drag, and release the pointer button, you create a new stroke. Each stroke is numbered in the

Modifiers tab, where it can be selected and edited.

Once you stop painting a stroke, it’s added to the Modifiers

tab along with an additional Stroke modifier that represents

the next stroke. For instance, if you paint your first stroke,

the Modifiers tab shows your stroke as Stroke1 and then

a stroke 2 as well, which represents the next stroke you

create. You always have one more stroke in the Modifiers

tab than strokes in the viewer.

Each stroke is listed in

the Modifiers tab for editing

Deleting Strokes

There are two ways you can delete paint strokes.

To delete any individual stroke, do the following:


Select the Paint node.


Click the Modifiers tab.


Right-click over the Stroke header you want to delete and choose Delete from the menu.

To delete all paint strokes you’ve made on every frame, do one of the following:

�Click the reset button in the upper-right corner of the Inspector.

�Delete the Paint node in the Node Editor.


Fusion Fundamentals | Chapter 81 Paint

FUSION

Animating and Tracking Paint Strokes

In some ways, animating paint strokes is no different than animating any other effect in the Inspector.

Each parameter that can be animated includes a gray diamond Keyframe button along the right side.

Clicking the Keyframe button sets a keyframe on the current frame and enables auto-keyframe mode

for the parameter. However, more commonly, the paint stroke is tracked using one of Fusion’s trackers,

or for motion graphics, animated using the Write-On Start and End sliders.

Animating with Write-On Controls

The Stroke and Polyline stroke types include Write-On controls located in the Stroke controls section

of the Inspector. These Write-On controls animate the appearance of a stroke along the path. You can

animate the Write-On controls using either the Stroke Animation drop-down menu or using the Start

and End sliders.

Stroke Animation Drop-Down Menu

The Stroke Animation drop-down menu includes six options for auto-animating a paint stroke. The first

two options do not truly animate the stroke as much as set a duration. The Limited Duration option

uses the Duration slider to set the number of frames the stroke is onscreen.

To auto-animate the stroke, you can choose one of the three Write options or the Trail option.

Choosing Write On automatically creates a write-on animation. The duration is set by two keyframes

that get added when you choose Write On from the menu. The Start keyframe is set on the frame

where you first created the stroke. The End keyframe is added on the current frame when you choose

Write On from the menu. The remaining options in the menu set their Start and End keyframes similarly

but change the direction of the animation based on the menu selection.

Write-On Start and End Parameters

The Write-On Start and End parameters allow you to manually control the start point and end point

along any stroke’s path, and use keyframes to animate each parameter individually. The Start

parameter determines the point at which the stroke begins, measured as a percentage offset from the

beginning of the stroke’s path. For example, a Start value of 50 moves the starting point of the stroke

to the middle of the stroke’s path. The End parameter works the same way but from the other end of

the stroke. You can animate a stroke onscreen, creating a handwriting effect by setting keyframes for

the End parameter from 0 to 100 over several frames.

Tracking a Paint Stroke

You can animate the position of a paint stroke using any of Fusion’s trackers. For instance, if you

cloned out a flag pole from a clip, but the camera moves, you can track the flag pole and attach the

resulting path to the paint stroke.


Fusion Fundamentals | Chapter 81 Paint

FUSION

Trackers can be attached to the Center parameters of a paint stroke

Right-clicking over the Stroke’s Center control in the view allows you to apply a tracker modifier


Fusion Fundamentals | Chapter 81 Paint

FUSION

To attach a tracker to a paint stroke:


With the Paint node, select the Stroke brush type and clone out an object on a frame.


In the Paint toolbar above the viewer, click the Select tool.


Drag a selection box around the stroke to select it.


Right-click the center control on the stroke, and then choose Stroke1:Center > Modify With >

Tracker Position.


Click the Modifiers tab to view the Tracker controls.


From the Node Editor, drag the MediaIn for the image you painted on, and drag it into the Tracker

Source field in the Inspector.

Drag the MediaIn you want to track into the

Tracker Source field in the Inspector


Click the Track Forward button.


After tracking, at the bottom of the Inspector, use the Tracker 1 X Offset/Y Offset controls to

reposition the paint stroke, if necessary.

Tracking a Group of Paint Strokes

You can assign a tracker to multiple strokes by adding the stroke to a group and connecting the

tracker to the group. Instead of connecting each individual stroke, the group’s center is used for all

of the strokes. Assuming the motion of each object is consistent in the same direction, as it would be

objects “nailed to the set”, then applying the tracker to the group makes cloning multiple objects out

with a single paint node very easy.

To group paint strokes, do the following:


Drag a bounding box, Shift-click, or Command-click to select every stroke that you want to

group together.


Click the Paint Group button in the Paint toolbar.

Selecting all the strokes and then clicking the Paint Group

button collects all the strokes into a single group

The group’s onscreen controls replace the controls for each paint stroke, and the Modifiers tab in the

Inspector shows the group’s parameters. The individual strokes are still editable by selecting Show

Subgroup Controls in the Modifiers tab of the Inspector. The group then comes with a Center, Angle,

and Size control for connecting to a tracker.


Fusion Fundamentals | Chapter 81 Paint

FUSION

Use the onscreen controls, or in the Modifiers tab, right-click over

the Paint Group’s Center X label to connect the tracker