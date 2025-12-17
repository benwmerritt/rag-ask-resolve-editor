---
title: "Open FX"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 185
---

# Open FX

DaVinci Resolve supports the use of third-party Open FX filters, transitions, and generators in the

Edit page. Once you install these effects on your workstation, they appear in this section of the Effects

Library, organized by type and group depending on the metadata within each effect.

Open FX

Exposes all Resolve FX and third-party Open FX installed on your workstation at once.

Filters: Contains the Resolve FX filters that ship with DaVinci Resolve, as well as any third-

party OFX plugins you’ve installed on your workstation. Filters can be dragged onto video

clips to apply an effect to that clip. Once applied, filters can be edited and customized by

opening the Open FX panel of the Inspector.

Generators: Contains any third-party OFX generators you have installed on your workstation.

Can be edited into the Timeline just like the native generators that ship with DaVinci Resolve,

but they also expose an Open FX panel next to the Transition panel in the Inspector, where

you can customize settings that are unique to that transition.

Transitions: Contains any third-party OFX transitions you have installed on your workstation.

OFX transitions can be used similarly to any other transition, but they also expose an Open FX

panel next to the Transition panel in the Inspector, where you can customize settings that are

unique to that transition.

Audio FX

On all platforms, DaVinci Resolve supports a set of built-in Fairlight FX, a native audio plugin format

that makes various audio tools and effects available on macOS, Windows, and Linux. On macOS

and Windows, DaVinci Resolve supports the use of third-party VST audio plugins, which includes

most of the professional third-party tools and effects used in the audio postproduction industry. On

macOS, DaVinci Resolve supports Audio Unit (AU) audio plugins. Once you install these effects on

your workstation, they appear in this panel of the Effects Library. Audio plugins let you apply effects to

audio clips or entire tracks’ worth of audio, to add creative qualities such as echo or reverb, or to take

care of mastering issues using noise reduction, compression, or EQ.


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

Effects Library Favorites

You can click on the far right of any transition, title, or generator flag that effect with a star as a favorite

effect. When you do so, the favorited effects appear in a separate Favorites area at the bottom of the

Effects Library Bin list. Favorited effects will be automatically categorized in the list.

Stars indicate a flagged favorite effect; all favorites

are filtered and automatically categorized.

Converting Fusion

Compositions to Edit Effects

If you have created a Fusion Composition that you would like to use across a number of projects, you

can now save it to the Effects toolbox in the Edit page. This allows easy access to the effect from the

Edit page, and simple application to video clips in the Timeline.

To convert a Fusion composition to an Edit effect:


Export the composition as a macro in Fusion, by right clicking on a node and selecting Create

Macro from the contextual menu.


Save the macro file (.setting) to the following directory:

MacOS: /Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/

Templates/Edit/Effects

Windows: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Templates\Edit\Effects

Linux: /opt/resolve/Fusion/Templates/Edit/Effects

The effect will now be available as a drag and drop effect in the “Fusion Effects” section of the

toolbox in the Effects Library on the Edit page.


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

Seeing Effects in the Timeline

When you apply any kind of an effect to a clip in the Timeline, be it an adjustment in the Inspector, a

speed effect, a plugin you’ve applied, etc., clips with that effect appear a darker shade of whatever

color they are to show you there’s an effect applied. Removing all effects from a clip (for example,

using the Remove Attributes command) returns that clip to its original color. This makes it easy to see,

at a glance, which clips have effects, and which clips don’t.

A clip with effects that’s shaded darker between two other regularly-shaded clips without effects

Using the Inspector

Once you’ve added effects to a timeline, the Effects Inspector is where you can edit their parameters.

The Inspector is the central area for editing all of the settings relating to filters, compositing, sizing,

titling, transitions, generators, and effects of all kinds.

The Inspector displays different

parameters depending on what

you’ve selected in the Timeline;

(left) parameters of a clip,

(right) parameters of a title.


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

Many of the instructions in this section require the use of the Inspector, which can be opened or

closed by clicking the Inspector button at the far right of the Edit and Cut page toolbars, or by double-

clicking a transition or generator in the Timeline.

There are three ways that the parameters of clips in the Timeline can be displayed in the Inspector:

�If no clips are selected in the Timeline, then the clip in the highest auto-select-enabled track that

intersects the playhead will have its parameters shown in the Inspector.

�The Inspector always shows the parameters of one or more selected items in the Timeline, which

will override the clip in the highest track that intersects the playhead, if necessary. Changing the

selection changes which parameters are displayed, and the parameters you edit in the Inspector

only alter the currently selected clip. If multiple clips are selected, the Inspector displays “Multiple

Clips” and allows you to adjust the parameters of all selected clips at the same time.

�Choosing Timeline > Selection Follows Playhead sets DaVinci Resolve to always select whichever

clip intersects the playhead in the Timeline. The result is that the Inspector always displays the

parameters of the clip at the playhead, with the added bonus that the clip at the playhead is also

selected for other editorial functions. If there are multiple superimposed clips intersecting the

playhead all at once, the topmost video clip with an enabled Auto Select control will be selected,

thus exposing its parameters in the Inspector, and all other clips will be ignored.

Inspector Effects Controls

Different Effects clips in the Timeline expose different controls. Whichever panels are exposed,

parameters within each panel are organized into groups, with a title bar providing the name of that

group, along with other controls that let you control all parameters within that group at the same time.

The Effects Inspector controls

These controls include:

Enable button: A toggle control to the left of the parameter group’s name lets you disable

and re-enable every parameter within that group at once. Orange means that track’s enabled.

Gray is disabled.

Parameter group title bar: Double-clicking the title bar of any group of parameters collapses

or opens them. Even more exciting than that, Option-double-clicking the title bar of one

parameter group collapses or opens all parameter groups at once.

Keyframe and Next/Previous Keyframe buttons: This button lets you add or remove

keyframes at the position of the playhead to or from every single parameter within the group.

When the button is highlighted orange, a keyframe is at the current position of the playhead.


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

When it’s dark gray, there is no keyframe. Left and right arrow buttons let you jump the

playhead from keyframe to keyframe for further adjustment.

Reset button: Lets you reset all parameters within that group to their default settings.

Adding Filters to Video Clips

DaVinci Resolve supports both built-in Resolve FX and third-party OFX plugins to create various

effects. These effects can be applied both to clips in the Edit page, and to nodes in the Color page.

This section shows how to apply, edit, and remove these filters in the Edit page.

For more information about using video effects in the Color page, see Chapter 151, “Using

Open FX and Resolve FX.”

For a detailed explanation of each of the Resolve FX plugins that accompany DaVinci Resolve,

see Part 12, “Resolve FX Overview.”

Methods of applying video filters in the Edit page:

To apply a video filter to a clip:

�Drag any filter from the Effects Library onto the clip in the Timeline you want to apply it to.

�Double Click the filter in the Effects Library to apply it to the selected clip.

�Drag the Filter from the Effects Library to the Inspector to apply it to the selected clip.

�Drag the Filter from the Effects Library to the Viewer to apply it to the clip being viewed.

To apply a video filter to multiple clips: Select all of the clips you want to apply a filter to in the

Timeline, and then drag any filter from the Open FX category of the Effects Library onto any of the

selected clips. This is undoable.

Applying a video filter to a single clip in the Timeline


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

To edit a clip’s video filters:

Select that clip and open the Inspector’s Effects tab. The effects will be further sub-grouped

by type: Fusion, Open FX, or Audio. If a clip does not have any effects assigned to it, this

panel will be dimmed.

Resolve FX controls appear in

the Effects panel of the Inspector.

Some video filters have custom onscreen controls that can be modified in the Viewer.

These can be exposed in the Edit page using the OFX mode of the Viewer.

Turning on the onscreen controls for

Resolve FX in the Edit page Timeline Viewer

Once enabled, the OFX onscreen controls appear in the Viewer.


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

Modifying onscreen controls foµr Resolve FX in the Edit page Timeline Viewer

Many audio filters expose custom controls that appear in a floating window.

To expose a filter’s custom controls:

Open the parameters if they’re not open already by double-clicking that filter’s title bar.

A button should appear at the top of the parameters for filters that have custom UI. Clicking

this button opens a floating window with all the custom controls. When you’re finished

adjusting the custom controls, close the window.

The Fairlight FX Noise Reduction custom UI interface


Editing Effects and Transitions | Chapter 47 Editing, Adding, and Copying Effects and Filters

EDIT

Methods of working with video filters in the Inspector:

�To rearrange the order of multiple video filters applied to a clip: Click the move up or move

down buttons in any filter’s title bar, to the left of each filter’s Trash Can button.

�To disable or re-enable a filter: Click the toggle control at the far left of each filter’s title bar.

Orange means that track’s enabled. Gray is disabled.

�To remove a filter: Click the Trash Can button.

�To reset a filter: Click the Reset button at the far right of the filter’s title bar.

�To open or collapse a filter’s parameters: Double-click the title bar.

�To open or collapse the parameters of all filters: Option-click the title bar.

Once applied to a clip, video filters can also be keyframed or automated just like any other Inspector

setting, to create dynamic effects that change over time.