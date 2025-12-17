---
title: "Full Screen Viewer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 103
---

# Full Screen Viewer

The Cut page has a Full Screen Viewer icon in the upper right that can be clicked to enable Full

Screen view. Press Escape to return to your normal view mode.

The Full Screen Viewer icon


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Enhanced Viewer

The Enhanced Viewer is an alternative for use in the Cut page. The larger viewer will take up the top

half of the screen, while leaving the timeline area in place. You can toggle the Enhanced Viewer by

pressing Option-F.

The Enhanced Viewer in the Cut page

Scrolling Through the Timeline

The playhead in the Cut page is fixed. When you play, shuttle, or jog through your program, the clips

in the Timeline flow past the playhead from right to left if you’re playing forward, or from left to right

if you’re playing backward. This means that for playback, editing, or trimming, you bring the frame

you want to see to the playhead, rather than bringing the playhead to the frame (as you do on the

Edit page).

To scroll or scrub through the Timeline, do one of the following:

�Set the Viewer to show the Timeline, then use any transport or playback controls or keyboard

shortcuts to move the clips in the Timeline back and forth, with the playhead indicating the

current frame.

�Position the pointer within the Timeline Ruler of the Upper Timeline, and drag to the left or right to

scrub through your entire program.

�Position the pointer within the Timeline Ruler of the larger Timeline Editor below, and drag to the

left or right to scrub through the immediate vicinity of the current frame.

�You can use the navigation tools Playback > Previous / Next > Clip (Up Arrow/Down Arrow) or

Marker (Shift - Up Arrow/Shift - Down Arrow) to navigate the Cut page Timelines.

TIP: If at any time you need to analyze the video in the Viewer, DaVinci Resolve’s full

set of scopes is available in the Cut page by selecting Workspace > Video Scopes > On

(Shift‑Command-W).


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Display Clip Names and Status in the Timeline

If you wish, you can see clip names and clip status icons directly on your clips in the Timeline,

for easier identification.

To Display Clip Names for Clips in the Cut Timeline:

�Click on the Timeline Options icon.

�Select Display Clip Names from the drop-down menu.

To Display Clip Status Icons for Clips in the Cut Timeline:

�Click on the Timeline Options icon.

�Select Display Clip Status from the drop-down menu.

Scene Cut Detection in the Cut Timeline (Studio Version Only)

You can use the Scene Cut functionality directly in a Cut timeline. This is useful if you’ve imported

video files of an already edited program, and you wish to automatically cut it back up into

individual clips.

For more information on using Scene Cut Detection, see Chapter 23, “Using Scene Detection.”

To use Scene Cut Detection on a Cut Page Timeline:


Select the video clips you want to split back into multiple cuts on the Timeline.


Select the Timeline Actions icon and choose Detect Scene Cuts from the drop-down menu.

The Boring Detector

The Boring Detector performs a live analysis of the lengths of each of your clips on the Timeline and

then highlights areas that are too long or too short and may demand your attention. It’s accessed by

clicking the Timeline Options icon and selecting Boring Detector. It can be toggled off by clicking the

icon again.

The Boring Detector icon and the Timeline showing its results

Analyze Timeline Edits

The Boring Detector’s parameters are modifiable in its Analyze Timeline Edits window.

�Boring Clips: By adjusting this slider, you can set the minimum number of seconds that a clip’s

duration has to be before being flagged as too long. Clips that exceed this length are highlighted

in light gray on the Upper Timeline.

�Jump Cuts: Adjusting this slider sets the maximum number of frames that a clip’s duration has to be

before being flagged as too short. Clips that are shorter than this length are highlighted in red on the

Upper Timeline. Setting this to 2 frames can help you automatically find accidental “flash frames.”


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

�Cancel: Closes the window without making any changes to the Boring Detector’s analysis.

�Analyze: Starts the live analysis of your timeline using the criteria you’ve selected above.

The Boring Detecter is persistent and continues to function as you make further edits in

the Cut page. It can be turned off by clicking the Boring Detector icon again.

The Boring Detector’s Analyze

Timeline Edits window

Setting In and Out Points

Ordinarily, source media is much longer than the actual clips you’ll be using in a program, so it’s

important to be able to define a range of media you want to edit into the Timeline. This is done by

setting In and Out points, either in the Media Pool in Thumbnail or Filmstrip mode, or in the Viewer in

Source Clip or the Source Tape.

Setting In and Out Points Using the Keyboard

When scrubbing through a thumbnail or filmstrip in the Media Pool, you can press the I (In) or O (Out)

keys to define a range of media. The edit points appear superimposed over the thumbnail area of the

clip, as well as the scroll area of the Viewer if the clip is being mirrored there.

Defining a range of media in the Media Pool

using In and Out points (in white)

When scrubbing or shuttling through media in the Viewer in Source Clip or the Source Tape, or

through your program with the Viewer in Timeline mode, you can press the I (In) or O (Out) keys to

define a range of media.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Defining a range of media in the Viewer using In and Out points

When scrubbing or shuttling through the Timeline as you drag the ruler to the left and right, you can

press the I (In) or O (Out) keys to define a range for incoming edit operations. The range is marked in

both the upper and lower areas of the Timeline.

Defining a range of the Timeline for editing operations using In and Out points

Setting In and Out Points Using the Pointer

If you’re using a pointing device such as a mouse, trackpad or tablet, you can drag the In and Out

handles found underneath the scroll area at the bottom of the Viewer to define a range of media.

The draggable In and Out controls at the bottom of the Viewer

Once you’ve set In and Out points, the jog In and Out controls, located at the far left and right of the

scroll area in the Viewer, let you fine-tune the location of the In and Out points. Click and drag on the

Jog In or Jog Out controls to move either edit point in precise increments. While you drag, a filmstrip

above shows you how many frames you’re trimming.

The draggable Jog In control being used to trim the In point


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

In and Out points set in the Timeline Ruler (either of the Upper Timeline or the Timeline Editor) can be

dragged to the left or right to fine-tune them.

The draggable In and Out points

in the Timeline Ruler

Editing the Duration Field in the Cut Page Viewer

When editing in the Cut page, you set In and Out points to insert a specified range of video. The

duration of that video range appears in the Duration field, which is in the upper-right corner of

the Viewer.

This field is now editable, and updates the Out point to match the value you enter. You can directly

enter a certain number of frames, use the + or - modifiers to change the value by that exact amount, or

make adjustments to the hh:mm:ss:ff field directly.

The editable duration field in the top right of the Viewer