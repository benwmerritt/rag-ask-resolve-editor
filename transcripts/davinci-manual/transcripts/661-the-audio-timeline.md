---
title: "The Audio Timeline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 661
---

# The Audio Timeline

The heart of the Fairlight page, the Audio Timeline, presents the audio channels and tracks of the

currently selected Timeline. Each audio track may contain multiple lanes depending on its Track Type,

or format.

The clips edited into the Timeline appear within each track, with any multichannel elements within

each clip occupying as many lanes as that track type has available (for example, 2 channel stereo,

or 6 channels for 5.1). At the left of each track is a header containing a number of controls.

These multi-lane audio tracks appear differently from the Edit page, which is optimized for

straightforward audio-for-video editing, and shows any multichannel files on single lane tracks with

composite waveforms.

The Fairlight page Timeline cannot be closed.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

The Audio page Timeline

Controls in the Audio Timeline

The Audio Timeline has the following controls.

�Timecode fields and Range buttons: These fields display the current timecode value of

the Playhead position along the Timeline Ruler, the Range In and Range Out points, and the

Range duration.

Clicking the Range In and Range Out buttons (to the left of their timecode fields) sets their

corresponding values and locations on the Timeline Ruler.

Timecode fields and Range

buttons in the Fairlight page

�Transport controls: Located at the top of the Timeline, this bar contains audio-specific transport

controls, which differ from those found on the Media, Edit, Color, and Deliver pages due to the

included recording capabilities. These controls include Fast Reverse, Fast Forward, Play Forward,

Stop, Record, Loop, and the Toggle Automation and Automation toolbar display icons.

Fairlight page transport controls


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

�Toggle Automation button: Clicking this button activates automation recording and playback, and

adds an Automation Follows Edit button to the Toolbar, between the Flags and Markers buttons.

For more details on the Toolbar, please refer to “Toolbar,” found later in this chapter.

�Automation toolbar: This button opens a secondary toolbar with all the controls you need for

recording mixer automation.

For more details on Automation, see Chapter 178, “Mix Automation.”

Fairlight page automation toolbar

�Monitoring controls: The three monitoring controls located at the far right of the transport controls

let you quickly adjust the output volume of your mix.

Clicking the Speaker icon mutes and unmutes the audio playback. The icon turns red when the

audio is muted.

The horizontal slider lets you gradually increase or decrease the output volume. The

corresponding signal level is displayed in decibels as you move the slider.

The DIM button lets you temporarily reduce the output volume, which is helpful if you want to have

a quick chat with your client about sports or the state of the world while keeping half an ear on the

mix. The slider turns yellow whenever you activate the DIM function.

The monitoring controls

�Timeline Ruler: The Timeline Ruler displays the program’s timecode and, in conjunction with the

playhead, indicates the current frame (or sample) where you’re working in the Timeline.

Within the Timeline Ruler, you’ll find a handle at the top of the playhead. You can move the

playhead by clicking and dragging the handle.

Markers added to the Timeline also appear in their corresponding locations within the

Timeline Ruler.

�Playhead: Shows the current frame and sample of playback and provides a visual representation

of where you are while playing, shuttling, and jogging through the Timeline. At the same time,

the large timecode display in the upper left-hand corner of the Timeline also shows the current

playhead location.

The playhead location is also a reference point for editing operations.

�Audio tracks: The Fairlight page supports multiple audio tracks. Each track may contain multiple

lanes to accommodate the audio channels within multi-channel audio clips using track mappings

such as stereo, 5.1, 7.1, Dolby Atmos, Ambisonics, or Adaptive (1–24 channels).

Audio clips edited into the Timeline appear within the tracks, with the recorded channels

occupying as many lanes as that clip has available.

A corresponding header area containing various controls is located to the left of each track.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

The Fairlight timeline is divided into tracks and lanes; track A1 is a mono track and has

a single lane for mono audio. Track A2 is stereo and has two lanes for stereo audio.

Track header

The controls in the track header let you lock/unlock, solo/mute, and record-arm the track.

In addition to a level meter, the track header includes informational fields showing the track type, track

number and name, track volume, and the number of clips on the track.

The track header controls of the Fairlight page timeline

�Track color: Each track can be color-coded with one of 16 colors, which will carry over to the

Fairlight and Edit page Mixers, Tracks Index, and Audio Meters.

To apply a color to a track, right-click the track header and choose a color from the Change Track

Color submenu.

You can apply the same color to multiple tracks by dragging over contiguous track headers or

Command-clicking multiple discontiguous track headers, then selecting a color from the Change

Track Color submenu.

�Track number: Indicates the number of each track.

�Track name: Each track has a name that defaults to the track number, such as Track 1, Track 2.

However, you can click any track’s name and edit it to be whatever you like. F

or example, you can rename each track with the type of audio you’re editing onto it, such as

Production, Ambience, SFX, or Music. These track names are also used to identify each track’s

channel in the Mixer, in the middle of each channel strip (each channel strip’s track number is

simultaneously displayed at the top).

�Audio channel type indicator: Audio tracks also show which channel configuration that track uses,

listing the number of channels for mono, stereo, 5.1, 7.1, Atmos, adaptive, and others.

�Fader value: A field displays the current fader setting at the position of the playhead, in dB. This

value corresponds to the track’s fader level on the Mixer panel. You can drag this value up or

down and the fader will follow.

�Lock Track button: When a track is locked, clips can’t be replaced, moved, or otherwise edited,

although clips on locked tracks can be graded when in the Color page. The lock shows closed

when track contents are locked and open when unlocked.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

�Arm button: This button arms recording onto that track.

�Solo button: Disables all other tracks but the current one, enabling you to quickly hear a single

track in isolation. This affects rendering, so if one or more tracks are soloed, the muted tracks

won’t be output or rendered.

�Mute button: Temporarily disables audio on that track so it’s not monitored or output. This affects

rendering, so if one or more tracks are muted, they won’t appear in the rendered output.

�Audio meters: Each track has audio meters in the track header that let you see levels

during playback.

�Toolbar editing tools: The toolbar contains both modal and command buttons to let you work on

your projects. More detail on these appears in the following section.

�Vertical and horizontal scroll bars: If your project is longer than the current width of the Timeline,

or the number of audio tracks is taller than the current height of the Timeline, these scroll bars let

you drag to navigate around your program. When the view is scrolled horizontally, the playhead

moves along with the track waveforms, so it may temporarily move out of view. If you start

playback, the playhead jumps back into view. You can also scroll vertically using the scroll wheel

(or other scroll control) of your mouse or other pointing device and can scroll horizontally by

holding the Command key down while using your scroll control.

�Individual Timeline track resizing: Any track in the Timeline can be individually resized by right-

clicking anywhere within that track’s header control area and choosing a track height from the

Lock Track Height To submenu of the contextual menu. You can choose a fixed size including

Micro, Mini, Medium, Large, Extra Large, and Custom. When you choose a fixed track height,

vertical zooming no longer affects that track until you change that track’s “Lock Track Height to”

option back to None. You can also highlight several or all tracks and set the track height to one

size. All highlighted tracks will change to that particular size unless changed again, either globally

or individually.

Resizing an individual audio timeline track using contextual menu options


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT