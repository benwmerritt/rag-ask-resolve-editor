---
title: "Absolute Timecode Entry"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 137
---

# Absolute Timecode Entry

Absolute timecode is entered simply by typing in a timecode value. So long as no clips or edit points

are selected when you press the Return key, the playhead will move to that timecode value. If an

edit point or clip is selected, those will be moved or trimmed to the corresponding timecode value,

if possible.

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

results in the value you type being added to the current timecode value for purposes of offsetting

the playhead or moving a selection. Adding a minus will subtract the value you type from the current

timecode value.

Here are two examples of relative timecode entry:

User-Typed Value

Result

+20.

00:00:20:00 is added to the current timecode value.

+3..

00:03:00:00 is added to the current timecode value.

-5

00:00:00:05 is subtracted from the current timecode value.


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

Copy and Paste Timecode in Viewer Timecode Fields

You can right-click on most Viewer timecode fields in the Media, Edit, and Color pages to choose

Copy and Paste commands from a contextual menu for copying and pasting timecode values. You

can also click in the timecode fields and use the normal Copy (Command-C), and Paste (Command-V)

keyboard commands. This works even between pages. The timecode value you’re pasting must be

valid timecode, for example you can’t paste 0 hour timecode onto a 1 hour timeline.

Right-clicking on a timecode field

to use the Copy Timecode command

Gang Viewers (Playhead Ganging)

Ordinarily, the playhead movement in the Source and Timeline Viewers is independent. However, if

you click the Option menu at the upper right-hand corner of either Viewer and turn Gang Viewers on,

the movement of the Source and Timeline Viewer playheads is locked together, so that they move

in unison. This is useful when you’re marking the In and Out points of a clip in the Source Viewer to

match the duration of a clip or other event in the Timeline.

When the Source and Timeline Viewers are ganged, you can still switch focus back and forth between

the Source and Timeline Viewers, and your video output device will consistently switch to output

whichever Viewer is in focus.

Adding Markers

While markers, flags, and clip labels are covered in much more detail elsewhere in the editing

section, the use of markers is so important that a summary of how to add and edit markers appears

here. Markers are used to call attention to a particular frame within a specific clip. Markers can be

individually colored, and can have customized name and note text. Whenever you enter text into

a marker, that marker displays a small dot that indicates there’s more information inside of it. Once

placed, markers snap to In and Out points, edit points, the playhead, and other markers whenever

snapping is enabled, making it easy to use markers to “measure” edits and trims that you make in

the Timeline.


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

Adding Markers to Clips

You can place markers on the jog bar of source clips in the Source Viewer (or in the Media Page

Viewer) and on clips that are selected within a timeline.

Markers placed on a source clip

Markers placed on a clip in the Timeline

To mark a source clip in the Source Viewer or Media Page Viewer, do one of the following:

�To place a marker without doing anything else, move the playhead to the frame you want to

mark, and then press M.

�To place a marker and immediately open the marker dialog to enter a name or note within it

during playback, press Command-M. Playback pauses until you enter the text you want to and

close the marker dialog again, at which point playback continues.

�Move the playhead to the frame you want to mark, then right-click in the jog bar and choose a

marker color from the Add Marker submenu of the contextual menu.

Once you’ve added some markers, you may want to edit their contents to make them more useful.

To open a marker’s edit dialog to alter its properties:


Do one of the following:

�Press Command-M to add a marker during playback and immediately open its edit dialog.

�Double-click any marker you want to edit.

�Move the playhead to the frame containing the marker you want to annotate using Shift-Up

Arrow/Down Arrow and press M.

�Select a marker anywhere in the Source Viewer or Timeline, and press Shift-M.


When the marker dialog opens, you can modify several properties.

The properties found in the marker dialog


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

For much more information about markers,

see Chapter 41, “Marking and Finding Clips in the Timeline.”

Setting In and Out Points

Now that you’ve used playback commands to review your clips, you can place In and Out points to set

the range of each clip that you want to edit into the Timeline. If you don’t set In or Out points, then the

entire clip will be edited into the Timeline. If you do set In and Out points, those points will be saved in

the Media Pool and used the next time you edit that clip.

Setting Clip In and Out Points in the Media Pool

You can set In and Out points right in the Media Pool to prepare for editing.

To set In and Out points while skimming a thumbnail in the Media Pool’s Metadata view:

Set the Media Pool to Metadata view, then move the pointer over the Thumbnail and wait a moment

until dragging the pointer begins to skim through that clip. As you skim, press I and O to set In and Out

points to encompass the part of that clip you’re going to want to use.

To set In and Out points while skimming a thumbnail in the Media Pool’s Thumbnail view:

Set the Media Pool to Thumbnail view, then move the pointer over a clip and wait a moment until

dragging the pointer begins to skim through that clip. As you skim, press I and O to set In and Out

points to encompass the part of that clip you’re going to want to use. When you’re finished, that clip’s

thumbnail will show a range indicator at the bottom to show how much of the clip you’ve selected.

To set In and Out points using the Media Pool’s List view Filmstrip:

Set the Media Pool to List view, then select a clip to expose it in the Filmstrip at the top of the Media

Pool, drag the pointer through the Filmstrip to watch it play, and press I and O to set In and Out points

to the appropriate range.

Marking In and Out points in the Filmstrip of the Media Pool in List view

The Filmstrip will dim the heads and tails to let you see the range of media you’ve marked. Once

you’ve marked In and Out points in the Filmstrip, you can drag them to the left and right to move them.


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

Setting Clip In and Out Points in the Source Viewer

For a better look at your footage, you can set In and Out points in the Source Viewer in preparation

for editing.

To set In and Out points in the Source Viewer:


Either skim a Media Pool thumbnail with Live Media Preview enabled in the Source Viewer’s

option menu, or open a clip into the Source Viewer.


Use JKL, the Spacebar, the transport controls, or drag in the jog bar to move the playhead to

where you want to set an In or Out point.


Do one of the following:

To mark simple In and Out points: Use the In and Out buttons to the right of the transport

controls, or press the I or O keys.

To mark split In and Out points in preparation for making a split edit: Right-click the Jog Bar

and choose Mark Split > Mark Video In (Shift-Option-I) / Mark Audio In (Command-Option-I) / Mark

Video Out (Shift-Option-O) / Mark Audio Out (Command-Option-O).

Marking In and Out points in the Source Viewer, both as simple (Left) and split edits (Right)

Simple In and Out points let you join the audio and video of two clips at a single edit point in the

Timeline. However, setting split In or Out points sets you up to create split edits where the video is

offset from the audio in a single step.

Clearing and Navigating In and Out Points

Once placed, you can also clear In and Out points you don’t want and move the playhead to In and

Out points you might want to edit.

To clear In and Out points:

�To clear In or Out points: Move the pointer over a marked thumbnail in the Media Pool or over

the Media Pool film strip, or open a clip in the Source Viewer, and then press Option-I to clear the

current In point, or Option-O to clear the current Out point.

�To clear Split In or Split Out points: Press Shift-Option-X to clear the Video In and Video Out

points. Press Command-Option-X to clear Audio In and Audio Out points.

�To clear both the In and Out points at once: With the pointer over a marked thumbnail in the

Media Pool or over the Media Pool film strip, or with the Source Viewer selected, press Option-X.


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

To jump the playhead to the current In or Out points in the Source or Timeline Viewer:

�Press Shift-I to move the playhead to the current In point (Playback > Go To > In).

�Press Shift-O to move the playhead to the current Out point (Playback > Go To > Out).

The Go to In and Go to Out commands are capable of placing the playhead at the implicit (but

unmarked) In and Out points defined by a three point edit you’re setting up, even when Preview Marks

have not been enabled. For example, if you mark In and Out points in the Timeline, and you then mark

an In point for a clip in the Source Viewer, pressing Shift-O (Go to Out) automatically moves the Source

Viewer playhead to the frame that will be the Out point of that clip were you to execute this edit.

In and Out points set in the Timeline and an In point set in the Source Viewer set up a three point edit,


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

Using Go to Out to move the Source Viewer playhead to the implicit Out point defined by a three point edit