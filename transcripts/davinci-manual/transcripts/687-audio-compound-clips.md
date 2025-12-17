---
title: "Audio Compound Clips"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 687
---

# Audio Compound Clips

DaVinci Resolve supports audio compound clips, which are created just like any other compound

clip, by selecting multiple audio clips, right-clicking one of them, and choosing New Compound Clip.

Alternately, compound clips with video clips may now contain multiple audio items as well.

When compound clips containing audio are opened in the Edit or Fairlight pages by right-clicking

an audio compound clip and choosing Open in Timeline, breadcrumb controls appear beneath the

Timeline that let you exit the compound clip and get back to the master Timeline.

Opening an audio compound clip; note the path control at the bottom left of the Timeline

Audio Crossfades

You can add Cross Fade transitions to any edit point between two audio clips that have enough

handles similarly to how you add video transitions, by dragging and dropping from the Effects Library,

by right-clicking an edit and choosing an option from the contextual menu, or by selecting an audio

edit point and choosing Timeline > Add Audio Only Transition (Shift-T).

Cross Fade transitions are a quick and easy way to fade the volume of the outgoing clip down while

simultaneously fading the volume of the incoming clip up, letting you create a smooth aural transition

between two audio clips.

An audio Cross Fade transition applied between two clips

You can double-click a Cross Fade transition to open it into the Inspector, revealing the

following parameters:

�Duration: The duration of the transition, shown in both seconds and frames.

�Alignment: A dropdown that lets you choose the transition’s position relative to the edit point it’s

applied to. Your choices are “End on Edit,” “Center on Edit,” and “Begin on Edit.”

�Transition style: You can choose –3dB, 0dB, or +3dB to set both the Fade In and Fade Out levels

to the same value. For more information on what these levels mean, see the following parameter.

�Fade In/Fade Out levels: There are three options that affect the incoming and outgoing halves of

the Cross Fade effect independently. 0dB applies a linear fade (this is the default). +3dB applies a


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

boosted curve; when applied to both Fade In and Fade Out, this can compensate for diminished

levels in the middle of a Cross Fade. –3dB applies an attenuating curve, which deliberately lowers

the level of the Cross Fade.

Crossfades can be created and edited on both the Edit and Fairlight pages.

Fades and Crossfades

Part of audio editing in the Fairlight page is the use of fades and crossfades. This section shows you

how to create these effects for smoothly segueing from one audio clip to another.

Basic fades can be created on Dolby Atmos master files placed on a timeline as a clip.

However, complex fades and batch fades are not supported.

Using Fades

Like the Edit page, each audio clip has fader handles that appear at the upper right and left corners of

a clip you’re hovering the pointer over.

Fader handles appear when you

hover the pointer over a clip

Pulling these handles out creates a fade effect with a duration equal to the length you

extended the handle.

Creating a fade effect by pulling out

one of the fader handles

Once you’ve created a fade effect, you can adjust the curve of the fade by dragging the handle that

appears right on top of the fader curve. Dragging the handle up and down affects the angle of the

curve, and dragging the handle left and right affects the shape of the curve. In this way, you can create

all manner of fade effects.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

Adjusting the curve of the fade

Batch Fade and Crossfade Editor in the Fairlight Page

Multiple fades are available to multiple clips with multiple tracks selected, significantly increasing

fade functionality. The Batch Fades window has fade shapes for Fade In, Cross Fade, and Fade Out.

The Fade Length is user definable by frame for each of these fade types, and there is an option to

overwrite existing fades on the highlighted clips.

All of the settings in the Batch Fades window

There are six options per Fade type for precise usage. When adding Fades between sources, it’s

important to determine the shape so that only the desired media is included in the fade. The curves

indicate the ramping slopes of the fade.

Each box has similar controls for affecting the individual Fade type.


Next to the Fade type name is the on/off toggle


There are six Fade curves to create the precise fade needed.


A Length box determines how many frames the fade will extend,


A click box to overwrite any previous fades, if needed.

The Crossfade box has three additional controls.


Equal Power maintains the signal level through the fade.


Equal Gain is used when crossfading media that could phase when combined. For instance,

if a music cue is crossfaded at the mid-point of the fade, there could be a jump in level or added

phasing issues. Using this option maintains the gain across the fade for that type of media.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT


Unlinked allows for a different curve type on either side of the crossfade.

This window will retain the settings that were last made so once a series of Fade types have been

chosen, then Batch Fades can be made without opening this window and can be accessed via the

Fairlight menu with a single click across highlighted regions. The Apply Batch Fades in the Fairlight

menu are applied with the settings made in the Batch Fades window.

Batch Fade options in

the Fairlight menu

This graphic shows highlighted clips and tracks ready to have Batch Fades applied.

Tracks and clips highlighted for Batch Fades


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

The graphic below shows how the Batch Fades are applied. Clips that are not connected have

Fade In and Fade Out applied. Clips that are connected have Crossfades applied. The Batch

Fades window determines each of the Fade parameters and then applies them to all of the

selected clips. In this example, the Overwrite box was unchecked. Compare the fades that

were already there and see that they retain their original Fade length and shape.

All of the highlighted clips have been faded according to the Batch Fades window.

NOTE: If the media is too short, a dialog box will alert you that there are insufficient handles

and that the fade could not be created. You can then choose to trim clips, skip clips, or cancel

the Batch Fade. If you cancel, you can then alter the settings to better suit the media.

Fade In and Out to Playhead

A pair of commands in the Trim menu let you move the playhead over a clip, and use the playhead

position to “Fade In to Playhead” or “Fade Out to Playhead.” These commands work in both the Edit

and Fairlight pages.

(Left) Placing the playhead where you want a fade in to end, (Right) Using Fade In to Playhead


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT