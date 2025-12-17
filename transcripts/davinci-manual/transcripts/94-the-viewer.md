---
title: "The Viewer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 94
---

# The Viewer

The Viewer lets you see clips from the Media Pool, or clips in the Timeline, and has numerous controls

to control what you see and how things play.

The single Viewer in the Cut page


The Cut Page | Chapter 26 Using the Cut Page

CUT

The Viewer has four mode options. Which option is currently in use can be seen, and switched,

by four buttons in the upper lefthand corner of the Viewer.

The Viewer modes buttons

The Different options are entered automatically by various actions (from left to right):

•	 You can double-click any clip to open it into the Viewer as a Source Clip.

•	 You can view an entire bin full of clips in the Source Tape.

•	 You can play your edited program in the Timeline.

•	 You can see all of your synced material at the same time in the Multi Source viewer.

Playing Clips and Navigating the Timeline

Several controls sit at the bottom of the Viewer. These let you play through and otherwise navigate

clips and the Timeline in different ways. These controls are described from left to right.

The toolbar at the bottom of the Viewer

�Tools button: The Tools button reveals a variety of controls for transform, crop, audio, speed

effects, camera stabilization and lens correction, dynamic zoom, and compositing, covered in

more detail later in this chapter.

�Voiceover: Reveals controls for recording voice over directly into the timeline.

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

�Transport controls: A set of Previous Edit (Up Arrow), Stop (Spacebar), Play (Spacebar), Next Edit

(Down Arrow), and Loop Playback (Command-/) buttons constitute clickable controls for controlling

playback of clips and the Timeline. Each button has a matching keyboard shortcut.

�Mark In/Out: Clickable controls to set In and Out points respectively.

�Playhead timecode: A number field shows you the timecode value at the playhead of a clip or of

the Timeline to give you a numeric reference for where you are.


The Cut Page | Chapter 26 Using the Cut Page

CUT

Optimized UI Layouts for Vertical Editing

Optimized layouts for vertical timelines and projects are supported in DaVinci Resolve. When a vertical

timeline or project is loaded, the UI automatically switches to a layout optimized for vertical viewers

on the Cut, Edit, and Color pages. Loading a normal landscape timeline or project then automatically

switches back to the original layout. No additional user intervention is needed.

You can change this behavior in Preferences > User > UI Settings > Use optimized UI layouts

for vertical video. Unchecking this box retains the normal horizontal layout, even for vertical

video timelines.

The UI now changes format to accommodate vertical video timelines automatically.

Tools

Clicking the Tools button reveals a toolbar that you can use to add and edit clip effects, right within

the Viewer with no Inspector needed. The Tools button reveals a variety of controls for transform,

crop, audio, speed effects, camera stabilization and lens correction, dynamic zoom, and compositing,

covered in more detail later in this chapter.

The Tools bar shown opened to the transform controls.


The Cut Page | Chapter 26 Using the Cut Page

CUT

Bypass Color Grades and Fusion

The Bypass Color Grades and Fusion Effects button/drop-down lets you turn off all grades and

effects that you may have applied in the Color page and/or Fusion page in order to improve playback

performance on low power computers. Click the button (Shift-D) to disable or reenable grading and

effects, or right-click this button to access a menu that lets you choose which things you want this

button to control.

The Bypass Grades and Fusion button,

shown being right-clicked to view its options

Export The Current Frame from The Viewer

You can now export a still frame from the Viewer in the Media, Cut, and Edit pages.

To Export a Still Frame from the Viewer:


Use the Viewer’s playback controls to navigate to the frame you want to export.


Select File > Export > Current Frame as Still.


Enter the name of the still frame in the File System viewer.


Enter the desired format of the still frame in the File System viewer.


Click on the Export button.

Audio Meter

An audio meter to the right of the Viewer shows you a graphical

representation of the audio levels playing in the current clip or in the

Timeline as you play through the Viewer, via animated vertical bars that

are tinted to indicate how loud the levels are:

�Green indicates safe levels

�Yellow indicates levels that are peaking at approximately safe levels

�Red indicates levels that may be peaking at levels that are too high,

risking clipping the signal and causing distortion

These animated bars serve as a visual reference you can use to help

you adjust the volume of different clips to create a pleasing balance,

and to make sure you don’t exceed the maximum desired level and

introduce clipping. A speaker button at the top of the meters lets you

mute or unmute audio playback.

The Audio Meter

showing an audio signal


The Cut Page | Chapter 26 Using the Cut Page

CUT

The Timeline

The word “timeline” refers both to an edited sequence of clips, which constitutes a program that is

stored in the Media Pool, and to the area of the Cut page interface where you can open this sequence

of clips to see its contents, and for playback and editing.

Timelines are created and stored in the Media Pool, along with all of your other clips. However, each

timeline is assembled and edited in what is sometimes referred to as the Timeline Editor. Different

pages of DaVinci Resolve show your timeline differently according to the special requirements of each

page focusing variously on different methods of editing, grading, compositing, and audio.

However, while the interface of the Timeline Editor changes from page to page, the actual contents

of the Timeline are identical, because each page’s Timeline Editor is in fact showing the exact same

Timeline that is currently open. This means that the advanced user can use every page of DaVinci to

do different things to the same Timeline, with only the interface changing to make different functions

possible in different pages.

For the Cut page user, the Timeline is divided into an Upper Timeline at the top, and a larger and more

detailed Timeline Editor showing a zoomed in portion of the Timeline around the playhead at the

bottom. Working together, these two views of your edited sequence make it possible to navigate your

entire project and cut in great detail.

The Timeline of the Cut page, comprising the Upper Timeline and the zoomed in Lower Timeline

Upper Timeline

The Upper Timeline always shows the entire program within the full width of your computer’s display.

The Upper Timeline’s playhead is always free, which makes it easy to use your pointer to scroll

around the entire program by dragging within the Timeline Ruler at top. This also serves as a visual

reference for keeping track of where you are in your program while you’re editing within the zoomed-

in Lower Timeline below.

Despite the Upper Timeline’s relatively small size, you can still edit in it, with most editing and

trimming functions that are available in the Lower Timeline also available in the Upper Timeline. Most

interestingly, it’s also possible to drag clips from one part of your program in the Lower Timeline, to

another area of your program in the Upper Timeline, and vice versa. Right-clicking on a clip in the

Upper Timeline will open the same context menu as right-clicking on a clip in the Cut page’s main

timeline, allowing you to perform the same operations.

A set of small numbers to the left of the Upper Timeline lets you click a number to choose the currently

selected track; this selection is mirrored on the zoomed in timeline below. The currently selected track

affects where incoming clips will be placed when editing, among other things.


The Cut Page | Chapter 26 Using the Cut Page

CUT