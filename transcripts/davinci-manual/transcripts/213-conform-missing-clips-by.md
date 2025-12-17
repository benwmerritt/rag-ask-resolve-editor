---
title: "Conform Missing Clips by"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 213
---

# Conform Missing Clips by

Importing Their Source Media

If you have a timeline with one or more missing clips, that means that the relationship between that clip

in the timeline and the Media Pool has been lost because there is no corresponding clip in the Media

Pool. If you decide to manually import clips into the Media Pool that correspond to missing clips, the

“Automatically conform missing clips added to Media Pool” checkbox in the General Options panel of

the Project Settings determines what happens. Please note, the “Auto conform clips with media added

into Media Pool” setting must be disabled if you use collaborative workflow.

As long as the “Auto conform clips with media added into Media Pool” setting is enabled in the

General Options panel of the Project Settings, DaVinci Resolve automatically updates the conformed

relationship between clips that you add to the Media Pool and missing clips in the various timelines of

your project. DaVinci Resolve also updates the conform relationship of all other timeline clips that have

Conform Lock Enabled turned off at this time as well. All of this is done at the time you import the clips.

However, if “Auto conform clips with media added into Media Pool” is turned off when you import

additional clips into the Media Pool, then DaVinci Resolve will not attempt to reconform anything

automatically, instead relying on you to reconform offline or missing clips manually using one of the

many methods of manual reconforming that are available such as Reconform From Bins or Conform

Lock With Media Pool Clip.

For more information about manually adding clips to the Media Pool, see Chapter 18, “Adding

and Organizing Media with the Media Pool.”

Using the Import

Additional Clips Command

If you find that there are a lot of missing clips in a timeline that have no corresponding Media Pool

clips, there’s an easy way to fix this, that automates the process of gathering a list of what’s missing so

as to import all missing clips and conform them at once. This only works for missing clips, it does not

work for unlinked clips (for which you should use the Relink command in the Media Pool).

Conformed Timeline showing missing clips


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

To import missing clips and reconform them to the Timeline:


In the Edit page, right-click a timeline in the Media Pool that has missing clips, and choose one of

the following commands from the Timelines > Import submenu:

Timelines > Import > Additional Clips With Loose Filename Match: Searches the Timeline for all

missing clips, and prompts you to specify a directory of media with which to attempt to conform

them, adding only the media that’s necessary to the Media Pool. The “Loose Filename Match”

command ignores file extensions, which lets you replace offline media with online media in a

different format.

Timelines > Import > Additional Clips With Tight Filename Match: Searches the Timeline for all

missing clips, and prompts you to specify a directory of media with which to attempt to conform

them, adding only the media that’s necessary to the Media Pool. The “Tight Filename Match”

command searches only for media with identical file extensions.


Choose the directory with the remaining media to be conformed in the dialog that appears,

and click OK.

If the conditions are met for matching the media files in the directory you selected to the missing

clips in the current Timeline, then the necessary clips are automatically added to the Media Pool

and conformed to the timeline.

Using Conform Lock As a Command

If, for whatever reason, an unlinked clip in a timeline simply won’t conform to a clip in the Media Pool,

even when you know it’s there, you can use the “Conform Lock with Media Pool Clip” command to

force a clip in the Timeline to conform to a clip in the Media Pool of your choosing.

This command automatically suspends the Conform Lock Enabled setting of a target clip and ignores

file names and reel names in favor of conforming the target clip to another clip that you’ve manually

selected, while timecode is still used to align the clip being conformed with the clip that was in the

Timeline originally.

To conform lock a clip in the Timeline to another clip in the Media Pool:


Select a clip in the Media Pool. The clip you select in the Media Pool must be equal in length or

longer than the clip you select in the Timeline for Force Reconform to work.


Right-click an unconformed clip in the Timeline, and choose “Conform Lock with Media Pool Clip”

from the contextual menu. The selected clip in the Timeline is conformed to the clip you selected

in the Media Pool in one of two ways:

If the selected Media Pool clip has timecode matching the selected Timeline clip: The new clip

is perfectly conformed to match the original clip.

If the selected Media Pool clip doesn’t have timecode matching the selected Timeline clip: The

new clip is conformed such that the first frame of the Media Pool clip is aligned with the first frame

of the reconformed clip in the Timeline, and occupies the same duration.


If you right-click that clip again, you’ll see that Conform Lock Enabled is enabled, showing you that

the clip has been conform locked to media for which it wasn’t originally a match.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

Relinking Clips to Media Files on Disk

The easiest and best known method of relinking clips in your project that have either gone offline

or are not linked to the correct set of media files on disk is to use the appropriately named “Relink

Media” or “Relink selected clips” command. Note, the Relink command will only work for clips that

are unlinked, it will not work for clips that are missing and so have no corresponding clips in the

Media Pool.

The Relink command is the most flexible method of relinking clips in the Media Pool of your project

with clips in a file system directory of your choice, using file name and timecode as the primary criteria

for re-creating the correspondence between each clip and its corresponding media file on disk. This

is a good command to use to relink media that’s been moved to another location or reorganized using

another file structure on disk.

To relink all unlinked media:


Select the orange Relink icon in the page’s Media Pool.


Select the Locate button next to the specific volume(s) that are missing, and choose a directory

where the missing files are now


If the quick search initiated by the Locate buttons doesn’t find media that you know is there, you

can initialize an exhaustive deep disk search for the media by clicking on the Disk Search button.


If there are still other clips that couldn’t be found, you’re prompted to either choose another

directory altogether to continue searching, or quit.

To relink selected clips:


Select one or more offline clips to relink, or select a bin in the Media Pool bin list that contains

clips you want to relink, then right-click one of the selected clips or the selected bin, and choose

“Relink Selected Clips” from the contextual menu.


When the Relink File dialog opens, choose a directory in which to look for the files you want to

relink to, and click OK. DaVinci Resolve attempts to find every clip with a matching file name in the

subdirectories of the directory you chose, using the original file paths of the clips being relinked to

do this as quickly as possible. By first looking for the clips in the directories they were originally in,

relinking can be quite fast.


If there are any clips that couldn’t be found using the method in step 2, you’re prompted with

the option to do a “deep search” by a second dialog. If you click Yes, then DaVinci Resolve will

look for each clip inside every subdirectory of the directory you selected in step 2. This may take

significantly longer, but should be completely successful so long as the media that’s required is

within the selected directory structure.


If there are still other clips that couldn’t be found, you’re prompted to either choose another

directory altogether to continue searching, or quit.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

Using “Change Source Folder”

to Relink Clips

If you’ve used your file system to move media that’s associated with a DaVinci Resolve project, but you

haven’t changed the directory structure with which it’s organized, you can use the “Change Source

Folder” command to quickly relink selected clips in the Media Pool to the new file path of the media

on disk, using the original file paths as a guide. This is a good relinking method to use, if possible, for

projects on a SAN where you don’t want to risk the excessively long search times that could result

from using the Relink command to examine a nested hierarchy of folders in a more flexible way.

To relink your Media Pool clips to a new location:


Select one or more clips in the Media Pool, then right-click one of the selected clips, and choose

“Change Source Folder” from the contextual menu. The Relink Media window appears displaying

the original path for the material, with controls for choosing a new directory.


Click the “Browse” button to the right of the “Change To” field, and then use the file navigation

dialog to find the new location of the media file, select it, and click Open.


If you succeeded in finding the appropriate media file, click Change. Otherwise, click Cancel.

Using the “Reconform From Bins”

Command

The “Reconform From Bins” command gives you a way of reconforming multiple clips in a timeline at

once to a specific bin (or bins) of clips with matching metadata. To use this command, you must first

select the clips you want to reconform in a timeline (you can choose all of them or just a subset) and

turn off Conform Lock Enabled, and then, using the Reconform From Bin command, you can manually

choose another bin of clips in the Media Pool that you want to reconform to.

An important aspect of the Reconform From Bins command is that DaVinci Resolve only reconforms

timeline clips that can be matched to source clips in selected Media Pool bins. All timeline clips

that cannot be matched are left alone. This makes Reconform From Bins an ideal command to use

when you’ve imported a subset of clips to the Media Pool that you need to reconform to clips found

throughout an existing timeline.

For example, you could use this method to:

�Replace transcoded versions of clips in a timeline with the original camera raw clips.

�Replace the previous versions of VFX clips in a timeline with new versions.

�Replace the offline-quality media you’ve been working with so far with online‑quality media.

�Replace the temp clips you were originally given with rescanned or recaptured stock footage.

To use Reconform From Bins, it’s important to organize the clips you’re adding to the Media Pool

sensibly, in a self-contained bin or bins separate from the other media used by that timeline. It can be a

sub-bin, but it must be separate.

Here’s a simple example. If the media you edited or originally imported is in Bin 1, then import the

updated versions of all clips that need to be reconformed into Bin 2. Using Reconform From Bins,

you can then decide whether the clips in your timeline should be conformed to Bin 1, or Bin 2 when

possible, because only timeline clips for which there is a valid match are reconformed, while all other

timeline clips are ignored.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

DaVinci Resolve has the ability to choose custom conform options to control what metadata is used

to match timeline clips to source clips in the Media Pool. This means that you’re not restricted to only

using Timecode, Reel Name, and File Name, you could also use any combination of Total Duration,

Resolution, Bit Depth, Frame Rate, File Format, Codec, and/or Media UMID/UID to control how clips

are conformed, depending on your needs and the problem you have to solve.

The Reconform from Bins dialog

However, if the criteria you’ve selected to control the conform doesn’t match, the Reconform From Bins

operation will fail, and you’ll need to either try again with other conform criteria, or manually replace

the necessary clips in the Timeline.

Here’s a step by step workflow.

To reconform a timeline to clips within a specific Media Pool bin:


Double-click the Timeline you want to reconform to open it.


Either select the specific clips you want to reconform, or press Command-A to select every clip in

the Timeline if you want to reconform clips throughout the entire timeline without having to make

individual selections.


Right-click one of the selected clips, and choose “Conform Lock Enabled” to disable Conform Lock

Enabled for the clips you want to reconform. This frees DaVinci Resolve to consider all possible

conform matches for those clips in cases where there may be multiple clips with overlapping

timecode in the Media Pool.


Right-click the current Timeline in the Media Pool, and choose Timelines > Reconform From Bins.

The Conform Options dialog appears, with Timeline Options and Choose Conform Bins list to the

left, and the Conform Options panel to the right.


From the Timeline Options section, choose whether you want to conform to All Clips or just

to Selected Clips. Then, choose whether you want to “Set clips to Conform Lock Enabled”

after conform.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

Choosing which clips in the Timeline to attempt to reconform


In the Choose Conform Bins section, click the disclosure triangle to the left of the Master bin to

reveal the sub-bins contained within.


Turn on the checkboxes for the bins with media you want to conform the Timeline to, and turn off

the checkboxes for bins with media that you want to ignore.

Selecting folders for reconform


Next, choose the conform options you want to be considered when matching timeline clips

to Media Pool clips in the selected bins. By default, Timecode is enabled. Choose additional

criteria to be even more selective about how you want clips to be reconformed, or choose

different criteria if you need to use other metadata to get better results for clips you’re having a

hard time conforming.

Selecting criteria to guide the reconform


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

TIP: Choosing Custom from the top of the pop-up menu for File Extensions, File Format,

and Codec displays editable fields into which you can enter multiple options, separated

by commas, in order to list multiple possibilities for a successful match. The order in which

you enter these is important, as DaVinci Resolve will attempt to conform clips starting

with the first format/codec at the left, moving to try the next format/codec to the right if no

match is found, until every entry in your list has been tried.

Click OK. Where possible, the Timeline is automatically updated to conform to the media

contained within the bins you checked.


After you’ve used “Reconform From Bins,” any timeline clips that have been reconformed and

that now have timecode and reel names/file names that match two or more source clips in the

Media Pool will display a clip conflict badge in the Timeline. To eliminate this badge, you can

select either just the clips that were conformed, or all clips in the Timeline, right-click them, and

choose Conform Lock Enabled to eliminate these warnings.