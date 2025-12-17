---
title: "The Timeline Comparison Window"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 134
---

# The Timeline Comparison Window

When you first open the Timeline Comparison window, the first thing you see is a pair of miniature

timelines. The currently open Timeline appears at the bottom and the Timeline you right-clicked

appears at the top.

The Timeline Comparison window

Comparison Window Playhead Output

By default, the two playheads are ganged together, with the top playhead being displayed in the

Source Viewer, and the bottom playhead being displayed in the Timeline Viewer. These playheads

can be unganged if you want to compare different areas of both timelines, simply by turning off Sync

Playheads in the option menu.

Highlighting Differences

Special highlights indicate sections of both timelines that are different. Individual changes are not

individually highlighted, although they can be seen, on the premise that you’re more interested in a

section by section analysis of what your collaborating editor has been doing, for purposes of deciding

whether to incorporate changes or reversions based on this comparison.

Each section of differences between the two timelines are highlighted.

When using this tool, you can change the bottom Timeline to match the top Timeline, on a section by

section basis, by right-clicking a highlighted section and choosing Accept Change from the contextual

menu. When you do this, the currently open Timeline is immediately changed to incorporate the

altered section from the Timeline you’re comparing to. If necessary, you can undo this.


Edit | Chapter 34 Creating and Working with Timelines

EDIT

The Change List

Clicking the Diff Index button opens the change list, which shows you a more conventional item by

item comparison of the differences between the two timelines.

The change list of the Timeline Comparison window


Edit | Chapter 34 Creating and Working with Timelines

EDIT

Chapter 35

Preparing Clips

for Editing and

Viewer Playback

Before you start editing, there are a wide variety of things you can do to prepare

your clips for editing. In this chapter, you’ll learn how to browse, select, and play

through clips that you need to log, adding markers, setting In and Out points, and

creating subclips as you identify pieces you’ll be using later as you edit.

Contents

Keyboard Shortcuts in This Chapter������������������������������������������������������������������������������������������������������������������������������������������� 721

Browsing Clips in the Media Pool������������������������������������������������������������������������������������������������������������������������������������������������ 722

Selecting Clips in the Media Pool to Edit��������������������������������������������������������������������������������������������������������������������������������� 723

Duplicating Clips in the Media Pool������������������������������������������������������������������������������������������������������������������������������������������� 724

Viewer Playback and Navigation������������������������������������������������������������������������������������������������������������������������������������������������� 725

Source and Timeline Viewers vs. Single Viewer Mode����������������������������������������������������������������������������������������������������� 725

Opening Clips Into the Source Viewer to Prepare for Editing���������������������������������������������������������������������������������������� 726

Viewer Transport Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������� 727

Simple Keyboard Shortcuts for Playback and Navigation������������������������������������������������������������������������������������������������ 727

Using JKL to Control Playback������������������������������������������������������������������������������������������������������������������������������������������������������� 728

Special-Purpose Playback Commands�������������������������������������������������������������������������������������������������������������������������������������� 729

Optimized UI Layouts for Vertical Editing��������������������������������������������������������������������������������������������������������������������������������� 730

Option to “Stop and Go to Last Position”����������������������������������������������������������������������������������������������������������������������������������� 731

Enabling and Disabling Audio Scrubbing���������������������������������������������������������������������������������������������������������������������������������� 731

Playback Post-Roll��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 731

Source Tape in the Edit Page Source Viewer������������������������������������������������������������������������������������������������������������������������� 731

Limiting the Source Tape Scope by Folder Structure��������������������������������������������������������������������������������������������������������� 732


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

Keyboard Shortcuts in This Chapter

Here’s a list of of keyboard shortcuts you might find helpful that relate to topics found in this chapter.

Key Shortcut

Function

Arrow Keys (Media Pool)

Move selection in Media Pool; left and right arrow keys also open and

close bins in the Bin list

Shift (modifier)

Hold Shift down when clicking-to-select clips to select a contiguous range

Command (modifier)

Hold Command down when clicking-to-select clips to select

non‑contiguous clips

Command-A

Select all; selects all clips in the Media Pool browser area

Return or Enter

Opens selected clip or timeline into the Source Viewer

(in dual viewer mode) or Viewer

I, O

Set in/out point in Media Pool, Source Viewer, or Timeline

Option-Shift-I, O

Set video-only in/out point in Media Pool, Source Viewer, or Timeline

Command-Shift-I, O

Set audio-only in/out point in Media Pool, Source Viewer, or Timeline

Shift-I, O

Move playhead to in/out point

Spacebar

Play and stop

J, K, L

Play reverse, stop, play forward; more uses covered later in this chapter

Moving the Playhead Using Timecode������������������������������������������������������������������������������������������������������������������������������������� 732

How to Enter Timecode Values����������������������������������������������������������������������������������������������������������������������������������������������������� 732

Absolute Timecode Entry����������������������������������������������������������������������������������������������������������������������������������������������������������������� 733

Relative Timecode Entry������������������������������������������������������������������������������������������������������������������������������������������������������������������� 733

Copy and Paste Timecode in Viewer Timecode Fields����������������������������������������������������������������������������������������������������� 734

Gang Viewers (Playhead Ganging)����������������������������������������������������������������������������������������������������������������������������������������������� 734

Adding Markers������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 734

Adding Markers to Clips�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 735

Setting In and Out Points����������������������������������������������������������������������������������������������������������������������������������������������������������������� 736

Setting Clip In and Out Points in the Media Pool������������������������������������������������������������������������������������������������������������������ 736

Setting Clip In and Out Points in the Source Viewer������������������������������������������������������������������������������������������������������������ 737

Clearing and Navigating In and Out Points������������������������������������������������������������������������������������������������������������������������������� 737

Clip Edit Points Are Saved���������������������������������������������������������������������������������������������������������������������������������������������������������������� 739

Turning In and Out Points into Markers With Duration and Back Again����������������������������������������������������������������� 740

Organizing Media by Creating Subclips������������������������������������������������������������������������������������������������������������������������������������� 741

Removing or Changing Subclip Limits����������������������������������������������������������������������������������������������������������������������������������������� 742


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

Key Shortcut

Function

Option-L

Play again

Option-K

Stop and go to last position (of playhead)

/

Play around current selection

Up, Down Arrow

Go to previous clip/edit, go to next clip/edit

M

Add marker; doesn’t stop playback

Command-M

Add marker, open modify marker while pausing playback, then

continue playback

Shift-M

Modify marker

Option-M

Delete marker

Shift-Up, Down Arrow

Go to previous/next marker

Option-B

Create subclip (in currently selected Media Pool bin)

Browsing Clips in the Media Pool

The following procedures show how to select one or more clips in the Media Pool to accomplish

various editing tasks, either by opening a clip in the Source Viewer, or selecting a group of clips with

which you want to do drag and drop editing. This section starts by presenting different ways you

can browse the contents of the Media Pool to find clips you want to use, in preparation for making a

selection for your next operation.

Methods of browsing clips in the Media Pool:

In the Metadata View mode, each clip is represented by its own card with a thumbnail and basic

clip metadata information visible. This view is designed to have more metadata information than a

thumbnail but more targeted information than the List view. This feature, combined with its Sort modes,

is a powerful way to organize and reorganize your clips in the Media Pool.

�Using thumbnail hover scrub in the Media Pool’s Metadata view: Drag the pointer over a

thumbnail to scrub through its contents.

The Metadata View icon view (highlighted icon in the top bar),

showing the thumbnail being scrubbed next to the clip’s metadata


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

�Using thumbnail hover scrub in the Media Pool’s Thumbnail view: Drag the pointer over a

thumbnail to scrub through its contents.

Thumbnail hover scrubbing

�Using the Media Pool Filmstrip in the Media Pool’s List view: Select “Show Filmstrip” in the

Media Pool’s option menu. Select a clip to expose it in the Filmstrip at the top of the Media Pool,

and hover the pointer over the Filmstrip to watch it play. At any time, you can double-click a clip in

the Filmstrip to open it into the Source Viewer.

Using the Filmstrip when the Media Pool is in List view

TIP: When browsing media, you can open clips you want to have a closer look at in the

Source Viewer by double-clicking them in the Media Pool. Meanwhile, you can continue to

open other clips in the Filmstrip with a single clip in order to compare different clips with your

main selection that remains in the Viewer.