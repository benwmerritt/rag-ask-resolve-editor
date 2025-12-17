---
title: "Modifiers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 267
---

# Modifiers

Modifiers are expressions, calculations, trackers, paths, and other mathematical components that

you attach to a parameter to extend its functionality. When a modifier is attached to a parameter, its

controls will appear separately in the Inspector Modifiers tab.

To attach a modifier:


Right-click over the parameter to which you want to attach a modifier.


Make a selection from the Modifier submenu in the contextual menu.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Animating Parameters in the Inspector

Fusion can keyframe most parameters in most nodes, in order to create animated effects such as

animated transforms, rotoscoping with splines, dynamically altering warping behaviors, and so on; the

list is endless. For convenience, a set of keyframing controls are available within the Inspector next to

each keyframable parameter. These controls are:

�A gray Keyframe button to the right each keyframable parameter. Clicking this gray button creates

a keyframe at the current position of the playhead, and turns the button orange.

�When you add a keyframe to a parameter, moving to a new frame and changing the parameter will

automatically add a keyframe at the current position.

�Whenever the playhead is sitting right on top of a keyframe, this button turns orange. Clicking an

orange Keyframe button deletes the keyframe at that frame and turns the button gray again.

�Small navigation arrows appear to the right and left if there are more keyframes in those

directions. Clicking on navigation arrows to the right and left of keyframes jumps the playhead to

those keyframes.

Orange Keyframe buttons in the Inspector

show there’s a keyframe at that frame

Once you’ve keyframed one or more parameters, If Show Modes/Options has been enabled,

the node containing the parameters you keyframed displays a Keyframe badge, to show that

node has been animated.

A keyframed node displays a

Keyframe badge in the Node Editor

Once you’ve started keyframing node parameters, you can edit their timing in the Keyframes

Editor and/or Spline Editor.

For more information about keyframing in Fusion, see Chapter 71, “Animating in Fusion’s

Keyframes Editor,” in the DaVinci Resolve Reference Manual or Chapter 9 in the Fusion

Reference Manual.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Removing Animation From a Parameter

To remove all keyframes from a parameter:


Right-click over the name of the keyframed parameter in the Inspector.


Choose Remove “node name:parameter name” from the contextual menu.

TIP: If you change the default spline type from Bézier, the contextual menu will display the

name of the current spline type.

Attaching a Parameter to an Existing Animation Curve

Multiple parameters can be connected to the same animation curve. This can be an invaluable

timesaver if you are identically animating different parameters in a node.

To connect a second parameter to the same animation curve:


Right-click on the second parameter you want to attach.


In the contextual menu, hover over the Connect To submenu.


In the Connect To submenu, choose the name of the animated parameter.

Connecting Parameters

It is often useful to connect two parameters together even without an animation curve. There are two

methods you can use.

Connecting Parameters by Publishing

If you want to tie two parameters together so adjusting one adjusts the other, you must connect them

together using the Publish menu command on the first parameter and the Connect menu command on

the second parameter.

To Publish and Connect parameters:


Right-click the name of the parameter you want to publish, and choose Publish from the

contextual menu.


Right-click on the second parameter you want to attach, and choose the name of the parameter

you just published from the Connect To submenu.

The Publish contextual menu


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

Connecting Parameters by Pick Whipping

You can also use simple expressions to link two parameters together. By using simple expressions via

pick whipping, values can be connected and combined visually without the need to publish a value

first. The pick whip is a temporary line drawn from one parameter to another in order to create a link

between the two.

To link two parameters using a pick whip:


Double-click the field of a parameter you want to pick whip to another parameter, type =, and then

press the Return key.


When Pick Whip controls appear underneath the parameter, drag a “whip” from the Add button to

the target parameter.

Now, adjusting the target parameter automatically adjusts the original parameter.

Pick whipping one parameter to another

TIP: Disabling the Auto Control Close node’s General preference, and then selecting two

nodes in the Node Editor will allow you to pick whip two parameters from different nodes.

The Expression field can further be used to add mathematical formulas to the value received from the

target parameter.

For more information on Pick Whipping and Expressions, see Chapter 74, “Using Modifiers,

Expressions, and Custom Controls,” in the DaVinci Resolve Reference Manual or Chapter 12 in

the Fusion Reference Manual.

Contextual Menus

There are two types of contextual menus you can invoke within the Inspector.

Node Contextual Menus

To display the Node Context menu from the Inspector, right-click on the Inspector header. The node’s

contextual menu includes the same menu options that are accessed by right-clicking on a node in the

Node Editor.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION

For more information see Chapter 67, “Working in the Node Editor.” in the DaVinci Resolve

Reference Manual or Chapter 5 in the Fusion Reference Manual for more information on

these options.

Parameter Contextual Menus

The contextual menu for individual parameters is accessed by right-clicking over the parameter’s

name, slider, thumbwheel, range control, button array, or other control type. For example, right-

clicking on a slider will provide the slider’s contextual menu, with options to animate the control or add

additional modifiers. Many of these options were described in this chapter.

Customizing Node Parameters

with User Controls

The user interface for each node in Fusion is designed to provide access to the parameters in a logical

manner. Sometimes, though, you may want to add, hide, or change the controls. This is commonly

done for simple expressions and macros, but it can be done for usability and aesthetic reasons for

favorites and presets.

User custom controls can be added or edited via the Edit Control dialog. Right-click the name of a

node in the Inspector (in the header bar) and choose Edit Control from the contextual menu. A new

window will appear, titled Edit Control.

The Edit Control window

In the Input attributes, you can select an existing control or create a new one, name it, define the

type, and assign it to a tab. In the Type attributes, you define the input controls, the defaults and

ranges, and whether it has an onscreen preview control. The Input Ctrl attributes box contains settings

specific to the selected node control, and the View Ctrl attributes box contains settings for the preview

control, if any.

All changes made using UserControls are stored in the node instance itself, so they can be copy/

pasted, saved to a setting, added to the Bins, or added to your favorites.


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION