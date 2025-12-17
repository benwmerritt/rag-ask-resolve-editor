---
title: "Import Blackmagic Cloud"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 744
---

# Import Blackmagic Cloud

Shared Folders to the Media Pool

You can now import and sync Blackmagic Cloud Folders into the Media Pool. This allows you to

connect to one or more cloud media folders and selectively download media from them to your

local machine. Blackmagic Cloud Folders are online common storage folders that are not tied to a

specific project. This lets you create a pool of commonly used media assets, such as title sequences,

credits, bumpers etc., and share them online without having to import them separately into each

individual project.

The Import Cloud Folder icon at the top of the Media Pool

To link a Blackmagic Cloud Folder to your project:


Sign into your Blackmagic Cloud account in DaVinci Resolve.


Click on the Import Blackmagic Cloud Folder icon at the top of the Media Pool in any page.


In the Blackmagic Cloud Folder dialog, click select to choose a Blackmagic Cloud Folder. The

choices here will show any Blackmagic Cloud Folder that you have created, or someone else has

shared with you. Click the Add button.


In the Download Folder Location, select a file location on your local system that you want the

media from the Blackmagic Cloud Folder to be stored in.


Choose whether you want to sync proxies only, or proxies and used originals.


Press Download to add the Cloud Folder to your Media Pool.

The Blackmagic Cloud Folder link dialog


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER

When you open the Blackmagic Cloud Folder in the Media Pool, it will be empty, and populate

one clip at a time as their clip names (not their media) are downloaded from the cloud. Also the

Blackmagic Cloud Folder is not actually linked to your project yet; it is only linked when the

first media clip is “used.”

A “used” clip is new terminology in DaVinci Resolve, and simply means a clip that has been

altered in any way inside the project. A clip can be used be by putting it on a timeline certainly,

but also includes other actions like applying a flag, altering its metadata, transcribing it, etc.

Once a clip is used, its media will start to download to your local machine. Clips that are used

are denoted by a red dot next to them in the Media Pool. Any unused clips will remain as

virtual clips in the Cloud Folder until used. Once downloaded, clips in Cloud Folders can be

used just like any other clip in the Media Pool.

The Cloud Folder linked in List view. Clips with red dots are “used,” and the original media has been down-

loaded. Unused clips have just their proxies available to view. The Cloud Sync column shows that the media is

registered and synced with the Blackmagic Cloud.


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER

Chapter 193

Blackmagic

Cloud Presentations

This chapter describes how to use the Presentations application in the Blackmagic

Cloud, allowing you to setup review and collaboration sessions online with people

from around the world.

Contents

Blackmagic Presentations�������������������������������������������������������������������������������������������������������������������������������������������������������������� 4127

Creating and Managing Presentations����������������������������������������������������������������������������������������������������������������������������������� 4128

Creating a New Presentation�������������������������������������������������������������������������������������������������������������������������������������������������������� 4128

Sharing a Presentation with Another User����������������������������������������������������������������������������������������������������������������������������� 4129

Enabling and Disabling a Presentation������������������������������������������������������������������������������������������������������������������������������������ 4130

Renaming a Presentation���������������������������������������������������������������������������������������������������������������������������������������������������������������� 4130

Deleting a Presentation��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4131

Leaving a Presentation����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4131

Using Presentations���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4131

Video Conferencing���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4131

Controlling a Clip in the Viewer��������������������������������������������������������������������������������������������������������������������������������������������������� 4132

Using Markers���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4134

Using Chat���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4135

Presentations in DaVinci Resolve���������������������������������������������������������������������������������������������������������������������������������������������� 4136

Sending a Timeline to Presentations���������������������������������������������������������������������������������������������������������������������������������������� 4136

Using Markers Between Presentations and DaVinci Resolve��������������������������������������������������������������������������������������� 4137


Blackmagic Cloud | Chapter 193 Blackmagic Cloud Presentations

DELIVER

Blackmagic Presentations

The Presentations application in Blackmagic Cloud allows real time collaboration and review of

DaVinci Resolve timelines using only an internet browser. Collaboration tools consist of video

conferencing for real time communication, a chat interface for persistent notes and comments, and

markers that sync directly with a DaVinci Resolve timeline. With these tools, you can play back a video

with frame accurate sync for all users, while video conferencing at the same time.

The Blackmagic Presentations application in a web browser

The Presentations application is comprised of three parts. The left column is My Presentations, where

all your different presentations are created, stored, and organized. The center area is the Viewer

that lets you navigate the clip, add markers, and adjust the audio playback. On top of the Viewer is

the Video Conferencing area, allowing you to collaborate in real time with other members. The right

column is divided into three sections: Clips, Markers, and Chat. Clips show all the available clips

to comment and collaborate on. Markers will show a list of markers and comments that sync with

a DaVinci Resolve timeline. Chat opens up a simple chat interface to have a record of your notes

and comments.

NOTE: As of this writing, Presentations is still in beta. As beta software, the features

described below may be changed, redesigned, or removed completely from the final release.


Blackmagic Cloud | Chapter 193 Blackmagic Cloud Presentations

DELIVER

Creating and Managing Presentations

Online collaboration in Presentations is comprised of two parts: first, the Presentation in the

Blackmagic Cloud and secondly, a timeline from a DaVinci Resolve workstation (described below).

This section describes the creation and management of Presentations.

NOTE: Presentations uses a slightly different nomenclature describing clips than DaVinci

Resolve. In Presentations, a “clip” is a DaVinci Resolve “timeline,” and not a clip that you

would find in the Media Pool.

Creating a New Presentation

Each presentation can be thought of like a project in DaVinci Resolve, except that it’s about discussion

rather than post production. Presentations contain multiple “clips” to review and have a variety of

collaboration tools, rather than editing/color/fx/audio tools. While making a new presentation for

each project is perfectly valid, you can also make presentations based off other criteria, like who is

collaborating, a date, or a specific stage of the post production process.

The My Presentations column


Blackmagic Cloud | Chapter 193 Blackmagic Cloud Presentations

DELIVER

To Create a Blackmagic Cloud Presentation


Log into your Blackmagic Cloud account in a web browser at www.blackmagicdesign.com.


Select the Presentations icon in the upper center of the web page.


In the My Presentations column, click on the Add Presentation button in the lower left.


Select a Name for the presentation and click Add.


Click on the Presentation in the My Presentations column to launch it.

If you find you have more presentations than can fit on the screen, the My Presentations column

can be sorted by name and date in ascending or descending order by clicking on the sort icon just

to the right.

The My Presentations column is also searchable by clicking on the magnifying glass to the right

and entering your search terms. Only presentations matching your search terms will be shown.

Until you upload your first clip from a DaVinci Resolve project, the Viewer will show “Upload clips

from DaVinci Resolve to get started.” That process is described below in the “Sending a Timeline

to Presentations” section.