---
title: "Multiband Compressor"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 716
---

# Multiband Compressor

A dynamics processor that compresses in highly definable frequency bands. The graph displays

frequencies in Hertz horizontally and gain in decibels vertically. This allows for precise compression

specific to defined frequency bands and is useful for taming only one or several parts of a signal.

The default setting of the Multiband Compressor

Each band has dynamics control in the determined frequency ranges of Low, Med, and High and are

adjustable by pushing the intersection mark on the graph per band or by typing in a frequency.

Bands 1 – 4: Controls for each band.

�Threshold: Sets the maximum allowable output level. The default is –25dB. The range is from

–50 to 0dB.

�Gain: Can add or attenuate up to 12 dB of gain.

�Ratio: Adjusts the compression ratio. This sets the gain reduction ratio (input to output) applied to

signals that rise above the threshold level. The default is 1.5.0:1. The range is 1.0:1 to 7:1.

�Limit: Limits the output amount by up to 15 dB. The default is 4.5 dB.

�Attack: Adjusts the attack rate time constant of the sidechain detector. The default is 1.4 mS. The

range is 0.1 to 100 mS.

�Hold: Keeps dynamics from being triggered again until a certain amount of time has passed, in mS

(milliseconds). Defaults to 0mS. The range is from 0 to 4000 mS.

�Release: Adjusts how quickly the sidechain detector stops applying dynamics when a signal goes

back below the threshold. The default is 150 mS. The range is 50 mS to 4.0 S.

Master: Controls for adjusting the final output from this plugin.

�Gain (dB): Adjusts the overall output level of the affected sound by adding or reducing

18 dB of gain.

�Q: Adjusts the width of affected frequencies. Lower values include a wider range of frequencies,

higher values include a narrower range of frequencies.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

Noise Reduction

A repair plugin designed to reduce a wide variety of noise in all kinds of recordings. A graph shows

a spectral analysis of the audio being targeted, along with a purple overlay that shows what noise is

being targeted. Two audio meters let you evaluate the input level (to the left) versus the output level

(to the right), to compare how much signal is being lost to noise reduction. There are three default

presets: De-Hiss, De-Rumble, and De-Rumble and Hiss.

The Noise Reduction Fairlight FX in action

Noise Reduction has the following controls:

�Bypass: Toggles this plugin on and off.

�Listen to Noise Only: This checkbox at the top right lets you listen only to the noise that is being

removed. This is very useful to determine if too much signal is being removed or if more noise

attenuation can be applied.

�Threshold (in dB): Relates to the signal-to-noise ratio (SNR) in the source recording. Recordings

with a poor signal-to-noise ratio will require a higher threshold value, resulting in more noise

reduction being applied.

�Attack (in ms): Primarily useful in Auto Speech mode, this controls the duration over which the

noise profile is detected. Ideally, the attack time should match the variability of the unwanted

noise. A low value corresponds to a faster update rate of the noise profile and is useful for quickly

varying noise; a high value corresponds to a slower update rate and can be used for noise

that’s more consistent.

�Sensitivity: Higher sensitivity values exaggerate the detected noise profile; the result is that more

noise will be removed, but more of the dialogue you want to keep may be affected.

�Ratio: Controls the attack time of the signal profile relative to the attack time of the noise profile.

A faster ratio detects and preserves transients in speech more easily, but the resulting speech

profile is less accurate.

�Frequency Smoothing: Smooths the resulting signal in the frequency domain to compensate

for harmonic ringing in the signal after the noise has been extracted.

�Time Smoothing: A toggle button enables smoothing of the resulting signal in the time

domain as well.

�Dry/Wet: A percentage control of the output mix of “dry” or original signal to “wet” or processed

signal. 0 is completely dry, 100% is completely wet.

�Level: To let you compensate for level that may be lost due to the noise reduction operation you’re

applying, this applies a pre-gain in, from -6dB to +18dB, just before the dry/processed mix.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

Phase Meter

Phase cancellation is a phenomena where the waveforms of a stereo recording (for example a stereo

recording of a music performance) go slightly out of sync with one another for whatever reason, and

begin to cancel one another out in unpredictable ways, resulting in the audio sounding strange.

This results in poor quality audio and can cause problems when you’re trying to compress a mix to a

distribution format such as AAF or MP3.

The Phase Meter plugin is a visual meter that lets you evaluate whether or not a signal is in phase

and is meant to be applied to a bus so you may evaluate the phase of a mix and correct whatever

problems may be occurring. The position of a green dot within a horizontal meter indicates the phase

of the signal. When there’s no signal or a signal on only one half of a stereo bus, the dot appears in the

center (0). When the signal is out of phase, the dot appears all the way to the left (–). When the signal is

in phase, the dot appears all the way to the right (+).

The Phase Meter plugin

Pitch

An effects plugin that shifts audio pitch without altering clip speed.

The Pitch Fairlight FX

Pitch has the following controls:

�Bypass: Toggles this plugin on and off.

�Semitones: A “coarse” adjustment that can shift audio pitch up to +/- 12 semitones.

�Cents: A “fine” adjustment that can tune audio pitch in +/-100th of a semitone.

�Dry/Wet: A percentage control of the output mix of “dry” or original signal to “wet” or processed

signal. 0 is completely dry, 100% is completely wet.

Reverb

A spatial simulation plugin, capable of recreating multichannel reverberation corresponding to rooms

of different sizes, adjustable via a graphical 3D cube control. This plugin lets you take a “dry” recording

and make it sound as if it’s within a grand cathedral, an empty room, a tiled bathroom, or other spaces.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

To understand this plugin’s controls, it helps to know that the signal follows three paths which are

combined to create the final effect:

�A direct path.

�An early reflection path (ER) simulating early reflection rays obtained from the first multiple

reflections on the walls, traveling from the virtual source to the virtual listener.

�A late reverberation path (Reverb) simulating the behavior of an acoustic model of the room.

A graph shows an approximate visualization of the reverb’s effect on the frequencies of the

audio signal.

The Reverb Fairlight FX

Reverb has the following controls:

�Bypass: Toggles this plugin on and off.

�Room Dimensions: By controlling the size of the virtual room a sound is to inhabit, these

parameters simultaneously control the configuration of Early Reflection and Late Reverberation

processing. The acoustic modes from this simulated room are computed and fed to Late

Reverberation processing. The shape, gain, and delay of the first reflections are computed and

then fed to Early Reflection processing.

Height, Length, Width: Defines the dimensions of the reverberant space, in meters.

Room Size: The calculated Room Width x Length, in meters.

�Reverb: Additional controls that further customize the configuration of Early Reflection and Late

Reverberation processing.

Pre Delay: Increase or negate the propagation time from the virtual source to the virtual listener.

As a result, it modifies the initial delay time between the source signal and the first reflection.

Reverb Time: Decay time of the Reverb tail. It controls the overall decay time of the acoustic

modes from late reverberation processing.

Distance: Modifies the distance between the virtual source and the virtual listener. It modifies only

the configuration of early reflections processing.

Brightness: Modulate the shape of the decay time over frequency. At maximum brightness, decay

time is identical at any frequency. At minimum brightness, higher frequencies result in shorter

decay time and therefore duller sound.

Modulation: Adds random low-frequency phase modulation from the tapping point of

ER processing. At 0%, modulation is not used.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

�Early Reflection Tone: Four post equalization controls modify the tone of early reflections to suit a

particular room’s characteristics.

Low Gain: Amount of gain added to the low frequency.

Low Frequency: Frequency range of 150 Hz to 500 Hz.

High Gain: Amount of gain added to the high frequency.

High Frequency: Frequency range of 1k Hz to 16k Hz.

�Reverb Tone: Four post equalization controls modify the tone of the reverb tail to suit a particular

room’s characteristics.

Reverb Tail Low Gain: Amount of gain added to the low frequency.

Reverb Tail Low Frequency: Frequency range of 150 Hz to 500 Hz.

Reverb Tail High Gain: Amount of gain added to the high frequency.

Reverb Tail High Frequency: Frequency range of 1k Hz to 16k Hz.

�Output: These controls recombine the three audio processing paths into a single output signal.

Dry/Wet: A percentage control of the output mix of “dry” or original signal to “wet” or processed

signal. 0 is completely dry, 100% is completely wet.

Direct Level: The amount of the direct level to mix into the final signal.

Early Reflection Level: The amount of early reflection to mix into the final signal.

Reverb Level: The amount of reverb to mix into the final signal.

Soft Clipper

The Soft Clipper is a limiting processor that reduces the output level above a defined threshold in

a rounded manner so that peaks are more cleanly attenuated. The Soft Clipper plugin will impart

saturation effects when pushed hard above the threshold, allowing for the introduction of warmth and

subtle distortion to the sound. A graph shows the shape of the curve adjustment this plugin makes to

the audio.

A soft clipper is often combined with a standard limiter in order to increase perceptual loudness of

material without imparting harshness.

The Soft Clipper Fairlight FX


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

Threshold: Introduces input gain to the signal prior to hitting the clipper, forcing audio peaks

over the threshold by that amount. As such, it will drive the saturation and distortion.

Shape: The shape of the clipper can be varied to change the character of the soft clipper from

full soft-clipping (all the way right, where the peaks are rounded) to full hard-clipping (all the

way left, where the peaks are squared off).

Output Level: Lets you adjust the output gain to compensate for signal loss during soft

clipping, if necessary.