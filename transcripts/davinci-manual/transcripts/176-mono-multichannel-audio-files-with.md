---
title: "Mono-Multichannel Audio Files with"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 176
---

# Mono-Multichannel Audio Files with

Suffixes Import as a Multichannel Clip

DaVinci Resolve can interpret and import mono audio files with channel name suffixes as a single

formatted multichannel audio clip. The format depends on the number of files detected and

the channel suffixes. As an example, Audio001.L.wav and Audio001.R.wav by themselves are

interpreted as a stereo ‘Audio001.wav’ clip. A third file with a ‘C’ or ‘LFE’ suffix results in LCR or 2.1

formatted media.

Importing multi-mono audio files to a single multichannel track

Switch Mono Audio Channels

of a Clip on the Timeline

You can change your mic (or other) audio sources on mono channel lanes in the Edit page by using

a context menu or via the Inspector. This can be handy when editing using a mix track, and you find

there is a lav mic that has noise on it, and you want to use boom audio instead.

There are two methods for changing mono audio sources: in the timeline or in the Inspector.

Changing mono audio sources via context menu on the timeline:

Right-clicking on an audio clip will reveal

the source audio channel choices to choose from

If you are on a mono timeline track and the parent audio file for your track contains multiple

mono tracks, right-click on it and an Audio Channel choice appears at the bottom of the

context menu. You can then choose any mono source from the hierarchical menu.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Command right-click on an audio clip in the timeline

to reveal just the source audio channels

Alternatively, for an even more streamlined workflow, you can press Command right-click and

you will then get a drop-down with only the mono sources:

Changing mono audio sources via the Inspector:

When a timeline clip is opened via the File Inspector, you can change mono track/lane

sources by using a drop-down on the channel waveform.

You can change the audio channel by using

a drop-down menu on the channel in the File

Inspector in the Auµdio Configuration section.

Editing Audio Into the Timeline

A separate set of audio tracks in the Edit page Timeline contain all of the audio that you edit into the

Timeline, as well as any stand-alone audio files that might have been imported along with an AAF

or XML file.

Editing Audio Using the Source Viewer

Opening an audio-only clip into the Source Viewer, or opening a clip with both video and audio and

setting the Viewer to Audio Waveform results in a split view, with the complete waveform of the entire

source clip shown in the top half, and a zoomed-in view of the waveform in the bottom half that can be

set to zoom from 1x to 50x from the Zoom menu at the upper left-hand corner of the Source Viewer.

This view makes it easy to drag the box at the top to find the section of audio you need relative to the

entire clip, and yet still place In and Out points with great precision using the scrubber bar below.

This view shows every channel within each track of the current clip.

You can add markers and set In and Out points for audio clips just as you would for any other clip, in

preparation for editing.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

An audio clip opened into the Source Viewer

Simultaneous Audio Waveform Display in the Source Viewer

It’s also possible to edit using audio waveforms even when the Source Viewer is set to Source.

Two options in the Option Menu let you see a superimposed audio waveform running along the

bottom of the Viewer, over the video of the currently selected clip.

�Show Current Frame Audio Waveform: Shows a zoomed-in section of audio that scrolls as you

play the clip. Useful for seeing dialog and music cues as you play through a clip.

�Show Full Clip Audio Waveform: Shows the audio waveform for the entire source media of

that clip. The section of audio from the In to Out points you’ve set in the Source Viewer are

highlighted. Useful for using the audio waveform to navigate throughout that clip using the

waveform as a reference.

The Source Viewer with “Show Current Frame Audio Waveform” enabled,

displaying the audio waveform along the bottom of the image


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Using Multi-Channel Timeline Tracks

Multi-channel audio tracks in the Edit page Timeline are extremely convenient when you’re dealing

with clips that are stereo, 5.1, 7.1, or have an arbitrary number of channels that were recorded in

the field, as you can fit all of these channels as a single clip into a single track, that will be correctly

mapped to your project’s outputs, and that can be edited conveniently as a single item in the Timeline.

However, when you open the Fairlight page you’ll see that although the overall number of audio

tracks is identical to the Edit page, the Fairlight page shows the channels that are otherwise hidden

on the Edit page as lanes within each track, which expose each channel as a visible audio item in the

Timeline. In this way, editors can work with multi-channel audio without worrying about visual clutter,

while audio editors and mixers can see every channel on every track to help them get their work done.

Getting back to audio tracks on the Edit page, there are different types of audio tracks just like there

are different types of audio clips: Mono, Stereo, 5.1, 7.1, and Adaptive. While you can edit any kind of

audio clip into any kind of audio track, all clip audio channels that exceed the number of channels

possessed by a particular type of timeline track will be muted. For example, you’re allowed to edit a

six-channel Adaptive audio clip into a Mono audio track, but only the first channel will play because

the Mono track only outputs one channel.

Because of this, it’s a good idea to organize your timeline such that all clips appear on tracks that can

accommodate the number of channels they have.

TIP: Editing an audio clip into the undefined gray area below existing audio tracks in the

Timeline will result in the automatic creation of new audio tracks that are equal in number

to the number of tracks the clip you’re dragging has, and each new track will have audio

mappings that match the incoming audio items.

Defining Timeline Audio Track Channels at Creation

When you first create a new audio track, you have to choose what kind of audio track it will be. Right-

clicking in the bottom audio portion of the Timeline track header reveals a contextual sub-menu that

lets you create one of three different kinds of audio tracks.

�Mono: Holds a single channel.

�Stereo: Holds stereo left and right channels. Stereo tracks can be panned.

�5.1: Holds the six channels corresponding to a 5.1 surround mix. For broadcast, SMPTE specifies

Left, Right, Center, LFE, Left Surround, Right Surround. For cinema distribution these tracks are

ordered Left, Center, Right, Surround Left, Surround Right, and LFE.

�7.1: Holds the eight channels corresponding to a 7.1 surround mix. For broadcast, SMPTE specifies

Left, Right, Center, LFE, Left Surround, Right Surround, Back Surround Left, and Back Surround

Right. For cinema distribution these tracks are ordered Left, Center, Right, Left Surround, Right

Surround, LFE, Back Left Surround, and Back Right Surround.

�Adaptive: Capable of holding up to 24 audio channels. An adaptive audio track can hold clips with

different combinations of channels, up to the maximum number of channels allowed within that

track. The number of channels allowable on a particular Adaptive track is user-definable (1–24) at

the time that track is created. If you edit a clip with more channels into an Adaptive track that was

created to hold fewer channels, the extra channels are muted.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Four audio tracks with a variety of audio tracks shown. From the top down, Mono, Stereo, Adaptive, 5.1

Changing How Many Channels an Audio Track Has

If you had set up your timeline with one kind of audio track, but you discover you actually need a

different kind, you can change any audio track’s type at any time. Just right-click anywhere in that

audio track’s timeline header, and choose an option from the Change Track Type To submenu of the

contextual menu.

Contextual menu for changing audio track types

Creating Timelines With Audio Mixer Presets

For advanced audio workflows and ease of use with Fairlight, you can now create a timeline with pre-

assigned audio tracks using a previously created Fairlight Configuration preset. To use this function,

create a new timeline, and check the “Use Fairlight Configuration Preset” box. A drop-down menu

then appears, allowing you to select the specific preset for the Timeline.

You can create Fairlight Configuration presets using the Fairlight Presets Library, available from the

Fairlight menu.

For more information, see Chapter 171, “Setting Up Tracks, Busses, and Patching.”


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT