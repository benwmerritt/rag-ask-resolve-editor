---
title: "Adjusting the Automation Line"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 703
---

# Adjusting the Automation Line

Once one or more keyframes are on the automation line, the resulting curve for the entire track can be

adjusted. Individual keyframes can be edited up or down using the same techniques as with adjusting

clip gain; the whole line can be adjusted, or a selection can be affected.

If you adjust the last keyframe on a line with multiple keyframe points, the line will change from that

point onwards to the newly set level.

Adjusting an individual keyframe changes the line from that point onwards.

Adjusting the Entire Line

To adjust the entire line:

�With automation view enabled, click anywhere within the track, and select all automation data on

the curve by choosing Command-A.

�Position the cursor close to the line and and the dual arrow cursor appears, allowing the level of

the entire line to be adjusted.

Select all automation to adjust the entire line

Adjusting a Selected Range

You can perform adjustments to only a specific range of the automation curve. This can be useful

when you want to make “snapshot” changes for a specific scene.

To adjust only a selected range:

�Use the Focus Mode Select tool (I-beam cursor) to select the range you want to affect.

�Position the mouse close to any area of the line, and the up/down arrow cursor appears.

�Trim the line up or down. A tooltip will appear showing the current value and a delta to the original

value, so any difference in a control’s value can be seen.

�At the bounds of the selection, “bounding keyframes” are automatically created, so the level at the

edge of the selection is preserved.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Trimming a selected range of the automation curve

TIP: Hold the Shift key when adjusting levels to maintain precision. When adjusting fader

levels this allows .1 dB accuracy, even when working with small track heights.

Drawing Automation with the Pencil Tool

The Pencil tool allows automation keyframes to be drawn freely:

�Choose the Pencil tool in the Automation toolbar, or when in Focus mode, hold down Option-Shift

to temporarily switch to the Pencil tool.

�Click the mouse and drag to draw keyframes in either direction.

Automating Switched Controls

Some automation parameters are switched (i.e., they have only fixed states). Examples of this type

of control are mutes (on or off). When adjusting switched automation, keyframes can only be at the

bottom end of the Automation view or the top.

Mute automation showing on and off states

Trimming Automation from Unity in the Mixer

Trim mode supports automation trimming from unity (Fader set to 0) in the Fairlight mixer by following

the steps below:


On the Automation toolbar, set the Automation mode to Trim.

The Automation toolbar - Trim mode


Choose a Touch mode (Latch, Snap, or Snap Latch).


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT


Click the Automation Arm button on the mixer channel or tracks you want to trim. The faders on

the armed mixer channels will turn yellow and snap to zero, and the dB Indicator above each

armed fader will read Δ0.0dB.

TIP: You can either Command-Option click the Automation Arm button to trim automation

on all tracks or Option-click the button to trim automation for a collection of tracks or

mixer channels you’ve selected.

Mixer faders set to trim automation from unity


Begin playback and move the fader above or below Δ0.0dB. The automation curve will be

trimmed, and the dB indicator will display the amount of trim as a plus or minus (+/-) value.

If you’ve chosen Snap mode, the fader will return to Δ0.0dB based on the Glide time set in Preference

> User > Fairlight > Automation.

Audio Panning to Video

Audio Panning to Video uses DaVinci Resolve’s state-of-the-art object-tracking engine to help you

quickly generate precision panning automation based on the movements of people and objects in the

Fairlight Viewer.

Audio Panning to Video offers Automatic and Manual modes of operation.

Automatic Tracking

In Automatic Tracking mode, you can select a person or object on screen, and DaVinci Resolve will

automatically process the related movement data across a selected timeline range, and then generate

the automation data.

To enable and use Automatic Tracking:


Click the Toggle Automation button to the right of the transport controls.

Toggle Automation button


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT


Click the Fairlight Viewer tools menu and choose Show Tracker Controls.

Fairlight Viewer Tools menu

The Tracker Controls will appear along the lower edge of the Viewer, and you’ll see an Auto

Tracker Object on screen.

Tracker controls

Audio Tracker Object

You can also select Show Tracker Coordinates, which provides an alpha-numerical representation

of the tracker’s current on-screen position.

Audio Tracker Object

with Coordinates


Select the target track you want to write panning automation to, and use the I-Beam tool to select

the Timeline range you want the tracking to work on.

Range Select tool

NOTE: Auto-tracking will not occur unless you select a Timeline range.


Click the Auto button in the Tracking Controls section to activate Auto Tracking.


Based on the panning movement you want to automate (horizontal or vertical), click the Left-Right

(L–R) or Down-Up (D–U) button.

TIP: The Front-Back (F-B) button is only available when the Auto button is off.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT


On the target track, click the Automation dropdown in the Track Header, then followed by Pan >

L/R Pan or Pan > U/D Pan to match your selection in the previous step.


Move the Auto Tracker Object on top of the on-screen object or person you want to track.


Click the Track button to begin the Auto-Tracking process.


Start playback to check your audio track. It should follow the object or person you selected

for tracking.

TIP: If the track is more complex, for example, a person who is changing their position

relative to the camera or may have moved out of frame, you may need to do your tracking

in sections.

In this instance, you can select an area that wasn’t tracking well, move the tracker object

into position, and track over the problem range to redo the track for that portion.

Manual Tracking

Manual mode lets you create keyframes based on the Playhead position on the Timeline, and DaVinci

Resolve will smoothly vector between the keyframes like any other automation curve data.

To enable and use Manual Tracking:


Click the Toggle Automation button to the right of the transport controls.


Select the target track that you want to write your panning automation to.


Click the Video Viewer tools menu and choose Show Tracker Controls.

The tracker controls will appear along the lower edge of the Viewer, and you’ll see a Tracker

Object on screen as a simple crosshair.

Tracker Controls manual mode

Manual Tracker Object

NOTE: The Tracker object will not appear onscreen unless an audio track

has been selected.

You can also choose to Show Tracker Coordinates.

Manual Tracker

Object with Coordinates


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT


Ensure that the Auto button is inactive in the Tracking controls. Now you’re in Manual

Tracking mode.


In the Tracking Controls, click the panning control you want to automate: Left-Right (L–R), Front-

Back (F-B), or Down-Up (D–U).


On the target track, click the Automation dropdown in the Track Header, then Pan > L/R Pan, Pan >

F/B Pan, or Pan > U/D Pan to match your selection in the previous step.

You can increase the track height if the Automation dropdown is not visible.


Move the Playhead to the Timeline location where you want the automation to start.


Write a keyframe at the current position in the video by Option-clicking the Viewer at the location

where you want to place the sound at that moment.

A corresponding Automation node is placed at the Playhead position on the automation line.


To add another keyframe, move the Playhead to another point in your timeline, Option-click the

on-screen person or object you’re tracking.

The Tracker Object jumps to that position, a keyframe is written, and a new Automation mode is

added at the Playhead position.

DaVinci Resolve will smoothly vector between the keyframes, as with any other automation

curve data.

10	 Continue creating keyframes at desired positions by repeating the previous step.

11	 To create a “bounding keyframe” to lock a position that holds the automaton line before moving to

a new position, Option-Shift-Click on a location.

12	  Start playback to check, and if needed, adjust your automation.