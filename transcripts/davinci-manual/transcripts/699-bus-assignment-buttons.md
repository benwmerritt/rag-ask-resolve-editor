---
title: "Bus Assignment Buttons"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 699
---

# Bus Assignment Buttons

To route a bus created in the Bus Assignment dialog directly on the Mixer, click the + sign to see

a dropdown menu of available busses. To route multiple busses simultaneously, Command-Click

(Ctrl+Click) each of your choices in the dropdown menu.

The Bus Outputs panel is where you can route bus signals.

Legacy Mixer Bus Assignment

In the Legacy Mixer the bus assignments have two sets of buttons that let you route audio from one

channel strip’s output to Sub and Main busses that you’ve set up for your mix.

The channel strip’s Bus Assignment buttons

�Main: These buttons let you assign a track or sub’s channels to one or more of the main busses.

�Submix: These buttons let you assign that track’s channels to one or more submix busses.

Nested Audio Timelines

Edited timelines can be combined with other timelines by dragging the desired nested timeline onto

an empty track in the destination timeline. This is a very powerful and useful feature.

For general information about nested timelines, see Chapter 43, “Take Selectors, Compound

Clips, and Nested Timelines.”

For example, you might have created a master timeline that will contain your master mix, and

you’d like to bring the work done on a separate timeline that is focused on dialogue editing.

The dialogue timeline could now appear as a single nested timeline, represented as single

track in the master mixing timeline.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Track A1, Dialogue, is a stereo representation of an edited timeline.

If you want to work with the individual tracks and clips again, you can use a process called decompose

to change that single nested timeline track back to the edited sequence. There are a number of

options to decompose to the original set of tracks, with several bussing options available.

This image shows what was a separate, edited timeline of tracks of dialogue and is now a single track,

A1 Dialogue, brought into the destination master mix timeline. By right-clicking the clip, a contextual

menu allows you to decompose the track in place, back into its original tracks and clip edits.

There are two decompose options for this. On the Fairlight page, you can Preserve Audio Data, and

when on the Edit page, you can Preserve Audio Data as well as decompose by Using Clips Only.

Decompose in Place contextual menu

Once you’ve chosen to decompose the track into its prior Timeline elements, then the Decompose

Preserving Audio Data dialog box appears, making several more options are available.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Options for signal routing when decomposing a clip

There are three options when choosing to decompose a nested timeline in the Fairlight page.

All three options preserve mix and plugin automation on the source tracks; they only differ in

terms of routing. The choices are:

New Matching Busses: All of the busses from the nested source timeline are brought into

the current timeline as separate, new busses. These busses will have all of the processing,

routings, settings, and automation carried over from the nested source timeline. Any

preexisting bus routing in the destination timeline is left unaltered.

This option is best when you want combine different mix layouts and to preserve all

preexisting bus routing in the destination timeline, while adding the bus topology from the

nested source timeline to the destination to create a single, larger entity.

Preserve Existing Paths: This option preserves all of the master bus information in the current

timeline and routes matching busses from the decomposed nested timeline to preexisting,

identical busses in the destination timeline.

This option is best when the nested source timeline and the destination timeline share

the same bus routing structure, as might be the case of a common layout template. In this

case, you just want to add the tracks to the destination timeline and route them to the

same designations in the master. You still get all of your mix automation and plugins carried

across as well.

Leave Unassigned: This option leaves the new tracks unassigned when created, ready to be

routed in whatever way you need.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Decomposed version of the nested dialogue timeline showing the original dialogue tracks and edits

Nested audio timelines can be very useful when managing large projects with many tracks

and sophisticated routing. Multiple editors can be working on various aspects at one time. For

instance, a dialogue editor could be doing the dialogue and ADR in one timeline, an effects editor

can be designing and spotting effects in another timeline, a music editor can be cutting and

spotting music in another timeline, all separately. Then these interim timelines can be imported

later to a master timeline for a final main mix.

This is also useful for picture editors who don’t want to have to deal with many tracks of audio

when cutting picture. When working in the Edit page, when a track sequence is decomposed,

it can also revert back to the original track layout with all of the audio clips ready to be

further edited.

VCA Faders

A VCA fader is used to control the level of multiple tracks with a single control. You can assign multiple

faders to a dedicated VCA, and a VCA channel strip then appears at the right of the Mixer. VCAs let

you simultaneously adjust the underlying level of multiple faders using one VCA master fader and can

be helpful in managing the levels of complex collections of audio tracks.

Group Labels in each control strip,

above the control strip label


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

The controls for doing this are found in the VCA and Group label area of each mixer channel strip,

which shows which VCA or Track Group each fader has been assigned to.

Making Fader VCA Assignments

You can assign any channel strip to one of 64 VCAs by right-clicking the VCA label area and choosing

a VCA from the dropdown that appears. If a fader is already assigned to a VCA, you can choose

“No VCA” to remove it.

NOTE: To reduce unneeded clutter, the VCA Assignment dropdown menu will only display

10 VCAs initially; others are added as needed. If the first 10 have all been assigned, the menu

display will add VCAs from the available pool, one a a time.

Right-clicking a VCA Label reveals a

dropdown menu that lets you assign faders

to or remove faders from that VCA.

TIP: You can quickly assign VCAs for a selected group of channel strips, or to all channel

strips, by holding down the Option key (Mac) or the Alt key (Windows) for all selected tracks

or Command-Option (Mac) or Control-Alt (Windows) for all mixer channel strips prior to

performing the operation. These shortcuts can save a lot of time in your workflow.

Using VCA Faders

Once you’ve assigned multiple faders to a VCA, a dedicated channel strip for that VCA appears at

the right side of the Mixer. Making adjustments to the VCA channel strip simultaneously controls all

the faders, solo buttons, and mute buttons of all channel strips that are members of that group, as

seen below.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Adjusting the VCA 1 fader also adjusts the SYNC,

VO, and Drum Hit faders that are assigned to that VCA.

When controlling faders belonging to a VCA, you can still move each individual channel strip fader

independently to make relative adjustments.

�Channel strip faders only move together when you adjust the VCA fader.

�While the VCA fader is being moved, each individual fader’s relative offset from other faders

controlled by the VCA is maintained.

For example, as seen in the screenshot above, the VCA 1 fader is moving the faders in tracks

SYNC, VO, and Drum Hit, while each individual channel strip fader in this group maintains its offset

from the others.