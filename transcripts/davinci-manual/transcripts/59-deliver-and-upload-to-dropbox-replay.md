---
title: "Deliver and Upload to Dropbox Replay"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 59
---

# Deliver and Upload to Dropbox Replay

A Dropbox Replay preset at the top of the Deliver page’s Render Settings panel lets you render and

upload a program for review. All options in the Render Settings panel update to present suitable

controls for this process.

NOTE: The Dropbox Replay Render settings are separate from the normal Dropbox Render

settings,  and you need to use this specific set of presets to integrate with Dropbox Replay.

The Dropbox Replay Render settings (highlighted).

Note they are different from the normal

Dropbox Render settings to the left.

When you export to Dropbox Replay, the available choices in the Resolution, Format, Video Codec,

and Audio pop-up menus are limited to those that are most suitable for Dropbox Replay. Choose

the desired export options, then click the Add to Render Queue button to add this job to the Render

Queue as you would with any other export. When that job is rendered, it automatically proceeds to

upload to Dropbox Replay, and an upload percentage indicator appears in the job listing to show how

far along this upload is. When it’s finished, the job displays the text “Upload completed.”

The job in the Render Queue shows you the percentage the

file has uploaded, and lets you know when it’s completed.

This upload is done in the background, so you can continue working on other things in DaVinci

Resolve while the file uploads. If you want to see how long the upload will take on any other page,

you can choose Workspace > Background Activity to see the Background Activity window.


Setup and Workflows | Chapter 13 Frame.io and Dropbox Replay Integration

MEDIA

Unlinking a Timeline from Dropbox Replay

If you wish to remove a specific timeline from using Dropbox Relay integration, simply right-click on the

Timeline and select Unlink from Dropbox Media from the contextual menu.

Upload New Versions to Dropbox Replay

DaVinci Resolve supports the versioning functions found in Dropbox Replay. This lets the Replay user

easily comment and switch between different versions of the same clip.

Once the original timeline has been rendered and uploaded to Dropbox using the Replay preset in the

Deliver page, an additional checkbox appears in the preset, called “Upload as new version.” With this

box checked, any subsequent renders of this timeline will automatically be added to the version

stack of the clip in Dropbox Replay. The latest version will always be the default for the clip in the

Replay interface.

Dropbox Replay Comments Sync

with Timeline Markers

When you render a timeline directly to Dropbox Replay, that timeline is automatically linked to

the movie that’s been uploaded to Dropbox Replay, and all comments, and graphical annotations

(drawings and arrows) from reviewers that are added online via the Dropbox Replay interface are

automatically synced to Dropbox markers on your timeline (so long as your computer has an active

internet connection). Dropbox markers are distinct from all other markers and can be independently

shown and hidden or deleted. Drawings and arrows from Dropbox Replay are converted into their

equivalent DaVinci Resolve annotation graphics for visibility in DaVinci Resolve.

Comments and graphical annotations from Dropbox Replay appear as markers

with their corresponding overlays in your DaVinci Resolve timeline.


Setup and Workflows | Chapter 13 Frame.io and Dropbox Replay Integration

MEDIA

Working With Dropbox Markers

Double-clicking any Dropbox marker in the Timeline opens a dialog that lets you send replies to

comments that appear on Dropbox Replay, enabling editors to respond directly to commenters.

The Dropbox Replay comment dialog that

appears when you open a Dropbox marker

You can also place Dropbox markers on the Timeline to have them automatically sync back to

Dropbox Replay, giving you the ability to send your own comments back to commenters (be kind).

If you delete one or more Dropbox markers on the DaVinci Resolve timeline, those markers will also be

deleted in Dropbox Replay. This includes the Mark > Delete All Markers > Dropbox command. This is

not undoable

Dropbox Marker Navigation

You can specifically navigate only the markers created in Dropbox Replay while in the comment dialog

of a Dropbox marker, using the Previous Marker (Shift-UpArrow) and Next Marker (Shift-DownArrow)

commands. This allows you to skip directly from comment to comment in Dropbox Replay without

having to either navigate all markers in-between, or double-click each Dropbox marker individually

to respond.


Setup and Workflows | Chapter 13 Frame.io and Dropbox Replay Integration

MEDIA

Chapter 14

Resolve Live

The Color page has another mode available to aid you in using DaVinci Resolve in

on-set grading workflows. Turning the Resolve Live option on puts DaVinci Resolve

into a live grading mode, in which an incoming video signal from a camera can be

monitored and graded during a shoot.

Contents

More About Resolve Live������������������������������������������������������������������������������������������������������������������������������������������������������������������ 313

Configuring Your System for Resolve Live������������������������������������������������������������������������������������������������������������������������������� 313

Setting up your Camera and Hardware for Resolve Live��������������������������������������������������������������������������������������������������� 313

Setting up DaVinci Resolve for Resolve Live��������������������������������������������������������������������������������������������������������������������������� 314

Grading Live��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 316

Going Live�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 316

Using Freeze�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 317

Using Snapshot��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 317

Resolve Live Audio Monitoring������������������������������������������������������������������������������������������������������������������������������������������������������ 318

Using Resolve Live Grades Later�������������������������������������������������������������������������������������������������������������������������������������������������� 319

Using LUTs in Resolve Live Workflows�������������������������������������������������������������������������������������������������������������������������������������� 319


Setup and Workflows | Chapter 14 Resolve Live

MEDIA

More About Resolve Live

Resolve Live has been designed to let you use all of the features of DaVinci Resolve to grade these

on-set video previews, in the process saving video snapshots that contain a captured image, your

grade, and reference timecode from the camera. The idea is that, using Resolve Live, you can work

with the cinematographer to develop looks and test lighting schemes on the footage being captured

during the shoot, and then later you can use those looks to build dailies, and as a starting point for the

final grade once the edit has been completed.

Additionally, you can use Resolve Live in conjunction with other Color page features such as the

Alpha output to build test composites to check green screen shots, comparing them against imported

background images in order to aid camera positioning and lighting adjustments. The built-in video

scopes can also be used to monitor the signal levels of incoming video. Finally, you can use 1D and

3D LUTs to monitor and grade log-encoded media coming off the camera.

Configuring Your System for Resolve Live

Setting up your Camera and Hardware for Resolve Live

Setting up Resolve Live is straightforward. Whether you’re using a tower workstation or a laptop,

any of the Blackmagic Design DeckLink or UltraStudio video interfaces can be used to connect your

DaVinci Resolve workstation to a camera and external video display. The important thing to keep in

mind is that, if you want to connect to a live incoming signal and output that signal for monitoring at

the same time, you need to either use two separate DeckLink PCIe cards or UltraStudio Thunderbolt

interfaces, or a single DeckLink card/Ultrastudio with multiple separate inputs and outputs on a single

PCIe card/device.

During the shoot, the digital cinema camera in use needs to be connected to your DaVinci Resolve

workstation video input via HD-SDI or HDMI, which must be configured to carry both the video image

and timecode that mirrors the timecode being written to each recorded clip. Most cameras allow

timecode output over HD-SDI and HDMI, and both DeckLink and UltraStudio interfaces can pass

this timecode to DaVinci Resolve. Without a proper timecode reference, you won’t be able to take

the shortcut of automatically syncing your saved Snapshots to recorded camera original media using

ColorTrace, although you can always apply grades manually.

Resolve Live hardware checklist:

•	 Install and update the Blackmagic Design Decklink card or Ultrastudio device you will be

using for live video input in your DaVinci Resolve workstation (see your Blackmagic Design

hardware documentation for specific details).

•	 Connect the video camera’s SDI or HDMI video output to the Blackmagic device’s video

input. Make sure that embedded timecode out of the camera is enabled as well.

•	 Select the appropriate video input for your device in the Blackmagic Desktop Video Setup

application on your computer.


Setup and Workflows | Chapter 14 Resolve Live

MEDIA

Video input options in the Blackmagic Desktop Video Setup

NOTE: the resolution and frame rate that your camera is outputting through

the SDI/HDMI cable.