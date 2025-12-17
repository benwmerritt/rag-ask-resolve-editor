---
title: "Chapter 21"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 83
---

# Chapter 21

Syncing Audio

and Video

When you’re working on a program where the production audio was recorded

separately from the production video (often referred to as “dual-system recording),

DaVinci Resolve provides tools for syncing the audio and video together in a

variety of ways to create media that you can edit easily. The process of syncing

audio and video together is often referred to as “syncing dailies.”

Contents

Syncing Audio to Video��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 438

Syncing Audio to Video Using Timecode�������������������������������������������������������������������������������������������������������������������������������� 438

Syncing Audio to Video by Matching Waveforms��������������������������������������������������������������������������������������������������������������� 439

Manually Syncing Audio to Video������������������������������������������������������������������������������������������������������������������������������������������������ 440

Retaining Video Metadata and Embedded Audio when Syncing Audio Manually����������������������������������������������� 441

Offsetting the Sync of Previously Synced Clips������������������������������������������������������������������������������������������������������������������� 442

Finding Synced Audio Files������������������������������������������������������������������������������������������������������������������������������������������������������������ 442

Displaying Synced Audio File Names on the Timeline����������������������������������������������������������������������������������������������������� 443


Ingest and Organize Media | Chapter 21 Syncing Audio and Video

MEDIA

Syncing Audio to Video

If you’re processing dailies for a shoot that used dual-system recording, where audio is recorded

to a separate device than video, you can “sync the dailies” in DaVinci Resolve in one of two ways.

Synced clips can be output as media files with embedded audio or output to tape, whatever your

client requires.

Syncing Audio to Video Using Timecode

Ideally, if the sound recordist on set was highly organized, and the camera and audio recorder both

used synchronized timecode, you can use a single command to automatically sync every clip in a

timeline to a bin of Broadcast .wav files that have matching timecode.

To batch sync audio to video using timecode:


Create a new project, open to the Media page by default, and import the video media you need to

sync into any bin of the Media Pool.


Import the matching Broadcast .wav files into the same bin as the accompanying video media you

imported in Step 1. If you want to stay more organized, you can create another bin to contain the

audio clips, but it must be inside the bin that contains the video files. The audio bin can be named

anything you like.

Organizing production audio in a bin created

within the accompanying camera media bin


Right-click the bin containing the matching audio and video clips, and choose one of the following

commands from the contextual menu:

Auto-Sync Audio Based on Timecode: Replaces each video clip’s previous audio channels with

audio channels from the newly synced .wav files.

Based on Waveform: Analyzes and compares the waveforms of each of the selected clips and

replaces each video clip’s previous audio channels with the newly synced .wav files.

Retain embedded audio: Adds new channels in addition to the audio channels that were

previously in the media file. The newly waveform-synced channels are added to an additional

track, so when edited into the timeline, a clip that’s synced this way appears with one video clip

and two audio clips that occupy two different audio tracks, so you can edit the camera original

audio independently from the synced audio.

Every clip in the selected bin for which there was an accompanying Broadcast .wav file with matching

timecode is immediately synced with an audio track. If multiple audio files overlap with matching time

code, each file will be synced and a new audio track added to the resulting clip to accommodate each

audio file. You can modify this behavior to only sync the single best matching file and ignore others

by checking the “Limit media pool audio sync to first timecode match” box in the Editing panel of the

User section in the DaVinci Resolve Preferences.

All synced clips appear with an audio icon at the bottom left in the Media Pool when Thumbnail view is

selected. Now that the clips are synced, you can edit them in the Edit page or use the Deliver page to

export offline dailies or online media with embedded sync audio for use in other applications.


Ingest and Organize Media | Chapter 21 Syncing Audio and Video

MEDIA

Syncing Audio to Video

by Matching Waveforms

If you don’t have matching timecode in the audio and video source clips you’re syncing, but you had

the foresight to record camera audio at the same time as the dual source production audio you want

to sync to, DaVinci Resolve can use waveform syncing to compare the audio waveforms of your audio

and video source files, and sync the ones that match.

Progress dialog for syncing dialog using waveforms

To batch sync dailies using waveform syncing:


Create a new project, open to the Media page by default, and import both the video and audio

media you need to sync. There’s no need to organize your files in any particular way, but it’s not a

bad idea, on multi-day shoots, to organize the audio and video files so that it’s easy to select all of

a single day’s clips at once so that you can sync your files in smaller batches. Even organizing your

clips by scene can make waveform syncing go faster by reducing the number of files that need to

be compared at once.


If you’ve placed the audio and video into separate bins, then you can Command-click both bins

in the bin list to select them and expose all of their contents in the Media Pool. If you placed your

media in the same bin, this is not necessary.


Select one of the exposed clips in the Media Pool, and press Command-A to select all audio and

video clips you want to sync.


Right-click one of the selected clips, choose Auto Sync Audio from the contextual menu, and

select one of the methods below.

Based on Timecode: Synchronizes the timecode between the audio and video clips, and replaces

each video clip’s previous audio channels with the newly synced .wav files.

Based on Waveform: Analyzes and compares the waveforms of each of the selected clips, and

replaces each video clip’s previous audio channels with the newly synced .wav files.

Use channel number: Lets you choose which audio track to perform the waveform analysis

on. With the default of “Auto,” DaVinci Resolve automatically picks the channels most suited for

waveform comparison. With “Mix,” DaVinci Resolve compares waveforms from the mixdown audio

from all available channels. This can be useful when audio may not be present on long sections of

one or channels. Users can also specify individual channels to avoid noisy audio.

Retain embedded audio: Analyzes and compares the waveforms of each of the selected clips,

and adds new channels in addition to the audio channels that were previously in the media file.

The newly waveform-synced channels are added to an additional track, so when edited into the

Timeline, a clip that’s synced this way appears with one video clip and two audio clips that occupy

two different audio tracks, so you can edit the camera original audio independently from the

synced audio.


Ingest and Organize Media | Chapter 21 Syncing Audio and Video

MEDIA

A progress bar dialog appears, showing you how long the syncing operation will take. When it’s

complete, your clips will be synced.

Progress dialog for syncing dialog using waveforms

TIP: After syncing, you may be notified via a dialog that one or more clips could not

be synced. Note these clips, as it may be possible to use waveform syncing more

successfully on just the selected pair of audio and video items that belong together.

Manually Syncing Audio to Video

If you have a collection of WAV or AIFF audio files with video source media that lacks matching

timecode, you need to manually sync each pair of media files together, one-by-one, using a

sync reference such as the clap of a clapperboard or any other sharp sound with a distinct

audio/visual correspondence.

To manually sync audio to video:


Create a new project, and import the video media you need to sync into the Media Pool. If a dialog

appears asking whether or not you want to update the project to match the media, click OK.


If you want to stay organized, create a second bin in the Media Pool, named Audio Clips, and

import the matching Broadcast .wav files into it. The name of the bin is not important, and having

all the audio in one bin is simply a matter of convenience.


Click the Waveform button at the top of the Audio Panel, which lets you view and scrub along the

waveform of audio clips you select in the Media Pool.


Select a video clip to sync, and move the Viewer playhead to line up with the first visual sync point

in the first clip. This could be the clap of a clapperboard, the red flash of a tablet computer’s slate

app, a hand clap, or any clear visual cue to which there is a corresponding audible sound.


Now, select whichever audio clip corresponds to the current video clip in the Viewer, to open its

waveform into the Audio Panel.


Use the Audio Panel transport controls and scrubber bar in the Source Viewer to move the

playhead to the audio sync point that corresponds to that video sync point. This may be a clap,

a beep, or some other staccato sound that’s easy to sync to. As you play through the clip, the

bottom half of the Viewer shows a zoomed out waveform for the entire clip, while the top half of

the Viewer shows a zoomed in section of the waveform that immediately surrounds the playhead.

Hopefully, the sync point you’re looking for is a distinct, loud spike somewhere towards the

beginning or the end (in the case of a tail slate) of the audio clip.


Ingest and Organize Media | Chapter 21 Syncing Audio and Video

MEDIA

Aligning video and audio sync points with the Audio Panel set to show the Waveform panel


When you’ve found the audio sync point that matches the video sync point, click the Link/Unlink

Audio button at the bottom right of the Audio Panel to embed the now synced audio into the

video clip.

Clicking the sync link button to lock sync

The audio and video items are linked. At this point, you can use the newly synced clips in the Edit

page, and use the Deliver page to export offline or online media with embedded audio for editing.

Retaining Video Metadata and

Embedded Audio when Syncing Audio Manually

When syncing audio to video manually in the Media page, you can choose whether to include the

original camera audio tracks in the synced file, or whether to retain the camera scene/take metadata,

rather than have the audio file scene take metadata overwrite it as normal.

In the Media page > Audio > Waveform tab, the option (3 dot) menu now offers 2 choices:

The Audio > Waveform tab (3 dot) option menu lets you choose

to retain embedded audio and/or video metadata.


Ingest and Organize Media | Chapter 21 Syncing Audio and Video

MEDIA

Retain embedded audio

�When enabled, embedded camera audio tracks are included with any newly synced audio during

the manual linking process (using the link icon on this pane).

Retain video metadata

�Default is off, which means that video files that are synced to audio files inherit metadata (e.g.,

scene and take) from the audio file. When this option is checked, the video file’s metadata is

retained and not overwritten instead.