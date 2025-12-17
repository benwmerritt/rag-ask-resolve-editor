---
title: "The Monitoring Panel"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 718
---

# The Monitoring Panel

Turning on the meters in the UI toolbar displays the Monitoring panel that runs along the top of the

Fairlight page, which shows all of the audio meters that correspond to the tracks in the Timeline, as

well as the Bus meters that correspond to the Mains, Subs, and Aux busses of your mix, the Control

Room meters, and a video viewer.

The Monitoring panel

With the increased track counts necessary for immersive audio, DaVinci Resolve gives you options for

extra metering so you can see more tracks in real time.

Right-clicking anywhere on the meters opens a menu that lets you choose between viewing them as

a single-row or double-height Track display. This menu also allows you to choose between narrow or

wide meters. When using the wide meter view, double-clicking anywhere on the Tracks meters panel

switches between single-row and double-height view.

Hovering a mouse below the Tracks panel reveals a cursor that lets you change the height of the

Monitoring panel.

The Compound meters and the Bus Output meters can also be resized by hovering on the right side of

the Loudness meter and dragging to the desired dimensions.

The double-height Monitoring panel

Track Meters and Monitoring Controls

At left, a row of audio meters corresponds to the channel strips of the Mixer, one meter for every audio

track in the timeline. Each track displays the number of meters that corresponds to that track’s audio

mapping, with mono tracks having a single audio meter, stereo tracks having two, 5.1 tracks having six,

and so on.


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT

Each track and bus meter (with the exception of the Loudness meters) display RMS (root mean square)

levels against a dB scale. A single line indicating the maximum value at any given moment in time is

held briefly just above the current RMS levels, which appear as a solid bar extending from the bottom

of the meter. RMS meters display a weighted “average” representation of the audio level that’s closer

to the way audio is actually perceived, although not as accurate in measuring perceived loudness as

the loudness meters discussed later in this section.

Track audio meters with different

numbers of meters depending

on that track’s audio mapping

The peak

meter at top

Each meter bar is color coded to indicate three different sound level “zones,” from low to medium

(green) to moderately high (yellow) to very high (red).

Each meter is identified by the track number it represents (track names are not shown over track

meters) as well as the color of that track.

Bus Meters

To the right of the track meters are the bus meters, in which all user-created mains and busses appear,

separated by type, and each displaying the number of meters that corresponds to that track’s audio

mapping. These meters allow you to monitor the sum of all tracks that have been routed to a particular

bus, as you can on bus channel strips.

Bus meters for the Mains, Subs, and Aux busses


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT

Meter Plugin

There is a Meter plugin available for temporarily adding a meter to a specific track, FlexBus, or when

using fixed busing to Sub, Aux, or Main. These are sample peak processing meters that are useful for

instances where you want a large meter that focuses on a specific bus while you’re working.

These meters are presented very simply, with a gray bar indicating level and a red peak line that holds

for two seconds, which indicates the highest peak. A numeric reading at the top of the meter gives the

exact level, in dB. This number continues to hold, indicating the loudest level measured for any given

stretch of playback. The option menu in this meter’s floating window presents different settings you

can choose.

For more information, see Chapter 181, “Fairlight FX.”

The Meter Fairlight FX

The signal here is radiating more to the

right, indicating the panning of the audio.

Surround Analyzer

The Surround Analyzer is a graphical meter that shows a spatial image of the audio being measured,

rather than a typical bar graph meter. Due to its changing shape because of the signal being played,

sometimes it is referred to as the “jellyfish meter.”

This type of metering is very useful; rather than relying on bars to indicate the directions in which

audio is radiating, you can clearly see the relationship of all of the channels to one another.


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT

Compound Meters and

Output Bus Selection Menu

The compound meters, to the right of the bus meters, consist of Control Room meters and Loudness

meters, shown side-by-side to provide a comprehensive analysis of your overall audio mix. Below,

dropdown menus let you choose which bus you want to monitor, as well as which set of speakers you

want to use to do the monitoring.

The Control Room meters (at left)

and Loudness meters (at right)

Monitoring Menus

Bus Monitoring Menu

The bus monitoring dropdown menu determines which bus is monitored by your audio output

(speakers or headphones), and thus which gets analyzed by the compound meters, letting you choose

which bus you want to monitor as you work. You can choose one of your mains or any other bus (or

track) you’ve set up that you want to focus on for more detailed work.

The monitoring menu lets you choose which

bus you want to monitor while working.

Speaker Set Monitoring Menu

To the right of the Monitoring menu, the output is set to “Auto” by default (if you have Automatic

speaker configuration checked on in Preferences > Video and Audio I/O > Audio I/O). This means

that your basic speaker set up is routed to the stereo or surround output your hardware supports

automatically and can’t be altered.


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT

Monitoring with Multiple Speaker Sets

If you want to manually configure multiple speaker sets, unchecking the automatic speaker

configuration preference will display a dropdown to the right and lets you choose one of the

available sets of speakers once they have been configured in the Video and Audio I/O panel

of the System Preferences. This gives you the flexibility to quickly compare your mix on a

variety of speakers and configurations to see how it holds up in different situations.

For more information on configuring different speaker setups, see Chapter 4, “System and

User Preferences.”

The monitoring menu lets you choose which bus you

want to monitor while working.

Control Room Meters

The mustard-colored Control Room audio meters show the sum of all audio channels that are routed

to the currently selected bus being monitored (as selected in the dropdown menu below). These are

peak meters measured in dBFS.

A true peak audio measurement is displayed at the top of the Control Room meter.

Loudness Meters

The set of meters all the way to the right are the Loudness meters, which consist of a set of two

graphical meters and a numerical readout. This lets you keep track of the “integrated loudness” of the

overall mix, which is the standard that all contemporary mixing specifications refer to when specifying

client deliverables. Unlike the RMS audio meters found in the Timeline or Mixer, which measure audio

in dB, Loudness meters do a different kind of analysis, measured in LUFS (loudness units relative to

full scale).

What Is LUFS?

LUFS measurements evaluate sound levels that are averaged over time referenced to full

scale. Full scale is the loudest level a digital audio system can handle before overloading

(“clipping”). LUFS allows totally different types of program material to be matched in perceived

level by human ears and has become the standard way that mixes are measured for final

delivery of your program material. LUFS are shown as negative numbers, such as -23, -14, etc.,

because the level is referenced to full scale (digital 0).


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT

Loudness Meter Options

Two options in the General Options of the Project Settings let you customize the Loudness meters.

�Target Loudness level: Lets you set the LUFS value that’s used as a reference level for loudness

metering. Defaults to –23 LUFS, which conveniently makes the display of these meters scale

similarly to traditional audio meters that you’re already used to.

�Loudness Scale: Lets you choose which scale you want to use with which to measure the meters.

Options currently include the default of EBU +9 Scale (–18 to +9), and EBU +18 Scale (–36 to +18).

Support for Multiple Loudness Standards

The Loudness Meter can be switched among a variety of international industry-standard loudness

monitoring standards. The standard you choose uses the integrated loudness value (along with a

specified tolerance defined by each selected standard) to indicate whether or not the current mix level

is of acceptable loudness via color coding of the Integrated Loudness value, and in the Integrated

Loudness graph described below. Blue values indicate loudness levels that are below tolerance,

yellow indicates loudness values that are within tolerance, and red indicates loudness values that

are above tolerance.

The built-in standards you can switch among include the following:

BS.1770-1: An older loudness standard used by DaVinci Resolve version 15 and before.

BS.1770-4: The most up-to-date loudness standard as of DaVinci Resolve 16; the

algorithms specified by this standard govern the other standards that are listed below

in this dropdown menu.

ATSC A/85: The American standard for acceptable loudness in broadcast.

EBU R128: The European standard for acceptable loudness in broadcast.

OP-59: The New Zealand and Australian standard for acceptable loudness in broadcast.

TR-B32: The Japanese standard for acceptable loudness in broadcast.

AGCOM 219: The Italian standard for acceptable loudness in broadcast.

NETFLIX: The Netflix standard for acceptable loudness in broadcast.

YouTube: The YouTube standard for acceptable loudness in broadcast.

Disney 2.0: The Disney 2.0 standard for acceptable loudness in broadcast.

Disney 5.1: The Disney 5.1 standard for acceptable loudness in broadcast.

All of these loudness standards are available for off-line readings as well, using the Loudness

Analyzer described in the next section.

NOTE: The target peak meter now uses the BS.1770-4 standard for measuring maximum

“true peak,” which means that this meter is capable of measuring “inter-sample peaks,” rather

than only the peaks at each sample of a waveform.


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT

Graphical Loudness Meters

Two separate meters give you a dynamic graphical measurement of the loudness of the selected

bus being monitored according to the loudness standard you’ve selected, which determines how

to analyze the subjective loudness of a given audio mix for purposes of compliance with required

broadcast quality control (QC) standards.

�A steel-blue meter labeled M (for momentary) has as many channels as the selected bus you’re

monitoring, excluding the LFE channel(s) of surround formats, which aren’t factored into loudness

metering. This meter measures LEQ (equivalent sound level), within a 400ms window following the

playhead as measured every 100ms. This lets you evaluate the LUFS (Loudness Units Full Scale)

level of the mix at the current frame as you play. This discrete-channel analysis is used to calculate

all other values of the loudness metering system.

�A second steel-blue mono meter to the right displays the sum of all channels in the M meter,

displayed in LU (loudness units). The number value displayed at the top of this meter is the

maximum LU value that’s been analyzed during any stretch of timeline playback. This value is held

until it’s reset, either by stopping and initiating playback a second time while Link to Playhead is

enabled, or when you click the Reset button at the bottom of the loudness meter area.

Numeric Loudness Meters

A set of values to the right of the meters give running reports on the audio level of your mix. While the

graphical meters are useful for analyzing your mix as you work, these numeric readouts are particularly

valuable for providing the strict information you need to adhere to written QC standards. Their

meaning is as follows:

Short: Measures the average LU level over a 30-second window following the playhead.

Short Max: Shows the maximum level over the same 30-second window. This analysis is

required by EBU R128.

Range: Measures the dynamic range of the Loudness of your mix (in LU, or loudness units),

which is the difference between the average soft and average loud parts of your mix.

Analyzes the overall loudness over a played range of the mix, discounts the lowest 10%

and highest 5%, and then gives a standardized expression of the difference between the

remaining soft and loud levels that were analyzed. The window of analysis is as long as you’ve

been playing. This analysis is required by most QC specifications.

Integrated: Measures the LUFS value of the portion of the range of the mix you’ve played

through. As you play, this integrated value accumulates. This analysis is required by most QC

specifications.

Absolute Scales and Dialog

While some users prefer to measure their levels to correspond to a relative scale of “0,” similar to

a VU meter where the needle rides above the “0,” others want to see the absolute measure of the

amplitude in LUFS and true peak. By default, the Loudness meter is set to relative scale, but you now

have the option to choose between relative scale and absolute scale in the Loudness meter.

Relative scale in the Loudness menu is relative to the selected scale, so a loudness unit of 0

corresponds to the target of the chosen measure type. For instance, if EBU R128 is selected, whose

target measure is -23dB LUFS, the “0” LU (Loudness Unit) is -23dB. If ATSC A/85 is chosen, whose

target is -24dB, then that becomes the corresponding equivalent of the relative LU of 0.


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT

When using the absolute scale, the Loudness meter displays the increments to reflect the chosen

measure type. In absolute scale the EBU R128 meter will display -23 instead of the relative scale’s 0.

The option in the Loudness panel reveals the various measure

types as well as the option for absolute scale.

Using the Loudness Meters

When using the Loudness meters to do a structured analysis of your mix to determine QC adherence,

a group of controls let you determine when analysis begins and ends.

Lock Metering to Transport: This setting is found in the compound meter option menu.

When enabled, all loudness metering analysis is automatically reset whenever you move

the playhead to another location in the Timeline. This is useful when you’re spot-checking

different parts of your mix, or working on a particular scene. Uncheck this option if you want

the measurement of playback to that point in the Timeline to remain.

Absolute Scale: An absolute measure of the selected scale type.

Pause and Reset buttons: When you’re doing a formal analysis of your mix, the Reset button

lets you reset all currently accumulated analyses, and the Start button initiates loudness value

accumulation. If you need to stop playback briefly to do something else, you can click Pause,

and then click Resume when you’re ready to continue the analysis.