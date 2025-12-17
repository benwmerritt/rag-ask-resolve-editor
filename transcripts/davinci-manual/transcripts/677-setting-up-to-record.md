---
title: "Setting Up to Record"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 677
---

# Setting Up to Record

Depending on how your workstation is set up, it’s possible to simultaneously record to multiple tracks

in the Fairlight page at once. How many tracks you can record to depend entirely on what hardware

you have available. This section describes the process of recording to tracks in the Fairlight page.

Patching Inputs

Before recording audio anything, you need to use the Patch Input/Output window to patch an available

audio input to a track.

DaVinci Resolve allows you to designate a full-time default input that is automatically patched to the

track input when the R (Record Arm) button is clicked or manually patching in an audio input before

record-arming it.

If you don’t have an audio interface connected, you can use your workstation’s inputs to

connect whatever audio device is set up as the default audio input on your system to the track

you want to record on.

Automatic Input Patching

The steps in this section explain how you can configure DaVinci Resolve to automatically patch in a

designated default audio input whenever you click the R (Record-Arm) button in the track header or

mixer channel of a track you want to record on.

To set up Automatic Input Patching:


Click the Fairlight menu > Patch Input/Output.


When the Patch Input/Output panel opens, select Setup I/O Names in the Options menu in the

upper-right corner. This opens the I/O Setup panel.

The Patch Input/Output Options menu


Place a checkmark in the Default column for the audio input you want to designate as the default

track input source, then close the I/O Setup panel.


Fairlight | Chapter 173 Recording

FAIRLIGHT

Default audio input selection in the I/O Setup panel

This input is automatically patched in when you record-arm any audio track using the R button in the

Track header or Mixer channel. The audio input name will appear in the channel strip’s input section.

Manual Input Patching

You can follow the steps below to manually select an input source without affecting the default audio

input you may have already set up.

To manually patch in an auto input:


Open the Patch Input/Output pane by clicking the Input button at the top of the Mixer channel

you want to record on and select Input. Alternatively, you can select Patch Input/Output from the

Fairlight menu.

Mixer channel strip Input button menu


Fairlight | Chapter 173 Recording

FAIRLIGHT


When the Patch Input/Output panel opens, select the audio input source and destination track

input. You can repeat this step until you’ve patched all the inputs you want to record from to all the

tracks you want to record to. You can patch as many inputs to as many tracks as your system can

accommodate.


Click the Patch button in the lower-right corner of the panel.

The Patch Input/Output panel with an Audio Input and Track Input selected

Arming Tracks

When you’re ready to record on a track, click the R (Record Arm) button on either the Track header or

corresponding Mixer channel.

Audio tracks cannot be record-armed unless they’ve been patched using one of the methods

explained above.

(Left) The Record Arm button activated on a Track header;

(Right) the Record Arm button activated on a channel strip


Fairlight | Chapter 173 Recording

FAIRLIGHT

Record Name Prefix

A right-click on the designated record track header has the option to set a recording name prefix to

the recordings for that track. This is a useful way to keep tabs of the various recordings required by

your project. For instance, if recording ADR you can add a prefix for each character’s recordings as in

the example below for a character named Pilot.

Right-clicking a track header reveals

the Set Track Record Name option

Example of a recording name prefix

for a character called Pilot

Choosing Where to Record Audio Clips To

The process of recording in the Fairlight page creates new clips and generates additional media on

disk. You can specify the location on disk where you want to save these recordings by opening the

Capture and Playback panel of the Project Settings. In the Capture section use the Browse button,

found underneath the “Save clips to” field, to choose a new location (a folder named “Capture” on your

scratch disk is the default location).

To choose where the new clips that are created are placed in the Media Pool, simply open the

Media Pool and select any bin in the Bin list, or create a new bin and select it if you want to put your

recordings in their own location.

User-Selectable Input Monitoring Options

The Fairlight > Input Monitor Style submenu presents five options governing how you want to monitor

inputs while recording.

�Input: You only hear the live signal being input; you never hear the contents of tracks.

�Auto: When one or more tracks are armed for recording, you hear the live input signal; on

playback you hear the contents of each track.

�Record: You only hear the live input signal while actively recording, meaning the Record button

has been pressed while one or more tracks are armed for recording. You don’t hear the input

signal while tracks are merely armed.

�Mute: You hear nothing.

�Repro: While recording, you only hear what’s just been recorded, played from the track. In

other words, you’re not listening to the live input, but you’re reviewing what’s just been recorded

as it’s recording.


Fairlight | Chapter 173 Recording

FAIRLIGHT

Recording Using the Onscreen Controls

You can record anywhere you want on the currently armed track or tracks by placing the playhead

where you want recording to begin. In this way, you can record to specific areas of your program

as you record voiceover, sound effects, foley, or other timed performances that need to fit into a

particular region of the edit.

To begin recording:


Position the playhead where you want recording to begin.


Click the Record button in the transport controls. Recording immediately begins, and the material

being recorded immediately begins drawing a waveform in real time, giving you immediate

feedback that the input you’re recording is properly connected or not, as well as where on the

currently armed track material is being recorded.

To stop recording, do one of the following:

�Click the Stop button in the transport controls.

�Press the Spacebar.

Recording and Editing Multiple

Takes Using Layering

There are two ways you can record multiple takes. You can either record them one after the other,

sequentially, and then edit them later. However, you also have the ability to record multiple takes to the

same region of the timeline, one on top of another, while at the same time preserving every take using

track layering.

In the following screenshot, multiple takes have been recorded over the same section of the timeline,

including some partial takes to correct specific phrases in the voiceover being recorded. When you

do this, the result looks like a series of cuts and overwritten clips, with the most recently recorded

segments being the ones that play back over the previously recorded segments.

Overlapping recordings with Audio Track Layers turned off

However, if you choose View > Audio Track Layers, you’ll see that all your recordings have actually

been preserved via a vertical stack of overlapping audio clips.


Fairlight | Chapter 173 Recording

FAIRLIGHT

Overlapping recordings with Audio Track Layers turned on, showing layering within the same track

The layering of audio clips in DaVinci Resolve means that the topmost superimposed clips in a layered

stack like this mutes the audio of overlapping clips that are lower in the stack.

Using layering, it’s easy to edit the best segments of the best takes, while preserving all other takes,

simply by adding edits and rearranging clips in the stack so the best parts are on top.

For more information about audio layering, see Chapter 175, “Editing Basics in the

Fairlight Page.”