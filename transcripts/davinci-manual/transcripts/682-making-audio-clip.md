---
title: "Making Audio Clip"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 682
---

# Making Audio Clip

Selections in the Timeline

Nearly every editing operation described in this chapter and others requires you to make a selection

to define which clips will be affected. Three editing modes in the toolbar give you different ways of

selecting clips, depending on what you’re trying to do, and how you like to work. These are (from

left to right) the Pointer mode, the Range mode, and the Focus mode. Which mode you choose

determines how clips and clip segments are selected in the Timeline in preparation for all manner of

editorial operations.

The Pointer, Range, and

Focus modes seen in the toolbar

Fairlight Edit Mode Remains Between Application Restarts

Fairlight retains the Edit Mode the project was saved with between restarts. Whatever edit mode you

were working in prior to closing the application will be active when reopened.

Why Are There Three Edit Modes?

While the Pointer and Range modes can also be used with the pointer, they’re really designed

to enable automatic selections based on the position of the playhead. This is accomplished

when using the Fairlight Editing console, the Fairlight Desktop Console, or keyboard shortcuts

to control Timeline transport, while specific tracks are selected to enable selection and editing

on those tracks.

The Focus mode is designed for efficient selections made using the pointer via a mouse,

trackpad, or pen and tablet, made in conjunction with a variety of commands for extending

and editing selections triggered via keyboard shortcuts. If you’re editing with a keyboard

and mouse, this mode is designed to let you work quickly by enabling a variety of different

selection functions based on clicking different parts of clips.

Selecting Tracks

In order to understand clip selection, you must first understand track selection. The Timeline on the

Fairlight page lets you select entire tracks to facilitate the automatic selection of clips that intersect

the playhead on those tracks using keyboard shortcuts, the Fairlight Desktop Console, or the Fairlight

Editing panel, in Pointer and Range modes (described in upcoming sections).

For example, were you to select tracks A2, A3, and A4, then moving the playhead to intersect two clips

on those tracks in Pointer mode automatically selects them, so they’re ready for any operation you

want to perform on both clips. To give a few examples, you could now split both clips at the playhead,

Cut Head or Tail to the playhead, Delete both clips, or Copy them in preparation for pasting elsewhere.

Additionally, there are times when clicking or dragging on one or more clips with the pointer results in

both those clips being selected, along with the tracks on which they sit. For example, selecting clips

using the Focus mode will also select the tracks those clips are on.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

If you’re manually selecting tracks using the pointer, there are different ways to do so.

Command-clicking multiple track headers selects t.hose tracks

Methods of selecting and deselecting tracks in the Fairlight page Timeline:

�To select a single track: Click anywhere in the background or on the track number of that track’s

header (not on a button). In Range mode you can also click in any unused area of the track itself.

�To deselect a single track: Click anywhere in the background or on the track number of a

previously selected track’s header (not on a button). In Range mode you can also click in any

unused area of the track itself. If multiple tracks are selected, Command-clicking one will remove

just that track from the selection.

�To select multiple tracks: Command-click in the track header background of every track you

want to select. In Range mode you can also Command-click in any unused area of the tracks

themselves. Command-clicking an already selected track will deselect it.

�To select multiple continuous tracks: Click anywhere in the background or on the track number of

a track header, and then drag a bounding box up or down over all other tracks you want to select.

In Range mode you can also drag a bounding box over any part of the tracks themselves, while

also defining a range in which you want to work.

�To move the selection to higher or lower tracks: Press Control-Option-Up Arrow or Down Arrow

to move the selection state to the next track higher (Control-Option-Up Arrow) or lower (Control-

Option-Down Arrow). If multiple tracks are selected, then the multi-selection will be moved as a

block; for example, selecting tracks A2 and A3 and then pressing Control-Option-Down Arrow will

result in tracks A3 and A4 being selected.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Using Pointer Mode

Pointer mode uses the position of the playhead to make automatic selections when using the Fairlight

Editing console or keyboard shortcuts to make clip selections on selected tracks. However, you can

also use this mode in conjunction with the pointer and keyboard shortcuts to make selections in a

different style. Pointer mode is primarily intended to allow efficient editing of whole clips.

�If no tracks have been selected: Clips that intersect the playhead are not selected. You can use

the pointer to select one or more clips by clicking, Command-clicking, or dragging a bounding

box. Clips you select in this way are highlighted in orange. Making selections in this way is similar

to making clip selections in the Timeline of the Edit page.

�If tracks have been selected: All clips that intersect the playhead on selected tracks will be

automatically highlight selected, but no In and Out points will be set. Clips on de-selected tracks

will be ignored. Selecting one or more clips with the pointer (by Command-clicking or dragging a

bounding box) creates an orange-highlighted selection.

�If you set In and Out points: Some functions will affect ranges of clips between In and Out points

on selected tracks. Clips on unselected tracks are ignored.

To choose Pointer mode:

�Click the Selection tool (the arrow) in the toolbar.

�Choose Trim > Pointer mode.

�Press A.

To automatically select clips using the playhead position in Pointer mode:


Press A to enter Pointer mode.


Select one or more tracks with clips you want to select.


Move the playhead to intersect those clips.

All clips that intersect the playhead on selected tracks of the Timeline are automatically

selected in their entirety. Automatic selections are illuminated brighter to indicate their selection.

Intersecting clips on unselected tracks are not selected.

Clips intersecting the playhead in Pointer mode are automatically selected with orange highlights


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Methods of selecting clips using the pointer:

�Click any clip to select it.

Click a clip to select it

�Command-click multiple clips to select them all at once.

Command-clicking multiple clips selects those clips, even if they’re separated by other clips

�Click anywhere in the background of the Timeline and drag a bounding box over multiple clips.

Dragging a bounding box over multiple clips selects all of them

Using Range Mode

Range mode also uses the position of the playhead to make selections of a partial range of clips in the

Timeline when using the Fairlight Editing console or keyboard shortcuts. You can also use this mode in

conjunction with the pointer and keyboard shortcuts to make partial selections of clips.

�If no tracks have been selected: Clips that intersect the playhead are not selected. You can use

the pointer to click a clip and select it in its entirety along with the track it’s on. You can also use

the pointer to drag on one or more clips to select a partial range in preparation for different editing

operations. Whenever you make a selection with the pointer, Timeline In and Out points are set to

the boundaries of the selection.

�If tracks have been selected: Selected tracks are brightened in the Timeline, and any clip on a

selected track that intersects the playhead will be automatically highlighted brighter. Clips on

de-selected tracks will be ignored. Dragging a crosshairs over one or more clips with the pointer


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

overrides all automatic selections and selects the regions of the clips you drag over, and the

tracks they’re on.

�If you set In and Out points: Partial regions of all clips on all selected tracks between the In and

Out points will be highlighted brighter. Clips on unselected tracks are ignored. While In and Out

points are set, the playhead no longer makes automatic selections; you must set new In and Out

points to modify the selection in this mode.

To choose Range mode:

�Click the Range Selection tool (the crosshairs) in the toolbar.

�Choose Trim > Range mode.

�Press R.

To automatically select clips in Range mode using the playhead position:


Press R to enter Range mode.


Select whichever tracks have clips you want to select.


Move the playhead to intersect those clips.

All clips that intersect the playhead, on the tracks you selected, define a selected range from the

beginning of the first selected clip to the end of the last selected clip.

Clips intersecting the playhead on a selected track in Range mode are automatically selected

To create custom clip ranges using In and Out points in the Timeline:


Press R to enter Range mode.


Select whichever tracks have clips you want to select.


Move the playhead and press the I (Mark In) and O (Mark Out) keys to define a range in

the Timeline.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

All clip segments that fall within the range of your In and Out points on selected tracks will

be selected.

Using the Range mode to select clip segments on selected tracks using In and Out points

Methods of selecting clips in Range mode via clicking and dragging:

�To select a single clip: Click any clip to select both it and the track it’s on, and define a range in

the Timeline that matches the duration of that clip.

Click to select a single clip as well as the track it’s on


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

�To select multiple clips: Command-clicking multiple clips to select them all at once defines a

range in the Timeline that matches the total overlapping duration of all clips in the selection, from

the beginning of the first selected clip to the end of the last selected clip.

Range selection by Command-clicking multiple clips

�To drag to select a range within a single clip: With the Range Selection tool selected, drag

anywhere on top of a clip to drag a bounding box over whatever segment of that clip (or of one

or more clips) to select both that clip segment and the track it appears on. This is a good way of

selecting part of a recording you want to move or delete.

Ranged selection within a clip using a bounding box


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

�To drag to select a range within multiple clips: Click and drag a bounding box over whatever

segment of one or more clips you want to select to select both those clip segments and the tracks

they appear on. Or, Command-click and drag anywhere on top of any clip to drag a bounding box

over whatever region of clips and tracks you like.

Ranged selection across multiple clips using a bounding box

In Range mode, whenever you make a selection, the In and Out point fields update with the range

that you’ve created.

The range fields showing you

the In and Out point values that

define the current range

These ranges can be cleared if necessary.

Methods of clearing In and Out points to clear the current range:

�Press Option-I to clear the current In point.

�Press Option-O to clear the current Out point.

�Press Option-X to clear both the In and Out points.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT