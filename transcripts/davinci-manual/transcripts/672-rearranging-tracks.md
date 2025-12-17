---
title: "Rearranging Tracks"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 672
---

# Rearranging Tracks

You can rearrange tracks by right-clicking in a track’s header area and choosing either Move Track

Up or Move Track Down in the contextual menu that appears. You can also move tracks in the Index

by grabbing them and moving them to the desired position. This method works when moving multiple

tracks at once.

Duplicating Tracks

Tracks can be duplicated by right-clicking a track header and choosing “Duplicate Track” from the

contextual menu.

You can duplicate multiple tracks simultaneously by selecting them, right-clicking any track header in

the group, and choosing “Duplicate Tracks” from the contextual menu.

The names of duplicate tracks will be appended with the word “copy.”

Timeline contextual menu - Duplicate Tracks

Duplicated tracks with appended names


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

Deleting Tracks

Right-click within a track’s Timeline header and choose Delete Track. If there are clips on a track you

remove, they are also deleted from the Timeline, but preserved in the Media Pool.

Timeline contextual menu - Delete Tracks

You can delete a selection of tracks in the Fairlight timeline by right-clicking any selected track header

and selecting Delete Tracks from the contextual menu.

You can remove all empty audio tracks in the Fairlight timeline by right-clicking any track header and

selecting Delete Empty Tracks from the contextual menu.

Disabling Tracks

You can disable an audio track by right-clicking its track header and choosing Disable Track from the

contextual menu.

To disable multiple tracks simultaneously, select them, right-click any track header in the group, and

choose Disable Tracks from the contextual menu.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

Timeline contextual menu - Disable Tracks

Disabled tracks

To reenable your tracks, repeat one of the selection processes based on the number of tracks, and

choose Disable Track or Disable Tracks from the contextual menu.

Changing Track Type

If you had set up your timeline with one kind of audio track, but you discover you actually need a

different type, you can change it at any time. Just right-click anywhere in that audio track’s Timeline

header, and choose an option from the Change Track Type To submenu of the contextual menu.

Link Grouping

The Link Group function allows you to link mono tracks of material that are related and manipulate

them as a one entity controlled by a single fader on a single channel strip. Only mono tracks

can be used to create a link group; other track types such as stereo, 5.1, 7.1, Atmos, or Adaptive

cannot be used.

Unlike a multi-channel track with lanes, a link group of mono tracks functions as independent, editable

tracks in the Timeline. However, each track is mapped when choosing a track type, using one of the

standard multi-channel mappings (stereo, 5.1, 7.1, Adaptive).

Link groups are extremely useful. For example, if you’ve been given independent “.L/.R” sides of a

stereo mix, or a set of six independent related audio files that need to be assembled as a single 5.1

surround mix, or when you have surround channels that need to be specifically re-edited on a channel

by channel basis.

To create a Link Group from individual mono tracks:


Create two or more Mono audio tracks that you want to group together. If you need to create

a link group with a specific channel mapping, such as 5.1, make sure you create enough tracks

(in this case, 6).


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT


Choose Fairlight > Link Group.


When the Link Group dialog appears, mono audio tracks are represented by active buttons

(all other track types are disabled, since they can’t be linked). Click to enable the button of

every track you want to include in the link group you’re about to create. The available track type

mappings when creating your group depends on how many tracks you’ve selected.

Selecting six tracks to use for creating a link group


After you’ve selected all the tracks you need, click one of the available “Link as” buttons below.

In this example, six tracks have been selected, so you could click 5.1 Film or 5.1.

When you select enough tracks, you can create

groups linked as specific surround mappings.

Afterwards, the tracks you selected should turn into a single block, showing they’ve been linked.

The Link Group window shows the link indicator

line next to the track names.

Depending on the number of mono channels selected, Fairlight will offer possible linking

options. For instance, when ten channels have been selected, both Atmos 7.1.2 and 5.1.4 are

option choices.

The Link As option is dependent on the number of channels being linked.


Close the Link Group window when you’re finished.

Once you’ve created a link group, you’ll see a single bar on the left side of the headers, spanning

the group. If the tracks are tall enough, each will be labeled, indicating its assigned channel based

on the track mapping chosen in step 4. For example, with a 5.1 surround mapping, L, R, C, LFE, Ls,

Rs, and so on. You also have the freedom to edit additional or different contributing elements of a

surround mix into the appropriate track that represents that channel.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

Tracks in a Link Group are labeled

to identify which track corresponds

to which surround channel.

Working Separately with Multichannel Audio File Elements

If you’ve edited a multichannel audio clip onto a multichannel track, you can convert that track and its

contents into a Link Group of mono tracks, each of which contains a single clip for that track’s channel.

This can be useful if you need to fix a multi-channel surround audio clip with an incorrect track

mapping. You can convert it into a Link Group, at which point you can easily rearrange the channels.

To create a Link Group from a single multichannel timeline:

Right-click the track header of a multichannel audio track, and choose Convert to Linked Group from

the contextual menu. This automatically creates one new audio track for each channel, all of which are

linked together. For example, converting a 5.1 audio track results in six new tracks with six individual

audio clips (one for each channel), all of which are linked together.

If necessary, you can also unlink a linked group to turn it back into independent mono tracks.

To unlink a Link Group:


Choose Fairlight > Link Group.


When the Link Group dialog appears, select the link group you want to unlink.


Click Unlink.


Close the Link Group window when you’re finished.


Fairlight | Chapter 171 Setting Up Tracks, Busses, and Patching

FAIRLIGHT

SMPTE and Film order Standards

The variations of routing of the multichannel files are due to the path order of SMPTE or Film

standards. They are:

5.1 film order: L, C, R, Ls, Rs, LFE

5.1 SMPTE order: L, R, C, LFE, Ls, Rs

7.1 film order: L, C, R, Lss, Rss, Lsr, Rsr, LFE

7.1 SMPTE order: L, R, C, LFE, Lss, Rss, Lsr, Rsr