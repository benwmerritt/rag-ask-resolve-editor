---
title: "List View Clip Usage Column"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 164
---

# List View Clip Usage Column

A Usage column can be optionally shown in the Media Pool while in List view. By default, this column is

empty, but if you right-click in the Media Pool and choose the Update Usage command, the project is

analyzed, and every use of that clip in every timeline of the entire project is logged in this column.

A Usage column shows how many times a clip is

used in every timeline, after analysis

NOTE: The usage column increments for each clip item that appears in the Timeline.

This means that if a clip consists of one video item and one audio item linked together, the

usage column will show the number 2.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

Chapter 42

Multicam Editing

If you’re working with media that was shot simultaneously using multiple cameras,

then you can use the Multicam Editing tools in DaVinci Resolve to create multicam

clips that can be edited using a visual switcher. Additional controls let you change

the angles of multicam clips that have already been edited into the Timeline.

Contents

Introduction to Multicam Editing�������������������������������������������������������������������������������������������������������������������������������������������������� 890

Creating and Modifying Multicam Clips����������������������������������������������������������������������������������������������������������������������������������� 890

Using Native Audio Channels from Source when Editing Multicam Angles������������������������������������������������������������ 892

Selecting a Single Reference Audio Track for Multicam Clips��������������������������������������������������������������������������������������� 892

Changing the Start Timecode for Multicam Clips����������������������������������������������������������������������������������������������������������������� 893

Converting Compound Clips or Timelines to Multicam Clips����������������������������������������������������������������������������������������� 893

Logging and Editing Multicam Clips������������������������������������������������������������������������������������������������������������������������������������������� 893

Setting up a Timeline for Multicam Editing���������������������������������������������������������������������������������������������������������������������������� 894

Opening and Altering Multicam Clips��������������������������������������������������������������������������������������������������������������������������������������� 895

Performing a Multicam Edit������������������������������������������������������������������������������������������������������������������������������������������������������������� 896

Multicam Controls in the Source Viewer��������������������������������������������������������������������������������������������������������������������������������� 897

Multicam Keyboard Controls����������������������������������������������������������������������������������������������������������������������������������������������������������� 898

Editing Multicam Clips in the Timeline�������������������������������������������������������������������������������������������������������������������������������������� 899

Multicam SmartSwitch (Studio Version Only)������������������������������������������������������������������������������������������������������������������������ 900

Multicam SmartSwitch Settings����������������������������������������������������������������������������������������������������������������������������������������������������� 902

Grading Multicam Clips��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 902


Edit | Chapter 42 Multicam Editing

EDIT

Introduction to Multicam Editing

If you’re working on a program where a performance, interview, or event was recorded using multiple

simultaneous cameras, DaVinci Resolve has multi-camera editing tools; multicam editing for short.

Editing using these tools is a three part process:

�First, you have to create multicam clips from the individual camera angles (called “ISOs,”

or isolated cameras).

�Second, you need to put the multicam clips you’ve created into a timeline.

�Third, you turn on the Multicam Viewer, and then you’re ready to start cutting and switching among

angles, as if you were a live multi-camera director.

This section describes all of these steps, and the various options available for each of them.

Creating and Modifying Multicam Clips

Before you do anything else, you need to create one or more multicam clips.

To create a multicam clip:


Import all the ISO (isolated camera) clips that correspond to the multi-camera performance or

event that you’ll be editing into the Media Pool.


Select all the clips that you need to sync together, right-click the selection, and choose “Create

Multicam Clip Using Selected Clips.”


When the New Multicam Clip Properties dialog opens, choose from the following options:

New Multicam Clip Properties dialog

Start Timecode: Presents the start timecode of the new multicam clip you’re about to create,

which is determined by either the timecode value of the sync point if Angle Sync is defined by

timecode, or by the sync point timecode value of the clip with the earliest timecode if Angle Sync

is defined by waveform.

Multicam Clip Name: Use to choose a more descriptive name than “Multicam 1” for the multicam

clip you’re about to create.


Edit | Chapter 42 Multicam Editing

EDIT

Frame Rate: Automatically lists the frame rate associated with the clips you selected. A Drop

Frame checkbox option is there if your clips are using drop frame timecode.

Angle Sync: The method used to synchronize all of the different angles. If you’re manually

syncing all of the angles, you can use In or Out points that you set within each clip. If matching

timecode was jam synced to each camera recording an angle, you can choose Timecode for a

fast sync that’s as accurate as the timecode is. If each camera had a microphone with which to

simultaneously record the location audio, you can choose Sound to use the shape of each audio

waveform to align all of the angles. If you’ve manually added your own sync point markers to your

clips, you can choose Marker.

Channel: If Sound is selected as your Angle Sync type, you can choose the audio channel from

the clip to use as a sync source.

Angle Name: The method used to name each angle within the multicam clip being created. The

angles can have Sequential numbering, use Angle or Camera metadata, or use the Clip or File name.

Split Multicam at gaps: If Sound is selected as your Angle Sync type, you can choose to split the

Multicam files anywhere there is a gap in the audio.

Detect clips from same camera: Turning on this checkbox results in multiple clips that are

identified as being from the same camera being put into the same angle track of the resulting

multicam clip being created. It also enables the “Detect using” drop-down menu.

Detect Using: The metadata used to determine which clips come from the same camera. You can

choose from Camera #, Angle, Reel Number, Reel Name, and Roll/Card #, which are user-editable

in the Metadata Editor of the Media page, or you can choose Reel Name which is automatically or

manually derived using either the Conform Options of the General Options panel of the Project

Settings, or the Name panel of the Clip Attributes window.

For more information on the Conform Options, see Chapter 4, “System and User Preferences.”

Move Source Clips to “Original Clips” Bin: A checkbox that lets you move all of the original ISO

clips into an Original Clips bin to get them out of the way after the multicam clip has been created.

Use source audio channels: When checked, this gives you access to the individual tracks and

channels in the source clip’s audio (see below for further description).


When you’re done choosing options, click Create. Depending on the Angle Sync method you

chose, a waveform analysis might generate a progress bar, and then the new multicam clip is

created in whichever bin is currently selected in the Media Pool. Multicam clips appear with a

multicam badge in the lower left-hand corner of the clip thumbnail.

A multicam clip showing

its badge in the Media Pool


Edit | Chapter 42 Multicam Editing

EDIT

Using Native Audio Channels from

Source when Editing Multicam Angles

There is an option in the multicam creation dialog to Use source audio channels. This option is

enabled by default. With this option enabled, the multicam clip is created in a mode where you have

access to the individual tracks and channels in the source angle.

If this arrangement does not suit you, you can uncheck this option and all the audio tracks and

channels for an angle are placed in a single adaptive track, wide enough to cover all the audio

channels in the source. The multicam clip audio is then placed on a timeline on an adaptive track.

Using native audio channels lets you access

individual tracks in the source angle.

Once the multicam clip is created with this option enabled, you can preview the audio tracks in the

Audio Configuration section in the inspector File tab. With the option disabled, the multicam clip audio

will be placed in an adaptive track. With the option enabled, the audio will be placed in the track

format of the source.

Multicam audio clips also have the ability to select alternative mono audio channels from the timeline

clip context menu (including Command right-click for faster access) and from the timeline clip audio

configuration section in the Inspector.

Selecting a Single Reference Audio Track for Multicam Clips

Multicam clips in DaVinci Resolve can use reference audio files (such as those recorded by an external

sound mixer) as the audio track for all angles, if you add an audio file to your multicam clip. During the

creation of the multicam clip, select Reference Audio/Angle 1 in the Multicam Audio selector.

This selection automatically identifies the first audio-only angle and sets it as the reference audio for

all the other angles. For multicam setups without an audio-only angle, the first angle is automatically

used as the reference audio for the multicam clip. When performing multicam cuts, you can access

the underlying channels in the reference audio angle by Command-right-clicking on the clip similar to

source audio multicam clips.


Edit | Chapter 42 Multicam Editing

EDIT

Setting up the Reference Audio track in a multicam clip