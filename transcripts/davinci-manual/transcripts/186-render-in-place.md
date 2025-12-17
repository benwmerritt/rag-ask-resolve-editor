---
title: "Render in Place"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 186
---

# Render in Place

Render in Place allows you to render and bake in all effects that are applied to a single clip on the

Edit page Timeline. This command, which only works in the Edit page, creates an entirely new media

file that replaces the original clip on the Timeline. This new file is created in the same directory as the

original source file and is added to the Media Pool automatically.

You can use Render in Place to improve the playback performance of a computationally intensive clip,

or use it to create a new high-quality master media with effects that have been finalized baked in.

For example, perhaps you have created a clip with a complicated speed ramp, and you want to pass it

to another editor or vfx artist in a round-trip rendering scenario, but you are worried about how other

programs may interpret the speed effects. In this scenario you could render the clip in place at master

quality, and then render and deliver the program.

Render in Place is not a one way operation. Afterwards, you have the option to “Decompose to

Original” to bring back the original clip with the original effects, if you need to make a change because

the clip was not really as finalized as you were hoping.

To Render in Place:


Select one or more clips on the Edit Page timeline. Selecting multiple clips results in each clip

being individually rendered in place, but as a batch operation.


Right-click the selection, and choose “Render in Place” from the contextual menu.


Choose the appropriate Render Clip Options, and then click the “Render” button.

Start Timecode: Sets the starting timecode value for the clip.

Format: Selects the media file format.

Codec: Selects the video codec.

Type: Specifies the compression parameters of the selected codec.

Include Handles: Gives you the option to specify the number of frames before and after the clip

In/Out points to be rendered.

Include Video Effects: Turn on this checkbox to bake in all effects that have been applied to the

clip, such as sizing, Open FX or Resolve FX, and speed effects. Turning this checkbox off renders

the clip with speed effects baked in, but no other effects applied.

Include Fusion Composition: Turn on this checkbox to bake in any compositions attached to the clip.

Include Color Grading Effects: Turn on this checkbox to bake in any color grading attached to the

clip from the Color page.


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

Render at Source Resolution: When checked the newly rendered media will be at the resolution

of the original source media, rather than the timeline resolution.


Use the File dialog that appears to choose where you want to save the resulting media. Choose a

location and click Open.

The Render in Place options

A progress bar appears to show you how long this will take. When finished, your new media is saved in

the designated location, added to the Media Pool, and will replace each corresponding source clip on

the Timeline.

If you’ve used Render in Place and end up having buyer’s remorse, or a late-breaking change comes

back to you later, you can easily decompose to the original clip with its editable effects to make

the change.

To Decompose to Original:


Select one or more clips that have already been Rendered in Place, on the Edit Page timeline.


Right-click the selection, and choose “Decompose to Original” from the contextual menu.

The original clip, along with all of its editable effects, will be returned to the Timeline. The new

media created in the Render in Place process will not be deleted from the source folder, nor will it

be removed from the Media Pool. It is effectively a new clip.

Fusion Effect Templates Cache

Fusion effect templates applied to clips on the timeline have more granular caching as well as

automatic render caching options.

The Render Cache Fusion Effect Filter menu in the timeline clip context menu has an Auto option that

is enabled by default. When render cache is set to Smart, any Fusion effects and templates applied to

a clip are automatically cached. Disabling auto allows you to individually pick which effects to cache.

When render cache is set to User, the Auto option automatically caches the Fusion effects, if the

project setting to Automatically Cache Fusion Effects in User mode is enabled. If the project setting is

disabled, Auto mode does not cache any Fusion effects, unless you individually select them.


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

Adjusting Multiple Clips at the Same Time

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

Making a relative adjustment of plus 4.9 in the

Rotation Angle of all selected clips

Adjustment Clips

You can also apply all sorts of effects to multiple clips in the Timeline using Adjustment clips, available

from the Effects bin of the Toolbox in the Effects Library. When an Adjustment Clip is superimposed

above one or more clips in the Timeline, any filters or other effects that are applied to the Adjustment

clip are also applied to all clips underneath it.

Adjustment clips can be used to apply the following types of effects:

�Resolve FX and Open FX plugins

�Inspector parameters including Composite, Transform, Cropping, and Dynamic Zoom

�Fusion page effects

�Color page grading and sizing

Adjustment clips are a fast and easily revised way to apply one or more effects and grades to a range

of clips. Adjustment clips that are difficult to playback in real time can be rendered to cache, just like

any normal video clip. Adjustment Clips can be named using the Inspector. To store an Adjustment

clip, simply drag it from the Timeline to the Media Pool. You can then manage the Adjustment clip just

like any other media type.


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

An Adjustment clip applying a Prism Blur Resolve FX’s vignette to two other clips

Paste Attributes

You can copy and paste video and audio attributes, as well as color corrections, from one clip

to multiple clips using the Paste Attributes command. This is a fast way to apply video and audio

adjustments and effects from one clip to many others in the Timeline.

To copy attributes:


Select a clip with attributes you want to apply to other clips, and press Command-C.


Select one or more other clips to paste to.


Choose Edit > Paste Attributes (Option-V), or right-click one of the selected clips and choose Paste

Attributes from the contextual menu.


When the Paste Attributes window appears, click the checkboxes of each of the attributes you

want to paste, and click Apply when you’re done.


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

The Paste Attributes window

The Paste Attributes window shows you the clip you’re copying from and the clip(s) you’re

pasting to at the top, and provides checkboxes you can use to select which attributes you’d

like to paste.

Keyframe Options for Pasting Keyframed Attributes

A pop-up menu below lets you choose how you’d like to apply any keyframes that are part of the

attributes being pasted; the options are Maintain Timing or Stretch to Fit.

Option to Ripple the Timeline for Pasting Speed Effects

When using Paste Attributes to copy speed effects from one clip to another, the Ripple Sequence

checkbox lets you choose whether or not the pasted speed effect will ripple the Timeline.


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT