---
title: "Assign and Apply Favorite"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 66
---

# Assign and Apply Favorite

Keywords to Clips and Markers

You can now set up to nine keywords as favorites in the Keyword Manager in the Workspace menu.

Simply type your new keyword in the slots on the left of the Keyword Manager to set them.

The nine Favorite Keywords slots in the Keyword Manager

You can quickly assign these keywords to selected clips or in a marker window from the Mark >

Favorite Keywords menu. Or even faster, use the default keyboard shortcuts Option-Shift 0 through 9.

The same menu also has an action to clear all keywords from a clip or marker.


Setup and Workflows | Chapter 16 Using Variables and Keywords

MEDIA

MEDIA

Ingest and

Organize Media

CONTENTS


Using the Media Page���������������������������������������������������������������������������������������������������������������������������� 350


Adding and Organizing Media with the Media Pool������������������������������������������������������������������� 368


Using Clip Metadata�������������������������������������������������������������������������������������������������������������������������������� 408


Using the Inspector in the Media Page�������������������������������������������������������������������������������������������� 423


Syncing Audio and Video����������������������������������������������������������������������������������������������������������������������� 437


Modifying Clips and Clip Attributes��������������������������������������������������������������������������������������������������� 444


Using Scene Detection��������������������������������������������������������������������������������������������������������������������������� 457


Ingesting From Tape������������������������������������������������������������������������������������������������������������������������������� 465


Capturing From the Cintel Film Scanner������������������������������������������������������������������������������������������ 473

Chapter 17

Using the

Media Page

The Media page is the primary interface for media import and clip organization in

DaVinci Resolve. It’s also where all timelines that you edit in DaVinci Resolve or

import from other applications are organized.

While timelines and clips are both saved in the Media Pool, it’s central to the way DaVinci Resolve

works that the source media used by a project is managed separately from your timelines. In this way,

you can manage and update the clips used by timelines with ease, importing and reorganizing clips,

switching between offline and online media, and troubleshooting any problems that occur.

The Media page also contains much of the core functionality used for on-set workflows, as well

as most of the functions that are used in the ingest, organization, and sound-syncing procedures

corresponding to digital dailies workflows.

Contents

Understanding the Media Page

User Interface������������������������������������������������������������������� 351

The Interface Toolbar���������������������������������������������������� 351

Showing Which Panel Has Focus������������������������� 352

The Media Storage Browser������������������������������������ 352

Playing Media in the Media Storage Browser� 353

The Media Storage Browser’s Volume List������ 353

The Media Storage Browser Area������������������������ 354

Revealing a Finder Location

in the Media Browser�������������������������������������������������� 356

Viewer�������������������������������������������������������������������������������� 356

Export The Current Frame from The Viewer��� 358

Live Media Preview������������������������������������������������������ 358

Media Pool����������������������������������������������������������������������� 358

The Bin List����������������������������������������������������������������������� 359

Showing Bins in Separate Windows�������������������� 359

Bins, Power Bins, and Smart Bins������������������������� 360

Filtering Bins Using Color Tags������������������������������ 360

Sorting the Bin List��������������������������������������������������������� 361

Deleted Timeline Backups�������������������������������������� 362

Metadata Editor������������������������������������������������������������� 362

Audio Panel��������������������������������������������������������������������� 363

Dual-Monitor Layout��������������������������������������������������� 364

Customizing the Media Page��������������������������������� 365

Undo and Redo in DaVinci Resolve�������������������� 366


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA

Understanding the Media Page

User Interface

By default, the Media page is divided into five different areas, designed to make it easy to find, select,

and work with media in your project.

The Media page

Much of the functionality and most of the commands are found within the contextual menus that

appear when you right-click clips in the Media Storage browser or Media Pool.

The Interface Toolbar

At the very top of the Media page is a toolbar with buttons that let you show and hide different parts of

the user interface. These buttons are as follows, from left to right:

The Interface toolbar

�Media Storage full/half height button: Lets you set the Media Storage browser to take up the full

height of your display, if you need more area for browsing at the expense of a smaller Media Pool.

�Media Storage: Lets you hide or show the Media Storage browser. Hiding the

Media Storage browser creates more room for the Viewer.

�Clone Tool: Shows or hides the Clone tool, used for cloning media from camera cards

or hard drives.

�Audio Panel: Hides or shows the Audio Panel.

�Metadata: Hides or shows the Metadata Editor.

�Inspector: Hides or shows the Inspector Panels.

�Capture: Switches the Viewer and Audio Panel to Capture Mode, exposing the controls necessary

for cuing up a device-controllable deck, and batch recording from tape.

�Audio Panel/Metadata Editor full/half height button: Lets you set the Audio Panel or Metadata

Editor to take up the full height of your display, if you need more area for either of those functions.


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA

Showing Which Panel Has Focus

Whenever you click somewhere on the DaVinci Resolve interface using the pointer, or use a keyboard

shortcut to “select” a particular panel (such as in the Edit page), you give that panel of the user

interface “focus.” A panel with focus will capture specific keyboard shortcuts to do something within

that panel, as opposed to doing something elsewhere in the interface.

Disabled by default, checking the “Show focus indicators in the user interface” box in the UI Settings

section of the User Preferences causes an orange highlight to appear at the top edge of the focused

panel, allowing you to keep track of which part of the current page is taking precedence. You can

switch focus as necessary to do what you need to do.

The Focus indicator shown at the top edge of the Media Pool, shown next to a Viewer that doesn’t have focus

The Media Storage Browser

The Media Storage browser lets you see all of the volumes connected to your workstation, browsing

them for media that you want to preview and eventually import into your DaVinci Resolve project in

one way or another. Whereas other applications rely on some sort of import dialog, DaVinci Resolve

provides the Media page for doing complex media import tasks. To facilitate media import, the Media

Storage browser is divided into two areas, the Volume List, and the Media Browser.

Media Storage browser with scrubbable clip view


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA