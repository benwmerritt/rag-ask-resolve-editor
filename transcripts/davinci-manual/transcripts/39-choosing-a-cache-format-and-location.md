---
title: "Choosing a Cache Format and Location"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 39
---

# Choosing a Cache Format and Location

The cache format is user selectable by opening the Master Settings panel of the Project Settings,

and using the “Render Cache Format” drop-down menu to choose one of the ProRes, DNxHR, or

uncompressed 10- or 16-bit float uncompressed .dvcc formats. Selecting a higher quality cache format

guarantees high quality image playback, but makes more demands on the throughput and size of

your available disk storage. On the other hand, choosing a more highly compressed cache format

makes real time playback possible on less capable computers with slower and smaller storage, at the

expense of slightly compromised image quality. Ideally, you should choose the highest quality cache

format that your workstation’s storage can accommodate.

The format you choose via the “Render Cache Format” menu will determine whether out-of-bounds

image data (including “super white” or HDR strength highlights) is preserved when the signal is

cached. Formats in this menu that end in “– HDR” preserve out-of-bounds image data, while formats

that don’t, wont. If you find that image data (typically bright highlights) is clipped after caching or

optimizing, you should switch to 16-bit float, ProRes 4444, ProRes 4444 XQ, or DNxHR 444; in

particular, any of these codecs are appropriate for HDR grading.

The Cache files location defaults to the first volume you add to the Scratch Disks list of the Media

Storage panel of the System Preferences. If no scratch disk is specified, your System disk will be

used, which may pose problems with capacity and/or performance depending on the size and type

of System disk you’re using, and on the media format you choose to cache to. For this reason, it’s

nearly always advisable to set your first scratch disk to the largest, fastest storage volume available to

your workstation.

When Caching Happens

When caching is enabled, cache indicators along the bottom of the Timeline Ruler of the

Edit page timeline shows the status of the cache. Red means “to be cached,” while blue means

“has been cached.”

Source, Clip, and Sequence Cache bars seen in the Timeline of the Edit page; red bars show

areas of the Timeline that need caching, blue shows areas that have been cached

In the Color page, cache indicators are node specific, showing the node in your grading node tree

(including all upstream nodes) at which caching will take place.

Node Cache indicator seen as a red colored node number

on node two of the Node Editor of the Color page


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Caching happens in two ways. First, when either Smart or User caching is enabled, caching always

happens whenever you play clips with red caching indicators.

Second, if background caching is enabled in the Project settings (it’s turned on by default), and you

don’t make any changes to your project for a user-definable number of seconds (this is adjustable in

the Master Settings panel of the Project Settings), caching will automatically begin during periods of

user inactivity. So feel free to use this as an excuse to take those coffee, mate, or tea breaks; DaVinci

Resolve will keep on working for you.

The Difference Between the

Smart Cache and User Cache Modes

The Smart Cache option of the Render Cache submenu provides the easiest user experience when

you want to “set it and forget it.” Choosing Smart triggers a variety of automatic caching behaviors

designed to optimize playback in DaVinci Resolve by rendering clip formats, grading operations, and

timeline effects that are known to be performance-intensive, while also letting you manually flag clips

that you’d like to cache that the Smart Cache hasn’t.

The User Cache, on the other hand, does not automatically cache clips in processor-intensive formats,

so this is a good option to choose when your workstation is capable of playing all media formats you’re

using in real time. Ordinarily, the User cache relies on you to control what is cached and what is not by

manually flagging specific clips and effects. However, the Master Settings panel of the Project Settings

has three options you can enable for automatically caching transitions, composites, and Fusion Effects

while in User Cache mode (these options are found in the Optimized Media and Render Cache group).

Of these settings, only “Automatically cache Fusion Effects in User Mode” is turned on by default.

Here are the differences between the Smart and User cache modes for each type of caching

DaVinci Resolve does.

Fusion Output Caching

�In Smart mode: For all clips with “Render Cache Fusion Output” set to either Auto (by default) or

On, three types of effects are rendered. First, H.264, H.265, DCP, JPEG2K, or camera raw clips

that have been edited into a timeline are cached. Camera Raw clips are cached using the currently

selected project or clip debayer settings. Second, Speed effects are cached at the source level,

which makes it possible to move cached speed effects clips on the Timeline without needing to

re‑cache them. Finally, Fusion Clips or clips with Fusion Effects applied to them are also cached,

and manually flagged clips are also cached in Smart mode.

�In User mode: Clips with Render Cache Fusion Output set to On are cached, while clips set to

Auto are ignored, except for clips with Fusion Effects, which are automatically cached in Auto

mode when the “Automatically cache Fusion Effects in User Mode” Project Setting is on.

Caching Specific Nodes in the Color Page

�In Smart mode: DaVinci Resolve automatically caches all nodes that use Motion Blur,

Noise Reduction, or Resolve FX and OFX plugins. Manually flagged nodes are also

cached in Smart mode.

�In User mode: DaVinci Resolve only caches nodes that have been manually flagged by right-

clicking them and choosing Node Cache > On to force that node to cache in User mode, along

with all upstream nodes to the left of them.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Cache Color Output Is Actually Node Caching for the Whole Grade

�In Smart mode: Manually flagged clips with Render Cache Color Output turned on cache the

entire output of the Color page node graph, effectively caching that clip’s entire grade. This is

most useful when you want to improve trimming and playback performance in the Edit page.

Flagging a clip for caching also causes EVERY SINGLE VERSION associated with that clip to be

cached as well.

�In User mode: Manually flagged clips with Render Cache Color Output turned on also cache the

entire output of the Color page node graph.

Caching of Resolve FX and OFX in the Edit Page Is Also Node Caching

Caching of Resolve FX and OFX filters applied to clips in the Edit page can only be set manually,

whether you’re in Smart or User mode. Only filters that you have flagged to cache by right-clicking the

clip they’re applied to and choosing them in the Render Cache OFX Filter submenu are cached.

Sequence Caching

�In Smart mode: DaVinci Resolve automatically caches all superimposed clips that use composite

modes other than “Normal,” any clips with opacity or speed effects, and any transitions.

Clips cannot be manually flagged for Sequence caching.

�In User mode: If you’ve enabled User mode and you find that your workstation does not have

adequate performance to play composite and opacity effects in the Edit page, you can force

these categories of effects to be automatically cached in User mode via a set checkboxes in

the Optimized Media and Render Cache section of the Master Settings of the Project Settings.

When these options are enabled, you also gain the ability to exclude specific tracks from being

cached, by right-clicking the track header of any video track you want to exclude from caching,

and choosing Exclude track from caching. Excluding an entire track from caching is a convenient

way of keeping a track full of effects that are capable of playing in real time on your workstation,

such as a track of titles, from wasting time and storage by being cached when it’s not necessary.

Manually Controlling the Cache

This section describes how to manually control each type of caching that is manually controllable in

DaVinci Resolve.

Controlling Fusion Output Caching

You can manually control which clips in the Timeline are cached, and which are not. You can select

one or more clips in the Timeline of the Edit page, or in the Thumbnail Timeline of the Color page,

right-click one of the selected clips or thumbnails, and choose an option from the Render Cache

Fusion Output submenu. There are three options:

�Auto: The clip will only be cached in Smart mode if it’s a format designated for caching or if

there’s a speed effect applied. The clip will only be cached in User Mode if “Automatically cache

transitions in User Mode” is enabled.

�On: The clip will be cached in either Smart or User mode, no matter what format or effects

are applied.

�Off: The clip will not be cached at all, in either Smart or User modes.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Controlling Node Caching

You can manually control which nodes in a grade are cached, and which are not. Right-click any node

in a node tree, and choose an option from the Node Cache submenu. There are three options:

�Auto: The flagged node and all upstream nodes will only be cached in Smart mode if it

contains an operation that’s designated for caching.

�On: The node will always be cached in either Smart or User mode, no matter

what operations it performs.

�Off: The node will not be cached, in either Smart or User modes. This lets you exclude nodes from

caching in Smart mode if they’re capable of real time operation on your system.

Controlling Color Output Caching

Each clip in the Timeline (including Adjustment clips) has a Color Output setting that you can turn on or

off by right-clicking that clip in the Timeline of the Edit page, and choosing Render Cache Color Output

from the contextual menu. A check mark indicates when this setting is turned on.

Controlling Edit Page Filter Caching

You can choose which of the Resolve FX or OFX filters applied to a particular clip should be cached

by right-clicking that clip in the Timeline of the Edit page, and choosing which of the filters in the

Render Cache OFX Filter submenu you want to cache.

Each filter applied to that clip appears in this submenu in the order in which it’s applied to the clip, and

you can turn the caching of specific filters on and off (selected filters appear with a check mark to the

left of their menu item).

Using Cached Media When Rendering in the Deliver Page

The “Use Render Cached Images” option in the “More options” section of the Video panel of

the Render Settings in the Deliver page lets you write media directly from the cache, rather than

re‑rendering the effects from scratch, in order to save rendering time when you output your project.

If you’re planning on using this option, it’s advisable to set the cache format to a suitably high-quality

format to guarantee the best results.

Clearing Cached Media

Each project’s cache is persistent; the cache is saved for future use even when the project is closed

and later reopened. If you need to delete a project’s cache to free up space on a storage volume,

there are three options in the Delete Render Cache submenu:

�All: You can delete all media in the cache to reset every single cached clip.

�Unused: You can choose to delete only Unused cache clips that no longer correspond to clips or

effects in the Timeline.

�Selected clips: You can make a manual selection of clips in the Timeline, and delete the cache

corresponding to just those clips.

To clear a project’s cache:

Open the project, and choose Playback > Delete Render Cache > All, Unused, or

Selected Clips.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

The Cache Manager

There is an advanced render cache management window to help you easily see the size and manage

your cache data for various projects across all your project libraries. This cache manager can be

accessed from Playback > Manage Render Cache.

The Cache Manager window ties in with the Project Manager, letting you select cached media from

any library accessible from your system, not just the current project library.

The functions of the Cache Manager are:

•	 Location: This drop-down menu lets you choose the type of project library to connect to.

Options are: Local, Network, Cloud, and All.

•	 Project Library: This drop-down menus lets you choose the project library whose projects

you want to manage. This lists all the project libraries in the selected Location, and you

can select one for management. You can also select All to reveal all project libraries in

that location.

•	 Project: The main window shows all the projects in the Project Libraries selected above. It

is categorized into sortable columns by Location, Project Library, Project Name, and Render

Cache. Check the box in the Render Cache column to select any projects you want to

delete the cache of.

•	 Clear Selected Cache: Click this button to delete the Cache for all the selected projects.

As of this writing there is no warning dialog or undo for this function, so double check that

you’ve selected the correct caches for deletion.

•	 Close: Closes the Cache Manager.

The Cache Manager


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA