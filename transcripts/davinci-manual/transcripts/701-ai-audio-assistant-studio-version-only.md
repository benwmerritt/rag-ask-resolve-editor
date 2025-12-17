---
title: "AI Audio Assistant (Studio Version Only)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 701
---

# AI Audio Assistant (Studio Version Only)

With the AI Audio Assistant, DaVinci Resolve can automatically organize and color-code your tracks,

even out your dialogue levels, and adjust the Fairlight mixer faders to create a professional-quality mix

of your music, sound effects, and dialogue.

During this process, your dialogue will also be cleaned up, and if needed, Voice Isolation and

De‑Essing will be applied. Ducking will be applied to music tracks, any required automation will be

written, and the appropriate mastering and finalizing plugins will be added and adjusted to help

achieve the correct loudness level for your chosen delivery standard.

To use AI Audio Assistant:


Open a timeline containing unmixed audio. The initial fader levels really don‘t matter as Audio

Assistant will handle all fader adjustments during the mixing process.


To begin the automatic mixing process, choose Timeline > AI Tools > Audio Assistant from the

Timeline menu, select the Delivery Standard for your mix from the drop-down menu, and click the

Auto Mix button.

Audio Assistant dialog - Delivery Standard


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT


The Audio Assistant dialog changes to display the progress of the mixing process with an option

to cancel it.

Audio Assistant dialog - Mix Progress


When the mixing process has concluded, you can play back the mix and, if needed, make further

adjustments or completely undo it.

NOTE: If a track is in the wrong category, right-click the corresponding track header and

choose the correct category from the Track Category section of the contextual menu, and

then rerun the Audio Assistant.

Third-Party Control Panel Support for Mixing

DaVinci Resolve supports HUI- and MCU-compatible third-party mixing control panels with up to

eight faders, such as the Mackie MCU Pro Control Surface, connected via USB MIDI, and selectable

in the Control Panels panel of the Resolve System Preferences. Supported basic panel controls that

correspond to Fairlight features at the time of this writing include the following.

Transport controls including:

�Rewind (REW)

�Fast Forward (FF)

�Stop (double-press the Stop button for Home in the Timeline)

�Play (double-press the Play button to “play again”)

�Record (press Record+Play to begin recording if one or more tracks is record-enabled)

�Jog control (Press SCRUB and rotate the jog wheel)


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Channel Strip controls including:

�Rotary controls for panning, with Rotary Value display and Rotary touch

�Alphanumeric Track Name display

�Record button to record-enable tracks (only works if an input is patched to a track input)

�Solo, with a double-press selecting or de-selecting that track

�Mute

�Select to select the track corresponding to that channel strip

�Fader control and optional Level display

�Channel and Fader Bank buttons to move left and right among banks of channel strips

�Double-press the Fader Bank Left button to move the playhead Home in the mixer (track 1)

�Double-press the Fader Bank Right to move to the Master channel strips

Marker buttons:

�Marker to add a marker

�Pressing the Marker+Stop buttons sets Home

�Pressing the Marker+FF/REW buttons jumps the playhead forward or backward

Additional supported controls for control panels that have them include:

�Master Solo clear/restore

�Undo (pressing the Undo+Option buttons does Redo)

�Arrows to move the selection

�Zoom horizontal and vertical controls

�Audio Tracks, to turn Automation On/Off

�Write/Trim/Touch/Latch switches

�Nudge controls

�Cut, Copy, and Paste

Monitoring controls include:

�Level control

�Dim

�Mute

�Alt Speaker

For more information on third-party mixing control panel support, see the Blackmagic Support

site at www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Chapter 178

Mix Automation

The Fairlight page provides straightforward, flexible, and powerful automation

capabilities for audio mixing.

Automation data can be created graphically by drawing automation changes, or by recording on-

screen mixer or effects controls movement and changes, using a mouse or Fairlight control surface.

You can even create panning automation based on the movements of on-screen people or objects in

the Fairlight Viewer.

Once recorded, mix parameter automation for any control type—faders or sends, panning, or effects—

can be played back in perfect sync with the audio and video.

This chapter covers automation mixing using the combined controls of the on-screen mixer and timeline.

For more information on basic mixing operations, see Chapter 177, “Mixing in the

Fairlight Page.”

Contents

Creating Mix Automation�������������������������������������������������������������������������������������������������������������������������������������������������������������� 3893

Why Use Track Automation?��������������������������������������������������������������������������������������������������������������������������������������������������������� 3893

What Can Be Automated���������������������������������������������������������������������������������������������������������������������������������������������������������������� 3893

Audio Panning to Video������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3894

Drawing Automation������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3894

Recording Automation��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3894

Drawing Mix Automation��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3895

Enabling and Viewing Automation�������������������������������������������������������������������������������������������������������������������������������������������� 3895

Editing Mix Automation Curves������������������������������������������������������������������������������������������������������������������������������������������������� 3898

Using Edit Operations���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3898

Adjusting the Automation Line���������������������������������������������������������������������������������������������������������������������������������������������������� 3899

Trimming Automation from Unity in the Mixer��������������������������������������������������������������������������������������������������������������������� 3900

Audio Panning to Video������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3901

Automatic Tracking���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3901

Manual Tracking �������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3903

Recording Mix Automation����������������������������������������������������������������������������������������������������������������������������������������������������������� 3904

Automation Controls����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3905


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Creating Mix Automation

The Fairlight page includes a comprehensive toolset for creating and editing mix automation.

You can draw automation data, or record mix changes by moving on-screen controls, or you can

use IntelliTrack-powered Audio Panning to Video, which writes panning automation based on the

movements of people or objects in the Fairlight Viewer. Yes, this really is “a thing.”

Why Use Track Automation?

If you’re a video editor, you may be more familiar with using clip-based automation to make changes

to your audio mix, but this approach has limitations. Sometimes there are global changes you may

want to make to a track over the timeline or want to adjust groups of tracks at once see Chapter 179,

“Track Groups.”

When working with time-based effects like reverb or a repeating delay, you may want to dynamically

adjust the level of “trails” as the track evolves. For example, you may have a scene that changes

perspective from a larger space to a smaller one, and the room ambience or tonal quality of the

dialogue needs to change over time as the characters move through the scene.

This is where track automation techniques (whether drawing or recording the movement of controls)

can be powerful and creatively inspiring.

What Can Be Automated

Automation can be recorded for nearly every control in a Mixer channel strip, including the fader,

sends, mute, and panning. You can also automate audio plugin parameters as well.

How to Record Automation �������������������������������������������������������������������������������������������������������������������������������������������������������� 3906

Recording Automation for Multiple Tracks���������������������������������������������������������������������������������������������������������������������������� 3906

Recording Automation for Specific Individual Tracks������������������������������������������������������������������������������������������������������ 3906

Automation Preview Mode������������������������������������������������������������������������������������������������������������������������������������������������������������ 3907

Automation Active Range�������������������������������������������������������������������������������������������������������������������������������������������������������������� 3908

Viewing Automation in the Timeline��������������������������������������������������������������������������������������������������������������������������������������� 3909

Right-Click to View Automation�������������������������������������������������������������������������������������������������������������������������������������������������� 3909

The Automation Dropdown Menu��������������������������������������������������������������������������������������������������������������������������������������������� 3909

Overwriting Automation����������������������������������������������������������������������������������������������������������������������������������������������������������������� 3910

Automation Follows Edit����������������������������������������������������������������������������������������������������������������������������������������������������������������� 3910

Editing Automation����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3911

Adjusting and Deleting Automation Keyframes������������������������������������������������������������������������������������������������������������������� 3911

Clear All Track Automation������������������������������������������������������������������������������������������������������������������������������������������������������������� 3912

Fairlight > Automation Controls�������������������������������������������������������������������������������������������������������������������������������������������������� 3913

Automation – Copy/Paste/Erase������������������������������������������������������������������������������������������������������������������������������������������������� 3913

Automation – Mix List����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3914

Playing Automation��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3915


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT