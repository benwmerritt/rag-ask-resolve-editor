---
title: "Creating Stereo 3D Clips"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 62
---

# Creating Stereo 3D Clips

From Separate Files

If you’re working with stereo media that was either captured or created as individual left- and right‑eye

files, then you need to convert each matching pair of clips into the stereo 3D clips that you’ll need to

work in DaVinci Resolve. This is a two-step procedure.

Step 1 – Import and Organize Your Media

You need to import all of the left-eye and right-eye media into separate bins.


Open the Media page, and create three Media Pool bins named “Left,” “Right,” and “Stereo Clips.”

The exact names are not important, but the way the media is organized is.


Import all left-eye media into the “Left” bin, and all right-eye media into the “Right” bin. If you’re

importing stereoscopic Cineform media, you still need to create this kind of organization, which

requires you to place duplicates of each clip into each of the “Left” and “Right” bins.

Step 2 – Generate 3D Stereo Clips

Once you’ve organized your media appropriately, you’re set up to synchronize the left- and right-eye

clips using timecode.


Create a new bin in the Media Pool, and name it “Stereo Clips.” This is the bin that will eventually

contain the linked stereo clips you’re about to create.

How to organize media for working in stereo 3D


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA


Right-click anywhere within the Media Pool and choose Stereo 3D Sync.

The Stereo 3D Sync dialog appears, with buttons for choosing the left-eye folder, choosing the

right-eye folder, choosing the output folder, and checkboxes for specifying whether to match

reel names and file names, and additional fields for entering characters that identify left- and

right-eye clips.

The Stereo Media Sync window


Click the Browse button corresponding to “Choose left eye folder” and then use the hierarchical

list of bins that appears to choose the bin you named “Left.” Follow the same procedure to choose

the right-eye media.


Click the Browse button corresponding to “Output folder” and then use the hierarchical list of bins

that appears to choose the bin you named “Stereo Clips.”


Choose which matching criteria to use. Ideally, you only need to use whichever one of the three

criteria that apply. The three options are:

Match Reel Name: If the reel names of the left- and right-eye media match, turn this checkbox on.

Match File Name checkbox: If the file names of the left- and right-eye media match,

turn this checkbox on.

Left Identifiers and Right Identifiers fields: If the left- and right-eye clips are identified by a

special subset of characters within the file name (for example, “3D_R” and “3D_L”), then you

can type each into the appropriate field, and these characters will be used to match the left

and right eyes together.


Click Sync.

The original clips in the Left and Right bins disappear, and a full set of Stereo 3D clips appear in

the output bin you selected in step four.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Final stereo clips, ready to be edited and graded

Step 3 – (Optional) Create Optimized Media

If your stereo media is excessively large, you can create optimized media.


Select the stereo clips you’ve created.


Right-click one of the selected clips, and choose Generate Optimized Media from the contextual

menu. A window appears showing you ho.w long it will take to finish creating optimized media.

Monitoring Stereoscopic 3D

in the Edit Page

You can now view a Stereoscopic 3D signal directly from the Edit page. Previously, the Edit page

was restricted to left eye for video output monitoring. The Edit Page Viewer itself still shows only

a single eye, but it now displays Stereoscopic 3D video from the Decklink or Ultrastudio video

outputs. The 3D palette in the Color page has the stereoscopic controls to select the stereo viewing

options (Side by Side, Anaglyph, Line by Line, etc.), as well as adjusting the convergence and other

stereoscopic parameters.

Converting Clips Between

Stereo and Mono

You also have the option of converting clips between mono and stereo 3D using a pair of commands

in the Media Pool.

Converting Stereo Clips Back to Mono

If necessary, you can split one or more stereo clips into mono clips using a single command.

To convert stereo clips into mono clips:


Select one or more stereo clips in the Media Pool.


Right-click one of the selected clips and choose Split Stereo 3D Clips from the contextual menu.

Afterwards, two new bins are created named Left and Right, containing the individual left- and right-

eye clips that you’ve split apart.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Converting Mono Clips or an Entire Timeline to Stereo

Non-stereo clips (for which there are not separate left- and right-eye media files) can be converted into

stereo clips either individually or throughout an entire timeline for one of two different reasons:

�You can convert non-stereo clips into stereo for use in a stereo project, so they output properly

along with the rest of a stereo timeline, albeit without adjustable convergence or depth effects.

�If you want to grade an HDR and non-HDR version of your program at the same time, converting

non-stereo clips to stereo makes it possible for you to a) manage two separate SDR and HDR

grades for each clip in a timeline using the left- and right-eye channels, and b) output the SDR and

HDR signals separately via your compatible Blackmagic Design interface’s left- and right-eye SDI

outputs when you turn on the “Use dual outputs on SDI” checkbox in the Video Monitoring section

of the Master Settings panel of the Project Settings.

To convert mono clips into stereo clips:


Select one or more non-stereo clips in the Media Pool.


Right-click one of the selected clips and choose Convert to Stereo from the contextual menu.

Afterwards, that clip appears in the Media Pool as a Stereo 3D clip, and when edited into a timeline,

can expose its controls in the 3D Stereo palette in the Color page.

If you have a timeline full of clips that you’ve just converted into stereo using the above procedure, you

need to take the additional step of setting the Timeline to stereo in order to create stereo grades for

each clip.

To convert a timeline to have stereo grades for

simultaneous HDR/SDR output while grading:

Right-click a timeline in the Media Pool and choose Timelines > Set Timeline to Stereo.

For more information about using stereo timeline workflows for simultaneous HDR and SDR

grading, see Chapter 9, “Data Levels, Color Management, and ACES.”

Attaching Mattes to Stereo 3D Clips

If you have left- and right-eye mattes that need to be attached to stereo clips, the process works

identically to importing mattes for regular clips, except that when you’ve selected a stereo 3D

clip in the Media Pool, you have two matte import commands, “Add As Left Eye Matte,” and

“Add As Right Eye Matte.”


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Organizing and Grading Stereo 3D Dailies

A common workflow is the creation of digital dailies within DaVinci Resolve before editing in an NLE.

This provides the editors, director, and producers with the advantage of having more attractive media

to work with, that’s also more comfortable to view if handled with the automatic geometry and color-

matching functions that match the media of each pair of shots together for a preliminary left- and

right-eye balance. The resulting Timelines can then be output to whichever media format is most

convenient to use.

Step 1 – Create 3D Stereo Clips

The very first step in the process of creating dailies is to import all of the left-eye and right-eye media

into individually organized bins, and to then link them together to create stereo 3D clips, as described

in the previous section.

Step 2 – Edit the New Stereo Clips

Into One or More Timelines for Grading

Now that you’ve created a set of Stereo 3D clips, you’re ready to edit them into one or more Timelines

for grading. You can do this by simply creating a new Timeline and deselect the Empty Timeline

checkbox. A new Timeline will be created with the stereo 3D clips you created.

Step 3 – Align Your Media

For the stereoscopic effect to work without causing headaches, it’s critical that both eyes are aligned.

This can be tricky to adjust using manual controls, but is something that can be automatically analyzed.

You can perform stereo 3D alignment to a single clip using the Stereo 3D Palette controls, or you can

select a range of clips to align all of them automatically at once. There are two methods of alignment;

which is more appropriate depends on the type of geometry issues you have to address.

�Transform Alignment: Analyzes the image and makes vertical and rotational adjustments to line

up the left- and right-eye images as closely as possible.

�Vertical Skew: Analyzes the images and makes a vertical-only adjustment to line up the left- and

right-eye images.

Controls for aligning the left- and right-eye media

Step 4 – Grading Stereo Media

Grade the clips in the Timeline as you would any other digital dailies, with the sole addition of

using the controls in the Stereo 3D palette to control monitoring and manage the adjustments

made to each eye as necessary. The currently selected eye will be reflected in the video scopes.

As when creating any other kind of dailies, you can use LUTs, the Timeline Grade, and individual clip

grading to make whatever adjustments are necessary to create useful media for editing.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Grading Windows

If you’re using windows, The Color group of the General Options panel of the Project Settings has a

checkbox called “Apply stereoscopic convergence to windows and effects” that correctly maintains

the position of a window that’s been properly placed over each eye when convergence is adjusted.

You must turn on a checkbox in the Project Settings

to enable stereo convergence for windows

When this option is enabled, the Window palette displays an additional Transform parameter,

“Convergence,” that lets you create properly aligned convergence for a window placed onto a

stereoscopic 3D clip.

The Convergence control in the

Transform section of the Window palette

After placing a window over a feature within the image while monitoring one eye, you can enable

Stereo output in the Stereo 3D palette and use the Pan and Convergence controls to make sure that

window is properly stereo-aligned over the same feature in both eyes. At that point, adjusting the

Convergence control in the Stereo 3D palette correctly maintains the position of the window within the

grade of each eye.

A convergence-adjusted window in stereo


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Matching Media From Left and Right Eyes

To help you manage the visual differences between left- and right-eye clips, there are also three

automatic color matching commands that can be used to batch process as many clips as you need to

adjust at once.

�Stereo Color Match (Primary Controls): Uses the Lift/Gamma/Gain controls to match one eye to

the other. The result is a simple adjustment that’s easy to customize, but may not work as well as

Custom Curves in some instances.

�Stereo Color Match (Custom Curves): Uses the Custom Curves to create a multipoint adjustment

to match one eye to the other. Can be more effective with challenging shots.

�Stereo Color Match (Dense Color Match): Performs a pixel by pixel, frame by frame color match

that is incredibly accurate. This operation is processor intensive, so if you’re going to batch

process many clips, or if you’re matching long clips, you’ll want to make sure you have adequate

time. Because this is such a precise match, it’s recommended to use Dense Color Match after

you’ve used one of the stereo alignment commands.

Controls for matching the grade of

the left and right eye media

Step 5 – Output Offline or Online Media for Editing

When you’re done applying whatever grading is necessary to make the media suitable for editing,

you’ll need to export each clip as separate left- and right-eye clips using the controls of the

Deliver page.


Open the Deliver page, and set up your render to output the format of media you require. Be sure

to do the following:

�Set Render Timeline As to Individual source clips.

�Turn on the “Filename uses Source Name” checkbox.

�To render both eyes’ worth of media, choose “Both eyes as” from the Render Stereoscopic 3D

option, and choose Separate Files from the accompanying pop-up menu. Optionally, you could

also choose to render only the left-eye or right-eye media.


Choose how much of the Timeline to render from the Render pop-up menu in the Timeline toolbar;

to render everything, choose Entire Timeline.


Click “Add Job to Render Queue.”


Click Start Render.

DaVinci Resolve will now render either two sets of left- and right-eye clips, or one set of media

corresponding to the eye you chose.

To make sure that the resulting edited project conforms easily to the originating DaVinci Resolve

project, it’s important to be sure that you render individual source clips, and that you turn on the

“Filename user Source Name” checkbox, in order to clone the timecode, reel numbers, and file names

of the source media.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA