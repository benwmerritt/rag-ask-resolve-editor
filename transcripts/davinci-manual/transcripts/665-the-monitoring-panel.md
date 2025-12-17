---
title: "The Monitoring Panel"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 665
---

# The Monitoring Panel

The Monitoring panel that runs along the top of the Fairlight page shows all of the audio meters

corresponding to the tracks in the Timeline, as well as the Master Output meter, Control Room meters,

and a video viewer.

The Monitoring panel

At left, a row of audio meters corresponds to the channel strips of the Mixer, one meter for every audio

track in the Timeline. Each track meter displays the number of channels that corresponds to that track’s

audio format, with mono tracks having a single audio meter, stereo tracks having two, 5.1 tracks having

six, and so on. All of these track and bus meters (with the exception of the Loudness meters) display

both peak and RMS (root mean square) levels against a dB scale.

To the right of the Track meters are the Bus meters, where all busses appear separated by type, each

displaying a meter with the number channels that corresponds to the bus’s audio format. This way you

can see the sum of all tracks that have been routed to a particular bus.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

The last set of meters, to the right of all others, are the Loudness meters, which consist of two sets of

meters and a numerical readout section. The Control Room meter reflects that main output level from

the program and the Loudness meter measures the mix’s loudness according to the user’s chosen

scale. This lets you keep track of the “integrated loudness” of the overall mix, which is the standard

that all contemporary mixing specifications refer to when specifying client deliverables.

The height of the monitoring panel can be adjusted by dragging the bottom of the panel.

Absolute and Relative Measurement Scales

While some users prefer to measure their levels to correspond to a relative scale of “0,” similar to

a VU meter where the needle rides above the “0,” others want to see the absolute measure of the

amplitude in LUFS and true peak. By default, the Loudness meter is set to relative scale, but you now

have the option to choose between relative scale and absolute scale in the Loudness meter.

Relative scale in the Loudness menu is relative to the selected scale, so a loudness unit of 0

corresponds to the target of the chosen measure type. For instance, if EBU R128 is selected, whose

target measure is -23dB LUFS, the “0” LU (Loudness Unit) is equal to -23dB. If ATSC A/85 is chosen,

whose target is -24dB, then that becomes the corresponding equivalent of the relative LU of 0.

When using the absolute scale, the Loudness meter displays the increments to reflect the chosen

measure type. In absolute scale the EBU R128 meter will display -23 instead of the relative scale’s 0.

The option in the Loudness panel reveals the various measure

types as well as the option for absolute scale.

When working with large track counts, you can right-click on the panel and see a contextual menu that

offers options for single or dual rows, as well as narrow or wide meters. You can also double click on

the bus master meters on the right side to access a double row view for them.

The double height Monitoring panel


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Viewer

A small viewer at the far right of the Monitoring panel allows you to view video playback; it always

shows the matching video frame at the position of the playhead.

�The viewer can be resized within the monitoring panel by dragging the left or lower edge of

its window.

�A button in the lower right-hand corner lets you expand the Viewer into its own floating window.

�The Fairlight page has Cinema Mode viewing (Command-F) or through the Workspace menu,

Workspace > Viewer Mode > Cinema Viewer.

�You can also use the Clean Feed mode view on a separate monitor by choosing Workspace >

Video Clean Feed and choosing the target monitor for dedicated video playback.

�You can choose to turn the Viewer off entirely in the Workspace > Fairlight Viewer submenu.

The Monitoring panel

The Media Pool

In the Fairlight page, the Media Pool serves as the repository of all audio clips in your project, both

clips that appear within the Timeline, and clips that you’ve added to your project but have not yet used.

When you record audio into the Timeline, the resulting clips appear in the Media Pool as well, for future

use. The Media Pool appears on all DaVinci Resolve pages, and contains all of the video clips and

timelines within your project.

The Bin list at the left shows a hierarchical list of folders called bins used for organizing your media,

which can also used to organize your timelines. By default, the Media Pool consists of a single bin,

named “Master,” but you can add more bins as necessary to organize timelines and clips by right-

clicking anywhere in the empty area of the Media Pool and choosing Add Bin. You can rename any bin

by double-clicking on its name and typing a new one, or by right-clicking a bin’s name and choosing

Rename Bin. The Bin list can be hidden or shown via the button at the upper left-hand corner of the

Fairlight page toolbar.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

The Media Pool in Thumbnail mode showing audio clips

The browser area to the right shows the contents of the currently selected bin in the bin list. Every

clip you import, every timeline you create, and every AAF, XML, EDL and other file types you can

import appear here. You can create or import as many timelines as you need within a single project.

As elsewhere, the Media Pool can be displayed in either Metadata view, Thumbnail view, or List view.

In List view, you can sort the contents by any one of a subset of the total metadata that’s available

in the Metadata Editor of the Media page. Of particular interest to audio editors are columns for Clip

Name, Reel Name, different timecode streams, Audio Channels, Format, Audio Codec, Date Added,

Flags, and Duration.

For more information on using all of the features of the Media Pool, see Chapter 18, “Adding

and Organizing Media with the Media Pool.” In the following sections, some key features of

the Media Pool are summarized for your convenience.

Importing Media Into the Media Pool on the Fairlight Page

While adding clips to the Media Pool in the Media page provides the most organizational flexibility and

features, if you find yourself in the Fairlight (or other) pages and you need to quickly import a few clips

for immediate use, you can do so in a few different ways.

Add media by dragging one or more clips from the Finder to the

Fairlight page Media Pool (macOS only):


Select one or more clips in the Finder.


Drag those clips into the Media Pool of DaVinci Resolve, or to a bin in the Bin list.

Those clips are added to the Media Pool of your project.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Use the File > Import > Media command:


With the Fairlight page open, choose File > Import > Media.


Use the Import dialog to select one or more clips to import, and click Open.

Use the Import Media command in the Fairlight page Media Pool:


With the Fairlight page open, right-click anywhere in the Media Pool, and choose Import Media.


Use the Import dialog to select one or more clips to import, and click Open.

Those clips are added to the Media Pool of your project.

For more information on importing media using the myriad features of the Media page,

see Chapter 18, “Adding and Organizing Media with the Media Pool.”

Media Pool Preview Player

The Media Pool has a preview player at the top that provides a place to open selected source clips in

the Media Pool, play them, add marks to log them, and set In and Out points in preparation for editing

them into the Timeline via drag and drop. The Media Pool Preview Player effectively acts as a Source

monitor for editing in the Fairlight page.

The preview player in the Media Pool

�Various viewing controls populate the title bar at the top. A dropdown menu at the upper left lets

you choose a zoom level for the audio waveform that’s displayed. To the right of that, a Timecode

window shows you the duration of the clip or the duration that’s marked with In and Out points.

Next to the right, a real-time performance indicator shows you playback performance. In the

center, the title of the currently selected clip is shown, with a dropdown menu to the right that

shows you the most recent 10 clips you’ve browsed. To the far right, a Timecode field shows you

the current position of the playhead (right-clicking this opens a contextual menu with options to

change the timecode that’s displayed, and to copy and paste timecode).

�The center of the Media Pool Preview Player shows you the waveforms in all channels of the

currently selected clip, at whatever zoom level is currently selected.

�Transport controls at the bottom consist of a jog bar for scrubbing, Stop, Play, and Loop buttons,

and set In and Out buttons.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT