---
title: "Creating Busses"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 673
---

# Creating Busses

Choosing Fairlight > Bus Format opens the Bus Format window, which lets you create the busses you

need (up to the limitations of your system) to organize the tracks and channels of your program.

The depth of options in the FlexBus system

The Bus list lets you rename the bus, choose the format of each bus (a dropdown menu appears in the

Format column of each entry of the list), shows the number of channels associated with a bus, and lets

you color-code each bus (a Color dropdown lets you choose that bus’s color). Simply click any item on

the Bus list to select it, and choose different options from the Format and Color dropdown menus, or

click on the Name of any bus to select it, and type a custom name.

At the bottom of the list are three buttons that let you Add Bus, Duplicate, or Remove selected busses.

When you’re done modifying the available busses, you can click OK to accept the changes and close

the Bus Format window, or Cancel to close the window without any changes (although all pre-existing

busses remain in place). The bottom button row also has a Used tally of what has been used and what

is available for your workstation.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

Immersive Formats (Studio Version Only)

To turn on the immersive formats, go to Preferences > Video and Audio I/O > System Panel >

Immersive Audio, and choose from among the appropriate options. Once enabled, the various

immersive bus formats are available in the Bus Format panel’s Bus list.

The legacy Bus Format window lets you add busses to the mixer.

The Video and Audio I/O panel lets you enable or disable Immersive Audio options.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

Legacy Fixed Bussing

Working with the FlexBus topology is highly recommended for its flexibility. In addition, some newer

features are only available using FlexBus. At some point, however, you may need to work with legacy

Fixed Bussing in a new project. To use Fixed Bussing in a newly-created project, prior to adding any

timeline, open Project Settings > Fairlight, and under the Bussing heading, check “Use fixed bus

mapping.” Now all bussing is handled with the legacy Fixed Bus topology.

Bus formatting with Fixed Bus

The legacy Bus Format window has four buttons that let you create the various Fixed Bus types.

Creating a new bus, whether it’s a Main, Sub, Aux, or Multi Track, adds the new bus to the list that

appears beneath.

The legacy Bus list works the same as the FlexBus list with choices for rename, format, color code, and

so on, and buttons that let you Duplicate or Remove selected busses.

When you’re done modifying the available busses, you can click OK to accept the changes and close

the Bus Format window, or Cancel to close the window (although any busses you’ve made remain

in place). The bottom button row also has a Used tally of what has been used and what is available for

your workstation.

Assigning Busses

Once you’ve created one or more busses, you can assign different tracks to specific busses or

perhaps also busses to busses, busses to tracks, and the final Main bus destinations.

Bus Assignment Using the Mixer

You can easily assign your track(s) to any available busses simply by using the plus (“+”) icon on a

Mixer channel strip:

�Select a mixer channel, and click on the plus (“+”) icon in the Bus Output or Bus Sends section.

�In the dropdown menu, choose the desired destination.

�A rectangle appears with the name of the bus, and the bus is now assigned.

Bus routing dropdown

menu on a channel strip

TIP: You can quickly assign a bus to any selected group of tracks, or to all tracks, by

holding down the Option key (Mac) or the Alt key (Windows) for all selected tracks or

Command‑Option (Mac) or Control-Alt (Windows) for all mixer channel strips prior to

performing the operation. These shortcuts can save a lot of time in your workflow.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

The Bus Assign Window

When you have a lot of busses or tracks to handle, the Bus Assign window lets you to easily manage

connecting to all of them at once. Choose Fairlight > Bus Assign to open the window. Multiple bus

assignments can be created within the dialog; these new assignments will be reflected in the Bus

Outputs section on the channel strips in the Mixer.

The top shows the Send and the Out of each available bus, while the bottom shows a list of all

available tracks and busses to connect to. The Bus Assign window defaults to List view, in which

each bus and track is shown as a list, but by using the icon in the upper right of the window, it can be

switched to Icon view, in which Available Tracks are shown as buttons.

Bus Assign window

Making Bus Assignments

Assigning Using List View

Click a button in the Busses section to select the Send or Out of that bus, and then click on any

destination in the tracks/busses list below, or drag over a group of tracks or busses to assign to all of

them. When assigned, the bus number will appear in the Bus Sends or Bus Outputs column.

�To assign every track, Sub, and Aux to a bus: Click a button in the Busses section to select that

bus, and then click Assign All.

�To clear all track assignments from a particular bus: Click a button in the Busses section to select

that bus, and then click Unassign All.

When you’re done making bus assignments, click the Close button to close the dialog.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

NOTE: While the dialog is open, you can undo any assignments you’ve made, one a time, or

redo them, using Command-Z and Command Shift-Z respectively.

Assigning Using Icon View

�Click a button in the Busses section to select the Send or Out of that bus, and then either click on

a target track button or drag a bounding box over all of the buttons for available tracks that you

want to assign to that bus.

�Once assigned, the Available Tracks buttons display which bus they’ve been assigned to. When

assigned, the Bus number will be followed by an “o” or an “s” to indicate if it’s the send or the out

of that bus.

Assigning multiple tracks to a bus in Icon view by dragging a bounding box

Setting Signal Paths

While bus creation and assignment allows you to submix tracks or route from one bus to another, you

often need to route signals from individual, external sources to a track or bus. For example, if you need

to record audio to a track, you need to patch the audio input on your hardware to the track you want

to record to. Making this type of connection is called “patching” in Fairlight and is accomplished using

the Patch Input/Output window, which is available on the Fairlight, Edit and Deliver pages, providing

patching changes on any of these.

Using the Patch Input/Output Window

Choosing Fairlight > Patch Input/Output opens the Patch Input/Output window, which can be

displayed in either List (default) or Icon view. This window is split into two halves, with the left half

containing whichever Source controls you choose and the right half containing whichever Destinations

you choose.

Creating a Patch

By default, the Patch Input/Output window shows the available Audio Inputs as the Source and

the Track Inputs as the destination. This makes it easy to patch whatever audio source (such as a

microphone connected to a USB audio interface) to a specific audio track of the Timeline to prepare

for recording. Patching and unpatching a source to a destination is straightforward. In the following

screenshot, the Audio 1 Input from an audio interface is highlighted and is being patched to a track

named “Walla.”


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

The Patch Input/Output window showing Source Audio Inputs and Destination Track Inputs

Patching a source to a destination:


Choose a type of source from the Source dropdown menu at the upper left-hand side of the window.


Click the item on the source list (or action button in Icon view) that you want to patch from on the

left side of the Patch Input/Output window.


Choose a destination from the Destination dropdown menu at the upper right-hand side of

the window.


Click the list item (or action button) of the destination you want to patch to on the right side.


Click the Patch button at the bottom right of the window. The source and destination will both

display the connection they’re patched to.

To unpatch a source and destination pair:


Click a list item or action button corresponding to a source or destination you want to unpatch.


Click Unpatch.

Patching in Icon view


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

Choosing Source and Destination Controls

The Audio Source and Destination dropdown menus let you choose different categories of sources

and destinations to patch together.

The following Source options are available:

�Audio Inputs: The available physical audio inputs on your workstation, for example the Fairlight

SX-36 audio interface, MADI, third party interfaces (for example, USB or Thunderbolt), or system

audio. Useful when patching to record audio.

�Bus Out: Any Busses.

�Monitor Direct: Monitor system Direct Out, routed post fold up/down matrix, pre the Monitor

VolumeLevel/Dim/Mute.

�Monitor Out: Monitor system output. Post fold up/down matrix and Monitor

VolumeLevel/Dim/Mute.

�System Generator: Provides various utility sources, including beeps and timecode generation:

OSC: Provides a test oscillator. The oscillator controls appear in a floating window accessed via

Fairlight > Test Tone Settings.

Noise: Uses the Noise generator with choice of white or pink noise, which can be selected via

Fairlight > Test Tone Settings.

Beeps: Refers to beeps generated by operations on the ADR panel, with controls found on

the ADR setup page.

Timecode generator: Generates timecode when enabled and the transport runs, with controls

provided in a floating window accessed via Fairlight > Remote Control Settings.

�Track Direct: Track Direct Out, can be pre or post the track fader, with an offset.

�Track Reproduction: This is the track playback signal, directly from disk, before any processing.

�Dolby Atmos Renderer: The output from the Dolby Atmos Renderer in the currently selected

Atmos output monitoring format. There is also a parallel stereo binaural output to feed

headphones.

The following Destination options are available:

�Audio Outputs: For example, the Fairlight SX-36 audio interface, MADI, third party interfaces

(for example, USB or Thunderbolt), or system audio. Useful when patching to playback audio to

speakers or headphone systems.

�Talk Back: The system for patching the General Purpose Input and General Purpose Output used

for talkback.

�Track Input: The inputs to the available audio tracks in the current timeline, which are the inputs to

the Record and Thru path.

�Dolby Atmos Send: You will need to patch this manually if you are creating original content. If you

import a Dolby Atmos master file, the Send patching for the bed and object tracks will be created

automatically. When an external Dolby RMU renderer is enabled, all sources patched to these

sends will be mirrored on the physical outputs to the external renderer, as defined by the base

audio outputs set in system preferences.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

Legacy Fixed Bus Patching

If you choose to use the legacy Fixed Bussing in the Project Settings, the options

appear a bit differently.

The following Audio Source options are available:

�Audio Inputs: The available physical audio inputs on your workstation, for example SX-36, MADI,

or system audio. Useful when patching to record audio.

�Monitor Direct: Monitor system Direct Out. Post fold up/down matrix, pre the Monitor

VolumeLevel/Dim/Mute.

�Monitor Out: Monitor system output. Post fold up/down matrix and Monitor

VolumeLevel/Dim/Mute.

�Main Direct: Main Bus Direct Out; can be pre or post the Main bus master fader, with an offset.

�Main Out: Main Bus Out; always post the Main bus master fader.

�Main Send: Main bus master insert send.

�System Generator: Provides various utility sources, including beeps and timecode generation:

OSC: Provides a test oscillator. The oscillator controls appear in a floating window accessed via

Fairlight > Test Tone Settings.

Noise: Uses the Noise generator with choice of white or pink noise, which can be selected via

Fairlight > Test Tone Settings.

Beeps: Refers to beeps generated by operations on the ADR panel, with controls found on the

ADR setup page.

Timecode generator: Generates timecode when enabled and the transport runs, with controls

provided in a floating window accessed via Fairlight > Remote Control Settings.

�Track Direct: Track Direct Out; can be pre or post the track fader, with an offset.

�Track Reproduction: This is the signal from the track playback, before any processing.

�Track Send: Track Insert send.

The following Audio Destination options are available:

�Audio Outputs: The available physical audio outputs on your workstation. For example, the

Fairlight SX-36 audio interface, MADI, third party interfaces (for example, USB or Thunderbolt),

or system audio. Useful when patching to play back audio to speakers or headphone systems.

�Main Return: Main Bus master insert return.

�Talk Back: The system for patching the General Purpose Input and General Purpose

Output for talkback.

�Track Input: The inputs to the available audio tracks in the current timeline, which are the inputs to

the Record and Thru path.

�Track Return: Track insert return.

�Dolby Atmos Send: You will need to patch this manually if you are creating original content.

If you import a Dolby Atmos master file, the Send patching for the bed and object tracks will be

created automatically. When an external Dolby RMU renderer is enabled, all sources patched to

these sends will be mirrored on the physical outputs to the external renderer, as defined by the

base audio outputs set in system preferences.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT