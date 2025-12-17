---
title: "Audio FX"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 124
---

# Audio FX

On all platforms, DaVinci Resolve supports Fairlight FX, which are built-in audio plugins that come with

DaVinci Resolve. Additionally, DaVinci Resolve supports the use of third-party VST audio plugins on

macOS and Windows, and Audio Unit (AU) audio plugins on macOS. Once you install these effects on

your workstation, they appear in this panel of the Effects Library. Audio plugins let you apply effects

to audio clips or an entire track’s worth of audio to add creative qualities such as echo or reverb, or to

take care of mastering issues using noise reduction, compression, or EQ.

Effects Library Favorites

You can click on the far right of any transition, title, or generator to flag that effect with a star as a

favorite effect. When you do so, the favorited effects appear in a separate Favorites area at the bottom

of the Effects Library Bin list.

Stars indicate a flagged favorite effect; all favorites are currently filtered.

Index

The index provides information about your timeline in a simplified spreadsheet format; it is used

for both reference and timeline navigation. The index is broken up into the Edit Index, Tracks, and

Markers tabs.

Edit Index

Clicking the Edit Index button opens the Edit Index. By default, this shows an EDL-style list view of

all the edit events in the current timeline. Whichever timeline is selected in the Timeline list displays


Edit | Chapter 33 Using the Edit Page

EDIT

its events here. However, the contents of the Edit Index can be filtered using commands found in

the Option drop-down, described later in this section.

Each clip and transition is shown as an individual event, each of which contains multiple columns of

information. If you re-edit a timeline, your changes are also reflected in this list. The Edit Index is useful

for creative editors that are looking for specific effects that are used in the current timeline, or for

finishing editors that need more information about a specific clip, or who might need to filter the entire

edit by specific criteria in order to troubleshoot various issues.

Edit Index List shown open

Navigating the Timeline Using the Edit Index

Whenever you move the Timeline playhead to intersect a clip, the Edit Index updates to show only the

clips on the video track the intersecting clip is on, and that clip’s event is highlighted in the Edit Index.

This makes it easy to see the correspondence between a clip in the Timeline and its event, which is

helpful when troubleshooting problems. There are also commands available in the Option menu to

display only clips on enabled tracks, only video clips, and only audio clips.

Edit Index Columns

Each event populates several columns of information. These columns can be rearranged by dragging

them to the left or right, depending on what information is most important to you.

The available columns of information are:

�#: The event number (which corresponds to the clip number shown in the Thumbnail timeline of

the Color page).

�Reel: The reel name of the corresponding clip.

�Match: Flags clips that have clip conflicts, which display a question mark in this column.

Once the clip conflict has been resolved, this flag disappears.

�V: Video event.


Edit | Chapter 33 Using the Edit Page

EDIT

�C: The event type (C for cut, D for dissolve or transition).

�Dur: A number showing the duration of a transition in frames.

�Source In/Source Out: The Source In and Source Out timecode indicating the range of timecode

referenced by that clip; corresponds to the timecode locations of each clip’s In and Out point

relative to the source media it comes from.

�Record Duration: The duration of the clip in the Timeline, determined by the

Record In/Out timecodes.

�Record In/Record Out: Record In and Record Out timecode indicating that clip’s

position in the Timeline.

�Name: The name of the clip.

�Comments: Whatever comments were present in the EDL that was imported. For example, clip

names exported from the original NLE to be used as reel names in RED workflows using EDL import.

�Source Start/ Source End: The very first and last frame of media available in the Source Media

for that clip.

�Source Duration: The duration, in timecode, of the total source media available in that clip.

�Codec: The codec of the corresponding clip.

�Source FPS: The frame rate of the corresponding clip.

�Resolution: The frame size of the corresponding clip.

�Color: The color of flags or markers applied to that clip.

�Notes: Notes entered inside of markers applied to clips or the Timeline.

�EDL Clip Name: Shows the name of the imported EDL, if that’s available.

�Marker Keywords: Lists all keywords found in a particular marker.

The columns in the Edit Index can be customized to prioritize the information that’s important to you.

Methods of customizing metadata columns in the Edit Index:

To show or hide columns: Right-click at the top of any column in the Edit Index and select an

item in the contextual menu list to check or uncheck a particular column. Unchecked columns

cannot be seen.

To rearrange column order: Drag any column header to the left or right to

rearrange the column order.

To resize any column: Drag the border between any two columns to the right or left to

narrow or widen that column.

You can also customize column layouts in the Edit Index. Once you’ve customized a column layout that

works for your particular purpose, you can save it for future recall.

Methods of saving and using custom column layout:

To create a column layout: Show, hide, resize, and rearrange the columns you need for a

particular task, then right-click any column header in the Media Pool and choose Create

Column Layout. Enter a name in the Create Column Layout dialog, and click OK.

To recall a column layout: Right-click any column header in the Media Pool and choose the

name of the column layout you want to use. All custom column layouts are at the top of the list.

To delete a column layout: Right-click any column header in the Media Pool and choose the

name of the column layout you want to delete from the Delete Column Layout submenu.


Edit | Chapter 33 Using the Edit Page

EDIT

Filtering the Edit Index

You can use options found in the Edit Index’s option menu to filter specific things that you want to

check out, whether to go through all of the marked clips to see if there are any notes you need to

address, or to isolate all offline clips, or to go through edits to see if there’s anything you need to fix.

You can filter the Edit Index in the following ways:

�Show All: Shows all entries in the list. Choose this option after using any of the other options to go

back to seeing the entire timeline.

�Show Active Track Items: Filters out all clips that appear on tracks above or below tracks

identified with a destination control. For example, if you have three video tracks and the

destination control is on track V2, then all clips on tracks V1 and V3 will be hidden from

the Edit Index.

�Show Video Track Items: Filters out all audio clips so only video clips appear in the list.

�Show Audio Track Items: Filters out all video clips so only audio clips appear in the list.

�Show Flags: Isolates clips with flags in the list. A submenu lets you choose to show all clips with

flags or only clips with a particular color of flag.

�Show Markers: Isolates all clips with markers in the list. A submenu lets you choose to show all

clips with markers or only clips with a particular color of marker.

�Show Clip Colors: Isolates all clips that have been labelled with clip colors in the list. A submenu

lets you choose to show all clips that are labelled using any clip color or only clips labelled with a

particular color.

�Show Through Edits: Filters only clips that have through edits, or cuts where continuous timecode

appears from the outgoing to the incoming half of the edit, that you may or may not want to

remove, depending on why they’re there.

�Show Offline Clips: Isolates all offline clips (clips that have become unlinked from the

corresponding source media on disk) in the Timeline, so you can quickly navigate to each one and

troubleshoot the issue.

�Show Clip Conflicts: Filters all clips with clip conflict warning badges (indicating there is reel,

name, and timecode metadata that overlap that of another clip) in the Timeline, so you can quickly

navigate to each one and check whether they’re using the correct clip.

�Show Clips With Speed Effects: Filters all clips with linear or variable Speed Effects in

the Timeline.

�Show Clips With Composite Effects: Filters all clips with Composite mode or Opacity settings

other than the default (Normal, 100).

�Show Clips With Transform Effects: Filters all clips with altered Transform settings.

�Show Clips With Filters: Filters all clips with Resolve FX or OFX filters applied to them.

�Show Stills and Freeze Frames: Filters all clips that are stills or that have freeze frame speed

effects applied to them.

�Show Compound Clips and Nested Timelines: Filters all compound clips and nested timelines in

the Timeline.

�Show VFX Connect Clips: Filters all Fusion Connect Clips.

Exporting the Edit Index

If you’ve filtered a series of edits in the Edit Index that you’d like to share with someone else, this

is easy to do. For example, you might filter the Edit Index to show a list of all the offline clips in the

current timeline, and then export a list as either a .csv or .txt file to give to your assistant editor so they

can chase down the necessary media. Both types of files are widely compatible with spreadsheet and

database software in the event you want to import the data into another application.


Edit | Chapter 33 Using the Edit Page

EDIT

To export the Edit Index:


Click on the Edit Index option menu, and choose Export Edit Index from the contextual menu.


Use the Export Edit Index window to choose a location to save the exported file, and choose a

format from the drop-down menu at the bottom. You can export either a Comma Separated Values

(.csv) file, or a Tab Delimited Values (.txt) file.


Click Save.

Tracks

Several of the most common track controls can be found together in the Track Index. The Track Index

is accessed by clicking on the Index Pane, and selecting the Tracks Tab. The index shows all the

current tracks in your timeline and their position and attributes. These are all modifiable right inside the

Track Index.

The Tracks Index

Tracks Index Columns

Each track reveals several columns of information. These columns can be rearranged by dragging the

column headers to the left or right, depending on what information is most important to you. Clicking

on a track row selects the track for modification.

The available columns of information are:

�Color: The current color of the track is shown. Right-click anywhere in the row and choose Change

Track Color to choose a new one.

�#: Displays the current track order. You can rearrange the order of the tracks by dragging the

number in this column up or down in the track hierarchy and releasing the mouse button. Note that

the actual absolute track number (V1, A1, etc.) does not change, but the track that is assigned to

that number will have changed.

�Name: The name of the Track. You can click in this field to rename the track.

�Track Controls: The same track controls that are found in the Track Header in the Timeline

can also be accessed here: Lock/Unlock, Auto Track Select, Disable/Enable Video Track,

Solo, and Mute.

�Format (audio track only): Shows the current format of the audio track. You can change this format

to any other by right-clicking anywhere in the row of an audio track and choosing Change Track

Type to, and then selecting a new format from the contextual menu.

�Monitor (audio track only): Selects which tracks can be selected in the monitor drop-down menu

in the upper right of the Edit Timeline or Fairlight page windows.

�ADC (audio track only): Checking this box turns on Automatic Delay Compensation (ADC)

for the track.


Edit | Chapter 33 Using the Edit Page

EDIT

Right-clicking on a track or multiple tracks in the track index allows you to delete all selected

tracks by choosing Delete Tracks from the contextual menu.

Clicking on the Tracks Index’s option menu lets you include or exclude track types (video,

audio, subtitle) from the tracks.