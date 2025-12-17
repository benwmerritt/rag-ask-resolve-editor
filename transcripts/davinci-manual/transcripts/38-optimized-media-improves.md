---
title: "Optimized Media Improves"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 38
---

# Optimized Media Improves

Overall Performance

If you’re editing processor-intensive source formats such as camera raw, H.264, or 8K media, and

your computer isn’t fast enough to work with it easily in real time, you can create pre-rendered, low-

overhead duplicate media to use instead, that’s automatically managed alongside the original media.

This is called “Optimized Media.” Optimized Media lets you work more quickly by allowing you to edit

with a more processor-efficient media format and resolution, while providing the ability to easily switch

your project back to the original source media whenever you want. So, you can use Optimized media

to edit, and switch back to the original source media when it’s time to finish and output. Switching is as

easy as choosing Playback > Use Optimized Media if Available to toggle Optimized media on and off.

The advantage of using optimized media to help you work faster is that it’s pre-generated, meaning

you can render it once and then use the files for the duration of your work in that project (unless you

change the debayering settings of the raw media). Also, optimized media improves the playback

performance of clips throughout DaVinci Resolve, including in the Media page and in the Media Pool

and Source Viewer of the Edit page, whereas the similar but different Fusion Output Cache component

of the Smart Cache only improves the performance of clips that are already in the Timeline by caching

them at the Timeline resolution. This makes optimized media ideal for editing workflows of all kinds.

Choosing the Appropriate Optimized Media Format for Your Project

You have the option of choosing the Format of the optimized media you create, using controls

in the Master Settings panel of the Project Settings. Be aware that the format you choose via

the “Optimized Media Format” menu will determine whether out-of-bounds image data (also

known as “overshoots”) and Alpha Channels are preserved when the clip is cached.

Preventing Clipping: You should use 16-bit float, ProRes 4444, ProRes 4444 XQ, or DNxHR

444 if you plan on grading using optimized media. This is particularly true for HDR grading.

Preserving Alpha Channels: Also be aware that the format you choose will determine

whether Alpha Channels will be preserved if they’re present in the clips being optimized.

Currently, the Uncompressed 10-bit, Uncompressed 16-bit Float, ProRes 4444, ProRes 4444

XQ, and DNxHR 444 formats preserve alpha channels.

Creating Optimized Media

Creating optimized media to work with is easy. Resolve automatically manages the relationship

between source clips and the optimized media you create, so all you need to do is choose which clips

to make optimized media for. You can manually choose which clips to optimize, or you can use a Smart

Bin to collect all of the media corresponding to one or more formats you need to optimize to gather

it procedurally. In either case, this gives you the option of only optimizing clips in formats that require

optimization, saving you time.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

For example, if you’re editing a project that consists half of camera raw media, and half of DNxHD

media, you probably only need to optimize the camera raw media, so you can create a Smart Bin that

gathers all of it, based on Resolution, Codec, File Name, or whatever other metadata is appropriate.

Once gathered, it’s an easy thing to select all of these clips in preparation for the next step.

To create optimized media for one or more selected clips:

Right-click one of the selected clips, and choose Generate Optimized Media from

the contextual menu.

All optimized media is written to the same directory as the Cache files are written, which defaults to

the first scratch disk listed in the Preference dialog’s Media Storage panel. The location of Cache and

Optimized files is also selectable via the “Cache files location” setting in the Master Settings panel of

the Project Settings.

Optimized Media for Raw Source Clips

In general, once you create optimized media, DaVinci Resolve keeps track of it and continues using it

regardless of whatever changes you make to your project, including changing the Timeline resolution.

However, any change to the camera raw settings of optimized clips will automatically discard the

optimized media, requiring you to re-generate optimized media for them.

Customizing the Type of Optimized Media You Create

The Master Settings panel of the Project Settings has a set of controls that govern what kind of media

files are created when you create optimized media.

Options available for creating optimized media in the Master Settings panel of the Project Settings

There are two settings affecting Optimized Media in the Optimized Media and Render Cache section:

�Resolution: Lets you choose whether to create optimized media at the same size as your original

media files (by choosing Original), or to reduce the bandwidth of your optimized media further by

reducing its resolution by a Half, Quarter, Eighth, or Sixteenth. The “Choose automatically” option

tries to balance visual quality with efficiency by only reducing the resolution of media files that are

larger than the currently selected Timeline resolution, using whatever reduction ratio best matches

the Timeline resolution.

�Optimized Media Format: Lets you choose the format and codec with which to generate

optimized media. Options include Uncompressed 10-bit, and Uncompressed 16-bit float for

maximum quality. Other options include ProRes Proxy through 4444 XQ, and DNxHR LB

through 444. All options will store image data in the optimized and proprietary .dvcc image format.

While smaller formats take less room on your scratch disk, there are two good reasons to use

higher-quality formats for creating Optimized Media.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Preventing Clipping: Be aware that the format you choose will determine whether out-of-bounds

image data is preserved when the signal is optimized. If you find that image data (typically super-

white levels) are clipped after optimization, you should switch to 16-bit float, ProRes 4444, or

ProRes 4444 XQ; in particular, any of these three codecs are appropriate optimized formats for

HDR grading.

Preserving Alpha Channels: Also be aware that the format you choose will determine whether

Alpha Channels will be preserved, if they’re present in the clips being Optimized. Currently,

the Uncompressed 10-bit, Uncompressed 16-bit Float, ProRes 4444, ProRes 4444 XQ, and

DNxHR 444 formats preserve alpha channels.

Choosing Resolution Automatically

The “Choose automatically” option of the Resolution setting bears a bit more explanation. When

selected, only source media with a higher resolution than the selected Timeline resolution will

generate downsized optimized media. How much each clip will be downsized depends on how

much larger each clip is than the Timeline resolution. For example, if you’re working within a 1080

resolution project, then 8K clips will generate quarter-resolution optimized media, and 4K clips will

generate half‑resolution optimized media, such that all optimized media is somewhere around 1080

resolution. All clips that are 1080 and smaller generate optimized media at the same resolution as the

source clips.

In the example of a 4K project, 8K clips will generate half-resolution optimized media, and all other

clips that are 4K and smaller will generate optimized media at the same resolution as the source clips.

Proxy Resolution

Width

Height

Full 8K UHD


Full UHD/Half 8K UHD


Full-HD/Half UHD/Quarter 8K UHD


Half-HD/Quarter UHD/Eighth 8K UHD


Quarter-HD/Eighth UHD/Sixteenth 8K UHD


Eighth-HD/Sixteenth UHD


Table of optimized resolutions for different television frame sizes

Switching Between Optimized and Original Media

Choosing whether or not you’re using optimized media is easy. Simply choose Playback > Use

Optimized Media if Available to switch your entire project between using optimized media (if it’s been

generated), or the original media. Furthermore, a checkbox in the Render Settings of the Deliver page

lets you choose whether you want to use optimized media to speed up rendering, or render using the

original media only.

NOTE: Optimized media is not included in Media Management operations, nor is it included

as part of Archive operations in the Project Manager.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Sharing Optimized Media Between Projects

Optimized Media is shared across projects in the same project library (previously optimized media was

confined to a single project). This means that if you create optimized media for a clip in one project,

that same optimized media will be used for that clip in any other project that’s in the same project

library. This happens automatically and requires no user input. This will dramatically cut down the

space requirements for working with the same media across different projects.

Rediscovering Lost Optimized Media

It’s difficult, but it is possible to lose track of optimized media you’ve generated in certain rare

circumstances. For example, if you generate optimized media on another workstation, but failed to

save the project, DaVinci Resolve may lose the relationship between the clips in the Media Pool and

the optimized media files you created. In these cases, it’s possible to rediscover the optimized media

so you don’t have to regenerate it.

To rediscover lost optimized media:

Select the clips in the Media Pool for which you know you have optimized media, then right-click one

of the selected clips and choose Rediscover Optimized Media from the contextual menu.

Deleting Optimized Media

The optimized media you generate within a project is persistent; it’s saved for future use even when

the project is closed and later reopened. If you need to delete optimized media to free up space on

your scratch volume (or wherever you’ve decided to locate your project’s cache files), you must delete

the optimized media manually in your OS. By default, the Optimized Media is stored in the first volume

in the Media Storage tab of the System Preferences.

Using Optimized Media for Delivery

An option in the More options section of the Render Settings in the Deliver page, “Use Optimized

Media,” lets you output using Optimized Media, rather than the original media, in order to save

rendering time. If you’re planning on using this option, it’s advisable to set the Optimized media format

to a suitably high-quality HDR-capable format to guarantee the best results.

Using the Smart or User Cache

Improves Effects Performance

Another option for achieving real time performance when the GPU Status indicator is in the red due

either to Timeline effects, Color page grading, or processor-intensive media in the Timeline, is to use

the Smart Cache or User Cache modes of the Render Cache. What DaVinci Resolve calls “caching” is

sometimes referred to by other applications as “rendering.” Both terms refer to the behind-the-scenes

creation of new media, with all effects “baked in,” which DaVinci Resolve plays back in real time in

place of the original source media containing processor-intensive effects at the same time. This results

in smooth playback without the risk of dropped frames.

The settings governing caching in the Master Settings panel of the Project Settings


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

The DaVinci Resolve Smart Cache and User Cache automatically render and cache clips, including

simple video clips, compound clips, Fusion clips, and nested timelines that have processor-intensive

grades and effects applied to them, or that you manually flag for caching by right-clicking any clip in

the Color page or Edit page timeline and enabling the Render Cache Clip Output option. When the

Smart or User Caches are enabled, frames of each automatically or manually flagged clip are cached

either during playback in the Timeline, or automatically whenever you pause work, to the “Cache files

location” specified in the Master Settings panel of the Project Settings.

Once you’ve cached clips in the Timeline, they play back in real time until they’re modified, which

automatically flushes the now out-of-date cache files for those modified clips and triggers the need

to re-cache.

To use clip caching on any page, do one of the following:

�Choose Playback > Render Cache > Smart to set DaVinci Resolve to automatically cache

computationally intensive effects and timeline clips in formats judged too processor-intensive to

play in real time.

�Choose Playback > Render Cache > User to set DaVinci Resolve to cache clips and effects

that you manually choose to cache, as well as automatically caching processor-intensive

effects (transitions, composites, and Fusion Effects) you specify in the Master Settings of the

Project Settings.

�Choose Playback > Render Cache > Off to disable all render caching.

�In the Color and Edit pages, press Option-R to cycle among Off, Smart, and User.

Choosing the Appropriate Cache Media Format for Your Project

You have the option of choosing the Format of the cached media you create, using controls in

the Master Settings panel of the Project Settings. Be aware that the format you choose via the

“Render Cache Format” menu will determine whether out-of-bounds image data (also known

as “overshoots”) and Alpha Channels are preserved when the clip is cached.

Preventing Clipping: You should use 16-bit float, ProRes 4444, ProRes 4444 XQ, or DNxHR

444 if you plan on grading using cached media. This is particularly true for HDR grading.

Preserving Alpha Channels: Also be aware that the format you choose will determine whether

Alpha channels will be preserved, if they’re present in the clips being cached. Currently, the

Uncompressed 10-bit, Uncompressed 16-bit Float, ProRes 4444, ProRes 4444 XQ, and DNxHR

444 formats preserve Alpha channels.

How Cached Media Is Organized

The cache mechanism in DaVinci Resolve actually comprises three independently managed media

caches that interact with one another. This is done to keep you working quickly by ensuring that

changes you make to your timeline don’t require a grade to be re-cached, and that changes you make

to a grade don’t require the timeline to be re-cached. The three levels of caching are:

First, Fusion Output Caching

Formerly called the “Source Cache” in previous versions of DaVinci Resolve. When enabled by turning

on the Smart Cache, by individually turning on Render Cache Fusion Output for a particular clip, or by

enabling the automatic caching of clips with Fusion Effects applied in the Project Settings, this caches

the portion of each source media file that appears in the Timeline in its pre-graded state for clips that

have the following characteristics:


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

�Clips in media formats DaVinci Resolve considers to be processor-intensive to decode,

such as H.264, HEVC, and various raw camera formats

�Clips with Fusion Effects that have been added in the Fusion page

Effectively, this is a “pre-Color page” cache. By caching all processor-intensive clips in the Timeline,

you’ll experience vastly improved trimming and grading performance. However, you also have the

option to turn the Fusion Output Cache on or off for individual clips, or for multiple selected clips all at

once. This lets you switch between using the native source of each clip with live effects, or the cached

clip in the cache format you’ve chosen.

The advantage of the Fusion Output Cache over Optimized Media is that you only cache clips that

are used in a timeline, which is ideal for finishing workflows. However, the Smart and User caches

aren’t useful for speeding up work done with source media in the Media Pool and Source Viewer

when you’re at the very beginning of an edit; that’s what Optimized Media is for (as described in the

previous section).

If Optimized media exists for a given clip, and “Use Optimized Media if available” is turned on, then

Optimized media will be used instead of the Fusion Output Cache if there are no Speed effects or

Fusion Effects applied to a particular clip.

Second, Node Caching

The Node Cache, which is a separate level of caching from the Fusion Output Cache, can be triggered

in several different ways, corresponding to the three different purposes it serves.

�When enabled by turning on the Smart Cache, nodes with processor-intensive operations (along

with all nodes appearing upstream in that grade’s node tree) are automatically cached, meaning

that, for example, if Nodes 1 and 2 are cached, you can continue adjusting Nodes 3, 4, and 5 to

your heart’s content without needing to re-render your grade to the cache. Operations that trigger

caching include Noise Reduction, Motion Blur, and any Resolve FX or OFX plugin that’s added to

a node. If you’ve added a Resolve FX to a node that’s capable of playing in real time but that node

is being flagged for caching anyway, you can force caching off for that node by right-clicking it and

choosing Node Cache > Off from the contextual menu.

�You can manually force any node to cache if it and its upstream nodes are compromising

performance but somehow not being automatically flagged, by right-clicking a node and choosing

Node Cache > On from the contextual menu.

�You can also turn on the “Render Cache Color Output” option for a clip in the Timeline of either

the Edit or Color pages. This forces that clip’s entire grade to be cached  via the Node Cache,

all the way through the Node tree’s output. This can result in higher real time performance in the

Edit page, at the expense of needing to completely re-cache that clip whenever you adjust any

part of its grade.

�If you apply Resolve FX or OFX filters to clips in the Edit page, these will also be cached via the

Node Cache. You can choose which OFX to cache via the Render Cache OFX Filter submenu

in the contextual menu for clips in the Timeline. This is useful when you have a combination of

realtime and non-realtime filters applied to a clip; caching the non-realtime filters only enables

you to continue adjusting realtime filters without the need to re-cache. However, be aware that

making changes to a filter being cached in the Edit page timeline will force that clip’s grade to be

re-cached in the Color page, and vice versa.

If multiple nodes are flagged for caching in a particular node tree, then each node will be individually

cached. That way, you can turn a cached node off and on to get a before-and-after look without

needing to re-cache the entire node tree. If a clip is part of a group in the Color page, you can enable

a Group Cache in the Group Pre-Clip and Group Post-Clip Node Editor modes, which cache these

parts of a group grade as part of the Node Cache.


Setup and Workflows | Chapter 8 Improving Performance, Proxies, and the Render Cache

MEDIA

Third, the Sequence Cache

The Sequence Cache is a separate cache for effects that are specifically applied within the Timeline in

the Edit page. These include transitions, opacity adjustments, adjustment layers and composite mode

superimpositions, as well as clips with Speed or Retime effects. Sequence Cache effects can be auto-

cached in both the Smart and User caches.