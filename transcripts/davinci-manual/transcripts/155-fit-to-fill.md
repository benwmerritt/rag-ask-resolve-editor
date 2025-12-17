---
title: "Fit to Fill"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 155
---

# Fit to Fill

Fit to fill edits are the only edit type that actually use all four edit points, and it’s the only edit type that

retimes clips at the same time as they’re being edited. By setting In and Out points in the incoming

source clip, and another pair of In and Out points in the Timeline, you can stretch or compress the

timing of the specified range of source media to cover the entire specified range of the Timeline. In the

process, the speed ratio of the clip changes so the clip plays in either fast or slow motion.

Fit to fill edits are especially valuable when you have a source clip in which the action is slightly slow,

and you just want to speed it up by squeezing it into a shorter duration of the Timeline. They’re also

incredibly handy in situations when you have a gap in an edited sequence of clips to fill with a source

clip that’s just not long enough, but in which slightly slower motion won’t be noticeable.

Fit to fill edits do not ripple the Timeline.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

To use fit to fill to edit a clip into the Timeline:


Do one of the following to define where in the Timeline to edit the incoming clip:

a)	 You can set both In and Out points in the Timeline, to define the duration you want to fill with

the incoming source clip as a three-point edit.

b)	 You can clear the Timeline In and Out points (pressing Option-X), so that you can instead use

the duration of whichever clip or gap intersects the playhead on the track with the destination

controls assigned to them. In the following screenshot, the clip can easily be edited to take the

place of the gap by positioning the playhead anywhere within it.

Setting timeline In and Out points to mark a gap


Next, you’ll need to set both In and Out points in the Source Viewer to define a longer or shorter

source clip that you want to fill into the available space. In this example, we have a very short

section of the source clip defined that, because of the matching action in the Timeline, must be fit

into the larger gap seen above.

Setting In and Out points in a source clip to define a shorter duration

segment that you want to completely fill the gap


Click the audio and video destination controls of the tracks you want to edit the incoming source

clip onto. If necessary, create new tracks.


Choose Edit > Fit to Fill, drag any clip onto the Fit to Fill overlay in the Timeline Viewer,

or press Shift-F11.

The resulting edit; the shorter source clip is retimed to fit into the longer timeline gap

The incoming source clip is retimed, as necessary, to fit into the specified duration of the Timeline. This

can be seen by the retiming badge that appears within the clip that’s just been edited into the Timeline.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Place on Top

Place on top edits automatically superimpose clips onto the first empty track above (for video clips)

or below (for audio clips) any other clips in the Timeline that either intersect the playhead or fall in

between the currently set Timeline In and Out points, regardless of the current track specified by

the destination controls. It’s designed to make it easy to superimpose titles and other clips you want

to composite over another clip, or to add additional versions of clips such as VFX on top of previous

versions that you want to preserve.

Place on top edits create new timeline tracks if necessary, and do not ripple the Timeline.

To use place on top to edit a clip into the Timeline:


To choose where in the Timeline the clip will be “placed on top,” do one of the following:

Move the playhead to intersect the clip you want to edit the incoming source clip on top of.

Set In and Out points in the Timeline to define the duration within which you want to place the

incoming source on top.


Set In and Out points in a source clip that you want to edit.


Choose Edit > Place on Top, drag any clip onto the Place on Top overlay in the Timeline Viewer,

or press F12.

Before and after using place on top, the incoming text generator is superimposed

to a track above the clip at the position of the playhead

Incoming video clips will be edited to the topmost video track so they are above any previously

existing video in the Timeline. Incoming audio clips are edited to the bottom-most audio track so

they are below any previously existing audio. If necessary, new video and/or audio tracks will be

created automatically to hold the new incoming clip.

Ripple Overwrite

Ripple Overwrite is a four-point edit that’s useful when you can identify a segment of the Timeline

you want to overwrite, but the incoming clip is of a different duration and you want DaVinci Resolve to

automatically ripple the Timeline to accommodate the difference.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

You can use the Ripple Overwrite command one of two different ways:

�You can overwrite an entire clip in the Timeline with another clip of different length.

�You can overwrite a section of the Timeline marked with In and Out points with a another clip of

different length.

In both cases, all clips to the right of the clip or timeline section being overwritten are rippled to the

right or left to make room or fill the gap. Because of this, the ripple overwrite edit will most likely

change the overall duration of your edited sequence of clips.

Using Ripple Overwrite on an Entire Clip in the Timeline

Using ripple overwrite as an automatic four-point edit, you can overwrite whichever clip in the Timeline

intersects the playhead on the tracks defined by the destination controls, in its entirety, with the

incoming clip. For this to work, there must be no In or Out points set in the Timeline.

After performing a ripple overwrite in this way, the original timeline clip is eliminated and the incoming

clip takes its place, and all clips to the right of the clip being replaced are either (a) rippled to the right if

the incoming clip is longer than the original timeline clip, or (b) rippled to the left if the incoming clip is

shorter than the original timeline clip. All of this is done in a single step.

This is useful in situations where you want to quickly switch one clip in the Timeline with another of

unequal duration and have the Timeline automatically make room to allow this all in one step.

To use ripple overwrite to replace an entire clip in the Timeline with another source clip:


Move the playhead in the Timeline to intersect the clip that you want to replace; the playhead’s

exact position is not important.


Click the appropriate audio and video destination controls of the track containing the clip you want

to replace, and press Option-X to eliminate any In and Out points there might be in the Timeline.


Open a clip into the Source Viewer, and set In and/or Out points as necessary to define how much

of the clip you want to edit into the Timeline.


To execute the edit, choose Edit > Ripple Overwrite, drag the clip to the Ripple Overwrite overlay

of the Timeline Viewer, or press Shift-F10.

Before and after of using ripple overwrite with no Timeline In or Out points; Clip K at the

position of the playhead is replaced in its entirety by the short segment of Clip U from the

Source Viewer; all clips with In points to the right are rippled to the left to fill the gap


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT

Using Ripple Overwrite on a Section of the Timeline Defined by In/Out Points

You can also use ripple overwrite as an explicit four-point edit, to overwrite a section of the Timeline

that’s marked with In and Out points with an incoming clip that’s also marked with In and Out points

that is of unequal duration.

After performing a ripple overwrite in this way, the section of the Timeline marked with In and

Out points is eliminated and the incoming clip takes its place, and all clips to the right of the clip being

replaced are either (a) rippled to the right if the incoming clip is longer than the original timeline clip,

or (b) rippled to the left if the incoming clip is shorter than the original timeline clip. All of this is done in

a single step.

A good example of when this can be useful is when you’re cutting a close-up of an actor performing

a particular action into a medium shot of the actor performing the same action that’s already in the

Timeline, and the action you’re matching is of different durations in each of the shots.

To use ripple overwrite to replace a section of the Timeline with another source clip:


Set In and Out points in the Timeline to mark what part of the clip or clips you want to overwrite.

You must set both In and Out points for this to work as expected. In this example, the part of the

clip where the woman leans forward is marked.

Setting In and Out points to identify an action in the Timeline that you want

to overwrite with another clip that has a matching action


Open a clip into the Source Viewer, and set In and/or Out points as necessary to define how much

of the clip you want to edit into the Timeline. In this example, a section of the woman’s close up

where she leans forward in a way that matches the same movement in the wider shot is marked.

Setting In and Out points to identify an action in a source clip that you want to

overwrite the action you’ve marked in the Timeline. It’s a matching action, but

the timing might be different, and that’s okay with this kind of edit.


Edit | Chapter 39 Three- and Four‑Point Editing

EDIT


To execute the edit, choose Edit > Ripple Overwrite, drag the clip to the Ripple Overwrite overlay

of the Timeline Viewer, or press Shift-F10. As a result, the section of the timeline that was marked

in step 1 is overwritten by the section of the source clip marked in step 2, and all clips to the right

of this edit in the Timeline are rippled to the right to make room for the much longer source clip.

The final result is an edit where the movements match nicely.

After the ripple overwrite, the part of the Timeline clip marked with In and Out points has

been overwritten by the part of the Source clip marked with In and Out points, and all

clips to the right of this edit in the Timeline are rippled left or right as necessary