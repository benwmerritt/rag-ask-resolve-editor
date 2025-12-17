---
title: "Going Immediately to a File System"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 77
---

# Going Immediately to a File System

Location in the Media Browser

Conversely, if you drag a folder from the macOS Finder into the Media Storage panel, the Media

Storage panel will immediately update to show the location of that folder.

Tracking Media Usage

As clips are added to timelines, two mechanisms come into play for keeping track of which clips are

used in which timelines.

Thumbnail Clip Usage Indicators

Whenever you open a timeline, all thumbnails in the Media Pool automatically update to show

highlighted usage bars to let you know which parts of that clip are used in that timeline.

Two colored highlights at the bottom of the

thumbnail indicate which parts of a clip are

used by the currently open timeline

If you right-click on a thumbnail that shows usage, a Usage submenu shows you a list of each

instance of that clip in the currently open timeline. Choosing an instance from this list jumps

the playhead to that clip in the Timeline.

List View Clip Usage Column

Exposing the Usage column when the Media Pool is in List view lets you see a value for the number of

times a clip appears in the current timeline. This usage column is now automatically updated; no user

intervention is required.

A Usage column shows how many times a

clip is used in a timeline, after analysis.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Updating Clip Usage for all Timelines

You can also see which clips have been used across all the timelines in your project.

From the Media Pool Options menu, select the “Update Usage for Entire Project” option.

The Update Usage dialog

DaVinci Resolve may prompt the user to load all timelines, if necessary, and update usage counts for

Media Pool clips. This can take some time, depending on the complexity and number of timelines you

have in your project.

Once completed, the usage count across all timelines will appear in the Usage column in the List view

of the Media Pool.

NOTE: The Usage column increments for each clip item that appears in the Timeline. This

means that if a clip consists of one video item and one video item linked together, the Usage

column will show the number 2.

Relinking Media Simply

DaVinci Resolve keeps track of the relationship between clips in your project and their corresponding

source media on disk. If, for whatever reason, source media that links to clips in your project becomes

unavailable, DaVinci Resolve has several different methods of relinking those clips in the Media Pool.

This section summarizes the methods of relinking. For more comprehensive information on

conforming projects and relinking media, see Chapter 56, “Conforming and Relinking Clips.”

Relink Media

If DaVinci Resolve fails to find your media, a Relink Media icon in the Cut and Edit page’s Media Pool

will highlight orange.

The Relink Media icon that

appears for unlinked media


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Clicking this icon opens a dialog box showing the volumes that the missing files initially belonged to.

You can then use this information to track down the media on your file system, find that specific hard

drive, or ask a client if they provided you the media from this volume. Clicking the Locate button lets

you re-connect the missing clips to a new file location of your choosing. If the quick search initiated

by the Locate buttons doesn’t find media that you know is there, you can initialize an exhaustive deep

disk search for the media by clicking on the Disk Search button.

The Relink Media dialog showing the volume

names where the missing clips originated

Relink Selected Clips

The easiest method of relinking clips in your project that have gone offline is to use the appropriately

named “Relink selected clips” command. This is the most flexible method of relinking clips in your

project with clips in a file system directory of your choice, using file name and timecode as the primary

criteria for drawing a correspondence between each clip and the corresponding media file on disk.

When you relink clips this way, the original file path in DaVinci Resolve is ignored, so this is a good

command to use to relink to media that’s been reorganized on disk.

To relink selected clips:


Do one of the following:

�Select one or more clips in the Media Pool browser that you want to relink, then right-click

one of the selected clips or the selected bin, and choose “Relink Selected Clips” from

the contextual menu.

�Select a bin in the Media Pool Bin list that contains clips you want to relink, then right-click one

of the selected clips or the selected bin, and choose “Relink Clips for Selected Bin” from the

contextual menu.


When the Relink File dialog opens, choose a directory in which to look for the files you want to

relink to, and click OK. DaVinci Resolve attempts to find every clip with a matching file name in the

subdirectories of the directory you chose, using the original file paths of the clips being relinked to

do this as quickly as possible. By first looking for the clips in the directories they were originally in,

relinking can be quite fast.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA


If there are any clips that couldn’t be found using the method in step 2, you’re prompted with

the option to do a “deep search” by a second dialog. If you click Yes, then DaVinci Resolve will

look for each clip inside every subdirectory of the directory you selected in step 2. This may take

significantly longer, but it should be completely successful so long as the media that’s required is

within the selected directory structure.


If there are still other clips that couldn’t be found, you’re prompted to either choose another

directory altogether to continue searching, or quit.

Change Source Folder

If you’ve used your file system to move media that’s associated with a DaVinci Resolve project, but

you haven’t changed the directory structure with which it’s organized, you can use the Change Source

Folder command to quickly relink selected clips in the Media Pool to the new file path of the media

on disk, using the original file paths as a guide. This is a good relinking method to use, if possible, for

projects on a SAN where you don’t want to risk the excessively long search times that could result

from using the Relink command to examine a nested hierarchy of folders in a more flexible way.

To relink your Media Pool clips to a new location:


Select one or more clips in the Media Pool, then right-click one of the selected clips, and choose

Change Source Folder from the contextual menu. The Relink Media window appears displaying

the original path for the material, with controls for choosing a new directory.


Click the “Browse” button to the right of the Change To field, and then use the file navigation

dialog to find the new location of the media file, select it, and click Open.


If you succeeded in finding the appropriate media file, click Change. Otherwise, click Cancel.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Chapter 19

Using Clip Metadata

DaVinci Resolve has powerful tools for viewing, editing, exporting, and importing

metadata associated with each clip in the Media Pool.

Once your metadata house is in order, you can use this metadata in the Cut, Edit, Color, and Fairlight

pages to find, sort, and organize the clips in your project, so you can work faster.

Contents

Editing Clip Metadata������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 409

Automatically Imported Metadata������������������������������������������������������������������������������������������������������������������������������������������������ 409

Using the Metadata Editor��������������������������������������������������������������������������������������������������������������������������������������������������������������� 409

Editing Keywords������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 411

Editing Metadata Using the File Inspector������������������������������������������������������������������������������������������������������������������������������ 412

Audio Classification for Clips (Studio Version Only)������������������������������������������������������������������������������������������������������������� 413

Face Detection to Generate People Keywords��������������������������������������������������������������������������������������������������������������������� 415

Creating Custom Metadata Groups���������������������������������������������������������������������������������������������������������������������������������������������� 417

Importing and Exporting Media Pool Metadata�������������������������������������������������������������������������������������������������������������������� 418

Different Ways of Using Clip Metadata������������������������������������������������������������������������������������������������������������������������������������ 420

Renaming Clips Using Clip Names���������������������������������������������������������������������������������������������������������������������������������������������� 420

Switching Between File Names and Clip Names������������������������������������������������������������������������������������������������������������������� 421

Using Metadata to Define Clip Names���������������������������������������������������������������������������������������������������������������������������������������� 421


Ingest and Organize Media | Chapter 19 Using Clip Metadata

MEDIA