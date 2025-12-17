---
title: "The Scene Detect Options Drop-down Menu"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 88
---

# The Scene Detect Options Drop-down Menu

The Options drop-down menu, located at the upper right-hand corner of the Scene Detect window,

contains a variety of commands.

�Reset Zoom: Sets the zoom level of the Scene Cut Graph such that the entire clip fits

within the current width.

�Reset Marks: Clears the current In and Out points you’ve set.

�Prune Scene Cuts: If you’ve identified a large number of false positive scene cuts (for example, a

cluster of cuts corresponding to a dissolve from one shot to another), use the In and Out buttons

to surround the undesirable range of scene cuts in the Scene Detect Graph, and then click Prune

Scene Cuts to eliminate all scene cuts between these points that are within one frame of another

scene cut. Within the group of identified cuts, the highest probability cut will remain while the

other cuts are deleted.

�Save Scene Cut: Saves the current scene cut detection information, including the probability

metadata, to disk. Scene Cut files use the file extension .sc and can be reimported later to

continue working on a lengthy scene detection task.

�Load Scene Cut: Imports an existing .sc file into the Scene Detect window. You must first open the

media file you’re working on into the Scene Detect window before you can load a Scene Cut file.

�Save EDL: Exports the Cut List as a CMX-style EDL.

�Load EDL: Loads a CMX-style EDL into the Cut List, letting you use the cut information from the

EDL during the Scene Cut Detection process.

�Auto Cue: When enabled, the playhead jumps to each new scene cut as it’s detected when

you initiate scene detection. This lets you evaluate each scene cut as it’s found using the

three viewers above.

An Example Scene Detect Workflow

This section describes an ideal workflow for using scene detection without an EDL.

To scene detect a media file:


Locate a media file to scene detect using the Media Storage browser of the Media page.


Verify its frame rate and if it uses drop-frame timecode, and make sure that the “Timeline frame

rate” matches the “Use drop frame timecode” parameter in the Master Settings panel of the

Project Settings. These parameters are not automatically set if the project already has media in the

Media Pool, and you may have problems if they don’t match your media.


Right-click the media file, and choose Scene Cut Detection.


When the Scene Detect window appears, click the Options drop-down menu and choose Auto

Cue (it should be on by default, but it’s always good to check), then click Auto Scene Detect.

Scene detection initiates, and you can evaluate each scene cut as it’s found. If any scene cut looks

wrong (three sequential frames in a row), note its place in the list for future evaluation.


When DaVinci Resolve has finished scene detection, move the playhead to some of the shorter

scene cuts, and verify if they’re actual cuts by checking the three viewers above. If the frames

being displayed are “different-same-same,” then it’s a genuine cut.

If the frames being displayed are “same-same-same” (actually three sequential frames),

then these aren’t cuts.


Ingest and Organize Media | Chapter 23 Using Scene Detection

MEDIA

TIP: Fast camera motion such as whip pans, sudden changes in lightness such as camera

flashes, or even film coming up to speed causing the shutter to “flash” can confuse the

analysis, which looks for large changes in the image.


If there are numerous low-confidence scene cuts that you’ve verified aren’t cuts, drag the magenta

confidence bar so that the low-confidence scene cuts fall below it to automatically remove them

all from the list.


Next, you may want to move down the Cut List, evaluating each scene cut to verify that it’s correct.

Click the first scene cut in the list, check it, then press the keyboard Down Arrow key to select the

next list item down, check it, and repeat until you’ve checked every item in the list. If you need to

move back up the list, you can press the Up Arrow key to select the previous list item. If any item

is not a cut point, click the “Delete” button at the bottom left corner of the Scene Detect window to

eliminate that scene cut.


If there are sections in the Scene Detect Graph with dense groups of spikes, these are probably

frames with types of motion that confused the Scene Cut Detector. To delete this unwanted

“noise” in the data, use the In and Out buttons to isolate the data, and then click “Prune” to delete

these unwanted scene cuts.


If there’s a gap between any two scene cuts that you’re positive should have another scene cut,

then scrub the playhead or use the transport controls to find the missing cut, and click the “Add”

button at the bottom left corner of the Scene Detect window to add another scene cut.

TIP: Adjacent shots with very similar ranges of color and contrast may sometimes go

undetected by the scene detection algorithm. If you know of scenes in the media you’re

analyzing that are like this, you may want to scrub through them a bit more carefully to make

sure you’re not missing anything. However, if you find you’ve missed a cut later, you can

always use the Split Clip control in the Edit page timeline to add a new edit point.

10	 When you’re confident that the Cut List is accurate, split the media file into individual clips in the

Media Pool by clicking “Add Cuts to Media Pool.”

11	 When the Conform Settings dialog appears, click OK if you checked your settings in step 2.

12	 Close the Scene Detect window.

The individually cut up clips of the media file you analyzed now appear in the Media Pool, and you can

edit the entire sequence of clips into a new Timeline in order, ready for grading.


Ingest and Organize Media | Chapter 23 Using Scene Detection

MEDIA

Chapter 24

Ingesting From Tape

DaVinci Resolve is capable of capturing media from tape using a compatible video

input device, such as a Blackmagic Design UltraStudio or DeckLink card. Device

control is supported.

Contents

Tape Ingest���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 466

The Tape Capture Interface������������������������������������������������������������������������������������������������������������������������������������������������������������ 466

Setting Up to Capture From Tape������������������������������������������������������������������������������������������������������������������������������������������������ 467

Deck Settings������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 467

Capture������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 468

The Three Methods of Capture����������������������������������������������������������������������������������������������������������������������������������������������������� 469

Using Capture Now������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 469

Logging and Capturing Individual Clips������������������������������������������������������������������������������������������������������������������������������������ 469

Logging and Capturing Multiple Clips���������������������������������������������������������������������������������������������������������������������������������������� 470

Batch Capture Via EDL����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 471


Ingest and Organize Media | Chapter 24 Ingesting From Tape

MEDIA

Tape Ingest

This chapter covers how to capture media from tape directly into the Media Pool in DaVinci Resolve.

Whether you need to capture a handful of clips to incorporate into an existing project, or you need to

recapture every clip corresponding to the events of an EDL, you can use the Media page in Capture

mode to capture from any device-controllable deck via a compatible video interface.

To switch to tape capture in the Media page:

�Click the Capture button, located to the left of the Interface toolbar at the top of the Media page.

The Media page updates to reflect the relevant controls for editing to tape, and the Audio panel is

replaced by a dedicated set of capture metadata and controls to help you track the resulting clips.

The Tape Capture Interface

While in Capture mode, the Media page is used to control the VTR, in order to establish In and Out

points for logging or capturing a selected range of the tape.

Tape Capture viewer in the Media page

�Transport controls: The transport controls, while similar in appearance to those used when simply

playing through selected clips in the Media page, now work to control the VTR.

�Shuttle control: A shuttle control appears in what was formerly the scrubber bar, which lets you

shuttle through the range of reverse and forward speeds compatible with the connected deck.

�In and Out controls: In Capture mode, the In and Out buttons to the right of the transport controls

define a range of the tape from which to capture.

�Capture panel: The panel automatically switches to the Capture panel, with tape-specific

metadata and capture controls. Populating File Name Prefix updates the file name preview that’s

shown above in the Header, that also shows the Capture directory, Resolution, and Frame Rate

specified in the Capture and Playback panel of the Project Settings.


Ingest and Organize Media | Chapter 24 Ingesting From Tape

MEDIA

Editable capture metadata

Setting Up to Capture From Tape

Before you begin capturing from tape, you need to adjust a variety of settings in the Capture and

Playback panel of the Project Settings. Two groups of settings, in particular, need to be defined.

Deck Settings

These settings affect both capture and playback when using the Tape Ingest options of the

Media page, or the Tape Output options of the Deliver page.

�Video capture and playback: You can choose the video format (frame size and frame rate) with

which to output to tape from this drop-down menu. HD timelines can be downconverted to SD,

and SD timelines can be upconverted to HD using the format conversion of your DeckLink card.

�Use left and right eye SDI: A checkbox that enables the Blackmagic Design DeckLink HD

Extreme 3D+ to ingest and output muxed stereoscopic video when used with supported VTRs,

such as HDCAM SR decks with 4:2:2 x 2 mode. (When muxed stereoscopic signals are ingested,

each eye is separated into individual left-eye and right-eye image files.)

�Video connection operates as: Selects between the available signal options: Use 4:4:4 SDI

and Enable Single Link. Which options are available depend on which video capture card

you are using.

�Data Levels: Lets you specify the data range (normally scaled or full range) that’s used when

ingesting from or outputting to tape. This option switches the data range of the signal output by

your video capture card, but only during capture from tape in the Media page, or output to tape in


Ingest and Organize Media | Chapter 24 Ingesting From Tape

MEDIA

the Deliver page. When capture or output is not currently occurring, your video capture card goes

back to using the identically named data range setting in the Master Settings panel of the Project

Settings pane, which governs how you monitor the signal being output on an external broadcast

display or projector.

�Video bit depth: 10-bit is the only available option.

�Use deck autoedit: If supported by your video deck, this is the best method to record video

to the deck, as it enables the deck to roll the edit using the specified preroll, and control the

edits via serial device control. If this checkbox is turned off, a basic edit On/Off mode is used

by the deck, with the potential for frame inaccuracies if the “Non auto edit timing” setting is not

properly adjusted.

�Non auto edit timing: Adjusts the edit synchronization of the connected deck when auto edit is

turned off.

�Deck preroll: Sets the number of seconds for preroll. How much is appropriate depends on the

performance of your deck.

�Video output sync source: When using a DeckLink card this is set to Auto. Other capture cards

may require you to set the sync source to “Reference” for playout and “Input” for ingest. This

setting is only available if you have the DVS card installed on your system.

�Add 3:2 pulldown: Inserts or removes the 3:2 pulldown required to record or play 23.98 fps media

to or from a 29.97 tape format.