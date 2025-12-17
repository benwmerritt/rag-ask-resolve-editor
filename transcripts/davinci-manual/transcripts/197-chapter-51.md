---
title: "Chapter 51"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 197
---

# Chapter 51

Speed Effects

You can import both linear and nonlinear speed changes from other applications, or

you can create these effects from scratch in order to speed up or slow down clips

in your programs.

DaVinci Resolve has a comprehensive set of controls for creating these kinds of effects using

dedicated Retime controls, curves, and specific edit types. Once created, DaVinci Resolve also

provides different ways of processing these effects to create the smoothest possible playback.

Contents

Speed Effects and Retiming���������������������������������������������������������������������������������������������������������������������������������������������������������� 1071

Creating Freeze Frames������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1071

Creating Simple Linear Speed Effects������������������������������������������������������������������������������������������������������������������������������������ 1072

Speed Change Controls in the Video Inspector���������������������������������������������������������������������������������������������������������������� 1073

Clip Retiming Controls���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1074

Retiming an Entire Clip���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1074

Rippling or Overwriting the Timeline When Using Retime��������������������������������������������������������������������������������������������� 1075

Reading Clip Speed Arrows����������������������������������������������������������������������������������������������������������������������������������������������������������� 1075

Creating Variable Speed Effects Using the Retime Controls���������������������������������������������������������������������������������������� 1075

Closing Retime Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1078

Using Retime Curves������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1078

Speed Effect Processing����������������������������������������������������������������������������������������������������������������������������������������������������������������� 1081

Optical Flow Quality Settings Affecting Speed Effects��������������������������������������������������������������������������������������������������� 1082


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT

Speed Effects and Retiming

Speed effects describe any effect that speeds up, slows down, or otherwise changes the

playback speed of clips in the Timeline. There are four basic ways you can create speed effects in

DaVinci Resolve.

�Importing speed effects: DaVinci Resolve is capable of reading linear speed effects from

imported EDL, AAF, and XML projects, and nonlinear speed effects from XML and AAF project

files. When speed effects are present, DaVinci Resolve plays clips at the specified speed.

You can also create speed effects of your own using controls in the Edit page. There are two

methods of adjusting clip speed: using the Change Speed dialog, and using the Retiming

effect in the Timeline.

�Creating speed effects using Fit to Fill edits: You can also change a clip’s speed in the Timeline

by editing it using the Fit to Fill command, which retimes the clip to fit into an arbitrary duration in

the Timeline of your choosing. For more information on using Fit to Fill, see Chapter 39, “Three-

and FourPoint Editing.”

�Creating freeze frames: You can use the freeze frame command to turn an entire clip into a freeze

frame of a frame intersecting the playhead.

�Creating simple linear speed effects: You can create simple fast or slow-motion speed effects

by using the Change Clip Speed command, or by using the left and right handles of the Retime

controls in the Timeline. Both of these methods are described in this section.

�Creating variable speed effects: You can create much more complex variable speed effects,

where the same clip speeds up or slows down multiple times by different amounts, using either

the Retime controls, or one of the two different speed curves that are available. These methods

are also covered later in this section.

Speed Effects and Audio

Any of the methods of creating linear speed effects that are available in DaVinci Resolve,

including the Change Clip Speed command, the Retime controls, and the Fit to Fill edit, will

retime a clip’s audio, without pitch correction on Linux and Windows, and with pitch correction

on Mac OS X (Yosemite and above), along with its video. However, audio that accompanies

variable speed effects will be muted.

Creating Freeze Frames

There are a few ways you can create a freeze frame, but the fastest is to position the playhead over

the frame you want to be the freeze frame, and choose Clip > Freeze Frame, or press Shift-R. The

entire clip becomes a freeze frame of the frame you parked the playhead over.

If you want to disable the freeze frame effect, you can select the clip and use the Remove Attributes

dialog to remove the speed effect, or you can simply open the Change Clip Speed dialog and turn the

Freeze Frame checkbox off.


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT

Creating Simple Linear Speed Effects

If all you need to do is to make a clip play in slow motion, speed it up, reverse the clip, or create

a freeze frame, you can apply a simple speed effect using either the browser or the Change

Speed dialog.

To change a clip’s speed, do one of the following:

�Select a clip, choose Clip > Change Clip Speed, and use the controls of the

Edit Speed Change dialog.

�Right-click a clip in the Timeline, choose Change Clip Speed, and use the controls of the

Edit Speed Change dialog.

�You can change the speed of multiple selected clips at the same time using either the Inspector or

the Change Clip Speed dialog box.

Change Clip Speed operations have the following options:

�Change Clip Speed parameters: Changes the speed of the selected clip by whatever percentage,

frame rate, or duration you like.

�Ripple Sequence checkbox: If you want the speed change you’re about to make to ripple the

Timeline, pushing or pulling all clips following the current one to accommodate the clip’s new size,

then turn on the checkbox.

Speed effect parameters shown in the Speed dialog

�Reverse Speed checkbox: Clicking this box sets the current speed to a negative value, reversing

the motion of the clip.

�Freeze Frame checkbox: Changes the entire clip to a freeze frame of whichever frame is at the

current position of the playhead.


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT

�Pitch Correction checkbox: Checking this box will perform pitch correction on the audio attached

to the clip so that while the audio duration is changed to match the picture speed, it will still sound

natural. Be aware that pitch correction on large speed adjustments may not sound as good as

pitch corrections made to small speed adjustments.

�Maintain Timing/Stretch to fit radio buttons: Choosing Maintain Timing leaves any keyframes

within the clip locked at their original position, while choosing Stretch Keyframes results in all

Composite, Transform, and Cropping keyframes being compressed or stretched by the same

percentage as the clip during a speed change.

Speed Change Controls

in the Video Inspector

You can also change the speed of your clip directly in the Video Inspector’s Speed Change controls.

This method has the benefit of being available in both Cut and Edit pages.

�Direction: Selects the desired motion of the clip, forward, backward, or freeze frame.

�Speed %: Adjusting this slider changes the clips motion on a percentage basis.

This value can be keyframed.

�Frames Per Second: Adjusting this slider changes the clips motion by increasing or decreasing

the number of frames per second to play the clip back at. This value can be keyframed.

�Duration: You can directly select how long you want the clip to be by setting a specific duration

here in HH:MM:SS:FF format. This will then automatically adjust the speed of the clip to playback

all frames in that exact amount of time.

�Ripple Sequence checkbox: If you want the speed change you’re about to make to ripple the

Timeline, pushing or pulling all clips following the current one to accommodate the clip’s new size,

then turn on the checkbox.

�Pitch Correction checkbox: Checking this box will perform pitch correction on the audio attached

to the clip so that while the audio duration is changed to match the picture speed, it will still sound

natural. Be aware that pitch correction on large speed adjustments may not sound as good as

pitch corrections made to small speed adjustments.

The Speed Change controls in the Video Inspector


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT

Clip Retiming Controls

Another method of altering clip speed in the Timeline is to apply the Retime effect. This method of

clip retiming provides a convenient control overlay that you can use to adjust clip speed directly in the

Timeline, and it also provides the controls that are needed for creating variable-speed effects.

To expose the Retime controls on a clip:

Select a clip, and choose Clip > Retime Controls (Command-R).

Right-click a clip and choose Retime Clip from the contextual menu.

The Retime controls appear over that clip in the Timeline. They consist of a Retime control track

running along the top of the clip with arrows that indicate the speed and direction of playback

(the default blue right-facing arrows indicate normal 100% playback) and a Clip Speed pop-up menu at

the bottom center of the clip, which also shows the current speed of the clip.

The Speed effect controls in the Timeline

Retiming an Entire Clip

The simplest way of using the Retiming effect is to change the playback speed of the entire clip, in the

process rippling the rest of the Timeline to the right of the retimed clip as you increase its duration by

stretching or compressing its duration.

To retime a clip by dragging:

Move the pointer to the left or right edge of the Speed Change name bar on top of the clip, and when

it turns into a Retime cursor, drag either side to stretch or squeeze the clip to retime it.

To retime a clip by specific amounts:


Select a clip and press Command-R.


Click the pop-up next to the speed percentage text at the bottom of the clip.


Do one of the following:

�Choose a new playback speed from the Change Speed submenu.

�Choose reverse segment to make the clip play in reverse. Reverse speed is shown in the Retime

control track as arrows facing left, instead of right.

To return a clip to its original speed:

Click the pop-up next to the speed percentage text at the bottom of the clip,

and choose Reset to 100%.


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT