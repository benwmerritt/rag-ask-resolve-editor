---
title: "Waveform Zero Crossing Indicator"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 689
---

# Waveform Zero Crossing Indicator

Waveforms have a zero crossing indicator line. Since a waveform is an image representation of sound

continually moving positive to negative, the zero crossing point is the level at which that fluctuation

occurs. When zooming into a waveform at the sample level, the waveform will display the zero crossing

line to enable precise editing.

The zero crossing is a useful feature when editing audio, since clean edits are made at

the zero crossing to avoid inducing clicks or pops. A crossfade between two audio clips

automatically brings both sides of the fade to the zero crossing.

The center line in the waveform indicator is the zero crossing.

Voice Convert (Studio Version Only)

DaVinci Resolve has an incredibly sophisticated AI-driven voice conversion tool, that allows you to

essentially swap one speaking voice for another. The use cases for this tool are wide reaching and

even somewhat controversial, however this Voice Convert toolset can be an invaluable resource in

a post production. It allows you to take a generated voice model that has been captured by DaVinci

Resolve and “drive” that voice model using another voice recording as its foundation.

In simple cases, you can replace your own voiceover tracks with a voice that has more depth and

gravitas to it, or even switch the gender of your own voice if you feel it’s more appropriate for the

subject matter. Perhaps you recorded audio in a noisy environment and wanted to make a pristine

version instead by using your own voice as a model, to replace your original noisy tracks. In more

complicated scenarios you can train your own voice convert model on your actor’s voice patterns

and use that to change and replace their previous voiceover, without having to get them back into

the recording booth. Finally, it is even possible to change the voice of an actor completely to another

voice, all while staying perfectly in sync with the picture. The inflection, pitch variations, and emotion

of the original all remain; it just sounds like someone else.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Needless to say, using this powerful tool requires a certain level of responsibility on the part of the

user. Privacy, copyright, and union laws and rules are all in flux at the moment around AI-generated

content, and it’s necessary to carefully navigate the ethics involved in its professional use.

The Voice Convert tool

NOTE: Using Voice Convert is very processor intensive and requires your system to have a

minimum of 8GB of video RAM before it will activate to avoid crashes and system instability.

Even with a strong system, creating a Voice Model will require prolonged intensive CPU and

GPU power, so multi-tasking while it’s working may be challenging.

Using Voice Convert

Like most of DaVinci Resolve’s AI tools, using Voice Convert is very simple, with all of the complex

processing involved handled by the voice model.

To use Voice Convert to change one voice to another:


Place the clip or clips you want to change the voice of in the timeline, and select them.


Right-click on the clip and select Voice Convert from the context menu, or select Clip > AI Tools >

Voice Convert in the main menu.


Select the track that you want the new audio to appear in (including overwriting the original).


Select the file name you want the new audio to be named.


Select the Voice Model you want to use for the new audio (you can make your own custom voice

models as explained below), and it’s parameters.


Click Render to start the Voice Convert process.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Voice Convert analyzing a clip

At this point the Voice Convert dialog will appear showing you the progress of the conversion.

Depending on the length and number of clips selected, this can take some time. When the process is

done, the new audio will appear in the timeline in the exact same place as the original audio (or on the

same place in another track if that option was selected). The new audio clips will also appear in the

Media Pool.

Simply play back the timeline to audition the new voice. You can change the audio back to the original

by right-clicking on a clip and selecting Revert to Original Voice from the context menu.

TIP: While you can drive voices with different accents, Voice Convert generally can’t recreate

another accent. For example, if you have a voice model that is a speaker with a British accent

and drive that voice with an American accent, you get more of an American version of the

British accented speaker. But if you speak with a British accent when driving the British voice

model, it will work well.

Voice Convert Settings

Each voice conversion requires selecting set up parameters to drive the model.

�Track: Select which track you want the new audio to be placed on. The default is Render in Place,

which will overwrite the original audio.

�File Name: Set the file name for the new audio clip. You can enter a specific name, or use the

metadata variables to create a template for file naming. By default the name is ClipName-(Voice

Model Name).

�Voice Model: Select which voice model you wish to use for the new audio. There are some

built-in options that come with DaVinci Resolve, and any custom options you create will also be

available here.

�Tight Matching to Source: Check this box to tightly follow the pitch, intonation, and volume

variance of the source voice. Uncheck this box to have a looser interpretation using the Pitch

Variance tool.

�Pitch Variance: When the Tight Matching to Source box is unchecked, this tool becomes

active. Lower values create a more monotone interpretation, while higher values have more

variance in pitch.

�Pitch Change: Use this slider to create a deeper (negative values) or higher (positive values) voice

based on the model. The values are in semitones and can be adjusted in 100 cents (.1 semitone)

increments.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Creating Your Own Voice Models

It is possible to create your own voice models for use with Voice Convert. These can be of your own

voice or even someone else’s that you have the rights to. This section goes over some best practices

to get a clean and usable voice model.

Preparing the Voice Model Assets

You will get the best results using ten minutes or so of clean, high-quality recordings of the voice to

be modeled. The audio should be free of excessive ambiance and noise, with little to no dynamics

processing. You will want consistent material that sounds natural. It can be useful to have a variety of

emotions expressed as well, if you want to hear those results for the driven voice. Treat it like a voice

over audition; show your range.

These voice assets do not necessarily need to be in one long clip, though if there are a lot of separate

files, it can be helpful to consolidate them all in a single bin for organization. The multiple clips should

be of consistent quality, without audio variations in the recorded sources.

Creating the Voice Model

To generate your own voice model, select one or more clips for analysis in the Media Pool, right-click

and choose AI Tools > DaVinci AI Tools Voice Training from the context menu. If this is the first time

you’ve run this tool, DaVinci Resolve will open up the Resolve Extras Download Manager to install the

required support files.

Voice Model generation

Initially, a warning splash screen appears to ensure you assume full responsibility for how you will

use this tool. Once you hit accept, The DaVinci AI Voice Training dialog appears, and there are two

options to set.

�Voice Model Name: Enter a descriptive name for your new model.

�Quality: Choose Faster or Better mode for analysis. Better takes about 3x the time as faster,

and 10 minutes or so of material can take a few hours to complete, depending on your

computer’s power.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Initially creating a voice model launches a foreground process, then once the initial analysis is

complete, it will switch to a background process, allowing you to continue to use DaVinci Resolve for

other purposes or other apps while it finishes.

Voice Model Progress

You can see the progress of the model in the Voice Model Generation Progress indicator in

the bottom right corner, or by selecting Workspace > Voice Model Progress.

Voice Model Generation Progress indicator will slowly fill blue as

the voice model finished. Hover over the top to get an ETA and

progress finished tooltip.

You can also alternatively choose to pause or discard the in-progress model instead. Quitting

DaVinci Resolve will also pause the background process, and it will automatically start up

again the next time DaVinci Resolve is launched.

Once the model is complete, the new voice preset will appear for use in the Voice

Convert dialog.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT