---
title: "Stereo Fixer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 717
---

# Stereo Fixer

A simple plugin designed to fix stereo source material in cases where only one side of a stereo signal

was recorded, where one side of a stereo recording is a different level to the other, or where the

stereo channels have been incorrectly Left/Right swapped.

This plugin can also be used as a “Mid/Side” decoder, for recordings that were made using this

microphone technique.

This plugin is for stereo clips only.

The Stereo Fixer Fairlight FX

�Format: The input processing mode you want to use to fix the stereo output.

Stereo: (Default) No format conversion is performed.

Reverse Stereo: Swaps the Left and Right side.

Mono: The output from the plugin is a mono mix of the two inputs.

Left Only: The left input is sent to both left and right outputs.

Right Only: The right input is sent to both left and right outputs.

M/S: The left output is the left (Mid) input minus the right input (Side). The right output is the left

(Mid) input plus right input (Side).

�Left/Right Gain: Lets you apply independent gain on the left or right outputs. This gain is applied

after (post) the input processing mode.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

TIP: For a comprehensive M/S decoder solution, simply chain two Stereo Fixer plugins

together. Use the first unit to control the Side signal level, thus controlling the width of the

second unit (set to M/S).

Stereo Width

An enhancement plugin that increases or reduces the spread of a stereo signal in order to widen or

reduce the separation between channels. If this plugin is added to a Mono channel, it will be disabled,

as there is no stereo width to either distribute or control.

A graph shows the currently selected width of stereo distribution as a purple arc, while inside of that

graph a stereo meter shows the Left and Right distribution of the audio signal. Two audio meters

measure levels, an Input meter to the left, and an Output meter to the right.

The Stereo Width Fairlight FX in action

Stereo Width has the following controls:

Width: Lets you control the spread of the stereo output. Settings range from 0 (Mono) to 1

(Stereo) to 2 (extra wide stereo).

Diffusion: Adds more complexity to the output.

Sparkle: Adds more high frequencies to the spread.

Surround Analyzer

The Surround Analyzer is a graphical meter that shows a spatial image of the audio being measured,

rather than a typical bar graph meter. Due to its changing shape because of the signal being played,

sometimes it is referred to as the “jellyfish meter.”

This type of metering is very useful; rather than relying on bars to indicate the directions in which

audio is radiating, you can clearly see the relationship of all of the channels to one another.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

The signal here is radiating more to the

right, indicating the panning of the audio.

Vocal Channel

An enhancement plugin for general purpose vocal processing consisting of High Pass filtering,

EQ, and Compressor controls.

Side by side EQ and Dynamics graphs are presented above the controls. An output audio meter lets

you monitor the final signal being produced by this plugin.

The Vocal Channel Fairlight FX

Vocal Channel has the following controls:

�High Pass: Enabled by a toggle, off by default. Has a single frequency knob that sets the threshold

below which frequencies are attenuated to reduce boominess or rumble.

�EQ: A three-band EQ for fine tuning the various frequencies of speech, enabled by a toggle,

including Low, Mid, and High Mode, Frequency, and Gain controls

Low/Mid/Hi Mode: Lets you choose from different filtering options to use for isolating a range of

frequencies to adjust. Different bands present different options.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

Low/Mid/Hi Freq (Hz): Lets you choose the center frequency to adjust.

Low/Mid/Hi Gain (dB): Lets you boost or attenuate the selected frequencies.

�Compressor:

Threshold (dB): Sets the signal level below which compression occurs. Defaults to -25dB.

The range is from -40 to 0dB.

Reaction: Adjusts how quickly compression is applied when a signal exceeds the threshold.

The default is 0.10.

Ratio: Adjusts the compression ratio. This sets the gain reduction ratio (input to output) applied to

signals which rise above the threshold level. The default is 1.5:1. The range is 1.1 to 7.0.

Gain (dB): Lets you adjust the output gain to compensate for signal loss during compression,

if necessary.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

Chapter 182

Audio Meters and

Audio Monitoring

The Meters panel at the top of the Fairlight page provides a visual reference of

the track levels in your mix, specialized meters showing the busses, meters for

monitoring mix and loudness, and a video Viewer for seeing the current project as

you work.

This chapter describes the use of these meters, and provides information about the different options

that are available.

Contents

The Monitoring Panel���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3979

Track Meters and Monitoring Controls���������������������������������������������������������������������������������������������������������������������������������� 3979

Bus Meters�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3980

Meter Plugin������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3981

Surround Analyzer����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3981

Compound Meters and Output Bus Selection Menu����������������������������������������������������������������������������������������������������� 3982

Monitoring Menus������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3982

Control Room Meters����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3983

Loudness Meters�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3983

Offline Loudness Analyzer������������������������������������������������������������������������������������������������������������������������������������������������������������ 3986

Metering Options������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3988

Level Metering Options������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3988

Pre-fader Metering���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3988

Target Loudness Level�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3989

Viewer����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3990

Cinema Viewer on Fairlight Page���������������������������������������������������������������������������������������������������������������������������������������������� 3990


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT