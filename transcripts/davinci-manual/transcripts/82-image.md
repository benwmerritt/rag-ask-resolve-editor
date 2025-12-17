---
title: "Image"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 82
---

# Image

The Image Inspector controµls for BRAW footage

The Image panel contains groups of parameters

that correspond to every camera raw media format

that’s supported by DaVinci Resolve. Using these

parameters in the Image panel, you can override

the original camera metadata that was written

at the time of recording and make simultaneous

adjustments to camera raw media throughout

your project.

For a detailed explanation of each of the

RAW camera parameters supported by

DaVinci Resolve, see Chapter 7, “Camera

Raw Settings.”

File

The File Inspector controls


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA

Metadata

The File panel of the Inspector provides a consolidated way to view and edit a subsection of a clip’s

most commonly used media file metadata. It’s easily accessible in the Inspector across the Media, Cut,

Edit, and Fairlight pages.

The tab is composed of the following parts:

Clip Details: Presents data about the clip’s data format (codec, resolution, frame rate, etc.).

Metadata: Presents a reduced set of common metadata fields for quick user entry.

•	 Timecode:  The start timecode of the clip. This field is editable if you want to manually

change the clip’s starting timecode.

•	 Date Created:  The date that the clip was created. This field is editable if you want to

manually change the clip’s creation date.

•	 Camera:  Sets the Camera # metadata.

•	 Reel:  Sets the Reel/Card ID.

•	 Scene:  The Scene number of the clip.

•	 Shot:  The Shot letter/number of the clip.

•	 Take:  The Take number of the clip.

•	 Good Take:  This checkbox indicates if the clip is a good or circled take.

•	 Clip Color:  Assign a specific color to a clip that is reflected in the Timeline.

•	 Name:  This can be entered manually and changes a clip’s name in that specific

timeline only.

•	 Comments:  Add a text description to the clip.

•	 Auto Select Next Unsorted Clip:  When this box is checked, the next clip in the Media Pool

is selected when you hit the Return button after entering a metadata field, and the cursor is

automatically placed in the same field. This allows rapid sequential metadata entry without

having to manually click to load each individual clip in the Media Pool. The Next Clip button

will select the next clip in the Media Pool, regardless of the checkbox status.

Audio Configuration

The File tab in the Inspector now has an Audio Configuration pane that handles the controls that were

formerly handled by Clip Attributes in the Media Pool (though that option is still available). The Audio

Configuration pane provides a more intuitive and visual way of changing the track properties of an

audio clip. Simply click on an audio clip in the Media Pool or Timeline, and then on the File Inspector to

reveal this interface.

The pane features a per-channel waveform display for all tracks within a multichannel audio file. If the

tracks have been named in the audio recorder, these names will appear over their respective tracks as

well. The Audio Configuration panel can preview up to 36 tracks of audio.

At the top of the pane, a composite waveform is shown of all the tracks and is updated depending

on the mute status of individual tracks. By default this composite is heard when the Play button is

activated, and all channels are audible.


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA

The Audio Configuration panel. Track 3 has been

muted and Track 5 has been disabled.

A format menu allows you to choose common configurations for your source audio file without

cumbersome manual re-routing. Custom routing can still be accommodated by choosing

custom in the drop-down, which brings up the older clip attributes for situations that require less

common configurations.

Audio for a selected source or timeline clip can be played or skimmed by moving the cursor along the

waveform, and the specific track is solo’ed when skimming or playing. The play position or track being

monitored can also be switched dynamically during playback. For example, you can start playback on

track one, then simply click on track two, and the playback continues from that position. These controls

let you quickly skim through and identify exactly what audio is on which track for further adjustment.

Each track has two adjustments that can be made, an Enable/Disable checkbox and a

Mute button.

Enable/Disable: Enabling a track makes that track available for use in editing operations.

Disabling a track removes that track from use in editing operations. For example, if you disable

Track 2 of a 4-track audio file, when you drag that audio file from the Media Pool into the

timeline, only 3 tracks (1, 3, and 4) will come over.

These adjustments can only be made on Media Pool clips; audio clips already in the timeline

will have these options disabled.

Mute: Clicking this icon will mute the track so it is unheard but leave the actual track in place

when used in editing operations and dragged into the timeline. Option clicking a mute button

on a channel will allow you to solo by muting all other channels.

Underneath the track layout is a simple transport control comprised of Play and Stop buttons to start

and stop audio playback.


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA

Adjusting Trim Levels of Individual Channels in a Source File

The level of individual source clip channels in the audio inspector can be be adjusted via a trim

control. This allows source clip audio in one channel to be brought up in level or brought down in level,

as needed.

The trimmed level is internal to source clip in the Media Pool and will be inherited whenever that

source clip configuration is used on a timeline, unless it is changed.

NOTE: The trim level is totally separate from clip gain in the timeline. Be aware that trimmed

levels can clip if you move them too high.

You can adjust the trim levels of individual

audio channels in a multichannel clip.

Using the Trim slider


Select one or more channels in the Audio Configuration section of the File Inspector


Adjust the Level slider at the bottom to the desired audio level.

The waveform will adjust dynamically to the level value and will display a trimmed value in dB in the

channel itself. If you have multiple lanes selected, all channels will be trimmed together. Relative levels

are not stored, so if you adjust one, it will then force any others in the selection to match. When no

channel lanes are selected, the Level control is grayed out.


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA

Multiple Clip Selection and Adjustments

You can select multiple audio clips and adjust their properties in the Audio Configuration

pane. For example, you can select a group of audio files and remove Track 2 from all of them

at once. However, the following should be noted:

•	 In a multiple clip selection, only the last selected clip will appear in the track layout of

the Audio Configuration pane. However the top composite waveform will be named

“Multiple Clips” to let you know that more than one clip has been selected.

•	 Any adjustments, like muting or enabling/disabling a track will be applied to all the

selected clips at once.

Timecode

The File tab in the Inspector now has a Timecode pane that handles the types of controls that were

formerly handled by Clip Attributes in the Media Pool (though that option is still available). Here you

can override the timecode details for a clip or clips in the Media Pool.

�Current Frame: Lets you assign a new time for the timecode at the currently viewed frame of

the clip.

�Slate: In situations where source media comes from a shoot where a timecode slate was used

during the shoot, then you can assign the slate timecode as a second timecode track that can be

used for various operations, without changing the primary timecode of the clip, which may already

be in use for program sync.

To set appropriate Slate timecode, select a clip in the Media Pool with a visible timecode slate, and

move the playhead to a frame where the timecode in the slate is clearly readable. Then, open the

Timecode panel of the Clip Attributes window, and type the timecode value you see in the image

into the Slate Timecode field.

�Offset Source: If an entire set of clips has timecode that’s merely offset, you can correct the

timecode offset for as many selected clips as you like.


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA