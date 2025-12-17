---
title: "Opacity"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 195
---

# Opacity

Each clip has an Opacity parameter, available in the Inspector, that lets you make it more transparent,

in a range from 0 (totally transparent) to 100 (totally opaque). When set to a value less than 100,

the selected clip is mixed with whatever clip is underneath it on the Timeline, according to the

composite mode that’s currently used. If no clip appears underneath the Timeline, then the clip is

mixed with black.

By keyframing this parameter, you can create more complicated fade to black effects or cross

dissolves. Keyframing is covered in more detail in Chapter 53, “Keyframing Effects in the Edit Page.”

To change a clip’s opacity:

Select the clip you want to adjust, open the Composite controls in the Video Inspector, and set

the Opacity slider to create the desired amount of transparency.

Video Fader Handles

If you want to dissolve a clip to or from another clip, or to or from black, the traditional way to do so has

been to use one of the transitions in the Effects Library. However, you can also use fader handles that

appear at the beginning and end a clip when you position the pointer right over it. Fader handles are a

fast, ubiquitous method of creating a fade to or from black. However, they also make it easy to fade to

or from other clips that are underneath one that’s superimposed, as seen in the following screenshot.

Dragging a video fader handle on a clip in track V2


Editing Effects and Transitions | Chapter 50 Compositing and Transforms in the Timeline

EDIT

To use a fader handle, move the pointer over the clip you want to adjust, and when small white fader

handles appear at the upper left and upper right of the video of the clip, drag them to the left or right

for the duration you want the fade effect to last.

Fade In and Out to Playhead Commands

A pair of commands in the Trim menu let you use the playhead position over a clip to “Fade

In to Playhead” or “Fade Out to Playhead.” This can be done for a single clip or for multiple

superimposed clips.

These commands work for both audio and video items, in both the Edit and Fairlight pages.

Alpha Channel Support

If a superimposed video or still image clip in the Timeline has an embedded alpha channel, that alpha

channel automatically creates transparency within that clip, compositing it against whatever is in the

track underneath. There’s no need for you to do anything for this to work.

Superimposing a clip with an alpha channel above automatically composites that clip against the clip beneath it

However, if you need to disable or alter the interpretation of an alpha channel for any clip, for example

if a clip is being interpreted as having an alpha channel of the wrong type, you can right-click that clip,

choose Clip Attributes from the contextual menu, and use the Alpha Mode pop-up menu of the Clip

Attributes Video panel to correct the problem.

NOTE: If you’ve imported clips with alpha channels, those alpha channels can be rendered

back out for Round Trip workflows. Choose a Format and Codec combination that supports

alpha channel output, and turn on the Export Alpha checkbox in the Video panel of the

Render Settings list.


Editing Effects and Transitions | Chapter 50 Compositing and Transforms in the Timeline

EDIT

Keying in the Timeline Using Resolve FX

You can pull keys directly in the Timeline using the Resolve FX Key filters. These are found in the

Resolve FX section of the Open FX category, of the Effects Library. The filter options are 3D Keyer,

HSL Keyer, and Luma Keyer.

For more information about using Resolve FX Key filters, see Chapter 159, “Resolve FX Key.”

Below is an example of using the Resolve FX 3D Keyer filter in the Timeline.

Setting Up a Green Screen (Chroma Key) on the Timeline

To set up a green screen composite, place your background video on a track underneath your

foreground video, and drag the 3D Keyer onto the foreground clip.

To adjust the key’s parameters, click on the Effects icon in the Inspector to reveal the Keyer’s controls,

and Select “Open FX Overlay” from the Transform Mode drop-down menu in the lower left of the

Timeline Viewer, to allow the effect qualifiers to work on the Timeline Viewer.

Applying the 3D Keyer to the News Anchor clip on the V2 Timeline; note that the “Open FX Overlay”

mode on the Viewer is selected (circled), allowing you to use the Inspector Effect controls in the Viewer.

To pull a Chroma Key in the Timeline using the 3D Keyer.


Superimpose your green screened foreground video on a track on top of your background video.


Put the Timeline Viewer in Open FX Overlay mode, using the drop-down menu at the lower left of

the Viewer. This option allows you to use the effect GUI controls directly on the Viewer.


Editing Effects and Transitions | Chapter 50 Compositing and Transforms in the Timeline

EDIT


Drag the 3D Keyer from the Effects Library onto the foreground video. The 3D Keyer is a fast and

high-quality keyer that’s easy to use, drawing strokes to identify the background and foreground

of the image you’re trying to key.


Select the foreground video clip, and open the 3D Keyer from the Effects tab in the Inspector.


Click the Pick eye dropper icon in the Controls section, and click and drag across the green

screen in the Timeline Viewer. A blue line will show you where you’ve selected, and the green

screen should mostly become transparent.


Optional) Use the Add eye dropper (drawing blue lines), to click and drag over any parts of the

green screen that are still not transparent. Use the Subtract eye dropper (drawing red lines) to add

back any foreground elements that may have gone transparent by mistake.


Turn on the Despill checkbox in the 3D Keyer to remove any green light (spill) that may have

reflected onto your foreground subject from the green screen.

Using Resolve FX and Open FX

Alpha for Track Compositing

DaVinci Resolve allows the direct use of the alpha channel from Resolve FX and Open FX plugins for

compositing on the Timeline. If an effect creates transparency in the image, a “Use alpha” checkbox

appears at the bottom of the effects parameters in the Effects tab of the Inspector. Checking this

box immediately applies the alpha channel to the selected clip, compositing it over any background

elements that appear in lower tracks. If more than one alpha-modifying effect is applied to a single

clip, the alpha channels are mixed together.

The Use Alpha checkbox at the bottom

of the Effects tab in the Inspector

Transform and Cropping

in the Video Inspector

DaVinci Resolve is a resolution-independent application. This means that, whatever the resolution of

your source media, it can be output at whatever other resolution you like. This also means that you can

freely mix clips of any resolution, fitting 4K, HD, and SD clips into the same timeline, and scaling each

to fit the project resolution as necessary.

Your project’s resolution can be changed at any time, allowing you to work at one resolution, and

then output at another resolution. This also makes it easy to output multiple versions of a program at

different resolutions, for example, outputting both HD and 4K sized versions of the same program.

DaVinci Resolve has a powerful toolset for making geometric transforms, using advanced algorithms

for optical-quality sizing operations. Within the Edit page, each clip has a set of transform parameters,

principally for use in storing sizing data imported from AAF or XML when you turn on the “Use sizing

information” checkbox. This has the advantage of keeping these imported Edit Transform settings

separate from the Input Sizing parameters found on the Color page, which are typically used by the

colorist to make pan and scan adjustments of various kinds.


Editing Effects and Transitions | Chapter 50 Compositing and Transforms in the Timeline

EDIT

Of course, you can also use these controls to create your own adjustments while working in the

Timeline, zooming into clips, repositioning them to improve the composition, and so on. While there

is some overlap between these parameters and those in the sizing palette of the Color page, they’re

both separate sets of parameters, so you can keep each set of adjustments separate.

When the time comes to output your program, the final resolution of each clip is calculated taking into

account the original resolution of the source media, the timeline resolution, image scaling settings, Edit

page transforms, and Color page transforms, so that the final resolution correctly uses the cleanest

geometric transformation based on the maximum resolution available to each source clip.

Transform

The Video Inspector transform group includes the following parameters, which are also editable in the

Edit Sizing mode of the Sizing palette in the Color page:

Zoom X and Y: Allows you to blow the image up or shrink it down. The X and Y parameters can

be linked to lock the aspect ratio of the image, or released to stretch or squeeze the image in one

direction only.

Position X and Y: Moves the image within the frame, allowing pan and scan adjustments to be made.

X moves the image left or right, and Y moves the image up or down.

Rotation Angle: Rotates the image around the anchor point.

Anchor Point X and Y: Defines the coordinate on that clip about which all transforms are centered.

Pitch: Rotates the image toward or away from the camera along an axis running through the center

of the image, from left to right. Positive values push the top of the image away and bring the bottom

of the image forward. Negative values bring the top of the image forward and push the bottom of the

image away. Higher values stretch the image more extremely.

Yaw: Rotates the image toward or away from the camera along an axis running through the center of

the image from top to bottom. Positive values bring the left of the image forward and push the right

of the image away. Negative values push the left of the image away and push the right of the image

forward. Higher values stretch the image more extremely.

Flip Image: Two buttons let you flip the image in different dimensions.

�Flip Horizontal control: Reverses the image along the X axis, left to right.

�Flip Vertical control: Reverses the clip along the Y axis, turning it upside down.

Smart Reframe (Studio Version Only)

The Smart Reframe feature makes it easier to quickly reframe material across extreme aspect ratio

changes. It’s useful for situations where you’ve shot a 16:9 horizontal video and find yourself needing

to create a vertically-oriented 9:16 version for mobile phones and social media deliverables, or

using 4:3 archival footage in a 2.39:1 widescreen movie. Smart Reframe can be used manually, or

automatically executed using the DaVinci Resolve Neural Engine.

Object of Interest: Tools for selecting the subject that the resize will frame around.

�Auto: DaVinci Resolve’s Neural Engine will analyze the clip and choose its most representative

object. This will be the only option if more than one clip is selected for Smart Reframing.

�Reference Point: Allows you to manually adjust a bounding box around the subject

to reframe around.

Reframe: This button executes the Smart Reframe command. This can take some time depending on

the length and number of clips.


Editing Effects and Transitions | Chapter 50 Compositing and Transforms in the Timeline

EDIT