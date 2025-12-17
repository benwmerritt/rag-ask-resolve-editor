---
title: "Clip Edit Points Are Saved"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 138
---

# Clip Edit Points Are Saved

Once set, In and Out points remain in place within each source clip or timeline until you set new ones.

If you quit DaVinci Resolve and later reopen the same project, each clip’s In and Out points are saved

for future reference.


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

Turning In and Out Points into Markers

With Duration and Back Again

If you want to log the most important sections of clips using In and Out points, you can only log a

single section at a time, as In and Out points are used to identify the next section of a clip to be edited

in a three point edit. However, two commands in the contextual menu of the Source Viewer jog bar

work together to let you turn In and Out points into Markers with Duration, and vice versa:

�Convert In and Out to Duration Marker: Turns a pair of In and Out points into a duration marker.

By default, no key shortcut is mapped to this command, but you can map one if you like.

�Convert Duration Marker to In and Out: Turns a duration marker into a pair of In and Out points,

while retaining the marker. By default, no key shortcut is mapped to this command, but you can

map one if you like.

Using these two commands, you can easily use markers with duration to mark regions of clips that you

want to log for future use, turning each region into an In and Out point when necessary for editing.

By default, these commands don’t have keyboard shortcuts assigned to them, but you can assign

them if you use them frequently.

To turn In and Out points into a duration marker:


Set In and Out points in the Source

Viewer jog bar to identify a region you want to log for future reference.

Marking In and Out points in

preparation to log that section of the clip


Do one of the following:

�Right-click the jog bar and choose Convert In and Out to Duration Marker.

�Choose Mark > Convert In and Out Into Duration Marker.

A duration marker appears above the In and Out points.

To edit its name or notes, double-click the marker, press Shift-M,

or choose Mark > Modify Marker.

A duration marker is created from the In and Out points

In this way, you can log several regions within a single clip for future use.

A clip with multiple logged sections identified via markers with duration


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

To turn a duration marker into an In and Out point:


Find a duration marker you want to convert into In and Out points..

Finding a duration marker to

convert into In and Out points


Do one of the following,

�Right-click the jog bar and choose Set In and Out from Duration Marker.

�Position the playhead over the duration marker and choose Mark > Set In and Out

from Duration Marker.

In and Out points appear under the duration marker.

In and Out points are created

from the duration marker

In this way, you can turn a duration marker that you’ve logged into In and Out points in

preparation for executing a three-point edit.

These are extremely useful logging techniques for three reasons. First, markers with duration

can be searched for in the Media Pool using the All Fields, Marker Name, and Marker Notes

Filter by options. Second, they can be filtered with Smart Bins using the Marker Name and

Marker Notes Media Pool Properties options. Lastly, once one or more duration markers have

been added to a clip, they can quickly be used to perform three-point edits into the Timeline.

Organizing Media by Creating Subclips

Subclips give you another way of organizing media in the Media Pool, letting you break excessively

long clips into shorter ones. For example, if the director of a project is fond of “rolling takes” where

multiple takes are all recorded within a single clip, you can break these takes up by making them

into subclips.

To create a subclip in the Edit page:


Do one of the following to open a clip into the Source Viewer in either the Media page or the

Edit page, in preparation for creating subclips.

�Double-click any clip in the Media Pool.

�Single-click any clip in the Media Library of the Media page to create a subclip without needing

to first import that clip into the Media Pool.


Set In and Out points in the Source Viewer to define the section you want to turn into a subclip.


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT


Do one of the following:

�Choose Mark > Create Subclip.

�Press Option-B.

�Right-click the jog bar and choose Create Subclip from the contextual menu.

�Drag a clip from the Source Viewer to the Media Pool.


A new subclip dialog appears, allowing you to name the subclip and decide to use its full extents

by turning on the checkbox.

The New SubClip dialog

Once created, subclips appear and work like any other clip in DaVinci Resolve. You can also

create subclips in the Media page while performing other organizational tasks there.

Removing or Changing Subclip Limits

Once created, you can right-click any subclip in the Media Pool or a timeline and choose Edit Subclip

to open a dialog in which you can turn on a checkbox to use the subclip’s full extents, or to change the

start or end timecode of the subclip via timecode fields, before clicking Update to modify the subclip.

The Edit Subclip dialog


Edit | Chapter 35 Preparing Clips for Editing and Viewer Playback

EDIT

Chapter 36

Editing Basics

In this chapter, you’ll learn many of the fundamental methods and commands you’ll

use when beginning to assemble clips into the Timeline.

This includes drag and drop operations to begin assembling a timeline, different ways of selecting and

deselecting the clips you’ve edited in preparation for different tasks, maintaining sync between the

audio and video components of clips you’re editing, and deleting clips and gaps you don’t want.

Contents

Keyboard Shortcuts in This Chapter������������������������������������������������������������������������������������������������������������������������������������������� 744

Drag and Drop Editing����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 745

Drag and Drop Editing of Individual Clips Into the Timeline������������������������������������������������������������������������������������������� 746

Drag and Drop Editing of Several Clips Into the Timeline At Once������������������������������������������������������������������������������� 747

Drag and Drop Editing of Video-Only or Audio-Only Edits��������������������������������������������������������������������������������������������� 748

Drag and Drop Insert Editing���������������������������������������������������������������������������������������������������������������������������������������������������������� 748

Dragging Clips From the File System Into the Timeline���������������������������������������������������������������������������������������������������� 749

Inserting Multiple Clips into the Timeline From the Media Pool��������������������������������������������������������������������������������� 750

Insert Selected Clips to Timeline Using Timecode�������������������������������������������������������������������������������������������������������������� 750

Insert Selected Clips to Timeline With Handles�������������������������������������������������������������������������������������������������������������������� 750

Audio Track Creation While Editing��������������������������������������������������������������������������������������������������������������������������������������������� 751

Not Creating New Tracks when Adding Clips to a Timeline������������������������������������������������������������������������������������������� 751

Using Keyboard Shortcuts and Three-Point Editing to Assemble a Program������������������������������������������������������� 751

Example: Assembling Clips Into the Timeline From the Source Viewer��������������������������������������������������������������������� 751

Example: Assembling Clips Into the Timeline From the Media Pool��������������������������������������������������������������������������� 753

Making Selections in the Timeline���������������������������������������������������������������������������������������������������������������������������������������������� 754

Manually Selecting Clips in the Timeline���������������������������������������������������������������������������������������������������������������������������������� 754

Selecting Clips Based on Markers, Flags, and Clip Color������������������������������������������������������������������������������������������������� 756

Selecting Edits in the Timeline������������������������������������������������������������������������������������������������������������������������������������������������������� 756

A Practical Example of Keyboard-Driven Selections���������������������������������������������������������������������������������������������������������� 758

Using Auto Select Controls to Define Selections��������������������������������������������������������������������������������������������������������������� 758

Defining Selections With the Help of Auto Select Controls�������������������������������������������������������������������������������������������� 758

Overriding Automatic Selections by Making Manual Selections���������������������������������������������������������������������������������� 759

Using Auto Select Controls to Control Other Operations������������������������������������������������������������������������������������������������ 760


Edit | Chapter 36 Editing Basics

EDIT

Locking Tracks You Don’t Want to Change���������������������������������������������������������������������������������������������������������������������������� 762

Position Lock for Finishing�������������������������������������������������������������������������������������������������������������������������������������������������������������� 763

Position Locking All Tracks�������������������������������������������������������������������������������������������������������������������������������������������������������������� 763

Position Locking Individual Tracks����������������������������������������������������������������������������������������������������������������������������������������������� 763

Disabling and Re-Enabling Clips in the Timeline���������������������������������������������������������������������������������������������������������������� 764

Deleting Clips and Gaps From the Timeline�������������������������������������������������������������������������������������������������������������������������� 765

Finding, Selecting, and Deleting Gaps in the Timeline������������������������������������������������������������������������������������������������������ 766

Deleting Multiple Timeline Gaps at Once���������������������������������������������������������������������������������������������������������������������������������� 767

Audio/Video Linking��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 768

Controlling Linked Selection����������������������������������������������������������������������������������������������������������������������������������������������������������� 768

Linked Move Across Tracks������������������������������������������������������������������������������������������������������������������������������������������������������������� 769

Dealing with Audio Video Sync Offsets������������������������������������������������������������������������������������������������������������������������������������� 770

Manually Unlinking and Relinking Audio and Video������������������������������������������������������������������������������������������������������������ 771

Linking Multiple Clips in the Timeline������������������������������������������������������������������������������������������������������������������������������������������ 771

Commands for Slipping Audio/Video Sync������������������������������������������������������������������������������������������������������������������������������ 772