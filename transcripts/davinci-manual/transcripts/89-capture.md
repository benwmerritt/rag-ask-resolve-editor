---
title: "Capture"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 89
---

# Capture

These settings are used when you use the Capture mode in the Media page to capture clips from tape

into the Media Pool, or when controlling the Cintel Film Scanner to scan film of different formats.

�Capture: Lets you choose whether to capture both Video and Audio, or Video only.

�Video Format: The format captured media will be saved to. When capturing from tape, the

available options are DPX and QuickTime.

�Codec: The codec used to write captured media. When capturing from tape, these include the

various type of Apple ProRes, 8- and 10-bit YUV 422, 10-bit RGB, and the various types of DNxHD.

�Save clips to: A field that displays the directory path to which media files captured from tape

are written. You want to choose a volume that’s fast enough to accommodate the data rate of the

media format you’re capturing.

Browse: Click this button to choose a directory to write captured media to. The directory you

choose appears in the field above.

�Save in this folder path: A series of checkboxes lets you specify what other information to use to

define the directory hierarchy that will hold the captured media. Every checkbox you turn on adds

an additional directory with a name defined by that checkbox’s metadata. You can choose any or

all of the following: Program name, Clip number, Reel number, Roll/Card.

�Apply reel number to: Lets you choose how to write the reel name. Two checkboxes let you write

the reel name to the file’s name, and/or to the Header data.

�Use prefix: A field lets you type in a prefix to be used in the media file’s name. This lets you add

text identification that will make the media more easily identifiable and searchable.

�Apply prefix to: Two checkboxes let you choose to use the prefix you typed in the file name, and/

or in the folder name.

�Use frame number with: When capturing to image sequences, you can choose how many digits to

use when writing the frame number into the name of each frame file.

�Set batch ingest handles to: Lets you add additional frames of handles to the beginning and end

of each scanned clip when batch capturing with the scanner.

�Input: A drop-down that lets you choose how many tracks of audio to capture, from 2 to 16.


Ingest and Organize Media | Chapter 24 Ingesting From Tape

MEDIA

The Three Methods of Capture

Once you’ve set up all relevant settings in the Project Settings window, including at minimum “Video

Capture and Playback,” “Capture Clips Saved to,” and Apply Reel Name to” settings, then you’re ready

to start capturing. Depending on your workflow, there are three methods of capturing from tape that

you can use.

For all capture methods, media can be ingested as QuickTime Movies or DPX image sequences.

Using Capture Now

If you simply need to capture a section of tape quickly, you can use the Capture Now command.

To Capture Now:


Use the transport controls and the In button to identify what you want to capture.


Enter all relevant information into the various fields of the Metadata Editor. The Header updates to

show a preview of the file name that will be saved.


Use the transport controls to start playback, and then click the Capture Now button at the bottom

of the Metadata Editor.


When the section of tape you wanted to record has finished, click Capture Now again to

stop capture.

A new clip appears in the Media Pool, automatically placed in a new folder in the Media Pool with a

name defined by the timecode value converted into a frame count, based on the ingest frame rate.

For example, 00086400.dpx is the file name of a clip captured at timecode 01:00:00:00.

Logging and Capturing Individual Clips

If you’re capturing an exact range of tape, or multiple sections at once, you can also work by logging

each section of tape you want to capture in advance, before using the Capture Clip or Batch Clips

commands in a second step.

To capture a single clip using device control:


Use the transport controls to find the beginning of the section of tape you want to record, and

click the In button. Then, find the end of the section of tape you want to record, and press the

Out button.


Enter all relevant information into the various fields of the Metadata Editor. The Header updates to

show a preview of the file name that will be saved.


When you’re finished, click Capture Clip.

Deck control is automatically used to play through the specified range of tape and capture that clip.

When capture is complete, the new clip appears in the Media Pool.


Ingest and Organize Media | Chapter 24 Ingesting From Tape

MEDIA

Logging and Capturing Multiple Clips

For efficiency’s sake, you can also log multiple clips at once, from multiple tapes if necessary, and then

batch capture them all at once.

To log one or more clips:


Use the transport controls to find the beginning of the section of tape you want to record, and

click the In button. Then, find the end of the section of tape you want to record, and press the

Out button.


Enter all relevant information into the various fields of the Metadata Editor. The Header updates to

show a preview of the file name that will be saved.


When you’re finished, click Log Clip.

That clip is added to the Media Pool as an offline tape clip, indicated by a black icon with a

tape badge.

Logged clip in the Media Pool prior to capture

To batch capture one or more logged clips:


(Optional) Put the Media Pool into List view, and click the Reel No column header to sort the

Media Pool clips by reel number. This makes it easier to select a range of clips to capture from a

particular reel.


Select one or more offline tape clips in the Media Pool that come from a particular reel.


Click Batch Clips, at the bottom of the Metadata Editor. To interrupt capture at any time,

click Batch Clips again.

Deck control is automatically used to play through the current tape in the VTR and capture every

logged clip you’ve selected that can be found on that tape, starting with the clip with the lowest

timecode value and ending with the clip having the highest timecode value. A progress bar

with accompanying text shows how much longer to go until capture is complete. As each clip is

captured, its corresponding logged clip in the Media Pool updates with a thumbnail reflecting the

captured media.

When DaVinci Resolve finishes capturing all clips from a particular reel, Batch Capture stops.


Ingest and Organize Media | Chapter 24 Ingesting From Tape

MEDIA

Batch Capture Via EDL

You can also use an EDL to create offline tape clips, one for each event in the EDL, with which to batch

capture all the media necessary to conform a project from tape.

To import an EDL as a batch capture list:


Open the Project Settings, click Master Panel in the sidebar, and make sure of the following:

�Set “Timeline frame rate” to the frame rate of your EDL.

�Turn on “Use drop frame timecode” if your EDL requires it.

�Make sure “Use Timecode” is set to “Embedded in the source clip.”

�Turn on “Assist using reel names from the.”


Choose File > Import Batch List From EDL.


When a Conform Settings dialog appears asking you to confirm the current Project Settings, click

OK if the settings are good.


Use the controls of the Select EDL files dialog to select one or more EDLs, then click Open. If you

select multiple EDLs, then every event in each EDL is imported at once.


In the dialog that appears next, choose a frame rate to conform the EDL at, and click OK.

Each event in the EDL now appears as offline tape clips in the Media Pool, ready for capturing.

If you load an EDL and there are already clips in the Media Pool that have the same reel name

and start timecode as events in the EDL, DaVinci Resolve will not create new offline tape clips

for those.

A set of logged clips imported from an EDL


(Optional) Put the Media Pool into List view, and click the Reel No column header to sort the

Media Pool clips by reel number. This makes it easier to select a range of clips to capture from a

particular reel.


(Optional) If there are any offline clips that you don’t need to capture, you can remove them from

the Media Pool by right-clicking them and choosing Remove Selected Clips.


Ingest and Organize Media | Chapter 24 Ingesting From Tape

MEDIA


Select which of the offline tape clips you want to capture. It’s best to select ranges of clips that

come from the same reel.


Click the Capture mode button to the left of the transport controls, and then click Batch Clips

to begin capture. To interrupt capture at any time, click Batch Clips again. Deck control is

automatically used to play through the current tape in the VTR and capture every logged

clip you’ve selected that can be found on that tape, starting with the clip with the lowest

timecode value and ending with the clip having the highest timecode value. A progress bar

with accompanying text shows how much longer to go until capture is complete. As each clip is

captured, its corresponding logged clip in the Media Pool updates with a thumbnail reflecting the

captured media.

When DaVinci Resolve finishes capturing all clips from a particular reel, Batch Capture stops.


Ingest and Organize Media | Chapter 24 Ingesting From Tape

MEDIA