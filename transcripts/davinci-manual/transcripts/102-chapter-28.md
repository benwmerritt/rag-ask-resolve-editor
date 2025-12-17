---
title: "Chapter 28"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 102
---

# Chapter 28

Fast Editing in

the Cut Page

The editing methods in the Cut page have been streamlined for fast editing,

and the interface of this page and the methods of assembling clips together using

different types of edits are designed to be easy to learn and quick to use.

Contents

Creating and Modifying Timelines���������������������������������������������������������������������������������������������������������������������������������������������� 544

Creating New Timelines�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 544

Opening Timelines������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 544

About Tracks in the Cut Page Timeline�������������������������������������������������������������������������������������������������������������������������������������� 544

Enlarging Tracks������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 545

Adding Tracks����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 545

Deleting Tracks�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 545

Navigating Clips in the Viewer and Timeline������������������������������������������������������������������������������������������������������������������������� 545

Viewer Options�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 545

Playing Clips and Navigating the Timeline in the Viewer�������������������������������������������������������������������������������������������������� 551

Full Screen Viewer�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 551

Enhanced Viewer���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 552

Scrolling Through the Timeline������������������������������������������������������������������������������������������������������������������������������������������������������ 552

Display Clip Names and Status in the Timeline��������������������������������������������������������������������������������������������������������������������� 553

Scene Cut Detection in the Cut Timeline (Studio Version Only)������������������������������������������������������������������������������������ 553

The Boring Detector���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 553

Setting In and Out Points����������������������������������������������������������������������������������������������������������������������������������������������������������������� 554

Setting In and Out Points Using the Keyboard����������������������������������������������������������������������������������������������������������������������� 554

Setting In and Out Points Using the Pointer���������������������������������������������������������������������������������������������������������������������������� 555

Editing the Duration Field in the Cut Page Viewer��������������������������������������������������������������������������������������������������������������� 556

Change Clip Duration Dialog���������������������������������������������������������������������������������������������������������������������������������������������������������� 556


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Video Only and Audio Only Edits������������������������������������������������������������������������������������������������������������������������������������������������ 557

Drag and Drop Editing����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 558

Append������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 558

Ripple Overwrite����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 558

Overwrite�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 559

Using Cut Page Edit Commands�������������������������������������������������������������������������������������������������������������������������������������������������� 559

Smart Indicators������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 559

Setting Up and Performing Edits��������������������������������������������������������������������������������������������������������������������������������������������������� 560

Smart Insert��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 560

Append������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 561

Ripple Overwrite������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 561

Close Up���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 562

Place On Top������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 562

Source Overwrite���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 563

Overwrite�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 565

Copy, Paste and Remove Attributes from Timeline Clips����������������������������������������������������������������������������������������������� 565

Subtitles���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 566

Subtitles in the Cut Timeline����������������������������������������������������������������������������������������������������������������������������������������������������������� 566

Create Subtitles from Audio (Studio Version Only)��������������������������������������������������������������������������������������������������������������� 566

Source Tape Editing���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 566

Metadata Entry Using the File Inspector����������������������������������������������������������������������������������������������������������������������������������� 566

Using the Source Tape����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 568

Limiting the Source Tape Scope by Folder Structure��������������������������������������������������������������������������������������������������������� 568

Sync Bin Multicam Editing��������������������������������������������������������������������������������������������������������������������������������������������������������������� 570

Preparing Footage for Sync Bin Editing������������������������������������������������������������������������������������������������������������������������������������� 570

Sync Clips Window������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 570

Sync Bin Editing������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 572

Resync Misaligned Synced Clips�������������������������������������������������������������������������������������������������������������������������������������������������� 575

Live Overwrite with a Mouse Drag���������������������������������������������������������������������������������������������������������������������������������������������� 576

Audio Transcription and Text Based Editing (Studio Version Only)���������������������������������������������������������������������������� 577


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Creating and Modifying Timelines

After you’ve imported and organized the media you need to use in a program, the next thing you must

do is create a timeline. Timelines are the organizational entities that contain the edited sequences of

clips that make up your program. You can have as many timelines as you like in your project, with each

timeline being an independent arrangement of clips. Timelines are stored in the Media Pool and can

be organized using bins, just like clips.

Creating New Timelines

A timeline is automatically created when you edit your first clip into the Timeline. You’ll see an icon for

the new timeline in the Media Pool, where you can rename it.

You can also create a new timeline by either choosing File > New Timeline (Command-N), or right-

clicking in the background of the Media Pool and choosing Create New Timeline. A dialog appears

that lets you choose a start timecode (the default is 01:00:00:00), a name, how many video and

audio tracks you want it to have, what kind of audio (the default is stereo), and whether or not you

want to create an empty timeline, or a timeline that automatically includes all clips in the Media

Pool with or without selected In/Out points (a quick and easy way of creating a stringout of all clips

you’ve imported).

By default, all timelines share the same frame rate, resolution, and monitoring settings as the overall

project. If you like, you can also click the Use Custom Settings button to choose individual frame rate,

resolution, and monitoring settings for that timeline.

Once you’ve created a new timeline, double-clicking it will open it into the Timeline Editor.

Opening Timelines

If you only have one timeline in your project, that timeline is always seen in the Timeline Editor.

If you have multiple timelines, you can double-click any timeline in the Media Pool to open it into the

Timeline Editor, ready for editing. You can also switch from working on one timeline to another by

using the drop-down list at the top of the Cut page Viewer. This unifies Viewer Timeline Selection

behavior across the Cut, Edit, Color, and Deliver pages.

The Timeline Selection drop-down at

the top of the Cut page Viewer

The Enlarge, Lock, Audio Enable, and Video

Enable buttons in the header of a timeline track

About Tracks in the Cut Page Timeline

Tracks in the Cut page timeline combine a clip’s audio and video into a single track for convenience,

as this makes it easy to keep audio and video organized and in sync when superimposing many

clips together. This means that tracks have both video and audio enable controls in the track header

controls, so that you can selectively disable video and mute audio when necessary.

Each track also has a lock control, which lets you prevent clips on that track from being

altered in any way.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Enlarging Tracks

Track size can be enlarged and minimized by clicking on the Track Sizing icon on the left side of the

track header. An expanded video track shows a full size video and audio track, if attached. This makes

it easier to see just the track you want to focus on. Only one track can be expanded at a time.

Clicking on the Track Sizing icon expands the track to show the full audio track of the clip

Adding Tracks

If your timeline doesn’t have enough tracks, you can click on the Timeline Actions menu and select

Add Video/Audio/Subtitle track, or right-click anywhere in the Timeline and choose “Add Track,” and a

new track will be added on top of the previously existing tracks.

TIP: Dragging a new clip to the undefined gray area at the top of the Timeline also

adds a new track.

Deleting Tracks

If you want to delete a specific track along with all clips on that track, you can right-click anywhere in

that track’s header and choose “Delete Track.”

If your timeline has too many empty tracks, you can right-click anywhere in the track header and

choose “Delete Empty Tracks” and all empty tracks will be removed.

Navigating Clips in the Viewer and Timeline

Before you can start editing, you need to find which parts of which clips you want to use and define

where in the currently open timeline you want to make an edit. The Single Viewer in the Cut page has

different options that let you choose what media you want to play through using the transport controls

found at the bottom.

Viewer Options

Three options, selectable via buttons at the upper left of the Viewer, let you control what the

Viewer shows.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

The Viewer option buttons (left to right): Source Clip,

Source Tape, Timeline, and Multi Source

Source Clip

This option shows the currently selected clip in the Media Pool. This is the mode the Viewer

automatically switches to whenever you double-click a clip in the Media Pool. In Source Clip, a scroll

area appears at the bottom of the Viewer, the width of which represents the duration of the currently

open clip. A playhead within the scroll area lets you scrub through the clip as a zoomed-in waveform

and shows whatever audio is playing within the clip. Handles to the left and right of the scroll area let

you reposition In and Out points within the clip to choose a section you want to edit into the Timeline.

These In and Out points can also be set using the I and O keys. Once set, you can drag In and Out

points to change them.

The Viewer showing Source Clip

The scroll area in Source Clip option, with In and Out points positioned to either side of the playhead

Source Tape

Using this option, every single clip in the currently open bin, and any subfolders in that bin, of the

Media Pool is shown in the Viewer as a “stringout” in the scroll area at the bottom of the Viewer. In the

scroll area, each clip appears one after the other in a long strip, with the order determined by the Sort

order. This makes it easy to scrub through a whole collection of clips while you’re figuring out what you

want to use. As you play through, whichever clip the playhead intersects is selected in the Media Pool,

so you know which clip you’re looking at.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT


The Viewer showing Source Tape

The scroll area in the Source Tape, with each clip separated by a thin line

Timeline

This option shows the current frame at the position of the playhead in the Timeline. Whenever you

click, drag, or adjust a clip in the timeline area, the Viewer switches to the Timeline. In this option there

is no scroll area; you must use the timeline area to scrub through your program. However, in the space

where the scroll area would otherwise be, icons appear to indicate when the playhead is positioned at

the first or last frame of a clip in the Timeline.

The Viewer showing the Timeline


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Multi Source

If you have multiple clips that are synced either by timecode or waveform, you can view them all at

once, even across multiple bins in your project. Choosing this option opens up the Multi Source viewer

in the Source Tape. It will lay out all synced media in a grid, and all media is ganged together as you

scrub through. Setting In and Out points in this mode are constant across the different angles, so you

can switch cameras and the same In and Out points you set remain valid on each clip. These features

let you quickly choose the best angle for a multi-camera shoot.

The Viewer showing the Multi Source

In and Out points set in the Multi Source. These points remain set when you switch camera angles.

The right side Viewer controls (left to right): Safe Area, Proxy Handling,

Timeline Resolution, and Bypass Color Grades and Fusion

Safe Area

This drop-down menu overlays many useful framing guides over the Viewer to let you see what part of

the image will be included and what will part will be cropped out if you change the Timeline’s aspect

ratio. The framing guides can be turned on and off by toggling the Safe Area Framing Guide icon in the

Viewer, and the exact guides can be selected in the drop-down menu.

Social Media: 1:1, 4:5, 9:16, 1.91:1, 16:9.

Broadcast and Film: Default (your current timeline aspect ratio), 1.33, 1.66, 1.77, 1.85, 2.35.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Safe Area Guides: These options add additional guide lines on the Viewer to protect your

composition from possibly being cut off at the extreme edges of a physical cathode ray tube.

While somewhat anachronistic in this age of flat screen digital televisions, many legacy programs

still adhere to these guidelines. Safe Areas still can be useful guides in ensuring your image is not

inadvertently cropped by the variety of mobile devices and social media sites in use today.

Action: Keep all movement and important action within this box.

Title: Keep all on screen text within this box.

Center: Designates the exact middle of the image.

The Safe Area Framing Guide icon (circled)

and the possible framing options

Proxy Handling

You can switch between using your original source media and the proxy media for playback in the

Cut page by using the Proxy Handling icon in the Viewer, and selecting one of the following options:

Disable All Proxies: This option disables the proxies altogether and forces the original media playback

only. If the original media is not available, the clip is replaced with a Media Offline graphic.

Prefer Proxies: This option will use proxies files for playback, and if there is no proxy file for a clip, the

original media will automatically be used instead.

Prefer Camera Originals: This option will use the original media files for playback, and if there is no

original media file for a clip, the proxy media will automatically be used instead.

The Proxy Handling icon in the Cut page Viewer

lets you select how you want to use proxy files.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Timeline Resolution

This drop-down menu, to the top-right of the Viewer, lets you quickly choose which resolution you

want to work at. A Custom option lets you open up the Timeline Settings panel in order to choose your

own options.

For more information about the Timeline Settings, see Chapter 6, “Project Settings.”

The Project Settings quick menu

Bypass Color Grades and Fusion

The Bypass Color Grades and Fusion Effects button/drop-down lets you turn off all grades and

effects that you may have applied in the Color page and/or Fusion page in order to improve playback

performance on low power computers. Click the button (Shift-D) to disable or reenable grading and

effects, or right‑click this button to access a menu that lets you choose which things you want this

button to control.

The Bypass Grades and Fusion button, shown

being right-clicked to view its options


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Playing Clips and Navigating the Timeline in the Viewer

Eight controls sit at the bottom of the Viewer. These let you play through and otherwise navigate clips

and the Timeline in different ways. These controls are described from left to right.

The toolbar at the bottom of the Viewer

�Tools button: The Tools button reveals a variety of controls for transform, crop, audio, speed

effects, camera stabilization and lens correction, dynamic zoom, and compositing, covered in

more detail later in this chapter.

�POI and Add POI: These tools are used for selecting and modifying Points of Interest in Replay,

which is described in its own manual. For more information on these tools, see the “DaVinci

Resolve Replay Editor Instruction Manual.”

�Fast Review button: Intended to help you watch through a large collection of media quickly,

clicking this button begins accelerated playback through the Source Tape or through the Timeline,

where the speed of playback is relative to the length of each clip you’re playing through. Long

clips play faster, whereas shorter clips play closer to real time. In this way, you can watch a lot of

material really quickly.

�Jog control: Clicking and dragging within the jog control lets you scrub very precisely through the

content of the Viewer.

�Transport controls: A set of buttons provide clickable controls to control playback of source clips

and the Timeline, whichever the Viewer is set to display; each button has a matching keyboard

shortcut. These include Previous Edit (Up Arrow), Stop (Spacebar), Play (Spacebar), Next Edit

(Down Arrow), and Loop Playback (Command /).

�Mark In/Out: Clickable controls to set In and Out points respectively.

�Playhead timecode: A number field shows you the timecode value at the playhead of a clip or

of the Timeline, to give you a numeric reference for where you are. There is also a dedicated

timecode entry mode for the Cut page. There are three ways of telling DaVinci Resolve that you

want to perform a timecode action, regardless of what the numeric keypad keys are assigned to in

the Keyboard Customization preferences.

�Select Playback > Goto > Timecode (=) and enter your timecode value.

�Press “+” or “-“ keys, and enter your timecode value to move the current position

forward or backward by that amount.

�Click on the Timeline Timecode display on the Viewer, and enter your timecode value.