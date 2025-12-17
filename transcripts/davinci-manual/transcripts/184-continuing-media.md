---
title: "Continuing Media"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 184
---

# Continuing Media

Management Jobs on Error

DaVinci Resolve has a more user-friendly behavior when dealing with errors during media

management operations. In previous versions, DaVinci Resolve would stop and wait for user input

immediately upon encountering an error, meaning that if an error happened while you were out at

lunch, nothing would happen until you came back. Now, DaVinci Resolve will skip error-flagged files

and continue to perform any remaining media management to all the other clips.

Options in the Media Management Window

The different Media Management operations offer different options.

�Entire Project Copy/Transcode all media: (Not available for Timelines) Choosing this option

copies the full amount of source media for every single clip in the project. If you add more media

later, and then use the Copy function again, DaVinci Resolve will only copy the additional files

needed to reflect the current Media Pool.

�Destination: Click the Browse button to choose a destination to which to copy the managed

media. To create a new directory, right-click a Volume icon in the File Browser list, choose New

Folder, type a name into the resulting dialog, and click OK.

�Timeline selections: If you’ve selected the Timelines mode of media management, you can

open the Timeline Selection controls and turn on the checkbox by each timeline with media you

want to include.

�Copy/Transcode All media: Copies all media available to that operation.

�Copy/Transcode Used media: Only copies media files for clips that are used in a timeline, and

copies them in their entirety.

�Copy/Transcode Used media and trim keeping x frame handles: Only copies media files that are

used in a timeline, but eliminates unused heads and tails except for user-specified handles.

�Use project name subfolder: Automatically creates a subfolder named for the project under the

destination directory that contains all the copied or transcoded media.

�Consolidate multiple edit segments into one media file: This option only becomes available if

you’ve selected “Copy and trim used media” If multiple clips in a timeline come from the same

media file, then a single consolidated media file will be generated that contains all frames from all

of these clips, along with whatever additional frames lie between them. Even though this option

results in more media being copied or moved, it’s extremely useful if you’re consolidating media

that you want to grade using the automatic grade linking of remote versions, as this preserves the

original relationship between each Timeline clip and the source media file it’s from.

�Preserve folder hierarchy after x folder levels: Retains a user-specified depth of the original

directory structure used by a clip’s corresponding source media file, recreating it when rendering

new files for output. The number you select determines how many levels of subdirectories DaVinci

Resolve will automatically create within the currently specified “Render job to” directory to match

the path used by the source files. Defaults to 0, which creates no matching subdirectories. The

number of path levels is defined relative to the head of each media file path.

�Relink to new files: (Appears for the Copy operation only) Relinks the selected clips and/or

timelines to the new media you’ve created by copying, wherever you’ve copied it to.


Edit | Chapter 46 Media Management

EDIT

Options for Transcode Only

The following options appear only when Transcode is the selected Media Management operation.

Settings: Exposes the default controls for the Media Management operation.

Video: Exposes the video codec controls for rendering to all available video formats.

Audio: Exposes the audio codec controls for rendering to all available audio formats.

File Naming When You Consolidate Media

When you’re media managing clip-based formats like QuickTime or MXF, if the “Trim Used Media”

option is on, and the “Consolidate Multiple Edit Segments Into One Media File” checkbox is off, then

timelines that use multiple clips derived from the same media file will generate multiple trimmed

media files. To prevent these files from overwriting one another, additional characters are appended

to each trimmed media file coming from the same source; which characters are used depends on the

video format.

For DPX files: _0, _1

For R3D files: _S000.RDC, _S001.RDC

For QuickTime files: _S000.mov, _S001.mov


Edit | Chapter 46 Media Management

EDIT

EDIT

Editing Effects

and Transitions

CONTENTS


Editing, Adding, and Copying Effects and Filters���������������������������������������������������������������������� 1002


Using Transitions�������������������������������������������������������������������������������������������������������������������������������������� 1017


Titles, Generators, and Stills��������������������������������������������������������������������������������������������������������������� 1037

50	 Compositing and Transforms in the Timeline������������������������������������������������������������������������������ 1053


Speed Effects�������������������������������������������������������������������������������������������������������������������������������������������� 1070


Subtitles and Closed Captioning������������������������������������������������������������������������������������������������������ 1083


Keyframing Effects����������������������������������������������������������������������������������������������������������������������������������� 1103


VFX Connect����������������������������������������������������������������������������������������������������������������������������������������������� 1121

Chapter 47

Editing, Adding,

and Copying Effects

and Filters

This chapter covers how to browse for and apply effects to clips in the Timeline,

how to copy them from clip to clip, how to remove them, and how to edit them

in the Inspector once they’ve been added.

For more information about the specific Resolve FX that are available, see “Resolve FX.”

Contents

Using the Effects Library���������������������������������������������������������������������������������������������������������������������������������������������������������������� 1003

The Toolbox������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1003

Open FX�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1004

Audio FX�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1004

Effects Library Favorites������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1005

Converting Fusion Compositions to Edit Effects��������������������������������������������������������������������������������������������������������������� 1005

Seeing Effects in the Timeline����������������������������������������������������������������������������������������������������������������������������������������������������� 1006

Using the Inspector��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1006

Inspector Effects Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1007

Adding Filters to Video Clips������������������������������������������������������������������������������������������������������������������������������������������������������� 1008

Render in Place�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1011

Fusion Effect Templates Cache��������������������������������������������������������������������������������������������������������������������������������������������������� 1012

Adjusting Multiple Clips at the Same Time���������������������������������������������������������������������������������������������������������������������������� 1013

Adjustment Clips��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1013

Paste Attributes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1014

Keyframe Options for Pasting Keyframed Attributes��������������������������������������������������������������������������������������������������������� 1015

Option to Ripple the Timeline for Pasting Speed Effects������������������������������������������������������������������������������������������������ 1015

Remove Attributes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1016


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

Using the Effects Library

All effects that you can add to your edit, including filters, transitions, titles, and generators, are found

in the Effects panel. The Effects panel shows a hierarchical list of all of the different transitions, title

effects, generators, and filters that are available, sorted by category.

To preview a video effect before placing it on a clip, ensure that “Hover Scrub Preview” is checked

in the Effects option menu, then simply hover your pointer over any thumbnail in the Effects tab and

move it across the thumbnail. The effect will preview in the Viewer using its default parameters, and

scrub through the clip that is selected in the Timeline. If no clip is selected then it will use the clip

currently under the playhead.

To activate a specific video effect on a clip, simply drag the thumbnail of the selected effect to a clip

on the Timeline. You can also double click the thumbnail, or drag an effect directly into the Inspector

to apply the effect to the selected clip. To adjust the effect’s parameters, open the Effects tab

in the Inspector.

Scrubbing over an Effect Thumbnail previews that effect in the Viewer.

You can search for a particular effect by clicking on the magnifying glass icon at the top of the Effects

Library. A drop-down menu just to the right of it lets you choose whether to search the entire FX library

(All Folders) or just the current folder.

You can search for effects and transitions using Category Names as a search term. For example,

searching for “Stylize” will bring up all the Resolve FX under the Stylize section.

The Toolbox

All of the video and audio transitions, titles, and generators that ship along with DaVinci Resolve:

Toolbox

Exposes all transitions, titles, generators, and effects at once.

Video Transitions: Contains all of the built-in transitions that are available from DaVinci,

organized by category. At the bottom of the list, a User category shows presets that

you’ve saved. You can drag any video transition to any edit point in the Timeline that has

overlapping clip handles to add it to your edit; you have the option to drag the transition so

that it ends on, is centered on, or starts on the edit point.

For more information, see Chapter 48, “Using Transitions.”


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

Audio Transitions: Contains audio transitions for creating crossfades.

Titles: Titles can be edited into the Timeline like any other clip. Once edited into the Timeline,

you can edit the title text and position directly in the Timeline Viewer, or you can access its

controls in the Inspector for further customization.

Generators: Generators can also be edited into the Timeline like any other clip. Selecting a

generator and opening the Inspector lets you access its controls for further customization.

You can also choose a standard duration for generators to appear within the Editing panel of

the User Preferences.

Effects: Effects are essentially placeholders in the Timeline that allow for more specialized

compositing in Fusion, or that let you modify the underlying tracks with an adjustment clip.