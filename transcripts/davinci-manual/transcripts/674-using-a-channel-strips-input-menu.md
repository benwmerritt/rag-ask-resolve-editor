---
title: "Using a Channel Strip’s Input Menu"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 674
---

# Using a Channel Strip’s Input Menu

The Input dropdown menu at the top of each track’s channel strip in the mixer provides some

shortcuts for patching different inputs and busses to the tracks of your mix. Each option in this

menu makes the Patch Input/Output window appear with various Source and Destination selections

automatically set up.

Input

The Patch Input/Output window appears set up to let you patch different inputs (such as the

system audio input) to the tracks of the timeline. This makes it fast for setting up audio inputs in

preparation for recording.

Bus

A shortcut to open the Patch Input/Output window (discussed previously in this chapter) that lets you

patch Bus Out or Bus Sends to Timeline track channels.

Path Settings

This opens the Path Settings window for the track, which contains controls for adjusting the input level

of audio signals coming from an input/output device.

The Path Settings window showing audio inputs and track inputs

These parameters are as follows:

Mic/Inst

Controls will only appear on this panel if you have connected channels 1 or 2 of a Fairlight SX36 audio

interface to your system. If connected, you can remotely control all of the options (including level) for

the mic/instrument inputs of the SX36 if they are assigned to the channel. If there is no connection to

an SX36, the area is empty.

Record Level

�Record: This button is linked and identical to the Record Enable button on the channel strip; here

for convenience. If you hit one, it will enable the other.

�Thru: Lets the input signal to pass into the mixer without enabling a record path. This is ideal when

you want a source signal to always be available and just want to monitor it.

�Record Level: Allows you to apply a digital gain adjustment to the record path to disk, post the

output of your audio interface’s analog-to-digital converter.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

TIP: The mixer channel in question can also be switched to Thru mode by Command-

clicking the Track Arm button, in either the Mixer or Track Header. The button will turn

green and ’T’ will be displayed within it.

Normally, this control should be left at 0.0 (no change, unity gain), as it affects the level you are

recording to disk. It is best practice to use the level controls on your audio interface to control the

input level into DaVinci Resolve in order to maximize audio fidelity. However, there might be a time

where you need a bit more level, or may not have access to an audio interface’s controls, and in

those cases you can adjust the input.

Trim

�Polarity: This button inverts the polarity of the signal coming into the channel strip (sometimes

referred to as “flipping the phase”).

For example, you may have an input signal, like an explosion, where the transient attack of the

signal produces with a massively positive-going waveform (where the waveform mostly appears

above the zero line).

If you invert the polarity, the signal will now be mainly negative-going and the waveform will be

concentrated beneath the zero line. Inverting polarity is sometimes used to more closely align

signals from multiple microphones and can be used creatively to affect frequency response of

such a signal.

�Trim Level: The Trim knob lets you adjust the level of the signal coming “off of disk” during

playback to optimize the level feeding effects and the busses. This is helpful when you want to

slightly trim an otherwise perfect element up or down in your mix.

Trim adjustments are applied post the recorded signal and Track FX (which processes directly “off

of disk”), and pre all other effects, and do not affect the recording level.

Direct Output

Each audio channel strip can enable a direct output that can be used to feed any other input

destination. You can patch this source using the Track Direct choice in the Patch Input/Output dialog

via the Source dropdown.

�On/Off: Enables and disables the direct output.

�Pre: Sets the direct output tap-off point to be pre (before) the channel fader. On by default.

�Level Control: Sets the direct output level from minus infinity (fully off) to +10 dB.

Default is 0.0 (unity gain).

For more information see Chapter 171, “Setting Up Tracks, Busses, and Patching.”

Insert

This button is linked and identical to the Effects In button on the channel strip; here for convenience.

Clicking this button in one location enables the other and switches all Fairlight FX, AU, or VST channel

effects in or out of the signal path.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

Input Menu with Legacy Fixed Bussing

When using the legacy Fixed Busing, the options there are a bit different. Here is how they look when

that is enabled.

Input

The Patch Input/Output window appears set up to let you patch different inputs (such as the system

audio input) to the tracks of the Timeline. This makes it fast for setting up audio inputs in preparation

for recording.

Aux Bus

A shortcut to open the Patch Input/Output window (discussed previously in this chapter), which

appears set up to let you patch different Aux busses to specific submix and Timeline track channels.

Sub Bus

A shortcut to open the Patch Input/Output window (discussed previously in this chapter), which

appears set up to let you patch different Sub (submix) bus channels to specific Timeline track channels.

Main Bus

A shortcut to open the Patch Input/Output window (discussed previously in this chapter), which

appears set up to let you patch different Main bus channels to specific Timeline track channels.

Path Settings

This option opens the Path Settings window, which contains controls for adjusting the input level of

audio signals coming from an input/output device.

The Fairlight Presets Library

The Fairlight page offers a powerful and flexible preset system that allows you to store and recall

presets for everything from the complete configuration of the audio page to individual presets for

plugins. To access the presets library, choose Fairlight > Presets Library.

Fairlight Presets Library with stored presets on the

left panel and destination tracks on the right


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

A Filter By dropdown menu on the upper left lets you choose the type of preset

you want to work with.

Filter By menu of preset types

The choices are:

�Equalizer Presets: Presets for the built-in channel EQ.

�Dynamics Presets: Presets for the built-in Dynamics Processor.

�Plugins Presets: Fairlight FX, AU, or VST.

�Global Track Presets: All settings for a Mixer channel strip.

�Global Bus Presets: All settings for a Mixer bus.

�Fairlight Configuration Presets: Many parameters of the Fairlight page are stored as a

preset including:

�Track height.

�What tracks are shown or hidden in the Tracks pane of the Index.

�Split point in the Mixer.

�Full Track vs. Small Track views in the Mixer.

�Track Groups enable status.

NOTE: Some items are not currently stored in Fairlight Configurations, such as which panels

are shown (for example, Media Pool or Index), Meter Panel show/hide, Fairlight video window

docking, and size if the video window is set to be floating.

Using the Presets Library

Select the preset type you want to work with from the Filter By dropdown menu on the left.

The tracks list on the right (which appears for most preset types) acts as both a list of sources that

contain information you want to store and a list of destinations that you want to assign to when you

have presets defined. To store and recall and assign presets:

•	 If you’re storing a preset for the first time, select the source track in the tracks list on the

right of the window that you’ll be grabbing the preset type from (unless it’s a Fairlight

Configuration preset, which has no tracks to chose from, as it is global).

•	 Click the Save New button to save your preset.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

•	 To load your preset onto another track, deselect any tracks currently selected in the track

list on the right, and select the track(s) you want to assign to. Click Apply and the preset

is loaded.

•	 To save a new version of an existing preset or update your present version, first choose a

track in the track list that has your preset assigned to it. Then click the Save New button, and

a dialog appears that allows you to choose to update the current version of the preset or

save a new preset based on the current settings.

•	 To Delete a preset, select it in the list, and click the Delete button.

Update or Create New preset dialog


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT