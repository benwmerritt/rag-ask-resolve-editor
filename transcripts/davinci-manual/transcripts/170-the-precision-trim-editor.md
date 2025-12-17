---
title: "The Precision Trim Editor"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 170
---

# The Precision Trim Editor

An enhanced trim mode similar to the Cut page’s precision trim editor is available in the Edit Page

viewer, allowing you to see a large display of frame changes on either side of your edit.

To access it, double-click an edit point, or choose “Trim Editor” from the Trim menu on the

selected edit point.

Trimming Edits in the Timeline Viewer

You can double-click any edit point between two clips in the timeline to open up the Trim Editor, which

provides a detailed method of adjusting both halves of an edit point. A graphical A/B roll interface

shows two filmstrips with the outgoing clip on top and the incoming clip on the bottom.


Edit | Chapter 44 Trimming

EDIT

These controls are draggable:

�Drag the left side of the top filmstrip’s handle to trim the Out point of the outgoing clip.

�Drag the right side of the bottom filmstrip’s handle to trim the In point of the incoming clip.

�Drag the white handle between the top and bottom filmstrips to roll the edit point, simultaneously

adjusting the outgoing and incoming edit points.

Numbers over each frame let you see exactly how many frames you’re trimming, while a pair of

buttons to the left and right of the transport controls in the Viewer toolbar let you adjust the outgoing

clip’s Out point and incoming clip’s In point in one frame increments.

The Viewer Trim Editor, seen when you double-click an edit in the timeline

Trim Tool Operations With the Keyboard

You can also perform every trim operation more precisely using the Nudge keyboard shortcuts.

To trim with the keyboard:


Press T to select the Trim tool.


To trim the selection, do one of the following:

To slide a clip: Press Shift-V to select a clip, and press the Comma key to slip it one frame to the

left, or the Period to slip it one frame to the right. Shift-Comma and Shift-Period slips the clip in

5-frame increments.

To slip a clip: Press Shift-V to select a clip, then press the S key to toggle to Slip mode (pressing

S again toggles back to Slide mode) and press Comma or Period to slide its contents to the left or

right. Shift-Comma and Shift-Period slides the contents in 5-frame increments.


Edit | Chapter 44 Trimming

EDIT

To roll an edit: Press V to select an edit point, then press the Comma key to nudge it one frame

to the left, or the Period to nudge it one frame to the right. Shift-Comma and Shift-Period rolls the

edit in 5-frame increments.

To ripple an edit: Press V to select an edit point, then press U to select either the incoming or

outgoing side of the edit by itself. Then, press the Comma key to ripple the selected In or Out

point of the clip to the left, or the Period to ripple it one frame to the right. Shift-Comma and Shift-

Period ripples in 5-frame increments.


If you want to suspend the 2- or 4-up display that appears in the Timeline Viewer while trimming,

you can Choose View > Enable Multiview Edit Preview to toggle the trimming displays off and on.

TIP: When holding down the Shift key while nudging to do a “fast nudge,” the duration of the

nudge is customizable in the Editing panel of the User Preferences. By default it’s five frames,

but you can set it to whatever you want.

Important Trimming Keyboard Shortcuts

When trimming using the keyboard, the following keyboard shortcuts are important for you to

remember. Most of these commands, and many more that haven’t been assigned to keyboard

shortcuts, can also be found in the Trim menu. You can remap many of these commands to different

keyboard shortcuts using the Keyboard Mapping panel of the User Preferences. For more information,

see Chapter 4, “System and User Preferences.”

Key Shortcut

Function

T

Trim mode, ripples edits and slips or slides clips.

A

Selection mode, resizes edits and moves clips.

Command-L and J

Fast trim commands, lets you dynamically trim the selection at 100%

forward and reverse speeds.

W

Dynamic trim or resize mode, uses JKL to trim the selection.

S

Toggles between Slip and Slide mode when a clip is selected in

Trim mode.

V

Selects the edit point closest to the playhead, and moves the

playhead there.

Shift-V

Selects the clip or gap that intersects the playhead. If there are

superimposed clips, turn off the Auto Select controls of tracks

containing clips you don’t want to select.

Shift

A modifier that temporarily disables the 2- and 4-up display that

appears when trimming edits and clips with either the pointer or

keyboard shortcuts.

Option-F1 through F9

Toggles Auto Select for video tracks 1 through 9, making it possible

to restrict certain selection and trim operations performed with

the keyboard.

Command-Option F1

through F9

Toggles Auto Select for audio tracks 1 through 9, making it possible

to restrict certain selection and trim operations performed with

the keyboard.


Edit | Chapter 44 Trimming

EDIT

Key Shortcut

Function

U

Toggles the currently selected edit point among the outgoing, centered,

or incoming part of the edit.

Option-U

Toggles the currently selected edit point or clip among Video+Audio,

Video Only, or Audio Only.

Comma (,)

After you’ve made a selection, nudges selected edits or clips one frame

to the left. Shift-Comma nudges 5 frames (the duration is customizable

in the Editing panel of the User Preferences).

Period (.)

After you’ve made a selection, nudges selected edits or clips one frame

to the right. Shift-Period nudges 5 frames (the duration is customizable

in the Editing panel of the User Preferences).

Forward-Slash (/)

This command works contextually depending on what’s selected in

the Timeline. Plays a section of the Timeline from x frames before to

y frames after (a) the playhead (if nothing’s selected), (b) the currently

selected edit point, (c) the currently selected clip, (d) a selection of

multiple clips. This command is useful for previewing how the current

selection plays within the context of the clips immediately surrounding

it. The pre-roll and post-roll time is customizable in the Editing panel of

the User Preferences.

Command-/

Toggles looped playback off and on.

Down Arrow, Up Arrow

Moves both the playhead and selection state to the next or previous

edit point. If multiple clips or edits are superimposed, the first clip on the

lowest numbered track will be selected first, then the next clip up, and

so on until the topmost superimposed clip is selected, before selecting

the next clip in the Timeline.

E

Extend edit. Resizes or ripples selected edit points to the current

position of the playhead.

Shift-[

Trim Start. Resizes (Selection) or ripples (Trim) the In point of all clips on

auto-select-enabled tracks that intersect the playhead to the position of

the playhead.

Shift-]

Trim End. Resizes (Selection) or ripples (Trim) the Out point of all clips on

auto-select-enabled tracks that intersect the playhead to the position of

the playhead.

Shift-Command-[

Ripple Trim Start. Regardless of whether Selection or Trim mode is

enabled, always ripples the In point of clips on auto-select-enabled

tracks that intersect the playhead to the position of the playhead.

Shift-Command-]

Ripple Trim End. Regardless of whether Selection or Trim mode is

enabled, always ripples the Out point of clips on auto-select-enabled

tracks that intersect the playhead to the position of the playhead.

IMPORTANT: While the Slip, Roll, and Slide tools will change the sync relationship of the

clips you’re adjusting with a matching soundtrack, the rest of the Timeline won’t be affected.

Using Ripple can alter the overall sync relationship of large portions of your timeline and its

matching soundtrack, so you should use it with extreme care.


Edit | Chapter 44 Trimming

EDIT

Trimming Using Timecode Entry

You can also use absolute or relative timecode entry to trim clips and edits. What is trimmed

depends on the selection you’ve made prior to entering timecode. If you want to use timecode to

trim the selection forward relative to its current position, be sure to type an equal sign or plus (= or

+) before the timecode value; to trim the selection backward relatively, type minus (–) before the

timecode value.

�To roll an edit: Select the center of an edit point, enter a timecode value, and press Return.

�To ripple an edit: Select either the outgoing or incoming half of an edit point, enter a timecode

value, and press Return.

�To slip a clip: Select a clip, and press S if necessary to switch to Slip mode, enter a timecode

value, and press Return.

�To slide a clip: Select a clip, and press S if necessary to toggle to Slide mode, enter a timecode

value, and press Return.

How to Enter Timecode Values

When entering timecode, type each pair of hour, minute, second, and frame values from left to right,

with a period representing a pair of zeros for fast entry. The numbers you enter appear in the timecode

field at the upper right-hand corner of the Viewer with focus. When you’re finished typing, press the

Enter key to execute the timecode command. The rules for timecode entry are as follows:

�The right-most pair of timecode values (or period) you enter is always the frame number.

�A period to the left or to the right of any number you type is considered to be a pair of zeroes.

�A single period between two numbers is considered to either be a single zero or ignored if it’s

between two pairs of numbers.

�Any untyped pairs of values to the left of what you enter are assumed to be whatever those values

were prior to the timecode you entered; this makes it easy to type partial timecode values even

when the Timeline starts at hour one.

�It’s not necessary to enter colons or semicolons.

IMPORTANT: With full length keyboards, you can use the number pad for implicit timecode

entry without invoking the Go To Timecode action (=). When using a multicam or printer light

operation, any already mapped number pad key will continue to invoke actions like switching

angles or incrementing color values.

When using the number keys above the letters on a keyboard, you must first select Go To

Timecode (=) or click in the field you wish to change before entering a new value.

Absolute timecode is entered simply by typing in a timecode value. So long as no clips or edit points

are selected when you press the Return key, the playhead will move to that timecode value. If an

edit point or clip is selected, those will be moved or trimmed to the corresponding timecode value,

if possible.


Edit | Chapter 44 Trimming

EDIT

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

115..

01:15:00:00

01:10:10:10

23...

23:00:00:00

Relative timecode is entered by starting the timecode value with a plus (+) or minus (–). Adding a plus

results in the value you type being added to the current timecode value for purposes of offsetting

the playhead or moving a selection. Adding a minus will subtract the value you type from the current

timecode value.

Here are two examples of relative timecode entry:

+20.

00:00:20:00 is added to the current timecode value.

-5

00:00:00:05 is subtracted from the current timecode value.