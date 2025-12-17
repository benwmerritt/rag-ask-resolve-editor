---
title: "Chapter 183"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 720
---

# Chapter 183

Signal Flow Diagrams

The diagrams in this chapter describe the Fairlight audio processing signal flow in

DaVinci Resolve. They’re intended for people who want an in-depth understanding

of how audio is processed.

Contents

Signal Flow Overview��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3992

Audio Processing Path������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3992


Fairlight | Chapter 183 Signal Flow Diagrams

FAIRLIGHT

Signal Flow Overview

The following simplified flow diagram describes Fairlight audio processing overall.

EXT

Number

Bus

Max Format

SOLO


Stereo

MULTI TRACK


Mono

AUX


SUB


MAIN


BUS ASSIGGNMENT – SUB TO MAIN

BUS ASSIGGNMENT – AUX TO MAIN

INSERTS

AND

PLUGINS

AUX SENDS

CHANNEL FADER,

PAN AND MUTE

EQ

DYNAMICS

INTERCHANGEABLE ORDER BETWEEN

EQ, DYNAMICS AND INSERTS

MAINS

SUBS

AUX

SOLO

MAINS

SUBS

AUX

SOLO

EXT

MAINS

SUBS

AUX

SOLO

DIRECT

SOLO

MULTI TRACK

OUTPUT

CONTROL ROOM

STUDIO

METER

MAIN

BUS 1–8

SUB

BUS 1–24

AUX

BUS 1–24

MULTI-TRACK

BUS 1–24

SOLO BUS

BUS

DIRECT

BUS

DIRECT

BUS

BUS

BUS

DIRECT

SOLO

SOLO

OUTPUT

OUTPUT

OUTPUT

OUTPUT

OUTPUT

EXTERNAL INPUTS

TALKBACK INPUTS

SIDE CHAIN INPUT

CHANNEL INPUT

DISK

OUTPUT

OUTPUT

OUTPUT

TO BUSES

Lorem ipsum

CMYK

PMS

DIELINE

11 GATEWAY COURT  |  PORT MELBOURNE  |  VIC  |  3207  |  AUSTRALIA  |  PH: (03) 9682 4770

Filename

Size

Updated

Artist

Colours

DaVinci Resolve Signal Flow Overview

DR_17 Signal Flow Overview.ai

20/04/2021

A3 420mm(W) x 297mm(H)

CMYK

Finished Artist

Tech Writer

Translator

Creative Director

Product Manager

Studio Manager

Retoucher

Marketing Manager

Production Manager

Audio Processing Path

EXT

OSCILLATOR


Number

Bus

Max Format

SOLO


Stereo

MULTI TRACK


Mono

AUX


SUB


MAIN


MAIN BUS 1–8

CONTROL ROOM


BAND

EQ

LIM

METER

INSERTS AND PLUGINS

UP TO 6 PLUGINS

SOLO

TALK

ENABLE

TALK

ENABLE

TALK

ENABLE

Post

A/B

Pre

COMP

SUB BUS 1–24


BAND

EQ

LIM

METER

INSERTS AND PLUGINS

UP TO 6 PLUGINS

BUS ASSIGGNMENT – SUB TO MAIN

BUS ASSIGGNMENT – AUX TO MAIN

Post

A/B

Pre

COMP

AUX BUS 1–24


BAND

EQ

FOLD

DOWN/UP

FORMAT

CHECK

LIM

METER

LOUDNESS

METER

MULTI-TRACK BUS 1–24

METER

METER

SOLO BUS

INSERTS AND PLUGINS

UP TO 6 PLUGINS

Post

A/B

Pre

COMP

INSERTS AND

PLUGINS

AUX SENDS

EQ


BAND

EQ


BAND

FILTER

DYNAMICS

COMP

LIM

GATE

METER

UP TO 6 PLUGINS

INTERCHANGEABLE ORDER BETWEEN

EQ, DYNAMICS AND INSERTS

Post

After (Post)

Fader

VCA GROUP

1-32

AFL/PFL

Pre Fader

Pre

SOLO

SOLO

FIXED

DIM

MUTE

MAINS

SUBS

AUX

SOLO

MAINS

SUBS

AUX

SOLO

EXT

METER

A/B


STUDIO

FOLD

DOWN/UP

FORMAT

CHECK

DIM

MUTE

TO BUSES

PLAYBACK

RECORD

GAIN

RECORD GAIN

FREQUENCY

WHITE NOISE

GAIN

PINK NOISE

OSCILLATOR

DIRECT

WHITE NOISE

PINK NOISE

GAIN

FADER

MUTE

PAN

PAN


Aux Sends may be taken

pre or post fade,

pre or post mute,

and pre or post pan,

in any combination.

EXTERNAL INPUTS

TALKBACK INPUTS

SIDE CHAIN INPUT

CHANNEL INPUT

TO/FROM DISK

BUS

DIRECT

BUS

DIRECT

BUS

DIRECT

BUS

BUS

OUTPUT

OUTPUT

OUTPUT

OUTPUT

OUTPUT

OUTPUT

OUTPUT

OUTPUT

OUTPUT

OUTPUT

OUTPUT

OUTPUT

CMYK

PMS

DIELINE

11 GATEWAY COURT  |  PORT MELBOURNE  |  VIC  |  3207  |  AUSTRALIA  |  PH: (03) 9682 4770

Filename

Size

Updated

Artist

Colours

DaVinci Resolve Audio Processing Path

DR_17 Audio Processing Path.ai

20/04/2021

A3 420mm(W) x 297mm(H)

CMYK

Finished Artist

Tech Writer

Translator

Creative Director

Product Manager

Studio Manager

Retoucher

Marketing Manager

Production Manager


Fairlight | Chapter 183 Signal Flow Diagrams

FAIRLIGHT

Chapter 184

Immersive

Audio Workflows

DaVinci Resolve offers substantial support for object and channel‑based surround

or immersive audio formats.

This chapter describes how to set up and mix with these formats when mixing in the Fairlight page.

Contents

About Immersive Audio Formats���������������������������������������������������������������������������������������������������������������������������������������������� 3994

Dolby Atmos����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3994

Dolby Atmos Speaker Configurations������������������������������������������������������������������������������������������������������������������������������������� 3995

Enabling Dolby Atmos��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3996

The Components of a Dolby Atmos Mix��������������������������������������������������������������������������������������������������������������������������������� 3996

Predetermined Dolby Atmos Master Rules��������������������������������������������������������������������������������������������������������������������������� 3997

Dolby Atmos Integration����������������������������������������������������������������������������������������������������������������������������������������������������������������� 3997

Binaural Audio Monitoring������������������������������������������������������������������������������������������������������������������������������������������������������������� 3998

Binaural Render Options���������������������������������������������������������������������������������������������������������������������������������������������������������������� 3999

Ambisonics������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 4000

Ambisonic Orders������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4001

Ambisonic File Support�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4001

Enabling Ambisonics������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4001

Ambisonic Metering Options�������������������������������������������������������������������������������������������������������������������������������������������������������� 4001

Ambisonics Metering������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 4001

Ambisonic Effects������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 4002

Setting Up an Ambisonic Mix������������������������������������������������������������������������������������������������������������������������������������������������������� 4002

Binaural Monitoring with Head Tracking�������������������������������������������������������������������������������������������������������������������������������� 4003

Head Tracking Video Viewer Overlay������������������������������������������������������������������������������������������������������������������������������������� 4004

Parallel Ambisonic and Channel-based Workflows���������������������������������������������������������������������������������������������������������� 4004

Ambisonic Rendering����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4004

Immersive Format Configuration���������������������������������������������������������������������������������������������������������������������������������������������� 4004

Exporting ADM BWF������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4005


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

About Immersive Audio Formats

Surround audio formats use multiple audio channels to position sound sources around the listener to

add a creative dimension to sound design. Their simplest formats, such as 5.1 and 7.1 surround, allow

the mixer to send varying amounts of any track to a combination of speakers, placing the audio in

various positions around an auditorium or living room, as centered in front, ambient from the rear, or

weighted towards the left or right of the listener.

More sophisticated immersive formats such as Dolby Atmos™ or Ambisonics define a virtual

soundstage where you can mix the resulting audio to match the speaker configuration or

listening setup.

Dolby Atmos

The traditional surround sound experience outputs a specific set of monitoring channels that requires

a specific number of monitor speakers placed in particular areas of a room, which can position sound

approximately within a ring around the listener. Dolby Atmos improves upon this by being an object-

based sound system operating within a 3D immersive space that can accommodate a wider variety of

different speaker configurations using more speakers positioned around the listener. This increases

dimensionality with more precise sound placement, adding height channels to produce sound

that comes specifically from above. DaVinci Resolve supports Dolby Atmos output render formats

5.1.4 to 9.1.6.

A practical example of this difference can be heard when panning in a 7.1 mix; since you’re sending

signals to specific points in a speaker array, those points are fixed. Although the physical size of rooms

can be larger or smaller, the mix is always sent to those assigned point speakers, so the experience

from room to room may be inconsistent. By comparison, Dolby Atmos gives re-recording mixers a way

to mix to an idealized space instead of fixed speaker positions. This means a Dolby Atmos mix, when

played in a Dolby Atmos room, takes into account the actual dimensions of the space, as well as the

number of speakers that are used, to recalculate audio playback to suit that exact space and playback

Parallel Loudness Measurement������������������������������������������������������������������������������������������������������������������������������������������������ 4007

Low-latency Rendering������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4007

Surround Buses in Fairlight (Studio Version Only)������������������������������������������������������������������������������������������������������������� 4007

Object-Based Format Support (Studio Version Only)������������������������������������������������������������������������������������������������������� 4007

Auro-3D Support (Studio Version Only)���������������������������������������������������������������������������������������������������������������������������������� 4007

Dolby Atmos Configuration Controls��������������������������������������������������������������������������������������������������������������������������������������� 4008

Atmos Re-Renders���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4008

MPEG-H Authoring��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4009

Track Configuration��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4010

Export�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4011

Quality Control������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4012

B-Chain Support for Audio Monitoring (Studio Version Only)�������������������������������������������������������������������������������������� 4012

Overview of Setting Up a B-Chain Configuration��������������������������������������������������������������������������������������������������������������� 4013

Space View�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4016

Space View Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4017


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

equipment, giving a more faithful recreation of the mix with much more specific sound placement,

when necessary.

To give a clear example of the benefits of Dolby Atmos, think of a small theatre that has standard

left, center, and right front-screen speakers. It then has four left surround and four right surround,

four overhead left, and four overhead right. For this example, let’s say you have sent a sound to the

surround left in Atmos, positioned at about one-half of the distance from the screen.

Now move the Atmos mix to a much larger room with twice as many monitor speakers. The new

theatre has eight left surrounds, eight right surrounds, eight overhead left, and eight overhead right.

Playing in this new configuration, Atmos automatically calculates the ratio of the room and the new

speaker array. In this example, when that sound is reproduced at one-half of the distance from the

screen, Dolby Atmos calculates the ratio of the sound in relation to the new playback setup, so the

listener hears exactly what the re-recording mixer intends.

For this example, let’s say to have that audio playing back at one-half of the distance from

the screen in the small room, the audio is played on the second surround speaker on the left.

When this same audio is played in the larger room, Atmos determines that the fourth surround

speaker is one-half the distance from the screen. The importance is not what speaker

the sounds are assigned to but rather where in space the sound should be heard. Atmos

calculates the ratio of the playback spaces and monitor speakers to faithfully reproduce a mix,

rather than assign sounds to a fixed speaker position.

Dolby Atmos Speaker Configurations

It is important to understand that the term Dolby Atmos isn’t restricted to describing any particular

speaker layout. Dolby Atmos is a complex metadata-driven system that interprets the audio from a

configured Atmos mix, determines the playback system of the end user, and calculates the mix to fit

each particular space and system. Assuming the possession of a Dolby Atmos compatible system, if a

7.1.4 Atmos mix is played by someone with only a two channel playback system, then it will intelligently

down mix the 7.1.4 Atmos to stereo. If a user has a standard 5.1 monitor system, then the 7.1.4 Atmos

soundtrack will down mix to five channel surround with a subwoofer.

The naming of the channel configurations in the Dolby Atmos format includes the height channels

in the nomenclature. Channel configurations are presented as three digits separated by periods,

such as 7.1.4, which is a typical speaker configuration. The first digit describes the number of main,

or ear-height monitoring channels that surround the listener. The second digit describes the number

of subwoofer channels. The third digit describes the number of height channels, which are speakers

positioned on, or in the case of a soundbar, pointed at the ceiling.

An example of a 7.1.4 Atmos monitor speaker configuration:

�Seven surround channels

�Left

�Center

�Right

�Left Surround

�Right Surround

�Left Back Surround

�Left Right Surround

�One Subwoofer

�Four height channels


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT