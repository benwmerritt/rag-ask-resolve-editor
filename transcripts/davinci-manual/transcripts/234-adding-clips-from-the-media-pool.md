---
title: "Adding Clips from the Media Pool"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 234
---

# Adding Clips from the Media Pool

You can open the Media Pool on the Fusion page and drag clips directly to the Node Editor to add

them to your node tree.

When you add a clip by dragging it into an empty area of the Node Editor, it becomes another

MediaIn node, disconnected, that’s ready for you to merge into your current composite in any one of a

variety of ways.

Dragging a clip from the Media Pool (Top), and dropping

it onto your composition (Bottom).

TIP: Dragging a clip from the Media Pool on top of a connection line between two other

nodes in the Node Editor adds that clip as the foreground clip to a Merge node.

When you add additional clips from the Media Pool, those clips becomes a part of the composition,

similar to how Ext Matte nodes you add to the Color page Node Editor become part of that

clip’s grade.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Audio with Media Pool Clips

Audio from a clip brought in through the Media Pool is muted by default. Hearing the audio from a

Media Pool clip is a two step process.

To hear audio from a clip brought in through the Media Pool, do the following:


Select the clip in the Node Editor.


In the Inspector, click the Audio tab and select the clip name from the Audio Track

drop-down menu.


Right-click the speaker icon in the toolbar, then choose the MediaIn for the Media Pool

clip to solo its audio.

You can now use the speaker icon contextual menu to switch back and forth between all the

MediaIn nodes.

Finding Clips in the Media Pool from the Node Editor

Complex Fusion Compositions can have multiple MediaIn nodes to keep track of. It is possible to find

the exact clip in the Media Pool assigned to a MediaIn node by selecting it, and then choosing Clip >

Find Clip in Media Pool (Option-F).

Adding Clips from the File System

You also have the option of dragging clips from the file system directly into the Node Editor. When you

do this, they’ll be added to the currently selected bin of the Media Pool automatically. So, if you have

a library of stock animated background textures and you’ve just found the one you want to use using

your file system’s search tools, you can simply drag it straight into the Node Editor to use it right away.

Using MediaIn Nodes

The MediaIn nodes in the Fusion Page are the foundation of every composition you create. This

section provides more detail about the controls available for adjusting MediaIn and Loader nodes.

MediaIn Node Inputs

MediaIn nodes have one Effects mask input and one output. In the case of the Effects mask input,

connecting a mask node such as a Polygon or B-Spline node creates an alpha channel in the

MediaIn node.

TIP: If you connect a mask node without any shapes drawn, that mask outputs full

transparency, with the result that the image output by the MediaIn node is uselessly blank.

If you want to rotoscope over a MediaIn node, first create a disconnected mask node, and

with the mask node selected (exposing its controls in the Inspector) and the MediaIn node

loaded into the viewer, draw your mask. Once the shape you’re drawing has been closed, you

can connect the mask node to the MediaIn node’s input, and you’re good to go.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Inspector Properties of MediaIn Nodes

Which Inspector options are available for MediaIn nodes of your composition depends on how you

imported the media.

MediaIn Node Parameters for Clips in a Timeline

When you create a composition using clips from the Edit page Timeline, the MediaIn nodes for those

clips display fewer parameters than those imported directly from the Media Pool, because the timing

of clips that have already been edited into a Timeline is already set.

The Inspector Image tab parameters for a clip from the Timeline

Image Tab

�Clip Name: Displays the name of that clip.

�Process Mode: Lets you choose whether the clip represented by that node will be processed as

Full Frames, or via one of the specified interlaced methods.

�Media Source: This control allows you to choose where media is sourced from; the three available

options include: Timeline, Background, and Media Pool.

Timeline: Links the clip from the Edit Timeline (default).

Background: This pulls frames from the lower video tracks in the edit. When toggling the Media

Source to Background, the composited result of all the lower tracks is visible.

�Media Pool: Links the clip directly from the Media Pool, bypassing the Edit Timeline.

�Layer: In the case of Multilayer or Photoshop PSD files, this selects the layer in the file to use. For

a Fusion Clip created using multiple video layers on the timeline, this will refer to the index number

of each of the layers.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Source Color Space

The Color Space Type menu sets the color space of the media to help achieve a linear workflow.

Unlike the Gamut tool, this doesn‘t perform any actual color space conversion but rather adds the

source space data into the metadata, if that metadata doesn‘t already exist. The metadata can then be

used downstream by a Gamut tool with the From Image option, or in a Saver if explicit output spaces

are defined there.

�Auto: Passes along any metadata that might be in the incoming image.

�Space: Allows the user to set the color space from a variety of options.

Source Gamma Space

The Curve Type menu automatically determines or allows you to choose the Gamma setting for the

image and allows the option to remove the Gamma curve to help achieve a linear workflow.

�Auto: Passes along any metadata that might be in the incoming image.

�Space: Allows you to choose a specific setting from a Gamma Space drop-down menu, while a

visual graph lets you see a representation of the gamma setting you’ve selected.

�Log: Similar to the Log-Lin node, this option reveals specific log-encoded gamma profiles so that

you can select the one that matches your content. A visual graph shows a representation of the

log setting you’ve selected. When Cineon is selected from the Log Type menu, additional Lock

RGB, Level, Soft Clip, Film Stock Gamma, Conversion Gamma, and Conversion table options are

presented to finesse the gamma output.

�Remove Curve: Depending on the selected gamma space or on the gamma space found in Auto

mode, the associated gamma curve is removed from the material, effectively converting it to

output in a linear color space.

�Pre-Divide/Post-Mujltiply: Lets you convert “straight” alpha channels into pre-multiplied alpha

channels, when necessary.

TIP: All content in the DaVinci Resolve Fusion page is processed using 32-bit floating-point

bit depth, regardless of the content’s actual bit depth.

Audio Tab

The Inspector for the MediaIn node contains an Audio tab, where you can choose to solo the audio

from the clip or hear all the audio tracks in the Timeline.

The MediaIn Audio tab


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

The Audio tab in the MediaIn node is used to select the track for playback, slip the audio timing, and

reset the audio cache

If the audio is out of sync when playing back in Fusion, the Audio tab’s Sound Offset wheel allows you

to slip the audio in subframe frame increments. The slipped audio is only modified in the Fusion page.

All other pages retain the original audio placement.

Purging the Audio Cache

The audio and its settings are cached for faster performance. If you change which audio tracks

you want to play back in Fusion, or you use the Sound Offset wheel to slip the audio tracks,

you need to purge the audio cache. Also, if you return to the Edit, Cut, or Fairlight page and

modify the audio levels, you need to purge the audio cache.

To purge the audio cache after any change to the audio playback:

Click the Purge Audio Cache button in the Inspector.

The audio will be updated when you next play back the composition.

Aligning Clips from the Media Pool

When you add a clip from the Media Pool or your file system directly into a composition, the resulting

MediaIn node has more options than clips from the Edit page Timeline. These additional options make

it easier to align the Media Pool clips with other clips from the Edit or Cut page Timeline. You can also

trim clips, hold the first or last frame for a longer duration than the original media, and reverse or loop

the clip to get more range for your composition.

The Inspector parameters for a clip imported from the Media Pool.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Below is a list of controls that are added beyond the controls that appear when a clip is added from

the Edit or Cut page Timeline.

�Global In/Out: Use this control to specify the position of this node within the composition.

For instance, when the clip is added to the comp from the Media Pool, it is added at frame 0.

However, the MediaIn node from the Edit page Timeline may not start until a much later frame,

based on where it is edited into the Timeline. Use Global In to specify the frame on which that

the clip starts so that it aligned with media from the Edit page Timeline. It is easiest to view and

change the alignment of different clips in the comp while viewing the Keyframes Editor.

To slide the clip in time or align it to other clips without changing its length, place the mouse

pointer in the middle of the range control and drag it to the new location, or enter the value

manually in the Global In value control.

If the Global In and Out values are decreased to the point where the range between the In and

Out values is smaller than the n number of available frames in the clip, Fusion automatically trims

the clip by adjusting the Clip Time range control. If the Global In/Out values are increased to

the point where the range between the In and Out values is larger than the number of available

frames in the clip, Fusion automatically lengthens the clip by adjusting the Hold First/Last Frame

controls. Extended frames are visually represented in the range control by changing the color of

the held frames to purple in the control.

�Trim: The Trim range control is used to trim frames from the start or end of a clip. Adjust the Trim

In to remove frames from the start and set Trim Out to specify the last frame of the clip. The values

used here are offsets. A value of 5 in Trim In would use the 5th frame in the sequence as the start,

ignoring the first four frames. A Trim Out value of 95 would stop loading frames after the 95th.

�Hold First Frame/Hold Last Frame: The Hold First Frame and Hold Last Frame controls will hold

the first or last frame of the clip for the specified amount of frames. Held frames are included in a

loop if the footage is looped.

�Reverse: Select this checkbox to reverse the footage so that the last frame is played first and the

first frame is played last.

�Loop: Select this checkbox to loop the footage until the end of the project. Any lengthening of the

clip using Hold First/Last Frame or shortening using Trim In/Out is included in the looped clip.