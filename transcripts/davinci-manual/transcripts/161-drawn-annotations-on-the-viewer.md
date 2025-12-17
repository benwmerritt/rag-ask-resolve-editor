---
title: "Drawn Annotations on the Viewer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 161
---

# Drawn Annotations on the Viewer

It’s now possible to use the Annotations mode of the Timeline Viewer to draw arrows and strokes of

different weights and colors directly on the video frame, in order to point out or highlight things that

need to be fixed. These annotations are stored within markers, similarly to marker names and notes.

To start, simply choose Annotations mode from the Timeline Viewer mode drop-down menu.

Choosing Annotations from the

Viewer Mode drop-down menu

Once in Annotations mode, an Annotations toolbar appears showing the following options:

Draw tool with line weight drop-down: Click the Draw tool to be able to

freeform draw on the Viewer. Click the Line Weight drop-down to choose from

one of three line weights to draw with.

Arrow tool: Click the Arrow tool to draw straight-line arrows pointing at features

you want to call attention to. Arrows are always drawn at the same weight,

regardless of the weight selected for the Line tool.

Line Tool: Click the Line tool to draw straight lines on the Viewer.

Rectangle Tool: Click the Rectangle tool to draw boxes on the Viewer.

Color drop-down: Choose a color for drawing or lines.

Methods of making and editing annotations:

�To create an annotation: Simply enable Annotations mode, then park the playhead on any frame

of the Timeline and start drawing. A marker will automatically be added to the Timeline at that

frame, and that marker contains the annotation data. If you park the playhead over a preexisting

timeline marker, annotations will be added to that marker.

�To edit a stroke or arrow you’ve already created: Move the pointer over a stroke or arrow and

click to select it, then choose a new line weight or color from the appropriate drop-down menu, or

drag that stroke or arrow to a new location to move it.

�To delete a stroke or arrow: Move the pointer over a stroke or arrow and click to select it, then

press the Delete or Backspace keys.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

Drawing annotations to highlight feedback

Reading Marker Information

Once you’ve added a number of markers with custom information, there are two ways of viewing this

information without having to open the marker dialog.

To read marker notes using your pointer:

�Double-click a marker to open its marker dialog.

�Move the pointer over any marker in the Source Viewer or Timeline to see a tooltip showing that

marker’s information.

Moving the pointer over a marker

displays its information in a tooltip

To read marker information in the Source and/or Timeline viewers:


Open the Source or Timeline Viewer’s option menu, and turn on Show Marker Overlays.


Stop playback, and move the playhead to a marker. That marker’s information is displayed in the

Viewer, superimposed.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

Marker information shown in the Source Viewer

Using Markers for Navigation

Markers can be used to aid navigation, via two keyboard shortcuts that let you jump the playhead

from marker to marker. When moving the playhead among markers, Clip and Timeline markers are

mixed together.

To move the playhead to the next or previous marker:

�Press Shift-Up Arrow to move the playhead to the next marker to the left in the Timeline.

�Press Shift-Down Arrow to move the playhead to the next marker to the right in the Timeline.

The marker under the playhead is then automatically selected.

To move the playhead to a specific marker using the Source or Timeline Viewer’s Marker list:

�For a source clip or timeline with multiple markers, you can move the playhead immediately to a

specific marker by opening the Source or Timeline Viewer’s Option menu, and choosing a marker

from the Markers submenu, which exposes all the markers that are available in that Viewer, by

name and note.

All markers in the currently open clip as seen in the Source Viewer Option menu Markers list


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

Using Timeline Markers for Chapters

Certain file types, like QuickTime, allow chapter-based navigation in the final video. This allows the

viewer to skip back and forth through the video landing at exact points specified by the video’s

creator. This chapter-based navigation is especially useful in instructional videos or long presentations.

Chapter points in DaVinci Resolve are set by timeline markers.

Currently only the QuickTime and MP4 formats support chapter markers in DaVinci Resolve.

To create a chapter marker in the Timeline:

�Put the playhead at the spot in the Timeline you wish to make a chapter point, and choose

Add Marker (M).

�Edit the marker by double-clicking on it, or by selecting Modify Marker (Command-M).

�Edit the Name field to create the chapter name that will show up in the player.

�Select a color for the marker. All chapter markers must be assigned the same color.

To export embedded chapter markers in a QuickTime movie:

�In the Deliver page, select Quicktime or MP4 as the Format in the Video Panel.

�Check the box next to Chapters from Markers, and select the chapter marker color you chose

earlier from the drop-down menu.

The Chapters from Markers checkbox in the

QuickTime Export Video settings of the Deliver page

Using Markers in the Marker Index

You can use the Marker Index to easily view, edit, and organize all your timeline and clip markers in

one convenient location. The Marker Index can be found by clicking on the Index panel, and selecting

the Markers tab.

Methods of working with markers in the Marker Index:

�To filter markers in the Marker Index: Click the Option menu of the Marker Index and choose

Show All or Show Only to choose a specific color. Each clip with a matching marker appears in

a list, with columns corresponding to the color(s), information, and notes of each timeline and

clip marker. Columns can be sorted in ascending or descending order by clicking on the column

header. Individual columns can be turned on or off by right-clicking on the column header, and

checking or unchecking the column name.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

�To move the playhead to the position of a marker in the Marker Index: Double-click that marker’s

entry in the list.

�To edit marker information: You can change the values of a marker by clicking in the Name,

Notes, or Keyword fields, and modifying the text field. Other values are not editable in the Marker

Index and should be changed in the timeline marker’s Edit dialog.

�To search for a specific marker: Click on the search icon (magnifying glass), and type in your

search terms. The search returns results from all fields in the Markers window. This includes Name,

Notes, and Keywords fields.

�To switch between Thumbnail and List view: Click on either the Thumbnail or List View icons in

the top bar of the Marker Index.

The Marker Index in List View mode lets you edit and organize all your timeline’s markers in one place.

Exposing Markers in Lists

You can also use the Edit Index to filter out a list of markers appearing within the current Timeline.

You can filter all markers at once, in which case columns expose the notes and colors applied to each

marker. You can also filter by a specific marker color if you only want to see one type of marker.

Methods of working with markers in the Edit Index:

�To filter all clips with markers in the Edit Index: Click the Markers tab of the Edit Index and

choose Show All or choose a specific color from the Option menu. Each clip with a matching

marker appears in a list, with columns corresponding to the color(s) and notes of each Timeline

and Clip marker.

�To move the playhead to the position of a marker in the Edit Index: Click that marker’s entry

in the list.

�To show hidden marker columns: Right-click any column header, and turn on any of the selections

to show that column. If necessary, columns can be rearranged by dragging them left or right.

You also have the option to export lists of markers as an EDL, a .txt, or .csv file.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

Exporting lists of markers:

�To export Timeline markers as an EDL: Right-click that timeline in the Media Pool, and choose

Timelines > Export > Timeline Markers to EDL. Choose a location and export format from the

Export Edit Index dialog, and click Save. Each Timeline marker is listed in the resulting EDL, with

any notes included along with a duration, where applicable.

�To export all filtered markers in the Edit Index as a .txt or .csv file: After you choose Show

Markers in the Edit Index option menu, then open the Option menu again, and choose Export Edit

Index. Choose a location and export format from the Export Edit Index dialog, and click Save.