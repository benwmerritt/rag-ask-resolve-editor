---
title: "Bins Interface"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 231
---

# Bins Interface

The Bins window is actually a separate application used to save content you may want to reuse at a

later time. The Bins window is separated into two panels. The sidebar on the left is a bin list where

items are placed into categories, while the panel on the right displays the selected bin’s content.

The Bin list sidebar

The Bin list organizes content into bins or folders using a hierarchical List view. These folders can be

organized to suit your workflow, but standard folders are provided for Clips, Compositions, Favorites,

Settings, and Tools. Parent folders contain subfolders that hold the content. For instance, the Tools bin

is a parent folder to all the categories of tools. To access subfolders, click the disclosure arrow to the

left of the parent folder’s name.

When you select a bin from the bin list, the contents of the folder are displayed in the Contents panel

as thumbnail icons.

The Bins icon view


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

A toolbar along the bottom of the bin provides access to organization, playback, and editing controls.

The Bins toolbar

�New Folder: Creates a new folder in the current window.

�New Reel: Creates an empty reel that can contain multiple clips edited together into a timeline.

�New Clip: Opens a dialog to link a new media file into a bin.

�Studio Player: Opens a playback viewer for a selected clip.

�Icon/List view: This button toggles between showing contents of a bin in thumbnail view

and list view.

�Checkerboard: Shows a checkerboard pattern in a clip thumbnail to signify transparency.

�Thumbnail size: Provides a few preset sizes for thumbnail icons.

Right-clicking in any area of the bin window displays a pop-up menu to access most of a bin’s features.

Right-clicking on an item in a bin shows the same menu with additional options for renaming, playing,

or deleting the item.

The Bin Studio Player

Selecting a clip in a bin and clicking the Studio Player button or double-clicking the clip opens the

Studio Player. The Studio Player can be used to view clips, view metadata, and add notes.

The Bin Studio Player

For more information on Bins, see Chapter 13, “Bins” in the Fusion Referance Manual.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

The Console

The Console is a window in which you can see the error, log, script, and input messages that may

explain something Fusion is trying to do in greater detail. The Console is also where you can read

FusionScript outputs, or input FusionScripts directly. In DaVinci Resolve, the Console is available by

choosing Workspace > Console or choosing View > Console in Fusion Studio. There is also a Console

button in the Fusion Studio User Interface toolbar.

Occasionally the Status bar displays a badge to let you know there’s a message in the Console you

might be interested in.

The Console window

A toolbar at the top of the Console contains controls governing what the Console shows. At the

top left, the Clear Screen button clears the contents of the Console. The next four buttons toggle

the visibility of error messages, log messages, script messages, and input echoing. Showing only a

particular kind of message can help you find what you’re looking for when you’re under the gun at

3:00 in the morning. The next three buttons let you choose the input script language. Lua 5.1 is the

default and is installed with Fusion. Python 2.x and Python 3.x require that you install the appropriate

Python environment on your computer. Because scripts in the Console are executed immediately, you

can switch between input languages at any time.

At the bottom of the Console is an Entry field. You can type scripting commands here for execution

in the current comp context. Scripts are entered one line at a time, and are executed immediately.

For more information on scripting, see the Fusion Scripting Manual.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Customizing Fusion

This section explains how you can customize Fusion to accommodate whatever workflow

you’re pursuing.

The Fusion Settings Window

Fusion has its own settings window, accessible by choosing Fusion > Fusion Settings in DaVinci

Resolve, or in Fusion Studio by choosing Fusion > Preferences on macOS or File > Preferences on

Windows or Linux. This window has a variety of options for customizing the Fusion experience.

For more information, see Chapter 75, “Preferences,” in the DaVinci Resolve Reference

Manual or Chapter 15 in the Fusion Reference Manual.

The Fusion Settings window set to the General panel


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Saving Fusion Layouts

It is possible to customize the layout and configuration of panels to suit the size of the desktop and

monitor, or to match personal preferences.

In DaVinci Resolve, configure and resize the panels you want displayed and then:

Choose Workspace > Layout Presets > Save Layout Presets.

In Fusion Studio, configure and resize the panels you want displayed and then:

Click the Grab Document Layout button in the Preferences > Layout panel to save the layout

for all new Compositions.

Click the Grab Program Layout button to remember the size and position of any floating views,

and enable the Create Floating Views checkbox to automatically create the floating windows

when Fusion restarts.

Showing and Hiding Panels

The UI toolbar at the top of the screen lets you open panels you need and hide those you don’t. It’s

the simplest way to create a layout for your particular needs at the moment.

The UI toolbar of the Fusion page

Resizing Panels

You can change the overall size of each panel using preset configurations, or you can adjust them

manually. The viewers and Work panel are inverse of each other. The more space used to display the

Work panel, the less space available for the viewers. To resize a panel, manually drag anywhere along

the raised border surrounding the edges of the panel.

Dragging the edge between

two viewers to resize it

Fusion Studio Floating Frame

Fusion Studio includes a Floating Frame window that can be used to house any panel.

To place a panel in the Floating Frame, do the following:


In Fusion Studio, choose Window > New Floating Frame.


Right-click in the Floating Frame and choose the panel from Add View submenu.

When using multiple monitors, you can choose to have floating panels spread across your displays for

greater flexibility.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION