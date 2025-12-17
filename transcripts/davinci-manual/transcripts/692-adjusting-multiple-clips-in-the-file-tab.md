---
title: "Adjusting Multiple Clips in the File Tab"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 692
---

# Adjusting Multiple Clips in the File Tab

You can select multiple audio clips and adjust their properties in the Audio Configuration pane.

For example, you can select a group of audio files and remove Track 2 from all of them at once.

However, the following should be noted:

�In a multiple clip selection, only the last selected clip will appear in the track layout of the Audio

Configuration Pane. However the top composite waveform will be named “Multiple Clips” to let

you know that more than one clip has been selected.

�Any adjustments, like muting or enabling/disabling a track will be applied to all the selected

clips at once.

Timecode

This pane includes controls that were formerly handled by Clip Attributes in the Media Pool (though

that option is still available). These controls let you override the timecode details for a clip or clips in

the Media Pool.

File tab – Timecode section

�Current Frame: This is where you can assign a new time for the timecode at the currently viewed

frame of the clip.

�Slate: In situations where source media comes from a shoot where a timecode slate was used

during the shoot, then you can assign the slate timecode as a second timecode track that can be

used for various operations without changing the primary timecode of the clip, which may already

be in use for program sync.

To set the appropriate Slate timecode, select a Media Pool clip with a visible timecode slate and

move the playhead to a frame where the timecode in the slate is clearly readable. Then, open the

Timecode panel of the Clip Attributes window and type the timecode value you see in the image

into the Slate Timecode field.

�Offset Source: If an entire set of clips has timecode that’s merely offset, you can correct the

timecode offset for as many selected clips as you like.


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

Adjusting Multiple Clips Simultaneously

There’s an easy way to make adjustments to the Inspector parameters of multiple clips at the same

time, without needing to use Paste Attributes (described later in this chapter). All you need to do is

simultaneously select every clip you want to alter, and then modify the parameter in the Inspector that

you want to change. As a result, every selected clip will be adjusted by the same amount. This works

for compositing effects, transforms, text parameters, filters, and audio settings, just about anything that

can be simultaneously exposed in the Inspector for multiple selected clips.

When you select multiple clips, the Inspector will display “Multiple Clips” as the title. If each of the

selected clips have different values in the parameter you’re adjusting, that parameter will have two

dashes in the value field. There are two ways you can make adjustments to multiple clips:

�If you want to make a relative adjustment to all selected clips while keeping their original offsets

from one another, then drag the virtual slider in the parameter field which will display a + or –

before however many units your adjustment is.

�However, if you want to set all selected clips to the same value, you can double-click in the

number field, type the value, and press Return.

Making a relative adjustment of plus 4.00 in

the Volume level of all selected clips

Animated Inspector Adjustments

Key-framing in the Edit page works slightly differently than when using the Keyframe Editor in the

Color page. Most simple key-framing tasks can be performed in the Inspector using three buttons

that appear to the right of any parameter that’s capable of being keyframed. It takes two keyframes at

minimum to create an animated effect.

The three keyframe controls that

appear in the Inspector, from left to

right: Previous keyframe, Create/

Delete keyframe, Next keyframe


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

Methods of key-framing parameters in the Inspector:

�To add a keyframe: Select a clip, open the Inspector, then move the Timeline playhead to the

frame where you want to place a keyframe, and click the Keyframe button next to the parameter

of the Inspector you want to animate. Once you’ve added at least one keyframe to a parameter,

all other adjustments you make to parameters in the Inspector, or using the onscreen Transform/

Crop controls in the Timeline Viewer, add new keyframes automatically if the playhead is at

another frame.

�To move the playhead to the next or previous keyframe: Click the small left- or right-hand

arrow to either side of a parameter’s keyframe control to jump the playhead to the next or

previous keyframe. You can also press Right-Bracket ( [ ) and Left-Bracket ( ] ) to go from

keyframe to keyframe.

�To edit an existing keyframe of a parameter: Move the playhead to be on top of the keyframe

you want to edit, and then change that parameter, either in the Inspector, or using the onscreen

controls of the Timeline Viewer.

Methods of changing keyframe interpolation in the Inspector:

�To change a keyframe to Ease In or Ease Out: Eased keyframes create animated changes that

begin slowly and accelerate to full speed, or slow down gradually to decelerate to a stop. This only

works when you have two or more keyframes creating an animated effect. Move the playhead to

a frame with a keyframe using the next/previous keyframe controls, then right-click the orange

keyframe button and choose Ease In, Ease Out, or Ease In and Out, depending on which keyframe

you’re editing and the effect you want to create.

�To change a keyframe to Linear: Move the playhead to a frame with a keyframe using the next/

previous keyframe controls, then right-click the orange keyframe button and choose Linear.

Methods of deleting keyframes and disabling keyframed effects:

�To delete a single keyframe: Open the Inspector, move the Timeline playhead to a frame with a

keyframe, and click the orange Keyframe button in the Inspector to delete it.

�To delete all keyframes for one parameter: Click the reset button to the right of a parameter’s

keyframe control in the Inspector.

�To delete all keyframes in a group of parameters in the Inspector: Click the reset button to the

right of a parameter group’s title bar in the Inspector.

�To disable or enable a single parameter’s keyframed effect: In the Timeline, click the toggle

control at the left of a parameter’s keyframe track. Orange means that track’s enabled.

Gray is disabled.

�To disable or enable a group of parameters in the Inspector: Click the toggle control at the

left of a parameter group’s title bar in the Inspector. Orange means that group is enabled.

Gray is disabled.

Paste and Remove Attributes

The Fairlight page has Paste Attributes and Remove Attributes commands that allow for the copying

and resetting of audio Inspector parameters and effects, similar to the same commands on the

Edit page.

For more information on how to do this, see Chapter 175, “Editing Basics in the Fairlight Page.”


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

Setting Clip Volume in the Timeline

Each audio clip, or audio item in the case of audio clips with linked audio on multiple tracks, has its

own Volume level. This means that audio clips with multiple channels share a common Volume setting.

There are several ways you can adjust these levels simply.

Adjusting Volume

Each clip (or item) of audio in the Timeline has a Volume overlay that lets you set that clip’s gain level

by simply dragging it up or down with the pointer. This overlay corresponds to the Volume parameter

in the Inspector.

Dragging a Volume overlay to adjust the clip level

Additionally, you can click any clip’s Audio Curve Editor button, at the bottom right-hand corner of each

audio clip, to open an audio-specific Curve Editor with which you can keyframe not just volume, but

pan, and the parameters of any audio filters you might have applied to that clip.

NOTE: Under the Fairlight menu > Show Clip Gain Line, you can show each clip’s gain in the

Timeline. This is a handy way to quickly see all of the relative gains of clips in the Timeline.

Clip information for all clips in the Timeline

can be enabled in the Clip Info display.


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

Adding and Adjusting Volume Keyframes

Mixing audio by adding and adjusting individual keyframes can be a fast and effective way of

balancing clip levels with one another and of fixing clip-specific dynamic level problems. When

manually editing any audio parameter curve, you can use the following procedures.

Methods of adjusting the Volume curve using the pointer:

�To adjust any curve segment: Position the pointer over the overall segment for clips with no

keyframes, or position it between any two keyframes, directly on top of the curve segment you

want to raise or lower. When the move cursor is displayed, click and drag up to raise the Volume,

or down to reduce the Volume.

�To adjust a section of level in a clip: Use the Edit Selection tool to highlight the portion to adjust.

Then with the Clip Gain line showing, increase or decrease to the desired level and keyframes will

automatically be created at the boundary of the gain adjustment.

�To add keyframes to the level curve: Hold the Option key down and click the curve to place a

keyframe at that frame. You must add at least two keyframes to create an automated change in

Volume. By using the Option and Command key you can remove any keyframe.

�To adjust a keyframe in any direction: Move the pointer over a keyframe so that the four-way

cursor appears, and then click and drag up or down to change the Volume, or side to side to

change its timing.

�To adjust a keyframe in only one direction: Move the pointer over a keyframe so that the four-way

cursor appears, and then click and drag in the intended direction of adjustment, either vertically

to change the volume of the clip at that frame, or horizontally to move the keyframe to a different

point in time. Once you start dragging a keyframe into a particular direction, keyframe movement

is constrained in that direction until you release that keyframe.

�To select one or more keyframes: Click any keyframe to select it.

�To select multiple discontiguous keyframes: Command-click all keyframes you want to select,

whether they’re next to one another or not.

�To select multiple contiguous keyframes: Click the first keyframe you want to select, and then

shift-click the last keyframe you want to select, and all keyframes between will also be selected.

NOTE: When adjusting the gain on clips, the tooltips will show the current gain level and

reflect whatever changes you make indicating the amount of change as the keyframe moves.

Normalizing Audio Levels

The Normalize Audio Levels command automatically adjusts the level of timeline clips to a specific

target level, and you can choose the method used to analyze each audio clip’s levels to determine

how to normalize each clip’s volume. Options include a variety of loudness normalization algorithms

specific to various international standards, which are useful for balancing the perceived overall

loudness of several clips to one another, regardless of transient levels throughout each clip. You can

also do Peak normalization, with options for both Sample Peak and True Peak.

The various loudness options are designed to analyze an audio signal based on its perceived

loudness to the listener, which results in a more accurate automatic balancing of different clips’ audio

levels to one another, regardless of transient peaks occurring throughout different clips.

The target peak meter now uses the BS.1774 standard for measuring maximum “true peak,” which

means that this meter is capable of measuring “inter-sample peaks,” rather than only the peaks at

each sample of a waveform. However, you still have the option to measure Sample Peak, which is the

previous method of measuring the actual peak of the samples in a media file.


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT

The change made by the Normalize Audio Volume command is only a volume adjustment; no

dynamics are applied, so the result of using this command is that the loudest parts of each selected

clip are going to match one another at the target level. This command is also available in the

Fairlight page.

To normalize one or more selected timeline clips:


Right-click one of the selected clips and choose Normalize Audio Levels. The Normalize Audio

Level dialog appears.

The Normalize Dialog in the Fairlight page


Choose the Normalization Mode you want to use. You can choose among a variety of

standardized loudness measurement algorithms, or Sample Peak, or True Peak.


Choose the reference level that you want to set the peak volume of the selected clips to

match, in dBFS.


Choose how you want to set the level of multiple selected clips:

When Set Level is set to Relative, all selected clips are treated as if they’re one clip, so that the

highest peak level of all selected clips is used to define the adjustment, and the volume of all

selected clips is adjusted by the same amount. This is good if you have a series of clips, such as a

dialog recording, where the levels are consistent with one another, and you want to normalize all

of them together.

When Set Level is set to Independent, the peak level of each clip is used to define the adjustment

to that clip, so that the volume of every selected clip is adjusted by an amount specific to that

clip. The end result may be a set of very different volume adjustments intended to make the peak

levels of each audio clip match one another. This is good if, for example, you’re trying to balance a

series of different sound effects with one another that have very different starting levels.

For more information about loudness normalization, see Chapter 182, “Audio Meters and

Audio Monitoring.”


Fairlight | Chapter 176 The Fairlight Inspector

FAIRLIGHT