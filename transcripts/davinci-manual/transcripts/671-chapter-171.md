---
title: "Chapter 171"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 671
---

# Chapter 171

Setting Up Tracks,

Busses, and

Patching

One of the first things you need to do when you’re setting up a new project for

mixing in the Fairlight page is to define the audio tracks and busses you’ll need to

route and combine the elements of your mix.

This chapter covers how to create audio tracks and how to use busses to manage your mixes in the

most efficient possible way. However, the Fairlight page gives you the flexibility to add or change

your set up at any time; you can also concentrate on being creative and deal with any required

housekeeping as your mix evolves.

Fairlight’s FlexBus structure supports bus-to-bus, track-to-bus, or bus-to-track signal routing,

along with expanded Dolby Atmos capabilities, including import, export, and manipulation of

Atmos ADM files.

Contents

Audio Tracks����������������������������������������������������������������� 3720

What Is a Bus?��������������������������������������������������������������� 3721

Surround Panning and Bussing ��������������������������� 3721

Bus to Bus Routing and Mixing����������������������������� 3721

Using Legacy Fixed Bussing��������������������������������� 3722

Busses in Nested Timelines���������������������������������� 3723

Exposing Bus Tracks in the Timeline����������������� 3723

Controlling Signal Flow������������������������������������������� 3723

Defining Audio Track Types����������������������������������� 3723

Rearranging Tracks���������������������������������������������������� 3725

Duplicating Tracks������������������������������������������������������ 3725

Deleting Tracks������������������������������������������������������������ 3726

Disabling Tracks���������������������������������������������������������� 3726

Changing Track Type������������������������������������������������ 3727

Link Grouping��������������������������������������������������������������� 3727

Working Separately with

Multichannel Audio File Elements���������������������� 3729

Creating Busses���������������������������������������������������������� 3730

Assigning Busses������������������������������������������������������� 3732

Bus Assignment Using the Mixer������������������������ 3732

The Bus Assign Window������������������������������������������ 3733

Setting Signal Paths�������������������������������������������������� 3734

Using the Patch Input/Output Window������������� 3734

Using a Channel Strip’s Input Menu������������������� 3738

Input Menu with Legacy Fixed Bussing����������� 3740

The Fairlight Presets Library�������������������������������� 3740

Using the Presets Library����������������������������������������� 3741


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

Audio Tracks

Each audio track in a DaVinci Resolve timeline corresponds to a single channel strip on the Mixer’s

left side. Depending on how an audio track has been configured, each audio track is assigned a

specific audio format, such as mono, stereo, 5.1 or 7.1 surround, or Dolby Atmos. Track routing allows

multiple audio channels within the clips on a track to be correctly routed to the proper audio output for

monitoring and rendering via the lanes that can be seen within each track on the Fairlight timeline.

Audio tracks in DaVinci Resolve often contain multiple channels from a given clip, but how those

individual audio channels are displayed depends on the page:

�The Cut and Edit pages display a single clip “lane” per audio track in the Timeline, regardless

of how many channels the clips on that track are representing. The waveform displayed is a

composite, showing a mix of the various channels within the clip.

�This can make it easier to work with multichannel tracks without the distraction of viewing multiple

channel lanes, which could make things look a lot “busier.” However, the tradeoff is that detailed

activity on any of the various channels on that track are not seen.

�The Fairlight page displays the same number of tracks as the Edit page, but each track on the

Fairlight page is divided into lanes, which shows each individual channel of a clip’s audio. This

additional visual information can help with editing and mixing.

(Top) 6 channel and stereo audio in the Cut and Edit pages represented by single

composite tracks. (Bottom) The same audio in the Fairlight page shows the six channel

and stereo tracks with multiple lanes that correspond to each of the file types.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

Now that you understand how tracks work on the Fairlight page, the next important concept you need

to understand in order to unlock the power of the Fairlight page is FlexBus, which lets you combine

multiple audio tracks in different ways.

What Is a Bus?

A bus is simply a common signal connection point in an audio mixer. Busses can be mono, stereo, or

any larger format, like 5.1 or Dolby Atmos 9.1.6 (where 16 audio signals are used). Bussed connections

are mixed together into a single signal that can be controlled via a single bus channel strip. For

example, by default a single bus called “Bus 1” combines the levels of every clip edited onto every

track of a timeline into the mixed signal that is output to your speakers or headphones.

You can use busses in creative ways to organize mixing of tracks in a timeline. For example, if you

have five audio tracks that have all of the edited dialogue audio clips for a particular program, you can

route the output of all five dialogue tracks to a dedicated submix bus. This allows the combined levels

from all the contributing dialogue tracks to be processed, adjusted, and mixed at once using a single

channel strip’s controls.

You can use multiple busses to organize a mix, including routing submix busses into other “main

busses.” Individual tracks can be routed to submix busses, then multiple submixes can be routed to

one or more “main output” busses. For example, you could have four submix busses, one for German

dialogue, one for English dialogue, one for Music, and one for Effects. You could route the German,

Music, and Effects submix busses to a Main 1 bus to output the German version of the program, and

route the English, Music, and Effects submix busses to a Main 2 bus to output the English language

version of the program.

Surround Panning and Bussing

When working on surround or immersive formats, audio tracks from the Timeline are routed to busses

via each channel strip’s multi-format surround panner, so busses can be configured to accommodate

specific audio formats, such as mono, stereo, LCRS, 5.1 surround, or 7.1 surround, and immersive

formats, such as Atmos. By using multiple bus routing, you can even output different formats

simultaneously.

Bus to Bus Routing and Mixing

Fairlight’s FlexBus structure offers complete user flexibility for bus types and signal routing, allowing

completely user-definable bussing, and making it possible to patch outputs and/or sends in any way

you need, as dictated by your project. Each track can output to up to ten busses and sends with

additional level and pan controls to a further ten busses. Busses can be sent to other busses up to six

layers deep, facilitating complex stem building, processing, and allowing discrete deliverables.

User-definable busses allow for bus-to-bus, bus-to-track, or track-to-bus routing, with each bus having

the ability to pass signals from mono to fully immersive formats, such as Dolby Atmos. As with any and

all of the track types in Fairlight, these bus types can be changed at any time if needed.

The power of the FlexBus system is that it allows users to direct signals to many different places at one

time, achieving complex mixing scenarios. Perhaps you need to generate two mixes that are identical

in content but need to be of different output levels. You can designate two mix busses, one with an

output level of -2dB true peak and one with an output level of -10dB true peak. The final mix signal is

sent to one bus that is then broken into two more busses, one with a limiter set to -2dB and one set to

-10 dB, creating these two different mixes at one time.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

The FlexBus structure allows for many different bus

track types to be created or changed.

Using Legacy Fixed Bussing

If you want to work using the previous method of Fixed Bus mapping, you can do so for new projects by

opening the Fairlight panel of the Project Settings, and turning on the “Use fixed bus mapping” checkbox.

If your project has Fixed Bussing enabled and you want to change to FlexBus, then uncheck the

“Use fixed bus mapping” checkbox. Note that once you have made the change it will not allow you to

change it back to legacy bussing.

For more information see Chapter 177, “Mixing in the Fairlight Page.”

Converting Older Fixed Bus Projects to FlexBus

Older Fixed Bus projects can be converted to FlexBus by doing the following:

•	 Open Project Settings > Fairlight.

•	 Under the Bussing heading, uncheck “Use fixed bus mapping.”

•	 A dialog will appear allowing you to convert the project to FlexBus.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

Busses in Nested Timelines

When you nest a timeline inside another timeline that has busses set up for mixing in the Fairlight

page, all bus routings continue to work as intended within the nested timeline, which exposes all

channels via the default main bus (Bus 1) in the enclosing timeline. In this sense, the audio of the

nested timeline can be considered to be a submix that outputs its resulting audio to the audio track it’s

edited onto. However, you can also decompose your nested timeline into its own bus structure within

the main timeline you’ve imported into, exposing all of the original tracks as they were.

This is a very powerful feature for combining work done at different times or by different

contributors, see Chapter 177, “Mixing in the Fairlight Page.” in section Nested Audio Timelines

for more information.

Exposing Bus Tracks in the Timeline

You can expose any bus as a track in the Timeline. This makes it possible to view and edit automation

that is applied to parameters on that bus.

To show a bus in the Timeline:


Enable the Toggle Automation button on the Fairlight toolbar. All busses are visible by default.


If you want to hide a bus, open the Index, and click the eye button for the bus you want to hide in

the Timeline.


If you want to work with automaton on a bus, choose the desired automation curve you want to

view from the dropdown menu in the track header controls.

Controlling Signal Flow

A good process for setting up editing and mixing in the Fairlight page is:

�Organize and configure the tracks on your timeline as required.

For example, clips well organized on tracks, set track types, color, grouping, etc.

�Create the busses needed to organize the desired signal flow in the mix.

�Route the audio tracks, or any submix busses to the desired bus destinations for the mix layout.

Defining Audio Track Types

If you decide to create a new audio track, you have to choose what kind of audio track it will be. Right-

clicking in the bottom audio portion of the Timeline track header reveals a contextual sub-menu that

lets you create different kinds of audio tracks.

�Mono: Holds a single channel with only one lane.

�Stereo: Holds stereo left and right channels, with two lanes.

�3.0: Holds three channels, with three lanes in either LRC (Left, Right, Center) or LCR

(Left, Center, Right) format.

�4.0: Holds four channels, with four lanes in either LRCS (Left, Right, Center, Surround), LCRS (Left,

Center, Right, Surround), or Quad format.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

�5.x: 5.0 holds five channels corresponding to a 5.0 surround mix, for a total of five lanes.

For broadcast, SMPTE specifies Left, Right, Center, Surround Left, and Surround Right.

For cinema distribution (5.0 Film), these tracks are ordered Left, Center, Right, Left Surround, and

Right Surround.

5.1 holds six channels corresponding to a 5.1 surround mix, for a total of six lanes. For broadcast,

SMPTE specifies Left, Right, Center, LFE, Surround Left, and Surround Right. For cinema

distribution (5.1 Film), these tracks are ordered Left, Center, Right, Left Surround, Right

Surround, and LFE.

�7.x: 7.0 holds seven channels corresponding to a 7.0 surround mix, for a total of seven lanes.

For broadcast, SMPTE specifies Left, Right, Center, Left Surround, Right Surround, Back Left

Surround, and Back Right Surround. For cinema distribution (7.0 Film), these tracks are ordered

Left, Center, Right, Left Surround, Right Surround, Back Surround Left, and Back Surround Right.

7.1 holds eight channels corresponding to a 7.1 surround mix, for a total of eight lanes.

For broadcast, SMPTE specifies Left, Right, Center, LFE, Left Surround, Right Surround, Back Left

Surround, and Back Right Surround. For cinema distribution (7.1 Film), these tracks are ordered Left,

Center, Right, Left Surround, Right Surround, Back Surround Left, Back Surround Right, and LFE.

�Adaptive: Holds up to 24 audio channels, each with its own lane within the track. An adaptive

audio track can hold clips with different combinations of channels, up to the maximum number of

channels allowed within that track. The number of channels allowable on a particular Adaptive

track is user-definable (1–24) at the time that track is created. If you edit a clip with more channels

into an Adaptive track that was created to hold fewer channels, the extra clip channels are muted.

�Dolby Atmos: There are several Dolby Atmos formats available: 5.1.2, 5.1.4, 7.1.2, 7.1.4, and 9.1.6.

The naming of the channel configurations in the Dolby Atmos format includes the height channels

in the nomenclature. Channel configurations are presented as three digits separated by periods,

such as 7.1.4. The first digit describes the number of main, or ear-height monitoring channels that

surround the listener. The second digit describes the number of subwoofer channels. The third

digit describes the number of height channels, which are speakers positioned on, or in the case of

a soundbar pointed to, the ceiling.

NOTE: The Dolby Atmos bus formats of 9.1.4, 9.16, and 22.2 are only available in DaVinci

Resolve Studio and also require that Dolby Atmos be enabled in Preferences > Video and

Audio I/O > Immersive Audio.

Adding Tracks (Contextual Menu)

There are two commands related to adding tracks in the right-click contextual menu on any audio

track’s header controls:

�Add Track: Adds a single audio track of the type you choose from a submenu.

�Add Tracks: Lets you insert as many tracks as you like, designating the track type and position in

relation to other tracks in the Timeline.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT