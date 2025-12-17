---
title: "Dust Buster (Studio Version Only)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 643
---

# Dust Buster (Studio Version Only)

This plugin is also designed to eliminate dust, dirt, and other imperfections and artifacts from clips,

but it does so only with user guidance, for clips where the Automatic Dirt Removal plugin yields

unsatisfactory results. This guidance consists of moving through the clip frame-by-frame and

drawing boxes around imperfections you want to eliminate. Once you’ve drawn a box, the offending

imperfection is auto-magically eliminated in the most seamless way possible. This works well for dirt

and dust, but it also works for really big stains and blotches, as seen below.

(Previous page) Drawing a box around dirt in the original

image, (Above) Result in the Dust Buster plugin

In many respects, the Dust Buster is similar to the Dead Pixel Fixer, however the Dust Buster effect is

designed to repair transient bits of dust and dirt that only last for a frame or two, whereas the Dead

Pixel Fixer is designed to work on blemishes that are fixed in place for the duration of a clip.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

General

These top level controls let you choose how to draw patches with which to repair temporally unstable

dust and dirt in the frame, whether or not to show their on-screen controls, and how.

�Navigation Controls: Four buttons let you jump to frames on which you’ve drawn patches.

There are four buttons:

First Modified Frame: Jumps the playhead to the first frame of that clip with a patch.

Previous Modified Frame: Jumps the playhead to the last frame back with a patch.

Next Modified Frame: Jumps the playhead to the next frame forward with a patch.

Last Modified Frame: Jumps the playhead to the last frame of that clip with a patch.

�Draw Rect: Click and drag to place a rectangular patch of any size from one corner to the opposite

corner. Once drawn, you can click on any edge of the overlay and drag to reposition it.

�Draw Ellipse: Click and drag to place an elliptical patch of any size from one corner to the opposite

corner. Once drawn, you can click on any edge of the overlay and drag to reposition it.

�Place Patch: Lets you place small patches specifically for tiny details such as dead pixels.

When you choose this option, a New Patch Size slider appears that lets you adjust the size of the

patches you’re about to place prior to placing them. Once drawn, you can click on the edge of any

patch and drag to reposition it.

�New Patch Size: (only when Place Patch is selected) Lets you choose how large of a patch to

place using the Place Patch tool.

�Show Patches: This checkbox lets you show or hide the onscreen outline of every patch in

the Viewer.

�Reset Frame: Clears all patches from the current frame.

Patch Type

There are six methods you can use to attempt to fix the contents of a selected patch. When drawing

new patches, the currently selected Patch Type will determine what the next patch will be. When

you’ve selected an existing patch, changing the Patch Type will change how that patch works.

�Auto: The default method. Once you’ve drawn a bounding box, the two frames prior to and the

two frames after the current clip will be analyzed and compared to the current image. The best

of these 5 frames will be sampled to remove the imperfection in the current frame. Images two

frames away are prioritized since that will avoid the appearance of frozen grain, but only if they’re a

suitable match to the content of the current frame.

�+/- 1 Frame: In this mode, if you draw a bounding box from left to right, the next frame will be

drawn upon to remove the imperfection. If you draw a bounding box from right to left, the previous

frame will be used.

�+/- 2 Frames: If you draw a bounding box from left to right, the image two frames forward will be

drawn upon to remove the imperfection. If you draw a bounding box from right to left, the image

two frames back will be used.

�Spatial: Automatically fills the interior of the selected patch with pixels drawn from the

surroundings of the patch, using the Fill Method. This works well for small blemishes, but for large

blemishes a pattern might be discernible, which gives away the effect.

�Clone: Clone mode copies part of the image to fill a shape or patch placed over the thing you

want to remove. In this mode, clicking and dragging to place a Rect or Ellipse over an imperfection

is followed by a second click to place the sample region you want to clone. Clicking once to place

a Patch will be followed by a second click to place the sample region. Selecting an existing shape

or patch and choosing Clone lets you click on the shape to position the clone region. The sample

region is indicated by a dotted shape that’s connected to the original shape.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

�Blend Clone: Operates similarly to Clone mode, except the copied part of the image that fills the

Rect, Ellipse, or Patch is blended with the image to integrate it more softly.

�Fill Method: When using the Spatial Patch Type, the fill method determines how the blemish in the

image is repaired.

Grid: Samples the pixels surrounding the Rect, Ellipse, or Patch, and blurs them inward both

horizontally and vertically. Extremely effective for tiny blemishes. For larger blemishes, a grid-like

pattern may emerge.

Horizontal: Samples the pixels to the left and right of the Rect, Ellipse, or Patch, and

blurs them inward.

Vertical: Samples the pixels to the top and bottom of the Rect, Ellipse, or Patch, and

blurs them inward.

Patchy: Samples pixels from all around the Rect, Ellipse, or Patch, and expands and blurs them

together to create a soft, non-uniform region with which to repair the blemish. Doesn’t have

the patterning of the grid methods of fill, but produces an extremely smooth result.

Smooth: Simply uses a gaussian blur to repair the blemish.

Patch Options

These options let you customize the effect of a patch filling over a blemish.

�Variability: (Spatial patches only) Raising this parameter lets you make the Fill Method

less uniform.

�Soft Edges: Lets you soften the edges of the patch.

�Size Adjust: Lets you change the size of a patch after its creation.

�Mute: Lets you turn a particular patch on or off via keyframing. Useful for blemishes that only show

up for a few pixels of a shot.

�Delete Patch: Deletes the currently selected patch; you can also Option-Click any patch

to delete it as well.

Advanced Controls

These controls let you customize the UI of this effect.

�Clone Sticks to Mouse: When enabled, drawing or placing a Rect, Ellipse, or Patch in Clone or

Blend Clone mode immediately switches to positioning the sample region, making it faster to use.

�New Patches Stay Selected: When enabled, patches stay selected after you draw them, in

preparation for further customization.

�UI Line Thickness: Lets you choose how thick the on-screen outlines should be.

�Output Mode: This lets you see different representations of the patched effect you’re creating.

There are four options.

Patched Result: The final result, with each patch repairing the blemish it’s covering.

Patch Locations: Shows a key where each placed patch is white against black.

Differences: Shows the difference of each patch against the original image.

Difference Magnitude: Shows a more pronounced Differences representation.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

Frame Replacer (Studio Version Only)

The Frame Replacer allows you to reuse or blend adjacent frames together to help remove any corrupt

frames or artifacts that show up for the duration of just a single frame. It’s useful for fixing problems like

a damaged film frame or a video frame that has pixelated digital breakup.

�Replace This Frame: Checking this box selects the specific frame in the clip that you want to

replace. This will also automatically apply a keyframe at the appropriate location in the clip.

�Replacement Method: Allows you to choose the method by which the new frame is created.

From Previous: Replaces the selected frame with the one immediately before it, effectively

duplicating the frame.

From Next: Replaces the selected frame with the one immediately after it, effectively duplicating

the frame.

Blend Prev/Next: Replaces the selected frame with a blend of the frames immediately before

and after it.

Optical Flow: Replaces the selected frame using DaVinci Resolve’s optical flow technology with a

blend of the frames before and after it.

Noise Reduction (Studio Version Only)

Based on the Noise Reduction controls in the Color page, the Resolve FX Noise Reduction is divided

into two types of GPU-accelerated noise reduction designed to subdue noise in problematic clips.

Both methods of noise reduction can be used separately or together, in varying amounts depending

on the needs of the particular material you’re working on.

Temporal NR Controls

The Temporal NR controls analyze images across multiple frames to isolate noise from detail.

Motion estimation settings let you exclude moving subjects from this operation to prevent unwanted

motion artifacts.

�Frames Either Side: The number of frames on either side of the current frame that you want

averaged to separate detail from the noise. You can choose between 0 and 5 frames. 0 applies no

frame averaging; higher values apply more frame averaging, at the expense of being significantly

more computationally intensive. A higher frame setting may yield a better analysis, but may also

yield unwanted artifacts if there are fast-moving images in the frame. A value of 1 may yield better

results for fast-moving images. If you need to use higher frame values, but see artifacts, you can

also try adjusting the Motion Threshold to fix the issue.

�Motion Est. Type: Picks the method DaVinci Resolve uses to detect motion in the image.

The default, Faster, is less processor intensive, but less accurate. Choosing Better can effectively

exclude motion more accurately, but is more processor intensive. None lets you disable motion

estimation altogether, resulting in the application of Temporal NR to the entire image.

�Motion Range: Three settings, Small, Medium, and Large, let you set the speed of motion that

Motion Estimation should expect to exclude. A Small setting assumes slow-moving subjects

with little or no motion blur, allowing Temporal NR to affect more of the image at a given Motion

Threshold setting. A Large setting assumes fast motion with blur occupying a larger area of

the image, which excludes more of the image from Temporal NR at the same Motion Threshold

setting. Choose the setting that gives you the best compromise between reducing noise and the

introduction of motion artifacts when adjusting the Motion Threshold parameter.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

Temporal Threshold Controls

The Temporal Threshold parameters allow you to control which image characteristics get more or less

noise reduction.

�Luma Threshold: Lets you determine how much or how little Temporal NR to apply to the luma

component of the image. The range is 0–100, where 0 applies no noise reduction at all, and 100 is

the maximum amount. Too high a setting may eliminate fine detail from the image.

�Chroma Threshold: Determines how much Temporal NR os applied to the chroma component

of the image. The range is 0–100, where 0 applies no noise reduction at all, and 100 is the

maximum amount. Too high a setting may eliminate fine color detail from the image. However,

you may find you can raise the Chroma Threshold higher than the Luma Threshold with less

noticeable artifacting.

�Luma Chroma Same Threshold: Ordinarily, the Luma and Chroma Threshold parameters are

ganged together so that adjusting one adjusts both. However, disabling this checkbox ungangs

these parameters, allowing you to adjust different noise reduction amounts to each component of

the image, depending on where the noise happens to be worst.

�Motion: Defines the threshold separating which moving pixels are in motion (above this threshold)

versus which moving pixels are static (below this threshold). Using Motion Estimation, Temporal

NR is not applied to regions of the image that fall above this threshold, to prevent motion artifacts

by not applying frame-averaging to parts of the image that are in motion. Lower values omit more

of the image from Temporal NR by considering more subtle movements. Higher values apply

Temporal NR to more of the image by requiring faster motion for exclusion. You can choose

between 0 and 100, where 0 applies Temporal NR to no pixels, and 100 applies Temporal NR to all

pixels. The default value is 50, which is a suitable compromise for many clips. Be aware that if you

set too high a Motion Threshold, you may see artifacts in moving parts of the image.

�Blend: Lets you dissolve between the image as it’s being affected by the Temporal NR parameters

(at 0.0) and the image with no noise reduction (100.0). This parameter lets you easily split the

difference when using aggressive temporal noise reduction.

Spatial NR Controls

The Spatial NR controls let you smooth out regions of high-frequency noise throughout the image,

while attempting to avoid softening by preserving detail. It’s effective for reducing noise that

Temporal NR can’t.

�Mode: The Mode drop-down menu lets you switch Spatial NR between three different algorithms.

All three modes of operation use the same controls, so you can switch between modes using the

same settings to compare your results.

Faster: Uses a computationally lightweight method of noise reduction that’s good at lower

settings, but may produce artifacts when applied at higher values.

Better: Switches the Spatial NR controls to use a higher quality algorithm that produces greatly

superior results to Faster, at the expense of being more processor intensive to render and not

allowing you to decouple the Luma and Chroma Threshold sliders for individual adjustments to

each color component.

Enhanced: Does a significantly better job preserving image sharpness and detail when raising the

Spatial Threshold sliders to eliminate noise. This improvement is particularly apparent when the

Spatial Threshold sliders are raised to high values (what constitutes “high” varies with the image

you’re working on). At lower values, the improvement may be more subtle when compared to the

“Better” mode, which is less processor intensive than the computationally expensive “Enhanced”

setting. Additionally, “Enhanced” lets you decouple the Luma and Chroma threshold sliders so you

can add different noise reduction amounts to each color component, as the image requires.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

�Radius: Options include Large, Medium, and Small. A smaller radius offers greater real-time

performance and can provide good quality when using low Luma and Chroma Threshold values.

However, you may see more aliasing in regions of detail when using low NR Threshold values.

Setting Radius to be progressively larger results in higher quality within areas of greater visual

detail at high Luma and Chroma Threshold values, at the expense of slower performance.

An NR Radius of Medium should provide suitable quality for most images when using medium

NR Threshold settings. As with many operations, there’s an adjustable tradeoff between quality

and speed.