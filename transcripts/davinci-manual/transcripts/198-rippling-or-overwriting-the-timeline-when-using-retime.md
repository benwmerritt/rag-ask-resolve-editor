---
title: "Rippling or Overwriting the Timeline When Using Retime"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 198
---

# Rippling or Overwriting the Timeline When Using Retime

Whether or not clips to the right in the Timeline will ripple to accommodate the change in duration

resulting in speed changes you make with the Retime controls depends on whether you’re using

the Selection tool/mode (in which case the Timeline won’t ripple), or the Trim tool/mode (in which

case the Timeline will).

Reading Clip Speed Arrows

When you retime a clip, the Clip Speed pop-up menu displays the current speed of the entire clip.

Additionally, the arrows in the Retime control track show you the speed and direction of playback.

When clip speed is slowed down below 100%, the Retime control track shows yellow playback

triangles that are spaced farther apart. When clip speed is sped up above 100%, the Retime control

track shows blue triangles that are bunched closer together. At 100% normal speed, the Retime control

track shows blue, evenly spaced triangles, while left-facing blue arrows indicates reverse playback.

Three clips set to different speeds. From left to right, 100% speed, slow motion,

and fast forward are indicated by the yellow arrows.

Creating Variable Speed Effects Using the Retime Controls

You can also use the Retime controls to insert freeze frames within the middle of a clip, and create

other custom variable speed effects using speed points. Additional variable speed options include

rewind and speed ramp effects, which automatically place speed points to create preset effects.

To create a freeze frame at a particular moment in time:


With the Retime controls exposed, move the playhead to the frame you want to freeze, within that

clip. Ideally, this will be for an effect where you want a character in motion to suddenly stop at a

particular frame.


Open the Clip Speed pop-up menu (the pop-up next to the speed percentage text at the bottom

of the clip), and choose Freeze Frame. Two new speed points are added to the clip, defining a

range within which the clip is frozen at that frame. This can be seen by the vertical red bars in

the Retime control track. Past the second speed point, the clip resumes playback from the next

frame forward.

Speed effect controls set to insert a momentary freeze frame within the clip


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT


Drag the second speed point forward or back to define the duration of the freeze frame. The result

is that the clip plays normally up until the first speed point, then freezes on that frame until the

second speed point, at which playback resumes.

To create variable-speed effects:


With the Retime controls exposed, move the playhead to the frame at which you want to change

the speed of the clip, and choose Add Speed Point from the Clip Speed pop-up menu.


Move the playhead forward to the next frame at which you want the clip speed to change again,

and add another speed point. It takes a minimum of two speed points to create a speed effect.


To alter the speed of the clip segment appearing between these two speed points,

do one of the following:

�Using the pointer, drag the top handle of the second speed point to the right to slow down clip

playback, or to the left to speed up clip playback within just that segment. Doing this either

shortens or lengthens the clip, and either overwrites or ripples neighboring clips depending on

whether you’re using the Selection or Trim modes.

�Also using the pointer, you can drag the bottom handle of any speed point to widen the range

of the clip that plays at that particular speed. Doing this reallocates frames from before and after

the speed segment being adjusted to keep all speed segments playing at the same speed, and

this also shortens or lengthens the clip, but by a different amount.

�Using the Clip Speed pop-up menu, choose a new speed for that segment from the

Change Speed pop-up menu. You can also set any segment to play in reverse by choosing

Reverse Segment.


To clear a speed point and eliminate that particular clip’s speed segment from the effect, choose

Clear Speed Point from any Clip Speed pop-up menu to eliminate whichever speed point appears

to its left.

When you create variable-speed effects, the arrows in the Retime control track can help you

keep track of what you’re doing, and each segment’s speed pop-up shows you the actual

numeric speed. The change in speed from each speed segment to the next is automatically

eased, for a smooth transition from one speed to another.

Speed controls set to ramp among three different playback speeds; arrow spacing shows the timing

There are two additional sets of commands for creating preset speed effects that use multiple

speed points.


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT

To add a rewind effect:

With a clip’s Retime controls exposed, open any Clip Speed pop-up menu and choose a preset

percentage from the Rewind submenu. This results in two additional speed points being added after

the rightmost speed point in the current segment, which creates the effect of the current segment

playing in fast reverse for the chosen percentage, and then playing a second time from the beginning.

Speed effect controls before and after creating a “rewind” effect

To add a speed ramp:

With a clip’s Retime controls exposed, open any Clip Speed pop-up menu and choose one of the two

options from the Speed Ramp submenu to replace the current speed effect with a series of five speed

segments that start at 10% and increase progressively to 30%, 50%, 70%, and then 90%. Once created,

you can drag the speed points to customize this effect to create whatever durations you require.

Speed effect controls set to create a gradual ramp from 0 to 100 percent playback speed


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT

Closing Retime Controls

When you’re finished creating your Retime effect, you can close the Retime controls so that clip

assumes a normal appearance again. Closing the Retime controls has no effect on the timing of the

clip, it just ensures you cannot accidentally modify the speed of the clip with the mouse.

To close the Retime controls in the Timeline:

�Click the X button at the upper left-hand corner of the Retime control box.

�Press the escape key.

�Select the retimed clip, and either choose Clip > Retime Controls, or press Command-R.

When a retimed clip has its Retime controls hidden, a Retime badge appears to the left of that

clip’s name in the Timeline. You can reopen the Retime controls whenever you need to make

further changes.

The Speed Effect badge that

shows a clip is being retimed

To reopen the Retime controls in the Timeline:

Select the retimed clip, and either choose Clip > Retime Controls, or press Command-R.

Once you’ve retimed a clip using the Retime effect, you can use that clip’s Retime Process

parameter in the Inspector to define how that clip’s retiming is processed, using the low quality

Nearest option, using Frame Blending, or using Optical Flow.

Using Retime Curves

You can also optionally use curves to retime clips, either in conjunction with the Retime controls, or by

themselves. For example, you can use the simpler retiming controls first to create the overall speed

effect you need, and then use either of the available Retime Curves to create further refinements by

adjusting Bezier curve handles to adjust the transition of one speed to another, or you can expose

either of the Retime Curves first and use it to create your speed effect from scratch by adding and

adjusting control points and curve segments.

No matter how you like to work, the control points of each of the speed curves have a 1:1

correspondence to the speed points that are exposed in the Retime controls, and curve segment

modifications are mirrored by speed point adjustments in the Retime controls if you have both

exposed at the same time. This means that, when creating complex variable retiming effects, it’s easy

to drag whichever control most easily adjusts the quality of speed you require.


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT

The Retime Curves let you adjust the transition from one speed to another using handles

In addition, there are two kinds of Retime curves you can use for maximum flexibility. Which is best

depends on what you’re more comfortable with, and on which will handle the type of motion you want

to create more easily:

�The Retime Frame curve exposes a diagonal line that represents a time graph. This is a type of

curve found in many other post-production applications, in which the vertical axis represents

each frame of that clip’s source media, and the horizontal axis represents each frame of playback

in the Timeline. With the default diagonal graph, there is a one-to-one correspondence between

each frame of source media and each frame of timeline playback; this represents 100% speed.

However, adding control points lets you alter how source frames are mapped to the Timeline.

For any two control points on the Retime Frame curve, so long as the control point at the left is

lower than the control point at the right of a curve segment, there will be forward motion, with

longer shallow curve segments creating slower motion, and steeper shorter curve segments

creating faster motion in the clip.

A diagonal Retime Frame curve with two segments: a long shallow segment to the left that

creates slow motion, and a short steep segment to the right that creates fast motion

�If a curve segment has a left control point that’s higher than the right control point, then the motion

will be reversed and that segment will play backward.


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT

A Retime Frame curve with an inverted curve that creates reverse motion

�The Retime Speed curve (seen below) exposes a flat line that represents 100% speed. Adding

pairs of control points and dragging each segment to raise or lower it alters speed; you must drag

the segments, not the control points themselves. Raising a curve segment shortens that segment

and speeds up that portion of the clip, while lowering a curve segment lengthens that segment

and slows down that portion of the clip. As you adjust each curve segment, a tooltip shows you

the exact speed percentage that segment represents. You should note that it’s impossible to

create reverse motion using the Retime Position curve; you need to use either the Retime controls

or the Retime Speed curve described above.

A Retime Speed curve with two segments: a shorter one that creates fast

motion, and a longer segment that creates slow motion


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT

Methods of working with speed curves:

�To expose speed curves for a clip in the Timeline: Right-click a clip in the Timeline, and choose

Retime Curve. The Curve Editor is exposed for that clip, and you can edit it as you would any other

curve, adding moving, and deleting control points.

�To switch between editing Retime Speed and Retime Frame curves: Use the Curve pop-up at

the upper left-hand corner of the Curve Editor to check or uncheck the curves you want to be

visible. Clicking on a curve within the editor makes that curve the currently edited one.

�To close a speed curve: Clicking the Curve button at the right-hand side of the clip’s title bar in the

Timeline toggles the curve open and closed.

As far as adding, removing, and smoothing control points on speed curves and adjusting

curve segments, they work identically to any other curve in the Timeline.

For more information, refer to “Keyframing in the Timeline and Curve Editor” see Chapter 53,

“Keyframing Effects in the Edit Page.”