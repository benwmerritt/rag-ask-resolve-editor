---
title: "Import and Export Transcriptions"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 159
---

# Import and Export Transcriptions

using SRT Files

Transcription text can be imported and exported using standard .srt files.

To Import a Transcription using an SRT File:

It’s important that the timecode of the clip you’re importing subtitles to, matches the timecode in the

.srt file for accurate results.


Click on the Option menu in the Transcription window and select Import Subtitles from the

dropdown menu.


Locate the .srt subtitle file in your file browser and click Open.


Click on the Transcribe icon in the Media Pool to open the Transcription window to view and edit

the subtitles.

To Export a Transcription using an SRT File:


Click on the Option menu in the Transcription window and select Export Subtitles from the

drop-down menu.


The Export Subtitles dialog box will appear.


Enter a file output name and path, to save your .srt file to.


4Enter the subtitle information for Caption Preset, Maximum Characters per Line, Number of Lines,

and Gap Between Subtitles, as needed.


Click on the Create button to save the .srt file.

The Export Subtitles dialog box from the

Transcription window’s Option menu.


Edit | Chapter 40 Text Based Editing

EDIT

Chapter 41

Marking and Finding

Clips in the Timeline

As you work on your project, you’ll find it useful to identify important information

about each clip, and about significant moments in each timeline, using a

combination of Flags, Markers, and clip Label colors.

These can be applied to source clips in the Media Pool, or to clips that have already been edited into

timelines. In the case of markers, these can also be added to the Timeline ruler itself to help you keep

track of important moments or notes, and to help you with snapping. You’ll also find yourself modifying

clips in different ways, unlinking and relinking the audio and video of different clips, enabling and

disabling clips in the timeline.

Contents

Using Flags���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 864

Using Markers���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 865

Adding Markers to Clips�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 865

Adding Markers to Timelines���������������������������������������������������������������������������������������������������������������������������������������������������������� 867

Saving In and Out Point Ranges As Markers with Duration��������������������������������������������������������������������������������������������� 868

Editing Marker Information and Keywords������������������������������������������������������������������������������������������������������������������������������� 869

Changing Marker Timing������������������������������������������������������������������������������������������������������������������������������������������������������������������� 870

Copy and Paste Multiple Markers in the Viewers and Timeline������������������������������������������������������������������������������������� 871

Marker Notes in Data Burn-Ins�������������������������������������������������������������������������������������������������������������������������������������������������������� 871

Drawn Annotations on the Viewer���������������������������������������������������������������������������������������������������������������������������������������������� 873

Reading Marker Information������������������������������������������������������������������������������������������������������������������������������������������������������������ 874

Using Markers for Navigation�������������������������������������������������������������������������������������������������������������������������������������������������������� 875

Using Timeline Markers for Chapters���������������������������������������������������������������������������������������������������������������������������������������� 876

Using Markers in the Marker Index��������������������������������������������������������������������������������������������������������������������������������������������� 876

Exposing Markers in Lists���������������������������������������������������������������������������������������������������������������������������������������������������������������� 877

Using Markers in the Media Pool������������������������������������������������������������������������������������������������������������������������������������������������� 878

Hiding Markers By Color������������������������������������������������������������������������������������������������������������������������������������������������������������������ 879

Deleting Markers By Color�������������������������������������������������������������������������������������������������������������������������������������������������������������� 879

Renaming Clips in the Timeline���������������������������������������������������������������������������������������������������������������������������������������������������� 879


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

Using Flags

Flags are meant to mark an entire clip, and they also flag every other clip in the Timeline that shares

the same Media Pool source clip, making this a handy way of quickly identifying which clips in a given

timeline come from the same Media Pool source.

The Flag and Marker

buttons and pop-ups.

You can apply multiple flags to clips, with a variety of colors to choose from. In addition to flagging

specific media files, flags can be useful for timeline filtering in the Color page, sorting by column in the

Media Pool, and a variety of other operations.

Methods for flagging clips:

�To flag a clip using the toolbar: Select one or more clips, and either click the Flag button to flag

that clip with the current color, or click the Flag drop-down in the toolbar to choose a different

color and then click the Flag button. In the Edit page, flags appear in the Timeline superimposed in

the name bar of each clip.

Color Labeling Clips in the Timeline������������������������������������������������������������������������������������������������������������������������������������������ 880

Custom Clip Colors������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 880

Clip Color Appearance����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 880

Assigning Clip Colors��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 881

Track Colors�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 882

Finding Clips, Media, Markers, Gaps, and Timelines�������������������������������������������������������������������������������������������������������� 882

Finding Clips in the Timeline����������������������������������������������������������������������������������������������������������������������������������������������������������� 882

Finding Offline Clips in the Timeline������������������������������������������������������������������������������������������������������������������������������������������� 883

Finding Edit Index Events Using Clips in the Timeline������������������������������������������������������������������������������������������������������� 883

Finding Clips�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 883

Finding Clips Using Markers or Flags����������������������������������������������������������������������������������������������������������������������������������������� 884

Finding Gaps������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 884

Finding the Currently Open Timeline in the Media Pool��������������������������������������������������������������������������������������������������� 884

Finding Media Using Match Frame Operations�������������������������������������������������������������������������������������������������������������������� 885

Matching From the Timeline������������������������������������������������������������������������������������������������������������������������������������������������������������ 885

Matching From a Source Clip���������������������������������������������������������������������������������������������������������������������������������������������������������� 886

Finding a Clip in the Media Pool Using a Timeline Clip��������������������������������������������������������������������������������������������������� 887

Using a Clip in the Source Viewer to Find a Media Pool Clip������������������������������������������������������������������������������������������ 887

Using a Clip in the Timeline to Find a Media Pool Clip������������������������������������������������������������������������������������������������������� 887

Tracking Media Usage����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 887

Thumbnail Clip Usage Indicators�������������������������������������������������������������������������������������������������������������������������������������������������� 887

List View Clip Usage Column���������������������������������������������������������������������������������������������������������������������������������������������������������� 888


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

�To flag a clip: Select one or more clips, and Choose Mark > Add Flag > Current Selected (G) to add

markers of a specific color directly to clips and the Timeline. The individual flag color commands

can be assigned specific keyboard shortcuts if you want to be able to place a specific flag

color at a keystroke.

�To flag a clip in the Source Viewer: Open a clip in the Source Viewer, and while the Source

Viewer has focus, choose Mark > Add Flag > Current Selected (G). The individual flag color

commands can be assigned specific keyboard shortcuts if you want to be able to place a specific

flag color at a keystroke.

�To remove all flags from a clip: Select one or more clips with flags you want to remove, then

click the Flag drop-down in the toolbar, and choose the top “Clear All” option.

�To show or hide a particular color of flags: Choose a color of flag to hide from the

View > Show Flags submenu, or choose View > Show Flags > All to show them all.

�To filter all flagged clips in the Edit Index: Click the Option menu of the Edit Index and choose

Show Flags. Each flagged clip appears in a list, with a column showing the color(s) of the flags

applied to each entry in the list.

Using Markers

Markers are used to call attention to a particular frame within a specific clip. Markers can be individually

colored, and can have customized name and note text. Whenever you enter text into a marker, that

marker displays a small dot that indicates there’s more information inside of it. Once placed, markers

snap to In and Out points, edit points, the playhead, and other markers whenever snapping is enabled,

making it easy to use markers to “measure” edits and trims that you make in the Timeline.

Adding Markers to Clips

You can place markers on the jog bar of source clips in the Source Viewer (or in the Media page

Viewer), and on clips that are selected within a timeline.

(Top) Markers placed on a

source clip,

(Bottom) Markers placed

on a clip in the Timeline

When you add markers to a source clip, those markers also appear in the Media Pool as

hierarchically disclosable items attached to that clip in List view (markers are not visible in

Thumbnail view). More information about using markers in the Media Pool’s List view appears later

in this chapter.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

Markers can be viewed as separate clips identified

by marker name when the Media Pool is set to List view

The following procedures describe how to add markers to clips and timelines in DaVinci Resolve.

To mark a source clip in the Source Viewer or Media Page Viewer, do one of the following:

�To place a marker without doing anything else, move the playhead to the frame you want to mark,

and then press M.

�To place a marker and immediately open the marker dialog to enter a name or note within it during

playback, press Command-M (or press M twice). Playback pauses until you enter the text you want

to and close the marker dialog again, at which point playback continues.

�Move the playhead to the frame you want to mark, then right-click in the jog bar and choose a

marker color from the Add Marker submenu of the contextual menu.

To mark a clip in the Timeline, do one of the following:

�Select one or more clips you want to mark, then move the playhead to the frame of a

selected clip in the Timeline, and click the Marker button in the toolbar (or press M) to place a

marker at that frame, using the current color (if multiple overlapping clips are selected, you’ll

add a marker to all clips).

�To place a marker during playback and immediately open the marker dialog to enter a name or

note within it, select one or more clips you want to mark, play through the selection until you want

to place a mark, then press Command-M (or press M twice). Playback pauses until you enter some

text and close the marker dialog again, at which point playback continues.

�Select one or more clips you want to mark, and then click the Marker drop-down to choose a

different color, and click the Marker button.

Markers appear in the Timeline at the top of

the title bar of the clip to which they’re applied


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT