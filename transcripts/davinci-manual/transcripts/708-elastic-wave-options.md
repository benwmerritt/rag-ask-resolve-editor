---
title: "Elastic Wave Options"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 708
---

# Elastic Wave Options

The Elastic Wave context menu has three options for processing:

�Off: Elastic Wave is not enabled for the clip (Default).

�Voice: Focused on human speech or singing. Note that this is not a good option for other material.

�General Purpose: Ideal for music and effects.

Elastic View

Elastic view shows Elastic Wave “time points,” which are similar, but the not the same as, Resolve

keyframes. Keyframes represent a point in time plus a value, and Elastic Wave time points represent

only a point in time.

When Elastic View is enabled, time points are visible on the selected clip.

Elastic Wave time points

Elastic Wave disabled

When disabled, the time points are not visible, but the info lane still shows that Elastic Wave is enabled

with the Elastic Wave icon.

Clearing Timing Points

“Timing points” are the moveable Elastic Wave control points that stretch or compress a given area of

a clip. If you choose “Clear Timing Points,” all selected points within a clip are cleared (deleted).

Elastic Wave can operate in the Edit window where video editors may want to re-time spoken word

performances so that when the audio is re-timed, the video follows the retiming to match. However,

when working in the Fairlight page, re-timing of video is disabled so that you can have separate

control of the audio file.


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

About Audio Plugins

There is no limit to the number of single or multiple plugins when in FlexBus mode that can be applied

to clips and to tracks. However there is a limit of 480 when using Fixed Bus Legacy. Plugins are

accessed via each track’s control strip, or via the Inspector which provides access to both clip and

track plugins.

Fairlight FX

Fairlight FX are proprietary DaVinci Resolve-specific plugins that run natively on macOS, Windows,

and Linux, providing high-quality audio effects with professional features to all DaVinci Resolve users

on all platforms.

Most Fairlight FX plugins, including Channel Dynamics and EQ, and dynamics processors like the

Multiband Compressor, Limiter, Reverb, and Ambisonics Meter, are Ambisonics native and offer

multichannel processing.

VST and VSTi

VST (Virtual Studio Technology) is an audio plugin standard created by Steinberg. The VST standard

allows third-party developers to create plugins for use within VST host applications or create VST host

applications.

The Fairlight page supports VST effects from Mono to 7.1 and beyond. These effects can be inserted

on mono channels or Link Groups, and compatible VST Ambisonic effects can be used on Ambisonic

tracks or busses.

If a stereo VST effect is inserted on an LCR, LCRS, or 5.1 Link Group, the left and right channels will

automatically be allocated to the left and right Link Group channels.

DaVinci Resolve supports VST3. VST effects are available on macOS and Windows

workstations, but not on Linux.

VST Effects versus VST Instruments (VSTi)

A VST effect is a type of VST plugin that is used to process audio. A VST effect might be a Reverb,

Compressor, or EQ. VST Instruments are typically used to synthesize sound or play back sampled

audio. VSTs have rapidly replaced hardware synthesizers and dedicated samplers due to their

flexibility, repeatability, and low cost.

Audio Units

Audio Units is an audio plugin API created by Apple for use on macOS workstations. Like VST,

Audio Units (AU) can either process audio or work as instruments.

Compatible AU Ambisonic effects are used on Ambisonic tracks or busses.


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

Using Audio Plugins

Fairlight FX are pre-installed with all DaVinci Resolve installations. If you install additional VST or

Audio Unit effects on your workstation, they appear in the Audio FX panel of the Effects Library,

organized in separate categories.

Audio plugins in the Effects Library

You can click on the far right of any effect to flag it with a star as a favorite effect. When you do so, the

favorited effects appear in a separate Favorites area at the bottom of the Effects Library Bin list, and it

also appears at the top of the Effects button’s menu on the Mixer when you click the “plus” button.

Stars indicate a flagged favorite effect; all favorites are currently filtered

Audio plugins let you apply effects to individual audio clips or entire tracks worth of audio, to add

creative qualities such as echo or reverb, or to take care of mastering issues using noise reduction,

compression, or EQ.


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

Applying Plugins

Methods of applying audio plugins to clips on the Fairlight page:

�To apply an audio effect to a clip: Drag any effect from the Audio FX panel of the Effects Library

onto the clip in the Timeline you want to apply it to.

�To apply an audio effect to multiple clips: Select all of the clips you want to apply an audio

effect to, then drag any effect from the Audio FX panel of the Effects Library onto any of the

selected clips.

When you apply an audio plugin to a clip, a badge appears to the left of that clip’s name bar in the

Timeline to let you know there’s an effect applied to it.

Timeline clips with audio plugins applied appear with a badge.

Methods of applying audio plugins to tracks on the Fairlight page:

�To apply an audio effect to an entire track in the Timeline: Drag any effect from the Effects

Library onto the track header.

Applying an audio effect to a whole track via the Timeline

�To apply an audio effect to a track or bus in the Mixer: Drag any effect from the Audio FX panel

of the Effects Library onto the clip in the Timeline you want to apply it to.

Applying an audio effect to a whole

track via drag and drop to the Mixer

�To apply an audio effect to a track or bus using the Mixer controls: Click the plus button in

the channel strip of the track you want to apply an effect to, and then choose an effect from the

dropdown menu that appears. All filters appear within categories to make them easier to find. If

you’ve clicked the star button of any filters in the Effects Library to favorite them, these favorite

filters appear at the top of the plus button’s dropdown list.

�To copy audio effects from one mixer channel to another: Hold the Option key and click and

drag the effect to the desired channel and slot to copy.

�To reorder audio effects in the Mixer: Click and drag the audio effect to move to the desired

slot position.


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

Applying an audio effect to a whole track via the Mixer’s own controls

TIP: The categories that VST and Audio Units effects are organized into in the Mixer can

be edited in the Audio Plugins panel of the DaVinci Resolve System Preferences window.

All plugins on a workstation are shown in the Available Plugins list, and clicking within the

Category column lets you use a dropdown menu with which to change categories.

NOTE: This does not apply to Fairlight FX plugins.

Editing Plugin Parameters

To edit a clip’s audio plugins:

�Select that clip and open the Inspector. All audio plugins applied to that clip appear in the Effects

tab, with that effect’s controls appearing directly in the Inspector.

To edit a track’s audio plugins, do one of the following:

�Click in the background of the Timeline header to select that track, and then open the Inspector.

Click the custom UI button for that effect to open its controls.

The custom UI button for audio

plugins in the Inspector

�Move the pointer over the plugin’s name in the Effects area of the Mixer, and click on the custom

UI button to open its controls.


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

The custom UI button for

audio plugins in the Mixer

Nearly all Fairlight FX, VST, and Audio Unit audio plugins have a custom user interface that

makes it much easier to manipulate that effect’s controls. These can be opened from within

DaVinci Resolve.

The custom audio effect interface for iZotope RX Voice De-noise