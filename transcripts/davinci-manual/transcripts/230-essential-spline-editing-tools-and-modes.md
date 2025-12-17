---
title: "Essential Spline Editing Tools and Modes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 230
---

# Essential Spline Editing Tools and Modes

The Spline Editor toolbar at the bottom contains a mix of control point interpolation buttons, Spline

loop modes, and Spline editing tools.

Control Point Interpolation

The first six buttons let you adjust the interpolation of one or more selected control points.

Control point interpolation controls

Smooth: Creates automatically adjusted Bézier curves to create smoothly

interpolating animation.

Linear: Creates linear interpolation between control points.

Invert: Inverts the vertical position of non-animated LUT splines. This does not operate on

animation splines.

Step In: For each keyframe, creates sudden changes in value at the next keyframe

to the right. Similar to a hold keyframe in After Effects® or a static keyframe in the

DaVinci Resolve Color page.

Step Out: Creates sudden changes in value at every keyframe for which there’s a change

in value at the next keyframe to the right. Similar to a hold keyframe in After Effects or a

static keyframe in the DaVinci Resolve Color page.

Reverse: Reverses the horizontal position of selected keyframes in time, so the keyframes

are backward.

Spline Loop Modes

The next three buttons let you set up spline looping after the last control point on a parameter’s spline,

enabling a limited pattern of keyframes to animate over a far longer duration. Only the control points

you’ve selected are looped.

Spline Loop modes

Set Loop: Repeats the same pattern of keyframes over and over.

Set Ping Pong: Repeats a reversed set of the selected keyframes and then a duplicate

set of the selected keyframes to create a more seamless pattern of animation.

Set Relative: Repeats the same pattern of selected keyframes but with the values of

each repeated pattern of keyframes being incremented or decremented by the trend of

all keyframes in the selection. This results in a loop of keyframes where the value either

steadily increases or decreases with each subsequent loop.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Spline Editing Tools

The next five buttons provide specialized Spline editing tools.

Spline editing controls

Select All: Selects every keyframe currently available in the Spline Editor.

Click Append: Click once to select this tool and click again to de-select it. This tool lets

you add or adjust keyframes and spline segments (sections of splines between two

keyframes), depending on the keyframe mode you’re in. With Smooth or Linear keyframes,

clicking anywhere above or below a spline segment adds a new keyframe to the segment

at the location where you clicked. With Step In or Step Out keyframes, clicking anywhere

above or below a line segment moves that segment to where you’ve clicked.

Time Stretch: If you select a range of keyframes, you can turn on the Time Stretch tool

to show a box you can use to squeeze and stretch the entire range of keyframes relative

to one another, to change the overall timing of a sequence of keyframes without losing

the relative timing from one keyframe to the next. Alternatively, you can turn on Time

Stretch and draw a bounding box around the keyframes you want to adjust to create a

time‑stretching boundary that way. Click Time Stretch a second time to turn it off.

Shape Box: Turn on the Shape Box to draw a bounding box around a group of control

points you want to adjust in order to horizontally squish and stretch (using the top/bottom/

left/right handles), corner pin (using the corner handles), move (dragging on the box

boundary), or corner stretch (Command-drag the corner handles).

Show Key Markers: Turning on this control shows keyframes in the top ruler that

correspond to the frame at which each visible control point appears. The colors of these

keyframes correspond to the color of the control points they’re indicating.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Thumbnail Timeline in the Fusion Page

In the Fusion page of DaVinci Resolve, the Thumbnail timeline (hidden by default) can be opened by

clicking the Clips button in the UI toolbar and appears underneath the Node Editor when it’s open.

The Thumbnail timeline shows every clip in the current Timeline, giving you a way to navigate from one

clip to another. Each thumbnail has a pop-up menu for creating and switching among multiple versions

of compositions, and resetting the current composition, when necessary.

The Thumbnail timeline lets you navigate the Timeline and manage versions of compositions.

Right-clicking on any thumbnail exposes a contextual menu.

The contextual menu for the Thumbnail timeline

To open another clip:

�Click any thumbnail to jump to that clip’s composition. The current clip is outlined in orange.

To navigate the Thumbnail timeline:

�Middle-click and drag the Timeline left or right to scroll through the clips in the Timeline.

�Click and drag the slider at the bottom of the Thumbnail timeline to scroll through the

clips in the Timeline.

To create and manage versions of compositions:

�To create a new version of a composition: Right-click the current thumbnail, and choose Create

New Composition from the contextual menu.

�To load a different composition: Right-click the current thumbnail, and choose “NameOfVersion”

> Load from the contextual menu.

�To delete a composition: Right-click the current thumbnail, and choose “NameOfVersion” >

Delete from the contextual menu.

�To rename a composition: Right-click the current thumbnail, and choose “NameOfVersion” >

Rename from the contextual menu.

To reset the current composition:

�Right-click the current thumbnail, and choose Reset Current Composition from the contextual menu.

To change how thumbnails are identified:

�Double-click the area underneath any thumbnail to toggle among clip format, clip name, and the

composition version name.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

The Media Pool in the Fusion Page

In DaVinci Resolve’s Fusion page, the Media Pool continues to serve its purpose as the repository

of all media you’ve imported into your project. This makes it easy to add additional clips to your

compositions simply by dragging the clip you want from the Media Pool into the Node Editor.

The media you add appears as a new MediaIn node in your composition, ready to be integrated into

your node tree however you need it.

TIP: If you drag one or more clips from the Media Pool onto a connection line between two

nodes in the Node Editor, the clips are automatically connected to that line via enough Merge

nodes to connect them all.

For more information on using the myriad features of the Media Pool, see Chapter 18, “Adding

and Organizing Media with the Media Pool.”

The Media Pool in Thumbnail mode showing video clips

Importing Media Into the Media Pool on the Fusion Page

If you find yourself in the Fusion page and you need to quickly import a few clips for immediate use,

you can do so in a couple of different ways.

To add media by dragging one or more clips from the

Finder to the Fusion page Media Pool (macOS only):


Select one or more clips in the Finder.


Drag those clips into the Media Pool of DaVinci Resolve, or to a bin in the Bin list. Those clips are

added to the Media Pool of your project.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

To use the Import Media command in the Fusion page Media Pool:


With the Fusion page open, right-click anywhere in the Media Pool, and choose Import Media.


Use the Import dialog to select one or more clips to import, and click Open. Those clips are added

to the Media Pool of your project.

For more information on importing media using the myriad features of the Media page,

see Chapter 18, “Adding and Organizing Media with the Media Pool.”

Bins in Fusion Studio

Bins in Fusion Studio are similar to the Media Pool in DaVinci Resolve. Bins are organizational panels

that provide an easy way of accessing commonly used tools, settings, macros, compositions, and

media content. They can keep all your custom content and resources close at hand, so you can use

them without searching through your hard drives. Bins can also be shared over a network to improve a

collaborative workflow with other Fusion Studio artists.

The Bins window

To open the Bins window:

Choose File > Bins from the menu bar.

Similar to the Media Pool in DaVinci Resolve, when adding an item to the Fusion bins, a link

is created between the item on disk and the bins. Fusion does not copy the file into its own

cache or hard drive space. The file remains in its original format and in its original location.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION