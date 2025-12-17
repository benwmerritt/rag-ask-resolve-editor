---
title: "Trim or Extend Clip to Playhead"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 111
---

# Trim or Extend Clip to Playhead

You can easily trim or extend a clip to a specific length by positioning the playhead on the Timeline

exactly where you want the video to start or end and then selecting the appropriate operation by

clicking on the Edit Actions icon.

To Trim or Extend Clip to Playhead:

�Place the playhead at the point that you wish to either extend the clip to, or cut the clip off at.

�Click on the Edit Actions icon.

�Select Trim Start to Playhead from the contextual menu to cut or extend the left side of the clip to

the playhead position.

�Select Trim End to Playhead from the contextual menu to cut or extend the right side of the clip to

the playhead position.

The original Timeline with playhead intersecting between the second and third set of “BB’s,”


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

(Top) The resulting clip when Trim Start to Playhead is selected,

(Bottom) The resulting clip when Trim End to Playhead is selected

Trimming Edits in the Viewer

You can double-click any edit point between two clips in the Timeline or Upper Timeline to open up

the Trim Editor, which provides a detailed method of adjusting both halves of an edit point. A graphical

A/B roll interface shows two filmstrips with the outgoing clip on top and the incoming clip on the

bottom. These controls are draggable:

�Drag the left side of the top filmstrip’s handle to trim the Out point of the outgoing clip

�Drag the right side of the bottom filmstrip’s handle to trim the In point of the incoming clip

�Drag the white handle between the top and bottom filmstrips to roll the edit point, simultaneously

adjusting the outgoing and incoming edit points

Numbers over each frame let you see exactly how many frames you’re trimming, while a pair of

buttons to the left and right of the transport controls in the Viewer toolbar let you adjust the outgoing

clip’s Out point and incoming clip’s In point in one frame increments.

The Viewer Trim Editor seen when you double-click an edit in the Timeline

Trimming Transitions in the Viewer

If you double-click a transition, that transition appears sandwiched between the outgoing and

incoming clips, with handles you can use to trim the transition’s length, as well as the outgoing and

incoming halves of the edit point to which the transition is applied.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

The Viewer Trim Editor seen when you double-click a transition in the Timeline

Dynamic Trimming Using JKL Controls

The Edit page’s Dynamic Trim mode using the JKL controls on the keyboard has been added to the

Cut page for quick keyboard trimming.

The Dynamic Trim mode lets you resize selected edit points and clips using the JKL transport control

keyboard shortcuts. This means that you can make an appropriate selection in the Timeline, then trim

them during playback, all while monitoring audio and watching the video.

Trimming while viewing the selected clip or edit point playing back has the advantage of letting you

get emotionally involved in what you’re watching, as well as experiencing the timing of a clip as it

plays, in order to help you get a better feel for how exactly you need to trim a particular cut.

While you’re dynamically trimming, you see the same two-up display, the same Timeline overlays, and

the same dynamically updating timeline that appear when you use the Trim tool with the mouse. The

only difference is that you’re trimming while your program plays.

The playhead turns yellow to show

you are in Dynamic Trim mode.

The green highlight shows that

only the Out point of the first clip

is active. Using the JKL keys on

the keyboard will then shift that

edit point forward or backward.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

The Dynamic Trim icon in the Timeline toolbar

To use Dynamic Trim mode to dynamically trim one or more selected clips or edits:


Select one or more edit points on the timeline that you wish to trim. Otherwise, the edit closest to

the smart indictor will be selected for trimming.


Press W to enter Dynamic mode, or select Trim > Dynamic Trim Mode, click the Dynamic Trim tool

in the toolbar. Once you’ve entered Dynamic Trim mode, the playhead tool turns yellow to serve as

a constant reminder that in this mode all you can do is trim clips.


Right-click the Dynamic Trim tool in the toolbar to choose the Dynamic Trim mode.

�Slip: Keeps a clip in the same place in the Timeline, while changing the range of media that

appears in that spot. Slip edits do not change the duration of the overall Timeline.

�Slide: Keeps a clip’s range of media the same, but moves that clip to the left or right by either

shortening the outgoing clip to its left while lengthening the incoming clip to its right, or

vice versa.


The edit point will be highlighted in green to show which edges of the clip are selected for

trimming. Press U to toggle through the available edit point types, or select Trim > Edit Point Type.


Use any combination of the JKL keyboard shortcuts to initiate playback and trimming, including:

� J+K or K+L to trim in slow motion, with slow motion audio playback

� Pressing K while tapping J or L to trim a frame at a time

� Pressing J or L to trim with real time playback

� Pressing J or L repeatedly to trim in fast-reverse or fast-forward, at a variety of speeds


As you dynamically trim, all audio clips in all audio tracks will play back as the playhead scrolls

across them, so you can hear your entire mix as you’re trimming.


After you’ve made a trim, pressing the Spacebar initiates Play Around Current Selection so you

can see how well that trim plays. In Dynamic Trim mode, the Spacebar only executes a Play

Around Current Selection operation, rather than play forward as it usually does.


When you’re finished, you can use the Up and Down Arrow keys to move both the selection

and playhead to another edit point or clip you’d like to trim, or you can press W again to toggle

Dynamic Trim mode off.

You always want to be sure to turn Dynamic mode off when you’re done (W), otherwise using the JKL

keys will continue trimming selections whenever one or more edits or clips are selected, instead of

playing the Timeline.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT

Trim with Safe Edit

Editing in the Cut Page timeline can be fast and furious, and if you wish to avoid accidentally

overwriting an adjacent clip while trimming you can turn on “Trim with Safe Edit” in the timeline options.

In the Timeline options, select Trim with

Safe Edit to prevent accidental overshoots.

With this mode enabled, you can trim and extend an edit point as normal until it intersects another clip.

When the trim cursor reaches the next clip’s bounds, it stops the trim and shows a small timer on the

cursor rather than pushing on with the overwrite. If you actually do want to overwrite the adjacent clip,

continue dragging with the mouse or rotating the Speed Editor dial to override the timer and overwrite

the adjacent clip with the trim operation.

The Safe Edit cursor stopping you

from overwriting the subsequent

clip; continue dragging the clip to

perform the overwrite anyway.


The Cut Page | Chapter 29 Trimming in the Cut Page

CUT