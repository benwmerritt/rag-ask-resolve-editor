---
title: "Chapter 59"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 217
---

# Chapter 59

Conforming

AAF Files

AAF (Advanced Authoring Format) is a project exchange format, originally

developed by the Advanced Media Workflow Association (AMWA). Commonly

used video applications that export project data in the AAF format include Avid

Media Composer, Avid Symphony, Autodesk Smoke and Flame Premium, and

Adobe Premiere Pro.

This chapter includes detailed information about recommended workflows for moving projects from

Media Composer (or Symphony) to DaVinci Resolve for grading, either as a one-way trip, or as a

round-trip workflow in which you return to Avid Media Composer for finishing. Since Media Composer

round-trip workflows have many variables, this is covered in depth within this chapter.

The end of this chapter also describes how to import audio projects from Pro Tools that have been

exported to AAF.

Contents

Supported Media Types in AAF Workflows�������������������������������������������������������������������������������������������������������������������������� 1183

Transcoding to DNxHD or DNxHR Always Works��������������������������������������������������������������������������������������������������������������� 1183

Linking to Media Using AMA and Consolidating������������������������������������������������������������������������������������������������������������������ 1183

Fast Imported Media�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1184

Logged Errors When Importing AAF����������������������������������������������������������������������������������������������������������������������������������������� 1185

Simple AAF Import����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1185

Supported AAF Timeline Features���������������������������������������������������������������������������������������������������������������������������������������������� 1189

Performing an AAF Avid Round Trip����������������������������������������������������������������������������������������������������������������������������������������� 1189

Step 1 – Create a Project in Media Composer����������������������������������������������������������������������������������������������������������������������� 1189

Step 2 – Exporting an AAF for DaVinci Resolve������������������������������������������������������������������������������������������������������������������� 1190

Step 3 – Conforming Your AAF in DaVinci Resolve������������������������������������������������������������������������������������������������������������� 1191

Step 4 – Continue Editing, Grading, and Finishing the Project������������������������������������������������������������������������������������� 1193

Step 5 – Render Graded Media and Export a New AAF�������������������������������������������������������������������������������������������������� 1193

Step 6 – Copy the Graded Media to Avid MediaFiles������������������������������������������������������������������������������������������������������� 1194

Step 7 – Import the Graded AAF�������������������������������������������������������������������������������������������������������������������������������������������������� 1194


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT

Supported Media Types in AAF Workflows

Media Composer provides several methods of ingesting and managing compatible media formats.

Ultimately, which formats are suitable for a Media Composer to DaVinci Resolve one-way or round trip

depends on whether they’re compatible with DaVinci Resolve.

There’s one other thing to keep in mind as you’re managing media in Media Composer; not all formats

are compatible with all media management operations. This combination of format compatibility

and operational compatibility requires you to carefully tailor your workflow around which media files

you’ll be using.

Transcoding to DNxHD or DNxHR Always Works

Since DNxHD and DNxHR were developed to be Media Composer’s core codecs, workflows where

you transcode other media formats to MXF-wrapped DNxHD/DNxHR before editing will always work,

and are the simplest when round tripping between Media Composer and DaVinci Resolve. DaVinci

Resolve supports both MXF-wrapped and QuickTime-wrapped DNxHD/DNxHR media.

Linking to Media Using AMA and Consolidating

Avid Media Access (AMA) is a means of directly linking clips to media files in Media Composer

without needing to either transcode them to DNxHD/DNxHR MXF files, or copy them to an Avid

MediaFiles directory. While convenient, workflows involving media that’s linked using AMA require a

bit more forethought.

Not all AMA-compatible media formats can be consolidated in Media Composer, which limits your

ability to create a smaller, more portable collection of media to move into DaVinci Resolve. Whether or

not an AMA-linked clip can be consolidated depends on its media format; Media Composer can only

consolidate formats that it can write. For example, since Media Composer cannot write R3D media,

then R3D media cannot be consolidated.

Furthermore, not all AMA-compatible media formats are compatible with DaVinci Resolve.

Simply being able to edit a media format in a Media Composer timeline doesn’t guarantee you can

use it in DaVinci Resolve. The following table lists which media formats can be AMA-linked in Media

Composer, which formats can be consolidated, and which are compatible for use in DaVinci Resolve.

If you’re prepping a sequence that uses a mix of media formats, some of which can be consolidated,

and some of which can’t, you should transcode all clips that aren’t compatible with consolidation to

an Avid native codec before beginning the process of consolidating media and exporting an AAF to

DaVinci Resolve.

Relinking Transcoded Media to AMA Media������������������������������������������������������������������������������������������������������������������������� 1194

Step 1 – Relink Your Transcoded Media to AMA-Linked Source���������������������������������������������������������������������������������� 1194

Step 2 – Export an AAF File����������������������������������������������������������������������������������������������������������������������������������������������������������� 1194

Step 3 – Import the AAF, Grade, Render, and Export�������������������������������������������������������������������������������������������������������� 1195

Step 4 – Reimport the AAF into Media Composer/Symphony�������������������������������������������������������������������������������������� 1195

Audio AAF Import from Pro Tools����������������������������������������������������������������������������������������������������������������������������������������������� 1195

Import AAF, EDL, XML����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1195

Import AAF to Current Timeline���������������������������������������������������������������������������������������������������������������������������������������������������� 1195


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT

Fast Imported Media

Another wrinkle is that Media Composer supports a media ingest method called “Fast Import,” where

imported media is quickly copied to the Avid MediaFiles directory by inserting the original image

data using the original codec into an MXF wrapper. This is an extremely fast and efficient way to

bring media into Media Composer projects, but the resulting files are not typically compatible with

DaVinci Resolve.

On the other hand, keep in mind that any media format that can be Fast Imported can also be

consolidated. If you’re planning to round trip a sequence that uses Fast Imported media, it’s

recommended that you either transcode the Fast Imported clips to DNxHD prior to AAF export, or

conform your exported AAF project to the camera original media in DaVinci Resolve instead.

TIP: Whenever you use a combination of media in your project that includes formats that

aren’t compatible with DaVinci Resolve, you can use the “Transcode Video To” checkbox in

the options of the Export As dialog when exporting an AAF project. This option lets you to

transcode all media that isn’t a compatible format into a format that is compatible. Some non-

standard frame sizes will not transcode in Avid and will return an unsupported resolution error.

Codec

Can be

Natively AMA-Linked

Can be

Consolidated

DaVinci Resolve

Compatible

ARRI ALEXA Raw

Non-native support

No

Yes

AVCHD

Yes

No

Yes

AVC-Intra and Long GOP

Yes

Yes

Yes

Blackmagic RAW

Non-native support

No

Yes

Canon XF

Yes

Yes

Yes

Cine (Phantom)

Yes

Yes

Yes

CinemaDNG

No

No

Yes

DVC PRO P2

Yes

Yes

No

QuickTime (ProRes)

Yes

Yes

Yes

R3D (RED)

Non-native support

No

Yes

Sony F65 Raw

Yes

No

Yes

Sony HDCAM SR (SStP)

Non-native support

No

Yes

Sony XAVC

Yes

Yes

Yes

Sony XDCAM

Yes

Yes

Yes

Compatible AMA-linked formats


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT

Logged Errors When Importing AAF

If you turn on the “Import log messages as markers” checkbox in the Load AAF dialog, certain error

messages that alert you to issues with the AAF import you’re trying to do will be added as markers

with notes to the Timeline. You have an option, via a pop-up embedded within the text of this

checkbox, of choosing the color of the markers used to store this information.

The following messages will create markers:

�Transition type ‘XXXX’ is not supported in this release. A Cross Dissolve will be inserted.

�Effect type ‘XXXX’ is not supported in this release. Plain clips will be imported.

�SMPTE Wipe Transition type ‘XXXX’ is not supported in this release. A Cross Dissolve will

be inserted.

�Interpolation type ‘XXXX’ is not supported in this release. Linear interpolation will be used.

�The clip ‘XXXX’ failed to link because the timecode extents do not match any clip in

the Media Pool.

�Mismatch between specified target timecodes ‘XXXX’ and located file timecodes ‘YYYY.’

�No overlap between specified target timecodes ‘XXXX’ and located file timecodes ‘YYYY.’

�Clip ‘XXXX’ in track ‘XXX’ at timecode ‘UNKNOWN’, with reel name ‘XXXX’ and filename ‘XXXX.’

�Clip ‘XXXX’ in track ‘XXX’ at timecode ‘UNKNOWN’, with reel name ‘XXXX’ and filename ‘XXXX.’

�File not found in search directories.

As of the time of this writing, this feature is only available when importing AAF files.

Simple AAF Import

This section covers the Import AAF, EDL, XML dialog in much more detail. One procedure lets you

accomplish any of the following workflows:

•	 Importing an AAF file and automatically conforming to and importing the media it’s linked to.

•	 Importing an AAF file and manually choosing another set of media, presumably in a different

format or resolution, with identical metadata, to conform to instead.

•	 Importing an AAF file that’s linked to offline media derived from a camera original format,

and automatically conforming it to and importing the camera original media.

You can select multiple XML, AAF, FCP XML, or EDL timelines (or any combination thereof) at the same

time using the Timeline Import dialog. The selected timelines will import sequentially, pausing after

each time the OK button is pressed, allowing you to adjust separate Import Settings for each timeline.

Each of these workflows is possible by choosing the correct combination of options, each of which is

described in the following procedure.

To load an AAF file and automatically link to its referenced media:


Do one of the following:

�From any page, choose File > Import Timeline (Shift-Command-I).

�Open the Edit page, right-click anywhere in the Media Pool, and choose Timelines >

Import > AAF/EDL/XML/DRT/ADL/OTIO.


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT


Using the file dialog that appears, find the project file you want to import, and click the file

to open it. The Load AAF window appears, depending on your selection.

Options when importing an AAF file


Choose the options that are applicable to your particular project. By default, these options are

based on metadata within the file you selected.

�Source file: The file you selected in the previous step.

�Import timeline: If there are multiple sequences within the selected AAF source file, this pop-up

menu lets you choose which sequence to import as a DaVinci Resolve timeline.

�Timeline name: The name of the Timeline you’re about to create. This defaults to the name of

the sequence that was exported, but you can change it if you like.

�Master timeline start timecode: The timecode at which the imported timeline will start. This

automatically matches the start timecode of the selected Import Timeline.

�Automatically set project settings: Leave this option on to automatically change the frame size

and frame rate settings in the Project tab of the Config page with those in this window. You can

import timelines with frame rates that are different from the Project frame rate.

�Automatically import source clips into media pool: Leave this checkbox on to automatically

import the media referenced by the AAF project file you selected into the Media Pool based on

the embedded file paths. If the media files are not automatically found at these locations, you

will be prompted to manually select a directory where the clips are located.


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT

Ignore file extensions when matching: Turn this checkbox on if you want to manually choose

a different directory of media to link to; for example, if the AAF you’re importing links to ProRes

Proxy media, and you want to relink to another directory of corresponding ProRes 4444 or

camera raw media.

�Use sizing information: Lets you import position, scale, and rotation transforms from the

originating NLE via the imported AAF project file. These transforms are stored in each clip’s

settings in the Edit page Inspector.

�Import log messages as COLOR markers: Turn on this checkbox and choose a color from the

accompanying drop-down menu for markers that will be placed in the Timeline with note text

describing import errors that you might want to troubleshoot later.

�Import multi-channel audio tracks as linked groups: Turn on this checkbox if you want to import

multi-channel audio, such as stereo, 5.1, and 7.1 audio into individual mono timeline tracks that

are linked together in the Fairlight page.

For more information about Linked Groups, see Chapter 171, “Setting Up Tracks, Busses, and

Patching.” If this checkbox is turned off, multi-channel audio will be imported into multi-channel

audio tracks in the Timeline.

�Import AAF to current timeline: Imports the AAF to the currently loaded Timeline, instead of

creating a new timeline in the Media Pool.

Insert Additional Tracks: Automatically assigns new tracks to the Timeline, so the AAF

referenced media does not overwrite current clips on the existing timeline.

Insert with offset: Overwrites the AAF referenced media on the Timeline and offsets it by the

amount set in timecode format.

�Set timeline resolution to: Two fields let you specify the width and height of the frame size you

want to work at in DaVinci Resolve. The default is whatever resolution is specified in the AAF file

being imported.

�Timeline frame rate: By default, this is derived from the frame rate of the AAF file being

imported. If you’re importing an AAF file into a project that already has media in the Media Pool,

the Timeline frame rate is locked and cannot be changed.

�Use drop frame timecode: By default, this is derived from the AAF file being imported.

�EDL frame rate: By default, this is derived from the frame rate of the selected file.

�Use drop frame timecode: By default, this is derived from the frame rate of the selected file.

�Mixed frame rate format: This drop-down menu lets you choose the method used to conform

mixed frame rates for rendering and playback. You can choose the “Final Cut Pro 7” or “Final Cut

Pro X” methods of conform, while for projects imported from Media Composer, Premiere Pro,

Smoke, or other NLEs, you should leave this set to “DaVinci Resolve.” This drop-down menu also

appears in the Load AAF dialogs when you import a project.


After choosing all necessary settings, click OK.


Assuming you left “Automatically import source clips into media pool,” turned on, if the media

linked to by the AAF file is not in the expected disk location, or if you turned on the “Ignore file

extensions when matching” checkbox, then another dialog appears prompting you to choose the

folder within which the media for this project is stored. Do one of the following:

�If you want to try to relink to media in another disk location: Click Yes, and then navigate

to the folder containing your media (all subfolders will be automatically traversed as well), select

it, and click OK.

�If you want to just import the Timeline with all offline clips: Click No.


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT

A prompt appears if all the media was not found

IMPORTANT: It’s always possible to choose the top level of any volume to automatically

find all media in any directories located within, but if the volume is large and full of many

files, scanning every folder and document of the volume may be an extremely time-

intensive process.


If you clicked Yes to selecting another folder, then use the folder selection dialog to navigate to

another folder, and click Ok. You can cycle through this process as many times as you need to

until you’ve found all the media that timeline is linked to.

Selecting the source folder for your AAF imported clips

The AAF file is imported. A new timeline and the referenced media files appear in the Media Pool,

and the Timeline is opened so you can see its contents. Simple nested clips should also come

through. Clips that could not be linked to a corresponding file on disk appear red in both the

Media Pool and Timeline to indicate that they’re offline and unlinked.

TIP: You can open the Edit Index and choose Filter Offline Clips from the option menu to

see a list of all offline clips in the current Timeline.


Import and Conform Projects | Chapter 59 Conforming AAF Files

EDIT