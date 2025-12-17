---
title: "Markers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 669
---

# Markers

The markers panel can be displayed in either thumbnail or list mode. In thumbnails mode, each marker

in your timeline corresponds to a thumbnail displaying the timecode of its location underneath it, and

the color of the marker to the left of the timecode location. In list view, each marker displays a row with

the following information; marker number, frame (showing a thumbnail), marker name, start timecode,

end timecode, duration, marker color, and notes.

The Markers panel shows a row of information for each of the markers in the Timeline.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Inspector

The Inspector’s Audio, Effects, and File panels on the Fairlight page offer features for working with

selected tracks, buses, and clips on the Audio Timeline.

TIP: You can make “granular” adjustments to virtual sliders by holding down the Option or

Shift key while clicking in and dragging left or right within the numerical value field.

The Audio Tab

The Audio tab lets you adjust the volume level of a selected track and apply and adjust Track FX.

When working with audio clips on the Audio Timeline or Media Pool, you can adjust the volume level

and pan setting of a selected clip, apply and adjust a selection of Fairlight FX and EQ, and raise or

lower the clip’s pitch.

Fairlight page - Inspector - Audio tab


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

The Audio Inspector in Clip mode (circled)

The Audio Inspector in Track mode (circled)

The Effects Tab

Audio Effects added to a track or bus via the Effects section of its Mixer channel strip or to a Timeline

clip from the Effects Library will appear in this panel.

The File Tab

This panel lets you view and edit the metadata and configuration of selected Timeline or Media

Pool clips.

For details on the Inspector for the Fairlight page, see Chapter 176, “The Fairlight Inspector.”

Clip Mode vs. Track Mode

The Inspector includes a Clip Mode and Track Mode button to eliminate confusion about whether your

parameter property changes in the Audio tab are applied to an audio clip or a track.

•	 Selecting an audio clip in the Media Pool or on the Timeline activates the Clip Mode button,

and the clip name appears at the top of the Inspector, to the right of the Track Mode button.

•	 Clicking the Track Mode button while a Timeline clip is selected causes subsequent

changes in the Audio tab to apply to the corresponding Mixer channel. The clip name at the

top of the Inspector will switch to the track name.

For details on the Fairlight Page Inspector, see Chapter 176, “The Fairlight Inspector.”


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Test Tone Settings for Generating Tone,

Noise, and Beeps

The Fairlight page has a general purpose oscillator, the settings of which you can customize by

choosing Fairlight > Test Tones Settings. This opens the Test Tones Settings window that you can

configure to generate tones, noise, or beeps using five sets of controls:

�Enable/Disable Test Tones toggle: Lets you turn the Oscillator on or off system-wide.

�Frequency control: Sets a custom frequency of oscillating tone, from 20 Hz to 15kHz.

Defaults to 1kHz.

�Frequency buttons: Lets you quickly select 100, 440, 1K, or 2K preset tones, or a continuous rising

sweep of frequencies from 20 Hz to 15kHz.

�Noise type buttons: Two buttons let you choose from White noise or Pink noise.

�Level dial: Sets the output level for the tone or noise, from –50dB to +10dB. Defaults to –15 dB.

You can set up the Oscillator to output whatever kind of tone or noise you require, and then patch it

to tracks for recording tones, or patch it to audio outputs for calibrating speakers. If you use the beep

options of the ADR panel, those are performed via the Oscillator.

To play the Test Tone out of your speakers:


Choose Fairlight > Patch Input/Output to open the Patch Input/Output window.


Choose System Generator from the Source dropdown menu, and choose Audio Outputs from the

Destination dropdown menu.


At the left, click the button of what you want to output, Osc (Oscillator) or Noise.


At the right, click the connected audio outputs that you want to patch to, and click Patch. Tone or

noise should immediately start playing out of your configured speakers. Depending on any

particular track’s I/O settings, if you have patched the Osc through a track you may need to

either Arm the track by pressing the R (record) button, or in the channel’s Path Settings press the

Thru button, to have the signal pass through for output monitoring.


To stop, select one of the patched buttons, and click Un-Patch.

To record a tone or noise from the Oscillator to an audio track:


Choose Fairlight > Patch Input/Output to open the Patch Input/Output window.


Choose System Generator from the Source dropdown menu, and choose Track Input from the

Destination dropdown menu.


At the left, click the button of what you want to output, Osc (Oscillator) or Noise.


At the right, click the connected audio outputs that you want to patch to, and click Patch. Close the

Patch Input/Output window.


Click the Arm Record (R) button in the track header of the track you patched the Oscillator to.

If your Main is properly patched to your outputs, you should hear the tone or noise, and that track’s

audio meter should reflect the level being output by the Oscillator.


Click the Record button of the transport controls to initiate recording of that tone to the patched

track. Click the Stop button or press the Spacebar to halt recording when you’re done.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Working with Timecode

Fairlight includes synchronization options that let you configure DaVinci Resolve to either chase and

synch to an external device or another application or generate and transmit timecode as an audio

signal so an external device can follow your Timeline.

You can access these settings by clicking the Fairlight menu and choosing Synchronization Settings.

Fairlight Synchronization settings

LTC and MTC Chase Sync

LTC Synchronization

If, for example, you want to configure Fairlight to chase and sync to either an external device or

computer system:


Enable External Sync.


Choose the Timecode option from the Source dropdown.


Select an appropriate audio input on your audio interface from the Timecode Audio

Input dropdown.


If needed, set your SMPTE offset. Otherwise, leave it set to +00:00:00:00.


Begin playback on the external device. Your mix in Fairlight will play back in sync with the

external device.

External Sync via LTC enabled


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

MTC Synchronization

To Configure Fairlight to chase and sync to either an app on your computer, such as a DAW, or an

external device that can transmit MIDI timecode:


Enable External Sync.


Choose the MIDI Timecode option from the Source dropdown.


Select the appropriate MIDI port from the MIDI Timecode Port menu. For example, if you want to

sync DaVinci Resolve to a DAW on your computer, choose IAC Driver Bus 1.


If needed, set your SMPTE offset. Otherwise, leave it set to +00:00:00:00.


Begin playback on the external device or DAW, and the audio from Fairlight will play back in time.

External Sync via MTC enabled

Status

This section of the Synchronized Settings dialog provides real-time information about the current

synchronization status during playback.

�Incoming Timecode: During playback, this field continually updates with the current timecode

transmitted to DaVinci Resolve.

�Transport Status: This indicator turns green to reflect stable synchronization during playback.

�Timecode Freewheel: When this checkbox is filled in, Fairlight will generate its own timecode

for a short time in case of issues with the incoming timecode. This process maintains stable and

uninterrupted synchronization.

Sync Status pane