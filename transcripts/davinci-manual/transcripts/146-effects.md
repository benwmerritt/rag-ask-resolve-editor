---
title: "Effects"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 146
---

# Effects

The Effects Inspector controls

Any Fusion FX, Open FX, or Audio FX filters that have been applied to a clip can be modified here in

their respective tabs. Different effects in the Timeline expose different controls in the Effects panel.

Whichever panels are exposed, parameters within each panel are organized into groups, with a title

bar providing the name of that group, along with other controls that let you control all parameters

within that group at the same time.

These controls include:

�Enable button: A toggle control to the left of the parameter group’s name lets you disable

and re-enable every parameter within that group at once. Orange means that track’s enabled.

Gray is disabled.

�Parameter group title bar: Double-clicking the title bar of any group of parameters collapses or

opens them. Even more exciting than that, Option-double-clicking the title bar of one parameter

group collapses or opens all parameter groups at once.

�Keyframe and Next/Previous Keyframe buttons: This button lets you add or remove keyframes at

the position of the playhead to or from every single parameter within the group. When the button

is highlighted orange, a keyframe is at the current position of the playhead. When it’s dark gray,

there is no keyframe. Left and right arrow buttons let you jump the playhead from keyframe to

keyframe for further adjustment.

�Reset button: Lets you reset all parameters within that group to their default settings.

�Use Alpha: Checking this box applies the Open FX alpha channel to the selected clip,

compositing it over any background elements that appear in lower tracks. If more than one alpha-

modifying effect is applied to a single clip, the alpha channels are mixed together.

For a detailed explanation of each of the Resolve FX plugins that accompany DaVinci Resolve,

see Part 12, “Resolve FX Overview.”


Edit | Chapter 37 Using the Inspector in the Edit Page

EDIT

Transition

The Transition Inspector controls

Double-clicking a transition in the Timeline opens that Transition Panel in the Inspector. Each transition

has the following properties you can edit.

�Transition Type: The currently selected transition. You can change to any other installed transition

by selecting one in the drop-down menu.

�Duration: The duration of the transition, shown in both seconds and frames.

�Alignment: A drop-down that lets you choose the transition’s position relative to the edit point it’s

applied to. Your choices are “Start on Edit,” “Center on Edit,” and “End on Edit.”

Additional properties that are specific to each type of transition appear in another group below.

Since the Cross Dissolve transition is the most common transition used, its properties will be shown as

an example.

�Style: The different Dissolve transitions (Cross Dissolve, Additive Dissolve, and so on) expose this

drop-down that lets you choose different ways for the outgoing clip to blend into the incoming clip

during the dissolve. There are six different options to choose from:

Video: A simple linear dissolve; the outgoing clip fades out as the incoming clip fades in.

Film: A logarithmic dissolve, simulating film dissolves as created by an optical printer.

Additive: The outgoing and incoming clips are cross faded using the Additive composite mode. As

a result, the transition seems to brighten at the halfway point.

Subtractive: The outgoing and incoming clips are cross faded using the Subtractive composite

mode. As a result, the transition seems to darken at the halfway point.

Highlights: The outgoing and incoming clips are cross faded using the Lighten composite mode.

The lightest parts of each clip are emphasized during this transition.

Shadows: The outgoing and incoming clips are cross faded using the Darken composite mode.

The darkest parts of each clip are emphasized during this transition.

�Start Ratio: Defines the percentage of completion for the transition at its first frame, from

0 to 100 percent. Setting the Start Ratio to anything but 0 results in the transition immediately

appearing at a more fully cross-dissolved state from the very first frame.

�End Ratio: Defines the percentage of completion for the transition at its last frame. Setting the

End Ratio to anything but 0 results in the transition never fully dissolving to the incoming shot at

its last frame.

�Reverse: Reverses the transition. This parameter is disabled for Dissolve transitions.


Edit | Chapter 37 Using the Inspector in the Edit Page

EDIT

�Ease: A drop-down that lets you apply nonlinear acceleration to the beginning, ending, or overall

duration of a transition. The result is to add inertia to the transition from the outgoing clip to the

incoming clip, providing a gentler change from each clip into and out of the transition.

None: The outgoing clip fades away to the next shot in a linear fashion.

In: The outgoing clip lingers as the beginning of the transition dissolves more slowly than the end.

Out: The outgoing clip fades away more quickly as the beginning of the transition dissolves more

quickly than the end.

In & Out: Both the outgoing and incoming clips make slower transitions at the beginning and end

of the dissolve, but the very center of the transition is faster as a result.

Custom: Lets you modify the parameters of the fade manually using the Transition Curves below.

�Transition Curve: Allows you to manually set keyframes controlling the progress of the transition

along its duration.

Other types of transitions display properties that are specific to that transition’s particular effect.

For a detailed explanation of each of the transitions that accompany DaVinci Resolve, see

Chapter 48, “Using Transitions.”

Image

The Image Inspector controls for BRAW footage

The Image panel contains groups of parameters that correspond to every camera raw media format

that’s supported by DaVinci Resolve. Using these parameters in the Image panel, you can override

the original camera metadata that was written at the time of recording and make simultaneous

adjustments to camera raw media throughout your project.


Edit | Chapter 37 Using the Inspector in the Edit Page

EDIT

For a detailed explanation of each of the RAW camera parameters supported by

DaVinci Resolve, see Chapter 7, “Camera Raw Settings.”

File

The File Inspector controls

Metadata

The File panel of the Inspector provides a consolidated way to view and edit a subsection of a clip’s

most commonly used media file metadata. It’s easily accessible in the Inspector across the Media,

Cut, Edit, and Fairlight pages.

The tab is composed of the following parts:

�Clip Details: Presents data about the clip’s data format (codec, resolution, frame rate, etc.).

�Metadata: Presents a reduced set of common metadata fields for quick user entry.

Timecode: The start timecode of the clip. This field is editable if you want to manually change the

clip’s starting timecode.

Date Created: The date that the clip was created. This field is editable if you want to manually

change the clip’s creation date.

Camera: Sets the Camera # metadata.

Reel: Sets the Reel/Card ID.

Scene: The Scene number of the clip.

Shot: The Shot letter/number of the clip.

Take: The Take number of the clip.


Edit | Chapter 37 Using the Inspector in the Edit Page

EDIT

Good Take: This checkbox indicates if the clip is a good or circled take.

Clip Color: Assign a specific color to a clip that is reflected in the Timeline.

Name: This can be entered manually and changes a clip’s name in that specific timeline only.

Comments: Add a text description to the clip.

Auto Select Next Unsorted Clip: When this box is checked, the next clip in the Media Pool

is selected when you hit the Return button after entering a metadata field, and the cursor is

automatically placed in the same field. This allows rapid sequential metadata entry without having

to manually click to load each individual clip in the Media Pool. The Next Clip button will select the

next clip in the Media Pool, regardless of the checkbox status.

Audio Configuration

The File tab in the Inspector now has an Audio Configuration pane that handles the controls that were

formerly handled by Clip Attributes in the Media Pool (though that option is still available). The Audio

Configuration pane provides a more intuitive and visual way of changing the track properties of an

audio clip. Simply click on an audio clip in the Media Pool or Timeline, and then on the File Inspector to

reveal this interface.

The Audio Configuration panel. Track 3 has been

muted and Track 5 has been disabled.

The pane features a per-channel waveform display for all tracks within a multichannel audio file. If the

tracks have been named in the audio recorder, these names will appear over their respective tracks as

well. The Audio Configuration panel can preview up to 36 tracks of audio.

At the top of the pane, a composite waveform is shown of all the tracks and is updated depending

on the mute status of individual tracks. By default this composite is heard when the Play button is

activated, and all channels are audible.


Edit | Chapter 37 Using the Inspector in the Edit Page

EDIT

A format menu allows you to choose common configurations for your source audio file without

cumbersome manual re-routing. Custom routing can still be accommodated by choosing

custom in the drop-down, which brings up the older clip attributes for situations that require less

common configurations.

Audio for a selected source or timeline clip can be played or skimmed by moving the cursor along the

waveform, and the specific track is solo’ed when skimming or playing. The play position or track being

monitored can also be switched dynamically during playback. For example, you can start playback on

track one, then simply click on track two, and the playback continues from that position. These controls

let you quickly skim through and identify exactly what audio is on which track for further adjustment.

Each track has two adjustments that can be made, an Enable/Disable checkbox and a

Mute button.

Enable/Disable: Enabling a track makes that track available for use in editing operations.

Disabling a track removes that track from use in editing operations. For example, if you disable

Track 2 of a 4-track audio file, when you drag that audio file from the Media Pool into the

timeline, only 3 tracks (1, 3, and 4) will come over.

These adjustments can only be made on Media Pool clips; audio clips already in the timeline

will have these options disabled.

Mute: Clicking this icon will mute the track so it is unheard but leave the actual track in place

when used in editing operations and dragged into the timeline. Option clicking a mute button

on a channel will allow you to solo by muting all other channels.

Underneath the track layout is a simple transport control comprised of Play and Stop buttons

to start and stop audio playback.

Adjusting Trim Levels of Individual Channels in a Source File

The level of individual source clip channels in the audio inspector can be be adjusted via a trim

control. This allows source clip audio in one channel to be brought up in level or brought down in level,

as needed.

The trimmed level is internal to source clip in the Media Pool and will be inherited whenever that

source clip configuration is used on a timeline, unless it is changed.

NOTE: The trim level is totally separate from clip gain in the timeline. Be aware that trimmed

levels can clip if you move them too high.


Edit | Chapter 37 Using the Inspector in the Edit Page

EDIT

You can adjust the trim levels of individual

audio channels in a multichannel clip.

Using the Trim slider


Select one or more channels in the Audio Configuration section of the File Inspector.


Adjust the Level slider at the bottom to the desired audio level.

The waveform will adjust dynamically to the level value and will display a trimmed value in dB in the

channel itself. If you have multiple lanes selected, all channels will be trimmed together. Relative levels

are not stored, so if you adjust one, it will then force any others in the selection to match. When no

channel lanes are selected, the Level control is grayed out.

Multiple Clip Selection and Adjustments

You can select multiple audio clips and adjust their properties in the Audio Configuration pane.

For example, you can select a group of audio files and remove Track 2 from all of them at once.

However the following should be noted:

•	 In a multiple clip selection, only the last selected clip will appear in the track layout of the

Audio Configuration pane. However the top composite waveform will be named “Multiple

Clips” to let you know that more than one clip has been selected.

•	 Any adjustments, like muting or enabling/disabling a track will be applied to all the

selected clips at once.


Edit | Chapter 37 Using the Inspector in the Edit Page

EDIT

Timecode

The File tab in the Inspector now has a Timecode pane that handles the types of controls that were

formerly handled by Clip Attributes in the Media Pool (though that option is still available). Here you

can override the timecode details for a clip or clips in the Media Pool.

�Current Frame: Lets you assign a new time for the timecode at the currently viewed frame

of the clip.

�Slate: In situations where source media comes from a shoot where a timecode slate was used

during the shoot, then you can assign the slate timecode as a second timecode track that can be

used for various operations, without changing the primary timecode of the clip, which may already

be in use for program sync.

To set appropriate Slate timecode, select a clip in the Media Pool with a visible timecode slate, and

move the playhead to a frame where the timecode in the slate is clearly readable. Then, open the

Timecode panel of the Clip Attributes window, and type the timecode value you see in the image

into the Slate Timecode field.

�Offset Source: If an entire set of clips has timecode that’s merely offset, you can correct the

timecode offset for as many selected clips as you like.


Edit | Chapter 37 Using the Inspector in the Edit Page

EDIT