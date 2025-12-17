---
title: "Eliminating Subframe Audio Edits"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 178
---

# Eliminating Subframe Audio Edits

If you have a variety of subframe edits and need to eliminate these subframe adjustments, you can

choose Timeline > Trim Audio Edits to Frame Boundaries. This conforms every edit on the timeline

to frame boundaries on any clips that were edited to subframe precision. If the clip is longer than the

nearest frame, it will be trimmed back, and if the start or end of a clip is close to a frame boundary

and there is additional material available on the clip, it will be extended to reach the nearest

frame boundary.

Record Voiceover Tool

In DaVinci Resolve 20, both the Cut and Edit pages have the ability to record voiceover directly to a

track in the timeline using a simplified interface. For serious and precise ADR work, the ADR toolset in

Fairlight will be more appropriate, but for simple VO and scratch tracks, the Record Voiceover tool is

quick and convenient.

The Record Voiceover tool

To open the Record Voiceover tool, select Timeline > Record Voiceover, or select the Voiceover icon

(the small microphone) on the Timeline Toolbar.

To Record Voiceover


File Name: Type in a descriptive file name for the new Voiceover file or just use the default name.


Audio Input: Choose which audio interface on your computer your microphone is connected to.


Record Track: Choose the audio track in the timeline you wish your voiceover track to be recorded

to. Or select Auto to have DaVinci Resolve choose for you based on your current track layout.


Then place the playhead on the timeline where you want the audio to start.


Click the Record Icon to start recording directly to the track.


Click the Record Icon again to stop the recording.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

When the recording stops, the playhead will automatically snap back to its original starting position for

you to either play back the voiceover clip in place or to instantly record a new take by simply clicking

on the Record Icon again. This new take will automatically overwrite the previous clip on the track.

However, all previous takes will still be available in the Media Pool.

You can choose additional options in the 3-dot option menu of the Voiceover tool.

Input Monitoring: Turning this option on will play back the microphone audio as it’s being

recorded, albeit with some lag. This allows the voice over artist, or the audio engineer, the

ability to hear the audio as it’s being recorded. Selecting this option will make a Mic Monitor

Level slider appear in the main Voiceover tool, which allows you to control how loud the

playback will be in the headphones.

Enable 3 Seconds Countdown: Turning this option on will present a visual three-second

countdown in the Timeline Viewer before the recording begins, allowing your talent a

little time to get ready to speak. There is no audio beep for this countdown; it is a visual

indicator only.

Mute Timeline Audio While Recording: Selecting this option will mute all audio tracks on

the timeline while you are recording so that you do not hear any other sounds that could be

distracting. If you want to mute just some of the tracks, you can do that manually using the

mute buttons in the audio track timeline header.

Stereo Input: Selecting this option will record to a stereo track instead of mono, if you’re using

a stereo microphone.

Hide Options: Selecting this option will remove the File Name, Audio Input, and Record Track

fields from the Voiceover tool, leaving only the Record icon to click on or off. This is useful if

you don’t want your voiceover talent to accidentally change your settings.

Audio Settings in the Inspector

Each clip or track has several audio-related parameters in the Audio panel of the Inspector.

For more details of these controls, see Chapter 37, “Using the Inspector in the Edit Page.”

Setting Volume

Each audio clip, or audio item in the case of audio clips with linked audio on multiple tracks, has its

own Volume level. This means that audio clips with multiple channels share a common Volume setting.

There are several ways you can adjust these levels simply.

Adjusting Audio in the Inspector

Each clip has individual Volume parameters that are accessible in the Audio panel of the Inspector

when one or more audio clips are selected.

Selecting an audio clip in the Timeline and adjusting its volume only alters that clip, which lets you set

basic levels for individual clips in your program. The Volume control affects every channel within that

clip simultaneously.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

The Volume parameter available for audio clips in the Inspector

If you select multiple clips in the Timeline, then adjusting the Volume sliders or virtual sliders for all of

them simultaneously will make a relative adjustment to all of the clips, preserving their offsets from

one another. If you want to set all clips to the same level, then making a numeric adjustment will set all

selected clips to the same absolute level.

Adjusting Audio in the Timeline

Each clip (or item) of audio in the Timeline has a Volume overlay that lets you set that clip’s level by

simply dragging it up or down with the pointer. Holding the Shift key down while you drag allows

finer adjustments. Option-clicking on the level creates a keyframe at that point to dynamically change

levels. This overlay corresponds to the Volume parameter in the Inspector.

Dragging a Volume overlay to adjust the clip level

You can also click the Curve Editor button at the bottom right-hand corner of the audio clip, which

opens the Audio Curve Editor. At the time of this writing, the only parameters you can edit in this

Curve Editor is volume and pan.

Showing the Volume overlay in the Curve Editor


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Adjusting Volume Using Keyboard Shortcuts

You can also adjust the volume of selected clips using keyboard shortcuts, even while the Timeline is

playing. There are several ways you can set this up.

To adjust just one clip: Select that clip, and use one of the commands for changing volume.

To adjust any clip at the position of the playhead: Turn on Timeline > Selection Follows

Playhead so that whichever clip intersects the playhead becomes selected, and use one

of the commands for changing volume. If multiple clips are intersecting the playhead, the

selected clip will be the one on the highest track.

To adjust multiple clips all together: Select all of the clips you want to adjust, all at once, and

use one of the commands for changing volume. If the clips you select have differing Volume

levels, these differences will be maintained as you make your adjustments.

The commands for changing volume are as follows:

To change volume in increments of 1dB: do one of the following:

•	 Clip > Audio > Increase Audio Level 1dB (Option-Command-Equals)

•	 Clip > Audio > Decrease Audio Level 1dB (Option-Command-Minus)

To change volume in increments of 3dB: do one of the following:

•	 Clip > Audio > Increase Audio Level 3dB (Option-Shift-Equals)

•	 Clip > Audio > Decrease Audio Level 3dB (Option-Shift-Minus)

Normalize Audio Volume Command

The Normalize Audio Levels command automatically adjusts the level of clips to a specific target

level, and you can choose the method used to analyze each audio clip’s levels to determine how to

normalize each clip’s volume. Options include a variety of loudness normalization algorithms specific

to various international standards, which are useful for balancing the perceived overall loudness of

several clips to one another, regardless of transient levels throughout each clip. You can also do Peak

normalization, with options for both Sample Peak and True Peak.

The various loudness options are designed to analyze an audio signal based on its perceived

loudness to the listener, which results in a more accurate automatic balancing of different clips’ audio

levels to one another, regardless of transient peaks occurring throughout different clips.

The target peak meter now uses the BS.1774 standard for measuring maximum “true peak,” which

means that this meter is capable of measuring “inter-sample peaks,” rather than only the peaks at

each sample of a waveform. However, you still have the option to measure Sample Peak, which is the

previous method of measuring the actual peak of the samples in a media file.

The change made by the Normalize Audio Volume command is only a volume adjustment; no

dynamics are applied, so the result of using this command is that the loudest parts of each selected

clip are going to match one another at the target level. This command is also available in the

Fairlight page.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

To normalize one or more selected audio clips:


Right-click one of the selected clips and choose Normalize Audio Levels. The Normalize Audio

Level dialog appears.

The Normalize Dialog in the Edit page


Choose the Normalization Mode you want to use. You can choose among a variety of

standardized loudness measurement algorithms, or Sample Peak, or True Peak.


Choose the reference level that you want to set the peak volume of the selected clips to match.


Choose how you want to set the level of multiple selected clips:

When Set Level is set to Relative, all selected clips are treated as if they’re one clip, so that the highest

peak level of all selected clips is used to define the adjustment, and the volume of all selected clips

is adjusted by the same amount. This is good if you have a series of clips, such as a dialog recording,

where the levels are consistent with one another, and you want to normalize all of them together.

When Set Level is set to Independent, the peak level of each clip is used to define the adjustment to

that clip, so that the volume of every selected clip is adjusted by an amount specific to that clip. The

end result may be a set of very different volume adjustments intended to make the peak levels of each

audio clip match one another. This is good if, for example, you’re trying to balance a series of different

sound effects with one another that have very different starting levels.

For more information about loudness normalization, see Chapter 182, “Audio Meters and

Audio Monitoring.”

Keyframing Audio

There are two ways you can keyframe audio in the Edit page. You can use each audio clip’s volume

curve in the Timeline, or you can use the keyframe controls in the Inspector to animate the Volume

parameter of individual clips as you would any other clip attribute, fading the level up or down,

panning from left to right, or dynamically changing any one of a host of filter controls, in subframe

increments, if necessary.

For more information on keyframing in the Inspector, see Chapter 53, “Keyframing Effects

in the Edit Page.” Any keyframes you create using the Keyframe controls of the Inspector

automatically appear on the volume curve of that audio clip in the Timeline.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT