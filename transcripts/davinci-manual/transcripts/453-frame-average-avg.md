---
title: "Frame Average [Avg]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 453
---

# Frame Average [Avg]

The Frame Average node

Frame Average Node Introduction

The Frame Average node averages together a series of frames to simulate clips shot with long shutter

speeds. Aside from motion blur-style effects, it can be useful for time warps or noise removal.

Inputs

The single input on the Frame Average node is used to connect a 2D image that will have the

averaging applied.

Input: The orange input is used for the primary 2D image that will be averaged.

Basic Node Setup

The image connected to the orange input is frame averaged based on the settings in the Inspector.

A Frame Average node blends the input image’s frames.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Inspector

The Frame Average Controls tab

Controls Tab

The Controls tab contains the parameters for setting the duration and guidance of the

averaged frames.

Sample Direction

The Sample Direction menu determines if the averaged frames are taken before the current frame,

after, or a mix of the two.

�Forward: Averages the number of frames set by the Frames slider after the current frame.

�Both: Averages the number of frames set by the Frames slider, taking frames before and after the

current frame.

�Backward: Averages the number of frames set by the Frames slider before the current frame.

Missing Frames

This control determines the behavior if a frame is missing from the clip.

�Duplicate Original: Uses the last original frame until a new frame is available.

�Blank Frame: Leaves missing frames blank.

Frames

This slider sets the number of frames that are averaged.

Keyframe Stretcher [KfS]

The Keyframe Stretcher node

Keyframe Stretcher Node Introduction

The Keyframe Stretcher node is inserted after animated nodes, so the keyframes stretch and the

comp’s duration is modified. It is used to scale the keyframes on the animation curve to the current

duration of the clip. This is particularly useful when creating title templates in Fusion for use in DaVinci

Resolve’s Edit or Cut page.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

TIP: The Keyframe Stretcher can be used on a single parameter by applying the

Keystretcher modifier.

Inputs

The single input on the Keyframe Stretcher node is used to connect a 2D image that contains

keyframe animation.

Input: The orange input is used for any node with keyframed animation. The input can be a Merge

node that is not animated but contains foreground and background nodes that are animated.

Basic Node Setup

The Keyframe Stretcher is added just before the Media Out or Saver node. All nodes that include

animation before the Keyframe Stretcher are modified if the comp changes duration.

A Keyframe Stretcher changing the animation of two text nodes.

The diagram below shows the original 50-frame animation added to a parameter. The Keyframe

Stretcher Start and End would be set to 0 and 50. The second keyframe is set at frame 10, and the

third keyframe is set at frame 40. Setting the Stretch Start to frame 11 and the Stretch End to frame 39

will keep the existing keyframes at the same speed (number of frames.) The middle will be stretched.

Original 50-frame animation

In the below example, the duration of the clip is extended to 75 frames. The first 10 frames and the last

10 frames of the animation run at the same speed as the original animation, while any animation in the

middle is stretched to fill the difference.

NOTE:  The actual Spline Editor will show only the original keyframe positions. The splines

are not changed by the Keyframe Stretcher; only the animation is changed.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Animation modified to 75 frames but stretching only the middle of the animation

Inspector

The Keyframe Stretcher Keyframes tab

Keyframes Tab

The Keyframes tab includes Source controls for setting the source duration and Stretch controls for

setting the area of the animation that gets modified.

Source Start/Source End

A source range is specified using the Source Start and Source End controls. These are typically set to

match the full range of the animation spline on the Keyframes control.

Stretch Start/Stretch End

The Stretch Start and Stretch End controls let you specify a middle zone where keyframes will be

stretched or squished. Handles outside the range will not get scaled. Any keyframes outside the

Stretch Start and End range always remain the same number of frames from the Start and End.

Any keyframe adjustments to the original control will be correspondingly scaled back to the source

curve and will match the original timing as expected.

Stretch Edges Instead

Enabling the Stretch Edges Instead checkbox overrides the Stretch Start and Stretch End controls and

stretches the edges of the animation.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Run Command [Run]

The Run Command node

Run Command Node Introduction

The Run Command node is used to execute an external command or batch file at specific points

during a render. You can choose to run a command at the start or the end of a render. Or you can have

the command execute once for each frame.

The Run Command can be used to net render other command line applications using the Fusion

Render Manager, as well as a host of other useful functions.

Inputs

The single input on the Run Command node is used to pass through a 2D image.

Input: The optional orange image input is not required for this node to operate. However, if it is

connected to a node‘s output, the Run Command will only launch after the connected node has

finished rendering. This is often useful when connected to a Saver, to ensure that the output frame has

been fully saved to disk first. If the application launched returns a non-zero result, the node will also fail.

Basic Node Setup

The Run Command node can be connected after a Saver and run once the final frame is completed.

Run Command placed after a Saver node.

Inspector

The Run Command Frame tab


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Frame Tab

The Frame tab is where the command to execute is selected and modified.

Hide

Enable the Hide checkbox to prevent the application or script from displaying a window when it

is executed.

Wait

Enable this checkbox to cause the node to wait for a remote application or tool to exit before

continuing. If this checkbox is disabled, the Fusion continues rendering without waiting for the external

application.

Frame Command

This field is used to specify the path for the command to be run after each frame is rendered. The

Browse button can be used to identify the path.

Interactive

This checkbox determines whether the launched application should run interactively, allowing

user input.

Number A (%a) and Number B (%b)

Various wildcards can be used with the frame commands; these wildcards will be substituted at render

time with the correct values.

�%a: Outputs the number from the Number A thumbwheel control.

�%b: Outputs the number from the Number B thumbwheel control.

�%t: Outputs the current frame number (without zero padding).

�%s: Substitutes using the text from the large text entry field.

If you want to add zero paddings to the numbers generated by %t, refer to the wildcard with %0x,

where x is the number of characters with which to pad the value. This also works for %a and %b.

For example, test%04t.tga would return the following values at render time:

test0000.tga

test0001.tga

test0009.tga

test0010.tga

You may also pad a value with spaces by calling the wildcard as %x, where x is the number of spaces

with which you would like to pad the value.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

The Run Command Start tab

The Run Command End tab

Start and End Tabs

The Start and End tabs contain a file browser for a command to be run when the composition starts to

render and when the composition is done rendering.

Example

To copy the saved files from a render to another directory as each frame is rendered, save the

following text in a file called copyfile.bat to your C\ directory (the root folder).

@echo off

set parm=%1 %2

copy %1 %2 set parm=

Create or load any node tree that contains a Saver. The following example assumes a Saver is

set to output D\ test0000.exr, test0001.exr, etc. You may have to modify the example to match.

Add a Run Command node after the Saver to ensure the Saver has finished saving first. Now

enter the following text into the Run Command node’s Frame Command text box:

C\copytest.bat D\test%04f.exr C\

Select the Hide Frame command checkbox to prevent the Command Prompt window from

appearing briefly after every frame.

When this node tree is rendered, each file will be immediately copied to the C\ directory as it

is rendered.

The Run Command node could be used to transfer the files via FTP to a remote drive

on the network, to print out each frame as it is rendered, or to execute a custom image-

processing tool.

The Run Command node is not restricted to executing simple batch files. FusionScript,

VBScript, Jscript, CGI, and Perl files could also be used, as just a few examples.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other miscellaneous nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION