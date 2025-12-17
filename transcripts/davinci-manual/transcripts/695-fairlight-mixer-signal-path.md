---
title: "Fairlight Mixer Signal Path"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 695
---

# Fairlight Mixer Signal Path

The signal path or layout (“topology”) of a mixer describes how the audio signals are routed from one

place to another.

The default signal flow on the Fairlight channel strip is as follows:


Audio source: Input menu allows choice of source, including file playback, bus, live input, etc.


Path Settings: Accessible from the Input menu. Allows adjustments to the input signal.


Track FX: Built-in effects, Voice Isolation (Studio only), and Dialogue Leveler. Disabled by default.


Effect: Fairlight FX, AU, or VST effects.


Dynamics: Dedicated channel dynamics processor with expander/gate, compressor, and limiter.


EQ: Dedicated 6 band EQ with variable gain, frequency, and Q.


Output Routing: Panning and bussing.

The main fader for the channel strip then controls the level to any assigned main output busses.

Bus Send faders control the level to any destination set for a mixer channel send and can be set

pre‑or post-fader.

What Is An Effects Insert?

Each time you add an effect to a channel, a signal processing “insert” (insertion point) is enabled.

The source signal flows from the input of the effect to its output, and then onwards to any additional

insert(s) to the next stop in the Mixer’s signal flow.

DaVinci Resolve supports a total of six inserts per channel in addition to the built in Dynamics and

EQ processing.

Click on the Input area to access the Input dropdown menu, letting you patch inputs, patch

busses, and configure the input settings of audio signals routed through Blackmagic or other

hardware audio interfaces.

“Pre” vs. “Post”

The term pre refers to a signal that is routed for use before another connection point. For

example, you may prefer to work with pre-fader metering as you can always see the original

signal level coming off of disk reflected in the meter level.

A signal that is post occurs after a connection point. For example, you generally want effect

sends that go to a reverb effect to follow the level of a track’s main fader so that the reverb

level follows the overall level. As a result, Bus Sends are set to have post fader routing

by default.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Input

For more information on using the options of the Input menu, see Chapter 171, “Setting Up

Tracks, Busses, and Patching.”

The Input dropdown menu allows you to

initiate patching any available sources

using the Patch Input/Output window.

Path Settings

Choose Input at the top of the Mixer channel strip to access the Path Settings control window. These

controls allow you to modify various aspects of the Mixer channel strip that may need adjustment prior

to, or post, recording to control the mic/line inputs on Fairlight audio interface hardware, and more.

Path Settings window

Mic/Inst

Controls will only appear on this panel if you have connected channels 1 or 2 of a Fairlight SX36 audio

interface to your system. If connected, you can remotely control all of the options (including level) for

the mic/instrument inputs of the SX36 if they are assigned to the channel. If there is no connection to

an SX36, the area is empty.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Record Level

�Record: Linked and identical to the Record Enable button on the channel strip; here for

convenience. If you hit one, it will enable the other.

�Thru: Allows the input signal to pass into the Mixer without enabling a record path. This is ideal

when you want a source signal to always be available and just want to monitor it.

�Record Level: Allows you to apply a digital gain adjustment to the record path to disk, post the

output of your audio interface’s analog-to-digital converter.

Normally, this control should be left at 0.0 (no change, unity gain), as it affects the level you are

recording to disk. It is best practice to use the level controls on your audio interface to control the

input level into DaVinci Resolve in order to maximize audio fidelity. However, there might be a time

where you need a bit more level, or may not have access to an audio interface’s controls, and in

those cases you can adjust the input.

Trim

�Polarity: Inverts the polarity of the signal coming into the channel strip (sometimes referred to

as “flipping the phase”). For example, you may have an input signal like an explosion where the

transient attack of the signal produces with a massively positive-going waveform (where the

waveform mostly appears above the zero line). If you invert the polarity, the signal will now be

mainly negative-going and the waveform will be concentrated beneath the zero line. Inverting

polarity is sometimes used to more closely align signals from multiple microphones and can be

used creatively to affect frequency response of such a signal.

�Trim Level: Allows you to trim the level of the signal coming off of disk, post the Track FX (which

process directly off of disk) and pre all other effects. Trim Level appears post the recorded signal

to disk and doesn’t affect the recording level. Trim is a playback adjustment and allows you to

adjust the level of the signal coming into your mix to optimize the level feeding effects and the

busses, or to slightly trim an otherwise perfect element in the mix up or down in level.

Direct Output

Each audio channel strip can enable a direct output that can be used to feed any other input

destination. You can patch this source using the Track Direct choice in the Patch Input/Output dialog

via the Source dropdown.

For more information see Chapter 171, “Setting Up Tracks, Busses, and Patching.”

�On/Off: Enables/disables the direct output.

�Pre: Sets the direct output tap-off point to be pre (before) the channel fader. On by default.

�Level Control: Sets the level from full off (minus infinity) to +10 dB. Default is 0.0 (unity gain).

Insert

Linked and identical to the Effects In button on the channel strip; here for convenience. If you hit one,

it will enable the other. Switches all Fairlight FX, AU, or VST effects on a channel in or out of the signal

path with a single switched control.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Effects

Fairlight FX, VST, or Audio Unit effects can be applied on the Mixer’s channel strips. Effects are

applied on the entire track, not just on one or more clips in the Timeline for that track.

Clicking the plus (“+”) button opens a dropdown menu, allowing you to apply any Fairlight FX, VST, or

AU effects installed on your machine to that track. The menu is organized by processing type. Within

each type, there is a hierarchical choice for Fairlight FX, AU, and VST (if you’re on a Mac) or Fairlight FX

and VST (if you’re on Windows).

NOTE: Depending on what you have installed on your machine, the collection of audio

effects available for the Mixer channel strip inserts is often close to (or identical to) those that

you can access for clip-based audio processing found in the Effects panel on the left side of

Cut, Edit, and Fairlight pages.

Clicking on the plus sigµn shows the

Effects dropdown list for assignment

TIP: You can store favorite effects for quick access at the top of the list by marking them as

favorites in the Effects panel. Mark a favorite by clicking on the star next to the name.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Hovering the mouse over any listed effect reveals controls for enabling/disabling, replacing or deleting

the effect, or opening an effect’s custom controls (the user interface for that effect).

Hovering the mouse

pointer over an effect

insert reveals controls

for that effect.

Changing the Order of Effects on a Channel

The order of effects on any Mixer channel strip can be changed by clicking on the Effects Order

button. A dropdown menu appears allowing you to change the order between various routing

combinations of all insert effects (Fairlight FX, or AU, or VST plugins) and the built-in Dynamics and EQ

modules. The default routing is Effects (“FX”), Dynamics, EQ.

Effects Order

dropdown menu

Different effects orders can produce very different creative results. For example, it is usually best

practice to apply noise reduction first in a signal chain, so you’re not affecting the volume or quality of

the noise floor you’re trying to remove, so the plugin can do its job most effectively. Or you may wish

to apply dynamics processing prior to EQ, as changing the spectral content of your source may affect

the response of the compressor.

Moving Inserts by Dragging

You can move inserts from one location to another simply by clicking and dragging to a new location.

Using this technique, you can move an effect from one channel to another, or swap or move the location

of an effect on a channel to another insert position on that channel (displacing the plugin already

present). Note that, at this time, you can’t use this technique to copy tracks to busses or vice versa.

Copying and Pasting Effects

You can copy entire effect chains with their specific effect parameters intact, track by track. Let’s say

that you’ve created a plugin chain on a dialogue track that has Noise Reduction, a De-Hummer, and a

Dynamics plugin that you have tweaked to the exact settings needed for those dialogue recordings to

sound great.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

You also have another track that has similar recordings that could benefit from the exact same chain of

plugins and those particular settings. Rather than install each plugin to the track and redo the settings,

you can simply right-click the track header (A1 for example) and click Copy. Then go to the track

header of the new track you want effected, right-click, and click Paste. You will now have the identical

plugin chain copied over to the new track, all with each of the settings exactly as you had created on

the source plugin dialogue track