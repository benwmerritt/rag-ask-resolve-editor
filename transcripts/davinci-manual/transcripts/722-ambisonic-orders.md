---
title: "Ambisonic Orders"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 722
---

# Ambisonic Orders

Ambisonics “orders” define the mathematical precision and number of discreet channels to represent

the sound field, ranging from the first to the seventh order. First order uses four discreet audio

channels, while higher orders use more channels, requiring greater processing power.

Although DaVinci Resolve Fairlight supports up to fifth order Ambisonics, requiring 36 channels, you

can get great results using third order and 16 channels.

Ambisonic File Support

DaVinci Resolve supports Ambisonic files in WAV, BWAV, or .caf (including 1OA AMB

and AmbiX) formats.

Adding a Media Pool clip to the timeline or creating a new timeline that refers to a clip creates a track

of the appropriate type, matching the file’s Ambisonic order and channels.

Enabling Ambisonics

Ambisonics is enabled by going to Preferences > Video and Audio I/O and clicking the Enable

Ambisonics checkbox in the Immersive Audio section.

Ambisonic Metering Options

Mixer and Track Header Meters

Fairlight Ambisonic metering utilizes a single, composite bar-graph meter in the Mixer, Track header,

and Meter panel. Unlike other audio formats, they don’t correlate to specific speaker positions or

levels we would track visually to determine what is happening with the signal.

Alternatively, you may want to use bar-graph meters that display Ambisonic signals as discrete,

separate bus streams by choosing Fairlight > Immersive Audio > Ambisonics Channel Metering.

Default Ambisonics metering (left)

and Discrete Channel metering (right)

Ambisonics Metering

This Fairlight FX audio plugin offers two different visual metering options for analyzing your audio.

The Ambisonics meter can be added to an audio track or bus via the channel strip’s Effects section.

For more information about the Ambisonics Meter, see Chapter 181, “Fairlight FX.”


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

Video Viewer Overlay

The Fairlight page also offers Ambisonic metering options as overlays on the Video viewer, allowing

you to analyze the sound intensity against the picture.

To enable the Ambisonics Meter overlay:

�Activate 360 Viewer Mapping in the Video Viewer tools menu.

�Go into the Ambisonics Meter submenu, click On, and select one of the metering modes.

Enabling the Ambisonics Meter overlay

Ambisonic Effects

While most Fairlight FX plugins, such as the Multiband Compressor, Limiter, Reverb, and Channel

Dynamics and EQ, are Ambisonic-native, DaVinci Resolve also supports compatible Ambisonic-native

third-party AU and VST effects.

For more information on the Channel Dynamics and EQ plugins, see Chapter 177, “Mixing in

the Fairlight Page.”

For more information on Audio Effects plugins and how they can be used in DaVinci Resolve,

see Chapter 180, “Audio Effects.”

For more information on individual Fairlight FX plugins, see Chapter 181, “Fairlight FX.”

Setting Up an Ambisonic Mix

To organize and set up your Ambisonic mix:

�The first thing you need to do is determine which Ambisonic order you want to work in.

A higher order such as third order (16 channels) is best for precise positioning.

�Create Ambisonic busses and assign your source tracks or other busses to them.

You can assign Ambisonic busses to other Ambisonic busses, even with differing orders.

The Fairlight engine and FlexBus will automatically handle any required up- or down-mixing.

�Use the 2D or 3D Spherical Panners on each channel to position your sources in the Ambisonic

space. You can use any channel-based format from mono to stereo to, for example, 7.1.2, and

position them freely in the spherical sound field.

For more information on the 2D and 3D Panners, see Chapter 177, “Mixing in the

Fairlight Page.”


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

�Click the Bus Monitoring menu to the far right of the Transport control, and select the source you

want to monitor.

Monitoring Source selection

�Choose your output format in the Monitor section dropdown next to the speaker output level

control. You’ll notice various options, including Binaural for monitoring on headphones. Once

you’ve selected a format, the corresponding decoder is automatically placed in the monitoring

path, and the audio is routed to your Audio I/O and sent out to your speaker system.

Output Format selection

Binaural Monitoring with Head Tracking

If you’ve selected the Binaural option as your output format, you can also monitor your Ambisonics mix

on headphones with support for Head Tracking for an enhanced monitoring experience.

Head Tracker preferences

Enabling Head Tracking

Head tracking functionality can be activated by going to Preferences > Control Panels > Head Tracker.

This adds two buttons to the left of the Monitor Bus Source dropdown immediately below the docked

Video Monitor panel:

HT: Switches Head Tracking on and off.

CAL: Calibrates the current tracker direction as the “Front” or point of origin.


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

Head Tracking Video Viewer Overlay

Binaural Head Tracking also lets you add an overlay to the video viewer for analyzing your mix against

the picture, by clicking Headtracking Display > On, which adds an onscreen crosshair, indicating the

current head (headphone) orientation.

This submenu also includes a Show Torso option which adds a head and torso to the video viewer,

that rotates as the head tracking angles and positions change.

Head Tracking Video Viewer overlay

Parallel Ambisonic and Channel-based Workflows

You can create Ambisonic and channel-based mixes in the same timeline and simultaneously render

multiple outputs in different formats.

Because of the common panning data, it’s also possible to set up a parallel mix in an

Ambisonic timeline by converting an existing production of a differing surround format

(e.g., Dolby Atmos) to Ambisonics format and importing that into your production.

Ambisonic Rendering

Ambisonic mixes can be rendered on the Deliver page as either a multichannel adaptive file with

the number of streams determined based on the Ambisonic order of the mix (e.g., 1OA, 2OA, etc.) or

downmixed to the format of your choice, such as 7.1.4.

Immersive Format Configuration

In Preferences > Video and Audio I/O > Immersive Audio, you can enable the various Immersive

options that are available. These are Ambisonics, Audio Vivid, Auro 3D, BS.2051, Dolby Atmos,

MPEG-H Audio, 22.2 Surround, SMPTE ST 2098, and 360 Reality Audio.

In Preferences > Video and Audio I/O > Dolby Atmos, you can configure the use of an external Dolby

Atmos Renderer for Dolby Atmos monitoring and mastering. You can manually enter the IP address of

the server, or select a discovered server using the dropdown menu. You should also choose the base

audio output of the audio outputs, which will used to send the audio to the external renderer.


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

Controls for enabling immersive audio formats in the Video and Audio I/O preferences

Exporting ADM BWF

You can export a Dolby Atmos master file as an audio-only ADM BWF, right from the Fairlight timeline.

These same options are also available in the Deliver page. Exporting a Dolby Atmos master file from

the Fairlight timeline uses the Timeline name as the filename. Be sure to change the Timeline name to

the desired filename.

�In the Media Pool, locate the current Timeline.

�Change the Timeline name to your desired export filename.

�As with all other bouncing and delivery methods, you will need to mark a range in the

Timeline to export.

�Press R for the Range Selection tool. Double-click any of the Timeline clips to set a range

for the entire clip.

�Choose Fairlight > Immersive Audio > Export Master File.


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

Export Immersive Master options

�In the Export Immersive Master dialog, set the File Name to Timeline Name and the Format

to Dolby Atmos ADM BWF. You can select either 48000 (delivery) or 96000 (delivery) for the

Sample Rate of the exported file. The Source is automatically set to the Atmos Send Patching. This

patching passes the signal through the sends to the internal Dolby Atmos Renderer for processing

and to generate a new Dolby Atmos master file.

�Click Export.

�In the Export Immersive Master finder window, navigate to the folder you want to file to save to.

Click Save.

The Export Immersive Master dialog shows the source and format for the new ADM export.

The Export allows for several types of file types:

•	 Dolby Atmos ADM BWF

•	 Dolby Atmos IMF IAB

•	 Fraunhofer MPEG-H Production

•	 Fraunhofer MPEG-H Production XML


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT