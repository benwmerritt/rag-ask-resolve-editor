---
title: "Inserting Multiple Clips into the"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 140
---

# Inserting Multiple Clips into the

Timeline From the Media Pool

For certain large volume editing projects, you can insert multiple clips from the Media Pool into

a timeline all at once. The parameters for the order and positioning of the clips depend on the

method used.

Insert Selected Clips to Timeline Using Timecode

Clips can now be edited directly from the Media Pool into a timeline, such that each clip’s source

timecode is aligned with an identical record timecode value in the Timeline. This can be useful for

long form multi-camera events, like weddings or concerts, where all cameras are linked by the same

timecode to ensure all edits are perfectly synced. This function matches the Source Overwrite edit on

the Cut page.

IMPORTANT: The timecode of the Timeline must overlap the timecode of the clip(s) for this

edit to function. This can be set in the Start Timecode field of the New Timeline settings.

To insert selected clips to timeline using timecode:


Select one or more clips to edit into the Timeline in the Media Pool. If there are In and Out points

set on the clip, the edit will respect those boundaries. If no In/Out points are set, each selected

clip’s full duration will be edited in its entirety.


Set a destination control to determine which track in the Timeline you want to edit to.


Right-click one of the selected clips and choose “Insert Selected Clips to Timeline Using

Timecode” from the drop-down menu.


All of the selected clips will be overwritten into the Timeline at their appropriate timecode

locations onto the destination track.

IMPORTANT: If multiple selected clips have overlapping timecode, no edit will occur.

Insert Selected Clips to Timeline With Handles

This command inserts multiple clips into the Timeline serially, using the current sort order of the

Media Pool, with handles subtracted from the current In and Out points of each clip (using the Default

Handles Length in the Editing panel of the User Preferences). Combined with the Add Transition tool

(Command-T), this function is useful when quickly creating montages from multiple clips.

To insert clips with handles to the Timeline:


Select the clips to insert into the Timeline with handles in the Media Pool.


Right-click any selected clip, then choose “Insert Selected Clips to Timeline With Handles.”

The clips will be inserted starting at the Timeline In point with the default handles length

already calculated.


Edit | Chapter 36 Editing Basics

EDIT

TIP: To finish creating the montage, select the clips in the Timeline, then choose

“Add Transition” (Command-T) from the Timeline menu. This will apply the default

transition to all of the clips at once.

Audio Track Creation While Editing

When dragging an audio clip to the undefined gray area of the Timeline below currently existing

audio tracks in order to create a new track, the new track is set to a channel mapping that reflects the

number of channels of the audio clip you’re dragging.

This also means that if you’ve used Clip Attributes to map a clip’s audio to consist of multiple tracks

where each track has a different channel mapping, for example, one 5.1 track, one stereo track, and six

mono tracks, then editing that clip into the Timeline so that the audio portion creates new tracks will

automatically create eight tracks: one that’s 5.1, one that’s stereo, and six that are mono.

Not Creating New Tracks when

Adding Clips to a Timeline

There is a menu item in Edit > Edit Options called Automatically Create Tracks on Edit. This option is on

by default and preserves DaVinci Resolve’s default behavior of automatically adding new tracks to the

timeline if your source material has more audio tracks than your timeline does.

When disabled, you have the ability to drag source clips on to the timeline without the timeline

automatically creating new tracks for the additional audio or video elements. In situations where your

source camera files have more audio tracks than on your timeline, disabling this option will not create

additional new tracks and will only bring elements visible in the track destination controls.

This can be useful if, for example, you wanted to only bring a single mixed track in with a clip from a

multitrack recorder and exclude the independent microphone tracks.

Using Keyboard Shortcuts and

Three-Point Editing to Assemble a Program

While drag and drop editing is intuitive enough, there are other methods of editing clips into the

Timeline by using the playhead to define where those clips will start that can be more efficient and

precise. These examples all use “overwrite” edits, which delete unwanted media from the Timeline as

you’re adding clips that you do want. Here are two examples of how to do this.

Example: Assembling Clips Into the

Timeline From the Source Viewer

The following example shows how you can use the Edit page to assemble a quick first cut of edits

using different features of the Media Pool, Viewers, and Timeline. Written out with every possible

option, this may seem like a lot of steps, but once you learn these fundamentals and develop some

muscle memory for the keyboard shortcuts in use, these methods become really fast to do.


Edit | Chapter 36 Editing Basics

EDIT


Press Command-1 to open the Bin list, and use the Arrow keys to select a bin (Up and Down to

change the selection, Right and Left to open and close bins). Then press Command-2 to choose

the clip browser, and use the Arrow keys to select a specific clip.


Press the Return or Enter key to open the selected clip into the Source Viewer.


Drag the playhead with the pointer or use the Spacebar or JKL keys to move the playhead and set

In and Out points (I and O) to define the section of that clip you want to edit into your program.


By default, the destination controls are assigned to tracks V1 and A1. If necessary, choose different

video and audio tracks to edit the clip to in the Timeline by doing one of the following:

�Click the destination controls of the tracks you want to edit to. You can also drag them from

where they are now to where you want them to be.

�Use the Command-Option Up and Down Arrow (for audio) and Command-Shift Up and Down

Arrow (for video) shortcuts to move the destination controls up and down.

�Use the Option-1–8 (for video) and Command-Option-1–8 (for audio) key shortcuts to assign the

video and audio destination controls to specific tracks.


By default, all destination controls are enabled. If you want to edit clips into the Timeline as audio

or video only, you can do one of the following:

�Click any destination control itself to disable the video or audio component.

�Press Option-1–8 (for video) or Command-Option-1–8 (for audio) for the currently assigned

tracks to toggle the destination controls on those tracks on and off.

Setting the destination

control to the track

you want to edit into.


In the Timeline Viewer or the Timeline itself, use the pointer, Spacebar, or JKL controls to move the

Timeline playhead to the frame you want the beginning of the clip you’re about to edit to start. If

no In or Out points are set in the Timeline, the playhead position is used as the In point by default.


To perform an overwrite edit, do one of the following:

�Drag the clip from the Source Viewer to the Timeline Viewer and drop it on the Overwrite

overlay. If you’re in single viewer mode, this overlay only appears when you drag a clip from the

Media Pool to the Timeline Viewer.

�Click the Overwrite Clip button in the toolbar.

�Choose Edit > Overwrite (or press F10).

The selected clip(s) are overwritten to the selected track at the position of the playhead, and

the playhead automatically moves to the end of the newly edited clip, ready for you to perform

another edit. If that clip is the last one on the Timeline, you’ll see the last frame to the left of the

playhead (with a jagged overlay at the right-hand side of the Timeline Viewer) instead of the

black that is the actual frame after that clip. This makes it easier for you to line up the next edit.

Otherwise, the playhead will show whatever frame happens to be at that point in time.


Edit | Chapter 36 Editing Basics

EDIT

The Timeline playhead at the first frame after the clip you’ve just edited; the Timeline Viewer

shows a jagged overlay at the right to let you know this isn’t a real frame


To edit another clip, open the next clip you want to edit into the Source Viewer, set In and Out

points, and use the Overwrite Clip button or command to edit it into the Timeline. Continue this

process until you’ve edited together the assembly of edits you want.

Example: Assembling Clips Into

the Timeline From the Media Pool

If you want, you can also edit clips directly into the Timeline from the Media Pool using a variety of

commands. This can be a fast way of appending clips to the end of the Timeline (although you can also

perform insert edits this way).


Edit | Chapter 36 Editing Basics

EDIT

To edit one or more clips from the Media Pool to the Timeline:


Press Command-2 or click with the pointer to choose a clip in the Media Pool.


Set In and Out points for one or more clips in the Media Pool by doing one of the following:

�In Metadata view, drag the pointer over a clip’s thumbnail and use the I and O keys. If Live Media

Preview is enabled in the Source Viewer, dragging over a clip’s thumbnail mirrors the content in

the Source Viewer.

�In Thumbnail view, drag the pointer over a clip’s thumbnail and use the I and O keys. If Live

Media Preview is enabled in the Source Viewer, dragging over a clip’s thumbnail mirrors the

content in the Source Viewer.

�In List view, drag over the Media Pool Filmstrip Viewer and use the I and O keys. If Live Media

Preview is enabled in the Source Viewer, dragging over the filmstrip mirrors the content in the

Source Viewer.


Change the sort order of the Media Pool’s browser area to put the clips into the order in which you

want them to appear. In Thumbnail view you can use the Sort Order menu, but in List view you can

click the header of any metadata column to sort by that column’s data.


Click, drag, use the Command-Option and Command-Shift Up and Down Arrow Key shortcuts,

or use the Option-1–8 and Command-Option-1–8 key shortcuts to assign the video and audio

destination controls to the tracks you want to edit the video and audio of the incoming clip(s)

to. Click any destination control itself to disable it if you want to edit clips into the Timeline as

audio or video only.


Select one or more clips you want to edit. Insert, overwrite, place on top, ripple overwrite, and

append at end edits are all capable of editing multiple clips at once, while replace and fit to fill

edits can only edit one clip at a time, and will only edit the first of multiple selected clips into

the Timeline.


To perform the edit, do one of the following:

�Use any of the editing commands in the Edit menu.

�Use the equivalent keyboard shortcuts to Insert (F9), Overwrite (F10), Replace (F11), Place On Top

(F12), Ripple Overwrite (Shift-F10), Fit to Fill (Shift-F11), or Append To End of Timeline (Shift-F12)

the selected clips into the Timeline.

�Right-click one or more selected clips in the Media Pool, and choose “Insert Selected Clips to

Timeline” or “Append Selected Clips to Timeline.”

The selected clip(s) are edited into the Timeline.

Making Selections in the Timeline

Once you’ve assembled a sequence of clips in the Timeline, you’ll probably need to manipulate them

further, moving, deleting, trimming, or otherwise adjusting the clips in the Timeline to make the edit

play with the pacing and verve you require.

Manually Selecting Clips in the Timeline

Many operations require you to make a selection first, to define the scope of what you’re about to do.

There are many ways to do so.

Selections you can make using the mouse:

�To select one clip: Click a clip with the mouse.

�To select all clips under the playhead: You can select all the clips under the playhead at once,

regardless of how many tracks they are spread across by selecting Trim > Select All Clips Under

Playhead (Option-Shift-V).


Edit | Chapter 36 Editing Basics

EDIT

�To select a continuous range of clips by dragging: Drag a bounding box from an empty area of

the Timeline to surround a group of clips.

Dragging a bounding box to select a continuous range of clips in the Timeline

�To select a continuous range of clips by Shift-clicking: Click the first clip you want to select,

and then Shift-click the last clip you want to select, and all clips in-between will automatically be

selected as well.

�To select a discontinuous range of clips: Command-click any clips to select them no matter

where they appear on the Timeline. Command-clicking a selected clip deselects it.

Command-clicking to select a discontinuous range of clips in the Timeline

Selecting clips using the keyboard or menu commands:

�To select one clip: Using the keyboard, make sure the Auto Select button for the track the clip is

on is enabled, then move the playhead over that clip and press Shift-V.

�To select a clip using keyboard navigation: Holding down the Command key and pressing the

Up, Down, Left, and Right Arrow keys allows you to select clips above and below the current track

and to the left and right, independently of the playhead.

�To select all clips forward of the playhead on the current track: Move the playhead to the first

clip you want to include in the selection, then press the Y key (Timeline > Select Clips Forward >

On This Track) to select that clip and every clip to its right in the same track of the Timeline.

�To select all clips forward of the playhead on all tracks: Move the playhead to the first clip

you want to include in the selection, then press Option-Y (Timeline > Select Clips Forward >

On All Tracks) to select that clip and every clip to its right in all tracks of the Timeline.

�To select all clips backward from the playhead on the current track: Move the playhead to

the last clip you want to include in the selection, then press Command-Y (Timeline > Select

Clips Backward > On This Track) to select that clip and every clip to its left in the same track

of the Timeline.


Edit | Chapter 36 Editing Basics

EDIT

�To select all clips backward from the playhead on all tracks: Move the playhead to the last clip

you want to include in the selection, then choose Command-Option-Y (Timeline > Select Clips

Backward > On All Tracks) to select that clip and every clip to its left in all tracks of the Timeline.

�To select all clips in the Timeline: Make sure the Timeline has focus, then press Command-A.

To change which clip is selected using the keyboard:

�Select a clip, then use the Up Arrow and Down Arrow keys to change the selection to the previous

or next clip among all tracks with Auto Select turned on.

Selecting Clips Based on Markers, Flags, and Clip Color

It’s also possible to select multiple clips that have a particular color of marker, flag, or clip coloration.

This is useful in any situation where you’re using these organizational tools to keep track of clips with

specific characteristics that you might need to later select for multi-clip operations.

For example, you might add purple markers to a series of audio clips that might need special

EQ settings. Later, you can choose Timeline > Select Clips By Marker Color > Purple to select all of

those clips in order to move them to another track, where you can apply the same EQ to all of them

using an audio filter applied to the track. There are three ways of selecting groups of clips.

To select groups of clips based on marker, flag, or clip color:

�Choose Timeline > Select Clips By Flag Color > Blue – Cream

�Choose Timeline > Select Clips By Marker Color > Blue – Cream

�Choose Timeline > Select Clips By Clip Color > Orange – Chocolate