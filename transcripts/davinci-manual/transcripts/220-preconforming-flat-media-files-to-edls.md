---
title: "Preconforming “Flat” Media Files to EDLs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 220
---

# Preconforming “Flat” Media Files to EDLs

Preparing an edited sequence for grading, along with each individual clip of media, can be time

consuming for effects-intensive projects, or it may be an unnecessary step for a project with no

effects whatsoever.

In these cases, it can be simpler and quicker to export a flattened master media file that can

be split back apart into its individual clips in DaVinci Resolve. This workflow is similar to a more

traditional tape-to-tape workflow, except that you’re working from a digital master, rather than a

tape‑based master.

The easiest way to do this is to use the Preconform button in the Edit page to split a single master file

that you’ve imported into the Media Pool back into individual clips in a new timeline.

To preconform a flattened master media file to an EDL:


Open the Media page, use the Media Storage browser to navigate to the flattened master media

file that you exported containing the entire program, and double-click to add it to the Media Pool.


Import and Conform Projects | Chapter 60 Conforming EDL Files

EDIT


Right-click anywhere in the background of the Media Pool, and choose Timelines > Import >

Preconformed EDL.


In the “Select an EDL file” dialog that appears, navigate to the EDL that matches the flattened

master media file you had exported, select it, and click Open.


In the “Parse preconform options” dialog that appears, give the new Timeline a name,

and click OK.

A new Timeline appears in the Media Pool list, and opening it in the Edit page shows the flattened

media file with edits added to its video track that correspond to those from the selected EDL, ready

for further editing and grading. The audio is left uncut, on the premise that you’re probably focused on

grading the visuals in this workflow, and not on re-editing the audio.

Override Input Color Space of Clips in

Preconform Workflows Using Color

Management

When you preconform a flattened master media file using an EDL with the File > Import Timeline > Pre-

conformed EDL command, and your project has Resolve Color Management or ACES enabled, you

can now change the Input Color Space of each clip in the resulting Timeline independently. To do so,

open the Color page, right-click the clips you want to customize, and choose an option from the Input

Color Space submenu of the contextual menu.

This is useful in workflows where you’ve received a flattened media file that was output with clips in

different color spaces, for example mixing Rec. 709 media with log-encoded clips of different kinds.

Conforming “Flat” Media Files

Using Split and Add

The second method of conforming an EDL to a flattened file is to use the “Split and Add” command in

the Media page to split one or more master media files into individual clips that match those of an EDL,

then importing the EDL itself in the Edit page in a second step.

This method is useful if there are clips in different folders or volumes that you want to conform to a

single EDL. For example, the majority of the first reel of a program may have been exported as a

single flattened file, but the corresponding EDL may require that an additional folder of effects clips be

added to the Media Pool to be fully conformed.

To split a flat media file in the Media page and import its EDL in the Edit page:


Before you import any media, make sure that the “Timeline frame rate” pop-up menu in the Master

Settings panel of the Project Settings is set to a frame rate that matches your project.


Open the Media page, use the Media Storage browser to navigate to the flattened master media

file that contains the entire program.


Select the flattened media file, right-click it, and choose “Split and Add into Media Pool.”


In the “Select EDL files for splitting clips” dialog that appears, navigate to the EDL that matches the

flattened master media file, select it, and click Open.


Select the frame rate of the project from the File Conform Frame Rate dialog that appears.

This frame rate should be identical to the “Timeline frame rate” pop-up you set in step 1.


Import and Conform Projects | Chapter 60 Conforming EDL Files

EDIT


Choose the appropriate options in the “Enter handle size for splitting” dialog that appears:

Handle size in number of frames: Enter a number of frames to be added as handles to the first

and last frame of the clip. This is useful when you’re using the “Split and Add into Media Pool”

command to import only the referenced sections of a directory of individual media files.

Split Unreferred Clips: Useful when the referenced media files include segments that aren’t

“referred to” by any events within the EDL used to split them. Turning this checkbox on adds all

such unreferred clip segments to the Media Pool as separate clips, for possible later use.


Click Split & Add. The Media Pool fills up with individual segments of the flattened master media

file, each of which matches an event in the EDL you used to split it.


To import the corresponding EDL to create a timeline with this media, do one of the following:

�From any page, choose File > Import AAF, EDL, XML (Shift-Command-I).

�Right-click anywhere in the background of the Media Pool, and choose Timelines > Import >

AAF/EDL/XML.


In the “Choose a file to import” dialog that appears, navigate to the EDL that matches the flattened

master media file, select it, and click Open.

10	 Choose whatever options are necessary from the Load EDL dialog that appears (the default

settings should work fine), and click OK.

The Master Timeline and the timeline you just imported appear in the Media Pool, the Conform EDL list

updates with the events from the imported EDL, and the Timeline editor shows the edited clips, ready

for grading. Clips that could not be linked to a corresponding file in the Media Pool appear with a red x

to indicate that they’re unconformed.

Importing an EDL to a New Track

This last procedure describes how to add an EDL, not as an individual new Timeline, but as an

additional video track to an existing Timeline. There are many reasons you might want to do this.

For example, if you need to move a multi-track project to DaVinci Resolve from an application that

can’t export either AAF or XML project exchange files that DaVinci Resolve understands, you can use

multiple EDLs. Simply export each track of the source project as an individual EDL, and then import

each EDL into DaVinci Resolve as additional tracks of the same Timeline.

This is also useful for workflows where effects clips are being managed on a separate track

assembled elsewhere, that you can then import directly into a graded Timeline to place many new

effects clips all at once.

To import an EDL to a new track of an existing timeline:


In this procedure, you have the option of adding whatever media is required by the EDL you’re

about to import to the Media Pool first, or you can add the media after the EDL has been imported.

It’s your choice.


Open the Edit page, select a timeline in the Media Pool, then right-click it and choose Timelines >

Import > EDL to New Track. A window appears prompting you to “Choose a file to import.”


Navigate to the EDL file you want to use, select it, and click Open.


A new video track is created above any previously existing tracks, and events from the selected

EDL are immediately loaded into it according to their record timecode positions. If you loaded

the media needed by the new clips at the beginning of this procedure, that media should be

conformed. Otherwise, you’ll need to track down the media files needed by the new unconformed

clips and add it to the Media Pool now.


Import and Conform Projects | Chapter 60 Conforming EDL Files

EDIT

Chapter 61

Conforming

OTIO Files

This chapter covers all workflows that let you import and conform timelines using

the .otio and .otioz formats.

Contents

More About Conforming OTIO Files����������������������������������������������������������������������������������������������������������������������������������������� 1203

Importing OTIO Project Files�������������������������������������������������������������������������������������������������������������������������������������������������������� 1203

Importing .otioz Files������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1206


Import and Conform Projects | Chapter 61 Conforming OTIO Files

EDIT

More About Conforming OTIO Files

DaVinci Resolve supports the Open Timeline IO (OTIO) format for importing and exporting timelines

between applications. OTIO is an open source media and timeline interchange format created by the

Academy Software Foundation. It’s designed to be application and platform agnostic, allowing you to

pass your timeline and its media assets between programs with more compatibility than AAF or XML.

Exporting OTIO for use by DaVinci Resolve is straightforward, and there really aren’t any settings

you need to manage when exporting an OTIO file other than deciding if you want to export the

Timeline only (.otio), or the Timeline and all its associated media (.otioz).

There are two different OTIO formats supported by DaVinci Resolve

.otio: These files contain just the metadata about the timeline and no associated media.

They are small, portable, and require the end user to link the Timeline to their own copies of

the media.

.otioz: These bundle files contain both the Timeline metadata and all of the Timeline’s media

assets zipped together into one file. As a result this file can be very large, as it contains the

full length media files of all assets used in the Timeline. However, it assures that whoever

imports the file has all the media needed and is linked automatically to replicate the Timeline

on their machine.

Importing OTIO Project Files

This section covers the Import OTIO dialog in much more detail. One procedure lets you accomplish

any of the following workflows:

�Importing an .otioz file automatically and its associated media.

�Importing an .otio file and automatically conforming to and importing the media it’s linked to.

�Importing an .otio file and manually choosing another set of media, presumably in a different

format or resolution, with identical metadata, to conform to instead.

�Importing an .otio file that’s linked to offline media derived from a camera original format and

automatically conforming it to and importing the camera original media.

You can select multiple XML, AAF, FCP XML, or EDL timelines (or any combination thereof) at the same

time using the Timeline Import dialog. The selected timelines will import sequentially, pausing after

each time the OK button is pressed, allowing you to adjust separate Import Settings for each timeline.

Each of these workflows is possible by choosing the correct combination of options, each of which is

described in the following procedure.

To load an OTIO file and automatically link to its referenced media:


Do one of the following:

�From any page, choose File > Import Timeline (Shift-Command-I).

�Open the Edit page, right-click anywhere in the Media Pool, and choose Timelines > Import >

AAF/EDL/XML/DRT/ADL/OTIO.


Using the file dialog that appears, find the project file you want to import, and select the file and

press the Open button. The Load OTIO window appears, depending on your selection.


Import and Conform Projects | Chapter 61 Conforming OTIO Files

EDIT

Options when importing an .otio file


Choose the options that are applicable to your particular project. By default, these options are

based on metadata within the file you selected.

�Source file: The file you selected in the previous step.

�Timeline name: The name of the Timeline you’re about to create. This defaults to the name of

the sequence that was exported, but you can change it if you like.

�Timeline start timecode: The timecode at which the imported timeline will start. This

automatically matches the start timecode of the selected Import Timeline.

�Automatically set project settings: Leave this option on to automatically change the frame size

and frame rate settings in the Project tab of the Config page with those in this window. You can

import timelines with frame rates that are different from the Project frame rate.

�Automatically import source clips into media pool: Leave this checkbox on to automatically

import the media referenced by the OTIO project file you selected into the Media Pool based on

the embedded file paths. If the media files are not automatically found at these locations, you

will be prompted to manually select a directory where the clips are located.

Ignore file extensions when matching: Turn this checkbox on if you want to manually choose a

different directory of media to link to. For example, if the OTIO you’re importing links to ProRes

Proxy media, and you want to relink to another directory of corresponding ProRes 4444 or

camera raw media.

�Import multi-channel audio tracks as linked groups: Turn on this checkbox if you want to import

multi-channel audio, such as stereo, 5.1, and 7.1 audio into individual mono timeline tracks that

are linked together in the Fairlight page.


Import and Conform Projects | Chapter 61 Conforming OTIO Files

EDIT

For more information about Linked Groups, see Chapter 171, “Setting Up Tracks, Busses,

and Patching.” If this checkbox is turned off, multi-channel audio will be imported into multi-

channel audio tracks in the Timeline.

�Set timeline resolution to: Two fields let you specify the width and height of the frame size you

want to work at in DaVinci Resolve. The default is whatever resolution is specified in the OTIO

file being imported.

�Timeline frame rate: By default, this is derived from the frame rate of the OTIO file being

imported. If you’re importing an OTIO file into a project that already has media in the Media Pool,

the Timeline frame rate is locked and cannot be changed.

�Use drop frame timecode: By default, this is derived from the OTIO file being imported.

�EDL frame rate: By default, this is derived from the frame rate of the selected file.

�Use drop frame timecode: By default, this is derived from the frame rate of the selected file.

�Mixed frame rate format: This pop-up menu lets you choose the method used to conform mixed

frame rates for rendering and playback. You can choose the “Final Cut Pro 7” or “Final Cut Pro

X” methods of conform, while for projects imported from Media Composer, Premiere Pro,

Smoke, or other NLEs, you should leave this set to “DaVinci Resolve.” This pop-up menu also

appears in the Load OTIO dialogs when you import a project.


After choosing all necessary settings, click Ok.


Assuming you left “Automatically import source clips into media pool,” turned on, if the media

linked to by the OTIO file is not in the expected disk location, or if you turned on the “Ignore file

extensions when matching” checkbox, then another dialog appears prompting you to choose the

folder within which the media for this project is stored. Do one of the following:

�If you want to try to relink to media in another disk location: Click Yes, and then navigate to

the folder containing your media (all subfolders will be automatically traversed as well), select it,

and click OK.

�If you want to just import the Timeline with all offline clips: Click No.

A prompt appears if all the media was not found.

IMPORTANT: It’s always possible to choose the top level of any volume to automatically

find all media in any directories located within, but if the volume is large and full of

many files, scanning every folder and document of the volume may be an extremely

time‑intensive process.


If you clicked Yes to selecting another folder, then use the folder selection dialog to navigate to

another folder, and click Ok. You can cycle through this process as many times as you need to

until you’ve found all the media that timeline is linked to.


Import and Conform Projects | Chapter 61 Conforming OTIO Files

EDIT

Selecting the source folder for your OTIO imported clips

The OTIO file is imported. A new Timeline and the referenced media files appear in the Media

Pool, and the Timeline is opened so you can see its contents. Clips that could not be linked to a

corresponding file on disk appear red in both the Media Pool and Timeline to indicate that they’re

offline and unlinked.

TIP: You can open the Edit Index and choose Filter Offline Clips from the option menu to see

a list of all offline clips in the current Timeline.