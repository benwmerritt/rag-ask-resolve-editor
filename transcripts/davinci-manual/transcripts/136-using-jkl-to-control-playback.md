---
title: "Using JKL to Control Playback"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 136
---

# Using JKL to Control Playback

The JKL keyboard shortcuts are common to many editing applications, and experienced editors know

these to be some of the most useful controls for playback and editing there are. Here’s a list of the

many different ways you can use these three keyboard shortcuts to play through clips and timelines

as you work.

J

Plays 100% backward

K

Stops playback

L

Plays 100% forward

Press J repeatedly

Increases backward play speed each time you press J,

for a range of fast-reverse speeds

Press L repeatedly

Increases forward play speed each time you press L,

for a range of fast-forward speeds

Shift-J

Plays in fast reverse

Shift-L

Plays in fast forward


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

Shift-K

Play Slow at 1/2, 1/4 or 1/8 speeds

Press and hold K+J

Plays backward at slow motion (with slow motion

audio playback)

Press and hold K+L

Plays forward at slow motion (with pitch-corrected audio

playback on macOS)

Pressing K while tapping J

Moves the playhead back one frame

Pressing K while tapping L

Moves the playhead forward one frame

Command-J and Command-L

Holding the Command key down while using the J and

L keyboard shortcuts lets you dynamically resize or trim

selected edit points or clips at 100 percent or faster speed,

depending on whether the Selection or Trim tool is enabled.

For more information on dynamic trimming,

see Chapter 44, “Trimming.”

When you’re playing back at faster or slower than real-time speed using the JKL commands, a

speed indicator appears to the right of the frame per second indicator of the Viewer.

A speed indicator above the Viewer shows

that you’re playing at 4x speed

Once you learn all the different methods of JKL playback, they will probably become one of

the main ways you move the playhead around in DaVinci Resolve.

Special-Purpose Playback Commands

In addition to the standard transport controls, there are some additional playback controls, available

via keyboard shortcuts or the Playback menu, that let you perform different playback operations.

�Loop: Command-Forward Slash (/). Toggles looped playback off and on. While looped

playback is on, playback initiated with any of the following commands will loop automatically until

you stop playback.

�Play around selection: Forward Slash (/). This command works contextually depending on what’s

selected in the Timeline. Plays a section of the Timeline from x frames before to y frames after (a)

the playhead (if nothing’s selected), (b) the currently selected edit point, (c) the currently selected

clip, (d) the currently selected transition, (e) a selection of multiple clips. This command is useful for

previewing how the current selection plays within the context of the clips immediately surrounding

it. The pre-roll and post-roll time is customizable in the Editing panel of the User Preferences.

�Play around current frame: Plays a section of the Timeline from x frames before to y frames

after the current position of the playhead. This command is useful for previewing how edits play

within the context of the clips immediately surrounding them. The pre-roll and post-roll time is

customizable in the Editing panel of the User Preferences.

�Play around current clip: (no default key assigned). Plays a section of the Timeline from x frames

before to y frames after the current clip intersecting the position of the playhead. The pre-roll and

post-roll time is customizable in the Editing panel of the User Preferences.


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

�Play Around In: Option-Space. Plays a section of the Timeline from x frames before to y frames

after the current assigned In point, letting you preview the transition from one clip to the next. The

pre-roll and post-roll time is customizable in the Editing panel of the User Preferences.

�Play Around Out: Shift-Space. Plays a section of the Timeline from x frames before to y frames

after the current assigned Out point, letting you preview the transition from one clip to the next.

The pre-roll and post-roll time is customizable in the Editing panel of the User Preferences.

�Play In to Out: Option-Forward Slash (/). If you’ve marked a section of a clip or timeline with In and

Out points, this command lets you preview how it will play.

�Play to In: (no default key assigned). Initiates playback and stops at the current In point.

�Play to Out: Option-Command-Forward Slash (/). Initiates playback and stops at the

current Out point.

Optimized UI Layouts for Vertical Editing

Optimized layouts for vertical timelines and projects are supported in DaVinci Resolve. When a vertical

timeline or project is loaded, the UI automatically switches to a layout optimized for vertical viewers

on the Cut, Edit, and Color pages. Loading a normal landscape timeline or project then automatically

switches back to the original layout. No additional user intervention is needed.

You can change this behavior in Preferences > User > UI Settings > Use optimized UI layouts

for vertical video. Unchecking this box retains the normal horizontal layout, even for vertical

video timelines.

The UI now changes format to accommodate vertical video timelines automatically.


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

Option to “Stop and Go to Last Position”

Playback > Stop and Go to Last Position lets you set DaVinci Resolve to a mode where the playhead

returns to where playback began whenever you stop. This option is most useful when editing audio,

although it’s available any time. When using the JKL keys to navigate the Viewer in this mode, “K” will

pause the playhead in place, while the space bar (stop) will go to last position.

This option is also available when you right-click on the Stop button in the transport controls of any

viewer. A contextual menu appears where you can turn “Stop and go to last position” on or off as the

default behavior.

Enabling and Disabling Audio Scrubbing

Audio scrubbing is enabled by default, meaning that you’ll hear audio when dragging the playhead

with the mouse back and forth. While this can be useful when you’re searching for audio cues, it can

also be distracting if you’re just focused on the picture.

To enable or disable audio scrubbing:

�Choose Timeline > Audio Scrubbing (Shift-S).

Playback Post-Roll

Enables the playhead to continue playing past the last clip in the Timeline for a duration equal to the

“Post-roll time” Project Setting in the Editing panel. This is good for editors that want to experience

a few moments of playback after cutting or fading to black after the last frame of audio and video in

the Timeline.

To enable or disable Playback Post-Roll:

�Choose Timeline > Playback Post-Roll.

Source Tape in the

Edit Page Source Viewer

The Cut page’s Source Tape is also available in the Edit Page Source Viewer. To enable it, simply

select a bin and then click on the Source Tape icon in the upper right of the Source Viewer, or

press Shift-Q.

You can also edit using the Source Tape in the Edit page. To do so, click on

the Source Tape icon in the Source Viewer (circled red).


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

Using this option, every single clip in the currently open bin, and any subfolders in that bin, of

the Media Pool is shown in the Source Viewer as a “stringout” in the scroll area at the bottom of

the Viewer. In the scroll area, each clip appears one after the other in a long strip, with the order

determined by the sort order. This makes it easy to scrub through a whole collection of clips while

you’re figuring out what you want to use.

As you play through, whichever clip the playhead intersects is selected in the Media Pool, so you know

which clip you’re looking at, and you have the ability to set In and Out points for any clip in the Source Tape.

For watching and reviewing a large amount of footage, the Fast Review button is also now available in

the lower left of the Source Viewer. Pressing this button will automatically adjust to a faster playback

speed, depending on the length of the clip being viewed in the Source Tape.

Limiting the Source Tape Scope by Folder Structure

As your project grows, it can become unwieldy to constantly have an entire film’s worth of media in the

Source Tape. It is possible to limit the scope of the Source Tape at the bin level. By clicking directly on

bins in the Bin list, you can quickly broaden or narrow the scope of the Source Tape. If you click on a

bin named Scene02, the Source Tape will then zoom in to only show you clips in that folder. Clicking

back on Master will zoom out the Source Tape to show the clips in all folders again.

This is also useful when navigating bin structures that reflect the original camera file system. For

example, you may have a camera that records to each memory card as a separate folder, and then

each individual clip is saved as a separate folder inside that folder. When you bring this file system into

the Media Pool using the Create Bins option, these nested levels are mirrored in the Media Pool bin

structure. Now when you click on a card bin in the Source tape, it will directly show you all the clips on

that card, rather than show many individual sub-bins.

Moving the Playhead Using Timecode

You can use absolute or relative timecode entry to either move the playhead in both the Source and

Timeline Viewers, or to move or trim selected edit points or clips. When navigating the Timeline, timecode

entry lets you move the playhead very precisely, or jump to specific timecode values really quickly.

TIP: The method of timecode entry described here is used for many different commands that

require timecode entry and is designed for fast and efficient editing.

How to Enter Timecode Values

When entering timecode, type each pair of hour, minute, second, and frame values from left to right,

with a period representing a pair of zeros for fast entry. The numbers you enter appear in the timecode

field at the upper right-hand corner of the Viewer with focus. When you’re finished typing, press the

Enter key to execute the timecode command. The rules for timecode entry are as follows:

�The right-most pair of timecode values (or period) you enter is always the frame number.

�A period to the left or to the right of any number you type is considered to be a pair of zeroes.

�A single period between two numbers is considered to either be a single zero, or ignored if it’s

between two pairs of numbers.

�Any untyped pairs of values to the left of what you enter are assumed to be whatever those values

were prior to the timecode you entered; this makes it easy to type partial timecode values even

when the Timeline starts at hour one.

�It’s not necessary to enter colons or semicolons.


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

IMPORTANT: With full length keyboards, you can use the number pad for implicit timecode

entry without invoking the Go To Timecode action (=). When using a multicam or printer light

operation, any already mapped number pad key will continue to invoke actions like switching

angles or incrementing color values.

When using the number keys above the letters on a keyboard, you must first select Go To

Timecode (=), or click in the field you wish to change before entering a new value.