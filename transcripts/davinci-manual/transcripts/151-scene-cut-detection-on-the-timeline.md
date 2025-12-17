---
title: "Scene Cut Detection on the Timeline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 151
---

# Scene Cut Detection on the Timeline

If you need to break down a previously edited video into its component clips for re-editing or color

correction, you can do so directly in the Timeline. Using the DaVinci Neural Engine, DaVinci Resolve

can automatically analyze and split up an edited video into individual clips.

Timeline Scene Cut Detection is also available in the Cut page. If you prefer, you can continue to use

the original Scene Cut Detection tool found in the Media Pool.

To use Scene Cut Detection on the Timeline:


Select one or more clips you want to split on the Timeline. Alternately, you can limit Scene Cut

Detection to just a portion of a clip by setting In and Out points on the Timeline around the section

you want to analyze.


Choose Timeline > Detect Scene Cuts.

A dialogue box appears, “Detecting scene cuts in clips x of x.” This process can take some time,

depending on the length, number, and complexity of the clips you’ve selected. When the Scene

Cut Detection has finished, the clip you selected will be broken up into a number of through edits

that now can be used as independent clips.

Checking and Fixing Your Results

If the Neural Engine has made an error, you can fix it manually by navigating to the cut using the Up

and Down Arrow keys to go back and forth in the Timeline, and by then doing one of the following:

�To remove a Cut: Click the through edit to select it, and press the “Delete” key.

�To make a New Cut: Place the timeline indicator at the cut point, and choose Timeline >

Split Clips (Command-\).

A single clip of a finished edit, consisting of multiple cuts before the Detect Scene Cuts command

Multiple individual clips extracted from the edited clip via Detect Scene Cut; the operation has been

contained by the In and Out points, and one of the resulting through edits has been highlighted in green.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

Clean Up Video Tracks

While it’s convenient to be able to edit overlapping clips on multiple video tracks to try slipping clips

back and forth, or to stack multiple takes or versions of a VFX clip, there comes a time when all those

unnecessary clips take a toll on the visual organization of your timeline, not to mention your colorist’s

sanity. For this reason, a trio of commands for cleaning up your timeline have been added to the

Timeline > Clean Up Video Tracks menu. These are:

�Flatten Unused Clips: All superimposed clips with In and Out points that are aligned with clips

below them are moved down to track V1, so long as they don’t have any kind of opacity, composite

mode, transition, or fade effect applied to them making them a compositing effect.

�Disable Unused Clips: All clips that are underneath superimposed clips that don’t have any kind of

opacity, composite mode, transition, or fade effect applied to them are disabled.

�Change Unused Clips Color: All clips that are underneath superimposed clips that don’t have

any kind of opacity, composite mode, transition, or fade effect applied to them have their color

changed to whatever you select.

(Top) The original timeline, (Bottom) The Flatten Unused Clips command is used to move superimposed clips with

In and Out points that match other clips underneath them to track V1 to simplify the Timeline for future work


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

Chapter 39

Three- and

Four‑Point Editing

A more controlled form of editing is to use three- and four-point editing to make a

specific range of source media fit into a specific range of the Timeline.

This chapter covers the basics of three- and four-point editing, as well as the wide variety of edit

commands that are available.

Contents

Keyboard Shortcuts in This Chapter������������������������������������������������������������������������������������������������������������������������������������������� 819

Introduction to Three-Point Editing�������������������������������������������������������������������������������������������������������������������������������������������� 820

Choosing a Track to Edit and Using Destination Controls��������������������������������������������������������������������������������������������� 820

Apply Track Destination Controls Using the Track Header Context Menu�������������������������������������������������������������� 822

Setting In and Out Points in the Timeline�������������������������������������������������������������������������������������������������������������������������������� 822

Mark Clip and Mark Current Selection�������������������������������������������������������������������������������������������������������������������������������������� 824

Preview Marks During Three‑Point Editing���������������������������������������������������������������������������������������������������������������������������� 826

Dragging Preview Marks to Change an Edit���������������������������������������������������������������������������������������������������������������������������� 827

The Rules of Three-Point Editing������������������������������������������������������������������������������������������������������������������������������������������������� 828

Editing Rules for Split In and Out Points������������������������������������������������������������������������������������������������������������������������������������ 830

Editing a Specific Range of the Source Clip Into the Timeline��������������������������������������������������������������������������������������� 830

Editing Part of a Source Clip to Fit Into a Specific Range of the Timeline����������������������������������������������������������������� 831

Backtiming a Source Clip When Editing Into the Timeline����������������������������������������������������������������������������������������������� 832

Switch Focus to Timeline After Edit�������������������������������������������������������������������������������������������������������������������������������������������� 834

Different Types of Three‑ and Four‑Point Edits�������������������������������������������������������������������������������������������������������������������� 834

Overwrite Edits�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 834

Insert Edits������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 835

Replace Edits������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 836

Fit to Fill������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 839


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Keyboard Shortcuts in This Chapter

Here’s a list of of keyboard shortcuts you might find helpful that relate to topics found in this chapter.

Key Shortcut

Function

Command-1

Choose Media Pool Bin list

Command-2

Choose Media Pool browser area

Arrow Keys

Move selection in the Media Pool Bin list or browser area

to choose a bin or clip

Return or Enter

Open selected clip or timeline into the Source Viewer

Q

Toggle focus between Source and Timeline Viewers

I, O

Set In or Out point

Shift-I, O

Move playhead to In or Out point

Option-I, O

Delete In or Out point

Shift-A

Set In and Out points to match the current clip selection in

the Timeline

X

Set In and Out points to fit the current clip at playhead in

the Timeline

Option-X

Delete both In and Out points

Command-Shift-Up, Down Arrow

Move video destination control up or down to another track

Command-Option-Up, Down Arrow

Move audio destination control up or down to another track

Option-1 through 8

Set video destination control to that track number;

press again to enable/disable

Command-Option-1 t horugh 8

Set audio destination control to that track number;

press again to enable/disable

Option-F1 through F8

Toggle video auto-select for that track number

Option-F9

Toggle all video auto-select controls off or on

Option-Command-F1 t hrough F8

Toggle audio auto-select for that track number

Place on Top��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 841

Ripple Overwrite������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 841

Append to End��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 844

Insert Selected Clips to Timeline Using Timecode�������������������������������������������������������������������������������������������������������������� 844

Insert Selected Clips to Timeline With Handles�������������������������������������������������������������������������������������������������������������������� 845

Three-Point Editing From the Media Pool������������������������������������������������������������������������������������������������������������������������������� 846

Example: Assembling Clips Into the Timeline From the Media Pool��������������������������������������������������������������������������� 846


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Key Shortcut

Function

Option-Command-F9

Toggle all audio auto-select controls off or on

Option-Shift-Q

Toggles “Switch to Timeline After Edit,” to set whether

focus stays on the Source Viewer or switches to the

Timeline after you make an edit; on by default

F9

Insert Edit selected clip(s) from Media Pool or

Source Viewer to the Timeline

F10

Overwrite Edit selected clip(s) from Media Pool or

Source Viewer to the Timeline

F11

Replace Edit the first of selected clip(s) from Media Pool or

Source Viewer to the Timeline

F12

Place On Top Edit from Media Pool or Source Viewer to

the Timeline

Shift-F10

Ripple Overwrite from Media Pool or Source Viewer to

the Timeline

Shift-F11

Fit to Fill from Media Pool or Source Viewer to the Timeline

Shift-F12

Append To End Edit from Media Pool or Source Viewer to

the Timeline

Undo

Command-Z

Redo

Command-Shift-Z

Introduction to Three-Point Editing

Three-point editing is a standard editorial method that’s shared with many other post-production

applications, so this procedure should feel familiar. The idea is that you need only set any combination

of three In and Out points in the source clip and Timeline to edit a clip into your program at a specific

time, and DaVinci Resolve automatically figures out the fourth edit point that’s necessary to execute

the edit. Three-point editing is most commonly accomplished using overwrite and insert edits.

Choosing a Track to Edit and

Using Destination Controls

The orange destination controls, found in the Timeline header area, let you specify which video and

audio tracks you want incoming source clips to be edited to when you use editing methods other than

drag and drop. No matter how many video or audio channels may be embedded within a single clip

of media, only one video and one audio destination control is available. In the case of video, you can

only expose one video channel of a clip at a time. In the case of audio, all audio channels for a given

clip are embedded within a single Timeline track, making it a snap to edit stereo or other multi-channel

audio sources together.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

For more information about working with audio, see Chapter 45, “Working with Audio in the

Edit Page.”

Setting the destination control of a track is a vital step in the process of creating an edit and is easy to

do. You can set the video and audio destination controls to be separate tracks.

To assign the destination tracks of incoming source clips, do one of the following:

�Click the destination control of any unassigned track to enable that track as the destination.

�Drag the destination control to any unassigned track in the Timeline.

�Right-click on the destination control to choose the source audio or video track.

�Press Command-Shift Up Arrow and Down Arrow to move the Video destination control up and

down among different video tracks, or press Command-Option Up Arrow and Down Arrow to

move the Audio destination control up and down among different audio tracks.

�Press Option-1 through 8 to set a video destination, or press Option-Command-1 through 8 to set

an audio destination on tracks 1 through 8.

�Press Option-Command-9 to set the audio destinations to all tracks.

Moving the destination

control to track V2,

labeled “Titles”

You can also disable the Video or Audio destination controls in situations where you want to edit a

source video clip into the Timeline without its audio, or vice versa.

To disable or reenable a destination control, do one of the following:

�Click an already assigned destination control to toggle it off and then on again.

�Pressing the “assign destination control” repeatedly for a given track (Option 1-8 for video,

Option‑Command-1-8 for audio) toggles the destination track on and off.

Disabled destination controls are highlighted gray.

A disabled

destination control


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT