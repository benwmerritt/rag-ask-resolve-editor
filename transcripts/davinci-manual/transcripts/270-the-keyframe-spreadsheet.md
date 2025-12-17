---
title: "The Keyframe Spreadsheet"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 270
---

# The Keyframe Spreadsheet

If you turn on the Spreadsheet and then click on the name of a layer in the keyframe track, the numeric

time position and value (or values if it’s a multi-dimensional parameter) of each keyframe appear

as entries in the cells of the Spreadsheet. Each column represents one keyframe, while each row

represents a single aspect of each keyframe.

Editing keyframes in the Spreadsheet

For example, if you’re animating a blur, then the Key Frame row shows the frame each

keyframe is positioned at, and the Blur1BlurSize row shows the blur size at each keyframe. If

you change the Key Frame value of any keyframe, you’ll move that keyframe to a new frame of

the Timeline.

Duplicating Spline Keyframes

Keyframes can be duplicated, either onto the same keyframe track or onto different tracks. This can

save you time if you need to repeat a keyframe sequence at another time on the same segment, or

even just create identically-timed keyframes on two different segments.

To duplicate keyframes, do the following:


Select one or more keyframes you want to duplicate.


Hold Command and drag one of the selected keyframes to a new position.

Time Stretching Keyframes

If you select a range of keyframes in a keyframe track, you can turn on the Time Stretch tool in the

lower left of the Keyframes Editor, to show a box you can use to squeeze and stretch the entire

range of keyframes relative to one another, to change the overall timing of a sequence of keyframes

without losing the relative timing from one keyframe to the next. Alternatively, you can turn on Time

Stretch and draw a bounding box around the keyframes you want to adjust to create a time-stretching

boundary that way. Click the Time Stretch tool again to turn it off.

Time stretching keyframes


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

Showing Keyframe Values

When a node and its accompanying segment have animated parameters, keyframes appear as

colored tick marks in keyframe tracks to indicate when animated changes occur. If the tracks and

splines are open on a parameter, choosing Show Values from the Keyframes Editor Option menu

shows editable fields beneath each keyframe. These fields show each keyframe’s current value and

allow you to edit them simply by entering a new number.

Show values from the Keyframes Editor Option menu

Timeline Filters

When a composition grows to include hundreds of nodes, locating specific node layers can quickly

become difficult. Timeline filters can be created and applied to sift out nodes that are not necessary to

the current operation. The Global Timeline preferences include a number of pre-made filters that you

can enable, or you can create new ones as needed.

To use a Timeline filter:

Open the Keyframes Editor Option menu and choose an item from the top of the menu. Default

Timeline filters include;

�Show All, which shows all node layers in the current composition.

�Show None, which hides all layers.

�Show Tools at Current Time, which only displays node layers under the playhead.

�If you’ve created custom filters, they appear here as well, in alphabetical order.

To go back to showing everything:

�Choose Show All from the Keyframes Editor Option menu. All layers will reappear.

Choosing a Timeline filter


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

To create a Timeline filter:


Choose Create/Edit Filters from the Keyframes Editor Option menu to open the Timeline panel of

the Fusion Settings window. This is where you can create new Timeline filters.

The Global Timeline preferences for enabling filters


Click the New button, enter a name for your new filter setting, and click OK. The filter you created

is now selected in the Filter pop-up menu at the top.


Use the “Settings for filters” list to turn on the checkboxes of nodes you want to be seen and turn

off the checkboxes of nodes you want to filter out. Each category of node can be turned on and

off, or you can open up a category’s disclosure control to turn individual nodes on and off. Clicking

Invert All immediately turns off all node categories.


When you’re finished creating filters, click the Save button to hide the Fusion Settings window.

Filters that you’ve created in the Timeline panel of the Fusion Settings window appear in the

Keyframes Editor Option menu.

To delete a filter:


Choose Create/Edit Filters from the Keyframes Editor Option menu to open the Timeline panel of

the Fusion Settings window. This is where you can delete Timeline filters.


Choose the filter you want to delete from the Filter pop-up menu.


Click the Delete button, and when a dialog asks if you really want to do that, click OK.

Selected Filtering

Choosing “Show only selected tools” from the Keyframes Editor Option menu filters out all segments

except for layers corresponding to selected nodes. This option can be turned on or off.

TIP: When “Show only selected tools” is enabled, you can continue to select nodes in the

Node Editor to update what’s displayed in the Keyframes Editor.


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

Sorting in the Timeline

You can change the order in which the nodes are displayed from top to bottom in the Timeline.

�You can use the Tree Item Order Selection menu to sort the tracks by an assigned number.

�You can use the Sort pop-up menu.

The Tree Item Order Menu

Right-clicking over any track on the Keyframes Editor will display a contextual menu that contains

the Tree Item Order Selection submenu. Choosing Start from the submenu allows you to start

numbering each item in the track header by clicking on them. The first item you click will be #1, the

second item #2, the third #3, and so on. Once you have selected all the items in the order you want

them to be organized in the Keyframes Editor, right-click over a track, and from the Tree Item Order

Selection submenu, choose End. The items will be ordered using the assigned numbers, with #1

appearing above #2, which appears above #3, and so on. The first items in the Keyframe track list

will always be the nodes that are the root of the node tree. The numbered nodes will appear in order

after the root nodes. For example, if the node tree starts with a background node, and then connects

to a Fast Noise, Blur, and Color Corrector, the background node will always appear at the top of the

Keyframes Editor track list because it is the root node.

The Keyframes Editor Tree Item Order Selection menu

If you begin numbering nodes in the track header and change your mind or decide on a different

order, you can choose Restart to begin numbering again or choose Cancel to keep the current order.

The Sort Menu

The Sort menu reorders how the layers of each node appear in the Keyframes Editor. Setting the

menu back to All Tools will display them in a linear order, scanning the Node Editor from left to right

and top to bottom. This is the default setting.

The Timeline Sort Order menu

�All Tools: Forces all tools currently in the Node Editor to be displayed in the Keyframes Editor.


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION

�Hierarchy: Sorts with the most background layers at the top of the header, through to the most

foreground layers at the bottom, following the connections of the nodes in the Node Editor.

�Reverse: The opposite of Hierarchy, working backward from the last node in the Node Editor

toward the most background source node.

�Names: Sorts by the alphabetical order of the nodes, starting at the top with the beginning

of the alphabet.

�Start: Orders layers based on their starting point in the composition. Nodes that start earlier

in the Global project time are listed at the top of the header, while nodes that start later are

at the bottom.

�Animated: Restricts the Timeline to showing animated layers only. This is an excellent mode to

use when adjusting the timing of animations on several nodes at once.

Markers

Markers help identify important frames in a project that might affect how you keyframe animation.

They may indicate the frame where a dragon breathes fire at a protagonist, the moment that someone

passes through a portal, or any other important frame in a composition that you need to keep track of.

Markers added to the Timeline in the Cut, Edit, Fairlight, or Color page will appear in the Keyframes

Editor and Spline Editor of the Fusion page. They can also be added from the Keyframes Editor or the

Spline Editor while working in Fusion Studio or the Fusion page. Markers in Fusion appear as a small

handle with a line extending vertically through the graph view when selected.

A marker being moved in the Keyframed Editor

To create a marker, do the following:

Right-click at a frame in the Timeline Ruler of the Keyframes Editor and choose Add Marker

from the contextual menu.

The most important attribute of a marker is its position. For it to add value, a marker must be placed on

the frame you intended it to be on. Hovering the cursor over a marker displays a tooltip with its current

frame position. If it is on the wrong frame, you can drag it along the Time Ruler to reposition it.

Markers added to the Time Ruler are editable in the Fusion page, and the changes appear back in the

other DaVinci Resolve pages. Time Ruler markers can be added, moved, deleted, renamed, and given

descriptive notes from within Fusion’s Keyframes or Spline Editor.

NOTE: Markers attached to clips in the Edit page Timeline are visible on MediaIn nodes in

Fusion’s  Keyframes Editor but not editable. They are not visible in the Spline Editor.


Fusion Fundamentals | Chapter 71 Animating in Fusion’s Keyframes Editor

FUSION