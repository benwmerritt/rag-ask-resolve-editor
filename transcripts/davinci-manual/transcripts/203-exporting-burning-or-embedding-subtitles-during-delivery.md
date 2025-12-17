---
title: "Exporting, Burning, or Embedding Subtitles During Delivery"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 203
---

# Exporting, Burning, or Embedding Subtitles During Delivery

When you’ve set up one or more subtitle tracks in a program, the Deliver page exposes a group

of Subtitle Settings at the bottom of the Video panel of the Render Settings that control if and how

subtitles or closed captions are output along with that timeline.

Available options for exporting subtitles can be found at

the bottom of the Video panel of the Render Settings

This panel has the following controls:

Export Subtitle checkbox: Lets you enable or disable subtitle/closed caption output.

Format pop-up: Provides four options for outputting subtitles/closed captions.

•	 As a separate file: Outputs each subtitle track you select as a separate file using the format

specified by the Export As pop-up. A set of checkboxes lets you choose which subtitle

tracks you want to output.

•	 Burn into video: Renders all video with the currently selected subtitle track

burned into the video.

•	 As embedded captions: Outputs the currently selected subtitle track as an embedded

metadata layer within supported media formats. There is currently support for CEA-608

closed captions within MXF OP1A and QuickTime files. You can choose the subtitle format

from the Codec pop-up that appears.

Export As: (only available when Format is set to “As a separate file”) Lets you choose

the subtitle/closed captioning format to output to. Options include IMSC1, DFXP, SRT,

and WebVTT.

Include the following subtitle tracks in the export: (only available when Format is set to

“As a separate file”) A series of checkboxes lets you turn on which subtitle tracks to output.

Codec: (only available when Format is set to “As embedded captions”) Lets you choose how

to format embedded closed captions; choices include Text and CEA-608.

NOTE: Neither analog (Line 21) nor digital (CEA-708) closed caption output via

Decklink or UltraStudio is supported at this time.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

Chapter 53

Keyframing Effects

The Edit and Cut pages also provide controls for keyframing effects that

you add to your timeline.

Contents

Keyframing Effects����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1104

Basic Keyframing in the Video Inspector������������������������������������������������������������������������������������������������������������������������������� 1105

Keyframing Motion Paths in the Timeline Viewer�������������������������������������������������������������������������������������������������������������� 1106

Keyframing in the Edit Timeline and Curve Editor������������������������������������������������������������������������������������������������������������� 1108

Keyframe Directly in the Timeline During Playback����������������������������������������������������������������������������������������������������������� 1108

The Keyframe Editor��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1109

Keyframe and Curve Editor��������������������������������������������������������������������������������������������������������������������������������������������������������������� 1111

The Keyframe Editor������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1111

The Curve Editor����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1116

Keyframable Open FX and Resolve FX������������������������������������������������������������������������������������������������������������������������������������ 1120


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

Keyframing Effects

Most parameters in the Inspector can be keyframed, in order to create animated effects such as

zooming in via the Zoom parameter, fading out via the Opacity parameter, or cropping from one side

to reveal a clip underneath via the Cropping parameters. Additionally, if you import a project from

an NLE that has keyframed sizing settings, those keyframes will be imported and exposed within

DaVinci Resolve.

The basic controls for keyframing are within the Video Inspector. Any parameter that can

be keyframed has a gray keyframe button to the right of its slider. If the playhead is on a

keyframe, this button turns orange and small navigation arrows appear to its right and left,

otherwise it stays gray.

Orange buttons in the Inspector show keyframe usage. Zoom

shows the playhead parked on the current keyframe with

additional keyframes set before and after this one as indicated

by the gray navigation arrows. Position shows the playhead

parked on the only keyframe set (orange diamond, no arrows),

and Rotation Angle shows no keyframe set (gray diamond).

Once you’ve keyframed one or more parameters within a particular group in the Inspector,

that clip displays a Keyframe icon at the far left of its name bar in the Timeline. Only keyframed

clips have this icon.

The Keyframe track button

(circled) in the Timeline,

appearing on a keyframed clip


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

Basic Keyframing in the Video Inspector

Keyframing in the Cut and Edit pages works slightly differently than when using the Keyframe Editor in

the Color page. Most simple keyframing tasks can be performed in the Inspector using three buttons

that appear to the right of any parameter that’s capable of being keyframed. It takes two keyframes at

minimum to create an animated effect.

The three keyframe controls that

appear in the Inspector, from left

to right: Previous keyframe, Create/

Delete keyframe, Next keyframe

Methods of keyframing parameters in the Inspector:

�To add a keyframe: Select a clip, open the Inspector, then move the Timeline playhead to

the frame where you want to place a keyframe, and click the Keyframe button next to the

parameter of the Inspector you want to animate. Once you’ve added at least one keyframe to a

parameter, all other adjustments you make to parameters in the Inspector, or using the onscreen

Transform/Crop controls in the Timeline Viewer add new keyframes automatically if the playhead

is at another frame.

�To move the playhead to the next or previous keyframe: Click the small left- or right-hand

arrow to either side of a parameter’s keyframe control to jump the playhead to the next or

previous keyframe. You can also press Right-Bracket ( [ ) and Left-Bracket ( ] ) to go from

keyframe to keyframe.

�To edit an existing keyframe of a parameter: Move the playhead to be on top of the keyframe

you want to edit, and then change that parameter, in the Inspector, or using the onscreen controls

of the Timeline Viewer.

Methods of changing keyframe interpolation in the Inspector:

�To change a keyframe to Ease In or Ease Out: Eased keyframes create animated changes that

begin slowly and accelerate to full speed, or slow down gradually to decelerate to a stop. This only

works when you have two or more keyframes creating an animated effect. Move the playhead to

a frame with a keyframe using the next/previous keyframe controls, then right-click the orange

keyframe button and choose Ease In, Ease Out, or Ease In and Out, depending on which keyframe

you’re editing and the effect you want to create.

�To change a keyframe to Linear: Move the playhead to a frame with a keyframe using the next/

previous keyframe controls, then right-click the orange keyframe button and choose Linear.

Methods of deleting keyframes and disabling keyframed effects:

�To delete a single keyframe: Open the Inspector, move the Timeline playhead to a frame with a

keyframe, and click the orange Keyframe button in the Inspector to delete it.

�To delete all keyframes for one parameter: Click the reset button to the right of a parameter’s

keyframe control in the Inspector.

�To delete all keyframes in a group of parameters in the Inspector: Click the reset button to the

right of a parameter group’s title bar in the Inspector.

�To disable or enable a group of parameters in the Inspector: Click the toggle control at the

left of a parameter group’s title bar in the Inspector. Orange means that group is enabled.

Gray is disabled.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

Keyframing Motion Paths

in the Timeline Viewer

If you’re keyframing a clip’s transform controls to create motion, a motion path appears when you turn

on the Transform controls using the drop-down menu at the lower left of the transport controls.

A visible motion path resulting from animated Position X and Y parameters

Each keyframed change to the Position X and Y parameters creates a control point on the surface

of the motion path, which is linear by default, creating a sharp edge. However, you can right-click

any control point and choose Smooth from the contextual menu to add Bezier handles to that

control point, which let you change the sharp angle to an adjustable curve.

Changing the linear control point into a Bezier curve

The control points making up any motion path can be dragged around at will to change the

path the selected clip will travel. Dots on the surface of the motion path indicate the velocity of

motion; dots that are closer together indicate slower motion, while dots that are farther apart

indicate faster motion. Dragging a motion path control point farther away from another one will

speed up the animation between both points, while dragging it closer will slow the animation

down, as you’re setting up the selected clip to travel a longer or shorter distance within the same

keyframed time.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

Dots on the motion path show that the left half has

slow motion, while the right half has faster motion

You can also adjust the shape of any control point’s curve by clicking to select that control point,

which exposes its Bezier handles, and then dragging the handles to adjust its curve. Once handles

have been exposed, there are a variety of methods you can use to adjust them and manipulate the

motion path.

Finally, you can adjust the acceleration of motion by adjusting the Acceleration handle on the stem

of any Bezier curve. Dragging an acceleration handle towards a control point creates an eased

keyframe, where motion slows to a stop, or begins from a stop. Dragging an acceleration handle

away from a control point creates more linear motion, where the object moves continuously

through that control point.

An acceleration handle on the Bezier handle of a curve lets you create eased

motion by dragging it in towards the control point being adjusted

Methods of adjusting the Bezier handles of motion paths:

�Drag any control point to reshape the motion path.

�Drag any Bezier handle to change the shape of the curve.

�Command-drag any Bezier handle to break the tangent between it and the opposite Bezier

handle. When you release the Command key, the two Bezier handles become locked together

again at whatever angle you created.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

To eliminate a control point on a motion path, along with its keyframe:

�Right-click any control point and choose Delete Keyframe.

To switch a control point between sharp and curved angles:

�Right-click any control point and choose Linear (for a sharp angle) or Smooth (for a curve).