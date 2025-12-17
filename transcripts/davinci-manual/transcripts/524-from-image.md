---
title: "From Image"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 524
---

# From Image

The From Image modifier only works on gradients, like the gradient on a Background node. It takes

samples of an image along a user-definable line and creates a gradient from those samples.

Unlike other modifiers, From Image is not located in the Modify With menu. This modifier can be

applied by right-clicking a Gradient bar in the Inspector and selecting From Image.

Inspector

From Image modifier


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Controls Tab

The From Image controls tab in the Inspector is used to select the node that contains the image you

want to sample. It allows you to define the starting and ending point in the image as well as how many

color samples to use in creating the gradient.

Image to Scan

Drop into this box the node from the Node Editor that you want to be color sampled.

Start X/Y, End X/Y

These two point controls define the Start and End points of the line along which the samples are taken

from the image defined in the Image to Scan box.

The points can also be moved directly in the viewer.

Number of Sample Steps

This defines how many individual color samples are taken along the line. You can also see the result

of this setting when you look at the actual node’s Gradient control. The more sample steps you define

here, the more individual color stops appear on the Gradient control. It is also possible to first create a

gradient using the From Image modifier and then remove that modifier from the Gradient control again.

The created gradient stays intact and can then be fine tuned by hand.

Edges

Edges determines how the edges of the image are treated when the sample line extends over the

actual frame of the image to be sampled.

Black

This outputs black for every point on the sample line outside of the image bounds.

Wrap

This wraps the edges of the line around the borders of the image.

Duplicate

This causes the edges of the image to be duplicated as best as possible, continuing the image beyond

its original size.

Color

This outputs a user-definable color instead of black for every point on the sample line outside of the

image bounds.

Example

The source image on the left shows the color selection line in red. The image on the right

shows the resulting gradient from that selection.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Gradient Color

The Gradient Color modifier allows you to create a customized gradient and map it into a specific time

range to control a value. Use the Start and End time controls to set the frames for the animation. If the

Start and End time values are set to 0, then the modifier returns the value at the starting point of the

gradient. You can use the Offset control to animate the gradient manually.

It can be applied by right-clicking a parameter and selecting Modify With > Gradient Color.

Inspector

The Gradient modifier Controls tab

Controls Tab

The Controls tab consists of a Gradient bar where you add and adjust points of the gradient. Start

Time and End Time thumbwheels at the bottom of the Inspector determine the time range the gradient

is mapped into.

Gradient

The Gradient control consists of a bar where it is possible to add, modify, and remove points of the

gradient. Each point has its color. It is possible to animate the color as well as the position of the point.

Furthermore, a From Image modifier can be applied to the gradient to evaluate it from an image.

Gradient Interpolation Method

The gradient is linearly interpolated from point to point in RGB color space by default. This can

sometimes result in unwanted colors. Choosing another color space may provide a better result.

Repeat

Defines how the left and right borders of the gradient are treated.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Gradients set to Once, Repeat, and Ping Pong from top to

bottom, respectiµvely, and shifting the gradient to the left.

•	 Once: When using the Gradient Offset control to shift the gradient, the border colors keep

their values. Shifting the default gradient to the left results in a white border on the left;

shifting it to the right results in a black border on the right.

•	 Repeat: When using the Gradient Offset control to shift the gradient, the border colors are

wrapped around. Shifting the default gradient to the left results in a sharp jump from white to

black; shifting it to the right results in a sharp jump from black to white.

•	 Ping Pong: When using the Gradient Offset control to shift the gradient, the border colors

ping-pong back and forth. Shifting the default gradient to the left results in the edge

fading from white back to black; shifting it to the right results in the edge fading from black

back to white.

Gradient Offset

Allows you to pan through the gradient.

Time Controls

The Start Time and End Time thumbwheels determine the time range the gradient is mapped into. This

is set in frames. The same effect can be achieved by setting the Gradient to Once and animating the

offset thumbwheel.

Key Stretcher Modifier

The Keyframe Stretcher modifier is primarily used when creating title templates in Fusion for use in

DaVinci Resolve’s Edit page or Cut page. The Keyframe Stretcher modifier is added to an animated

parameter, so the keyframes in the animated parameter stretch when the template is trimmed in the

Timeline. It can be applied by right-clicking a parameter and selecting Modify with > KeyStretcher.

For more information on the Keyframe Stretcher Modifier controls, see the "Keyframe

Stretcher", see Chapter 111, "Miscellaneous Nodes," in the DaVinci Resolve Reference Manual

or Chapter 51 in the Fusion Reference Manual.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

MIDI Extractor

The MIDI Extractor modifier provides the ability to modify the value of a control using the values

stored in a MIDI file. This modifier relies on some knowledge of MIDI, which is beyond the scope of

this manual.

The value produced by the modifier is extracted from the MIDI event selected in the Mode menu. Each

mode can be trimmed so that only specific messages for that event are processed—for example, only

some notes are processed, while others are ignored. The value of the event can be further scaled or

modified by additional factors, such as Scale, Velocity, Attack, and Decay.

It can be applied by right-clicking a parameter and selecting Modify With > MIDI Extractor.

Inspector

The MIDI Extractor modifier Controls tab

Controls Tab

The Controls tab is used to load the MIDI file, modify its timing, and determine which MIDI messages

and events trigger changes in the Fusion parameter.

MIDI File

This browser control is used to specify the MIDI file that is used as the input for the modifier.

Time Scale

Time Scale is used to specify the relationship between time as the MIDI file defines it and time as Fusion

defines it. A value of 1.0 plays the MIDI events at normal speed, 2.0 plays at double speed, and so on.

Time Offset

Time Offset adjusts the sync between the MIDI file’s timing and Fusion’s timing. If there is an

unexpected delay, or if the MIDI file should start partway into or before some animation in Fusion, this

control can be used to offset the MIDI data as required.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Result Offset, Result Scale

These sliders adjust the range of values produced by the modifier. By default, values between 0

and 1 (or -1 and 1 for PitchBend mode) are generated. This does not always suit the node/parameter,

and scale can be used to make this range larger (such as * 0.0 - 2.0). Offset is used to provide some

constant value as a base.

Result Curve

The Result Curve can also be used to adjust the output. However, this adjusts the curve of the result.

By default, for any input MIDI data, the results fall linearly between 0.1 and 1.0 (for example, a velocity

127 note generates 1.0, whereas 63 generates approximately 0.5).

The Result Curve applies a gamma-like curve so that middle values can produce higher or lower

results while still maintaining the full scale.

Mode

This menu provides Beat, Note, Control Change, Poly AfterTouch, Channel AfterTouch, or Pitch Bend,

indicating from which MIDI event the values are being read. Beat mode is slightly different in that it

produces regular pulses based on the tempo of the MIDI file (including any tempo maps).

The Beat mode does not use any specific messages; it bases its event timing on the tempo map

contained in the MIDI file.

Combine Events

This menu selects what happens when multiple events occur at the same time. In Notes mode, this

can happen easily. For other events, this can happen if Multiple Channels are selected.

Use this to take the result from the most recent event to occur, the oldest event still happening, the

highest or lowest valued event, the average, sum, or the median of all events currently occurring.

Beat (Quarters) (Beat Mode Only)

This defines how often a beat occurs when in Beat mode. This is in quarter notes, so a value of 1.0

gives a beat every quarter.

Note Range (Note and Poly Aftertouch Modes Only)

This defines what range of notes causes a value to be generated. For example, use this to pick out the

kick drum from a GM drum track by setting the note range between 35–36.

Pitch Scale (Note Mode Only)

Pitch Scale defines how much the result changes with pitch. A value of 1.0 causes the result to vary

from 0.0 to 1.0 over the entire range.

Velocity Scale (Note Mode Only)

This defines how much the result changes with velocity. A value of 1.0 causes the result to vary from

0.0 to 1.0 over the entire range. This is added to the result from Pitch Scale for the final result.

Control Number (Control Change Mode Only)

This specifies the MIDI controller number from which to extract events.

Envelope Controls (Note and Beat Modes Only)

These define an Envelope to follow for values before, during, and after the note or beat. Pre-Attack

Time defines how long before the event it starts ramping up to the pre-attack level. Attack is the Time/

Level to ramp to once the event has occurred, followed by the Decay ramp and Sustain, until the

event stops. This stage is for Notes only. Beats have an instantaneous duration, so it goes straight to


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Release. Release is the ramp-down time after the event finishes. When trying to do a Beat, set Release

to some value, or there likely will not be much of a beat.

These values can be used to follow actual sounds in the MIDI sequence or just to create interesting

effects. All time values used in the MIDI Extractor are in seconds.

The MIDI Extractor modifier Channels tab

Channels Tab

The Channels tab is used to select the Channels used in the modifier.

Channels

Channels checkboxes select which of the 16 channels in the MIDI file are actually considered for

events. This is a good way to single out a specific instrument from an arrangement.

About MIDI

A single MIDI interface allows 16 channels. Typically, these are assigned to different

instruments within a device or different devices. Usually, MIDI data is 7 bits, ranging from

0–127. In Fusion, this is represented as a value between 0–1 to be more consistent with how

data is handled in Fusion.

There are numerous different MIDI messages and events, but the ones that are particularly

useful with this modifier are detailed below.

MIDI Messages

Note On: This indicates that a note (on a specific channel) is being turned on, has a pitch

(0–127, with middle C being 60) and a Velocity (0–127, representing how fast the key or strings

or whatever was hit).

Note Off: This indicates that a note (on a specific channel) is being turned off, has a pitch

(0–127, with middle C being 60) and a Velocity (0–127, representing how fast the key or strings

or whatever was released).

Control Change: This message indicates that some controller has changed. There are 128

controllers (0–127), each of which has data from 0–127. Controllers are used to set parameters

such as Volume, Pan, amount of Reverb or Chorus, and generic things like foot controllers or

breath controllers.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

MIDI Events

Channel Aftertouch: This event defines that pressure is being applied to the keys (or strings

or whatever) during a note. This represents general, overall pressure for this channel, so it

simply uses a pressure value (0–127).

Poly Aftertouch: This event defines that pressure is being applied to the keys (or strings or

whatever) during a note. It is specific to each particular note and therefore contains a note

number as well as a pressure value (0–127).

Pitch Bend

The Pitch Bend controller generally specifies the degree of pitch bending or variation applied

to the note. Because pitch bend values are transmitted as a 14-bit values, this control has a

range between -1 and 1 and a correspondingly finer degree of resolution.