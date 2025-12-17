---
title: "Viewing Automation in the Timeline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 705
---

# Viewing Automation in the Timeline

Once you’ve recorded automation for a supported plugin parameter or Mixer channel control, you can

select and view it on the corresponding timeline track using one of the methods described below.

Right-Click to View Automation

Fairlight lets you select and view track automation by right-clicking parameters on Fairlight FX,

supported Audio Unit or VST plugins, or Mixer channel controls. The parameter or control name is

displayed in the track header, and the corresponding automation curve appears in the Timeline.

This time-saving method is especially useful when automating supported plugins with an extensive

parameter list, such as a parametric EQ or mixer channel strip emulation.

The Automation Dropdown Menu

When automation is enabled via the Toggle Automation button, you can use the Automaton dropdown

menu on the track header to choose which automation curve to view, with options for Fader, Mute,

Pan, EQ, Compressor, Limiter, Aux, Plugins, and Misc controls..

Mixing automation for the Fader shown in the Timeline

NOTE: When viewing Fader Level automation on a track that is assigned to a VCA, the VCA

automation curve will also be visible.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Overwriting Automation

Once you’ve recorded automation for a particular clip, you can overwrite that automation in

subsequent passes. Using either of the previously described methods of recording automation,

adjusting the levels of a track control with previously recorded automation displays a red line that

shows the new level relative to the previously recorded level.

Setting new levels to overwrite previously recorded automation displays a red line

Pressing play to actually record this new automation will overwrite the previous levels at this

new value.

New automation overwrites the previous levels

Automation data can be copied, pasted, and erased under the Fairlight Menu > Automation > Copy/

Paste/Erase.

Automation Follows Edit

When editing your timeline, you can choose whether automation will follow the movement of clips or

stay locked to its position. This is enabled by default but can be changed by unchecking Fairlight >

Automation > Follows Edit.

When enabled, anytime you move or edit a clip on the Timeline, the automation you’d written over its

range will follow with it, ensuring that as you make changes to the edit, the automation for a given clip

range will remain the same.

This is also extremely useful when doing an initial edit of audio clips that contain automation data. For

instance, if you have a recurring sound effect that pans left to right, first automate that panning to the

audio clip. When this clip is copied through the Timeline it will retain the same panning automation for

each new instance. This can be very useful for a variety of edits that require the same automation data

for audio clips in a timeline.

Be aware, however, that Automation Follows Edit will need to be turned off when copying and pasting

clips or sequences where the automation that has been applied is not relevant to the new edits.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

When Automation Follows Edit is enabled, automation data “lives with” the time range it came

from. Any of that data, like volume or panning, will travel with clips. So if a complete section has

been removed, all of the automation inside of the clips contained in that section are also removed.

If a section of clips changes its location in the Timeline, all of the automation embedded in those clips

move to the new location on the Timeline with the clips.

When automation is enabled in the Fairlight toolbar, the Automation Follows Edit button will appear.

The Automation Follows Edit button to

the left of the Flag button on the toolbar

Editing Automation

When automation is enabled (Toggle Automation button is on), the Pencil tool appears. Combined with

the Focus mode, these tools let you edit automation in different ways.

Focus mode provides the main tools

used for editing automation. The Pencil

appears when automation is enabled

(Toggle Automation is on).

Adjusting and Deleting Automation Keyframes

The Focus tools let you adjust automation in two different ways.

Adjusting Individual Keyframes

Using the Focus tools, you can click and drag any automation keyframe up or down and left or right

(bounded by its neighboring keyframes) to adjust it directly. When zoomed in, this can be an effective

way of making precise adjustments. The segment of automation affected by the keyframe being

dragged continues to show green to indicate the new curve being created, and a tooltip with the

currently adjust value appears, while the previously created data is shown in gray. When you release

the mouse button, the curve is adjusted

Single keyframe being adjusted showing prior level in gray


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Adjusting and Deleting Multiple Keyframes

You can also use the Focus mode I-beam selector tool to create a selection of select multiple

keyframes, or to move or delete them.

Use the Focus mode I-beam selector to select a range of keyframes

If you delete the keyframes in the range, the remaining section of the curve flattens out to fit the first

and last keyframe of the selection.

Automation curve after deleting the selected keyframes

Adding and Editing New Keyframes

See “Working with Audio Keyframes on the Timeline” earlier in this chapter for more information about

working with drawing and editing keyframes.

Clear All Track Automation

If you want to erase all automation on a track or bus, including all send and plugin automation, you can

do so by right-clicking the track header and selecting Clear Track Automation from the menu. A new

window will appear offering the following options for changing your mind or erasing the automation:

�Cancel: To keep your automation data.

�Reset: Clear all automation and return all affected controls and parameters to their default settings

and values.

�Hold: Clear all automation and retain the settings and values of all affected controls and parameters.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Fairlight > Automation Controls

A series of commands in the Fairlight > Automation submenu let you initiate various automation tasks.

These commands are:

�All Read: Switches all parameters that are in Trim or in Write mode back to Read mode.

�Punch In: When Preview mode is on, switches all parameters currently in Preview (blue) into

Write or Trim. When Preview mode is off, this switches all Automation-enabled parameters on all

selected channels into Write or Trim.

�Punch Out: When Preview mode is on, switches all parameters currently in Write, Trim or Preview

into Read. When Preview mode is off, this switches all Automation-enabled parameters on all

selected channels into Read.

�Fill Range: When there is an active In and Out range in the Timeline, the current value of all

parameters in Preview will be written over that range.

�Glide Range: In Preview mode, “glides” all parameters from their existing values at the In point to

the preview values at the Out point of the Timeline.

�Join Mix: Lets you manually resume writing automation in Latch mode from the current level and

moving to any other.

Automation – Copy/Paste/Erase

The Fairlight > Automation submenu also has special local choices for Copy, Paste, and Erase of

automation data. Copy/Paste allows you to do powerful range-based manipulation of automation, or to

create a “snapshot” change where all automation data is pasted for a single point in time, allowing all

enabled parameters to switch at once to new levels.

Using these commands requires that you choose which automation parameters are affected explicitly

by using the Automation Enables controls (the same ones used to choose what automation data is

recorded). For example, if you want to affect fader, mute, and pan automation, you must activate the

enables for those parameters first. Only the parameters enabled are affected.

NOTE: Clip view or Automation view (any parameter) can be used with these commands; the

choice of what is affected is governed by the Automaton Enables, not by the view.

Enables set for copy, paste, or erase of Fader, Mute, and Pan data only

�Copy: If there is an active In and Out range in the Timeline, Fairlight > Automation > Copy will copy

the automation data of all selected channels and enabled parameters within this range to the

clipboard. If there is no active In and Out range, this command copies the data of all automated

parameters on all selected and enabled data at the playhead (Snapshot mode).

�Paste: Pastes the active range or in point for all automation data copied to the clipboard for

Automation-enabled parameters.

If there is an active In to Out range defined, then the range will be filled with any automation data

copied to the automation clipboard using Automation > Copy. If there is no active In to Out range

defined, then the automation clipboard is simply pasted in its entirety.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

TIP: Track Automation can be copied between Faders, Sends, and Direct-Out levels.

For example, you can copy the Fader Level automation from one track to the Send Level

of another, and vice versa.

The contents of the clipboard can potentially target a different channel set and/or with a different

target time, just by using a new in point or track selection.

If there is an active In to Out range defined in the Timeline, and the clipboard was in

Snapshot mode when the data was copied, then this range will be filled with static values of the

snapshot data.

�Erase: If there is an active In and Out range in the Timeline, Erase will delete the automation data

of all selected channels within the range, obeying all Automation Enable buttons. If there is no

range selected, nothing is affected.

TIP: To clear all automation from a Timeline or group of tracks, select the entire timeline

range, enable the Automation Enable buttons for the types of automation you wish to

clear, and choose Fairlight > Automation > Erase. Alternatively, Fairlight > Automation >

Mix List can be used to clear all automation from the Timeline.