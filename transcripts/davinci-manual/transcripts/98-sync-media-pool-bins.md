---
title: "Sync Media Pool Bins"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 98
---

# Sync Media Pool Bins

with File System Folders

You can now sync a Media Pool bin with a folder on your computer’s file system (MacOS, Windows,

Linux etc.). This allows you to add additional media into a folder on your computer and have it

automatically import to its respective bin in DaVinci Resolve.

To set up a folder with Automatic Syncing:


On the Cut page, use the Import Folder icon on the top menu bar to set up matching folder and

sub folder names.

Use the Import Media Folder icon in the Cut page


Right-click on the imported folder and choose ”Automatically Resync Media Files.“

Right-click on the bin and select Automatically Resync Media Files


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

Newly added clips in this folder will be added automatically to the media bin. This can be useful when

working with cloud-synced media files (as when using DaVinci Resolve’s Replay capabilities), or any

files that may be added to the folder later.

To manually resync the contents of a Media Pool bin once, right-click a bin and choose

”Resync Media Files.”

Right-click on the bin and select Resync Media Files

to perform the sync operation manually.

For both Resync actions, ensure that:

�At least one clip is present in the media bin.

�All existing clips in the media bin share the same file path.

�The media bin name matches the parent folder of the clip paths. You can ensure this is set up

correctly by using “Import Media Folder” in the Cut page, or “Add Folder and SubFolders into

Media Pool (Create Bins)” in the Media page.

Sync actions will add new clips from sub-folders if the corresponding sub-bins exist. However, newly

created sub-folders without corresponding media bins are not tracked, and new media bins without

the corresponding sub-folders are skipped.

For example, say you were editing a sporting event, and you had a graphics operator creating

animated lower-thirds for each of the players. By creating a common network folder called “CG” and

automatically syncing it in DaVinci Resolve, each time a new lower-third was finished and saved, it

would automatically appear in your bin in the Media Pool, ready for use.

Here’s how you would set this up:

•	 Create a folder on your network storage called “CG.” Both the editor and the graphics

operator need to have access to this folder.

•	 Note that because this folder is currently empty, it can not be used in a Resync action yet.

Only after there is at least one media file in the folder can you perform a Resync.

•	 The graphics operator finishes his first animated lower third and saves it to the “CG” folder

as a .mov file (though any DaVinci Resolve readable media format would work).

•	 The editor then imports the “CG” folder into the Media Pool in DaVinci Resolve and selects

Automatically Resync Media Files from the context menu.

•	 As the graphics operator finishes and saves additional lower thirds into that folder, they

automatically appear in the Editor’s “CG” bin in the Media Pool, without having to specifically

import them.

•	 For organizational purposes, the graphics operator then creates a new folder in “CG” for

the other team, called “Team B.” Unfortunately, because this folder structure was not in

the original imported bin, it does not show up in the editor’s media pool. However if they

had created this Team B folder before the editor imported it, and it had media in it, it would

been there.

•	 Now in this case, the editor simply imports the same bin again, selects Automatically Resync

Media Files, and the new folder and all its media appear as expected. Any further files in

dropped in “Team B” will show up in the editor’s media pool.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

IMPORTANT: Media entries for clips that are removed or not found on the file system are

set as offline media. This allows for retention of metadata and is useful when the clip path is

temporarily offline, on cloud storage where file status may be in flux, or moved away by apps

or workflows seeking to write a new version in its place.

Import Blackmagic Cloud Shared

Folders to Media Pool

You can now import and sync Blackmagic Cloud Folders into the Media Pool. This allows you to

connect to one or more cloud media folders and selectively download media from them to your

local machine. Blackmagic Cloud Folders are online common storage folders that are not tied to a

specific project. This lets you create a pool of commonly used media assets, such as title sequences,

credits, bumpers etc, and share them online without having to import them separately into each

individual project.

The Import Cloud Folder icon at the top of the Media Pool

To link a Blackmagic Cloud Folder to your project:


Sign into your Blackmagic Cloud account in DaVinci Resolve.


Click on the Import Blackmagic Cloud Folder icon at the top of the Media Pool in any page.


In the Blackmagic Cloud Folder dialog, click select to choose a Blackmagic Cloud Folder. The

choices here will show any Blackmagic Cloud Folder that you have created or someone else has

shared with you. Click the Add button.


In the Download Folder Location, select a file location on your local system that you want the

media from the Blackmagic Cloud Folder to be stored in.


Choose whether you want to sync proxies only, or proxies and used originals.


Press Download to add the Cloud Folder to your Media Pool.

The Blackmagic Cloud Folder link dialog


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

When you open the Blackmagic Cloud Folder in the Media Pool, it will be empty and populate one

clip at a time as their clip names (not their media) are downloaded from the cloud. Also the Blackmagic

Cloud Folder is not actually linked to your project yet; it is only linked when the first media clip

is “used.”

A “used” clip is new terminology in DaVinci Resolve and simply means a clip that has been altered in

any way inside the project. A clip can be used be by putting it on a timeline certainly, but also includes

other actions like applying a flag, altering its metadata, transcribing it, etc. Once a clip is used, its

media will start to download to your local machine. Clips that are used are denoted by a red dot next

to them in the Media Pool. Any unused clips will remain as virtual clips in the Cloud Folder until used.

Once downloaded, clips in Cloud Folders can be used just like any other clip in the Media Pool.

The Cloud Folder linked in List view. Clips with red dots are “used” and the original media

has been downloaded. Unused clips have just their proxies available to view. The Cloud

Sync column shows that the media is registered and synced with the Blackmagic Cloud.

ATEM Switcher Integration

If you’ve recorded a multi-camera event with the ATEM Mini Pro ISO or ATEM Mini Extreme ISO,

it is possible to move that entire project into DaVinci Resolve. ATEM projects include the master

program clip, as well as each individual camera’s “ISO” (isolated) clips, and each camera angle’s audio

recordings. All transitions, timecode, and camera number metadata are imported, as well as whatever

graphics were stored in the ATEM’s Media Pool. Once the project is loaded, you can seamlessly

continue your multi-camera edit in the Cut page.

This initial live recording coupled with later post-production editing workflow is often referred to

as “Live to Tape.” Live to Tape gives you the all the benefits of the spontaneity, verisimilitude, and

fast turnaround inherent to live production but with the added benefit of being able to later add

and remove sections and adjust the editorial flow of the program. Live to Tape also allows you to

fix simple mistakes, such as choosing a better camera angle, or replacing a title or graphic with an

updated version. Because of this flexibility, Live to Tape is the preferred method of recording almost

all broadcast network game shows, current events shows, and sitcoms. Essentially, any type of multi-

camera production that does not primarily depend on being live in real time for its main purpose (like

news or sports) is shot Live to Tape instead.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

The Live to Tape workflow requires the following elements, all of which are provided by the ATEM Mini

Pro ISO and ATEM Mini Extreme ISO.

�A program master clip that was shot live, including all the mixed camera angles, audio, transitions,

etc. from the beginning of the show until the end, for reference.

�Separate ISO recordings from each camera used to shoot the program master clip. An ISO is an

isolated (ISO) camera recording of the entire show from that camera’s perspective only, from the

beginning to end and without interruption.

�A timeline of the live recorded show that indicates where all the camera angles were switched,

what transitions were used, and what graphics were involved.

Importing ATEM Mini Pro ISO Projects

Importing an ATEM project essentially rebuilds the master program clip as a timeline inside

DaVinci Resolve from the camera ISOs, transitions, and graphics. This new timeline will match the

master program clip in every way, just created from the original source materials rather than as a single

compressed video file.

Refer to your ATEM’s specific documentation for how to set up ISO recording, but one important

setting is to make sure that you’ve checked the “ISO Record All Inputs” setting in the ATEM software

control before you start shooting.

To import an ATEM Mini Pro ISO Project:


(Before you shoot) Check the “ISO Record All Inputs” setting in the ATEM software control.


At this point, record your show using the ATEM device, and note the project’s folder location.


Select File > Import Project.


Select the DaVinci Resolve Project file (.drp) in the ATEM project folder, in the file browser.


Click on the Open button.

An ATEM Mini Pro project opened in the Cut page Sync bin


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT