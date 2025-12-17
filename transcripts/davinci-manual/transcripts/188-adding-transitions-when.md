---
title: "Adding Transitions When"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 188
---

# Adding Transitions When

There’s Not Enough Handles

If the outgoing and incoming overlapping handles at a given edit point don’t have enough frames to

fit the standard transition duration, and you try to add a transition by selecting one or more edit points

and pressing Command-T, or by right-clicking an edit point and using the transition options in the

resulting contextual menu, then you’ll be presented with a dialog that gives you three choices:

Trim Clips: You can automatically trim the incoming and outgoing sides of each selected edit point to

create the overlap needed for adding the standard transition.

Skip Clips: Don’t add transitions to the selected edit points that lack the appropriate overlap.

Cancel: Cancel the operation entirely.

Adding Transitions By

Dragging to Create Overlap

There’s another method you can use to create transitions that makes it easy to create transitions while

you’re doing drag and drop editing by simply overlapping the beginning and end of two clips where

you want a transition to appear. Just press and hold the Option and Shift keyboard modifiers together

while you drag a clip or edit to create overlap with another clip. You can do this in three ways:

Select the In or Out point of a clip, then press and hold Option-Shift down and drag the

selected edit point to overlap a neighboring clip where you want to create a transition.

Creating a transition by Option-Shift dragging an

edit point to create an overlap between two clips

Select a clip, then press and hold Option-Shift down and drag the entire clip to overlap a

neighboring clip where you want to create a transition.

Creating a transition by Option-Shift dragging a whole

clip to create an overlap between it and another clip


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

Hold the Option-Shift keys down while you drag a clip from the Media Pool to overlap a clip

that’s already in the Timeline.

Creating a transition by Option-Shift dragging a clip

from the Media Pool to overlap a clip in the Timeline

Transition Properties in the Inspector

Double-clicking a transition in the Timeline opens that Transition tab in the Inspector. Each transition

has the following properties you can edit.

Transition Type: The currently selected transition. You can change to any other installed transition by

selecting one in the drop-down menu.

Duration: The duration of the transition, shown in both seconds and frames.

Alignment: A drop-down that lets you choose the transition’s position relative to the edit point it’s

applied to. Your choices are “Start on Edit,” “Center on Edit,” and “End on Edit.”

Additional properties that are specific to each type of transition appear in another group below.

Since the Cross Dissolve transition is the most common transition used, its properties will be shown as

an example.

Style: The different Dissolve transitions (Cross Dissolve, Additive Dissolve, and so on) expose this

drop-down that lets you choose different ways for the outgoing clip to blend into the incoming clip

during the dissolve. There are six different options to choose from:

�Video: A simple linear dissolve; the outgoing clip fades out as the incoming clip fades in.

�Film: A logarithmic dissolve, simulating film dissolves as created by an optical printer.

�Additive: The outgoing and incoming clips are cross faded using the Additive composite mode. As

a result, the transition seems to brighten at the halfway point.

�Subtractive: The outgoing and incoming clips are cross faded using the Subtractive composite

mode. As a result, the transition seems to darken at the halfway point.

�Highlights: The outgoing and incoming clips are cross faded using the Lighten composite mode.

The lightest parts of each clip are emphasized during this transition.

�Shadows: The outgoing and incoming clips are cross faded using the Darken composite mode.

The darkest parts of each clip are emphasized during this transition.

Start Ratio: Defines the percentage of completion for the transition at its first frame, from 0 to 100

percent. Setting the Start Ratio to anything but 0 results in the transition immediately appearing at a

more fully cross-dissolved state from the very first frame.

End Ratio: Defines the percentage of completion for the transition at its last frame. Setting the

End Ratio to anything but 0 results in the transition never fully dissolving to the incoming shot at its last

frame.

Reverse: Reverses the transition. This parameter is disabled for Dissolve transitions.


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

Ease: A drop-down that lets you apply nonlinear acceleration to the beginning, ending, or overall

duration of a transition. The result is to add inertia to the transition from the outgoing clip to the

incoming clip, and providing a gentler change from each clip into and out of the transition.

�None: The outgoing clip fades away to the next shot in a linear fashion.

�In: The outgoing clip lingers as the beginning of the transition dissolves more slowly than the end.

�Out: The outgoing clip fades away more quickly, as the beginning of the transition dissolves more

quickly than the end.

�In & Out: Both the outgoing and incoming clips make slower transitions at the beginning and end

of the dissolve, but the very center of the transition is faster as a result.

�Custom: Lets you modify the parameters of the fade manually using the Transition Curves below.

Transition Curve: Allows you to manually set keyframes controlling the progress of the transition along

its duration.

Other types of transitions display properties that are specific to that transition’s particular effect.

These are described at length in the following section.

Using Transition Curves in the Edit Page

You can create even more highly customized transition effects using the transition curve associated

with each transition you add to the Timeline. Clicking the button at the bottom-right corner of a

transition in the Timeline reveals a Keyframe Editor, and clicking the Curve Editor button in the

Keyframe Editor track for the transition reveals the Transition Curve Editor.

A transition curve opened underneath a Cross Dissolve transition

The Transition Curve Editor works identically to the Curve Editor you can access from any clip, except

instead of using the curve to animate image transforms, you use the curve to retime the transition.

Combined with eased or bezier keyframes at the beginning and end of a transition curve, you can

create transitions that slowly start and quickly end, quickly start and slowly end, or any variation your

project requires. A graphical representation of the curve appears as a shaded area on the transition

itself in the Timeline.


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

Methods of editing a transition curve:

To change the interpolation of a control point: Click the control point you want to edit,

and then click one of the four Bezier interpolation buttons in the Curve Editor title bar.

Adding Bezier handles to a transition control point lets you create an eased transition. If you

chose an option from the Ease drop-down of the Transition Properties in the Inspector, one or

both of the transition curve keyframes may already be set to Bezier.

To adjust a Bezier handle: Drag the Bezier handle in any direction to alter the curve.

Whenever you customize Bezier handles on a transition curve, the Ease drop-down of the

Transition Properties in the Inspector changes to Custom.

To add a new control point to a curve: Option-click anywhere on a curve to add a new

control point.

To drag a control point on a curve: Click any control point and drag left or right to retime it,

and up or down to change the value of the control point. Once you begin to move the pointer,

the control point is constrained in that direction.

To delete a control point from a curve: Right-click a keyframe and choose Delete Selected

from the contextual menu. You cannot delete the last two control points of a transition curve.

To turn a curve on and off: Clicking the white dot at the upper left-hand corner of the

Keyframe Editor lets you turn a transition curve’s effect on and off, without disabling the

transition. When you turn the keyframes off, the transition defaults to a linear transition with

no easing.

Favorite Transitions

While DaVinci Resolve provides a wide variety of transitions by default, most editors typically only use

a subset of these in their day-to-day work. Also, it’s typical to save customized versions of a particular

transition in order to reuse that specific set of transition settings over and over again.

To set a transition or other effect as a favorite in the Effects Library:

Move the pointer over any transition, and click the star button when it appears to set that

transition as a favorite. Click any transition’s star to “un-favorite” it. Favorites are displayed

in the Favorites area of the Effects Library bin list in the Edit page, or the Favorites tab in the

Transitions panel in the Cut page.

Changing the Standard Transition

Different projects may require different transitions be used as the standard transition. DaVinci Resolve

gives you several tools for dealing with this.

To change the standard transition:

Right-click any transition or effect and choose “Set as Standard Transition.” The standard

transition appears with an orange indicator to the left of its name in the Effects Library.


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

The Effects Library open in the Edit page, showing starred transitions that have been

favorited, and the standard transition with an orange indicator to the left of its name

The Transitions tab open in the Cut page, showing starred transitions that have been favorited,

and the standard transition with an orange indicator to the left of its name

To change the standard transition duration:

Open the Editing panel of the User Preferences, and change the “Standard transition duration”

setting (there are controls for setting the duration in either Seconds or Frames). Click Save

when you’re finished.


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT