---
title: "Resizing the Timeline’s Video"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 133
---

# Resizing the Timeline’s Video

and Audio Track Regions

If you need to see more of the video or audio tracks in the available area of the Timeline, you can

drag the horizontal divider that separates the audio and video tracks up or down to create room

where you need it.

Dragging the Timeline center divider to make

more room for audio or video tracks

Tabbed and Stacked Timelines

The Timeline now supports the option to have tabs that let you browse multiple timelines quickly.

With tabbed timeline browsing enabled, a second option lets you open up stacked timelines to

simultaneously display two (or more) timelines one on top of another.

Tabbed Timelines

The Timeline View Options menu in the toolbar has a button that lets you enable tabbed browsing and

the stacking of timelines.

A button in the Timeline View Options

enables tabbed timelines.

When you first turn this on, a Timeline tab bar appears above the Timeline, displaying a tab for the

currently open timeline that contains a Close button and a Timeline drop-down menu. Once you

enable Tab mode, opening another timeline from the Media Pool opens it into a new tab.

To the right of the currently existing tabs, an Add Tab button lets you create additional tabs that default

to “Select Timeline.” Click any tab’s drop-down menu to choose which timeline to display in that tab.


Edit | Chapter 34 Creating and Working with Timelines

EDIT

Tabs above the Timeline Editor let you switch among multiple timelines quickly

Right-clicking a tab opens a contextual menu that gives access to several commonly used

Timeline functions.

Tabbed timeline contextual menu options:

Close Timeline: Closes the current tab’s timeline, and removes the tab. The same as clicking

on the “x” inside the tab.

Close All Other Timelines: Closes all open timelines and tabs except for the one that you

right clicked and chose this option on.

Rename Timeline: Opens the tab’s text editing field, allowing you to change the name of the

timeline inside the tab. This will change the timeline’s name across the project in the Media

Pool as well.

Find Timeline in Media Pool: Opens the bin where the timeline is stored in the Media Pool,

and highlights the timeline in orange.

Duplicate TImeline: Creates a duplicate of the selected timeline in the same bin, with

the word “copy” appended to the timeline name. It also automatically opens the copied

timeline in a new tab.

Right-clicking on a tab will

show the timeline options.

Methods of working with tabbed timelines:

�Click any tab to switch to that timeline.

�Use the drop-down menu within any tab to switch that tab to display another timeline from the

Media Pool. Each tab’s drop-down menu shows all timelines within that project, in alphabetical

order, but a timeline can only be open in one tab or stack at a time.

�Drag any tab left or right to rearrange the order of timeline tabs.

�Click any tab’s Close button to close that timeline and remove that tab.

�Middle-click any tab to close that timeline and remove that tab.


Edit | Chapter 34 Creating and Working with Timelines

EDIT

Stacked Timelines

While tabbed browsing is turned on, an Add Timeline button appears on the far right of the tab bar that

enables you to stack two (or more) timelines one on top of another. This lets you have two (or more)

timelines open at the same time, making it easy to edit clips from one timeline to another.

A good example of when this is useful is when you’ve created a timeline that contains a

stringout of selects from a particular interview. You can stack two Timeline Editors, one on top

of another, and then open the Selects Timeline at the top and the Timeline you’re editing into

at the bottom. With this arrangement, it’s easy to play through the top timeline to find clips you

want to use, to drag and drop into the bottom timeline to edit into your program.

The button for closing a stacked timeline

To enable or disable stacked timelines:

Click the Add Timeline button at the right of the Timeline tab bar.

The button for adding a stacked timeline

Once you’ve enabled stacked timelines, each timeline has its own tab bar and an orange underline

shows which timeline is currently selected.

At the right of each Timeline tab bar, a Close Timeline button appears next to the Add Timeline button,

which lets you close any timeline and remove that timeline browsing area from the stack.

Two timelines stacked on top of one another


Edit | Chapter 34 Creating and Working with Timelines

EDIT

View and Edit Dual Timelines

Using the Source Viewer

You can now work on two timelines simultaneously in the Edit page, one loaded in the Source Viewer

and one in the Timeline Viewer. This allows you to easily compare two timelines or copy content

between one timeline to another.

Enable Display Stacked Timelines in the

Timeline View options to use dual timelines

To get the best use from this feature, you should first enable Display Stacked Timelines in the Timeline

View Options icon in the upper left of the timeline. Enabling this view will allow each timeline to appear

in its own tab, and the Viewer will automatically switch focus, depending on which tab is selected.

Then, in order to load a timeline into the Source Viewer, right-click on a timeline in the Media Pool

and choose “Open in Timeline with Source Viewer.” The timeline will appear in the Source Viewer,

as a new tab with the name and playhead turning blue to help you keep track of what timeline is in

what Viewer. The timeline in the Source Viewer is read only. You can switch between the timelines by

clicking on the tabs, pressing Q, or by clicking in the appropriate Viewer.

You can change the timeline that appears in the Source Viewer either by right-clicking another timeline

in the Media Pool and selecting the “Open in Timeline with Source Viewer” option, or by selecting one

of the timelines in the dropdown menu at the top of the Source Viewer.

You can perform standard cut and copy operations from the read-only source timeline to the actual

timeline, as well as drag from the Source Timeline viewer (left) into the Timeline viewer (right) to

make an edit.

A dual timeline editing setup, with the Silent Natural timeline in the Source Viewer (blue), and the FX

timeline in the Timeline Viewer. Switching tabs automatically focuses the appropriate Viewer.


Edit | Chapter 34 Creating and Working with Timelines

EDIT

There are also keyboard shortcuts that make focusing between viewers that much quicker:

�To toggle between the Source and Timeline Viewers, press Q.

�To turn on and off the Source Timeline view, press Option-Q.

TIP: You can also right-click on a normal media clip and select Open in Timeline with Source

Viewer to load that clip into the Viewer as a timeline. These “timelines” will be read only, but

will otherwise allow the same timeline to timeline editing operations currently possible. This

mode is useful for very long clips like interviews.

Duplicate Frame Detection

You can turn on Duplicate Frame Detection (often referred to as Dupe Detection) for clips in the

Timeline by choosing View > Show Duplicate Frames. Doing so shows colored bars at the top of clips

in the Timeline whenever a range of frames has been used more than once.

Duplicate Frame Detection shows colored bars where

a range of frames is used more than once in a timeline.

Comparing Timelines

For instances where you’re importing multiple versions of a timeline that’s been edited in another

application, or where you’re working with multiple editors on different versions of the same Timeline

in either collaborative mode or on multiple separate DaVinci Resolve installations, DaVinci Resolve

provides a method of comparing two timelines with one another. Using the Timeline Comparison

window, you can both see a visual comparison of which sections of two timelines differ, and you can

derive a more traditional change list by opening up the Difference Index.

To compare two timelines:


Open the first timeline you want to compare.


Right-click a second timeline in the Media Pool, and choose Compare With Current Timeline.

A Timeline Comparison window appears, showing you the currently opened Timeline at the bottom

and the Timeline you right-clicked at the top.


Edit | Chapter 34 Creating and Working with Timelines

EDIT