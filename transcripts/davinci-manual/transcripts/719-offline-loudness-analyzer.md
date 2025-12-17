---
title: "Offline Loudness Analyzer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 719
---

# Offline Loudness Analyzer

Users also have the ability to analyze an audio file’s loudness offline. This is a fast way to measure

loudness in imported audio files or bounced mixes.

To initiate offline loudness analysis:

�Right-click the file in the Timeline, and choose Analyze Audio Level from the contextual menu.

A dialog box displays the available options for measurement.

All of the measurements available in the real-time loudness meter are accessible in the dropdown

menu inside the Analyze Audio Level panel. When the analyzer mode is chosen, the target

measurements for that mode will display next to the reading in parenthesis. Once you have

clicked the analyze button, the results will display in the panel next to the chosen mode’s target

measurement values.


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT

Select the audio file, choose the desired analyzer

mode, in this case EBU R128, and click analyze.

Visualizing Loudness Monitoring

When you show the track of a Main bus in the Timeline, as long as the track is high enough (ahem, tall

enough), you can show or hide a series of “Loudness History” curves to visualize the loudness analysis

of the mix on that bus over the duration of the mix.

The available curves are:

�Integrated: A thick curve shows the averaged “integrated” loudness analysis of the current mix,

which is a measurement that’s taken from the beginning to the end of playback. This graph is the

primary gauge of whether or not measured loudness is acceptable. The color of each segment

of this curve indicates whether that part of the mix is “to spec.” Blue indicate loudness levels that

are below tolerance, yellow indicates loudness values that are within tolerance, and red indicates

loudness values that are above tolerance. By evaluating the colors of the curve, you can easily

spot which parts of your mix might need adjustment to meet the necessary specification.

�Momentary: A measurement of the loudness measured in the past 400ms, shown by a thin green-

blue curve, which provides an analysis of transient level changes.

�Short Term: A measurement of the loudness of the past 3 seconds, shown by a thin blue line,

which provides a more averaged analysis than the Momentary curve, yet still indicates the

dynamics of the mix.

To show the loudness history for Main 1:


Open the Automation controls by clicking the automation button on the Fairlight toolbar.


Open the Index, and click the eye button for the Main you want to see in the Timeline. Loudness

History appears as an option in the track header controls as long as the track is tall enough to

show the controls. These controls will be hidden on short tracks.


Turn on the Loudness History toggle, and check the curves you want to see. The Integrated,

Momentary, and Short Term loudness analyses can be individually displayed or hidden, to expose

overlapping graphs in that track in which you can see your program’s loudness over time.

Viewing the loudness graph of the mix going out of a Main

NOTE: Currently, loudness history is only supported for Main 1.


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT

Metering Options

DaVinci Resolve has a variety of metering options that allow you to tailor metering to your workflow.

The settings appear in Project Preferences > Fairlight on the Audio Metering pane, but they affect

mixer, Fairlight effects, or master metering on the Cut and Edit pages.

Level Metering Options

You can chose the response characteristic of the level meters for channel strips and Fairlight FX.

The Meter Type dropdown allows you to choose between IEC 60268-18, Digital VU, and Custom

response characteristics. Both meter types have separate “hold and fall” metering, allowing you to see

the highest peak that is reached.

IEC 60268-18: A digital PPM-type meter with reference standard of -18 dBFS, a fast response

to peaks, and a slower release characteristic. This is the default in DaVinci Resolve and is

used in all Blackmagic Design software and hardware products.

Digital VU: A dual-value meter, showing the peak level as a single segment with fast ballistics,

and the RMS (volume unit) as a bar graph. It has a far faster quasi linear decay characteristic,

making it easy to monitor average levels while allowing sounds with quick transients and

decays to be more easily tracked. This option can be best for audio editing and mixing.

Custom: Allows each aspect of the meter response to be chosen, including level detector,

scale, peak, deck and peak indication.

Pre-fader Metering

By default, “Pre fader metering on tracks” is unchecked (disabled), setting the metering on channel

strips to be post (after) the fader level and mute button. For example, if the source audio file has peaks

that are hitting -2 dBFS, and the channel fader is lowered from 0 to -10, then the peaks that show on

the meter will now be at -12.

When pre-fader metering is on, the metering point is set to be before the fader, and is not affected by

the fader’s position. However, the meter is affected by clip gain settings or key framing as these level

changes occur before the clip’s signal enters the mixer’s signal path.

With pre-fader metering, you could lower the fader to be fully off (minus infinity) and the meter will still

read the level of the source signal. This allows you to always be aware of the source signal and what it

is doing before being altered by mixer’s controls or processing.

Many video editors prefer to work with post-fader metering, but most audio mixers prefer to work with

pre fader in order to be aware of what the actual source level is at any time.


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT

Solo and Pre-fader Metering

When pre-fader metering is enabled, soloing one or more tracks will show a lighter “ghost” version of

meter activity on non-soloed tracks, allowing you to always see audio levels on tracks that are muted

by the soloing process. This makes it easy to focus on tracks that are actually audible while still seeing

activity on those that are not.

If pre-fader metering is off (the default), when one or more tracks are soloed, no metering occurs on

tracks unsoloed tracks.

Pre-fader metering with light shaded meters on non-soloed tracks

Target Loudness Level

Allows the target loudness level in LUFS for the master Loudness meters to be set to your desired

output target level. For example, DaVinci Resolve’s default loudness standard target is -23 LUFS,

but the YouTube target LUFS specification is -14 LUFS. If -14 LUFS is set, the “0” mark on the

loudness meter scale moves to this level, allowing you to focus your master mix levels towards that

loudness standard.


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT

Viewer

A small viewer to the right of the Monitoring panel shows the frame of video at the position of the

playhead. This is the same image that’s output to the external broadcast display of your workstation if

you have one connected.

The Viewer lets you see the picture you’re mixing to.

Clicking the Expand Viewer button at the bottom right-hand corner lets you open the Viewer into

a floating window, which you can then position anywhere you want.

To close the floating Viewer, click the Dock Viewer button at the upper right-hand corner of the

floating viewer window.

Click the button at the upper right-hand corner to dock the Viewer again.

Cinema Viewer on Fairlight Page

Sometimes when you need to verify lip sync, sound effects sync, or simply review a new section of

a mix you’ve been working on, it helps to watch the visuals of the program full screen as you listen

to your mix. You can now set the Fairlight page Viewer to Cinema Mode by choosing Workspace >

Viewer Mode > Cinema Mode (Command-F).


Fairlight | Chapter 182 Audio Meters and Audio Monitoring

FAIRLIGHT