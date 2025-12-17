---
title: "Image Stabilization"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 56
---

# Image Stabilization

DaVinci Resolve provides Image Stabilization controls in the Cut, Edit, and Color pages that all

control the same transform operation that happens between Edit sizing and Input Sizing in the image

processing pipeline. The transform that’s made via the Image Stabilization controls refers all the way

back to either the source resolution of each clip, or the resolution output by the Fusion page if it’s in use.

Input Sizing on the Color Page

The Sizing palette on the Color page has another dedicated set of keyframable transform parameters

that work with the various DaVinci control panels to let the colorist apply pan and scan adjustments

while working through a project. These parameters work independently of the Edit page Transform

parameters, allowing you to keep imported transform settings separate from other transform settings

that you apply. However, for convenience the Edit sizing controls are available in the Color page as well.

The transform that’s made via the Input Sizing controls refers all the way back to either the source

resolution of each clip, or the resolution output by the Fusion page if it’s in use.

Node Sizing on the Color Page

Using Node Sizing, you can apply individual sizing adjustments to clips on a per-node basis within the

Color page, which is similar in principal to using Transform nodes in the Fusion page. All Node Sizing

adjustments within a grade are cumulative, and any keyframing done to Node Sizing parameters is

stored in that node’s Node Format keyframe track in the Keyframe Editor. Two good examples of Node

Sizing include realigning color channels individually in conjunction with the Splitter/Combiner nodes

or duplicating windowed regions of an image by moving them around the frame. Subsequent Node

Sizing operations do not refer back to the source resolution of a clip, so using multiple Node Sizing

operations to reduce and enlarge an image will reduce image resolution and sharpness.

Output Sizing on the Color Page

Output sizing is an additional transform that is applied after Edit sizing, Fusion sizing, Input sizing, and

Node sizing. It’s an overall adjustment that affects every clip at once, which is suitable for making last-

minute format alterations that you want to affect the entire program. Technically, Output Sizing includes

the Blanking controls, but those are important enough to discuss separately. Output Sizing also does

not refer back to the source resolution of clips, so if you use Edit or Input Sizing to shrink a clip, and

Output Sizing to enlarge it again, the final result will be somewhat softened as you’re enlarging the

lower resolution image output by Input Sizing.


Setup and Workflows | Chapter 11 Image Sizing and Resolution Independence

MEDIA

Output Blanking

Output blanking is not a sizing operation, but it’s often related and so worth mentioning here. Blanking

is an adjustment you can use to add black areas to the top, bottom, left, or right of an image, in order

to add “letterboxing” (black bars at the top and bottom of the image) or “pillarboxing” (black bars at the

left and right of the image) that lets you fill in the unused parts of an image frame that’s either shorter

or thinner than the current output resolution.

Once all transforms, compositing operations, and color corrections have been applied by the DaVinci

Resolve image processing pipeline, the very last operation to be performed is Output blanking, if

it’s enabled. This guarantees that overlapping images, grading, and other adjustments are properly

“blacked out” no matter what you’re doing to the program.

Output Blanking controls are found in the Timeline menu (as a series of aspect ratios) as well as in the

Output Sizing parameters of the Color page Sizing palette (via Top, Right, Bottom, and Left controls).

TIP: Text and graphics superimposed via the Data Burn-In window, if enabled, are the only

effects that will appear in front of picture areas affected by blanking. This lets you add timecode

and other information over letterboxed areas that you don’t want to obscure the picture.

Format Resolution on the Delivery Page

By default, the Format Resolution setting in the Render Settings of the Deliver page matches the

timeline resolution when “Match timeline settings” is enabled in the Output Scaling Preset in the Image

Scaling panel of the Project Settings.

Choosing a new resolution from the “Set Resolution to” drop-down menu lets you override the current

Format Resolution setting before rendering. Using this control, you can queue up multiple jobs, each

set to a different resolution, to output multiple formats during a single render session.

For more information on rendering and setting up jobs for the Render Queue,

see Chapter 186, “Using the Deliver Page.”


Setup and Workflows | Chapter 11 Image Sizing and Resolution Independence

MEDIA

Rendering Sizing Adjustments and Blanking

When rendering your final output, you have the option of choosing whether or not to “bake in” the

sizing operations that have been performed. For example, you may have set up a whole set of specific

sizing adjustments for the clips in a program, but then you’re requested to render the project and its

media as individual clips for round trip re-delivery to the editor for further work. In this case, you can

choose to either render the sizing into the final media, or not.

Whether or not sizing is rendered into your final media depends on the “Disable edit and input sizing”

checkbox in the Advanced Settings options of the Render Settings panel. You can disable sizing and

blanking either when rendering the current timeline as a single clip, or when rendering individual clips.

If “Disable sizing and blanking output” is turned off: Output Blanking, Cut and Edit page

sizing adjustments, Color page Input and Output Sizing adjustments, and Image Stabilization

are rendered into the final rendered media using the optical-quality sizing algorithms available

to DaVinci Resolve. This is best if your sizing adjustments are approved and final, and you

want to “bake” sizing adjustments into the final media you’re delivering.

If “Disable sizing and blanking output” is turned on: Output Blanking, Cut and Edit page

sizing adjustments, Color page Input and Output Sizing adjustments, and Image Stabilization

are not rendered, and each clip will be rendered either at the source resolution if “Render at

source resolution” is enabled in individual clips mode, or to the currently specified resolution

of the timeline or project. However, the sizing adjustments you’ve made will be exported as

part of the XML or AAF file that you’re exporting. This is best for workflows where the editor

wants to continue adjusting sizing after you’ve handed off the graded project relative to the

original size of the clips.

Keep in mind that if you want to render Input Sizing adjustments into the media you’re outputting, the

“Force sizing to highest quality” checkbox guarantees that DaVinci Resolve will use the highest-quality

sizing setting, even if you’ve temporarily chosen a faster-processing option for a slower computer.

NOTE: “Disable sizing and blanking output” does not disable any transform operations that

happen within the Fusion page. Those will continue to be applied to the final output.


Setup and Workflows | Chapter 11 Image Sizing and Resolution Independence

MEDIA

Chapter 12

Data Burn-In

This chapter covers how to use the Data Burn-In window that’s available to every

page in DaVinci Resolve.

Contents

Data Burn-In�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 298

Project vs. Clip Mode������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 299

Setting Up Burned-In Metadata��������������������������������������������������������������������������������������������������������������������������������������������������� 299

Saving and Loading Burn-In Presets������������������������������������������������������������������������������������������������������������������������������������������� 299

Data Burn-In Metadata���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 300

Custom Output Options��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 301

Gang Rendered Text Styles������������������������������������������������������������������������������������������������������������������������������������������������������������ 302

Prefix Render Text������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 302


Setup and Workflows | Chapter 12 Data Burn-In

MEDIA

Data Burn-In

The Data Burn-In window lets you display select metadata as a timeline-wide “window burn”

that’s superimposed over the image in the Viewer. This window burn is written into files that you

render in the Deliver page, and it’s also output to video, for viewing on your external display, or for

outputting to tape.

The Burn-In window is available by choosing Workspace > Data Burn-In.

Data Burn-In window

Traditionally, window burns are useful as a reference when creating offline media that you need to

keep track of later. However, the Data Burn window is extremely flexible. For example, it’s also useful

for watermarking review files that you don’t want to be distributed accidentally with either custom text

or graphics with alpha channels, for adding graphical logos or “bugs” to programs in preparation for

broadcast (again, optionally using graphics with alpha channels), for superimposing custom reference

guidelines of some sort over the images being monitored, or even just for temporarily displaying

timecode or clip names to refer to on your monitor while editing, mixing, or reviewing graded dailies

with a client.

Viewer displaying record timecode, source timecode, and source clip name


Setup and Workflows | Chapter 12 Data Burn-In

MEDIA