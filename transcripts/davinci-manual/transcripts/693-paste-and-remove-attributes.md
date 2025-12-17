---
title: "Paste and Remove Attributes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 693
---

# Paste and Remove Attributes

for Clips and Tracks

The Fairlight page has Paste Attributes and Remove Attributes commands that allow for the copying

and resetting of audio parameters and effects, similar to the same commands on the Edit page.

The Paste Attributes dialog in the Fairlight page

The Paste Attributes dialog box gives you three types of attributes to choose from. Volume will paste

the copied attributes to the clip. Plugins will paste any plugin attributes to the clip. Equalizer will past

EQ data copied from another clip. One or all of these can be copied at one time.

The Remove Attributes dialog box gives you the same three types of attributes to choose from

for removal of a clip. When the Volume box is enabled, all Clip Gain keyframes will be removed

from the clip.


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

Chapter 177

Mixing in the

Fairlight Page

The Mixer is “control central” of the Fairlight page, providing all of the functionality

you need to mix the various audio tracks of your program into a harmonious whole.

By using EQ, dynamics, panning, level control, and Fairlight FX, VST and Audio Units audio plugin

effects of all kinds, all with full automation, you can hone your sound and balance each track’s

elements with one another.

This chapter focuses on explaining the various functions of the Mixer so you can harness its

power for yourself.

Contents

Introduction to Mixing��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3845

The Mixer����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3845

Tracks and Busses����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3845

FlexBus Routing and Mixing��������������������������������������������������������������������������������������������������������������������������������������������������������� 3846

Customizing the Onscreen Mixer Controls�������������������������������������������������������������������������������������������������������������������������� 3849

Selecting Channel Strips and Tracks�������������������������������������������������������������������������������������������������������������������������������������� 3850

Track Organization���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3851

Rearranging Tracks��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3851

Disabling Tracks��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3852

Managing Channel Strips Using the Index�������������������������������������������������������������������������������������������������������������������������� 3853

Fairlight Mixer Signal Path������������������������������������������������������������������������������������������������������������������������������������������������������������ 3855

What Is An Effects Insert?�������������������������������������������������������������������������������������������������������������������������������������������������������������� 3855

Input��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3856

Path Settings���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3856

Effects����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3858

Changing the Order of Effects on a Channel����������������������������������������������������������������������������������������������������������������������� 3859

Moving Inserts by Dragging��������������������������������������������������������������������������������������������������������������������������������������������������������� 3859

Copying and Pasting Effects�������������������������������������������������������������������������������������������������������������������������������������������������������� 3859


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Copying and Pasting Effect Settings���������������������������������������������������������������������������������������������������������������������������������������� 3860

Effects In������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3860

Dynamics������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3861

The Dynamics Graph������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3861

Master Dynamics Controls������������������������������������������������������������������������������������������������������������������������������������������������������������ 3862

Expander/Gate������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3863

Compressor������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3863

Limiter������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3866

EQ�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3866

Master EQ Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3867

The EQ Graph�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3868

Bands 1 and 6��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3868

Bands 2 – 5������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3869

Bus Sends��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3869

Creating Sends����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3870

Accessing the Bus Sends Window�������������������������������������������������������������������������������������������������������������������������������������������� 3870

Legacy Bus Sends – “Auxiliaries”����������������������������������������������������������������������������������������������������������������������������������������������� 3871

Pan������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3871

Channel Strip Pan Controls������������������������������������������������������������������������������������������������������������������������������������������������������������ 3871

2D Panner Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3872

3D Panner Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3875

Bus Assignment Buttons��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3879

Legacy Mixer Bus Assignment���������������������������������������������������������������������������������������������������������������������������������������������������� 3879

Nested Audio Timelines����������������������������������������������������������������������������������������������������������������������������������������������������������������� 3879

VCA Faders������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3882

Making Fader VCA Assignments����������������������������������������������������������������������������������������������������������������������������������������������� 3883

Using VCA Faders����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3883

Recording Fader Automation for VCAs����������������������������������������������������������������������������������������������������������������������������������� 3884

Nesting VCAs��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3884

Arm, Solo, and Mute Buttons������������������������������������������������������������������������������������������������������������������������������������������������������ 3885

Fader Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3886

Metering Options������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3887

Level Metering Options������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3887

Pre-fader Metering���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3887

Target Loudness Level�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3888

Bouncing Audio���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3888

AI Audio Assistant (Studio Version Only)������������������������������������������������������������������������������������������������������������������������������� 3889

Third-Party Control Panel Support for Mixing������������������������������������������������������������������������������������������������������������������� 3890


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Introduction to Mixing

This chapter describes how to use the Mixer to adjust the levels and fine-tune the audio of each track

in the timeline. It’s focused on the function of the channel strip controls, with the following exceptions:

For more information about bussing, see Chapter 171, “Setting Up Tracks, Busses, and Patching.”

For more information about recording audio, see Chapter 173, “Recording.”

For more information about mix automation, see Chapter 178, “Mix Automation.”

The Mixer

The Audio Mixer provides a set of graphical controls you can use to assign track channels to output

channels, adjust EQ and dynamics, set levels and record automation, pan stereo and surround audio,

mute and solo tracks, and add Fairlight FX, or VST, or AU effects plugins. At its most basic, each audio

track in your timeline corresponds to an individual channel strip in the Mixer, and by default there’s a

single main stereo mix bus labeled “Bus 1” that combines all these tracks into an overall mix.

The Audio Mixer with channel strips corresponding to the tracks in the Timeline

Tracks and Busses

Once you start creating busses, the Audio Mixer exposes two sets of channel strips. The leftmost set

of channel strips correspond to the audio tracks in the Timeline, while the right-most set of channel

strips expose sets of controls for each bus that you’ve created.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

By default, the Audio Mixer is divided into two sections, one for tracks (at left) and one for busses (at right).

If you have more tracks and busses than can be displayed all at once given the width of your computer

display, then each half of the Mixer has independent scroll bars so you can choose which tracks and

which busses you want to see next to one another. You can also remove the split between sections

and have a single, continuously scrollable view with all tracks, or change the order or split point for

the channels.

FlexBus Routing and Mixing

The Fairlight audio engine bussing system is called FlexBus. As its name suggests, FlexBus offers a

hight level of flexibility for bus types and signal routing. DaVinci Resolve Fairlight’s older Fixed Bus

configuration (prior to DaVinci Resolve v17) offered a more limited fixed bus topology, and can still be

used, but FlexBus makes it possible to patch outputs and/or sends in any way required, as dictated by

your project.

With FlexBus, each track can output to up to ten busses and sends with additional level and

pan controls to a further ten busses. Busses can be sent to other busses up to six layers deep,

facilitating complex stem building, processing, and allowing discrete deliverables.

For more information, see Chapter 171, “Setting Up Tracks, Busses, and Patching.”

What is a Bus?

A bus is simply a common signal connection point in an audio mixer. Busses can be mono, stereo, or

any larger format, like 5.1 or Dolby Atmos 9.1.6 (where 16 audio signals are used). Bussed connections

are mix points for the audio, allowing each audio track feeding their signals to the bus to be summed

together to create a master output for that bus.

Bus-to-Bus Routing

A mix may use a single bus (for example, the default stereo Main 1 bus may be all that you need if

you’re doing basic stereo mixing). Or you can create “submixes” where multiple busses feed into other

busses to create a master mix. For example, you might have a dialogue bus, an effects bus, and a

music bus so you have control over those elements separately via the bus “masters” for each, then

feed the 3 masters into a main output bus for final mix rendering.

You may want to route the output of a bus to an audio track to record the resulting signal, or route to

monitor speakers to listen to the real time output. Finally, the Deliver page can render the output of

your designated master bus to create a final bounced file.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

The FlexBus structure allows for many different bus

track types to be createdµ or changed.

User-definable busses allow for bus-to-bus, bus-to-track, or track-to-bus routing, with each bus having

the ability to sum together signals from mono to fully immersive formats (such as Dolby Atmos and

Ambisonics) at your discretion. As with any and all of the audio track types in Fairlight, you can change

bus types at any time if needed.

The power of the FlexBus system is that it allows you to direct signals to many different places at one

time to achieve complex mixing scenarios. Perhaps you need to generate two mixes that are identical

in content but need to be of different output levels. You can designate two mix busses, one with a

target output level of -14 LUFS and one with a target output level of -24 LUFS. The final mix signal is

sent to one bus that is then broken into two more busses, one with a limiter set to accommodate the

-14 LUFS mix and one set to the correct level for the -24 LUFS mix, allowing you to create these two

different mixes at one time.

In Ambisonic workflows, you can route an Ambisonic bus to another Ambisonic bus, even with differing

orders, and any required up- or down-mixing is automatically handled by the Fairlight engine and FlexBus.

FlexBus supports expanded Dolby Atmos capabilities and Ambisonics; for more information

see Chapter 184, “Immersive Audio Workflows.”

FlexBus bus routing buttons


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Legacy Fixed Bussing

Prior to DaVinci Resolve 17, the Mixer had a fixed topology with specific, fixed numbers of sends,

submix busses, and main outputs. DaVinci Resolve still supports this older “legacy” bussing topology

to maintain compatibility with earlier projects.

With the current FlexBus bussing, the Mixer looks slightly different. The Aux panel on the legacy Mixer

has been renamed Bus Send, and the Main/Submix panel has been changed to Bus Outputs.

In the legacy Fixed Bus view:

�Each audio track’s channel strip has a set of Main and Submix bus buttons that let you assign the

audio output by that channel strip to a Sub (typically used to combine different subsets of tracks

into submixes) or to a Main (typically used to output or render overall mixes).

�Each Sub and Aux’s channel strip has a set of Main buttons so that different combinations of Subs

can be assigned to each Main. Main channel strips have no buttons because, from a bussing

perspective, they’re the final output.

�Main and Submix buttons let you assign tracks to busses, and busses to other busses.

Main and Submix bus buttons

Using Legacy Fixed Busing

If you want to work using the previous method of Fixed Bus mapping, you can do so

for new projects by accessing the Project Settings > Fairlight panel, and turning on the

“Use fixed bus mapping” checkbox. However, as there is no practical advantage to using

the older legacy fixed bus system, and several features are only available in FlexBus, using

FlexBus is recommended.

Converting Older Fixed Bus Projects to FlexBus

Older Fixed Bus projects can be converted to FlexBus by doing the following:

�Open Project Settings > Fairlight.

�Under the Bussing heading, uncheck “Use fixed bus mapping.”

�A dialog will appear, allowing you to convert the project to FlexBus.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT