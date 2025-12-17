---
title: "Chapter 172"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 675
---

# Chapter 172

Transport Controls,

Timeline Navigation,

and Markers

The Fairlight page has unique transport control, zooming, and scrolling options

not found in the other pages of DaVinci Resolve that help you to work with audio

more efficiently.

This chapter covers how to navigate around the Fairlight version of the Timeline.

Contents

Transport Controls and JKL Navigation��������������������������������������������������������������������������������������������������������������������������������� 3744

Transport Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3744

Using JKL to Control Playback����������������������������������������������������������������������������������������������������������������������������������������������������� 3744

Dragging the Playhead to Scrub������������������������������������������������������������������������������������������������������������������������������������������������� 3745

Looping Playback������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3745

Loop Jog Scrubbing�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3745

Moving the Playhead Using Timecode������������������������������������������������������������������������������������������������������������������������������������ 3746

Clip, Marker, and Track Navigation������������������������������������������������������������������������������������������������������������������������������������������� 3747

Selecting Tracks���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3747

Moving the Clip Selection��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3748

Moving the Track Selection����������������������������������������������������������������������������������������������������������������������������������������������������������� 3748

Zooming and Scrolling��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3748

Setting the Zoom Level of the Timeline����������������������������������������������������������������������������������������������������������������������������������� 3749

Scrolling Through the Timeline���������������������������������������������������������������������������������������������������������������������������������������������������� 3749

Using Flags������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3750

Using Markers������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3750

Adding Markers to Clips������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3751

Adding Markers to Timelines��������������������������������������������������������������������������������������������������������������������������������������������������������� 3751


Fairlight | Chapter 172 Transport Controls, Timeline Navigation, and Markers

FAIRLIGHT

Transport Controls and JKL Navigation

Because of the Fairlight page’s audio-focused workflow, the transport and playback controls differ

from those found in the Media, Edit, Color, and Deliver pages.

Transport Controls

Fairlight page transport controls

The Fairlight transport controls are also designed to mirror their counterparts on the Fairlight control

panels. They include the following functions:

Rewind and Fast Forward: Initiates accelerated playback through the Timeline in either

direction. Pressing either of these buttons multiple times speeds up this motion, cycling

through 8x, 24x, 60x, 150x, and 360x play speeds.

Play: Plays forward. Identical to pressing the Spacebar or L keys while playback is stopped.

Stop: Stops playback. Identical to pressing the Spacebar or K keys while playback is engaged.

Record: Initiates recording if you have an audio source patched to a track, and if that track is

enabled for recording. For more information about recording, see Chapter 173, “Recording.”

Loop: Toggles looped playback off and on. While looped playback is on, playback will loop at

the end of the Timeline, and will also loop when you use the Play In to Out command, and will

continue to loop automatically until you stop playback.

Automation controls: This button exposes the automation toolbar.

For more information about recording automation, see Chapter 178, “Mix Automation.”

Using JKL to Control Playback

The JKL keyboard shortcuts are common to many editing applications, and experienced editors know

these to be some of the most useful controls for playback and editing there are. Here’s a list of the

many different ways you can use these three keyboard shortcuts to play through clips and timelines

as you work.

J

Plays 100% backward.

K

Stops playback.

L

Plays 100% forward.

Press J repeatedly

Increases backward play speed each time you press J,

for a range of fast-reverse speeds.

Press L repeatedly

Increases forward play speed each time you press L,

for a range of fast-forward speeds.


Fairlight | Chapter 172 Transport Controls, Timeline Navigation, and Markers

FAIRLIGHT

Shift-J

Plays in fast reverse.

Shift-L

Plays in fast forward.

K+J

Plays backward at slow motion (with slow motion audio playback).

K+L

Plays forward at slow motion

(with pitch-corrected audio playback on OS X).

Pressing K while tapping J

Moves the playhead back one frame.

Pressing K while tapping L

Moves the playhead forward one frame.

If you’re using Fairlight with the keyboard, then this will probably become one of the main ways you

move the playhead around in DaVinci Resolve.

NOTE: All of the keyboard commands listed in this document are based on the

DaVinci Resolve keyboard customization preset. There is great power in the remapping of

keyboard commands to systems that may be more familiar to you like Premiere Pro or Pro

Tools. However, if their keyboard command set does not offer the same commands as the

DaVinci Resolve keyboard commands, they won’t work the same. For instance, the Pro Tools

keyboard preset does not support J-K-L timeline navigation.

Dragging the Playhead to Scrub

You can also drag the playhead left and right to scrub through the visible area of the Timeline by

clicking and dragging anywhere within the Timeline ruler at the top of the Timeline, directly below the

toolbar. If you’re zoomed in at a reasonable level for editing, scrubbing the playhead using your pointer

will result in smooth, tape-like slow and fast audio playback, giving you a great deal of precision while

trimming audio.

Looping Playback

Two controls govern looping on the Fairlight page, similarly to how looping works on the Edit page.

Loop: Command-Forward Slash (/). Toggles looped playback off and on. While looped

playback is on, playback initiated with any of the following commands will loop automatically

until you stop playback.

Play In to Out: Option-Forward Slash (/). If you’ve marked a section of a clip or timeline with In

and Out points, this command lets you preview how it will play.

Loop Jog Scrubbing

Currently available only on the Fairlight page, choosing Timeline > Loop Jog enables a brief sample

preview to be heard while scrubbing the playhead through the Timeline. This can make it easier to

recognize bits of dialog or music as you’re quickly scrubbing through tracks, in situations where you’re

trying to locate specific lines or music cues. It also enables this brief sample preview to loop endlessly

when you hold the playhead on a frame, so you can pause while scrubbing and hear (by default) the

current 80 ms prior to the playhead as it loops.


Fairlight | Chapter 172 Transport Controls, Timeline Navigation, and Markers

FAIRLIGHT

A pair of settings in the User Preferences let you customize this behavior.

Loop Jog Alignment: Three options let you choose whether you loop audio Pre the position

of the playhead, Centered on the playhead, or Post the position of the playhead.

Loop Jog Width: A field lets you choose how many milliseconds of audio to loop when Loop

Jog is enabled. How many milliseconds of audio corresponds to one frame depends on the

frame rate of the video. For example, at a frame rate of 25 fps, there are 1000/25 = 40 ms per

frame, so the default value of 80 ms equals two frames of looping.

Moving the Playhead Using Timecode

You can use absolute or relative timecode entry to move the playhead in the Timeline. Timecode entry

lets you move the playhead very precisely or jump to specific timecode values really quickly.

How to Enter Timecode Values

When entering timecode, type each pair of hour, minute, second, and frame values from left to

right, with a period representing a pair of zeros for fast entry. The numbers you enter appear in the

Timecode field at the upper right-hand corner of the Viewer with focus. When you’re finished typing,

press the Enter key to execute the timecode command. The rules for timecode entry are as follows:

�The right-most pair of timecode values (or period) you enter is always the frame number.

�A period to the left or to the right of any number you type is considered to be a pair of zeroes.

�A single period between two numbers is considered to either be a single zero or ignored if it’s

between two pairs of numbers.

�Any untyped pairs of values to the left of what you enter are assumed to be whatever those values

were prior to the timecode you entered; this makes it easy to type partial timecode values even

when the Timeline starts at hour one.

�It’s not necessary to enter colons or semicolons.

IMPORTANT: With full length keyboards, you can use the number pad for implicit timecode

entry without invoking the Go To Timecode action (=). When using a multicam or printer light

operation, any already mapped number pad key will continue to invoke actions like switching

angles or incrementing color values.

When using the number keys above the letters on a keyboard, you must first select Go To

Timecode (=), or click in the field you wish to change before entering a new value.

Absolute Timecode Entry

Absolute timecode is entered simply by typing the timecode value you want to move the playhead to,

and when you press the Return key, the playhead will move to that timecode value.


Fairlight | Chapter 172 Transport Controls, Timeline Navigation, and Markers

FAIRLIGHT

Here are some examples of absolute timecode entry using this method:

Original TC Value

User-Typed Value

New TC Value

01:10:10:10


15:24:52:18

01:10:10:10

2..

01:02:00:00

01:10:10:10


01:10:10:15

01:10:10:10


01:10:10:12

01:10:10:10

1.2

01:10:01:02

01:10:10:10

1115..

11:15:00:00

01:10:10:10

23...

23:00:00:00

Relative Timecode Entry

Relative timecode is entered by starting the timecode value with a plus (+) or minus (–). Adding a plus

results in the value you type being added to the current timecode value for purposes of offsetting the

playhead from its current position. Adding a minus will subtract the value you type from the current

timecode value. Here are three examples of relative timecode entry:

User-Typed Value

Result

+20.

00:00:20:00 is added to the current timecode value.

+3..

00:03:00:00 is added to the current timecode value.

–5

00:00:00:05 is subtracted from the current timecode value.

Clip, Marker, and Track Navigation

The Up and Down Arrow keys are used to move the playhead from one edit point to the next in the

Fairlight page Timeline, just as in the Edit page Timeline.

However, holding Command-Option down while using the Arrow keys gives you Fairlight page-

specific behaviors that are used to navigate among clips, markers, and tracks in the Fairlight page in a

way that’s different than other pages of DaVinci Resolve but very useful to the way the Fairlight page

operates. This section covers the basics.

Selecting Tracks

Which tracks are selected determine the behavior of the Arrow keys.

�In Pointer mode: You can select tracks by clicking or Command-clicking (to select multiple tracks)

anywhere in the background area or on the track number of the track headers. If you click and

drag in the track header, you can use a bounding box to select multiple tracks. Pointer mode will

not select in unused areas of the Timeline.

�In Range or Focus mode: You can select tracks by clicking or Command-clicking anywhere

either in the background area or on the track number of the track header, or in any unused

area of the track itself in the Timeline. If you click and drag, you can use a bounding box to

select multiple tracks.


Fairlight | Chapter 172 Transport Controls, Timeline Navigation, and Markers

FAIRLIGHT