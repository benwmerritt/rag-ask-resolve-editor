---
title: "Common Controls For All Fairlight FX"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 710
---

# Common Controls For All Fairlight FX

Before going into the specific controls of each Fairlight FX plugin, there are some common controls

that all plugins share, found at the top of the custom GUI window for each plugin.

Common controls for all Fairlight FX

�Presets: A cluster of controls that let you recall and save presets specific to each plugin.

Add Preset button: Click this button to save the current settings of the Fairlight FX you’re using.

A dialog box lets you enter a Preset name and click OK.

Preset dropdown menu: All presets for the currently open plugin appear in this menu.

Previous/Next preset buttons: These buttons let you browse presets one by one, going up and

down the list as you evaluate their effects.

�A/B Comparison: A set of buttons that lets you compare two differently adjusted versions of

the same plugin. The A and B buttons let you create two sets of adjustments for that plugin,

and toggle back and forth to hear which one you like better. The arrow button lets you copy

the adjustments from one of these buttons to the other, to save the version you like best while

experimenting further.

�Reset: A single reset control brings all parameters in the current plugin to their default settings.

When the Automation is turned on, an automation button appears at the top right of each of the

plugins. Automatable parameters for that effect are available in the Plugin dropdown menu for

that track.

Flanger���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3958

Foley Sampler�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3959

Frequency Analyzer�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3963

Gain����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3963

LFE Filter������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3964

Limiter������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3964

Meter�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3966

Modulation�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3967

Multiband Compressor�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3969

Noise Reduction��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3970

Phase Meter�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3971

Pitch������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3971

Reverb������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3971

Soft Clipper������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3973

Stereo Fixer�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3974

Stereo Width����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3975

Surround Analyzer����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3975

Vocal Channel������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3976


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

Automation activated and available to the Fairlight FX

NOTE: Although Default is the preset when initially opened, many of the plugins, have

presets already created. Reverb, for instance, has Cathedral, Concert Hall, and Studio presets

built in.

These can be excellent starting points to change, rename, and save for your specific needs.

These new presets will also be available in the Preset dropdown menu.

TIP: Fairlight FX support “granular” control adjustments by holding down the Option or Shift

key while clicking in and dragging left or right within the numerical value fields for virtual

sliders in a Fairlight FX plugin or the Inspector.

Track FX

These built-in Fairlight FX plugins are accessed via the Track FX section of Audio Track channel strips

or in the Inspector. If the Track FX section doesn’t appear in the Mixer, click the three dots in the

upper-right corner of the Mixer and select Track FX.

The available plugins in this category are: Voice Isolation, Dialogue Leveler, Dialogue Separator,

Music Remixer, and Ducker.

Each plugin occupies a fixed, dedicated insert point in the Track FX section, with the Voice Isolation and

Dialogue Leveler visible by default. To reveal the other Track FX plugins, click the three dots in the upper-

right corner of the Mixer and select each plugin from the “Visible Track FX” submenu at the bottom.

TIP: Track effects can be applied to stereo-linked groups (stereo-linked tracks).

The Mixer menu


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

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

Dialogue Leveler controls:

�Dialogue Leveler: Enables or disables the plugin.

�Waveform Processing display: This shows a scrolling waveform and a gray line indicating

Dialogue Leveler processing. However, this display is not available when using the Dialogue

Leveler found in the Inspector to process audio clips on the timeline.

�Preset Menu: This menu provides the following options:

Allow wider dynamics: This is the default and is best for audio with a wider-ranging

dynamic from loud-to-soft, and where the clip levels are medium to high.

More lift for low levels: Select this option if the source has more low-level

dialogue that you want to boost.

Lift soft whispery sources: Select this option if the source has whispered

dialogue and background noise.

Optimize moderate levels: Select this option if the source is at medium levels throughout.

�Reduce Loud Dialogue: When enabled, louder dialogue is ridden downward when it peaks, acting

like a “perfect limiter” where you don’t have to adjust the threshold or time parameters. Due to the

“near real-time” functionality, analysis occurs prior to audible playback for optimal results.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

�Lift Soft Dialogue: This setting finds and lifts low-level dialogue, evening-out material that is

quieter while more variable in level. Because the process is dialogue-focused, it doesn’t tend to

raise background sounds unless they’re audible at the same time as the dialogue.

The Lift Soft Dialogue option is often the most useful of the three options, as it makes quieter lines

of dialogue louder and naturally smooth without boosting background noise.

�Background Reduction: This option gently removes background noise based on the internal

preset selected in the Preset menu.

�Output Gain: You can use this control to adjust the output level by clicking and dragging it or

entering a value in the numeric field. The range of the Output Gain control of 0.0 to +6.0 dB.

TIP: Before using the Dialogue Leveler on a track, it can be useful to set an optimum baseline

level for use with the default “Allow wider dynamics” preset by normalizing the audio.

For more information on normalizing audio, see Chapter 176, “The Fairlight Inspector.”

Dialogue Separator (Studio Version Only)

Dialogue Separator uses DaVinci Neural Engine AI to give you individual control over the level of

dialogue, background sounds, and the reverberant field or ambient room sound (“ambience”).

The Dialogue Separator plugin

The Dialogue Separator is useful when, for example, a source file has a great roomy sound, but there’s

music or crowd noise in the background. In this instance, you can rebalance the audio to reduce the

background sounds or adjust the room sound to make the dialogue more intelligible.

Another use case would be when someone moves toward the camera in a roomy environment while

speaking. You could use automation to rebalance the audio so that the ambient room sound gradually

becomes “drier” as they get closer, without affecting the background.

Dialogue Separator is currently a mono-only plugin. If your source is stereo, you’ll need to split it into

dual-mono and process both mono tracks separately.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT

Ducker

This plugin lets you use the audible signal from a track or multiple tracks to lower the level of another.

Although it can be used in many creative ways, a common use of “ducking” is automatically lowering a

music or sound effects bed so that dialogue or a VO track can be heard more prominently in a mix.

This is achieved without compressing the incoming signals. When set up correctly in the Ducker

interface or via the Audio tab in the Inspector, your audio tracks can practically “mix themselves.”

In a simple use case, the Ducker uses level changes of a single incoming dialogue or VO track to

decrease the volume of the sound effects bed of a noisy freeway.

In a more complex situation, such as a scene where three characters are conversing next to the same

noisy freeway, a single Ducker plugin can use the level changes of each dialogue track to attenuate

the traffic noise.

With only one input source (Dialogue 1), the Ducker would only be effective when the first character

speaks. However, this new feature lets you add the other two dialogue tracks (Dialogue 2 and

Dialogue 3)  as input sources for attenuating the traffic noise.

The Ducker plugin

Using the Ducker

Continuing with the use cases mentioned above:


Choose the target track that you want to attenuate (the Freeway Traffic track), and open

the Ducker.


Click the Source dropdown and select Dialogue 1 as the input source.

�To use additional input sources, Command-click the other track names; in this example,

Dialogue2 and Dialogue3.

�Play a bit of your sequence, and adjust the duck level and other controls to taste.

Adding Input Sources via the Inspector

If you prefer working within the Inspector:


Select the Freeway Traffic track, ensure the Ducker is switched on, and open the Inspector’s

Audio tab.


Click the plus sign to the right of the Source 1 dropdown containing Dialogue 1 to create a

dropdown menu for Source 2, then choose Dialogue2 from the list.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT


Click the plus sign to the right of the Source 2 dropdown to create a dropdown menu for Source 3,

then choose Dialogue3 from the list.

Adding Ducker input sources in the Inspector

Ducker Controls

�Duck Amount: This control determines level attenuation on the target track in dB with a default

value of 2.7 dB. Most of the time, a value between 2.0 dB and 5.0 dB works the best.

�Lookahead: Adjusts the amount of lookahead time in milliseconds, with a default value of

15ms. Lookahead allows the Ducker to start attenuating the destination track before the

source track is audible.

The larger the value, the more the Ducker will “pre-anticipate” the source track. If you want the

Ducker to start lowering the sound before a line of dialogue or VO begins, you can experiment

with higher values, but the default will usually produce good results.

�Rise Time: This determines how many milliseconds it takes for the Ducker to reach the amount of

reduction specified by the Duck Amount. The default value is 10 milliseconds, which should work

for most situations. Longer Rise Times may be useful with higher Duck Amount values and longer

gaps in the source track.

�Hold: This parameter determines how long the target signal will be attenuated. The default is 150ms.

�Recovery Time: This value indicates how quickly the target signal will return to its previous level

after attenuation. The default time value is 750ms, but setting the correct Recovery time is crucial

to a natural-sounding ducking process, so you should try different values to find the best results.

Ducker Graph Display

This area shows a gray line representing the incoming signal against the action of the Ducker, shown

in yellow. Dips in the yellow line signify attenuation of the target track based on the Duck Amount in

combination with the other parameters.


Fairlight | Chapter 181 Fairlight FX

FAIRLIGHT