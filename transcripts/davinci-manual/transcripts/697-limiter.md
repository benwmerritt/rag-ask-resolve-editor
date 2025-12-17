---
title: "Limiter"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 697
---

# Limiter

The third set of dynamics parameters let you apply limiting, which imposes a targeted maximum level

allowed for a signal. Limiting is similar to compression but essentially has a very high ratio.

�Limiter: Enables the Limiter.

Threshold: Sets the threshold above which limiting will occur. As the Limiter is designed to hard

limit the output, this also essentially sets maximum allowable output level. The default is –21 dB.

The range is from –50 to 0 dB. It’s best to set the amount of limiting by listening, and looking at the

amount of gain reduction in the meter. Too much limiting can “squash the life out of the sound” as

all of the internal dynamics of a mix can be lost. Used properly, you can smooth out the final mix

and achieve higher average level. You can also watch the yellow animated balls in the display to

see how the real time limiting response is affected by the controls.

Attack: Adjusts the attack rate time constant of the sidechain detector. The default is 0.71 ms. The

range is 0 to 100 ms.

Hold: Once the input level falls below the threshold, Hold keeps limiting active until the hold time

has elapsed, when release time will start. Default is 0 ms. The range is from 0 to 4000 ms.

Release: Adjusts how quickly the sidechain detector stops applying limiting when the signal falls

below the threshold. The default is 90 ms. The range is 50 to 4000 ms.

NOTE: When limiting is applied to the final output of your channel (or to an entire mix), you

often will need to use the Makeup Gain slider to maximize the output level (if a master) or to

match the original level of an individual track (unity). You can audition the difference in level

by bypassing the Dynamics module overall, or the Limiter only.

EQ

Each Mixer channel strip has a 6-band equalizer EQ, with a mini-EQ graph that displays the current

EQ curve, bypasses the plugin, and opens it when double-clicked.

This plugin offers a choice of high and low shelving, parametric or notch response curves, and

high and low pass filters with selectable slopes up to 24dB/octave, with controls for boosting and

attenuating different frequency ranges.

Each band has controls for the filter type (Bell, Lo-Shelf, Hi-Shelf, Notch), Frequency, Gain, and Q-factor

(sharpness of the band), with the available controls for each band of EQ changing depending on the

filter type.

You also have a choice of four response curves, from the Native Fairlight response curve to emulations

of classic EQs.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

The channel strip EQ window

The channel strip’s EQ Indicator.

(Left) EQ is adjusted, and (Right) EQ is flat (no EQ).

Master EQ Controls

The Equalizer window has the following overall controls:

�Enable button: Turns the plugin on and off.

�Reset button: The circular Reset icon on the upper right of the EQ resets all parameters to their

default settings and values.

�Equalizer Type: This dropdown offers the Native Fairlight response curve and three emulations of

classic mixing console EQs.

Earth: Native Fairlight response (Default)

Air: SSL 4K

Ice: Neve V

Fire: Focusrite

�Preset Menu: Your EQ settings can be saved as presets by clicking the Plus button to the left of

the Preset menu.

�Gain fader: This post-EQ fader lets you boost or attenuate the processed signal to compensate for

your EQ adjustments.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

The EQ Graph

The EQ graph provides a visual representation of the current EQ settings, with numbered “handles” for

each active EQ band, which can be dragged in any direction to change the corresponding frequency

and level. You can also use your mouse wheel to adjust the Q (bandwidth) of each band.

The EQ graph

Dragging the numbered handles on this graph in turn modifies the parameters of the corresponding

band, and conversely, changing each band’s parameters will also alter the EQ graph, which serves the

additional purpose of providing a graphical representation of the equalization curve being applied to

that track. If you have a mouse wheel, it can be used to control Q.

Bands 1 and 6

The outer two sets of band parameters are for processing the lowest or highest frequencies of an

audio signal.

Band 1 controls active

Band 6 controls active

�Band filter type: Clicking the Band 1 or Band 6 buttons activates or deactivates their

respective controls.

�Band filter type: Bands 1 and 6 are switched off by default, but when active, they each

allow access to filtering options below:

Band 1: Low Shelf, Bell, High Shelf, and High Pass.

Band 6: Low Pass, Low Shelf, Bell, and High Shelf.

�Frequency: Adjusts the center frequency of the EQ band.

�Filter Slope: The high and low pass filters offer selectable slopes starting at 6dB/octave

up to 24dB/octave.

�Gain: When bands 1 and 6 are set to a bell or shelving response curve, this parameter cuts or

boosts the selected frequency with a range of ±20 dB.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Bands 2 – 5

The middle four sets of band controls let you make a wide variety of equalization adjustments.

They’re on by default to make it easy to begin making adjustments.

The Band 3 controls

�Band enable button: Clicking these Band buttons activates or deactivates

their respective controls.

�Band filter type: Bands 2 to 5 offer the following filtering options: Low Shelf, Peaking,

Notch, and High Shelf.

�Frequency: Adjusts the center frequency of the EQ adjustment.

�L, ML, MH, H Buttons: These buttons restrict the center frequency of a band to one of the

following frequency ranges: Low, Medium Low, Medium High, or High.

�Gain: This control is available when a band is set to a bell or shelving response curve and adjusts

the level of the center frequency within a range of ±20 dB.

�Q Factor: This parameter is available when a band is set to a bell response or when the Equalizer

type is set to Fire and adjusts the bandwidth of an EQ band, with a range of .3 to 10.3.

Smaller Q factors widen the bandwidth, while higher values make it narrower, determining how

much neighboring frequencies are also affected as the center frequency is adjusted.

Bus Sends

Bus Sends let you route a channel strip’s source signals to a bus destination, with control over level,

pan, mute, and pre/post fader routing. You can create bus sends on channels that go to any bus

destination you’ve created.

Some common mixing tasks that sends can be useful for:

�Submixing: For example, to render separate mixed outputs that are different formats, such as

stereo, 5.1 surround, or Dolby Atmos, all at the same time.

�Feeding signals to a shared effect: For example, route to a reverb plugin, where post fader sends

on various mixer channels feed a reverb placed on a bus channel strip by varying amounts.

�Headphone cue mixes: Create separate pre-fader mixes for the talent so you don’t disturb what

you’re listening to on your main monitor speakers.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Creating Sends

To create a Bus Send and access its controls:

�Click on the assign button with the plus sign (+) in the Bus Sends area of the Mixer.

�A dropdown menu appears with a list of busses; select one to assign.

�Your send is now created.

You can hover over the rectangular name button and access a disable/bypass button, an

access icon to show the Bus Send window for the channel, and an “x” to delete the send.

A tooltip appears showing the send bus name.

Hovering over the

rectangular name

button will show

send controls.

Accessing the Bus Sends Window

You can access the Bus Sends window to control a channel’s sends by clicking in the center of the

name button.

Bus Send window controls

Each Bus Send you create exposes the following controls in the Bus Send window:

�On: Turns the send on or off.

�Pre: Switches the send to use pre- or post-fader routing. Enabling this button allows that track to

send levels to the destination bus before level adjustments on that track are applied.

�Send Level: Adjusts the amount of signal sent from the selected feed to the send bus.

The range is OFF to +10dB.

�Pan: Provides panning across Bus Send destinations.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Uses for Pre-fader Routing

One common use of pre-fader sends is for cue mixes to ADR or voice over talent, where the

artist wants to hear a completely different mix than the control room mix. Using pre-fader

sends and setting up a complete mix to a bus that feeds the headphone system allows a mix

that is completely independent.

Pre-fader sends can also be used for special creative effects that might involve a dialogue

channel being sent to a reverb plugin via a send. If the send is routed pre-fader, when the

main channel fader is lowered to close to zero, the dialogue is still being fed to the reverb,

so the dialogue will sound extremely reverberant (almost all of the signal is “wet”). Gradually

raising the channel fader will make it sound like the voice is moving closer to the listener,

changing the reverb balance and sounding more present.

Bus send levels are shown in the rectangles for each send and have the color codes assigned

to the destination busses.

Bus Send

levels shown

on the Mixer

channel strip