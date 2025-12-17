---
title: "Face Detection to"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 79
---

# Face Detection to

Generate People Keywords

You can select multiple clips in the Media Pool, then right-click the selection and choose AI Tools >

Analyze clips for people from the context menu to automatically analyze all selected clips using the

DaVinci Neural Engine, identifying faces that can be used to help organize the media. A progress

dialog shows you how long until the analysis is finished (you can cancel the operation if necessary).

Afterwards, the People Management window appears that shows you the results, automatically

organized into a number of bins in a sidebar.

�A “People” bin shows each face that has been recognized as an individual person. Click, pause,

then click again underneath any thumbnail to edit the name or role of that person. You must assign

a name if you want a keyword to appear for that individual in the People field of the Metadata

Editor. Assigning names renames the bins corresponding to each found person and enables

retagging to fix mistaken identification.

The Face Recognition window seen immediately after a Face Recognition operation


Ingest and Organize Media | Chapter 19 Using Clip Metadata

MEDIA

�Individual bins collect all clips with a particular person, allowing you to evaluate whether or not the

contents have been identified correctly. If you see an incorrectly identified clip, you can right-click

it and re-tag it from the contextual menu, or choose “Untag” if it’s a new person that has not been

identified at all.

A bin for a particular person lets you evaluate the contents

�An “Other People” bin shows all faces that could not be identified. You can right-click any of these

to re-tag it as one of the people that have been already identified, or you can choose New Person

if it’s someone who wasn’t initially identified (this sometimes happens when multiple people have

very similar features).

The Face Recognition window seen immediately after a Face Recognition operation


Ingest and Organize Media | Chapter 19 Using Clip Metadata

MEDIA

Clicking the Close button closes this window and assigns the names you edited as keywords to

the People field of the “Shot & Scene” group in the Metadata Editor. Clips with multiple people

who have been identified have multiple keywords assigned.

The People keywords field of the Shot & Scene group in the

Metadata Editor, populated with who is in that shot

Once People keywords are assigned to one or more clips, a People smart category of smart

bins can automatically be created in the Smart Bins sidebar of the Media Pool, making it easy to

immediately begin finding clips that have specific people in them. To create this People Smart Bin,

select “Automatic Smart Bins for People Metadata” box in the Preferences > User > Editing window.

You can reopen the Face Recognition window at any time to make modifications by choosing

Workspace > People. You can reset all faces by clicking the People Management Option menu

and choosing “Reset Face Database.”

NOTE: A command in the Option menu of the Face Recognition window, Reset Face

Database, lets you reset all analyzed results if the results are not acceptable and you don’t

want to save the resulting metadata.

Creating Custom Metadata Groups

The Metadata panel in the User Preferences lets you create custom sets of metadata parameters

that will be exposed in the Metadata Editor. Using this panel, you can create customized subsets of

metadata that are focused on your particular needs.

Presets that you create are available from the Option menu that’s just to the left of the Metadata

categories drop-down menu.

Choose any custom preset to restrict the Metadata Editor to only showing the metadata fields in that

preset. To see the full set of custom metadata fields you’ve saved to a particular preset, you should

set the Metadata Categories drop-down menu to All Groups. To make the full set of metadata fields

reappear, just choose default presets in the same drop-down.


Ingest and Organize Media | Chapter 19 Using Clip Metadata

MEDIA

Custom Metadata Categories drop-down menu

Making and managing metadata presets is simple.

To create a new metadata preset:


Open the Metadata panel of the User pane of the Preferences window, and click New.


Click the checkboxes of every metadata tag you want to include in this preset, or click the

checkbox of a group name on the list to include all metadata tags within it.

Every single metadata tag available in DaVinci Resolve appears within one of several groups that

appear as a list. To open any group to see its contents, move the pointer over that group’s entry

on the list, and click the Open button when it appears.


When you’re finished, click the Save button under Metadata Options.


Click the Save Button for the User Preferences.

To edit an existing metadata preset:


Select a preset from the list, and click Edit.


Turn checkboxes on and off to include or exclude whatever tags you need.


Click the Save button under Metadata Options.


Click the Save Button for the User Preferences.

To delete a metadata preset:

�Select a preset from the list and click Delete.

Importing and Exporting

Media Pool Metadata

Once you’ve taken the trouble to add metadata to the clips in your project, DaVinci Resolve makes

it possible to export metadata from the Media Pool of one project for import into the clips of another

project, for instances where you need to move metadata around.

For example, a DIT might have entered a lot of metadata to the DaVinci Resolve project used for

generating dailies, but then an impatient editor might have created a separate project to begin editing

those dailies. Instead of requiring the editor to enter each clip’s metadata all over again, you can

export the metadata from the DIT’s project and import it into the editor’s new project, automatically

matching the relevant metadata to each corresponding clip.


Ingest and Organize Media | Chapter 19 Using Clip Metadata

MEDIA

To export Media Pool metadata:


Open a project containing Media Pool metadata you want to export.


Optionally, select which clips in the Media Pool you want to export metadata for.


Choose File > Export Metadata From > Media Pool to export metadata from every clip in the Media

Pool, or choose File > Export Metadata From > Selected Clips to only export metadata from clips

you selected in step 2.


When the Export Metadata dialog appears, enter a name and choose a location for the file to be

written, then click Save. All metadata is exported into a .csv file that can be viewed and/or edited

in any spreadsheet application.

If you open the resulting metadata .csv file, the first line is a header that lists what metadata is to be

found for each item listed in this document, and in what order. Only metadata fields that have been

populated for at least one clip are exported and listed in this header; unused metadata fields in the

Metadata Editor or Media Pool are ignored.

This file can now be imported into another project file to reattach the metadata to the same clips.

To import Media Pool metadata:


Open a project containing clips you want to populate with imported metadata.


Optionally, select which clips in the Media Pool you want to import metadata to.


Choose File > Import Metadata To > Media Pool to import metadata to potentially every clip in the

Media Pool, or choose File > Import Metadata To > Selected Clips to only import metadata to clips

you selected in step 2.


When the Import Metadata dialog appears, choose a metadata .csv file to import, and click Open.


When the Metadata Import dialog appears, choose the Import Options you want to use to

match the .csv file’s metadata to the correct clips in the currently open project. By default,

DaVinci Resolve tries to use “Match using filename” and “Match using clip start and end

Timecode” to match each line of metadata in the .csv file with a clip in the Media Pool, but there

are other options you can use such as ignoring file extensions, using Reel Name, and using source

file paths.


Next, choose which Merge Option you want to use in the Metadata Import dialog.

There are three options:

Only update metadata items with entries in the source file: The default setting. Only updates a

clip’s metadata if there’s a valid entry in the imported .csv file. Other clip metadata fields are left as

they were before the import.

Update all metadata fields available in the source file: For each clip that corresponds to a line

of metadata in the imported .csv file, every single metadata field referenced by the .csv file is

overwritten, regardless of whether or not there’s a valid entry for that field.

Update all metadata fields available in the source file and clear others: For each clip that

corresponds to a line of metadata in the imported .csv file, every single metadata field referenced

by the .csv file is overwritten, regardless of whether or not there’s a valid entry for that field.

Furthermore, metadata fields that aren’t referenced by the imported .csv file are cleared of

whatever metadata was there before.


When you’re finished choosing options, click Ok and all available metadata from the source .csv

file will be imported.


Ingest and Organize Media | Chapter 19 Using Clip Metadata

MEDIA

The Metadata Import dialog that lets you choose

options for how to match and merge imported metadata