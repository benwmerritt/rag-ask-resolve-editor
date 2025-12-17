---
title: "Bins, Power Bins, and Smart Bins"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 666
---

# Bins, Power Bins, and Smart Bins

There are actually three kinds of bins in the Media Pool, and each appears in its own section of the

Bin list. The Power Bin and Smart Bin areas of the Bin list can be shown or hidden using commands in

the Media Pool Options menu (…): Show Smart Bins and Show Power Bins. Here are the differences

between the different kinds of bins:

�Bins: Simple, manually populated bins. Drag and drop anything you like into a bin, and that’s

where it lives, until you decide to move it to another bin. Bins may be hierarchically organized, so

you can create nested bins, one inside of the other, if you like. Creating new bins is as easy as

right-clicking within the bin list and choosing Add Bin from the contextual menu.

�Power Bins: Hidden by default. Power bins are shared among all of the projects in your current

project library, making them ideal for shared title generators, graphics movies and stills, sound

effects library files, music files, and other media that you want to be able to quickly and easily

access from any project. You put whatever materials you want into Power Bins; it’s a manual

process. To create a new Power Bin, show the Power Bins area of the Bin list, then right-click

within it and choose Add Bin.

�Smart Bins: These bins build “custom collections” of media that use metadata or analysis to

automatically populate the bins dynamically, meaning that the contents will change depending on

what the Smart Bin is set to focus on. For example, a sound effects Smart Bin will show only sound

effects, and the bin’s contents will grow or shrink depending on the number of effects files that

have been identified in the project, which may change over time. Smart Bins can allow very fast

and efficient organizing of project contents.

There are several automatically created Smart Bin types available (see Preferences > User> Editing

> Automatic Smart Bins).

You can choose to have Resolve’s Audio Classification analysis categorize your files (automatically

creating “Collections” smart bins). Or, you can manually add metadata to your clips using the

Metadata Editor, adding Scene, Shot, and Take information, keywords, comments and description

text, and more to make it faster to find what you’re looking for when you need it.

You can create your own criteria for a Smart Bin. To create a new custom Smart Bin, make sure

the Smart Bin area of the Bin list is showing, then right-click within it and choose Add Smart Bin.

A dialog appears in which you can edit the name of that bin and the rules it uses to filter clips, then

click Create Smart Bin.

NOTE: To view Smart Bins other than Keywords and Collections, you must first enable

any additional Smart Bin choices in Smart Bin Preferences > User > Editing > Automatic

Smart Bins.

Showing Bins in Separate Windows

If you right-click a bin in the Bin list, you can choose “Open As New Window” to open that bin into its

own window. Each window is its own Media Pool, complete with its own Bin list, Power Bins and Smart

Bins lists, and display controls.

This is most useful when you have two displays connected to your workstation, as you can drag these

separate bins to the second display while DaVinci Resolve is in single screen mode. If you hide the

Bin list, not only do you get more room for clips, but you also prevent accidentally switching bins if you

really want to only view a particular bin’s contents in that window. You can have as many additional

Bin windows open as you care to, in addition to the main Media Pool that’s docked in the primary

window interface.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Filtering Bins Using Color Tags

If you’re working on a project that has a lot of bins, you can apply color tags to identify particular bins

with one of eight colors by right-clicking any bin and choosing the color you want from the Color

Tag submenu.

For example, you can identify the bins that have clips you’re using most frequently with a red

tag. A bin’s color tag then appears as a colored background behind that bin’s name.

Once you’ve tagged one or more Media Pool bins, you can use the Color Tag Filter dropdown

menu (the dropdown control to the right of the Bin List button) to filter out all but a single

color of bin.

To go back to seeing all available bins, choose Show All from the Color Tag Filter dropdown.

Using color tags to

identify bins

Using Color Tag filtering

to isolate the red bins

Sorting the Bin List

The Bin list (and Smart Bin list) of the Media Pool can be sorted by Bin Name, Date Created, Date

Modified, in either ascending or descending order. Simply right-click anywhere within the Bin list and

choose the options you want from the Sort by submenu of the contextual menu.

You can also choose User Sort from the same contextual menu, which lets you manually drag all bins

in the Bin list to be in whatever order you like. As you drag bins in this mode, a red line indicates the

new position that bin will occupy when dropped.

If you use User Sort in the Bin list to rearrange your bins manually, you can switch back and forth

between any of the other sorting methods (Name, Date Created, Date Modified) and User Sort.

Your manual User Sort order will be remembered, making it easy to use whatever method of bin

sorting is most useful at the time, without losing your customized bin organization.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Dragging a bin to a new position in

the Bin list in User Sort mode

The Audio Only

Smart Bin

Filtering Clips With Audio in the Fairlight Page

The Media Pool on the Cut, Edit, Color, Fusion and Fairlight pages can show Audio Only clips using

the Collections smart bin labeled “Audio Only” found in the Collections are of Smart Bins. This makes

it easy for you to find audio clips that you’re looking for, which may be hidden along with lots of video

clips in the same bin.

The Media Pool filter options in the option menu

If you’d like to work with some additional options, the Media Pool in the Fairlight page also has the

ability to filter out audio-only clips, or video clips with audio, in the currently selected bin. To use this

feature, click the Option menu of the Media Pool and choose Show All Clips, Show Audio Only Clips,

or Show Clips With Audio, Show Audio Waveforms, and Show Non-Rectified Audio Waveforms.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Effects Library

The Effects Library on the Fairlight page displays both the built-in Fairlight FX audio plugins that

accompany DaVinci Resolve on macOS, Windows, and Linux, as well as whatever Audio FX are

available on your workstation.

�Fairlight FX are built-in audio processing effects that are fully cross-platform on all platforms

DaVinci Resolve supports.

�On macOS and Windows, DaVinci Resolve supports the use of third-party VST audio plugins.

�On macOS, DaVinci Resolve supports Audio Unit (AU) audio plugins.

Once you install third-party effects on your workstation, they appear in this panel of the Effects Library

alongside the Fairlight FX that are always available. Audio plugins let you apply effects to audio

clips or as a real time process on an entire audio track (affecting all clips on that track), to add basic

dynamics or tonal processing compression, limiting or EQ, noise reduction, or creative spatial effects

like delay or reverb.

The Effects Library

Similar to the Media Pool, the Effects Library’s Bin list can be opened or closed using a button

at the top left.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Effects Library Favorites

To save an effect as a Favorite:

•	 Hover over the far right of any effect to see a star

•	 Click on the star to add the effect to the Favorites effects list.

•	 Favorites appear in a separate area on the lower left next to the Effects Library Bin list.

Stars indicate a flagged favorite effect, all favorites are currently filtered

NOTE: Items that are set as Favorites in the Effects Library list will also appear at the top of

the Mixer’s Effects dropdown menu effects list.

ADR

The Fairlight page of DaVinci Resolve has a sophisticated, yet intuitive, interface for doing “ADR”

(Automated Dialog Replacement). Comprehensive cue list management, industry-standard audio

beeps and visual cues, sophisticated take management with star ratings and layered take organization

help you manage your work while getting the best parts of each performance.

When open, the ADR interface consists of three panels to the left of the Timeline: a List panel, a

Record panel, and a Setup panel.

The List Panel

This is where you create a list of cues you need to re-record, either from within the Fairlight page, or

imported from a .csv file that someone provides you. It presents controls for adding, editing, importing,

and exporting cues that you want to record.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

The Setup panel of the ADR interface