---
title: "Enabling and Disabling Clips and Tracks"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 149
---

# Enabling and Disabling Clips and Tracks

As you work in the Timeline, you’ll find there are times when you want to disable clips that you don’t

want to appear during playback, without actually removing them from the edit. For example, you may

decide to disable superimposed clips that are positioned as insert shots in the middle of a scene

because of a client’s notes, but you don’t want to eliminate the clips because they might change

their minds.

A disabled clip oµn track V2


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

In another example, you’ve edited a series of titles on track V3, so you need to disable track V3 in its

entirety to output a textless version of the movie as a deliverable.

When a clip or track is disabled, clips within it appear dimmed, and these disabled clips don’t appear

in the Color page, and aren’t output to tape or rendered to disk in the Deliver page until that track is

re-enabled first.

Track V3 is disabled, making the Timeline textless as a result

To disable/enable one or more clips in the Timeline:

�Select one or more clips, then right-click the selection and check or uncheck Enable Clip in the

contextual menu, or press D to toggle a clip’s enabled state.

To disable/enable an entire track:

�Click the track enable button.

You can change multiple Track Header controls in the Edit page (Lock Track, Visibility, Auto

Track Selection, etc.) by simply clicking on an icon and dragging your pointer up or down

across the track headers. You can do this for one type of control at a time and not across

Audio and Video tracks.

Clicking on the Lock icon on A1, then

dragging the pointer down to A3,

will lock all audio tracks in between.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

Copying and Pasting Clips in the Timeline

Clips can be cut, copied, and pasted in a variety of ways using standard keyboard shortcuts. You can

cut or copy one clip or a selection of several, and you can also choose to copy or cut just the video or

audio media of a clip. When pasting, you can paste to the same timeline, or to a different timeline if you

want to move media from one to another.

Methods of doing simple cut, copy, and paste:

�To cut one or more clips, leaving a gap: Make a selection, and choose Edit > Cut (Command-X).

The selected clip or clips are removed from the Timeline and stored in memory for pasting.

�To ripple cut one or more clips and ripple the Timeline to close the gap: Make a selection, and

choose Edit > Ripple Cut (Command-Shift-X). The selected clip or clips are removed from the

Timeline and stored in memory for pasting. All clips on tracks with Auto Select enabled will be

rippled to the left to fill the gap left by the cut clips.

�To copy one or more clips: Make a selection, and choose Edit > Copy (Command-C). The selected

clip or clips are left in the Timeline, but copies are stored in memory for pasting.

�To paste one or more clips to the same track: Move the playhead to the frame where you want

the pasted selection to start, and then choose Edit > Paste (Command-V). By default, each copied

clip is pasted onto the same track it was copied from.

�Pasted clips will be added at the Playhead position.

�Pasted clips overwrite any clips in that track that are in the way.

�Pasted clips are automatically selected, ready for nudging left or right, or for other operations.

�To paste one or more clips to a different track: Pasting clips to a different track requires a slightly

different procedure. Move the playhead to the frame where you want the pasted selection to start,

then either Option-click any empty area on the track you want to paste the clip(s) to or Option-click

the Auto Select control of that track to solo that track, and then choose Edit > Paste (Command-V).

�Pasted clips will be added at the Playhead position.

�Pasted clips overwrite any clips in that track that are in the way.

�Pasted clips are automatically selected, ready for nudging left or right, or for other operations.

Paste Insert

Another paste command, Edit > Paste Insert (Command-Shift-V), lets you paste clips that you cut

or copied via an insert edit, so that an edit is added at the position of the playhead to clips that are

already in the Timeline, and all media to the right of the playhead is rippled farther right to make room

for the clip or clips being pasted. As with all other ripple edits, only clips on tracks with their Auto

Select control turned on are affected. Pasted clips are automatically selected, ready for nudging left or

right, or for other operations.

Cut/Copy/Paste of Partial Clip

Segments Using In and Out Points

By default, pasted clips will be added at the playhead position. You can use the Timeline’s In and Out

points to cut and copy partial segments of longer clips in various ways. This is a valuable technique for

doing in-depth audio and dialog editing, although it’s useful for copying partial segments of any kind

of clip in the Timeline.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

IMPORTANT: In order to use In and Out points for pasting, you must first go to Preferences >

User > Editing, and check the box “Prioritize pasting to the in and out range.”

To cut or copy part of a clip to paste elsewhere:


Set In and Out points to isolate the part of the clip you want to cut or copy. You can use the Auto

Select controls to include or omit clip segments on specific tracks while you do this.


Press Command-X to cut or Command-C to copy that clip segment.


Clear the In and Out points by pressing Option-X. Otherwise, you’ll paste the clip segment right

back into the same place it started.


Move the playhead to the frame of the Timeline you want the pasted clip to start, and use the

Paste or Paste Insert commands to paste the clip segment there. Pasted clips are automatically

selected, ready for nudging left or right, or for other operations.

You can also use In and Out points to paste only a partial segment of a much longer clip that you’ve

cut or copied.

To paste only part of a clip:


Select a clip, and press Command-X to cut or Command-C to copy that clip.


Set In and Out points to identify the region of the Timeline you want to paste into.


Use the Paste or Paste Insert commands to paste only as much of the Cut or Copied clip as will fit

between the In and Out points you’ve placed. Pasted clips are automatically selected, ready for

nudging left or right, or for other operations.

Copying and Pasting Clips to a Different Track

If all Auto Select controls on all tracks are turned on, clips are always pasted back to the same track

they were copied from, starting at the position of the playhead. This is valuable for the many instances

where you’ll find yourself copying and pasting clips you want to repeat, especially when doing

audio editing.

However, if you want to paste the clips you cut or copied to a different track entirely, you need to use

the Auto Select controls to specify which track you want to paste to. Here are the rules:

�You can force paste what you copied to a specific track by Option-clicking that track’s Auto Select

control to solo it before pasting.

�When one or more Auto Select controls are disabled, then clips are pasted to the lowest-

numbered track with an enabled Auto Select control.

�If you’ve copied clips on multiple tracks, clips on the lowest copied track will be pasted to the

lowest Auto Select enabled track, and all other clips will be pasted to higher tracks, with new

tracks automatically created, if necessary.

�If Auto Select is disabled on every single track, then a new track will be created above all other

video tracks and/or below all other audio tracks, and the clip will be pasted into this new track,

which has Auto Select turned on.

Audio Channels When Copying and Pasting Audio Clips

Copying and pasting audio has one other consideration. If you’re force pasting a clip into a different

track, the track you solo the Auto Select control of could possibly be set to an audio channel mapping

that doesn’t match the clips you’re pasting there. An example of when this would happen is if you copy

stereo audio clips from a stereo track and paste them to a mono audio track.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

DaVinci Resolve allows you to do this, so you have the freedom of pasting audio clips to any track you

want to. However, extra audio channels within clips that exceed the number of channels supported by

the audio track they’re on will be muted. Fortunately, this situation is easy to rectify. Simply right-click

the track header of the problem audio track, and use the Change Track Type To submenu to change

its channel mapping to one more appropriate to the clips you’ve pasted into it.

Auto Align Clips

Auto Align Clips slides one or more selected clips to align with the timecode or audio waveforms of

another clip that has matching timecode or audio. This function works for video clips, which can be

aligned using timecode, and for audio clips, which can be aligned using either timecode or waveform

matching. Waveform matching can also be used if you’re working with audio/video clips.

You can only select one clip per video or audio track to align, and they all will align to whichever clip

is on the lowest-numbered video or audio track. Clips selected that have no overlapping timecode or

audio waveform will not be moved and left in their original position on the Timeline.

For example, clip A on track V1 overlaps with clip B on track V2, but not with clip C on track V3, or clip

D on track V4. Selecting all clips and using Auto Align Edits will slide clip B to align with clip A, but clips

C and D won’t be moved because they don’t overlap with clip A.

The original Timeline with clip A (blue) and clip B (orange) that have some overlapping audio but are out of sync

The same Timeline after the Auto Align command; clip B (orange) has been slipped to sync

via audio waveform with clip A (blue). Clips C (tan) and D (green) were also selected, but

because they had no overlapping timecode or audio, they remained in place.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

In another example, clip A on track V1 overlaps with clips B, C, and D on tracks V2, V3, and V4

respectively. Selecting all clips and using Auto Align Edits will slide clips B, C, and D to be aligned

with clip A.

The original Timeline with clip A (blue), and clip B (orange), C (tan),

and D (green) all have overlapping audio, but are out of sync.

The same timeline after the Auto Align command. All clips are now in sync and the audio waveforms now all

match. All the other clips moved to clip A’s (blue) position because it was the lowest clip on the Timeline.

To use Auto Align clips:


Arrange the clips you want to align with one another on the Timeline so that there’s one clip per

track. All clips will sync to the clip on the lowest track number. All clips must have overlapping

timecode or audio waveforms.


Select every clip that you want to align (only one per track).


Right-click one of the selected clips, and choose an option from the Auto Align Clips submenu,

either “Based on Timecode,” or “Based on Waveform.”

If Timecode is selected, the operation will be instant. If Waveform is used, a progress bar

will appear showing you how long it will take DaVinci Resolve to analyze the selected audio

waveforms before your clips are aligned. If you’ve selected clips that can’t be aligned, a

warning box will appear and tell you which clips had errors.

For video, this can be useful for multi-camera editing situations where you want to align an

insert with the action of an alternate angle. For audio, this is useful for situations where you

have multiple recordings of the same audio that you want to align for further editing.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

NOTE: Waveform matching won’t work for re-recorded audio, such as dialog that’s been

re-recorded using the ADR tools of the Fairlight page, as the correspondence between two

waveforms must be precise for a match to be found.