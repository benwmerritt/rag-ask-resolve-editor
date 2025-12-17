---
title: "Re-editing Media Directly to the Timeline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 215
---

# Re-editing Media Directly to the Timeline

If, for whatever reason, none of the above methods of relinking or reconforming have worked,

sometimes the only thing left to do is to replace the problem clip in your timeline with a different clip.

For example, you may need to replace an old version of an effects shot with a newer one, or or you

need to replace an offline version of a stock footage shot with a higher quality one, and the problem

is that you’ve got a mismatched filename and/or timecode, no reel name, and the files are completely

different formats, frame sizes, and durations.

In this case, it’s a good thing that DaVinci Resolve has such good editing tools.

For more information on editing, see Chapter 34 through Chapter 47. When fixing conform

problems via manual editing, the replace edit is your special friend. For example, you could

use a replace edit to match a new incoming clip’s timing to the old one. Or you could use a

three-point edit, a place on top edit, or even a simple drag and drop edit to put the new clip

into the Timeline to take the place of the old one.

For specific information on the different edit types in DaVinci Resolve, see Chapter 36,

“Editing Basics.”


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

How Grades Are Linked

to Multiple Timelines

If you’ve set your project up to use Remote versions, then any clips that refer to the same file in

the Media Pool are linked and share the same Remote versions of grades that are applied to them.

For example, two clips that are close-ups from the same take refer to the same media file, so they’re

both automatically linked to one another and share the same remote grades.

Clips using Remote versions also exhibit this behavior when they appear in multiple timelines.

Clips using Remote versions that are located in different timelines, but that refer to the same file in

the Media Pool, are linked and share the same remote versions of grades. This is why you can grade

one timeline, and then import a re-edited version via EDL, AAF, or XML, and have the new timeline

automatically inherit all grades from the previous timeline.

However, you can override this behavior to have one timeline that’s independently graded from the

others. Simply select that timeline, open the Color page, right-click any clip in the Thumbnail timeline,

and choose Copy Remote Grades to Local from the contextual menu. All grades are copied to Local

versions, and from that point on all changes you make to grades in that timeline have no effect on the

other timelines in your project.

For more information about Local and Remote versions, see Chapter 142, “Grade

Management.”


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

Chapter 57

Creating Digital

Dailies for Round

Trip Workflows

DaVinci Resolve can be used to create media for editors to use in other

applications in situations where those applications are unable to import a given

project format but DaVinci Resolve can.

In the process, you can use DaVinci Resolve’s many organizational, effects, and grading capabilities to

create media that’s a pleasure to edit with, normalizing log-encoded media, syncing dual-source audio

in a variety of ways, and doing some fast (or not-so-fast) grading to make sure that the media being

edited looks its best.

Furthermore, once you’ve created a project to accomplish these tasks, you’ve also given yourself a

jump-start on reconforming the project should your workflow be to move the edited project back into

DaVinci Resolve for editing and finishing. This chapter covers a workflow for importing, preparing, and

outputting media for these situations.

Contents

Step 1 – Ingest Media and Add/Edit Metadata���������������������������������������������������������������������������������������������������������������������� 1171

Step 2 – Sync Audio to the Dailies���������������������������������������������������������������������������������������������������������������������������������������������� 1172

Step 3 – Do Whatever Grading is Necessary������������������������������������������������������������������������������������������������������������������������ 1172

Step 4 – Export Media Suitable for Editing���������������������������������������������������������������������������������������������������������������������������� 1175

Step 5 – Reconform Media to an EDL, AAF, OTIO, or XML Project File������������������������������������������������������������������ 1176

Step 6 – Output Final Media for Finishing������������������������������������������������������������������������������������������������������������������������������ 1176


Import and Conform Projects | Chapter 57 Creating Digital Dailies for Round Trip Workflows

EDIT

Step 1 – Ingest Media and Add/Edit Metadata

It’s not necessary to have a project file exported from an NLE to start working in DaVinci Resolve.

Using the Media Storage browser on the Media page, you can access any volume that’s currently

available to the system, and import any compatible media format into the Media Pool.

Media Storage browser with scrubbable clip thumbnails

The Media Pool is DaVinci Resolve’s internal project library of available media for the currently open

project. If you like, clips in the Media Pool can be organized into multiple bins. Once media has been

added to the Media Pool, you can access a variety of descriptive metadata using the Metadata Editor,

adding descriptions, notes, scene and take information, flags, day and date information, program and

episode information, and so on. This data can populate metadata tags when exporting ALE lists to

move the metadata to a compatible NLE.

For more information on ingesting media in the Media page, see Chapter 18, “Adding and

Organizing Media with the Media Pool.”

The Media Pool


Import and Conform Projects | Chapter 57 Creating Digital Dailies for Round Trip Workflows

EDIT

Step 2 – Sync Audio to the Dailies

If your video format has embedded audio, DaVinci Resolve can simply pass that audio through when

outputting media from the Deliver page. However, if the program you’re working on employs dual-

system audio recording, there are a variety of methods available for syncing it in the Media page. You

can also import timecoded Broadcast WAVE files into the same bin as the accompanying video clips

(you can place them into a sub-bin if you like), in preparation for syncing the dailies in DaVinci Resolve.

Once you’ve imported the video and audio media you want to sync into the Media Pool of the Media

page, you can right-click the enclosing folder and choose “Auto-Sync Audio Based on Timecode”

which automatically syncs every timecode-matched pair of audio and video media clips within the

same folder, all at once. Alternately, you can choose “Auto-Sync Audio Based on Timecode and

Append Tracks” to add the synced audio tracks to any audio tracks already present in the video clips.

TIP: For the best results, consider using different folders for each day’s audio and video clips.

If you don’t have synced timecode, but your video clips have separately recorded audio (usually via

an on-camera microphone) that matches the dual-system audio recordings, you can use waveform

syncing to quickly sync each video clip with its matching audio clip. Import your separately recorded

audio files into the same bin as the accompanying video clips (you can place them into a sub-bin if you

like), in preparation for syncing. Once imported, you can right-click the enclosing folder and choose

“Auto-Sync Audio Based on Waveform” which automatically syncs every timecode-matched pair of

audio and video media clips within the same folder, all at once. Alternately, you can choose “Auto-Sync

Audio Based on Waveform and Append Tracks” to add the synced audio tracks to any audio tracks

already present in the video clips.

TIP: With waveform syncing, for the best and fastest results, consider using different folders

for each day’s audio and video clips, or even different folders for each scene, to reduce the

number of waveforms that need to be compared at one time.

Finally, if all you have in the way of sync reference is a humble clapboard, you can manually sync video

and audio clips by selecting a video clip to open into the Media page viewer, and then clicking the

Waveform button in the Audio panel and clicking the corresponding audio clip to show its waveform

in the audio panel. In this way, you can drag the Viewer and Audio panel’s playheads to the video and

audio sync points, and click the Audio panel’s link button to lock the A/V sync of that clip.

For more information on syncing audio and video in the Edit page, see Chapter 22, “Modifying

Clips and Clip Attributes.”

Step 3 – Do Whatever Grading is Necessary

Many productions that decide not to record camera raw media instead elect to record a log-encoded

or “flat” image to ProRes or DNxHD media files in order to preserve the most image data for grading

without clipping highlights or shadows. This can be accomplished using in-camera settings that

record log-encoded QuickTime or MXF media, or via external video recorders such as the Blackmagic

Video Assist. Depending on the camera you’re shooting with, the recorded media will use one of a

variety of log-encoded gamma curves such as Log-C, S-Log, S-Log2, S-Log3, BMD Film, CanonLog,

Panasonic VLog, or REDlog Film, among others.


Import and Conform Projects | Chapter 57 Creating Digital Dailies for Round Trip Workflows

EDIT

In other workflows, raw video formats are recorded and later debayered as log-encoded clips in order

to preserve the maximum amount of debayered data for grading, or in preparation for transcoding.

If you’re outputting high-quality media files meant to be used themselves for later finishing, then you

may want to simply pass the source image data through unaltered. However, if you’re creating offline

media for editors, directors, and producers to watch for the next three months, you can grade this data

in a variety of ways to provide more pleasing output that’s been “normalized” in order to look closer to

what was monitored on-set during the shoot.

There are many ways of normalizing log-encoded media in DaVinci Resolve. If you’re working with one

or more raw formats, you can choose to debayer all clips straight to Rec. 709 in the Camera Raw panel

of the Project Settings. However, if you’re working with log-encoded ProRes or DNxHD media, you

need to normalize these clips using other methods.

An easy and powerful way to do so is to use DaVinci Resolve Color Management. To do so, set the

“Color science” setting within the Color Management panel of the Project Settings to “DaVinci YRGB

Color Managed.” Then, right-click each clip or group of clips in the Media Pool, and choose the

appropriate setting for each type of media from the Input Color Space submenu (you can define the

Input Color Space of multiple selected clips at once).

For more information on using DaVinci color management, see Chapter 9, “Data Levels, Color

Management, and ACES.”

Enabling DaVinci Resolve color management

If you don’t want to use DaVinci color management, you can also use one or more LUTs (Lookup

Tables) to  normalize log-encoded media. You can apply a LUT to the entire project to normalize the

particular log characteristics of the media you’re processing. Project-wide LUTs can be applied in the

Color Management panel of the Project Settings.

For more information, see Chapter 4, “System and User Preferences.”


Import and Conform Projects | Chapter 57 Creating Digital Dailies for Round Trip Workflows

EDIT

Project-wide LUT table settings on the Lookup Tables panel of the Project Settings

In the case of LUT-managed shooting workflows where a variety of LUTs have been custom-

designed to monitor different scenes, you can manually apply individual LUTs to one or more

selected clips from each scene using the Media Pool’s contextual menu.

You can also edit each scene’s clips into timelines, and apply separate LUTs to each clip in

the Clip mode of the Node Editor of the Color page, or apply a single LUT to an entire timeline

using the Timeline mode of the Node Editor.

For more information on using LUTs as part of grades, see Chapter 143, “Node Editing Basics.”

Alternately, if on-set color correction from the shoot been provided via a CDL-compliant EDL

exported from one of several on-set grading solutions that are available, you can use the

ColorTrace™ from CDL command to batch import grading information from another application.

For more information on CDL import workflows, see Chapter 149, “Copying and Importing

Grades Using ColorTrace.”

Selecting Timeline in the Node Editor

If your project’s workflow requires that you start out with even higher quality dailies, you can

go ahead and manually grade individual clips as you would with any project. However, if you

want to create a fast “one-light” adjustment for every clip in the Master Timeline at once,

you can use the Timeline grade mode of the Node Editor in the Color page to apply a single

correction simultaneously to every clip in the current Timeline. This is particularly useful as

you can readjust the Timeline grade as much as you like, and the changes are automatically

applied to every clip in the Timeline.

For more information, see Chapter 143, “Node Editing Basics.”


Import and Conform Projects | Chapter 57 Creating Digital Dailies for Round Trip Workflows

EDIT