---
title: "The Cut Page"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 93
---

# The Cut Page

CONTENTS


Using the Cut Page����������������������������������������������������������������������������������������������������������������������������������� 497


Importing and Organizing Media in the Cut Page������������������������������������������������������������������������ 516


Fast Editing in the Cut Page����������������������������������������������������������������������������������������������������������������� 542


Trimming in the Cut Page����������������������������������������������������������������������������������������������������������������������� 578


Using the Inspector in the Cut Page�������������������������������������������������������������������������������������������������� 597


Video and Audio Effects in the Cut Page���������������������������������������������������������������������������������������� 619


Quick Export����������������������������������������������������������������������������������������������������������������������������������������������� 650

Chapter 26

Using the Cut Page

The Cut page is a focused environment for fast editing. It’s useful in situations where you need

to quickly cut a news segment, build an episode of web content, edit a straightforward program,

experiment with multiple arrangements of a scene, or put together a first assembly edit.

The Cut page is also a good introductory editing interface for people who are new to editing, as it

presents a streamlined set of tools that are fast to learn and simple to use. Whatever your background,

you’ll find the Cut page to be a valuable addition to your editing experience in DaVinci Resolve.

Contents

Overview of the Cut Page���������������������������������������������������������������������������������������������������������������������������������������������������������������� 498

Overview of the Cut Page User Interface��������������������������������������������������������������������������������������������������������������������������������� 498

Customizing the UI������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 498

Choose Settings Before You Start����������������������������������������������������������������������������������������������������������������������������������������������� 499

Timeline Resolution Quick Menu�������������������������������������������������������������������������������������������������������������������������������������������������� 499

The Media Pool������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 500

The Viewer������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 501

Playing Clips and Navigating the Timeline������������������������������������������������������������������������������������������������������������������������������� 502

Optimized UI Layouts for Vertical Editing��������������������������������������������������������������������������������������������������������������������������������� 503

Tools������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 503

Bypass Color Grades and Fusion������������������������������������������������������������������������������������������������������������������������������������������������� 504

Export The Current Frame from The Viewer��������������������������������������������������������������������������������������������������������������������������� 504

Audio Meter��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 504

The Timeline������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 505

Upper Timeline�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 505

Lower Timeline��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 506

Tracks���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 508

Gaps�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 511

Timeline Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 511

Audio Mixer����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 511

Audio Mixer Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 512

Mute and Solo Tracks For Output�������������������������������������������������������������������������������������������������������������������������������������������������� 513

Replay���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 513

Undo and Redo in DaVinci Resolve��������������������������������������������������������������������������������������������������������������������������������������������� 513


The Cut Page | Chapter 26 Using the Cut Page

CUT

Overview of the Cut Page

With the addition of the Cut page, DaVinci Resolve now has two editing environments, intended for

two different audiences. While the Cut and Edit pages share many of the same panels such as the

Media Pool, the Timeline, and the Viewer, the controls that are exposed on the Cut page have been

designed for speed, so you can cut professional programs faster than you’ve ever been able to before.

Overview of the Cut Page User Interface

The default workspace of the Cut page consists of the Media Pool, a single Viewer, and the

Timeline area. These three regions let you quickly import and organize clips, edit clips, and even

export the result, all from within the Cut page.

The Cut page interface

Customizing the UI

A User Interface toolbar at the top of the Cut page lets you hide and show different panels as

necessary. For example, you can hide the Media Pool if you wanted more room for the Viewer.

You can also replace the Media Pool with other browsers in the Media Pool’s default area, showing

the Sync Bin, Transitions, Titles, or Effects Browser in order to add those effects to your program in

the Timeline. On the right side of the User Interface toolbar you can perform a Quick Export, expand

the Viewer to Full Screen, or open the Inspector.

Separate tabs on the left let you open the Media Pool,

Sync Bin, Keyframe Editor, Transitions, Titles, and Effects browser.


The Cut Page | Chapter 26 Using the Cut Page

CUT

You can resize the Media Pool and Viewer by dragging the vertical seam that connects them to the left

or right, in the process making one panel bigger and the neighboring panel smaller.

The Viewer resize handle

The Timeline resize handle

You can also resize the Timeline area by dragging the timeline handle (at the upper right corner of

the Timeline) up or down, making more or less room for the Timeline while simultaneously resizing the

Media Pool and Viewer areas.

Choose Settings Before You Start

When you first create a new project, you need to define its Timeline settings; you can optionally

choose from common presets or a fully custom setup.

Timeline Resolution Quick Menu

This drop-down menu, to the top-right of the Viewer, lets you quickly choose which resolution you

want to work at. A Custom option lets you open up the Timeline Settings panel in order to choose your

own options.

For more information about the Timeline Settings, see Chapter 6, “Project Settings.”

The Project Settings quick menu


The Cut Page | Chapter 26 Using the Cut Page

CUT

The Media Pool

The Media Pool contains all video clips, audio clips, graphics, and other media that you import into

your project. You can create bins with which to organize all of this media, to make it easier to find what

you need quickly. These bins are opened via the bin drop-down at the upper left-hand corner.

Each piece of media you import, whether it’s video, audio, or graphics, appears as an individual clip

and can be selected, scrubbed for fast viewing, reorganized into bins, opened into the Viewer for

playback, or edited into a timeline using the edit buttons or via drag and drop.

The Media Pool in Thumbnail view

View icons at the upper right of the Media Pool let you see your clips in different ways, depending on

what you need to accomplish.

The Viewing ModeFs buttons

Metadata view: Each clip is represented by its own card with a scrubbable thumbnail

and basic clip metadata information visible. This view is designed to have more

metadata information than a thumbnail view but more targeted information than the

List view.

Thumbnail view: Each clip is represented by a scrubbable thumbnail. Hover the

playhead over each thumbnail and move it left and right to see the clip’s image play,

and use the I and O keys to mark sections of a clip that you want to use. Clicking on

the lower right corner of a thumbnail reveals the clip’s metadata.

Filmstrip view: Each clip is represented by a filmstrip of consecutive frames the

length of the Media Pool. Hover the playhead over the clip and move it left and

right to see the clip’s image play, and use the I and O keys to mark sections of a clip

that you want to use.

List view: Each clip appears as an item in a multi-column list showing a variety

of metadata about each clip. In List view, you can click the header of any column

to sort the contents by that column’s information (clicking again toggles the sort

order between Ascending and Descending). Scrolling right reveals additional

columns of information.


The Cut Page | Chapter 26 Using the Cut Page

CUT

A Sort Media By drop-down menu lets you choose which

criteria defines the order in which clips in the Media Pool

are arranged. Options include: Custom, Timecode, Camera,

Date Time, Clip Name, Bin, Scene Shot, Clip Color, Date

Modified, Date Imported, and Online Status. You can choose

to sort in Ascending (bottom to top) or Descending (top to

bottom) order.

Lastly, a search field lets you type a term you want to use to

find one or more clips that match that criteria. When you type

anything, the contents of the Media Pool shrink to show only

clips that match your criteria.

The Sort Media

By dropdown menu