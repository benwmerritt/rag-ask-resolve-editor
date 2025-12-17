---
title: "Copying Keyframes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 611
---

# Copying Keyframes

It’s possible to copy a set of keyframes from one node to another, either within the current grade, or in

another clip entirely. It’s also possible to copy an entire grade with keyframes from one clip to another.

To copy a set of keyframes from one node to another:


Select a node to copy keyframes from, and choose Edit > Copy (Command-C).


Do one of the following:

�To copy all keyframes, select another node to paste keyframes and other adjustments to, and

choose Edit > Paste (Command-V).

�If you want to just copy only the keyframe information from a specific keyframe track, choose

Edit > Paste Attributes (Option-V), then click the “Copy Keyframes and Align Using” checkbox,

and select the appropriate parameters to copy.

TIP: This procedure also works for tracking data that you want to copy from one node to

another, either in the current clip, or another clip altogether.

To copy an entire grade with keyframes from one clip to another:


Click the thumbnail of the clip you want to copy to in the Thumbnail timeline.


Right-click the thumbnail of the clip you want to copy from, and choose Apply Grade from the

contextual menu.

NOTE: When copying a grade with keyframes from one clip to another, the keyframes

will automatically be placed at matching frames that correspond to the source timecode

of the originating clip. This makes it easy to copy a grade with keyframes to the same clip

elsewhere in the Timeline, but it may not provide the desired results if you’re applying a

grade with keyframes from one clip to a completely different one.

Keyframes and Saved Stills

If you save a still from a clip using keyframes within the grade, by default keyframes are not saved.

However, the still and grade that are saved reflect whatever parameter values are contained by the

next keyframe to the left of the position of the playhead. For example, if a clip has a dynamically

keyframed transition from a saturation of 50 to a saturation of 0, and you place the playhead right

in the middle of both keyframes when you save a still, the grade and still that are saved have a

saturation of 50.

However, if you right-click the background of the Gallery, choose one of the options within the

“Apply Grades Using” submenu, and choose the appropriate “Keyframes Aligning…” options, then

grades saved within a still are saved with the keyframes, which reference the source timecode, or

start frame of the original clips. This means that if you apply a saved grade with keyframes to a clip,

the keyframes will automatically be placed at matching frames that correspond to the source timecode

or start frame of the original clip. This makes it easy to copy a grade with keyframes to the same clip

elsewhere in the Timeline, but it may not provide the desired results if you’re applying a grade with

keyframes from one clip to a completely different one.


Color | Chapter 148 Keyframing in the Color Page

COLOR

Adding EDL Marks

Just as clip grades are separate from the timeline grade that can be applied to the entire Timeline, so

clip keyframes are separate from timeline keyframes. Keyframes you apply to the timeline grade work

exactly the same as clip keyframes. However, there is one extra option you have when keyframing the

timeline grade.

If you find yourself wanting to adjust a timeline grade individually to take into account variations from

one clip to the next, you can use the Add EDL Marks on Tracks command to add a Static keyframe

(mark) to the Keyframe Editor at the position of every edit point in the entire Timeline.

To add EDL marks:


Choose Timeline from the Node Editor’s mode drop-down menu.


If you want to keyframe a grade, then create whatever grade you need to apply to the entire

Timeline. If you want to keyframe Sizing settings, you don’t need to do anything else.


Right-click the Corrector track or the Sizing track in the Keyframe Editor, and choose Add EDL

Marks on Tracks.

Marks appear at the frame of every edit point in the Timeline. You may want to widen the

Keyframe Editor to make it easier to work with all these keyframes.

After you’ve added EDL marks, you can delete them if you decide you don’t want them any more.

To delete EDL marks:

�Right-click the Corrector track in the Keyframe Editor, and choose Delete EDL Marks on Tracks.

If you’ve added your own keyframes in addition to the EDL marks, then the Delete EDL Marks on

Tracks command only eliminates the EDL marks. Your custom marks are left alone.


Color | Chapter 148 Keyframing in the Color Page

COLOR

Chapter 149

Copying and

Importing Grades

Using ColorTrace

ColorTrace is a key feature of DaVinci Resolve, which lets you copy grades quickly

and easily from the clips of one timeline to those within another, based on the

source timecode of each clip (or using clip names when in Automatic mode).

You can even use ColorTrace to copy grades between timelines within the same project,

and ColorTrace one stereo timeline to another.

Contents

Copying Grades Using ColorTrace������������������������������������������������������������������������������������������������������������������������������������������� 3396

Using ColorTrace in Automatic Mode�������������������������������������������������������������������������������������������������������������������������������������� 3397

Using ColorTrace in Manual Mode������������������������������������������������������������������������������������������������������������������������������������������� 3400

Importing CDL Data Using ColorTrace����������������������������������������������������������������������������������������������������������������������������������� 3402

Using CDL Adjustments������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3404

Calculating CDL Functions������������������������������������������������������������������������������������������������������������������������������������������������������������ 3404


Color | Chapter 149 Copying and Importing Grades Using ColorTrace

COLOR

Copying Grades Using ColorTrace

ColorTrace copies whichever version of a clip’s grade was applied in the Source timeline you’re

copying from, either local or remote, depending on which grades each clip in the Source timeline is set

to use. Furthermore, ColorTrace copies Group Pre-Clip and Group Post-Clip grades, as well as Fusion

compositions. These improvements make this an extremely reliable tool for copying grades from one

timeline to another in a wide variety of situations.

To use ColorTrace:


Open the Media page and select the Timeline you want to use ColorTrace with from the Media

Pool, then open it and choose Timelines > ColorTrace > ColorTrace From Timeline.

Choosing ColorTrace for a selected Timeline

The ColorTrace Setup window appears, which shows every project library, user, project, and

timeline within a single hierarchical list.


Using the Project List browser, select the specific Timeline you want to copy grades from.

You’ll need to click the disclosure triangle to the left of the project library, user name, and project

that contains that Timeline in order to select it.

ColorTrace project and Timeline selection window


Color | Chapter 149 Copying and Importing Grades Using ColorTrace

COLOR


(Optional) If you’re using ColorTrace with a project that has numerous VFX clips in a workflow

where all VFX clips have specific reel names that identify them, you can enter these names

(with asterisks (*) used as wildcards that indicate text in each reel name that can vary) in the

“Effects Shot Definitions” field.

This speeds automatic ColorTrace operations by enabling DaVinci Resolve to use fuzzy

string matching when a clip’s reel number qualifies it as a VFX shot so that the best match is

displayed first on the list. You can enter multiple VFX reel names with wildcards, one per line,

for simultaneous string matching. You can use whatever reel name text makes sense for your

workflow, some examples of VFX reel names are as follows:

*_COMP_*

VFX*

EFFECTS*


Click Continue.

The ColorTrace window appears with two tabs that let you choose how to work.


Choose which mode to work in by clicking the Automatic or Manual tab:

�In Automatic mode, ColorTrace automatically searches for matching clips between the selected

Timeline and the current Timeline. Each clip is color coded depending on the correspondence

that’s been identified.

�In Manual mode, you copy grades yourself, using the Copy and Paste procedures, or by

dragging and dropping using your mouse.

The ColorTrace window is complex; details about the operation of each mode are covered

separately in the following sections.


When you’re finished using ColorTrace, click Close.

Using ColorTrace in Automatic Mode

In Automatic mode, ColorTrace automatically finds the correspondences between clips in the selected

Timeline that you want to copy grades from (the Source timeline), and those in the current Timeline that

you want to copy grades to (the Target timeline).

Selecting the Automatic or Manual ColorTrace

Each clip in the Target Timeline Thumbnail timeline is outlined with a color that indicates its status.

Red: No match was found at all. Generally true for clips in the current Timeline that weren’t

used in the Timeline you’re ColorTrace matching to.

Blue: Due to overlapping timecode and reel names, multiple correspondences have been

found (similar to a reel conflict), and you must select the correct one for each clip. This often

happens with VFX and motion graphics clips that you’ve imported with timecode starting at

00:00:00:00.

Green: A match has been found.


Color | Chapter 149 Copying and Importing Grades Using ColorTrace

COLOR

ColorTrace Thumbnail outlines indicate matching,

overlapping, and non matching clips.

In Automatic mode the correspondence between each clip in the Source timeline and each clip in the

Target timeline should be automatically made. However, overlapping timecode and reel names can

cause problems. The other controls in the ColorTrace window help you deal with the subset of clips

that can’t be automatically matched, or are matched in error. These controls are:

The ColorTrace window shown in Automatic mode

Matching Source Clips list: Shows a scrollable collection of thumbnails that might correspond to the

selected clip in the Target timeline.

Target Timeline: Shows each clip in the Timeline you want to copy grades to, color coded according to

how good a match it is.

Clip Info pane: Displays two columns of properties for the source clip and the target clips that you’ve

selected. These properties include the reel, source timecode, record timecode, clip name, project

names, and timeline names of each clip, for easy comparison.

Attributes and options checkboxes: A series of checkboxes lets you specify which clip attributes are

copied as part of the ColorTrace operation.

Color: Enables the copying of grades.

�Preserve Num Nodes: When copying grades, lets you prevent the first X nodes of the target clip

grades from being overwritten by the first X nodes of the source clip grades.

�Input Sizing: Enables the copying of Input Sizing attributes.

�Convergence: Enables the copying of Convergence for Stereo 3D projects.

�Floating Windows: Enables the copying of Floating Windows for Stereo 3D projects.

�Auto Align: Enables the copying of Auto Align settings for Stereo 3D projects.

�All Versions: Copies all versions, rather than just the current version, from the source to the

target clips. The currently selected version of each source clip is always correctly copied.

�Version Camera Raw Settings: Enables the copying of versioned Raw settings, rather than just

the current Raw setting.

�Track Marks: Enables the copying of keyframes.


Color | Chapter 149 Copying and Importing Grades Using ColorTrace

COLOR

�Flags and Markers: Enables copying of all flags and markers.

�Hide Matching Clips: Hides all clips which have been successfully matched, and only show the

clips with multiple or no matches. This lets you focus on the subset of problem clips within a

potentially long timeline.

�Ignore Reel Names: If you believe the reel names are in error, you can turn this checkbox on to

ignore them, matching all source and target clips by timecode alone.

Copy Grades: Copies the matched source grades to each green and purple target clip.

Copy Grades & Exit: Once you’ve finished making all the grade matches you can, click this

button to copy the matched source grades to each green and purple target clip, and close the

ColorTrace window.

Here’s how to use these controls to sort out which source clips to copy from for each blue and red

target clip in the Target timeline.

To manually choose which source grades should be copied to which target clips:


Click any blue clip thumbnail in the Target timeline.

Revealing a number of different possible correspondences in the Matching Source Clips Timeline

A collection of clips with overlapping timecode and reel names appears. If you want to ignore the

reel names because you believe they might be in error, turn on the Ignore Reel Names checkbox.


If a comparison of the Source and Target thumbnails doesn’t make the choice obvious, then click

any of the clips in the Matching Source Clips timeline to view its metadata for comparison in the

source/target columns below.

Source and Target clip metadata for comparison


Color | Chapter 149 Copying and Importing Grades Using ColorTrace

COLOR


Once you’ve decided on a clip correspondence, double-click the Matching Source Clip thumbnail

you want to copy from. If no clip in the Matching Source Clip pane is a good match, double-click

the “Set As New Shot” box.

The Source and Target thumbnails both turn purple, to show that you’ve

created a correspondence.

The matching Source and Target clips now both marked with purple outline

Continue working your way through every thumbnail with Blue and Red Xs until you’ve found

matches for every clip in the Timeline for which it’s possible.


When you’re finished, click Copy Grades & Exit.