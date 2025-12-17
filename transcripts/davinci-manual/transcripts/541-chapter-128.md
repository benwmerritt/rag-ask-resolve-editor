---
title: "Chapter 128"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 541
---

# Chapter 128

Color Page Timeline

and Lightbox

The Timeline in the Color page, consisting of the Thumbnail Timeline and the

Mini‑Timeline, is primarily used for navigating the current arrangement of clips, and

for keeping track of clip properties such as whether they’re graded and ungraded,

whether they use tracking, which version they’re using, and so on.

It can also be used for quickly copying grades from one clip to another, for creating groups, and for

comparing clips in the Viewer.

The Lightbox is the twin sibling of the Thumbnail Timeline, and provides an image‑based method of

comparing clips, managing grades, and performing a wide variety of organizational tasks.

This chapter covers the use of the Timeline and Lightbox.

Contents

Navigating Using the Color Page Timeline������������������������������������������������������������������������������������������������������������������������� 3024

Thumbnail Timeline�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3024

Mini-Timeline���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3024

Using Multiple Timeline Playheads������������������������������������������������������������������������������������������������������������������������������������������� 3025

Show Current Clip With Handles������������������������������������������������������������������������������������������������������������������������������������������������ 3026

Thumbnail Info������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3026

Thumbnail Contextual Menu Commands����������������������������������������������������������������������������������������������������������������������������� 3028

Sorting and Filtering Clips in the Thumbnail Timeline�������������������������������������������������������������������������������������������������� 3028

Changing Timelines�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3028

A and C Mode Sorting��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3029

Flags, Clip Colors, and Markers�������������������������������������������������������������������������������������������������������������������������������������������������� 3030

Timeline Filtering�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3031

Using the Lightbox���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3035


Color | Chapter 128 Color Page Timeline and Lightbox

COLOR

Navigating Using the Color Page Timeline

The Color page Timeline consists of two parts that work together, the Thumbnail Timeline and the

Mini Timeline. These work together to let you examine and navigate the Timeline of your program in

different ways.

The Color page Timeline

The scroll bar for the Mini-Timeline is independent of the scroll bar for the Thumbnail Timeline, and

both can be set to show different ranges of clips. Using the scroll control of your pointing device lets

you zoom into or out of the Mini-Timeline. When zoomed all the way out, the Mini-Timeline displays

the entire timeline within the available width of the screen, making it a fast way of navigating the entire

program from the beginning to the end. However, you can zoom into a particular section when you

need more information about how an intricate arrangement of superimposed clips are organized while

you’re grading.

Thumbnail Timeline

Provides a concise visual representation of your project where each clip is a single numbered

thumbnail, regardless of its duration. Clicking a thumbnail moves the playhead to the first frame

of that clip, while using the Up/Down Arrow keys moves the selection to the previous or next clip.

Whichever clip is at the current position of the playhead appears with its thumbnail outlined in orange.

Middle‑clicking and dragging as well as using the scroll wheel of your pointing device lets you scroll

backward and forward through the Thumbnail timeline.

The Color page Thumbnail Timeline

Each thumbnail displays a variety of information above and below it, including a rainbow outline

around the number of graded clips, the clip format, file name, or grading version text below each

thumbnail, tracking or stabilization badges, flag badges, and link badges to indicate clip groups or

automatic remote grade linking, where existent.

Mini-Timeline

Shows a miniature representation of the Timeline in the Edit page, where each clip’s width

is proportional to its duration, and superimposed clips are shown on top of one another.

The Mini‑Timeline can show a maximum of six video tracks; if your edit uses more, a scroll bar lets you

change which tracks are displayed. Clicking a clip in the Mini-Timeline selects that clip and moves the

playhead to its first frame.


Color | Chapter 128 Color Page Timeline and Lightbox

COLOR

The Color page Mini-Timeline

Scrolling, Zooming, and Navigation

A Timeline Ruler contains the top handle of the playhead, displays the record timecode of the current

edit, and acts as a scrubber bar that typically spans a longer section of the Timeline. The scroll wheel

of your mouse lets you zoom in and out of your edit, and if you zoom all the way out you can fit every

clip in the Mini-Timeline into the available width of the ruler, letting you scrub through every clip in the

Timeline quickly. Clicking anywhere within the ruler instantly jumps the playhead to that frame.

Enabling/Disabling Tracks

The far left of the Mini-Timeline shows numbers for each track, and hovering the pointer over the

track number of any track in the Mini-Timeline of the Color page reveals a tooltip showing the name

of that track. Clicking a track number enables/disables that track along with all clips on that track,

similarly to using the Timeline > Enable/Disable Video Tracks submenu commands (Shift-Command-1

through 9). Clips on disabled tracks are not rendered in the Viewer or video output, and are hidden

from the Thumbnail Timeline. If a track has been disabled in the Edit page, it will appear dimmed in the

Mini-Timeline.

Option-clicking a track number in the Mini-Timeline turns that track number red, letting you hide

clips from the Thumbnail Timeline without actually disabling the video in your program. This is useful

in situations where you want to prevent clips in a particular track (such as motion graphics or titles

rendered from another application) from intercepting the playhead when using the next/previous

clip commands.

Setting In/Out Points for Looping

You can use the I and O keyboard shortcuts to set custom In and Out points in the Timeline. Once set,

turning on Loop in the Viewer transport controls enables this range to be looped, whether it’s a partial

range of one clip, or a range spanning multiple clips together.

Using Multiple Timeline Playheads

DaVinci Resolve supports creating up to four separate playheads in the Mini-Timeline, that you can

use to jump back and forth among different parts of your timeline. Only one playhead can be selected

at any given time, and the currently selected playhead corresponds to the current clip, highlighted in

orange. Each playhead in the Mini-Timeline is labeled with a letter, A through D.

Multiple playheads in the Mini-Timeline for multi-region navigation


Color | Chapter 128 Color Page Timeline and Lightbox

COLOR

To add a new playhead to the Mini-Timeline:

�Choose a playhead from the Color > Active Playheads submenu. That playhead will be placed at the

same position as the original playhead, but it is now the one that is selected, so dragging the new

playhead to a new position of the Mini-Timeline will reveal the original playhead you were using.

To select another playhead to view:

�Click on the top handle of any playhead to select it, making that the currently active playhead

controlled by the transport controls. By default, no keyboard shortcuts are mapped to the four

playheads that are available, but you can create a custom keyboard mapping that you can use to

quickly switch among them.

�Using the DaVinci Advanced control panel, you can use the A, B, C, and D buttons on the jog/

shuttle panel to switch to the playhead you want to control.

To eliminate all additional playheads from the Mini-Timeline:

�Choose Color > Active Playheads > Reset Playheads.

Show Current Clip With Handles

If you’re working on a project that’s part of a round-trip workflow, and you know you’ll be rendering

handles for each clip, it can be useful to temporarily expose these handles for the current clip that you’re

grading, so you can easily apply tracking or keyframing effects to the full frame range of each clip.

To show or hide clip handles in the Mini-Timeline of the Color page:

�Choose View > Show Current Clip With Handles.

(Left) The current clip in the Mini-Timeline, (Right) The same clip shown with Show Current Clip With Handles enabled

While this mode is enabled, Unmix is turned on and cannot be disabled, in order to let you view the

overlapping handles of each clip clearly. The duration of handles that are exposed is defined by the

Default Handles Length parameter of the Editing panel in the User Preferences. Clip Handles can be

shown or hidden at any time.

Thumbnail Info

The thumbnails make it easy to find the clips you’re looking for visually, and they always show the media

as it’s currently graded. The most obvious piece of information is the frame that’s used for each clip’s

thumbnail. If you feel that a particular clip’s thumbnail isn’t representative of its content, you can change it.

To change the current thumbnail:

�Move the pointer over a thumbnail, drag to the left or right to scrub through the clip, and stop

when you find a frame you want to use as the new thumbnail.

Dragging a thumbnail to change

the representative image


Color | Chapter 128 Color Page Timeline and Lightbox

COLOR

If media is replaced in the middle of a color correction timeline, or if you copy or ripple a grade to a

range of clips, the thumbnails may not immediately update to accurately represent the current state of

each clip. In this case, you can manually refresh the thumbnails.

To refresh all thumbnails in the Timeline:

�Right-click anywhere in the Thumbnail timeline and choose Update All Thumbnails.

You can also choose to display the codec, clip names, and version used by each clip in the Timeline.

To switch the Thumbnail timeline between showing clip names, codecs, and versions:

�Double-click the thumbnail clip name of any clip to cycle through each clip’s codec,

clip name, and version.

Additional information appears above and below each thumbnail, providing a way of keeping track

of which clips have been graded, which clips are using different versions, which clips have been

cached, and so on.

Each clip thumbnail has a number of

valuable indications permitting quick

comparison to other shots.

The following list explains each piece of information that can appear above, within, or below the

thumbnails in the Timeline.

�Clip number: (top left) Each clip’s number appears above its thumbnail. Clips are numbered in

ascending order according to the position of their first frame, from left to right, regardless of the

video track in which they appear.

�Grade indicator: (top left) If a clip has been graded, a thin rainbow indicator surrounds the

clip number.

�Source Timecode: (top center) The source timecode from the first frame of each clip appears

above each thumbnail.

�Cache indication: (red timecode) Any clip that’s marked for caching, whether automatically via the

Smart cache, or manually, has its timecode turn red to indicate that it will be cached. After it’s been

cached, the timecode turns blue.

�Track number: (top right) The video track in which a clip is edited appears above the thumbnail.

�Clip Color dot: (upper right) If a clip has a clip color assigned to it, a colored dot appears

on top of its thumbnail.

�Flag icon: (upper left) If a clip has been flagged, a flag icon of the appropriate color appears on top

of its thumbnail. If a clip has multiple flags, as many as can be drawn appear along the top.

�Linked media or group icon: (bottom right) If clips are set to use remote versions, and if multiple

clips share the same source media file, then by default their remote version 1 grade will be

automatically linked. If the current clip is linked, a small link icon appears below the thumbnail of

every clip in the Timeline that’s also linked to that clip. When you select another clip that’s not

linked, the linked clip icons disappear.


Color | Chapter 128 Color Page Timeline and Lightbox

COLOR

�Tracker icon: (bottom right) If any node within a particular clip’s grade has been tracked, a small

crosshairs tracker icon appears below the thumbnail.

�3D indicator: (bottom right) All stereo 3D clips in the Timeline appear with this icon below

the thumbnail. The color indicates which eye you’re monitoring; red for the left eye,

blue for the right eye.

�Version name/Source format: (bottom left) What text is displayed below each thumbnail can be

changed by double-clicking the space underneath each thumbnail. There are several options;

keep double-clicking to cycle among them:

Clip format or codec: This is what’s displayed by default.

Clip Name: Depending on what View > Show File Names is set to, the clip name or file

name is displayed. If you’re working with multicam clips, the multicam angle or name is displayed.

Version name or number: Provides information about whether a clip is using a remote version,

or a local version, indicated by an (L). If you’ve given the current version a name, it appears;

otherwise the version will be labeled “Version” with its number.