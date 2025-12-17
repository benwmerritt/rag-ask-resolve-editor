---
title: "Preview and Audition Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 668
---

# Preview and Audition Controls

Selecting an item in the Sound Effect list loads it into the preview player where you can play it or

audition it in your timeline using the controls underneath the search field.

�Clip name: The name of the current clip you’ve selected.

�Next/Previous buttons: Two buttons let you select the next or previous sound effect clip in the

Sound Effect list.

�Duration display: Shows the duration of the current clip, or of the section of the clip marked with

In and Out points.

�Playhead timecode display: The playhead’s current position.

�Waveform overview display: The waveform of the entire sound effect appears here, providing a

zoomed out view of the selected clip. All channels are summed together in this display.

�Zoomed in waveform display: A zoomed-in section of the selected clip that lets you see more

waveform detail for setting In, Out, and Sync points.

�Jog bar: Lets you navigate through or scrub around the clip.

�Transport controls: Play, stop and loop buttons let you control playback, although you can also

use the space bar and JKL controls. Right-click the Stop button to switch it into “Stop and Go to

Last Position” mode.

�Marking controls: The Sync Point button lets you mark a specific frame on the sound effect that

you want to sync to the Timeline’s current playhead position when you use the Audition controls.

The In and Out buttons let you mark which portions of the sound effect clip you want to edit into

the Timeline.

�Audition controls: The Audition button puts you into Audition mode, where the currently selected

sound effect clip is automatically placed at the position of the playhead in the currently selected

Timeline track. You can then move over to the timeline and listen to the clip in your mix. Cancel

and Confirm buttons let you choose whether you want to remove the clip from the Timeline and try

again with another clip, or leave the sound effect clip in.

To audition clips you’ve selected in the Sound Library in the Timeline:


Select a sound effect clip you’ve found from the list that you want to audition in the Timeline.


(Optional) In the Sound Library, use the scrubber bar to move the playhead to the part of the

sound effect that you want to sync to, and click the Sync Point button to place a sync mark on

that clip.

For example, if you’re syncing the sound effect of a car door closing, you might sync the first frame

of the door fully closed to the peak of the “slam” sound effect, rather than any door squeaking

earlier in the sound effect.


(Optional) Set In and Out points to define the range of the sound effect you want to potentially use.


Select a track you want to preview the sound effect in by clicking its track header or Mixer

channel strip.


Position the playhead at the place in the Timeline you want to place your clip.


Click the Audition button in the Sound Library. That clip now appears, temporarily, in the Timeline,

and you can play through that section of the Timeline to see how you like the sound effect in

context with the rest of the mix.


If you like the sound effect, click Confirm to keep it in the Timeline. If you don’t, click Cancel, and it

will disappear from the Timeline.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

NOTE: In order Use the Audition function, a track has to be selected first.

Additionally, if you select another sound effect after auditioning, without first confirming

the prior sound, the Audition process is cancelled, and the prior sound is removed

from the timeline.

Sound Effect List

All sound effect clips that match the current search criteria appear in this scrollable list. Double-clicking

anywhere on an item of this list plays that sound effect in its entirety.

Clip Name: The name of that sound effect file in the storage system.

Description: Any metadata that’s embedded within the files of professionally created sound

effect libraries appears here.

Duration: The duration of that sound effect file.

Audio Channel: The number of channels in that sound effect file.

Star rating: A clickable control you can use to rate sound effects within DaVinci Resolve. Star

rating information is not saved outside of DaVinci Resolve.

Waveform: The overall waveform of the entire sound effect library is stretched or compressed

within the available width of the Sound Library, regardless of the actual duration of each clip.

Index

The Index provides a handy interface for listing all of the clips in the current edit, all the tracks in the

current Timeline, and all the markers in the current Timeline. Using these lists, multiple items can be

selected, tracks can be managed, and marker notes can be consulted with ease. Each of these three

categories of information is displayed in separate panels: the Edit Index, Tracks, and Markers.

Edit Index

Displays the Edit Index as seen in the Edit page. Each audio clip in the currently open Timeline

corresponds to a row in the Edit Index, with columns for video track, Source In and Out, Record In and

Out, Name, and other descriptive metadata. All selected clips (including clips that are automatically

selected because they intersect the playhead) are selected in the Edit Index. The Option menu lets

you filter the Edit Index by various criteria, for example showing only clips with a particular color of flag,

marker, or color, only clips with speed effects, only clips with audio filters, or compound audio clips.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

The Tracks panel shows a row of information for each of the tracks in the Timeline

Tracks

Every track in the currently open Timeline corresponds to a row of controls and information in this

panel. From left to right, each track has a color control, a visibility control, a number, a name, track

controls, a format, ADC, Tags, and, if a VCA is used, the number of that VCA group. These controls

can be used to hide or show tracks, color code them, rename them, turn track controls on singly or by

dragging over several at a time, change their format, add to (or remove them from) the audio monitor

list, and rearrange them (by dragging one or more rows up and down this list) and toggle the automatic

delay compensation (ADC) on/off (on by default).

The Tracks panel shows a row of information for each of the tracks in the Timeline.

NOTE: The ADC column (automatic delay compensation) has a check box allowing the

enabling of ADC on a track-by-track basis.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Audio Monitor Checkbox

A monitor checkbox appears for each bus or track in the Tracks list. When checked, that track or

bus will appear in the Audio Monitoring dropdown menu as a choice for monitoring. All busses are

checked on by default, and will appear in the list unless unchecked here.

MPEG-H Options in the Tracks Panel

If you have MPEG-H enabled for immersive audio authoring in the preference pane of Video and

Audio I/O, additional columns appear in this panel.

When MPEG-H is enabled, the Tracks panel shows additional columns of

metadata information for defining each track in the Timeline.

These columns include:

�Track Type: Allows definition of either a static component or a dynamic object. When dynamic is

selected, the dynamic track-level pan automation from that track is also exported. Only a track can

be set to dynamic.

�Kind: A content type label, such as Mixed content, Music, Dialogue, Effect, etc. When Kind is

defined for a bus (rather than the default state of Undefined), that bus is automatically bounced

during the export process.

�Language: The content-specific language for that track.

Switch Group: Allows the track to be assigned to a user-defined switch group. A switch group

allows the track to be grouped together with other tracks in the final content, forming a selectable

item when rendered. For example, a switch group of dialogue, containing an English and a

Chinese language track, could allow the user to select between these languages on playback.

In order to define a switch group, click that track’s cell in the Switch Group column, and

choose “Sw Groups…” to open the Switch Groups Manager window, which lets you create new

switch groups.

The Switch Group Manager


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Once one or more groups has been created, they’re available for selection in the dropdown menu

of any cell in the SW Groups column. This lets you quickly make a variety of custom assignments.

The dropdown in the SW Group column

�Presets: Allows a track to be assigned to a user-defined preset. For example, a Bed Mix and

Language switch group could form one preset, while the same tracks and a spoken subtitle could

form another. In order to define a Preset, click that track’s cell in the Presets column, and choose

“Presets…” to open the Preset Manager window, which lets you create new Presets.

The Preset Group Manager

Once one or more presets has been created, they’re available for enabling in the dropdown menu

of any cell in the SW Groups column. Any track can be added to multiple presets, so the Presets

dropdown contains one checkbox per preset so you can make multiple assignments.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

The dropdown in the Presets column

Once configured, the metadata from these presets form how the content is exported in the final

deliverable, so there will be a set of presets that contain all configured components and switch groups.