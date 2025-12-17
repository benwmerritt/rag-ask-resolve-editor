---
title: "Exporting to CDL"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 739
---

# Exporting to CDL

DaVinci Resolve can export and import basic grading data to and from other applications via a Color

Decision List (CDL). CDLs are an industry-standard file format originally developed by the American

Society of Cinematographers’ technology committee. DaVinci Resolve supports the 1.2 CDL standard

that defines the slope, offset, and power for each of the red, green, and blue channels, as well as the

overall saturation of each clip in a program.

CDL files are formatted similarly to EDLs, with SOP (Slope/Offset/Power), and SAT (Saturation) values

embedded as metadata in much the same way as comments are in a more typical EDL.

Here’s an example of a single CDL event:

020 001 V C 03:02:49:13 03:02:53:00 01:01:28:11 01:01:31:22

*ASC_SOP (1.109563 1.717648 0.866061)(-0.238880 -0.390357 0.353743)

(0.672948 1.384022 0.889876)

*ASC_SAT 1.000000

Because the CDL definition of a grade is so narrow, projects you’re planning to export to other

applications via a CDL must be constrained to only those operations the CDL mathematically defines.

Here are some things to keep in mind:

�Only primary corrections in the first node of each clip are exported.

�Restrict yourself to using the Lift/Gamma/Gain, Offset, and Saturation controls.

�Keyframes are never exported. If keyframes are present in a grade, only the parameter values at

the first frame of the clip are used.

�The track grade and group grades are completely ignored.

�If there is an HSL Qualifier or a Power Window in the first node, it is ignored and the corrections in

that node are exported as if it were a primary correction.

�Do not make Y’ only adjustments; they’re not compatible with CDLs. To ensure that your exported

CDL is accurate, set the Lum Mix parameter in the Primary Controls palette for each grade to 0.

For workflows involving frequent CDL export, you can turn on the “Luminance Mixer defaults

to zero” option in the Color  section of the General Options panel of the Project Settings to

guarantee this parameter is always set to 0.

If your timeline conforms to all of these restrictions, then you’re ready to export a CDL.

To export a CDL:


Open the Edit page, right-click the Timeline you want to export in the Media Pool, and choose

Timelines > Export > CDL from the contextual menu.


Enter a name for the CDL, choose a location to save it to, and click OK.

For more information on importing a CDL to add grades to your project, see Chapter 149,

“Copying and Importing Grades Using ColorTrace.”


Deliver | Chapter 190 Exporting Timelines to Other Applications

DELIVER

Exporting the Edit Index

as a CSV or TXT File

You can export the current contents of the Edit Index, in the Edit page, as a self-contained file to use

for reference in a variety of ways.

To export the Edit Index:


Open the Edit Index, and choose one of the Edit Index filters from the Edit Index option menu,

if necessary. For example, you could filter the edit index by Offline Clips Only if you wanted to

export a list of all offline clips in the current timeline.


Right-click that timeline in the Media Pool, and choose Timelines > Export > Edit Index, then

choose a location and export format from the Export Edit Index dialog, and click Save.

Exporting to ALE

DaVinci Resolve is also capable of exporting ALE (Avid Log Exchange) files. ALE is a tab-delimited,

ASCII text-based clip logging list format that enables the exchange of clip metadata that can’t be

embedded inside MXF files. ALE files are designed to let you export a log of all clips that are used in a

particular timeline with all of the metadata that’s associated with those clips in DaVinci Resolve, so this

metadata can be imported into and associated with clips inside Media Composer or Symphony.

ALE files are divided into three sections, labeled Heading, Column, and Data:

�The Heading provides information about the clips being logged, including the picture and audio

format, and the frame rate.

�The Column line defines each of the columns of metadata being exported in the list. There’s an

automatic minimum of metadata columns that are automatically included, regardless of whether

they’re populated or not. However, additional metadata columns are automatically added to

this list by DaVinci Resolve when any corresponding metadata field in the Metadata Editor is

populated. For example, if you enter information into the Camera, Keyword, and Shot fields of

the Metadata Editor, then those columns will be added to the exported ALE. There are no user

settings that control this.

�The Data section contains multiple lines, one for each event being referenced in the list, that

contain all the data corresponding to that clip.

If you’re exporting stereoscopic clips from stereoscopic timelines, the following additional columns of

metadata are automatically included in the two ALE files that are generated:

�Pan (relative to timeline resolution)

�Tilt (relative to timeline resolution)

�Zoom

�Rotate

�Convergence (relative to timeline resolution)

�HFlip (0 or 1)

�VFlip (0 or 1)

If you’re exporting ALE files from projects using ARRIRAW clips, the following additional columns of

metadata can be included:

�Temperature

�Tint


Deliver | Chapter 190 Exporting Timelines to Other Applications

DELIVER

To export an ALE file:


Open the Edit page, right-click the Timeline you want to export in the Media Pool, and choose

Timelines > Export > ALE from the contextual menu.


Enter a name for the ALE file, choose a location to save it to, and click OK.

The ALE file is saved, and a dialog appears reminding you of the file path to which it was saved

(click OK to dismiss it).

Here’s an example of a short ALE export:

Heading

FIELD_DELIM

TABS

VIDEO_FORMAT


AUDIO_FORMAT

48khz

FPS

23.976

Column

Name, Tracks, Start, End, Take, Tape, UNC, FPS, Reel, Scene, Shoot, date,

Manufacturer, Source Resolution, Source, Bit Depth, DESCRIPT, Comments,

Audio SR, Audio Bit Depth, Auxiliary TC1, KN Start, Source File Path,

Display Name

Data

A001_C002_V01.CBF6A4FD139AD.mxf, V, 10:28:27:03, 10:28:28:00,

A001_C002_V01.CBF6A4FD139AD

/Volumes/Disk_1/Avid MediaFiles/MXF/1/A001_C002_V01.CBF6A4FD139AD.mxf

23.98, DaVinci Resolve, 1920x1080, 10

/Volumes/Disk_1/Avid MediaFiles/MXF/1/A001_C002_V01.CBF6A4FD139AD.mxf

A001_C002_V01.CBF6A4FD139AD

A016_C008_V01.CBF6A4FD13ABD.mxf,V, 23:35:56:03, 23:36:00:11,

A016_C008_V01.CBF6A4FD13ABD

/Volumes/Disk_1/Avid MediaFiles/MXF/1/A016_C008_V01.CBF6A4FD13ABD.mxf

23.98, DaVinci Resolve, 1920x1080, 10

/Volumes/Disk_1/Avid MediaFiles/MXF/1/A016_C008_V01.CBF6A4FD13ABD.mxf

A016_C008_V01.CBF6A4FD13ABD

A004_C012_V01.CBF6A4FD1438E.mxf, V, 14:07:31:21, 14:07:35:15,

A004_C012_V01.CBF6A4FD1438E

/Volumes/Disk_1/Avid MediaFiles/MXF/1/A004_C012_V01.CBF6A4FD1438E.mxf

23.98, DaVinci Resolve, 1920x1080, 10

/Volumes/Disk_1/Avid MediaFiles/MXF/1/A004_C012_V01.CBF6A4FD1438E.mxf

NOTE: The commas shown above are not normally in the ALE but shown here for field clarity.


Deliver | Chapter 190 Exporting Timelines to Other Applications

DELIVER

Exporting to ALE with CDL

Avid Media Composer and Symphony also support the import of ALE files with additional CDL

metadata columns with which to associate SOP (Slope/Offset/Power) and SAT (Saturation) adjustment

metadata to each clip that’s logged in the ALE.

When you import an ALE with CDL file into Media Composer, the SOP and SAT data populate

metadata columns for preservation and export in various Avid workflows. Here’s an example of the

Heading, Column, and Data sections of a sample ALE with CDL, with one line of clip and CDL data.

To export an ALE with CDL file:


Open the Edit page, right-click the Timeline you want to export in the Media Pool, and choose

Timelines > Export > ALE and CDL from the contextual menu.


Enter a name for the ALE file, choose a location to save it to, and click OK.

The ALE file is saved, and a dialog appears reminding you of the file path to which it was saved

(click OK to dismiss it).

Here’s an example of a short ALE with CDL export:

Heading

FIELD_DELIM

TABS

VIDEO_FORMAT


AUDIO_FORMAT

–

FPS

23.976

Column

Name, Tracks, Start, End, Take, Tape, UNC, FPS, Reel, Scene, Shoot date,

Manufacturer, Source Resolution, Source Bit Depth, DESCRIPT, Comments,

Audio SR, Audio Bit Depth, Auxiliary TC1, KN Start, Source File Path,

Display Name KeyKode, ASC_SOP, ASC_SAT, RESOLVE_SIZING

Data

A001_C002_V01.CBF6A4FD139AD.mxf, V, 10:28:27:03, 10:28:28:00,

A001_C002_V01.CBF6A4FD139AD

/Volumes/Disk_1/Avid MediaFiles/MXF/1/A001_C002_V01.CBF6A4FD139AD.mxf

23.98, DaVinci Resolve, 1920x1080, 10

/Volumes/Disk_1/Avid MediaFiles/MXF/1/A001_C002_V01.CBF6A4FD139AD.mxf

A001_C002_V01.CBF6A4FD139AD

(1.0260 1.0260 1.0260)(-0.0260 -0.0260 -0.0260)(0.8237 0.8237 0.8237) 0.8640

(0.0000 0.0000 1.0000 0.0000 0.0000 0 0)

NOTE: The commas shown above are not normally in the ALE but shown here for field clarity.


Deliver | Chapter 190 Exporting Timelines to Other Applications

DELIVER

Exporting Timeline Markers to EDL

This command lets you export a quick report listing the text of all markers that have been added to

the Timeline as notes in an EDL. Clip markers are ignored. This report is in EDL format, with one event

for each Timeline marker, with a placeholder reel number (001 by default), and source and record

timecodes that correspond to each marker’s position in the Timeline (with a duration of one frame). An

EDL note for each event lists the Marker note, if there is one. There is no note available for the color of

the markers

Here’s an example of an exported Timeline Marker EDL:

TITLE: ( no title )

001  001

V

C

01:00:09:09 01:00:09:10 01:00:09:09 01:00:09:10

Replace with another car door sound effect

002  001

V

C

01:00:20:12 01:00:20:13 01:00:20:12 01:00:20:13

Trim this clip shorter

003  001

V

C

01:00:30:12 01:00:30:13 01:00:30:12 01:00:30:13

Find another stock footage clip of the bridge

004  001

V

C

01:00:30:13 01:00:30:14 01:00:30:13 01:00:30:14

Trim this montage three seconds shorter

Exporting and Importing

Media Pool Metadata

DaVinci Resolve makes it possible to export metadata from the Media Pool of one project for import

into the clips of another project, for instances where you need to move metadata around. This process

exports all metadata from the Media Pool as a .csv file.

For example, a DIT might have entered a lot of metadata to the DaVinci Resolve project used for

generating dailies, but then an impatient editor might have created a separate project to begin editing

those dailies. Instead of requiring the editor to enter each clip’s metadata all over again, you can

export the metadata from the DIT’s project and import it into the editor’s new project, automatically

matching the relevant metadata to each corresponding clip.

To export Media Pool metadata:


Open a project containing Media Pool metadata you want to export.


Optionally, select which clips in the Media Pool you want to export metadata for.


Choose File > Export Metadata From > Media Pool to export metadata from every clip in the Media

Pool, or choose File > Export Metadata From > Selected Clips to only export metadata from clips

you selected in step 2.


When the Export Metadata dialog appears, enter a name and choose a location for the file to be

written, then click Save. All metadata is exported into a .csv file that can be viewed and/or edited

in any spreadsheet application.


Deliver | Chapter 190 Exporting Timelines to Other Applications

DELIVER

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

clip’s metadata if there’s a valid entry in the imported .csv file. Other clip metadata fields are left as

they were before the import.

Update all metadata fields available in the source file:  For each clip that corresponds to a line

of metadata in the imported .csv file, every single metadata field referenced by the .csv file is

overwritten, regardless of whether or not there’s a valid entry for that field.

Update all metadata fields available in the source file and clear others:  For each clip that

corresponds to a line of metadata in the imported .csv file, every single metadata field referenced

by the .csv file is overwritten, regardless of whether or not there’s a valid entry for that field.

Furthermore, metadata fields that aren’t referenced by the imported .csv file are cleared of

whatever metadata was there before.

The Metadata Import dialog that lets you choose options for

how to match and merge imported metadata


The Metadata Import dialog that lets you choose options for how to match and merge

imported metadata


When you’re finished choosing options, click Ok and all available metadata from the source .csv

file will be imported.


Deliver | Chapter 190 Exporting Timelines to Other Applications

DELIVER

DELIVER