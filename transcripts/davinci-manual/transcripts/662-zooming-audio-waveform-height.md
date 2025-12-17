---
title: "Zooming Audio Waveform Height"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 662
---

# Zooming Audio Waveform Height

You can zoom into or out of the audio waveforms shown in each clip of one or more tracks, to make

them taller or shorter, or you can reset them to their default sizes. This doesn’t change the audio levels

of clips in affected tracks, it just lets you make the audio waveforms easier to see.

To zoom audio waveform height using your scroll wheel:

Hold down Command-Option, and roll the scroll wheel or control up or down to resize all waveforms in

all tracks.

You can also use commands that are accessed in the top menu View > Zoom Audio Waveform for

any track on the Timeline. You can select one or multiple tracks to resize their waveforms all at once.

There are three sets of commands in the menu:

�Reset

�Zoom Increase Height

�Zoom Decrease Height

Right-clicking any clip in the Timeline allows you to access the Track Waveform Zoom submenu with

even more zoom options.

Smart Zoom Track Height

When you select a track in the Timeline or Mixer and press Command-Option-E, Smart Zoom

increases the track height and centers your selection to occupy the whole viewable area of the

Timeline. Once you’ve finished your edits, press Command-Option-E again to close Smart Zoom.

As with other Da Vinci Resolve key commands, you can re-map Smart Zoom in the Keyboard

Customization dialog.

For more information on Keyboard Customization, see Chapter 4, “System and User

Preferences.”

Standard Timeline view


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Smart Zoom Timeline view

Audio Editing Modes

The Fairlight page has two audio editing modes: Overwrite Mode and Layered Audio Editing Mode.

Overwrite Mode

As the name suggests, if one a portion of a clip overlaps another clip during an edit, the area that is

affected on the underlying clip is non-destructively deleted to accommodate the incoming clip. If the

overlapping clip is moved or deleted, the underlying clip remains truncated.

Any area that is removed by this process is still present in the original clip and can be exposed by

trimming the start or end (depending on what you’ve affected).

Overwrite is the default mode and is best for most generalized editing.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

(Left) Overwrite edit showing original clips, (Right) Right hand clip dragged left

Resulting overlap

Layered Audio Editing

Layered Audio Editing is a special audio editing mode that lets you superimpose multiple audio clips

in the same track, with audio clips edited into the top layers muting overlapping sections of audio clips

appearing on lower layers. With layered audio editing enabled (Timeline > Layered Audio Editing),

superimposed audio clips are treated similarly to superimposed video clips that have opacity set to

100%, with clips on top obscuring (or muting) clips underneath. You can separately toggle this on and

off in the View menu > Show Audio Track Layers.

This mode is very useful for any situation where you’re combining segments of multiple takes together

(“comping”) to create a single voiceover, audio vocal track, ADR, or dramatic performance, as you can

choose which segments to use via their superimposed position in the stack of clips appearing in that

track, while preserving the other takes underneath in case you might want them later.

However, it’s important to understand that if you delete any clip on a layer that is “above” another, the

lower layer will then “poke through.” This can involve extra housekeeping when editing and is one of

the reasons that Overwrite Editing mode is the default mode.

TIP: Layered Audio Editing mode can be used on audio tracks on the Edit page as well.

Layered Audio Editing and Show Audio Track Layers enabled


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Layered Audio Editing with Show Audio Track Layers disabled. All layers are folded into a single view.

Flatten Audio Layers

After working with Layered Audio Editing, it can be useful to create a “comp” (composite) of a

performance in order to have a single element that reflects the final desired result. Timeline > Flatten

Audio Track Layers allows you to create a single edit without layers where the clip boundaries are

preserved. Choosing this command will cut across each layered clip at the in/out points and flatten

them into a single layer.

After choosing Flatten Audio Layers, audio layers showing (so blank space above)

If you are exporting to an AAF, you’ll want to turn off layered audio editing, as only the first,

lowest layer is exported. If you had already been using layered audio editing, you can first

use Flatten Audio Layers, then perform your AAF export. Keep in mind that if you have

created any layered crossfades, only fades on the incoming clip are retained.

Switching Among Multiple Timelines

Timelines can be organized like any other clip in the Media Pool. To open or switch among timelines,

use the following procedures. Each Timeline retains the view settings last made within it, including

track heights, zoom settings, etc.

To switch timelines, do one of the following:

�In the Edit, Cut, or Fairlight page Media Pool, double-click a timeline.

�In the Edit page Timeline Viewer, choose a timeline from the Timelines dropdown menu at the top

of the viewer.

�In the Color page, choose a timeline from the Timelines dropdown menu at the top of the viewer.

�In the Fairlight page, choose a timeline from the Timelines dropdown menu to the left of the

transport controls.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Toolbar

The Toolbar has buttons that let you choose modes of functionality and other buttons that let you

execute commands such as placing markers and flags.

Icons in the Fairlight Page toolbar when the Automation button is highlighted in the transport bar

Timeline View Options dropdown menu: Contains a variety of controls that allow

you to customize the display of clips and set navigation and scrolling options in

the Timeline.

Grid View Options dropdown menu: Contains controls to customize the timeline grid,

allowing you to view reference lines or align clips to timecode or musical beat locations.

Pointer Mode: The default mode in which you can move and resize clips in the

Timeline, roll edits, and do other basic editing tasks. While this mode can be used

with the pointer, it’s designed for letting you make automatic selections of clips at the

position of the playhead in selected tracks, using keyboard shortcuts or the Fairlight

Editing console.

Range Mode: An editing mode in which you can select partial regions of one or more

clips for partial editing. It’s designed for letting you make automatic selections using In

and Out points to define regions of selected tracks, using keyboard shortcuts or the

Fairlight Editing console.

Focus Mode: In Focus mode you can access Multi Tool behavior depending on

cursor position:

The Selection tool (I-beam): Appears when you move the cursor over the upper

area of the waveform track “lane,” and lets you make time range selections of clips or

automation keyframe data (depending on the track view).

The Hand tool: Appears when you move the cursor over the lower area of the

waveform lane, and lets you select a clip or clips by clicking, move them by dragging, or

apply Cut, Copy, and Paste operations. This tool is available in the other modes as well.

The Trim tool (Up/Down arrows): Appears when you move the cursor close to the clip

gain line, and lets you trim the automaton curve for clip gain or keyframe levels. When

trimming an automation parameter, a tooltip shows the level along with the delta to the

original value. Trim tool cursors for trimming clip boundaries to trim clip start or end, or

perform rolling trims are also available. This tool is available in the other modes as well.

Pencil: A tool that lets you write automation data using the pointer as a pencil.

The Pencil tool appears when automation is enabled.

Razor (Scissors): Click to add a cut to every clip on an unlocked track that intersects

the position of the playhead.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Snapping: Enables or disables clip snapping. When turned on, clip In and Out points,

markers, and the playhead all snap to one another for reference while you’re editing.

Linked Selection: When you select an edit point with both video and audio

components, and Linked Selection is enabled, both the video and audio edit points

are selected, so when you apply a video transition to an edit, a crossfade is added to

the audio.

Also lets you link together any otherwise unrelated audio clips to perform edit

operations (for example, trimming) to any linked clips at one time.

Automation Follows Edit: Enables or disables mix automation that is unique to

a timeline to be embedded into the clips so that when cutting and pasting new

instances of them in the Timeline they retain their levels, panning, filter settings,

etc. This is extremely useful when using multiple instances of the same audio clips

throughout an edit.

The Automation Follow Edit button appears when automation is enabled, and is

enabled by default.

Flag Clip/Flag Colors dropdown menu: Flags identify clips, and indicate all clips that

correspond to the same item of media in the Media Pool. Clips can have multiple flags.

Clicking the Flag button automatically adds a flag to whichever clip is currently selected

in the Timeline. A dropdown menu lets you choose flag color, and has a choice to clear

all flags from the currently selected clip (if one is selected) or clear flags from the entire

timeline (if no clip is selected).

Add Marker/Marker Colors dropdown menu: Markers identify specific frames of

individual clips or timelines. If a clip is selected in the timeline, clicking the Add Marker

button adds a marker to the clip at the position of the playhead in the Timeline. If no

clips are selected, clicking the Add Marker button adds a marker to the timeline ruler at

the position of the playhead. A dropdown menu lets you choose marker color, and has

a choice to clear all markers from the currently selected clip (if one is selected) or clear

markers from the entire timeline (if no clip is selected).

Transient Detection: Enables transient detection for all clips on a given track. Once

enabled, a transient button appears on tracks to enable the transients on a track’s clips

to be easily identified and navigated. When the Jump to Transient button is enabled,

the Up and Down arrow keys navigate to transients within a clip.

Vertical Slider: Lets you adjust the vertical zoom level of tracks.

Horizontal Slider: Lets you adjust the horizontal zoom level of the Timeline.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT