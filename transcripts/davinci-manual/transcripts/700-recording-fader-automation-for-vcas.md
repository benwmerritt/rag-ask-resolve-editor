---
title: "Recording Fader Automation for VCAs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 700
---

# Recording Fader Automation for VCAs

You can record automation data to a VCA fader, and all faders in that VCA group will follow even

though they’re not actually automated themselves. This makes it easy to record complex automation

involving multiple faders when you still might want the freedom to finely adjust each individual

fader later on.

Nesting VCAs

VCAs can also be “nested,” where one or more VCAs can be controlled by yet another VCA.

To nest a VCA, simply assign the VCAs you want have controlled to yet another “master” VCA.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Arm, Solo, and Mute Buttons

These controls are identical to the controls found on the track header of each timeline audio track.

�Record Arm: Enables a track for recording when the Record button on the transport is engaged

(highlights red when enabled).

�Solo: Lets you mute all other tracks in order to play a track you need to focus on in isolation

(highlights green when enabled).

If Solo is enabled for multiple tracks, all soloed tracks will play, and all non-soloed tracks

will be muted.

Solo status affects rendering, so if one or more tracks are soloed, the muted tracks won’t be

output or rendered.

�Solo Safe: Command-Shift-click a Solo button to put it into Solo Safe mode

(highlights blue when enabled).

Channel strips set to Solo Safe always play even if Solo is enabled for other tracks.

Solo Safe can be useful for effect returns busses with effects like reverb where you may want to

hear the reverb when tracks feeding it are soloed.

�Exclusive Solo: When active, clicking the Solo button on a track takes other soloed tracks out

of Solo mode. This means only one track can be soloed and heard at any given time, which

is useful if you want to compare audio sources, to hear sonic differences when comparing

levels or processing.

NOTE: Soloing a track in Exclusive Solo mode will not affect a track that is in Solo Safe

mode. If you want to include that track, you need to manually deactivate the Safe Solo

button first.

Disabled by default, Exclusive Solo can be enabled by selecting it in the Fairlight menu. You can

also map a key command to this function in the Keyboard Customization dialog.

For more information on Keyboard Customization, see Chapter 4, “System and User

Preferences.”.

�Mute: Turning on Mute disables audio playback from that track (highlights orange when enabled).

This affects rendering, so if one or more tracks are muted, they won’t be output or rendered.

The channel strip’s Record Arm, Solo, and Mute buttons

TIP: You can click a button and drag across multiple channel strips to turn that button on

or off for multiple tracks easily.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Fader Controls

Each track’s vertical fader lets you control the level that’s output by that track, either by using your

mouse, or using a physical fader of your Fairlight console or third party control surface. If you’re

working with a console, then the onscreen faders serve as a visual reference of what levels are set.

dB Indicator: Numerical at the top of the track indicates the volume, in decibels, that track is

currently set to.

Fader: Each track’s vertical fader can be dragged with your mouse or other pointing device

to adjust the volume of that track and perform automation recording. Dragging up increases

volume, dragging down decreases volume. Fader handles turn red while you record level

automation, and they turn green when automation has been recorded for that track.

Methods of adjusting channel faders:

�To change level: Click and drag any fader up or down.

�To reset the level to default level of 0 dB: Double-click a fader’s handle. This does not work after

you’ve recorded automation for a track, unless you erase the automation first.

A Fader in

the Fairlight Mixer


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Metering Options

DaVinci Resolve has a variety of metering options that allow you to tailor metering to your workflow.

The settings appear in Project Preferences > Fairlight in the Audio Metering section, but they affect

mixer, Fairlight effects, or master metering on the Cut and Edit pages.

Level Metering Options

You can choose the response characteristic of the level meters for channel strips and Fairlight FX.

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

scale, peak, deck, and peak indication.

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

pre-fader in order to be aware of what the actual source level is at any time.

Solo and Pre-fader Metering

When pre-fader metering is enabled, soloing one or more tracks will show a lighter “ghost” version of

meter activity on non-soloed tracks, allowing you to always see audio levels on tracks that are muted

by the soloing process. This makes it easy to focus on tracks that are actually audible while still seeing

activity on those that are not.

If pre-fader metering is off (the default), when one or more tracks are soloed, no metering occurs on

tracks unsoloed tracks.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Pre-fader metering with light shaded

meters on non-soloed tracks

Target Loudness Level

Allows the target loudness level in LUFS for the master Loudness meters to be set to your desired

output target level. For example, DaVinci Resolve’s default loudness standard target is -23 LUFS,

but the YouTube target LUFS specification is -14 LUFS. If -14 LUFS is set, the “0” mark on the

loudness meter scale moves to this level, allowing you to focus your master mix levels towards that

loudness standard.

Bouncing Audio

Bouncing audio refers to mixing and rendering audio from one or more Timeline tracks onto another

track of the Timeline, in the process “baking in” processor intensive effects and complicated

or intricate audio edits to create a new continuous piece of audio media. The bounced file is

written to the directory location specified by the Project Settings > Capture and Playback panel >

“Save clips to” field.

There are two commands available for bouncing audio on the Fairlight page:

�Timeline > Audio > Bounce Selected Tracks in Place

�Timeline > Audio > Bounce Mix to Track

To use Bounce Selected Tracks to New Layer:


Set In and Out points to define the range of the Timeline you want to bounce. If you don’t do this,

nothing will happen.


Command-click the track headers or mixer channel strips of all tracks you want to bounce in order

to select them.


Choose Timeline > Audio > Bounce Selected Tracks to New Layer.

The audio on each track is processed and rendered and appears as the top layer of audio on that

track. While View > Show Audio Track Layers is turned off, it will appear as if the new bounced

audio is the only clip on that track. However, the original audio (with any unrendered clip-based

effects) is still available as the bottom of the stack of layered audio on that track; turning on View >

Show Audio Track Layers will reveal this.

The bounced audio is a new audio media file that’s written to the directory location specified by

the Project Settings > Capture and Playback panel > “Save clips to” field.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

To use Bounce Mix to Track:


Choose Timeline > Bounce Mix to Track. The Bounce Mix to Track window appears, showing all

busses that are currently available.


In the Destination Track column, set which mixes you want to bounce by choosing either

New Track, or choosing a specific existing track from the dropdown menus.


Click OK.

The specified mix is processed, mixed, and bounced to the specified track as a new piece of

audio. This creates new audio media that’s written to the directory location specified by the

Project Settings > Capture and Playback panel > “Save clips to” field.

TIP: There’s also a Bounce Audio Effects command in the contextual menu of audio clips in

the Timeline that have clip-based audio effects applied to them. For more information,

see Chapter 180, “Audio Effects.”

For more information on exporting clips, ranges, and files, see Chapter 175, “Editing Basics in

the Fairlight Page.”