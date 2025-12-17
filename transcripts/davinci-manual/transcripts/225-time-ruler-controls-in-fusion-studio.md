---
title: "Time Ruler Controls in Fusion Studio"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 225
---

# Time Ruler Controls in Fusion Studio

The Time Ruler, located beneath the viewer area, displays two different frame ranges: one for the

entire composition, called the global range, and the other called the render range, which determines

what to render and what to cache in memory for previews. The global start and end range takes up the

entire Time Ruler and sets the total duration of a composition. You cannot move the playhead outside

the global range.

The Time Ruler displaying ranges for a clip in the Timeline via yellow marks (the playhead is red)

Global Start and End Range

The global start and end range is simply the total duration of the current composition.

You can change the global range by doing one of the following:

�To change the global range for all new compositions, choose Fusion Studio > Preferences on

macOS or File > Preferences on Windows or Linux. In the Global and Default Settings panel, enter

a new range in the Global range fields.

�To change the Global range for the current composition, enter a new range in the Global Start and

End fields to the left of the transport controls.

�Dragging a node from the Node Editor to the Time Ruler automatically sets the Global and Render

Range to the extent of the node.

Render Range

The render range determines the range of frames used for interactive playback, disk caches, and

previews. Frames outside the render range are not rendered or played, although you can still drag the

playhead to these frames to see the unused frames.

To preview or render a specific range of a composition, you can modify the render range in a

variety of ways.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

You can set the render range in the Time Ruler by doing one of the following:

�Hold down the Command key and drag a new range within the Time Ruler.

�Right-click within the Time Ruler and choose Set Render Range from the contextual menu to set

the Render Range based on the selected Node’s duration.

�Enter new ranges in the Range In and Out fields to the left of the transport controls.

�Drag a node from the Node Editor to the Time Ruler to set the range to the duration of that node.

The Playhead

A red playhead within the Time Ruler indicates the currently viewed frame. Clicking anywhere within

the Time Ruler jumps the playhead to that frame, and dragging within the Time Ruler drags the

playhead within the available duration of that clip or composition.

Zoom and Scroll Bar

A two-handled gray scroll bar lets you zoom into the range shown by the Time Ruler, which is useful

if you’re using a very large Global range such that the Render range is a tiny sliver in the Time Ruler.

Dragging the left or right handles of this bar zooms relative to the opposite handle, enlarging the width

of each displayed frame. Once you’ve zoomed in, you can drag the scroll bar left or right to scroll

through the composition.

TIP: Holding the middle mouse button and dragging in the Time Ruler lets you scroll the

visible range.

Transport Controls in the Fusion Page

The Transport Controls in DaVinci Resolve’s Fusion page include buttons that control playback as

well as time fields on the left side for setting the render range and the current time on the right side.

Additional controls are available in the right-click menu.

Controlling Playback

There are six transport controls underneath the Time Ruler in the Fusion page. These buttons include

Composition First Frame, Play Reverse, Stop, Play Forward, Composition Last Frame, and Loop.

The Fusion page controls for playback

Navigation Shortcuts

Many standard transport control keyboard shortcuts you may be familiar with work in Fusion, but some

are specific to Fusion’s particular needs.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

To move the playhead in the Time Ruler using the keyboard, do one of the following:

Spacebar: Toggles forward playback on and off.

JKL: Basic JKL playback is supported, including J to play backward, K to stop, and L to

play forward.

Back Arrow: Moves 1 frame backward.

Forward Arrow: Moves 1 frame forward.

Shift-Back Arrow: Moves to the clip’s Global Start frame.

Shift-Forward Arrow: Moves to the clip’s Global End frame.

Command-Back Arrow: Jumps to the Render Range In point.

Command-Forward Arrow: Jumps to the Render Range Out point.

Real-Time Playback Not Guaranteed

Because many of the effects you can create in the Fusion page are processor-intensive, there

is no guarantee of real-time playback at your project’s full frame rate unless you’ve cached your

composition first (discussed later).

Frame Increment Options

Right-clicking either the Play Reverse or Play Forward buttons opens a contextual menu. This menu

contains options to set a frame increment value, which lets you use a keyboard shortcut to move the

playhead in sub-frame or multi-frame increments.

Moving the playhead in multi-frame increments can be useful when rotoscoping. Moving the playhead

in sub-frame increments can be useful when rotoscoping or inspecting interlaced frames one field at a

time (0.5 of a frame).

Right-click the Play Forward or

Play Backward buttons to choose a frame

increment in which to move the playhead.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Looping Options

The Loop button can be toggled to enable or disable looping during playback. You can right-click this

button to choose the looping method that’s used:

Playback Loop: The playhead plays to the end of the Time Ruler and starts from the

beginning again.

Ping-pong Loop: When the playhead reaches the end of the Time Ruler, playback reverses

until the playhead reaches the beginning of the Time Ruler, and then continues to ping-pong

back and forth.

Render Range Fields

The two time fields on the left side of the transport controls are used to modify the Render Range.

You can enter time values in frames, or click and drag inside the fields to modify the In and Out of the

render range for previews and caching.

The Render Start and Render End time fields

Audio Monitoring

Playing a composition in DaVinci Resolve’s Fusion page will play the audio from the Edit or Cut page

Timeline. You can choose to hear the audio or mute it using the Audio toolbar button to the left of the

transport controls. The audio waveforms are displayed in the Keyframes Editor to assist in the timing of

your animations.

TIP: If the Mute button is enabled on any Timeline tracks, audio from those tracks will not be

heard in Fusion.

For Fusion Studio, audio can be loaded using the Loader node’s Audio tab. The audio functionality is

included in Fusion Studio for scratch track (aligning effects to audio and clip timing) purposes. Final

renders should almost always be performed without audio. Audio can be heard if it is brought in

through a Loader node.

To hear the audio from a specific Loader node:

Right-click over the Speaker icon and choose the file name that contains the audio

you want to hear.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Audio Toolbar Button

The Audio button in the toolbar is a toggle that can be used to enable or mute audio playback

associated with the clip. Additionally, right-clicking this button displays a contextual menu that can be

used to select a MediaIn node in the Fusion page or an external WAV file in Fusion Studio.

The Current Time Field

The Current Time field at the right of the transport controls displays the frame number for the playhead

position, which corresponds to the frame seen in the viewer. Clicking and dragging in this field scrubs

the playhead position back and forth. However, you can also enter time values into this field to move

the playhead by specific amounts.

When setting ranges and entering frame numbers to move to a specific frame, numbers can be

entered in sub-frame increments. You can set a range to be –145.6 to 451.75 or set the playhead to

115.22. This can be very helpful when animating parameters because you can set keyframes where

they actually need to occur, rather than on a frame boundary, so you get more natural animation.

Having sub-frame time lets you use time remapping nodes or just scale keyframes in the Spline view

and maintain precision.

The Fusion Page Viewer Quality and Proxy Options

Right-clicking anywhere in the transport control area other than over the Play Forward/Play Reverse

buttons lets you turn on and off Fusion quality controls. You can either enable high-quality playback at

the expense of more significant processing times or enter various proxy modes that temporarily lower

the display quality of your composition to speed processing as you work.

Rendering for final output is always done at the highest quality, regardless of these settings.

High Quality

As you build a composition, often the quality of the displayed image is less important than the

speed at which you can work. The High Quality setting gives you the option to either display

images with faster interactivity or at final render quality. When you turn off High Quality, complex

and time‑consuming operations such as area sampling, anti-aliasing, and interpolation are skipped

to render the image to the viewer more quickly. Enabling High Quality forces a full-quality render

to the viewer that’s identical to what is output during final delivery.

Motion Blur

The Motion Blur button is a global setting. Turning off Motion Blur temporarily disables motion blur

throughout the composition, regardless of any individual nodes for which it’s enabled. This can

significantly speed up renders to the viewer. Individual nodes must first have motion blur enabled

before this button has any effect.

Proxy

The Proxy setting is a draft mode used to speed processing while you’re building your composite.

Turning on Proxy reduces the resolution of the images that are rendered to the viewer, speeding

render times by causing only one out of every x pixels to be processed, rather than processing

every pixel. The value of x is decided by adjusting a slider in the Proxy section in the Fusion >

Fusion Settings > General panel.

Auto Proxy

The Auto Proxy setting is a draft mode used to speed processing while you’re building your

composite. Turning on Auto Proxy reduces the resolution of the image while you click and drag to

adjust a parameter. Once you release that control, the image snaps back to its original resolution.

This lets you adjust processor-intensive operations more smoothly, without the wait for every

frame to render at full quality causing jerkiness. You can set the auto proxy ratio by adjusting a

slider in the Proxy section of the Fusion > Fusion Settings > General panel.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Selective Updates

When working in Fusion, only the tools needed to display the images in the viewer are updated.

The Selective Update options select the mode used during previews and final renders.

The options are available in the Proxy section of the Fusion > Fusion Settings > General panel.

The three options are:

•	 Update All (All): Forces all the nodes in the current node tree to render. This is primarily

used when you want to update all the thumbnails displayed in the Node Editor.

•	 Selective (Some): Causes only nodes that directly contribute to the current image to be

rendered. So named because only selective nodes are rendered. This is the default setting.

•	 No Update (None): Prevents rendering altogether, which can be handy for making many

changes to a slow-to-render composition.