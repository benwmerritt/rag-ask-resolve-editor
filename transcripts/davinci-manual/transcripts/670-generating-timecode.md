---
title: "Generating Timecode"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 670
---

# Generating Timecode

To generate and transmit timecode as an audio signal from your audio interface to an external device

or application:


Switch on Generate Timecode.


Select the audio interface output from the Interface Output dropdown you want to transmit the

timecode audio through.


Begin playback of your mix in Fairlight. DaVinci Resolve will continue sending the timecode audio

signal to the destination until you click the Stop button.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Generate Timecode enabled

TIP: If you’re using a Fairlight SX36 audio interface, the signal can be used to synchronize

another DaVinci Resolve system or any system that can use timecode audio as a reference.

Pro Tools AAF Import

DaVinci Resolve can import AAF projects and media from Pro Tools, enabling you to move an

audio project from a Pro Tools workstation to a Fairlight workstation. AAF import supports the

import of embedded audio and track automation. To do so choose File > Import Timeline > Import

AAF/EDL/XML.

Dual-Monitor Layout

The Fairlight page has a dual-monitor layout that provides maximum space for the mixer and audio

meters on one screen and a full-screen timeline on the other. If you have an single ultra-wide monitor,

you can also use the dual-monitor layout, and DaVinci Resolve will scale the interface as if you had two

normal monitors side by side.

To enter dual screen mode:

Choose Workspace > Dual Screen > On.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

The Fairlight page in dual screen mode

To switch which UI elements appear on which monitors:

Choose Workspace > Primary Display > Display 1 or Display 2, which reverses the contents of

both monitors in dual screen mode.

Customizing the Fairlight Page

The default layout is quite efficient for a number of tasks on most displays. You can always return

to the default layout by choosing Workspace > Reset UI Layout. However, the Fairlight page can be

customized to create more room for specific areas of the interface to accommodate different tasks.

To resize any area of the Fairlight page:

�Drag the vertical or horizontal border between any two panels to enlarge one and shrink the other.

To resize the height of individual audio tracks:

�Move the pointer to the bottom border of any audio track header, and when it becomes a resize

cursor, drag that border up or down to resize that track. Each track can have an independent size

when you do this.

To resize any column of the Index:

�Move your pointer over the divider between any two columns and drag when the horizontal resize

cursor appears.

To rearrange Index columns:

�Drag the header of any column to the left and right to move that column.

NOTE: if you want to retain the height view set for your tracks when a project is closed and

re-opened, right-click on the track header and choose “Lock Track Height to.” You can

choose “Custom” as the size for any track height you may want other than standard sizes.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

TIP: You can also use the option key to adjust heights for all selected tracks or Command-

option to adjust all selected tracks.

Fairlight Configuration Presets

You can store and recall complete configuration presets for the Fairlight page, or individual areas of it,

using the Presets Library functions, found in Fairlight > Presets Library.

For more more information on using the Presets Library, see Chapter 171, “Setting Up Tracks,

Busses, and Patching.”

Undo and Redo in DaVinci Resolve

No matter where you are in DaVinci Resolve, Undo and Redo commands let you back out of steps

you’ve taken or commands you’ve executed, and reapply them if you change your mind. DaVinci

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

You can also undo several steps at a time using the History submenu and window.

To undo and redo using the History submenu:


Open the Edit > History submenu, which shows (up to) the last twenty things you’ve done.


Choose an item on the list to undo back to that point. The most recent thing you’ve done appears

at the top of this list, and the change you’ve just made appears with a check next to it. Steps

that have been undone but that can still be redone remain in this menu, so you can see what’s

possible. However, if you’ve undone several changes at once and then you make a new change,

you cannot undo any more and those steps disappear from the menu.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

The History submenu, which lets you undo several steps at once

Once you’ve selected a step to undo to, the menu closes and the project updates to show you its

current state.

To undo and redo using the Undo window:


Choose Edit > History > Open History Window.


When the History dialog appears, click an item on the list to undo back to that point. Unlike

the menu, in this window the most recent thing you’ve done appears at the bottom of this list.

Selecting a change here grays out changes that can still be redone, as the project updates to

show you its current state.

The Undo history window that lets you browse the

entire available undo stack of the current page


When you’re done, close the History window.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT