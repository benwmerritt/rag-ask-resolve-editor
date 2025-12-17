---
title: "Edit Index"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 6
---

# Edit Index

Clicking the Index button opens the Edit Index. By default, this shows an EDL-style list view of all the

edit events in the current timeline. Whichever timeline is selected in the Timeline list displays its events

here; each clip and transition is shown as an individual event, each of which contains multiple columns

of information. If you re-edit a timeline, your changes are automatically reflected in this list.

Edit Index List shown open


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Source/Offline and Timeline Viewers

The Source Viewer lets you view individual clips from the Media Pool to prepare them for editing.

Meanwhile, the Timeline Viewer shows the frame at the position of the playhead in the Timeline. You

can select either viewer by clicking, and the name of the viewer that currently has focus appears in

orange. The color shown in the Source Viewer usually reflects that of the original source media, while

the Timeline Viewer shows whatever grading you’ve done in the Color page.

Source and Timeline Viewers

If you want to change the Edit page layout to hide the Source Viewer, you can choose Workspace >

Single Viewer Mode to hide the Source Viewer and instead use just a single viewer to contextually

display either a selected Source Clip or the current frame of the Timeline.

Single Viewer mode

In Single Viewer mode, whatever you select in the Media Pool or Timeline determines which controls

appear in the Viewer, which lets you do nearly everything you can do with two simultaneously

open viewers.

You can also put either the Source or Timeline Viewers into Cinema Viewer mode by choosing

Workspace > Viewer Mode > Cinema Viewer (Command-F), causing whichever viewer is currently

selected to fill the entire screen. This command toggles Cinema Viewer mode on and off.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Inspector

The Inspector can be opened to let you customize compositing, transform, and cropping parameters

for clips, as well as clip-specific retime and scaling options. Furthermore, the Inspector lets you edit

the parameters of transitions, titles, and generators used in the Timeline, in order to customize their

effect. Ordinarily, the Inspector opens alongside the Source and Timeline Viewers, but on smaller

displays, opening the Inspector switches the Edit page to a single-viewer mode, showing you the

Timeline item that you’re inspecting alongside the Inspector with that clip’s parameters.

The Inspector, opened and showing a clip’s parameters

Toolbar

Eleven buttons starting from the left, running along the top of the Timeline, let you choose different

tools for performing various editing functions.

Buttons in the toolbar

Timeline

The Timeline shows whichever timeline you’ve double-clicked in the Timelines browser. It’s the

workspace where you either edit programs together from scratch, or import sequences from other

applications to work on inside of Resolve. You can only have one Timeline open at a time.

The Timeline is divided into audio and video tracks, each of which has a series of header controls

at the left that let you choose destination tracks for editing, name tracks, and turn tracks on and off,

among other things. The appearance of the Timeline can be customized using the Timeline View

Options drop-down in the toolbar.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

An edited timeline

Floating Timecode Window

A timecode window is available from the Workspace menu on every page, including the Edit page.

Choosing this option displays a floating timecode window that shows the timecode of the Viewer

or Timeline that currently has focus. This window is resizable so you can make the timecode larger

or smaller.

A new floating timecode window is available

Motion Graphics and

Visual Effects in DaVinci Resolve

To begin with, DaVinci Resolve has a wealth of effects in both the Edit and Color pages for creating

titles, transforming and animating clips, compositing and creating transparency effects, cutting mattes,

applying filters, image stabilization, lens dewarping, and so on.

Then of course there’s the Fusion page, which adds considerably more powerful VFX and motion

graphics capabilities via its node-based interface and deep toolset of effects nodes, keyframing and

curve editing controls, and 2D and 3D compositing features.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

To use DaVinci Resolve to the best effect, it’s prudent to begin to think of the Edit, Fusion, and

Color pages as complementary sets of controls.

•	 For editors, the Fusion and Color pages are really just two giant inspectors; one filled with

every compositing tool you could hope to use, and the other filled with every control for

color and visual adjustment you could want, each of which are only one click away.

•	 For compositing artists, the Edit page can be considered a robust shot management

interface as well as an opportunity to do VFX work that’s deeply integrated with the edit of

the program you’re working on.

•	 For colorists, the Edit page is a refined environment for dealing with conform issues and

taking care of myriad finishing tasks quickly and easily, that itself is only one click away.

For more information on the effects that are available in DaVinci Resolve, see the

chapters available within Part 6, “Editing Effects and Transitions” and Part 11, “Color

Page Effects”.

VFX Connect

As robust as the built-in compositing capabilities of DaVinci Resolve now are, when you run into

instances where the various capabilities found in the Edit, Fusion, and Color pages aren’t enough to

achieve the effect you require, you can use the VFX Connect features of DaVinci Resolve to send one

or more clips from the Edit page Timeline to Blackmagic Fusion, the powerful node-based compositing

application from Blackmagic Design, in order to do more robust compositing and effects work there.

Furthermore, the VFX Connect feature can also be used to round-trip media to and render results from

third-party applications such as The Foundry’s Nuke, Autodesk Flame, or Blender.

The New VFX Connect Clip dialo

This is a simple round-trip operation that lets you send clips from the DaVinci Resolve timeline to

Fusion or another application, where you’ll add effects and do whatever work needs to be done

before rendering a finished effect file that, if properly named, will automatically appear back in your

timeline. When you use VFX Connect with Blackmagic Fusion, a project file is automatically generated

and the render path is automatically named for automatic linking from the DaVinci Resolve timeline.

If you use this feature with third-party applications, you’ll need to set up the naming of your rendered

effect file manually.

For more information, see Chapter 63, “Introduction to Compositing in Fusion.”


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO