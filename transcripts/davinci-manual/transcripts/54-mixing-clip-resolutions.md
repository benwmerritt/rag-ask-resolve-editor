---
title: "Mixing Clip Resolutions"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 54
---

# Mixing Clip Resolutions

Media used in a project does not have to match the timeline resolution. In fact, it’s extremely common

to mix multiple resolutions within the same timeline. Clips that don’t match the current resolution will be

automatically resized according to the currently selected Image Scaling setting (described below).

Changing the Timeline Resolution

As mentioned earlier, you can change the timeline resolution whenever you like. When you do so,

each Edit page transform, Fusion clip effects output, Color page Power Window, Input and Output

Sizing adjustment, tracking path, spatial keyframing value, as well as any other other resolution-

dependent Resolve FX effect or transform operation in DaVinci Resolve is automatically and

accurately scaled to fit the new resolution.

You Can Use Separate Timelines

to Output Different Resolutions

Beginning in DaVinci Resolve 16, you have the option of creating separate timelines with individual

Format (including Input Scaling), Monitoring, and Output Sizing settings for situations where

you need to set up multiple timelines to create multiple deliverables with different resolutions,

pixel aspect ratios, frame rates, monitoring options, or output scaling options than the overall project,

including “Mismatched Resolution Files” settings.

For more information, see Chapter 34, “Creating and Working with Timelines.”

You Don’t Need Separate Timelines

to Output Different Resolutions

Because of the way DaVinci Resolve works, it’s not necessary to create separate timelines when all

you need is to output the same timeline at multiple resolutions. Instead, you can focus on mastering a

single timeline, which you can output to as many other resolutions as you need.

For example, with only a single timeline in a project set to 4096x2160 (4K DCI) resolution, you can

easily output UHD, HD, center-cut SD, and center-cut Instagram sized deliverables in any format you

need by simply changing the Resolution drop-down setting in the Deliver page Render Settings before

you create a job to render. DaVinci Resolve takes care of the rest.

The Deliver page drop-down menu in the Render Settings panel lets you

choose what resolution you want to output the current timeline using


Setup and Workflows | Chapter 11 Image Sizing and Resolution Independence

MEDIA

Using High Resolution Media in Lower Resolution Projects

Every set of transform and sizing parameters and settings that resize clips is combined intelligently,

so that the full resolution of a clip’s source media is always used as the source for any transform. For

example, if you’re using 8K media within a 1920x1080 project, and you need to enlarge a clip using the

Input Sizing palette’s Zoom parameter to 200%, the image is scaled relative to the native 8K resolution

of the source, and the result is fit into the current timeline resolution. This automatically guarantees

the highest quality for any image transform you make so long as you don’t zoom in past the native

resolution of any given clip.

This also applies to situations where, for example, you shrink a clip in the Edit page using the Edit

Sizing controls, only to re-enlarge the same clip in the Color page, using the Input Sizing controls.

In this situation, DaVinci Resolve is smart enough to do the math combining the project resolution,

the Edit Sizing, and the Input Sizing controls so that a single transform is applied to the native source

resolution of that clip, giving you the best quality result.

NOTE: This changes when you apply Fusion effects to any clip,

as described later in this chapter.

Clip Source Resolution

Clip resolution in DaVinci Resolve is handled by the combination of Pixel Aspect Ratio and Resolution.

Pixel Aspect Ratio (PAR)

The Timeline Format settings, found in the Master Settings of the Project Settings, let you specify a

Pixel Aspect Ratio for the project, in addition to the frame size. This setting defaults to Square Pixel,

which is appropriate for high definition projects and most digital media. However, there are also

options for 16:9 anamorphic, 4:3 standard definition, or Cinemascope. Which options are available

depends on what timeline resolution you’ve selected.

In addition, each clip has individually adjustable PAR settings in the clip attributes, for

situations where you’re mixing multiple types of media within a single project. For example, if

you’re mixing SD clips with non-square pixels and HD clips with square pixels, you can sort out

all of the SD clips in the Media Pool and assign them the appropriate NTSC or PAL non-square

pixel ratio PAR setting.

For more information, see Chapter 22, “Modifying Clips and Clip Attributes.”

Clip Resolution

Ordinarily, the resolution of a clip is entirely dependent on the resolution that was selected when that

media was shot, or rendered out of a compositing, VFX, or 3D application. Once a piece of media has

been created, the native resolution of that media cannot be changed, and to maintain the ideal amount

of sharpness for that clip, you need to make sure that whatever transforms you apply to resize a clip

zoom into that clip no more than 10-20% over its native resolution (if even that), otherwise the image

will visibly soften.


Setup and Workflows | Chapter 11 Image Sizing and Resolution Independence

MEDIA

However, DaVinci Resolve provides advanced Super Scale image processing in the Clip Attributes of

every video and image clip, that make it possible to resize clips beyond their native resolution while

maintaining the perceptible sharpness of a clip that’s still within it’s native resolution. This is an illusion,

but it’s a convincing one.

The DaVinci Resolve Sizing Pipeline

This section discusses the various sizing controls that are available in DaVinci Resolve, and how they

work together.

“Super Scale” High Quality Upscaling (Studio Version Only)

For instances when you need higher-quality upscaling than the standard Resize Filters allow, you

can now enable one of the “Super Scale” options in the Inspector or in the Video panel of the Clip

Attributes window for one or more selected clips. Unlike using one of the numerous scaling options in

the Edit, Fusion, or Color pages, Super Scale actually increases the source resolution of the clip being

processed, which means that clip will have more pixels than it did before and will be more processor-

intensive to work with than before, unless you optimize the clip (which bakes in the Super Scale effect

into the optimized media) or cache the clip in some way.

Super Scale options in the Video panel of the Clip Attributes

The Super Scale dropdown menu provides the options of 2-3-4x, and 2-3-4x Enhanced, as well as

Sharpness and Noise Reduction options to tune the quality of the scaled result. Most of the Super

Scale parameters are in fixed Low, Medium, or High increments, however the Enhanced modes let

you apply them in variable amounts. Selecting one of these options enables DaVinci Resolve to use

advanced algorithms to improve the appearance of image detail when enlarging clips by a significant

amount, such as when editing SD archival media into a UHD timeline, or when you find it necessary to

enlarge a clip past its native resolution in order to create a closeup.

You may find that, depending on the source media you’re working with, setting Sharpness to Medium

yields a relatively subtle result that can be hard to notice, but setting Sharpness to high should be

immediately more preferable, while also sharpening grain and noise in the image to an undesirable

extent at the default settings. However, while raising Noise Reduction will ameliorate this effect, it will

also diminish the gains you obtained by raising Sharpness. In these cases, it’s worth experimenting

with keeping Sharpness at Low or Medium so that Super Scale sharpens all aspects of a clip, but then

using the Noise Reduction tools of the Color page (with their additional ability to be fine-tuned) to

diminish the unwanted noise.

TIP: Super Scale, while incredibly useful, is a processor-intensive operation, so be aware that

turning this on will likely prevent real-time playback. One way to get around this is to create

Optimized Media for clips in which you’ve enabled Super Scale, since Optimized Media

“bakes in” the Super Scale effect. Another way to work is to create a string-out of all of the

source media you’ll need to enlarge at high-quality, turn on Super Scale for all of them, and

then render that timeline as individual clips, while turning on the “Render at source resolution”

and “Filename uses > Source Name” options.


Setup and Workflows | Chapter 11 Image Sizing and Resolution Independence

MEDIA

Fusion Effects and Resolution

All image processing by the Fusion page takes place before effects that are applied by the Edit page,

with the sole exception of the Lens Correction effect. When it comes to sizing and image resolution,

whether or not the Fusion page affects resolution depends on how you use it.

Fusion Effects Inherit the Source Resolution of a Clip

When you open a clip on the Timeline in the Fusion page, the Fusion page is set to the full source

resolution of that clip, regardless of the Timeline resolution. This can be seen if you look at the

resolution that’s listed above the upper right-hand corner of the Viewer. This means that if you

don’t apply any operations that reduces the image resolution (described later), subsequent sizing

adjustments in other pages will refer to the same resolution as the source clip.

The available resolution and bit depth of the currently selected clip is visible

above the upper right-hand corner of the Viewer, circled in red

Fusion Clips Inherit the Timeline Resolution

If you combine multiple clips on the Timeline into a Fusion clip, the Fusion page is set to the timeline

resolution, regardless of the source resolution of the clip. The image is then output to the Edit page at

this timeline resolution, and all subsequent sizing adjustments are performed relative to the timeline

resolution, with no reference to the original resolution in the source clip.


Setup and Workflows | Chapter 11 Image Sizing and Resolution Independence

MEDIA

The available resolution and bit depth of a clip that’s been turned into a

Fusion Clip, that’s set to the timeline resolution of 1920x1080

Operations in the Fusion Page That Change Resolution

If you don’t do anything to change the size of a clip in the Fusion page, then its resolution stays the

same and you’ll effectively output the source resolution of that clip to the Edit page.

However, if you Merge the image with a second clip attached to the background which has a different

resolution, or if you use a Crop or Resize node to increase or decrease the resolution of the image,

then the new resolution will be passed to the Cut and Edit pages as the effective source resolution of

that clip.

In short, the Fusion page passes whatever resolution is output by the last node of your composition

back to the Edit page as the effective resolution of that clip in the DaVinci Resolve image

processing pipeline.

Fusion Page Transform Operations Are Resolution Independent

Within the Fusion page, multiple Transform nodes operate in a resolution independent manner relative

to the resolution of the source clip. This means that if you shrink an image to 20% with one Transform

node, and then enlarge it back up to 100% using a second Transform node, you end up with an image

that has all the resolution and sharpness of the input image.

Fusion Page Resize Operations Are Not

Within Fusion there are two kinds of transform effects, the Transform node and the Resize node. Which

of these nodes you use has a dramatic impact on resolution independence.


Setup and Workflows | Chapter 11 Image Sizing and Resolution Independence

MEDIA

•	 The Transform node always refers back to the input resolution of the clip (as defined by the

Clip Attributes) to enable resolution-independent sizing, such that multiple Transform nodes

can scale the image down and up repeatedly within the Fusion page with no unnecessary

loss of image resolution.

•	 The Resize node actually decreases image resolution when you shrink an image or

increases image resolution (with filtering) when enlarging. This means that the Resize node

will break resolution independence, and the resolution of the image will be fixed at whatever

you specify from that point in your composite’s node tree forward.

In most situations, you probably want to use the Transform node to maintain resolution independence

relative to the source media, unless you specifically want to alter and perhaps reduce image resolution

to create a specific special effect which purposefully degrades the image. For example, if you want

a clip to be forced to a standard definition resolution in order to make it look like a low-resolution

archival clip, the Resize node will accomplish this. Enlarging the result with a Transform node will then

perform a filtered enlargement that will look like a real SD clip being enlarged.

Transforms from the Fusion Page to the Edit Page

All transform operations you apply on the Cut, Edit, and Color pages are resolution independent,

referring to the original resolution of the source media, so long as you don’t use the Fusion page.

For example, if you shrink an image to 20% in the Edit page (using Edit sizing controls) and then

enlarge it in the Color page back to 100% (using Input sizing controls), you end up with an image that

has all the resolution and sharpness of the original media, because the final resolution is drawn from

the original source media.

However, once you use the Fusion page to do anything to a clip, from adding a small effect to creating

a complex composition, the resolution-independent relationship of the Edit and Color pages to the

source media is broken, and whatever resolution is output from your Fusion composition is the new

effective resolution of the clip that appears in the Timeline. This means if you shrink an image to

20% in the Fusion page (using a Transform node) and then enlarge it in the Color page by 150%, you

end up with an image that isn’t as sharp as the original because the downconverted image in the

Fusion page is effectively the new source resolution of that clip.