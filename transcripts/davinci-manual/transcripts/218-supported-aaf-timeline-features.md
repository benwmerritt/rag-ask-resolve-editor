---
title: "Supported AAF Timeline Features"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 218
---

# Supported AAF Timeline Features

The following additional AAF timeline information will automatically be imported to DaVinci Resolve:

�Timeline Markers: Any timeline markers within the AAF will be imported. Timeline markers can

also be exported from DaVinci Resolve to AAF for round-trip workflows.

�Nested Clips: DaVinci Resolve will import AAF files with simple nested clips.

�Boris Continuum FX: Boris Continuum FX effects and settings will be imported along with

a timeline via AAF export. You’ll need to have the same Continuum suite of effects installed

on both machines (OFX version for DaVinci Resolve, AVX for Avid). When importing an AAF,

Boris Continuum effects that were used in the original NLE will appear on each affected clip

in the resulting DaVinci Resolve timeline, with all previously applied parameters available in

the Inspector. The Sapphire and Mocha suites are not available for AAF import at this time.

Performing an AAF Avid Round Trip

This section outlines a comprehensive workflow for creating projects in Media Composer that will be

compatible with DaVinci Resolve, moving projects from Media Composer to DaVinci Resolve, then

grading, rendering, and sending the final graded project back to Media Composer. The following steps

include procedures covering the following tasks:

�Ingesting all media as high quality MXF-wrapped DNxHD, then round tripping from Media

Composer to DaVinci Resolve.

�Importing and editing Resolve-compatible AMA-linked media formats, then round tripping from

Media Composer to DaVInci Resolve.

�Transcoding AMA-linked media files into offline-quality DNxHD clips for editing, then exporting an

AAF file and reconforming it in DaVinci Resolve to high quality camera original media as part of the

round trip.

Because there are so many variations in the way that Media Composer can ingest media and output

AAF projects, you should familiarize yourself with the following procedures before continuing with your

own project.

Step 1 – Create a Project in Media Composer


When creating a project in Media Composer, take note of the image format details, as these

should be matched in DaVinci Resolve. In particular, set the image format (e.g., 1080p/24) and

raster dimensions (e.g., 1920x1080) to match your desired mastering format. Also, color space

should be set to RGB 709 if you’re planning to send ingested/transcoded media from Media

Composer to DaVinci Resolve for grading.

NOTE: This information can also be found in the Avid Project Format tab.


Open your project, and ingest all necessary media into a new bin using one or both of the

following methods:

�Transcode media for editing: The simplest workflow for AAF import and round-trip workflows is

to ingest transcoded, native MXF-wrapped DNxHD media using the Import command.

�Import AMA-linked clips: You can also import AMA-linked clips, so long as all AMA-linked files

are in a format that’s compatible with DaVinci Resolve. Keep in mind that not all AMA-compatible

formats can be consolidated in Media Composer. In this case, import AMA-linked media into a

new bin using the Link to AMA File(s) command, and edit as usual.


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT

Once you’ve ingested all necessary media, you can edit your project as you would any other,

keeping in mind which effects are compatible with DaVinci Resolve. For more information

on effects in Media Composer to DaVinci Resolve round trips, see Chapter 55, “Preparing

Timelines for Import and Comparison.”

Step 2 – Exporting an AAF for DaVinci Resolve

When you’re finished editing, you need to export an AAF that will conform the .mxf media you used

in Media Composer into a DaVinci Resolve timeline. Two export configuration options are available,

depending on whether DaVinci Resolve and Media Composer are on the same system.


Select the sequence you want to export, and choose File > Output > Export to File.


In the Export As dialog, type a name for the AAF file you’ll be exporting.


Choose a location to save the AAF. You can save it anywhere you like, but if you’re moving the

project to another workstation, you may want to save it to a specific folder on a removable hard

drive where you store your AAF and XML files. The location you choose can also be used as the

location of the media that’s exported to accompany the AAF.


Click the Options button to open a more detailed window of export settings.


Turn on the AAF Edit Protocol checkbox. This option forces Media Composer to export a simplified

AAF file that’s more compatible with the project exchange workflows of different applications.


Choose the appropriate option from the Export Method pop-up menu to configure how the AAF

and its accompanying media will be exported. The option you choose depends on the following:

If Media Composer and DaVinci Resolve are on the same system: Choose “Link to (Don’t Export)

Media” to export an AAF file that links to the existing media in its current location. Click the Audio

Details tab and choose “Link to (Don’t Export) Media” from the Export Method pop-up menu.

If Media Composer and DaVinci Resolve are on different systems: Choose one of the two

following export methods:

�Copy All Media: For each source clip used, the entire corresponding media file is copied. This

can be useful when you want to preserve the original relationship of each clip to the source

media file it came from. However, be aware that you’ll potentially be exporting a lot of media

when you use this option.

�Consolidate Media: This is a more efficient media management workflow for finished projects,

since unused media will not be copied. You can specify additional handles to add to the

beginning and end of each exported media file, in frames, in the Handle Length field. Should

any media file and its handles overlap another media file and its handles, both will be combined

into a single exported media file.


(Optional) If you’re using a combination of media in your project that includes formats that aren’t

compatible with DaVinci Resolve, you can optionally turn on the “Transcode Video To” checkbox

and choose a media format from the pop-up menu to the right. This option automatically

transcodes all media in your sequence that doesn’t match the format specified in the pop-up to

match that format.


If you’re copying or consolidating media to another drive, choose “Folder” from the Media

Destinations Video/Data pop-up menu. Turn on the “Use Same Folder As AAF File” checkbox

to save the exported media to the same folder you selected in step 3. If you leave this checkbox

turned off, you can click Select Folder to choose another location.


Click Save, and when you return to the Export As dialog, click Save again.


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT

Once export is complete, you’ll see a duplicate sequence and duplicate media populating

your Media Composer bin, with the suffix “.Exported” appended to the sequence, and “.new”

appended to each media clip. In the file system, the resulting folder contains an AAF file, and

an Avid MediaFiles folder that contains the exported media.

Step 3 – Conforming Your AAF in DaVinci Resolve


Open DaVinci Resolve and create a new project.


Before you do anything else, you need to set DaVinci Resolve to properly read the timecode and

reel number information from the AAF files that Media Composer creates. Click the gear button

at the lower right-hand side of the DaVinci Resolve window to open the Project Settings window,

click General Options to reveal the Conform Options, and do the following:

�Make sure that “Use Timecode” is set to “Embedded in the source clip.”

�Turn the “Assist using reel names from the” checkbox on, and choose

“Embedding in source clip file.”

Conform assistance with reel names embedded in the source clip


Click Save.


Do one of the following:

�From any page, choose File > Import AAF, EDL, XML (Shift-Command-I).

�Open the Edit page, right-click anywhere in the Media Pool, and choose

Timelines > Import > AAF/EDL/XML.


When the File Selection window opens, select the AAF file you exported from Media Composer,

and click Open.


When the Load AAF dialog appears, the settings you choose determine which media

files the AAF will be conformed to:

Load AAF window conform options


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT

To conform to the transcoded or AMA-linked media files you edited: Leave the “Automatically

import source clips into media pool” checkbox turned on.

To conform to a different set of camera original media files: Turn on both the “Automatically

import source clips into media pool” and “Link to source camera files” checkboxes, which

references the Source Name metadata that Media Composer/Symphony embeds in exported AAF

files to track the correspondence in file naming between transcoded and camera original media.

To conform to a directory of media of your choosing: Turn on both the “Automatically import

source clips into media pool” and “Ignore file extensions when matching” checkboxes.

To conform to media that’s already in the Media Pool: Turn off the “Automatically import source

clips into media pool” checkbox. There must be clips in the Media Pool for this to work.


Additionally, make sure that the “Automatically set project settings” checkbox is on.


There are three other options that are relevant to AAF import:

Load AAF window conform options

Use Sizing Information: (Optional) Use this checkbox if you want to import position, scale, and

rotate transform data from the originating Media Composer project into DaVinci Resolve.

Import log messages as COLOR markers: Turn on this checkbox and choose a color from the

accompanying drop-down menu for markers that will be placed in the Timeline with note text

describing import errors that you might want to troubleshoot later.

Import multi-channel audio tracks as linked groups: Turn on this checkbox if you want to import

multi-channel audio, such as stereo, 5.1, and 7.1 audio into individual mono timeline tracks that are

linked together in the Fairlight page.

For more information about Linked Groups, see Chapter 171, “Setting Up Tracks, Busses,

and Patching.” If this checkbox is turned off, multi-channel audio will be imported into

multi-channel audio tracks in the Timeline.


Click OK.

As long as the media remains where it was when you exported it from Media Composer, the timeline

and all its media should now import. However, if the location of the media files you’re conforming

to has changed, then you may need to identify the location of the media via an additional dialog.

For example, if you’ve copied the media from the portable hard drive it was originally conformed to,

to a faster storage volume, then a file dialog appears, requesting that you choose the folder containing

the media used by your project. If prompted, do so and click OK.

Once import is complete, the Media Pool fills with the source media used by the imported project, and

the edit appears as the current Timeline in the Edit page.


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT

Step 4 – Continue Editing, Grading, and Finishing the Project

Edit the Timeline in the Edit page and grade each clip in the Color page as you would any other.

However, you should be aware that if you use the tools found in the Edit page to make any editorial

changes to the timeline you’ve imported, your export options will change later on:

�If you don’t make editing changes: Then you have the option to have DaVinci Resolve use the

Avid AAF file that you originally imported to generate an updated one. This preserves audio and

all other unsupported effects from the original AAF file, so that they reappear when you export a

new AAF back to Media Composer. If you use this option, you need to make sure the original AAF

file you import remains in the same location.

�If you do make editing changes: Then you need to use the “Generate New AAF” command to

export an AAF of the re-edited Timeline from DaVinci Resolve back to Media Composer. This

newly generated AAF file will not include any effects that are not supported by DaVinci Resolve.

Step 5 – Render Graded Media and Export a New AAF


When you’re ready to send a graded project back to Media Composer, select the Timeline you

graded and open the Deliver page.


Choose “Avid AAF” from the Presets at the top of the Render Settings to load its settings.

Selecting the Avid AAF setup for round-trip


In the Format section, choose the MXF codec you want to render to.


In the File section, choose the appropriate file destination path for the rendered media. The

location you choose depends on whether Media Composer and DaVinci Resolve are on the same

computer or not.

If Media Composer and DaVinci Resolve are on the same computer: Create a new folder within

your Avid MediaFiles folder (Avid MediaFiles/MXF/) named with a number. Make sure you choose

a previously unused number.

If DaVinci Resolve is on a different computer using different storage: Select any directory on the

portable hard drive you’ll be using to bring the media back to the Media Composer workstation

from which it came.


If you require handles for your rendered output, you can add handles in the Advanced Settings

of the Video tab. When making any changes to the File render settings, make sure to leave

the “Render Clip with Unique Filename” checkbox turned on to ensure that each clip rendered

has a different file name as multiple clips in the edited sequence may originate from the same

source clip.


In the Timeline, click Select Entire Timeline to select the entire Timeline for delivery, and then click

Add to Render Queue at the bottom of the Render Settings to add the job you’ve set up to the

Render Queue.


Click Start Render at the bottom of the Render Queue to initiate rendering.

The project renders, and an AAF is automatically exported to the same directory as the media

you’ve rendered.


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT

Step 6 – Copy the Graded Media to Avid MediaFiles


For workflows where DaVinci Resolve and Media Composer are on separate workstations, locate

the media directory containing the media files that were rendered out of DaVinci Resolve on the

portable hard drive being used to transport the project back to your Avid workstation, and copy it

into the Avid MediaFiles/MXF/ directory.


Rename the directory to be a number. Make sure you choose an unused number.