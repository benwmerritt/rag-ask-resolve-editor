---
title: "Editing Audio Clips Into the Timeline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 177
---

# Editing Audio Clips Into the Timeline

When you edit a video clip with accompanying audio, or an audio-only clip, into the Edit page Timeline,

what you see depends on how the audio’s internal tracks and channels were defined in the Media

Pool, using Clip Attributes. If you’ve defined a clip to expose multiple tracks of audio, each exposing

a different channel, then you exchange the convenience of managing multiple channels of audio as a

single item for the freedom to individually edit each channel of audio separately, as individual clips in

the Timeline.

For example, if you’ve been given a multi-channel recording that consists of two boom microphones,

two separate lavaliere microphones, and a mixdown track that were recorded simultaneously, you can

use the Audio panel of the Clip Attributes window to set that clip’s audio up as 5-channel Adaptive

audio with 5 tracks containing one channel each. Editing this into the Timeline, you end up with five

separate audio items appearing in five tracks.

Editing a multi-channel production recording as five separate tracks of audio

This way, when you edit that clip into the Timeline, each audio channel appears as its own clip in

its own audio track of the Timeline, which can be separately edited so you can edit the scene to

isolate the best dialog from each microphone.

Editing multi-track audio to isolate the best dialog from each microphone


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Changing Audio Clip Attributes After Editing

It’s best to make decisions about which audio tracks and channels are assigned prior to beginning

editing. This is because once you’ve edited a clip into a timeline, you can’t use the Clip Attributes

window to edit how many audio tracks and audio channels are exposed in the Timeline.

However, you can use Clip Attributes to change which channels are assigned and/or muted within

the available tracks and channels you’ve edited into the Timeline. For example, if you’re editing clips

that have five channels of source audio (channels 1 and 2 are a stereo mix and channels 3 through 5

are three different microphones), you may have set your synced source clips to have one audio track

and five audio channels, with channels 3–5 muted. Later you have a few clips that would sound much

better if you only used channel 4, which is the isolated lavaliere microphone for that actor, so you can

select those clips and use the Audio panel of Clip Attributes to mute all channels but channel 4.

If, for whatever reason, you need to expose more audio tracks in the Timeline than you originally set

an audio clip to use, you can do the following.

To re-edit an audio clip to expose more audio tracks than were originally available:


Right-click the clip you want to change the audio track mapping of in the Timeline, and choose

Find in Media Pool from the contextual menu.


Right-click that clip in the Media Pool and choose Clip Attributes from the contextual menu.


Open the Audio panel of the Clip Attributes dialog, and choose how many audio tracks and audio

channels you want to set that clip up with. Click OK.


Once that’s done, edit the changed audio clip from the Media Pool to the Timeline to replace the

original clip using whichever method makes sense.

Displaying Waveforms in the Timeline

The Timeline View options palette lets you turn Audio Waveform display on and off via a button at

the top. The Audio View options let you define how you wish your waveforms to be presented on

the Timeline.

Audio View Options: Three buttons govern the look of audio waveforms in the Timeline, when visible.

�Non-Rectified Waveform: Lets you toggle between the waveform being drawn from the bottom of

the audio track up, or centered and mirrored about itself.

�Full Waveform: Hides the divider bar that keeps the waveform separate from the file name area of

each audio clip, so the waveform occupies the full space of each audio bar in the Timeline.

�Waveform Border: Draws a dark border around the edges of each waveform to make them

easier to see.

Video track height slider: Lets you resize the size of all video tracks at once, independently of the

audio tracks.

Audio track height slider: Lets you resize the size of all audio tracks at once, independently of the

video tracks.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

The Audio Waveform display option (circled in

red) in the Timeline View drop-down. Audio

View Options are (L-R) Non-Rectified Waveforms,

Full Waveform, and Waveform Border.

While a single averaged audio waveform representing all the channels in that clip is shown by default,

you can switch any clip to seeing each individual waveform in a vertical stack by right-clicking any

audio clip and choosing Display Individual Audio Channels.

Whenever you cut an audio clip, you cut all audio channels with it. Audio channels that are embedded

within a single track cannot be individually edited.

Enabling the display of multiple channel waveforms in the Timeline

Editing Audio In the Timeline

Using In and Out Points

Audio clips can be edited using all of the commands and tools available for video clips. However,

it’s good to know that one of the most common techniques of editing audio in other environments is

available in DaVinci Resolve, and that is the ability to identify a range of audio to cut, copy, or delete

using Timeline In and Out points, so that you can easily eliminate, move, or duplicate partial sections of

audio without having to use the Razor Edit or Split Clip commands.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

To delete a section of audio using In and Out points:


Set In and Out points in the Timeline to identify the range of audio you want to eliminate. If

necessary, turn off the Auto Select controls of tracks to omit overlapping audio clips you don’t

want to delete from this operation.


Press the Backspace key to delete the section of audio and leave a gap, or press the Forward

Delete key to delete the section of audio and ripple the Timeline to close the gap.

Setting In and Out points to identify

a range of audio to delete

Deleting the audio using the

Backspace key to leave a gap

To copy a section of audio using In and Out points:


Set In and Out points in the Timeline to identify the range of audio you want to copy.

If necessary, turn off the Auto Select controls of tracks with overlapping audio you don’t want to

copy; you can Option-click the Auto Select control of the audio track you’re copying from to solo it,

and you can Shift-click any video track’s Auto Select control to turn them all off. In this example,

we’re copying some background ambience to continue building an ambience track.

Setting In and Out points to identify a range of audio to copy


Press Command-C to copy that section of audio.


Press Option-X to clear the Timeline In and Out points, and move the playhead to where you want

to paste the copied section of audio.


Press Command-V to paste the copied audio. If you’re looping a section of audio, you can paste

many times to loop what you’ve copied.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Pasting the background ambience several times to loop it

Resizing Audio Clips in

Subframe Increments

DaVinci Resolve lets you optionally make subframe audio adjustments to the In and Out points of

audio clips in the Timeline.

Enabling and Disabling Subframe Editing

The “Align audio edits to frame boundaries” preference in the Editing panel of the DaVinci Resolve

User Preferences lets you choose whether audio clip In and Out points align to whole frame

boundaries, just like video clips. When this option is turned on, you cannot make subframe audio edits.

When turned off (the default), you can.

Subframe Editing of In and Out Points

While you cannot move the playhead in subframe increments, you can resize audio clips in

subframe increments by dragging an audio clip’s In or Out point in the Timeline, or by dragging

an audio edit to perform a roll. This can be useful for trimming minute bits of audio such as pops,

clicks, or vocalizations.

Resizing the Out point of an audio item in subframe

increments, seen within a one-frame playhead shadow

Know that if you have Linked Selection turned on and you’re trying to resize a selected Video+Audio

pair of items, the whole-frame resizing required for video prevents you from being able to resize the

audio separately. This is easily solved by Option-Clicking to select the linked audio item by itself, at

which point you can subframe resize it freely.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Also, if snapping is enabled, it may be impossible to make a subframe adjustment if you’re too close to

another edit point, a marker, or the playhead. In this case, pressing the N key to turn snapping off will

solve the problem.