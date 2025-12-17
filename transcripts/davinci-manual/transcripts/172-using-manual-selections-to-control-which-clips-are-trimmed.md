---
title: "Using Manual Selections to Control Which Clips Are Trimmed"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 172
---

# Using Manual Selections to Control Which Clips Are Trimmed

It’s important to know that manual selections you make in the Timeline that highlight specific clips

always take precedence over whatever the Auto Select controls are set to. For example, if Auto Select

is turned on for tracks V1, V2, and V3, but you’ve selected a clip on track V1, only the selected clip will

be still be affected by whatever operation you decide to perform. For example, if you use Trim End, the

clip on track V1 will be affected.

Manual selection of a clip on track V1 overrides

the Auto Select controls on all tracks

Using Auto Select to Control Which Tracks Are Rippled

Each track’s Auto Select control is also used to control how trimming and editing operations that ripple

the Timeline affect timelines with multiple tracks and superimposed clips. Using Auto Select controls,

you can turn off rippling on specific tracks, while leaving it on for others.

For ease of use, you’ll typically want to leave Auto Select on for all tracks when rippling clips, to ensure

that all the parts of your timeline stay in sync with one another. However, when the occasion requires,

the Auto Select controls provide the option to suspend rippling on specific tracks while allowing

rippling on others.


Edit | Chapter 44 Trimming

EDIT

The rules are simple:

�Tracks with Auto Select enabled: Ripple editing or ripple deleting affects all clips to the right of

the clip or clips on that track being trimmed.

Before and After, clip to the right of Clip T on tracks V2, V1, A1, and A2 are

rippling because those tracks’ Auto Select controls are enabled

�Tracks with Auto Select disabled: Rippling is disabled on these tracks.

Before and After, clip to the right of Clip T on tracks V1 and A1 are rippling because those tracks’ Auto Select controls

are enabled, but clips on tracks V2 and A2 aren’t rippling because those tracks’ Auto Select controls are disabled


Edit | Chapter 44 Trimming

EDIT

Another set of rules govern what happens when you select clips or edits for trimming on tracks with

Auto Select disabled:

�Selected Tracks with Auto Select turned off with an edit selection: If you select the outgoing or

incoming half of an edit on a track that has Auto Select off, the result will be a resize operation.

Ripple deleting clips leaves a gap.

Before and After, clips to the right of Music Cue 03 on tracks V1, V2, A1, and A2 are rippling

because Auto Select is enabled on those tracks, but because the clip being trimmed on track

A3 has Auto Select disabled, it doesn’t ripple, instead resizing to open up a gap

Trimming Multiple Edits or Clips at Once

DaVinci Resolve lets you select multiple edit points or clips for certain trimming operations, making it

possible to trim multiple edits and clips at the same time. In simple cases, this makes it easy to resize,

ripple, slip, and slide several superimposed clips at the same time, which is a real convenience, or

you can select the In point of every title generator in a credit sequence at once in preparation for

shortening or lengthening them all at once. In more complicated cases, this lets you create more

complicated trimming scenarios, such as multi-track asymmetric trimming, to quickly take care of

difficult tasks.

No matter how ambitious a trim operation you want to set up, the procedure is exactly the same as for

an ordinary trim operation. Just make sure you follow these three general steps, and you’ll be good:


Choose Selection mode, and select the edit points or clips you want to trim. To make multiple

selections, click once to select the first item, then Command-click each subsequent item you

want to add to the selection. You can select as many clips and/or edit points on as many tracks

as you like.


To ripple, slip, or slide the entire selection at once, choose Trim mode. To resize or move each

selected item at once, continue using Selection mode.


Use the mouse, keyboard shortcuts, or timecode entry to execute the trimming operation, just as

you would if a single edit point or clip were selected.


Edit | Chapter 44 Trimming

EDIT

The following sections describe each of the special-case multi-selection trim operations that are

possible, along with each one’s special rules and limitations.

Resizing and Rolling Multiple Edit Points

You can resize or roll multiple edit selections at once. In this way, you can adjust the edit points of

multiple superimposed clips all together. Trimming multiple edit points essentially lets you “gang” them

so that all selected edits move together as one.

�To resize multiple clips at once, select the left (outgoing) or right (incoming) half of each edit point

you need to adjust, then use the Selection tool to drag those edit points to resize them all.

�To roll multiple clips at once, select every edit point you need to adjust right at the center, so

that both the incoming and outgoing halves of each edit point are selected, then use either the

Selection or Trim tools to drag those edit points to roll them all.

NOTE: You cannot combine ripple and roll operations at the same time.

Rippling Multiple Edit Points

It’s also possible to select multiple incoming or outgoing edit points on either superimposed video

tracks, or on the same video track, in order to ripple them all at once. A good example of when you’d

want to ripple multiple clips on the same track is if you’ve got an end credit sequence of 14 text

generators, and you’d like to shorten the entire sequence by a particular amount. This example can be

seen below.

When you ripple trim multiple edits on the same track, how many frames are trimmed in a particular

trim depends on what method you use to do your trimming.

�If you use use the Trim tool via dragging in the Timeline, then you can choose to ripple the entire

selection of edits by an arbitrary duration, for example, shortening or lengthening the entire

selection by eight frames. To do this, DaVinci Resolve performs your multi-selection trim operation

one edit at a time, removing a frame at a time from each selected edit from the left to the right

as you trim, until either you stop the operation, or every single selected edit has had a frame

removed, at which point DaVinci Resolve begins trimming the second frame from each selected

edit from the left to the right, and then the third, and so on, until you stop trimming. Working this

way, you can use the mouse to trim any number of clips to fit into any duration.

�You can also choose to ripple each selected edit by the same amount, for example removing

three frames from each of the selected edits, all at once. To do so, hold the Command key down

while dragging selected edits with the Trim tool, or use Dynamic JKL trimming, or trim by entering

relative timecode values, or use the nudge keys (Period and Comma).

To ripple trim multiple edits on the same track:


Click the Trim tool, and drag a bounding box in the Timeline to select all 14 edits.


Press the U key to select the incoming half of each selected edit.


Use whichever trimming method you prefer to ripple the sequence to be shorter or longer.

Dragging using the Trim tool lets you trim by an arbitrary number of frames, while holding the

Command key down while dragging with the Trim tool, using timecode entry to trim, using the

Comma and Period nudge keys, or using Dynamic JKL trimming lets you trim every selected edit

by the same number of frames.


Edit | Chapter 44 Trimming

EDIT

(Before) Selecting 14 incoming credits edit points, (After) Trimming them all at once

In the following example, the incoming edit of three clips in the following montage are selected

and simultaneously rippled using the Trim tool. Notice that each overlapping clip ripples along with

the nearest selected edit that’s to the left of it; this means that the superimposed clip in track V2

and the audio clip in track A4 ripples along with the third selected edit, while the audio clip in track

A2 ripples along with the second selected edit. Since the audio clip in track A3 starts to the left of

the first selected edit, it does not ripple.

Selecting three incoming edit points,

Trimming them all at once


Edit | Chapter 44 Trimming

EDIT