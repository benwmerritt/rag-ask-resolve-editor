---
title: "Adding Markers to Timelines"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 160
---

# Adding Markers to Timelines

You can also place markers of any color into the Timeline ruler to denote specific times for future

reference, or add notes about issues you want to keep track of.

Timeline markers placed for future reference

You should note that all markers placed on clips or in the Timeline also appear within the Mini-Timeline

of the Color page, making it easy to place notes for later reference when grading.

Clip and Timeline markers as seen in the Mini-Timeline of the Color page

Once you’ve added one or more markers placed on clips, snap to clip In and Out points, edit points,

the playhead, and other markers whenever snapping is enabled.

To mark the Timeline itself, make sure all clips

are deselected, and do one of the following:

�Press M.

�Click the Marker button to place a marker of the currently selected color in the Timeline ruler.

�To place a marker during playback and immediately open the marker dialog to enter a

name or note within it, select one or more clips you want to mark, then press Command-M

(or press M twice). Playback pauses until you enter some text and close the marker dialog again,

at which point playback continues.

�Click the Marker drop-down to choose a different color, and click the Marker button.

�Right-click in the Timeline ruler and choose a marker color from the Add Marker submenu of the

contextual menu.

�Choose Mark > Add Marker > Current Color (M) to add the current marker color. Alternatively, you

can choose Mark > Add Marker > Blue/Cyan/Green/and so on to add a marker of a specific color

directly to clips or the Timeline. These commands can be assigned specific keyboard shortcuts if

you want to be able to place a specific marker color at a keystroke.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

Individually mappable marker color commands

Saving In and Out Point Ranges As Markers with Duration

You can also create markers with duration to keep track of any region of a clip or timeline that you’ve

defined with In and Out points. This lets you identify multiple regions of a clip that you might later want

to edit into a program.

To turn In and Out points into a marker with duration:


Set In and Out points in the Source Viewer jog bar to identify a region you want to log for

future reference.

Marking In and Out points in preparation

to log that section of the clip


Do one of the following:

�Right-click the jog bar and choose Convert In and Out to Duration Marker

�A marker with duration appears above the In and Out points. To edit its name or notes,

double‑click the marker, press Shift-M, or choose Mark > Modify Marker.

A marker with duration is created from

the In and Out points

In this way, you can log several regions within a single clip for future use.

A clip with multiple logged sections identified via markers with duration


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

This an extremely useful logging technique for two reasons. First, markers with duration can be

searched for in the Media Pool using the All Fields, Marker Name, and Marker Notes Filter by options.

Second, they can be filtered with Smart Bins using the Marker Name and Marker Notes Media Pool

Properties options.

Editing Marker Information and Keywords

Once you’ve added some markers, you may want to edit their contents to make them more useful.

To open a marker’s edit dialog to alter its properties:


Do one of the following:

�Press Command-M to add a marker during playback and immediately open its edit dialog.

�Double-click any marker you want to edit.

�Move the playhead to the frame containing the marker you want to annotate using Shift-Up

Arrow/Down Arrow and press M.

�Select a marker anywhere in the Source Viewer or Timeline, and press Shift-M.


When the marker dialog opens, you can modify several properties in separate fields. For fast

editing, you can press Tab to select the next field, or you can press Shift-Tab to select the

previous field.

Editable properties in the Marker dialog

Time: The frame the marker is positioned at relative to that clip or timeline. This is editable, so you

can numerically change a marker’s position.

Duration: Optional; the length of a marker that’s been assigned a duration. This is also editable, so

you can numerically assign a duration to a marker or alter a marker that already has duration.

Name: The name of the marker, defaults to the number of that marker in the order it was added

(Marker 1, Marker 2, etc.).

Notes: A field where you can enter any information you want to keep track of.

Color: A series of buttons for choosing the color of the marker.

Keyword: A keyword field lets you keyword markers in the same way you can keyword clips in the

Metadata Editor, which can be a powerful way of identifying sections of clips you want to find later

in Smart Bins or Search operations. Typing text in the Keyword field automatically searches the

dictionary for matching keywords. Press Return to accept a found keyword (you can choose from

a list using the Arrow keys), or press the Up Arrow key back to the Keyword field to manually enter

your own new variation instead.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

For more information about using and editing Keywords,

see Chapter 16, “Using Variables and Keywords.”

Remove Marker: Deletes that marker.

Done: Closes the marker edit dialog.


When you’re finished, click Done.

Once you add notes to a marker, a small symbol appears on top of that marker to show

you it has information.

A small dot on a marker

shows that it contains notes

Changing Marker Timing

Once you’ve placed one or more markers, there are a variety of ways you can move them around to

better line up with important events in source footage or the Timeline, or delete them once they’re

no longer useful. Additionally, you can enable or disable the ability to have markers ripple along with

other clips in areas of the Timeline that are affected by rippling operations.

To move one or more markers in the Timeline or Source Viewer:

�Click a marker or Command-click multiple markers you want to move, and drag them to a

new location.

�Drag a bounding box from the Timeline up into the Timeline ruler to select multiple markers, and

drag them to a new location.

�Open a marker’s edit dialog and manually edit the time and duration timecode fields to numerically

move that marker, or to create a marker with a specific duration. Furthermore, the timecode in

these fields can be copied from or pasted to.

To enable marker rippling:

�Choose Timeline > Ripple Timeline Markers. When checked, all markers to the right of a clip being

ripple edited, trimmed, or ripple deleted will ripple to the left along with the rest of the Timeline.

You can turn this behavior off and on at will.

To modify marker duration:

�Option-drag any marker to the right or left to create a marker with duration.

A marker with duration in the Timeline

�Move the playhead to the frame containing the marker you want to modify and press M, or

double‑click the marker you want to edit, then type a number into the duration field, and

click Done.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

�Markers with duration appear as a bar in the Timeline ruler or jog bar of the Source Viewer.

Drag the middle of a marker with duration to move it, or drag the left or right edge to

change its duration.

�To eliminate a marker’s duration, set its numeric duration to 00:00:00:00 in the marker dialog, or

drag either end so that it merges with the other as a single marker.

Methods of deleting markers:

�To remove one or more markers using the mouse: Click to select a marker, or Command-click to

select multiple markers, and press the Delete key. You can also double-click a marker to open its

dialog, and click the Delete button.

�To remove a marker using the keyboard: Move the playhead to the marker you want to delete,

and press Option-M.

�To remove all markers from a clip: Select one or more clips with markers you want to remove,

then either press the Backspace key, or click the Marker drop-down in the Toolbar, and

choose Clear All.

�To remove all markers from the Timeline: With all clips deselected, choose Clear All from the

marker drop-down menu in the Toolbar, or right-click the Timeline ruler, and choose Remove All

Markers from the contextual menu.

Copy and Paste Multiple Markers in the Viewers and Timeline

In the Edit page, you can select multiple markers by Shift or Command-Clicking them, or by dragging a

boundary box. Once selected, these markers can be copied to the clipboard by pressing Command-C.

They can then all be pasted into another clip, timeline, or compound clip at the playhead position by

pressing Command-V.

If a timeline clip is selected for Paste, DaVinci Resolve will create clip markers on the clip. If no

selection is made, DaVinci Resolve will make timeline markers instead.

This is useful to make sure critical marker information is easily sharable between various iterations of

media across timelines. The copy and paste operations can be done in either the Source and Timeline

Viewers, or in the Timeline itself.

Marker Notes in Data Burn-Ins

You can use marker notes for display in Data Burn-Ins. To do so:


Create a Marker and add a word or words in the Notes section.


Open Workspace > Data Burn-In.


Check one of the Custom Text options.


In the field that opens, type the “%” sign, and then start to spell the word “marker.”


Choose Marker Notes from the list.


Adjust the font/position/opacity parameters as necessary.

Any text that you put in the Marker Notes section will now show up as a Data Burn-In. If you want the

notes to last more than a single frame, make sure to change the marker to a duration marker instead.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

The marker note “Stock Footage” is now a Burn-In, using the % metadata tags in a Custom Text field.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT