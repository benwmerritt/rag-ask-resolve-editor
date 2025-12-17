---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 127
---

# Inspector

The Inspector can be opened to let you customize compositing, transform, and cropping parameters

for clips, as well as clip-specific retime and scaling options. Furthermore, the Inspector lets you

edit the parameters of transitions, titles, and generators used in the Timeline, in order to customize

their effect.

The Inspector, opened and showing a clip’s parameters


Edit | Chapter 33 Using the Edit Page

EDIT

When the Inspector is open, the Source and Timeline viewers move to the left, to sit alongside the

Inspector showing the selected clip’s parameters. However, if your computer display’s resolution is not

high enough, opening the Inspector may result in the Source Viewer being hidden.

Methods of showing parameters in the Inspector:

To open a video or audio clip’s transform settings when the Inspector is closed: Select that

clip, and then click the Inspector button at the far right of the Edit page toolbar.

If the Inspector is already open: You need only select a clip or effect to reveal its

controls in the Inspector.

If the Inspector is closed: Double-clicking any transition will automatically open it.

The Inspector shows different buttons at the top that let you switch among different pages of

parameters. For example, when you select a clip with both audio and video components, the Inspector

shows Video and Audio buttons at the top that let you switch among each set of controls.

Timeline

The Timeline shows whichever timeline you’ve double-clicked in the Timelines browser. It’s where

you either edit programs together from scratch, or import sequences from other applications.

For imported programs, the Timeline provides a visual representation of the edited program that’s

helpful for verifying that the project was imported correctly, checking the media corresponding to

each clip in the program, and performing whatever editorial tasks are necessary to prepare a project

for grading (such as replacing or adding clips, superimposing composites, and modifying composite

modes or transitions).

An edited timeline

�Timeline Ruler: The Timeline Ruler shows the program’s timecode, and the playhead indicates the

current frame of the current clip. Whichever clip intersects the playhead is the one that you’ll be

working on in the Color page. Dragging within the Timeline Ruler moves the playhead. When you

add markers to the timeline, these markers appear within the Timeline Ruler, as well.

�Playhead: The playhead automatically syncs with the Timeline Viewer’s jog bar playhead, the

playheads in the Mini-Timeline and Thumbnail timeline of the Color page, Cut page, and the

playhead on the Deliver page. Furthermore, the Edit Index event that corresponds to the clip

intersecting the playhead is automatically highlighted.


Edit | Chapter 33 Using the Edit Page

EDIT

�Timecode field: Shows the current timecode value corresponding to the position of the playhead.

�Video Tracks: DaVinci Resolve supports multiple video tracks. At the left of each track is a header

area that contains a number of controls.

�Track Header: The Track Header contains different controls for selecting, locking/unlocking,

and enabling/disabling tracks. Each track header also lists how many clips appear on that track.

The Track Header contains the following five controls, from left to right:

Track Header area showing

the controls for each track

that are located within

Track Color: Each track can be color-coded with one of 16 different colors. These color codes

correspond to the Edit page Mixer, and to the Fairlight page Mixer and Audio Meters. You can

choose a new color for any track by right-clicking the track header and choosing from the Change

Track Color submenu.

Destination control and Track Number: These controls are highlighted orange when that track is

selected for editing, dark gray when that track is not selected, and flat gray if that track is disabled

for editing. The Destination buttons dictate into which tracks audio and video media in the Source

Viewer will be placed when an edit is executed. Ordinarily, there is one video destination control

(V1) and one audio destination control (A1). If you add additional tracks, you can see that each

destination control is numbered according to its track position. The bottom track is “V1,” and

subsequently numbered tracks appear higher in the Timeline. Click any track’s number to select

that track for different editing functions; the selected track is highlighted black.

Track Name: Each track has a name that defaults to the type of track and the track number, such

as Video 1, Audio 1. However, you can click any track’s name and edit it to be whatever you like.

For example, you can rename each audio track with the type of audio you’re editing onto it, such

as Production, Ambience, SFX, or Music. These track names are also used to identify each track’s

channel in the Edit page Mixer and in the Fairlight page Mixer.

Enable Track/Mute button: A slash indicates when a track is disabled. This control lets you

turn tracks on and off. Clips on tracks that are turned off aren’t visible in the viewer, don’t show

up in the Color page, and aren’t available for rendering or output. For Audio tracks this is

the Mute button.

Lock Track button: Light gray when turned on, dark gray when turned off. When a track is

locked, clips can’t be replaced, moved, or otherwise edited, although clips on locked tracks can

be graded.

Auto Select button: On by default. Light gray when that track is selected, dark gray when that

track is not selected. When this control is on, clips on that track are automatically included in

operations that affect all clips that intersect the position of the playhead, or that intersect a region

defined by the Timeline In and Out points. When this control is off, clips on that track are ignored

by those same operations. Furthermore, rippling is suspended on tracks with Auto Select turned

off for operations that would otherwise ripple the Timeline. Note, manual selections made in the

Timeline that highlight specific clips take precedence over the Auto Select controls, so if Auto

Select is turned off on track 1, but you’ve selected a clip on track 1, the selected clip will be still be

affected by whatever operation you’re about to perform.


Edit | Chapter 33 Using the Edit Page

EDIT

Audio Channel Type indicator: Audio tracks also show which channel configuration that track

uses, listing the number of channels for mono, stereo, 5.1, 7.1, and adaptive.

Number of clips: The number of clips on that particular track of the Timeline is listed, but only if

the track is tall enough to have room for them.

�Vertical and horizontal scroll bars: If your project is longer than the current width of the Timeline,

or the number of video tracks is taller than the current height of the Timeline, these scroll bars let

you drag to navigate around your program.

�Individual Timeline track resizing: Any track in the Timeline can be individually resized by

dragging its top divider in the Track Header area.

Resizing an individual timeline

track by dragging its top

border in the Track Header

Timeline Options

Specific elements and behaviors within the Timeline can be customized in various ways.

Fixed Playhead Mode in the Timeline

You can select the fixed playhead mode from the Timeline View options in the Edit page. This view

option will keep the playhead static in the middle of the timeline, while the tracks on the timeline move

underneath it, similar to the Cut page.

Selecting the Fixed Playhead mode in the Timeline View options


Edit | Chapter 33 Using the Edit Page

EDIT

Selection Follows Playhead

As of DaVinci Resolve 17, the Clip selection no longer automatically moves along with the playhead.

Instead, a new set of commands lets you create and move a selection by holding down the Command

key and pressing the Up, Down, Left, and Right Arrow keys. This allows you to select clips above and

below the current track and to the left and right, independently of the playhead.

You can return the Clip Selection mode back to its previous behavior of automatically selecting the top

clip it’s intersecting by choosing the option Timeline > Selection Follows Playhead.

Show Playhead Shadow

Ordinarily, the playhead is shown in the Timeline as a single line that indicates the beginning of the

frame that you’re viewing in the Timeline Viewer. However, you can choose Show Playhead Shadow

from the User Preferences UI Settings to display an orange-ish background surrounding the playhead.

This shadow can make it easier to see the playhead’s position, and it can also serve as a measuring

tool for projects where you have an interest in visualizing a specific offset, in frames, both before

and after the current position of the playhead. This offset can be adjusted by changing the Pre- and

Post-Playhead Shadow Length parameters in the Editing panel of the User Preferences, which let you

specify the number of frames to shadow both before and after the playhead. The default length of the

playhead shadow is 5 frames.

(Left) The playhead’s

default look, (Right) The

playhead showing the

optional playhead shadow

TIP: You can set the “Pre-playhead shadow length” to 0, and the “Post-playhead shadow

length” to 1 if you want to display a “Media Composer-style” playhead that shows the duration

of the current frame.


Edit | Chapter 33 Using the Edit Page

EDIT

Enabling and Disabling Audio Scrubbing

Audio scrubbing is enabled by default, meaning that you’ll hear audio when dragging the playhead

with the mouse back and forth. While this can be useful when you’re searching for audio cues, it can

also be distracting if you’re just focused on the picture.

To enable or disable audio scrubbing:

Choose Timeline > Audio Scrubbing (Shift-S)

Playback Post-Roll

Enables the playhead to continue playing past the last clip in the Timeline for a duration equal to the

“Post-roll time” Project Setting in the Editing panel. This is good for editors that want to experience

a few moments of playback after cutting or fading to black after the last frame of audio and video in

the Timeline.

To enable or disable playback post-roll:

Choose Timeline > Playback post-roll