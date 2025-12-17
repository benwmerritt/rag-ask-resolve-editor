---
title: "Lower Timeline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 95
---

# Lower Timeline

The zoomed in Lower Timeline (often referred to simply as “the Timeline”) shows you a close-up view

of the portion of the currently open timeline that immediately surrounds the playhead. The zoom level

is fixed; you cannot change it. The zoomed-in lower timeline is intended for detailed editing, but clips

can be dragged between the Timeline and Upper Timeline for fast reordering of clips across the entire

duration of your program.

The Toolbar contains several editing functions grouped together in Action and Option menus.

These functions are accessed by clicking on the appropriate icon and selecting a function from the

drop‑down menu. These tools are discussed in detail throughout the Cut section of the manual.

The Toolbar icons (from left to right):

Timeline Options, Timeline Actions, Edit Actions

Timeline Options

The tools under this icon deal with how the clips and timeline are displayed, and certain modes and

tools that apply to the whole timeline.

All of the Timeline Options functions


The Cut Page | Chapter 26 Using the Cut Page

CUT

�Ripple On: Toggles ripple editing behavior on track V1.

�Snap: Toggles the playhead snapping behavior on or off.

�Trim to Audio: Opens an expanded audio view on the timeline when trimming a clip.

�Trim with Safe Edit: Toggles the Safe Edit function to prevent you from accidentally overwriting

adjacent clips while trimming.

�Display Clip Names: Toggles displaying the clip name on the timeline clip.

�Display Clip Status: Toggles displaying the status icons of various operations on the timeline clip.

�Display Speed Keyframes: Toggles displaying the Speed Keyframes on a clip with speed

changes applied.

�Viewer Background: Lets you choose how the blank areas of the Viewer background are

displayed, either Checkerboard, Black, Gray, or Alert Red.

�Set Default Transition: Opens the Set Default Transition window, letting you choose the transition

type, duration, and alignment for the default transition.

�Edit Using (Audio Track): Lets you choose either All audio tracks or select specific audio pairs to

edit with on the Cut page.

�Minimize Subtitle Track: Shrinks the vertical size of the subtitle tracks to give you more room in

the timeline.

�Fixed Playhead: Toggles the fixed playhead on or off. On leaves the playhead in place while the

timeline passes underneath it, while off makes the playhead move along the timeline.

�Boring Detector: Activates the Boring Detector.

Timeline Actions

The tools under this icon are generally used to add new items or make modifications to the Timeline.

All of the Timeline Actions functions


The Cut Page | Chapter 26 Using the Cut Page

CUT

�Create Subtitles from Audio: Automatically creates subtitles for all dialog in the timeline.

�Detect Scene Cuts: Performs a Detect Scene Cuts operation, splitting one long clip of a finished

program into individual clips again.

�Audio Assistant: Uses AI to automatically perform an audio mix of your timeline

based on common deliverable requirements.

�Voice Convert: Uses AI to let you change the speaking voice from one person to another.

�Add Video Track: Adds a video track to the timeline.

�Add Audio Track: Adds an audio track to the timeline.

�Add Subtitle Track: Adds a Subtitle Track to the timeline.

�Split Clips: Splits the current clip in two at the playhead position.

�Join Match Edit Clips: Rejoins two continuous clips that have been split.

�Add Marker: Adds a marker at the playhead position.

�Set Color and Add Marker: Adds a marker and opens the Markers editor, so you can change the

color and add comments, etc.

�Clear Transition from All Edits: Removes all existing transitions from the timeline.

�Add Dissolve to All Edits: Adds a Cross Dissolve to every edit point on the timeline.

�Add Transition to All Edits: Adds the last used transition to every edit point on the timeline.

Edit Actions

The tools under this icon are used to adjust clips on the Timeline.

All of the Edit Actions functions

�Trim Start to Playhead: Deletes everything of the clip to the left of the playhead.

�Trim End to Playhead: Deletes everything of the clip to the right of the playhead.

�Resync Clip: If a clip has slipped sync from the rest of the program, this operation will resync it.

Tracks

The Timeline is divided into multiple tracks, with each track capable of holding a sequence of clips in

order to create a program. The main tracks, which are labeled numerically, combine a clip’s video and

audio into a single item in the Timeline, for simplicity. Editing the In or Out point of a clip edits the video

and audio together.


The Cut Page | Chapter 26 Using the Cut Page

CUT

Cut Page Timeline tracks. Track ST1 shows a subtitle track. Track V1 shows both Video only and

combined Video+Audio clips in an enlarged view. Track A4 shows a separate audio track.

TIP: In the Edit page, Video+Audio clips are presented as separated Video and Audio items

on different tracks. When you open the Fairlight page, audio is presented on tracks with

lanes, where each audio channel can be seen. In this way, each page gives you different sets

of controls over the contents of the Timeline that are appropriate for each page.

Track Header Controls

The track controls, in order, allow you to enlarge a track, lock the track for edits, mute audio, and

enable or disable video for the track.

Controls to enlarge, lock, mute audio,

and disable video for the track

The Importance of Track 1

Each track in the Timeline of the Cut page is designed to carry specific parts of your program. Track 1

is intended for the primary video+audio of your program, often called the “A-roll,” since these are the

primary shots comprising the timing and pacing of the story you’re telling. Adding, deleting, inserting,

trimming, or otherwise rearranging clips on Track 1 results in the rest of the edited timeline being

automatically rippled to accommodate the change you’ve made, with clips to the right of the changed

area moving left to fill the gap of a deleted or shortened clips, or moving right to make room for an

inserted or lengthened clip.

Tracks 2 and Above

Tracks 2 and above are intended for “B-roll,” which is additional footage you stack on top of other clips

in Track 1 to illustrate what someone is saying in the audio of Track 1, or for superimpositions used for

compositing effects that combine two images together in creative ways. Moving or resizing clips on

Track 2 and above only moves or resizes that one clip; other clips in the Timeline are not rearranged

and the Timeline is not rippled when you do this.

For instances where multiple video clips overlap one another on multiple tracks, the video clip on

the highest track obscures those on lower tracks, meaning that only the top clips appear during

playback. This is useful when you’re experimenting with rearranging multiple clips in a complex scene.

For example, you could be editing a scene where an interview clip is on the bottom track, and various

b-roll clips are edited on tracks above the interview so you can freely rearrange them in different ways,

while it’s always easy to reveal the speaker on the bottom track by leaving a gap in the superimposed

b-roll clips.


The Cut Page | Chapter 26 Using the Cut Page

CUT

Editing a scene with multiple superimposed clips

However, if you superimpose video-only or video+audio clips for compositing, you can use the

composite modes and the opacity slider found in the Composite section of the Viewer Tools controls

to mix multiple images together in different ways for artistic effects.

(Left) Superimposing clips you want to composite, (Right) Creating compositing effects with multiple superimposed clips

You can add additional Video+Audio tracks, when necessary, by either dragging a clip to the

undefined gray area of the Timeline above the other existing tracks to make a new track automatically,

by clicking the New Track button at the upper lefthand corner of the Timeline, or by right-clicking in the

timeline header area and choosing “Add Video Track” from the contextual menu.

Audio-Only Tracks

You can also edit audio-only clips such as music, narration, or sound effects, onto separate audio-

only tracks underneath, which are then labeled A1, A2, A3, etcetera. If you drag an audio clip to

the undefined gray area of the Timeline below the other existing tracks, an audio-only track will

automatically be created.

Audio-only tracks in the Cut page Timeline


The Cut Page | Chapter 26 Using the Cut Page

CUT