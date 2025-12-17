---
title: "MediaIn Node [MI]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 424
---

# MediaIn Node [MI]

The MediaIn node

MediaIn Node Introduction

NOTE: The MediaIn node is only available in DaVinci Resolve.

The MediaIn node is the foundation of every composition you create in DaVinci Resolve’s Fusion page.

In most cases, it replaces the Loader node used in Fusion Studio for importing clips. There are four

ways to add a MediaIn node to the Node Editor.

�In the Edit or Cut page, position the playhead over a clip in the Timeline, and then click the Fusion

page button. The clip from the Edit or Cut page Timeline is represented as a MediaIn node in the

Node Editor.

�Drag clips from the Media Pool into the Node Editor, creating a MediaIn node in the Node Editor.

�Drag clips from an OS window directly into the Node Editor, creating a MediaIn node

in the Node Editor.

�Choose Fusion > Import> PSD when importing PSD files into the Node Editor. Each PSD layer is

imported as a separate MediaIn node.

NOTE: Although a MediaIn tool is located in the I/O section of the Effects Library, it is not

used as a method to import clips.

When clips are brought in from the Media Pool, dragged from the OS window, or via the Import

PSD menu option, you can use the MediaIn node’s Inspector for trimming, looping, and extending the

footage, as well as setting the source’s color and gamma space.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

Inputs

The single input on the MediaIn node is for an effect mask to crop the image brought in by

the MediaIn.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the source image to appear

only within the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The MediaIn node is typically the starting point for all composites done in the Fusion page of DaVinci

Resolve. It contains the clip from the Edit page or Cut page. Any clip brought in from the Media Pool is

also added as a MediaIn node.

Two MediaIn nodes: one from the Edit page Timeline and one from the Media Pool

Inspector

MediaIn node Image tab

Image Tab

When brought in from the Media Pool or dragged from an OS window, the MediaIn node’s Image tab

includes controls for trimming, creating a freeze frame, looping, and reversing the clip. You can also

reselect the clip the MediaIn links to on your hard drive. A subset of these controls is available when

the MediaIn node is brought in from the Edit or Cut page Timeline.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

Global In and Out

Only used when a clip is brought in through the Media Pool or an OS window, the Global In and Out

handles are used to specify the start and end of this node within the Fusion effect. Use Global In to

specify the frame on which the clip starts and use Global Out to specify the frame on which the clip

ends within the comp’s global range. The node does not produce an image on frames outside of

this range.

If the Global In and Out values are decreased to the point where the range between the In and Out

values is smaller than the number of available frames in the clip. Fusion automatically trims the clip

by adjusting the Trim range control. If the Global In/Out values are increased to the point where the

range between the In and Out values is larger than the number of available frames in the clip, Fusion

automatically lengthens the clip by adjusting the Hold First/Last Frame controls. Extended frames

are visually represented in the range control by changing the color of the held frames to green in

the control.

To slide the clip in time or move it through the project without changing its length, place the mouse

pointer in the middle of the range control and drag it to the new location, or enter the value manually in

the Global In value box.

�Clip Name: Displays the name of that clip.

Process Mode

Use this menu to select the Fields Processing mode used by Fusion when loading the image. The

Has Fields checkbox control in the Frame Format preferences determines the default option, and the

default height as well. Available options include:

�Full frames

�NTSC fields

�PAL/HD fields

�PAL/HD fields (reversed)

�NTSC fields (reversed).

The two reversed options load fields in the opposite order and thus result in the fields being spatially

swapped both in time order and in vertical order as well.

Media Source: This control allows you to choose where media is sourced from; the three available

options include: Timeline, Background, and Media Pool.

�Timeline: Links the clip from the Edit Timeline (default).

�Background: This pulls frames from the lower video tracks in the edit. When toggling the Media

Source to Background, the composited result of all the lower tracks is visible.

�Media Pool: Links the clip directly from the Media Pool, bypassing the Edit Timeline.

Layer: In the case of Multilayer or Photoshop PSD files, this selects the layer in the file to use. For a

Fusion Clip created using multiple video layers on the timeline, this will refer to the index number of

each of the layers.

Trim

The Trim range control is used to trim frames from the start or end of a clip. Adjust the Trim In to

remove frames from the start and adjust Trim Out to specify the last frame of the clip. The values used

here are offsets. A value of 5 in Trim In would use the fifth frame in the sequence as the start, ignoring

the first four frames. A value of 95 would stop loading frames after the 95th frame.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

Hold First Frame/Hold Last Frame:

The Hold First Frame and Hold Last Frame controls hold the first or last frame of the clip for the

specified amount of frames. Held frames are included in a loop if the footage is looped.

Reverse

Select this checkbox to reverse the footage so that the last frame is played first, and the first frame is

played last.

Loop

Select this checkbox to loop the footage until the end of the project. Any lengthening of the clip using

Hold First/Last Frame or shortening using Trim In/Out is included in the looped clip.

Source Color Space

Lets you choose a color space for the image data output by this MediaIn node.

�Auto: uses the Timeline color space, or whichever color space is assigned by Resolve Color

Management (RCM) if it’s enabled.

�Space: Space lets you choose a specific setting from a Color Space drop-down menu, while a

visual “horseshoe” graph lets you see a representation of the color space you’ve selected.

Source Gamma Space

Lets you choose a gamma setting for the image data output by this MediaIn node. Once the gamma

curve type is set, you can choose to remove the curve to help achieve a linear workflow.

�Auto: Uses the Timeline gamma, or whichever gamma is assigned by Resolve Color Management

(RCM) if it’s enabled.

�Space: Lets you choose a specific setting from a Gamma Space drop-down menu, while a visual

graph lets you see a representation of the gamma setting you’ve selected.

�Log: Displays the Log Type drop-down menu where you can choose a specific log encoding

profile. A visual graph shows a representation of the log setting chosen from the menu. Additional

Lock RGB, Level, Soft Clip, Film Stock Gamma, Conversion Gamma, and Conversion table options

are presented to finesse the gamma output.

�Remove Curve: The associated gamma curve is removed from, or a log-lin conversion is

performed on, the material, effectively converting it to a linear output space.

�Pre-Divide/Post-Multiply: Lets you convert “straight” Alpha channels into premultiplied Alpha

channels, when necessary.

Audio Tab

The Inspector for the MediaIn node contains an Audio tab, where you can choose to solo the audio

from the clip or hear all the audio tracks in the Timeline.

The Audio tab in the MediaIn node is used to select the track

for playback, slip the audio timing, and reset the audio cache.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

If the audio is out of sync when playing back in Fusion, the Audio tab’s Sound Offset wheel allows you

to slip the audio in subframe frame increments. The slipped audio is only modified in the Fusion page.

All other pages retain the original audio placement.

Audio with Media Pool Clips

Audio from a clip brought in through the Media Pool is muted by default. Hearing the audio from a

Media Pool clip is a two step process.

To hear audio from a clip brought in through the Media Pool, do the following:


Select the clip in the Node Editor.


In the Inspector, click the Audio tab and select the clip name from the Audio Track

drop-down menu.

If more than one MediaIn node exists in the comp, the audio last selected in the Inspector is heard.

You can use the Speaker icon in the toolbar to switch between the MediaIn node audio files.


Right-click the Speaker icon in the toolbar, then choose the MediaIn for the clip you want to hear.

Purging the Audio Cache

The audio and its settings are cached for faster performance. If you change which audio tracks you

want to play back in Fusion, or you use the Sound Offset wheel to slip the audio tracks, you need

to purge the audio cache. Also, if you return to the Edit, Cut, or Fairlight page and modify the audio

levels, you need to purge the audio cache.

To purge the audio cache after any change to the audio playback:

�Click the Purge Audio Cache button in the Inspector.

The audio will be updated when you next playback the composition.

MediaOut Node [MO]

The MediaOut node

NOTE: The MediaOut node is only available in DaVinci Resolve.

MediaOut Node Introduction

Every composition you create in DaVinci Resolve’s Fusion page must include a MediaOut node.

The MediaOut node sends the final output back to your Timeline on DaVinci Resolve’s Edit or

Cut page. In most cases, it replaces the Saver node used in Fusion Studio for exporting clips.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

The composition output by the Fusion page’s MediaOut node is propagated via the Color page’s

source inputs, with the sole exception that if you’ve performed transforms or added plugins to that clip

in the Edit or Cut page, then the handoff from the Fusion page to the Color page is as follows:

Fusion

Effects

Edit

Page

Plugins

Color

Effects

When using Resolve Color Management or ACES, each MediaOut node converts the output image

back to the Timeline color space for handoff to the Color page.

NOTE: Additional MediaOut nodes can be added to the Node Editor from the Effects Library.

Additional MediaOut nodes are used to pass mattes to the Color page.