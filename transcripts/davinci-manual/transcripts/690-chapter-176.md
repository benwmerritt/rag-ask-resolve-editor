---
title: "Chapter 176"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 690
---

# Chapter 176

The Fairlight Inspector

Each Timeline and Media Pool clip and every audio track or bus have settings and

properties that can be adjusted, animated, and edited in the Fairlight Inspector.

This lets you easily perform tasks, such as matching the levels or EQ of several clips

while reserving the track level for your overall mix or adjusting levels or audio effect

parameters on tracks and busses.

It is important to note that clip-based effects differ from real-time track and

bus effects in that they only apply to individual clips on the Timeline or in the

Media Pool, rather than all clips on a track.

This chapter describes how to use these controls within the Fairlight Inspector.

Contents

Clip Mode vs. Track Mode������������������������������������������������������������������������������������������������������������������������������������������������������������ 3824

Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3824

The Audio Tab������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3825

Clip Mode����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3825

Track Mode������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3829

The Effects Tab����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3830

The Transition Tab����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3831

The File Tab������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3831

File Information������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3831

Audio Configuration������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3833

Adjusting Multiple Clips in the File Tab����������������������������������������������������������������������������������������������������������������������������������� 3836

Timecode ���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3836

Adjusting Multiple Clips Simultaneously������������������������������������������������������������������������������������������������������������������������������ 3837

Animated Inspector Adjustments��������������������������������������������������������������������������������������������������������������������������������������������� 3837

Paste and Remove Attributes����������������������������������������������������������������������������������������������������������������������������������������������������� 3838

Setting Clip Volume in the Timeline���������������������������������������������������������������������������������������������������������������������������������������� 3839

Adjusting Volume������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3839

Adding and Adjusting Volume Keyframes����������������������������������������������������������������������������������������������������������������������������� 3840

Normalizing Audio Levels�������������������������������������������������������������������������������������������������������������������������������������������������������������� 3840

Paste and Remove Attributes for Clips and Tracks��������������������������������������������������������������������������������������������������������� 3842


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

Clip Mode vs. Track Mode

The Inspector includes a Clip Mode and Track Mode button to eliminate confusion about whether your

parameter property changes in the Audio tab are applied to an audio clip or a track.

(Left) the Clip mode (circled); (Right) the Track mode (circled)

�Selecting an audio clip in the Media Pool or on the Timeline activates the Clip Mode button, and

the clip name appears at the top of the Inspector, to the right of the Track Mode button.

When you select a Media Pool clip, the term “Media Pool “ appears before the clip name at the top

of the Inspector. Only the clip name will be displayed if you select a timeline clip.

The term “Media Pool “ appears before

the clip name at the top of the Inspector

�Clicking the Track Mode button while a Timeline clip is selected causes subsequent changes

in the Audio tab to apply to the corresponding Mixer channel. The clip name at the top of the

Inspector will switch to the track name.

�Clicking a track header also activates track mode.

�In either instance, the clip name at the top of the Inspector will switch to the track name.

Common Controls

Selecting an audio clip, audio track, or bus channel strip in the Mixer exposes some common audio-

specific parameters and controls in the Audio and Effects panels.

Closed and open Inspector group controls in the Fairlight page


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

These controls include:

�Enable button: A toggle control to the left of the parameter group’s name lets you disable

and re-enable every parameter within that group at once. Orange means that track’s enabled.

Gray is disabled.

�Parameter group title bar: Double-clicking the title bar of any group of parameters collapses or

opens them. Even more exciting than that, Option-double-clicking the title bar of one parameter

group collapses or opens all parameter groups at once.

�Keyframe and Next/Previous Keyframe buttons: This button lets you add or remove keyframes at

the position of the playhead to or from every single parameter within the group. When the button

is highlighted orange, a keyframe is at the current position of the playhead. When it’s dark gray,

there is no keyframe. Left and right arrow buttons let you jump the playhead from keyframe to

keyframe for further adjustment.

�Reset button: Lets you reset all parameters within that group to their default settings.

TIP: You can make “granular” adjustments to virtual sliders by holding down the Option or

Shift key while clicking in and dragging left or right within the numerical value field.

The Audio Tab

Clip Mode

When working with audio clips (Clip mode) on the Audio Timeline or Media Pool, the Audio tab offers

the controls and audio effects described below.

NOTE: Parameters for audio clips on locked tracks cannot be edited in the Inspector. For more

information on locking audio tracks, see Chapter 175, “Editing Basics in the Fairlight Page.”

Volume

The Volume control that lets you adjust the gain of that clip.

Volume control in the Inspector

Pan

This control lets you pan a selected clip. While most professional mixes will restrict panning to the

more robust panner found in the Fairlight page Mixer, this simple clip-based Pan control is useful for

editors of visuals working in the Edit page to quickly create simple panning effects to aid in a craft edit.

Dragging the slider lets you pan audio left to right. This control is centered at 0 by default.

Pan control in the Inspector


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

Voice Isolation (Resolve Studio only)

When activated, this control applies Voice Isolation.

For more information about Voice Isolation, see Chapter 181, “Fairlight FX.”

Voice Isolation control in the Inspector

Dialogue Leveler

Each audio clip in the Timeline or Media Pool has Dialogue Leveler controls that let you apply the

effect to the clip.

For more information about Dialogue Leveler, see Chapter 181, “Fairlight FX.”

Dialogue Leveler controls in the Inspector

Pitch

The Pitch control lets you alter the pitch of a clip without changing the speed. Two sliders let you

adjust clip pitch in Semi Tones (large adjustments, a twelfth of an octave) and Cents (fine adjustments,

100th of a semi tone).

Pitch control in the Inspector

Speed Change

The Speed Change control lets you alter the speed of the clip. It has the option to have the clip’s pitch

follow the adjusted speed change or maintain the original speed’s pitch.


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

Speed Change control in the Inspector

The Speed Change window has the following overall controls:

Enable button: Turns the overall Speed Change effect off and on, without resetting

the controls.

Reset button: Resets all controls of the Speed Change window to their defaults.

Direction: The Right Arrow maintains the forward direction of the waveform, the Left Arrow

reverses the direction of the waveform, and the Snowflake icon creates a freeze frame.

Speed %: A flywheel control to adjust the speed by a percentage plus or minus 100%.

Frames Per Second: A flywheel control that syncs with the Speed % control showing the

FPS relative to the speed change.

Duration: Indicates the new timing of the clip.

Ripple Sequence: When checked this moves all the media after the action to ripple edit to the

new duration.

Pitch Correction: When checked this maintains the original pitch of the clips when speed

changed. When unchecked the audio will speed up or slow down with the speed adjustment.

The slower the speed change, the lower the pitch; the higher the speed change, the higher

the pitch.

NOTE: When in the Speed Change controls, do not use the freeze frame option. This will

negatively affect the selected audio file.

Parametric Equalizer

This four-band equalizer has both graphical and numeric controls for boosting or attenuating different

ranges of frequencies within that clip, before it even gets to the EQ built into the Mixer. Each band has

controls for the filter type (Bell, Lo-Shelf, Hi-Shelf, Notch), Frequency, Gain, and Q-factor (sharpness of

the band), with the available controls for each band of EQ changing depending on the filter type.

When a channel strip’s EQ is enabled, the equalization curve that’s being applied is displayed in the

Mixer. A channel strip’s EQ settings affect all the clips on that track, so you must open the EQ window

to make those modifications.


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

The channel strip’s EQ indicator

Master EQ Controls

The Equalizer window has the following overall controls located in the upper right and

left corners.

•	 Enable button: Turns the overall EQ effect off and on, without resetting the controls.

•	 Reset button: Resets all controls of the EQ window to their defaults.

EQ Graph

This graph displays the current EQ curve with handles that correspond to each enabled

EQ band listed below. You can drag any numbered handle to boost or attenuate the range

of frequencies governed by that band, using whatever type of equalization that band has

been set to.

The EQ graph with user-draggable handles


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

Dragging the numbered handles on this graph in turn modifies the parameters of the

corresponding band, and changing each band’s parameters will also alter the EQ graph,

which serves the additional purpose of providing a graphical representation of the

equalization being applied to that track.

Bands 1 and 4

The outer two sets of band controls let you make high-pass and low-pass adjustments,

if necessary.

•	 Band enable button: Turns each band of EQ on and off.

•	 Band filter type: Bands 1 and 4 can be switched among six specific filtering options

for processing the lowest or highest frequencies in the signal. These include (from top

to bottom): Hi-Shelf, Hi-Pass, Bell, Notch, Lo-Pass, and Lo-Shelf. Bands 2 and 3 can be

switched among Lo-Shelf, Bell, Notch, and Hi-Shelf.

•	 Freq: Adjusts the center frequency of the EQ adjustment.

•	 Gain: Adjusts the amount by which the affected frequencies are impacted. Negative values

attenuate those frequencies, while positive values boost those frequencies.

Bands 2 and 3

The middle two sets of band controls let you make a wide variety of equalization adjustments.

•	 Band enable button: Turns each band of EQ on and off.

•	 Band filter type: Bands 2–5 can be switched among four different filtering options (from top

to bottom): Lo-Shelf, Bell, Notch, and Hi-Shelf.

•	 Frequency: Adjusts the center frequency of the EQ adjustment.

•	 Gain: Adjusts the amount by which the affected frequencies are affected. Negative values

attenuate those frequencies, while positive values boost those frequencies.

•	 Q Factor: Adjusts the width of affected frequencies. Lower values include a wider range of

frequencies; higher values include a narrower range of frequencies.

NOTE: This may seem obvious, but not all parameters are available for every curve type.

For instance, a Bell curve filter has Frequency, Gain, and Q adjustments, but a Lo-Pass or

Hi‑Pass filter will only have Frequency available to adjust.