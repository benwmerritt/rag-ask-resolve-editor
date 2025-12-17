---
title: "ADR (Automated Dialog Replacement)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 679
---

# ADR (Automated Dialog Replacement)

Clicking the ADR button on the Interface toolbar opens the Fairlight ADR panel, which offers a

thoroughly professional automated dialog replacement workflow. Dialog replacement, for those who

don’t know, is the process whereby audio professionals bring in actors to re-record unusable dialog

recordings from the comfort of their recording studios, line by line and with a great deal of patience.

The ADR panel on the Fairlight page

The Fairlight page aims to help you make this a structured and straightforward process. Simple, but

powerful, Cue list management lets you efficiently assemble a re-recording plan.

Industry-standard audio beeps and visual cues via your BMD video output device help the actors in

the booth nail their timings and their lines. Then, sophisticated take management with star ratings and

layered take organization in the Timeline help you manage the resulting recordings to pick and choose

the best parts of each take when you edit the results.

The ADR Interface

The ADR interface consists of three panels to the left of the Timeline: a List panel, a Record panel, and

a Setup panel. The controls of these panels are described in the order in which they’re used..

The Setup Panel

As its name implies, the Setup panel is where you configure your ADR session.

The Setup panel of the ADR interface


Fairlight | Chapter 174 ADR (Automated Dialog Replacement)

FAIRLIGHT

This panel presents the following controls:

�Pre Roll and Post Roll: Specifies how many seconds to play before and after each cue’s specified

In and Out points, giving actors a chance to listen to what comes before and after each cue in

order to prepare. If you enable the Beep options below, they’ll provide a countdown during the

specified pre-roll.

�Record Source: This dropdown menu lets you choose the audio input you want to record from,

creating a patch to the Record Track. However, this menu is disabled until you select a track in the

Record Track dropdown menu.

�Record Track: This menu lets you choose the track you want to record on. Making this selection

creates a patch from the Record Source to the Record Track and automatically toggles Record

Enable on.

�Guide Track: This dropdown lets you choose the track containing the production audio you want

to re-record. The talent will use the audio playback from this track as a guide when recording their

replacement performance.

�Record File Name: This text field lets you enter a filename for the recorded audio.

�Character Setup: This is where you can add the character names you’ll be re-recording, which

helps with cue creation and management. Click the Add button to enter a new character name.

To delete a character from the list, click the character name and then the Remove button.

�Beep to In Point: Enables a three-beep sequence, which the talent hears leading up to the

recording. For the beeps to be audible, the Beeps channel of the System Generator must be

patched to your audio outputs by going to Fairlight > Patch Input/Output.

�Beep at In Point: Enables one last beep at the In point. For the beep to be audible, the

Beeps channel of the System Generator must be patched to your audio outputs by going to

Fairlight > Patch Input/Output.

�Count In: Provides an onscreen counter that counts down to the start of the cue.

�Video Streamer: A visual cue for the talent to watch during pre-roll to ready them for recording.

A pair of vertical lines superimposed over the program being output to video move towards one

another across your video output screen during the pre-roll to the cue. This gives the talent a

visual indication of the time remaining until they should begin talking. When the beeps play, these

lines get taller. Both lines come together at the Time In frame, at which point a cross shows that

recording is beginning.

�On Screen Cue Text Style: Clicking this heading reveals a set of parameters for configuring the

look and placement of onscreen text cues.

�Smart Timeline: When turned on, this option automatically moves the playhead to each cue as it’s

selected in the Cue list, and zooms in to frame the duration of that cue in the Timeline.

�Mixing Control: Enables automated switching of audio playback, to independently control

what the talent and the audio engineer hear at various stages of the ADR recording process.

For example, with this enabled, the Guide track is not routed to the Control room while the

engineer is reviewing a take.


Fairlight | Chapter 174 ADR (Automated Dialog Replacement)

FAIRLIGHT

The List Panel

This is where you create a list of cues you need to re-record, either from within the Fairlight page or

imported from a .csv file.

The List panel of the ADR interface

This panel includes the following controls:

�Cue editing controls: Displays the data for the currently selected cue (or a cue that was just

created). In and Out timecode fields store the Timeline In and Out points that were set when the

cue was created but can be manually edited for fine tuning. A Character dropdown menu lets you

choose which character that line of dialog belongs to. A text entry field lets you enter the dialog

cue that’s to be re-recorded, so you and the talent can both refer to it.

�New Cue button: Clicking this button adds a new cue to the list using whatever In and Out points

have been set in the Timeline, and whatever character was last selected.

�Cue list: The list of all cues that have been entered or imported. The Cue list can be filtered using

the Filter dropdown menu at the top-right of the ADR panel (next to the option menu). You can

choose to show the cues for all characters, or for any selected combination of characters. You can

also choose to hide all cues that are marked as done to experience the joy of this list shrinking

more and more the closer you are to being finished.

Additionally, the ADR interface option menu has three commands pertaining to the List panel:

�Import Cue List: Lets you import a properly formatted .csv file to create cues that have been

prepared in a spreadsheet. Correct formatting for cue lists you want to import is no headers,

one line per cue, with four individual columns for In timecode, Out timecode, Character Name,

and Dialog.

�Export Cue List: Lets you export the contents of the Cue list to a .csv file, for exchange or

safe‑keeping.

�Clear Cue List: Deletes all cues in the Cue list. It’s recommended you export a copy of your Cue

list before eliminating it completely, in case you ever need to revisit a cue.


Fairlight | Chapter 174 ADR (Automated Dialog Replacement)

FAIRLIGHT

The Record Panel

This is where you actually run the ADR recording session you’ve set up, using the dialog cues you’ve

put into the Cue list.

The Record panel of the ADR Interface

This panel presents the following controls:

�Record and rehearse controls: Four transport controls and two buttons let you control recording

during ADR sessions. These controls are only clickable when you’ve selected a cue from the

Cue list to record.

Rehearse: Runs the section of the Timeline specified by a cue without actually recording anything,

giving the talent an opportunity to run through their dialog and practice their timing and delivery.

Beeps and on-screen streamers are not played during a rehearsal.

Play: Plays the currently selected take from the Take list (described below). If no take is selected,

the most recently recorded one on top is played.

Stop: Immediately stops rehearsal, playback, or recording.

Record: Initiates recording of the cue to the specified audio track, with cue beeps and video

streamer cues.

Keep Playing: At the end of a take you may wish to keep playing, so the talent can hear the next

section of the track. Pressing the Keep Playing button at any time, even while recording, results in

post roll being ignored and normal playback resuming after the cue’s Out time.

Keep Recording: At the end of a take you may wish to keep recording until you manually stop.

Pressing the Keep Recording button at any time, even while recording, results in the Out point of

the current cue being ignored and recording continuing until you stop it.

�Take list: The Take list shows every take you’ve recorded for the current cue, with take number,

name, and a five-star rating that you can set to keep track of which takes worked and which didn’t.

Earlier takes are at the bottom of this list, while recent takes are at the top (the same order in which

the corresponding layered audio clips appear in the Timeline track they’ve been recorded to).


Fairlight | Chapter 174 ADR (Automated Dialog Replacement)

FAIRLIGHT

�Cue list: The list of all cues that have been entered or imported. The Cue list can be filtered using

the Filter dropdown menu at the top-right of the ADR panel (next to the Option menu). You can

choose to show the cues for all characters, or for any selected combination of characters. You can

also choose to hide all cues that are marked as done to experience the joy of this list shrinking

more and more the closer you are to being finished.

�Cue list Done column: A sixth column appears in the Record panel only, labeled Done.

It contains check boxes for each cue that you can turn on to keep track of which cues you’ve

successfully finished.

Additionally, the ADR interface Option menu has one command pertaining to the Record panel:

�Record Early In: Enables recording during pre-roll, in the event you’re working with talent that likes

to start early.

Setting up to Do an ADR Session

Setting up to record ADR is straightforward but requires a few steps.

Creating tracks in preparation to record ADR:


In the Timeline, create a new audio track to which you’ll be doing ADR recording. Make sure it has

the correct channel configuration for your recording (mono is typical for dialog).


If you’re recording ADR to your main timeline, you may want to Solo both the Guide track and the

Record track, so you and the talent can focus on the audio being re-recorded without hearing all

the other tracks of the current mix.

Now you’re ready to configure the Setup panel.

Configuring the Setup panel:


Open the ADR interface, and then open the Setup panel.


Choose the Pre Roll and Post Roll you want to use, in seconds. A pre roll of at least 3 seconds is

recommended to give the talent time to get ready.


From the Record Source dropdown menu, choose the microphone you patched earlier.


From the Record Track dropdown menu, choose the Record track you created.


From the Guide Track dropdown menu, choose the track with the original production audio that

you’re replacing.


At the bottom of this panel, turn on which Preroll Cue options you and the talent want to use as

you record each cue. Options include:

a)	 Beep to In Point and Beep at In Point provide an audible count down to when

to start performing.

b)	 An animated Video Streamer gives a countdown to the start time, shows the duration of the

cue being recorded, and also displays the text of the dialog for that cue on screen for the

actor to refer to, so they can keep their eyes on the screen and not a script.

Next, if you’ve enabled Beep to In Point and Beep at In Point, you need to patch the Fairlight oscillator

to your output channels so the talent can hear the preview beeps.


Fairlight | Chapter 174 ADR (Automated Dialog Replacement)

FAIRLIGHT

Patching the Oscillator to play beeps over your audio output:


Choose Fairlight > Patch Input/Output to open the Patch Input/Output window.


Choose System Generator from the Source dropdown menu, and click to select Beeps.


Choose Audio Outputs from the Destination dropdown, and choose the left/right outputs you

want these preview beeps to play out of. You can drag a bounding box to select multiple outputs,

thereby connecting the mono Beeps input to stereo output for comfortable listening.


Click Patch to make the connection, then close the Patch Input/Output window.