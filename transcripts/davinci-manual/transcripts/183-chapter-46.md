---
title: "Chapter 46"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 183
---

# Chapter 46

Media Management

Media Management in DaVinci Resolve refers to operations that let you copy

or transcode the media that’s linked to clips in your timeline, with the option to

eliminate unused media in the process.

Media Management is used to consolidate media from an edited timeline or from a

project nearing completion.

Contents

What Is Media Management in DaVinci Resolve?��������������������������������������������������������������������������������������������������������������� 994

Media Management of Timelines Creates .drt Files���������������������������������������������������������������������������������������������������������� 994

File Formats That Are Compatible With Media Management�������������������������������������������������������������������������������������� 995

Using Media Management�������������������������������������������������������������������������������������������������������������������������������������������������������������� 995

Continuing Media Management Jobs on Error��������������������������������������������������������������������������������������������������������������������� 999

Options in the Media Management Window������������������������������������������������������������������������������������������������������������������������� 999

Options for Transcode Only����������������������������������������������������������������������������������������������������������������������������������������������������������� 1000

File Naming When You Consolidate Media�������������������������������������������������������������������������������������������������������������������������� 1000


Edit | Chapter 46 Media Management

EDIT

What Is Media Management

in DaVinci Resolve?

If you’ve edited a program within DaVinci Resolve, you can use the Media Management command to

take care of a variety of tasks, including but not limited to:

�Creating a duplicate of your project’s clips that eliminates unused media in preparation for handing

the media off to another facility.

�Transcoding all clips in a timeline to another format while eliminating unused heads and tails.

For example, if you’re preparing to export a project to hand off to another DaVinci Resolve

user somewhere else, or even an XML or AAF to give to someone using a completely

different NLE or finishing application, you can use Media Management in DaVinci Resolve

to consolidate and relink the media used by the timeline you’re handing off, so the exported

project or timeline references a smaller set of media.

Even if you’re not handing a project off, if you’ve ingested an enormous amount of source

media into a project, and after the majority of the editing decide that you want to create a

consolidated set of the media you’re using in order to lighten the project’s load in the Media

Pool, you can create a duplicate of the media to reconform to, omitting unused clips and

trimming the unused heads and tails of the clips you are using in the process.

But Media Management isn’t just useful for projects you’ve edited in DaVinci Resolve. For

example, if you’re importing a project from another application and you’ve been given an

enormous amount of source media to conform to, you may be hesitant to copy all of it to your

accelerated storage volume, since (a) most of it is probably unused by the project file you’ve

been given, (b) it’ll take forever to copy from the cheap USB 2 hard drive they’ve given you,

and (c) it will clog up your local storage, taking valuable space away from other projects. In this

case, you can use the Media Management to copy a reduced set of media files consisting of

only the clips used in the current timeline of the Edit page.

Media Management of Timelines

Creates .drt Files

When performing Media Management operations to copy or transcode media from a timeline, a

DaVinci Resolve Timeline (.drt) file is automatically created in the same bin as the resulting media files,

linked to the newly created media. This timeline can then be imported into the same or a new DaVinci

Resolve project.


Edit | Chapter 46 Media Management

EDIT

File Formats That Are Compatible

With Media Management

No matter what you use if for, Media Management is designed to work with all video formats that are

have decode support within DaVinci Resolve, and is capable of outputting a few more formats than the

Deliver page can. Compatible formats include but are not limited to:

�QuickTime

�MXF

�R3D

�Image-based raw media

formats including Blackmagic RAW

and Alexa raw

�DPX, EXR, JPEG 2000, TIFF, Cineon, and

other compatible image sequence formats

�AVI

�H.264

�XAVC

�AVC-Intra

In addition, the “trim unused media” options of the Copy or Move operations are now compatible

with clips that use codecs employing temporal compression, such as H.264, XAVC, and AVC-Intra,

mp3, Flac, and QuickTime, enabling you to eliminate unused media for these formats during media

management without recompressing or transcoding.

Using Media Management

Using Media Management is simple.

To media manage clips and timelines in a project you’ve created:


Select the items you want to media manage, either clips or one or more Timelines.


Choose File > Media Management, and the Media Management window appears.

Media Management window


Edit | Chapter 46 Media Management

EDIT


Choose the scope of the Media Management operation, shown at the top of the window. You

can choose to affect the Entire Project, only one or more Timelines, or only Clips. What you had

selected prior to opening the Media Management window affects the scope that is selected when

you open this window, but it doesn’t limit to operation to only the selected items. So, if nothing

was selected in the Media Pool, then “Entire Project” is automatically highlighted. If any clips were

selected, then “Clips” is highlighted automatically. If any Timelines were selected, then “Timelines”

is highlighted. However, if for whatever reason the wrong option is highlighted, you need only click

the option you want to select it instead.

Media Management scope options


Next, choose which operation you want to perform:

Copy: Creates duplicates of all media associated with clips or timelines at the destination.

Transcode: Creates duplicates of all media associated with clips or timelines in a new format that

you specify; all transcoded clips are written to the same destination.

Media Management operations


Click the Browse button and use the File Destination dialog to choose a location for the managed

media to be written. The file path of this location appears in the Media Destination field.


Choose the options associated with the operation you selected. If you choose to media manage

Timelines, then a Timeline Selection option lets you choose which Timelines you want to include

in this operation. The current size of the selected media is listed below, alongside an estimate of

the size of the media after the operation you’ve selected. Depending on which options you select,

the estimate may be larger or smaller, but this will show you if you need to change the selected

options to achieve a more desirable final size.


Edit | Chapter 46 Media Management

EDIT

Media Management options shown for copying

trimmed media from a specific timeline


When you’ve finished choosing options, click Start. A progress bar appears showing you how long

the operation will take.

The following workflow illustrates how you can use Media Management to cut down the amount of

media you need to deal with when you’re conforming a project imported from elsewhere, and you’ve

been given far more media then you actually need, because you only need what’s actually in the

timeline you’re importing.

To use Media Management to create a consolidated

duplicate of media for a project you’re conforming:


Connect the portable drive containing the media to be conformed to your workstation.


Import the AAF or XML project file you were given into the Edit page, and conform it to the media

on the portable drive you connected in step 1. You’re only doing this to identify what clips you

need to media manage, not because you’ll be working off that volume.


Choose File > Media Management. The Media Management window appears.


Choose Timelines at the top of the window, and then open the Timeline selection section and turn

on the checkbox of the timeline you want to consolidate the media for.


Click the Browse button and choose the volume you want to write the consolidated media to.


Edit | Chapter 46 Media Management

EDIT


Choose the following options for consolidating the media. For this operation, you’ll want to enable:

�Click the Browse button, and choose the accelerated storage volume you’re using for all media

you’re using with DaVinci Resolve.

�Choose the “Timelines” Media Management scope, if it’s not selected already, to manage all

media from the selected timeline.

�Choose “Copy” to make a duplicate of the media from the portable storage volume to your

accelerated storage.

�Choose “Copy and trim used media keeping 12 frame handles” if you’re comfortable

with 12 frame handles.

�Turn on “Consolidate multiple edit segments into one media file” if you don’t mind having larger

media files that preserve the relationship of what clips come from which single media files. This

can make grading simpler later on.

�Turn on “Relink to new files” to automatically relink the timeline you’ve selected to the new

media that’s being generated.

The Consolidate dialog lets you choose how and

where to copy the trimmed media.


When you’re done choosing these settings, click Start. A progress bar appears showing you how

long the operation will take.

A subset of media used by that timeline is copied to the specified directory, and a DaVinci Resolve

Timeline (.drt) is automatically generated that is relinked to the timeline and clips in the Media Pool.

You are now ready to continue working on the project.


Edit | Chapter 46 Media Management

EDIT