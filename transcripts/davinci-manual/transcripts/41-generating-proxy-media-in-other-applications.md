---
title: "Generating Proxy Media in Other Applications"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 41
---

# Generating Proxy Media in Other Applications

Proxy files can also be generated in applications outside of DaVinci Resolve, such as other NLEs or

various media asset management systems. To properly link the proxy to its source media in DaVinci

Resolve, the proxy file must meet the following criteria:

�Proxy files must have identical timecode to the source file.

�Proxy files must have the same file name as the source file (excluding extensions).

�Proxy files must have the same frame rate as the source file.

�The format and codec used for proxy files must be supported in DaVinci Resolve.

If your proxy file meets these criteria, you’ll be able to manually link proxy media created in other

applications to source clips in the Media Pool as described below.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Managing Proxy Media

You can check the status and location of all your proxy media in the List view of the Media Pool. Right-

click on any column heading and click the checkboxes of “Proxy” and “Proxy Media Path.”

�Proxy: This column shows the current proxy status.

None:  Indicates no proxy media has been created.

Offline: Indicates a proxy has been created but cannot be found in the Proxy Media path.

(Resolution): A number indicating the resolution of the created proxy and that it is online.

�Proxy Media Path: The location of where DaVinci Resolve is looking for the proxy file. If this

location is incorrect, you can relink the proxy to a new path manually.

The proxy columns in List view, showing Proxy Media status and location

Linking Clips to Proxy Media

If you’ve created proxy media in another application, or moved the internally created proxy media out

of its default location in “ProxyMedia,“ you’ll need to manually link the proxies to their source media

files in your Media Pool.

To link proxy media to a source clip:


Select one or more clips in the Media Pool you wish to link proxy media to.


Right-click one of the selected clips, and choose “Link Proxy Media” from the contextual menu.


Use the file browser to find the specific proxy file or directory (in the case of multiple clips) to set a

new Proxy Media path, and click Open. If you select an incorrect file or directory, a warning dialog

box will appear and no linking will occur.


If the linking was successful, the proxy media icon will show up on the clip’s thumbnail in the

Media Pool.

The Proxy Icon showing in

the lower left corner of the

thumbnail, indicating proxy

media is linked for this clip

To unlink proxy media from a source clip:


Select a clip or clips in the Media Pool you wish to unlink proxy media from.


Right-click on any clip and select “Unlink Proxy Media” from the contextual menu. This will remove

the metadata link from proxy to source and will set the status in the Proxy column to “None.”

NOTE: Unlinking a proxy file does not delete it. The proxy file remains on the hard drive

where it was created. As of this writing, proxy files must be deleted manually using your

OS file system outside of DaVinci Resolve.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Re-generating Proxy Media

You can generate more than one proxy file per clip. This can be useful if you want to set multiple

Camera Raw parameters and choose between them, or to create proxy files of different resolutions.

To generate a new proxy:


Make your desired changes to the current clip’s settings.


Right-click on the same clip and select “Generate Proxy Media” from the contextual menu.

A new proxy file is created in the same directory as the previously linked proxy file, and its file name

is appended with “_s00x” to differentiate it. The latest proxy generated is automatically linked to

the source file, but previous proxy versions are retained on disk, so you can then manually relink the

different versions as needed.

Switching Between Proxy Media and Original Media

You can switch between using your original source media and the proxy media for playback in the

Cut page by using the Proxy Handling icon in the Viewer, or in the Edit page, by selecting Playback >

Proxy Handling and selecting one of the following options.

Disable All Proxies: This option disables the proxies altogether and forces the original

media playback only. If the original media is not available, the clip is replaced with a Media

Offline graphic.

Prefer Proxies: This option will use proxy files for playback, and if there is no proxy file for a

clip, the original media will automatically be used instead. If the original media is not available,

the proxies will be used, and the timeline will have a purple line across it for the duration that

the original clips are missing.

Prefer Camera Originals: This option will use the original media files for playback, and if there

is no original media file for a clip, the proxy media will automatically be used instead, and the

timeline will have a purple line across it for the duration that the original clips are missing.

TIP: Regardless of the proxy mode, a purple line on your timeline indicates the original media

is missing and gives you a visual indicator to help identify those missing clips.

Using Proxy Files for Delivery

By default, the Deliver page always reverts proxies to the original source media for final output to

ensure the highest quality render. Checking the “Use proxy media” box in the Advanced Settings of

the Video Render settings in the Deliver page overrides this so DaVinci Resolve uses proxy media for

final output instead. This can be useful if you need to save rendering time while making dailies, or to

quickly create outputs of your timeline for producers or audio engineers where master quality is not

necessarily needed. You will also need to check the “Use proxy media” box if you are editing with

proxies and do not have access to the original source media.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Moving Proxies Using a DaVinci Resolve Archive (.dra)

When moving proxies from one DaVinci Resolve system to another, it can be time consuming and

problematic to manually copy many individual assets (proxies, graphics, source files, etc.) from different

folders and locations. By far the easiest way to move complete projects from system to system is by

letting DaVinci Resolve do all that file management for you, by creating a DaVinci Resolve Archive

(.dra). An archive file contains not only your project, but all its media as well, maintaining the file paths

and organization of the original project.

To create a DaVinci Resolve Archive file, right-click on any project in the Project Manager, and choose

“Export Project Archive” from the drop-down menu. Within this mechanism, a new Archive setting in

DaVinci Resolve makes working with proxies simple and elegant.

Creating a Proxy-Only Archive to Share

In the Archive Options dialog, if you check Proxy Media, and uncheck Media Files and Render Cache,

DaVinci Resolve will make an Archive using only the proxy media. This allows you to create a compact

and easily transported version of your project to either move to another computer, or to give to an

editor working remotely. If proxy media is not available for a clip (say a graphic or a media file you

didn’t create a proxy for in the first place), the original media is automatically exported to ensure that

nothing goes offline.

Archive Setting options for exporting only Proxy Media

The resulting .dra is a folder that is a fully self-contained version of your project and proxy media.

This folder can easily be moved from drive to drive, or zipped up and sent across the internet.

Working Remotely Using Proxy Media

The proxy workflow in DaVinci Resolve opens up many new possibilities for editing collaboration and

media management. For example, one common workflow is to use the RAW camera master source

clips in the editing suite but to then generate low resolution proxies to take home to edit on a laptop.

To create a portable set of proxies for editing on a laptop:


Set up the Resolution and Format settings for the proxies in the Project Settings. In this case, you

may want to use “Choose Automatically” and a low-bandwidth, easily editable codec like ProRes

LT or DNxHR LB.


Select all source media in the Media Pool and Generate Proxy.


Export a DaVinci Resolve Archive (.dra) onto an external drive, with only Proxy Media checked.


Go away. Once at home, connect that drive to your home laptop, and use the Restore Project

Archive command in the Project Manager to import the archive.


When you’ve finished working at home, export a timeline, bin, or project from your laptop when

finished, and bring just that file back into the edit suite to continue working with the original

source media.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Another common scenario might involve sending proxies over the internet to an editor in

another city or country.

To send a project to another editor over the internet:


Set up the Resolution and Format settings for the proxies in the Project Settings. In this case,

you may want to use a low resolution like “quarter” or “one-eighth,” and a low-bandwidth,

highly‑compressed codec like H.265 for the smallest file sizes possible.


Select all of the source media in the Media Pool and Generate Proxy.


Export a DaVinci Resolve Archive (.dra), with only Proxy Media checked.


Using the file compression tools in your OS, zip the archive folder so it becomes one large file.


Upload the resulting .zip to the online file sharing service you prefer, and send the download link

to the remote editor.


Once the other editor unzips and imports the archive, you and they can then simply send

timelines, bins, and/or project files back and forth to collaborate. These files are small enough to

transfer over email or an instant messaging service.

Additionally, you may have your editing computer connected via ethernet to a Media Asset

Management system that can create its own proxies. In order to edit smoothly via the network, you

need to use low bandwidth proxies instead of the source media.

To create proxy media externally to edit over a local network:


Import the original source media files to your Media Pool from the network storage system

you’re using.


Set up the proxy generation settings in your Media Asset Management software to accommodate

the amount of network bandwidth you expect to have access to.


Make sure the timecode and frame rate of the proxies match the original source media, and render

the proxies to a network location.


Select all of your original source media in the Media Pool, and choose  “Link Proxy Media.”


Choose the proxy media at the network location where they’ve been rendered.

Proxy Media vs. Other Playback

Optimizations in DaVinci Resolve

There continue to be other methods of optimizing real time performance in DaVinci Resolve, so it’s

natural that one might wonder how this is different from Optimized media, Timeline Proxy Mode, and

other performance optimization techniques available in DaVinci Resolve. The key aspect of proxy

media that differentiates it is that proxy media is independent, portable, and can be created by

applications outside of DaVinci Resolve, if desired.

Proxy Media vs. Timeline Proxy Mode

One of the oldest performance optimization options, originally named “Proxy Mode” in previous

versions of DaVinci Resolve, has been renamed “Timeline Proxy Mode” in DaVinci Resolve 17 to

differentiate it from Proxy Media. While the new Proxy Media feature creates actual media files on disk,

“Timeline Proxy Mode” simply reduces the resolution of the timeline on-the-fly, allowing for increased

real time playback performance. To be clear, Proxy Media and Timeline Proxy Mode are two entirely

different features, which are wholly independent of one another.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Proxy Media vs. the Render Cache

Proxy Media is designed to create easy-to-edit primary source material on the Timeline, for improved

performance before you start editing. The Render Cache is designed to improve the real time

performance of clips that have enough computationally intensive effects (such as Resolve FX, color

corrections, noise reduction, compound clips, fusion compositions, etc.) to slow playback, even at the

current Timeline resolution. Proxy Media is independent and portable (you can move clips wherever

you want; you just have to relink them afterward), while the Render Cache media is not designed to be

moved or interacted with externally and only works with the project it was made for.

Proxy Media vs. Optimized Media

On the surface, Proxy Media and Optimized Media appear similar in function. Both options are

designed to create lower bandwidth, easier to edit versions of source media. However, Optimized

Media is managed internally by DaVinci Resolve, cannot be exported, and is not user accessible.

In contrast, Proxy Media creates fully portable and independent media that can be easily managed

by the user.