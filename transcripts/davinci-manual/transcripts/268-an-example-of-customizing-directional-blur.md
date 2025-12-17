---
title: "An Example of Customizing Directional Blur"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 268
---

# An Example of Customizing Directional Blur

In the following example, let’s suppose we wanted to create a more intuitive way of controlling a linear

blur than using the Length and Angle sliders independently.

Default Directional Blur controls in the Inspector

We could use the Center input control, along with its preview control, to set an angle and distance

from directly within the viewer using expressions.


Right-click the label for the Length parameter, choose Expression from the contextual menu, and

then paste the following expression into the Expression field that appears:

-sqrt(((Center.X-.5)*(Input.XScale))^2+((Center.Y-.5)*(Input.YScale)*(Input.

Height/Input. Width))^2)


Next, right-click the label for the Angle parameter, choose Expression from the contextual menu,

and then paste the following expression into the Expression field that appears:

atan2(Center.Y-.5)/(Input.OriginalWidth/Input.X , .5-Center.X) * 180 / pi

Directional Blur controlled by the Center’s position


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

This functions fine, but the controls are confusing. The Center control doesn’t work as the center

anymore, and it should be named “Blur Vector” instead. The controls for the Length and Angle aren’t

meant to be edited, so they should be hidden away, and we’re only doing a linear blur, so we don’t

need the buttons for Radial or Zoom. We just need to choose between Linear and Centered.

Adding Another Control

For the first task, let’s rename the Center. From the Add Control window, select Center from the

ID list. A dialog will appear asking if you would like to Replace, Hide, or Change ID. We’ll choose

Replace. Now we are editing the Center input. We’ll change the Name to Blur Vector, set the Type to

Point, and the Page to Controls, which is the first tab where the controls are normally. Press OK, and

our new input will appear on our node in the Node Editor. The ID of the control is still Center, so our

SimpleExpressions did not change.

To hide the Length and Angle, we’ll run the UserControls script again. This time when we select the

Length and Angle IDs, we’ll choose Hide in the dialog. Press OK for each.

Finally, to change the options available in the Type, we have two options. We can hide the buttons and

use a checkbox instead, or we can change the MultiButton from four entries to two. Let’s try both.

�To add the checkbox, run UserControls again, but this time instead of selecting an existing ID, we’ll

type Centered into the Name. This will set the name and the ID of our input to Centered. The Type

is set to Number, and the Page is set to Controls. Now in the Type Attributes, set the Input Ctrl to

be CheckboxControl. Press OK, and now we have our checkbox. To make the new control affect

the Type, add a SimpleExpression to the Type:

iif(Centered==1, 2, 0).

Once that’s done, we can use the UserControls to hide the Type control.

�To make a new MultiButton, run the UserControl script, and add a new control ID, TypeNew. You

can set the Name to be Type, as the Names do not need to be unique, just the IDs. Set the Type to

Number, the Page to Controls, and the Input Ctrl to MultiButtonControl. In the Input Ctrl attributes,

we can enter the names of our buttons. Let’s do Linear and Centered. Type them in and hit Add for

each. Press OK, and we have our new buttons with the unneeded options removed. To make this

new control affect the original Type, add a SimpleExpression to the Type:

iif(TypeNew==0, 0, 2).

Once that’s done, we can use the UserControls to hide the original Type control.

Directional Blurs with UserControls applied


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Chapter 71

Animating in Fusion’s

Keyframes Editor

This chapter covers how you can keyframe effects in Fusion’s Inspector and how

you can edit clips, effects, and keyframes in the Keyframes Editor.

Contents

Keyframing in the Inspector��������������������������������������������������������������������������������������������������������������������������������������������������������� 1459

Removing Animation in the Inspector�������������������������������������������������������������������������������������������������������������������������������������� 1460

Attaching a Parameter to an Existing Animation Curve��������������������������������������������������������������������������������������������������� 1460

Keyframes Editor Overview���������������������������������������������������������������������������������������������������������������������������������������������������������� 1460

Keyframes Editor Tracks������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1461

The Timeline Header������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1461

The Playhead���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1462

Spreadsheet������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1462

Scaling and Panning the Timeline��������������������������������������������������������������������������������������������������������������������������������������������� 1463

Working with Segments in the Timeline�������������������������������������������������������������������������������������������������������������������������������� 1463

Moving Segments in the Timeline���������������������������������������������������������������������������������������������������������������������������������������������� 1464

Trimming Segments��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1464

Holding the First or Last Frame��������������������������������������������������������������������������������������������������������������������������������������������������� 1464

Working with Keyframes in the Timeline������������������������������������������������������������������������������������������������������������������������������� 1465

Drag and Drop Keyframe Editing������������������������������������������������������������������������������������������������������������������������������������������������ 1465

Keyframe Editing Using the Time Editor���������������������������������������������������������������������������������������������������������������������������������� 1465

The Keyframe Spreadsheet����������������������������������������������������������������������������������������������������������������������������������������������������������� 1466

Duplicating Spline Keyframes������������������������������������������������������������������������������������������������������������������������������������������������������� 1466

Time Stretching Keyframes������������������������������������������������������������������������������������������������������������������������������������������������������������ 1466

Showing Keyframe Values�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1467

Timeline Filters������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1467

Selected Filtering�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1468


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

Keyframing in the Inspector

Most parameters in most effects nodes can be keyframed in order to create animated effects such as

animated transforms, rotoscoping with splines, dynamically altering warping behaviors, and more; the

list is endless.

For convenience, a set of keyframing controls is available within the Inspector next to each

keyframable parameter. These controls are:

�A gray Keyframe button to the right each keyframable parameter. Clicking this gray button creates

a keyframe at the current position of the playhead, and turns the button orange.

�Whenever the playhead is sitting right on top of a keyframe, this button turns orange. Clicking an

orange Keyframe button deletes the keyframe at that frame and turns the button gray again.

�Small navigation arrows appear to the right and left if there are more keyframes in those

directions. Clicking on navigation arrows to the right and left of keyframes jumps the playhead to

those keyframes.

Orange Keyframe buttons in the Inspector

show there’s a keyframe at that frame

Sorting in the Timeline�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1469

The Tree Item Order Menu������������������������������������������������������������������������������������������������������������������������������������������������������������� 1469

The Sort Menu�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1469

Markers����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1470

Jumping to Markers����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1471

Renaming Markers������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1471

Show Marker List����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1471

Deleting Markers����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1471

Autosnap�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1472

Autosnap Points������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1472

Autosnap Markers������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1472

The Spreadsheet Editor������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1472

Selecting a Node to Edit������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1473

Inserting Keyframes���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1473

Selecting Multiple Nodes to Edit�������������������������������������������������������������������������������������������������������������������������������������������������� 1473

Customizing the Keyframes Editor��������������������������������������������������������������������������������������������������������������������������������������������� 1474

Line Size��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1474

Display Point Values��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1474


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

Once you’ve keyframed one or more parameters, if Show Modes/Options has been enabled,

the node containing the parameters you keyframed displays a Keyframe badge to show that

node has been animated.

A keyframed node displays a

Keyframe badge in the Node Editor

Once you’ve started keyframing node parameters, you can edit their timing in the Keyframes

Editor and/or Spline Editor.

Removing Animation in the Inspector

To remove a keyframed spline from a parameter:


Right-click the keyframe control of the parameter you want to remove animation from.


Choose Remove [Name of parameter] from the contextual menu.

Attaching a Parameter to an Existing Animation Curve

Multiple parameters can be connected to the same animation curve. This can be an invaluable

timesaver if you are identically animating different parameters in a node.

To connect a second parameter to the same animation curve:


Right-click on the second parameter you want to attach.


In the contextual menu, hover over the Connect To submenu.


In the Connect To submenu, choose the name of the animated parameter.

Keyframes Editor Overview

The Keyframes Editor is essentially a timeline view of your composition, within which each clip

and effect node in your composition is represented by a track. These tracks have the same color

coding as the nodes they represent and are labeled where appropriate. A Time Ruler at the top

indicates the timing of your composition, while numerous controls let you control the contents of the

Keyframes Editor.

The Keyframes Editor can be used for one of two things:

�To adjust the timing of elements in a project, whether they’re clips or effects. You can trim, slide,

and extend clips, adjust the timing of an animation spline, or trim the duration of an effects node.

You can freely rearrange the order of nodes in the Timeline without affecting the layering order of

your composition. All compositing operations are handled in the Node Editor, while the Keyframes

Editor manages the timing of your composition.

�To create and/or edit keyframes that you’ve applied to effects in a track-based manner, you can

retime keyframes, add and delete keyframes, and even edit keyframe values


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

The Keyframes Editor

To show the Keyframes Editor, do one of the following:

�Click the Keyframes Editor button in the UI toolbar to toggle visibility of the Keyframes Editor

on and off.

�Press F7 on the keyboard.