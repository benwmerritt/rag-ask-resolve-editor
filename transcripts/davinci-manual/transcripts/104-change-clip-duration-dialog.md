---
title: "Change Clip Duration Dialog"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 104
---

# Change Clip Duration Dialog

The Change Clip Duration dialog allows you to directly change the duration of a clip by typing in

frames, a timecode value, or using time and frame-based presets. You can activate the Change Clip

Duration dialog by selecting one or more clips on the Timeline and choosing Clip > Change Clip

Duration (Command-D), or by right-clicking on a clip and choosing Change Clip Duration from the

contextual menu. The Change Clip Duration dialog works both on the Cut and Edit pages.

The new Change Clip Duration box in Timecode mode.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Options for the Change Clip Duration Dialog box:

�Format: You can chose between working with Time (Timecode) or Frame values.

�Duration: Type in the timecode value or number of frames you wish to make the new duration of

the selected clip.

�Preset: Select a duration by clicking on 1, 5, or 15 seconds (or their equivalent value in frames). End

will extend the duration to the last frame of the selected clip, regardless of any Out points set.

�Extend Beyond Clip Length (Cut page only): This will append black filler to any clip whose

duration is set longer than the clip itself.

�Cancel/Change: Click Cancel to to exit without changing the duration of the clip, or Change to

apply the duration change to the selected clip.

TIP: You can change the duration for more than one clip at a time by selecting multiple clips

before opening Change Clip Duration. All clips selected will be the changed to the same

duration set in the Change Clip Duration dialog box.

Video Only and Audio Only Edits

Normally, any edit function in the Cut page uses both the Audio and Video sections of a clip to insert

into the Timeline. However, there are several scenarios where you would only want either the Audio or

the Video portions to be used instead.

To perform an Audio Only edit:

Select the Audio Only icon to the left of the Upper Timeline, deselect to return to the normal

audio and video edit.

To perform a Video Only edit:

Select the Video Only icon to the left of the Upper Timeline, deselect to return to the normal

audio and video edit.

(Left) The Audio Only icon, (Right) The Video Only icon


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Drag and Drop Editing

Drag and drop editing can be an easy way of assembling clips into a loose edit. Once you’ve defined

a range of media using the Source Clip or the Source Tape, you can click and drag either from the

Viewer or the Media Pool to the Upper Timeline or the Timeline below to edit a clip into your program.

How and where you drag determines how that clip will be edited.

Append

If you drag a clip onto an empty timeline, or to the dark gray area to the left of clips in the Timeline,

that clip will become the first clip of your edit. If you drag a clip to the far left or right edge of all other

clips in the upper or lower areas of the Timeline, you will append that clip to the ending or beginning of

the Timeline.

(Top) Dragging a clip

to the far right of the

Timeline to append it,

(Bottom) The appended clip

Ripple Overwrite

If you drag a clip onto a pre-existing clip in either the Timeline or Upper Timeline so that the entire clip

highlights and you drop it immediately, you’ll perform a Ripple Overwrite edit, substituting the previous

clip in the Timeline with the new clip. If you’ve ripple overwritten a clip on Track 1, all clips to the right

of it will be rippled to make room if the incoming clip is longer, or close the gap if the incoming clip

is shorter.

(Top) Dragging clip DD onto

clip BB on the Timeline to

Ripple Overwrite clip BB,

(Bottom) Clip DD is shorter

than clip BB, so the

Timeline becomes shorter

once the edit is done


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Overwrite

If you drag a clip onto a pre-existing clip in either the Timeline or Upper Timeline and wait a moment,

the Timeline overlay changes from a highlight over the whole clip to a highlight showing just the

portion of the incoming clip overlaid on the existing clip. When you drop the clip, you’ll perform

an Overwrite edit, which writes over the media that’s already in the Timeline with the media of the

incoming clip. Overwrite edits don’t ripple the Timeline.

(Top) Dragging clip DD

onto clip BB on the

Timeline and pausing to

perform an Overwrite,

(Bottom) Clip DD overwrites

the middle of clip BB,

breaking it into two pieces

while the Timeline remains

the same duration

Using Cut Page Edit Commands

At the bottom of the Media Pool is a set of five buttons that let you make other kinds of edits. Some of

these edits have keyboard shortcuts assigned to them and are also available via dedicated keys on

the DaVinci Resolve Editor Keyboard.

Smart Indicator showing

where an edit will occur

The edit buttons underneath the Media Pool, (Left to Right) Smart Insert,

Append, Ripple Overwrite, Close Up, Place On Top, Source Overwrite

Smart Indicators

Some of the intelligent tools in the Cut page do not require you to select specific In and Out points

in the Timeline; they rely on the playhead’s relative position over a clip to guess where you likely will

want to make your edit. The point where DaVinci Resolve intends to make that edit is marked using a

Smart Indicator icon on the Timeline Ruler. To make the edit points easier to identify on the Timeline,


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

after a few seconds, the Smart Indicator will move up and down on the Timeline ruler, while the actual

edit point will strobe green (red if the clip has reached its start or end frame).

Setting Up and Performing Edits

No matter what kind of edit you intend to make, the process of setting them up and performing them is

the same. This section describes the general process of setting up an edit, and the following sections

will describe how each particular edit works.

To set up and perform an edit:


First, locate a clip you want to edit into the Timeline. There are two general ways of doing this:

a)	 Open a bin with clips you want to use, then click the Source Tape in the Viewer to show a

stringout of all clips in the current bin, and its subfolders, in the currently selected sort order.

Now, you can scrub around all these clips using JKL or the DaVinci Speed Editor’s shuttle/jog/

scroll wheel to find the media you’re looking for.

b)	 Open a bin with clips you want to use, and navigate the thumbnails, filmstrips, or columns

to select the clip you want, using the Search field if necessary to help find the clip you’re

looking for.


Scrub a thumbnail or filmstrip, or use the controls in the Viewer, or use the controls of your DaVinci

Speed Editor to locate frames at which you want to set In and Out points to define an edit range,

and use the I (In) and O (Out) keys to set those points.


If necessary, choose which video track you want to edit to by clicking in its track header to select

it. Selected tracks are highlighted.


Perform an edit to put the selected range of the source clip into the selected video track at the

desired frame, using either the buttons at the bottom of the Media Pool, or keyboard shortcuts.

Different edit commands will put the source clip into different locations.


After you’ve committed your edit, you can press Q (or click the Timeline Viewer button) to switch

the Viewer to the Timeline to play and review the edit you’ve just made, and then press Q again

to switch back to the Source Clip or Source Tape (whichever was last used) to locate the next clip

you want to edit, starting all over again at Step 1.

Smart Insert

Automatically inserts an incoming clip at the closest edit point to the playhead (as shown by the Smart

Indicator) on the selected track, pushing all clips to the right of the edit point forward to make room

for the incoming clip if you’ve inserted to Track 1. Because this is a smart operation, you are prevented

from inserting a clip at any arbitrary frame; incoming clips are only inserted at the closest previously

existing edit point.

(Top) Before doing

a Smart Insert,

(Bottom) After inserting clip

DD between clips AA and BB


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT