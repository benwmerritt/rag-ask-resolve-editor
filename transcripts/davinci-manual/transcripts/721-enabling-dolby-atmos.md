---
title: "Enabling Dolby Atmos"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 721
---

# Enabling Dolby Atmos

Atmos must be enabled by going into Preferences > Video and Audio I/O > Immersive Audio panel and

turning on Enable Dolby Atmos. When enabled, the Change Track Type contextual menu when right-

clicking on a track will then include the additional Atmos track types.

The Components of a Dolby Atmos Mix

Mixes created in Atmos have several specifically identified components. These work together to

create an immersive mix, but each element allows the Dolby Atmos system to fit the sound specifically

to the space and speaker configuration during playback.

These consist of:

The Bed track: Contains the bulk of mixed audio, including dialog, ambient sound effects, and

music. These sorts of sounds will contain panning information, but the panning will be general.

Wind, traffic in the distance, room tones, and sync dialog would all most likely fall within the

bounds of a standard bed track of 7.1.2 or 5.1.

Object tracks: Pinpoint the placement of sounds moving specifically across the immersive

space. Users can use these specific tracks to create panning anywhere in the room. Sounds

can fly through space, around a room from height channels, to side and back channels,

mimicking the motion of objects on the screen. Object tracks use the Atmos metadata to do

the calculations discussed in the last example. ADM files are Atmos exports used with the IMF

file type as master deliverables, which are in the broadcast wave file format.

It’s up to users to define which tracks are Bed tracks, and which are Object tracks; these track

designations, are descriptions of what the tracks you create are going to be used for. Ultimately, it’s

up to the mixer which audio is organized on Bed tracks, and which is organized on Object tracks.

Theoretically, users can create a mix consisting entirely of Object tracks if desired, but typically the

mix would be split into beds consisting of generally panned sounds, and Object tracks for sounds

requiring specific room placement.

Object tracks and height channels open up possibilities that were never possible prior to Atmos.

Imagine a scene where a man is hiding from Police while a helicopter circles overhead, or a scene

where kids are in a basement and are startled to hear loud footsteps above them. With Atmos, the

audience can now experience these immersive sounds along with the characters.

These are real-world examples, but sound in animation, science fiction, and fantasy can explore space

in ways that are only limited by the creator’s imagination. Flying fairies or creatures can move about

the space front to back, high and low. Perhaps there’s a scene with a ship moving full speed ahead

underwater, breaking up and out into the sky, flying and dodging weapons coming from all sides.

Object tracks are ideal to pinpoint sound effects requiring spatial specificity, but more importantly,

Atmos assures the re-recording mixer that the final choices made in the mix will be faithfully recreated

from theatre to theatre, and from room to room.

NOTE: Buses feeding the Atmos master become beds, and Tracks feeding the Atmos master

become objects.


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

Predetermined Dolby Atmos Master Rules

The first ten tracks in every Dolby Atmos Master are assigned as a bed by default. From there the

default bed is a 7.1.2 bed, however, it can be designated to a 2.0 up to the 7.1.2 bed. There is no option

to add objects to these first ten tracks. Starting at track eleven, the tracks that follow can then be

made into various beds or objects as needed.

A simple way to think of this is that buses routed to the Atmos Master are treated as beds, carrying

predefined multiple sources. An Atmos bed is a fixed surround format that can contain height

channels. Objects, are generally mono but can send any format track that DaVinci Resolve supports

and follow the metadata as a single object element. Objects routed to the Atmos Master are treated

as tracks, carrying dynamic audio content and positional metadata. LFE will need to be sent to a bed,

since objects are positional metadata. If the object is 5.1 for example, the LFE channel will need to be

routed to a Bed bus in order to be rendered in the Atmos master.

The Dolby Renderer will render the file if it is dragged from the Media Pool into a track in the Timeline.

In this case it will render the media with the embedded metadata to the master’s output format. This

is a simple way to monitor pre-mastered content and to perform simple actions, such as trimming or

syncing for new packaging and deliverables.

When importing a Dolby Master file from the Fairlight menu, Fairlight > Immersive Audio > Import

Master File, the resulting import will extract all of the audio and metadata for further content creation.

This type of importing into Fairlight maps all of the metadata, tracks, beds, and objects from the master

file into the Timeline, allowing you to adjust, process, and manipulate further, to rewrite panning,

punch-in and add new media, and create a new Atmos Master.

Dolby Atmos files are a package of items. Simply linking files will not create an Atmos Master file. It is

not possible, for instance, to take a rendered set of twelve tracks, link them, and then configure their

outputs to a 7.1.4 Atmos bed. Note that 7.1.4 is not a Atmos bed type. Although this is the way typical

PCM audio is linked and routed, it is not the case for Atmos content, which is far more than just a

collection of tracks.

The renderer takes the 128 channels consisting of the beds and objects and renders it. Those

channels are either internal sources or contained within the master file. A simple linked file will not play

back through the Renderer. It must be played back as all linked files in Fairlight do, through the native

monitor. The Dolby Atmos Renderer plays, renders, and extracts Atmos Master files. Fairlight allows for

.atmos, ADM, and IMF file types to be imported and played through the Renderer.

NOTE: As mentioned above, the LFE can only be rendered in an Atmos master when routed

as part of a bed due to the Dolby Atmos specification.

Dolby Atmos Integration

There is native Mac M1, Windows, and Linux support for the internal Dolby Atmos workflow including:

�Input

�Content creation

�Internal renderer

�Export of Dolby Atmos Master Files

There is a dedicated Dolby Atmos Master bus format which provides a master fader in the Mixer for

the Dolby Atmos Renderer and is indicated by the Dolby logo in its header. It also provides a loudness

history graph in its Timeline view with integrated, momentary, and short term loudness measures.


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

In the Bus Format window you will see that there are no outputs from this track; it is a control for the

Dolby Atmos Renderer.

Only a single master bus can be created, and it will always mirror the format and metering of the

internal renderer. When there are no patches to the Dolby Atmos Sends, all sources routed to a Dolby

Atmos Master bus will target the master, as with a traditional bus workflow. In this send workflow,

buses become beds and tracks become objects.

For Mac and Windows machines, the integration of the external Dolby Atmos Renderer has been

updated, providing a much closer integration when running an external workflow. This has unified the

tools available within the internal renderer workflows with the external renderer. This includes:

�External Renderer discovery within the preferences.

�UI enable to switch between the internal and external workflow.

�Tally of the master connection state and master file status.

�Storage and recall of the program metadata within the DaVinci Resolve Timeline, including all input

configuration, trims, down-mix, and binaural settings.

�Direct control of the metadata from the renderer and binaural controls within DaVinci Resolve and

bi-directional control of that program metadata from the server.

�Tally of the input configuration within the Patch page.

�Multi-client workflow support, allowing multiple instances of DaVinci Resolve to run attached to

the same server for larger workflows.

�Tally of the active bed and object assignments on the Dolby Atmos Sends within the Patch page.

When assigning a bed or track to the Atmos Master on the Patch page, beds are indicated with a

purple marking and objects are indicated with a green marking.

Binaural Audio Monitoring

You can monitor your Dolby Atmos Master in Binaural by choosing Binaural in the monitor section.

The Binaural monitoring option

Depending on your monitoring system, you can also create a parallel speaker monitoring set up with

Binaural. For instance, you can create a 5.1. external monitor mix along with a binaural headphone mix.

In Preferences > Video and Audio I/O, you can set Binaural to the headphone outs in the Audio I/O

panel, and a 5.1 monitor in the Monitor Speaker configuration. Then, in the Patch Input/Output panel,

you can route to the appropriate positional channels specific to your system and settings and also

assign available channels for the headphones.


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

Using the Patch Input/Output to assign parallel binaural monitoring

Binaural Render Options

Binaural rendering is a simulation of the distance between the sound source and the listener. In the

Index there are options on how you can choose to render the binaural objects. The default option

is Mid, but you can also choose Off, Near, or Far, depending on the desired rendering for binaural.

These choices will all be stored in the Dolby Atmos file.

Binaural choices in the Tracks Index for assigning perceived distance


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT

You can use Clip Attributes to render a Dolby Atmos Master in Binaural. Simply right click the file to

open Clip Attributes, select Binaural, and then right-click to create a new Timeline with the file. In the

example below, a 7.1.4 file will be rendered to a Binaural audio file.

Using Clip Attributes to render to a Binaural file

Ambisonics

Ambisonics is a full-sphere multi-channel immersive “adaptive” audio format that lets you position

sounds in the horizontal and vertical planes.

Compared to other surround formats, Ambisonics transmission channels aren’t speaker-specific and

represent a complete sound field captured by a specialized microphone for an accurate positional

depiction of “sound in space,” or generated from channel-based sources via sophisticated encoders.

The flexibility of this audio format makes Ambisonics compatible with various speaker configurations,

such as 5.1 and 7.1.4, headphones, and large arrays in multiple applications, including theme parks, art

installations, video games, and virtual reality.

You can even work and mix between channel-based and Ambisonics formats, without the need for

third-party audio plugins.

DaVinci Resolve Fairlight’s full Ambisonics support includes spherical panning, Ambisonic bussing,

Fairlight, AU, and VST Ambisonics effect plugins, accuracy up to fifth order High Order Ambisonics

(HOA), and channel and binaural decoding to headphones.


Fairlight | Chapter 184 Immersive Audio Workflows

FAIRLIGHT