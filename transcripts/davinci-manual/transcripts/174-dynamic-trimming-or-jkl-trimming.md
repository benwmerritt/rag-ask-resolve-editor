---
title: "Dynamic Trimming (or “JKL Trimming”)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 174
---

# Dynamic Trimming (or “JKL Trimming”)

If you want to also have the option of trimming using the JKL shortcut keys in slow motion or frame by

frame, in addition to trimming at 100% or greater playback speeds, then you’ll need to enable Dynamic

Trim mode.

To use Dynamic mode to dynamically trim one or more selected clips or edits:


It’s not necessary to make a selection prior to enabling Dynamic mode for trimming, since the act

of entering Dynamic mode automatically selects the closest edit point to the playhead. However, if

you want to use Dynamic mode to make a complex trim operation, you can select any combination

of edit points to resize, ripple, or roll, or you can select one or more clips that you want to slip or

slide (using the S key to toggle between slipping and sliding).


Press W to enter Dynamic mode, or click the Dynamic tool in the toolbar. If nothing is selected in

the Timeline, then the edit point that’s nearest to the playhead will be automatically selected. If

you’ve already made a selection, that selection will remain and be used for trimming.

Once you’ve entered Dynamic mode, the Dynamic Trim tool in the toolbar turns yellow to let you

know that you’re in Dynamic mode, and the icon shows you whether you’re in Slip or Slide mode

for trimming. Additionally, the playhead turns yellow to serve as a constant reminder that you’re in

Dynamic mode, in which all you can do is trim clips.

The Dynamic tool highlights in the toolbar to let you

know you’re in Dynamic mode; this tool also indicates

whether you’re in Slip (Left) or Slide (Right) mode


Choose the type of operation you want to perform by clicking either the Selection tool

(or pressing A) or the Trim tool (or pressing T):

In Selection mode:

You can dynamically resize or roll edits if you’ve selected one or more edit points in the Timeline.

You can move or slip clips if you’ve selected one or more clips in the Timeline. You can choose

whether to move or slip selected clips by pressing the S key, or by right-clicking the Dynamic trim

tool in the toolbar and choosing Slip or Slide from the drop-down menu.

In Trim mode:

You can dynamically ripple or roll edits if you’ve selected one or more clips in the Timeline.

You can slide or slip clips if you’ve selected one or more clips in the Timeline. You can choose

whether to slide or slip selected clips by pressing the S key, or by right-clicking the Dynamic trim

tool in the toolbar and choosing Slip or Slide from the drop-down menu.


If you’ve selected multiple edit points or clips, then you can use the Left and Right arrow keys in

Dynamic mode to move the playhead to the selected edit point you want to monitor while you’re

trimming. If the playhead isn’t aligned with a selected edit point, then it will jump to the nearest

selected edit point once trimming commences.


Edit | Chapter 44 Trimming

EDIT


Use any combination of the JKL keyboard shortcuts to initiate playback and trimming, including:

J+K or K+L to trim in slow motion, with slow motion audio playback

Pressing K while tapping J or L to trim a frame at a time

Pressing J or L to trim with real time playback

Pressing J or L repeatedly to trim in fast-reverse or fast-forward, at a variety of speeds

As you dynamically trim, all audio clips in all audio tracks will play back as the playhead scrolls

across them, so you can hear your entire mix as you’re trimming.


After you’ve made a trim, pressing the Spacebar initiates Play Around Current Selection so you

can see how that trim plays.

In Dynamic mode, the Spacebar only executes a Play Around Current Selection operation, rather

than play forward as it usually does. What is played by Play Around Current Selection depends on

what is selected; a selected edit plays around just that edit, a selected clip plays around the whole

clip, multiple clips or edits play around the total selection, including the current Pre-Roll and Post-

Roll settings in the Editing panel of the User Preferences.


When you’re finished, you can use the Up and Down Arrow keys to move both the selection

and playhead to another edit point or clip you’d like to trim, or you can press W again to toggle

Dynamic mode off.

You always want to be sure to turn Dynamic mode off when you’re done, because otherwise using JKL

will continue trimming selections whenever one or more edits or clips are selected, instead of playing

the Timeline.

NOTE: While Dynamic mode is enabled, you can use JKL for playback if no clips or edit

points are selected (press Command-Shift-A to deselect all). However, if anything in the

Timeline is selected, then JKL will trim the selection as described above.

Trim Operations that are

Targeted Using the Playhead

The following series of Trim editing commands let you trim clips and edits in different ways using the

position of the playhead to guide the result.

Trim Start and Trim End

The Trim > Trim Start (Shift-[) and Trim End (Shift-]) commands let you move the In or Out point of

all clips that intersect the playhead as either a ripple operation (in Trim mode) or a resize operation

(in Selection mode). You do not need to make a selection to use Trim Start and Trim End, making

these commands fast to use in the right situation. A classic use of Trim End is when you have several

superimposed clips of different lengths that you want to either start or end at the same time.

�Trim Start resizes or ripples (depending on what mode you’re in) all clips that intersect the

playhead, so that each clip’s In point is moved to the current playhead position.


Edit | Chapter 44 Trimming

EDIT

Before and after a Trim Start operation, all clips that

intersect the playhead are trimmed

�Trim End resizes or ripples intersecting clips so that each intersecting clip’s Out point is moved to

the current playhead position.

Before and after a Trim End operation, all clips that intersect the playhead are

trimmed; clips that don’t intersect the playhead are not affected

Clips that don’t intersect the playhead are not affected. Furthermore, you can exclude clips on

specific tracks from this operation by disabling the Auto Select controls on those tracks.


Edit | Chapter 44 Trimming

EDIT

Resize, Ripple, and Roll Start and End Commands

Another set of commands in the Trim menu lets you combine the Trim Start and Trim End functions

with the act of choosing either Selection or Trim mode, and the ability to resize, ripple, or roll, all with

single commands.

�Resize Start to Playhead

�Resize End to Playhead

�Ripple Start to Playhead (Command-Shift-[)

�Ripple End to Playhead (Command-Shift-])

�Roll Start to Playhead

�Roll End to Playhead

Just as with Trim Start and Trim End, these commands use the Timeline Auto Select controls to

determine, of all clips intersecting the playhead, which clips on which tracks to trim. Many of these

commands don’t have keyboard shortcuts by default, but if you prefer this way of working, you can

assign them to keyboard shortcuts of your choosing using the Keyboard Mapping Customization tool

(Option - Command - K).

Slip and Slide Playhead to In and Out Commands

Yet another set of commands in the Trim menu lets you slip a clip from the frame at the current position

of the Playhead to the In or Out point of that clip.

�Slip Playhead to In

�Slip Playhead to Out

TIP: The Slip Playhead to In command functions identically to using the extend edit while the

playhead intersects a selected clip.

Just as with Trim Start and Trim End, these commands use the Timeline Auto Select controls to

determine, of all clips intersecting the playhead, which clips on which tracks to trim. These commands

don’t have keyboard shortcuts by default, but if you prefer this way of working, you can assign them

to keyboard shortcuts of your choosing using the Keyboard Mapping Customization tool (Option -

Command - K).

Extend Edits

The Extend Edit command (choose Trim > Extend Edit, or press E) lets you resize or ripple one or more

selected edit points or clips. Unlike Trim Start and Trim End, it doesn’t matter if the playhead intersects

clips when doing an extend edit.

Extend Editing Edit Points

Make one selection per track of any combination of In or Out points, and press the E key to move

those edit points to the current position of the playhead.


Edit | Chapter 44 Trimming

EDIT

Before and after a multi-track extend edit performed in Selection mode. Before, the red

selections indicate that you’ve selected the first frame of media for those clips. After, the

selections turn green to indicate that there’s additional frames at the head of the edit for trimming.

In Trim mode, selected edit points will ripple instead of resizing affected clips. However, to simplify

multi-track extend edit operations when using the Trim tool, the lowest numbered video track with

auto-select enabled defines the amount by which the extend edit will ripple the rest of the Timeline; all

selected edit points on other tracks are simply resized to the position of the playhead.


Edit | Chapter 44 Trimming

EDIT

Before and after a multi-track extend edit performed in Trim mode; you can see that the

lowest numbered track with a selection defines how far the Timeline will be rippled

Using Extend Edits to Slide Clips

You can also use the Extend Edit command to slide the contents of a single selected clip using either

the Selection or Ripple tools. Simply select a clip, position the playhead over the frame of that clip

you want to slip to the In point of that clip’s position in the Timeline, and press E to perform the slip.

You can even do this during playback if you want to watch the clip play and press E to slip that frame

back when the moment feels right.

Using the extend edit to slip a clip in the Timeline, the red marker shows that the

frame at the playhead is slipped back to the In point of that clip in the Timeline


Edit | Chapter 44 Trimming

EDIT