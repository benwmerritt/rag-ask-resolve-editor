---
title: "Chapter 109"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 438
---

# Chapter 109

Matte Nodes

This chapter details the Matte nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Alpha Divide [ADv]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2428

Alpha Multiply [AMl]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2429

Chroma Keyer [CKy]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2430

Clean Plate�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2435

Cryptomatte [Cry] (Studio Version Only) �������������������������������������������������������������������������������������������������������������������������������� 2438

Delta Keyer������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2440

Depth Map [DMp]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2449

Difference Keyer [DfK]��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2452

Luma Keyer [LKy]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2455

Magic Mask [MagM]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2459

Matte Control [Mat]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2464

Primatte [Pri]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2469

Relight [RLt]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2484

Ultra Keyer [UKy]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2488

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2495


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Alpha Divide [ADv]

The Alpha Divide node

Alpha Divide Node Introduction

As the name gives away, the Alpha Divide’s sole purpose is to divide an incoming image’s color

channels by its alpha channel. When you color correct an image that contains a premultiplied

alpha channel, first apply an Alpha Divide node before any color correction node to create a non-

premultiplied image. Then you can perform the color correction. After the color correction, add an

Alpha Multiply node to return the image to its premultiplied state.

Inputs

The Alpha Divide node includes two inputs in the Node Editor.

Input: The orange input accepts a 2D image with a premultiplied Alpha.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input limits the pixels where the

Alpha divide occurs. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Alpha Divide node is placed before any color correction is done to an image with a premultiplied

Alpha channel. Here the MediaIn node is assumed to have a premultiplied Alpha channel. The Alpha

Divide node is inserted, and then color correction nodes operate on the “straight” Alpha. An Alpha

Multiply node is placed at the end of the chain to premultiply the Alpha channel again. If only a single

color correction node is used, then the Pre-Divide/Post-Multiply checkbox on the Options tab can be

used in place of the Alpha Divide/Alpha Multiple nodes.

An Alpha Divide node is inserted before color correcting an image with premultiplied alpha.

Inspector

This node has no controls.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Alpha Multiply [AMl]

The Alpha Multiply node

Alpha Multiply Node Introduction

As the name gives away, the Alpha Multiply’s sole purpose is to multiply an image’s color channels by

its alpha channel. When you color correct an image that contains a premultiplied alpha channel, first

apply an Alpha Divide node before any color correction node to create a non-premultiplied image.

Then you can perform the color correction. After the color correction, add an Alpha Multiply node to

return the image to its premultiplied state.

Inputs

The Alpha Multiply node includes two inputs in the Node Editor.

Input: The orange input accepts a 2D image with a “straight” or non-premultiplied alpha.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input limits the pixels where the

Alpha multiply occurs. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Alpha Multiply node is placed after color correction is done to an image with a premultiplied Alpha

channel. Here the MediaIn node is assumed to have a premultiplied Alpha channel. The Alpha Divide

node is inserted, and then color correction nodes operate on the “straight” Alpha. An Alpha Multiply

node is placed at the end of the chain to premultiply the Alpha channel again. If only a single color

correction node is used, then the Pre-Divide/Post-Multiply checkbox on the Options tab can be used

in place of the Alpha Divide/Alpha Multiple nodes.

An Alpha Multiply node is inserted after color correcting an image with premultiplied alpha.

Inspector

This node has no controls.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Chroma Keyer [CKy]

The Chroma Keyer node

Chroma Keyer Node Introduction

The Chroma Keyer node creates an alpha channel (matte) for an image by removing selected colors

from the scene. Unlike the Delta Keyer or Primatte, which use specific optimizations for keying from

blue and green colors, the Chroma Keyer works equally well with any color.

NOTE: When working with blue- or green-screen shots, it is best to use the Delta Keyer or

Primatte node, rather than the more general purpose Chroma Keyer node.

Inputs

The Chroma Keyer node includes four inputs in the Node Editor.

Input: The orange input accepts a 2D image that contains the color you want to be keyed for transparency.

Garbage Matte: The gray garbage matte input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps masks. Connecting a mask to this input causes areas of the

image that fall within the matte to be made transparent. The garbage matte is applied directly to the

alpha channel of the image.

Solid Matte: The white solid matte input accepts a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input causes areas of the image

that fall within the matte to be fully opaque.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input limits the pixels where the

alpha multiply occurs. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Chroma Keyer node takes in a 2D image like the MediaIn node below and removes a color that

you identify by dragging over it in the viewer. The result is that the selected color is replaced with

transparency, allowing you to composite the image as the foreground in a Merge node.

A Chomra Keyer node creating transparency on the MediaIn node.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Inspector

The Chroma Key tab

Chroma Key Tab

The Chroma Key tab is used to make the initial selection of color for keying.

Key Type

The Key Type menu determines the selection method used for the matte creation.

�Chroma: The Chroma method creates a matte based on the RGB values of the

selected color range.

�Color: The Color method creates a matte based on the hue of the selected color range.

Color Range

Colors are made transparent by selecting the Chroma Keyer node in the node tree, and then dragging

a selection around the colors in the viewer. The range controls update automatically to represent the

current color selection. You can tweak the range sliders slightly, although most often selecting colors

in the displays is all that is required.

Lock Color Picking

When this checkbox is activated, selecting colors from the viewer is disabled to prevent accidental

addition to the range. It is a good idea to activate this checkbox once you make the color selection for

the matte. All other controls in the node remain editable.

Soft Range

This control softens the selected color range, adding additional colors into the matte.

Reset Color Ranges

Clicking this button resets the Chroma Keyer’s range controls, discarding all color selections. All other

sliders and controls maintain their values.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

The Chroma Key Image tab

Image Tab

The Image tab primarily handles removing spill color on the foreground subject. Color spill occurs

when light containing the color you are removing is reflected onto the foreground subject.

Spill Color

This menu selects the color used as the base for all spill suppression techniques.

Spill Suppression

This slider sets the amount of spill suppression applied to the foreground subject.

When this slider is set to 0, no spill suppression is applied.

Spill Method

This menu selects the strength of the algorithm used to apply spill suppression to the image.

�None: None is selected when no spill suppression is required.

�Rare: This removes very little of the spill color and is the lightest of all methods.

�Medium: This works best for green screens.

�Well Done: This works best for blue screens.

�Burnt: This works best for blue. Use this mode only for very troublesome shots. Most likely you will

have to add strong color correction after the key to get, for example, your skin tones back.

Fringe Gamma

This control is used to adjust the brightness of the fringe or halo that surrounds the keyed image.

Fringe Size

This expands and contracts the size of the fringe or halo surrounding the keyed image.

Fringe Shape

Fringe Shape forces the fringe toward the external edge of the image or toward the inner edge of the

fringe. Its effect is most noticeable while the Fringe Size slider’s value is large.

Cyan/Red, Magenta/Green, and Yellow/Blue

Use these three controls to color correct the fringe of the image. This is useful for correcting

semitransparent pixels that still contain color from the original background to match the

new background.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

The Chroma Key Matte tab

Matte Tab

The Matte tab refines the softness, density, and overall fit of the resulting matte.

Filter

This control selects the filtering algorithm used when applying blur to the matte.

�Box: This is the fastest method but at reduced quality. Box is best suited for minimal

amounts of blur.

�Bartlett: Otherwise known as a Pyramid filter, Bartlett makes a good compromise between speed

and quality.

�Multi-box: When selecting this filter, the Num Passes slider appears and lets you control the

quality. At 1 and 2 passes, results are identical to Box and Bartlett, respectively. At 4 passes and

above, results are usually as good as Gaussian, in less time and with no edge “ringing.”

�Gaussian: The Gaussian filter uses a true Gaussian approximation and gives excellent results, but

it is a little slower than the other filters. In some cases, it can produce an extremely slight edge

“ringing” on floating-point pixels.

Blur

Matte Blur blurs the edge of the matte based on the Filter menu setting. A value of zero results in a

sharp, cutout-like hard edge. The higher the value, the more blur applied to the matte.

Clipping Mode

This option determines how edges are handled when performing domain of definition rendering.

This is profoundly important when blurring the matte, which may require samples from portions of the

image outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition. If the

upstream DoD is smaller than the frame, the remaining area in the frame will be treated as

black/transparent.

�Domain: Setting this option to Domain will respect the upstream domain of definition when

applying the node’s effect. This can have adverse clipping effects in situations where the node

employs a large filter.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

�None: Setting this option to None will not perform any source image clipping at all. This means

that any data required to process the node’s effect that would normally be outside the upstream

DoD will be treated as black/transparent.

Contract/Expand

This slider shrinks or grows the semitransparent areas of the matte. Values above 0.0 expand the

matte, while values below 0.0 contract it.

This control is usually used in conjunction with the Matte Blur to take the hard edge of a matte and

reduce fringing. Since this control affects only semitransparent areas, it will have no effect on a matte’s

hard edge.

Gamma

Matte Gamma raises or lowers the values of the matte in the semitransparent areas. Higher values

cause the gray areas to become more opaque, and lower values cause the gray areas to become

more transparent. Completely black or white regions of the matte remain unaffected.

Since this control affects only semitransparent areas, it will have no effect on a matte’s hard edge.

Threshold

This range slider sets the lower threshold using the handle on the left and sets the upper threshold

using the handle on the right.

Any value below the lower threshold setting becomes black or transparent in the matte.

Any value above the upper threshold setting becomes white or opaque in the matte. All values within

the range maintain their relative transparency values.

This control is often used to reject salt and pepper noise in the matte.

Restore Fringe

This restores the edge of the matte around the keyed subject. Often when keying, the edge of the

subject where you have hair is clipped out. Restore Fringe brings back that edge while keeping the

matte solid.

Invert Matte

When this checkbox is selected, the alpha channel created by the keyer is inverted, causing all

transparent areas to be opaque and all opaque areas to be transparent.

Solid Matte

Solid Mattes are mask nodes or images connected to the solid matte input on the node. The solid

matte is applied directly to the alpha channel of the image. Generally, solid mattes are used to hold out

keying in areas you want to remain opaque, such as someone with blue eyes against a blue screen.

Enabling Invert will invert the solid matte, before it is combined with the source alpha.

Garbage Matte

Garbage mattes are mask nodes or images connected to the garbage matte input on the node.

The garbage matte is applied directly to the alpha channel of the image. Generally, garbage mattes

are used to remove unwanted elements that cannot be keyed, such as microphones and booms.

They are also used to fill in areas that contain the color being keyed but that you wish to maintain.

Garbage mattes of different modes cannot be mixed within a single tool. A Matte Control node is often

used after a Keyer node to add a garbage matte with the opposite effect of the matte applied to the keyer.

Enabling Invert will invert the garbage matte, before it is combined with the source alpha.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Post-Multiply Image

Select this option to cause the keyer to multiply the color channels of the image against the alpha

channel it creates for the image. This option is usually enabled and is on by default.

Deselect this checkbox and the image can no longer be considered premultiplied for purposes

of merging it with other images. Use the Subtractive option of the Merge node instead of the

Additive option.

For more information on these Merge node settings, see Chapter 95, "Composite Nodes," in

the DaVinci Resolve Reference Manual, or Chapter 35 in the Fusion Reference Manual.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other matte nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.