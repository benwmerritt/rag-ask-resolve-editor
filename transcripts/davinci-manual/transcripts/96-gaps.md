---
title: "Gaps"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 96
---

# Gaps

Because Track 1 is meant to hold the principal clips for your program, the Timeline automatically ripples

itself to close gaps that would otherwise result when you move or rearrange clips in Track 1, and

superimposed clips in Tracks 2 and above move to keep in sync with the clips they’re superimposed

over. However, you can move superimposed clips on Tracks 2 and above to place them wherever you

want, and gaps will be left between multiple clips on the same superimposed track so they can be

edited at specific places.

Timeline Controls

The Timeline controls in the upper left-hand corner of the Timeline let you enable/disable Rippling on

Track 1, enter Dynamic Trim mode, Split a clip at the playhead position, create Markers, and open the

Keyframe Editor.

The Cut page Timeline controls

Audio Mixer

The Cut page can show a full Audio Mixer, with access to all the tracks and busses of your mix, in

addition to shortcuts to any audio Track FX, Dynamics, and Equalizer tools. To enable the Audio Mixer,

select the Mixer tab at the top of the Cut page.

The Audio Mixer in action during Cut page playback

A unique feature of the Cut page Audio Mixer is the ability to expand it fully using the Expand icon in

the upper right of the Mixer. This will replace the whole lower timeline with the Mixer, giving you plenty

of room to monitor complex audio compositions, while still being able to access the editing functions

of the Upper Timeline.


The Cut Page | Chapter 26 Using the Cut Page

CUT

The Audio Mixer expanded, allowing you to see all audio tracks while still editing in the Upper Timeline of the Cut page.

Audio Mixer Controls

Each track’s channel strip has the following controls:

�Track Number: The number of the timeline audio track corresponding to each channel strip

appears here.

�Track Effects: Double-click on one of the track effects at the top of the fader controls to open.

FX: Opens the Track Effects controls in the Inspector.

EQ: Opens the Track Equalizer.

DY: Opens the Track Dynamics.

�Pan control: Lets you pan a Mono track’s audio from left to right, or invert a Stereo track’s left and

right audio channels, or do surround mixing.

�Name: The name of the audio track that channel strip corresponds to. If you’ve edited the audio

track names in the Timeline, those names will appear here.

�Solo: Mutes all tracks other than ones that are soloed.

�Mute: Disables that audio track.

�dB: Shows you the volume, in decibels, that track is currently set to.

�Fader: Each track’s vertical fader can be dragged with your mouse or other pointing device to

adjust the volume of that track and perform automation recording. Dragging up increases volume,

dragging down decreases volume.

�Audio meters: Audio meters to the right of each fader display the audio volume of all channels on

that track during playback. Each channel strip has individual meters corresponding to the number

of channels that track has been set to accommodate.


The Cut Page | Chapter 26 Using the Cut Page

CUT

Mute and Solo Tracks For Output

When you use the Mute or Solo controls of the Audio Mixer, track audio is disabled, both during

playback and delivery for output. Make sure you have re-enabled any tracks you need before heading

to the Deliver page. You can only modify mute and solo tracks on the Edit, Cut, and Fairlight pages.

Replay

The Cut page allows live multi-camera broadcast editing, playout, and replay with speed control.

Some of the Replay features are only available with Blackmagic Design hardware, such as a desktop

video interface, cloud store and ATEM switcher.

Please see the dedicated DaVinci Resolve Replay Editor Instruction Manual for more

information.

The Cut page Timeline controls

Undo and Redo in DaVinci Resolve

No matter where you are in DaVinci Resolve, Undo and Redo commands let you back out of

steps you’ve taken or commands you’ve executed, and reapply them if you change your mind.

DaVinci Resolve is capable of undoing the entire history of things you’ve done since creating or

opening a particular project. When you close a project, its entire undo history is purged. The next time

you begin work on a project, its undo history starts anew.


The Cut Page | Chapter 26 Using the Cut Page

CUT

Because DaVinci Resolve integrates so much functionality in one application, there are three separate

sets of undo “stacks” to help you manage your work.

�The Media, Edit and Fairlight pages share the same multiple-undo stack, which lets you backtrack

out of changes made in the Media Pool, the Timeline, the Metadata Editor, and the Viewers.

�Each clip in the Fusion page has its own undo stack, so you can undo changes you make to the

composition of each clip, independently.

�Each clip in the Color page has its own undo stack, so you can undo changes you make to grades

in each clip, independently.

In all cases, there is no practical limit to the number of steps that are undoable (although there may be

a limit to what you can remember). To take advantage of this, there are three ways you can undo work

to go to a previous state of your project, no matter what page you’re in.

To simply undo or redo changes you’ve made one at a time:

Choose Edit > Undo (Command-Z) to undo the previous change.

Choose Edit > Redo (Shift-Command-Z) to redo to the next change.

You can also undo several steps at a time using the History submenu and window. At the time of this

writing, this only works for multiple undo steps in the Media, Cut, Edit, and Fairlight pages.

To undo and redo using the History submenu:


Open the Edit > History submenu, which shows (up to) the last twenty things you’ve done.


Choose an item on the list to undo back to that point. The most recent thing you’ve done appears

at the top of this list, and the change you’ve just made appears with a check next to it. Steps

that have been undone but that can still be redone remain in this menu, so you can see what’s

possible. However, if you’ve undone several changes at once and then you make a new change,

you cannot undo any more and those steps disappear from the menu.

The History submenu, which lets you undo several steps at once

Once you’ve selected a step to undo to, the menu closes and the project updates to

show you its current state.


The Cut Page | Chapter 26 Using the Cut Page

CUT

To undo and redo using the History window:


Choose Edit > History > Open History Window.


When the History dialog appears, click an item on the list to undo back to that point. Unlike

the menu, in this window the most recent thing you’ve done appears at the bottom of this list.

Selecting a change here grays out changes that can still be redone, as the project updates to

show you its current state.

The Undo history window that lets you browse the

entire available undo stack of the current page


When you’re done, close the History window.


The Cut Page | Chapter 26 Using the Cut Page

CUT