---
title: "Switching Among Multiple Timelines"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 128
---

# Switching Among Multiple Timelines

Timelines can be organized like any other clip in the Media Pool. To open or switch among timelines,

use the following procedures.

To switch timelines, do one of the following:

•	 Double-click a timeline in the Media Pool on any page.

•	 Turn on Stacked Timelines in the Timeline View Options menu of the Edit page toolbar, so

that all timelines you open appear as tabs. Clicking different tabs switches to that timeline.

•	 In the Edit page Timeline Viewer, choose a timeline from the Timelines drop-down menu at

the top of the viewer.

•	 In the Color page, choose a timeline from the Timelines drop-down menu at the top of

the Viewer.

•	 In the Fairlight page, choose a timeline from the Timelines drop-down menu to the left of the

transport controls.


Edit | Chapter 33 Using the Edit Page

EDIT

Toolbar

At the center of the toolbar that sits above the Timeline, several buttons let you choose different tools

and options for performing various editing functions.

Buttons in the toolbar

Timeline View Options: The controls let you customize the look of the clips on the

tracks (Filmstrip, Thumbnail, or Minimized), audio waveform displays, stacked timelines,

subtitles, and the adjustable height of the video and audio tracks.

Selecting the Timeline View options

Keyframe Editor: Opens the Keyframe Editor in the timeline.

Voiceover: Opens the Voiceover tools to record directly into the timeline.

Selection Mode: The default mode in which you can move and resize clips in the

Timeline, roll edits, and do other basic editing tasks. In this mode, making specific

selections in the Timeline and using the nudge commands of Comma and Period

resizes, moves, or rolls the selection, as does absolute or relative timecode entry.

Trim Edit Mode: In this mode, the Trim tool lets you make slip, slide, ripple, and roll

edits by dragging different parts of clips in the Timeline, by making specific selections

and using the “nudge” keyboard shortcuts of Comma and Period to move the selection

left or right, or by making specific selections and using timecode entry to make relative

or absolute adjustments.

Dynamic Trim Mode: This mode works in conjunction with either the Selection or

Edit modes. With Dynamic Trim mode enabled, you can either resize and move clips

(in Selection mode), or ripple, slip, or slide them (in Trim mode) using the JKL keyboard

shortcuts that play forward and backward through the Timeline. While enabled, the

spacebar triggers the Play Around Current Selection command. The Toolbar button

for this mode also changes to show you whether you’re in slip or slide mode for

nudging, timecode-entry adjustment, or dynamic trim (set by pressing the S key).


Edit | Chapter 33 Using the Edit Page

EDIT

Blade Edit Mode: Lets you add cuts to clips at the playhead in

the Timeline by clicking.

Insert Clip: Performs an insert edit to the Timeline with whatever

clip is in the Source Viewer.

Overwrite Clip: Performs an overwrite edit to the Timeline

with whatever clip is in the Source Viewer.

Replace Clip: Performs a replace edit to the Timeline

with whatever clip is in the Source Viewer.

Snapping: Enables or disables clip snapping. When turned on, clip In and Out points,

markers, and the playhead all snap to one another for reference while you’re editing.

Linked Selection: Enables or disables audio/video linking. When turned on, clicking a

video clip in the Timeline automatically selects the corresponding audio clip if they’re

linked together. When turned off, clicking a video clip won’t select its audio. Clip linking

can be toggled while you work by pressing the Option key while clicking to make

selections in the Timeline.

Position Lock: Prevents clips from being moved to the left or right, and it prevents all

ripple operations. Essentially ensures all the Timeline elements stay in sync and can’t

be adjusted accidentally.

Flag Clip/Flag Colors drop-down menu: Flags identify clips, and indicate all clips

that correspond to the same item of media in the Media Pool. Clips can have multiple

flags. Clicking the Flag button automatically adds a flag to whichever clip is currently

selected in the Timeline. A drop-down menu to the right lets you choose differently

colored flags, and clear all flags from the currently selected clip.

Add Marker/Marker Colors drop-down menu: Markers identify specific frames

of individual clips. Clicking the Add Marker button adds a marker of the currently

displayed color to the clip at the position of the playhead in the Timeline. A drop-down

menu to the right lets you choose differently colored markers, and clear all markers

from the currently selected clip.

Full Extent Zoom: Dynamically adjusts the zoom level to encompass the whole

Timeline as you add or remove clips.

Detail Zoom: Zooms the Timeline in on the Playhead to the frame level.

Custom Zoom: Zooms the Timeline to the level selected by the Zoom slider

to its immediate right.

Zoom Slider: Lets you zoom into or out of the clips in the Timeline. Use the scroll

wheel of your mouse to horizontally zoom into and out of the Timeline. Scrolling up

zooms in, while scrolling down zooms out. You can also use Command-Plus to zoom in,

and Command‑Minus to zoom out, and Shift-Z to fit every clip in your program into the

available width of the Timeline.

These functions are described in greater detail in the following sections of this chapter.


Edit | Chapter 33 Using the Edit Page

EDIT

Toolbar Audio Monitoring Controls

At the far right of the toolbar, a set of three monitoring controls lets you quickly control the output

volume of your mix. An audio Enable/Disable button lets you turn audio playback on and off, while a

slider lets you change the volume, and a DIM button lets you temporarily duck the monitored volume

being output in order to have a quick chat with your client about sports or the state of the world while

keeping half an ear on the mix.

The monitoring controls in the Edit page

When there are multiple audio Mains defined for a project, an additional drop-down dialog appears

with the audio monitoring controls in the toolbar that lets you choose which Main you’re listening to.

The Mixer and Meters

The Audio Mixer provides a set of graphical controls you can use to set track levels, pan stereo audio,

and mute and solo tracks, all while you continue to edit.

The Audio Mixer, with four channel strips

corresponding to the four tracks in the Timeline

To open the Audio Mixer:

�Click the Mixer button on the Interface toolbar.

The Audio Mixer exposes a set of channel strips with

controls that correspond to the tracks in the Timeline,

and each channel strip displays a number of audio

meters equal to the number of channels within that

track. By default, a Main 1 channel strip appears all the

way to the right that lets you adjust the overall level

of the mix. However, if you add subs and mains on

the Fairlight page, those will appear at the right of the

mixer as well.

For more information about the use of the Mixer

in the Edit page, see Chapter 45, “Working with

Audio in the Edit Page.”

For more information about using the Mixer in

the Fairlight page, see Chapter 177, “Mixing in

the Fairlight Page.”


Edit | Chapter 33 Using the Edit Page

EDIT

Displaying Audio Meters

If you just want to see your program’s levels, you can also switch to display the “Control Room”

audio meters instead of the Mixer. How many audio meters appear depends on the current speaker

configuration in the Video and Audio I/O panel of the System Preferences.

To show the Audio Meters:

�Click the Mixer button on the Interface toolbar to display the audio panel, and then choose Meters

from the option menu at the upper right-hand corner.

Using Video Scopes

DaVinci Resolve has a set of four real-time video scopes that you can use to monitor the internal data

levels of clips in your project as you work. Each scope provides an unambiguous graphical analysis

of the various characteristics of the video signal, showing you the relative strength and range of

individual color components including luma, chroma, saturation, hue, and the red, green, and blue

channels that, together, comprise the color and contrast of the images in your program.

To open video scopes from the Media, Cut, Edit, Color, or Deliver pages, do one of the following:

�Choose Workspace > Video Scopes > On/Off (Command-Shift-W) to open video scopes into a

floating window.

�Choose Workspace > Dual Screen > On to open video scopes as part of a dual screen layout.

Video scopes in a floating window

The video scopes aren’t just available in the Color page. They’re also available in the Media, Cut,

Edit, and Deliver pages for whenever you need to evaluate the video signal more objectively,

such as when you’re setting up to capture from tape or scan from film, or when you’re setting up

for output.

For more information on using the video scopes, see Chapter 124, “Using the Color Page.”


Edit | Chapter 33 Using the Edit Page

EDIT