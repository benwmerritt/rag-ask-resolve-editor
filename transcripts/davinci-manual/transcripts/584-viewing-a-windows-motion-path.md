---
title: "Viewing a Window’s Motion Path"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 584
---

# Viewing a Window’s Motion Path

You can turn on the motion path of the window you’re tracking by choosing Show Track from the

Tracker Option menu.


Color | Chapter 140 Motion Tracking Windows

COLOR

Chapter 141

Using the Gallery

The Gallery provides a way to save, browse, and use saved still frames from

different clips in a program. Each project is saved with its own individual set of stills,

and each still you save consists of a DPX image of the saved frame, and the grade

metadata. You can use saved stills for reference when matching one clip to another,

or you can use them to copy grades to other clips, or other timelines.

There are two ways to work with the contents of the Gallery. The Color page has a small Gallery, to

the left of the Viewer, that provides quick access to saved stills and grades as you work. The Gallery

window, which can be opened via a button at the top right of the Gallery, provides a dedicated

interface for organizing your grades, copying grades and memories between projects, and for

accessing a dedicated collection of DaVinci Resolve looks.

Contents

Using the Gallery�������������������������������������������������������� 3257

Saving Stills�������������������������������������������������������������������� 3257

Selecting Stills�������������������������������������������������������������� 3258

Deleting Stills���������������������������������������������������������������� 3258

Where are Stills Saved?������������������������������������������� 3259

Changing the PowerGrade Still Directory������ 3259

Live Previews of Gallery Stills������������������������������ 3259

Hover Scrub in the Gallery������������������������������������� 3259

Playing Stills and Setting Up Image Wipes�� 3260

Timeline Wipes������������������������������������������������������������� 3261

Gang Timeline Wipe With Current Clip������������� 3261

Change a Timeline Wipe Using

the Timelines Album of the Gallery��������������������� 3261

Labeling and Searching

for Stills and Sources������������������������������������������������� 3261

Automatic Labeling���������������������������������������������������� 3262

Manual Labeling���������������������������������������������������������� 3262

Searching For Stills���������������������������������������������������� 3263

Match Reference Wipe Frame������������������������������ 3263

Gallery Options����������������������������������������������������������� 3263

Organizing Stills Using Albums�������������������������� 3265

PowerGrade Albums������������������������������������������������ 3266

Browse all Grades

from the Current Timeline�������������������������������������� 3267

The Gallery Management Window�������������������� 3267

What’s Available in the Stills Navigator����������� 3268

Browse and Import Timeline

Grades From Other Projects�������������������������������� 3269

Importing and Exporting Stills����������������������������� 3270

Using and Organizing Memories������������������������� 3271


Color | Chapter 141 Using the Gallery

COLOR

Using the Gallery

The Gallery in the Color page and the expanded Gallery window environment share many of the same

commands for organizing stills. However, the commands for saving stills and customizing split-screen

views are restricted to the Color page.

Color page Gallery

Saving Stills

One of the most common operations is to save a clip as a still (with that clip’s embedded grade) for

future reference and use.

To save an individual still in the Color page, do one of the following:

�Choose Color > Stills > Grab Still (Option-Command-G).

�Right-click on the Viewer and choose Grab Still.

�Press GRAB STILL on the Transport panel of any of the DaVinci Resolve control panels.

It’s also possible to save stills automatically for every clip in the entire Timeline. This can be useful if

you’re planning to export a set of grades to hand off to another colorist, or if you need to apply a series

of grades manually from one project to another when ColorTrace™ won’t work.

To save a still for every clip in the current timeline,

right-click the Viewer, and choose one of the following:

�Grab All Stills > From First Frame: The first frame of each clip is saved to the Gallery.

�Grab All Stills > From Middle Frame: The middle frame of each clip is saved to the Gallery.

�Grab Missing Stills > From First Frame: Only the first frame of clips with no stills in the Gallery are

saved to the Gallery.

�Grab Missing Stills > From Middle Frame: Only the middle frame of clips with no stills in the

Gallery are saved to the Gallery.


Color | Chapter 141 Using the Gallery

COLOR

You can cancel the Grab All Stills operation at any time by clicking on the Cancel button in the

“grabbing stills” dialog box. This is useful if you notice a clip needs to be altered after starting the tool,

and you don’t want to wait for the operation to finish grabbing stills from the entire timeline before

fixing it. Once you’ve made your correction, simply run Grab All Stills again.

By default, when you save one or more stills, they’re named “TrackNumber.ShotNumber.

VersionNumber” with dots separating each number. If you like, you can choose an option from the

General Options panel of the Project Settings to “Automatically label Gallery stills” in different ways.

This is covered in more detail later in this chapter.

Selecting Stills

To select a range of stills, do one of the following:

�Click one still, then Shift-click another to select a contiguous range of stills.

�Command-click any stills you like to make a noncontiguous selection.

�Right-click any still, and choose one of the following commands;

Select All: Selects every clip in the Gallery.

Select Current to Last: Selects every still from the one you’ve clicked through the

last still in the Gallery.

Select First to Current: Selects every still from the one you’ve clicked through the

first still in the Gallery.

Deleting Stills

If you need to remove one or more stills, this can only be done using the Gallery’s contextual menu.

To delete one or more stills, do one of the following:


Select one or more stills in the Gallery.


Right-click one of the selected stills and choose Delete Selected.

Each still is also saved with a variety of metadata that is used by DaVinci Resolve to manage

the contents of the Gallery in different ways. This metadata can also be used for searching and

sorting, and is viewable by opening the Still Properties window.

To display a still’s properties:

Right-click a still in the Gallery and choose Properties.

A floating translucent window appears displaying the date the still was created, what clip it

was grabbed from, when it was grabbed, and the source and record timecode values of the

frame it came from.

Right-click on a still to choose Still Properties


Color | Chapter 141 Using the Gallery

COLOR

Where are Stills Saved?

By default, all grades/stills you save are saved in the DPX format, and are placed in the directory

path defined in the “Gallery stills location” field in the Working Folders section of the Master Settings

panel of the Project Settings. This path defaults to a hidden “.gallery” directory that’s created at the

location of the first Media Storage Volume you specify in the Media Storage panel of the System

Preferences window.

Changing the PowerGrade Still Directory

Optionally, you can change the location where PowerGrade stills are saved by Opening the Gallery

Option menu and choosing Change PowerGrades Path. You’ll be prompted via a “Select PowerGrades

Folder” dialog to choose a directory where all PowerGrades will be saved.

Live Previews of Gallery Stills

The Live Preview option, found in the Gallery option menu, lets you preview how the current clip would

look with a particular Gallery Still grade applied to the currently selected clip simply by moving the

pointer over the still you want to preview.

Enabling and Disabling the Gallery Live Preview:


Open the Gallery option menu and choose Live Preview.

The Live Preview option for the Gallery browser lets

you hover over a saved grade to preview it on

the current clip in the Viewer


Click a node in the Node Editor you want to preview applying the grade from a still to. The live

preview will display how the current clip will appear with the grade of the still you select applied to

the currently selected node of current grade, which will affect the result.


Move the pointer over the still you want to preview.

The Viewer image updates to show how that clip would look with that still’s grade applied to the

currently selected node.

Hover Scrub in the Gallery

When Live Preview is enabled in the Gallery option menu, the Hover Scrub Preview submenu lets you

choose how you want Live Preview to be shown by a thumbnail in the Gallery and in the Viewer when

you hover the pointer over a still or LUT in the LUT Browser:

�You can choose to scrub both the thumbnail you’re hovering over and the Viewer, letting you

preview the current still’s grade or a LUT over the duration of the current clip in both the thumbnail

and Viewer.

�You can choose to scrub just the thumbnail, leaving the Viewer to show just the grade or LUT over

the frame at the position of the playhead.


Color | Chapter 141 Using the Gallery

COLOR

�You can disable scrubbing altogether, in which case both the thumbnail and the Viewer will only

show the grade or LUT over the frame at the position of the playhead.

The Hover Scrub Preview options when Live Preview is enabled