---
title: "Individual Destination Controls with Decompose on Edit"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 168
---

# Individual Destination Controls with Decompose on Edit

In Edit > Edit Options, when the setting to Decompose Compound Clips on Edit is enabled, compound

clips and timelines either selected in the Media Pool or loaded in the Source Viewer have support for

track destination controls from the underlying clip.

This means that if a timeline with three video tracks and two audio tracks is loaded into the

Source Viewer, the timeline track destination controls will show three available video tracks

and two available audio tracks for track destination patching.

With Edit > Edit Options > Decompose Compound Clips on

Edit enabled, the resulting tracks available for track destina-

tion tracking


Edit | Chapter 43 Take Selectors, Compound Clips, and Nested Timelines

EDIT

Compositing With and Grading Compound Clips

Since compound clips act like a single clip in the Timeline, they appear as a single MediaIn node in

the Fusion page, and you can grade them as a single clip in the Color page. However, if you want

to individually apply effects, adjust the RAW camera settings, or grade the original clips inside the

compound clip, you can use the Open in Timeline command to access its constituent clips, and then

open the Fusion or Color pages, where you’ll find each of the individual clips available for separate

compositing or grading. When you’re done, go back to the Edit page and close the compound clip,

and you’ll go back to seeing it as a single clip whenever you open the Fusion and Color pages.

Nested Timelines

Timelines, and sections of timelines, can be edited inside other timelines, either partially or whole.

For example, if you’ve edited a program in scenes or reels such that each reel is contained in a

separate timeline, you can edit all of the timelines together, one after the other, into a single timeline to

assemble them into a final program.

Multiple timelines edited together into a single sequence

Nested timeline clips appear with a special badge to the left of the timeline name.

The badge that indicates a nested timeline

Timelines can be edited like any other clip, you can select one or more timelines and drag and

drop them into another timeline, drag them onto the Timeline Viewer editing overlay, or use

the toolbar editing buttons or keyboard shortcuts to edit them, just as you would any other clip.

Additionally, you can select multiple timelines in the Media Pool, right-click them, and

choose Create Timeline Using Selected Clips to quickly assemble a group of timelines into a

nested sequence.

The one exception is that you must drag and drop a timeline into the Viewer if you want to use

it to set In and Out points, since double-clicking a timeline, or selecting a timeline and pressing

Return simply opens it into the Timeline Editor. However, you can set In and Out points for

timelines in the Filmstrip of the Media Pool, or you can edit a timeline into another timeline

in its entirety, and then trim the head and tail down to just what you need. Double-clicking a

nested timeline opens it into the Source Viewer for trimming, exactly like any other clip.


Edit | Chapter 43 Take Selectors, Compound Clips, and Nested Timelines

EDIT

Re-Editing a Nested Timeline

If you want to edit the contents of a nested timeline, you can right-click it and choose Open in

Timeline. Unlike compound clips, no path control appears when you do this, because you’ve simply

opened the original timeline. To go back to the previous timeline, find and double-click it in the Media

Pool, or choose it from the Timeline drop-down at the top of the Timeline Viewer.

Editing an original timeline does nothing to change the duration of nested instances of that timeline

inside other timelines. If you trim or delete clips in the original timeline that appear in nested instances

of that timeline, then those areas of the nested timeline simply go black.

Swapping the Contents of the Source Viewer and Timeline

When editing the partial contents of one timeline into another, it can be useful to see the contents of

a timeline that’s open in the Source Viewer in the Timeline Editor. To do so, choose Timeline > Swap

Timeline and Source Viewer (Command-Page Up). This puts the timeline that was open in the Source

Viewer into the Timeline Editor, and the timeline that was in the Timeline Editor into the Source Viewer.

This makes it easier to mark In and Out points while seeing the exact boundaries of clips, prior to

pressing Command-Page Up to swap the contents of the Source Viewer and Timeline Editor once

again in preparation for executing the next edit.

Editing Source Media From a Timeline or Compound Clip

If you have a timeline that has clips you want to edit into another timeline, but as source clips and not

as nested timeline segments, you can turn on Edit > Decompose Compound Clips on Edit.

This a mode determines whether a timeline is edited into another timeline as a nested timeline, or

immediately decomposed into its constituent source clips. Turning this mode on lets you edit source

clips from a timeline using drag and drop, 3-point edits, or whatever other method you find convenient.

To go back to editing nested timelines, turn Edit > Decompose Compound Clips on Edit off.

This mode is especially useful for workflows where you’re assembling “selects” timelines with the best

moments of various interviews or performances, which you later want to edit as sources into the actual

program you’re editing.

Marking Clips in Timelines Loaded into the Source Viewer

While you’re editing Source Media from a timeline that’s loaded into the Source Viewer, you can use

the Mark Clip (the X key) to set Viewer In and Out points that match the start and end of whatever clip

intersects the playhead within that timeline. This makes it easy to edit one clip from a Timeline in the

Viewer into your program, all by itself.

(Left) A timeline in the Source Viewer, (Right) Pressing X marks In

and Out points for the clip at the playhead, ready for editing

Decomposing Nested Timelines

There are two main ways you can turn a nested timeline back into its constituent clips.


Edit | Chapter 43 Take Selectors, Compound Clips, and Nested Timelines

EDIT

Decomposing in Place

To decompose a nested timeline that’s already been edited into another timeline, right-click it and

choose Decompose in Place. You can also do this for multiple selected nested timelines, all at once.

(Top) A nested timeline, (Bottom) The result of using Decompose In Place

If the decomposed clip has more audio, video, or subtitle tracks as a result, then additional tracks will

be added to the Timeline to make room. If this is a problem, you can rearrange the clips

Decomposing Nested Timelines While Editing

If you want to edit an entire timeline into another timeline solely as the source clips, you can turn

on Edit > Decompose Compound Clips on Edit, and then edit that timeline into your program using

whatever method you find convenient, as described previously in this chapter.

Compositing and Grading Nested Timelines

Similarly to compound clips, nested timelines act like a single clip in the Timeline; they appear as a

single MediaIn node in the Fusion page for compositing, and you can grade them as a single clip in

the Color page. However, if you want to individually add effects to or grade the original clips inside

a nested timeline, you can either open that timeline from the Media Pool, or right-click that clip and

choose Open in Timeline in order to access its constituent clips for compositing or grading.


Edit | Chapter 43 Take Selectors, Compound Clips, and Nested Timelines

EDIT

Audio Buses in Nested Timelines

When you nest a timeline inside of another timeline that has buses set up for mixing in the Fairlight

page, all Sub and Aux routings work as intended within the nested timeline, which exposes all

channels of Main 1 in the enclosing timeline. In this sense, the audio of the nested timeline can be

considered to be a submix that outputs its resulting audio to the audio track it’s edited onto.

For more information about Buses and audio mixing in general, see Part 13, “Fairlight.”

Match Frame for Nested Timelines

and Compound Clips

Match Frame to Source Clip feature is supported for compound clips as well as nested timelines.

Based on the context, the relevant underlying source clip is loaded into the Source Viewer.

With a compound clip or timeline loaded in the Source Viewer, when performing a match frame (from

the Source Viewer), DaVinci Resolve prioritizes finding a nested copy of the clip in the timeline to

perform the match frame. If a nested copy is not found, match frame is automatically performed to

match the underlying source clip to a timeline instance.

Similarly, when the match frame is performed from the timeline (or timeline viewer), DaVinci Resolve

first attempts to find the same underlying clip and frame in the compound clip or nested timeline

loaded in the Source Viewer. If the frame cannot be found, then match frame to source is automatically

performed as usual. This is especially useful when you are comparing two different versions of a

timeline and going back and forth.

Converting Compound Clips

or Timelines to Multicam Clips

It’s possible to convert compound clips and timelines into multicam clips for easier editing using the

Edit page’s Multicam Editing interface. This conversion is a one-way process. You cannot reconvert

a multicam clip back to a timeline or compound clip. If you wish to preserve the original timeline or

compound clip, make sure to duplicate it first, and then convert the copy.

For more information, see Chapter 42, “Multicam Editing.”

To convert a compound clip or timeline to a Multicam clip:

�Right-click on the clip or timeline in the Media Pool and choose “Convert Compound Clips

(Timelines) to Multicam Clips” from the drop down menu.


Edit | Chapter 43 Take Selectors, Compound Clips, and Nested Timelines

EDIT