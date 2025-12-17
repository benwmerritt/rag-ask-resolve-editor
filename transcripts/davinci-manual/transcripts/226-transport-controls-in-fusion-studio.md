---
title: "Transport Controls in Fusion Studio"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 226
---

# Transport Controls in Fusion Studio

The transport controls in Fusion Studio include buttons to control playback, time fields on the left

side for setting the global range and render range, and a Render button to initiate rendering of the

composite. There are also controls on the right side for proxy and motion blur. The time field on the far

right is used for the current time.

Fusion Studio transport controls

Controlling Playback

There are eight transport controls underneath the Time Ruler in Fusion Studio. These buttons

include Composition First Frame, Step Backward, Play Reverse, Stop, Play Forward, Step Forward,

Composition Last Frame, and Loop.

Fusion Studio transport controls

Navigation Shortcuts

Many standard transport control keyboard shortcuts you may be familiar with work in Fusion, but there

are some keyboard shortcuts specific to Fusion’s particular needs.

To move the playhead in the Time Ruler using the keyboard, do one of the following:

•	 Spacebar: Toggles forward playback on and off.

•	 JKL: Basic JKL playback is supported, including J to play backward, K to stop,

and L to play forward.

•	 Back Arrow: Moves 1 frame backward.

•	 Forward Arrow: Moves 1 frame forward.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

•	 Shift-Back Arrow: Moves to the clip’s Global End frame.

•	 Shift-Forward Arrow: Moves to the clip’s Global Start frame.

•	 Command-Back Arrow: Jumps to the Render Range In point.

•	 Command-Forward Arrow: Jumps to the Render Range Out point.

Real-Time Playback Not Guaranteed

Because many of the effects you can create in the Fusion page are processor-intensive, there is

no guarantee of real-time playback at your project’s full frame rate, unless you’ve cached your

composition first. For more information, see the “Fusion RAM Cache for Playback” section later in

this chapter.

Frame Increment Options

Right-clicking the Step Backward, Play Reverse, Play Forward, or Step Forward buttons opens a drop-

down menu with options to set a frame increment value. Selecting a frame number from the menu lets

you move the playhead in sub-frame or multi-frame increments whenever you use a keyboard shortcut

or press the Step Forward/Backward buttons.

Moving the playhead in multi-frame increments can be useful when rotoscoping. Moving the playhead

in sub-frame increments can be useful when rotoscoping or inspecting interlaced frames one field at a

time (0.5 of a frame).

Right-click the Step

Forward or Step

Backward buttons

to choose a frame

increment in which to

move the playhead.

Looping Options

The Loop button can be toggled to enable or disable looping during playback. You can right-click this

button to choose the looping method that’s used:

�Playback Loop: The playhead plays to the end of the Time Ruler and starts from the

beginning again.

�Ping-pong Loop: When the playhead reaches the end of the Time Ruler, playback

reverses until the playhead reaches the beginning of the Time Ruler, and then continues to

ping-pong back and forth.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Range Fields

The four time fields on the left side of the transport controls are used to quickly modify the global

range and render range in Fusion Studio.

Global Time Fields to the left of the transport controls

Audio

The Audio button is a toggle that mutes or enables any audio associated with the clip. Additionally,

right-clicking on this button displays a drop-down menu that can be used to select a WAV file, which

can be played along with the composition, and to assign an offset to the audio playback.

Render

Clicking the Render button in the transport controls displays the composition’s Render Settings dialog.

This dialog is used to configure the render options and initiate rendering of any Saver nodes in the

composition. Shift-clicking on the button skips the dialog, using default render values (full resolution,

high quality, motion blur enabled).

The Current Time

The Current Time field at the right of the transport controls shows the frame at the position of the

playhead, which corresponds to the frame seen in the viewer. However, you can also enter time values

into this field to move the playhead by specific amounts.

When setting ranges and entering frame numbers to move to a specific frame, numbers can be

entered in sub-frame increments. You can set a range to be –145.6 to 451.75 or set the playhead

to 115.22. This can be very helpful when animating parameters because you can set keyframes where

they actually need to occur, rather than on a frame boundary, so you get more natural animation.

Having sub-frame time lets you use time remapping nodes or just scale keyframes in the Spline view

and maintain precision.

NOTE: Many fields in Fusion can evaluate mathematical expressions that you type into them.

For example, typing 2 + 4 into most fields results in the value 6.0 being entered. Because

Feet + Frames uses the + symbol as a separator symbol rather than a mathematical symbol,

the Current Time field will not correctly evaluate mathematical expressions that use the

+ symbol, even when the display format is set to Frames mode.

Fusion Studio Viewer Quality and Proxy Options

Five buttons along the right side of the transport controls let you either enable high-quality playback

at the expense of greater processing times, or enter various proxy modes that temporarily lower the

display quality in order to speed processing as you work.

Rendering for final output is always done at the highest quality, regardless of these settings.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Five buttons control the viewer quality, motion blur, proxy

options, and image-processing update settings.

HiQ

As you build a composition, often the quality of the displayed image is less important than the

speed at which you can work. The High Quality setting gives you the option to either display

images with faster interactivity or at final render quality. When you turn off High Quality, complex

and time-consuming operations such as area sampling, anti-aliasing, and interpolation are skipped

to render the image to the viewer more quickly. Enabling High Quality forces a full-quality render

to the viewer that’s identical to what will be output during final delivery.

MB

The Motion Blur button is a global setting. Turning off Motion Blur temporarily disables motion blur

throughout the composition, regardless of any individual nodes for which it’s enabled. This can

significantly speed up renders to the viewer. Individual nodes must first have motion blur enabled

before this button has any effect.

Prx

A draft mode to speed processing while you’re building your composite. Turning on Proxy reduces

the resolution of the images that are rendered to the viewer, speeding render times by causing

only one out of every x pixels to be processed, rather than processing every pixel. The value of x

is decided by adjusting a slider in the General panel of the Fusion Preferences, found under the

Fusion menu on macOS or the File menu on Windows and Linux.

Aprx

A draft mode to speed processing while you’re building your composite. Turning on Auto Proxy

reduces the resolution of the image while you click and drag to adjust a parameter. Once you

release that control, the image snaps back to its original resolution. This lets you adjust processor-

intensive operations more smoothly, without the wait for every frame to render at full quality

causing jerkiness. You can set the auto proxy ratio by adjusting a slider in the General panel of

the Fusion Preferences, found under the Fusion menu on macOS or the File menu on Windows

and Linux.

Selective Updates

The last of the five buttons on the right of the transport controls is a three-way toggle that

determines when nodes update images in the viewer. By default, when working in Fusion, any

node needed to display the image in the viewer is updated. The Selective Update button can

change this behavior during previews and final renders.

The three options are:

•	 Update All (All): Forces all the nodes in the current node tree to render. This is primarily

used when you want to update all the thumbnails displayed in the Node Editor.

•	 Selective (Some): Causes only nodes that directly contribute to the current image to be

rendered. So named because only selective nodes are rendered. This is the default setting.

•	 No Update (None): Prevents rendering altogether, which can be handy for making a lot of

changes to a slow-to-render composition.

The options are also available in the Fusion Preferences General panel.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Changing the Time Display Format

By default, all time fields and markers in Fusion count in frames, but you can also set the time display

to SMPTE timecode or Feet + Frames.

To change the time display format:


Choose Fusion > Fusion Settings in DaVinci Resolve, choose Fusion Studio > Preferences in

Fusion Studio on macOS, or choose File > Preferences in Fusion Studio on Windows or Linux.


When the Fusion settings dialog opens, select the Defaults panel and choose a Timecode option.


Select the Frame Format panel. If you’re using timecode, choose a frame rate and turn on the

“has fields” checkbox if your project is interlaced. If you’re using feet and frames, set the Film Size

value to match the number of frames found in a foot of film in the format used in your project.


Click Save.

Keyframe Display in the Time Ruler

When you select a node with keyframed parameters, those keyframes appear in the Time Ruler

as little white tic marks, letting you navigate among and edit keyframes without having to open the

Keyframes Editor or Spline Editor to see them.

The Time Ruler displaying keyframe marks

To move the playhead in the Time Ruler among keyframes:

�Press Option-Left Bracket ([) to jump to the next keyframe to the left.

�Press Option-Right Bracket (]) to jump to the next keyframe to the right.

The Fusion RAM Cache for Playback

When assembling a node tree, all image processing operations are rendered live to display the final

result in the viewers. However, as each frame is rendered, and especially as you initiate playback

forward or backward, these images are automatically stored to a RAM cache as they’re processed so

you can replay those frames in real time. The actual frame rate achieved during playback is displayed

in the Status bar at the bottom of the Fusion window during playback. Of course, when you play

beyond the cached area of the Time Ruler, uncached frames need to be rendered before being added

to the cache.

Priority is given to caching nodes that are currently being displayed, based on which nodes are loaded

to which viewers. However, other nodes may also be cached, depending on available memory and on

how processor-intensive those nodes happen to be, among other factors.

Memory Limits of the RAM Cache

There is a single setting in DaVinci Resolve for limiting the RAM used for caching. This setting is

located in the DaVinci Resolve Preferences Memory and GPU panel.

�Limit Fusion Memory Cache To: This slider sets the maximum amount of RAM that Fusion can

access for caching. It is a subset of the RAM allocated to DaVinci Resolve. You can assign a

maximum of 75% to Fusion from DaVinci Resolve’s total RAM allocation. When not using the Fusion

page, the RAM is released for other pages in DaVinci Resolve.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

There are two settings in Fusion Studio for limiting the RAM used for caching. These settings

are located in the Preferences Memory panel.

Limit Caching To: This slider sets the maximum amount of RAM used for caching. The 60%

default setting on a 32-GB system limits the cache to 19.2 GB. The maximum amount you can

assign to Fusion Studio is limited to 80% of the total system memory. This leaves a minimum

amount of memory for other applications and the operating system.

Leave at least # MBytes: This number field further limits caching in cases where the system’s

available free RAM drops below the entered value. For instance, setting this to 200 MB

attempts to keep 200 MB of RAM free for the OS or other applications. Setting the number

field to 0 allows Fusion Studio to use the full amount of RAM specified by the Limit Caching To

setting, ignoring other apps.

When the size of the cache reaches the Fusion Caching/Memory Limits setting found in

the Memory panel of the Preferences, then lower-priority cache frames are automatically

discarded to make room for new caching. You can keep track of the RAM cache usage via a

percentage indicator on the far right of the Status bar at the bottom of the Fusion window.

Displaying Cached Frames

All cached frames for the currently viewed node are indicated by a green line at the bottom of the

Time Ruler. Any green section of the Time Ruler should play back in real time.

The green lines indicate frames that have been cached for playback.

Temporarily Preserving the Cache When Changing Quality or Proxy Settings

If you toggle the composition’s quality settings or proxy options, the cache is not immediately

discarded. The green line instead turns red to let you know the cache is being preserved and can be

used again when you go back to the original level of quality or disable proxy mode. However, if you

play through those frames at the new quality or proxy settings, this preserved cache is overwritten

with a new cache at the current quality or proxy setting.

A red line indicates that cached frames from a

different quality or proxy setting are being preserved.

There’s one exception to this, however. When you cache frames at the High Quality setting,

and you then turn off High Quality, the green frames won’t turn red. Instead, the High Quality

cached frames are used even though the HiQ setting has been disabled.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION