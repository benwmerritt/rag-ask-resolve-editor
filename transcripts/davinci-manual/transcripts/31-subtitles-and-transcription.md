---
title: "Subtitles and Transcription"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 31
---

# Subtitles and Transcription

The Subtitles panel lets you adjust presets that govern subtitles being created in subtitle tracks of

the timeline.

�Max Character Per Line: Defaults to 60. Lets you choose the maximum number of characters

allowed on one line in a subtitle.

�Minimum Caption Duration: Defaults to 3 seconds. Lets you choose the minimum duration

allowed for subtitles in the timeline.

�Maximum Characters Per Second: Defaults to 30. Automatically calculates the maximum

allowable characters per second based on a subtitle clip’s duration.

The Transcription setup panel lets you select the language that DaVinci Resolve uses to

analyze audio clips for transcription.

Language: Select one of the supported languages here. Selecting Auto lets DaVinci Resolve

analyze the audio clip and choose the language spoken.

Fusion

Fusion allows consistent frame numbering for all compositions, including trimmed clips. This means

that any composition created in Fusion can start with the same start frame number. In new projects

you can change the default start frame for Fusion compositions in the project settings.

�Legacy Fusion Composition Frame Count: Sets the Fusion composition at zero frames to the first

frame of the source media for the composition.

�Default Start Frame: Lets you type in a default frame number to start your fusion comps in

this project.

�This helps with Visual FX workflows in three ways:

�Matching existing keyframes to the right frame offsets—when replacing an asset with mismatched

frame offsets (e.g., a sub clip, different format or round trip, or VFX connect workflows with

mismatching handles).

�Rendering to specific frame ranges—when aligning to delivery standards for commercial

workflows (e.g., compositions should start at sequence frame 1000).

�Consistent Referenced Comp behavior—essential when applying a referenced composition to

different clips with different trims.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

Fairlight

The Fairlight panel lets you set up your project’s audio sample rate, as well as setting up various

audio-specific tools in the Fairlight page.

Timeline Sample Rate

This setting can only be changed prior to creation of your first timeline. Once one or more timelines

have been created in a project, the Audio Sample Rate is locked to whatever was chosen.

The Audio Sample Rate, measured in kilohertz, is the number of samples per second used for

audio processing in DaVinci Resolve. This setting defaults to 48000 (or 48 kHz), which is typical for

broadcast and cinema work. However, you can change this to 96000 or 192000 if you want to mix and

process audio at higher precision. Be aware that using a higher sample rate, such as 96 kHz instead of

48 kHz, will use twice as much processing power and result in media that’s twice the size.

NOTE: Regardless of the Timeline Sample Rate you select, when you import audio files at

different sample rates, they will be automatically re-sampled to the Timeline Sample Rate so

they play correctly.

Bussing

If you want to work using the previous method of fixed-bus mapping, you can do so for new

projects by opening the Fairlight panel of the Project Settings and turning on the “Use fixed bus

mapping” checkbox.

If your project has fixed busing enabled and you want to change to FlexBus, then uncheck the “Use

fixed bus mapping” checkbox. Note that once you have made the change, it will not allow you to

change it back to legacy busing. The advantages to changing from legacy busing to FlexBus are

enormous, so you will not regret making the change.

Audio Metering

Two options in the General Options of the Project Settings let you customize the Loudness Meters on

the Fairlight page, while the others affect all other audio meters in DaVinci Resolve.

�Meter Type: Lets you select the desired Meter Type.

�Level detector: If the Meter Type is set to Custom, this lets you select Sample Program, VU, or

RMS for audio level metering detection.

�Scale: If the Meter Type is set to Custom, this lets you select either IEC 60268-18 or Quasi Linear

for audio level metering scaling.

�Decay: If the Meter Type is set to Custom, this lets you set the time in seconds for level metering

decay in 20 dB increments, following peak levels registering on the meters.

�Peak Indicator: If the Meter Type is set to Custom, this lets you select the hold time for peak level

indication in the meters.

�Off

�Short hold + fall

�Medium hold + fall

�Medium hold

�Long hold

�Infinite hold

�Pre fader metering on tracks: Lets you choose how meters in the Fairlight page display their

audio analysis. There are two options:


Setup and Workflows | Chapter 6 Project Settings

MEDIA

Post Fader (unchecked): Meters always display the level of each clip’s signal after whatever fader

adjustments have taken place. Fading a track’s level down diminishes the visible level of that

audio signal in the meter. This setting is good if you prefer a visual indication of the relative levels

you’ve set your various audio tracks to, which is a very NLE-oriented behavior.

Pre Fader (checked): Meters always use the volume levels of the audio clips in that track, even if

you’ve lowered the level using the sliders. If you’ve keyframed a clip’s volume, that change will be

reflected by the audio meters, even though fader changes are not. Viewing meters this way means

you can always see how much level is available to clips in your mix, regardless of what the current

fader levels are set to, in the event you want to keep track of audio you want to bring back into the

mix later on. This is a very DAW-oriented behavior.

�Target Loudness level: Lets you set the LUFS value that’s used as a reference level for loudness

metering. Defaults to –23 LUFS, which conveniently makes the display of these meters scale

similarly to traditional audio meters that you’re already used to.

�Loudness Scale: Lets you choose which scale you want to use with which to measure the meters.

Options currently include the default of EBU +9 Scale (–18 to +9), and EBU +18 Scale (–36 to +18).

�Bus Meter Alignment Level: Sets the peak of the bus meter.

�Bus Meter High Level: Sets the dB level at which the meter starts showing red.

�Bus Meter Low Level: Sets the dB level at which the meter starts showing yellow.

Path Mapping

The Path Mapping panel lets you configure your system’s file paths, allowing you to seamlessly link

and share media clips while collaborating with other users on their own systems. For example, Editor

A and Colorist B are collaborating on the same project. Editor A is working on a Mac in L.A., where

Colorist B is working on a PC in Bangkok. They are both sharing media in a cloud service’s folder, but

the file paths to that cloud folder are different for both of them locally.

�The Editor’s Mac folder is at /Users/editor/cloudfolder/Episode 12

�The Colorist’s Windows folder is at D:\Projects\Episodes\cloudfolder\Episode 12

Normally if they were collaborating, each one would constantly have to re-link the files from the

other before they could continue as the path names would not match. By both of them adding the

“Episode 12” location, and mapping their local paths in this section, DaVinci Resolve will automatically

convert the file paths on the fly as they work. There would be no need for re-linking the clips as long

as all the media they used was in the same hierarchy in the Episode 12 folder.

You can use Path Mapping to make things easier for non-collaborative workflows as well. For example,

for a single user on a laptop, they could setup a link from their local media folder to their NAS.

This removes the need to relink the media each time they leave and return to the office.

NOTE: Path Mapping differs from using the older Mapped Mount option in the Media Storage

preferences. Mapped mount requires each user knowing the file path of all the other users.

Path Mapping lets the user just present their own file path, and DaVinci Resolve takes care of

the translation for all the other users instead.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

Project Media Locations

This setting lets you set up your project’s media locations so that they can easily be shared and

translated with other DaVinci Resolve users. The idea is to have a media folder in common with all the

other users (i.e., all connected to the same shared cloud storage folder), and set up the path to your

own individual folder here.

�Location: Shows you the name of the shared folder.

�Local Path: Shows the path to this folder on your filesystem.

�Add: Opens a filesystem dialog to let you select the shared folder.

Once the location is selected, press the Browse button and use the file system to set the local

path to that folder on your computer.

�Remove: Removes a shared folder from the Path Mapping settings. It does not delete the folder

from your system.

�Automatically setup when relinking: With this setting enabled, when relinking offline media,

DaVinci Resolve automatically creates a mapping. It compares the path in the project file and the

user selected path and creates a relative path between the two. It checks if other offline media

in this project is available in those relative paths and relinks them as appropriate. It also does the

same check with proxies in proxy subfolders.

The Path Mapping Project Settings


Setup and Workflows | Chapter 6 Project Settings

MEDIA

Chapter 7

Camera Raw

Settings

This chapter discusses in detail each of the settings available for every camera

raw format that is supported in DaVinci Resolve. These settings are available in

the Camera Raw panel of the Project Settings, via the Inspector in the Media, Cut,

and Edit pages, or in the Camera Raw palette of the Color page.

Contents

Camera Raw Decoding Explained������������������������ 166

Camera Raw Project Settings���������������������������������� 166

Camera Raw Image Inspector���������������������������������� 167

ARRI�������������������������������������������������������������������������������������� 168

Master Settings��������������������������������������������������������������� 168

Project Settings�������������������������������������������������������������� 168

Use Camera Metadata������������������������������������������������� 169

Blackmagic RAW������������������������������������������������������������ 170

BRAW Sidecar Metadata Files���������������������������������� 170

Master Settings���������������������������������������������������������������� 170

Project Settings���������������������������������������������������������������� 171

Use Camera Metadata�������������������������������������������������� 173

Canon RAW����������������������������������������������������������������������� 173

Master Settings���������������������������������������������������������������� 173

Project Settings��������������������������������������������������������������� 174

Use Camera Metadata�������������������������������������������������� 174

CinemaDNG���������������������������������������������������������������������� 175

Master Settings���������������������������������������������������������������� 175

Project Settings��������������������������������������������������������������� 176

Use Camera Metadata�������������������������������������������������� 177

Nikon RAW������������������������������������������������������������������������� 178

Panasonic Varicam RAW������������������������������������������� 180

Master Settings��������������������������������������������������������������� 180

Project Settings�������������������������������������������������������������� 180

Use Camera Metadata�������������������������������������������������� 181

Phantom Cine������������������������������������������������������������������� 181

Master Settings���������������������������������������������������������������� 181

Project Settings��������������������������������������������������������������� 181

RED��������������������������������������������������������������������������������������� 182

Master RED Settings����������������������������������������������������� 182

Master���������������������������������������������������������������������������������� 183

Project Settings�������������������������������������������������������������� 183

Decoder Settings����������������������������������������������������������� 186

Use Camera Metadata�������������������������������������������������� 187

Sony RAW�������������������������������������������������������������������������� 188

Master Settings��������������������������������������������������������������� 188

Project Settings�������������������������������������������������������������� 188

Use Camera Metadata������������������������������������������������� 190


Setup and Workflows | Chapter 7 Camera Raw Settings

MEDIA