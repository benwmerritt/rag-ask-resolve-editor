---
title: "Gallery"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 531
---

# Gallery

The Gallery is used for storing still frames to use as reference, and grades you might like to copy;

stills and grades are stored together. A button lets you open up the Album browser, used for

organizing your stills. At the bottom of the Gallery, Memories let you store grade information that you

can apply using a control panel or keyboard shortcuts. The Gallery on the Color page mirrors the

contents of the Gallery page.

For more information on the Gallery page, see Chapter 141, “Using the Gallery.”

The Gallery has Memories, stills saved in albums and your PowerGrades

LUT Browser

The LUT Browser provides a centralized area for browsing and previewing all of the LUTs installed on

your workstation. All LUTs appear in the sidebar, by category.

The LUT Browser

By default, all LUTs appear with a test thumbnail that give a preview of that LUT’s effect, but you can

also get a live preview of how the current clip looks with that LUT by hover scrubbing with the pointer

over a particular LUT’s thumbnail (this is described in more detail below).


Color | Chapter 126 Using the Color Page

COLOR

To open the LUT Browser:

Click the LUT Browser button in the UI Toolbar at the top of the Color page.

Methods of working with the LUT Browser:

To see the LUTs in any category: Click on a LUT category to select it in the sidebar, and its

LUTs will appear in the browser area.

To make a LUT a favorite: Hover the mouse over a LUT and click the star badge that appears

at the upper right-hand corner, or right-click any LUT and choose Add to Favorites. That LUT

will then appear when you select the Favorites category.

To search or filter for specific LUTs: Open a bin that has the LUT you’re looking for, then click

the magnifying glass icon to open the search field, and type text that will identify the LUTs

you’re looking for.

To see LUTs in Column or Thumbnail view: Click the Column or Thumbnail buttons at the top

right of the LUT Browser to choose how to view LUTs in the browser area.

To sort LUTs in Thumbnail view: Click the Thumbnail Sort drop-down menu and choose

which criteria you want to sort LUTs by. The options are Filename, Type, Relative Path, File

Path, Usage, Date Modified. There are also options for ascending and descending sort modes.

To sort LUTs in Column view: Click the column header to sort by that column. Click a header

repeatedly to toggle between ascending and descending modes.

To update the thumbnail of a LUT with an image from a clip: Choose a clip and frame that

you want to use as the new thumbnail for a particular LUT, then right-click that LUT and choose

Update Thumbnail With Timeline Frame.

To reset the thumbnail of a LUT to use the standard thumbnail: Right-click a LUT and

choose Reset Thumbnail to go back to using the standard test image.

To refresh a LUT category with new LUTs that may have been installed: Select a LUT

category, then right-click anywhere within the browser area and choose Refresh to refresh the

contents of that category from disk.

Methods of adding LUTs to a grade from the LUT Browser:

To apply a LUT to the current node: Select a clip in the Thumbnail timeline, then right-click a

LUT and choose Apply LUT to Current Node from the contextual menu.

To apply a LUT to a specific node: Drag a LUT from the LUT Browser and drop it onto the

node you want to apply a LUT to. If you drag a LUT onto a node that already has a LUT, the

previous LUT will be overwritten by the new one.


Color | Chapter 126 Using the Color Page

COLOR

Media Pool

The Media Pool is available in the Color page, making it easy to drag and drop clips you want to use

as external mattes right into the Node Editor, for easy and fast connection to create various Color

page effects. When opened, the Media Pool replaces the Gallery, fitting into the same area. In most

respects, the Media Pool in the Color page works the same as the Media Pool on nearly every other

page of DaVinci Resolve.

The Media Pool is available in the Color page.

When you drag a clip from the Color page Media Pool to the Node Editor, two things happen:

�That clip is turned into an external matte in the current grade, which you can use as a matte for

secondary adjustments, or as a compositing layer (in conjunction with the Layer mixer) for mixing

textures or images with your grade.

�That clip is also automatically attached to the Media Pool clip that corresponds to the clip you’re

grading as a clip matte, to help you keep track of which clips are using other clips as mattes.

For more information about the Media Pool, see Chapter 18, “Adding and Organizing Media

with the Media Pool.”


Color | Chapter 126 Using the Color Page

COLOR

Node Editor

The Node Editor is where you assemble one or more individual corrections (nodes) together into

a complete multi-correction grade (node tree). This is a powerful way of assembling grades, since

different types of nodes let you create different combinations of corrections and very specific

adjustments by reordering operations, combining keys, or changing the layer order of different

adjustments.

For more information about the Node Editor, see Chapter 143, “Node Editing Basics.”

Node Editor to construct your grade processing signal flow

Timeline

The Timeline provides several ways of navigating the clips in your project, as well as keeping track

of what has been done to which clips. The Timeline is divided into two parts, each of which shows

different information and provides differing controls, and each of which can be opened or closed

separately via the Clips and Timeline buttons on the Interface toolbar.

The Thumbnail timeline with a Mini-Timeline below

Thumbnail Timeline

At the top is the Thumbnail timeline, in which each clip is represented by a single frame. The Thumbnail

timeline (or its alter-ego, the Lightbox) provides the easiest way of selecting which clip you want

to work on and of making clip selections for various grade management operations. The currently

selected clip that reveals its controls in the various palettes of the Color page is highlighted in orange.

Much valuable information appears above and below each thumbnail, such as each clip’s clip number,

source timecode, track number, whether it’s been flagged, whether it’s automatically linked or part of a

group, whether it’s been tracked, and so on.


Color | Chapter 126 Using the Color Page

COLOR

A clip thumbnail in

the Thumbnail timeline

What’s displayed underneath each thumbnail can be changed by double-clicking the space

underneath each thumbnail. There are several options; you can keep double-clicking to cycle

among them:

•	 Clip format or codec (the default)

•	 Clip Name (clip name or file name, depending on what View > Show File Names is set to) or

Multicam Angle (if you’re working with multicam clips)

•	 Version name or number

Mini-Timeline

Underneath, the Mini-Timeline shows a small representation of the video tracks of the Timeline in the

Edit page wherein each clip is as long as its actual duration. This provides the best representation

of the structure of the current timeline, in which clip length shows duration and multiple tracks are

displayed, so you can see which clips are superimposed. A Timeline Ruler lets you scrub the playhead

across multiple clips and can be zoomed out enough to show every clip in your entire program.

The Mini-Timeline lets you see timeline structure, and small track header controls let

you enable tracks, disable tracks, and set the playhead to ignore specific tracks

Small track labels at the left of each track in the Mini-Timeline let you enable or disable tracks by

clicking them (enabled tracks have white labels, disabled tracks have gray labels). Option-clicking one

of these controls sets that track to be enabled but ignored by the playhead when you use the Next

and Previous Clip commands, in the event you want to ignore clips you don’t need to grade (tracks in

this mode show a red label).

Within the Mini-Timeline the currently selected clip is highlighted in orange, and you can click any clip

to select it. A scroll bar at the bottom lets you navigate to the left and right, while using the scroll wheel

of your mouse zooms in and out. The Mini-Timeline shows at most six tracks of video. If your project

has more tracks than that, you can scroll up and down to reveal the hidden tracks. Any markers that

were placed on clips or the Timeline in the Edit page appear here, and you can click any marker to

reveal and edit its color and notes.

As seen above, a colored outline appears around the clip number of shots that have been graded, and

this outline is doubled if there are additional versions applied to that clip.


Color | Chapter 126 Using the Color Page

COLOR

For more detailed information about the Color page Timeline, see Chapter 126, “Color Page

Timeline and Lightbox.”