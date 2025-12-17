---
title: "Step 4 – Export Media Suitable for Editing"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 216
---

# Step 4 – Export Media Suitable for Editing

Once you’ve organized your clips, synced the dailies, and applied whatever grading is necessary

for the purpose at hand, you’ll use the Deliver page to set up the format, file naming convention,

and organization of the media you’re outputting for editing or finishing.

Deliver page with several jobs set up for rendering

Furthermore, if you need to apply a window burn, watermark, or logo to the media you’re processing,

that can be accomplished using the Project panel of the Data Burn-In window, available by choosing

Workspace > Data Burn-In. Window burns can be formatted with a lot of flexibility, and are written out

to media that’s either rendered or output to tape.

For more information, see Chapter 12, “Data Burn-In.”

Choosing metadata to display onscreen in the Data Burn-in window


Import and Conform Projects | Chapter 57 Creating Digital Dailies for Round Trip Workflows

EDIT

Once you’ve selected the appropriate render settings and window burn options, you can output one

or several versions of the media, to accommodate jobs where you need to provide several media

deliverables.

For more information on setting up and using the Deliver page, see Chapter 186, “Using the

Deliver Page.”

Step 5 – Reconform Media to an EDL, AAF,

OTIO, or XML Project File

Once the offline media you’ve delivered has been edited in whichever NLE is used for the project,

it’s simple to reimport the edited project via an AAF, XML, OTIO, or EDL file, depending on which is

most suitable to your application. This edit data can be used to reconform the original media that you

imported into the Media Pool, so that you immediately have access to whatever graded adjustments

you made to create the offline media, as applied to the source media.

Importing AAF, XML, OTIO, or EDL files in the Edit page creates new timelines, and you can import

multiple subsequent Timelines to accommodate changes that have been made to the edit, if you

find yourself grading a project that is in progress editorially. In fact, depending on how you set up

your grades, you can use remote versions which will automatically ripple to follow each clip when

you import a re-edited version of the program as a new timeline, saving you from having to recreate

your work.

For more information on using remote versions, see Chapter 142, “Grade Management.”

Step 6 – Output Final Media for Finishing

Once you’re finished with your final grade, you’ll again use the controls of the Deliver page to render

the program’s final media, either as individual clips for a round-trip workflow, or as a single media file

or image sequence for delivery as a digital master.


Import and Conform Projects | Chapter 57 Creating Digital Dailies for Round Trip Workflows

EDIT

Chapter 58

Conforming

XML Files

XML is one of the most straightforward methods of bringing edits with as many

video tracks as you need from different NLEs into DaVinci Resolve.

XML import has the added benefit of allowing a variety of supported effects to be imported along with

the edit data, as well as multiple tracks of video data.

This chapter covers the relatively simple procedure used to import XML projects into DaVinci Resolve.

This can be for a one-way trip, in which you’re finishing a project in DaVinci Resolve, or as part of a

round-trip workflow, in which you return to the NLE of origin for finishing.

XML round-trip workflows are fairly simple; for more information on exporting individual clips,

see Chapter 187, “Rendering Media.”

Contents

More About Conforming XML Files�������������������������������������������������������������������������������������������������������������������������������������������� 1178

Importing XML Project Files����������������������������������������������������������������������������������������������������������������������������������������������������������� 1178


Import and Conform Projects | Chapter 58 Conforming XML Files

EDIT

More About Conforming XML Files

DaVinci Resolve can import projects that were exported to the Final Cut Pro 7 or Final Cut Pro X XML

formats.  Adobe’s Premiere Pro and Autodesk Smoke and Flame Premium are also capable of using

the Final Cut Pro XML project exchange format to accommodate round-trip workflows. However, for

the best results you need to make sure that you’re exporting XML from Premiere Pro version 5.5.1 or

newer; ideally you want to export from the latest version of Premiere Pro that’s available.

Exporting XML for use by DaVinci Resolve is straightforward, and there really aren’t any settings you

need to manage when exporting an XML file other than the version of XML you want to export. For this

reason, it’s best to do whatever timeline and/or media management you need to before XML export.

Manage Your Media Before Exporting an XML

In workflows using imported XML or AAF projects (or even EDLs), it’s easiest to relink and

conform to the accompanying media files if they’re all located in a single directory path.

Having media sorted into multiple directories is fine as long as they’re all within a single main

directory that you can select at the appropriate stage of project import.

Importing XML Project Files

This section covers the Import AAF/EDL/XML dialog in much more detail. One procedure lets you

accomplish any of the following workflows:

�Importing an XML file and automatically conforming to and importing the media it’s linked to.

�Importing an XML file and manually choosing another set of media, presumably in a different

format or resolution, with identical metadata, to conform to instead.

�Importing an XML file that’s linked to offline media derived from a camera original format, and

automatically conforming it to and importing the camera original media.

Each of these workflows is possible by choosing the correct combination of options, each of which is

described in the following procedure.

You can select multiple XML, AAF, FCP XML, or EDL timelines (or any combination thereof) at the same

time using the Timeline Import dialog. The selected timelines will import sequentially, pausing after

each time the OK button is pressed, allowing you to adjust separate Import Settings for each timeline.

To load an XML file and automatically link to its referenced media:


Do one of the following:

�From any page, choose File > Import Timeline (Shift-Command-I).

�Open the Edit page, right-click anywhere in the Media Pool, and choose Timelines >

Import > AAF/EDL/XML/DRT/ADL/OTIO.


Using the file dialog that appears, find the project file you want to import, and click the file to

open it. The Load XML window appears, depending on your selection.


Import and Conform Projects | Chapter 58 Conforming XML Files

EDIT

Options when importing an XML file


Choose the options that are applicable to your particular project. By default, these options are

based on metadata within the file you selected.

�Source file: The file you selected in the previous step.

�Import timeline: If there are multiple sequences within the selected XML source file, this pop-up

menu lets you choose which sequence to import as a DaVinci Resolve timeline.

�Timeline name: The name of the Timeline you’re about to create. This defaults to the name of

the sequence that was exported, but you can change it if you like.

�Master timeline start timecode: The timecode at which the imported timeline will start. This

automatically matches the start timecode of the selected Import Timeline.

�Automatically set project settings: Leave this option on to automatically change the frame size

and frame rate settings in the Project tab of the Config page with those in this window. You can

import timelines with frame rates that are different from the Project frame rate.

�Automatically import source clips into media pool: Leave this checkbox on to automatically

import the media referenced by the XML project file you selected into the Media Pool based on

the embedded file paths. If the media files are not automatically found at these locations, you

will be prompted to manually select a directory where the clips are located.

Ignore file extensions when matching: Turn this checkbox on if you want to manually choose

a different directory of media to link to, for example if the XML you’re importing links to ProRes

Proxy media, and you want to relink to another directory of corresponding ProRes 4444 or

camera raw media.


Import and Conform Projects | Chapter 58 Conforming XML Files

EDIT

�Use sizing information: Lets you import position, scale, and rotation transforms from the

originating NLE via the imported XML project file. These transforms are stored in each clip’s

settings in the Edit page Inspector.

�Use color information: For Final Cut Pro X XML files only. This option lets you import a subset of

color correction data from the Final Cut Pro X color board controls.

�Import multi-channel audio tracks as linked groups: Turn on this checkbox if you want to import

multi-channel audio, such as stereo, 5.1, and 7.1 audio into individual mono timeline tracks that

are linked together in the Fairlight page.

For more information about Linked Groups, see Chapter 171, “Setting Up Tracks, Busses,

and Patching.” If this checkbox is turned off, multi-channel audio will be imported into

multi-channel audio tracks in the Timeline.

�Set timeline resolution to: Two fields let you specify the width and height of the frame size you

want to work at in DaVinci Resolve. The default is whatever resolution is specified in the XML file

being imported.

�Timeline frame rate: By default, this is derived from the frame rate of the XML file being

imported. If you’re importing an XML file into a project that already has media in the Media Pool,

the Timeline frame rate is locked and cannot be changed.

�Use drop frame timecode: By default, this is derived from the XML file being imported.

�EDL frame rate: By default, this is derived from the frame rate of the selected file.

�Use drop frame timecode: By default, this is derived from the frame rate of the selected file.

�Mixed frame rate format: This pop-up menu lets you choose the method used to conform

mixed frame rates for rendering and playback. You can choose the “Final Cut Pro 7” or “Final Cut

Pro X” methods of conform, while for projects imported from Media Composer, Premiere Pro,

Smoke, or other NLEs, you should leave this set to “DaVinci Resolve.” This pop-up menu also

appears in the Load XML dialogs when you import a project.


After choosing all necessary settings, click OK.


Assuming you left “Automatically import source clips into media pool,” turned on, if the media

linked to by the XML file is not in the expected disk location, or if you turned on the “Ignore file

extensions when matching” checkbox, then another dialog appears prompting you to choose the

folder within which the media for this project is stored. Do one of the following:

�If you want to try to relink to media in another disk location: Click Yes, and then navigate

to the folder containing your media (all subfolders will be automatically traversed as well), select

it, and click OK.

�If you want to just import the Timeline with all offline clips: Click No.

A prompt appears if all the media was not found


Import and Conform Projects | Chapter 58 Conforming XML Files

EDIT

IMPORTANT: It’s always possible to choose the top level of any volume to automatically

find all media in any directories located within, but if the volume is large and full of many

files, scanning every folder and document of the volume may be an extremely time-

intensive process.


If you clicked Yes to selecting another folder, then use the folder selection dialog to navigate to

another folder, and click Ok. You can cycle through this process as many times as you need to

until you’ve found all the media that timeline is linked to.

Selecting the source folder for your XML imported clips

The XML file is imported. A new timeline and the referenced media files appear in the Media

Pool, and the Timeline is opened so you can see its contents. Clips that could not be linked to a

corresponding file on disk appear red in both the Media Pool and Timeline to indicate that they’re

offline and unlinked.

TIP: You can open the Edit Index and choose Filter Offline Clips from the option menu to

see a list of all offline clips in the current Timeline.


Import and Conform Projects | Chapter 58 Conforming XML Files

EDIT