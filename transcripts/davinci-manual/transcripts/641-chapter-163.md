---
title: "Chapter 163"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 641
---

# Chapter 163

Resolve FX Revival

This category consists of plugins that let you fix common technical, damage, and

quality problems that bedevil programs being finished, remastered, or restored.

Contents

Automatic Dirt Removal

(Studio Version Only)�������������������������������������������������� 3551

Main Controls��������������������������������������������������������������� 3552

Fine Controls���������������������������������������������������������������� 3552

Chromatic Aberration Removal

(Studio Version Only)������������������������������������������������ 3552

Advanced Options������������������������������������������������������ 3553

Estimation Options����������������������������������������������������� 3553

Aberration Correction����������������������������������������������� 3553

Dead Pixel Fixer (Studio Version Only)������������� 3554

General��������������������������������������������������������������������������� 3555

Patch Type��������������������������������������������������������������������� 3556

Patch Options�������������������������������������������������������������� 3556

Advanced Controls���������������������������������������������������� 3557

Deband (Studio Version Only)������������������������������� 3557

Deband Parameters�������������������������������������������������� 3558

Deflicker (Studio Version Only)���������������������������� 3558

Main Parameters�������������������������������������������������������� 3558

Temporal NR����������������������������������������������������������������� 3558

Speed Optimization Options�������������������������������� 3559

Restore Original Detail After Deflicker������������ 3559

Output������������������������������������������������������������������������������ 3559

Dust Buster (Studio Version Only)��������������������� 3560

General����������������������������������������������������������������������������� 3561

Patch Type����������������������������������������������������������������������� 3561

Patch Options�������������������������������������������������������������� 3562

Advanced Controls��������������������������������������������������� 3562

Frame Replacer (Studio Version Only)������������� 3563

Noise Reduction (Studio Version Only)����������� 3563

Temporal NR Controls��������������������������������������������� 3563

Temporal Threshold Controls������������������������������ 3564

Spatial NR Controls��������������������������������������������������� 3564

Spatial Threshold Controls������������������������������������ 3565

Global Blend����������������������������������������������������������������� 3565

Using Noise Reduction������������������������������������������� 3565

Object Removal (Studio Version Only)������������� 3567

General���������������������������������������������������������������������������� 3567

Analysis���������������������������������������������������������������������������� 3567

Render����������������������������������������������������������������������������� 3568

Clean Plate�������������������������������������������������������������������� 3568

Patch Replacer (Studio Version Only)��������������� 3570

Main Controls����������������������������������������������������������������� 3571

Patch Positions�������������������������������������������������������������� 3571

Onscreen Controls������������������������������������������������������ 3571


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

Automatic Dirt Removal

(Studio Version Only)

The Automatic Dirt Removal plugin uses optical flow technology to target and repair temporally

unstable bits of dust, dirt, hair, tape hits, and other unwanted artifacts that last for one or two

frames and then disappear. All repairs are made while maintaining structurally consistent detail

in the underlying frame, resulting in a high quality restoration of the image. Fortunately, despite

its sophistication, this is a relatively easy plugin to use; just drop the plugin on a shot, adjust the

parameters for the best results, and watch it go.

(Top) Original image, (Bottom) Using Automatic Dirt Removal

NOTE: This plugin is less successful with vertical scratches that remain in the same

position for multiple frames and is completely ineffective for dirt on the lens that remains for

the entire shot.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

Main Controls

The primary controls used to adjust how much dirt is removed from the image.

�Motion Estimation Type: Lets you choose from among None, Faster, Normal, and Better. This

tunes the tradeoff between performance and quality.

�Neighbor Frames: Lets you choose how many frames to compare when detecting dirt.

Choosing more frames of comparison takes longer to process, but usually results in finding more

dirt and artifacts.

�Repair Strength: This slider lets you choose how aggressively to repair dirt and artifacts that are

found. Lower settings may let small bits through that may or may not be actual dirt, while higher

settings eliminate everything that’s found.

�Dirt Size Threshold: This slider lets you tune how large a detected bit of dirt must be to be

removed. Raising this parameter lets you omit things like film grain from the operation but may

allow smaller bits of dirt through.

�Show Repair Mask: This checkbox lets you see the dirt and artifacts that are detected by

themselves, so you can see the effectiveness of the results as you fine tune this filter.

Fine Controls

These controls let you fine tune the effect in an effort to perfect the tradeoff between removing dirt

successfully and preserving true image detail.

�Motion Threshold: This slider lets you choose the threshold at which pixels in motion are

considered to be dirt and artifacts. At lower values more dirt may escape correction, but you’ll

experience fewer motion artifacts. At higher values, more dirt will be eliminated, but you may

experience more motion artifacts in footage with camera or subject motion.

�Edge Ignore: This slider lets you exclude hard edges in the picture from being affected by dirt or

artifacts that are removed. Higher values omit more edges from being affected.

Chromatic Aberration Removal

(Studio Version Only)

A Revival category plugin that lets you manually correct the slight color fringing that results from

chromatic aberration in a lens. Show Estimated Fringes checkboxes for the RGB channels display an

“alignment guide” that visually isolates each of the types of fringing against gray.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

(Previous page) The original image in close up, showing chromatic aberration,

(Above) The image with Estimated Red Fringes enabled, letting you see the

specific problems as differences between red and cyan stripes

Advanced Options

Advanced Options provide additional parameters for problem shots.

�Lens Center: Center X and Y parameters let you offset the center of the lens if you’re dealing

with a reframed and re-rendered shot. You can also drag the lens center on-screen control in the

Viewer to reposition.

�Stronger Correction: Shows the location of image features that resemble fringing.

Estimation Options

The Estimation options are used solely to highlight and identify areas of fringing. They do not affect

the final output of the image. They only become available when one of the Show Estimated Fringes

boxes is checked in the Aberration Correction section.

�R/C, G/P, B/Y Balance: These tools adjust the incoming balance between their respective colors

to better identify hard to see fringing.

�Brightness: Magnifies the fringe indicators that are displayed when you turn on either of the

Estimated Fringes checkboxes.

Aberration Correction

These tools let you make manual adjustments to correct aberration issues.

�R/C, G/P, B/Y Scale: Adjust these sliders to eliminate the fringing from their respective colors.

�R/C, G/P, B/Y Edge: Adjust to compensate for the difference in fringing due to the curvature of the

lens’ edges.

�Show Estimated Fringes: Checking this box will show just the estimated fringes over a gray

background. It will also activate the Estimation Options sliders, which will let you further highlight

and identify areas of fringing.

This makes it easy to make manual adjustments to correct the problem, using the Scale and Edge

controls to individually adjust Red/Cyan, Green/Purple, and Blue/Yellow fringing.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

(Top) The original image in close up, showing chromatic aberration as a cyan

fringe along the right of the smokestack and as a red fringe along the closest corner

of the building, (Bottom) The corrected image in close up; this fringe is gone.

Dead Pixel Fixer (Studio Version Only)

If you have clips that were shot on a camera with one or more “dead” or “stuck” pixels in the sensor,

you may have black or white spots that are fixed in place in the image. This filter is designed to let you

place patches on each dead or stuck pixel, identifying them so you can use different methods of fixing

the problem.

In many respects, the Dead Pixel Fixer is similar to the Dust Buster, however the Dust Buster effect is

designed to repair transient bits of dust and dirt that only last for a frame or two, whereas the Dead

Pixel Fixer is designed to work on blemishes that are fixed in place for the duration of a clip.

To fix dead or stuck pixels, apply the Dead Pixel Fixer filter, make sure the OFX onscreen controls are

enabled in the viewer, and then click on each pixel you need to fix with the mouse to place a patch

on it. You can click anywhere on the image to place as many patches as you like, there’s no limit. You

can also Option-click to delete patches you no longer need. To move any patches, simply drag it to

another location.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

Multiple dead pixel removal patches

When you place multiple patches, you can click to select whichever patches you want to adjust the

controls for. Each patch can have different control settings.