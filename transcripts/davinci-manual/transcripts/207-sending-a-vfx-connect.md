---
title: "Sending a VFX Connect"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 207
---

# Sending a VFX Connect

Directory to Another Machine

If you’re going to hand off a VFX Connect directory to someone else using a different workstation,

it’s a good idea to render self-contained media for the Fusion composition to make it easy to hand off

everything the compositing artist will need. Otherwise, you’ll need to manually find and provide the

associated media files yourself. There are two ways of rendering self-contained media for Fusion:

�If you check “Open VFX Connect Clip” in the New VFX Connect Clip dialog, then DaVinci Resolve

by default renders each of the video clips you selected, along with every speed effect, transform,

and Color page operation that’s been applied to each clip, using the Timeline Color Space.

�If you haven’t opened the VFX Connect clip in Fusion yet, you can also right-click any

VFX Connect clip in the Media Pool, and choose VFX Connect > Render Media from the

contextual menu.

Once that’s done, there are two ways you can locate the actual VFX Connect directory’s

location, in order to copy it for whomever is going to be doing the compositing work for you.

•	 You can turn on the Custom Location checkbox in the New VFX Connect Clip dialog, then

click the Browse button and choose a location where the resulting directory is easily copied.

•	 You can also right-click on any VFX Connect clip in the Media Pool, and choose Reveal in

Finder to open that VFX Connect clip’s directory.

Since your DaVinci Resolve project keeps track of the location of the VFX Connect directory from the

moment it’s created, you don’t want to move it, since DaVinci Resolve is counting on it being where it

thinks it is. Once your colleague has completed the compositing work in Fusion, all they need to do is

send you back the Fusion Composition file (just so you can keep everything together), and the media

they rendered, both of which you need only copy to the top level of the corresponding VFX Connect

directory. Once you do that, DaVinci Resolve should automatically see the rendered media and refresh

those VFX Connect clips on your timeline.

Creating Multiple Versions of Fusion Clips on Another Machine

If you’ve handed off the directory created by the VFX Connect process to someone off site, they can

still create multiple versions of the composite that can be managed by DaVinci Resolve.

Use the Save As command in Fusion to save a duplicate of the Fusion project with the “_v1”

segment of the filename incremented to the next version number, such as “_v2” if it’s version two

of the composite. Make sure you save this duplicate Fusion project into the same directory as the

original, so DaVinci Resolve can find it. Once created, you can change this duplicate project file any

way you need.

When you’re finished, select the Saver node (at the very end of the Fusion node tree), and change the

filename by incrementing the V1 part of the Filename field. For example, if your clip is being named

Output_V1.mov, then change the filename to Output_V2.mov in the Tools tab, and render. If you’re

rendering a DPX image sequence, then you’ll want to change the name of the folder that encloses the

frames, so change the filename from “.../fusion/OutputDirectory_V1/Output_00000000.dpx” to “.../

fusion/OutputDirectory_V2/ Output_00000000.dpx” to obtain a correctly named second version.


Editing Effects and Transitions | Chapter 54 VFX Connect

EDIT

Updating VFX Connect Clips

Using Render Media and Refresh

If you change a grade or effect that’s applied to a clip inside of a VFX Connect clip, you’ll need to

right-click that clip and choose VFX Connect > Render Media to re-render updated media files for the

Fusion project.

If you re-render a Fusion composite and overwrite media that’s already referenced by a VFX Connect

clip in an open DaVinci Resolve project, you may need to refresh that media reference in DaVinci

Resolve. The easy way to do this is to right-click any VFX Connect clip in the Media Pool, and choose

VFX Connect > Refresh.


Editing Effects and Transitions | Chapter 54 VFX Connect

EDIT

EDIT

Import and

Conform Projects

CONTENTS


Preparing Timelines for Import and Comparison������������������������������������������������������������������������ 1130


Conforming and Relinking Clips��������������������������������������������������������������������������������������������������������� 1144


Creating Digital Dailies for Round Trip Workflows���������������������������������������������������������������������� 1170


Conforming XML Files����������������������������������������������������������������������������������������������������������������������������� 1177


Conforming AAF Files���������������������������������������������������������������������������������������������������������������������������� 1182

60	 Conforming EDL Files����������������������������������������������������������������������������������������������������������������������������� 1196


Conforming OTIO Files ������������������������������������������������������������������������������������������������������������������������ 1202


Conforming ADL Files���������������������������������������������������������������������������������������������������������������������������� 1207

Chapter 55

Preparing

Timelines for Import

and Comparison

Generally speaking, “conforming” a project describes the process of importing a

project exchange file from another post-production application, and automatically

relinking each clip in the imported timeline to the high-quality media files each clip

corresponds to.

If you need to continue editing, color correct, or finish a project that was put together in another

application, you can import via the EDL, AAF, or XML project exchange formats. When you go through

the process of conforming a project, you use the imported project data to arrange the clips in the

Media Pool into a timeline that constitutes the program that’s about to be graded.

This chapter walks you through the process of preparing timelines in other applications prior to moving

them into DaVinci Resolve and covers which effects have counterparts in the DaVinci Resolve timeline.

It ends with instructions on how to set up to compare a reference movie to the Timeline.

Contents

Preparing to Move Your Project to DaVinci Resolve����������������������������������������������������������������������������������������������������������� 1131

Move Clips to the Lowest Video Track���������������������������������������������������������������������������������������������������������������������������������������� 1131

Organize Unsupported Media Files���������������������������������������������������������������������������������������������������������������������������������������������� 1131

Creating an Offline Reference Movie����������������������������������������������������������������������������������������������������������������������������������������� 1132

Mixed Frame Sizes and Mixed Codecs������������������������������������������������������������������������������������������������������������������������������������� 1132

Mixed Frame Rates������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1132

Importing Effects when Conforming Edits����������������������������������������������������������������������������������������������������������������������������� 1134

About Supported Color Corrections������������������������������������������������������������������������������������������������������������������������������������������ 1135

About Supported Transitions��������������������������������������������������������������������������������������������������������������������������������������������������������� 1135

Transition Names��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1136

About Supported Opacity, Position, Scale, and Rotation Settings����������������������������������������������������������������������������� 1136

About Flip and Flop Support���������������������������������������������������������������������������������������������������������������������������������������������������������� 1136


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT

Preparing to Move Your Project

to DaVinci Resolve

When you’re preparing to move a project from another NLE to DaVinci Resolve, there are a few steps

you can take to make your work more organized.

Move Clips to the Lowest Video Track

Editors often use the multiple tracks NLEs offer for simple clip organization in the edit of a scene. While

this is convenient for offline editorial, it is less convenient when you’re trying to conform, grade, finish,

and render the media used by a project as quickly and efficiently as possible.

For this reason, it’s a good idea to move all clips that are not stacked or superimposed as part of a

compositing operation down to track V1 of the Timeline in your NLE. This produces a simplified edit

that has many advantages. The project becomes smaller to move because there’s less media in the

Timeline, and consequently becomes faster to render. Furthermore, the colorist is spared confusion

because this eliminates “hidden” media that is nonetheless connected to other clips that can be seen.

It’s also helpful, once you’ve reorganized the Timeline, to eliminate any empty tracks that are left.

This can be done from within DaVinci Resolve, but doing it in your NLE further simplifies the project

import process.

Organize Unsupported Media Files

Depending on your workflow and on the NLE you’re working with, there may be clips using formats

that are unsupported in DaVinci Resolve. Unsupported generators, media formats, and other effects

constructs may simply not be seen in DaVinci Resolve, and will consequently appear as unlinked clips.

If you know this in advance, you can move all such clips into dedicated tracks where they can be

isolated, and the track can be turned off to hide the unsupported clips, simplifying timeline navigation.

This also saves the colorist from the need to worry about why there are offline clips in the Timeline at

3 o’clock in the morning, immediately before starting a render.

Pitch and Yaw����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1136

About “Ken Burns Effect” and Dynamic Zoom����������������������������������������������������������������������������������������������������������������������� 1137

About Speed Effects��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1137

About Nested Sequences and Compound Clips������������������������������������������������������������������������������������������������������������������ 1137

About Supported Composite Modes����������������������������������������������������������������������������������������������������������������������������������������� 1138

About Supported Still Image Formats��������������������������������������������������������������������������������������������������������������������������������������� 1138

About Supported Alpha Channels���������������������������������������������������������������������������������������������������������������������������������������������� 1138

About Imported Text Effects���������������������������������������������������������������������������������������������������������������������������������������������������������� 1139

About Imported Audio in AAF Projects������������������������������������������������������������������������������������������������������������������������������������ 1139

Verifying Imported Timelines Using Offline References������������������������������������������������������������������������������������������������ 1140

Why Set Up An Offline Comparison?����������������������������������������������������������������������������������������������������������������������������������������� 1140

Assigning a Clip or Timeline for Offline Comparison����������������������������������������������������������������������������������������������������������� 1141

Setting Up an Offline Reference/Timeline Comparison���������������������������������������������������������������������������������������������������� 1142


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT