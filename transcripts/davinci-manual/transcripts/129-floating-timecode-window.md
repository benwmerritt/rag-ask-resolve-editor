---
title: "Floating Timecode Window"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 129
---

# Floating Timecode Window

A Timecode Window is available from the Workspace menu on every page except Fusion. Choosing

this option displays a floating timecode window that shows the timecode of the Viewer or Timeline that

currently has focus. This window is resizable so you can make the timecode larger or smaller.

A new floating timecode window is available

Dual-Monitor Layout

The Edit page has a dual-monitor layout that provides maximum space for the Timeline and Viewers

on the primary monitor, and an enlarged Media Pool, simultaneously displayed Timelines browser, Edit

Index, Effects Library, and Metadata Editor on the secondary monitor. The second screen of a dual-

screen layout can be resized but not reorganized.

If you have an single ultra-wide monitor, you can also use the dual-monitor layout, and DaVinci Resolve

will scale the interface as if you had two normal monitors side by side.

To enter dual-screen mode:

Choose Workspace > Dual Screen > On.


Edit | Chapter 33 Using the Edit Page

EDIT

The Edit page in dual-screen mode

To switch which UI elements appear on which monitors:

Choose Workspace > Primary Display > (Monitor Name), which reverses the contents of both

monitors in dual screen mode.

To view only the timeline in a monitor:

Choose Workspace > Full Screen Timeline.

Customizing the Edit Page

The default layout is quite efficient for a number of tasks on most displays. You can always return

to the default layout by choosing Workspace > Reset UI Layout. However, the Edit page can be

customized to create more room for specific areas of the interface to accommodate different tasks.

To resize any area of the Edit page:

�Drag the vertical or horizontal border between any two panels to enlarge one and shrink the other.

To expand the width of the Timeline:

�Click the Media Pool/Effects Library/Edit Index height button to reduce the area used by the Media

Pool, Effects Library, and/or Edit Index to shrink to half height. At this size, the Media Pool/Effects

Library/Edit Index are restricted to the top of the UI (you can only show one at a time), and the

Timeline takes up the full width of your display.

�Hiding the Edit Index and the Effects Library causes the Timeline to expand to the full

width of your screen.

To resize the height of individual video or audio tracks:

�Move the pointer to the top border of any video track header, or the bottom border of any audio

track header, and when it becomes a resize cursor, drag that border up or down to resize that

track. Each track can have an independent size when you do this.


Edit | Chapter 33 Using the Edit Page

EDIT

To enable a full-screen timeline in Dual Screen mode:

�Choose Workspace > Dual Screen > Full Screen Timeline, which causes the Timeline to fully

occupy the primary display, while the Browser, Viewers, Audio Mixer, Edit Index, and Effects

Library appear on the secondary display.

To customize the columns in the Edit Index:

�To show or hide columns in the Edit Index: Right-click any column header, and choose the

column you want to show or hide from the contextual menu. Checked columns are shown,

unchecked columns are hidden.

To resize any column of the Edit Index:

�Move your pointer over the divider between any two columns and drag when the horizontal resize

cursor appears.

To sort the Edit Index by any column:

�Click the Option button at the top right to display all active tracks, just the video, or just the

audio tracks.

To rearrange Edit Index columns:

�Drag the header of any column to the left and right to move that column.

To show and hide the Audio Meters or Audio Mixer:

�Click the Mixer button in the UI toolbar.

To switch between the Audio Meters and the Audio Mixer:

�Choose Meters or Mixer from the Option menu at the top right corner of the Mixer.

Undo and Redo in DaVinci Resolve

No matter where you are in DaVinci Resolve, Undo and Redo commands let you back out of steps

you’ve taken or commands you’ve executed and reapply them if you change your mind. DaVinci

Resolve is capable of undoing the entire history of things you’ve done since creating or opening a

particular project. When you close a project, its entire undo history is purged. The next time you begin

work on a project, its undo history starts anew.

Because DaVinci Resolve integrates so much functionality in one application, there are three separate

sets of undo “stacks” to help you manage your work.

�The Media, Edit and Fairlight pages share the same multiple-undo stack, which lets you backtrack

out of changes made in the Media Pool, the Timeline, the Metadata Editor, and the Viewers.

�Each clip in the Fusion page has its own undo stack so that you can undo changes you make to

the composition of each clip, independently.

�Each clip in the Color page has its own undo stack so that you can undo changes you make to

grades in each clip, independently.

In all cases, there is no practical limit to the number of steps that are undoable (although there may be

a limit to what you can remember). To take advantage of this, there are three ways you can undo work

to go to a previous state of your project, no matter what page you’re in.

To simply undo or redo changes you’ve made one at a time:

�Choose Edit > Undo (Command-Z) to undo the previous change.

�Choose Edit > Redo (Shift-Command-Z) to redo to the next change.


Edit | Chapter 33 Using the Edit Page

EDIT

You can also undo several steps at a time using the History submenu and window. At the time of this

writing, this only works for multiple undo steps in the Media, Cut, Edit, and Fairlight pages.

To undo and redo using the History submenu:


Open the Edit > History submenu, which shows (up to) the last twenty things you’ve done.


Choose an item on the list to undo back to that point. The most recent thing you’ve done appears

at the top of this list, and the change you’ve just made appears with a check next to it. Steps

that have been undone but that can still be redone remain in this menu, so you can see what’s

possible. However, if you’ve undone several changes at once and then you make a new change,

you cannot undo any more and those steps disappear from the menu.

Once you’ve selected a step to undo to, the menu closes and the project updates to show you its

current state.

The History submenu, which lets you undo several steps at once

To undo and redo using the Undo window:


Choose Edit > History > Open History Window.


When the History dialog appears, click an item on the list to undo back to that point. Unlike

the menu, in this window the most recent thing you’ve done appears at the bottom of this list.

Selecting a change here grays out changes that can still be redone, as the project updates to

show you its current state.

The Undo history window that lets you browse the

entire available undo stack of the current page


When you’re done, close the History window.


Edit | Chapter 33 Using the Edit Page

EDIT

Chapter 34

Creating and

Working with

Timelines

In this chapter, you’ll learn how to create and modify the timelines into which you

edit clips to create the edited sequences that are your programs.

Contents

Creating and Duplicating Timelines������������������� 698

Individual Timeline Settings for Format,

Monitoring, Output, and Color�������������������������������� 698

Creating Blank and Stringout Timelines������������ 699

Creating Timelines by Drag and Drop���������������� 700

Creating Timelines From

Bins and Selections������������������������������������������������������� 701

Creating Timelines Using an IMF

or DCP Composition Playlist (CPL)������������������������� 701

Duplicating Timelines�������������������������������������������������� 702

Disabling Timelines������������������������������������������������������� 702

Adding Media Pool Timelines

Directly to the Render Queue��������������������������������� 702

Import and Export DaVinci Resolve

Timelines (.drt)����������������������������������������������������������������� 703

Backing Up and Restoring Timelines������������������ 704

Timeline View Options���������������������������������������������� 705

Modifying Timeline Tracks��������������������������������������� 707

Naming Timeline Tracks������������������������������������������� 708

Using the Tracks Index���������������������������������������������� 708

Tracks Index Columns������������������������������������������������ 709

Toggle Track Header Control States

by Clicking and Dragging������������������������������������������ 710

Using Timeline Snapping and Zooming�������������� 711

Zoom Around Mouse Pointer������������������������������������ 712

Scrolling Through the Timeline ����������������������������� 712

Scroll Wheel Controls on Timeline������������������������� 712

Resizing the Timeline’s Video

and Audio Track Regions������������������������������������������� 713

Tabbed and Stacked Timelines������������������������������� 713

Tabbed Timelines����������������������������������������������������������� 713

Stacked Timelines���������������������������������������������������������� 715

View and Edit Dual Timelines

Using the Source Viewer�������������������������������������������� 716

Duplicate Frame Detection��������������������������������������� 717

Comparing Timelines��������������������������������������������������� 717

The Timeline Comparison Window������������������������ 718


Edit | Chapter 34 Creating and Working with Timelines

EDIT