---
title: "Splitting Clips"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 110
---

# Splitting Clips

You can split any clip into two pieces, effectively adding an edit point in the middle, in preparation for

moving part of a clip, deleting part of a clip, inserting another clip at that edit point, or adding an effect

of some kind to one part of a clip but not another.

To split a clip:


Move the playhead to the frame of a clip where you want to split it.


Do one of the following:

�Click on the Edit Actions icon, and select split from the drop-down menu.

�Right-click the top handle of the playhead and click the Split button that appears on

the radial menu.

�Press Command-Backslash.

�Press the Split Clips (scissor) icon on the far left of the Cut page Edit commands.

(Left) Before splitting a clip, (Right) After, a new edit point bisects the clip into two pieces

Disabling and Deleting Clips

Clips that you no longer want can be disabled or deleted.

Disabling and Muting Clips

You can turn off the audio and/or video for a clip in the Timeline, without removing the clip itself. This

is useful in instances where you want to use a clip’s audio or video selectively, or for instances where

you want to disable the audio and video for a clip that you don’t want to use, without eliminating it

completely from the Timeline in case you change your mind.

Disabling Clips

You can turn off a clip’s video while leaving it in the Timeline by selecting it and pressing D, or by right-

clicking it and deselecting Enable from the contextual menu. The clip turns dull to show it’s disabled.

Audio will continue to play for that clip unless you mute it as well.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

A disabled clip in the Timeline

Muting Clips

You can turn off a clip’s audio while leaving it in the Timeline by right-clicking it and choosing Mute

from the contextual menu. A mute icon is superimposed over the beginning of the clip to show audio is

disabled. Video will continue to play for that clip unless you disable it as well.

A muted clip in the Timeline

Deleting Clips

If you want to completely eliminate one or more clips from the Timeline, select them and press the

Delete key. The clip(s) will be removed. If you’ve deleted a clip on Track 1, the Timeline will ripple to

close the gap automatically.

Selecting clip DD to delete it

Deleting clip DD results in clips EE through NN moving left to fill the gap in Track 1;

superimposed clips move to keep in sync with the clips underneath them


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

Deleting Parts of Clips

If you want to delete only part one or more clips, set In and Out points around the section of the

Timeline you want to delete, and press the Delete key. The section of the Timeline between the In and

Out points will be removed. If you’ve deleted part of a clip on Track 1, the Timeline will ripple to close

the gap automatically.

Marking In and Out points to delete that section of the Timeline

After deleting whatever’s between the In and Out points, all clips to the right

of the marked section move left to close the gap in Track 1

Trimming Clips

You can also quickly modify your edited timeline by resizing the In and Out points of any clip, moving

the edit points between clips, and slipping the contents of a clip.

Resize Clips While Rippling the Timeline

If you move the pointer over the far left or right edge of a clip in the Timeline or Upper Timeline, it

turns into a Resize icon to indicate that you can drag the In or Out point of that clip to make it shorter

or longer, in the process rippling all clips to the right in the Timeline to accommodate the new length

of the clip. While you drag, a tooltip shows you how many frames you’ve moved the clip and the clip’s

new duration. As you do so, the audio will scrub along with the Resize cursor.

If you resize a clip in Track 1, the rest of the edited timeline automatically ripples to accommodate the

changes you’ve made, with clips to the right of the changed area moving left to fill the gap of a deleted

or shortened clips, or moving right to make room for an inserted or lengthened clip.

Clicking the Out point of clip DD in Track 1


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

Dragging to shorten clip DD ripples the Timeline; a tooltip

appears to show you how many frames you’ve resized

Moving or resizing clips on Track 2 and above only moves or resizes that one clip; other

clips in the Timeline are not rearranged and the Timeline is not rippled when you do this.

Clicking the out point of clip HH in Track 2

Dragging to lengthen the clip doesn’t ripple the Timeline

TIP: When you resize the Out point of a clip on Track 1 that’s underneath a superimposed clip,

and the superimposed clip has an In point that’s to the right of the In point of the clip you’re

resizing, then dragging the Out point of the clip you’re trimming past the left of the In point of

the superimposed clip will delete that superimposed clip from the Timeline.

Rolling an Edit

You can click and drag any edit point between two clips in the Timeline or Upper Timeline to

“roll” it, basically resizing the Out point of the outgoing clip and the In point of the incoming clip

simultaneously. This lets you move an edit point without changing the duration of the overall timeline.

While you drag, a white overlay in the Timeline lets you see how much media you have available for

rolling (depending on the available handles in the source media). As you do so, the audio will scrub

along with the right clip’s In point.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

(Top) Clicking an edit

between clips CC and DD

(Bottom) Dragging to the right

rolls it forward, simultaneously

resizing clips CC and DD

Slipping Clip Content

For each clip in the Timeline, a Slip handle appears at the center of the clip. Dragging this handle lets

you slip the contents of that clip to present a different range of media, without changing the position or

duration of the clip, and without changing any other part of the Timeline.

You can even select multiple clips, such as two superimposed clips, or a number of clips in a row, and

slip them all at the same time. While you drag, a white overlay in the Timeline lets you see how much

media you have available for slipping (depending on the source clip’s duration).

(Top) Clicking a clip’s slip handle, (Bottom) Dragging a clip’s slip handle to change the range of media within that clip

Roll and Trim Audio Edit Points to Add Split Edits

You can independently trim the audio channel of a video clip in the Cut page. This allows you to do a

split edit (L-cut or J-cut), where the audio of one video clip is extended under the video of a different

clip. This lets you manipulate the flow and rhythm of a scene in terms of reaction shots and more

natural sounding dialogue.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

To Trim Audio Only and Perform a Split Edit on a Cut Page Timeline:

�Expand the track on the Cut page by clicking on the Enlarge Track icon on the left side of the track

header. This is not strictly necessary but makes it easier to find the correct trigger point for the tool

and see the audio waveform as you’re trimming it.

�Hover the pointer over the edit point in the lower audio portion of the track. When the trim icon

shows a musical note to the right, you can then slide that edit point back and forth and only the

audio portion of the clip will be expanded forwards or backwards.

�The Trim View will also appear in the Viewer as you edit, along with expanded audio waveforms

that are zoomed into the frame level for precision.

Placing the pointer in the audio part of the track

triggers the trim indicator with the musical note icon.

This allows you to drag just the audio edit point back

and forth in the Timeline, leaving the video in place.