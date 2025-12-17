---
title: "Creating and Editing Track Groups"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 707
---

# Creating and Editing Track Groups

To create a track group, do one of the following:

�Select one or more tracks via their track headers in the Timeline. Right-click on any track you want

to include in the group and select Create Group. This also works in the Mixer on a channel strip.

�Select one or more tracks via their track headers in the Timeline. Then click the Create Group icon

in the upper-right corner of the Groups list.

Create Groups icon

In the resulting dialog, do the following:


Type a name for the group. Click the dropdown list to the right of the Group Name field to select a

group color.


Select which controls you want to include for the group (Editing, Fader, Solo, Mute, Arm, Sends,

Panning, and Automation). Click Set as Default to use these selections when creating other groups

in the future.


Select tracks in the Add Channels column on the left, then click the >> icon to add selected tracks

to the group. You can also select tracks in the Channels Added column on the left and click the <<

icon to remove those tracks from the group.


Click Save to save the group.


The new group appears in the Groups list.

Create Group - Group Settings dialog


Fairlight | Chapter 179 Track Groups

FAIRLIGHT

To activate or deactivate a group:

�Select or deselect the group in the Groups list. Selecting a group highlights it, indicating it

is active.

To rename a group:

�Double-click the group name in the Groups list.

�Type the new name you want for the group.

To edit a group:

�Hover over the group you want to edit and click on the Settings icon to open the Modify Groups

(Group Settings) dialog.

�Make any changes you wish, then choose Save.

Tools icon to launch Modify Groups dialog

To delete a track group:


Open the Tracks Index.


In the Groups list, hover over the group you want to remove, click the Trash Can icon on the right,

and then click the Delete button in the confirmation dialog.

The Mixer and Track Groups

Temporary Override (“Clutch”)

When working on the Mixer, holding down Command‑Shift (Mac) or Control-Shift (Windows) and

moving a fader or faders within a group allows them to be manipulated independently of other group

members (i.e., this is like suspending the group for just the faders that are “clutched”).

Group Management via Mixer Channel Strips

You can also manage group assignment and creation by clicking the Group name section of

any channel strip, which opens a menu with the following information and the option to create a

new group:

�Active and inactive channel groups

�A checkmark next to the group name the channel strip belongs to, if applicable.


Fairlight | Chapter 179 Track Groups

FAIRLIGHT

Group menu on a Mixer channel strip


Fairlight | Chapter 179 Track Groups

FAIRLIGHT

Chapter 180

Audio Effects

DaVinci Resolve includes Fairlight FX audio plugins and support for compatible

third-party VST and Audio Unit plugins for use in the Edit and Fairlight pages, which

let you add effects such as echo, reverb, noise reduction, and aural enhancement

to audio clips, tracks, and busses.

This chapter covers different methods of using these effects on clips and tracks.

Contents

Elastic Wave Audio Retiming������������������������������������������������������������������������������������������������������������������������������������������������������ 3923

Elastic Wave Options����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3926

Elastic View������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3926

Clearing Timing Points�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3926

About Audio Plugins������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3927

Fairlight FX�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3927

VST and VSTi �������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3927

Audio Units�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3927

Using Audio Plugins������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3928

Applying Plugins�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3929

Editing Plugin Parameters������������������������������������������������������������������������������������������������������������������������������������������������������������� 3930

Working with Plugins in the Inspector�������������������������������������������������������������������������������������������������������������������������������������� 3931

Sidechaining����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3932

Applying Audio Plugins to Busses������������������������������������������������������������������������������������������������������������������������������������������� 3933

Dealing With Processor Intensive Plugins��������������������������������������������������������������������������������������������������������������������������� 3933

Caching Audio Clips With Plugins��������������������������������������������������������������������������������������������������������������������������������������������� 3933

Exporting Audio Clips With Plugins������������������������������������������������������������������������������������������������������������������������������������������ 3934


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

Elastic Wave Audio Retiming

Elastic Wave retiming is a fast and easy keyframe-based way of dynamically retiming audio, squishing

and stretching different parts of a waveform to subtly retime audio playback for a variety of reasons, all

while maintaining constant pitch. For example, if you’re using the audio from another take to replace

that of the current take, but the performer’s timing is just a little bit different, you can use Elastic Audio

to make small adjustments to retime the second performance to match the first.

To use Elastic Wave retiming on an audio clip:


In this example, two tracks of foley effects have been recorded, and the bottom one needs to be

retimed to match the top one.


Right-click an audio clip and choose Elastic Wave retiming from the contextual menu to reveal the

Elastic Wave retiming controls.

Enabling Elastic Wave


Command-click anywhere on the clip to add speed keyframes to parts of the waveform you

want to retime by stretching or squishing. You can also place speed keyframes to lock parts of a

waveform you don’t want to retime.


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

Adding a speed keyframe with Elastic Wave retiming enabled


Dragging the speed keyframe to the left or right speeds up the audio on one side of the

keyframe and slows down the audio on the other side of the keyframe, from that keyframe to the

neighboring keyframes applied to that clip. Using an audio clip’s waveform as your guide, you

can use multiple speed keyframes to match the waveform of one performance to the waveform

of another, in order to make the timing match. Or, you can adjust speed keyframes freeform to

manipulate performances or sounds for creative effect.

You can also drag the beginning or end of an audio clip to retime that portion of the clip going

forwards or back to the next speed keyframe that’s been added.


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

Adjusting a series of speed keyframes to retime one performance to match another


If you’ve made some speed keyframe adjustments, but you find yourself wishing a speed

keyframe you created had been placed at a different position relative to the audio waveform being

adjusted, you can hold the Command key down and drag any speed keyframe to move it closer

to or farther away from a part of the waveform you want it to retime. This fine-tunes the audio

retiming adjustment occurring at that point in the clip.

(Left) Before Command-dragging a speed keyframe to be closer to the

original beginning of the sound being retimed, (Right) After


When you’re done, you can click the close button at the upper-left-hand corner to hide the Elastic

Wave retiming controls.


Fairlight | Chapter 180 Audio Effects

FAIRLIGHT

To remove Elastic Wave retiming keyframes, do one of the following:

�To remove a single speed keyframes: Right-click on a speed keyframe and choose Remove

Speed Keyframe from the contextual menu.

�To remove all speed keyframes and eliminate the Elastic Wave retiming effect: Right-click a clip

and choose Reset Speed Curve.

NOTE: All Elastic Wave retiming adjustments you make in the Fairlight page appear in the

Edit page as variable speed effects, accessible using the Retime controls. Be aware that

while all Elastic Wave retiming effects can appear as Edit page retime effects, not all Edit

page retime effects can appear as Elastic Wave retiming effects on the Fairlight page.