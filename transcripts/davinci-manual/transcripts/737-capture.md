---
title: "Capture"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 737
---

# Capture

These settings are used when you use the Capture mode in the Media page to capture clips from tape

into the Media Pool. Media is captured as DPX image sequences.

�Capture: Lets you choose whether to capture both Video and Audio, or Video Only.

�Video Format: The format that scanned film frames are saved as.  When capturing from tape, the

available options are DPX and QuickTime. When capturing from the Cintel film scanner, this is

restricted to Cintel Raw Image (CRI), which is a raw data format that DaVinci Resolve automatically

debayers as a Cineon log-encoded image for grading.

�Codec: The codec used to write captured media. When capturing from tape, these include the

various type of Apple ProRes, 8- and 10-bit YUV 422, 10-bit RGB, and the various types of DNxHD.

Cintel Raw Image files default to RGB.

�Save clips to: A field that displays the directory path to which media files captured from tape are

written. You want to choose a volume that’s fast enough to accommodate the data rate of the

media format you’re capturing.

�Browse: Click this button to choose a directory to write captured media to. The directory you

choose appears in the field above.

�Save in this folder path: A series of checkboxes let you specify what other information to use to

define the directory hierarchy that will hold the captured media. Every checkbox you turn on adds

an additional directory with a name defined by that checkbox’s metadata. You can choose any or

all of the following: Program name, Clip number, Reel number, and Roll/Card.

�Apply reel number to: Lets you choose how to write the reel name. Two checkboxes let you write

the reel number to the file’s name, and/or to the Header data.

�Use prefix: A field lets you type in a prefix to be used in the media file’s name. This lets you add

text identification that will make the media more easily identifiable and searchable.


Deliver | Chapter 189 Delivering to Tape

DELIVER

�Apply prefix to: Two checkboxes let you choose to use the prefix you typed in the file name,

and/or in the folder name.

�Use frame number with: When capturing to image sequences, you can choose how many digits to

use when writing the frame number into the name of each frame file.

�Set batch ingest handles to: When capturing to image sequences from a batch list, defines how

many frames of additional handles to ingest along with each logged clip.

�Enable audio input: Turn this checkbox on to capture audio along with the video. If you’re

capturing QuickTime or MXF files, the audio will be written as additional tracks inside each file.

If you’re capturing to a DPX image sequence, then a broadcast .wav file is recorded separately.

�Input: Lets you choose how many tracks of audio to capture, from 2 to 16.

Playout Settings

These settings only affect the video signal that’s output when you use the Edit to Tape mode of the

Deliver page.

�Output: Lets you choose whether to output both Video and Audio, Video Only, or Audio Only if

you’re doing an audio layback.

�Output Source Timecode: Turn this checkbox on to output each individual clip’s source timecode.

This option is only applicable when assemble editing to tape.

�Output LTC: With a Blackmagic Design DeckLink or UltraStudio device using HD-SDI, longitudinal

timecode (LTC) is available on track 16 of the HD-SDI video signal, making it easy to use a Mini

Converter de-embedder to extract this analog timecode audio signal and feed it directly to a

recording device. This is particularly helpful if you have outboard video processing equipment

such as a noise reducer or format converter that does not pass through the VITC timecode.

�Delay LTC by x frames: When outputting LTC to bypass outboard processing gear, such as a

noise reducer or format converter, you can compensate for the processing delay by delaying the

timecode by a matter of frames to ensure that the processed image and timecode reach the deck

at the same time. With a DVS card there is a separate timecode output.

�Enable audio output: When this checkbox is enabled, DaVinci Resolve will play all available

timeline audio along with the video being output, so both can be recorded to tape.

�Offset audio by x frames: Lets you specify an offset between the audio track and video to achieve

proper A/V sync in cases where the video is being delayed by outboard processing hardware.

�Output x channels of audio: Choose the number of audio tracks to output to tape.

�Set batch playout head handle to x seconds: When batch outputting multiple clips, you can

specify a number of frames before the In point of each clip to be output as well.

�Set batch playout tail handle to x seconds: When batch outputting multiple clips, you can specify

a number of frames after the Out point of each clip to be output as well.

�Apply gaps between clips: This checkbox lets you add a black gap, of the specified duration in

frames, between every two clips being output when outputting in batch mode.


Deliver | Chapter 189 Delivering to Tape

DELIVER

Edit to Tape Queue Option Menu Settings

The following settings and options are available in the Option menu found at the top right-hand corner

of the Edit to Tape Queue.

�Show Job Details: Lets you see more information about each job listed in the Render Queue.

�Clear Recorded: Clears all queue items that have already been output to tape.

�Clear All: Clears every queue item.

�Sort by Reel & Timecode: Does a multi-criteria sort by reel and timecode, reel first, then timecode.

�Sort by Timecode: Sorts by timecode only.

�Output Source Timecode: Sets tape output to write source timecode to tape (each clip’s individual

timecode), rather than record timecode (from the Timeline).

�Use Preview for Tape Output: Enables Preview mode when outputting to tape. Preview mode lets

you test how an edit to tape operation will work before actually recording it.

Tape Output Procedures

There are a few different ways you can output media to tape, depending on what you need

to accomplish, and on how intensive your grades are relative to the processing capabilities of

your workstation.

Power Mastering

Power Mastering allows you to select either a range of clips, or an entire timeline, to be output to tape

in real time, without rendering. This can save you from a time-consuming render, and it also saves disk

space. Power Mastering is a no-compromise procedure, since your program is still output at full quality.

If there are a handful of clips with grades that you know are too processor-intensive to be Power

Mastered, you can use the Render Cache controls to cache the problem clips before output.

For more information, see Chapter 8, “Improving Performance, Proxies, and the

Render Cache.”

Outputting a Program From the Timeline

The simplest method of outputting to tape is to output a single Timeline, either in its entirety, or in part

if you’re insert editing a small section that has been revised.

To Power Master to tape:


Use the Render Cache, if necessary, to cache any clips that are too processor-intensive to output

in real time.


Click the Edit to Tape mode button to the left of the transport controls to switch to tape output.


Define how much of the current Timeline to output by moving the playhead throughout the

program, and then right-clicking clips that define the beginning and end of the range you need to

output and using the Mark In and Mark Out commands.


Deliver | Chapter 189 Delivering to Tape

DELIVER


Use the transport controls to find the In point on tape at which you want to start recording, and

click the In button.


Choose Insert from the dropdown menu at the upper right-hand side of the Viewer, if you’re either

outputting to a striped and blacked tape, or inserting over an existing program on tape.


Click the Power Mastering (lightning bolt) button at the bottom of the tape settings to add the job

you’ve just set up to the Edit to Tape Queue.


Click Start Record to begin the process of outputting to tape. Device control is used to record to

the designated section of tape; a progress bar appears at the bottom of the Render Queue to

show how long this will take.

If you don’t want to Power Master, you can render the section of the Timeline you need to output as a

single clip first, as a self-contained media file, and then add that clip directly to the Edit to Tape Queue.

This might be an easier solution if you’re outputting an extremely processor-intensive timeline.

To output a pre-rendered media file to tape:


Click the Add Clips button at the bottom of the tape settings, and use the VTR Record dialog to

select the media file you rendered in step 1, and click Add Clip(s) to Queue.

The media file you selected is added to the Edit to Tape Queue as a Power Mastering job, and will

be output in its entirety.


Use the transport controls to find the In point on the tape at which you want to start recording, and

click the In button.


Choose Insert from the dropdown menu at the upper right-hand side of the Viewer, if you’re either

outputting to a striped and blacked tape, or inserting over an existing program on tape.


To preview what the edit will look like before actually writing it to tape, choose “Use Preview for

Tape Output” from the Edit to Tape queue option-menu, and then click Start Record to watch

DaVinci Resolve run through the edit using the deck. After previewing the edit, turn this setting off.


Click Start Record to begin the process of outputting to tape. Device control is used to record to

the designated section of tape; a progress bar appears at the bottom of the Render Queue to

show how long this will take.

Batch Outputting Multiple Clips

You also have the option of outputting a number of clips to tape in a batch operation, as opposed to

outputting from the Timeline. When you set up a batch of multiple clips in the Edit to Tape Queue, then

DaVinci Resolve will automatically record them sequentially to tape.

How the timecode is generated during batch output depends on the “Output Source Timecode”

setting in the Capture and Playback panel of the Project Settings. If this is turned off, then a continuous

timecode track will be written to cover everything being output to tape. If this is turned on, then each

clip’s source timecode will be written to tape discontinuously.

When batch outputting to tape, you can add black handles to each of the clips to space them out,

making later ingest easier, using the “Set batch playout head/tail handle” settings in the Capture and

Playback panel of the Project Settings.


Deliver | Chapter 189 Delivering to Tape

DELIVER

To make a Batch Record multiple clips to tape:


Use the transport controls to find the In point on tape at which you want to start recording, and

click the In button.


Do one of the following to add items to output to the Edit to Tape Queue:

�Click the Add Clips button at the bottom of the tape settings, and choose one or more media

files from the VTR Record browser, and click Add Clip(s) to Queue.

�Right-click any clip in the Timeline, choose Render This Clip, and then click the Power Mastering

button at the bottom of the tape settings to add that clip to the Queue.


Choose either Assemble or Crash from the dropdown menu at the upper right-hand side of the

Viewer. Because you’re outputting clips with discontinuous timecode, you cannot insert edit when

batch outputting.


Once you’ve added all the clips you want to output to the queue, click Start Record to begin

outputting to tape. Device control is used to record to the designated section of tape; a progress

bar appears at the bottom of the Render Queue to show how long this will take.


Deliver | Chapter 189 Delivering to Tape

DELIVER