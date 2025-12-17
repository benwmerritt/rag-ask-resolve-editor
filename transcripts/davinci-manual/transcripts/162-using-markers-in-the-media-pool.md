---
title: "Using Markers in the Media Pool"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 162
---

# Using Markers in the Media Pool

Once you’ve added one or more markers to source clips in the Media Pool, you can use them for

editing in a considerably more direct way than just using them to move the playhead around. Markers

can be exposed in the List view of the Media Pool, and once exposed, they can be opened into the

Source Viewer, edited into the Media Pool, or turned into subclips just like any other clip.

To show markers in the Media Pool:

�Set the Media Pool to List view, then click the disclosure button to the left of the clip with

markers you want to work with. They appear as a hierarchical list underneath the clip to which

they’re attached.

�Use the Right Arrow key to open a clip’s marker hierarchy. Use the Up and Down arrows to select

a particular marker. Use the Left Arrow key to close the clip’s marker hierarchy.

Markers exposed in the Media Pool in List view

To open a marker in the Media Pool into the Source Viewer:

�Double-click any marker to open that clip into the Source Viewer with the playhead at the position

of that marker.

To edit a clip defined by the marker into the Timeline:

�Drag any marker into the Timeline. A clip will be edited into the Timeline with the In point

defined as the frame at the marker, and the Out point defined by either (a) the frame before

the next marker in that clip, or (b) the duration of that marker if the duration is greater than the

default 1 frame.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

To turn a marker in the Media Pool into a subclip:

�Select one or more markers, and drag the selection into another region of the Media Pool, or into

another Bin, and a sub clip will be generated with the clip start defined as the frame at the marker,

and the clip end defined by either (a) the frame before the next marker in that clip, or (b) the

duration of that marker if the duration is greater than the default 1 frame.

To add metadata to a marker subclip in the Media Pool:

�Select a marker subclip in the Media Pool and then edit the name, notes, keywords and color

fields in the Media Metadata panel.

Hiding Markers By Color

View > Show Markers enables users to either show and hide markers based on color, or show them

all at once. An example of when this is useful is when you’re using the color of markers to send

information to specific artists, such as green for Fairlight mixing notes, or orange for Fusion page

compositing notes. Users on those pages can then hide all other markers except for the color they’re

interested in, enabling them to visually prioritize only the markers they care about.

Deleting Markers By Color

Mark > Delete All Markers lets users remove all markers of a specific color all at once, or remove all

markers altogether.

Renaming Clips in the Timeline

For organizational purposes, you can create custom clip names that are tied to a specific timeline.

This can be useful to display information about a clip that is persistent, readily apparent, and does not

require you to click on a flag or marker to view. Clips renamed in this manner are only changed in the

current timeline, and do not modify the Clip Name in the Media Pool.

You can rename clips on the Timeline by using the File Inspector and entering a new name in the Name field.

Renaming a clip in the File Inspector’s Name field

The new name will show in the Timeline track at bottom of the clip.

IMPORTANT: Changing a clip name in the Timeline only affects the instance of the clip in

that specific Timeline. It does not rename the original Clip Name in the Media Pool, nor does

it rename that same clip that may exist in other timelines. If you want to rename a clip across

your entire DaVinci Resolve project, modify the Clip Name in the Media Pool instead.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

The new clip name shown in the Timeline.

TIP: If you want to use a custom clip name on more than one timeline, you can copy and

paste the clip between timelines, and the pasted clip will retain its custom name. However

both clip names will be independent from each other from that point forward.

Color Labeling Clips in the Timeline

By default, different clips have specific colors that identify each type of clip. Furthermore, clips with

effects applied to them (adjustments in the Inspector, volume level changes, speed changes, and so

on), appear as a darker shade of their default color to help you identify at a glance which clips have

been modified.

The following table lists what these default colors are.

Clip Type

Color

Video Clip

Steel Blue

Audio Clip

Light Green

Generator

Light Purple

Text

Beige

Clip with effects

Shaded darker

Custom Clip Colors

Additionally, you can assign one of 16 colors to clips. Each clip can only have a single color assigned

to it. Also, unlike flags, clip colors are clip-specific, so assigning a clip color to one use of a clip in the

Timeline has no effect on any other clips that share the same source media in the Media Pool.

Clip Color Appearance

How these colors appear depends on the location of the clip. There are two options:

�Clip thumbnails in the Media Pool or the Thumbnail timeline of the Color page show a small

colored dot at the upper-right-hand corner of the thumbnail.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

Thumbnails with label colors showing as dots in the corner

�Clips in the Timeline are tinted everywhere but the thumbnail area of video clips. If you edit a clip

into a track that has itself been colored, the clip color overrides the track color.

A timeline with audio clips that have been tinted to identify what they are to the editor

NOTE: Clip colors are distinct from flags, which appear as badges in the Timeline, Media

Pool, and Color page.

Assigning Clip Colors

Clip colors can be assigned in many different areas of DaVinci Resolve.

To assign a clip color to one or more clips, do one of the following:

�Use the Media page to assign clip colors to clips in the Media Pool using the Shot & Scene preset

in the Metadata Editor. Clip colors do not appear in the Media Pool. Clip colors can be removed by

clicking the X to the left of the Clip Color buttons in the Metadata Editor.

�Right-click one or more selected clips in the Timeline, and choose a color from the Clip Color

submenu of the contextual menu. Clip colors can be removed by choosing Default Color from this

same submenu.

�Colorists can right-click one or more selected clip thumbnails in the Color page and choose

a color from the Clip Color submenu of the contextual menu. Clip colors can be removed by

choosing Default Color from this same submenu.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

Track Colors

Another method of visually organizing clips is the use of track colors. Each track can be color coded

with one of 16 different colors. These color codes also appear in the Fairlight page, where they also

correspond to the Edit page Mixer, and to the Fairlight page Mixer and Audio Meters.

To choose a new color for any track:

Right-click the track header and choose a color from the Change Track Color submenu.

When you assign a color to a track, that track’s color appears in a thin strip to the left of that

track’s header controls.

All clips that you place onto that track will appear with that color, unless they’ve been assigned

an individual clip color, in which case the individual clip color overrides the track color. This

makes track colors a great method of visual organization, because you don’t have to do any

advance preparation; the very act of placing a clip on a specific track color codes it according

to that track’s designated purpose.

Color-coded

timeline tracks

A timeline with color-coded tracks automatically tints the clips on each

track; individual colored clips on V1 can be seen at left

Finding Clips, Media, Markers,

Gaps, and Timelines

DaVinci Resolve has several methods of locating clips, markers, and gaps, to help you troubleshoot

problem timelines, or to find media that you want to edit into a timeline differently.

Finding Clips in the Timeline

DaVinci Resolve makes it easy to find one or more clips in the Timeline that correspond to specific

criteria using the Edit Index.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

To find a clip in the Timeline:


Open the Edit Index.


Click the magnifying glass button to open the search controls.


Choose a criteria from the Filter By drop-down menu.


Type a search term in the Search field at the top right of the Edit Index.

As soon as you start typing, all edit events that don’t match the search criteria are temporarily

hidden. To show all of the clips in the Edit Index again, click the X at the right of the search field.


Click any event in the Edit Index to move the playhead to that clip in the Timeline.