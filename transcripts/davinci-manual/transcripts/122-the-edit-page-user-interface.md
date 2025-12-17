---
title: "The Edit Page User Interface"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 122
---

# The Edit Page User Interface

The Edit page has evolved into a source-record style NLE that contains nearly every editorial tool

you need for creative editing through finishing. The Edit page is divided into three main regions: the

browsers found at the left, the Viewers at the top, and the Timeline at the bottom, all of which work

together to let you import, edit, and trim timelines with a flexible variety of tools and methods.

The Edit Page in its entirety

The Interface Toolbar

At the very top of the Edit page is a toolbar with buttons that let you show and hide different parts of

the user interface. These buttons are as follows, from left to right:

The Interface toolbar

Media Pool/Effects Library/Edit Index height button: Lets you set the area used by the Media Pool,

Effects Library, and/or Edit Index to take up the full height of your display (you can display two at

a time), giving you more area for browsing at the expense of a narrower timeline. At half height,

the Media Pool/Effects Library/Edit Index are restricted to the top of the UI (you can only show one

at a time), and the timeline takes up the full width of your display.

Media Pool: Opens or hides a smaller version of the full Media Pool page,

allowing access to all the video clips, audio clips, and images used in the project.

Effects Library: Opens or hides the repository of all transitions, generators,

OpenFX, and audio filters available to use in the Edit page.

Index: Opens or hides the Edit, Tracks, and Markers indexes.


Edit | Chapter 33 Using the Edit Page

EDIT

Sound Library: Opens or hides the libraries of sound effects and music

registered with DaVinci Resolve. For more information on using the

Sound Library, see Chapter 170, “Using the Fairlight Page.”

Keyframes: Opens the Keyframes and Curves Editor.

Quick Export: Opens the Quick Export window.

Mixer: Opens or hides the Audio Mixer, giving you graphical controls to

adjust your sound mix.

Metadata: Shows or hides the Metadata Editor.

Inspector: Shows or hides the Inspector, which shows you the transform and

compositing effects of selected clips, or the editable options of selected effects

such as transitions or generators.

Navigating the Edit Page

Each of the panels in the Edit page user interface can be given focus via the Workspace > Active Panel

Selection submenu. Additionally, the following keyboard shortcuts can be used to give focus to

select bins, clips, the Source and Timeline Viewers, the Timeline, the Effects Library, Edit Index,

and Inspector.

Key

Function

Command-1

Media Folders

Command-2

Media Clips

Command-3

Source Viewer

Command-4

Timeline

Command-5

Timeline Viewer

Command-6

Effects

Command-7

Edit Index

Command-8

n/a

Command-9

Inspector

Q

Toggle between Source and Timeline Viewers


Edit | Chapter 33 Using the Edit Page

EDIT

Showing Which Panel Has Focus

Each panel you use has “focus,” meaning that clicking an item or control within a particular panel

makes that panel the active panel, which serves to direct keyboard shortcuts that are shared among

many panels to the particular panel you’re using. If you want to see which panel is in focus, you can

turn on the “Show focus indicators in the User Interface” checkbox in the UI Settings panel of the

User Preferences. When on, a red line at the top of the active panel indicates that it has focus.

The focus indicator shown at the top edge of the Media Pool,

shown next to a viewer that doesn’t have focus

The Media Pool

In the Edit page, the Media Pool contains all of the video, audio, and still image media you’ve imported

for editing into the project at hand, as well as all of the timelines that you’re going to be editing into.

The Media Pool is also mirrored on the Media, Cut, Fusion, Color, and Fairlight pages, so you can

access any audio or video clip, graphic, or timeline from any page where they can be used.

The Media Pool in Thumbnail mode

The Bin list at the left shows a hierarchical list of bins used for organizing your media, which is also

used to organize your timelines. By default, the Media Pool consists of a single bin, named “Master,”

but you can add more bins as necessary to organize timelines and clips by right-clicking anywhere


Edit | Chapter 33 Using the Edit Page

EDIT

in the empty area of the Media Pool and choosing Add Bin. You can rename any custom bin by

double-clicking on its name and typing a new one, or by right-clicking a bin’s name and choosing

Rename Bin. The Bin list can be hidden or shown via the button at the upper left-hand corner of the

Edit page toolbar.

The browser area to the right shows the contents of the currently selected folder. Every timeline you

create, and every AAF, XML, or EDL file you import, appears here. You can create or import as many

timelines as you need within a single project.

As in the Media page, the Media Pool can be displayed in either Metadata, Icon, or List view. In List

view, you can sort the contents by any one of a subset of the total metadata that’s available in the

Metadata Editor of the Media page. Of particular interest to editors are columns for Name, Reel Name,

different timecode streams, Description, Comments, Keyword, Shot, Scene, Take, Angle, Circled, Start

KeyKode, Flags, Usage, Resolution, and Frames Per Second.

For more information on using the myriad features of the Media Pool, see Chapter 18, “Adding

and Organizing Media with the Media Pool.” In the sections that follow, some key features of

the Media Pool are summarized for your convenience.

Importing Media Into the Media Pool on the Edit Page

While adding clips to the Media Pool in the Media page provides the most organizational flexibility and

features, if you find yourself in the Edit, Cut, Fusion, Color, or Fairlight page and you need to quickly

import a few clips for immediate use, you can do so in a couple of different ways.

To add media by dragging one or more clips from the Finder to

the Edit page Media Pool (macOS only):


Select one or more clips in the Finder.


Drag those clips into the Media Pool of DaVinci Resolve or to a bin in the Bin list.

Those clips are added to the Media Pool of your project.

To use the Import Media command in the Edit page Media Pool:


With the Edit page open, right-click anywhere in the Media Pool, and choose Import Media.


Use the Import dialog to select one or more clips to import, and click Open.

Those clips are added to the Media Pool of your project.

For more information on using the myriad features of the Media Pool, see Chapter 18, “Adding

and Organizing Media with the Media Pool.” Below, some key features of the Media Pool are

summarized for your convenience.

Bins, Power Bins, and Smart Bins

There are actually three kinds of bins in the Media Pool, and each appears in its own section of the Bin

list. The Power Bin and Smart Bin areas of the Bin list can be shown or hidden by selecting/deselecting

in the Media Pool option menu Show Smart Bins, and Show Power Bins. Here are the differences

between the different kinds of bins:


Edit | Chapter 33 Using the Edit Page

EDIT

Bins: Simple, manually populated bins. Drag and drop anything you like into a bin, and that’s

where it lives, until you decide to move it to another bin. Bins may be hierarchically organized,

so you can create a Russian dolls nest of bins if you like. Creating new bins is as easy as right-

clicking within the bin list and choosing Add Bin from the contextual menu.

Power Bins: Hidden by default. These are also manually populated bins, but these bins

are shared among all of the projects in your current project library, making them ideal for

shared title generators, graphics movies and stills, sound effects library files, music files,

and other media that you want to be able to quickly and easily access from any project. To

create a new Power Bin, show the Power Bins area of the Bin list, then right-click within it and

choose Add Bin.

Smart Bins: These are procedurally populated bins, meaning that custom rules employing

metadata are used to dynamically filter the contents of the Media Pool whenever you select

a Smart Bin. This makes Smart Bins fast ways of organizing the contents of projects for which

you (or an assistant) has taken the time to add metadata to your clips using the Metadata

Editor, adding Scene, Shot, and Take information, keywords, comments and description text,

and myriad other pieces of information to make it faster to find what you’re looking for when

you need it. To create a new Smart Bin, show the Smart Bin area of the Bin list (if necessary),

then right-click within it and choose Add Smart Bin. A dialog appears in which you can edit the

name of that bin and the rules it uses to filter clips, and click Create Smart Bin.

Showing Bins in Separate Windows

If you right-click a bin in the Bin List, you can choose “Open As New Window” to open that bin into its

own window. Each window is its own Media Pool, complete with its own Bin List, Power Bins and Smart

Bins lists, and display controls.

Media Pool bins opened as new windows


Edit | Chapter 33 Using the Edit Page

EDIT

This is most useful when you have two displays connected to your workstation, as you can drag these

separate bins to the second display while DaVinci Resolve is in single screen mode. If you hide the

Bin list, not only do you get more room for clips, but you also prevent accidentally switching bins if

you really want to only view a particular bin’s contents in that window. You can as many additional

Bin windows open as you care to, in addition to the main Media Pool that’s docked in the primary

window interface.