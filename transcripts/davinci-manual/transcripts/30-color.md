---
title: "Color"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 30
---

# Color

These settings affect clip versions and timeline interactions when working in the Color page.

�Automatically label gallery stills using: When enabled, DaVinci Resolve automatically generates

labels for all gallery stills you take based on the following controls:

Naming drop-down: Lets you choose what name to use for new stills. Options include: Clip Name,

Clip Version Name, Source Timecode, Timeline Timecode, Timeline Name, Display LUT Name,

Custom Label Using Tags (using metadata variables).

Append still number on export checkbox: When enabled, each new still has an appended still

number. Where the number appears depends on the following radio buttons.

As Suffix/As Prefix buttons: Lets you choose to place still numbers at the end of an auto

generated gallery label or at the beginning.

�Luminance mixer defaults to zero: Selecting this option sets the Y channel of the YRGB

parameters for all grades to zero. This is required to be able to export a compliant ASC-CDL, and

will impact all grades that use the Lum Mix control.

�Use legacy Log grading ranges and curve: DaVinci Resolve 12.5 introduced a modification to

the Log grading controls that provides smoother, more pleasing results using the same controls.

To maintain backward compatibility with older projects, a “Use legacy Log grading ranges

and curve” checkbox in the Color panel of the Project Settings lets you switch your project

between the older Log control behavior and the newer one. Older projects that are opened in

DaVinci Resolve have this checkbox turned on by default, while new projects have this turned off

by default.

�Use S-curve for contrast: On by default, this checkbox sets the contrast control in the Color

Wheels palette to apply an “S-curve” to the image, such that the shadows and highlights of a

signal will not be clipped when you increase the value. If you would prefer for these contrast

adjustments to be made linearly, and for the signal to be allowed to clip when you reach the upper

and lower boundaries of the video signal, you can turn this checkbox off.

�Use legacy sizing interactions for windows and effects: DaVinci Resolve 14.1.1 improved how

window tracking applies transformations, to correctly handle things like pixel aspect ratio (par).

New projects should leave this setting disabled, however older projects should leave this

checkbox enabled to ensure tracking and transforms remain applied the way they were before.

�Apply stereoscopic convergence to windows and effects: When enabled, DaVinci Resolve

correctly maintains the position of a window that’s been properly placed over each eye as

convergence is adjusted in the 3D palette. Enabling this checkbox also enables an additional

Convergence parameter in the Window palette that lets you create properly aligned convergence

for a window that’s placed onto a stereoscopic 3D clip, as seen in the following screenshot.

l

The Convergence control in the Transform section of

the Window palette appears when you enable “Apply

stereoscopic convergence to windows and effects”


Setup and Workflows | Chapter 6 Project Settings

MEDIA

�Use local version for new clips in timeline: Automatically sets all new clips that are added to

existing timelines, or all clips that are added to new timelines that are imported via AAF, EDL, or

XML, to use local grades by default. If you want all clips added to new timelines to use remote

grades instead, as with DaVinci Resolve version 9 and earlier, you can turn this checkbox off.

�Automatically match master timeline with media pool: If you turn on this option before importing

any media into the Media Pool, or importing any timelines that will in turn import media into the

Media Pool, you can create projects with a Master Timeline. When enabled, clips are added to and

removed from the Master Timeline as they’re added to and removed from the Media Pool, so that

the Master Timeline always contains all media in the Media Pool. Once media has been imported

into a project, this setting cannot be changed.

�Save timeline thumbnails with project: To minimize project size, and maximize the speed

of saving and loading projects, you should leave this checkbox unchecked. If you select the

checkbox, all of your Timeline thumbnails will be stored inside every project, instead of in the

default directory that’s ordinarily dedicated to stills, during both Save and Auto Save operations.

This provides a good history of the project but takes much longer to complete and uses more hard

disk space.

�Use BGR pixel order for DPX v2: Lets you choose a different pixel order for projects using

DPX version 2 media.

�Embed timecode in audio output: When turned on, directs DaVinci Resolve to output LTC

timecode that’s embedded in channel 16 of the SDI stream and channel 2 of the analog audio

output from your video interface.

�Use Timelines Bin: This option is only available to be changed before you add clips to the Media

Pool; after you’ve added clips, it’s no longer available. Turning Use Timelines Bin on creates a

dedicated Timelines bin in the Media Pool, at the top of the Bin List. When enabled, the Timelines

bin contains all timelines in a project, and you’re prevented from putting timelines into any other

bin in the Media Pool. Whenever you create or import a new timeline, it automatically appears in

the Timelines bin. You can add subfolders to the Timelines bin for more specific organization.

Dynamics Profile

Defines the default transition from one dynamic keyframe to the next for keyframed effects in the

Color page. By default this transition is linear, with the “Dynamic profile start” and “Dynamic profile

end” parameters set to 1. However, if you need to alter the acceleration of the interpolation of values

from one dynamic keyframe to the next, then you can change that keyframe’s Dissolve Type in order

to “ease” the effect transition you’re creating. The values in these settings correspond to the graph

curves found in the Dynamic Attributes dialog when editing keyframes in the Color page.

For more information, see Chapter 148, “Keyframing in the Color Page.” in “Changing Dynamic

Attributes”.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

Versions

Ten text fields provide a way for you to designate automatic names for the versions of grades that you

select in the Color page. To the right of each text field, a drop-down menu lets you add a name from a

handy list of predefined terms that’s been provided. Alternately, you can simply click any field and type

your own custom name.

When you change the name of a version in the Color page, the names you define in this list are

available from a drop-down menu in the Version Name dialog.

Using the named drop-down when editing the name of a version

Using a predefined list of names for your different versions avoids typos that can later create folder

naming issues when you use the “Commercial Workflow” options for rendering your media in the

Deliver page.

Camera Raw

This panel contains groups of parameters that correspond to every camera raw media format that’s

supported by DaVinci Resolve. Using these parameters in the Camera Raw panel, you can override

the original camera metadata that was written at the time of recording, and make simultaneous

adjustments to all camera raw clips using the “project” raw settings.

To provide more detail, these settings are covered in detail in a dedicated chapter.

For more information, see Chapter 128, “Camera Raw Palette.”


Setup and Workflows | Chapter 6 Project Settings

MEDIA

Capture and Playback

All settings in this panel let you define the functionality of capture and playout to tape using

device controlled VTRs connected to your Resolve workstation via the connected video capture

and output interface.

For more information on deck capture, see Chapter 24, “Ingesting From Tape.”

For more information on video output to tape, see Chapter 189, “Delivering to Tape.”

Deck Settings

These settings affect both capture and playback when using the tape ingest options of the Media

page, or the tape output options of the Deliver page.

�Video capture and playback: You can choose the video format (frame size and frame rate) with

which to output to tape from this drop-down menu. HD timelines can be downconverted to SD,

and SD timelines can be upconverted to HD using the format conversion of your DeckLink card.

�Use left and right eye SDI: A checkbox that enables supported video interfaces to ingest and

output muxed stereoscopic video when used with supported VTRs, such as HDCAM SR decks

with 4:2:2 x 2 mode. (When muxed stereoscopic signals are ingested, each eye is separated into

individual left-eye and right-eye image files.) This parameter only appears when your hardware is

set up appropriately.

�Video connection operates as: Selects between the available signal options: Use 4:4:4 SDI

and Enable Single Link. Which options are available depend on which video capture card you

are using.

�Data Levels: Lets you specify the data range (normally Video or Full) that’s used when ingesting

from or outputting to tape. This option switches the data range of the signal output by your video

capture card, but only during capture from tape in the Media page, or output to tape in the Deliver

page. When capture or output is not currently occurring, your video capture card goes back to

using the identically named data range setting in the Master Project Settings pane, which governs

how you monitor the signal being output on an external broadcast display or projector.

�Video bit depth: Choose the bit depth that corresponds to the capability of your deck. Depending

on your workstation’s configuration, you can choose between 8-bit and 10-bit. Outputting to 10-bit

is more processor intensive, but higher quality for compatible devices, and is the default setting.

�Use deck autoedit: If supported by your video deck, this is the best method to record video

to the deck, as it enables the deck to roll the edit using the specified preroll, and control the

edits via serial device control. If this checkbox is turned off, a basic edit On/Off mode is used

by the deck, with the potential for frame inaccuracies if the “Non auto edit timing” setting is

not properly adjusted.

�Non auto edit timing: Adjusts the edit synchronization of the connected deck when auto

edit is turned off.

�Deck preroll: Sets the number of seconds for preroll. How much is appropriate depends on the

performance of your deck.

�Video output sync source: When using a DeckLink card this is set to Auto. Other capture cards

may require you to set the sync source to “Reference” for playout and “Input” for ingest. This

setting is only available if you have a DVS card installed on your system.

�Add 3:2 pulldown: Inserts or removes the 3:2 pulldown required to record or play 23.98 fps media

to or from a 29.97 tape format.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

Capture

These settings are used when you use the Capture mode in the Media page to capture clips from tape

into the Media Pool.

�Capture: Lets you choose whether to capture both Video and Audio, or Video Only.

�Video Format: The format that scanned film frames are saved as. When capturing from tape, the

available options are DPX and QuickTime. When capturing from the Cintel film scanner, this is

restricted to Cintel Raw Image (CRI), which is a raw data format that DaVinci Resolve automatically

debayers as a Cineon log-encoded image for grading.

�Codec: The codec used to write captured media. When capturing from tape, these include the

various type of Apple ProRes, 8- and 10-bit YUV 422, 10-bit RGB, and the various types of DNxHD.

Cintel Raw Image files default to rgb.

�Save clips to: A field that displays the directory path to which media files captured from tape are

written. You want to choose a volume that’s fast enough to accommodate the data rate of the

media format you’re capturing.

Browse: Click this button to choose a directory to write captured media to. The directory you

choose appears in the field above.

�Save in this folder path: A series of checkboxes let you specify what other information to use to

define the directory hierarchy that will hold the captured media. Every checkbox you turn on adds

an additional directory with a name defined by that checkbox’s metadata. You can choose any or

all of the following: Program name, Clip number, Reel number, and Roll/Card.

�Apply reel number to: Lets you choose how to write the reel name. Two checkboxes let you write

the reel number to the file’s name, and/or to the Header data.

�Use prefix: A field lets you type in a prefix to be used in the media file’s name. This lets you add

text identification that will make the media more easily identifiable and searchable.

�Apply prefix to: Two checkboxes let you choose to use the prefix you typed in the file name, and/

or in the folder name.

�Use frame number with: When capturing to image sequences, you can choose how many digits to

use when writing the frame number into the name of each frame file.

�Set batch ingest handles to: When capturing to image sequences from a batch list, defines how

many frames of additional handles to ingest along with each logged clip.

�Input: Lets you choose how many tracks of audio to capture, from 2 to 16.

Playout

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

such as a noise reducer or format converter that passes through the VITC timecode.

�Delay LTC by x frames: When outputting LTC to bypass outboard processing gear, such as a

noise reducer or format converter, you can compensate for the processing delay by delaying the

timecode by a matter of frames to ensure that the processed image and timecode reach the deck

at the same time. With a DVS card there is a separate timecode output.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

�Offset audio by x frames: Lets you specify an offset between the audio track and video to achieve

proper A/V sync in cases where the video is being delayed by outboard processing hardware.

�Output x channels of audio: Choose the number of audio tracks to output to tape.

�Set batch playout head handle to x seconds: When batch outputting multiple clips, you can

specify a number of frames before the In point of each clip to be output as well.

�Set batch playout tail handle to x seconds: When batch outputting multiple clips, you can specify

a number of frames after the Out point of each clip to be output as well.