---
title: "Markers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 125
---

# Markers

You can use the Marker Index to easily view, edit, and organize all your timeline and clip markers in

one convenient location. The Marker Index can be found by clicking on the Index panel and selecting

the Markers tab.

Methods of working with markers in the Marker Index:

�To filter markers in the Marker Index: Click the Option menu of the Marker Index, and choose

Show All or Show Only to choose a specific color. Each clip with a matching marker appears in

a list, with columns corresponding to the color(s), information, and notes of each timeline and

clip marker. Columns can be sorted in ascending or descending order by clicking on the column

header. Individual columns can be turned on or off by right-clicking on the column header and

checking or unchecking the column name.

�To move the playhead to the position of a marker in the Marker Index: Double-click that marker’s

entry in the list.

�To edit marker information: You can change the values of a marker by clicking in the Name,

Notes, or Keyword fields and modifying the text field. Other values are not editable in the Marker

Index and should be changed in the timeline marker’s Edit dialog.

�To search for a specific marker: Click on the Search icon (magnifying glass), and type in your

search terms. Currently the search only queries the Marker Name column; you cannot search by

notes and keywords.

�To switch between Thumbnail and List view: Click on either the Thumbnail or List View icons in

the top bar of the Marker Index.

The Marker Index in List View mode lets you edit

and organize all your timeline’s markers in one place.


Edit | Chapter 33 Using the Edit Page

EDIT

Source and Timeline Viewers

By default, the Edit page presents a traditional source/record style editing experience. The Source

Viewer lets you view individual clips from the Media Pool to prepare them for editing. Meanwhile, the

Timeline Viewer lets you play through your program, showing you the frame at the position of the

playhead in the Timeline.

Source and Timeline Viewers

You can select either viewer by clicking with the pointer, or by pressing Q (Source/Timeline Viewer),

and the name of the viewer that currently has focus appears in orange.

How Each Clip’s Grade Looks in Each Viewer

Because of DaVinci Resolve’s deep color and effects tools, the state of the image you see in each

viewer of the Edit page depends on a number of things.

The Source Viewer

The Source Viewer shows each clip as it looks at the source. If you have Resolve Color Management

(RCM) turned on or source LUTs applied, then the Source Viewer will show your clips as they’re being

processed by RCM and/or the source LUTs, since those are source-level color operations. However,

in the absence of RCM and source LUTs, the image in the Source Viewer looks exactly the same as it

does on disk. If you have log-encoded media that looks flat and low-contrast, then that’s how it’s going

to look in the Source Viewer.

The Timeline Viewer

The Timeline Viewer follows all of the same rules as the Source Viewer, with the addition that

the Timeline Viewer also shows you how each clip in the Timeline looks with Fusion page and/or

Color page operations applied, since the Timeline Viewer is actually showing you the output of the

Color page, so you can see every clip of your program in context of how the image is being affected

by the DaVinci Resolve image processing pipeline.

NOTE: The Color Viewer Lookup Table options in the Color Management panel of the

Project Settings only affect the GUI Viewer in the Color page. They do not affect the viewers

in the Edit page.


Edit | Chapter 33 Using the Edit Page

EDIT

Turning Grades and/or Fusion Effects Off in the Timeline Viewer

The Bypass Color Grades and Fusion Effects button/drop-down from the Color page is also available

on the Edit page either via the View > Bypass Color and Fusion drop-down, or via a toggle button/

drop-down menu in the Timeline Viewer. If you choose Bypass All Grades or click the Viewer control,

you’ll turn off whatever is checked in the optional menu, which lets you choose whether or not you

want to bypass both Color and Fusion, or just one or the other.

(Left) Menu commands for bypassing Color and Fusion, (Right) Edit page Timeline Viewer controls

Turning off color grades and Fusion effects is an easy way to improve playback performance on low

power systems when you just need to make a quick set of edits, and it’s also a convenient way to

quickly evaluate the original source media.

Timecode Toolbar on Edit Viewers

You can enable the same Timecode toolbar from the Media page in the Edit page. In the Edit page

Source or Timeline Viewer, select the Option (3-dot) menu, and select Show Timecode Toolbar

from the drop-down. The Timecode Toolbar shows the In/Out point timecodes, as well as the total

duration set.

The Timecode toolbar activated in the Source monitor

Source and Timeline Viewers vs. Single Viewer Mode

If you want to change the Edit page layout to hide the Source Viewer, you can choose Workspace >

Single Viewer Mode to instead use just a single viewer to contextually display either a selected Source

Clip or the current frame of the Timeline.

In Single Viewer mode, whatever you select in the Media Pool or Timeline determines which controls

appear in the Viewer, which lets you do nearly everything you can do with two simultaneously

open viewers.


Edit | Chapter 33 Using the Edit Page

EDIT

Single Viewer mode turned on

Previous and Next Clips or Timelines in Viewers

In the Viewer’s Option (3-dot) menu in the Media. Edit and Color pages, you can navigate to the recent

next/previous clip or timeline directly from the submenu.

Edit page Source Viewer: Previous/Next Clip

Edit page Timeline Viewer: Previous/Next Timeline

Selecting the next clip from the Viewer Option menu


Edit | Chapter 33 Using the Edit Page

EDIT

Viewer Controls

Both viewers share the following onscreen controls:

�Zoom drop-down menu: Choosing Fit fits the currently visible frame to the available size of the

Viewer. Choosing a percentage zooms the visible frame to that size. You can also use the scroll

wheel functionality of your mouse, trackpad, or tablet to zoom in and out of the Viewer..

�Duration field: At the top left-hand side of the Source Viewer, this displays the total duration of the

clip, or the duration from the In to the Out point, if these have been placed. In the Timeline tab, this

displays the total duration of the currently selected timeline.

�GPU Status Display: Every viewer in DaVinci Resolve exposes a GPU status indicator and a

frame-per-second (FPS) meter, which appears in the Viewer’s title bar, which shows you your

workstation’s performance whenever playback is initiated. Since DaVinci Resolve uses one or

more GPUs (graphics processing units) to handle all image processing and effects, the GPU status

display shows you how much processing power is being used by whichever clip is playing.

�Clip Name: The clip name is displayed at the center of the Source Viewer title bar.

The Source Viewer: Displays a drop-down at the top of the Source Viewer, next to the name

of the currently open clip, which lets you open a menu containing a list of the last 10 clips you

opened in the Source Viewer. This list is first in, first out, with the most recently opened clips

appearing at the top. If you wish to clear the visual history in the menu, you can remove unwanted

entires and start a new queue by clicking on the Viewer’s option menu and selecting Clear

Recently Viewed Clips.

The Timeline Viewer: Displays the timeline name and is also a drop-down menu that lets you

switch among other timelines in the current project. The clip/timeline name is highlighted orange

when either the Source or Timeline Viewer has focus.

�Bypass Color Grades and Fusion Effects: The Bypass Color Grades and Fusion Effects button/

drop-down from the Color page is also available on the Edit page either via the View > Bypass

Color and Fusion drop-down, or via a toggle button/drop-down menu in the Timeline Viewer.

Turning off color grades and Fusion effects is an easy way to improve playback performance on

low power systems when you just need to make a quick set of edits, and it’s also a convenient way

to quickly evaluate the original source media.

�Source/Timeline Timecode/Frame/Keykode Display: At the top right-hand side of the Source

Viewer, this field shows the timecode of the current frame at the position of the playhead in the

Source Viewer’s jog bar, and can be switched between source timecode, source frame, and

keykode by right-clicking and choosing from the contextual menu. In the Timeline Viewer, this field

shows the record timecode of the current frame at the position of the playhead in the Timeline,

and can be switched between source and record timecode, source and record frames, and

keykode by right-clicking and choosing from the contextual menu.

�Source Viewer Option menu: Contains the following commands:

Gang Viewers: With Gang Viewers enabled, the movement of the Source and Timeline Viewer

playheads is locked together, so that they move in unison. This is useful when you’re matching the

timing of part of a clip in the Source Viewer to match an event in the Timeline.

Live Media Preview: Enabled by default, makes it possible for thumbnails that you’re skimming

in the Media Pool to show the skimmed frame in the Viewer. When skimming with Live Media

Preview enabled, the playhead that appears in the thumbnail is locked to the playhead displayed

in the Viewer’s jog bar.

Show Timecode Toolbar: The Timecode toolbar shows the In/Out point timecodes, as well as the

total duration set.


Edit | Chapter 33 Using the Edit Page

EDIT

Show All Video Frames: When available processing power is insufficient to play the clip or

clips at the position of the playhead due to the grade, transforms, or effects that are applied

at that moment in the Timeline, you have the ability to choose exactly how performance in

DaVinci Resolve degrades. When off, DaVinci Resolve prioritizes audio playback at the expense of

dropping video frames when processing power is tight, resulting in a more conventional playback

experience. When on, audio quality is compromised while every frame of video plays in slower-

than-real time to maintain playback.

Show Zoomed Audio Waveform: When enabled, shows an audio waveform overlay at the

bottom of the Source Viewer with a zoomed in section of the audio surrounding the current

position of the playhead.

Show Full Clip Audio Waveform: When enabled, shows an audio waveform overlay at the bottom

of the Source Viewer that displays the audio over the entire duration of the clip.

Previous Clip: Goes to the previous clip in the Media Pool.

Next Clip: Goes to the next clip in the Media Pool.

Clear Recently Viewed Clips: Clears the memory of the recent clips in the Source Viewer.

Show Marker Overlays: Enabled by default, markers that intercept the playhead when playback is

paused appear superimposed in the Viewer.

Markers submenu: When one or more markers are applied to the clip in the Source Viewer, they

appear in this list in chronological order, listed by Name and Note. Choosing a marker from this

menu jumps the playhead to that marker in the Source Viewer.

�Timeline Viewer Option menu: Contains the following commands:

Gang Viewers: With Gang Viewers enabled, the movement of the Source and Timeline Viewer

playheads is locked together, so that they move in unison. This is useful when you’re matching the

timing of part of a clip in the Source Viewer to match an event in the Timeline.

Show All Video Frames: When available processing power is insufficient to play the clip or

clips at the position of the playhead due to the grade, transforms, or effects that are applied

at that moment in the Timeline, you have the ability to choose exactly how performance in

DaVinci Resolve degrades. When off, DaVinci Resolve prioritizes audio playback at the expense of

dropping video frames when processing power is tight, resulting in a more conventional playback

experience. When on, audio quality is compromised while every frame of video plays in slower-

than-real time to maintain playback.

Show Timecode Toolbar: The Timecode toolbar shows the In/Out point timecodes, as well

as the total duration set.

Timeline Sort Order: These options allow you to set the sort order that timelines use in the

timeline selector in the top middle of the Viewer. Options are: Alphabetical, Creation Date, or

Recently Used (shows the last 10 actively used timelines).

Previous Timeline: Goes to the previous timeline in the Media Pool.

Next Timeline: Goes to the next timeline in the Media Pool.

Show Marker Overlays: Enabled by default, markers that intercept the playhead when

playback is paused appear superimposed in the Viewer.

Show Timecode Overlays: When enabled, shows the source timecode of the video and audio

clips under the position of the playhead when playback is paused.

Show Overlays During Playback: When enabled, shows timecode and marker overlays

on the Viewer constantly during playback. When disabled, overlays are only visible while

playback is paused.

Markers submenu: When one or more markers are applied to a Timeline, they appear in this list

in chronological order, listed by Name and Note. Choosing a marker from this menu jumps the

playhead to that marker in the Timeline.


Edit | Chapter 33 Using the Edit Page

EDIT

�Source Viewer Mode drop-down (Source Viewer only): This drop-down menu lets you set the

Source Viewer to display different views of the clips you’re working on, depending on what you

need to do.

Source: Shows the video of the currently open clip in the Source Viewer.

Offline Reference Movie button: If you’ve assigned an offline reference movie to the currently

selected timeline, clicking the Offline Mode button lets you display the offline movie so you can

compare it with the currently open timeline. In this mode, Source and Timeline playback are

synced; an Offset field replaces the duration field, letting you re-sync the offline reference movie,

if necessary.

Audio Track: Shows the audio waveforms corresponding to all channels of the currently open clip

in the Source Viewer. The top of this audio-only view shows the waveform for the entire duration

of the clip, while the main region of the viewer shows a zoomed in section of the audio waveform.

The level of zoom displayed is controlled by the zoom drop-down at the upper left-hand corner of

the Source Viewer.

Multicam: Shows you the multi-angle Multicam Viewer that you can use to switch among different

angles of video and audio while multicam editing a clip in the Timeline.

For more information on multicam editing, see Chapter 42, “Multicam Editing.”

Annotations: Allows you to draw directly onto the current frame to highlight areas for

further attention.

�Transform Mode drop-down (Timeline Viewer Only): This functions as both a toggle switch and a

drop-down menu. Clicking the button control to the left enables or disables onscreen controls that

you can use to transform the clip right in the viewer. Clicking the drop-down control to the right

lets you switch between two modes of transforms:

Transform: Exposes controls for Pan (X) and Tilt (Y), Scale X and Y, and Rotation.

Crop: Exposes controls to crop from the top, bottom, left, and right.

Dynamic Zoom: Shows controls to do quick pan and scan effects on the selected clip.

OpenFX Overlay: Exposes the onscreen controls of an applied OpenFX filter.

Fusion Overlay: Exposes the onscreen controls of an applied Fusion FX or Title filter.

Annotations: Allows you to draw directly onto the current frame to highlight areas for

further attention.

Smart Reframe: Exposes the onscreen controls of the Smart Reframe.

�Jog control: Clicking the Jog control and dragging left and right lets you move slowly through a

clip or the Timeline a frame at a time.

�Transport controls: These controls include, from left to right, Jump to First Frame, Play Reverse,

Stop, Play Forward, Jump to Last Frame.

�Loop Playback: Enables or disables looped playback. Looping is also controllable via the

Playback > Loop/Unloop command (Command-/). When enabled, each playback command loops

back to the beginning when the end of that command’s range is reached. In and Out points in

the Source or Timeline Viewers do not trigger looping. For example, when enabled, the Play

command will play through the entire clip or timeline, and then loop back to the beginning when

the end is reached and start playing automatically. The Play Around command, on the other hand,

will start at the beginning of pre-roll, play through the post-roll, and then immediately loop back

around to the beginning of pre-roll, continuing playback in this manner until you stop it.


Edit | Chapter 33 Using the Edit Page

EDIT

�Match Frame: In the Source Viewer, Match Frame attempts to move the playhead in the Timeline

to match the current frame of the clip in the Source Viewer. In the Record Viewer, Match Frame

opens the Media Pool clip corresponding to the clip at the current position of the playhead into

the Source Viewer, setting In and Out points and the playhead position to match those of the

clip in the Timeline.

�In/Out buttons: Places In and Out points with which to define a range of the clip, or of the

Timeline, in preparation for making different kinds of edits.

�Jog bar: In the Source Viewer, drag within the jog bar to reposition the Source playhead, scrubbing

through the clip. In the Timeline tab, drag to reposition the playhead throughout the entire program.

Transport Controls and Important Playback Controls

While the operation of the main transport controls is probably obvious, there are additional

playback controls of interest to the editor that may not be so readily found.

For more information about transport controls, see Chapter 35, “Preparing Clips for Editing

and Viewer Playback.”