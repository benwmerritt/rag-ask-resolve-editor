---
title: "Asymmetric Trimming"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 173
---

# Asymmetric Trimming

Asymmetric resize or ripple trimming can also be done to multiple clips, with one selection per track

allowable on as many tracks as you require. To asymmetrically trim two or more clips, select an

outgoing edit point on one track, and then Command-click an incoming edit on another track.

Selecting opposite outgoing video and incoming audio edit points

in preparation for performing an asymmetric ripple trim

To select the outgoing video edit of one clips and the incoming audio edit of the next clip in

preparation for making a split edit, you can Option-click the outgoing video edit to suspend linked

selection, and then Command-click the incoming audio edit to add it individually to the selection.

Now when you drag, nudge, or use timecode to trim, each selected edit point will move in the

opposite direction.

Dragging to perform an asymmetric ripple trim to create a split edit using the Trim tool

DaVinci Resolve allows you to do asymmetric trims to multiple edits in the same video and/or

audio track. There are two compelling reasons for doing so:

Select the outgoing half of an edit point (the left side), then Command-click to select the incoming half

of the same edit point (the right side) separately. This will not perform a roll edit, but will allow you to

either use the Selection tool to resize both edit points away from each other to create a gap, or use

the Trim tool to ripple both sides of the edit to shorten both clips while tightening up the Timeline at

the same time.


Edit | Chapter 44 Trimming

EDIT

Before and After ripple trimming both the incoming and outgoing halves

of an edit to shorten the duration of both clips at once

You can also select the In and Out points of a clip in the Timeline at the same time, and use the

Trim tool to ripple both the beginning and end of the clip closer to the center, shortening the clip

while preserving the content in the middle, while tightening up the Timeline.

Before and After ripple trimming both the In and Out points of a clip at the same time, shortening

the clip by removing heads and tails, and preserving the action in the middle


Edit | Chapter 44 Trimming

EDIT

In short, you can use nearly any combination of edit selections you need to simultaneously

trim multiple clips in the same track, in multiple tracks, whatever you need to do to save time.

Furthermore, asymmetric trimming can be done in either Selection or Trim mode, either to open

and close gaps, or to move edit points to overlap one another to create split edits.

Slipping Multiple Clips

You can simultaneously slip any number of selected clips (so long as they have handles) on any

combination of tracks by selecting the clips you want to slip, then choosing the Trim tool, and dragging

their name bars or using the Comma and Period keys to nudge the selection.

Dragging to slip multiple selected clips at once

Sliding Multiple Clips

You can select as many clips as you like in preparation for a slide operation. If you select multiple

contiguous clips, they slide together as one.

(Before) Selecting four clips to slide, (After) All four clips slid to the right using the mouse


Edit | Chapter 44 Trimming

EDIT

Keyboard Trimming

During Looped Playback

A great technique for editors who like to do precision trimming using the Nudge commands is

the ability to enable looped-playback so that the Play Around command (Forward Slash) will loop

continuously around the edit point you’re trimming as you nudge one or five frames at a time to fine-

tune the cut.

To trim while looping:


Move the playhead near the edit point you want to trim, and press V to select it.


Press the U to choose which side of the edit you want to select in order to ripple or roll it, and/or

Option-U to choose whether you want to trim video+audio, the video only, or the audio only.


Press Command-Forward Slash (/) to enable looped playback.


Press Forward Slash (/) to play around the current selection. With looping on, playback

will continue until you stop it. Pre-roll and post-roll can be changed in the Edit panel of the

User Preferences.


During looped playback, press the Comma (,) and Period (.) keys to trim the selection back or

forward by a single frame, or Shift-Comma and Shift-Period to trim the selection in 5-frame

increments. If you do this during the post-roll of looped playback, the loop immediately replays

from the beginning so you waste no time seeing the result.


When you’re finished, press the Spacebar or K key to stop playback.

TIP: When holding down the Shift key while nudging to do a “fast nudge,” the duration of the

nudge is customizable in the Editing panel of the User Preferences. By default it’s five frames,

but you can set it to whatever you want.

Dynamic JKL Trimming

One of DaVinci Resolve’s most interactive trimming features is the ability to dynamically resize,

ripple, roll, slip, slide, or move selected edit points and clips using the JKL transport control keyboard

shortcuts. This means that you can make an appropriate selection in the Timeline (edit points to resize,

ripple, or roll, or clips to slip or slide) then trim them during playback, while monitoring audio and

watching the video.

Trimming while viewing the selected clip or edit point playing back has the advantage of letting you

get emotionally involved in what you’re watching, as well as experiencing the timing of a clip as it

plays, in order to help you get a better feel for how, exactly, you need to trim a particular cut.

While you’re dynamically trimming, you see the same two-up or four-up display, the same Timeline

overlays, and the same dynamically updating Timeline that appear when you use the Trim tool with the

mouse. The only difference is that you’re trimming while your program plays.


Edit | Chapter 44 Trimming

EDIT

There are two methods of doing dynamic trimming:

�Quick Trim: You can select one or more edit points or clips, and immediately trim it by pressing

Command-J or Command-L to trim back or trim forward. This is a fast way of dynamically trimming,

but you can only trim forward and backward at 100 percent speed or greater.

�Turning on Dynamic mode: If you want to do more detailed work, you can press the W key

to enable Dynamic mode (or choose Trim > Dynamic Trim Mode), at which point you are in a

special mode where the JKL shortcuts only trim the current selection, whatever it happens to be.

However, this mode also gives you additional options for controlling which part of the selection, in

the case of multiple selection trims, you want to monitor for audio/video playback.

TIP: If nothing is selected while you’re in Dynamic Trim mode, JKL simply plays through the

Timeline, as usual.

Quick Trimming

If you’re in a hurry and you can accomplish the trim you want via real time or faster playback, then

pressing the Command key while using the J or L keyboard shortcuts lets you dynamically trim any

selection in the Timeline, with audio/video playback.

To dynamically trim using Command-J or Command-L:

�To dynamically roll an edit: In either Selection or Trim mode, select the center of one or more

edit points, and hold the Command key down while using J or L to move the selection around.

�To dynamically ripple an edit: Choose Trim mode, select the outgoing or incoming half of

one or more edit points, and hold the Command key down while using J or L to move the

selection around.

�To dynamically resize an edit: Choose Selection mode, select the outgoing or incoming half

of one or more edit points, and hold the Command key down while using J or L to move the

selection around.

�To dynamically move a clip: Choose Selection mode, select one or more clips, and hold the

Command key down while using J or L to move the selection around.

�To dynamically slip or slide a clip: Choose Trim mode, select one or more clips to slip, or a single

clip to slide, press S to toggle between Slip or Slide modes, then hold the Command key down

while using J or L to execute either slip or slide operations.

If you’re trimming multiple selections, you can control which edit point you monitor during the trim

operation by positioning the playhead at one of the selected edit points.

TIP: When you’re finished with a “quick trim” operation and you want to see how that edit

plays, you can press the Forward Slash key (/) to play around the current selection to quickly

preview that section of the Timeline.


Edit | Chapter 44 Trimming

EDIT