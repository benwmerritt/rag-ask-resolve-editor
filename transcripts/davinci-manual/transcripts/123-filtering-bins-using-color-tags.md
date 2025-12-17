---
title: "Filtering Bins Using Color Tags"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 123
---

# Filtering Bins Using Color Tags

If you’re working on a project that has a lot of bins, you can apply color tags to identify particular bins

with one of eight colors. Tagging bins is as easy as right-clicking any bin and choosing the color you

want from the Color Tag submenu.

For example, you can identify the bins that have clips you’re using most frequently with a red tag.

A bin’s color tag then appears as a colored background behind that bin’s name.

Once you’ve tagged one or more Media Pool bins, you can use the Color Tag Filter drop‑down menu

(the drop-down control to the right of the Bin List button) to filter out all but a single color of bin.

To go back to seeing all available bins, choose Show All from the Color Tag Filter drop-down.

Using Color Tags

to identify bins

Using color tag filtering

to isolate the red bins

Sorting the Bin List

The Bin list (and Smart Bin list) of the Media Pool can be sorted by Bin Name, Date Created, or Date

Modified, in either ascending or descending order. Simply right-click anywhere within the Bin list and

choose the options you want from the Sort by submenu of the contextual menu.

You can also choose User Sort from the same contextual menu, which lets you manually drag all

bins in the Bin list to be in whatever order you like. As you drag bins in this mode, a highlighted line

indicates the new position that bin will occupy when dropped.


Edit | Chapter 33 Using the Edit Page

EDIT

If you use User Sort in the Bin list to rearrange your bins manually, you can switch back and forth

between any of the other sorting methods (Name, Date Created, Date Modified) and User Sort and

your manual User Sort order will be remembered, making it easy to use whatever method of bin

sorting is most useful at the time, without losing your customized bin organization.

Dragging a bin to a new

position in the Bin list

in User Sort mode

More About Timelines and Grading

DaVinci Resolve projects contain one or more edited timelines (sometimes called a sequence in other

applications) which are also organized in the Media Pool, and displayed in the Timeline Editor (referred

to as “the Timeline”). Timelines contain clips, the source media of which is kept in the Media Pool, and

which also appear as edit events in the Edit Index that can be shown at the right of the Timeline.

Timelines, Grades, and Versions

Within any given timeline, grades are associated with the timecode of the source clip they’re

applied to. That means that as you alter the timeline, each clip’s grade moves along with it, making

it extremely easy to move back and forth between editing and grading as your needs require. By

default, each timeline in a project has independent sets of grades using local versions; this is true

even if your timelines are duplicates. That means each clip within every timeline has a completely

independent grade.

However, if you switch the clips in one or more timelines to use Remote versions, a clip’s grades

are shared by every instance of that clip in all timelines with clips that also use Remote versions.

If you import a new timeline that rearranges clips into a different order and switch it to using Remote

versions, then grades will automatically follow the clips, so that the clips within each new timeline

inherits the grades applied to those same clips in other timelines.

You can switch a timeline between using Local and Remote grades at any time.

For more information on using Local versus Remote versions, see Chapter 142, “Grade

Management.” You can also copy grades from one timeline to another using the

ColorTrace feature.

For more information about ColorTrace, see Chapter 149, “Copying and Importing Grades

Using ColorTrace.”


Edit | Chapter 33 Using the Edit Page

EDIT

Enabling the Use of a Master Timeline

Previous versions of DaVinci Resolve had a Master Timeline, which consisted of one long timeline

containing every clip in the Media Pool, arranged by default in ascending order by timecode. While

the Master Timeline was useful for a variety of tasks, architectural improvements have rendered it

unnecessary, and by default the Master Timeline does not appear in new projects created by DaVinci

Resolve version 10 or later.

However, if you want a Master Timeline in order to have a single timeline that always contains all clips

currently in the Media Pool, there’s a way you can create one. You need to do it immediately upon

creating a new project, before adding any media to the Media Pool. Once you’ve added one or more

clips to the Media Pool, the option you need to do so will be disabled.

To create a new Master Timeline:


Create a new project, open the General Options panel of the Project Settings, and turn on the

“Automatically match master timeline with media pool” checkbox. If you also want all clips to use

Remote versions as you grade by default as in previous versions of DaVinci Resolve, you can turn

off the “Use local version for new clips in timeline.”

The option to use a Master Timeline is in the Color section

of the General Options panel of the Project Settings


Click Save to close the Project Settings window.


Open the Edit page, and choose File > New Timeline (Command-N).


When the New Timeline Properties window appears, turn the Empty Timeline checkbox off,

and click Create New Timeline.

Now, in addition to the new timeline, a Master Timeline appears in the Timeline list.

TIP: If you want to make sure that you always have a Master Timeline when you create

new projects, you can alter the Project Setting preset for your user account to reflect these

settings, or you can create a new Project Setting preset with these settings that you can

easily switch to.


Edit | Chapter 33 Using the Edit Page

EDIT

The Master Timeline consists of one long sequence of every clip in the Media Pool, arranged in

ascending order by timecode. Each clip in the Master Timeline appears at its full duration, regardless

of the duration of corresponding clips in an EDL-, AAF-, or XML-imported timeline. Whenever you add

more clips to the Media Pool, they’re automatically added to the Master Timeline.

Creating a Master Timeline

The Master Timeline is useful for organizing media for which no editing has yet been done, such as

when grading digital dailies. The Master Timeline is also useful for identifying a range of similar clips,

based on their similar ranges of timecode. For example, you could find all the talking head shots from

a particular section of tape clustered together in the Master Timeline.

Using the Effects Library

All effects that you can add to your edit, including filters, transitions, titles, and generators, are found in

the Effects Library, which is split into two parts. To the left is a bin list that shows a hierarchical list of all

of the different Transitions, Title Effects, Generators, and Filters that are available, sorted by category.

To the right is a browsing area in which you can see the contents of whichever bins are selected.

The Effects Library

Similar to the Media Pool, the Effects Library’s bin list can be opened or closed using a button at the

top left, while a menu just to the right of this button lets you sort the list into different categories.


Edit | Chapter 33 Using the Edit Page

EDIT

The Toolbox

All of the video and audio transitions, titles, and generators that ship along with DaVinci Resolve

appear in the Toolbox category of the Effects Library.

Toolbox: Exposes all Transitions, Titles, Generators, and Effects at once.

Video Transitions: Contains all of the built-in transitions that are available from DaVinci

Resolve. You can drag any video transition to any edit point in the Timeline that has

overlapping clip handles to add it to your edit; you have the option to drag the transition so

that it ends on, is centered on, or starts on the edit point.

For more information, see Chapter 48, “Using Transitions.”

Audio Transitions: Contains audio transitions for creating crossfades.

Titles: Titles can be edited into the Timeline like any other clip. Once edited into the Timeline,

you can edit the title text and position directly in the Timeline Viewer, or you can access its

controls in the Inspector for further customization.

Generators: Generators can also be edited into the Timeline like any other clip. Selecting a

generator and opening the Inspector lets you access its controls for further customization.

You can also choose a standard duration for generators to appear with in the Editing panel of

the User Preferences.

Effects: Contains unique placeholder effects like Adjustment Clip, and Fusion Composition,

that can be customized to apply sophisticated effects to your programs.

OpenFX

DaVinci Resolve supports the use of third-party OpenFX filters, transitions, and generators in the

Edit page. Once you install these effects on your workstation, they appear in this section of the

Effects Library, organized by type and group depending on the metadata within each effect.

OpenFX: Exposes all Resolve FX and third-party OpenFX installed on your

workstation at once.

Filters: Contains the Resolve FX filters that ship with DaVinci Resolve, as well as any third-

party OFX plugins you’ve installed on your workstation. Filters can be dragged onto video

clips to apply an effect to that clip. Once applied, filters can be edited and customized by

opening the OpenFX panel of the Inspector.

Transitions: Contains any third-party OFX transitions you have installed on your workstation.

OFX transitions can be used similarly to any other transition, but they also expose an OpenFX

panel next to the Transition panel in the Inspector, where you can customize settings that are

unique to that transition.

Generators: Contains any third-party OFX generators you have installed on your workstation.

Can be edited into the Timeline just like the native generators that ship with DaVinci Resolve,

but they also expose an OpenFX panel next to the Transition panel in the Inspector, where

you can customize settings that are unique to that transition.


Edit | Chapter 33 Using the Edit Page

EDIT