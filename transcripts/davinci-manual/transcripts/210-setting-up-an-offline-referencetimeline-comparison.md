---
title: "Setting Up an Offline Reference/Timeline Comparison"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 210
---

# Setting Up an Offline Reference/Timeline Comparison

Once you’ve assigned a clip or timeline as an Offline Reference Movie, it’s easy to see a comparison.

Selecting the Offline

video in the Source Viewer

To view an offline reference comparison:


Open the Source Viewer’s Mode pop-up menu and choose the checkerboard icon

indicating Offline Reference.

The Offline Reference Clip you assigned previously now appears within the Offline Viewer, and

plays back in sync with the Timeline. If your clips have sizing applied, have Fusion or other effects,

or are graded, you can see a side-by-side comparison between the state of each clip in the Offline

Reference Clip, and the graded Timeline clip.

The Edit page in Offline/Timeline mode


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT


If the currently selected Offline Reference is out of sync (which can be confirmed via the position

of a slate, two-pop, title, or other known shared sync point at the beginning of the program), you

can use the sync field at the upper left-hand corner of the Source Viewer in Offline mode to slip

the sync of the reference by whatever number of frames you need.


If you like, you can optionally choose other ways of comparing clips, by right-clicking anywhere

within the Timeline Viewer and choosing Vertical Wipe, Horizontal Wipe, Diagonal Wipe, Mix Wipe,

Difference (a Composite mode), Box (wipe), Venetian Blind, or Checkerboard. These modes offer

you different ways of quickly and directly comparing the content, sizing, color, and alignment of

the Offline Reference Movie to the clips in your timeline.

Different viewing options for comparing the Offline Reference Movie to the

Timeline are available in the Timeline Viewer contextual menu

If you choose a wipe or difference comparison, that comparison will also be visible on the display

connected to your video output interface, and dragging anywhere within the Timeline Viewer will

adjust the ratio and position of the wipe.


To turn an offline comparison viewer mode off, simply right-click the Timeline Viewer again and

choose No Wipe.


When you’re done doing this offline comparison, choose Source from the Source Viewer’s Mode

pop-up menu, and the Source Viewer is ready for viewing clips from the Media Pool, as normal.


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT

Chapter 56

Conforming and

Relinking Clips

Whether you import a DaVinci Resolve project or a project exchange file from

another application, you’ll need to deal with the need to relink media files in the

Media Pool and reconform timelines to either the same or compatible media files

that may either be in the Media Pool or that may need to be imported from disk.

This chapter discusses the rules with which DaVinci Resolve conforms clips to match timelines, and

describes the numerous methods with which you can control clip linking, timeline conform, as well

as how you can deal with problems that arise using the numerous problem-solving techniques that

DaVinci Resolve makes available.

Contents

Conforming and Relinking Media����������������������������������������������������������������������������������������������������������������������������������������������� 1145

Conforming and Relinking During Project Import���������������������������������������������������������������������������������������������������������������� 1145

Conforming and Relinking Existing Timelines and Clips�������������������������������������������������������������������������������������������������� 1145

The Difference Between Unlinked and Missing Clips����������������������������������������������������������������������������������������������������� 1146

Duplicate Clips are Considered Separate Sources������������������������������������������������������������������������������������������������������������ 1147

Summary of Methods for Conforming and Relinking�������������������������������������������������������������������������������������������������������� 1147

Conform Multiple Selected Timelines�������������������������������������������������������������������������������������������������������������������������������������� 1149

Unlinking Clips�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1149

Conforming Clips During XML and AAF Import������������������������������������������������������������������������������������������������������������������ 1150

Importing Clips Before Importing an EDL, AAF, or XML������������������������������������������������������������������������������������������������ 1152

Essential Clip Metadata for Easy Conforming and Relinking����������������������������������������������������������������������������������������� 1152

Defining Clip Metadata When Adding Media to the Media Pool���������������������������������������������������������������������������������� 1153

How Reel Names Are Identified��������������������������������������������������������������������������������������������������������������������������������������������������� 1153

Conform Missing Clips by Importing Their Source Media���������������������������������������������������������������������������������������������� 1157

Using the Import Additional Clips Command������������������������������������������������������������������������������������������������������������������������ 1157

Using Conform Lock As a Command���������������������������������������������������������������������������������������������������������������������������������������� 1158

Relinking Clips to Media Files on Disk������������������������������������������������������������������������������������������������������������������������������������� 1159

Using “Change Source Folder” to Relink Clips������������������������������������������������������������������������������������������������������������������� 1160


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

Using the “Reconform From Bins” Command���������������������������������������������������������������������������������������������������������������������� 1160

Using Reconform From Media Storage������������������������������������������������������������������������������������������������������������������������������������ 1163

Understanding, Fixing, and Using Reel Conflicts�������������������������������������������������������������������������������������������������������������� 1166

Using Clip Conflicts as a Conform Tool������������������������������������������������������������������������������������������������������������������������������������� 1167

Resolving Clip Conflicts��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1167

Re-editing Media Directly to the Timeline����������������������������������������������������������������������������������������������������������������������������� 1168

How Grades Are Linked to Multiple Timelines�������������������������������������������������������������������������������������������������������������������� 1169

Conforming and Relinking Media

DaVinci Resolve provides a wealth of tools to help you deal with managing the relationship

between clips in the Media Pool and clips in timelines, and with the links between each clip and its

corresponding media file on disk. You can use these tools to manage different project workflows, or to

deal with problems that can occur when importing project files in any format from a variety of sources.

This section describes every method available in DaVinci Resolve for conforming clips and relinking

media. More information on the clip metadata that’s used to determine the correspondences between

clips and media is found later in this chapter.

Conforming and Relinking During Project Import

When you import an AAF or XML file, you have the ability to relink the clips that are imported into the

Media Pool to the corresponding source media files on disk as part of the process. As an automatic

result, the imported timeline is conformed to the clips in the Media Pool, and you end up with a Media

Pool full of clips, and an arrangement of those clips in the imported timeline. Because it all usually

happens at the same time, it’s easy to confuse the distinction between a timeline’s relationship to the

clips in the Media Pool, and each clip’s relationship to their corresponding source media file on disk.

The workflow for importing an EDL makes this process more explicit, since you must first import all

of the clips you need into the Media Pool, making sure that they have the correct reel names and

timecode. This creates the link between the Media Pool clips and the source media on disk. You then

import the EDL in a second step, which creates a timeline that attempts to reconform itself to the clips

in the Media Pool using reel name and timecode information.

Conforming and Relinking Existing Timelines and Clips

There are many reasons why you might want to reconform or relink media long after you’ve started

editing or grading a project, so DaVinci Resolve provides additional tools to facilitate these workflows

as well. For example, you may have started a project using placeholder VFX or stock footage clips,

but you later need to replace these with final versions of the same shots. Or, you may have decided

to edit a project using transcoded versions of the camera raw media files you were given, only to

decide later that you want to switch one or all of the clips in the timeline to use the original camera

media instead for grading and finishing. DaVinci Resolve has a wide variety of tools to support these

workflows and more.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

The Difference Between Conforming and Relinking

While these two terms are often used synonymously, conforming typically refers to the process

of matching clips in a timeline to the appropriate source clips in the Media Pool, while relinking

typically refers to the process of matching a source clip in the Media Pool to its corresponding

media file on disk. This is a recent change necessitated by an expansion of relinking and

reconforming options, so the author offers his apologies if this usage is not always consistent.

The Difference Between

Unlinked and Missing Clips

While it may seem pedantic, there’s an important difference between clips that are unlinked, and

clips that are missing when it comes to the relationship between clips in the Media Pool and clips in a

timeline. First off, both of these “offline” clip states look different in the timeline, but these differences

aren’t just cosmetic.

A missing clip in the Timeline (left) compared to an unlinked clip in the Timeline (right)

An unlinked clip is a clip that exists in the Media Pool, but has lost the link to its corresponding media

file on disk. However, unlinked clips still contain metadata, they still have a relationship to instances

of that clip that have been edited into timelines in your project, and they can be easily relinked to

media files with matching file names and timecode using the Relink command (described later),

or reconformed to previously or newly imported clips in specific bins of the Media Pool with the

Reconform From Bins command (also described later).

Missing clips do not exist in the Media Pool at all, although clips flagged as missing can still appear in

the timelines of your project. However, since missing timeline clips have no corresponding source clips

in the Media Pool, the clip in the timeline has no metadata that can be seen in the Metadata Editor, and

it will have lost any remote grades that are associated with that source clip.

For more information about remote grades, see Chapter 142, “Grade Management.”

You can fix missing clips in a timeline in one of two ways:

�If the “Automatically conform missing clips added to Media Pool” setting is enabled in the General

Options panel of the Project Settings, then simply reimport the corresponding source clips into

the Media Pool and they will be automatically conformed to missing clips with matching timecode

and file names in the timeline (this only happens at the time of import, it doesn’t work for matching

clips that are already in the Media Pool). Please note, this setting must be disabled if you use

collaborative workflow.

�If the “Automatically conform missing clips added to Media Pool” setting is disabled in the General

Options panel of the Project Settings, then you’ll have to import the missing clips and either

manually reconform them one at a time to the missing timeline clips using the Conform Lock with

Media Pool Clip command, or use the Reconform From Bin(s) or Import Additional Clips With

Loose/Tight Filename Match commands to try reconforming them all at once.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

However you choose to reconform the missing clips, you won’t get the original remote grades

or manually edited metadata back unless you had previously exported the appropriate

metadata and grades, in which case you can reimport and apply these in separate steps.