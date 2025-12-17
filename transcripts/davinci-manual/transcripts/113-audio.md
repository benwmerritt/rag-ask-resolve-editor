---
title: "Audio"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 113
---

# Audio

The Audio Inspector Clip and Track parameters

The Audio Inspector can work on both individual clips or entire tracks, based on which icon is selected

in the upper left of the Inspector. Normally this option automatically adjusts for you based on what

you have selected in the timeline. For example, when you click on an audio clip in the timeline,

the Inspector will open in Clip mode, and if you click on an audio track header in the timeline, the

Inspector will switch to Track mode automatically. These can always be manually overridden simply by

clicking on the appropriate icon. Clip and Track modes contain different options for audio editing.

The Audio Inspector in Clip mode (circled)

The Audio Inspector in Track mode (circled)


The Cut Page | Chapter 30 Using the Inspector in the Cut Page

CUT

The Audio tab contains commonly used audio controls for video editing purposes, including Volume,

Pan, Pitch, and Equalizer. It also contains several incredibly useful DaVinci Neural Engine powered

tools like Voice Isolation, Dialog Leveler, and Music Remixer.

�Volume: Each clip has a single volume control that corresponds to the volume overlay over each

audio clip.

�Pan: A simple Pan slider that controls stereo panning. While most professional mixes will restrict

panning to the more robust panner found in the Fairlight page Mixer, this simple Pan control is

useful for editors of visuals working in the Edit page to quickly create simple panning effects to aid

in a craft edit.

�Voice Isolation (Studio Version Only): Voice Isolation is a plugin that can remove loud,

undesirable sounds from existing voice recordings. This effect utilizes AI to provide models that

let you completely remove undesired sounds. The AI model is trained for any type of human voice,

male or female, young or old, so you can get incredible results that isolate dialog from background

sounds in a recording, including everything from air conditioning or fans to extremely loud sounds

like a jackhammer, restaurant background noise, or music playing at the same time that the subject

is speaking, and so on.

For more information about Voice Isolation, see Chapter 31, “Video and Audio Effects in

the Cut Page.”

Amount: Lets you adjust the amount of voice isolation processing.

For more information about Voice Isolation, see Chapter 181, “Fairlight FX.”

�Dialogue Leveler: The Dialogue Leveler analyzes source material to detect dialog and then “ride

down” louder areas, “lift up” softer areas, and lower background sounds that are not dialog. It

works without typical dynamics processor “pumping” (compression/limiting) or other obvious

side effects and produces results similar to detailed manual clip gain adjustments or by carefully

“riding” the track with fader automation.

Preset Menu: The preset menu provides the following options:

�Optimized for most sources: This option is selected by default and works well for most sources.

�More lift for low levels: Select this option if the source has more low level dialog that you

want to boost.

�Lift soft whispery sources: Select this option if the source has whispered dialog and

background noise.

Reduce Loud Dialogue: When enabled, louder dialogue is ridden downward on peaks and acts

somewhat like a “perfect limiter” where you don’t have to adjust threshold or time constants.

Due to the “near real time” aspect, analysis occurs prior to audible playback for optimal results.

Lift Soft Dialogue: When enabled, finds low level dialogue and lifts and evens out material that is

more variable in level and softer, but because the process is dialogue focused, it doesn’t tend to

raise background sounds (unless they are happening at the same time as the dialogue itself). More

often than not, the Lift Soft Dialogue option is the most useful of the three options, as it makes less

audible lines of dialogue more audible and naturally smooth, while not boosting background noise.

Background Reduction: When enabled, reduces background sounds by focusing on dialogue and

gently removing them based on the internal presets (Preset menu).

Output Gain: Adjust the Output Gain by clicking and dragging on the Output Gain control

or by entering a value in the numeric field (Output Gain control in dB with 0 to +6 dB range

with .1dB resolution).


The Cut Page | Chapter 30 Using the Inspector in the Cut Page

CUT

�Dialogue Separator (Track Mode Only): The Dialogue Separator uses DaVinci Neural Engine AI

to give you individual control over the level of dialogue, background sounds and “ambience,” the

reverberant field, or ambient room sound. If you have a source file that contains a great roomy

sound, but there is music in the background or crowd noises, you can rebalance so that the

background sounds come down a bit, or adjust the room sound down a bit for better intelligibility.

For more information about the Dialogue Separator, see Chapter 31, “Video and Audio

Effects in the Cut Page.”

�Music Remixer: The Music Remixer is a DaVinci Neural Engine AI-based effect. This Track FX

plugin uses AI to split music into individual basic stems: Vocals, Drums, Bass, Guitar and “Other,”

which means “everything else.” You can use the level controls to rebalance or remix the sources,

or the mute buttons to make instant changes and bring parts in and out of your mix. Music Remixer

lets you creatively adjust a music track to suit your needs. For example, you might have a track

where you need to remove the vocal or rearrange to allow for quieter moments or a build.

For more information about the Music Remixer, see Chapter 31, “Video and Audio Effects

in the Cut Page.”

�Music Editor: Allows you to seamlessly extend or shorten music to the length of your edit. You can

enter a desired duration and press the Adjust button in order to shorten or extend the clip to that

duration. Music Editor does not use time compression/expansion or alter the pitch of the music,

but instead uses editing techniques like a music editor might to fit the material to desired length

to picture. It will look for logical places to create transitions based on whether you’re extending

length (by repeating sections), or removing material, and attempt to use the ending or fade of

the original composition, if it times well. If the ending is abrupt, it’s up to you to manually create

a fade out.

For more information about the Music Editor, see Chapter 31, “Video and Audio Effects in

the Cut Page.”

NOTE: Music Editor is an “intelligent edit” that works effectively with beat driven music

(pop, dance, etc.). It is not intended for free form, ambient, or non-beat driven material.

�Ducker (Track Mode Only): The Ducker Track FX plugin allows you to automatically lower the level

of a track by using an external source signal – this is known as “ducking.” Most commonly, ducking

is used to have dialogue or VO automatically lower a music or sound effects bed, but it can be

used in many creative ways. Set up correctly, your sources can often “mix themselves,” and you

can create very useful results.

The Ducker uses changes in level only to do its work; the audio is not compressed or

limited. For more information about the Ducker, see Chapter 31, “Video and Audio Effects

in the Cut Page.”


The Cut Page | Chapter 30 Using the Inspector in the Cut Page

CUT

Choose the target track that you want to affect (the “destination” track), and open the Ducker.

Source: This is the source track you want to use to duck the level of the target track. You can add

multiple or remove additional source tracks by pressing the +/- buttons to the right.

Duck Level: Adjust the amount of “ducking” applied.

�Pitch: Lets you alter the pitch of a clip without changing the speed. Two sliders let you adjust clip

pitch in semi tones (large adjustments, a twelfth of an octave) and cents (fine adjustments, 100th of

a semi tone).

Equalizer

This six-band parametric equalizer has both graphical and numeric controls for boosting or attenuating

different ranges of frequencies within that clip, before it even gets to the EQ built into the Mixer. Each

band has controls for the filter type (Bell, Lo-Shelf, Hi-Shelf, Notch), Frequency, Gain, and Q-factor

(sharpness of the band), with the available controls for each band of EQ changing depending on the

filter type.

TIP: Clip EQ settings can be copied and pasted from one Clip EQ to another, and between

Clip EQ and Track EQ instances.

Clip  EQ in the Audio Inspector

Master EQ Controls

The Equalizer window has the following overall controls located in the

upper‑right and left corners:

•	 Enable button: Turns the overall EQ effect off and on, without resetting the controls.

•	 Reset button: Resets all controls of the EQ window to their defaults.


The Cut Page | Chapter 30 Using the Inspector in the Cut Page

CUT

Clip EQ Graph

This graph displays the current EQ curve with handles that correspond to each enabled

EQ band listed below. You can drag any numbered handle to boost or attenuate the range

of frequencies governed by that band, using whatever type of equalization that band has

been set to.

The Clip EQ graph with user-draggable handles

Dragging the numbered handles on this graph in turn modifies the parameters of the

corresponding band, and changing each band’s parameters will also alter the EQ graph, which

serves the additional purpose of providing a graphical representation of the equalization

being applied to that track.

Bands 1 and 6

The outer two sets of band controls let you make high-pass and low-pass adjustments, if necessary.

�Band enable button: Turns each band of EQ on and off.

�Band filter type: Bands 1 and 6 can be switched among five specific filtering options for

processing the lowest or highest frequencies in the signal.

�For Band 1, these include (from top to bottom): Lo-Shelf, Bell, Notch, Hi-Shelf, and Hi-Pass.

�For Band 6, the options are (from top to bottom): Lo-Pass, Lo-Shelf, Bell, Notch, and Hi-Shelf.

�Freq: Adjusts the center frequency of the EQ adjustment.

�Gain: Adjusts the amount by which the affected frequencies are impacted. Negative values

attenuate those frequencies, while positive values boost those frequencies.

�Q Factor: This parameter adjusts the width of affected frequencies and appears whenever the

Bell option is selected. Lower values include a wider range of frequencies; higher values include a

narrower range of frequencies.

Bands 2 through 5

These band controls let you make a wide variety of equalization adjustments.

�Band enable button: Turns each band of EQ on and off.

�Band filter type: These Bands offer four filtering options (from top to bottom): Lo-Shelf, Bell, Notch,

and Hi-Shelf.

�Frequency: Adjusts the center frequency of the EQ adjustment.

�Gain: Adjusts the amount by which the affected frequencies are impacted. Negative values

attenuate those frequencies, while positive values boost those frequencies.

�Q Factor: This parameter appears when the Bell setting is selected. It adjusts the width of

affected frequencies. Lower values include a wider range of frequencies; higher values narrow the

range of frequencies.


The Cut Page | Chapter 30 Using the Inspector in the Cut Page

CUT

NOTE: There are many more refined plugins and effects for audio clips in the Audio FX

library. If you apply any of these, the controls will appear in the Inspector’s Effects tab Audio

section, instead of here.