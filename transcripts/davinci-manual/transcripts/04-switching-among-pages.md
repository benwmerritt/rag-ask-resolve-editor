---
title: "Switching Among Pages"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 4
---

# Switching Among Pages

Buttons for switching pages appear at the bottom of the UI.

DaVinci Resolve is divided into seven main pages of functionality, each of which facilitates a different

specialization of a typical post production workflow, and each of which can be accessed using buttons

at the very bottom of the DaVinci Resolve interface. These buttons are organized in order of workflow,

and they’re always available, letting you quickly switch between importing media, fast editing, detailed

editing, compositing, grading, audio mixing, and outputting your project in a structured manner.

Minimizing the Resolve Page Bar

If you right-click anywhere within the Resolve Page bar at the bottom of the DaVinci Resolve UI,

two options appear in a contextual menu: “Show Icons and Labels” and “ Show Icons Only.” If you

show icons only, the Resolve Page bar at the bottom takes less room.

The Page bar showing icons only, to save space

Switching Pages Using Keyboard Shortcuts

You can also switch pages using the following keyboard shortcuts, which can be referenced from the

Workspace > Switch to Page submenu.

Hide Pages You Don’t Use

You can leave the page navigation bar showing and just hide the buttons of specific pages.

For example:

�If you like the quick navigation of this bar but there are pages you simply don’t want to use

�If you’re setting up a DaVinci Resolve workstation for an artist making specific contributions to a

project, and you want to hide easy access to pages of functionality they won’t (or shouldn’t) be

using; this can be especially useful in collaborative workflow projects

You can disable/re-enable each page’s buttons using the Workspace > Show Page submenu.

Effects and adjustments that have been applied on hidden pages continue to affect the current

project, they’re only hidden, and you can still navigate to them using the Workspace > Switch to Page

submenu commands or keyboard shortcuts.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Hide Page Navigation Altogether

If you’re an artist that only uses a single page of the DaVinci Resolve experience, or if you want more

screen real estate to work with given your existing computer display’s limited resolution, you can

choose Workspace > Show Page Navigation to hide the page navigation bar at the bottom of the

DaVinci Resolve user interface. While this bar is closed, you can still navigate to other pages using the

Workspace > Switch to Page submenu commands or keyboard shortcuts.

To toggle the Show Page Navigation function:

Check Workspace > Show Page Navigation.

With this interface element hidden, you can use keyboard shortcuts to access the individual

pages (Shift - 2 through 8), Project manager (Shift - 1), and Project settings (Shift - 9). You can

also access these functions from DaVinci Resolve’s main menu bar.

The Media Page

The Media page is the primary interface for clip import, media management, and clip organization in

DaVinci Resolve. It’s central to the way DaVinci Resolve works that the source media used by a project

is organized separately from the project data that you import and manage in the Edit page. In this way,

you can manage and update the clips used by timelines in the current project with ease, switching

between offline and online media, reorganizing clips, and troubleshooting any problems that occur.

Media page

The Media page also contains much of the core functionality that will be used for on-set workflows,

and in the ingest, organizational, and sound-syncing steps of digital dailies workflows. This chapter

covers most of the functionality found in the Media page, including functions in detail that are

referenced throughout this manual.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

The Media page is divided into six different areas, designed to make it easy to find, select, and work

with media in your project. Much of the functionality and most of the commands are found within the

contextual menus that appear when you right-click clips in the Library, File Browser, or Media Pool.

For more information on using the Media page, see Chapter 17, “Using the Media Page.”

The Media Storage Browser

The Media Storage browser shows a list of all volumes that are currently available to your Resolve

workstation. It’s used to locate media that you want to import manually into your project.

Media Storage with scrubbable Clip view

Viewer

Clips that you select in any area of the Media page show their contents in the Viewer. A jog bar

appears at the bottom, letting you drag the playhead directly with the pointer, while a jog control

between the mode drop-down and transport controls lets you move through a long clip more

slowly. The full width of the jog bar represents the full duration of the clip in the Viewer. The current

position of the playhead is shown in the timecode field at the upper right-hand corner of the Viewer.

Simple transport controls appear underneath the jog bar, letting you Jump to First Frame, Play/Stop,

and Jump to Last Frame. Audio levels can be adjusted by right-clicking on the speaker icon and

dragging the slider.

You can also put the Viewer into Cinema Viewer mode by choosing Workspace > Viewer Mode >

Cinema Viewer (Command-F), so that it fills the entire screen. This command toggles Cinema Viewer

mode on and off.

If you have two monitors connected to your computer, you can make the Viewer fill one entire screen

and keep the Resolve UI in the other monitor by choosing Workspace > Full Screen Viewer On, and

selecting the display you wish to use for the Viewer.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Media page Viewer

Media Pool

The Media Pool contains all of the video, audio, and still image media that you import into the current

project. It also contains any media that’s automatically imported along with timelines that have been

imported into DaVinci Resolve. Ordinarily, all media imported into a project goes into the Master bin,

however the Media Pool can be organized into as many user-definable bins as you like, depending

on your needs. Media can be freely moved from one bin to another from within the Media Pool. The

Media Pool also appears on the Edit, Fusion, Color, and Fairlight pages, making it possible to browse

and open clips and timelines everywhere they’re relevant.

Media Pool showing the selected bins’ clips


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Metadata Editor

When you select a clip in any area of the Media page, its metadata is displayed within the Metadata

Editor. If you select multiple clips, only the last clip’s information appears. The Metadata Editor’s header

contains uneditable information about the selected clip, including the file name, directory, duration,

frame rate, resolution, and codec.

A series of editable fields within the Metadata Editor lets you review and edit the different metadata

items that are available. A drop-down menu at the upper right of the Metadata Editor lets you choose

from many different sets of metadata fields and checkboxes, each grouped for a specific task

or workflow.

Clip Metadata Editor

Audio Meters exposed

Audio Panel

The Audio panel can be put into one of two modes via a pair of buttons above the audio meters.

In the default Meters mode, Audio Meters are displayed that show the levels of audio in clips you’re

playing. In Waveform mode, you can load audio clips side by side with video clips opened in the

Viewer in order to sync them together manually. The Audio panel can also be hidden.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO