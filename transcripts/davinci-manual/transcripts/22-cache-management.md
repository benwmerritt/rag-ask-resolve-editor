---
title: "Cache Management"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 22
---

# Cache Management

This section allows you to delete your local cache automatically after a certain number of days to keep

your drive from filling up with older projects.

Of course, you can always manage these files manually from the Playback > Manage Render Cache

menu, but this new preference lets you set and forget a cleanup operation.

Media Cache Settings

Delete Cache files older than xx days: Check the box and select the number of days after

which the automatic deletion of the Cache files will occur.

Editing

The settings in this panel affect new timeline settings, editorial default values, trim behaviors, timeline

UI appearance, and frame interpolation settings.

New Timeline Settings

These settings define the presets that populate the New Timeline Options window whenever you

create a new timeline.

�Start Timecode: You can change the Start Timecode if a specific start time is required.

�No. of Video Tracks: Enter how many video tracks you want to have. You can also drag within this

field to adjust the number of video tracks with a virtual slider.

�No. of Audio Tracks: Enter how many audio tracks you want to have. You can also drag within this

field to adjust the number of audio tracks with a virtual slider.

�Audio Track Type: Choose the channel mapping you want the new audio tracks to use.

Automatic Smart Bins

These settings let DaVinci Resolve automatically create Smart Bins whenever clips with relevant

metadata appear in the Media Pool, or whenever such metadata is added to clips that are already

in the Media Pool. You can choose which Smart Bins are automatically created via a series

of checkboxes.

General Settings

These settings define the timing of resolve-generated effects and editing operations.

�Standard generator duration: Defines the default duration of generators you edit into the

Timeline, in Seconds or Frames. The default value is 5 seconds.

�Standard transition duration: Defines the duration of transitions, in Seconds or Frames, that you

add to an edit point in DaVinci Resolve. The default value is 1 second.

�Standard still duration: Defines the duration of stills that you import such as TIFF, PNG and other

supported graphic file formats, in Seconds or Frames. The default value is 5 seconds.

�Pre-roll time: Determines how much of the Timeline before the current position of the playhead to

play when using the Play Around command.

�Post-roll time: Determines how much of the Timeline after the current position of the playhead to

play when using the Play Around command.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

�Audio subframe nudge: Determines the number of milliseconds or subframes are nudged when

you use the Subframe Left/Right controls.

�Default handles length: The value used when creating a timeline with handles. The default is one

second worth of frames.

�Default fast nudge length: The number of frames that are nudged when you use the

Shift-Comma (,) and Shift-Period (.) keyboard shortcuts.

�Pre-playhead shadow length: The number of frames in the Timeline prior to the playhead covered

by the Playhead Shadow, if enabled by checking the “Show playhead shadow box” in the User UI

Settings preferences.

�Post-playhead shadow length: The number of frames in the Timeline after the playhead covered

by the Playhead Shadow, if enabled by checking the “Show playhead shadow box” in the

User UI Settings preferences.

�Timeline overlay retains the last performed action: Turn this checkbox on if you want

DaVinci Resolve to always remember the last edit type you used in the Timeline Viewer Overlay,

and highlight it on this Overlay whenever you drag another clip over the Timeline Viewer to let

you know that the last edit you performed is the new default edit if you drop clips to the left

of the overlay.

�Always highlight current clip in the media pool: When turned on, any clips at the position of the

playhead on the Edit or Color pages will be automatically highlighted in the Media Pool.

�Prioritize pasting to the in and out range: Normally, pasted clips appear at the playhead position

in the timeline. Check this box if you wish them to be pasted according to the timeline in and out

points instead.

�Sync the Master Timeline to the current frame: If you turned on “Automatically match master

timeline with media pool” in the Color settings, then this option lets you make sure that whenever

you open the Master Timeline, the playhead is at the same clip and frame that it was in the

previous Timeline you were working on.

�Show offline reference for timeline gaps: If there’s a missing clip in a conformed timeline that

results in a gap in the Timeline Editor, turning this option on sets DaVinci Resolve to show the

corresponding frames of an “offline reference movie,” if one has been assigned to that timeline,

instead of black. This can be helpful in emergency situations when you’re missing timeline clips

right before a screening or review session; this feature lets you play or output the missing frames

using the corresponding media from the offline reference movie, instead of outputting black.

For more information on using and assigning Offline Reference Movies, see Chapter 55,

“Preparing Timelines for Import and Comparison.”

�Show offline reference for non-conformed edits: If there’s missing media in a project that results

in an unlinked clip in the Timeline Editor (represented by a red exclamation point overlay on that

clip), turning this option on sets DaVinci Resolve to show the corresponding frames of an “offline

reference movie,” if one has been assigned to that timeline, instead of black. This can be helpful

in emergency situations when you’re missing source media right before a screening or review

session; this feature lets you play or output the missing frames using the corresponding media

from the offline reference movie, instead of outputting black.

For more information on using and assigning Offline Reference Movies, see Chapter 55,

“Preparing Timelines for Import and Comparison.”


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

�Use custom safe area overlays: When turned on, displays Action Area and Title Area fields that

let you set a custom percentage for each. The default values are 93% for Action Area and 90%

for Title Area.

�Align audio edits to frame boundaries: When turned on, the In and Out points of audio clips

always align themselves with whole frame boundaries, just like video clips. When turned off, you

can perform subframe audio edits to audio-only clips, or to linked audio when you’ve suspended

linked selection.

�Configure clips as multi-mono on import: Checking this box allows you to import any

multichannel audio in a multiple mono configuration. This lets you take any Stereo, 5.1, or other

multichannel sources and automatically configures them to multiple mono files with the same

number of tracks when you add them to the Media Pool.

�Limit media pool audio sync to first timecode match: When two or more audio clips overlap

timecode with a video clip, the default behavior is to sync all overlapping audio clips by making

as many new tracks as necessary. Checking this box replaces this behavior by having DaVinci

Resolve choose what it thinks is the most likely single audio track, and sync just that single audio

clip, ignoring the others.

�Import Finder tags as Keywords (Mac only): When turned on, any color tags that are set and

defined in Mac OS for a media file will automatically be imported as keyword metadata alongside

that media file.

NOTE: Even when Align audio edits to frame boundaries is turned off, if linked selection is

on, you’ll be unable to make subframe edits while you’re resizing both the audio and video of

linked clips.

Text

Check the Display Only Specific Fonts box to explicitly limit the font options shown for your text

elements. This lets you set a white list of fonts that you are cleared to use, and hide all other fonts on

the system.

To set up an allowed fonts list:


Check the box in Preferences > User > Editing > Text > Display Only Specific Fonts.


Select a font filter file.

A font filter file is any UTF-8 text file with a combination of explicit font names or text with asterisk

wildcards to match multiple fonts, listed one entry per line.

*Gothic* (any font name with Gothic in it)

Arial

Helvetica* (any font name beginning with Helvetica)

Open Sans

Default Fades

These settings define the curves of the default audio fades in Fairlight.

�Fade In/Out: Define the curve type for fade ins and outs.

�Crossfades: Define the curve type for the ins and out of the crossfade.

Checkboxes for None, Equal Power, and Equal Gain for crossfade type.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Color

The settings in this panel govern different behaviors in the Color page.

General Settings

Affect a variety of behaviors while working in the Color page.

�Master reset maintains RGB balance: Defines how the DaVinci control panel trackball/ring reset

buttons reset primary color adjustments. When this option is turned off (the default), pressing the

ALL Reset button returns the primary correction values to their default values. When this checkbox

is turned on, then pressing the ALL Reset button (a) resets the YRGB values so that the overall

values are kept and the ratio of YRGB to each other is maintained, and (b) pressing the RGB Reset

button sets the three color channels to the average of what they were previously set to.

�Wipe wraps when viewing reference stills: Turning this on (the default) lets stills wrap around

the edge of the screen while you’re adjusting the wipe using the mouse, rather than stopping

at the screen’s edge. If you find this behavior awkward when trying to quickly create full-frame

comparisons with stills to flip on and off, it can be disabled.

�High-Visibility Power Window Outlines: Turning this on sets Power Window outlines to be drawn

as green (for the center shape) and yellow (for the softness shapes), to make these windows easier

to see in certain circumstances, instead of the default white and gray.

�Mattes display high contrast black and white: When enabled, the HILITE command, which displays

the current key, shows a black and white matte (i.e., high contrast) rather than the standard gray matte.

For more information on this setting, and on use of the HILITE command, see Chapter 135,

“Secondary Qualifiers.”

�Next scene switches to visible track: When grading a project with multiple tracks, you can use

this option to alter the “next scene” command to work better in projects with multi-clip composites.

With this option turned off, pressing NEXT SCENE on the DaVinci control panel, or using the

Down Arrow keyboard shortcut, moves the playhead to the very next clip in the Thumbnail

timeline, regardless of whether it’s in front of or behind another clip. Turning this option on causes

the NEXT SCENE command to move the playhead to the clip in the highest track if the next clip is

part of a multi-clip composite with multiple clips stacked over one another.

�Previous or Next node navigates only to correctors: Node navigation only selects corrector

nodes and bypasses mixer, splitter and combiner nodes, etc.

�Preserve node numbers when adding nodes: Checking this box increments the node numbering

by the order in which they are created, regardless of its position in the node tree. Unchecked

reflows the node numbering automatically based on the node’s position in the tree.

�Always perform copy and paste on selected nodes: Bypasses the interface focus-based

selection for copying and pasting full grades vs. individual nodes. When checked, DaVinci Resolve

will only copy and paste between selected nodes regardless of the interface focus.

�Use Legacy Auto Color: As of DaVinci Resolve 16, the A button in the Color Wheels palette and

the Shot Match command available from the Thumbnail Timeline contextual menu both now use

advanced algorithms, based on the DaVinci Neural Engine, to provide superior results when

automatically adjusting color balance and contrast. This checkbox lets you set the A button to use

the older algorithm instead.

�Use Legacy Shot Match: As of DaVinci Resolve 16, the Shot Match command available from the

Thumbnail Timeline contextual menu uses an advanced algorithm, based on the DaVinci Neural

Engine, to provide superior results when automatically adjusting color balance and contrast.

This checkbox lets you set the Shot Match command to use the older algorithm instead.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

�Histogram Background on Grading Tools: This drop-down menu lets you turn the histogram

that appears in the background of the Curves palette either Off, On based on the node’s Input

(changes made to the curve do not affect the background histogram), or On based on the node’s

Output (changes made to the curve do affect the background histogram).

�Automatically cue x frames into timeline clips: This setting affects the operation of the NEXT

SCENE and PREV SCENE commands in the Color page. The default cue point when moving from

one clip to the next is the first frame of each clip. Entering a value, in frames, in this field sets the

default cue point to the specified number of frames after the first frame of each clip you move the

playhead to. This can be convenient if the source material has black or camera rollup flashes at the

beginning of every clip while you’re trying to grade dailies.

�Neighboring Clips in Split Screen: Lets you choose how many neighboring clips next to the

current clips are shown in a grid in the Color page Viewer when you turn on the Neighbor Clips

option of the Split-Screen shot comparison control.

�Switching clips: (this setting can also be changed from the Option menu in the Node Editor)

When switching clips, DaVinci Resolve can switch to the same or another node in the node graph.

The four options below determine which node is selected:

Selects last adjusted node: The default setting, where each clip in the Timeline retains its own

independent node selection that’s remembered whenever you move back to that clip.

Selects first node: The first node is always selected when you move to another clip.

Selects last node: The last node is always selected when you move to another clip.

Selects same node: If the clip you’ve moved to has as many or more nodes as the last clip, the

node of the same number will be selected. If the clip you’ve moved to has fewer nodes than the

last clip, the next highest node will be selected.

�Color picker: Changes the way that colors are selected when using the Secondary color

correction controls. DaVinci Resolve is the normal and modern mode, however some colorists who

are familiar with the legacy 2K prefer the DaVinci 2K mode.

Ripple Mode

This setting determines the behavior of the Ripple command that’s initiated in the Color page.

�Target clips are set to: The Ripple mode that’s used when you select a Ripple command in the Color

page, either using the RIPPLE button on the Advanced Panel, or selected from the Color menu.

For more information on using this function, see Chapter 142, “Grade Management.”

Exact values changed: Changes made to the current clip are rippled to the specified clips using

the exact parameters that were changed. For example, if the Master Gain level in the current

clip is changed to 0.75 of its range, each clip you ripple will have a Master Gain level of 0.75.

Only parameters you adjust are rippled.

Percent value changed: Changes made to the current clip are rippled to the specified clips by the

percentage of change you made to the altered parameters. For example, if the current clip has a

Master Gain level of 1.00 and is changed to 0.90 units, then the Master Gain level of each clip you

ripple will have a relative reduction of 10% relative to its previous value.

Unit values changed: Changes made to the current clip are rippled to the specified clips by the

same delta of change, using whichever units make sense for the affected parameter. For example,

if the current clip had a Master Gain of 0.80 and you increased it to 0.90, each rippled scene’s

Master Gain level increases by 0.10.

All values are copied: The current clip’s grade is rippled to the specified clips in its entirety.

No comparison is made with the original clip’s parameters, and all memory parameters are rippled.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Printer Light Step Calibration

For film projects, when you have tight integration with a film lab, it is possible to adjust the printer light

calibration sets to match the lab you are using. You should work with your lab technician to set up the

Lab Aim settings, the Steps adjustments, which is an incremental value, and the Density Increment

adjustment, which is the amount of correction applied within each step. Usually, the Step and Density

values will be identical, but this will be up to your lab and your preference.