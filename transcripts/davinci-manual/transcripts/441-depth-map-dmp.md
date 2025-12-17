---
title: "Depth Map [DMp]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 441
---

# Depth Map [DMp]

The Depth Map node

Depth Map Node Introduction

Depth Map creates an Alpha channel based on the perceived distance of objects in your clip. By being

able to isolate a specific depth region, the opportunities to manipulate the resulting image are greatly

expanded. For example, combined with a Blur node you could simulate a depth of field effect, but

confined only to the distant background of your shot. You could enhance a foreground object, like a

person, increasing contrast, saturation, and sharpness, similar to using a qualifier. You can use a Depth

Map to fix video issues, for example fixing a color temperature problem by isolating a far window that

was shot in daylight, causing background actors to be tinted blue, while leaving the foreground subject

that was shot with studio lighting unaffected.

The resulting Depth Map Alpha channel is visualized as a black and white image, with white being the

area that is affected by the resulting changes and black areas remaining unchanged.

Inputs

The Depth Map node includes two inputs in the Node Editor.

Input: The yellow input accepts a 2D image that contains the shot you wish to analyze for depth.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input limits the pixels where the

difference matte occurs. An effects mask is applied to the tool after the tool is processed.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Basic Node Setup

The Depth Map is designed to take an input from an image source and create an Alpha channel based

on the perceived distance from the camera. Then it will feed that Alpha to downstream nodes. In the

example below, the Depth Map is used to isolate the background of the image and apply a color grade

to just the background, while leaving the foreground actors unaffected as they move through the frame.

A sample Depth Map node structure for isolating subjects based on distance from the camera

Inspector

The Depth Map Controls tab

Controls Tab

The Controls tab in the Depth Map contains all the parameters for adjusting the quality of the

resulting matte.

�Mode: Depth Map is a very computationally intensive effect. The quality setting allows a Faster

mode to speed up the responsiveness to adjustments, while the default Better mode gives the

best results and should be turned on when the adjustments are finished.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

�Depth Map Preview: By default this box is checked and shows you the current Depth Map for

making adjustments. When this check box is disabled, the resulting Alpha can then be used for

grading on other nodes.

�Invert: Checking this box reverses the Depth Map, switching its transparent and opaque regions.

Resulting Map Adjustment

These controls let you determine how the Depth Map’s contrast is adjusted.

�Adjust Map Levels: When deselected (default), all scaling is turned off, allowing you to adjust the

full range of the Depth Map. When enabled, this option clips the Depth Map’s levels to 0 and 1.

This functions as a preview of what will happen to the Depth Map when used as an Alpha channel

where the values are always clipped to 0 and 1. Checking this box also activates the tools below.

�Far Limit: This control adjusts the black levels of the Depth Map.

�Near Limit: This control adjusts the white levels of the Depth Map.

�Gamma: This control adjusts the intermediate depth values to be brighter or dimmer compared to

the fixed black and white levels.

Isolate Specific Depth

These controls allow you to sweep backwards and forwards in the scene by depth, allowing you to

isolate a specific depth range to adjust.

�Isolation: This checkbox turns the depth isolation tools on or off.

�Target Depth: This controls the specific depth you want to isolate. 1 is fully in the foreground, while

0 is fully in the background.

�Tolerance: Sets the range to either side of the Target Depth to include in the Depth Map.

�Softness: This sets a subtle ramp-in and ramp-out of the selected range, giving it a more

organic selection.

Map Finesse

These controls modify the resulting Depth Map’s Alpha channel for use in grading.

�Post Processing: This control turns the Map Finesse tools on or off.

�Post-Filter: This control blends the map to the smooth areas and edges of the image. It is used to

prevent later grading effects from visibly varying within the region.

�Contract/Expand: This control dilates or erodes the overall shape at the edges; useful for fine

tuning the boundary between the affected and unaffected regions of the map.

�Blur: This control softens the boundary of the map, allowing it to blend more smoothly into the

resulting image.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Matte nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Difference Keyer [DfK]

The Difference Keyer node

Difference Keyer Node Introduction

Difference keying is a process that produces a matte based on the differences between two images.

A difference key uses two input images: one containing the subject with the background and another

containing the background without the subject.

Although the process sounds reasonable at first glance, subtle variations in the camera position from

shot to shot usually make it difficult to get clean results. Think of the futile attempt of trying to key

smoke in front of a brick wall and using a clean plate of the brick wall as your difference input. Part of

the wall’s structure is always visible in this keying method. Instead, a Difference Keyer is often used to

produce a rough matte that is combined with other nodes to produce a more detailed matte.

Inputs

The Difference Keyer node includes four inputs in the Node Editor.

Background: The orange background input accepts a 2D image that contains just the set without your

subject.

Foreground: The green foreground input accepts a 2D image that contains the shot with your subject

in the frame.

Garbage Matte: The gray garbage matte input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps masks. Connecting a mask to this input causes areas of the

image that fall within the matte to be made transparent.

Solid Matte: The white solid matte input accepts a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input causes areas of the image

that fall within the matte to be fully opaque.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input limits the pixels where the

difference matte occurs. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

When you do not have content shot on a blue or green screen, the Difference Keyer can be one

node in a chain of many used to extract an object from the background. The example below has

the MediaIn1 as the main subject and a clean background shot without the subject (Background). A

B-Spline is used to limit the area the Difference Keyer must deal with for extraction. The result is a

matte that can be used to help but not solve the key.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

A Difference Keyer with two inputs: one of the subject on a

background and the other of just the background

Inspector

The Difference Keyer Controls tab

Controls Tab

The Controls tab in the Difference Keyer contains all the parameters for adjusting the quality of

the matte.

Threshold

This range slider sets the lower threshold using the handle on the left and sets the upper threshold

using the handle on the right. Adjusting them defines a range of difference values between the

images to create a matte.

A difference below the lower threshold setting becomes black or transparent in the matte.

Any difference above the upper threshold setting becomes white or opaque in the matte.

The difference values in the range in between create a grayscale matte.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Filter

This control selects the filtering algorithm used when applying a blur to the matte.

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

This blurs the edge of the matte using the method selected in the Filter menu. A value of zero results

in a sharp, cutout-like hard edge. The higher the value, the more blur.

Clipping Mode

This option determines how edges are handled when performing domain of definition rendering.

This is profoundly important when blurring the matte, which may require samples from portions of the

image outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition. If the

upstream DoD is smaller than the frame, the remaining area in the frame is treated as black/

transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that would usually be outside the upstream

DoD is treated as black/transparent.

Contract/Expand

This slider shrinks or grows the semitransparent areas of the matte. Values above 0.0 expand the

matte, while values below 0.0 contract it.

This control is usually used in conjunction with the blur to take the hard edge of a matte and reduce

fringing. Since this control affects only semitransparent areas, it has no effect on a matte’s hard edge.

Gamma

Matte Gamma raises or lowers the values of the matte in the semitransparent areas. Higher values

cause the gray areas to be more opaque, and lower values cause the gray areas to be more

transparent. Wholly black or white regions of the matte remain unaffected.

Invert

Selecting this checkbox inverts the matte, causing all transparent areas to be opaque and all opaque

areas to be transparent.

Solid Matte

Solid Mattes are mask nodes or images connected to the solid matte input on the node. The solid

matte is applied directly to the alpha channel of the image. Generally, solid mattes are used to hold out

keying in areas you want to remain opaque, such as someone with blue eyes against a blue screen.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Enabling Invert, inverts the solid matte before it is combined with the source alpha.

Garbage Matte

Garbage mattes are mask nodes or images connected to the garbage matte input on the node. The

garbage matte is applied directly to the alpha channel of the image. Generally, garbage mattes are

used to remove unwanted elements that cannot be keyed, such as microphones and booms. They are

also used to fill in areas that contain the color being keyed but that you wish to maintain.

Garbage mattes of different modes cannot be mixed within a single tool. A Matte Control node is

often used after a Keyer node to add a garbage matte with the opposite effect of the matte applied to

the keyer.

Enabling Invert inverts the garbage matte before it is combined with the source alpha.

Post-Multiply Image

Select this option to cause the keyer to multiply the color channels of the image against the alpha

channel it creates for the image. This option is usually enabled and is on by default.

Deselect this checkbox and the image can no longer be considered premultiplied for purposes

of merging it with other images. Use the Subtractive option of the Merge node instead of the

Additive option.

For more information on these Merge node settings, see Chapter 95, "Composite Nodes,"

in the DaVinci Resolve Reference Manual, or Chapter 35 in the Fusion Reference Manual.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Matte nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.