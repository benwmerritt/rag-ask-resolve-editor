---
title: "Keyboard Shortcuts"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 14
---

# Keyboard Shortcuts

Since the majority of DaVinci Resolve users are on macOS, this manual presents all keyboard

shortcuts using the macOS conventions of the Command key and the Option key. For users of other

systems, all keyboard shortcuts that use the Option key in macOS use the ALT key in Windows

and Linux, and all keyboard shortcuts that use the Command key in macOS use the Control key in

Windows and Linux.

TIP: To keep controls identical between macOS, Windows, and Linux, the Control key in

macOS is not used by default for any keyboard shortcuts. However, you can assign your own

keyboard shortcuts to the Control key if you like, opening up a whole new set of keyboard

shortcuts for your own use on macOS.


DaVinci Resolve Interface | Chapter 2 Using the DaVinci Resolve User Interface

INTRO

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

�Each clip in the Fusion page has its own undo stack, so that you can undo changes you make to

the composition of each clip, independently.

�Each clip in the Color page has its own undo stack, so that you can undo changes you make to

grades in each clip, independently.

In all cases, there is no practical limit to the number of steps that are undoable (although there may be

a limit to what you can remember). To take advantage of this, there are three ways you can undo work

to go to a previous state of your project, no matter what page you’re in.

To simply undo or redo changes you’ve made one at a time:

�Choose Edit > Undo (Command-Z) to undo the previous change.

�Choose Edit > Redo (Shift-Command-Z) to redo to the next change.

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


DaVinci Resolve Interface | Chapter 2 Using the DaVinci Resolve User Interface

INTRO

To undo and redo using the Undo window:


Choose Edit > History > Open History Window.

When the History dialog appears, click an item on the list to undo back to that point. Unlike

the menu, in this window the most recent thing you’ve done appears at the bottom of this list.

Selecting a change here grays out changes that can still be redone, as the project updates to

show you its current state.


When you’re done, close the History window.

The Undo History window that lets you

browse the entire available undo stack

of the current page


DaVinci Resolve Interface | Chapter 2 Using the DaVinci Resolve User Interface

INTRO

MEDIA

Setup and

Workflows

CONTENTS


Managing Projects and Project Libraries������������������������������������������������������������������������������������������� 75


System and User Preferences���������������������������������������������������������������������������������������������������������������� 96


DaVinci Control Panels Setup�������������������������������������������������������������������������������������������������������������� 130


Project Settings������������������������������������������������������������������������������������������������������������������������������������������� 137


Camera Raw Settings������������������������������������������������������������������������������������������������������������������������������ 165


Improving Performance, Proxies, and the Render Cache����������������������������������������������������������� 191


Data Levels, Color Management, and ACES���������������������������������������������������������������������������������� 219


HDR Setup and Grading������������������������������������������������������������������������������������������������������������������������ 253


Image Sizing and Resolution Independence��������������������������������������������������������������������������������� 282


Data Burn-In������������������������������������������������������������������������������������������������������������������������������������������������� 297


Frame.io and Dropbox Replay Integration������������������������������������������������������������������������������������� 303


Resolve Live�������������������������������������������������������������������������������������������������������������������������������������������������� 312


Stereoscopic Workflows������������������������������������������������������������������������������������������������������������������������ 320


Using Variables and Keywords������������������������������������������������������������������������������������������������������������ 343

Chapter 3

Managing Projects

and Project Libraries

This chapter covers how to use the Project Manager to organize the projects

you’re working on in DaVinci Resolve, as well as how to deal with managing the

project libraries that serve as the organizational foundation of the Project Manager.

You’ll also see how to export and import projects, and how to archive a project and

its media for long‑term storage.

Contents

Using the Project Manager���������������������������������������������������������������������������������������������������������������������������������������������������������������� 76

Creating a New Project������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 77

Project Management������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 77

Importing and Exporting DaVinci Resolve Projects (.drp Files)����������������������������������������������������������������������������������������� 78

Project Manager View Options��������������������������������������������������������������������������������������������������������������������������������������������������������� 79

Searching for Projects���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 81

Organizing Projects in Folders����������������������������������������������������������������������������������������������������������������������������������������������������������� 81

Managing Project Libraries���������������������������������������������������������������������������������������������������������������������������������������������������������������� 82

Project Library Types����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 82

Opening the Project Libraries Sidebar������������������������������������������������������������������������������������������������������������������������������������������ 83

Moving Projects From One Project Library to Another on the Same Workstation�������������������������������������������������� 83

Managing Project Libraries in the Project Libraries Sidebar���������������������������������������������������������������������������������������������� 84

Quick Access to Recent Projects from the File Menu���������������������������������������������������������������������������������������������������������� 88

Saving Projects����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 89

Live Save������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 89

Project Backups��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 90

Project Notes��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 93

Dynamic Project Switching���������������������������������������������������������������������������������������������������������������������������������������������������������������� 93

Archiving and Restoring Projects��������������������������������������������������������������������������������������������������������������������������������������������������� 94


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA