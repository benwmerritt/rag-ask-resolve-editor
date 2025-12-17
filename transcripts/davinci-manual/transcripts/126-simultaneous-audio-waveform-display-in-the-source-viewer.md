---
title: "Simultaneous Audio Waveform Display in the Source Viewer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 126
---

# Simultaneous Audio Waveform Display in the Source Viewer

When the Source Viewer is set to Source, two options in the Option menu let you see a superimposed

audio waveform running along the bottom of the viewer, over the video of the currently selected clip.

Show Zoomed Audio Waveform: Shows a zoomed-in section of audio that scrolls as you play

the clip. Useful for seeing dialog and music cues as you play through a clip.

Show Full Clip Audio Waveform: Shows the audio waveform for the entire source media of

that clip. The section of audio from the In to Out points you’ve set in the Source Viewer are

highlighted. Useful for using the audio waveform to navigate throughout that clip using the

waveform as a reference.

The Source Viewer with “Show Full Clip Audio Waveform” enabled


Edit | Chapter 33 Using the Edit Page

EDIT

Cinema Viewer Mode

You can also put either the Source or Timeline Viewers into Cinema Viewer mode by choosing

Workspace > Viewer Mode > Cinema Viewer (P), causing whichever viewer is currently selected to fill

the entire screen, which is good for doing a test viewing of your edit without the distractions of the

DaVinci Resolve Edit Page UI. This command toggles Cinema Viewer mode on and off.

Viewer Indicators

Certain frames trigger visible indicators in either the Source or Timeline viewers. For example, if the

playhead is at the very first or last frame of media available to a particular clip, indicators appear in the

lower-left or right corner of the frame to let you know there’s no more media in that direction.

The first and last frame

clip indicators

If the playhead in the Timeline is on the first frame of black immediately after the last video clip

in the Timeline, an end of sequence indicator appears in the Timeline Viewer to let you know

that you’re viewing the last frame of the current sequence of clips, even though the playhead

is actually on a frame of black. This makes it easy to see what you’re doing while you’re first

assembling clips together.

The end-of-sequence indicator

Other Viewer Options

There are additional overlays and options you can use to customize how the viewer appears.

�Safe Area and Guides: In the upper‑right corner of the Timeline Viewer, you can turn on and

select one or multiple Safe Area guides to be overlayed on the Viewer.

This allows you to easily see if the important action in the frame still is composed adequately for

different delivery requirements.


Edit | Chapter 33 Using the Edit Page

EDIT

�Show Checkerboard, Black, Gray, or Alert Red Backgrounds in Viewers: Selecting Viewer

Background in the Timeline View options changes the empty area of the Viewer (if there is any)

to the selected option, making it easier to see which parts of the Viewer are black because of

blanking and which parts are simply empty because of the way the image is zoomed or panned.

The Safe Area selector

Fast Review in the Timeline Viewer

Fast Review plays back your timeline at variable fast forward speeds where the speed of playback is

dependent on the length of each clip on the Timeline. Longer clips play back at faster speeds than

shorter ones. This feature is designed to allow you to quickly scan through a large amount of material

on a timeline.

To use the Fast Review feature on your Edit page Timeline, select Playback > Fast Review. Pressing K

or the spacebar will return you to the normal JKL playback mode. If you use this feature often you can

bind Fast Review to a specific key in the Keyboard Customization window.

NOTE: Fast Review does not work for clips in the Source Viewer, only for timelines in the

Timeline Viewer.

Opening Clips in the Source Viewer

There are two methods of opening clips into the Source Viewer. Which is enabled depends on the

“Live Media Preview” setting found in the Viewer options menu (the three-dots menu found at the

upper right-hand corner of the Viewer).

�When Live Media Preview is enabled (by default), skimming a thumbnail in the Media Pool also

shows the skimmed frame in the Source Viewer, effectively opening each clip you skim in the

Media Pool into the Source Viewer. As you skim, the playhead that appears in the thumbnail is

locked to the playhead that’s displayed in the Viewer’s jog bar.

�When Live Media Preview is disabled, you must either double-click a clip in the Media Pool to

open it into the Source Viewer, or you can select a clip in the Media Pool and press the Return key

to open it into the Source Viewer.

Which method is best is purely a matter of preference.


Edit | Chapter 33 Using the Edit Page

EDIT

Timeline Viewer Edit Overlays

Dragging a clip from the Media Pool or Source Viewer onto the Timeline Viewer also exposes edit

overlays that let you choose what kind of edit you want to make by choosing which overlay to drop

the clip onto.

The overlay that appears when you drag a clip onto the

Timeline Viewer lets you choose from a variety of edits

This overlay exposes every type of edit that’s available in DaVinci Resolve, including the Insert,

Overwrite, Replace, Fit to Fill, Place On Top, Ripple Overwrite, and Append at End edits, all of which

are also available from the Edit menu. It’s a useful method of making three-point edits if you like drag

and drop editing, but it also provides a nice reminder of what types of edits are available, given all the

different options that are available.

By default, the larger empty area to the left of these overlays defaults to the highlighted Overwrite

overlay, while all the smaller buttons let you perform each of the other edit types that are available.

However, the “Timeline overlay retains the last performed action” checkbox in the Editing panel of the

User Preferences can be turned on if you want DaVinci Resolve to always remember the last edit type

you used, and highlight it on this overlay whenever you drag another clip over the Timeline Viewer to

let you know that the last edit you performed is the new default edit if you drop clips to the left of the

overlay. For example, with this option enabled, if you perform a place on top edit, then the next time

you drop a clip into the empty area to the left of the overlays, the result will be another place on top

edit. This option is off by default.

Copy and Paste Timecode in Viewer Timecode Fields

You can right-click on most Viewer timecode fields in the Media, Edit, and Color pages to choose

Copy and Paste commands from a contextual menu for copying and pasting timecode values. You

can also click in the timecode fields and use the normal Copy (Command-C), and Paste (Command-V)

keyboard commands. This works even between pages. The timecode value you’re pasting must be

valid timecode, for example you can’t paste 0 hour timecode onto a 1 hour timeline.


Edit | Chapter 33 Using the Edit Page

EDIT

Right-clicking on a timecode field to use the Copy Timecode command

Export The Current Frame from The Viewer

You can now export a still frame from the Viewer in the Media, Cut, and Edit pages.

To Export a Still Frame from the Viewer:


Select either the Source or Timeline viewer for export.


Use the Viewer’s playback controls to navigate to the frame you want to export.


Select File > Export > Current Frame as Still.


Enter the name of the still frame in the File System viewer.


Enter the desired format of the still frame in the File System viewer.


Click on the Export button.

Metadata Editor

Both the Media and Edit pages have a Metadata Editor. In the Edit page, the Metadata Editor opens

in the same place as the Inspector, to the right of the Source and Timeline Viewers. When you select

a clip in the Media Pool or Timeline, its metadata is displayed within the Metadata Editor, and the title

bar indicates whether you’re evaluating a clip in the Timeline or Media Pool. If you select multiple clips,

only the last clip’s information appears. The Metadata Editor’s header contains uneditable information

about the selected clip, including the file name, directory, duration, frame rate, resolution, and codec.

Because there are so very many metadata fields available, two drop-down menus at the top

let you change which set of metadata is displayed in the Metadata Editor.

Metadata Presets (to the left): If you’ve used the Metadata panel of the User Preferences to

create your own custom sets of metadata, you can use this drop-down to choose which one to

expose. Surprisingly enough, this is set to “Default” by default.

Metadata Groups (to the right): This drop-down menu lets you switch among the various

groups of metadata that are available, grouped for specific tasks or workflows.

The heart of the Metadata Editor is a series of editable fields underneath the header that let

you review and edit the different metadata criteria that are available.

For more information on editing clip metadata, and on creating custom metadata presets, see

Chapter 19, “Using Clip Metadata.”


Edit | Chapter 33 Using the Edit Page

EDIT

Clip Metadata Editor

showing the Clip

Details panel for a

clip in the Timeline