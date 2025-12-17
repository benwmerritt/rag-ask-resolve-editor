---
title: "Keyframe Editor"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 9
---

# Keyframe Editor

The Keyframe Editor provides an interface for animating Color, Sizing, and Stereo Format adjustments

over time. Each node in the Node Editor corresponds to a track in the Keyframe Editor, which lets you

animate each node’s adjustments independently.

Keyframe Editor displaying dynamic grade changes

Furthermore, each node’s track can be opened up to reveal parameter groups, so that you

can animate subsets of an individual node’s functions independently of other functions within

the same node.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

The Fairlight Page

In single monitor mode, the Fairlight page is an optimized look at the audio tracks of your project, with

an expanded mixer and custom monitoring controls that make it easy to evaluate and adjust the levels

of your program in order to create a smooth and harmonious mix.

Fairlight page

About Audio Monitoring and Audio Input

The audio processing throughout DaVinci Resolve, including on the Fairlight page and

audio processing using Fairlight FX plugins, is equally compatible with all platforms that

DaVinci Resolve runs on, including macOS, Windows, and Linux.

DaVinci Resolve supports audio monitoring using:

•	 The audio of a supported Blackmagic Design I/O device such as an UltraStudio or Decklink.

•	 Your macOS, Windows, or Linux workstation’s on-board audio.

•	 Any Core Audio compatible, Windows compatible, or Advanced Linux Sound

Architecture (ALSA)-supported third-party audio interface.

•	 The Fairlight Audio Accelerator, MADI Upgrade, and Fairlight Audio Interface.

DaVinci Resolve supports audio input using the embedded audio on an incoming

SDI video feed when capturing incoming A/V source, via system audio and also via the

Fairlight Audio Accelerator, MADI Upgrade, and Fairlight Audio Interface.

The Audio Timeline

The heart of the Fairlight page, the Audio Timeline presents the audio channels and tracks of the

currently selected timeline differently than the Edit page does, in a one-channel-per-track format that’s

optimized for audio mixing and sweetening. The Audio page Timeline cannot be closed.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

The Audio Timeline

Audio layering in a mono audio track

The Fairlight page of DaVinci Resolve supports multiple audio tracks, and each audio track may

contain multiple lanes. The clips edited into the Timeline appear within each track, with the recorded

channels within each clip occupying as many lanes as that clip has available. At the left of each track is

a header area that contains a number of controls.

The Fairlight page differs in another unique respect from the Edit page Timeline, in that it supports

audio layering. Audio layering is a special audio editing mode that lets you superimpose multiple audio

clips in the same track, and whatever audio clip is on top dictates which audio will play. In a way, when

audio layering is enabled, superimposed audio clips are treated the same as superimposed video clips

that all have opacity set to 100%, with clips on top obscuring (or muting) clips underneath.

Turning on Track Layers opens up space to edit more audio into each track


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Audio layering is incredibly useful for any situation where you’re combining pieces of multiple takes

together to create a single VO, audio vocal track, or dramatic performance, as you can choose which

pieces to prioritize via their superimposed position in the track, while you’re preserving the other takes

underneath in case you want them later.

TIP: Track Layering can be used on the Edit page as well.

Toolbar

The toolbar has buttons that let you choose modes of audio-specific functionality and other buttons

that let you execute commands, such as placing markers and flags.

Buttons in the Fairlight page toolbar

Mixer

The Audio Mixer provides a set of graphical controls

you can use to assign track channels to output

channels, adjust EQ and Dynamics, set levels and

record automation, pan stereo and surround audio, and

mute and solo tracks, all while you continue to edit.

The Audio Mixer exposes a set of channel strips with

controls that correspond to the tracks in the Timeline,

one for each track, plus a Master strip corresponding

to the Master audio track in the Timeline, that lets you

choose the number of audio channels to output, and

also lets you adjust the overall level of the mix.

Dedicated Channel Strip Controls

The Mixer also has a series of dedicated channel strip

controls that add powerful mastering capabilities to

DaVinci Resolve. These include:

�EQ

�Dynamic

�Pan

The Audio Mixer, with

channel strips corresponding

to the tracks in the Timeline


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

EQ: Double-clicking exposes a four-band parametric equalizer with additional Hi and Lo Pass

filters, that has both graphical and numeric controls for tuning the frequencies of the audio on

each track. You can select from among four types of EQ filtering from the Equalizer Type drop-

down menu, with options for Earth (the default), Air, Ice, and Fire. Each band has controls for the

filter type (Bell, Lo‑Shelf, Hi-Shelf, Notch), Frequency, Gain, and Q-factor (sharpness of the band).

The channel strip EQ window

Dynamics: Double-clicking exposes a set of dynamics controls with compressor, limiter, and

expander or gate sections. The Equalizer button at the upper left-hand corner lets you turn all

EQ on and off. The first section can be switched between working as an Expander or a Gate,

with attendant Threshold/Range/Ratio and Attack/Hold/Release controls. The second section

provides Compressor controls, while the third section provides Limiter controls. These controls

may be used either singly or in concert to manage the dynamics of the audio on that track.

The channel strip Dynamics control window


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Pan: A pan control compatible with stereo and surround panning. You can drag within this

control to adjust pan, or you can double-click to expose a Pan window. What controls are

available in the Pan window depend on the mapping of the audio track, but both stereo and

surround panning controls are available, with corresponding numeric controls.

The Pan control window