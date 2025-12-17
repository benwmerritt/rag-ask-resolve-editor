---
title: "Chapter 195"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 749
---

# Chapter 195

Live Sync

This chapter describes how to edit using the Live Sync feature with

DaVinici Resolve, Blackmagic Cloud and Blackmagic Cameras.

Contents

Live Sync��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4151

Setting Up Live Sync on Blackmagic Cloud Storage��������������������������������������������������������������������������������������������������������� 4151

Setting up Live Sync on Blackmagic Cameras�������������������������������������������������������������������������������������������������������������������� 4152

Setting up Live Sync with the Blackmagic Camera App for iOS and Android������������������������������������������������������ 4152

Logging into Blackmagic Cloud��������������������������������������������������������������������������������������������������������������������������������������������������� 4153

Blackmagic Cloud Projects Panel����������������������������������������������������������������������������������������������������������������������������������������������� 4153

Uploading Clips to a Blackmagic Cloud Project������������������������������������������������������������������������������������������������������������������ 4153

Live Sync������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4154

Clip Upload Status Indicators������������������������������������������������������������������������������������������������������������������������������������������������������� 4154

Live Sync in DaVinci Resolve������������������������������������������������������������������������������������������������������������������������������������������������������� 4155

Setting up a Cloud Project in DaVinci Resolve�������������������������������������������������������������������������������������������������������������������� 4155

Editing Live Sync in DaVinci Resolve���������������������������������������������������������������������������������������������������������������������������������������� 4155


Blackmagic Cloud | Chapter 195 Live Sync

DELIVER

Live Sync

Live Sync allows the near real time editing of camera files as they are being recorded. This has

obvious benefits for time sensitive applications, such as news and live events, however even scripted

drama and documentaries can benefit from editing as you go for quick turnarounds.

Live Sync automatically will start uploading an HD H.265 proxy file, even while the master clip is still

being recorded in the camera. This file is immediately accessible from the Media Pool in DaVinci

Resolve. As the clip continues to be recorded in the camera, the clip continues to grow in the Media

Pool, letting you access future events from the same clip. As each clip finishes, the Media Pool grows

with new proxy clips. Depending on your need, you can export your final project using this proxy

media for immediate delivery or relink your footage to the camera masters later for the highest-

quality output.

Live Sync is an integrated system requiring a Blackmagic Camera, Blackmagic Cloud Storage, and

DaVinci Resolve to work seamlessly. This chapter will explain how to set up these three elements to

work together.

Editing a live clip as it is being recorded in the Cut page. The Blackmagic Cloud Sync Manager is in the lower right.

Setting Up Live Sync on

Blackmagic Cloud Storage

In order to record and edit Live Sync footage, you first need somewhere accessible to both the editor

and the camera operator to store the project and camera files, and that place is Blackmagic Cloud

Storage. At the minimum you will need enough cloud storage space to hold all of the proxy files from

the Blackmagic Camera. If you also wish to upload the camera originals, you will need considerably

more space, depending on the codec the camera is using.

For more information on setting up a Blackmagic Cloud Storage account and purchasing

space, see Chapter 192, “Blackmagic Cloud Storage.”


Blackmagic Cloud | Chapter 195 Live Sync

DELIVER

The Blackmagic Cloud Storage web interface

Once you have your Blackmagic Cloud Storage space and project library set up, after the first clip is

recorded from a Blackmagic Camera, you will see a Camera Uploads folder created. Inside that folder

is a Proxy subfolder (where all the Live Sync proxies will be stored), and a list of currently uploaded

master clips. Having this specific folder helps organize and separate your incoming camera footage

from any other media folders you have in your storage.

NOTE: While you can do simple media management (deleting and organizing clips) in

the Blackmagic Cloud Storage web interface, the media management tools both in the

Blackmagic Camera and DaVinci Resolve are much better suited for this purpose. It’s best to

leave the Cloud Storage simply as a passive sync from these devices.

Setting up Live Sync on

Blackmagic Cameras

Each Blackmagic Camera model will have its own method of uploading clips to the Blackmagic Cloud;

please see your camera’s documentation on the specifics for that model. Below are the instructions for

setting up the Blackmagic Camera app for iOS and Android.

Setting up Live Sync with the

Blackmagic Camera App for iOS and Android

When you sign into Blackmagic Cloud on your Blackmagic Camera app, you can choose to upload

clips directly to a DaVinci Resolve Cloud project or to manually select the clips you want to upload

from your camera’s media pool. Alternatively, clips can also be uploaded straight to your own private

Blackmagic Cloud storage directly, without syncing to a Resolve Cloud project.

You can choose to upload proxy files or both proxy and original files in Settings > Media >

Upload Clips.


Blackmagic Cloud | Chapter 195 Live Sync

DELIVER

Logging into Blackmagic Cloud

To log into your Blackmagic Cloud account:


Go to Settings > Blackmagic Cloud > Log in to Blackmagic Cloud, or tap the

Blackmagic Cloud icon in the upper right of the Media workspace.


Enter your login details, tap ‘login’ and use the touchscreen keyboard to enter

your email address and password.

Once logged in, your Blackmagic Cloud avatar will be displayed in the Media and Chat

workspaces. You can tap your avatar to view your account details or to log out of your account.

Blackmagic Cloud Projects Panel

Tap the sidebar icon at the top left of the Media workspace to open the Blackmagic Cloud

projects panel.

When you are signed into your Blackmagic Cloud account, projects that you can

upload clips to are listed in the ‘Blackmagic Cloud’ section of the Viewer.

Uploading Clips to a Blackmagic Cloud Project

Selecting a Blackmagic Cloud project lets you upload proxy files, or both proxies and originals, as

you record clips to your camera’s media. When a project is selected in the projects panel, a clip

will be immediately uploaded as soon as you stop recording on your phone. This will happen in the

background as you continue recording clips for as long as your phone is connected to the Internet and

logged into your Blackmagic Cloud account.


Blackmagic Cloud | Chapter 195 Live Sync

DELIVER

To upload to a Blackmagic Cloud project:


Tap on a Blackmagic Cloud project to select it.


Tap the the Camera icon to close the Media Pool and return to the HUD.


The name of the selected Blackmagic Cloud project will appear above the timecode display on

your phone’s HUD. The next time you record a clip, your camera will automatically start uploading

media to the selected cloud project.

If your phone’s internet connection is interrupted, the name of the cloud project will be grayed

out and uploads paused. Your camera will automatically restart the uploading process when the

internet connection is restored.

When you have finished recording, tap on the Media icon to open the Media Pool and view

the upload status of your clips.

Your Blackmagic Cloud avatar will remain visible in the menus and you will stay logged in,

even if you have disconnected your phone from the internet. This ensures that any recordings

you have in your project upload queue will resume as soon as possible after connecting your

phone again. Your phone will immediately try to reestablish your internet connection and

resume any uploads it has in its queue.

This also means when you choose to record directly into a project, you can operate in areas

with patchy cellular coverage and not worry about reconnecting to upload as the process

happens automatically. For example, you could record clips in locations where there is no

Internet connection or cellular signal at all, and then simply connect when you are in range or

have a wifi Internet connection and quickly upload your proxies then.

Live Sync

Turn this slider on in the Media Settings to immediately start uploading a proxy file to your Blackmagic

Cloud project as you record a clip. The clip will appear in your DaVinci Resolve Cloud project, and

grows dynamically in the Media Pool as the recording comes in over the internet. This lets the editor

work on the first part of a shot even while it’s still being recorded in real time. The editor can always

return to the same clip again and again for additional material as it grows.

The speed at which the Live Sync clip updates is dependent on the speed of your internet connection.

Clip Upload Status Indicators

When you have chosen to upload clips to a Blackmagic Cloud project, you can check the upload

status by selecting the project from the Blackmagic Cloud projects panel.

Next to the cloud project name, the overall upload status is displayed including number of clips,

completed percentage, upload speed and estimated time remaining.


Blackmagic Cloud | Chapter 195 Live Sync

DELIVER