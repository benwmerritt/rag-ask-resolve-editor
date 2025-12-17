---
title: "Chapter 64"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 223
---

# Chapter 64

Exploring the

Fusion Interface

This chapter provides an orientation on the Fusion user interface, providing a

quick tour of what tools are available, where to find things, and how the different

panels fit together to help you build and refine compositions in this powerful

node‑based environment.

Contents

The Fusion User Interface�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1218

The Work Area��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1219

Interface Toolbar��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1219

Choosing Which Panel Has Focus���������������������������������������������������������������������������������������������������������������������������������������������� 1220

Viewers����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1221

Zooming and Panning into Viewers������������������������������������������������������������������������������������������������������������������������������������������� 1222

Loading Nodes Into Viewers��������������������������������������������������������������������������������������������������������������������������������������������������������� 1222

Clearing Viewers��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1223

Viewer Controls����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1223

Time Ruler and Transport Controls������������������������������������������������������������������������������������������������������������������������������������������� 1225

Time Ruler Controls in the Fusion Page���������������������������������������������������������������������������������������������������������������������������������� 1225

Time Ruler Controls in Fusion Studio���������������������������������������������������������������������������������������������������������������������������������������� 1226

The Playhead����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1227

Zoom and Scroll Bar��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1227

Transport Controls in the Fusion Page�������������������������������������������������������������������������������������������������������������������������������������� 1227

Audio Monitoring��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1229

Transport Controls in Fusion Studio������������������������������������������������������������������������������������������������������������������������������������������� 1231

Changing the Time Display Format������������������������������������������������������������������������������������������������������������������������������������������� 1235

Keyframe Display in the Time Ruler������������������������������������������������������������������������������������������������������������������������������������������� 1235

The Fusion RAM Cache for Playback���������������������������������������������������������������������������������������������������������������������������������������� 1235

Toolbar������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1237

Customizing the Toolbar������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1237


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Node Editor������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1239

Adding Nodes to Your Composition������������������������������������������������������������������������������������������������������������������������������������������ 1239

Removing Nodes from Your Composition������������������������������������������������������������������������������������������������������������������������������ 1240

Identifying Node Inputs and Node Outputs�������������������������������������������������������������������������������������������������������������������������� 1240

Node Editing Essentials������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1240

Navigating the Node Editor������������������������������������������������������������������������������������������������������������������������������������������������������������ 1242

Vertical Node Editor Layouts��������������������������������������������������������������������������������������������������������������������������������������������������������� 1243

Keeping Organized����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1243

Status Bar����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1244

Effects Library�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1245

The Inspector��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1246

The Tools and Modifiers Panels��������������������������������������������������������������������������������������������������������������������������������������������������� 1246

Parameter Header Controls����������������������������������������������������������������������������������������������������������������������������������������������������������� 1246

Parameter Tabs������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1247

Keyframes Editor��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1247

Keyframes Editor Control Summary������������������������������������������������������������������������������������������������������������������������������������������ 1248

Adjusting Clip Timings���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1248

Adjusting Effect Timings������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1248

Adjusting Keyframe Timings��������������������������������������������������������������������������������������������������������������������������������������������������������� 1249

Spline Editor������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1250

Spline Editor Control Summary������������������������������������������������������������������������������������������������������������������������������������������������������ 1251

Choosing Which Parameters to Show���������������������������������������������������������������������������������������������������������������������������������������� 1251

Essential Spline Editing���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1251

Essential Spline Editing Tools and Modes������������������������������������������������������������������������������������������������������������������������������ 1252

Thumbnail Timeline in the Fusion Page��������������������������������������������������������������������������������������������������������������������������������� 1254

The Media Pool in the Fusion Page������������������������������������������������������������������������������������������������������������������������������������������ 1255

Importing Media Into the Media Pool on the Fusion Page��������������������������������������������������������������������������������������������� 1255

Bins in Fusion Studio������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1256

Bins Interface����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1257

The Bin Studio Player������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1258

The Console������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1259

Customizing Fusion��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1260

The Fusion Settings Window�������������������������������������������������������������������������������������������������������������������������������������������������������� 1260

Showing and Hiding Panels������������������������������������������������������������������������������������������������������������������������������������������������������������ 1261

Resizing Panels������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1261

Fusion Studio Floating Frame�������������������������������������������������������������������������������������������������������������������������������������������������������� 1261

Fusion Keyboard Remapping������������������������������������������������������������������������������������������������������������������������������������������������������� 1262

Fusion Studio Keyboard Remapping���������������������������������������������������������������������������������������������������������������������������������������� 1262

Undo and Redo������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1263


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

The Fusion User Interface

If you open up everything at once, Fusion is divided into four principal regions designed to help

you make fast work of node-based compositing. The viewer(s) are at the top, the work area is at the

bottom, the Inspector is at the right, and the Effects Library is the area found at the left. In DaVinci

Resolve’s Fusion page, the Effects Library shares space with the Media Pool. All these panels work

together to let you add effects, paint to correct issues, create motion graphics or title sequences, or

build sophisticated 3D and multi-layered composites.

The Fusion user interface shown completely

However, Fusion doesn’t have to be that complicated, and in truth, you can work very nicely with only

the viewer, Node Editor, and Inspector open for a simplified experience.

A simplified set of Fusion controls for everyday working


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

The Work Area

You probably won’t see the term “the work area” used much, in favor of the specific panels within the

work area that you’ll be using. Still, the area referred to as the work area is the region at the bottom

half of the Fusion user interface, within which you can expose the three main panels used to construct

compositions and edit animations in Fusion. These are the Node Editor, the Spline Editor, and the

Keyframes Editor. By default, the Node Editor is the first thing you’ll see, and the main area you’ll be

working within, but it can sit side-by-side with the Spline Editor and Keyframes Editor as necessary.

You can make more horizontal room on your display for these three panels by putting the Effects

Library and Inspector into a half-height mode, if necessary.

The work area showing the Node Editor, the Spline Editor, and the Keyframes Editor

Interface Toolbar

At the very top of Fusion is a toolbar with buttons that let you show and hide different parts of the user

interface (UI). Buttons with labels identify which parts of the UI can be shown or hidden. In DaVinci

Resolve’s Fusion page, if you right-click anywhere within this toolbar, you have the option of displaying

this bar with or without text labels.

The UI toolbar of the Fusion page

The UI toolbar of Fusion Studio

These buttons are as follows, from left to right:

�Media Pool/Effects Library Full Height: Lets you set the area used by the Media Pool (DaVinci

Resolve only) and/or Effects Library to take up the full height of your display, giving you more area

for browsing at the expense of a narrower Node Editor and viewer area. At half-height, the Media

Pool/Templates/Effects Library are restricted to the top half of the UI along with the viewers (you

can only show one at a time), and the Node Editor takes up the full width of your display.

�Media Pool: (DaVinci Resolve only): Shows and hides the Media Pool, from which you can drag

additional clips into the Node Editor to use them in your Fusion page composition.

�Effects Library: Opens or hides the repository of all node tools available to use in Fusion.

From here, you can click nodes to add them after the currently selected node in the Node Editor,

or you can drag and drop nodes to any part of the node tree you like.

�Clips: (DaVinci Resolve only): Opens and closes the Thumbnail timeline, which lets you

navigate your program, create and manage multiple versions of compositions, and reset the

current composition.

�Nodes: Opens and closes the Node Editor, where you build and edit your compositions.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

�Console (Fusion Studio only): The Console is a window in which you can see the error, log,

script, and input messages that may explain something Fusion is trying to do in greater detail. The

Console is also where you can read FusionScript outputs, or input FusionScripts directly.

�Spline: Opens and closes the Spline Editor, where you can edit the curves that interpolate

keyframe animations to customize and perfect their timing. Each keyframed parameter appears

hierarchically within the effect in which it appears in a list to the left.

�Keyframes: Opens and closes the Keyframes Editor, which shows each clip and effects node in

your Fusion composition as a layer. You can use the Keyframes Editor to edit and adjust the timing

of keyframes that have been added to various effects in your composition. You can also use the

Keyframes Editor to slide the relative timing of clips that have been added to Fusion, as well as

to trim their In and Out points. A spreadsheet can be shown and hidden within which you can

numerically edit keyframe values for selected effects.

�Metadata (DaVinci Resolve only): Hides or shows the Metadata Editor, which lets you read and

edit the available clip and project metadata associated with any piece of media within a composite.

�Inspector: Shows or hides the Inspector, which shows you all the editable parameters and controls

that correspond to selected nodes in the Node Editor. You can show the parameters for multiple

nodes at once, and even pin the parameters of nodes you need to continue editing so that they’re

displayed even if those nodes aren’t selected.

�Inspector Height: Lets you open the Inspector to be half height (the height of the viewer area)

or full height (the height of your entire display). Half height allows more room for the Node Editor,

Spline Editor, and/or Keyframes Editor, but full height lets you simultaneously edit more node

parameters or have enough room to display the parameters of multiple nodes at once.

Choosing Which Panel Has Focus

Whenever you click somewhere on the Fusion interface using the pointer or using a keyboard

shortcut to “select” a particular panel, you give that panel of the user interface “focus.” A panel with

focus captures specific keyboard shortcuts to do something within that panel, as opposed to doing

something elsewhere in the interface.

To make it easier to keep track of which panel has focus, a highlight appears at the top edge of

whichever panel has focus. In DaVinci Resolve, you must turn on “Show focus indicators in the

User Interface” in the UI Settings panel of the User Preferences to see the highlight.

The focus indicator shown at the top edge of the Media Pool, shown next to a viewer that doesn’t have focus


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION