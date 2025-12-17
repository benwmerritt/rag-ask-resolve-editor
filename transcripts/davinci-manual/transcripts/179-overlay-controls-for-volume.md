---
title: "Overlay Controls for Volume"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 179
---

# Overlay Controls for Volume

Each audio clip in the Timeline appears with a Volume overlay control on top of it, that by default starts

out completely flat. Similar to such controls found in other applications, the level curve lets you alter

each clip’s levels, either overall, or dynamically using keyframes.

Volume curves adjusting the level of a clip’s audio in the Timeline

Additionally, you can click any clip’s Audio Curve Editor button, at the bottom right-hand

corner of each audio clip, to open an audio-specific Curve Editor in which you can also

keyframe volume.

The button for opening an audio clip’s Curve Editor

How to Add and Adjust Volume Keyframes

Mixing audio by adding and adjusting individual keyframes can be a fast and effective way of

balancing clip levels with one another, fixing level problems within a particular clip, or even creating

simple mixes (although the mixing capabilities of the Fairlight page are considerably more robust).

When manually editing any audio parameter curve, you can use the following procedures.

Methods of adding or selecting audio keyframes using the pointer:

�To add keyframes to the Volume curve: Hold the Option key down and click the curve to

place a keyframe at that frame. You must add at least two keyframes to create an automated

change in Volume.

�To select one or more keyframes: Click any keyframe to select it.

�To select multiple discontiguous keyframes: Command-click all keyframes you want to select,

whether they’re next to one another or not.

�To select multiple contiguous keyframes: Click the first keyframe you want to select, and then

shift-click the last keyframe you want to select, and all keyframes between will also be selected.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Methods of adjusting keyframes in the Volume overlay (or curve) using the pointer:

�To adjust any curve segment: Position the pointer over the overall segment for clips with no

keyframes, or position it between any two keyframes, directly on top of the curve segment you

want to raise or lower. When the Move cursor is displayed, click and drag up to raise the volume,

or down to reduce the volume.

�To adjust a keyframe in any direction: Move the pointer over a keyframe so that the four-

way cursor appears, and then click and drag up or down to change the volume, or side

to side to change its timing. The timing of audio keyframes can be adjusted in subframe

increments, for precision mixing.

�To adjust a keyframe in only one direction: Move the pointer over a keyframe so that the four-

way cursor appears, press Shift, and click and drag in the intended direction of adjustment, either

vertically to change the volume of the clip at that frame, or horizontally to move the keyframe to

a different point in time. Once you start dragging a keyframe into a particular direction, keyframe

movement is constrained in that direction until you release that keyframe. The timing of audio

keyframes can be adjusted in subframe increments, for precision mixing.

�To change one or more Linear keyframe to Ease In or Ease Out: Eased keyframes create

animated changes that begin slowly and accelerate to full speed, or slow down gradually to

decelerate to a stop. This only works when you have two or more keyframes creating an animated

effect. Select one or more keyframes, then right-click one of the selected keyframes and choose

Ease In, Ease Out, or Ease In and Out, depending on which keyframe you’re editing and the effect

you want to create.

�To change one or more eased keyframes to Linear: Select one or more keyframes, then right-

click one of the selected keyframes and choose Linear.

Methods of Cutting, Copying, Pasting, and Deleting keyframes:

�To cut or copy, and paste one or more keyframes: Make a selection of keyframes, and use the

Cut (Command-X) or Copy (Command-C) key shortcuts. Then, move the playhead to where you

want the first of the copied keyframes to start, and press Paste (Command-V).

�To delete one or more control points from a curve: Select the keyframe(s) you want to delete and

press Backspace.

Audio Fade Handles

When you position the pointer directly over an audio clip, a pair of Audio Fade handles appear at the

In and Out points. Dragging each of these handles towards the center of the clip lets you fade in the

clip volume at the beginning of the clip, and fade out the clip volume at the end of the clip.

Audio Fade handles at either end of an audio clip


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

NOTE: When you import a Final Cut Pro X project, the fade handles for each clip

automatically import as well.

Audio Fade Handles can also be adjusted in subframe increments, if necessary, to

create a precise transition.

Adjusting an Audio Fade handle in subframe increments,

seen within a one-frame playhead shadow

Once you’ve created a fade effect, you can adjust the curve of the fade by dragging the handle that

appears right on top of the fader curve. Dragging the handle up and down affects the angle of the

curve, and dragging the handle left and right affects the shape of the curve. In this way, you can create

all manner of fade effects.

Adjusting the curve of the fade Fade effects can

be created and edited on both the Edit and Fairlight pages.

Audio Crossfades

When you select an edit point with both video and audio components, and Linked Selection is

enabled so that both the video and audio edit points are selected, then when you apply a video

transition to an edit, a crossfade is added to the audio.

You can add Cross Fade transitions to any edit point between two audio clips that have enough

handles similarly to how you add video transitions, by dragging and dropping from the Effects Library,

by right-clicking an edit and choosing an option from the contextual menu, or by selecting an audio

edit point and choosing Timeline > Add Audio Only Transition (Shift-T).

Cross Fade transitions are a quick and easy way to fade the volume of the outgoing clip down while

simultaneously fading the volume of the incoming clip up, letting you create a smooth aural transition

between two audio clips. If you need to do precision editing, the start and end points of a crossfade

can be edited in sub-frame increments.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

An audio Cross Fade transition applied between two clips

You can double-click a Cross Fade transition to open it into the Inspector, revealing

the following parameters:

�Duration: The duration of the transition, shown in both seconds and frames.

�Alignment: A drop-down that lets you choose the transition’s position relative to the edit point it’s

applied to. Your choices are “End on Edit,” “Center on Edit,” and “Begin on Edit.”

�Transition style: You can choose –3dB, 0dB, or +3dB to set both the Fade In and Fade Out levels

to the same value. For more information on what these levels mean, see the following parameter.

�Fade In/Fade Out levels: There are three options that affect the incoming and outgoing halves of

the Cross Fade effect independently. 0dB applies a linear fade (this is the default). +3dB applies a

boosted curve; when applied to both Fade In and Fade Out, this can compensate for diminished

levels in the middle of a Cross Fade. –3dB applies an attenuating curve, which deliberately lowers

the level of the Cross Fade.

Crossfades can be created and edited on both the Edit and Fairlight pages.

TIP: If you need an asymmetrical crossfade, that’s accomplished by “checkerboarding”

clips on two tracks with overlapping handles at the beginning and end, and using the Fader

handles to create exactly the timing and curves necessary to create the effect you require.

Voice Isolation (Studio Version Only)

Voice Isolation uses an AI model trained for any type of human voice, male or female, young or old,

which lets you completely remove loud, undesirable sounds from existing voice recordings with

incredible results.

You can get rid of all kinds of background noise, from air conditioners or fans to jackhammers,

restaurant background noise, music playing during a featured piece of dialogue, and more.

The Amount control adjusts the mix between the original source and the isolated voice. When

set to 50, the mix is roughly equal. Values between 70 and 80 work well for natural results while

strongly isolating the source.

Although Voice Isolation can be used on an audio track in real time, it cannot be used on live audio

input. It can be used on any mono, stereo, or dual-mono audio track, but it isn’t supported on tracks

with more than two channels.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

The Voice Isolation plugin

Dialogue Leveler

The Dialogue Leveler analyzes source material to detect dialogue and then “rides down” louder areas,

“lifts up” softer areas, and lowers background sounds that are not dialogue.

It works without the typical “pumping” or other unwanted side effects of dynamics processors

(compression/limiting) to produce results like those achieved through detailed, manual clip gain

adjustments or “riding” the track with fader automation.

The Dialogue Leveler can often “fix and mix” a recording made with a single boom mic, where one

character is closer than another or turns away from the mic and levels it out so that the original relative

dynamics are preserved while increasing intelligibility and average level.

The Dialogue Leveler plugin

Although Dialogue Leveler can be used on an audio track in real time, it cannot be used on live audio

input. It can be used on any mono, stereo, or dual-mono audio track, but it isn’t supported on tracks

with more than two channels.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Dialogue Leveler controls:

Dialogue Leveler: Enables or disables the plugin.

�Waveform Processing display: This shows a scrolling waveform and a gray line indicating

Dialogue Leveler processing. However, this display is not available when using the Dialogue

Leveler found in the Inspector to process audio clips on the timeline.

�Preset Menu: This menu provides the following options:

Allow wider dynamics: This is the default and is best for audio with a wider-ranging dynamic from

loud to soft, and where the clip levels are medium to high.

More lift for low levels: Select this option if the source has more low-level dialogue that you want

to boost.

Lift soft whispery sources: Select this option if the source has whispered dialogue and

background noise.

Optimize moderate levels: Select this option if the source is at medium levels throughout.

�Reduce Loud Dialogue: When enabled, louder dialogue is ridden downward when it peaks, acting

like a “perfect limiter” where you don’t have to adjust the threshold or time parameters. Due to the

“near real-time” functionality, analysis occurs prior to audible playback for optimal results.

�Lift Soft Dialogue: This setting finds and lifts low-level dialogue, evening out material that is

quieter while more variable in level. Because the process is dialogue-focused, it doesn’t tend to

raise background sounds unless they’re audible at the same time as the dialogue.

The Lift Soft Dialogue option is often the most useful of the three options, as it makes quieter lines

of dialogue louder and naturally smooth without boosting background noise.

�Background Reduction: This option gently removes background noise based on the internal

preset selected in the Preset menu.

�Output Gain: You can use this control to adjust the output level by clicking and dragging it or

entering a value in the numeric field. The range of the Output Gain control of 0.0 to +6.0 dB.

TIP: Before using the Dialogue Leveler on a track, it can be useful to set an optimum baseline

level for use with the default “Allow wider dynamics” preset by normalizing the audio.

For more information on normalizing audio, see Chapter 176, “The Fairlight Inspector.”


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT