---
title: "Fairlight"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 23
---

# Fairlight

Video I/O Offset

The two preferences found in this section let you offset overall video playback up to 7 frames earlier

than your audio playback, to account for situations where image processing applied to your video

output is causing delays that make the video out of sync with your audio. For example, let’s say your

video output is going through a video convertor that adds a 1 frame delay, and then connects to a

video projector that adds another 1 frame of delay. You can set your Video Monitor Offset to 2 frames

to compensate, so the audio/video sync is solid.

�Video Monitor Offset: This drop-down menu lets you choose an offset from 0 to 7 frames.

�Apply Offset during Jog and Shuttle: Turning this checkbox on ensures that the offset you

choose is also applied when you use Jog and Shuttle to move through your program.

General Settings

The two preferences found in the General Settings section both let you customize the Loop Jog

behavior that’s currently available only on the Fairlight page. Choosing Timeline > Loop Jog enables

a brief sample preview to be heard while scrubbing the playhead through the Timeline. This can

make it easier to recognize bits of dialog or music as you’re quickly scrubbing through tracks, in

situations where you’re trying to locate specific lines or music cues. It also enables this brief sample

preview to loop endlessly when you hold the playhead on a frame, so you can pause while scrubbing

and hear (by default) the current 80 ms prior to the playhead as it loops. A pair of settings let you

customize this behavior.

�Loop Jog Alignment: Three options let you choose whether you loop audio Pre the position of the

playhead, Centered on the playhead, or Post the position of the playhead.

�Loop Jog Width: A field lets you choose how many milliseconds of audio to loop when Loop Jog

is enabled. How many milliseconds of audio corresponds to one frame depends on the frame rate

of the video. For example, at a frame rate of 25 fps, there are 1000/25 = 40 ms per frame, so the

default value of 80 ms equals two frames of looping.

�Enable auto patching: Checking this box routes the first of your system audio inputs to the track

that has “arm for record” on.

�Mixer follows selected track: Checking this box ensures that the selected track appears focused

and left-most in the Mixer pane.

�Include mixer events in Undo history: Checking this box ensures that you can undo mixer events

(such as edits to panning or track mute state).


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Automation

The two preferences found in the Automation section let you customize the Glide Time between

Automation events and whether or not Automation events are included when recalling a preset or

when copying and pasting.

�Glide Time: Enter a value in milliseconds to customize the Glide Time for automation.

�Write on Preset or Clipboard Paste: Checking this box ensures that Automation events are

written to the track when recalling a track preset or copying and pasting. Note that when enabled,

the information written is still dependent on the status of what master automation is enabled or

disabled. For example, if plugin automation is disabled, no plugin automation will be written.

Playback Settings

These preferences let you improve realtime performance in DaVinci Resolve by disabling specific

UI features and optimizing the quality of some operations.

�Hide UI overlays: When using a single GPU for both display and CUDA, OpenCL, or Metal

processing, or if your display GPU is underpowered, or if you lack the PCIe bandwidth required for

the currently specified resolution or frame rate, you may be able to improve real time performance

by turning this option on. When enabled, onscreen controls such as the cursor, Power Window

outlines, and split-screen views are disabled and hidden during playback. When playback is

paused, all onscreen controls reappear.

�Minimize interface updates during playback: When enabled, gives priority to real time

performance during playback by reducing user-interface updates. This is helpful when

you’re creating complex grades on systems with low processing power, or when working on

projects at high resolutions.

�Performance Mode Automatic/Manual: A trio of radio buttons let you choose between Automatic

(default) and Manual (user selectable) behaviors when you turn on Performance Mode in DaVinci

Resolve, or you can turn Performance Mode Off altogether. Set to Automatic, Performance mode

automatically optimizes a variety of operations in a bid to balance performance with the necessary

level of image quality, for fast onscreen performance while always maintaining the highest level of

quality for video output. Set to Manual, there are three different settings you can choose to disable

for instances where a particular performance tradeoff Resolve is making results in an undesirably

noticeable reduction in image quality in Performance Mode:

Optimized Sizing: Relates to how image resizing is handled.

Optimized Decode Quality: Relates to how clip resolution vs. timeline resolution is handled.

Optimized Image Processing: Relates to how image processing operations are handled.

Control Panels

The parameters in this panel let you customize the functionality of the DaVinci Control panels.

Panel Sensitivity

Lets you choose the orientation of red on the trackballs, how sensitive trackballs and rings are, and

how sensitive the qualifier knobs are.

�Classic DaVinci trackball alignment: When enabled, this checkbox sets all color balance controls

in DaVinci Resolve to the traditional orientation they’ve always used, which is close to, but not

exactly the same as, the vectorscope alignment of hues. When disabled, the alignment of color

balance controls is exactly the same as the vectorscope alignment of hues, which is similar to how

other color grading applications work. You should choose the mode you’re most familiar with.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

�Grading style: Controls the orientation of the trackballs relative to the corrections they make.

There are two options:

DaVinci: Most users will be familiar with the standard DaVinci controls as this mimics the

vectorscope (how closely depends on the Classic DaVinci trackball alignment setting).

Rank: The Rank settings are somewhat different, so this option is for users who are familiar

with color controls that the Rank control system offered. In this mode, the orientation of red and

green are reversed.

�Lift RGB balance: Controls how quickly adjustments made to the Lift trackball (on the left) will

adjust the Lift Color Balance parameters in the Color page. This setting affects third-party panels.

�Lift master: Controls how quickly adjustments made to the Lift ring (surrounding the leftmost

trackball) will adjust the Lift Contrast parameter in the Color page. This setting affects

third‑party panels.

�Gamma RGB balance: Controls how quickly adjustments made to the Gamma trackball

(second from the left) will adjust the Gamma Color Balance parameters in the Color page. This

setting affects third-party panels.

�Gamma master: Controls how quickly adjustments made to the Gamma ring (surrounding the

second trackball from the left) adjust the Gamma parameter in the Color page. This setting affects

third‑party panels.

�Gain RGB balance: Controls how quickly adjustments made to the Gain trackball (third from

the left) will adjust the Gain Color Balance parameters in the Color page. This setting affects

third-party panels.

�Gain master: Controls how quickly adjustments made to the Gain ring (surrounding the third

trackball from the left) will adjust the Gain Contrast parameter in the Color page. This setting

affects third-party panels.

�Cursor offset: Controls how quickly adjustments made to the fourth trackball affect the cursor,

window position, log-mode offset, and other controls that can be manipulated via this trackball.

�Cursor master: Controls how quickly adjustments made to the fourth ring affect log-mode master

offset, and other controls that can be manipulated via this ring.

�Hue/Saturation/Luminance qualifier: Controls the sensitivity of the HSL panel control knobs.

�Jog: Controls the sensitivity of the jog wheel.

�Shuttle: Controls the sensitivity of the shuttle dial.

Display Settings

Lets you adjust the display of your Blackmagic Design control panels.

�LCD brightness: Controls the overall brightness of the DaVinci control panel displays.

�Key backlighting: Depending on which control panel you have selected, two controls let you

choose LCD Brightness and Key backlighting of the DaVinci Resolve Mini panel, or three controls

let you adjust the color balance of the lit buttons of the DaVinci Resolve Advanced control panel

(the default is red).

Metadata

The metadata panel lets you create custom sets of metadata parameters that will be exposed in the

Metadata Editor.

For more information on using this panel, see Chapter 19, “Using Clip Metadata.”


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Keyboard Customization

Choosing DaVinci Resolve > Keyboard Customization opens the standalone Keyboard Customization

window. This window lets you choose which set of keyboard shortcuts you want to use, discover which

keyboard shortcuts are available, or create your own custom keyboard mappings that more closely

adhere to the way you like to work, in whichever pages you find yourself working.

The Keyboard Customization window

Choosing Keyboard Shortcut Emulation Presets

Using a drop-down at the top right of this menu, you can choose the default DaVinci Resolve set or

any one of the other sets that attempt to mimic other NLEs you might be more familiar with. Please

note that keyboard shortcuts can only be remapped to commands that functionally exist within DaVinci

Resolve, so if a specific feature of another NLE does not have an equivalent in DaVinci Resolve, that

key shortcut may not be mapped in the same way. Fortunately, the editorial feature set of DaVinci

Resolve broadly overlaps with common features in other NLEs, so you should find that most features

you’re used to have a functional equivalent.

You can choose one of the preset keyboard mappings

to emulate another NLE you’re familiar with or the

default DaVinci Resolve keyboard mapping.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

You also have the ability to create your own custom sets of keyboard shortcuts. The Commands list

below shows a hierarchical list of commands organized by the menu they appear within. This list lets

you select individual commands to remap and can be searched if you’re having a hard time finding

what you’re looking for. This is described in more detail later in this section.

Viewing Commands Assigned to Specific Key Combinations

To see what command a particular key of the keyboard is mapped to, you can click any combination of

modifier and other keys on the virtual keyboard at the top of this window. The currently selected keys

reveal how they’re mapped in the “Active Key” list below.

Selecting keys and modifiers on the virtual keyboard

displays their command mapping below

TIP: Starting in DaVinci Resolve 15.2, commands can have multiple keys or key combinations

assigned to them, and number keys on the numeric keypad of an extended keyboard can be

assigned independently from keys at the top of a keyboard.

Panel-Specific Keyboard Mappings

When customizing keyboard shortcuts, they can be assigned to the “Application” so that shortcut

works identically within every part of the DaVinci Resolve UI that’s applicable, or you can map a

particular keyboard shortcut to do a particular command within a specific panel.

Panel-specific keyboard shortcuts let you use a single key to do different things depending on which

panel has focus; for example, one key can do different things in the Media Pool, the Edit Timeline, the

Metadata Editor, and the Sound Library, to give a few Edit Page examples. This provides enormous

flexibility, but if you go this route, you need to be aware of which panel has focus. Fortunately, starting

in DaVinci Resolve 15.2, focus is indicated by a colored highlight at the top of each panel.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Keyboard shortcuts can now be mapped to specific panels so that

different panels can use the same shortcut to accomplish different things