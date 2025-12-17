---
title: "Resetting Preferences"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 19
---

# Resetting Preferences

Resetting all preferences to their defaults is simple. Click the Option menu at the upper-right corner of

the Preferences window and choose Reset System Preferences.

System

The System pane of the Preferences window consists of a series of panels that configure the computer

and other hardware that comprises your DaVinci Resolve workstation.

Memory and GPU

The top section of this panel provides Memory Configuration options, while the bottom section of this

panel provides controls over how GPU processing is handled.

Memory Configuration

This section has the following preference settings handling memory usage.

System Memory: The total available RAM on your workstation is listed here.

Limit Resolve Memory Usage to: This preference limits the total amount of system memory that

Resolve uses, keeping memory available for other applications. The maximum and default setting

for this preference is 75 percent of your system’s RAM.

Limit Fusion Memory Cache to: Lets you limit how much RAM the playback cache on the Fusion

page is allowed to use. Depending on the length of clips you’re working on in the Fusion page,

the playback cache can occupy a considerable amount of available memory. The amount you

allocate here is taken from the total amount of memory allocated by the “Limit Resolve Memory

Usage to” setting.

GPU Configuration

This section lets you choose how GPU processing should be handled.

Options for configuring the GPUs on your workstation


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

GPU processing mode: Lets you set DaVinci Resolve to use the OpenCL, CUDA, or Metal GPU

computing APIs for doing effects processing. Which is best depends on the GPUs that are

installed in your computer. Most users can leave this set to Auto to let DaVinci Resolve choose

what’s appropriate. Otherwise, here are specific recommendations. If you have a macOS system,

you should use Metal. Linux and Windows users with AMD GPUs should use OpenCL. Linux and

Windows users with Nvidia GPUs should use CUDA, but make sure you have the correct drivers

for your system, and that you have the latest update to CUDA installed. Additionally, when you

manually choose an option from this drop-down menu, the GPU selection mode drop-down

also appears.

Use Apple Neural Engine when possible: Lets you toggle the use of Apple Silicon’s Neural Engine

in compute tasks.

Use neural engine optimization on NVIDIA: Lets you toggle the use of NVIDIA Neural Engine in

compute tasks.

GPU selection mode: Lets you choose between Auto, which lets DaVinci Resolve choose which

of the available GPUs on your computer to use for processing, and Manual, which lets you choose

which GPUs to enable or disable for processing from a list that appears below. This can be useful in

instances where you have multiple GPUs installed on a machine and you want to choose only the

most powerful GPUs for processing. This can also be useful in instances where an external eGPU

is connected to a laptop or all-in-one with a weaker GPU, so you can choose the more powerful

eGPU for processing.

Use Display GPU For Compute: By default, a single GPU system uses the same GPU for the

DaVinci user interface and also for image processing. As greater processing speeds are achievable

with two or more GPUs, if two GPUs are installed for image processing, this checkbox enables the

shared use of the display GPU instead of dedicating it to just the DaVinci user interface. Users of

the non-studio version of DaVinci Resolve are restricted to the use of a single GPU.

GPU selection list: This list only appears when GPU processing mode is set to either OpenCL,

CUDA, or Metal, and when GPU selection mode is set to Manual. A list of every GPU installed in

your computer appears, and you can use checkboxes to the left of each GPU to enable or disable

specific GPUs from being used for processing.

Optimized Viewer Updates: This only appears on multi-GPU macOS and Windows systems or on

single- and multi-GPU Linux systems; enables faster viewer update performance.

Media Storage

This panel lets you define the scratch disk and other media storage locations used by DaVinci

Resolve, as well as proxy locations, and the default cache directories locations to be used when

creating new projects.

Media Storage Locations: This list lets you define the scratch disk of the system. The first volume

in this list is where Gallery stills and cache files are stored, so you want to make sure that you

choose the fastest storage volume to which you have access.

Mapped Mount: This column allows you to specify translatable media path mapping between Mac,

Linux, and Windows file system conventions.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Direct I/O: This option allows DaVinci Resolve to write directly to the drive using the kernel buffers,

bypassing the normal storage cache in RAM. This allows access to the full performance of the drive.

Automatically display attached storage locations: This checkbox lets DaVinci Resolve access

media on all temporarily and permanently mounted volumes, including SATA and eSATA, SAS, USB,

FireWire, Thunderbolt, Gigabit Ethernet (GbE or GigE), Fibre Channel, and otherwise connected

hard drives, without having to add them to this list. This is on by default.

If you’re using the Apple App store version of DaVinci Resolve, turning on “Automatically display

attached local and network storage locations” automatically prompts you via a dialog to add

“Macintosh HD” as a storage location. Clicking Add Location prompts you to select the Macintosh

HD volume with another dialog, and clicking Open then adds that volume to the Media Storage

Volumes list. After you click Save to close the Preference windows, Resolve should now auto‑mount

any volumes attached to your computer in the Media Storage browser of the Media page. Don’t

do this until after you’ve added a fast storage volume to the Media Storage Locations list, because

you don’t want Macintosh HD as the first volume in this list – the very first volume in this list should

always be reserved for your fast scratch volume.

Proxy Generation Location: These options let you define where any proxy media you create

will be rendered to.

�Proxy subfolders in media file locations: The proxy media is generated inside a subfolder

named “Proxy” at the same level in the file hierarchy as the original media file. This means that

if your original media is all in the same folder, you will have one “Proxy” folder containing all of

the proxy clips. If your original media is all contained in separate folders (i.e., one folder for each

video clip), you will have multiple “Proxy” folders, one inside every clip folder and containing

one proxy clip each.

�Use project settings: Uses the “Proxy generation location” destination, found in the Working

Folders section of the Master Settings of the Project Settings.

�Ask when creating: Opens a filesystem dialog, allowing you to select a specific folder for the

proxy generation.

Adding Storage Locations Manually

Some versions of DaVinci Resolve do not allow automatic display of attached volumes. In this case,

you can right-click anywhere in the background of the Media Storage panel’s volumes list on the

Media page and choose “Add New Location” to open a dialog you can use to choose a volume you

want to add.

Manually adding a volume to the

Media Storage panel’s volumes list


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Using Path Mapping to Access Volumes From Other Operating Systems

Shared media path mapping support for Mac, Linux and Windows makes it easier for multi-system

shops to share Resolve projects among different platforms that use different file path conventions.

To add a mapped mount string:


Open the Media Storage panel of the Resolve Preferences window.


Add the volume you want to map to the Scratch Disks list.


Double-click the Mapped Mount column of the drive you added to edit it.


Enter the alternate file path you want that volume to have. For example, if you’re on a Windows

workstation and you want to access a Linux volume, type the Linux file path into the Mapped

Mount column.

NOTE: If the volume you’ve selected to use for the cache becomes unavailable,

DaVinci Resolve will warn you with a dialog.

Decode Options

This panel contains all options available for using the GPU to accelerate the decoding and debayering

of various formats.

Use GPU for Blackmagic RAW decode: Lets you use your GPU to accelerate the decoding of

Blackmagic RAW (BRAW) media.

Decode H.264/HEVC using hardware acceleration: Allows the use of hardware acceleration for

H.264 or HEVC playback, if available on the computer you’re using.

Use easyDCP decoder: Since DaVinci Resolve has its own DCP encoder and decoder built in, this

checkbox lets you switch over to using easyDCP to do DCP decoding, if you have a license installed

on your workstation.

Automatically refresh growing files in the media pool: If you’re using a third-party application that

records live to a growing video file, you can now begin to edit that file while it’s still recording. Simply

import the growing file into the Media Pool, and when this box is checked, DaVinci Resolve will

continuously refresh to determine if the file has changed, and automatically update its attributes in the

Media Pool.

Stream files during download from Blackmagic Cloud: Check this box to be able to use a clip via

streaming, before it downloads completely from the Blackmagic Cloud.

Use GPU for RED Debayer: Lets you use your GPU to accelerate debayering of R3D media.

The latest RED API enables accelerated 8K debayering using either Metal or Cuda.

There are three options:

�None

�Debayer

�Decompression and Debayer


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Video & Audio I/O

The preferences in this panel let you choose video and audio interfaces on your workstation.

Video I/O

This section lets you choose which Blackmagic Design video interfaces you want to use for

monitoring, capture, playback, and Resolve Live, assuming you have any connected to your

workstation. If you have more than one Blackmagic Design video device connected to your computer,

you can independently configure them for playback and capture. If no interfaces are connected, no

options will be available.

�Capture Device: If you have a compatible video capture card for video input, you should choose

from the card options that appear here. This setting also sets the selected input device for use

in Resolve Live, allowing you to monitor and color correct a live video signal. Any changes to this

setting require a restart of the program.

�Monitor Device: If you have a compatible video output card, you should choose from the card

options that appear here. Leaving this set to “None” disables external video output. Disabling

video output can improve real time performance when external monitoring and output is not a

priority. You can also choose “None” when you’re using DaVInci Resolve with another application

open at the same time that’s using your workstation’s video output interface. When you’ve quit

the other application, you can reselect the video output interface for use by DaVinci Resolve. Any

changes to this setting require a restart of the program.

�Release video device when not in focus: When turned on, DaVinci Resolve releases control of the

video output device whenever you switch to another application.

�Audio monitoring delay: Allows you to adjust any latency between the video images and

the audio monitoring.

Video input/output options in the System Preferences

Audio I/O

This section lets you define the audio hardware and different sets of speakers with which to monitor

audio playback. To access more than the default stereo system output that most workstations default

to, you must use whatever software is available for your operating system to choose the desired audio

hardware you want to use, and define how many audio outputs are required for the type of monitoring

you want to do (stereo, immersive, and so on). For example, on macOS you’ll use the Audio Midi

Setup utility to choose output hardware and select a speaker configuration to be made available on

your system.

�I/O Engine: Lets you choose the audio hardware that DaVinci Resolve uses to process

audio. Choices include System Audio, Desktop Video, Fairlight Audio Accelerator, and ASIO

(Windows only).

�System Audio:  System Audio interfaces with your computer’s native audio hardware and enables

the following parameters.

Playback processing buffer size: Lets you determine the size of the Playback buffer; to the right a

latency display indicates the approximate latency of your choice in milliseconds.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Record buffer size: Lets you determine the size of the Record buffer; to the right a latency display

indicates the approximate latency of your choice in milliseconds.

Input Device: Lets you chose the audio input device from the hardware attached to your system.

Output Device: Lets you chose the audio output device from the hardware attached

to your system.

Automatic speaker configuration: Checking this box sets DaVinci Resolve to output audio via

your workstation’s built-in audio output, even if a compatible video I/O interface is enabled for

capture and playback or for Resolve Live. Unchecking this box exposes additional controls with

which you can define your own speaker setup.

Assigning different audio I/O devices and required buffer adjustments

About Audio Monitoring and Audio Input

The audio processing throughout DaVinci Resolve, including on the Fairlight page and

audio processing using Fairlight FX plugins, is equally compatible with all platforms that

DaVinci Resolve runs on, including macOS, Windows, and Linux. In particular, DaVinci

Resolve supports audio monitoring and audio input using (i) the audio of a supported

Blackmagic Design I/O device such as an UltraStudio or Decklink, (ii) your macOS, Windows,

or Linux workstation’s on‑board audio, (iii) any Core Audio-compatible, Windows-compatible,

ASIO, or Advanced Linux Sound Architecture (ALSA)-supported third party audio interface.

Alternately, you can monitor audio with the optional Fairlight Audio Accelerator, which is a

PCI card that’s designed to handle even more channels of audio I/O monitoring and recording,

and that’s also capable of accelerating audio processing operations to provide better

performance for audio operations.

NOTE: ASIO is a trademark and software of Steinberg Media Technologies GmbH.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Monitor Speaker Configuration

When the Automatic Speaker Configuration box is unchecked it reveals another panel in the Video

and Audio I/O Preferences. Here you can assign your monitors to the default Main or Near sets, and

you can also create an additional 15 monitor sets specific to your needs.

�Monitor Set: Choose the default Main or Near or create up to 15 other

user-definable configurations.

�Rename: This button allows you to rename any of the monitor sets to something more

meaningful for your individual needs.

�Format: A drop-down menu allows you to choose the desired format type from Mono up to

Dolby Atmos 9.1.6. Below the Format type there are three windows to create the Monitor Set:

Layout: Breaks out the channels that correspond to the chosen format.

Output: Where you can assign the Output channels to your system.

Trim: Where you can reduce each individual level by up to -24dB of gain or add up to +10dB

of gain for fine tuning the speaker calibration required for your particular playback space.

Monitor System External Inputs

You can create multiple sets of monitoring with up to 16 user-definable setups from this panel. This

allows flexibility to have different combinations of monitoring speakers that you can switch among for

checking, reviewing, and creating different mixes.

�External Monitor Source:  Chose None or up to 16 definable configurations.

�Rename: Lets you specify a name for an External Monitor Source.

�Format: When a Format is chosen, a drop-down menu appears allowing you to choose the

desired format type from Mono up to Dolby Atmos 9.1.6. Once a format has been chosen, three

more windows appear:

Layout: Which breaks out the channels that correspond to the chosen format.

Source: Where you can assign either Input Destination or Audio Repro.

Input: Where you can assign an individual track when in Audio Repro, or assign the

specific channel when in Input Destination.

�Rename: This button allows you to rename any of the numerically labeled monitor sets to

something more meaningful for your individual needs.

Patching and renaming different external inputs in Video and Audio I/O Preferences


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Immersive Audio Controls

These two Preference panels allow you to configure for the type of immersive audio that you want to

have available in your project and also for linking to a Dolby RMU for doing Dolby Atmos mixing.

�Immersive Audio: This panel allows you to enable the various types of immersive audio

offered within DaVinci Resolve. Those formats are: Ambisonics, Audio Vivid, Auro 3D, BS.2051,

Dolby Atmos, MPEG-H Audio, 22.2 Surround, SMPTE ST 2098, and 360 Reality Audio.

Immersive Audio Preferences

�Dolby Atmos: Checking this box allows the use of an external Dolby Atmos renderer.

Once checked you can enter the IP address of the RMU and choose the base audio output.

Dolby Atmos Preferences