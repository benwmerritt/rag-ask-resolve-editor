---
title: "Audio Panel"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 731
---

# Audio Panel

This panel contains all audio-oriented parameters.

�Export audio: Turn this checkbox on to render the source audio, or audio that you’ve synchronized

in DaVinci Resolve, along with the media being output by DaVinci Resolve.

�Format: You can choose which format of audio you want to render. Depending on which format

you choose, different audio codec options will appear below.

MXF OP1A(IMF): Generates media files that conform to the OP1a (Operational Pattern 1a) SMPTE

378M format of MXF media for file exchange.

MXF OP-Atom: Generates media files that conform to the SMPTE 390M format of MXF media for

file exchange.

QuickTime: Exposes all available formats of audio compatible with QuickTime.

MP4: Generates media in the MPEG-4 file format.

WAVE: Generates media in the WAVE file format.

MP3: Generates media in the MPEG-3 file format.

FLAC: Generates media in the FLAC file format.

�Codec: Lets you choose between Linear PCM (the default), AAC audio, IEEE Float, or MP3. AAC

audio encoding is only available on macOS.

�Sample Rate: Lets you set the sample rate, in Hz, of the output of the audio.

�Bit Rate Strategy: (Available for AAC encoding) You can choose among Constant Bit Rate,

Average Bit Rate, Variable Bit Rate Constrained, and Variable Bit Rate.


Deliver | Chapter 187 Rendering Media

DELIVER

�Quality: (Available for AAC encoding when Bit Rate Strategy is set to Variable Bit Rate) Five

settings you trade between speed and quality when encoding AAC audio.

�Data Rate: (Available for AAC encoding when Bit Rate Strategy is set to Constant, Variable, or

Variable Constrained) Lets you choose the maximum data rate for AAC encoding.

�Bit Depth: Lets you specify the bit depth at which to output the source audio.

�Render one track per channel checkbox: This checkbox lets you specify whether you want to

export each channel as an individual track in the structure of the exported file. Multi-channel

formats can be specified (2.0, 5.1, etc.), or can be output as flat multi-mono files.

�Render as discrete audio tracks checkbox: This checkbox is similar to the above, in that it still

outputs one channel per track. However, discrete tracks have no positioning info, nor do they

group as multi-channel clips (2.0, 5.1, etc.). For example, a mono file exported with Render one

track per channel, comes in front and centered. The same file exported as a discrete audio track

has no built in position information.

�Output Track #: This dropdown menu lets you choose which Main or Submix bus you want to

output. A Plus button to the right lets you add additional tracks you want to export in this job, so if

you want to export multiple Mains or multiple Subs, you can add more Track pop-ups.

When you choose a track with multiple channels of audio, a field appears showing how many

channels will be output; you have the option of using a virtual slider to change how many channels

are output.

In Single Clip Mode, when you choose “All Timeline Tracks, each audio track in the current timeline

will be rendered as an individual track in the rendered media file you’re outputting. Multi-channel

tracks containing multi-channel clips will output audio tracks containing the same number of

channels in the output media, which means you can output mixed combinations of mono, stereo,

5.1 or 7.1, and adaptive audio tracks, and each separately rendered audio track will reflect identical

channel mappings.

�Language: (Only available when outputting to the IMF format) This dropdown menu lets you

choose the language of a particular output track when you’re outputting to IMF. Since IMF files can

accommodate multiple audio tracks containing different mixes for different regions, it’s important

to identify each output track you’re outputting by language.

�Content: (Only available when outputting to the IMF format) This dropdown menu lets you

choose the content of a particular output track when you’re outputting to IMF. Since IMF files

can accommodate multiple audio tracks containing different mixes and content, it’s important to

identify each output track you’re outputting by content.

�Audio Normalization: You can select loudness standard presets from the Audio tab in the Render

settings on the Delivery page to automatically have the deliverable normalized accordingly.

These controls let you control the audio normalization on a per output basis. Unchecking this box

bypasses audio normalization and optimization.

Normalize to Standard: Check this box to normalize loudness or peak (scaling whichever first

exceeds thresholds) to a standard.

Optimize to Standard: Check this box to optimize loudness and peak (ensuring that loudness

meets the desired range and peaks remain lower than threshold) to a standard.

Standard: Choose the normalization standard you want to apply.

Target Level: Set the normalization level in dBFS.

Output Track #: Check the box to apply the normalization to these outputs.


Deliver | Chapter 187 Rendering Media

DELIVER

File

This panel contains all other parameters.

�Filename Uses: Three options let you automatically name the media file(s) that are

output automatically.

Use Custom Filename: Lets you enter your own name in the Custom name/File prefix field.

Use Timeline Name: (When rendering a Single Clip) When this option is selected, the name of the

Timeline is used.

Use Source Filename: (When rendering Individual Clips) When this option is selected, the

filename of each clip’s corresponding source media file is cloned, and used as the filename of

media being output by DaVinci Resolve. This is preferred when you’re generating offline media

for use by an editor that you later want to reconform to the originating DaVinci Resolve project.

When this checkbox is turned off, you can customize filenames using the other options in this

section of settings.

�Custom name: Lets you use custom text to name all rendered files. If you’re not using the source

filename, and not rendering to a file format that uses timecode, you can enter a filename here.

When editing the Custom Name or File Prefix (or File Suffix), you can use “metadata variables” that

you can add as graphical tags that let you display clip metadata. This is especially useful when

rendering Individual Source Clips.

For example, you could add the corresponding metadata variable tags

%scene_%shot_%take and the File Prefix would be written as “12_A_3” if “scene 12,”

“shot A,” “take 3” were in the source clip’s metadata.

For more information on the use of variables, as well as a list of all variables that are

available in DaVinci Resolve, see Chapter 16, “Using Variables and Keywords.”

�File suffix: Lets you add custom text and/or metadata variables (described previously) to the end

of all rendered files.

�Use unique filenames: (When rendering Individual Clips, and only when Filename uses is set

to Custom name) When enabled, additional characters are added to every rendered media file

to guarantee that each rendered media file has a completely independent name. This prevents

multiple rendered clips from the same source media file from overwriting one another when

saved to the same directory. “Uniquely” named clips append the clip name with the track and

clip number identifying a clip’s position in the currently selected session. For example, a clip

that’s linked to a media file named “DropThatThingCU.mov,” and edited as the twenty-fifth clip on

track V2, will be named “DropThatThingCU_V2-0025.mov” when rendered. When enabled, two

other options are revealed.

Use unique filename prefix/Use unique filename suffix: (When Use Unique Filenames is on)

Radio buttons let you choose whether to add the unique identifier at the beginning or end of a

clip. Choosing Prefix would result in “V2-0025 _DropThatThingCU.mov,” whereas choosing Suffix

would result in “DropThatThingCU_V2-0025.mov” when rendered.

�Add source frame count to filename: (When rendering Individual Clips, and only when Filename

uses is set to Custom name) When enabled, the source frame number of each clip is appended to

the end of the rendered file name. This is another way to make sure that multiple rendered clips

with custom names don’t overwrite one another.

�Use filename digits: Lets you specify how many digits to use when rendering an image sequence,

although the specified digits will also be used for any media format. This is particularly useful

if you’re outputting media to be used by an application that has strict requirements for image

sequence numbering. Defaults to eight digits.


Deliver | Chapter 187 Rendering Media

DELIVER

�Each clips starts at frame: (When rendering Individual Clips) This permits timecode to be written

to the header, and frame count to be written to the filename of the image sequences, which is

ideal for VFX workflows.

�Start timeline timecode at: (When rendering Single Clip) This option is only available when

rendering clips in Single clip order. Specifies the timecode that will be written to the media

being output by DaVinci Resolve. For DPX files, timecode is written into the header data, and

is simultaneously converted to a frame count that’s inserted into the filename of each frame

file, which provides a logical count of the frame numbers. For other media formats, timecode is

written to the appropriate metadata container. You may find it useful to use custom start times,

for example starting each reel of a project at a particular value, depending on the standards

employed at your shop.

�Place clips in separate folders: (When rendering Individual Clips) Useful if you need to preserve

the filenames of files you’re outputting when the filenames of clips coming from the same source

media file may cause them to overwrite one another. This option is also commonly used when

rendering VFX shots for additional post-production work, allowing the VFX department to identify

clips quickly and distribute the work accordingly.

�Preserve Source directory levels: (When rendering Individual Clips) Retains a user-specified

depth of the original directory structure used by a clip’s corresponding source media file,

recreating it when rendering new files for output. The number you select determines how many

levels of subdirectories DaVinci Resolve will automatically create within the currently specified

“Render job to” directory to match the path used by the source files. Defaults to 0, which creates

no matching subdirectories.

After Head/From Tail: When setting how many directory levels of each clip’s file path to preserve

(using the “Preserve x levels” parameter), click one of these buttons to specify whether that

number of path levels is defined relative to the head or the tail of each media file path.

Preserved Path: Shows you a preview of the preserved path you’ve set up so you know you’ve

gotten it right.

�File Subfolder: (Only appears in Additional Output panels) Lets you specify a subdirectory into

which to render the media files being output. If the specified subdirectory doesn’t exist, a new one

with that name will be created within the currently specified “Render job to” directory.

�Use commercial workflow: (When rendering Individual Clips) Automatically renders every version

that’s applied to each clip in the session, except for versions that have been flagged using the

“Render Disabled” flag, found in the Version submenu for each clip in the Timeline. This option is

typically used when you’ve graded multiple versions of a clip to be used for VFX work, and you

want to deliver each grade as a separate media file. This is also used when rendering programs

for commercial broadcast where you have two or more versions of a grade for each scene. When

using this option, alternate methods of outputting each rendered media file are used, and four

additional settings are revealed.

Alternative pass offset: Lets you separate the timecode values written into each version of a clip

with an offset. For example, if the default version timecode is 01:00:20:00, and you select a 10

minute offset in the Alternative Pass Offset timecode entry, then the second graded version of

that clip will start at 01:10:20:00, the third version will start at 01:20:20:00, and so on until every

version is rendered. You can offset the clips by whatever value you like, but the idea is to make

it easy for editors and VFX artists to find the versions of each grade. If the clips are shared with

a finishing artist, and they know that each alternate pass is 10 minutes apart, then it’s easy for

the finisher to change the clip version just by adding 10 minutes to the referenced timecode.

To simplify the workflow further, you can put separate source reels in separate folders using the

next three options.

Place reels in separate folders: Automatically places all media that’s output using a particular reel

name into corresponding folders.


Deliver | Chapter 187 Rendering Media

DELIVER

Place clips in separate folders: Automatically places alternate grades of clips into

separate folders.

Use version name for folders: Labels each folder with the name of the version when using the

Commercial Workflow option.

�Render speed: A dropdown menu lets you throttle the speed at which media is rendered.

Ordinarily you’ll leave this set to the default of Maximum. However, some storage systems that are

shared by multiple rooms in a facility use storage area networks (SANs) with insufficient bandwidth

for multiple real-time image streams. DaVinci Resolve’s incredibly fast rendering speeds can cause

playback problems with other users accessing the SAN if available bandwidth is insufficient. In this

case, you can throttle the render speed to limit SAN bandwidth usage to between 1 to 50 percent

of full rendering speed.

�Disk space currently used: Shows the amount of disk space available on the target volume.

�Disk space used after render: Shows the new disk usage based on the specified range of the

current session that you’re rendering.

Additional Outputs

Each job you create in the Render Settings defaults to a single output. However, you can create

multiple outputs when you need to deliver multiple versions of media, with individual video

formats and codecs and different data burn-in settings, to be rendered into individually named

subfolders (optional).

The menu command for creating an additional output,

shown next to an existing additional output in panel 2

This can be useful for setting up multiple rendered passes when your client requires two sets

of media, for example QuickTime ProRes 422 (HQ) media along with MXF DNxHD media.

This is also useful when you need to output two sets of media where one has window burns,

and the other is clean.


Deliver | Chapter 187 Rendering Media

DELIVER

To add additional outputs in the Render Settings:

�Choose Create Additional Output from the Render Settings Option menu. A row of numbers below

the Filename and Location controls let you open each output you create and adjust its settings.

You can have as many outputs as you require.

To remove an additional output:

�Open the additional output panel you want to remove, and click the Delete button at the bottom.