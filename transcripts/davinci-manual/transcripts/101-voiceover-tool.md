---
title: "Voiceover Tool"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 101
---

# Voiceover Tool

The Cut page in DaVinci Resolve has a dedicated voiceover and teleprompter interface, easily

accessible in the Viewer by clicking on the Voiceover icon. The Voiceover tool makes it simple to

record perfectly timed scripts directly into the Cut page timeline. You can even apply Voice Isolation

and the Dialog Leveler on the fly to get great results, even with substandard microphones and

recording environments.

Recording a VO audio track directly into the Cut Page timeline using the Voiceover tool

The Voiceover icon (red) opens the Voiceover toolset

Using Voiceover on the Cut Page

At its most basic, you can quickly “punch in” a recording using only a microphone and an In point,

but the Voiceover tool has a variety of features to make the process more precise and repeatable,

including teleprompter support and AI-based audio tools. Below is a sample setup that makes the

most out of the Voiceover features on the Cut page.


Connect an external microphone and headphones to your computer, then format a plain text (.txt)

script for your VO.


Press the Voiceover tool icon in the Viewer.


In the Voiceover settings, select your microphone interface.


Select the Audio Track you want the voiceover clip to be recorded to. By default, the Cut page

creates a new track called VO.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT


You have additional options for countdowns and to select the file folder that your voice recordings

are saved into.


Determine where in the timeline this voiceover is needed. In a simple setup, just place the

playhead at the location you want the VO to start. You can also set an In point in the timeline to

serve as a cue point that the Voiceover tool returns to for subsequent takes.


You can optionally turn on the Voice Isolation and Dialog Leveler, if you’re recording in a

substandard audio environment (for example, directly into your laptop microphone in an office

environment) to clean up your audio as you record it.


Click the Record button to start the teleprompter and recording to the selected track. The

interface will change to red to let you know you’re “on the air.”


Click Stop to end the recording. The playhead will automatically snap back to your start position,

so you can then play your new voiceover in place.

10	 If you need to try again, press the Cue button to automatically return to the In point, and press

Record again to give it another take. The new voiceover will automatically overwrite the old take

on the timeline. However, all of your previous VO takes will still be saved in the Media Pool, if you

want to go back to them.

Using the Prompter

The Voiceover tool has a build in Prompter toolset that lets you import a text (.txt) script, and during

recording the text scrolls over the picture for accurate voiceover performance and placement.

The built-in Prompter in the Voiceover tool

To use the Prompter while recording voice over:


Open and set up the Voice Over tool as described above.


In the Script Settings, enable the Prompter Overlay, and load the Script File. You have additional

settings for how the script is formatted in the Viewer.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT


You can set In and Out points on the timeline to mark the VO range for the teleprompter. The

teleprompter will then adjust its speed automatically to start scrolling at the In point, and end

at the Out point. By default, the script scroll length will cover the entire timeline if no In or Out

points are set.


When you press record, the text will scroll over the image while your voice over is being recorded.

Voiceover Settings

The Voiceover tool has several optional settings to fine tune your VO session.

Clicking on the Voiceover icon (red) opens the Voiceover toolset at the bottom of the Viewer

Voiceover Settings

�Audio Input: Select which computer interface your microphone is connected to.

�Record Track: Select which audio track in the timeline you want the VO to be recorded to.

By default, the Cut page creates a new track labeled VO, but you can manually override it to

another track in this setting.

�Monitoring:

Timeline & Microphone: Lets you hear both the timeline audio and your voice input

while you’re recording.

Timeline Audio Only: Lets you hear the timeline audio only while you’re recording.

Microphone Audio Only: Lets you hear your voice input only, and mutes the timeline

while you’re recording.

Mute Monitoring When Recording: Mutes all audio playback while you’re recording.

Useful to avoid audio feedback in certain recording setups without headphones.

�No Countdown: No visual countdown appears; when you press Record, start talking.

�3 Secs Countdown: Puts a three second visual countdown on the Viewer before the recording

begins to allow a little time to get ready first. This is a visual cue only; there are no audio beeps.

�5 Secs Countdown: Puts a five second visual countdown on the Viewer before the recording

begins to allow a little time to get ready first. This is a visual cue only; there are no audio beeps.

�Voiceover Recording File Location: Select where your new audio files are saved to.

Script Settings

�Enable Prompter Overlay: Turns on or off the text overlay for the loaded script.

�Load Script File: Opens a file selector to choose a text file to load into the prompter.

�Clear Script File: Removes the text file from the prompter.

�Font Size: Lets you choose the font size of the on screen text.

�Line Spacing: Lets you choose the line spacing of the on screen text.

�Side Margin: Lets you choose how big of a margin to use for the on screen text.

�Background Opacity: Lets you choose the transparency level of the on screen text.

�Audio Meters: A miniature set of audio meters shows your microphone’s audio levels.

�Input Monitoring: Click the headphone icon to toggle between hearing your microphone input

while you’re recording, or muting it.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

�Cue: Snaps the playhead back to the initial record In point.

�Record: Starts the audio recording into the timeline.

�Stop: Stops the audio recording.

�Voice Isolation: Activates the Voice Isolation effect as you are recording to minimize any

background noise.

�Dialog Leveler: Activates the Dialog Leveler effect as you are recording to keep a constant

volume for your track.

�Stereo Fixer: Activates the Stereo Fixer effect as you are recording to eliminate common channel

errors involved in translating between mono and stereo sources.

ATEM Switcher Integration

If you’ve recorded a multi-camera event with the ATEM Mini Pro ISO or ATEM Mini Extreme ISO,

it is possible to move that entire project into DaVinci Resolve. ATEM projects include the master

program clip, as well as each individual camera’s “ISO” (isolated) clips, and each camera angle’s audio

recordings. All transitions, timecode, and camera number metadata are imported, as well as whatever

graphics were stored in the ATEM’s Media Pool. Once the project is loaded, you can seamlessly

continue your multi-camera edit in the Cut page.

This initial live recording coupled with later post-production editing workflow is often referred to

as “Live to Tape.” Live to Tape gives you the all the benefits of the spontaneity, verisimilitude, and

fast turnaround inherent to live production but with the added benefit of being able to later add

and remove sections and adjust the editorial flow of the program. Live to Tape also allows you to

fix simple mistakes, such as choosing a better camera angle, or replacing a title or graphic with an

updated version. Because of this flexibility, Live to Tape is the preferred method of recording almost

all broadcast network game shows, current events shows, and sitcoms. Essentially, any type of multi-

camera production that does not primarily depend on being live in real time for its main purpose (like

news or sports) is shot Live to Tape instead.

The Live to Tape workflow requires the following elements, all of which are provided by the ATEM Mini

Pro ISO and ATEM Mini Extreme ISO.

�A program master clip that was shot live, including all the mixed camera angles, audio, transitions,

etc. from the beginning of the show until the end, for reference.

�Separate ISO recordings from each camera used to shoot the program master clip. An ISO is an

isolated (ISO) camera recording of the entire show from that camera’s perspective only, from the

beginning to end and without interruption.

�A timeline of the live recorded show that indicates where all the camera angles were switched,

what transitions were used, and what graphics were involved.

NOTE: The live webcam view from the ATEM is available only on MacOS.

Importing ATEM Mini Pro ISO Projects

Importing an ATEM project essentially rebuilds the master program clip as a timeline inside DaVinci

Resolve from the camera ISOs, transitions, and graphics. This new timeline will match the master

program clip in every way, just created from the original source materials rather than as a single

compressed video file.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

Refer to your ATEM’s specific documentation for how to set up ISO recording, but one important

setting is to make sure that you’ve checked the “ISO Record All Inputs” setting in the ATEM software

control before you start shooting.

To import an ATEM Mini Pro ISO Project:


(Before you shoot) Check the “ISO Record All Inputs” setting in the ATEM software control.


At this point, record your show using the ATEM device, and note the project’s folder location.


Select File > Import Project.


Select the DaVinci Resolve Project file (.drp) in the ATEM project folder, in the file browser.


Click on the Open button.

An ATEM Mini Pro project opened in the Cut page Sync bin

Relinking Blackmagic Camera Masters to ATEM ISOs

The ATEM records each camera’s ISO as an H.264 HD video stream, which may not be of high enough

resolution or quality for some purposes. It’s possible to instantly switch your ATEM camera ISOs to the

original camera recordings made in a Blackmagic Camera instead. This workflow enables the highest

visual quality of Blackmagic RAW and the ability to output in higher resolutions (such as 4K or UHD)

than are supported by the ATEM internally. Essentially, the ATEM can reference an additional set of

higher quality ISOs recorded in the cameras, rather than those from the ATEM itself. This feature is

only available using Blackmagic Cameras.

This workflow requires one more step in the process, namely making sure that you have sufficient

recording space attached to each camera to record the show in its entirety. Refer to your ATEM’s

specific documentation for how to set up ISO recording and camera control, but one important setting

is to make sure that you’ve checked the “ISO Record All Inputs” and the “Record in All Cameras”

settings in the ATEM software control before you start shooting.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

To relink to Blackmagic Camera masters from ATEM ISO recordings:


(Before you shoot) Check the “Record in All Cameras” setting in the ATEM software control.


(Before you shoot) Check the “ISO Record All Inputs” setting in the ATEM software control.


At this point, record your show using the ATEM device and note the project’s folder location.


Copy all the resulting camera masters from each camera’s memory card to the ATEM project’s

“Video ISO Files” folder, and then import the project into DaVinci Resolve.


DaVinci Resolve automatically creates a separate Blackmagic RAW folder in your project and

moves all the camera masters to that folder.


Use the menu Timeline > Switch to Camera Originals to instantly switch between referencing the

ATEM H.264 ISOs and the Blackmagic Camera masters.

Once your project is imported successfully into DaVinci Resolve, it can be edited using the variety of

specialized Multicam editing tools found in the Cut page, including the Sync Bin, Live Overwrite, and

the DaVinci Resolve Speed Editor.

For more information on using these tools, see Chapter 28, “Fast Editing in the Cut Page.”


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT