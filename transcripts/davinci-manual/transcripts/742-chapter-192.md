---
title: "Chapter 192"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 742
---

# Chapter 192

Blackmagic Cloud

Storage

This chapter describes how to set up and use your Blackmagic Cloud Storage.

Contents

Blackmagic Cloud Storage�������������������������������������������������������������������������������������������������������������������������������������������������������������� 4113

Using the Blackmagic Cloud Storage Web App������������������������������������������������������������������������������������������������������������������� 4114

Cloud Folders���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4118

Personal Storage Folders���������������������������������������������������������������������������������������������������������������������������������������������������������������� 4118

Setting up a Blackmagic Cloud Project in DaVinci Resolve����������������������������������������������������������������������������������������� 4119

Blackmagic Cloud Sync Manager����������������������������������������������������������������������������������������������������������������������������������������������� 4121

Automatic Proxy Generation and

Upload to Blackmagic Cloud Storage������������������������������������������������������������������������������������������������������������������������������������� 4122

Cloud Storage Sync Icons�������������������������������������������������������������������������������������������������������������������������������������������������������������� 4122

Sync Specific Media Originals in Proxy Synced Cloud Projects���������������������������������������������������������������������������������� 4123

Import Blackmagic Cloud Shared Folders to the Media Pool�������������������������������������������������������������������������������������� 4124


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER

Blackmagic Cloud Storage

Blackmagic Cloud Storage provides a centralized and secure space online for your media assets and

proxies. How you use this space is up to you, from a multi-user world-wide collaboration session, to a

single user just picking up their laptop and leaving their workstation behind, to simply having a secure

back up of media from an old spinning hard drive. Blackmagic Cloud Storage is completely integrated

into DaVinci Resolve and the existing Blackmagic Cloud service.

All Blackmagic Cloud users, both new and existing, get a limited amount of free storage.

You can log into cloud.blackmagicdesign.com to access this storage, and purchase project libraries

and/or additional storage. User plans and prices are listed there.

The Free Storage can be used to:

•	 Upload camera captures from the Blackmagic Camera app.

•	 Downloads require logging into the Blackmagic Cloud Website,

and manually downloading the clips.

The Paid Storage can be used to:

•	 Sync media and proxies for DaVinci Resolve Cloud collaboration projects.

•	 Remote Camera Collaboration from the Blackmagic Camera app.

•	 Upload camera captures from the Blackmagic Camera app.

The Cloud Storage interface


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER

Using the Blackmagic

Cloud Storage Web App

When you open the cloud storage tab in the Blackmagic cloud website, you are presented with a

media interface that lets you navigate and see clips belonging to specific cloud projects.

The Storage Spaces interface

Selecting Storage Spaces

The left pane shows your Storage Spaces. These are divided into your Cloud folders, Personal

Storage, Project Libraries, and any project libraries Shared With Me from other users. Next to the

storage space selection, there is a sort and search tool that lets you find and arrange your projects by

name. At the bottom, you will find your usage data, showing how much media you’ve used and what

available Cloud Storage space is left.

Storage Space type selection


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER

�All Storage: Shows all available project libraries as well as your personal storage.

�Cloud Folders: Shows media from your shared cloud storage folders, which are shareable but not

attached to any specific project.

�Personal Storage: Shows media from your personal folders, which are not attached to any

specific project.

�Project Libraries: Shows media from your cloud project libraries.

�Shared With Me: Shows media from other user’s cloud project libraries that have been

shared with you.

Using the Cloud Storage Media Interface

Once a Storage Space has been selected, all the media associated with that space will show up in

the Cloud Storage Media interface. From here you can see thumbnails of the clips, access the clip’s

metadata, and download or delete clips.

The Cloud Storage Media interface

At the top of the interface is a toolbar that lets you navigate, sort, and perform delete and

download operations on your clips.


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER

The Media Interface toolbar

�Storage Space Panel: Clicking on this icon toggles the left Storage Spaces panel on or off.

�Navigate Up one Level: Clicking on the “<“ icon navigates you up one level in the file hierarchy.

�Navigate File Hierarchy : Shows the file path inside your project in a drop-down menu, which

allows you to jump directly to specific enclosing folders.

�Search: Lets you search and find clips by file name.

�Sort: Lets you organize clips in the interface based on name, size, modified and created times, and

kind, in either ascending or descending order.

�List View: Shows the clips in List view.

�Thumbnail View: Shows the clips in Thumbnail view.

�New Folder: Creates a new bin in the Project.

�Information: Shows the metadata associated with the clip.

�Option Menu: Shows media operations; currently these are:

Download: Lets you download a selected clip or clips from the cloud storage to your computer.

Delete: Lets you delete folders or clips from a project. You can not undo this operation.

Scrubbing Video Clips

You can hover your pointer over a clip’s thumbnail to scrub the clip back and forth to see its

full range of media. Simply hover over the clip and use your mouse to move the red line back

and forth through the clip.

Hover the pointer over the thumbnail,

then move the mouse left or right to

scrub through the clip

Selecting Multiple Clips

You can select multiple clips for operations in the Media Interface exactly as in

DaVinci Resolve. A blue outline around the selected clips and an on screen notification

at the bottom lets you know which, and how many, clips have been selected.

•	 Selecting a Range of Clips: Shift-click, or click and drag a bounding box

over the clips you want to select.

•	 Selecting Individual Clips: Command-click the clips you want to select.


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER

Viewing Clip Metadata

When the Information icon is selected in the toolbar, a clip’s metadata will be displayed to the right of

the Media Interface. This metadata is viewable, but not modifiable, from the Blackmagic Cloud Storage

web app. To adjust a clip’s metadata, you will need to do it from the File inspector in DaVinci Resolve.

A clip’s metadata is viewable (but not modifiable) by

selecting the Info icon in the Media Interface toolbar.


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER