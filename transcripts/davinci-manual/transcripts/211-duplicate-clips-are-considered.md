---
title: "Duplicate Clips are Considered"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 211
---

# Duplicate Clips are Considered

Separate Sources

Another thing that’s good to understand is that in DaVinci Resolve, duplicate clips are considered

to be completely separate from the original Media Pool or Timeline clips you duplicated them from.

For example, if you import five clips into Media Pool Bin 1, then edit them into a timeline, and then

drag the five clips you edited into Media Pool Bin 2, the clips in Bin 1 are not intrinsically linked to the

clips in Bin 2.

This means, if you select the clips you originally imported in Bin 1 and choose Unlink Selected Clips,

the instances of those clips that you edited into the timeline will also be unlinked, but the duplicate

clips you created when you dragged the timeline clips into Bin 2 are completely unaffected.

Summary of Methods for

Conforming and Relinking

As a result of timelines and clips being managed separately, there are several ways you can reconform

clips in a timeline to clips in the Media Pool, and clips in general to a project’s corresponding source

media on disk. Which methods will be most valuable depend entirely on the workflow you’re using.

�Conforming clips during XML and AAF import: When you import a project via AAF or XML, you’re

given the option of using the embedded file paths in the AAF or XML file to import all referenced

media into the Media Pool for automatic reconforming to the clips in the imported timeline. If the

media has been moved so that the file paths are invalid, then you’ll be asked to find the location

of the media as part of the import process. You also have the option to ignore the AAF or XML

file’s embedded file paths and instead import another set of media files in a different location (and

perhaps in a different media format altogether) that have the same file names and timecode as the

clips in the AAF or XML file you’re importing.

�Importing clips before importing an EDL, AAF, or XML: In EDL workflows, you must import the

media an EDL will be conformed to into the Media Pool before you import the EDL. However, you

can do this for AAF and XML import workflows as well. When you import clips into the Media Pool

before importing an AAF or XML, DaVinci Resolve is able to automatically reconform the clips in

the imported timeline to those in the Media Pool first, before next looking for media on disk for

clips that could not be found in the Media Pool. This behavior depends on what options you’ve

selected in the Import AAF/EDL/XML dialog.

�Conform missing clips by importing their source media into the Media Pool: As long as the

“Automatically conform missing clips added to Media Pool” setting is enabled in the General

Options panel of the Project Settings, DaVinci Resolve automatically tries to update the conformed

relationship between clips you’re adding to the Media Pool and any missing clips in the various

timelines of your project. This behavior is triggered whenever you add clips to the Media Pool by

importing clips, copying and pasting, or creating duplicates of clips. For example, if a timeline clip

is missing because there is no corresponding clip in the Media Pool, the simple act of importing a

clip with a matching file name and timecode into the Media Pool will automatically reconform the


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

missing timeline clip without you needing to do anything else. Please note, the “Auto conform clips

with media added into Media Pool” setting must be disabled if you use collaborative workflow.

�Using the Import Additional Clips commands: The process of importing media just for missing

clips in a timeline can be automated by right-clicking that timeline in the Media Pool and using

the Timelines > Import > Additional Clips With Loose (or Tight) Filename Match contextual menu

commands, which automatically search the selected directory tree of your file system for media

that matches all of the offline clips in that timeline. The “Loose Filename Match” command ignores

file extensions (letting you conform to alternate media formats), while the “Tight Filename Match”

command requires file extensions to match.

�Reconform online clips by importing new media into the Media Pool: As long as the

“Automatically conform missing clips added to Media Pool” setting is enabled in the General

Options panel of the Project Settings, DaVinci Resolve automatically tries to update the conformed

relationship between clips you’re adding to the Media Pool and any clips in the various timelines

of your project that have their Conform Lock Enabled setting turned off. This behavior is triggered

whenever you add clips to the Media Pool by importing clips, copying and pasting clips, or

creating duplicates of clips.

By default, each clip that’s part of an imported timeline, or that you’ve edited into a brand new

timeline, has Conform Lock Enabled turned on by default (unless the source media goes missing).

Conform Lock Enabled simply means that a particular clip in a timeline is set to only consider

the source clip in the Media Pool to which it’s currently conformed as the correct match; all other

clips in the Media Pool are ignored, even if there are multiple clips with the same file name and

overlapping timecode that would make them also a valid match (such as when you have multiple

copies of the same clip that in different formats, or multiple versions of VFX clips with the same

name and timecode).

If you right-click a clip with multiple potential matches in the Media Pool in the timeline and turn

Conform Lock Enabled off, that clip will display a “clip conflict” error, with an attention badge to the

left of its name in the timeline. Double-clicking that badge reveals a dialog showing you every clip

in the Media Pool with a matching file name or reel name and overlapping timecode, so that you

can choose which Media Pool clip you want to conform that timeline clip to.

NOTE: The “Auto conform clips with media added into Media Pool” setting must be

disabled if you use collaborative workflow.

�Using Conform Lock commands to force a timeline clip to conform itself to a clip

in the Media Pool: A manual command for conforming a selected clip in the timeline with a

selected clip in the Media Pool. Useful when none of the automated methods of conforming work,

for whatever reason.

�Using the Relink command on clips or bins in the Media Pool: If you have a DaVinci Resolve

project in which there are unlinked clips in the Media Pool, that means the relationship between

those clips and their corresponding source media files on disk have been lost. In this case, you

can use the Relink Media, Relink Selected Clips, or Relink Clips in Selected Bins commands to

relink clips to the corresponding source media on whatever storage volume it’s on. In the process,

you’ll automatically relink any instances of those clips in all timelines in which they appear in that

project. You can relink only unlinked clips by selecting them specifically, but you can also relink

clips that are already linked if you want to force relink them to different media files (Relink Clips in

Selected Bins relinks both unlinked and linked clips at once). The Relink command automatically

searches all subdirectories within the currently selected directory, which is useful if you’re relinking

to media that’s been moved to another location, and that may have a different directory structure

as a result. However, a warning about searching large SAN volumes – you probably don’t want to

use this command to choose a starting directory that’s too high up the file path, as the resulting

search times may be unexpectedly long.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

�Using the Change Source Folder command: You also have the option to relink offline clips in the

Media Pool using the Change Source Folder command, which changes the directory structure

of each selected clip’s file path into a new file path based on a parent directory you select.

This is mainly useful if you’re relinking clips to media that you’ve moved to another location, but

that uses the same subdirectory structure as when the media was originally imported. For this

reason, it’s a safe and fast command to use when relinking to a structured collection of media on a

SAN volume.

�Using the Reconform From Bin(s) command: If you’ve imported multiple versions of the same

clips, with identical file names, overlapping timecode, or other matching criteria into separate bins

of the Media Pool, you can turn off Conform Lock Enabled for every clip in a timeline you want to

reconform, and then use the Reconform From Bin(s) command to reconform those timeline clips

to Media Pool clips in one or more specific bins of your choosing. Reconform From Bin(s) also lets

you choose the specific conform criteria you want to use to match clips in the timeline with clips

in the selected bins. A key feature of this command is that DaVinci Resolve will only reconform

timeline clips that are able to be matched to media in the bins you’ve selected; timeline clips for

which no match can be found are left as they were before you used this command.

�Using the Reconform From Media Storage command: This command lets you reconform timeline

clips to clips in a selected directory in your file system that hasn’t been imported into the Media

Pool first, and also lets you choose the specific conform criteria you want to use to match clips in

the timeline with clips in the selected bins. A key feature of this command is that DaVinci Resolve

will only reconform timeline clips that are able to be matched to media within the directory

structure you’ve selected; timeline clips for which no match can be found are left as they were

before you used this command.

�Overwriting clips on disk that are linked to in a DaVinci Resolve project: Last, but certainly not

least, DaVinci Resolve is smart enough to automatically relink clips in the Media Pool that have

been overwritten on disk by another version of the same file, so long as the file name, timecode,

and reel name (if used) in the new version of the file still match.

The following sections illustrate each of these methods of conforming and relinking media in

more detail.

Conform Multiple Selected Timelines

You can conform multiple timelines from the same source media at the same time. Simply select which

timelines you wish to conform in the Media Pool by Option or Shift-clicking them. Right-click on one of

the selected timelines and select Timelines Reconform from Bins or Reconform from Media Storage.

Unlinking Clips

You can also choose to unlink clips in the Media Pool. To do so, select the clip or clips you

want to unlink, right-click one of the selected clips, and choose Unlink Selected Clips from the

contextual menu.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

Conforming Clips During

XML and AAF Import

For workflows where you’re importing AAF or XML projects, and relinking the resulting clips in

DaVinci Resolve to media files that are either on disk, or conforming them to clips that are in the Media

Pool already, the rules for how clip metadata is defined for reconforming depend on two settings in

the Load AAF or XML dialog: “Automatically import source clips into media pool,” and “Ignore file

extensions when matching.”

The most important settings for conforming media in the Load dialog

The ways in which these two checkboxes interact to let you choose how media is conformed to an

imported AAF or XML file are complex, but here are the rules.

When Importing Clips With File Extensions

Matching Those in the AAF or XML File

Turn “Automatically Import” on and “Ignore file extensions” off.

This is the default setting, and is most useful when the AAF or XML file you’re importing contains

references to media you want to add to the Media Pool and use.

�First, if there are already clips in the Media Pool, DaVinci Resolve tries to conform as many of these

clips as possible by matching the file paths in the AAF or XML file to the stored file paths of each

clip in the Media Pool.

�Second, for all remaining clips not found, DaVinci Resolve imports as many clips as possible into

the Media Pool from any storage volumes that are visible to DaVinci Resolve, using the file paths

from the XML or AAF.

�Third, for all remaining clips not found, DaVinci Resolve tries a clip name match of clips that are

already in the Media Pool.

�Fourth, for all remaining clips not found, DaVinci Resolve tries a timecode match (along with a reel

name match if  this is enabled) of clips that are already in the Media Pool.

�Finally, for all remaining clips not found, the user is prompted to manually choose

another folder to search.

When Importing Clips With Different File Extensions

Turn “Automatically import” on and “Ignore file extensions” on.

Turning both of these options on is useful in situations where the sequence you’re importing was

originally edited using offline quality media, and you want to conform to high-quality online media in

a completely different format, possibly in the Media Pool, possibly on another disk. One example of

this is as when the edit was done using QuickTime or Avid DNxHD media, but you’re reconforming

to Blackmagic RAW files on another disk in order to grade the camera original raw media. Leaving

“Automatically import source clips into media pool” on, in this case.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

�First, if there are already clips in the Media Pool, DaVinci Resolve tries to conform as many of

these clips as possible by matching clip names.

�Second, for all remaining clips not found, the user is prompted to choose another folder

to search, and DaVinci Resolve imports as many clips as possible by matching clip names,

ignoring file extensions.

�Third, for all remaining clips not found, DaVinci Resolve tries a timecode match (and reel name

match if this is enabled in the General Options panel of the Project Settings) of clips that are

already within the Media Pool.

�Fourth, for all remaining clips not found, the user is prompted to manually choose

another folder to search.

Turn “Automatically import” on and “Link to source camera files” on.

The “Link to source camera files” checkbox only appears when you import AAF files. Turning this

option on when automatically importing media relinks the imported project to the original camera

source files that are kept track of by Media Composer/Symphony via the “Source Name” metadata

within the AAF file.

When You’re Only Relinking to Clips Already in the Media Pool

Turn “Automatically import” off.

Turning “Automatically Import source clips into media pool” off is useful in situations where you only

want to conform the imported AAF or XML to clips in the Media Pool. This is most useful in situations

where you’ve imported all of the camera original media into the Media Pool first, for example when

creating the dailies that were then edited, and you want to conform the imported AAF or XML to the

media that’s already there.

�First, if there are already clips in the Media Pool, DaVinci Resolve tries to conform as many of these

clips as possible by matching the file paths in the XML or AAF to the file paths stored for each clip

in the Media Pool.

�Second, for all remaining clips not found, DaVinci Resolve tries a clip name match of clips that are

already in the Media Pool.

�Third, for all remaining clips not found, DaVinci Resolve tries a timecode match (and reel

name match if this is enabled) of clips that are already within the Media Pool. In this case, the

file name is not used.

Beware When Choosing a Volume or Folder to Search

When prompted to choose a folder to search, you can optionally choose an entire volume;

DaVinci Resolve always searches through all subdirectories, and eventually all media on that

volume will be found. However, depending on the size and number of files on the selected

volume, this operation could take an unexpectedly long time, especially on a SAN volume.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT