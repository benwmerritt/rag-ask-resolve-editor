---
title: "Audio Panning to Video"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 702
---

# Audio Panning to Video

IntelliTrack-powered Audio Panning to Video accelerates creativity by automatically tracking people

or objects in the Fairlight viewer to generate pan automation that matches their on-screen movements

with the precision afforded by Resolve’s state-of-the-art object tracking engine.

Drawing Automation

If you’re a video editor or audio creative, drawing mix automation data may be more straightforward

in many contexts, when making static or ramped level changes or switched changes to controls

such as a mute button, especially if you are using a mouse without the benefits of using Fairlight

hardware control.

For example, trying to finesse a real-time “performance” of fader movements or effect

parameter changes, you could select a timeline range and mute several tracks at once, “carve

out” fixed level boosts or drops on tracks at the exact point you want them to occur based on

an on-screen event or dialogue, or slowly increase the strength of a reverb applied to foley

footsteps as a character walks into a long, dark cavern.

When drawing automation, you don’t need to pay attention to the various Fairlight automation

recording modes or control enables/disables for the automation parameter you want to create

or edit; you can just draw or adjust your automaton data in the corresponding track “lane” on

the Timeline.

Recording Automation

You can also create mix automation by recording real-time on-screen fader, control movements,

or plugin parameter changes during playback. Afterwards, your “performance” can be accurately

played back. Another advantage of recording your automation is that you can intuitively “perform” the

changes against the picture as actions occur.

In this way, you can create a dynamic mix where different audio levels, pan, EQ, dynamics, and audio

processing settings change over time to fade music up or down against effects or dialogue, pan the

sound effect of a car driving by from one speaker to another, or gradually increase the strength of a

reverb effect as your character walks into that long, dark cavern.

While the recording of keyframe automation is commonly associated with either the on-screen mixer

or the Fairlight console, you can also record automation using controls found in the Inspector, or using

the controls of the Pan, EQ, and Dynamics plugin effects, thereby enabling you to record automation

for the various audio effects that you’ve applied to a track.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Drawing Mix Automation

Automaton can be drawn in the Timeline for any parameter by globally enabling automation recording

and playback, viewing a parameter to be automated, then drawing the automation in the Timeline.

Enabling and Viewing Automation

The Toggle Automation button, to the right of the transport controls, turns automation recording and

playback on and off. It must be enabled to draw or record track-based automation and to see busses

on the Timeline.

Toggle

Automation button

TIP: You can quickly enable/disable automation safe on or off for a selected group of channel

strips, or to all channel strips, by holding down the Option key (Mac) or the Alt key (Windows)

for all selected tracks or Command-Option (Mac) or Control-Alt (Windows) for all mixer

channel strips prior to performing the operation. These shortcuts can save a lot of time in

your workflow.

Automation View

Audio tracks normally display an arrangement of clips on the Timeline (“Clips View”).

In Clips View, clips can be placed or edited, and clip gain for individual clips can be adjusted,

see Chapter 176, “The Fairlight Inspector.” Effects can also be added to clips, which can be

managed in the Inspector.

Tracks can also show an Automation View, which appears when the automation button is enabled.

When active, a dropdown menu appears under the track controls in the track header. By default, the

menu will display “None,” indicating you are working with clips only; no automation data will appear.

Fairlight Automation View showing “None”


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Clicking on the dropdown menu allows you to choose an automation parameter to view or edit.

Choices are included for all parameters that can be controlled on a track, including fader, sends, pan,

mute, and built-in dynamics and EQ as well as AU or VST plugin effects.

Fairlight Automation View menu choices

For a faster workflow, you can right-click the Mixer channel control or parameter on a Fairlight FX

plugin, supported Audio Unit, or VST plugin you want to view or edit.

Once a parameter is chosen, the automation view changes so that the focus is on editing track

automation data rather than manipulating clips. The clips darken and the automation data line is

shown in light gray. When automation is drawn or recorded for the parameter, the line will change to

bright green.

NOTE: When in Automation View you can still move and trim clips, but cut/copy/paste and

delete operate on automation keyframe data only. When in Automation View, timeline-based

clip gain keyframe adjustment is not available, but overall clip gain can still be adjusted using

Volume slider in the Audio tab of the Inspector.

Vector-based Automation

Audio keyframe automation is vector-based, so levels will smoothly ramp between any 2 points on the

Timeline based on the direction of the change in control value and the time between the points.

For example, if you have a single keyframe setting fader level to 0 dB that occurs at 01:00:20:00

on the timeline, and then add a point at at 01:00:28:00 at -10.5 dB, the level will change smoothly

between 0 dB and -10 dB over the 8 seconds between the 2 points.

This allows you to draw individual keyframes to quickly construct different transition shapes, such as

fade-ins or fade-outs, with just a few points, or adjust them up or down by specific amounts quickly

and easily.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Creating Curves

Keep in mind that audio automation keyframes are not Bezier keyframes, so they only let you

create a single level adjustment at that point in time. If you make a large adjustment with only a

single new keyframe, you can end up with an abrupt level change, or level changes that don’t

have a curve you may want (exponential changes can be particularly useful on fade ins or outs

to get a natural result). You can create convex or concave shapes when drawing by adding just

a few keyframes to create your curve, or you can perform the change exactly as you want by

recording the automation (see “Recording Mix Automation” later in this chapter).

A fade out transition with 5 keyframes

for an exponential shape

Track Automation Line

Audio automation on a track is represented by a line that extends over length of the Timeline, called

the automation line, or “curve.” The level of the line can be changed by dragging, entering keyframes

one at a time, or using the Pencil tool to draw a series of keyframes.

Automation line for fader level showing multiple keyframes

Sample Accuracy: Audio keyframes allow creation of precisely placed parameter changes on

timeline tracks. On the Fairlight page, audio keyframes are sample accurate, meaning they can

be placed at any sample location with sub-millisecond precision, allowing more precision than

keyframe handling on the Cut and Edit pages. However, sample-accurate audio automation

data created on the Fairlight page can be accurately played back on the other pages.

Sample accuracy is important when working to picture as the location of audio events often

does not fall on exact frame or sub-frame boundaries.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Working with Audio Keyframes on the Timeline

To draw automated changes to any audio control:

�Enable the Automation button to see Automation View on all audio tracks.

�On the track(s) where you want to create automation, choose the parameter you wish to automate

in the Automation type dropdown menu in the track header.

�Using Focus Mode’s Multi tool allows you to draw automation using the up/down arrow cursor

(to adjust an overall curve), enter or delete keyframes one a time using modifier keys, create

different curves depending on individual keyframe position, select and delete a range of

keyframes, and more.

Adding and Deleting Individual Keyframes

Managing keyframes on the automation line is nearly identical to working with clip gain.

�To add a keyframe: Hold down the option key and a plus sign appears. Click to place a keyframe

on the automation line.

�To remove a keyframe: Hold down Command-option and a minus sign appears. Click on

keyframe to delete it.

For more information see Chapter 176, “The Fairlight Inspector.”

TIP: You can quickly flip between Clips View and Automation View using the keyboard shortcut

F4. This can be changed by using the DaVinci Resolve > Keyboard Customization dialog.

Editing Mix Automation Curves

Using Edit Operations

Normal editing operations such as cut, copy, paste, delete, and nudge can all be used on automation

keyframe data. When automation data is cut or deleted, the value at either end of the selection

is preserved.

Nudging can be very useful when fine-tuning the location of automation events.

Before and after cut or deletion


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT