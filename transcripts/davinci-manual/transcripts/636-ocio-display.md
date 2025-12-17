---
title: "OCIO Display"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 636
---

# OCIO Display

This effect allows you to to view display transforms using an OCIO config file (.ocio).

�OCIO Config File: Click Browse to load a .ocio config file for the display transform.

�Source Space: Choose the color space of the source material from the list.

�Display: Choose which monitor and type your Viewer is on.

�View: Choose which color space to view on your monitor.

OCIO File Transform

This effect allows you to to load and apply Look Up Tables (LUTs) to the node.

�LUT File: Click Browse to load a LUT from the file browser.

�CCC ID: This is the ID key used to identify the specific file transform located within the ASC CDL

color correction XML file.

�Forward: Applies the LUT to the node.

�Reverse: Attempts to remove the LUT from the node.

�Interpolation: Allows the user to select the color interpolation to achieve the best quality/render

time ratio.


Resolve FX Overview | Chapter 161 Resolve FX OpenColorIO

COLOR

Chapter 162

Resolve FX Refine

These plugins let you make different kinds of targeted improvements.

Contents

Beauty (Studio Version Only)��������������������������������� 3525

Operating Mode���������������������������������������������������������� 3525

Automatic����������������������������������������������������������������������� 3526

Advanced����������������������������������������������������������������������� 3526

Ultra Beauty������������������������������������������������������������������� 3527

Custom Mixer��������������������������������������������������������������� 3528

Blend�������������������������������������������������������������������������������� 3529

Combine������������������������������������������������������������������������� 3529

Advanced Options����������������������������������������������������� 3530

Depth Map (Studio Version Only)������������������������� 3531

Main Controls���������������������������������������������������������������� 3532

Resulting Map Adjustment������������������������������������� 3532

Isolate Specific Depth����������������������������������������������� 3532

Map Finesse������������������������������������������������������������������ 3532

Advanced Options������������������������������������������������������ 3533

Face Refinement (Studio Version Only)���������� 3535

Main Controls��������������������������������������������������������������� 3536

Face Location���������������������������������������������������������������� 3537

Skin Isolation����������������������������������������������������������������� 3537

Skin Texture������������������������������������������������������������������ 3538

Smoothing Controls�������������������������������������������������� 3538

Color Grading�������������������������������������������������������������� 3539

Side Lighting���������������������������������������������������������������� 3539

Eye Shadow������������������������������������������������������������������ 3539

Eye������������������������������������������������������������������������������������� 3540

Lips������������������������������������������������������������������������������������ 3540

Teeth���������������������������������������������������������������������������������� 3541

Blush����������������������������������������������������������������������������������� 3541

About Forehead, Cheeks,

and Chin Retouching�������������������������������������������������� 3541

Forehead������������������������������������������������������������������������� 3542

Cheeks����������������������������������������������������������������������������� 3542

Chin������������������������������������������������������������������������������������ 3542

Relight (Studio Version Only)��������������������������������� 3542

Setting up Relight������������������������������������������������������� 3542

Using Relight���������������������������������������������������������������� 3544

The Relight Settings������������������������������������������������� 3544

The Relight On-Screen Controls������������������������� 3547


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

Beauty (Studio Version Only)

Beauty is a plugin that lets you control texture. In Ultra Beauty mode, you can selectively smooth

image detail that falls above a particular threshold, while preserving detail falling below a particular

threshold. In this way, you can smooth larger textures you don’t want, while either preserving or

exaggerating smaller textures that you do want.

In the case of faces and skin, this plugin provides another method of smoothing larger, unwanted

blemishes, while preserving desirable edge detail and underlying structures such as pores, so you can

improve the complexion of subjects on shoots where hair and makeup was not available, without over-

softening realistic skin details and creating an overly fake plastic look.

(Left) The original image, (Right) A face with Beauty applied to soften the complexion while retaining fine facial detail

Please note that this plugin is not only for skin detail, and it’s not only for softening. Once you isolate

the fine detail you want to preserve in a subject, you also have the option of exaggerating it to create

highly textured results. This plugin is effective for any subject with textures that need refinement.

TIP: This plugin is best used within a qualification that isolates the particular feature you’re

trying to smooth. The default settings apply a moderate amount of smoothing and fine detail

recovery that’s appropriate for faces in closeup but will not be universally appropriate for all

situations, so some fine-tuning will always be necessary. For naturalistic results, this plugin

produces the best results when used in moderation.

Operating Mode

The Beauty plugin has three operational modes, including an Automatic mode with simpler operation

when your objective is to create a maximally smooth or textured result while still preserving important

details, an Advanced mode if you want more nuanced control, and an Ultra Beauty mode that provides

additional controls that let you preserve fine detail that you want, while smoothing coarse details that

you don’t want.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

Automatic

Automatic mode reveals easy-to-use controls for smoothing or coarsening detail.

�Amount: Lets you choose how much smoothing or coarsening to apply.

�Scale: Lets you reduce or increase the amount of smoothing or coarsening that’s accomplished

with the range of the Amount slider.

Advanced

Advanced mode reveals more manual controls for smoothing or coarsening detail, without the

complexity of the Ultra Beauty mode.

�Show Split View: Checking this box puts a four up display in the Viewer showing the output of the

Smoothing, Texture Recovery, Feature Recovery, and Final Output respectively. This is useful to

have up when dialing in the advanced options below.

The Split View of the Advanced Beauty mode showing Smoothing (top left), Texture Recovery

(top right), Feature Recovery (bottom left), and Final Output (bottom right) views.

Smoothing

These parameters let you remove imperfections. There are two smoothing controls to adjust. Apply

these controls with enough strength to get rid of all the details to be smoothed away. The damage

from over-smoothing will be reversed in Texture and Feature Recovery.

�Smoothing Threshold: Adjust this slider to set the amount of detail in the image to keep.

�Diffuse Lighting: Adjusts the amount of detail in the mid-tones.

�Preview Smoothed: Shows the result of just the smoothing operation in the Viewer.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

Texture Recovery

These parameters let you restore areas of fine texture from the original video in flat areas

away from the edges.

�Texture Threshold: Adjust this slider to set the amount of fine texture in the image to keep.

�Add Texture: Increases or decreases the scale of the texture in the Texture Threshold. Positive

numbers add texture, while negative numbers remove it.

�Preview Texture: Shows the result of just the Texture Recovery operation in the Viewer.

Feature Recovery

These parameters let you determine how much of the recoverable Smoothing and Textures to bring

back into the image.

�Recovery Amount: Adjust this slider to set the amount detail you’ve isolated (shown in white on

the Feature Recovery view) to bring back into the image.

�Preview Recovery Areas: Shows the result of just the Feature Recovery operation in the Viewer.

Ultra Beauty

The Ultra Beauty controls reveal the full power of the Beauty plugin, with preview modes to examine

different aspects of this plugin’s behavior, while specifically adjusting the level of smoothing or

coarsening you want, the amount of texture to preserve, and which additional features of the subject

you want to recover from this operation to fine tune the result.

Smoothing

These parameters let you remove imperfections. There are two smoothing methods to chose from.

Apply these controls with enough strength to get rid of all the details to be smoothed away. The

damage from over-smoothing will be reversed in Detail Recovery. To see the effects of the smoothing

alone, reduce the Detail Recovery strength, and texture to zero.

�Flatten: Reduces texture and filters out detail.

Strength: How much smoothing effect is applied to the image.

Levels: Controls how strongly abstracted the image is to smooth levels.

Quality: Controls the sharpness of the resulting effect. Full being the sharpest and Fastest being

the blurriest.

�Filter: Flattens smooth areas the image, leaving edges only where they divide flat regions from

each other.

Strength: How much smoothing effect is applied to the image.

Filter Radius: Controls what scale of details are being filtered.

Edge Threshold: Controls at what level an edge will be preserved or smoothed over. A low

threshold will preserve even weak edges, while a high threshold will smooth over an increasing

number of edges unless they are very high contrast.

Detail Recovery

These parameters let you restore the areas of the original video around the image edges,

adding detail back into the image.

�Strength: Determines the amount of recovered detail.

�Width: Controls how far to either side of the edges image detail is recovered.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

�Gamma: Controls whether to recover all edges, or only the stronger ones. A higher gamma

reduces the amount of edges recovered.

�Blur: Softens the map of edges where detail is to be recovered.

�Preview Edges/Details: Enable this checkbox to show the areas where image detail is to

be recovered; this allows you to see directly how the other controls in this section will affect

the image.

�Preview Recovery: Enable this checkbox to show the actual detail being recovered alone over a

neutral gray background.

Texture Recovery

These parameters let you restore areas of fine texture from the original video in flat areas

away from the edges.

�Texture: Determines the amount of recovered texture to restore.

�Scale: Lets you set a threshold below which texture is extracted from the original image and

applied to the result.

�Detail/Edge Balance: Lets you bias the recovery towards all textures (a negative value), or only to

stronger details like edges (a positive value).

�Preview Texture: Enable this checkbox to show the actual texture being recovered alone over a

neutral gray background.

Grain

These parameters let you add grain to the image to simulate detail in areas of the video

with bad or no texture. Grain will only appear in smooth areas and will not cover the recovered edges.

�Strength: Controls the amount of grain added to the image.

�Size: Controls the size of the individual grains.

�Softness: Softens the grain texture.

�Saturation: Applies saturation to the grain.