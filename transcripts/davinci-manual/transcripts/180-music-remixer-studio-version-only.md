---
title: "Music Remixer (Studio Version Only)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 180
---

# Music Remixer (Studio Version Only)

This DaVinci Neural Engine AI-based plugin splits music into individual stems: Vocals, Drums, Bass,

Guitar, and “Other” (“everything else”), letting you creatively rebalance or remix the track.

You can use the level controls to adjust the volume of each stem and the Mute buttons to remove

or bring them back into your mix. For example, you may want to remove or lower a vocal because it

clashes with a featured piece of dialogue.

The Music Remixer plugin

Music Editor (Studio Version Only)

DaVinci Resolve 20 supports seamlessly extending or shortening music to the length of your edit.

The new AI powered Music Editor can be accessed in the Audio tab of the Inspector. You can enter a

desired duration and press the Adjust button in order to shorten or extend the clip to that duration.

NOTE:NMusic Editor is an “intelligent edit” that works effectively with beat-driven music (pop,

dance, etc.). It is not intended for free form, ambient or non-beat driven material.

Music Editor does not use time compression/expansion or alter the pitch of the music, but instead uses

editing techniques like a music editor might to fit the material to desired length to picture. It will look for

logical places to create transitions based on whether you’re extending length (by repeating sections),

or removing material, and attempt to use the ending or fade of the original composition if it times well.

If the ending is abrupt, it’s up to you to manually create a fade out.

The Music Editor in the Audio Inspector


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

To Use Music Editor to retime a music clip:


Select the clip on the timeline you wish to retime. This clip does need to be beat-driven music.


In the Audio Inspector under AI Music Editor enter a new Target Length for the music duration

you want.


Press the Adjust button.


Alternatively, you can check the Live Trim box to use the Trim tools to resize the clip and

dynamically retime the music on the timeline. You can turn the checkbox off to return to normal

editing (e.g., trimming) for that clip after the desired edit has been created.

Once the analysis is complete, four versions of potential edits you can use appear at the bottom,

each with a different approach to the edit, numbered 1-4. Any subsequent editing can be done almost

instantaneously. The edited pieces of music show indicators on the clip to mark the portions where

cuts and transitions occur.

The initial music is too long

The Music Editor has retimed the audio clip to match the length of the video. Note the jagged lines on the audio clip

indicating where the original was cut. In the waveform you can see the end of the music is retained in the retimed clip.

TIP: While timings can be quite close, sometimes they may not be exact. If you need to get

an exact timing after working with AI Music Editor, you might use the Elastic Wave tool on the

Fairlight page and choose the algorithm for general purpose (music).

The edited clip is actually a specialized Music Editor clip which allows you to further trim

your edit. If you want to access the underlying edit, you can also right-click on the clip and

decompose, exposing the edit points and any crossfades created. However, keep in mind

that once decomposed, you can’t trim the length of the clip as an entity as each editing

snippet is now a separate clip.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Dialogue Separator Track FX

(Studio Version Only)

Dialogue Separator uses DaVinci Neural Engine AI to give you individual control over the level of

dialogue, background sounds, and the reverberant field or ambient room sound (“ambience”).

The Dialogue Separator plugin

The Dialogue Separator is useful when, for example, a source file has a great roomy sound, but there’s

music or crowd noise in the background. In this instance, you can rebalance the audio to reduce the

background sounds or adjust the room sound to make the dialogue more intelligible.

Another use case would be when someone moves toward the camera in a roomy environment while

speaking. You could use automation to rebalance the audio so that the ambient room sound gradually

becomes “drier” as they get closer, without affecting the background.

Dialogue Separator is currently a mono-only plugin. If your source is stereo, you’ll need to split

it into dual-mono and process both mono tracks separately.

Ducker Track FX

This plugin lets you use the audible signal from a track or multiple tracks to lower the level of another.

Although it can be used in many creative ways, a common use of “ducking” is automatically lowering a

music or sound effects bed so that dialogue or a VO track can be heard more prominently in a mix.

This is achieved without compressing the incoming signals. When set up correctly in the Ducker

interface or via the Audio tab in the Inspector, your audio tracks can practically “mix themselves.”

In a simple use case, the Ducker uses level changes of a single incoming dialogue or VO track to

decrease the volume of the sound effects bed of a noisy freeway.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

In a more complex situation, such as a scene where three characters are conversing next to the same

noisy freeway, a single Ducker plugin can use the level changes of each dialogue track to attenuate

the traffic noise.

With only one input source (Dialogue 1), the Ducker would only be effective when the first character

speaks. However, this new feature lets you add the other two dialogue tracks (Dialogue 2 and

Dialogue 3) as input sources for attenuating the traffic noise.

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

•	 Select the Freeway Traffic track, ensure the Ducker is switched on, and open the

Inspector’s Audio tab.

•	 Click the plus sign to the right of the Source 1 dropdown containing Dialogue1 to create a

dropdown menu for Source 2, then choose Dialogue2 from the list.

•	 Click the plus sign to the right of the Source 2 dropdown to create a dropdown menu for

Source 3, then choose Dialogue3 from the list.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Adding Ducker input sources in the Inspector

Ducker Controls

�Duck Amount: This control determines level attenuation on the target track in dB with a default

value of 2.7 dB. Most of the time, a value between 2.0 dB and 5.0 dB works the best.

�Lookahead: Adjusts the amount of lookahead time in milliseconds, with a default value of 15ms.

Lookahead allows the Ducker to start attenuating the destination track before the source track

is audible.

�The larger the value, the more the Ducker will “pre-anticipate” the source track. If you want the

Ducker to start lowering the sound before a line of dialogue or VO begins, you can experiment

with higher values, but the default will usually produce good results.

�Rise Time: This determines how many milliseconds it takes for the Ducker to reach the amount of

reduction specified by the Duck Amount. The default value is 10 milliseconds, which should work

for most situations. Longer Rise Times may be useful with higher Duck Amount values and longer

gaps in the source track.

�Hold: This parameter determines how long the target signal will be attenuated. The

default is 150ms.

�Recovery Time: This value indicates how quickly the target signal will return to its previous level

after attenuation. The default time value is 750ms, but setting the correct Recovery time is crucial

to a natural-sounding ducking process, so you should try different values to find the best results.

Ducker Graph Display

This area shows a gray line representing the incoming signal against the action of the Ducker, shown

in yellow. Dips in the yellow line signify attenuation of the target track based on the Duck Amount in

combination with the other parameters.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT