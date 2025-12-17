---
title: "Audio"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 118
---

# Audio

A slider lets you adjust audio levels of the current clip in the Viewer, making the volume of that audio

clips softer or louder. This is identical to each clip’s volume setting in the Edit and Fairlight pages.

Audio controls in the Viewer

Effects Overlay

Turning on either Open FX or Fusion overlays lets you use the on screen viewer controls for those

effects that use them.

The Effects overlay activates the on screen viewer controls for effects.

Smart Reframe (Studio Version Only)

The Smart Reframe feature in DaVinci Resolve makes it easier to quickly reframe material across

extreme aspect ratio changes. It’s useful for situations where you’ve shot a 16:9 horizontal video and

find yourself needing to create a vertically-oriented 9:16 version for mobile phones and social media

deliverables or using 4:3 archival footage in a 2.39:1 widescreen movie. Smart Reframe can be used

manually or automatically executed using the DaVinci Resolve Neural Engine.

Smart Reframe in action with the Reference Point bounding box active (right)

The Smart Reframe tool is found in the Sizing tab of the Inspector and is available in both the Cut and

Edit pages.


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

To use the Smart Reframe tool:


Duplicate your Timeline, right-click the Timeline and choose Timelines > Timeline Settings, and click

Use Custom Settings to change the Timeline Resolution to the aspect ratio needed for delivery.

Make sure that “Mismatched resolution files” is set to “Scale full frame with crop,” and click OK.


Select one or more clips you want to reframe, and open the Inspector to the Video tab.


Open the Smart Reframe controls, leave the Object of Interest drop-down menu set to Auto

(if you’ve selected more than one clip, Auto is the only setting available), and click “Reframe.”

DaVinci Resolve will analyze your footage and should automatically adjust each individual clip’s

position to a more aesthetically pleasing framing.


(Optional) If the “Auto” setting does not give you desirable results for a particular clip, you can

manually select the main subject using the following steps.

a)	 To manually select the subject area, choose “Reference Point” from the Object of Interest

drop-down menu, and click the Target icon just to the right of the menu. This automatically sets

the Viewer mode to Smart Reframe, exposing the onscreen controls for choosing a reference.

b)	 Drag the Reference Point bounding box around the main subject of interest in the frame.

You may use the Transform controls directly above in the Inspector to move the source clip

around if your subject is outside the current framing.

c)	 Click “Reframe.”

The Inspector’s Smart Reframe controls showing

the manual reference point selected

DaVinci Resolve locks onto and, if necessary, tracks your subject using the reference you’ve selected,

automatically panning and scanning the original clip as needed to keep the reference within the new

aspect ratio. While involving a bit of manual adjustment, this function still dramatically reduces the time

involved in pan and scanning footage by manually adjusting and keyframing the sizing controls.

Voice Isolation (Studio Version Only)

Voice Isolation uses an AI model trained for any type of human voice, male or female, young or old,

which lets you completely remove loud, undesirable sounds from existing voice recordings with

incredible results.

The Voice Isolation plugin


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

You can get rid of all kinds of background noise, from air conditioners or fans to jackhammers,

restaurant background noise, music playing during a featured piece of dialogue, and more.

The Amount control adjusts the mix between the original source and the isolated voice. When set

to 50, the mix is roughly equal. Values between 70 and 80 work well for natural results while strongly

isolating the source.

Although Voice Isolation can be used on an audio track in real time, it cannot be used on live audio

input. It can be used on any mono, stereo, or dual-mono audio track, but it isn’t supported on tracks

with more than two channels.

Dialogue Leveler

The Dialogue Leveler analyzes source material to detect dialogue and then “rides down” louder areas,

“lifts up” softer areas, and lowers background sounds that are not dialogue.

It works without the typical “pumping” or other unwanted side effects of dynamics processors

(compression/limiting) to produce results like those achieved through detailed, manual clip gain

adjustments or “riding” the track with fader automation.

The Dialogue Leveler can often “fix and mix” a recording made with a single boom mic, where one

character is closer than another or turns away from the mic. and levels it out so that the original relative

dynamics are preserved while increasing intelligibility and average level.

The Dialogue Leveler plugin

Although Dialogue Leveler can be used on an audio track in real time, it cannot be used on live audio

input. It can be used on any mono, stereo, or dual-mono audio track, but it isn’t supported on tracks

with more than two channels.

Dialogue Leveler controls

Dialogue Leveler: Enables or disables the plugin.

Waveform Processing display: This shows a scrolling waveform and a gray line indicating

Dialogue Leveler processing. However, this display is not available when using the

Dialogue Leveler found in the Inspector to process audio clips on the timeline.


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

Preset Menu: This menu provides the following options:

•	 Allow wider dynamics: This is the default and is best for audio with a wider-ranging dynamic

from loud to soft, and where the clip levels are medium to high.

•	 More lift for low levels: Select this option if the source has more low-level dialogue that you

want to boost.

•	 Lift soft whispery sources: Select this option if the source has whispered dialogue and

background noise.

•	 Optimize moderate levels: Select this option if the source is at medium levels throughout.

Reduce Loud Dialogue: When enabled, louder dialogue is ridden downward when it peaks,

acting like a “perfect limiter” where you don’t have to adjust the threshold or time parameters.

Due to the “near real-time” functionality, analysis occurs prior to audible playback for

optimal results.

Lift Soft Dialogue: This setting finds and lifts low-level dialogue, evening out material that is

quieter while more variable in level. Because the process is dialogue-focused, it doesn’t tend

to raise background sounds unless they’re audible at the same time as the dialogue.

The Lift Soft Dialogue option is often the most useful of the three options, as it makes quieter

lines of dialogue louder and naturally smooth without boosting background noise.

Background Reduction: This option gently removes background noise based on the internal

preset selected in the Preset menu.

Output Gain: You can use this control to adjust the output level by clicking and dragging it or

entering a value in the numeric field. The range of the Output Gain control of 0.0 to +6.0 dB.

TIP: Before using the Dialogue Leveler on a track, it can be useful to set an optimum baseline

level for use with the default “Allow wider dynamics” preset by normalizing the audio.

For more information on normalizing audio, see Chapter 176, “The Fairlight Inspector.”

Music Remixer (Studio Version Only)

This DaVinci Neural Engine AI-based plugin splits music into individual stems: Vocals, Drums, Bass,

Guitar, and “Other” (“everything else”), letting you creatively rebalance or remix the track.

You can use the level controls to adjust the volume of each stem and the Mute buttons to remove

or bring them back into your mix. For example, you may want to remove or lower a vocal because it

clashes with a featured piece of dialogue.


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

The Music Remixer plugin

Music Editor (Studio Version Only)

DaVinci Resolve 20 supports seamlessly extending or shortening music to the length of your edit.

The new AI powered Music Editor can be accessed in the Audio tab of the Inspector. You can enter a

desired duration and press the Adjust button in order to shorten or extend the clip to that duration.

Note: Music Editor is an “intelligent edit” that works effectively with beat-driven music (pop, dance,

etc.). It is not intended for free form, ambient or non-beat driven material.

Music Editor does not use time compression/expansion or alter the pitch of the music, but instead uses

editing techniques like a music editor might to fit the material to desired length to picture. It will look for

logical places to create transitions based on whether you’re extending length (by repeating sections),

or removing material, and attempt to use the ending or fade of the original composition if it times well.

If the ending is abrupt, it’s up to you to manually create a fade out.

The Music Editor in the Audio Inspector

To Use Music Editor to retime a music clip:


Select the clip on the timeline you wish to retime. This clip does need to be beat-driven music.


In the Audio Inspector under AI Music Editor, enter a new Target Length for the music duration

you want.


Press the Adjust button.


Alternatively, you can check the Live Trim box to use the Trim tools to resize the clip and

dynamically retime the music on the timeline. You can turn the checkbox off to return to normal

editing (e.g., trimming) for that clip after the desired edit has been created.

Once the analysis is complete, four versions of potential edits you can use appear at the bottom,

each with a different approach to the edit, numbered 1-4. Any subsequent editing can be done almost

instantaneously. The edited pieces of music show indicators on the clip to mark the portions where

cuts and transitions occur.


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

The initial music is too long

The Music Editor has retimed the audio clip to match the length of the video.

Note the jagged lines on the audio clip indicating where the original was cut.

In the waveform you can see the end of the music is retained in the retimed clip.

TIP: While timings can be quite close, sometimes they may not be exact. If you need to get

an exact timing after working with AI Music Editor, you might use the Elastic Wave tool on the

Fairlight page and choose the algorithm for general purpose (music).

The edited clip is actually a specialized Music Editor clip which allows you to further trim your edit. If

you want to access the underlying edit, you can also right-click on the clip and decompose, exposing

the edit points and any crossfades created. However, keep in mind that once decomposed, you can’t

trim the length of the clip as an entity as each editing snippet is now a separate clip.