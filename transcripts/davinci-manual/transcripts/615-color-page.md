---
title: "Color Page"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 615
---

# Color Page

Effects

CONTENTS

151	 Using Open FX and Resolve FX�������������������������������������������������������������������������������������������������������� 3416

152	 Sizing and Image Stabilization���������������������������������������������������������������������������������������������������������� 3429

153	 The Motion Effects and Blur Palettes��������������������������������������������������������������������������������������������� 3445

Chapter 151

Using Open FX

and Resolve FX

This chapter covers the use of Resolve FX and Open FX plugins, that allow you to

use the built-in filters that come with DaVinci Resolve, as well as third-party filters

from a variety of companies, to create complex effects and adjustments that aren’t

possible using the ordinary palette tools in the Color page.

Contents

Resolve FX���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3417

Open FX��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3417

Where are OFX Installed?��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3418

Open FX Plugins Can Be Processor Intensive��������������������������������������������������������������������������������������������������������������������� 3418

Browsing the Effects Library�������������������������������������������������������������������������������������������������������������������������������������������������������� 3418

Effects Library Favorites������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3419

Using Resolve FX and Open FX in the Color Page��������������������������������������������������������������������������������������������������������� 3420

Applying Resolve FX and Open FX Plugins������������������������������������������������������������������������������������������������������������������������ 3420

Adding a Plugin to an Existing Corrector Node������������������������������������������������������������������������������������������������������������������ 3420

Adding a Plugin as a New Corrector Node���������������������������������������������������������������������������������������������������������������������������� 3421

Adding a Plugin as a Stand-Alone FX Node (Legacy)������������������������������������������������������������������������������������������������������� 3421

Resolve FX and Open FX Settings������������������������������������������������������������������������������������������������������������������������������������������� 3422

Editing Effects Using the Full Screen Viewer����������������������������������������������������������������������������������������������������������������������� 3422

Resolve FX and Open FX Onscreen Controls�������������������������������������������������������������������������������������������������������������������� 3423

Keyframing Resolve FX and OFX in the Inspector����������������������������������������������������������������������������������������������������������� 3424

Motion Tracking Resolve FX and Compatible OFX Plugins���������������������������������������������������������������������������������������� 3425

IntelliTrack AI Point Tracker (Studio Version Only)������������������������������������������������������������������������������������������������������������� 3428


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR

Resolve FX

Resolve FX are the built-in plugins that come with DaVinci Resolve. These plugins span the gamut from

blurs and complex color adjustments to stylized image treatments and lighting effects to sharpen and

repair operations that are too complex to accomplish using the palette controls of the Color page.

An image before/after using the Abstraction Resolve FX filter

Most Resolve FX plugins have been optimized for real-time playback, making it possible to apply

complex effects such as Lens Flares, Light Rays, Film Grain, or Warping, and make adjustments while

getting immediate, high-quality feedback, and enabling you to play each variation of your effect as

you work without the need to wait for rendering or caching to happen first. Of course, if you’re working

with extremely high-resolution or raw source media, if your workstation is particularly old, or if you’re

applying many Resolve FX all at once, your performance may slow, necessitating the use of either the

Smart Cache or User Cache.

Open FX

Open FX (OFX) is an open plugin standard intended to enable easier development of cross-platform

visual effects plugins for a variety of applications. Popular plugin packages include BorisFX Sapphire

and Continuum Complete, Red Giant Universe, and NewBlue TotalFX, all of which are ubiquitous tools

for feature and broadcast work. The available Open FX plugin packages are also growing every year

as this format becomes more widely adopted among developers.

With Open FX support, you can use plugins to do many stylized operations that would be difficult or

impossible to do using the other tools in DaVinci Resolve. Everything from lens flares, optical blurs and

prism effects, lens warp correction, film and video grain and damage effects, dead-pixel corrections,

and more can be accomplished with the right plugin collection.

One of the many Sapphire OFX plugins from GenArts


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR

The installation and licensing of Open FX plugins is handled by a vendor’s own installer. Once

installed, Open FX plugins appear within the Library of the Open FX panel, which can be opened by

clicking the FX button at the top right of the Color page or Edit page Interface toolbar.

Where are OFX Installed?

According to the standard governing how OFX work, all OFX plugins on a particular workstation

are installed into a standardized location to foster plugin compatibility with multiple applications.

These locations are:

On macOS: /Library/OFX/Plugins

On Windows: C:/Program Files/Common Files/OFX/Plugins

On Linux: /usr/OFX/Plugins

Open FX Plugins Can Be Processor Intensive

Because they create such a wide variety of effects, some third-party Open FX plugins can be

extremely processor intensive, all the more if you add multiple plugins to a single grade. If you find

your playback performance dropping because of a particularly expensive effects operation, you can

use the Smart Cache to automatically cache nodes and clips that have Open FX plugins applied to

them. Once fully cached, you can play these clips back in real time, at least until you change that clip’s

grade again.

For more information on caching and on improving performance in DaVinci Resolve overall,

see Chapter 8, “Improving Performance, Proxies, and the Render Cache.”

Browsing the Effects Library

All of these built-in plugins appear within categories at the top of the Effects Library.

Click the Effects button to open the Effects Library

When you click the Effects button, the Effects panel opens out of the right side of the Node Editor to

show the Library, resizing the Viewer, Gallery, and Node Editor to make room. The Effects Library is

organized hierarchically. Each vendor’s plugins appear under a header with the name of that plugin

collection, and possibly organized into categories, separated by headers with Open or Close arrows

that appear to the right of the category name, which let you show or hide the contents so that you can

make the hierarchy as compact or spread out as you like.


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR

To open and close Effects categories, do one of the following:

�Move the pointer over the header you want to open or close, and click the Close or Open arrow to

the right of the category name.

�To open or close all headers at once, Option-click the Open or Close arrow.

Since many Open FX plugin collections are quite large, an optional Search field can be opened at the

top of the Library that lets you quickly find plugins by name or partial name.

To search for an Effects filter by name:


Click the magnifying glass button at the upper right-hand corner of the Effects panel.


Type your search string into the Search field that appears. A few letters should be enough to

isolate only those plugins that have that character string within their name.

The Library in the Effects

panel showing available effects

Stars indicate a flagged

favorite effect

Effects Library Favorites

You can click on the far right of any Resolve FX or OFX filter to flag it with a star as a favorite filter.

When you do so, choosing Favorites from the Effects Library option menu filters out all clips that are

not favorites, letting you see only effects you most commonly use. To “de-favorite” any effect, click its

star to turn it off.


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR