---
title: "Frequency Analyzer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 715
---

# Frequency Analyzer

The Frequency Analyzer provides visual information about your clips or tracks as either a Spectrum or

Waterfall graph to identify possible sonic issues so you can further sculpt your audio.

Options in the Mode menu in the upper right let you examine either the Full frequency range of the

signal (default) or close-up views of the Low, Midrange, or High frequencies.

Frequency Analyzer Spectrum view

Frequency Analyzer plugin Waterfall view

Gain

This plugin is used to accurately increase or decrease the volume level of an audio signal by a specific

number of decibels. It is helpful in numerous contexts, such as making a quick adjustment to the

overall volume of a track that has extensive mixer or plugin automation written to it.

This plugin is used to accurately increase or decrease the volume level of an audio signal by a specific

number of decibels. It is helpful in numerous contexts, such as making a quick adjustment to the

overall volume of a track that has extensive mixer or plugin automation written to it.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

The Fairlight Gain plugin

LFE Filter

A low-pass filter that you can apply to a FlexBus or Main that’s in a surround sound format, to feed low-

frequency sound to an LFE channel as part of a surround sound mix. The filter will exclude any sounds

above your chosen frequency setting to the audio that is sent to a sub-woofer in the LFE channel.

It helps keep unwanted and unnecessary audio from being sent to the sub-woofer and increases

playback clarity.

A Frequency control lets you choose which low frequency range you want to include, and a Trim

control lets you set the level of the resulting LFE channel. If it is multi-channel but has no LFE channel

available, such as a 5.0 format, then this plugin does nothing.

The LFE plugin

Limiter

The Limiter detects and reduces peaks in an audio signal, so the overall level can be boosted without

clipping while reducing the dynamic range in a similar manner to a compressor.

This is a true peak limiter that can look 64 samples ahead of the input signal, allowing an extremely

smooth limiting response.

The Input control lets you adjust the incoming signal level, while the Threshold and Release

control when limiting occurs and for how long. The graph indicates which parts of the signal are

being affected.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

The Limiter plugin

Limiter controls

Bypass: Toggles this plugin on and off.

Input Meter: Shows the level of the incoming signal.

Input Level: This control lets you adjust the incoming signal level within a range of

-18 dB to +18 dB. Activating the Soft button causes the limiter to use a gentler attack.

Ceiling: This determines the threshold (level) at which the Limiter starts reducing the input

signal. When set to -24 dB, any signal above that level is limited. When set to 0 dB, no

limiting occurs.

Release: This determines how long the limiting (signal reduction) takes place. Setting this

control to 0.01 milliseconds results in a very fast release time, while the longer release time of

1000 milliseconds is the slowest.

Reduction Meter: This shows the amount of level (gain) reduction applied to the input signal.

Output Meter: Shows the output level after the limit.

Limiter Sidechaining

The Fairlight FX Limiter supports sidechaining, which lets you temporarily lower the level of a target

track or bus using the audible signal from a source track or bus.

This is very helpful when multiple tracks are “fighting” for space in a mix because they share some or

all the same frequency range. For example, a track or bus with dialogue and a bus or track with traffic

and crowd noise.

Essentially, this is another form of “ducking” where, in the example above, the dialogue attenuates the

traffic and crowd noise until the dialogue stops. This allows the voices to be heard more prominently

in the mix.

Sidechain controls


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

Using the Limiter Sidechain

Carrying on with the example mentioned above:


Open the Limiter on the destination track or bus with the traffic and crowd noise.


Select the Dialogue track or bus in the source dropdown to the right of the Listen button.

�This is the audio you’re using to attenuate the level of the target track.

�Using a bus as the source lets you use multiple sources to trigger changes in your target track.

Clicking the Listen button lets you hear the incoming signal if you need to confirm that the correct

input signal is coming into the Limiter. This button turns yellow when active.

Meter

A sample peak processing meter that’s useful for temporarily adding a meter to a specific track or

FlexBus. These meters are useful for instances where you want a large meter that focuses on a

specific bus or track while you’re working.

The Meter Fairlight FX

These meters are presented very simply, with a gray bar indicating level and a red peak line that holds

for two seconds, which indicates the highest peak. A numeric reading at the top of the meter gives the

exact level, in dB. This number continues to hold, indicating the loudest level measured for any given

stretch of playback.

Meter can be resized by pulling from the bottom right and has the following controls located in

the option menu:

Reset Peak on Play: When enabled, the numeric peak level is reset every time playback

stops and starts again. When disabled, the numeric peak level persists until changed by a

higher peak.

Reset: Resets the numeric peak level.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

Modulation

An effect plugin. General purpose modulation plugin for sound effects or sound design. Four effects

combine an LFO, FM adjustment, AM adjustment, Sweep and Gain filters to allow simultaneous

frequency, amplitude and space modulation. In conjunction with the Rotation controls, simple Tremelo

and Vibrato effects can be combined with auto-filter and auto-Pan tools in order to provide texture

and movement to a sound.

An animated graph shows the results of adjusting the Modulator, Frequency, and Amplitude

parameters of this plugin, giving you a visualization of the kind of modulations that will be applied to

the signal as you make adjustments. Output meters let you see what level is being output.

The Modulation Fairlight FX

Modulation has the following controls:

�Bypass: Toggles this plugin on and off.

�Modulator: A low frequency oscillator (LFO), shown in blue in the animated graph.

Shape: Specifies the shape of the LFO waveform that modulates the audio. Six options

include Sine, Triangle, Saw1, Saw2, Square, Random.

Rate (Hz): Adjust the speed of the modulating LFO. Lower settings result in warbling audio,

while extremely high settings result in buzzing audio the timbre of which is dictated by the

shape you’ve selected.

�Frequency: Frequency modulation (FM) of a secondary oscillator, shown as

green in the animated graph.

Level (%): Acts as a Dry/Wet knob controlling the amount of Frequency Modulation that’s applied,

intensifying or easing off the effect.

Phase: Since each of the four primary effects within this plugin can be applied together, along

with the fact that modulation with level components (Tremelo/Rotation/Filter) have the ability

to combine or cancel out one another, phase controls are available. Altering the phase of an

individual effect allows control of such interaction (e.g., cancel out a high level change, or

offset a cancellation).


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

�Filter: Sweep and gain filters.

Filter (%): Acts as a Dry/Wet knob controlling the amount of filter sweep and gain to additionally

use to modify the signal. The amount you’ve selected is previewed in a 1D graph to the side.

Tone: Adjusts the center frequency of sweep.

Phase: Since each of the four primary effects within this plugin can be applied together, along

with the fact that modulation with level components (Tremelo/Rotation/Filter) have the ability

to combine or cancel out one another, phase controls are available. Altering the phase of an

individual effect allows control of such interaction (e.g., cancel out a high level change, or

offset a cancellation).

�Amplitude: Amplitude modulation (AM) of a secondary oscillator, shown as

green in the animated graph.

Level (%): Acts as a Dry/Wet knob controlling the amount of Amplitude modulation applied.

(Disabled in Ring Modulation Mode.)

Phase: Since each of the four primary effects within this plugin can be applied together, along

with the fact that modulation with level components (Tremelo/Rotation/Filter) have the ability

to combine or cancel out one another, phase controls are available. Altering the phase of an

individual effect allows control of such interaction (e.g., cancel out a high level change, or

offset a cancellation).

Ring Modulation Mode: Enables a Ring Modulation effect (where the signal is multiplied by the

modulator, rather than modulated by it).

�Rotation: These controls are only available when applied to a multi-channel track.

Rotate: Amount of Rotation applied.

Offset: Start offset of rotation in order to further place the signal in space.

Phase: Since each of the four primary effects within this plugin can be applied together, along

with the fact that modulation with level components (Tremelo/Rotation/Filter) have the ability

to combine or cancel out one another, phase controls are available. Altering the phase of an

individual effect allows control of such interaction (e.g., cancel out a high level change, or

offset a cancellation).

�Output: Controls for adjusting the final output from this plugin.

Dry/Wet (%): A percentage control of the output mix of “dry” or original signal to “wet” or

processed signal. 0 is completely dry, 100% is completely wet.

Output Level (dB): Adjusts the overall output level of the affected sound.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT