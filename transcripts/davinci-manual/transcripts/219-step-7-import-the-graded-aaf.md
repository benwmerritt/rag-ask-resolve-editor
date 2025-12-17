---
title: "Step 7 – Import the Graded AAF"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 219
---

# Step 7 – Import the Graded AAF

Reopen the original project in Media Composer. If the media in the new directory of the

Avid MediaFiles folder is in a compatible format, it will automatically be added to the internal

database of media.


Create a new bin to contain the graded sequence you’re about to import.


Open the new bin, then choose File > Input > Import Media, select the graded AAF file that you

exported from DaVinci Resolve, and click Open.


As long as the media is available in the Avid MediaFiles directory, the new bin you’ve created

should automatically fill up with the clips that were rendered out of DaVinci Resolve, and a new

sequence should appear.


Double click the sequence you’ve imported to open it into the Record monitor and Timeline, fully

conformed with the color corrected clips from DaVinci Resolve. This sequence is now ready for

finishing in Media Composer.

Relinking Transcoded Media to AMA Media

This next workflow is useful when you’ve been editing transcoded, offline versions of processor- or

bandwidth-intensive media, but you want to send the original high-quality source media (such as

ALEXA or RED raw files) to DaVinci Resolve for grading. In certain situations, it may be better to

reconform your sequence to the original AMA-linked media files in Media Composer before you round

trip from Media Composer to DaVinci Resolve.

Step 1 – Relink Your Transcoded Media to AMA-Linked Source


Edit a sequence using media that you’ve transcoded within Media Composer.


When you’re finished, open the bin that contains your project’s camera original media, and select

the AMA-linked clips that correspond to the transcoded clips you’ve been editing.


Right-click the edited sequence in its bin, and choose Relink from the contextual menu.


When the Relink dialog appears, turn on “Select items in ALL open bins.” Select “Tape Name

or Source File Name” under the Source Name settings, and leave the “Create new sequence”

checkbox turned on.

A new sequence is created that is now linked to the AMA-linked camera originals.

Step 2 – Export an AAF File


Select the new sequence that was created, and choose File > Output > Export to File.


Type a new name, choose a location for the file, and click Options.


Choose AAF from the Export As pop-up menu, and choose “Link to (Don’t Export) Media” from the

Export Method pop-up menu.


Click Audio Details, and choose “Link to (Don’t Export) Media” from the Export Method pop-up menu.


Click Save to exit the Export Settings dialog, and then click Save again to export the file.


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT

Step 3 – Import the AAF, Grade, Render, and Export


Open DaVinci Resolve, and import the AAF file you exported into the Edit page. You’ll need to

manually select the media in a second dialog.


Grade the project as you would any other.


When you’re done grading, use the AAF Round Trip option in the Deliver page to render the

graded media into a new (numbered) directory in the Avid MediaFiles directory.


Open the Edit page, select the original AAF timeline you imported, right-click it, and choose

Export AAF/XML. Pick a location for the file and click Save.

Step 4 – Reimport the AAF into Media Composer/Symphony

Open Media Composer, and import the AAF you exported from DaVinci Resolve. Your graded

sequence is now ready for finishing.

Audio AAF Import from Pro Tools

Importing audio AAF timelines from Pro Tools (or any DAW software capable of exporting AAF)

works similarly to the workflow for importing a video AAF from Media Composer that’s detailed at the

beginning of this chapter. However, there are two methods you can use.

Import AAF, EDL, XML

Using the File > Import Timeline > Import AAF, EDL, XML command (Command-Shift-I), you can select a

Pro Tools AAF. You’re presented with all the same import options as a Media Composer AAF, but what

you end up with is an audio-only timeline, to which you can add a reference video if you need to.

Import AAF to Current Timeline

Using the File > Import Timeline > Import AAF to Current Timeline command lets you import an audio

AAF to the currently open timeline. When you use this command, the import dialog presents similar

import options, however, there are two additional options to choose from.

Additional options available when you use the

“Import AAF to current timeline” command

The “Import AAF to current timeline” checkbox is on, and presents two options:

�Insert Additional Tracks: Lets you import the audio tracks starting at the beginning of the current

timeline, placing them underneath the lowest track with existing audio in the Timeline.

�Insert with offset: Lets you import the audio tracks with a specified offset from the beginning of

the Timeline.


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT

Chapter 60

Conforming

EDL Files

The edit decision list (EDL) is the lowest common denominator project exchange

format there is, and most professional post-production applications are capable

of exporting and importing projects in this format, including Media Composer,

Autodesk Flame Premium, and the legacy Final Cut Pro 7.

This chapter covers all workflows that let you import and conform timelines using the EDL format.

Contents

Conforming EDL Files������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1197

EDL Export of a Project and Its Media������������������������������������������������������������������������������������������������������������������������������������� 1198

Conforming EDLs to Individual Media Files�������������������������������������������������������������������������������������������������������������������������� 1198

Preconforming “Flat” Media Files to EDLs����������������������������������������������������������������������������������������������������������������������������� 1199

Override Input Color Space of Clips in Preconform Workflows Using Color Management������������������������ 1200

Conforming “Flat” Media Files Using Split and Add�������������������������������������������������������������������������������������������������������� 1200

Importing an EDL to a New Track����������������������������������������������������������������������������������������������������������������������������������������������� 1201


Import and Conform Projects | Chapter 60 Conforming EDL Files

EDIT

Conforming EDL Files

DaVinci Resolve supports the CMX 3600 format for EDL import and export. The universality of EDLs

is due, in part, to their longevity; different EDL formats have been in use for decades. It’s also due to

their simplicity. At least as used by DaVinci Resolve, EDLs describe a very narrow range of editorial

information, including clip arrangement, clip name (via embedded comments), video transitions (cuts or

dissolves), and linear speed settings (percentage of fast forward or slow motion).

Another limitation is that EDLs only support a sequence of shots on a single video track. If you need to

move projects with multiple tracks of audio and video, then you can export each track as a separate

EDL from the originating application, and then right-click the timeline you want to import them into

in the Media Pool and use the Timelines > Import > EDL to New Track contextual menu command to

import each separate EDL to a new track of a single timeline in DaVinci Resolve. This is described later

in this chapter.

NOTE: While the EDL format supports a variety of SMPTE-defined video transition codes,

all EDL transitions are turned into cross dissolves of identical duration in DaVinci Resolve.

If you’re not familiar with the EDL format, each edit appears as a numbered event that contains the

reel number, edit type, source timecode (In and Out points), and record timecode (In and Out points).

Here’s a sample of a simple four event EDL:

TITLE:   Pool Shark Edit

FCM: NON-DROP FRAME

001  REEL_ONE AA/V  C        10:59:23:01 10:59:28:16 01:00:00:00 01:00:05:15

002  REEL_ONE AA/V  C        11:39:48:15 11:39:51:13 01:00:05:15 01:00:08:13

003  REEL_ONE AA/V  C        13:16:30:21 13:16:34:19 01:00:08:13 01:00:12:11

004  REEL_ONE AA/V  C        14:09:43:16 14:09:44:20 01:00:12:11 01:00:13:15

Since DaVinci Resolve was originally designed to work by importing and exporting EDLs, there are

several methods you can use to import projects using EDLs. In all cases, you must first add the media

referenced by that EDL to the Media Pool before you can import its EDL.

The three primary workflows are:

�Conforming EDLs to individual media files: Importing an EDL that references a collection of

discrete media files that have already been imported into DaVinci Resolve.

�Preconforming, or “notching,” a “flattened” master media file using an EDL: Importing an EDL

that references a “flattened” master media file. Flattened master media files are created when an

entire sequence is exported from an NLE as a single self-contained media file.

�Importing an EDL directly to a new track of an existing edit: If you’re importing a multi-track

video project, and the only means of doing so is using EDLs, you can export each track of the

source project as an individual EDL, and then import each EDL into DaVinci Resolve directly into

additional tracks of the same Timeline. This is also useful for workflows where effects clips are

being managed on a separate track assembled elsewhere, that you can then import directly into a

graded timeline to place many new effects clips all at once.

You can select multiple XML, AAF, FCP XML, or EDL timelines (or any combination thereof) at the same

time using the Timeline Import dialog. The selected timelines will import sequentially, pausing after

each time the OK button is pressed, allowing you to adjust separate Import Settings for each timeline.

This description covers the different ways that EDLs can be used in DaVinci Resolve.


Import and Conform Projects | Chapter 60 Conforming EDL Files

EDIT

EDL Export of a Project and Its Media

When using EDL workflows, it’s important to make sure that every clip in your edited sequence, and

every source media file it’s linked to, has an appropriate reel number/reel name, and true timecode

written into that file. When conforming EDLs, DaVinci Resolve requires reel names and accurate

timecode to successfully conform the imported EDL timeline to media in the Media Pool.

To export an EDL that can be easily conformed by DaVinci Resolve, each NLE has particular settings

that you should use. The primary supported format is CMX 3600, although DaVinci Resolve also

supports the DEDL format exported by both Smoke and Flame. Also, most editing applications let

you choose which video and audio tracks you want to export, and how to handle the start timecode

for the selected sequence of clips you’re exporting. In general, it’s a good idea to make sure that the

exported start timecode matches that of your sequence timeline.

There are other details, however, that vary by application. For example, when exporting an EDL from

Media Composer using Tools > List Tool, you need to make sure that the Active Setting is set to

Default EDL, and that the Output Format is set to CMX_3600. When exporting an EDL from Premiere

Pro, you have the option of enabling Use Source File Name and Include Transitions. When exporting

an EDL from the legacy Final Cut Pro 7, you need to make sure you set Reel Conflicts to Generic Edits,

and turn on the File Names checkbox. Most applications provide other settings that are optional,

including EDL notes of various kinds, but for a cleaner, easier to read EDL, you can turn these off

if you like.

Conforming EDLs to Individual Media Files

The advantage of working with discrete media files is that they are the “purest” version of the media,

without any effects (such as dissolves or superimpositions) “baked” into the visuals that might create

complications when you’re grading.


Before you import any media, make sure that the “Timeline frame rate” pop-up menu in the Master

Settings panel of the Project Settings is set to a frame rate that matches your project and media.

Otherwise, the EDL’s timecode will be misinterpreted.


Open the Media page, use the Media Storage browser to locate the media you want to add to the

project, and add it to the Media Pool by right-clicking the enclosing directory and choosing one of

the following commands:

Add Folder into Media Pool: Adds all compatible media files within that folder to the Media Pool.

Subfolders are not traversed.

Add Folder and SubFolders into Media Pool: Adds all compatible media files from that folder, and

all subfolders within that folder, to the Media Pool.

Add Folder Based on EDLs into Media Pool: Prompts you to choose an EDL. Only media

referenced by that EDL is imported, and only the selected folder is searched for that media.

Add Folder and SubFolders Based on EDLs into Media Pool: Prompts you to choose an EDL.

Only media referenced by that EDL is imported, and the selected folder and all subfolders are

searched for that media.

TIP: The “Add Folder...Based on EDLs” commands are useful for efficiently adding just

the media you need to the Media Pool in instances where there might be many terabytes

of unmanaged source media, most of which is unused.


Import and Conform Projects | Chapter 60 Conforming EDL Files

EDIT


Do one of the following:

�From any page, choose File > Import Timeline (Shift-Command-I).

�Open the Edit page, right-click anywhere in the Media Pool, and choose Timelines >

Import > AAF/EDL/XML/DRT/ADL/OTIO.

A window appears prompting you to “Select a file to import.”


Navigate to the EDL file you want to use, select it, and click Open. The Load EDL window appears.


Choose the options that are applicable to your particular project. All greyed out options are not

editable, either because they’re not applicable, or are not defined by the Project Settings that are

currently applied. The options you can set include:

Source File: The file you selected in the previous step.

Timeline name: The name of the Timeline you’re about to create. This defaults to the name of the

EDL file you selected, but you can change this if you like, for example, to add the import date if this

is a new version of the edit.

Automatically set project settings checkbox: Turn this option on if you want to overwrite the

frame size setting in the Master Project Settings panel of the Project Settings. You cannot

overwrite the Timeline frame rate when importing an EDL.

Set timeline resolution to: Two fields let you specify the width and height of the frame size you

want to work at in DaVinci Resolve. This defaults to your Project settings, but can be overridden by

turning on the “Automatically set project settings” checkbox.

EDL framerate: Choose the frame rate of the sequence that you exported as an EDL. You can use

this option to convert the EDL frame rate from 30 to 24 frames per second if you set the Timeline

frame rate to 24 fps and if the EDL frame rate is set to 30 fps; this is useful when an offline edit is

done at 30 fps with media using 3:2 pulldown. Note that 25 fps to 24 fps conversion is not supported.

Use drop frame timecode checkbox: Only enabled if the EDL frame rate pop-up menu is set to 30

fps. Turn this on if your EDL uses drop-frame timecode.


When you’re finished choosing options, click OK.

The EDL is imported, a new timeline appears highlighted in the Media Pool, and its corresponding

sequence of clips appears in the Timeline Editor if you’re in the Edit page. Clips that could not

be linked to a corresponding file in the Media Pool appear with a red thumbnail to indicate that

they’re unconformed.