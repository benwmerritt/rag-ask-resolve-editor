---
title: "Object Removal [ORm]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 404
---

# Object Removal [ORm]

The Object Removal node

Object Removal Node Introduction

Object Removal uses the DaVinci Neural Engine to attempt to remove an object in the frame as

automatically as possible. This node works best when removing a moving object that passes over

a temporally stable background, or dirt on the lens of a shot where the camera is in motion. Smaller

objects get better results than larger objects, but your results really depend on the footage.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Inputs

You can add masks and clean plates to the Object Removal node.

Input: The orange input is used for the primary footage you wish to remove an object from.

Clean Plate: The magenta input accepts a clean plate image source, if selected in the controls.

Mask: The green input accepts a mask shape (i.e., polygon, ellipse, rectangle, etc.) that is drawn

around the object you want to remove from the scene.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines,

basic primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input

limits the filter to only those pixels within the mask. An effects mask is applied to the tool after the

tool is processed.

Basic Node Setup

Connect the media you wish to remove the object from to the yellow Input, and then either a polygon

shape to the green Mask input, or a frame without the object to the clean plate input.

The Object Removal tool node structure. You will need either a polygon or another shape

attached to the green Mask input, or a clean plate attached to the pink clean plate input.

To setup the Object Removal:


Draw a polygon around the object that you want to remove from the scene in the Polygon node.


Track the polygon either manually, or using a tracker, to make sure that the object you want to

remove is always inside its boundaries through the duration of the clip.


Press the Scene Analysis button in the Object Removal tool controls.

These steps should accommodate most simple object removal tasks, but if there are issues,

you can adjust the parameters of the tool in the Inspector. The Object Removal tool is not

appropriate for all scenes and works best with small objects that move through the frame, not

in front of or behind other objects.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Drawing and tracking a polygon around the cyclist, then pressing the Scene Analysis

button in the Object Removal controls, removes the cyclist from the background.

Inspector

The Object Removal controls help you remove

unwanted objects from an image.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Controls

The Object Removal controls let you adjust the parameters of the object analysis.

�Show Mask Overlay: Lets you see the actual mask used, highlighted in red, for the

Object Removal.

Analysis

�Scene Analysis: Press this button to analyze the clip using the selected parameters and replace

the object with the appropriate background. You will need to press this button again if you change

any of the parameters in this section.

�Assume No Motion: If the camera has been locked off for the shot while the object moves through

it, check this box to greatly simplify the background analysis.

�Scene Mode: Provides different methods of analyzing the scene, improving the analysis of how

the area that needs to be replaced moves to best determine how to fill the hole left by the object

being removed.

Background: Analyzes the entire image except for the object region.

Boundary: Analyzes the boundary area surrounding the object region.

Object: For analyzing an object that moves with the background, like a sticker that’s on a window

while the camera moves.

�Analysis Boundary: Sets the object’s boundary size for analysis.

�Show Scene Mask Overlay: Toggles the scene mask overlay on or off, letting you see what’s

behind the mask.

Render

�Search Range: If you notice, while playing through the analyzed result, that the object removal

mask has gray fringing on some frames, you can try adjusting the “Search Range” slider, which

is the distance, in frames, from the current frame that the Object Removal plugin is searching for

replacement image detail. For example, if the Search Range is 20, it searches +/-20 frames from

the current location, or 40 frames total. The allowance of 10 frames means we look at every fourth

frame. You will generally get the best results for the smallest range that gives an acceptable result.

�Blend Mode: If the patch is successfully filled, but the result isn’t blending well with the

background, you can try changing the Blend mode. The default is Linear, which is a simple cloning

operation, but you can also choose Adaptive Blend, which can provide better results except in

certain situations where the edges of the replacement patch have a different color or brightness

than the background.

Clean Plate

�Clean Plate Source: Lets you set the source of the clean plate. Options are Gray Image, which is

effectively no source; Internal, which takes a “best guess” approach to generating a background

with which to fill the frame and integrates this with frames that could be successfully filled in; and

External, which lets you connect your own plate to the pink input from another node.

�Build Clean Plate: Executes the building of a new clean plate background based on the Clean

Plate Source parameter set.

�Show Clean Plate: Checking this box lets you see behind the mask to the clean plate behind it.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Pseudo Color [PsCl]

The Pseudo Color node

Pseudo Color Node Introduction

The Pseudo Color node provides the ability to produce variations of an image’s color based on

waveforms generated by the node’s controls. Static or animated variances of the original image can

be produced.

Inputs

There are two Inputs on the Pseudo Color node: one for an image and one for an effects mask.

Input: The orange input is used for the primary 2D image that gets its color modified.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input restricts the pseudo color to be

within the pixels of the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Pseudo Color node is not a stand-alone generator, so it must have an image input that it uses to

generate variations in colors.

Pseudo Color node applied to an image

Inspector

Pseudo Color RGBA controls


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Red/Green/Blue/Alpha Tabs

The node’s controls are separated into four identical tabs, one for each of the RGBA color channels.

Color Checkbox

When enabled, the Pseudo Color node affects this color channel.

Wrap

When enabled, waveform values that exceed allowable parameter values are wrapped to the

opposite extreme.

High and Low

High and Low determine the range to be affected by the node in a specific color channel.

Soft Edge

This slider determines the soft edge of color transition.

Waveform

This selects the type of waveform to be created by the generator. Four waveforms are available: Sine,

Triangle, Sawtooth, and Square.

Frequency

This controls the frequency of the waveform selected. Higher values increase the number of

occurrences of the variances.

Phase

This modifies the Phase of the waveform. Animating this control produces color cycling effects.

Mean

This determines the level of the waveform selected. Higher values increase the overall brightness of

the channel until the allowed maximum is reached.

Amplitude

Amplitude increases or decreases the overall power of the waveform.

Common Controls

Settings Tab

The Settings tab controls are common to all Effect nodes, so their descriptions can be found in “The

Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION