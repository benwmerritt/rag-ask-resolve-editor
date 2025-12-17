---
title: "Copying and Pasting Motion Paths"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 281
---

# Copying and Pasting Motion Paths

It is possible to copy an entire motion path to the clipboard and then paste it onto another node or

path or composition.

Methods of copying and pasting motion paths:

�To copy a motion path: In the Inspector’s Modifiers tab, right-click on the path’s control header

and choose Copy from the contextual menu.

�To cut a motion path out of a node: In the Inspector, right-click on the path’s control header and

choose Cut from the contextual menu.

�To paste the copied path over another path: In the Inspector, right-click on the path’s control

header and choose Paste from the contextual menu.

When pasting a path, the old motion path will be overwritten with the one from the clipboard.

Removing Motion Paths

There are multiple ways to remove or delete a path, and they all involve a right-click contextual

menu. Removing a path modifier does not remove the object or the spline shape; it only removes the

animation from the object and the modifier from the Modifiers tab in the Inspector.


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION

To remove a path, do one of the following:

�In the Modifiers tab, right-click over the Path1 header and choose Delete from the menu.

�In the Inspector, right-click over the Center XY parameter and choose Remove Path1

from the menu.

�Right-click the center coordinate control in the viewer for the object you’re animating, and choose

Remove Path1 from the submenu of the NameOfObject; Center submenu.

Removing an entire motion path at once

Recording Motion Paths

You can animate both of the control’s spatial and temporal information at the same time using the

Record mode. This is useful when both position and speed are crucial to achieve the desired result.

Right-click on the desired path and select Record from the contextual menu. This displays a submenu

of available data that may be recorded.

Use the Record Time option in conjunction with the Draw Append mode to create complex motion

paths that will recreate the motion precisely as the path is drawn.

The time used to record the animation may not suit the needs of a project precisely. Adjust the path’s

Displacement spline in the Spline Editor to more correctly match the required motion.

Importing and Exporting Polylines

You can import and export polyline shapes into a common editable ASCII text file or its native format.

These methods are used to save a particularly useful or generic mask or path for future use or for use

in another application, such as Maya or LightWave. You can also import FXF, SSF, or Nuke shape files.

Native Format

To save a polyline shape in Fusion’s native ASCII format, right-click on the header of the Mask node

in the Inspector and select Settings > Save As from the contextual menu. Provide a name and path for

the saved file and select OK to write a file with the .setting extension. This file will save the shape of a

mask or path, as well as any animation splines applied to its points or controls.

To load the saved setting back into Fusion, you first create a new polyline of the same type, and

then select Settings > Load from the mask’s context menu or drag the .setting file directly into the

Node Editor.

If you want to move a polyline from one composition to another, you can also copy the

node to the clipboard, open your second composition, and paste it from the clipboard into the

new composition.


Fusion Fundamentals | Chapter 73 Animating with Motion Paths

FUSION

Chapter 74

Using Modifiers,

Expressions, and

Custom Controls

Some of the most powerful aspects of Fusion are the different ways it allows you to

go beyond the standard tools delivered with the application.

This chapter provides an introduction to a variety of advanced features, including Modifiers,

Expressions, and Scripting, which can help you extend the functionality and better integrate

Fusion into your studio.

Contents

The Contextual Menu for Parameters in the Inspector��������������������������������������������������������������������������������������������������� 1527

Using Modifiers������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1527

Adding the Right Modifier for the Job��������������������������������������������������������������������������������������������������������������������������������������� 1527

Adding Modifiers to Individual Parameters����������������������������������������������������������������������������������������������������������������������������� 1527

Combining Modifiers and Keyframes���������������������������������������������������������������������������������������������������������������������������������������� 1528

Publishing a Parameter�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1528

Connecting Multiple Parameters to One Modifier�������������������������������������������������������������������������������������������������������������� 1529

Adding and Inserting Multiple Modifiers��������������������������������������������������������������������������������������������������������������������������������� 1529

Performing Calculations in Parameter Fields����������������������������������������������������������������������������������������������������������������������� 1531

Using SimpleExpressions��������������������������������������������������������������������������������������������������������������������������������������������������������������� 1531

Pick Whipping to Create an Expression����������������������������������������������������������������������������������������������������������������������������������� 1533

Removing SimpleExpressions������������������������������������������������������������������������������������������������������������������������������������������������������ 1533

Customizing User Controls����������������������������������������������������������������������������������������������������������������������������������������������������������� 1534

FusionScript������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1537


Fusion Fundamentals | Chapter 74 Using Modifiers, Expressions, and Custom Controls

FUSION

The Contextual Menu for

Parameters in the Inspector

Most of the features in this chapter are accessed via a contextual menu that appears when you right-

click most parameters in the Inspector. Different contextual menus are available based on where in the

Inspector you right-click. Specifically, right-clicking over parameter names or sliders displays a feature-

rich contextual menu that can add animation, expression fields, modifiers to extend functionality, as

well as publishing and linking capabilities, allowing you to adjust multiple controls simultaneously.

Using Modifiers

Parameters can be controlled with modifiers, which are extensions to a node’s toolset. Many modifiers

can automatically create animation that would be difficult to achieve manually. Modifiers can be as

simple as keyframe animation or linking the parameters to other nodes, or modifiers can be complex

expressions, procedural functions, external data, third-party plugins, or fuses.

Adding the Right Modifier for the Job

Which modifiers are available depends on the type of parameter you’re right-clicking over. Numeric

values, text, polylines, gradients, and points each have different sets of modifiers that will work with

them, so the Modify With menu is filtered based on each parameter.

Adding Modifiers to Individual Parameters

You add modifiers to a parameter using the Inspector’s contextual menu, or by right-clicking the

onscreen control for a parameter in the viewer. Either way, a dynamic list of modifiers that are

appropriate for the selected parameters is displayed. For instance, a Perturb modifier can be added to

any slider to auto-animate the parameter by randomly wiggling the value. Once the modifier is added,

controls are displayed in the Modifiers tab to adjust the speed and amplitude of the random animation.

The Inspector contextual menu is used to add a Perturb

modifier to the Center X and Y parameters


Fusion Fundamentals | Chapter 74 Using Modifiers, Expressions, and Custom Controls

FUSION

A modifier’s controls are displayed in the Modifiers tab of the Inspector. When a selected node has a

modifier applied, the Modifiers tab will become highlighted as an indication. The tab remains grayed

out if no modifier is applied.

The Modifiers tab with two modifiers applied

Modifiers appear with header bars and header controls just like the tools for nodes. A modifier’s title

bar can also be dragged into a viewer to see its output.

Combining Modifiers and Keyframes

Modifiers that auto-animate parameters like Perturb and Shake can be combined with keyframes to

create more natural, organic looking animations. For instance, you can create the general motion path

for an element by keyframing the Center X and Y parameters, and then apply a modifier to the same

parameters to create a secondary wiggling motion.

To combine a keyframed motion path with a Perturb modifier:


Add a Transform to an image like a butterfly or spaceship.


Select the Transform node in the Node Editor.


In the Inspector, click the Keyframe button to the right of the Center X and Y parameters.


Position the butterfly or spaceship image where you want the start of the animation to begin.


Continue to move the playhead in the render range and reposition the image until you create a

figure-8 motion path.


Right-click over the Center X label in the Inspector and choose Modify With > Perturb.


Click the Modifiers tab at the top of the Inspector and adjust random, wiggling motion by setting

the Strength, Wobble, and Speed parameters while the animation plays.

Publishing a Parameter

The Publish modifier makes the value of a parameter available, so that other parameters can connect

to it. This allows you to simultaneously use one slider to adjust other parameters on the same or

different nodes. For instance, publishing a motion path allows you to connect multiple objects to the

same path.


Fusion Fundamentals | Chapter 74 Using Modifiers, Expressions, and Custom Controls

FUSION

Publish a parameter in order to

link other parameters to it

Once a parameter is published, you can right-click another parameter and choose Connect To >

[published parameter name] from the contextual menu. The two values are linked, and changing the

parameter value of one in the Modifiers tab changes the other.

Using the pick whip between two parameters provides similar linking behavior with more

flexibility. Pick whipping between parameters is covered later in this chapter.