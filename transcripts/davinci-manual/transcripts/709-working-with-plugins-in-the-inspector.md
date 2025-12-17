---
title: "Working with Plugins in the Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 709
---

# Working with Plugins in the Inspector

Methods of working with audio plugins in the Inspector:

�To rearrange the order of multiple audio effects applied to a clip: Click the move up or move

down buttons in any effect’s title bar, to the left of each effect’s Trash Can button.

�To disable or re-enable an effect: Click the toggle button at the far left of each effect’s title bar.

�To remove an effect: Click the Trash Can button.

�To reset any effect parameter: Click the Reset button at the far right of the

parameter you want to reset.

�To open or collapse an effect’s parameters: Double-click the title bar.

�To open or collapse the parameters of all effects: Hold the Option key down and

double-click any effect’s title bar.

Once applied to a clip or track, audio plugins can also be keyframed or automated just like volume and

pan settings, to create dynamic audio effects that change over time.


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

Sidechaining

DaVinci Resolve supports the sidechaining of compatible Fairlight FX, AU, and VST plugins, which

lets you temporarily lower the level of a target track or bus using the audible signal from a source

track or bus.

This process, also known as “ducking,” is helpful when multiple tracks compete for space in a mix

because they share some or all the same frequencies, such as a track or bus with dialogue and a bus

with a crowd cheering at a sports event.

In the example above, the dialogue is fed to the sidechain input of a compatible dynamics plugin (i.e.,

a compressor or limiter) on the Mixer channel for the crowd noise. When the controls on the dynamics

are set correctly, the voices on the Dialogue channel will subtly and slightly lower or attenuate the

level of the crown noise, allowing the voices to be heard more prominently in the mix. When the

dialogue stops, the cheering returns to its original level.

Sidechain controls

To use sidechaining

•	 Open the compressor or limiter on the Mixer channel with the crowd noise.

•	 Select the Dialogue channel in the source dropdown at the top of the plugin,

to the right of the Listen button.

This is the audio you’re using to attenuate the level of the cheering crowd.

Using a bus as the ducking source lets you use multiple sources to trigger changes

in your target track.

•	 Click the On button, which turns red, indicating that the Sidechain (S/C) function is active.

•	 Adjust the controls to taste during playback of your mix, while ensuring the effect

sounds natural.

You can experiment with this procedure using the Compressor section of the Channel

Dynamics plugin or the Fairlight FX Limiter.

For more information on sidechaining with the Channel Dynamics plugin, see Chapter 177,

“Mixing in the Fairlight Page.”

For more information on sidechaining with the Fairlight FX Limiter, see Chapter 181,

“Fairlight FX.”

•	 Clicking the Listen button lets you hear the incoming signal if you need to confirm that

the correct input signal is coming into the Limiter. This button turns yellow when active.


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

Applying Audio Plugins to Busses

You can apply audio plugins to Main and Sub buses just like any other track, with which to apply any

audio mastering effects operations you require to individual submixes, or even to an entire main.

TIP: You can quickly assign plugins for a selected group of channel strips, or to all channel

strips, by holding down the Option key (Mac) or the Alt key (Windows) for all selected tracks

or Command-Option (Mac) or Control-Alt (Windows) for all mixer channel strips prior to

performing the operation. These shortcuts can save a lot of time in your workflow.

Dealing With Processor Intensive Plugins

As you apply more and more plugins directly to clips in complicated mixes, you may discover you lack

the processing power to play all audio tracks and effects in real time. When this happens, there are

two ways you can ease the burden that audio clip effects are placing on your workstation.

Caching Audio Clips With Plugins

One quick fix is to manually enable the caching of one or more selected audio clips with audio effects

applied to them to improve your project’s performance. Once an audio clip is cached, all plugin effects

are “baked in” and that clip’s audio waveform updates to reflect the altered audio. Cached clips appear

with a small badge to the right of the FX badge in the name bar of the clip.

A cache badge lets you know this audio clip has cached effects

This is a non-destructive operation that has no lasting effect on the source media of cached clips. You

can still alter a cached clip’s plugin parameters whenever you want. Opening the graphical controls of

a cached clip temporarily suspends audio caching, and when you’re finished, the clip is automatically

re-cached and its waveform is updated to reflect the change so long as Cache Audio Effects

remains enabled.

To cache audio effects for one or more selected clips:

�Right-click an audio clip with a plugin applied and choose Cache Audio Effects to enable

audio effect caching for that clip. If you right-click one of multiple selected clips, you’ll enable

Cache Audio Effects for all selected clips at once. Once enabled, that clip will be continue to

be cached (and re‑cached if you change the plugin’s parameters) until you manually disable

audio caching.


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

To disable audio caching for one or more selected clips:

�Right-click an audio clip that’s been cached and choose Cache Audio Effects to disable audio

effect caching for that clip.

Exporting Audio Clips With Plugins

Another way of easing the burden of audio clip effects on your system is to export the effected clip to

another layer. This creates a new piece of audio media with the effect “baked in,” which is written to

the directory location specified by the “Save clips to” field of the Capture and Playback panel of the

Project Settings.

To bounce one or more selected audio clips with effects to another layer:

�Right-click an audio clip with a plugin applied and choose Export Audio Files. If you right-click one

of multiple selected clips, you’ll have options for what you would like exported for each selected

clip all at once.

Exported clips no longer have editable effects, but you can always choose View > Show Audio

Track Layers to see the original underlying clip that still has the original plugin effect applied, and

you can unmute it, move it back up to the top, edit the effect, and export another version of the

clip, which appears as the topmost layer.

For more information on exporting clips to files, see Chapter 175, “Editing Basics in the

Fairlight Page.”


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

Chapter 181

Fairlight FX

Fairlight FX are DaVinci Resolve-specific audio plugins that run natively on macOS,

Windows, and Linux and provide high-quality audio effects with professional

features to all DaVinci Resolve users.

These plugins are available on the Edit and the Fairlight pages and offer various options for repairing

faulty audio, creating effects, and simulating spaces.

On the Fairlight page, they’re categorized as either Track FX or Audio Effects based on their position

in the Fairlight Mixer’s signal path.

For more information on For more information on the Fairlight Mixer’s signal path, see Chapter

177, “Mixing in the Fairlight Page.” This chapter explains what they do and how to use them.

Contents

Common Controls For All Fairlight FX����������������������������������������������������������������������������������������������������������������������������������� 3936

Track FX ������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3937

Dialogue Leveler�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3938

Dialogue Separator (Studio Version Only)����������������������������������������������������������������������������������������������������������������������������� 3939

Ducker����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3940

Music Remixer (Studio Version Only)���������������������������������������������������������������������������������������������������������������������������������������� 3942

Voice Isolation (Studio Version Only)���������������������������������������������������������������������������������������������������������������������������������������� 3942

Insert Effects���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3943

Ambisonics Meter������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3943

Chain FX������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3944

Chorus����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3946

De-Esser������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3948

De-Hummer������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3949

Delay�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3950

Dialogue Processor���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3951

Dialogue Leveler�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3952

Distortion����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3953

Echo���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3955

EQ ‑ Fairlight EQ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3956


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT