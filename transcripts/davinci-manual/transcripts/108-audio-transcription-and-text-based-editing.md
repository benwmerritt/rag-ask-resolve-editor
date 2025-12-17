---
title: "Audio Transcription and Text Based Editing"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 108
---

# Audio Transcription and Text Based Editing

(Studio Version Only)

The most critical metadata about any clip is knowing what people have said in it. A full transcription

of a shot is useful in narrative film letting you find specific clips based on the dialog in the script,

but a transcript is especially important in unscripted documentary and news production, both to

understand what pieces of the story you actually captured and for a variety of organizational, creative,

and legal requirements.

Until recently, transcribing audio was a labor-intensive process, requiring a human being to listen to

a clip in real time and then type out what was being said in a log sheet. With recent advances in the

DaVinci Resolve Neural Engine, your computer can now perform the tedious work of transcribing each

clip for you automatically, and most importantly, accurately. In addition, having text transcripts attached

to the clips in your project gives you powerful new text-based editing tools to select, search, and

insert clips into your timeline.

For more information on Text Based Editing in detail, see Chapter 40 “Text Based Editing.“


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Chapter 29

Trimming in

the Cut Page

Once you’ve assembled a sequence of clips together into a loosely edited timeline,

the Cut page provides numerous methods for modifying them in the Timeline.

These tools are intended to improve the pace of your program by fine-tuning the timing of each clip,

as well as the edits that separate them them. The idea is to make these kinds of adjustments easy, so

your program’s content is clear, and the timing of your program’s playback is satisfying. This process of

making modifications to the edits in a timeline is referred to as “trimming.”

Contents

Tools That Help You Work in the Timeline������ 579

Ripple on Main Track Option

to Disable Ripple Trims���������������������������������������������� 579

Fixed or Free Playhead���������������������������������������������� 579

Snapping��������������������������������������������������������������������������� 580

Locking, Muting and Disabling Tracks���������������� 580

Audio Trim View�������������������������������������������������������������� 581

Timeline Markers������������������������������������������������������������ 581

Making Selections������������������������������������������������������� 582

Moving Clips in the Timeline���������������������������������� 584

Ripple Overwriting An Entire Clip in Track 1���� 584

Ripple Trimming on Secondary Tracks������������� 585

Overwriting the Middle of Other Clips��������������� 585

Overwriting The Edges of Other Clips��������������� 585

Swapping Clips�������������������������������������������������������������� 586

Copy, Cut, and Paste��������������������������������������������������� 586

Splitting Clips����������������������������������������������������������������� 587

Disabling and Deleting Clips���������������������������������� 587

Disabling and Muting Clips�������������������������������������� 587

Deleting Clips����������������������������������������������������������������� 588

Deleting Parts of Clips������������������������������������������������ 589

Trimming Clips��������������������������������������������������������������� 589

Resize Clips While Rippling the Timeline���������� 589

Rolling an Edit����������������������������������������������������������������� 590

Slipping Clip Content��������������������������������������������������� 591

Roll and Trim Audio Edit Points

to Add Split Edits������������������������������������������������������������ 591

Trim or Extend Clip to Playhead���������������������������� 592

Trimming Edits in the Viewer����������������������������������� 593

Trimming Transitions in the Viewer���������������������� 593

Dynamic Trimming Using JKL Controls������������ 594

Trim with Safe Edit������������������������������������������������������� 596


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

Tools That Help You Work in the Timeline

As you begin the process of trimming clips in the Timeline, a series of buttons at the top left of the

Timeline help you to align clips and keep track of important frames while you work.

Ripple on Main Track Option to Disable Ripple Trims

When trimming on the main track (track 1) in the Cut page, you can disable the automatic rippling of

the clips on that track. This lets you have the option to make simple trim adjustments without the other

clips in the Timeline moving up and down the Timeline.

To Enable or Disable Rippling on a Cut Page Timeline:

•	 Click on the Timeline Options icon and select Ripple On in the contextual menu, or click

directly on the Ripple On icon to the left of the Timeline ruler. Click it again to toggle Rippling

on or off.

•	 Alternatively you can hold down the Option key while trimming with the mouse on the main

track to temporarily disable rippling.

The Ripple On control toggles r

ippling on the main track.

Fixed or Free Playhead

You can choose whether to keep the default fixed playhead on the Cut timeline (video flows under the

playhead), or have it move freely with the video instead (playhead flows over the video). To choose the

mode, click on the Timeline Options icon, and check or uncheck Fixed Playhead,

�When checked, the playhead is fixed in the center of the Timeline, and your edited clips scroll past

it as you play (press the Spacebar), jog, or shuttle (use the JKL keys) in either direction. Locked

mode works great when you use the DaVinci Resolve Editor Keyboard, because the Timeline

flows past the playhead while you use the Jog/Shuttle/Scroll wheel. You can also scroll the

Timeline using your pointer by dragging the Timeline Ruler at the top to the left or right, which also

drags all of your clips to the left or right.

�When unchecked, the playhead moves across the clips as you play (press the Spacebar), jog, or

shuttle (use the JKL keys) in either direction; the clips stay still. This mode can be useful when

you’re doing precision trimming in the Timeline using a pointing device, as the clips stay put while

you drag parts of clips to make adjustments. Once the playhead gets to the right or left edge of

the Timeline, the Timeline pages over to reveal the next part of your edit. You can also move the

playhead by clicking in the Timeline Ruler to jump the playhead to that frame, or by positioning

the pointer over the playhead’s top handle, or over the playhead itself, and dragging the playhead

wherever you want it to go.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

Snapping

You can turn Snapping on or off by clicking the Timeline Options icon and checking or unchecking the

magnet-shaped Snap icon, or press N to enable or disable snapping.

When snapping is turned on, clip in and out points, markers, and the playhead all snap to line up with

one another, making it easy edit clips together at their boundaries, or to line up clips with markers or

the playhead as reference for key frames you want to cut to. When a clip’s boundary is snapping, a

white line shows you the edges that are being aligned with one another.

The indicator that appears when clip

boundaries are snapping to another edge

NOTE: When the playhead is locked, clips don’t snap to it.

However, it’s also important to be able to turn snapping off when this behavior impedes your ability to

make small adjustments to clips in the Timeline. You can press N to temporarily turn snapping on or

off while you’re in the middle of dragging a clip in the Timeline, or while scrubbing the playhead using

the pointer.

�When you change snapping while dragging a clip, an edge, or the Timeline, it’s considered

to be a temporary operation, and snapping reverts to its previous state when you release the

mouse button.

�When you change snapping in between dragging operations, the snapping state remains set until

the next time you change it.

Locking, Muting and Disabling Tracks

As you work in the Timeline, you may find it useful to lock tracks with clips you don’t want to

accidentally change as you work. For example, you might lock an audio track that has an edited piece

of music you’re now cutting other video and audio clips to, so you don’t accidentally alter or trim the

music that serves as the base of your program. Clips on locked tracks appear stippled to let you know

they can’t be altered.

A locked audio track, the Lock icon is closed and clips on that track are stippled


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

You may also find it useful to mute the audio or disable the video of tracks you don’t want to see while

playing the Timeline. For example, you might want to disable a track filled with title graphics if you

want to get a closer look at the underlying video in the background. Each track has Mute and Enable

controls, while audio-only tracks only have Mute controls. White controls are enabled, while gray

controls are disabled.

Track 1 is disabled; the Enable button is orange and clips on the track are dimmed

Audio Trim View

When performing a trim operation in the Cut page, you can set the option to expand the audio

waveform of a Timeline clip while trimming. This mode gives a much more accurate view of the audio,

making it easier to pick a specific edit point between words, beats, etc.

To toggle Audio Trim view:

Click the Timeline Options icon, and check Trim to Audio.

With this option enabled, you’ll see an expanded waveform for audio/video clips that are

being trimmed in the Timeline, while you’re trimming. This shrinks back down after you finish

the trim operation.

The Audio Trim view showing an expanded audio waveform while trimming in the Timeline

Timeline Markers

You can place markers in the Timeline Ruler (of both the Upper Timeline and the Timeline Editor) to

keep track of important frames of clips you want to remember, alternate edit points you’re thinking of,

key moments in the edit, or to make notes of things you need to do. You can edit marker text, which

appears as an overlay in the Viewer, and you can change the color of markers to distinguish them from

one another.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

The Marker button in the

Timeline track header

Methods of working with markers:

�To add a marker: Move the playhead to a frame you want to mark, then click the Marker button in

the Timeline header, or press the M key. You can also add a marker from the Timeline Actions icon.

�To add a marker with a specific color: Move the playhead to a frame you want to mark, then click

the Timeline Actions icon, and select Set Color and Add Marker. This will both add a marker and

open the Markers Edit window, letting you pick a specific color and add a comment.

�To jump the playhead among markers: Hold the shift key and press the Up or Down Arrow keys

to jump the playhead from marker to marker.

�To edit a marker’s name, text, color, or keywords: Double-click a marker, or jump the playhead to

a marker and press M again. When the marker dialog opens, edit the Name, Notes field, Keyword

field, or color of the marker, then press Return or click Done to close the dialog. Markers with

custom notes appear with a dot.

�To move a marker: Drag a marker to another frame in the Timeline Ruler.

�To delete a marker: Select a marker, and press Delete. Or, align the playhead with a marker, and

press Option-M. Or, jump the playhead to a marker, press M to open the marker dialog, and then

click Remove Marker.

Blue, red, and orange markers in the Timeline; the red marker contains text, the others do not