---
title: "Selecting Edits in the Timeline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 141
---

# Selecting Edits in the Timeline

A variety of editing and trimming methods require you to select an edit point, or part of an edit point, in

order to resize, ripple, or roll an edit. You can do so using the mouse or using the keyboard.

Methods for selecting edit points using the mouse:

�To select an edit to roll: Move the mouse to the center of an edit point, and when the ripple cursor

appears, click to select the edit.

Selecting an edit point to roll

�To select just the incoming or outgoing half of an edit point to resize or ripple: Move the mouse

to the left or right of the center of an edit, and when the resize/ripple cursor appears, click to

select that portion of the edit.

Selecting incoming or outgoing

halves of an edit point to resize or ripple


Edit | Chapter 36 Editing Basics

EDIT

To select multiple edit points, do one of the following:

�To select multiple roll points: Command-click the center of multiple edit points. Command-click a

selected edit point to deselect it.

Command-clicking the center of several edits to prepare to roll them all

�To select multiple ripple points: Command-click the left or right sides of multiple edit points.

Command-clicking the left or right of several edits to ripple them all

�To drag to select many edit points: Select the Trim tool (T), and drag a bounding-box over the

edit points you want to select. You can press U to switch all selected edit points among rippling

incoming edits, rippling outgoing edits, and rolling edits.

Using the Trim tool, you can drag a bounding box to select multiple edits

There is also a flexible set of keyboard shortcuts that makes it easy to select edit points in

preparation for various operations if you like to avoid using the mouse.

Keyboard shortcuts for selecting edits:

V: Selects the nearest edit point to the playhead on the lowest track with Auto Select enabled.

Selects both the audio and video edit points of a clip together.

Option-E: Selects the nearest video edit point to the playhead on the lowest track with Auto

Select enabled. Linked audio edit points are not selected.

Shift-E: Selects the nearest audio edit point to the playhead on the lowest track with Auto

Select enabled. Linked video edit points are not selected.

U: Once you’ve selected an edit point, this shortcut toggles among selecting the outgoing

half, incoming half, or the entire edit.

Option-U: Once you’ve selected an edit point, this shortcut toggles among selecting the

video+audio of the edit, just the video, or just the audio.


Edit | Chapter 36 Editing Basics

EDIT

To move the selection to another edit:

�Select a single edit point, then use the Up Arrow key (Previous Edit) or Down Arrow key (Next

Edit) to change the selection to the previous or next edit point among all tracks with Auto Select

turned on.

To deselect all edit points:

�Using the mouse: Click any empty area of the Timeline.

�Using the keyboard: Press Shift-Command-A.

A Practical Example of Keyboard-Driven Selections

Here’s an example of how you would use these keyboard shortcuts together as a

sequence of operations.

To select an edit point using the keyboard:


Press Command-4 to give focus to the Timeline.


Move the Timeline playhead close to the edit point you want to select using the JKL keys.


Press the V key to select the nearest edit point to the playhead on the lowest track with Auto

Select enabled. If there are overlapping superimposed clips on multiple tracks, turn off the Auto

Select controls of tracks with edits you don’t want to select using Option-F1 through Option-F8

corresponding to the Auto Select controls on tracks 1–8. Using the mouse, you can solo a track’s

Auto Select state by Option-clicking its Auto Select button. (Option-F9 toggles the Auto Select

controls of all video tracks.)


Initially, the entire edit is selected, in preparation for a roll edit. To toggle among selecting the

outgoing half, incoming half, and the entire edit, press the U key.


To toggle among selecting the video+audio of the edit, just the video, or just the audio,

press Option-U.


Perform whatever operation you need to. When you’re finished, using Up-Arrow or Down-Arrow to

move the selection backward or forward in the Timeline, or press Command-Shift-A to deselect it.

Using Auto Select Controls

to Define Selections

The Timeline Auto Select controls are extremely useful and versatile controls that serve many

purposes. In short, they give you a way to specify which tracks will be affected or considered when

you’re performing an operation upon multiple superimposed clips on multiple tracks of the Timeline.

Also, the Timeline Auto Select controls are particularly convenient when you’re using keyboard

shortcuts to edit and you don’t want to have to grab your mouse to explicitly select a single clip, since

you can turn Auto Select on or off via keyboard shortcuts.

Defining Selections With the Help of Auto Select Controls

Here is the easiest example of when the Auto Select controls are indispensable. In the following

example, there are two superimposed video clips and three superimposed audio clips. Supposing you

only want to delete the media from tracks V2, V1, and A1, but you want to leave the media on A2 and

A3 alone, you can turn off the Auto Select controls for tracks A2 and A3, and set Timeline In and Out

points to define the range of the clips you want to delete. When you press the Delete key, only the

media on the Auto Select-enabled tracks is deleted.


Edit | Chapter 36 Editing Basics

EDIT

Before and After deleting a clip with Auto Select on Tracks A2, A3, and A4 turned off

TIP: If you set In and Out points to perform an operation and you don’t see any shading

in the Timeline to indicate which parts of the Timeline will be affected and which won’t,

chances are you have another selected clip in the Timeline somewhere you can’t see

that’s overriding auto select. Press Command-Shift-A to de-select all and things should

go back to normal.

Overriding Automatic Selections by Making Manual Selections

It’s important to note that manual selections that you make which highlight specific clips in the Timeline

always override whatever the Auto Select control of a track is set to. In the following example, three

clips are superimposed and the Auto Select control of every track except V2 has been turned off.

Setting Timeline In and Out points now automatically defines that region of the clip on track V2 to be

deleted were you to press the Delete key. You can see the affected part of the Timeline because it’s

highlighted while the rest of the Timeline is dimmed.

Soloing the Auto Select control on track V2 to limit a Delete operation


Edit | Chapter 36 Editing Basics

EDIT

However, if you clicked the clip on track V1 to select it manually, the automatic selection defined by the

In and Out points disappears in favor of the highlighted clip you just clicked. This is because manual

selections almost always take precedence over automatic selections you define using the In and Out

points and Auto Select controls.

Making a manual selection overrides the Auto Select controls

This is good to keep in mind for situations where the fastest way to do the operation you need to do is

to simply manually select the clip you want to define the operation.

Using Auto Select Controls to Control Other Operations

Other operations that are affected by the Auto Select controls include any command that uses “the

clip on the lowest-numbered track with Auto Select enabled” to define what happens. This includes

Copy and Paste, Mark Clip, Go To Next Edit/Previous Edit, the Selection Follows Playhead mode, Next

Gap/Previous Gap, and so on (a full list of affected operations appears later).

A common example of when this is important is whenever you use the Mark Clip command to

automatically set In and Out points to match the duration of a clip on the Timeline. If that clip happens

to be at a section of the Timeline where there are multiple superimposed clips, each of which has a

different duration, then by default the In and Out points (first and last frames) of the clip on the lowest

numbered track is used to set Timeline In and Out points when you use Mark Clip.

Using Mark Clip with all Auto Select controls enabled, the clip on the lowest-

numbered video track with Auto Select enabled defines the result

However, if you disable the Auto Select control of track V1, then whichever clip is on the lowest

video track with Auto Select still enabled is used as the target clip for the Mark Clip operation. In this

example, the shorter clip on track V2 now sets the locations of the In and Out points.


Edit | Chapter 36 Editing Basics

EDIT

Using Mark Clip with Auto Select controls enabled

Methods of enabling and disabling the Auto Select controls:

�To toggle Auto Select for any track: Click any track’s Auto Select control.

�To toggle Auto Select for video tracks: Press Option-F1 through F8 to toggle Auto Select on the

corresponding tracks.

�To toggle Auto Select for audio tracks: Press Option-Command-F1 through F8 to toggle Auto

Select on the corresponding tracks.

�To toggle all video track Auto Select tracks off and on: Press Option-F9.

�To toggle all audio track Auto Select tracks off and on: Press Option-Command-F9.

�To “solo” Auto Select for a track and disable Auto Select on all other tracks: Option-click any

Auto Select control to leave that control on while turning off all other Auto Select controls of that

type (video or audio).

�To turn all audio or video Auto Select controls on and off: Shift-click any video or audio Auto

Select control to toggle on or off all Auto Select controls of that type (video or audio).

The following operations are affected by the state of each track’s Auto Select control:

�Cutting, ripple cutting, copying, or deleting clips: When using Timeline In and Out points to

delete a range of media from the Timeline, only media on tracks with an enabled Auto Select

control will be cut, copied, or deleted.

�Deleting gaps: When selecting and deleting gaps in the Timeline, clips on other tracks that

overlap the selected gap will also be deleted on tracks with an enabled Auto Select control. Media

to the right of affected tracks will ripple left to close the gap.

�Selecting edit points using the keyboard: When you press V to select the nearest edit point, the

edit point on the lowest track with Auto Select enabled is selected. When pressing the Up Arrow

and Down Arrow keys to move the selection from edit point to edit point, edit points on tracks with

a disabled Auto Select control are ignored.

�Selecting clips using the keyboard: When a clip is selected, you can press the Up Arrow and

Down Arrow keys to move the selection from clip to edit clip, but clips on tracks with a disabled

Auto Select control are not seen by this operation.

�Using Mark Clip: When using the Mark Clip command, clips on tracks with disabled Auto Select

controls are ignored. This lets you choose a target clip to use for marking the clip when there are

multiple overlapping superimposed clips.

�Match Frame: When making a Match Frame operation, clips on tracks with disabled Auto Select

controls are ignored. This lets you choose a target clip to use for matching a frame when there are

multiple overlapping superimposed clips.

�Rippling the Timeline during a trim operation: Tracks with Auto Select turned off will not be

rippled. For more information on the rules of ripple trimming, see Chapter 44, “Trimming.”


Edit | Chapter 36 Editing Basics

EDIT

�Pasting clips: All copied clips will be pasted to the lowest numbered track with Source Control

enabled. If all tracks of a particular type have their Auto Select controls turned off, then no clips of

that type will be pasted at all.

�Paste Insert: Tracks with Auto Select turned off will not be rippled or affected by clips being

pasted via a Paste Insert command.

�Using the insert or ripple overwrite edits: Only clips on tracks with Auto Select turned on will be

rippled during an insert edit or ripple overwrite edit.

�Finding gaps: When using Playback > Previous Gap (Command-Option-Semicolon) or Next Gap

(Command-Option-Apostrophe), gaps on tracks with Auto Select disabled will be ignored.

�Using Selection Follows Playhead: When you turn on “Selection Follows Playhead” so that

the clip intersecting the position of the playhead is automatically selected. If multiple clips are

intersecting the playhead, the clip on the highest track will be selected. Clips on tracks with Auto

Select disabled will not be selected.