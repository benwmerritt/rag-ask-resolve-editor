---
title: "Track Mode"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 691
---

# Track Mode

When working with audio tracks or busses (Track mode) the Audio tab lets you adjust the volume level

and enable and adjust Fairlight Track FX.

For more information on Fairlight Track FX, see Chapter 181, “Fairlight FX.”


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

Audio tab - Track mode

NOTE: Parameters for locked tracks cannot be edited in the Inspector. For more information

on locking audio tracks, see Chapter 175, “Editing Basics in the Fairlight Page.”

The Effects Tab

Audio Effects added to a track or bus via the Effects section of its Mixer channel strip or to a timeline

clip from the Effects Library will appear in this tab.

Fairlight FX Delay controls in the Effects tab

For more information, see Chapter 180, “Audio Effects.”


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

The Transition Tab

If you’ve applied any Transitions (Crossfade) between clips in either the Edit or Fairlight pages, you can

adjust them in the Transition tab, which can be opened by double-clicking a Crossfade transition.

Crossfade controls in the Transition tab of the Inspector

The following properties can be edited:

�Transition Type: The currently selected transition. You can change to any other installed transition

by selecting one in the dropdown menu.

�Duration: The duration of the transition, shown in both seconds and frames.

�Alignment: A dropdown that lets you choose the transition’s position relative to the edit point it’s

applied to. Your choices are “Start on Edit,” “Center on Edit,” and “End on Edit.”

�Fade In: This dropdown offers selection from -3dB to 3dB.

�Fade Out: This dropdown offers selection from -3dB to 3dB.

For more information on adjusting crossfades, see Chapter 175, “Editing Basics in the

Fairlight Page.”

The File Tab

The File tab includes different sections where you can view or edit the properties and configuration of

audio clips on the Timeline and in the Media Pool.

File Information

In addition to the name of the audio clip, this section of the File tab provides additional details about

the file, as shown in the screenshot below.

File tab - File Information section


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

Metadata

Except for the embedded Timecode field, every text field can be edited with information of

your choice.

File tab - File Metadata section

Auto Select Next Unsorted Clip

When this box is checked, pressing the Return key after filling in a metadata field selects the next

Media Pool clip with the cursor in the same field.

This allows rapid sequential metadata entry without clicking the Next Clip button or manually clicking

the next Media Pool clip.

Auto Select Next Unsorted Clip checkbox and Next Clip button

Whenever a Media Pool clip is selected, the name displayed to the right of the Clip and Track

and Mode buttons will begin with “Media Pool – “.

File tab - Media Pool clip selected


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

Audio Configuration

This section of the File tab includes features and controls that let you intuitively change an audio clip’s

channel properties. These changes determine the number of active channels in the clip and their

individual source and volume levels when inserted into the Timeline.

The appearance of the Audio Configuration pane will vary depending on the format of the clip

you’re trimming. For example, the screenshots below depict a 6-channel clip in the Media Pool

in two different channel formats.

6-channel adaptive - Media Pool clip

6-channel mono - Media Pool clip

�Format: When an audio clip is selected in the Media Pool, the Format dropdown displays its current

channel format, standard channel configurations, and a Custom option. You can apply these

channel configurations to the clip without having to use the Clip Attributes to customize the clip.

Format dropdown menu - for a 6-channel adaptive clip

When a timeline clip is selected, the Format dropdown displays its current channel format and the

Custom option. However, the timeline clip is comprised of two mono channels; it is possible to

change the audio sources for each channel.

Choosing the Custom option opens the Audio tab of the Clip Attributes dialog.


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

For more information on using the Clip Attributes dialog, see Chapter 22, “Modifying Clips

and Clip Attributes.”

�Waveforms: When working with a Media Pool clip, the first waveform beneath the Format

dropdown displays a composite of all channels within the audio file. The remaining waveforms

represent the audio content of each channel within the clip.

The composite waveform is not available when working with timeline clips.

You can listen to the audio by skimming it with your mouse cursor, clicking the Play button in the

transport control below the last waveform, or pressing the spacebar.

If you click anywhere within any waveform, playback will continue playing the audio from that

point. This concept is explained in more detail in the Transport Controls section below.

�Channel Controls: When working with source clips in the Media Pool, each clip channel has its

own Enable/Disable checkbox and Mute button.

�Active/Inactive: Filling in the checkbox enables the channel, making it active and available for

editing operations. Conversely, when the checkbox is empty, the channel is unaffected by editing

operations, as if it were removed from the clip.

Using the example of a 6-channel mono clip in the Media Pool, if you deactivate channel 2, only

five tracks (1, 3, 4, 5, and 6) will be included when it’s dragged from the Media Pool to the Timeline.

6 mono channel Media Pool clip

�Mute: Clicking this button mutes the channel while leaving it in place within the clip. So, in the case

of the six-channel Media Pool clip, if you filled in the checkbox for channel two and then activated

the Mute button, all six channels will be included when the clip is dragged onto the Timeline, but

only channels 1, 3, 4, 5, and 6 will be audible.

TIP: Option-clicking a Mute button or Active/Inactive checkbox toggles all others to the

opposite state, effectively soloing the channel you are interacting with.


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

�Channel Source: When working with multichannel clips comprised of all mono channels, the Audio

Configuration pane will include a dropdown displaying the name of the current audio source of

each waveform. Clicking the dropdown lets you choose from a list of mono audio sources.

This is useful if, for example, you need to change the signal for a person’s lavalier mic to another

or the boom mic channel has a loud noise because it was bumped during a take and needs to be

changed to another source.

Audio Channel Source menu

Changing the Channel Source on the Timeline

To change an audio source on the Timeline, right-click the audio channel you need to correct and

select an option from the list at the bottom of the contextual menu.

Audio Channel Source menu - Timeline menu

A quicker way to access these options is to Command right-click the audio channel in question.

Audio Channel Source menu - Simplified Timeline menu

�Transport Controls: Once the playback has been started using the Play button, clicking anywhere

within a waveform effectively “solos” that channel and continues playing the audio from that point.

If you are working with a Media Pool clip, clicking anywhere within the composite waveform lets

you hear the mix of enabled and unmuted channels from that point.

When working with a timeline clip, you can switch to hearing all channels by clicking the Stop

button followed by the Play button.

�Level: This control becomes active once one or more channels are selected and is used to trim

the level of individual channels of multichannel Media Pool or timeline clips.


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

This feature can be helpful when one or more channels aren’t loud enough and needs to be

trimmed to match the other channels.

Trim adjustments made within timeline clips are independent of their clip gain and do not affect

their corresponding Media Pool clip.

TIP: Command or Shift-clicking to select multiple channels lets you simultaneously trim

all channels in that selection. However, it’s important to note they will all be trimmed by

the same amount (in dB).