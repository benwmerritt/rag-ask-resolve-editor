---
title: "General"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 642
---

# General

These top level controls let you choose how to draw patches with which to repair blemishes in the

frame, whether or not to show their on-screen controls, and how.

�Draw Rect: Click and drag to place a rectangular patch of any size from one corner to the opposite

corner. Once drawn, you can click on any edge of the overlay and drag to reposition it.

�Draw Ellipse: Click and drag to place an elliptical patch of any size from one corner to the opposite

corner. Once drawn, you can click on any edge of the overlay and drag to reposition it.

�Place Patch: Lets you place small patches specifically for tiny details such as dead pixels. When

you choose this option, a New Patch Size slider appears that lets you adjust the size of the patches

you’re about to place prior to placing them. Once drawn, you can click on the edge of any patch

and drag to reposition it.

�New Patch Size: (only when Place Patch is selected) Lets you choose how large of a patch to

place using the Place Patch tool.

�Show Patches: This checkbox lets you show or hide the onscreen outline of every

patch in the Viewer.

�Hide During Interaction : Hides the onscreen outline of every patch in the Viewer while you’re

moving a patch; this makes it easier to see the effect of moving the patch on the image, without

the outline getting in the way.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

Patch Type

There are three methods you can use to attempt to fix the contents of a selected patch. When drawing

new patches, the currently selected Patch Type will determine what the next patch will be. When

you’ve selected an existing patch, changing the Patch Type will change how that patch works.

�Spatial: Automatically fills the interior of the selected patch with pixels drawn from the

surroundings of the patch, using the Fill Method. This works well for small blemishes, but for large

blemishes a pattern might be discernible, which gives away the effect.

�Clone: Clone mode copies part of the image to fill a shape or patch placed over the thing you

want to remove. In this mode, clicking and dragging to place a Rect or Ellipse over an imperfection

is followed by a second click to place the sample region you want to clone. Clicking once to place

a Patch will be followed by a second click to place the sample region. Selecting an existing shape

or patch and choosing Clone lets you click on the shape to position the clone region. The sample

region is indicated by a dotted shape that’s connected to the original shape.

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

together to create a soft, non-uniform region with which to repair the blemish. Doesn’t have the

patterning of the grid methods of fill, but produces an extremely smooth result.

Smooth: Simply uses a gaussian blur to repair the blemish.

Patch Options

These options let you customize the effect of a patch filling over a blemish.

�Variability: (Spatial patches only) Raising this parameter lets you make the Fill Method

less uniform.

�Soft Edges: Lets you soften the edges of the patch.

�Size Adjust: Lets you change the size of a patch after its creation.

�Mute: Lets you turn a particular patch on or off via keyframing. Useful for blemishes that only show

up for a few pixels of a shot.

�Delete Patch: Deletes the currently selected patch; you can also Option-Click any

patch to delete it as well.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

Advanced Controls

These controls let you customize the UI of this effect.

�Clone Sticks to Mouse: When enabled, drawing or placing a Rect, Ellipse, or Patch in Clone or

Blend Clone mode immediately switches to positioning the sample region, making it faster to use.

�New Patches Stay Selected: When enabled, patches stay selected after you draw them, in

preparation for further customization.

�UI Line Thickness: Lets you choose how thick the on-screen outlines should be.

�Patches Stick to: This parameter lets you deal with fixing dead pixels or blemishes on clips that

have been stabilized.

Source: Patches you place stay put, unless you apply motion stabilization to the shot, in which

case the patches are transformed along with the image so they remain “stuck” to the feature in the

source clip they’re fixing.

Scene: If you’re eliminating a blemish on a moving subject, you can use the FX Tracker to track the

thing you’re fixing, so the patch follows along with it.

�Output Mode: This lets you see different representations of the patched effect you’re creating.

There are four options.

Patched Result: The final result, with each patch repairing the blemish it’s covering.

Patch Locations: Shows a key where each placed patch is white against black.

Differences: Shows the difference of each patch against the original image.

Difference Magnitude: Shows a more pronounced Differences representation.

Deband (Studio Version Only)

Low bit-depth media that has areas with shallow gradients of color, such as a sky or a wall, often

exhibit color banding, seen as visible stripes, because there aren’t enough color values to smoothly

represent the gradiation from light blue to darker blue in the sky.

An example of banding in the sky of an image

Minimizing banding using the Deband filter

This filter is designed to isolate the edges of color banding and minimize them by dithering pixels

from either side to soften the transition. This filter works best when applied to regions of the image

that have been isolated with a secondary qualifier or window, otherwise you risk all edges within your

image being dithered and thus softened (although this can be an interesting stylistic effect).


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

Deband Parameters

Deband controls include:

�Edge Threshold: Adjusts how well-defined an edge needs to be in order to be affected by this

filter; lowering this excludes fainter edges, while raising this includes them.

�Radius: Lowers or raises the intensity of dithering in areas that will be affected.

�Post Refine: Narrows (by lowering) or widens (by raising) the areas affected by dithering.

�Display Edge: A checkbox that shows you a black and white high-contrast preview of which edges

are being detected for dithering, which can help you fine-tune your results.

Deflicker (Studio Version Only)

The Deflicker plugin handles such diverse issues as flickering exposure in timelapse clips, flickering

fluorescent lighting, flickering in archival film sources, and in certain subtle cases even the “rolling

bars” found on video screens shot with cameras having mismatched shutter speeds. Two key aspects

to this filter are that it only targets rapid, temporally unstable variations in lightness, and that it’s able

to target only the areas of an image where flickering appears, leaving all other parts of the image

untouched. As a result, this plugin can often repair problems once considered “unfixable.”

Original image with flicker bars in the blue screen

Result setting Deflicker to Fluoro Light,

(clip courtesy Redline Films)

Main Parameters

By default, the top section of this plugin exposes a single control, which in many cases may be

all you need.

�Deflicker Settings pop-up menu: The top two options, Timelapse and Fluoro Light, are presets

that effectively eliminate two different categories of flickering artifacts. If neither of these presets is

quite as effective as you’d hoped, a third option, Advanced Controls, opens up the Isolate Flicker

controls at the heart of this plugin to let you tailor it further to your needs.

Temporal NR

Hidden by default, these controls only appear when you set Deflicker Setting to Advanced Controls,

and let you choose how to detect motion in the scene so that flickering may be correctly addressed

relative to the motion of subjects and items within the frame where it appears.

�Frames Either Side: Specifies the number of frames to analyze to determine what’s in motion.

Higher values are not always better; the best setting is, again, scene dependent. The default is 3.

�Mo.Est. Type: Picks the method DaVinci Resolve uses to analyze the image to detect motion.

Despite the names of the available options, which options will work best is highly scene


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

dependent. The default, Faster, is less processor intensive, but less accurate, however this can be

an advantage and actually do a better job with high detail images that would confuse the Better

option. Choosing Better is more accurate, but more processor intensive, and Better will try harder

to match fine details which can sometimes cause problems. None lets you disable motion analysis

altogether, which can work well (and will be considerably faster) in situations where there’s no

motion in the scene at all. The default is Better.

�Motion Range: Three settings, Small, Medium, and Large, let you choose the speed of the motion

in the frame that should be detected.

�Luma Threshold: Determines the threshold above which changes in luma will not be considered

flicker. The range is 0–100, 0 deflickers nothing, 100 applies deflickering to everything.

The default is 100.

�Chroma Threshold: Determines the threshold above which changes in chroma will not be

considered flicker. The range is 0–100, 0 deflickers nothing, 100 applies deflickering to

everything. The default is 100.

�Luma Chroma Same Threshold: Lets you choose whether to gang the Luma and Chroma

Threshold sliders or not.

�Motion Threshold: Defines the threshold above which motion will not be considered flicker.

Speed Optimization Options

Closed by default, opening this control group reveals two controls:

�Reduced-Detail Motion checkbox: On by default, reduces the amount of detail that’s analyzed

to detect flicker. In many cases, this setting makes no visible difference but increases processing

speed. Disable this setting if your clip has fine detail that is being smoothed too aggressively.

�Limit Analysis Area checkbox: Turning this on reveals controls over a sample box that you can

use to limit deflickering to a specific region of the image. This option is useful when:

a)	 Only one part of the image is flickering, so focusing on just that area speeds the operation

considerably, or

b)	 Part of the image is being smoothed too much by deflickering that’s fixing another part of the

image very well.

Restore Original Detail After Deflicker

Closed by default, opening this control group reveals two controls:

�Detail to Restore slider: Lets you quickly isolate grain, fine detail, and sharp edges that should not

be affected by the deflicker operation, preserving those fine details exactly.

�Show Detail Restored checkbox: Turning this checkbox on lets you see the edges that are

detected and used by the Detail to Restore slider, to help you tune this operation.

Output

The Output pop-up menu lets you choose what Deflicker outputs, with options to help you

troubleshoot problem clips. Here are the available options:

�Deflickered Result: The final, repaired result. This is the default setting.

�Detected Flicker: This option shows you a mask that highlights the parts of the image that are

being detected as having flickering, to help you evaluate whether the correct parts of the image

are being targeted. This mask can be very subtle, however.

�Magnified Flicker: This options shows you an exaggerated version of the Detected Flicker mask,

to make it easier to see what the Deflicker plugin is doing.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR