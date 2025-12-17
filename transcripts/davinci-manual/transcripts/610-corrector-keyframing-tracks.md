---
title: "Corrector Keyframing Tracks"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 610
---

# Corrector Keyframing Tracks

All of the parameters governing the adjustment of color and contrast controls, as well as various

effects, Power Windows, and other adjustments are sorted into various sub-tracks within the

Corrector track.

Linear Win: Controls parameters corresponding to the Linear window.

Circ Win: Controls parameters corresponding to the Circular window.

Polygon Win: Controls parameters corresponding to the Polygon window.

PowerCurve: Controls parameters corresponding to the PowerCurve window.

Gradient Win: Controls parameters corresponding to the Gradient window.

Color Corrector: Controls all parameters found in the Camera Raw, Color Wheels,

Primary Controls, RGB Mixer, and Curves palettes.

Qualifier: Controls all parameters in the Qualifier palette.

Defocus: Controls all parameters in the Blur and Key palettes.

NR: Controls the Spatial and Temporal Noise Reduction and Motion Blur parameters

found in the Motion Effects palette.

Open FX: Controls all parameters of whichever OFX plugin is applied to the current node.

Node Format: Controls all parameters of the node sizing mode of the Sizing palette for

the current node.

ResolveFX Keyframe Tracks

The Color Page Keyframe Editor supports viewing and editing keyframes for ResolveFX and OpenFX

plugins in the Color page in one of two ways:


Color | Chapter 148 Keyframing in the Color Page

COLOR

�Plugins that have been added to a Corrector node appear within the hierarchical list of keyframe

tracks that appear within that node’s top-level keyframe track.

The keyframe track of a Resolve FX plugin added to a Corrector node

�Plugins that have been added as standalone nodes appear within a new FX track of the Keyframe

Editor. Each plugin that’s added as a separate node has a separate FX track.

The keyframe track of a Resolve FX plugin added as a standalone node

The Sizing Keyframing Tracks

The Sizing keyframing tracks govern sizing transforms and stereoscopic adjustments separately from

the color controls.

Input Sizing: Controls the Input Sizing parameters found within the Sizing palette.

Convergence: Controls the Convergence parameter in the Stereo 3D palette.

Float Window: Controls the Left, Right, Top, and Bottom Position/Rotate/Softness Floating

Windows parameters.

Auto Align: Controls the Pitch and Yaw parameters in the Stereo 3D palette.

TIP: Output Sizing can only be keyframed when you

choose Timeline mode in the Node Editor.


Color | Chapter 148 Keyframing in the Color Page

COLOR

The Ext Matte Node’s Freeform Isolation Track

If your node tree has an External Matte, the EXT MATTE node exposes a Freeform Isolation track in

the Keyframe Editor. This is useful for time offsets or Sizing repositioning of the Ext Matte image.

Automatic Keyframing

Every track in the Keyframe Editor has an Auto-Keyframing button that can be turned on or off. When

auto-keyframing is enabled for a particular track, every change made to a parameter or control

associated with that keyframe track automatically generates a keyframe. There are two ways you

can use this:

�Used with a keyframing track, auto-keyframing makes it simple to set up animated changes

to specific adjustments within a node. This is a lot easier than manually placing keyframes

one by one.

�On the other hand, turning on auto-keyframing for the Corrector track correspondingly enables

auto-keyframing for every keyframing track belonging to that node. In this case, keyframes

will automatically be placed on whatever keyframing track corresponds to the parameters or

controls you adjust.

Auto-keyframing selected for

Circular window on Node 1

When auto-keyframing is disabled, changes you make alter existing keyframes. How this alteration

works depends on the location of the playhead, and the type of keyframes in the Keyframe Editor. For

more information, see the next section.

Modifying Keyframes

Once you’ve started adding keyframes to animate changes to a grade, there are a variety of methods

available to navigate and edit these keyframes to further customize these effects. This section covers

the different ways you can navigate among, alter, and remove keyframes.

Navigating Among Keyframes

For many operations, it’s necessary to move the playhead directly on top of the keyframe you want

to modify. While you can always use the transport controls or pointer to move the playhead, there are

also commands for jumping to a specific keyframe.

To move the playhead among a series of keyframes:

�Choose Playback > Next > Keyframe (the right bracket key) or Playback > Previous > Keyframe (the

left bracket key).


Color | Chapter 148 Keyframing in the Color Page

COLOR

Moving Keyframes

If you need to change the timing of a series of keyframes, you can move the position of any keyframe,

along with whatever values that keyframe contains.

To move a single keyframe using the onscreen interface:

�Use the pointer to drag any keyframe to another location.

�Drag keyframes in a top-level Corrector or Sizing track to simultaneously move all other keyframes

on the same frame within that corrector.

To move multiple keyframes at the same time:


If necessary, open the keyframe track with the keyframes you want to move.


Drag a bounding box around the keyframes you want to move. Selected keyframes appear

highlighted in red.


Drag any of the selected keyframes to move them to the left or right.

Changing Keyframe Values

Unlike many other applications, DaVinci Resolve lets you alter keyframe values when the playhead

isn’t directly on an existing keyframe. How this works depends on the location of the playhead relative

to the keyframes that are in the Keyframe Editor, and what kind of keyframes you’re editing.

�If the playhead is to the left or on the first Dynamic keyframe: The Dynamic keyframe at or to the

right of the playhead updates with the new adjusted values.

�If the playhead is to the left or on the last Dynamic keyframe: The Dynamic keyframe at or to the

left of the playhead updates with the new adjusted values.

�If the playhead is between two Dynamic keyframes: The Dynamic keyframe to the left

of the playhead updates with the new adjusted values, but the Dynamic keyframe to the

right is unaffected.

�If the playhead is between two Static keyframes (marks): Adjustments made between two Static

keyframes always affect the keyframe to the left of the playhead. The entire segment of the clip

between that keyframe and the next is affected equally.

Changing Dynamic Attributes

By default, the transition from one Dynamic keyframe to the next is linear. However, if you need to alter

the acceleration of value interpolation from one Dynamic keyframe to the next, then you can change

that keyframe’s dynamic attributes.

To change a keyframe’s dynamic attributes:


Click to select a keyframe in the Keyframe Editor.


Right-click the selected keyframe, and choose Change Dynamic Attributes.


When the Dynamic Attributes window appears, do one or both of the following:

�Choose a new outgoing acceleration curve using the Start slider, affecting the interpolation

occurring to the right of that keyframe.

�Choose a new incoming acceleration curve using the End slider, affecting the interpolation

occurring to the left of that keyframe.

As you choose different acceleration curves, the display to the right shows the resulting

curve graph.


Color | Chapter 148 Keyframing in the Color Page

COLOR

Changing the dissolve profile


When you’re happy with the curve, click OK.

By using different Start and End values, you can make animated adjustments “ease in” or “ease out” of

a particular keyframe, to create a more gradual or abrupt transition.

TIP: The default dynamic profile start and end of each new keyframe can be set via the

Dynamics Profile values in the General Options panel of the Project Settings.

Deleting Keyframes

You have the option to delete individual keyframes, or to delete all the keyframes within a particular

grade at once.

To delete individual keyframes, do one of the following:

�Move the playhead on top of the keyframe you want to delete, then choose Mark > Delete

Keyframe (Option-]). Every keyframe at the position of the playhead is deleted.

�Using the pointer, click a keyframe in the Keyframe Editor to select it, then right-click that keyframe

and choose Delete Selected Keyframe. Only the selected keyframe is deleted.

To delete every keyframe for the current clip:

�Choose Mark > Delete All Keyframes.


Color | Chapter 148 Keyframing in the Color Page

COLOR