---
title: "Creating and Importing ADR Cue Lists"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 680
---

# Creating and Importing ADR Cue Lists

You must have a list of cues to be able to use the ADR interface properly. There are two ways you can

create a Cue list to record with, make one from scratch on the Fairlight page, or import one. The ADR

panel accommodates both workflows.

AI Create ADR Cues (Studio Version Only)

AI Create ADR Cues is part of DaVinci Resolve’s Intellicut feature set, which also includes two other

features: Remove Silence and AI Checkerboard to New Tracks.

For more information about Remove Silence and AI Checkerboard to New Tracks,

see Chapter 175, “Editing Basics in the Fairlight Page.”

It’s an old joke that ADR isn’t really automatic. However, this feature analyzes and transcribes a

selection of timeline clips on a track, then automatically generates individual ADR cues, with two

output options explained below.

Timeline clip contextual menu for creating ADR cues

NOTE: The dialogue must be spoken in one of the supported languages listed in the Project

Settings under Subtitles and Transcriptions > Language.

For more information about the Subtitles and Transcription settings, see Chapter 6,

“Project Settings.”

ADR cues will be generated in the language selected in the Project Settings under Subtitles

and Transcriptions. The default selection is “Auto,” which applies the language setting of your

computer’s operating system to all projects. However if, for example, you manually select

English as the project language and then create ADR cues for dialog spoken in French, the

resulting cues will be written in English.


Fairlight | Chapter 174 ADR (Automated Dialog Replacement)

FAIRLIGHT

Create ADR Cues

Right-clicking a selection of timeline clips on a track and choosing AI Tools > Create ADR Cues from

the contextual menu opens the Transcribing Audio dialog, showing the progress of the analysis and

transcription. Once the dialog closes, the transcribed cues are added to the List page in the ADR

panel, along with their Cue ID, Time In/Out, and Durations.

New ADR cues

Create ADR Cues with Speakers

Right-clicking the timeline clip selection and selecting AI Tools > Create ADR Cues with Speakers from

the contextual menu adds the transcribed cues to the List page, as described above, along with each

Speaker’s name in the Character column.

New ADR cues with speaker names added to the Character column

Manually Creating an ADR Cue List

If you’ve been doing all of your dialog editing inside of DaVinci Resolve, you can go ahead and create

a list by marking the sections of the Timeline you need to re-record and creating cues from those

timings. To create cues properly, you should start by adding the names of each character you’ll be

creating a cue for in the Setup panel. These names make it easier to enter cues and will help you to

filter and sort the list as necessary later on.

To add character names before entering cues:


Open the Setup panel of the ADR interface.


Click Add New.


When a selected entry appears in the Character Setup list, type a name.


Press Return when you’re done.

To edit the Character Setup list, do one of the following:

�If you mis-spell a name, you can double-click any name in this list to edit it.

�To delete a name, you can select it and click Remove to eliminate it.


Fairlight | Chapter 174 ADR (Automated Dialog Replacement)

FAIRLIGHT

Once you’ve created a complete set of character names, you can begin creating your Cue list.

To manually add cues to the Cue list:


Open the List panel of the ADR interface. This is where all the controls for creating and

editing cues are.


In the Timeline, set In and Out points to mark the section of dialog you want to turn into a cue.

Those timecode values appear in the Cue Editing section of the List panel.


Click New Cue to add a blank cue to the Cue list.


In the Cue Editing section, choose the character who’s speaking that cue from the Character

dropdown (only names that have been entered in the Setup tab appear in this list).


If necessary, select the text field below, and type the dialog that needs to be re-recorded.


Repeat steps 2 through 5 until you’re finished creating all the cues you intend to re-record. If you

need to edit any cue, simply click to select that cue, and edit it in the Cue Editing section above.

Importing Cues

If you or an assistant has already created a Cue list using a spreadsheet with separate columns for

character names, dialog, and In/Out timecode values, then you can also create a Cue list by importing

this data from an exported .csv file.

To import a .csv file to the Cue list:


Choose Import Cue List from the ADR option menu, then use the dialog to choose the .csv file

containing the Cue list you were given, and click Open.


An ADR Setup dialog appears, showing the data from the .csv file previewed as a series of

columns. This lets you see if each column of incoming data is being assigned correctly. If it’s not,

you can reassign each column of the incoming data to the correct column of the ADR panel.

Correct formatting for Cue lists you want to import is to have no header text, and to enter

information using one row per cue, with four individual columns for In timecode, Out timecode,

Character Name, and Dialog. If any of these columns are transposed, you can correct this by

choosing the correct data type for each column from the dropdown menus at top.

Dialog for rearranging columns of cue data, if necessary


Click Import CSV. The cues should appear in the Cue list.


Fairlight | Chapter 174 ADR (Automated Dialog Replacement)

FAIRLIGHT

To export a .csv file from the Cue list:

�Choose Export Cue List from the ADR option menu, choose a location to save the file,

and click Save.

Recording ADR to the Timeline

Once you’ve configured your workstation for recording, and you’ve set up a Cue list to work with, it’s

time to start recording each cue.

To record a cue from the Cue list:


Open the Record panel of the ADR interface.


If you want to record a particular character’s cues, you can select each unnecessary character in

the ADR Option menu to uncheck that character, hiding their dialog in the Cue list.


With the list showing the character cues you need, select the cue you want to start recording. That

cue contains the timecode necessary to determine which part of the Timeline to record to, and the

playhead automatically moves to that part of the Timeline.


Click the Rehearse button a few times to run through the cue with the talent. When you click

Rehearse, both audio and video corresponding to that cue will play, including pre roll and post roll,

along with all beep and onscreen cues.


When the talent is ready to try a take, click the Record button, and let the Fairlight page do

the work of playing through pre roll with beep notifications and visual streamer cues, initiating

recording, and then stopping recording automatically once the cue is done. To record another

take, simply click the Record button again.

Every time you complete a recording, a take appears in the Take list. Making multiple recordings

results in multiple takes in the list. In the Timeline, all new takes appear as layered audio, so you

can record as many takes as you like into the same area of the Timeline. Once you’ve finished

recording takes, you’ll have a neatly organized stack of alternate takes to draw upon as you edit

together the best parts of each recording.


If you or the talent want to hear a particular take again, select it in the Take list and click Play.

You can use the 5-star ratings control to keep track of how you liked each take.


When you’re finished recording a cue, click the Done checkbox for that cue, and select the next

cue you want to record. When you’re finished re-recording dialog, simply close the ADR interface.


Fairlight | Chapter 174 ADR (Automated Dialog Replacement)

FAIRLIGHT

Chapter 175

Editing Basics in

the Fairlight Page

You can use the Fairlight page to refine the editing of audio that was initially

assembled in the Edit page, or you can use the Fairlight page to both record and

edit audio programs from scratch.

Because audio clips have properties that video clips do not, audio editing encompasses additional

procedures that are not available in the Edit page. This chapter takes you through the fundamental

steps of editing audio the Fairlight way.

Contents

Compatible Audio Formats����������������������������������������������������������������������������������������������������������������������������������������������������������� 3774

Editing Audio Clips Into the Timeline�������������������������������������������������������������������������������������������������������������������������������������� 3774

Overwriting Vs. Layering Clips That Overlap������������������������������������������������������������������������������������������������������������������������ 3775

Choosing Parts of Clips to Edit in the Media Pool�������������������������������������������������������������������������������������������������������������� 3775

Dragging Audio Clips Into the Timeline����������������������������������������������������������������������������������������������������������������������������������� 3776

Moving Audio Clips to Embedded Timecode Position����������������������������������������������������������������������������������������������������� 3778

Support for Mixed Audio Track Formats from Source Clips������������������������������������������������������������������������������������������ 3779

Making Audio Clip Selections in the Timeline������������������������������������������������������������������������������������������������������������������� 3780

Fairlight Edit Mode Remains Between Application Restarts���������������������������������������������������������������������������������������� 3780

Selecting Tracks��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3780

Using Pointer Mode�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3782

Using Range Mode����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3783

Using Focus Mode���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3788

Commands For Editing and Extending the Selection������������������������������������������������������������������������������������������������������ 3790

Locking Audio Tracks������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3791

Splitting Clips���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3791

Remove Silence (Studio Version Only)��������������������������������������������������������������������������������������������������������������������������������������� 3791

AI Checkerboard to New Tracks (Studio Version Only)��������������������������������������������������������������������������������������������������� 3792

Manually Split Clips in Pointer or Range Mode�������������������������������������������������������������������������������������������������������������������� 3793

Linked Clips in the Fairlight Page���������������������������������������������������������������������������������������������������������������������������������������������� 3794


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Trimming Clips Without Rippling the Timeline������������������������������������������������������������������������������������������������������������������ 3794

Multi-Point Editing Overview�������������������������������������������������������������������������������������������������������������������������������������������������������� 3794

Resizing the In and Out Points of a Clip���������������������������������������������������������������������������������������������������������������������������������� 3795

Trim Start and Trim End������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3795

Trim to Selection��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3795

Moving and Overwriting Clips���������������������������������������������������������������������������������������������������������������������������������������������������� 3796

Snap to Playhead�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3797

Subframe Nudging����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3797

Slipping���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3797

Duplicating Clips�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3798

Disabling and Re-Enabling Clips in the Timeline������������������������������������������������������������������������������������������������������������� 3799

Deleting Audio Clips and Regions�������������������������������������������������������������������������������������������������������������������������������������������� 3799

Cut, Copy, and Paste����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3799

Conventional Cut, Copy, and Paste������������������������������������������������������������������������������������������������������������������������������������������ 3799

Using the Cut/Copy Head and Tail Commands������������������������������������������������������������������������������������������������������������������ 3802

Paste and Remove Attributes����������������������������������������������������������������������������������������������������������������������������������������������������� 3803

Clip Attributes Naming�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3803

Copying and Pasting Clip Attributes���������������������������������������������������������������������������������������������������������������������������������������� 3803

Copying and Pasting Track Attributes������������������������������������������������������������������������������������������������������������������������������������� 3803

Removing Attributes������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3804

EQ, Level, and AI Dialogue Matching������������������������������������������������������������������������������������������������������������������������������������� 3804

EQ Matcher������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3804

Level Matcher�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3805

AI Dialogue Matcher������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3806

Audio Clip Layering�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3806

Audio Compound Clips������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3808

Audio Crossfades������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3808

Fades and Crossfades�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3809

Using Fades������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3809

Batch Fade and Crossfade Editor in the Fairlight Page��������������������������������������������������������������������������������������������������� 3810

Fade In and Out to Playhead��������������������������������������������������������������������������������������������������������������������������������������������������������� 3812

Creating Crossfades With Overlapping Fades��������������������������������������������������������������������������������������������������������������������� 3813

Using Crossfades From the Edit Page�������������������������������������������������������������������������������������������������������������������������������������� 3814

Finding Clips in the Media Pool�������������������������������������������������������������������������������������������������������������������������������������������������� 3814

Changing Clip Color in the Timeline���������������������������������������������������������������������������������������������������������������������������������������� 3814

Editing Audio Clips in External Editors����������������������������������������������������������������������������������������������������������������������������������� 3815

Exporting Audio Clips to External Files���������������������������������������������������������������������������������������������������������������������������������� 3816

Sample Editing������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3817

Waveform Zero Crossing Indicator��������������������������������������������������������������������������������������������������������������������������������������������� 3818

Voice Convert (Studio Version Only)����������������������������������������������������������������������������������������������������������������������������������������� 3818

Using Voice Convert�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3819

Voice Convert Settings������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3820

Creating Your Own Voice Models����������������������������������������������������������������������������������������������������������������������������������������������� 3821


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT