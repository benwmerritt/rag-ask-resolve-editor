---
title: "Creating Crossfades With Overlapping Fades"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 688
---

# Creating Crossfades With Overlapping Fades

While a fade gradually fades a single track of audio up or down, a crossfade fades two overlapping

clips at the same time, fading one clip up and another clip down, for the aural equivalent of a cross

dissolve. There are currently two ways of creating a crossfade in the Fairlight page. Both depend on

clip layering to allow you to have overlapping fades over overlapping clips.

To create a crossfade by overlapping two clips together:


Add a fade out to the end of one clip, and a fade in to the beginning of another clip. By default, all

fades you add in this way are linear, although you can adjust them to whatever gain you want.

Adding fades to adjacent clips


Drag the first clip to overlap the second clip by the length of the fade you’ve created.

Dragging the clips to overlap, the overlapping

parts will be preserved via clip layering


Drop the clip. The overlapping fades will both be preserved thanks to clip layering, and a

crossfade will appear in the Timeline.

The resulting crossfade


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

To create a crossfade over two clips that are already layered:

�Drag a fader handle at the beginning or end of a clip that’s layered, and a crossfade will

automatically appear.

Creating a crossfade by adjusting

the fader handle of a layered clip

Using Crossfades From the Edit Page

You can also add crossfades in the Edit page, but they appear in the Fairlight page as transitions in the

Edit page style.

The resulting crossfade

Finding Clips in the Media Pool

You can right-click any clip in the Timeline and choose Find in Media Pool to automatically select that

clip in the Media Pool, for instances where you might want to edit another copy of that clip somewhere

else in the Timeline, or re-edit another segment from that clip into the same area.

NOTE: Automation Follows Edit when clips with embedded automation are moved or pasted

from the Timeline. When clips with automation are instead pulled from the Media Pool, they

are in their default state with no automation attached.

Changing Clip Color in the Timeline

You can right-click one or more selected clips in the Timeline to change the clip color, to be more

organized. For example, you might set production audio clips containing dialog from different actors

to different colors, or you could set clips with dialog, music, and effects to different colors in order to

easily differentiate each clip’s purpose.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Editing Audio Clips in External Editors

While working in the Fairlight page, you have the ability to process an audio file using a third-party

application if necessary, in the event you need to use another application’s capabilities to create an

effect or solve an issue that can’t be accomplished in the Fairlight page itself. To do this, you must

first add one or more applications to the External Audio Process list in the Audio Plugins panel of the

System Preferences.

The External Audio Process list configured to send audio to Adobe Audition

To add an external audio process:


Open the System tab of the DaVinci Preferences, and select the Audio Plugins panel.


Click the Add button in the “Setup External Audio Processes” section.


To give the audio process a different name, double click in the Name column and type a new name.


Double-click in the empty Path column for the new process, and choose an application to assign

to that process from the dialog.


Choose the type of process you want it to be from the dropdown menu in the Type column.

Once you have one or more external audio applications configured in Preferences, you can use

them to process any audio clip in the Fairlight page by right-clicking an audio clip and choosing the

application you want to use from the External Audio Process submenu of the contextual menu.

When you do this, a duplicate of the audio clip media is copied (bounced) to the directory location

specified by the “Save clips to” field of the Capture and Playback panel of the Project Settings. At that

point, the external application is either opened or launched as a command from the command line

(depending on how the external application has been configured in Preferences).

Once the bounced audio is opened in the external application, you can process it however you need

to and bake in any changes made by saving/rendering/outputting and overwriting the original copied

audio media file. DaVinci Resolve detects when changes have been made, and the altered result is

automatically reimported as an additional audio layer on top of the original clip in the Timeline.

The way an audio application is configured in the DaVinci System Preferences dictates how the

bounced audio file is passed to the external program. There are three choices:

�Command Line: As a command line parameter, if your audio application is able to be

run from the Terminal.

�Clipboard: By placing the path to the bounced file in the clipboard, so you can paste it into the

application which has been automatically launched, or import it via a File > Open dialog.

�Reveal: By revealing the bounced copy in the file manager of your workstation, so you can drag

and drop it onto the application which has been automatically launched.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Exporting Audio Clips to External Files

For any workflow where you need to write clips from the Timeline to external files with extensive file

altering capabilities, you can use the Export Audio Files command.

To export clips to external files:


Select one or more clips in the Timeline.


Right-click the desired selected files and choose Export Audio Files from the contextual menu.


When the Export Audio Files dialog appears, choose the following:

a)	 Click Browse to choose a location to save the exported audio files.

b)	 (Optional) Enter a tag and one of the various Name options.

c)	 Choose a File Format, Sample Rate, and Bit Depth for the exported files.

d)	 Choose a Channel Format of Multi-Mono or Interleaved for the exported files.

e)	 Choose a Source of Individual Clips or Consolidated Clips; a dropdown menu further defines

the ranges of the complete timeline, a selected range, or just the selected clips.

f)

Checkboxes can further define using only the selected tracks, including hidden tracks and

padding to frame boundaries.

g)	 When exporting you can choose to include the Clip Level, the Clip Fades, the Clip EQ and FX,

and the Clip iXML.

h)	 The exported files can be normalized to predetermined target levels and target loudness

values with all of the standards offered throughout the Fairlight page.

The dialog that lets you choose options

for exporting clips to files


Click Export.

The selected audio files are written to the location you chose.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Sample Editing

You can zoom quite far into audio clips on the Fairlight page timeline, until you see the individual

samples that comprise the audio waveform of each clip. Samples are represented by control points

once you’ve zoomed in far enough.

When you zoom in far enough, you can see the individual samples of an audio clip as control points

You can non-destructively edit these control points to eliminate clicks and pops, and to effect other

fixes to problem audio clips.

Methods of editing audio samples:

�To see the editable audio samples: Zoom all the way into an audio clip until you see the sample

control points, using either Command-Plus or Command-Minus, the scroll wheel of your pointing

device, or by holding down the ZOOM button of your Fairlight editing panel and turning the

JOG/EDITING wheel.

�To edit a single audio sample: Click and drag that audio sample up or down to change its height.

�To edit a section of samples: Click and drag horizontally left or right across the samples you want

to edit to “redraw” the waveform any way you’d like.

�To reset all edited samples to their original state: Right-click an audio clip with edited samples,

and choose Reset Edited Samples from the contextual menu.

Black points show the previous levels when samples have been edited in a clip

Sample editing can be undone, just like any other editing procedure, as the edited sample points are

stored non-destructively within the DaVinci Resolve project.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT