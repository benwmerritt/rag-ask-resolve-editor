---
title: "List View"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 100
---

# List View

Each clip appears as an item in a multi-column list showing a variety of metadata about each clip. In list

view, you can click the header of any column to sort the contents by that column’s information (clicking

again toggles the sort order between Ascending and Descending). Scrolling right reveals additional

columns of information. Clicking on an item on the list may let you change its value, depending on

the column.

The List View mode

Metadata Display Palette

When in the Source Tape or Source mode in the Viewer, a small tag icon becomes available directly to

the left of the search bar in the Media Pool. Clicking on this icon activates the Metadata Display palette

at the top of the Media Pool. The display shows basic information about whatever clip is selected in

order for you to quickly review the details about selected clips.

Next to the search bar in the Cut page Media Pool, is a small tag icon (circled red)

that opens the Metadata display panel at the top of the Media Pool.

The information on the display includes: Camera Name, Scene/Shot/Take, Frame Rate,

and Resolution.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

Sorting and Searching

Once you’ve imported media into your project, searching and sorting controls help you find

what you need.

Searching

A search field lets you type a term you want to use to find one or more clips that match that criteria. When

you type anything, the contents of the Media Pool shrink to show only clips that match your criteria.

Navigable Clip Paths

The Media Pool in the Cut page has a navigable title bar that shows a clip’s Media Pool hierarchy.

As you navigate in the Media Pool, the current clip is highlighted, and its hierarchy will now appear in

top of the Media Pool title bar. By clicking directly on bins in this bin path, you can quickly broaden or

narrow the scope of the Media Pool, say from Shoot Day to Camera to Card to Clip and vice versa.

The Media Pool title bar showing a clip’s Media Pool

hierarchy. Clicking directly on these bins will narrow or

broaden the scope of the clips in the Source tape.

Sort Media By

A Sort Media By drop-down menu lets you choose which

criteria defines the order in which clips in the Media Pool are

arranged. Options include: Custom, Timecode, Camera, Date

Time, Clip Name, Bin, Scene Shot, Clip Color, Date Modified,

Date Imported, and Online Status, and you can choose to

sort in Ascending (bottom to top) or Descending (top to

bottom) order.

Lastly, a search field lets you type a term you want to use to

find one or more clips that match that criteria. When you type

anything, the contents of the Media Pool shrink to show only

clips that match your criteria.

TIP: If you want to sort by a criteria that’s not in the

drop-down menu, you can switch the Media Pool to

List view, then sort by any column you might want

(such as “Date Created”), and then switch back to Icon

or Filmstrip view.

The Media Pool Sort options


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

Finding Timeline Clips in the Media Pool

From time to time, you’ll find yourself wanting to find the source clip in the Media Pool that

corresponds to a clip in the Timeline. For example, you might want to go back to a part of an interview

clip you’ve already used to find another phrase on the same topic.

To find a timeline clip in the Media Pool:

�Right-click a clip in the Timeline, and choose Find in Media Pool from the contextual menu.

The corresponding clip is selected in the Media Pool, which scrolls to show that clip, if necessary.

�If you have several clips that are synced, right-click a clip in the Timeline, and choose Find in

Multi Source from the contextual menu. The corresponding clip is selected in the Media Pool

and opened in the Multi Source Viewer, which allows you to choose another camera angle of the

same shot.

Clip Color

Clip colors are an organizational tool that make it easier to keep track of different kinds of clips visually.

For example, you can assign colors based on good takes, based on characters or subjects in the

program, based on type of media (b-roll versus a-roll for example), or using any one of a number of

organizational strategies. Whatever helps you keep track of things you need to keep track of.

Changing clip colors:

�You can assign colors to clips by right-clicking one or more selected clips in the Media Pool

or Timeline, and choosing one of 16 available colors from the Clip Color submenu of the

contextual menu.

Removing clip colors:

�Clip colors can be removed by right-clicking one or more selected clips in the Media Pool or

Timeline, and choosing Clear Color from the Clip Color submenu of the contextual menu.

�Clip colors appear as a colored dot on a clip thumbnail when in Thumbnail view, as a clip color in

Filmstrip view, and as a patch in the Clip Color column when in Column view.

Clip color in – Thumbnail

Clip color in – Filmstrip

Clip color in – Column views

�Clips with assigned colors also appear tinted in the Timeline, similarly to the Filmstrip tint

in the Media Pool.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

A timeline with a video clip that has been colored to identify what they are to the editor

Relinking Media

DaVinci Resolve attempts to automatically keep track of the relationship between clips in your project

and their corresponding source media on disk. If, for whatever reason, source media that links to clips

in your project becomes unavailable because it’s been moved, DaVinci Resolve has several different

methods of relinking those clips in the Media Pool. This section summarizes two methods of relinking,

“Relink Media” and the “Relink selected clips” command.

For more information on other methods of conforming projects and relinking media, see

Chapter 56, “Conforming and Relinking Clips.”

Relink Media

If DaVinci Resolve fails to find your media, a Relink Media icon in the Cut page’s and Edit page’s Media

Pools will highlight orange.

The Relink Media icon that

appears for unlinked media

Clicking this icon opens a dialog box showing the volumes that the missing files initially belonged to.

You can then use this information to track down the media on your file system, find that specific hard

drive, or ask a client if they provided you the media from this volume. Clicking the Locate button lets

you re-connect the missing clips to a new file location of your choosing. If the quick search initiated

by the Locate buttons doesn’t find media that you know is there, you can initialize an exhaustive deep

disk search for the media by clicking on the Disk Search button.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

The Relink Media dialog showing the volume names

where the missing clips originated

Relink Selected Clips

The appropriately named “Relink selected clips” command is the most flexible method of relinking

clips in your project with clips in a directory of your choice, using file name and timecode as the

primary criteria for reconnecting the relationship between each clip and its corresponding media

file on disk.

To relink selected clips or clips in a selected bin:


Do one of the following:

�Select one or more clips in the Media Pool browser that you want to relink, then right-click

one of the selected clips or the selected bin, and choose “Relink Selected Clips” from

the contextual menu.

�Select a bin in the Media Pool bin drop-down menu that contains clips you want to relink, then

right-click the selected bin and choose “Relink Clips for Selected Bin” from the contextual menu.


When the Relink File dialog opens, choose a volume and directory in which to look for the files

you want to relink to, and click OK. DaVinci Resolve attempts to find every clip with a matching

file name in the subdirectories of the directory you chose, using the original file paths of the clips

being relinked to do this as quickly as possible. By first looking for the clips in the directories they

were originally in, relinking can be quite fast.


If there are any clips that couldn’t be found using the method in step 2, you’re prompted with

the option to do a “deep search” by a second dialog. If you click Yes, then DaVinci Resolve will

look for each clip inside every subdirectory of the directory you selected in step 2. This may take

significantly longer, but it should be completely successful so long as the media that’s required is

within the selected directory structure.


If there are still other clips that couldn’t be found, you’re prompted to either choose another

directory altogether to continue searching, or quit.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT