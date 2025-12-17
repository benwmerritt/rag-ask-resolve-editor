---
title: "The Five Color Page Sizing Modes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 618
---

# The Five Color Page Sizing Modes

The Sizing Palette on the Color page can be put into one of five modes, each of which accomplishes a

different task.

�Edit Sizing: These controls mirror those found in the Inspector of the Edit page.

�Input Sizing: These controls let you make sizing adjustments to individual clips that affect their

overall geometry (pan, tilt, zoom, and rotation). These controls are useful for doing clip-by-clip pan

and scan adjustments.

�Output Sizing: These controls are nearly identical, except that they affect every clip in the entire

timeline, all at once. Output sizing is useful for making a formatting adjustment to an entire

timeline, such as changing an HD timeline to an SD timeline with simple adjustments to crop and

pan the resulting framing.

�Node Sizing: Lets you add targeted sizing adjustments at any point within the node tree. Like Input

Sizing, Node Sizing is specific to a particular clip. Unlike Input Sizing, Node Sizing is affected by

operations that split color channels (such as the splitter/combiner nodes) and limit the image (such

as qualifiers and windows). You can also add as many node sizing adjustments to a clip’s grade

as you need.

�Reference Sizing: A set of sizing controls that lets you reposition the still when a wipe comparison

is being made. Using these controls, you can move the still image to better compare it to the clip

you’re wiping it against. The Reference Sizing controls only work when you have a wipe enabled.

Sizing Order of Processing on the Color Page

Input Sizing adjustments are applied before all image processing that takes place in the node graph,

including Node Sizing, while Output Sizing adjustments are applied after image processing in the

node graph.

Sizing Controls

Input, Node, and Output Sizing share many of the same controls. When the Sizing palette is set to

Input Sizing mode, the controls transform each clip individually. If you’re simply pushing in on one or

two clips, or making individual pan and scan adjustments to account for a change in format, these are

the controls you want to use.

The Sizing palette


Color Page Effects | Chapter 152 Sizing and Image Stabilization

COLOR

�Pan: Moves the clip along the horizontal, X axis. Positive values move the clip right, negative

values move the clip left.

�Tilt: Moves the clip along the vertical, Y axis. Positive values move the clip up, negative values

move the clip down.

�Zoom: Adjusts the overall dimensions of the clip. The range is from 0.250 (1/4x size) to

4.000 (4x size). Normal size is 1.000.

�Rotate: Positive values rotate the clip clockwise. Negative values rotate the clip counter-clockwise.

�Width: Stretches the image wider or narrower. The range is from 0.250 (1/4x width) to

4.000 (4x width). Normal width is 1.000.

�Height: Stretches the image taller or shorter. The range is from 0.250 (1/4x height) to

4.000 (4x height). Normal height is 1.000.

�Pitch: Rotates the image toward or away from the camera along an axis running through the

center of the image, from left to right. Positive values push the top of the image away and bring

the bottom of the image forward. Negative values bring the top of the image forward and push

the bottom of the image away. Higher values stretch the image more extremely.

�Yaw: Rotates the image toward or away from the camera along an axis running through the center

of the image from top to bottom. Positive values bring the left of the image forward and push the

right of the image away. Negative values push the left of the image away and push the right of the

image forward. Higher values stretch the image more extremely.

�Key Lock: (Node Sizing only) Lets you choose how regions of the image that are isolated by one or

more windows will be transformed. There are two options:

Off: While off, the transform controls will move the windowed region to another area of the frame,

effectively duplicating the windowed area.

On: While on, the transform controls will move other areas of the frame into the windowed regions,

effectively covering up the windowed area with another portion of the picture.

�Flip Image: Two buttons let you flip the image in different dimensions.

Flip Horizontal control: Reverses the image along the X axis, left to right.

Flip Vertical control: Reverses the clip along the Y axis, turning it upside down.

�Lens Correction: (Edit Sizing only) Two controls let you correct for lens distortion in the image, or

add lens distortion of your own (only available in the Studio version).

Analyze: Automatically analyzes the frame in the Timeline at the position of the playhead for

edges that are being distorted by wide angle lens. Clicking the Analyze button modifies the effect

of the Distortion slider so that it gives a more accurate result, but it doesn’t perform a correction.

Distortion: Dragging this slider to the right applies a warp to the image that lets you straighten the

bent areas of the picture that can be caused by wide angle lenses. It’s not necessary to click the

Analyze button prior to using this slider, but using the Analyze button can improve the accuracy of

the result.

Blanking Controls

Output Sizing mode also has a set of Blanking controls that you can use to add custom blanking

to a clip or project. For example, you can use these controls to add nonstandard letterboxing or

pillarboxing to an image. Along with all other Output Sizing adjustments, blanking is added last in the

image processing pipeline, so it’s not affected by any of the color or contrast adjustments you make.

�Top: Adjusts the top letterbox.

�Right: Adjusts the right pillarbox.

�Bottom: Adjusts the bottom letterbox.


Color Page Effects | Chapter 152 Sizing and Image Stabilization

COLOR

�Left: Adjusts the left pillarbox.

�Smooth: A checkbox that lets you turn on edge anti-aliasing for source blanking. Overrides the

Anti-alias Edges drop-down menu found in the Image Scaling panel of the Project Settings.

NOTE: It might be necessary to turn anti-aliasing off if you notice black blurring at the edges

of blanking being applied to an image.

Blanking presets are also available by choosing from the Timeline > Output Blanking submenu.

Choosing one of these options automatically sets the Blanking parameters of the Sizing palette’s

Output Sizing mode. The following presets are available:

1.33: SD or 4:3

1.66: European theatrical

1.77: HD or 16:9

1.85: Theatrical flat aspect ratio

2.00: Univisium. Aspect ratio designed to accommodate both theatrical

wide-screen and HD delivery.

2.35: Original anamorphic (scope) theatrical wide-screen

2.39: Current 35mm anamorphic  (scope) theatrical wide-screen

2.40: Current 35mm anamorphic (scope) theatrical wide-screen (rounded up for Blu‑Ray)

Reset: Restores the clip to its original aspect ratio.

Anti-aliasing at the edges of blanking is handled by an Anti-Alias Edges setting in the Image Scaling

panel of the Project Settings. For more information, see Chapter 4, “System and User Preferences.”

Resetting the Sizing Palette

You can reset every control within the Sizing palette at any time by clicking the reset button in the

upper right-hand corner of the palette.

Input and Output Sizing Presets

If there are Input or Output Sizing settings that you find yourself using repeatedly, you can save them

as presets for easy recall. For example, if there’s a group of input settings that you use to resize

a clip of a particular format to match the current project, you can save it as a preset that you can

use whenever.

�Preset drop-down menu: Provides access to all the currently saved presets in the current

project library.

�Delete Preset: To delete a preset, select it from the drop-down menu, click the trash can button,

then click OK.

�Save As New Preset: To add a preset, make whatever settings adjustments you need, then click

the plus button. When the Format Preset dialog appears, enter a name, check that the settings are

correct, then click Save in the Format Preset window.

�Update Preset: To change a preset, load the preset you want to change, make whatever changes

you need, then click Update in the Format Preset window.


Color Page Effects | Chapter 152 Sizing and Image Stabilization

COLOR

The Input and Output Sizing modes save different presets. Each of these sets of presets is available

from the “Override input scaling” and “Override output scaling” drop-down menus in the Image

Scaling project setting menu.

Using Node Sizing for

Channel and Paint Effects

Using Node Sizing, you can apply individual sizing adjustments on a per-node basis. All Node Sizing

adjustments within a grade are cumulative, and any keyframing done to Node Sizing parameters is

stored in that node’s Node Format keyframe track in the Keyframe Editor. Two good examples of Node

Sizing include realigning color channels individually in conjunction with the Splitter/Combiner nodes,

or duplicating windowed regions of an image by moving them around the frame.

Example 1

Using node sizing on individual color channels:


Choose Color > Nodes > Add Splitter/Combiner Node to add this node structure to the

current grade.


Select one of the three Corrector nodes connected between the Splitter and Combiner nodes that

corresponds to the color channel you want to transform.

Adding the Splitter/Combiner nodes to use Node Sizing on individual color channels


Open the Sizing palette, choose Node Sizing from the mode drop-down, and use the Sizing

parameters to transform that channel as necessary. For example, if you have an old video clip with

misaligned color components, you could pan a misaligned channel to the left or right to try and

improve its alignment.


Color Page Effects | Chapter 152 Sizing and Image Stabilization

COLOR

Before and after panning the green channel

Example 2

Using Node Sizing to duplicate a windowed area of an image to cover a blemish:


Create a new node.


Open the Window palette, create a Circular window, and then shrink and reposition it to surround

a feature you want to remove.


Open the Tracking palette, and track the window to follow the feature to be removed.


After the track is complete, now move the window to an adjacent area of clean detail that’s right

next to the feature you want to remove. This is the area of the image you’re going to duplicate and

cover the unwanted feature with.


Now, open the Sizing palette, choose Node Sizing from the mode drop-down, check Key Lock,

and use the Sizing parameters to move a duplicate of the windowed area to cover up the

unwanted feature.


Color Page Effects | Chapter 152 Sizing and Image Stabilization

COLOR

Before/after using Node Sizing to clone an area of the image to

cover up the actor with a plant to create a clean background

When you’re done, playing through the clip should show that the duplicated area of the image

is still tracking the feature you want to remove.