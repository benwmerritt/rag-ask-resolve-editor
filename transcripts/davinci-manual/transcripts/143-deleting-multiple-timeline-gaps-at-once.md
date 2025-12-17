---
title: "Deleting Multiple Timeline Gaps at Once"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 143
---

# Deleting Multiple Timeline Gaps at Once

You can also ripple-delete video and audio gaps in the Timeline all at once using the Edit > Delete

Gaps command. This removes gaps among consecutive clips in the Timeline on all Auto Select

enabled tracks. Each segment of the Timeline with a gap is rippled, in order to move clips that are to

the right of each gap left to close that gap.

All gaps are defined for purposes of this command as empty spaces between clips that span all tracks

in the Timeline. In the following example, various audio/video, audio-only, and video-only clips have

gaps between them. Using Remove Gaps causes the Timeline to be rippled such that these clips abut

one another as a continuous sequence, without any of them overlapping any others.

(Top) Before removing gaps, (Bottom) After removing gaps


Edit | Chapter 36 Editing Basics

EDIT

This is an extremely powerful and wide-ranging command. However, it’s made safer by following strict

rules in order to maintain overall A/V sync in timelines:

�Gaps will not be removed past the point where video and/or audio clips will overlap one another.

�Gaps will not be removed if they’re under superimposed video clips that bridge the gap.

�Gaps will not be removed if one or more continuous audio clips bridge the gap.

�You can limit the range of the gaps to be deleted by setting In/Out points on the Timeline.

�If a linked set of video and audio items has a gap that includes an L or J split edit, it will be closed

to the point that the audio or video, whichever extends the farthest, abuts the nearest clip to it.

Disabling a track’s Auto Select Control omits that track from consideration when following the

above rules. This lets gaps on other tracks be closed so clips overlap those on the Auto Select-

disabled track.

WARNING: Performing Remove Gaps with Auto Select disabled on one or more tracks could

result in massive loss of video/audio sync if you’re not careful. To avoid this, Shift-click one

video Auto Select control (or press Option-F9) and one audio Auto Select control (or press

Command‑Option-F9) to toggle all video and all audio Auto Select controls until they’re all

turned on at once.

Audio/Video Linking

DaVinci Resolve gives you complete control over the linked relationship between the video and audio

associated with a clip. By default, DaVinci Resolve tries its best to keep the video and audio of clips

and timelines in sync. However, there are several ways you can suspend automatic syncing when you

need to make a specific kind of edit.

Controlling Linked Selection

While selecting edits and clips, you can also choose whether the video and audio associated with a

clip should be selected together (linked) or not. This determines whether operations performed to

the video of a clip automatically affect the audio of the clip, and vice versa. In most instances, you’ll

probably want to leave Linked Selection turned on, so that selecting the video of a clip to move it

elsewhere in the Timeline also results in the audio being selected and moved at the same time.

Disabling A/V linking in this case could cause your video and audio to go out of sync undesirably.

However, there are plenty of instances when you’ll want to temporarily suspend this linked A/V

relationship, such as when you want to create a split edit, where a clip’s audio In point is at a different

frame than the video In point. In this case, you can suspend Linked Selection to select just the audio In

point, then roll it either farther back or forward to create the split, without changing the In point of that

clip’s video. When you’re finished, you can re-enable A/V linking.

At all times, the state of Linked Selection is visible via the Chain-link button at the right of the toolbar.

The Link Audio/Video button


Edit | Chapter 36 Editing Basics

EDIT

To turn Linked Selection off and on:

�Click the Link Audio/Video button (or press Shift-Command-L).

To temporarily suspend Linked Selection while making a selection:

�Press the Option key while clicking a clip or edit point to select the video without selecting the

audio, or vice versa.

Linked Move Across Tracks

The Timeline > Linked Move Across Tracks setting works in conjunction with Linked Selection to let

you change how linked video and audio items move in the Timeline when you drag them up and down

to reorganize clips from track to track. Depending on the task at hand, one or the other behaviors

might be more convenient, but no matter how you have this mode set, video/audio sync is always

maintained when you move clips left and right.

�When Linked Move Across Tracks is enabled: (On by default) Dragging one of a linked pair of

video and audio items up or down in the Timeline moves the linked item up or down as well.

So, moving a video clip from track V1 to V2 results in its linked audio clip moving from track

A1 to A2 as well.

Before and after with Linked Move

Across Tracks enabled; if video

clip is moved, the linked audio

clip moves simultaneously

�When Linked Move Across Tracks is disabled: Dragging one of a linked pair of video and audio

items up or down to another track in the Timeline only moves that one item, other linked item(s)

remain in the same track. So, moving a video clip from track V1 to V2 leaves the audio clip in track

A1, where it was originally. This makes it easy to reorganize video clips into different tracks while

leaving your audio clips organized the way they were, or vice versa. Keep in mind that in this

mode, while you can move one item of a linked pair up and down freely, moving that item left or

right results in all linked items moving by the same amount, so sync is maintained.


Edit | Chapter 36 Editing Basics

EDIT

Before and after with Linked

Move Across Tracks disabled;

if the video clip is moved, the

linked audio clip remains in its

original position or vice versa

Dealing with Audio Video Sync Offsets

Audio/video sync is one of the most important things to maintain in any edited program. However,

there are times when you may want to override the sync relationship of a clip’s audio and video to

make a particular edit, so moving a clip’s audio and video out of sync is allowed.

If you disable Linked Selection and then move the audio or video of a clip independently of its linked

video or audio counterpart, you’ll see red “out-of-sync” indicators at the left of each clip’s name bar,

that displays the timecode offset by which the audio and video of that clip are out of sync. In the

following example, the audio and video of a clip have been moved out of sync by Option-clicking the

video and dragging it to the left.

Sync markers on a clip with audio and video out of sync

If you’ve moved the audio and video of a clip out of sync with one another, there’s a really easy

way of getting them back into sync, by right-clicking the red out-of-sync indicator of any clip and

choosing one of the available commands:

�Slip into place: Slips the content of the selected clip, without moving the clip, so that it’s in sync

with the other items that are linked to that clip.

�Move into place: Moves the selected clip so that it’s in sync with the other items that are

linked to that clip.

�Slip others into place: Slips the content of all other items that are linked to the selected clip,

without moving them, so that all linked items are in sync.


Edit | Chapter 36 Editing Basics

EDIT

�Move others into place: Moves all other items that are linked to the selected clip so

that all linked items are in sync.

Commands in the

contextual menu

of sync tooltips

Manually Unlinking and Relinking Audio and Video

By default, clips that you import into DaVinci Resolve have their video and audio linked together,

which makes it easy to maintain the relationship and sync of the audio and video components of a

clip while you’re editing. However, there are many reasons you might want to override this automatic

relationship, either breaking the A/V linking of a clip’s audio and video completely, or breaking it and

relinking in a different way, or to different clips.

Methods of permanently changing audio/video linking in the Timeline:

�To unlink audio and video from one another: Select a clip, then right-click it and choose Link from

the contextual menu (or press Option-Command-L). Unlinked clips do not appear with a chain icon

before the clip name in the Timeline.

�To link audio and video clips to one another: Command-click an audio clip and a video

clip so they’re both selected, then right-click the selected clips and choose Link from the

contextual menu (or press Option-Command-L). A chain icon appears before the name of linked

clips in the Timeline.

(Left) linked video and

audio with a chain icon to

the left of the clip name,

(Right) unlinked audio and

video items have no icon.

Linking Multiple Clips in the Timeline

You don’t just have to link audio and video clips that sync together, though. You can actually link any

number of video and audio clips that you want to be able to select, move, and edit together as one,

even if they were never originally meant to be synced. This makes linking an organizational mechanism

as much as a sync management tool.

Here are some examples of how you can use this:

�You can link a text generator with a subtitle to the clip it plays along with.

�You can link a sandwich of overlapping audio sound effects with the video clip they accompany.

�You can link off camera audio to an on camera shot.

�You can link the background and foreground clips of a green screen composite,

with sound from both.


Edit | Chapter 36 Editing Basics

EDIT

Linking multiple clips in the Timeline works the same as linking a single audio and video clip together;

every single linked item appears with a chain icon to the left of the clip name, and suspending linked

selection to force any single clip out of sync will result in the display of an “out-of-sync” indicator.

Multiple audio and video items that have been

manually linked together to act as a single clip in

the Timeline when Linked Selection is enabled