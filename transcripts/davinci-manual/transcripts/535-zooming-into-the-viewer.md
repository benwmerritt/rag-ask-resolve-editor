---
title: "Zooming into the Viewer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 535
---

# Zooming into the Viewer

When using the Viewer to sample tricky colors or draw a detailed PowerCurve, it can be advantageous

to zoom into the image.

To zoom into or out of the Viewer, do one of the following:

•	 Move the pointer to within the Viewer, and then roll the scroll wheel to zoom in or out of

the image.

•	 Press Command-Equal to zoom in, or Command-Minus to zoom out.

To pan around the Viewer:

•	 Move the pointer to within the Viewer, then middle-click and drag to pan around the image.

To reset the size of the Viewer image:

•	 Choose 100% (Actual Size) (Option-Shift-Z) from the sizing drop-down menu in the

upper left of the Viewer.

•	 Choose View > Zoom > Zoom to Fit (Shift-Z).

To enable or disable image zoom being sent to video out:

•	 Choose “Gang viewer zoom with video output” from the option menu of the Viewer to zoom

the image shown on video out identically to the zoom level of the Viewer, enabling you to

evaluate a zoomed-in portion of the image on your suite’s hero display.

Using the Jog Bar and Transport Controls

One of the principal uses of the Viewer is to control playback. The jog bar, directly underneath the

image in the Viewer, contains a playhead that you can drag to the left and right to navigate quickly

through the currently selected clip as fast as you can move the pointer. The playhead in the jog bar

is locked to the playheads found in the Timeline and Keyframe Editor. Moving one playhead moves

all three.

How much of the Timeline the jog bar navigates depends on whether the Node Editor is set to Clip or

Timeline mode. In Clip mode, the jog bar width equals the duration of the currently selected clip. In

Timeline mode, the jog bar width equals the total duration of the entire Timeline.

A row of transport controls below the jog bar provides more specific control over timeline playback.

�Previous clip: Moves the playhead to the first frame of the previous clip.

�Reverse: Initiates 100% playback in reverse.

�Stop: Stops playback.

�Play: Initiates 100% playback.

�Next clip: Moves the playhead to the first frame of the next clip.

�Loop: Lets you restrict playback to the current clip, looping to the first frame if you’re playing

forward to the end of a clip, or looping to the last frame if you’re playing in reverse to the

beginning of a clip.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Two other buttons let you control audio playback and clip display in the Viewer:

�Unmix: Turning on Unmix disables all transitions, composited superimpositions, and effects

that mix two or more clips together. Unmix allows you to judge the appearance of a clip without

distraction whenever you need to make an adjustment based on how the clip looks on its own,

or whenever you need to make changes based on frames that would otherwise be hidden

underneath a transition such as a dissolve or fade from black. When you’re ready to see how your

grades work in context with transitions and composites again, turn Unmix off.

�Mute: Audio playback can be turned on or off by clicking on the speaker icon, or adjust the level

by right-clicking on the speaker icon and dragging the slider.

Navigating Using the Arrow Keys

You can use the Arrow Keys of the keyboard to navigate clips and the Timeline in different ways.

�Up/Down Arrow: Moves the playhead to the first frame of the previous or next clip.

�Left/Right Arrow: Moves the playhead back or forward one frame at a time.

�Shift-Left/Right Arrow: Moves the playhead back or forward one second at a time.

Controlling Playback Using the Spacebar and JKL Keys

You can also use the spacebar to start and stop playback, or the JKL keyboard shortcut convention for

controlling playback, where J plays in reverse, K stops playback, and L plays forward. There are many

additional uses of these keyboard shortcuts.

For more information see Chapter 35, “Preparing Clips for Editing and Viewer Playback.” in

“Using JKL to Control Playback”

Fast Review on the Color Page

The Fast Review playback command (Playback > Fast Review) is now available on the Color page.

Intended to help you watch through long sequences of clips quickly, clicking this option begins

accelerated playback through the Timeline, where the speed of playback is relative to the length of

each clip you’re playing through. Long clips play faster, whereas shorter clips play closer to real time.

Navigating Using Timecode

You can also use absolute or relative timecode entry to move the playhead in the Color page Viewer.

When entering timecode, type each pair of hour, minute, second, and frame values consecutively, with

a period representing a pair of zeros for fast entry. The last pair of timecode values (or period) you

enter is always assumed to be the frame number, with any untyped values assumed to be zero. It’s not

necessary to enter colons or semicolons.

For more information, see Chapter 35, “Preparing Clips for Editing and Viewer Playback.” in

“Moving the Playhead Using Timecode.”


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Viewer and Transport Timecode Displays

The Viewer has two timecode displays, each of which defaults to a different timecode setting.

A timecode display at the top, the Header timecode display, shows the Source timecode by default.

The timecode display at the bottom, the Transport timecode display, shows the Record timecode by

default. The bottom timecode display can be changed to show one of four different options, which are

similar to those found in the Data Burn-In palette.

To change a timecode display to a different setting:

The top timecode display is a drop-down menu that can be changed to whatever timecode, frame

number, or KeyKode you want to display. The bottom timecode display can also be changed by right-

clicking on it and choosing the type of value to show from the contextual menu that appears. There are

the following options:

�Timeline Timecode: The timecode corresponding to the playhead’s position in the

overall Timeline.

�Source Timecode: The timecode corresponding to the playhead’s position relative to the

currently selected clip.

�Timeline Frame: The frame count corresponding to the playhead’s position in the overall Timeline.

�Source Frame: The frame count corresponding to the playhead’s position relative to the currently

selected clip.

�KeyKode: The KeyKode number corresponding to the media’s KeyKode track, if there is one.

�Show Timecode at 30 FPS: Displays 24 fps timecode, via 3:2 pulldown, as 29.97 fps timecode.

Has no effect on video playback.

�Copy and Paste Timecode: Two commands make it easy to copy and paste timecode values.

In the same way, the top timecode display can alternately be changed to show KeyKode, if it’s

available, within a DPX media file’s header.

Enhanced, Full, and Cinema Viewing

You can expand the Viewer into Enhanced Viewing mode by choosing Workspace > Viewer Mode >

Enhanced Viewer Mode (Option-F).

Enhanced Viewing Mode

In Enhanced Viewing mode, the Viewer works exactly as it does at its regular size, but it expands to

fill up the entire area of the screen above the palettes and Keyframe Editor. To exit Enhanced Viewing

mode, press (Option-F) again.

This can be useful if you need a closer view of the image for purposes of making detailed corrections,

examining noise patterns up close, making a tricky color selection, or drawing a complicated

PowerCurve.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Color page in Enhanced Viewer mode

Full Viewing Mode

In Full Viewing mode (available by choosing Workspace > Viewer Mode > Full Page Viewer, pressing

Shift-F, or Option-clicking the Enhanced Viewing mode button), the Viewer takes up even more room

by hiding the palette controls, but leaves room for the transport controls, the Onscreen Control drop-

down menu, the timecode display, and the page buttons along the bottom of the DaVinci Resolve UI.

This mode is useful when you need an even closer look at the image, but you still want access to a

minimal set of onscreen controls.

Color page in Full Viewer mode


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Cinema Viewing Mode

Another option, Cinema mode, allows for full-screen viewing. Cinema mode is available by choosing

Workspace > Viewer Mode > Cinema Mode Viewer (P). In Cinema mode, the menu bar is hidden,

and the image is presented full screen without any of the ordinary onscreen controls. Moving the

pointer over the screen reveals a set of hidden onscreen controls that include a play button, jog

bar, mute button, and exit button (which lets you turn off Cinema mode). You also have the option of

superimposing scopes over the image, which can be valuable in on-set situations.

Color page in Cinema mode

Cinema mode is useful for doing detailed reviews of media in on-set and digital dailies workflows

when working remotely without a secondary video display.

TIP: If you’d like to superimpose timecode over the image in Cinema mode for reference, you

can use the controls within the Data Burn-In window (Workspace > Data Burn-In) to set up

whatever information you’d like to display during playback.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR