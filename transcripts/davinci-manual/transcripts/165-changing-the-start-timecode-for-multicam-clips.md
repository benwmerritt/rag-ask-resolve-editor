---
title: "Changing the Start Timecode for Multicam Clips"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 165
---

# Changing the Start Timecode for Multicam Clips

You can change the starting timecode for both multicam and compound clips. To do so, right-click

on the multicam or compound clip in the Media Pool, and select Starting Timecode from the context

menu. A Set New Start Timecode box will appear, then type in the new starting timecode you wish to

use, and click OK.

Converting Compound Clips or Timelines to Multicam Clips

You can convert compound clips and timelines into multicam clips for easier editing using the Edit

page’s Multicam Editing interface. This conversion is a one-way process. You cannot reconvert a

multicam clip back to a timeline or compound clip. If you wish to preserve the original timeline or

compound clip, make sure to duplicate it first, and then convert the copy.

To convert a compound clip or timeline to a multicam clip:

Right-click on the clip or timeline in the Media Pool and choose “Convert Compound Clips

(Timelines) to Multicam Clips” from the drop down menu.

Logging and Editing Multicam Clips

Once you create one or more multicam clips, you can view them in the Media page or in the Source

Viewer of the Edit page, and add markers to them (all angles share the same markers) to prepare for

the multicam edit you’re planning on performing. When viewing multicam clips in the Media page, you

can choose how many angles to show in the viewer via the Viewer Option menu.


Edit | Chapter 42 Multicam Editing

EDIT

Markers set in a multicam clip in the Media page to prepare for editing

Setting up a Timeline for Multicam Editing

Once you’ve created one or more multicam clips, preparing them for editing is as simple as editing

them into the Timeline, either by dragging and dropping the multicam clip to the Timeline from

the Media Pool, or by opening the multicam clip into the Source Viewer, and then using any of the

available editing methods to cut it into the Timeline from there. Once edited, they appear in the

Timeline like any other clip, just with a multicam badge to the left of the clip name.

Multicam clip badge

in the Timeline

When you perform a multicam edit, DaVinci Resolve plays the entire audio mix while you’re editing, so

if you want to take the opportunity to edit a master audio mix file or additional piece of music to play

along with the multicam clip, you can do so.


Edit | Chapter 42 Multicam Editing

EDIT

Opening and Altering Multicam Clips

After you’ve created a multicam clip and put it into a timeline, you can modify it in a variety of ways by

right-clicking it in the Media Pool and choosing “Open in Timeline.” This replaces the contents of the

Timeline with a vertical stack of superimposed angles, one per track, each of which is offset from the

beginning of the Timeline to align with one another.

An open multicam clip appears like a timeline with a vertical stack of clips

With the multicam clip open, you can make a variety of changes in preparation for editing:

�You can slide a multicam clip left or right to alter its sync (selecting an angle and using the Period

(.) and Comma (,) “nudge” keyboard shortcuts can be a good way of doing this).

�You can delete the track of an angle you don’t need (right-click the track header and

choose Delete Track).

�You can rearrange tracks to rearrange the order in which angles appear (right-click any track

header and choose Move Track Up or Move Track Down).

�You can rename tracks to change the angle name that appears by default in the Multicam Viewer

and that will also appear in the Timeline when you do cut and switch editing.

�You can disable audio or video tracks that correspond to angles you don’t want to see, but don’t

want to eliminate, either.

�You can grade each multicam angle separately (discussed later in this section).

When you’ve finished altering the contents of the multicam clip, you can close it using the path

control at the bottom left-hand corner of the Timeline. Click the name of the edited timeline to

go back, in preparation for the next steps.

A path control lets you exit the multicam clip


Edit | Chapter 42 Multicam Editing

EDIT

Performing a Multicam Edit

After you’ve created one or more multicam clips and edited them into a timeline, actually executing a

multicam edit is simple.


Open the Timeline you created to hold the multicam clip or clips comprising your edit, and position

the playhead where you want to start editing.


Choose Multicam from the Source Viewer mode drop-down.

Switching the Source Viewer

to Multicam viewing

The Source Viewer changes to display all of the different angles within that clip as

switching controls.


Choose how many angles you want to display from the drop-down menu at the bottom right of the

Source Viewer. If you’re using a computer that’s not very fast, you may need to reduce the number

of angles you’re viewing to maintain real time playback.

Choosing how many angles to

view in the Multicam Viewer

If there are more angles within the multicam clip intersecting the playhead in the Timeline than the

Multicam Viewer is set to show, then page controls appear to the left of this drop-down menu that

let you choose which set of angles you want to view.

You can move to another page of angles by doing one of the following:

�Click any dot to jump to that page of angles.

�Click the arrows to move among next/previous sets of angles.

�Choose Edit > Multicam > Previous Page (Option-Shift-Left Arrow) or Next Page

(Option-Shift-Right Arrow).


Choose whether you want to switch both the audio and video, just the video, or just the audio

using the Audio/Video selection buttons at the bottom center of the Multicam Viewer. You can

also choose Edit > Multicam > Video and Audio (Option-Shift-[ ), Video Only (Option-Shift-] ),

Audio Only (Option-Shift-\).


Edit | Chapter 42 Multicam Editing

EDIT

Buttons for choosing

whether to switch the

video, the audio, or both


Start playback, and while watching the program play, do one of the following:

�Click any angle in the Multicam Viewer to insert a cut in the Timeline and switch to that angle. As

you cut-and-switch, the cuts immediately appear in the Timeline while you play onward.

�Option-click any angle to switch the angle used by the current clip without adding a cut. This is

useful if you later regret the angle you cut to and just want to switch the entire segment since the

last cut you made. This can also be accomplished by choosing Edit > Multicam > Previous Angle

(Command-Shift-Left Arrow) or Next Angle (Command-Shift-Right Arrow).

As you play, the entire mix in the Timeline will play along with what you’re switching, so you can

work in context.

A timeline while it’s being edited using cut and switch


When you’re ready to stop multicam editing, simply stop playback. If you want to start trimming the

Timeline to fine-tune what you’ve done, choose Source from the Source Viewer mode drop-down,

and you can re-edit and trim the multicam clips in the Timeline just like any others.

Multicam Controls in the Source Viewer

The Source Viewer, in Multicam mode, has four sets of controls that let you set up and execute

multicam editing.

�Multicam Angle buttons: Each multicam angle displayed in the Source Viewer is a button that lists

the angle name underneath. Clicking any of these buttons inserts a cut and switches the angle of

the next clip, while Option-clicking changes the angle of the clip at the position of the playhead

without adding a cut.

�Audio/Video Selection buttons: Clicking any of these buttons toggles the audio, video, or audio

and video tracks for the cut selection of the Multicam clip. Audio makes an audio only cut, video

makes a video only cut, and audio and video cuts both.

�Multicam display drop-down: Lets you choose how many angles to view while switching.

Depending on your workstation’s performance, reducing the number of angles can improve

playback performance while you edit. You can choose from a grid of 1x1, 1x2, 2x2, 3x3, or

4x4 angles to view.

�Multicam Page buttons: If there are more angles within the multicam clip intersecting the playhead

in the Timeline than the Multicam Viewer is set to show (via the multicam display drop‑down), then

page controls appear that let you choose which set of angles you want to view. Click any dot to

jump to that page of angles, or click the arrows to move among next/previous sets of angles.


Edit | Chapter 42 Multicam Editing

EDIT

The Source Viewer showing Multicam switching controls