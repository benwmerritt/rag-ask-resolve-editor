---
title: "Transform"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 656
---

# Transform

The Transform Resolve FX adds considerable control over the standard transforms in the Inspector’s

Sizing or the Color page Sizing palette. This effect includes all the standard Position, Tilt, Zoom,

and Rotate controls but adds corner pinning, two kinds of on-screen controls, motion blur, and

Edge behavior controls.

General

�Control Mode: This drop-down menu includes three methods for controlling the transforms.

One is based on sliders in the Inspector, while the other two are based on manipulating

the Viewer’s image.

Sliders: Uses sliders and checkboxes in the Inspector to control the transforms. This method has

no Viewer overlays with which to control the position, scale, or rotation but provides exact control

using numeric values.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Interactive-Canvas: Choosing this mode moves the controls from the Inspector to the Timeline

Viewer. The Viewer’s controls are shown as a bold white outline and four vertices, one at

each corner. You can drag on any part of the white outline for stretching, squeezing, and

corning pinning. Dragging the center of the image repositions the frame. The red subdivision

overlays make it easy to create shearing effects by dragging line segments to move two

corners simultaneously.

Interactive-Pins: Adjusting the image in this mode is done by manually placing control points,

called pins, in the Timeline Viewer. Adding one pin only gives you position control. At least two

points are required for scaling and rotation. Dragging on one of the pins scales or rotates the

image around the other pin. Using three pins, you can create perspective distortions by dragging

any one of the pins. You can add up to four pins for unique corner pinning distortions.

TIP: You can Option-Click on a pin to remove it or use the Reset Canvas button to

remove all the pins.

Resolve FX Transform Interactive-Canvas mode (Top) and Interactive-Pins mode (Bottom)

Only one Control mode can be active at a time. For instance, you cannot make adjustments with the

sliders and then switch to one of the interactive methods. The sliders will be reset once a different

method is selected. However, can you apply two Transform effects to a clip, adjusting one with Sliders

and the other using an interactive method.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Position Controls

�Canvas Keyframe: Only displayed when the Control mode is set to Interactive-Canvas or

Interactive-Pins. The Canvas Keyframe has no control except for a keyframe button allowing you

to keyframe the changes you make in the Viewer.

�Reset Canvas: Resets any interactive changes made in the Viewer and any keyframes created

from those changes.

The following parameters are only displayed when the Control Mode is set to Sliders.

�Position X and Y: Moves the image within the frame, allowing pan and scan adjustments to be

made. X moves the image left or right, and Y moves the image up or down.

�Zoom: Allows you to blow the image up or shrink it down.

�Rotate: Rotates the image around the center.

�Width: Stretches or squeezes the image in one direction only.

�Height: Stretches or squeezes the image in one direction only.

�Pitch: Rotates the image toward or away from the camera along an axis running through the

center of the image, from left to right. Positive values push the top of the image away and bring

the bottom of the image forward. Negative values bring the top of the image forward and push the

bottom of the image away. Higher values stretch the image more extremely.

�Yaw: Rotates the image toward or away from the camera along an axis running through the center

of the image from top to bottom. Positive values bring the left of the image forward and push the

right of the image away. Negative values push the left of the image away and bring the right of the

image forward. Higher values stretch the image more extremely.

�Flip Horizontal/Vertical: Two checkboxes let you flip the image in different dimensions.

Flip Horizontal: Reverses the image along the X-axis, left to right.

Flip Vertical: Reverses the clip along the Y-axis, turning it upside down.

Image Adjustment

�Crop: This checkbox exposes the crop tools, allowing you to selectively remove parts of the frame

from each side.

�Edge Softness: This control sets the amount of feathering to the Alpha channel for compositing.

�Edge Rounding: This control rounds the corners of the Alpha channel for compositing.

Animation

�Motion Blur: Keyframing the transform so the frame moves rapidly will create a blurring effect.

The amount of the blur is controlled using the Motion Blur slider.

Advanced Options

�Edge Behavior: This menu determines how edges of the frame are handled when the transforms

are scaled smaller than the Timeline Resolution.

Transparent: The area outside the transformed image is set to be transparent, allowing the video

on tracks underneath this one to be shown behind the image.

Reflect: The image is flipped and flopped to create a mirrored image, which extends to the

Timeline Resolution frame boundary.

Wrap-Around: Duplicates the image to create a video wall effect, which is used to fill in the space

to the Timeline Resolution frame boundary.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Replicate: Duplicates the outermost pixels along the edge of the image. The pixels are stretched

out from each side to reach the Timeline Resolution boundary.

�Composite Type: Sets the Composite type for blending multiple video layers together.

For more information on what each Composite type does, see Chapter 50, “Compositing and

Transforms in the Timeline.”

Global Blend

�Blend: Lets you dissolve between the image with no Transform applied and one with the

Transform fully applied.

Video Collage

Video Collage is designed to make it easier to create grid-based layouts of multiple video layers to

create different kinds of split-screen effects, where each video layer appears within a “tile” that can be

styled in different ways. Layout controls let you choose how many rows and columns there are, which

determine how many tiles are available to arrange tiles of video next to one another in different ways,

with additional controls for creating offsets, changing the margins around and spacing between the

tiles, and rounding the corners of each tile.

This effect is designed to be used in the Cut and Edit pages, and there are two ways that you can set

this up, which are chosen using the Workflow drop-down menu.

Create Background

The Create Background option is perhaps the simplest way to create a split-screen using this effect.

This mode creates a frame with holes in it, behind which you can position multiple layers of video.

These clips are placed on tracks underneath the background clip in the Timeline, and use each clip’s

individual sizing controls in the Inspector (which can be used via on-screen Transform controls in the

Viewer) to scale and position them correctly within the holes. The Video Collage effect is applied

to the topmost superimposed video or still image clip in the Timeline, in order to use that clip as a

background for the frame.

In the following example, the Video Collage effect is applied to the clip on track 5, which has four

other clips underneath it in a stack, each of which has been positioned to fit in one of the holes of

the frame.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

A stack of clips to create a split-screen effect; the top-most clip is used as the

background by the Video Collage effect in Create Background mode, while the stack of

clips underneath are all positioned to fit into the holes created in the top clip.

Create Background mode makes it easy to create a split-screen layout of different clips without

having to resize them with precision to align the edges and sizes of each clip. The width of the

frame that’s created gives some wiggle-room to reposition and animate each individual clip within

the hole it shows through. You can see the resulting effect created in the previous example below.

The resulting split-screen effect, with four clips arranged to show through the holes created

in the top “background” clip that’s creating the frame; you can see the onscreen controls

corresponding to the clip on track 4 that have been used to position and resize it to fit.

Create Tile

This mode of operation is a bit more work to set up, as it requires you to create a layout in one

instance of this effect, but it gives you more options, automatically transforming each layer of video in

your stack of clips in the Timeline to fit a layout you design. The best way to work in Create Tile mode

is to edit a stack of superimposed clips in the Timeline, but this time if there’s a clip you want to use as

the background, it should go at the bottom of the stack.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

A stack of clips to create a split-screen effect in Tile mode;

the bottom clip is going to be used as the background.

Then, apply the Video Collage clip to the topmost clip, and set the Workflow drop-down menu to

Create Tile. Immediately, you’ll see that the current layer has been fit inside the first rounded tile

of the default layout of four tiles. For clarity, video tracks 4, 3, and 2 have been muted so you can

see the current clip turned into a tile against the bottom clip that serves as the background for

this arrangement.

The topmost clip set to create the first tile in a layout; video tracks 4, 3, and 2 are disabled

to show the top clip against the bottom clip that’s being used as the background.

Ultimately, you’ll use Paste Attributes to apply a copy of this effect to each clip on the Timeline that’s

supposed to fit inside a tile, and once you choose which clip goes inside each tile, that’s what will

create the arrangement. Before you do that, however, you need to customize the layout.

To get a preview of the entire layout for further customization, turn on the Preview Layout checkbox in

the Inspector. This draws a preview of how all the tiles will be placed using the current layout. Using

this preview, you can make whatever changes you want to set things up, before you copy this plugin to

all the other clips in the stack.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Turning on Preview Layout to customize the layout

With Preview Layout enabled, you can use the Layout controls below to choose how many columns

and rows of tiles there are, to stagger the tiles horizontally or vertically, to round or square off each tile

by a variable amount, and to alter the margins and spacing. In this way, you can create a wide variety

of different symmetrical layouts really easily. In this example, we’ll create a layout with one row, three

columns, that’s staggered vertically.

Our new customized layout, shown next to the Inspector controls for this effect

Now that this is done, we’ll turn off Preview Layout to focus on the current clip’s integration into our

layout, and we can see that it doesn’t quite fit into the box. Click the Tiles button in the Inspector. This

reveals the Tile-specific controls, which include the Resize Content controls. Click the disclosure control

to open these up, and use the Pan, Tilt, and Zoom controls to make this image fit into the tile full screen.

Tiles controls in the Inspector with Preview Layout disabled,

so we can focus on customizing the current tile


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

You should also note the Active Tile drop-down menu. This menu serves two purposes. First, it

defines which tile the current clip is displayed within. This becomes important later on when you apply

this effect to multiple superimposed clips. However, it also determines which tile you further customize

using the Tile-based controls of the Inspector. If needed, tiles can be individually styled.

The Manual Tile Management checkbox is off by default, which enables DaVinci Resolve to

automatically update the number of tile entries in the Active Tile drop-down menu with items equal to

the number of grid positions (or grid nodes) defined by the rows and columns you’ve set, without you

needing to do anything. For simple symmetrical layouts, this is easiest. However, if you turn Manual

Tile Management on, you gain the ability to add and delete tile positions manually, which enables

other options. For now, we’ll leave this turned off.

(Left) The Active Tile drop-down with Manual Tile Management turned off, (Right) The Active Tile controls

with Manual Tile Management turned on, and additional controls for manual tile management displayed

So, now we’ve created a custom overall layout, and we’ve tailored the top clip in the stack to fit the

first tile in the layout. Now it’s time to apply this effect to the next two clips in the stack (remember the

bottom clip will be used as a background, so it doesn’t need this plugin applied to it). Select the top

clip with the effect applied to it in the Timeline, and press Command-C to copy it. Then, select the next

two clips, right-click one of them, and choose Paste Attributes (Option-V). When the Paste Attributes

window appears, turn on the Plugins checkbox, in Video Attributes and click Apply. Those two clips

disappear as they receive the Video Montage effect and fit themselves into Tile 1, just like the top clip.

Using Paste Attributes to apply the copied effect from the top clip to the other clips in this arrangement


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

To assign each clip to the correct tile in the layout, select each clip in the arrangement, one at a time,

open the Effects panel of the Inspector, click the Tiles button in the Inspector (if necessary), and set

each clip to be the next available tile in the Active Tile drop-down menu. In this example, the top clip

was in Tile 1, the second clip down will be in Tile 2, and the third clip down will be in Tile 3.

Assigning the Active Tile for each layer in the Timeline

TIP: If you enable the Open FX Overlay of the Timeline Viewer, each tile has an overlay that

lets you click a tile in the Viewer to make that the Active Tile.

If you like, you can rearrange which clips go into which tiles using this control, but for now we’ll keep

things simple. As you do this, each tile becomes populated, and the final layout is revealed, with the

background clip showing behind everything. If necessary, you can use the Resize Content controls (in

Tiles mode) to resize each tile’s contents to fit the tile better.

The current layout, with each clip in the stack assigned to a different tile

NOTE: If you’ve customized a layout, copied and pasted attributes to the other clips you

want to use in that layout, and have assigned each clip to its position in the layout, and you

then decide you need to make a change to the Globals layout controls, you’ll need to go

through the process of copying the updated effect, pasting attributes to the other clips, and

reassigning each clip to the appropriate position in the layout to make that update to the

other clips as well.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

So, these are the overall workflows of the Video Collage effect. There is, of course, much

more you can do, but this is the basis of how you create your initial layout.