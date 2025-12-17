---
title: "Sync Media Pool Bins"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 72
---

# Sync Media Pool Bins

with File System Folders

You can sync a Media Pool bin with a folder on your computer’s file system (MacOS, Windows, Linux,

etc.). This allows you to add additional media into a folder on your computer and have it automatically

import to its respective bin in DaVinci Resolve.

To set up a folder with Automatic Syncing:


On the Cut page, use the Import Folder icon on the top menu bar to set up matching folder and

sub folder names.


Right-click on the imported folder and choose ”Automatically Resync Media Files.“

Use the Import Media Folder

icon in the Cut page

Right-click on the bin and select

Automatically Resync Media Files

Newly added clips in this folder will be added automatically to the media bin. This can be useful

when working with cloud-synced media files (as when using DaVinci Resolve’s Replay capabilities),

or any files that may be added to the folder later.

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


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Sync actions will add new clips from sub-folders if the corresponding sub-bins exist. However, newly

created sub-folders without corresponding media bins are not tracked, and new media bins without

the corresponding sub-folders are skipped.

For example, say you were editing a sporting event, and you had a graphics operator creating

animated lower-thirds for each of the players. By creating a common network folder called “CG” and

automatically syncing it in DaVinci Resolve, each time a new lower-third was finished and saved, it

would automatically appear in your bin in the Media Pool ready for use.

Here’s how you would set this up:

•	 Create a folder on your network storage called “CG.” Both the editor and the graphics

operator need to have access to this folder.

•	 Note that because this folder is currently empty, it can not be used in a Resync action yet.

Only after there is at least one media file in the folder can you perform a Resync.

•	 The graphics operator finishes his first animated lower third and saves it to the “CG”

folder as a .mov file (though any DaVinci Resolve readable media format would work).

•	 The editor then imports the “CG” folder into the Media Pool in DaVinci Resolve and selects

Automatically Resync Media Files from the context menu.

•	 As the graphics operator finishes and saves additional lower thirds into that folder, they

automatically appear in the Editor’s “CG” bin in the Media Pool, without having to specifically

import them.

•	 For organizational purposes, the graphics operator then creates a new folder in “CG” for

the other team, called “Team B.” Unfortunately, because this folder structure was not in

the original imported bin, it does not show up in the editor’s media pool. However, if they

had created this Team B folder before the editor imported it, and it had media in it, it would

been there.

•	 Now in this case, the editor simply imports the same bin again, selects Automatically Resync

Media Files, and the new folder and all its media appear as expected. Any further files in

dropped in “Team B” will show up in the editor’s media pool.

IMPORTANT: Media entries for clips that are removed or not found on the file system are

set as offline media. This allows for retention of metadata and is useful when the clip path is

temporarily offline, on cloud storage where file status may be in flux, or moved away by apps

or workflows seeking to write a new version in its place.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Adding Media to the Cut, Edit,

Fusion, and Fairlight Pages

While adding clips to the Media Pool in the Media page provides the most organizational flexibility and

features, if you find yourself in the Cut, Edit, Fusion, or Fairlight page and you need to quickly import a

few clips for immediate use, you can do so in a couple of different ways.

To add media by dragging one or more clips from the Finder to the Media Pool (macOS only):


Select one or more clips in the Finder.


Drag those clips into the Media Pool of DaVinci Resolve, or to a bin in the Bin list.

Those clips are added to the Media Pool of your project.

To use the Import Media command in the Media Pool:


Right-click anywhere in the Media Pool, and choose Import Media.


Use the Import dialog to select one or more clips to import, and click Open.

Those clips are added to the Media Pool of your project.

Removing Media From the Media Pool

If you’ve added clips to the Media Pool that you need to eliminate, this is easy to do, either singly, or in

the aggregate.

To remove clips from the Media Pool, do one of the following:

�Select one or more clips in the Media Pool, then press the Delete or Backspace key.

�Select one or more clips in the Media Pool, right-click one of the selected clips, and then choose

Remove Selected Clips.

�Right-click anywhere in the Media Pool, and choose Remove All Clips in Bin.

NOTE: If you’ve turned on “Automatically match master timeline with media pool” in the

General Options panel of the Project Settings, you cannot remove all clips from the Media

Pool if there are other timelines using that media.

To remove clips from the Master Timeline (if it’s exposed):

�Open the Edit page, then select one or more clips in the Media Pool, right-click one of the

selected clips, and choose “Remove Selected Clips from Master Timeline.”

For more information about using the Master Timeline, see Chapter 33, “Using the Edit Page.”


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Removing Unused Media from a Project

You can have DaVinci Resolve automatically remove any unused media clips from the Media Pool in

preparation for archiving or handing off a clean project to another workstation. This action loads all

timelines, compound clips, and Fusion compositions then analyzes them for media usage. Any clips

not found during this analysis are removed from the Media Pool. This option does not delete any clips

from your disk, it only removes them from the Media Pool and the Project. This operation is un-doable.

Depending on the size of the Project, this operation can take several minutes.

To remove unused media from a Project:


Click on the Media Pool Option (3-dot) menu.


Select Remove Unused Clips from the drop-down menu.


Click on the Load All Timelines button to start the operation, or Cancel to abort it.

Select Remove Unused Clips from the Media Pool Option menu

Click the Load All Timelines button to start the analysis

Adding and Removing External Mattes

If you’ve been provided with matte files to accompany one or more media files used by a program

you’re grading, you can attach them directly to specific clips in the Media Pool, in order to use them as

key sources for a Clip Grade in the Node Editor of the Color page. You can even use matte files that

pack multiple mattes within a single piece of media. This can be done by either writing different mattes

to each of the red, green, and blue channels of a clip, or by embedding multiple matte passes within a

single OpenEXR file.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Matching RGB and Matte images

When the Media Pool is in Icon view, clips with clip mattes appear with a badge.

A clip matte, seen in Icon view

Clip mattes appear listed underneath a clip in the Media Pool when it’s in List view.

A clip matte, seen in List view

Alternately, you can add a timeline matte to the Media Pool, which isn’t attached to any clip,

that can be used as a key source in the Color page within any clip’s Clip grade, or within a

Timeline Grade. Timeline mattes appear as stand-alone clips in the Media Pool.

A timeline matte,

seen in Thumbnail view


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA