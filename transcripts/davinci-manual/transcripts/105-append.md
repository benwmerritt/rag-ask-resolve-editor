---
title: "Append"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 105
---

# Append

The position of the playhead is ignored; incoming clips are always placed after the last

clip in the Timeline.

Performing an Append edit

of clip DD to the Timeline

Ripple Overwrite

At its simplest, Ripple Overwrite substitutes a clip in the Timeline with an incoming clip. If you use

Ripple Overwrite on a clip on Track 1, this will automatically move all clips that are to the right of the

affected clip in the Timeline either forward to make room if the incoming clip is longer, or back to

eliminate gaps if the incoming clip is shorter.

Performing a Ripple Overwrite

to substitute an entire clip

at the playhead (BB) with

the incoming clip (DD)

However, Ripple Overwrite works differently if you’ve set In and Out points in the Timeline to define

a range. In this case, the incoming clip substitutes whatever portion of the Timeline falls within this

range, moving all other clips that are to the right of the affected range either forward to make room if

the incoming clip is longer, or back to eliminate gaps if the incoming clip is shorter.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Performing a Ripple

Overwrite to substitute a In/

Out range of the Timeline

(part of clips BB and CC)

with the incoming clip DD

Close Up

Lets you edit a clip into the Timeline as a zoomed-in close up, to make up for a lack of actual close ups

that would have been shot with either longer lenses or by moving the camera closer to the subject.

This function is particularly useful when you’re working with 4K media in a 1080 timeline, or 8K media

in a 4K timeline, which enables you zoom into existing wide shots to create medium shots, or medium

shots to create close up shots, with no loss of quality.

Performing this edit adds the incoming clip as an approximate 150% scaled close up, also performs a

face detection, and if a face or faces are found, automatically re-positions the face in the frame. Which

frame of the Timeline the incoming clip aligns with depends on the following:

�If no In or Out points are set on the Timeline, the incoming clip aligns with the Timeline playhead

as the In point.

�The incoming clip aligns with a timeline In point if one has been set.

�The incoming clip’s Out point will align with a timeline Out point if one has been set without an In

point. This “backtimes” the clip.

(Top) Before a Close Up edit,

(Bottom) After editing

clip DD into the Timeline

with a Close Up edit

Place On Top

Lets you edit the incoming clip as a superimposition above whatever other clips are in the Timeline;

the incoming clip is always placed on top, so if there are clips in tracks 1, 2, and 3, the incoming clip

is automatically placed on track 4, regardless of which track is selected. The frame the incoming clip

aligns with depends on the following:


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

�When the playhead is near an edit point (within five frames), the incoming clip aligns with the

closest timeline edit point in proximity to the playhead (as shown by the Smart Indicator) if no

timeline In or Out points have been defined.

�When the playhead is not near an edit point, the incoming clip aligns with the playhead if no

timeline In or Out points have been defined.

�The incoming clip aligns with a timeline In point if one has been set.

�The incoming clip’s Out point will align with a timeline Out point if one has been set without an

In point. This “backtimes” the clip.

(Top) Before placing a

clip on top, (Bottom) After

editing clip DD

into the timeline with

a Place On Top edit

Source Overwrite

This edit requires overlapping timecode in multiple clips to work properly, such as when recording

synced timecode to multiple cameras during a multi-cam shoot. If there is no overlapping timecode,

this edit does nothing.

If you are working with footage from multiple cameras that have synced timecode, then the easiest

way to use this edit type is to set In and Out points over a clip in the Timeline where you want to cut

away to another angle. In the following example, a wide shot of a cooking show covers the moment

when the chef starts slicing a chili.

Setting Timeline In and Out points to identify a cutaway

You can then select a clip in the Media Pool that corresponds to the desired angle you want to add as

a cutaway, that has synced timecode that overlaps with the clip in the Timeline. Don’t set In and Out

points; if necessary you can clear previously set In and Out points by pressing Option-X.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Choosing a Media Pool clip from another camera that has overlapping timecode

When you click the Source Overwrite button, a synced section of the selected Media Pool clip will be

edited into the Timeline between the In and Out points you placed, superimposed on top. The result is

a perfectly timed cutaway.

Using Source Overwrite to edit a superimposed and synced section of the

source clip into the Timeline between the In/Out points

Alternatively, you can also use Source Overwrite to automatically place a source clip with a marked In/

Out region on top of a clip in the Timeline so that its timecode syncs with the timecode of the timeline

clip, when you don’t know exactly how much of the incoming source clip you want to edit into the

Timeline, and you just want it synced appropriately.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Overwrite

While there’s no button available for performing an overwrite edit, you can use the F10 key to perform

an overwrite edit, which overwrites a section of the Timeline with the incoming clip, without moving

other clips in any way. The frame the incoming clip aligns with depends on the following:

�The incoming clip aligns with the playhead if no timeline In or Out points have been defined.

�The incoming clip aligns with a timeline In point if one has been set.

�The incoming clip’s Out point will align with a timeline Out point if one has been set without an

In point. This “backtimes” the clip.

(Top) Before, positioning the

playhead at the frame you

want to use as the In point for

the incoming clip, (Bottom)

After overwriting the end of

clip CC with incoming clip DD

Copy, Paste and Remove

Attributes from Timeline Clips

You can copy, paste, and remove attributes from clips in the Cut page timeline, similar to how the

Edit page operates. To do so, right-click on the clip in the timeline you want to get the attributes

from, and select copy. Then select the clip you want to modify on the timeline, right-click and select

Paste Attributes. A check box menu will appear, allowing you to select the specific attributes that you

want to paste.

You can cut, copy, and paste clip attributes from the Cut page

timeline, using the controls in the context menu.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT