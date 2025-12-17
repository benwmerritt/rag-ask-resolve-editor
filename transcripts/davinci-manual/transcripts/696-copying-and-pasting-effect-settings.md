---
title: "Copying and Pasting Effect Settings"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 696
---

# Copying and Pasting Effect Settings

If you have a setting for one effect that you spent a lot of time getting right and see that it could also

work just as well on another track’s effect, you can copy and paste just those settings.

For example, you have a Reverb on a dialogue track that you have tweaked to perfection. You see that

those exact settings will work well for another dialogue track that is on your timeline. Rather than try to

recreate those settings, you can duplicate them.

�Hold down the option key and drag the Reverb plugin you want to copy to a new location. This

creates a copy at the new location and leaves the original intact.

�Alternatively, you can use Copy and Paste in the plugin three dot Options menu. To apply those

settings to the other track, just click Copy from the Options menu of the source Reverb effect, then

open the Reverb plugin window of the destination Reverb effect, and click the Options menu to

paste. Now all of the parameters are the identical between the two plugins.

For more information on using audio effects, see Chapter 180, “Audio Effects.”

TIP: You can create and load presets for entire channel strips and use them in any project or

timeline using the Fairlight > Presets Library.

Effects In

The Effects In button allows you to bypass all Fairlight FX, AU, or VST effects plugins for the channel

with a single control. When it is lit (orange), all effects are enabled; when it is unlit, all effects

are bypassed.

NOTE: Track FX (Voice Isolation with Resolve Studio and Dialogue Leveler) and the built-in

Dynamics and EQ processors are not affected by Effects In.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Dynamics

Each Mixer channel strip has a built-in Dynamics processor, with a mini Dynamics Indicator graph that

appears on the channel strip and acts as the access button. Double-clicking the Dynamics Indicator

brings up the Dynamics processor window, with three modules: an Expander/Gate, a Compressor,

and a Limiter. Each can be used separately or in concert to manage the dynamics of the audio

on the target track.

The Dynamics control window

The Dynamics Graph

When you enable any combination of the Dynamics window modules you may need for a track, the

Dynamics graph updates with curves that show you how the signal is being affected by the Expander/

Gate, Compressor, and/or Limiter settings that are being applied. The Dynamics graph also provides a

real time animated display that meters the true response of the input/output signals compared to the

graphic that shows the basic response curve.

�The X axis (horizontal scale) represents the input signal level.

�The Y axis (vertical scale) represents the output level.

�The blue line represents the threshold.

�The light green line represents the dynamics curve (dependent on the process type and setting;

this will change).

�The light green balls that animate in the upper area of the graph follow how the Dynamics control

settings affect the signal as it moves above or below the threshold. The balls are affected by the

attack and release settings, allowing you to visualize the way the compressor is affecting the

input signal.

�The smaller lines that appear on the on the input and outline X-Y lines allow you to see exactly

where the input/output levels are.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

The Dynamics graph shows the response curve and how the

signal is being affected by the current settings in real time.

The Dynamics Indicator on the channel strip displays the same curve, so you can see at a glance what

is happening on that channel (but without the real time display). This indicator cannot be adjusted; you

must open the Dynamics window to make modifications.

The channel strip

Dynamics Indicator

Master Dynamics Controls

The Dynamics window contains the following overall controls at the top of the window:

�Enable button: Turns the overall dynamics effect off and on, without resetting the controls.

NOTE: You can also turn dynamics on/off by single clicking on the Dynamics button

(the mini graph) in the channel strip.

�Reset button: The circular reset icon on upper right next to the three dot Options menu resets all

controls of the Dynamics window to their defaults.

�Preset Menu: Dynamics presets appear here. You can create, change, and save presets, and use

the default presets as good starting points for your track’s specific needs.

�Make Up Gain control: A post-dynamics level control that lets you boost the signal to compensate

for dynamics settings that may have lowered the overall level.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Expander/Gate

The first of three sets of dynamics modules, the Expander/Gate controls can be switched between

expansion and gating. Expansion emphasizes differences in volume by lowering the level of soft parts

of the signal relative to the level of louder parts and can be used to minimize noise while increasing

the dynamic range of a signal. Gating reduces the level or even silences parts of a signal that fall

below the set threshold level in order to reduce or eliminate noise in quiet parts of a recording.

�Expander: This button enables the Expander.

Threshold: Sets the signal level below which expansion occurs. Defaults to –35 dB. The range is

from –50 to 0 dB.

Range: Amount of decrease in signal level in dB, affected by both threshold and ratio. As ratio

increases, range can have more of an effect. At lower ratios, as threshold increases, the effect of

range increases.

Ratio: Sets the attenuation ratio (input to output) applied to signals which fall below the threshold

level. It controls the rate at which signals will drop, while Range controls how much the signal will

drop. Defaults to 1:1.1. The range is 1:1.1 to 1:3.0.

Attack: Adjusts how quickly the expansion occurs when a signal exceeds the threshold.

Defaults to 1.4 ms (milliseconds). The range is 0 to 100 ms.

Hold: Controls how long the Expander is kept open after the input has fallen below the threshold,

in ms. Defaults to 0 ms. The range is from 0 to 4000 ms (4 seconds).

Release: Adjusts how quickly or gradually the Expander attenuates when the input signal goes

back below the threshold. Defaults to 93 ms. The range is 50 to 4000 ms (4 seconds).

�Gate: This button enables the Gate.

Threshold: Sets the signal level below which gain reduction occurs. The range is from –50 to 0 dB.

Hold: Controls how long time the Gate is kept open after the input has fallen below the threshold,

in ms. Defaults to 0 ms. The range is from 0 to 4000 ms (4 seconds).

Range: Sets the maximum amount of gain reduction that will be applied when the signal falls

below the gate threshold. Once the signal has fallen below the level determined by the gate

threshold minus the gate range, no gain reduction is applied. The default is 18 dB. The range is

from 0 to 60.2 dB.

Ratio: Unused for gate.

Attack: Adjusts how quickly the gating occurs when a signal exceeds the threshold. Defaults to

1.4 ms. The range is 0 to 100 ms.

Hold: Keeps dynamics from being triggered again until a certain amount of time has passed, in ms

(milliseconds). Defaults to 0 ms. The range is from 0 to 4000 ms (4 seconds).

Release: Adjusts how quickly or gradually the sidechain detector stops attenuating when the input

signal goes back below the threshold. Defaults to 93 ms. The range is 50 to 4000 ms (4 seconds).

Compressor

The second set of dynamics parameters let you apply compression, which detects the envelope

of an audio signal in order to automatically change its level. A compressor is used to compress a

signal’s dynamic range by reducing differences in level between the loudest and quietest parts of the

input signal.

Compression can be used to raise the signal’s overall level to be boosted without clipping, increasing

perceived loudness. Compression is often used to allow voices to have more presence within a mix,

and to smooth out changes in the levels of tracks with too much dynamic range for the task at hand.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

However, “overcompressing” can remove natural dynamics of a sound, or remove too many of

the natural transients (energy bursts or “attacks”) that give the original sound its character. But

more extreme compression can also be used creatively to change a sound’s character to give it

more perceived attack, change its release characteristic, or change the balance and blend of the

environment a sound is recorded in (for example, compressing a source signal with a higher ratio and

fast release to raise up the presence of a room sound that the source is recorded in).

�Compressor: Enables the Compressor.

�Threshold: Sets the signal level above which compression is applied. The default is –15 dB. The

range is –50 to 0 dB.

�Ratio: Adjusts the compression ratio. This sets the gain reduction ratio (input to output) applied

to signals which rise above the threshold level. The default is 2.0:1. The range is 1.0:1 to 10:1.

Commonly used ratios for dialogue processing are 2.5:1 to 3:1. With a 3:1 ratio, for every 3 dB of

increase in signal above the threshold, 1 dB is output.

�Knee: Affects behavior with signals that are very near the threshold. The knee can smooth out the

transition between where you don’t hear any compression and when the “hard compression” (the

set ratio) starts.

The Knee: Control allows a smoothing of the slope of the threshold point. You can see Knee’s

effect on the graph when using a ratio like 4:1 and adjusting Knee; the graph will show the line

where compression “kicks in” being rounded off by higher values of the Knee control.

Normally, compression begins directly above the threshold. This is known as a “hard knee.”

For a smoother and less audible handling of compression, you can set a softer knee, so the

compression turns on gradually as signals approach the threshold and rise above.

Hard and Soft Knee graphs

Mix: Adjusts the mix between the compressed (0) and non-compressed input signal (100), allowing

you to balance the compressed signal against the original, unaffected sound. For example, if you’re

creating a large explosion impact sound effect, it might sometimes be useful to mix in just a bit of

the original, uncompressed signal with a more compressed version to preserve more of the original

character along with compressed version. The default is 0 (all compression, no original signal).

Attack: Adjusts how quickly the compression will occur when a signal exceeds the threshold.

The default is 1.4 ms. The range is 0 to 100 ms.

Hold: After the attack phase has been completed, the Hold parameter controls how long this initial

attenuation is maintained, before entering the release phase. Defaults to 0 ms. The range is from

0 to 4000 ms.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Release: Adjusts how quickly or gradually the sidechain detector stops applying compression

when a signal falls back below the threshold. The default is 93 ms. The range is 50 to 4000 ms

(4 seconds).

Sidechain: This redesigned section lets you set up sidechain compression or “ducking” using

the parameters and controls listed below, instead of using a Send from a track or bus to feed the

sidechain input:

Sidechain module

On: When clicked, this button turns red indicating that the Sidechain module is active.

Listen: Clicking this button lets you hear the incoming signal on its own, which is helpful if you

need to confirm that the correct audio signal is being sent to the Sidechain module.

Source: This button selects the track or bus the incoming audio is coming from.

Sidechaining and “Ducking” with Dynamics

The Dynamics module allows you to set up “sidechain” compression, which lets you temporarily lower

the level of a target track or bus using the audible signal from a source track or bus.

For example, you may have a dialogue on a track or bus (the source) and another with music (the

target), and you want the dialogue to be heard more prominently. This can be done by following the

steps below:

Choosing the track header in the Fairlight timeline to add dynamics


Open the Dynamics plugin on the music track or bus, and switch on the Compressor.


Click the Source dropdown and select the dialogue track or bus.

TIP: Using a bus as the ducking source lets you use multiple sources to trigger changes in

your target track.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT


Click the On button, which turns red, indicating that the Sidechain section is active.


While playing a section of your mix, set the amount of gain reduction by lowering the Threshold

and raising the Ratio until the target audio is attenuated to a level that makes the dialogue

more audible.


If needed, adjust the Hold parameter to ensure the gain reduction doesn’t fluctuate too wildly.


You may also need to adjust the Release parameter to stop the gain reduction from

ending too abruptly.

Clicking the Listen button lets you hear the incoming signal if you need to confirm that the correct

input signal is coming into the Limiter. This button turns yellow when active.