---
title: "Automatic Cache Deletion"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 40
---

# Automatic Cache Deletion

A User Preference allows you to delete your local cache automatically after a certain number of days

to keep your drive from filling up with older projects.

It is found in DaVinci Resolve > Preferences > User > Cache Management > Delete cache older

than xx days.

Check the box to automatically delete any cache files older than the number of days set in

the field.

You can always manage these files manually from the Playback > Manage Render Cache

menu, but this new preference lets you set and forget a cleanup operation.

Using Proxy Media

DaVinci Resolve includes a Proxy Media workflow to provide a playback optimization option that

makes it easier to exchange projects online, work on projects remotely, and work with external media

asset management systems. It creates a simple and flexible system for editing collaboration that can

be custom configured to your specific requirements.

Creating and Using Proxy Media

Proxy Media is essentially more highly compressed (and potentially lower resolution) versions of your

source media that are linked to your source media in DaVinci Resolve via metadata. This is done in

such a way as to make it easy to switch back and forth between the original and proxy media as your

needs require.

Typically, this lets you use lower bandwidth proxy media for increased real-time effects performance

and full speed playback while editing, while easily reverting back to more bandwidth and processor-

intensive source media for color correction, finishing, and final output. In addition to enabling better

performance, these proxy files are fully portable, which lets you move your whole project easily

from workstation to workstation, and even across the internet, accompanied by much more compact

proxy media.

You set the resolution and format of your proxies in the Optimized Media and Render Cache section of

the Master Settings panel in the Project Settings. There are two settings that control the actual media

files created by the Generate Proxy Media command.

Proxy Media Resolution: Choose “Original” to keep proxies the same resolution as the

source media. If you prefer, reduce the resolution of the proxy media files by choosing Half,

Quarter, Eighth, or Sixteenth to save bandwidth. The “Choose Automatically” option balances

visual quality with efficiency by only reducing the resolution of media files that are larger than

the currently selected Timeline resolution, using whatever reduction ratio best matches the

Timeline resolution.

Proxy Media Format: Lets you choose the specific QuickTime format and codec that the

proxy files will be created with. There are several ProRes and DNxHR varieties to chose

from, as well as H.264 and H.265 options. Which format you chose will be determined by the

bandwidth and quality tradeoffs that you need for a particular project. For example, if you


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

simply want better playback speed from RAW media while preserving image quality, you may

want to pick a high‑quality codec like ProRes 422 HQ, or DNxHR HQX. If your goal is to send

your media across the internet to another editor, you may want to chose a more compressed

format, such as ProRes Proxy, or even H.264 or H.265, to keep file sizes small.

The Proxy Media Resolution and Format settings

To generate proxy media in DaVinci Resolve:


Select all of the clips you wish to generate proxies for in the Media Pool.


Right-Click any selected clip and choose “Generate Proxy Media” from the contextual menu.

DaVinci Resolve will display a progress bar and give you a time estimate for completion as it renders

out your selected clips to the format and codec determined by the Proxy Media Resolution and

Format settings.

NOTE: If your source clip has a separate audio file synced to it in the Media Pool, any proxies

generated from that clip will include the synced audio, but that audio will be embedded in the

video clip instead of being created as a separate file.

Where is Proxy Media Saved?

Proxy media is created in the “Proxy generation location” destination, found in the Working Folders

section of the Master Settings of the Project Settings. The proxies are further organized into subfolders

by original source clip location. It is important to have enough free space on this drive to contain the

proxies. Once created, these proxy files can then be moved to any other drive location on the system,

if you wish, and then re-linked to their source files.

This location can be overridden by adjusting the Proxy Generation Location options in the Media

Storage settings in the DaVinci Resolve Preferences.

Proxy Handling Display

In both the Media Pool and on the Timeline in the lower left corner of a clip, there can be found a

proxy status icon. This icon changes to let you know exactly which type of media DaVinci Resolve is

currently using.

The Proxy Only icon

Purple PXY Only: This icon indicates that only

proxy media is available; the camera original

media is missing.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

The Proxy

Preferred icon

Purple PXY over a White Background: This

icon indicates that both camera originals and

proxy media for this clip exist, and that proxy

media is being used.

The Camera Original

Preferred icon

White HQ over a Purple Background: This

icon indicates that both camera originals and

proxy media for this clip exist, and that original

media is being used.

The Camera Original

Preferred icon

No Icon: No icon means that proxy workflow

has been disabled, and all media is Camera

Original.

You can select which media you prefer to use in the Proxy Handling selector in the top right

of the Viewer. This is a global setting that changes proxy handling for all the viewers across

DaVinci Resolve.

The Proxy Handling Selector in the Viewer

lets you choose which type of media to use.

Creating Proxy Files with the Blackmagic Proxy Generator

The Blackmagic Proxy Generator is a separate program that can automatically generate proxy media

from master video files placed in a watch folder. This is a small, lightweight application that can be left

to run in the background while importing media. This frees up your DaVinci Resolve program to do

more creative tasks while the proxies are generated.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Using Watch Folders

Watch folders are simply specific folders in your OS that are constantly monitored by the Blackmagic

Proxy Generator. When new files are added to the watch folder, the Blackmagic Proxy Generator

is notified, and it automatically transcodes those new files into proxy media, without any additional

human interaction needed. You can have as many different watch folders as you want; the only

requirement is that the storage media the watch folder is on has enough space to hold both the

original media files and the new proxy media.

IMPORTANT: The proxy media is generated inside a subfolder named “Proxy” at the same

level in the file hierarchy as the original media file. This means that if your original media is

all in the same folder, you will have one “Proxy” folder containing all of the proxy clips. If your

original media is all contained in separate folders (i.e., one folder for each video clip), you will

have multiple “Proxy” folders, one inside every clip folder and containing one proxy clip each.

NOTE: You can not name a watch folder “proxy.” That name is reserved for the

Proxy Generator.

To Add a New Watch Folder

You need to create at least one watch folder and can have as many different watch folders as you

need. For example, you could have separate watch folders for each card, or scene, or date, or

whatever makes the most sense for your workflow.


Select the Add button.


Create a new folder, or select an existing folder in the file system window.


Click on the open button.

The new watch folder will appear in the Watch Folders pane of the Blackmagic Proxy Generator and

will display its location and current status.

To Remove an Existing Watch Folder

When you’re finished using a specific watch folder, you can remove it from the Blackmagic Proxy

Generator’s watch list. Removing a folder does not delete it or its files from your drive; it only stops the

Blackmagic Proxy Generator from monitoring it.


Select the watch folder from the Watch Folders list.


Select the Remove button.

If you’ve accidentally removed the wrong watch folder, you can simply add it back again using the

steps above.

Monitoring Watch Folders

You can see the status of all your watch folders in the Watch Folders section of the Blackmagic Proxy

Generator. You can manually change the order that they appear in the list by dragging an entry up or

down in the list. The estimated disk space required for the proxies can be found below, and there are

three columns that contain information about each folder.

�Volume: This is the logical volume (disk, network storage, usb drive, etc.) that the watch folder

is on. This lets you know which physical device needs to be attached to the computer for the

Blackmagic Proxy Generator to function.

�Folder: This is the name of the Watch Folder. It does not show the folder’s path, only the name of

the watch folder itself.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

�Status: This column shows the current status of the files in the watch folder.

Waiting: This folder has clips in it that have not been transcoded yet into proxies. It is waiting

for the Blackmagic Proxy Generator to be started or for a folder ahead of it in the queue

to be finished.

Processing (x/x): This folder has clips that are currently being transcoded. The number to the left

of the slash is the current clip number, the number to the right is the total number of clips to be

transcoded.

Completed: This folder has finished transcoding all proxy files for the media in the folder.

The Watch Folders section of the Blackmagic Proxy Generator

Setting the Proxy Format

You can select the proxy codec you wish to use by selecting the format from this list.

The Proxy Media Format section of the Blackmagic Proxy Generator


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Starting and Stopping the Blackmagic Proxy Generator

Once you’ve set up a watch folder and selected a proxy format, all you need to do is select the Start

button in the Processing pane to automatically transcode and monitor your watch folders. If you want

to stop the process at any time, just select the Stop button. You can also toggle Start/Stop by pressing

the space bar.

The Processing pane of the Blackmagic Proxy Generator

In the Processing pane, you can also see the status of the current job. The pane displays the progress

of the job in terms of number of clips rendered (x of x), a progress bar, and a percentage indicator.

It also displays the name of the current clip, the frames-per-second (fps) that the render is happening

at, and an estimated time left to complete.

Managing Proxies from the Blackmagic Proxy Generator

There are two options to help manage your proxy files once they’ve been created. The Processing

mode must be stopped for them to be available.

Delete Proxies: This option deletes all proxy files (and the Proxy folder) from the

selected watch folders.

Extract Proxies: This option copies all proxy files from the selected watch folders to a new

destination in the file system dialog. This is useful to create a separate proxy-only folder that

you can hand over to another person on a portable hard drive or upload onto cloud storage.

Linking Proxies from the Blackmagic Proxy Generator in DaVinci Resolve

Once your proxies are created they are linked automatically to their original source media in

DaVinci Resolve when you import the original clips in the watch folder into the Media Pool. You can

also link and unlink them manually as explained in the Managing Proxy Media section later in

this chapter.