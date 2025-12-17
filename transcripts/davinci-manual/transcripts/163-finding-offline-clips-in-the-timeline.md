---
title: "Finding Offline Clips in the Timeline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 163
---

# Finding Offline Clips in the Timeline

It’s also easy to use the Edit Index to find all of the offline clips that may be in the Timeline.

To locate offline media in the current Timeline via the Edit Index:


Open the Edit Index.


Click the Option menu of the Edit Index and choose Show Offline Clips Only.


The Edit Index is filtered to only show the offline clips in the currently open Timeline, and you can

click any item on the list to jump the playhead to that particular clip in the Timeline.


Click any event in the Edit Index to move the playhead to that clip in the Timeline.

Finding Edit Index Events Using Clips in the Timeline

You can also locate specific Edit Index events using the Timeline playhead.

To locate a clip in the Edit Index from the Timeline:

�Move the Timeline playhead to intersect a clip you want to find in the Edit Index. That clip’s

corresponding event (or events if the playhead intersects multiple clips) are automatically

highlighted in the Edit Index.

�To move the playhead to a clip in the Timeline via the Edit Index.

�Click any event in the Edit Index to move the Timeline playhead to the In point of that clip.

Finding Clips

As you work, there are a variety of methods you can use to find clips in the Media Pool or your

file system.

Methods of finding clips in the Media Pool or File System:

�To find a clip in the Media Pool: Open the Media Pool, and use the drop-down menu next to the

Search button to choose whether to search through all bins in the current project, or just look at

the currently selected bin or bins in the Bin List. If necessary, select the bin or bins that you want

to search, and click the magnifying glass button to open the search controls. Optionally choose a

criteria from the Filter By drop-down menu, then type a search term in the Search field. As soon as

you start typing, all clips that don’t match the search criteria are temporarily hidden.

�To locate a Timeline clip in the Media Pool: Right-click any clip in the Timeline, and choose

Find in Media Pool. That clip appears highlighted in the Media Pool.

�To locate a Source Viewer clip in the Media Pool: With any clip open in the Source Viewer,

press Option-F.

�To locate a media file in the Finder from the Media Pool: Right-click any clip in the Media Pool

and choose Reveal in Finder. A Finder window, or its equivalent in Windows and Linux, opens to

the directory with that clip, which appears highlighted.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

�Reveal Media Pool Bin from Multi-Bin or Search Displays: If you’ve searched for a clip and have

results across multiple bins, you can now reveal where that clip is in the Media Pool by right-

clicking on the clip and selecting Reveal Media Pool Bin from the contextual menu.

�To find the audio clip that a video clip has been synced to: Right-click a video clip that’s been

synced to audio, and choose “Reveal synced audio in Media Pool” from the contextual menu. The

bin holding the synced audio clip is opened and that clip is selected.

Finding Clips Using Markers or Flags

If you’re using markers to keep track of notes, issues, or items on your to-do list, there are a few

different ways of finding and moving among them.

Methods of finding markers or flags:

�To find all markers or flags via the Edit Index: Click the Option menu of the Edit Index and choose

Show Markers or Show Flags. Each clip with one or more markers appears in a list, with columns

corresponding to the color(s) and notes of each timeline and clip marker.

�To find a specific marker or flag in the Edit Index: Click the magnifying glass button in the Edit

Index, choose Notes in the Filter by drop-down, and type a search term in the Search field.

�To move the playhead to the next marker forward or previous: Choose Playback > Previous

Marker (Shift-Up Arrow) or Next Marker (Shift-Down Arrow).

Finding Gaps

Gaps, or spaces between two clips on the Timeline, appear by default as black. Unwanted gaps may

appear as black flashes while your program plays back, and are generally to be avoided. DaVinci

Resolve makes it easy to find gaps in specific tracks of your timeline.

To find gaps in the Timeline:


Make sure that the Auto Select control is enabled on any track you want to search for gaps. Turn

Autoselect off on any tracks you don’t want to search for gaps (for example, title tracks where gaps

are to be expected).


Do one of the following:

�Choose Playback > Previous Gap or press Option-Command-Semicolon.

�Choose Playback > Next Gap or press Option-Command-Apostrophe.

The playhead will automatically move to the first frame of the next gap in the Timeline.

To delete gaps in the Timeline:


Make sure that the Auto Select control is enabled on any track you want to delete gaps.

Turn Autoselect off on any tracks you don’t want to delete gaps (for example, title tracks where

gaps are to be expected).


Choose Edit > Delete Gaps. If you want to limit the range of the deleted gaps this command

respects both In/Out ranges and clip selections on the Timeline.

Finding the Currently Open Timeline in the Media Pool

If you’re not using one of the available methods for organizing timelines separately from clips, it can

be easy to lose track of where your timeline happens to be. To find the currently open Timeline in the

Media Pool, choose Timeline > Find Current Timeline in Media Pool.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

Finding Media Using Match

Frame Operations

Match frame operations are a terrific time saver when you need to match the original source clip to a

clip in the Timeline, or when you want to use a clip in the Source Viewer to find that same clip in the

Timeline. With a single command, you can match one clip to another in order to set up a new edit to

take care of a variety of tasks.

Matching From the Timeline

A classic example of using Match Frame is when you originally edited a video clip into the Timeline

without its corresponding audio, and you later decide you want that audio in the Timeline after all.

An easy fix is to move the playhead in the Timeline to intersect the clip you need to fix, and use the

Match Frame command to automatically load the original source media for that clip into the Source

Viewer, setting Source In and Out points that match those of the Timeline clip, and putting the Source

playhead at the same frame as the Timeline playhead. At that point, you can simply edit the source

audio and video back into the Timeline to overwrite the video-only clip you started with, confident that

you’re editing exactly the same range of media at the same place.

Using the pointer to Match Frame from the Timeline to find a source clip:

Hold the Option key down and double-click the clip in the Timeline.

The original source media for that clip is automatically loaded into the Source Viewer, with In

and Out points that match those of the targeted Timeline clip; the Source playhead is at the

same frame as the Timeline playhead.

Using keyboard shortcuts or Viewer controls to Match Frame

from the Timeline to find a source clip:


Move the Timeline playhead to intersect the clip you want to target.

Placing the playhead over a clip to Match Frame


If there are other clips on a multi-track timeline that overlap the clip you’re targeting for this

operation, then the clip on the highest video track will be used as the target for Match Frame

operations. If you want to target a clip on a lower track, you can click on the specific clip under

the playhead to highlight it. Alternatively you can disable the Auto Selection controls of all

timelines above, or Option-click the Auto Selection control of the track with the clip you’re

targeting to solo it.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT


Press the F key, or click the Match Frame button at the bottom right of the Timeline Viewer (it’s at

the left of the In and Out buttons).

The frame that’s matched to the frame at the playhead in the Timeline;

In and Out points are set to match those of the clip in the Timeline

The original source media for that clip is automatically loaded into the Source Viewer, with In and Out

points that match those of the targeted Timeline clip; the Source playhead is at the same frame as the

Timeline playhead.

Matching From a Source Clip

Match Frame also works in the opposite direction. You can open a source clip into the Source

Viewer that you know corresponds to a clip in the Timeline, and then you can use Match Frame to

automatically find any clip in the Timeline that corresponds to media found within the source clip.

To use Match Frame in the Source Viewer to find a clip in the Timeline:


Open a clip in the Source Viewer that includes a range of media that’s already been edited into

the Timeline. If no part of the source clip has been edited into the Timeline, source match framing

won’t work.


Move the Source Viewer playhead to a frame that you want to find in the Timeline. Again, if the

frame at the position of the playhead in the Source Viewer hasn’t already been edited into the

Timeline, the Source Match Frame command won’t work.


Click the Match Frame button at the bottom right of the Source Viewer (it’s at the left of the In and

Out buttons), or press the F key.

The Timeline playhead automatically moves to the clip and frame after the current playhead position

that matches the clip in the Source Viewer.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT

Finding a Clip in the Media Pool

Using a Timeline Clip

There are two ways you can use a clip in the Timeline to find a clip in the Media Pool.

Using a Clip in the Source Viewer to Find a Media Pool Clip

To locate the original clip in the Media Pool that corresponds to a clip in the Timeline:


Open a Timeline clip into the Source Viewer by doing one of the following:

�Double-click a clip in the Timeline.

�Move the playhead to a clip in the Timeline, press Shift-V to select it, then press the Return key.


Press Option-F to locate the source clip corresponding to the clip that’s open in the Source Viewer

in the Media Pool. That clip appears highlighted in the Media Pool.

Using a Clip in the Timeline to Find a Media Pool Clip

To locate a Timeline clip’s corresponding clip in the Media Pool, right-click any clip in the Timeline, and

choose Find in Media Pool from the contextual menu. That clip appears highlighted in the Media Pool.

Tracking Media Usage

As clips are added to timelines, two mechanisms come into play for keeping track of which clips are

used in which timelines.

Thumbnail Clip Usage Indicators

Whenever you open a timeline, all thumbnails in the Media Pool automatically update to show

highlighted usage bars to let you know which parts of that clip are used in that timeline.

Two colored highlights at the bottom of the

thumbnail indicate which parts of a clip are

used by the currently open Timeline

If you right-click on a thumbnail that shows usage, a Usage submenu shows you a list of each instance

of that clip in the currently open Timeline. Choosing an instance from this list jumps the playhead to

that clip in the Timeline.


Edit | Chapter 41 Marking and Finding Clips in the Timeline

EDIT