---
title: "Tracking"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 575
---

# Tracking

After you’ve made one or more clicks to guide the analysis, you can motion track these clicks to follow

the subject throughout that shot using the tracking controls within this palette. If you’ve made multiple

clicks, they’re all tracked at once, and each click automatically follows along with whatever image

details immediately surround that click, so there’s no set up necessary. You simply make one or more

clicks, then press the track forward or backward button. When you track a click, the overall tracking

bar shows you which frames have been tracked (tracked frames are blue).

Controls let you track all mask analysis clicks forward and backward through the shot.

Once you’ve added the clicks that are necessary to isolate the subject, and you’ve motion tracked

them to follow along with the motion of the shot, a mask is automatically generated live for each frame

of the shot. This is important to know because any change you make, adding or removing clicks or

moving them manually, will alter the resulting mask on the fly.

Fixing Masks with the Paint Tool

Occasionally the Magic Mask might miss its mark over the course of tracking and include something

in the mask you don’t want, or exclude something that you do. There is a simple paint tool available in

the toolbar to patch up holes in the mask, or remove masked areas from the selection. The paint tool

works on a frame by frame basis, and so won’t track with the mask. It’s great for removing short mask

hiccups, but for anything more than fixing a few frames, you should go back and refine your mask

using the add and subtract tools.


Color | Chapter 139 Magic Mask

COLOR

The Add/Subtract Paint Stroke tools

and the Brush Size control

The plus and minus paint tools let you add or subtract strokes from the mask as necessary, while the

paint brush size tool lets you grow or shrink the brush used to make the strokes.

(Left) In this frame, Magic Mask accidentally included the silver rings on her fingers in the mask.

For most of the track it did not, so we just need to fix a few frames. (Right) Selecting the Subtract Paint

Stroke tool (green circle) and adjusting its size, we carefully paint a hole in the mask over her rings.

The final frame, with the rings

correctly excluded from the mask


Color | Chapter 139 Magic Mask

COLOR

The Magic Mask Interface

The Magic Mask palette is divided into three sets of controls: the Toolbar, the Click list, and the Mask

Finesse panel. When you first open the Magic Mask palette, it’s empty, and you’re told to click in the

Viewer to create a mask.

The controls of the Magic Mask palette

Magic Mask Toolbar

A toolbar at the top contains most of the interactive controls of the Magic Mask palette.

Tracking Controls: The following controls let you track all available clicks to follow camera or subject

motion in the frame. From left to right, these include:

�Go To Reference Frame: Moves the playhead to the frame on which you initially made the clicks.

�Go To First Frame of Tracked Area: Moves the playhead to the first tracked frame of a range

of tracked frames in preparation for tracking backwards if there are untracked frames at the

beginning of the clip.

�Track One Frame Reverse: Tracks one frame backwards and stops. Useful if you’re tracking frame

by frame to watch the progress of a particularly complicated bit of motion. If something goes

wrong, you can back up to the last frame where the click was able to properly track the subject,

and drag the click to a better location using the pointer to make it follow the subject properly. If

necessary, you can go a frame at a time, dragging the click to a better position every time it fails to

follow the feature you’re using it to isolate.

�Track Reverse: Continuously tracks from the current frame all the way to the beginning of the clip.

�Stop Tracking: Stops tracking in cases where there’s a problem with the track and you want to

make a change.

�Track Forward and Reverse: Tracks from the current frame all the way to the end of the clip, then

returns to the original tracking point and tracks backwards to the beginning of the clip.

�Track Forward: Continuously tracks from the current frame all the way to the end of the clip.

�Track One Frame Forward: Tracks one frame forward and stops. Useful if you’re tracking frame by

frame to watch the progress of a particularly complicated bit of motion. If necessary, you can go a

frame at a time, dragging the click to a better position every time it fails to follow the feature you’re

using it to isolate.

�Go To Last Frame of Tracked Area: Moves the playhead to the last tracked frame of a range

of tracked frames in preparation for tracking forwards if there are untracked frames at the end

of the clip.


Color | Chapter 139 Magic Mask

COLOR

Click tools: Two tools at the right let you choose whether to make clicks to identify the feature you

want to isolate or identify things that aren’t the feature in order to eliminate unwanted excursions in

the resulting mask. The plus eyedropper adds an area to the mask; the minus eyedropper removes an

area from the mask.

Paint tools: The three paint tools let you do quick touchup work on a mask on a frame by frame basis.

The plus paint brush lets you add to the mask, while the minus paint brush lets you subtract from the

mask. The paint brush size control lets you change the size of the brush.

Invert Mask: A button lets you invert the resulting mask in cases where you want to use the feature

analysis of this palette to isolate everything except the feature or features being analyzed.

Mask Overlay: Turns on an onion-skinned overlay to see what parts of the image are being masked

alongside which aren’t, so you can continue to refine the result by adding, moving, or deleting clicks.

The isolated part of the mask is tinted translucent red.

Click List

Once you start making clicks to identify features for mask generation, they appear in this Click list.

Click list header: The header, at the left of the Click list, has controls for selecting and

deleting individual clicks.

Click timeline area: A Timeline ruler shows the duration of the current clip you’re creating a

mask for. The Overall Track displays how many frames of each click have been tracked. There

is a small colored mark (blue or red) on each click track to show where the reference frame is.

Mask Adjustment Controls and Matte Finesse

There are two sets of controls for refining the mask that’s output by the Magic Mask palette. The first

set of controls, at top, let you adjust how the mask is generated based on the analysis data, which lets

you refine the mask result based on characteristics of the image.

Quality: Two options let you choose a tradeoff between quality and performance. Faster lets

you generate a lower quality mask more quickly, that’s suitable for garbage matting. Better

generates a higher quality mask with more detail, that’s more processor-intensive.

Smart Refine: In Better mode this control lets you expand or contract the resulting mask

based on the analysis of the image, such that expanding the mask doesn’t expand it deeply

into surrounding parts of the image that aren’t connected to that person or object. This

operation does not introduce softness. Instead, it enlarges or shrinks the overall mask

generated by this palette.

A second set of mask manipulation controls are for manipulating the mask after it’s been generated.

Most of these are the same Matte Finesse controls that are available in the Qualifier palette, which are

useful for trying to fix issues with problem masks or soften the edges when you need to have a more

feathered result.

�Mode/Shape: Lets you choose how you want to modify the Alpha channel/key. You can choose

Shrink or Grow to dilate or erode the edges of the matte with great accuracy. Or, you can choose

Opening or Closing to plug or expand holes to clean up a ragged matte. Shape lets you choose

the shape of the growth or contraction.


Color | Chapter 139 Magic Mask

COLOR

�Radius: this slider adjusts how much to shrink, grow, open, or close the edge’s key.

�Smoothing: Smooths along the temporal frames.

�Blur Radius: In small amounts, blurring a key does well to take the edge off problem edges.

However, blurring a key can also feather the edges of a key past the border of the subject you’re

keying, with the result being a visible “halo” around your subject, depending on the adjustment

you’re making.

�Clean Black: Clean Black is a specialized operation that eliminates noise seen as white speckling

in the black area of a key. Raising Clean Black lets you “fill holes” in the background portion of a

key and erode translucent edges.

�Clean White: Clean White is another specialized operation that eliminates noise (seen as black

speckling when viewing a high-contrast highlight) in the white portion of a key that includes

areas of the image you’re isolating and expands the key by making light parts of a key lighter the

higher you raise this parameter, pushing light gray areas of the key toward white. The practical

result is that raising Clean White lets you “fill holes” in the foreground portion of a key and grow

translucent edges.

�Iterations: Refines the recognized shape.

�Denoise: Provides a distinct way to post-process extracted keys to selectively reduce the noise in

a key, getting rid of stray areas of qualification and softly filling holes in a matte.

�In/Out Ratio: Using In/Out Ratio can help eliminate fringing. Raising In/Out Ratio will fill in small

black holes in the matte, while lowering In/Out Ratio below 0 will eliminate speckling by pushing

small white bits of the matte toward black.

�Black Clip: Raising Black Clip applies a “lift” adjustment such that translucent areas of the matte

(gray areas when viewing a high-contrast highlight) are pushed toward black.

�White Clip: Lowering White Clip applies a “gain” adjustment such that translucent areas of the

matte (gray areas when viewing a high-contrast highlight) are pushed toward white.

�Post Filter: Performs a final clean up of the key, using the original image for reference; useful for

bringing back some fine detail in sharp edges or hair.

�Consistency: After you’ve tracked each click to follow the subject over the duration of the clip,

this setting lets you choose how much temporal smoothing is necessary to ameliorate jitter in the

edges of the resulting mask in areas of low confidence, such as frizzy hair or translucent clothing.

Higher settings apply more smoothing to the edges of the mask but are more processor intensive

and may affect how closely the mask follows motion in the image. Lower settings will be faster and

more accurate but may allow more edge jitter in the resulting mask, which can be distracting in

the final adjustment you’re making. This parameter defaults to 0, so your first application of Magic

Mask will always begin with the most accurate (and potentially most active) application of this

feature’s analysis.

IMPORTANT: Consistency requires a click to have a duration of at least a few frames in order

to function correctly. This requires you to track each click to follow the motion of the camera

and subject in order to extend the duration of each click. Because Consistency is trying to

eliminate one or two frame “noise” in the shape of the mask, clicks of short duration may end

up having their effect eliminated.

NOTE: The original Magic Mask is still accessible in DaVinci Resolve 20 by selecting Legacy

Object Mask from the Magic Mask 2 options menu.


Color | Chapter 139 Magic Mask

COLOR