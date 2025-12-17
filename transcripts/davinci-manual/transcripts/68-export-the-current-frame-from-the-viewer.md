---
title: "Export The Current Frame from The Viewer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 68
---

# Export The Current Frame from The Viewer

You can now export a still frame from the Viewer in the Media, Cut, and Edit pages.

To Export a Still Frame from the Viewer:


Use the Viewer’s playback controls to navigate to the frame you want to export.


Select File > Export > Current Frame as Still.


Enter the name of the still frame in the File System viewer.


Enter the desired format of the still frame in the File System viewer.


Click on the Export button.

Live Media Preview

Enabled by default, the Live Media Preview setting found in the Viewer options menu (the three-

dots menu found at the upper right-hand corner of the Viewer) makes it possible for thumbnails that

you’re skimming in either the Media Storage browser or Media Pool to show the skimmed frame in the

Viewer. When skimming with Live Media Preview enabled, the playhead that appears in the thumbnail

is locked to the playhead displayed in the Viewer’s jog bar. You can turn Live Media Preview on or off.

When Live Media Preview is on in the Viewer options

menu, skimming thumbnails mirrors to the Viewer

Media Pool

The Media Pool is central to the DaVinci Resolve experience. It contains all of the media that you

import into the current project, as well as all of the timelines you create. It also contains all media that’s

automatically imported along with Projects, Timelines, or Compositions that have themselves been

imported into DaVinci Resolve. In the Media page, enough room is given to the Media Pool to make it

an ideal place to sort, sift through, and organize the clips in your project. However, the Media Pool is

also mirrored in the Cut, Edit, Fusion, Color, and Fairlight pages, so you can access clips as you build

timelines, composites, grades, and sound design.

Media Pool with the Bin list open


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA

The Bin List

Ordinarily, all media imported into a project goes into the Master bin, which is always at the top of the

Bin list and encompasses everything in a given project. However, you can add bins of your own, and

the Media Pool can be organized into as many user-definable bins as you like, depending on your

needs. Media can be freely moved from one bin to another from within the Media Pool. When working

in projects with multiple bins, you can choose to expose the bin structure in one of two ways:

Bin list open: The Bin List button at the upper left-hand corner of the Media Pool lets you

open a separate List view showing all bins in your project, hierarchically. Bins that contain

other bins appear with a disclosure button to their left, that you can use to show or hide the

contents. With the Bin list exposed, it’s easy to organize clips among a large collection of bins.

Bin list closed: When the Bin list is closed, all bins are hidden, and contents of whichever bin

is currently selected populate the Media Pool browser.

Showing Bins in Separate Windows

If you right-click a bin in the Bin list, you can choose “Open As New Window” to open that bin into its

own window. Each window is its own Media Pool, complete with its own Bin, Power Bins and Smart

Bins lists, and display controls.

This is most useful when you have two displays connected to your workstation, as you can drag these

separate bins to the second display while DaVinci Resolve is in single screen mode. If you hide the

Bin list, not only do you get more room for clips, but you also prevent accidentally switching bins if you

really want to only view a particular bin’s contents in that window. You can have as many additional

Bin windows open as you care to, in addition to the main Media Pool that’s docked in the primary

window interface.

Media Pool bins opened as new windows


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA

Bins, Power Bins, and Smart Bins

There are actually three kinds of bins in the Media Pool, and each appears in its own section of the

Bin list. The Power Bin and Smart Bin areas of the Bin list can be shown or hidden by using the Media

Pool option menu and selecting/deselecting Show Smart Bins and Show Power Bins. Here are the

differences between the different kinds of bins:

Bins: Simple, manually populated bins. Drag and drop anything you like into a bin, and that’s

where it lives, until you decide to move it to another bin. Bins may be hierarchically organized,

so you can create a Russian dolls nest of bins if you like. Creating new bins is as easy as right-

clicking within the Bin list and choosing Add Bin from the contextual menu.

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

Filtering Bins Using Color Tags

If you’re working on a project that has a lot of bins, you can apply color tags to identify particular bins

with one of eight colors. Tagging bins is as easy as right-clicking any bin and choosing the color you

want from the Color Tag submenu.

Using Color Tags

to identify bins

Using Color Tag filtering to

isolate the blue bins


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA

For example, you can identify the bins that have clips you’re using most frequently with a red

tag. A bin’s color tag then appears as a colored background behind that bin’s name.

Once you’ve tagged one or more Media Pool bins, you can use the Color Tag Filter

drop‑down menu (the drop-down control to the right of the Bin List button) to filter out all but a

single color of bin.

To go back to seeing all available bins, choose Show All from the Color Tag Filter drop-down.

Sorting the Bin List

The Bin list (and Smart Bin list) of the Media Pool can be sorted by bin Name, Date Created, or

Date Modified, in either ascending or descending order. Simply right-click anywhere within the Bin list

and choose the options you want from the Sort by submenu of the contextual menu.

You can also choose User Sort from the same contextual menu, which lets you manually drag all bins

in the Bin list to be in whatever order you like. As you drag bins in this mode, an orange line indicates

the new position that bin will occupy when dropped.

If you use User Sort in the Bin list to rearrange your bins manually, you can switch back and forth

between any of the other sorting methods (Name, Date Created, Date Modified) and User Sort and

your manual User Sort order will be remembered, making it easy to use whatever method of bin

sorting is most useful at the time, without losing your customized bin organization.

Dragging a bin to a new position in

the Bin list in User Sort mode

You can now enable waveform thumbnails in the

Media Pool that you can scrub with Live Media Preview.


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA

Deleted Timeline Backups

From the Media Pool Options menu, you can select Deleted Timeline Backups and examine deleted

timelines and available backup files for each timeline. You can select backups to be restored or

choose to permanently delete selected backups.

Metadata Editor

Both the Media and Edit pages have a Metadata Editor. When you select a clip in any area of the

Media page, its metadata is displayed within the Metadata Editor. If you select multiple clips, only the

last clip’s information appears. The Metadata Editor’s header contains uneditable information about

the selected clip, including the file name, directory, duration, video codec, frame rate, resolution, audio

codec, sample rate, and number of channels.

Because there are so very many metadata fields available, two drop-down menus at the top let you

change which set of metadata is displayed in the Metadata Editor.

Metadata Presets (to the left): If you’ve used the Metadata panel of the User Preferences to

create your own custom sets of metadata, you can use this drop-down to choose which one to

expose. Surprisingly enough, this is set to “Default” by default.

Metadata Groups (to the right): This drop-down menu lets you switch among the various

groups of metadata that are available, grouped for specific tasks or workflows.

The heart of the Metadata Editor is a series of editable fields underneath the header that let

you review and edit the different metadata criteria that are available.

For more information on editing clip metadata and creating custom metadata presets, see

Chapter 19, “Using Clip Metadata.”

Clip Metadata Editor showing the Clip Details panel


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA