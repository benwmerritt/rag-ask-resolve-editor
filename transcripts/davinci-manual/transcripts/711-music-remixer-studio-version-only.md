---
title: "Music Remixer (Studio Version Only)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 711
---

# Music Remixer (Studio Version Only)

This DaVinci Neural Engine AI-based plugin splits music into individual stems: Vocals, Drums, Bass,

Guitar, and “Other” (“everything else”), letting you creatively rebalance or remix the track.

You can use the level controls to adjust the volume of each stem and the Mute buttons to remove

or bring them back into your mix. For example, you may want to remove or lower a vocal because it

clashes with a featured piece of dialogue.

The Music Remixer plugin

Voice Isolation (Studio Version Only)

Voice Isolation uses an AI model trained for any type of human voice, male or female, young or old,

which lets you completely remove loud, undesirable sounds from existing voice recordings with

incredible results.

The Voice Isolation plugin

You can get rid of all kinds of background noise, from air conditioners or fans to jackhammers,

restaurant background noise, music playing during a featured piece of dialogue, and more.

The Amount control adjusts the mix between the original source and the isolated voice. When

set to 50, the mix is roughly equal. Values between 70 and 80 work well for natural results while

strongly isolating the source.

Although Voice Isolation can be used on an audio track in real time, it cannot be used on live audio

input. It can be used on any mono, stereo, or dual-mono audio track, but it isn’t supported on tracks

with more than two channels.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

Insert Effects

Ambisonics Meter

This Fairlight FX plugin can be inserted on an Ambisonics track or bus to present a graphic display of

your Ambisonic sound field. Clicking the three dots in the upper right opens an options menu where

you can choose either “power” (Power Map), or “Sonar” style map as the metering method.

Both meters convey the intensity of the sound and its current location in the Viewer.

Ambisonics meter - Power Map view

Ambisonics meter - Sonar view


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

Chain FX

Fairlight Chain FX lets you build chains of up to six Fairlight FX or compatible Audio Units or VST

effects plugins, which can be adjusted using a single control.

Chain FX plugin

Master Controls

The Chain FX window has the following controls located in the upper section of the interface.

Preset Menu: This is where you can save and recall Chain FX settings.

�Chain FX combinations can be saved as presets by clicking the Plus button to the left of the Preset

menu and recalled by clicking the menu and making a selection.

�You can also scroll through the presets by clicking the left or right “arrow” ( < or >) to the right of

the drop-down menu.

�You can save a Chain FX configuration as the default by selecting the Set as Default option from

the Options menu (three dots) located in the upper-right corner, to the right of the Reset button.

�Chain FX presets can be copied and pasted to other instances of the plugin for a faster workflow.

TIP: Chain FX presets can also be recalled by clicking the plus sign on an insert slot,

followed by Chain FX.

Compare Buttons (A and B): These buttons let you quickly compare two different Chain FX settings.

If you create a Chain FX setting or select a preset when button A is active (red), then click button B and

create a different setting or choose a different preset, clicking between the buttons quickly switches

from one to the other.

Bypass Button: Switches the Fairlight EQ on and off.

Reset Button: Clicking the circular Reset icon, located in the upper-right corner of the EQ, undoes the

most recent action you’ve taken in the plugin interface.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

Sidechain (SC) Section:

�On Button: Clicking this button activates the Sidechain section of the plugin, prompting you to

select an audio track or buss as the input source from the Source drop-down menu.

For more information about Sidechaining, see Chapter 180, “Audio Effects.”

�Listen Button: Clicking this button lets you hear only the incoming audio signal, which is helpful if

you need to confirm that the correct audio signal is being sent to the Sidechain module.

�Source: This button selects the track or buss the incoming audio signal is coming from.

Building an FX Chain

To create an effect chain in a Chain FX instance:


1.

Open an empty Chain FX plugin by clicking an empty Effects slot on a Mixer Channel Strip and

choosing Multi Effect > Fairlight FX > Chain FX.

Ensure that the plugin is active.


Add the first Fairlight FX or compatible third-party plugin by clicking the plus sign in the Plugin

Chain section and selecting a plugin from the menu.

While the plugin is active, either recall an existing preset or adjust the controls to dial in your

desired settings.


Repeat the previous step until you have built an FX chain of up to six plugins that works for you.


Save the resulting combination of plugins, in their current state as a Chain FX Preset, by clicking

the Plus button to the left of the Preset menu.

TIP: Clicking the name of any plugin listed in the effect chain opens its respective

plugin window.

You can also create a new effects chain by opening any compatible plugin, such as a

compressor, clicking the three dots in the upper-right corner of the plugin window, and

selecting Add to Plugin Chain from the menu.

Add to Plugin Chain menu option


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

This opens a new Chain FX instance with the plugin you originally selected (the compressor, in

this example) already inserted in the first slot.

•	 The Chain FX plugin replaces the compressor in the mixer channel insert.

•	 You can add more plugins to the effect chain by clicking the plus sign in the Plugin Chain

section and selecting a plugin from the menu.

Chorus

A classic Chorus effect, this layers voices or sounds against modulated versions of themselves to add

harmonic interest in different ways.

An animated graph shows the results of adjusting the Modulation parameters of this plugin, giving

you a visualization of the kind of warble or tremolo that will be added to the signal as you make

adjustments.

The Chorus Fairlight FX

Chorus has the following controls:

�Bypass: Toggles this plugin on and off.

�Input Format: (Only visible when Chorus is inserted on a multi-channel track.) Lets you choose

how multiple channels are input to the Chorus. Stereo sets separate Left and Right channels.

Mono sums Left and Right to both channels. Left inputs the Left channel only, and Right inputs the

Right channel only.

�Delay: The amount of delay between the original sound and the Chorus effect.

Delay Time: Length of the Chorus delay lines.

Separation: Time separation of the delay voices.

Expansion: Sets L/R length differences, phase offset of modulators.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

�Modulation: These controls adjust the low frequency oscillator (LFO) that drives the tremolo of the

chorus effect in different ways.

Waveform: Specifies the shape of the LFO that modulates the rate of the Chorus, affecting the

timing of the oscillations. There are six options for the oscillator for you to choose from:

Sine (Smooth oscillations)

Triangle (Sudden oscillations)

Saw1 (Jerky oscillations)

Saw2 (Jerky oscillations)

Square (Hard stops between oscillations)

Random (Randomly variable oscillations)

Frequency: Rate of LFO controlling the Chorus. Lower values generate a warble,

higher values create a tremolo.

Pitch: Amount of frequency modulation, which affects the pitch of the Chorus.

Level: Depth of level modulation. Affects the “length” of the segment of Chorus that’s added to the

sound. Low values add only the very beginning of the Chorus effect, high values add more fully

developed Chorus warble or tremolo.

�Feedback: A signal fed back to the Chorus Delay Line

Amount (%): The percentage of signal fed back to the Chorus Delay Line. Values can be positive

or negative, the default is 0 (no effect). Increasing this parameter adds more of the Chorus effect

to the signal, lowering this parameter adds more of the inverted Chorus effect to the signal. At

values closer to 0, only a faint bit of Chorus can be heard in the audio, but at values farther away

from 0 (maxing at +/- 99), a gradually pronounced Chorus becomes audible.

Blend (%): Amount of feedback which bleeds into the opposite channel (Stereo mode only).

�Output: Controls for adjusting the final output from this plugin.

Dry/Wet (%): A percentage control of the output mix of “dry” or original signal to “wet” or

processed signal. 0 is completely dry, 100% is completely wet.

Output Level (dB): Adjusts the overall output level of the affected sound.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT