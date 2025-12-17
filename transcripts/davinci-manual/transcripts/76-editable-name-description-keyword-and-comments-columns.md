---
title: "Editable Name, Description, Keyword, and Comments Columns"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 76
---

# Editable Name, Description, Keyword, and Comments Columns

In addition to the Clip Name, when the Keyword, Description and Comments columns are displayed by

the Media Pool in List view, you can edit their contents by clicking once within a clip’s Description or

Comments field, waiting a moment, and then clicking a second time to select that field.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Using Metadata View in the Media Pool

In the Metadata View mode, each clip is represented by its own card with a thumbnail and basic

clip metadata information visible. This view is designed to have more metadata information than a

thumbnail but more targeted information than the List view. This feature, combined with its sort modes,

is a powerful way to organize and reorganize your clips in the Media Pool.

The metadata fields of the Metadata view (from the top down):

�Thumbnail: A scrubbable thumbnail image of your clip.

�Row 1: A main description field that is variable and determined by the sort order selection.

�Row 2: Start Timecode, Date Created, Camera #.

�Row 3: Scene, Shot, Take.

�Row 4: Clip Name, Comment.

The Media

Sort options

The Metadata View icon view (highlighted icon in the top bar),

showing the thumbnail being scrubbed next to the clip’s metadata

The strength of the Metadata view is the automatic clustering of your clips based on the sort order

you choose in the Media Pool Sort By menu, at the very upper-right corner of the Media Pool.

Each different sort mode changes the main description field on the card, as well as re-arranging

the Media Pool to reflect the selected organization method.

The sort modes available in the Metadata view are:

�Bin: This mode clusters the clips by bin, changes the main description field to clip name, and

orders the list by timecode.

�TImecode: This mode clusters the clips by creation date, changes the main description field to

creation date and start timecode, and orders the list by timecode.

�Camera: This mode clusters the clips by camera #, changes the main description field to

camera # and start timecode, and orders the list by timecode.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

�Date Time: This mode clusters the clips by day, changes the main description field to creation date

and file name, and orders the list by timecode.

�Clip Name: This mode clusters the clips by the first letter of the clip name in alphabetical order,

changes the main description field to clip name, and orders the list by timecode.

�Scene, Shot: This mode clusters the clips by scene, changes the main description field to

scene-shot-take, and orders the list by scene-shot-take.

�Clip Color: This mode clusters the clips by clip color name, changes the main description field to

creation date and start timecode, and orders the list by timecode.

�Date Modified: This mode clusters the clips by day, changes the main description field to creation

date and file name, and orders the list by the last time the clip was modified by the OS filesystem.

�Date Imported: This mode clusters the clips by day, changes the main description field to

creation date and file name, and orders the list by the date the clip was added to the Media Pool.

�Ascending: Orders the Media Pool from lowest numerical value to highest, and

alphabetically from A to Z.

�Descending: Orders the Media Pool from highest numerical value to lowest,

and alphabetically from Z to A.

The Metadata view with clips sorted by Scene-Shot-Take

The Metadata view with the same clips sorted by Camera


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Finding Clips, Timelines, and Media

There are several ways to locate different items in the Media Pool and Media Storage, be they clips,

timelines, or media on disk.

Finding Clips and/or Timelines Within the Media Pool

Clicking the magnifying glass button at the upper right-hand corner of the Media Pool exposes the

Search Options, which by default can be used to locate one or more clips in the currently selected bin

or bins, based on the metadata that’s selected in the Filter By drop-down menu to the left of it.

The Search Options drop-down menu (as

seen in the Edit page Media Pool) lets you

choose what metadata you’re searching

A drop-down menu right next to the magnifying glass icon lets you choose the scope of your search.

This lets you choose whether a search looks through all bins in the current project for the specified

criteria, or just looks at the currently open bin, or currently selected bins in the Bin list, in cases where

you’re looking for an instance of media in a specific hierarchical location of the Media Pool.

The drop-down menu next to the magnifying glass

icon lets you set the bin search parameters

To find a clip in the Media Pool:


(Optional) Use the drop-down menu next to the Search button that exposes the Search and Filter

by controls in the Media Pool to choose whether you select All Bins or Selected Bins.


(Optional) If you’re searching Selected Bins, then open the Bin list and select one or more bins in

which to search.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA


(Optional) Choose a criteria from the Search Options drop-down menu at the top right of the Media

Pool; you can choose All Fields to do a simultaneous search of every metadata column in the

Media Pool at once, or you can choose a specific criteria to restrict your search.


Type a search term in the Search field. As soon as you start typing, all clips that don’t match the

search criteria are temporarily hidden. To show all clips in the Media Pool again, click the cancel

button at the right of the search field.

Finding Synced Audio

If you’ve synced dual-system audio and video clips together in DaVinci Resolve, you can find the audio

clip that a video clip has been synced to using the following procedure.

To find the audio clip that a video clip has been synced to:

•	 Show the Media Pool in List view, and reference file name in the Synced Audio column.

•	 Right-click a video clip that’s been synced to audio, and choose “Reveal synced audio in

Media Pool” from the contextual menu. The bin holding the synced audio clip is opened and

that clip is selected.

Finding Timeline Clips in the Media Pool

If you have a clip in a timeline and you want to find the corresponding clip that it’s conformed to in the

Media Pool, you can right-click that clip, and choose Find in Media Pool from the contextual menu.

Finding Timelines in the Media Pool

If you’d like to find the currently open timeline’s location in the Media Pool, you can choose Timeline >

Find Current Timeline in Media Pool.

Finding Media in the Media Storage Panel and Finder

If you find yourself needing to determine the location of a clip’s source media file on disk, you

can right-click an item in the Media Pool and choose Reveal in Media Storage panel. The Library

automatically opens to the folder containing the media file you’ve selected, with that media file

selected in the Library browser to the right.

Another feature that’s only available for macOS systems is the ability to right-click an item in the

Media Pool and choose Reveal In Finder. A file system window opens up, revealing the media file that

clip is linked to.

Reveal Media Pool Bin from

Multi-Bin or Search Displays

If you’ve searched for a clip and have results across multiple bins, you can now reveal where that

clip is in the Media Pool by right-clicking on the clip and selecting Reveal Media Pool Bin from the

contextual menu.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA