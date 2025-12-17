---
title: "Dialogue Separator Track FX"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 119
---

# Dialogue Separator Track FX

(Studio Version Only)

Dialogue Separator uses DaVinci Neural Engine AI to give you individual control over the level of

dialogue, background sounds, and the reverberant field or ambient room sound (“ambience”).

The Dialogue Separator is useful when, for example, a source file has a great roomy sound, but there’s

music or crowd noise in the background. In this instance, you can rebalance the audio to reduce the

background sounds or adjust the room sound to make the dialogue more intelligible.

Another use case would be when someone moves toward the camera in a roomy environment while

speaking. You could use automation to rebalance the audio so that the ambient room sound gradually

becomes “drier” as they get closer, without affecting the background.

Dialogue Separator is currently a mono-only plugin. If your source is stereo, you’ll need to split it into

dual-mono and process both mono tracks separately.


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

The Dialogue Separator plugin

Ducker Track FX

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

Dialogue 3) as input sources for attenuating the traffic noise.

The Ducker plugin


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

Using the Ducker

Continuing with the use cases mentioned above:


Choose the target track that you want to attenuate (the Freeway Traffic track), and open the Ducker.


Click the Source dropdown and select Dialogue 1 as the input source.

�To use additional input sources, Command-click the other track names; in this example,

Dialogue2 and Dialogue3.

�Play a bit of your sequence, and adjust the duck level and other controls to taste.

Adding Input Sources via the Inspector

If you prefer working within the Inspector:


Select the Freeway Traffic track, ensure the Ducker is switched on, and open the Inspector’s

Audio tab.


Click the plus sign to the right of the Source 1 dropdown containing Dialogue1 to create a

dropdown menu for Source 2, then choose Dialogue2 from the list.


Click the plus sign to the right of the Source 2 dropdown to create a dropdown menu for Source 3,

then choose Dialogue3 from the list.

Adding Ducker input sources in the Inspector

Ducker Controls

•	 Duck Amount: This control determines level attenuation on the target track in dB with a

default value of 2.7 dB. Most of the time, a value between 2.0 dB and 5.0 dB works best.

•	 Lookahead: Adjusts the amount of lookahead time in milliseconds, with a default value of

15ms. Lookahead allows the Ducker to start attenuating the destination track before the

source track is audible.


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

The larger the value, the more the Ducker will “pre-anticipate” the source track. If you want

the Ducker to start lowering the sound before a line of dialogue or VO begins, you can

experiment with higher values, but the default will usually produce good results.

•	 Rise Time: This determines how many milliseconds it takes for the Ducker to reach the

amount of reduction specified by the Duck Amount. The default value is 10 milliseconds,

which should work for most situations. Longer Rise Times may be useful with higher Duck

Amount values and longer gaps in the source track.

•	 Hold: This parameter determines how long the target signal will be attenuated.

The default is 150ms.

•	 Recovery Time: This value indicates how quickly the target signal will return to its previous

level after attenuation. The default time value is 750ms, but setting the correct Recovery

time is crucial to a natural-sounding ducking process, so you should try different values to

find the best results.

Ducker Graph Display

This area shows a gray line representing the incoming signal against the action of the Ducker,

shown in yellow. Dips in the yellow line signify attenuation of the target track based on the

Duck Amount in combination with the other parameters.

Beat Detector (Studio Version Only)

DaVinci Resolve can automatically detect beats for a piece of music on the timeline, and supports

snapping to these beat marker locations. This can be especially useful when trying to make edits

to the beat.

NOTE: The Beat Detector will only work effectively with beat-driven music, and with 4/4 or

3/4 time signatures at this time.

To detect beats, right-click on the timeline audio clip and select Detect Music Beats from the context

menu. Once analyzed, the timeline clip displays beat indicator overlays that you can snap other

timeline elements to.

A music track with the Beat Detector applied. The lined overlays match up with the beat of the music.


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

Dialogue Matcher (Studio Version Only)

Dialogue Matcher allows you to match one piece of dialogue to another, matching level, EQ, and

reverb. This can help with situations where new recordings may not match the environment of existing

ones. The Dialogue Matcher is a fully automated tool that only requires the user to capture a tone

profile from a clip and then to apply it to another.

Capturing a Dialogue Profile from a clip using the main menu

To Use Dialogue Matcher:


Select a reference clip whose dialogue you want to match, right-click, and choose Clip > AI Tools >

Dialogue Matcher > Capture Dialogue Profile.


Select the clip whose dialogue you want to change, right-click and choose Clip > AI Tools >

Dialogue Matcher > Apply Dialogue Profile.


You can enable or disable the Dialogue Matcher on a clip by right-clicking and choosing Clip > AI

Tools > Dialogue Matcher > Enable.


You can Remove the Dialogue Matcher on a clip by right-clicking and choosing Clip > AI Tools >

Dialogue Matcher > Remove Applied Profile.

Audio Assistant (Studio Version Only)

With the Audio Assistant, DaVinci Resolve can automatically organize and color code your tracks, even

out your dialogue levels, and adjust the mixer faders to create a professional-quality mix of your music,

sound effects, and dialogue.

During this process, your dialogue will also be cleaned up, and if needed, Voice Isolation and

De‑Essing will be applied. Ducking will be applied to music tracks, any required automation will be

written, and the appropriate mastering and finalizing plugins will be added and adjusted to help

achieve the correct loudness level for your chosen delivery standard.


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

To use AI Audio Assistant:


Open a timeline containing unmixed audio. The initial fader levels really don‘t matter as Audio

Assistant will handle all fader adjustments during the mixing process.


To begin the automatic mixing process, choose Timeline > AI Tools > Audio Assistant from the

Timeline menu, select the Delivery Standard for your mix from the dropdown menu, and click the

Auto Mix button.

Audio Assistant dialog - Delivery Standard


The Audio Assistant dialog changes to display the progress of the mixing process with an option

to cancel it.

Audio Assistant dialog - Mix Progress


When the mixing process has concluded, you can play back the mix and, if needed, make further

adjustments or completely undo it.

NOTE: If a track is in the wrong category, right-click the corresponding track header and

choose the correct category from the Track Category section of the contextual menu, and

then rerun the Audio Assistant.


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT