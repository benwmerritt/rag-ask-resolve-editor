---
title: "Moving the Clip Selection"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 676
---

# Moving the Clip Selection

The Command-Option-Left and Command-Option-Right Arrow key shortcuts are used to move the

playhead left and right in the Timeline, navigating from clip to clip or from marker to marker. How these

keys function depends on whether or not one or more tracks is selected in the Timeline.

�If no tracks are selected: The Left and Right Arrow keys will jump the playhead from Timeline

marker to Timeline marker. Clip markers will be ignored.

�If one or more tracks are selected: The Left/Right Arrow keys will jump the playhead among clip

In points, clip Out points, and Timeline markers.

Moving the Track Selection

The Command-Option-Up and Command-Option-Down Arrow key shortcuts are used to move

the track selection up and down in the Timeline, changing which tracks are selected. By changing

which tracks are selected, you can alter which clip’s In and Out points are used to jump the playhead

around the Timeline.

If no tracks are selected, then nothing happens.

Zooming and Scrolling

The Fairlight page has several methods of zooming into and out of the Timeline, and scrolling when

you’re zoomed to the point where your edited sequence of clips extends past the left and right edge

of the visible timeline.

The Playhead

Zooming is always centered on the position of the Playhead. By default the Playhead moves along the

Timeline as it plays. However, Fairlight offers the option of a Fixed Playhead where the Timeline moves

while the Playhead remains centered.

The Playhead options are found

in the Timeline Scrolling panel.


Fairlight | Chapter 172 Transport Controls, Timeline Navigation, and Markers

FAIRLIGHT

Setting the Zoom Level of the Timeline

Depending on how you like to work, there are several methods of zooming into and out of

the Timeline.

Using the Vertical Zoom slider: A pair of sliders at the right of the toolbar let you zoom

vertically and horizontally. The first one lets you scroll vertically in order to see more detail in

the height of your waveforms. If no tracks are selected, then zooming is centered on the top

audio track in the Timeline. If one or more tracks are selected, then zooming is centered on

the topmost selected audio track.

Using the Horizontal Zoom slider: A pair of sliders at the right of the toolbar let you zoom

vertically and horizontally. The second one lets you zoom horizontally in order to see more

detail in the width of your waveforms.

Pressing Command-Equal (=) and Command-Minus (–): Command-Equal (also referred to as

Command-Plus) and Command-Minus let you zoom horizontally into the Timeline.

Use Shift-Z to Zoom to Fit: Command-Z lets you zoom horizontally to fit all clips in your

program to the available width of the Timeline.

Using scroll controls of your pointing device to scroll horizontally: Holding the Option

key down and using the scroll wheel (or scroll control) of your pointing device will zoom

horizontally into the Timeline. Holding the Command key down and using the scroll wheel will

move the Timeline earlier or later than its current time, without moving Playhead.

Using scroll controls of your pointing device to scroll vertically: Holding the Shift key

down and using the scroll wheel (or scroll control) lets you zoom vertically in the Timeline.

In this case, if no tracks are selected, then zooming is centered on the top audio track in

the Timeline. If one or more tracks are selected, then zooming is centered on the topmost

selected audio track.

Using the Fairlight panel’s Jog/Edit wheel: If you have a Fairlight panel, you can hold

the ZOOM button down while turning the Jog/Edit wheel to zoom into the Timeline at the

position of the playhead.

Scrolling Through the Timeline

However closely you’re zoomed into the Timeline, if you’re zoomed enough so that clips extend past

the visible area of the Timeline, scroll bars appear below. If the playhead is offscreen, a small orange

tic mark indicates its position relative to the entire timeline, which is represented by the total width of

the scroll bar’s background.

If you drag the playhead, or otherwise use any of the transport controls or playback key shortcuts to

move through the Timeline, the contents of the Timeline refresh every time the playhead hits the left

or right edge of what’s visible.


Fairlight | Chapter 172 Transport Controls, Timeline Navigation, and Markers

FAIRLIGHT

Using Flags

Flags are meant to mark an entire clip, and they also flag every other clip in the Timeline that shares

the same Media Pool source clip, making this a handy way of quickly identifying which clips in a given

timeline come from the same Media Pool source. Flags are visible in every page of DaVinci Resolve,

making them an excellent method of tracking media from page to page.

The Flag and Marker

buttons and pop-ups.

You can apply multiple flags to clips, with a variety of colors to choose from. In addition to flagging

specific media files, flags can be useful for sorting by column in the Media Pool, as well as a variety of

other operations. Whenever you enter text into a flag, it displays a small dot that indicates there’s more

information inside of it.

Methods for flagging clips in the Fairlight page:

To flag a clip: Select one or more clips, and either click the Flag button to flag that clip with

the current color, or click the Flag pop-up in the toolbar to choose a different color and then

click the Flag button. In the Edit page, flags appear in the Timeline superimposed in the name

bar of each clip.

To remove all flags from a clip: Select one or more clips with flags you want to remove,

then click the Flag pop-up in the toolbar, and choose the top “Clear All” option.

To change the Flag color or remove individually: Double-click the Flag icon on the clip

and a Marker dialog box appears to change the Flag color, remove the flag, or make a note

regarding the flag.

Using Markers

Markers are used to call attention to a particular frame within a specific clip. Markers can be

individually colored, and can have customized name and note text. Whenever you enter text into

a marker, that marker displays a small dot that indicates there’s more information inside of it. Once

placed, markers snap to In and Out points, edit points, the playhead, and other markers whenever

snapping is enabled, making it easy to use markers to “measure” edits and trims that you make in the

Timeline. Markers are visible in every page of DaVinci Resolve, making them an excellent method of

tracking frames in clips and specific moments in the Timeline from page to page.

You can add markers to the Timeline (in the Timeline ruler) or to clips. The full procedures for placing

and editing markers in the Fairlight page’s onscreen interface are identical to those for the Edit

page, so for more information, see Chapter 41, “Marking and Finding Clips in the Timeline.” For now,

here’s a summary.


Fairlight | Chapter 172 Transport Controls, Timeline Navigation, and Markers

FAIRLIGHT

Adding Markers to Clips

The following procedures describe how to add markers to clips in the Timeline of the Media page.

To mark a clip in the Timeline, do one of the following:

�Select one or more clips you want to mark, then move the playhead to the frame of a selected

clip in the Timeline, and click the Marker button in the toolbar (or press M) to place a marker

at that frame, using the current color (if multiple overlapping clips are selected, you’ll add a

marker to all clips).

�To place a marker during playback and immediately open the marker dialog to enter a name or

note within it, select one or more clips you want to mark, play through the selection until you want

to place a mark, then press Command-M. Playback pauses until you enter some text and close the

marker dialog again, at which point playback continues.

�Select one or more clips you want to mark, and then click the Marker pop-up to choose a different

color, and click the Marker button.

Adding Markers to Timelines

You can also place markers of any color into the Timeline ruler to denote specific times for future

reference, or add notes about issues you want to keep track of. You should note that all markers

placed on clips or in the Timeline also appear within the Mini-Timeline of the Color page, making it

easy to place notes to reference particular audio cues that might be valuable when editing or grading.

To mark the Timeline itself, make sure all clips are deselected,

and do one of the following:

�Click the Marker button (or press M) to place a marker of the currently selected color

in the Timeline ruler.

�To place a marker during playback and immediately open the marker dialog to enter a

name or note within it, select one or more clips you want to mark, then press Command-M.

Playback pauses until you enter some text and close the marker dialog again, at which point

playback continues.

�Click the Marker pop-up to choose a different color, and click the Marker button.

�Right-click in the Timeline ruler and choose a marker color from the Add Marker submenu of the

contextual menu.


Fairlight | Chapter 172 Transport Controls, Timeline Navigation, and Markers

FAIRLIGHT

Chapter 173

Recording

It’s possible to record to one or more tracks on the Fairlight page, accommodating

workflows as varied as editors recording scratch voiceover or temp sound effects,

recording engineers recording narration, ADR, or foley as part of the audio finishing

process, music studios recording orchestras for the music score, or garage bands

recording their latest magnum opus.

While DaVinci Resolve is a comprehensive post-production environment for cinema and video, the

Fairlight page can be used for any audio recording application you might have, from books on tape to

live music to feature films and television.

Contents

Setting Up to Record����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3753

Patching Inputs����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3753

Arming Tracks�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3755

Record Name Prefix�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3756

Choosing Where to Record Audio Clips To��������������������������������������������������������������������������������������������������������������������������� 3756

User-Selectable Input Monitoring Options��������������������������������������������������������������������������������������������������������������������������� 3756

Recording Using the Onscreen Controls������������������������������������������������������������������������������������������������������������������������������� 3757

Recording and Editing Multiple Takes Using Layering��������������������������������������������������������������������������������������������������� 3757

Recording VSTi Instruments�������������������������������������������������������������������������������������������������������������������������������������������������������� 3758


Fairlight | Chapter 173 Recording

FAIRLIGHT