---
title: "Beat Detector (Studio Version Only)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 181
---

# Beat Detector (Studio Version Only)

DaVinci Resolve can automatically detect beats for a piece of music on the timeline, and supports

snapping to these beat marker locations. This can be especially useful when trying to make edits

to the beat.

NOTE: The Beat Detector will only work effectively with beat-driven music, and with 4/4 or

3/4 time signatures at this time.

To detect beats, right-click on the timeline audio clip and select Detect Music Beats from the context

menu. Once analyzed, the timeline clip displays beat indicator overlays that you can snap other

timeline elements to.

A music track with the Beat Detector applied. The lined overlays match up with the beat of the music.

Dialogue Matcher (Studio Version Only)

Dialogue Matcher allows you to match one piece of dialogue to another, matching level, EQ, and

reverb. This can help with situations where new recordings may not match the environment of existing

ones. The Dialogue Matcher is a fully automated tool that only requires the user to capture a tone

profile from a clip and then to apply it to another.

Capturing a Dialogue Profile from a clip using the main menu


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

To Use Dialogue Matcher:


Select a reference clip whose dialogue you want to match, right-click, and choose Clip > AI Tools >

Dialogue Matcher > Capture Dialogue Profile.


Select the clip whose dialogue you want to change, right-click and choose Clip > AI Tools >

Dialogue Matcher > Apply Dialogue Profile.


You can enable or disable the Dialogue Matcher on a clip by right-clicking and choosing Clip > AI

Tools > Dialogue Matcher > Enable.


You can Remove the Dialogue Matcher on a clip by right-clicking and choosing Clip > AI Tools >

Dialogue Matcher > Remove Applied Profile.

Audio Assistant (Studio Version Only)

With the Audio Assistant, DaVinci Resolve can automatically organize and color-code your tracks, even

out your dialogue levels, and adjust the mixer faders to create a professional-quality mix of your music,

sound effects, and dialogue.

During this process, your dialogue will also be cleaned up, and if needed, Voice Isolation and De-

Essing will be applied. Ducking will be applied to music tracks, any required automation will be written,

and the appropriate mastering and finalizing plugins will be added and adjusted to help achieve the

correct loudness level for your chosen delivery standard.

To use AI Audio Assistant:


Open a timeline containing unmixed audio. The initial fader levels really don‘t matter as

Audio Assistant will handle all fader adjustments during the mixing process.


To begin the automatic mixing process, choose Timeline > AI Tools > Audio Assistant from the

Timeline menu, select the Delivery Standard for your mix from the dropdown menu, and click the

Auto Mix button.


The Audio Assistant dialog changes to display the progress of the mixing process with an option

to cancel it.

Audio Assistant dialog - Delivery Standard

Audio Assistant dialog -  Mix Progress


When the mixing process has concluded, you can play back the mix and, if needed, make further

adjustments or completely undo it.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

NOTE: If a track is in the wrong category, right-click the corresponding track header and

choose the correct category from the Track Category section of the contextual menu, and

then rerun the Audio Assistant.

The Audio Mixer

The Audio Mixer on the Edit page is a simplified version of the Mixer on the Fairlight page, designed to

provide a streamlined set of graphical controls you can use to set basic track levels (there is no track

level fader automation on the Edit page), pan stereo audio at the track level, and mute and solo tracks

as you work.

To open the Audio Mixer, do the following:

Click the Mixer button on the Interface toolbar.

The Audio Mixer exposes a set of channel strips with controls that correspond to the tracks in the

Timeline, and each channel strip displays a number of audio meters equal to the number of channels

within that track. By default, a Main 1 channel strip appears all the way to the right that lets you adjust

the overall level of the mix. However, if you add subs and mains on the Fairlight page, those will

appear at the right of the mixer as well.

The Audio Mixer, with four channel strips corresponding

to the four tracks in the Timeline


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

NOTE: You cannot record automation in the Edit page. Comprehensive mixing controls with

full automation recording are found in the Fairlight page.

Audio Mixer Controls

Each track’s channel strip has the following controls:

�Track Color: Each track can be differently color-coded to help you keep organized. These colors

also appear in the timeline track header and the Fairlight page.

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

Mute and Solo Tracks For Output

When you use the Mute or Solo controls of the Audio Mixer, track audio is disabled both during

playback and delivery for output. Make sure you have re-enabled any tracks you need before heading

to the Deliver page. You can only modify mute and solo tracks on the Edit, Cut, and Fairlight pages.

Displaying Audio Meters

If you just want to see your program’s levels, you can also switch to display the “Control Room”

audio meters instead of the Mixer. How many audio meters appear depends on the current speaker

configuration in the Video and Audio I/O panel of the System Preferences.

To show the Audio Meters:

Click the Mixer button on the Interface toolbar to display the audio panel and then choose

Meters from the option menu at the upper right-hand corner.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Audio Compound Clips

DaVinci Resolve supports audio compound clips, which are created just like any other compound

clip, by selecting multiple audio clips, right-clicking one of them, and choosing New Compound Clip.

Alternately, compound clips with video clips may now contain multiple audio items as well.

When compound clips containing audio are opened in the Edit or Fairlight pages by right-clicking

an audio compound clip and choosing Open in Timeline, breadcrumb controls appear beneath the

Timeline that let you exit the compound clip and get back to the master Timeline.

Opening an audio compound clip

Audio Playback for Variable Speed Clips

Video/audio clips with variable speed effects applied to them can now play either pitch-corrected or

un-pitch-corrected variable speed audio. An option in the Speed menu of the Retime controls lets you

choose whether or not the audio is pitch-corrected.

Using Audio Filters

DaVinci Resolve includes Fairlight FX, a set of DaVinci Resolve-specific audio plugins that run natively

on macOS, Windows, and Linux, providing high-quality audio effects with professional features to all

DaVinci Resolve users on all platforms. Additionally, DaVinci Resolve supports the use of third-party

VST audio plugins on Mac OS X and Windows. On Mac OS X, DaVinci Resolve supports Audio Unit

(AU) audio plugins. Once you install these effects on your workstation, they appear in the Audio FX

panel of the Effects Library.

Audio plugins let you apply effects to individual audio clips or entire tracks worth of audio, to add

creative qualities such as echo or reverb, or to take care of mastering issues using noise reduction,

compression, or EQ.

Methods of applying audio filters to clips in the Edit page:

�To apply an audio filter to a clip: Drag any filter from the Audio FX panel of the Effects Library

onto the clip in the Timeline you want to apply it to.

�To apply an audio filter to multiple clips: Select all of the clips you want to apply an audio filter to,

then drag any filter from the Audio FX panel of the Effects Library onto any of the selected clips.


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

Audio filters in the Effects Library

To edit a clip’s audio filters:

�Select that clip and open the Inspector. All audio filters applied to that clip appear under the

Effects panel, in the Audio tab, with that filter’s controls appearing directly in the Inspector.

Many VST and Audio Unit audio filters have a custom user interface that makes it much easier to

manipulate that filter’s controls. These can be opened from within DaVinci Resolve.

The custom audio filter interface for iZotope RX4


Edit | Chapter 45 Working with Audio in the Edit Page

EDIT

To expose a filter’s custom controls:

�Click the Custom Control button (the button to the right of the trash can). The custom

controls appear in a floating window. When you’re finished adjusting the custom controls,

close the window.

The button for opening a filter’s custom control

Methods of working with audio filters in the Inspector:

�To disable or re-enable a filter: Click the toggle button at the far left of each filter’s title bar.

�To remove a filter: Click the Trash Can button.

Once applied to a clip or track, audio filters can also be keyframed or automated just like volume and

pan settings, to create dynamic audio effects that change over time.