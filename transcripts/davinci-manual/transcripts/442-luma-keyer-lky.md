---
title: "Luma Keyer [LKy]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 442
---

# Luma Keyer [LKy]

The Luma Keyer node

Luma Keyer Node Introduction

The Luma Keyer node uses the overall luminance of an image to create an Alpha channel. The label

of this node may seem misleading since it allows pulling mattes from almost any channel. In some

respects, it is more accurate to call this node an all-purpose channel keyer, but its primary purpose is

for extracting alpha channels based on luminance

Inputs

The Luma Keyer node includes four inputs in the Node Editor.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Input: The orange input accepts a 2D image that contains the luminance values you want to be keyed

for transparency.

Garbage Matte: The gray garbage matte input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps masks. Connecting a mask to this input causes areas of the

image that fall within the matte to be made transparent. The garbage matte is applied directly to the

alpha channel of the image.

Solid Matte: The white solid matte input accepts a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input causes areas of the image

that fall within the matte to be fully opaque.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input limits the pixels where the

luminance key occurs. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Luma Keyer takes an input from an image with significant luminance difference to extract a key.

You can then use the output of the Luma Keyer into any mask input.

A Luma Keyer output connecting into an effect mask on a Merge node

Inspector

The Luma Keyer Controls tab


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Controls Tab

The Controls tab in the Luma Keyer contains all the parameters for adjusting the quality of the matte.

Channel

This menu selects the color channel used for creating the matte. Select from the Red, Green, Blue,

Alpha, Hue, Luminance, Saturation, and Depth (Z-buffer) channels.

Threshold

This range slider sets the lower threshold using the handle on the left and sets the upper threshold

using the handle on the right. Adjusting them defines a range of luminance values to create a matte.

A value below the lower threshold setting becomes black or transparent in the matte.

Any value above the upper threshold setting becomes white or opaque in the matte.

The values within the range create a grayscale matte.

Filter

This control selects the filtering algorithm used when applying a blur to the matte.

�Box: This is the fastest method but at reduced quality. Box is best suited for minimal amounts of blur.

�Bartlett: Otherwise known as a Pyramid filter, Bartlett makes a good compromise between

speed and quality.

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

�Frame: The default option is Frame, which automatically sets the node’s domain of definition to use

the full frame of the image, effectively ignoring the current domain of definition. If the upstream

DoD is smaller than the frame, the remaining area in the frame is treated as black/transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that is usually outside the upstream DoD is

treated as black/transparent.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

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

Solid mattes are mask nodes or images connected to the solid matte input on the node. The solid

matte is applied directly to the alpha channel of the image. Generally, solid mattes are used to hold out

keying in areas you want to remain opaque, such as someone with blue eyes against a blue screen.

Enabling Invert inverts the solid matte before it is combined with the source alpha.

Garbage Matte

Garbage mattes are mask nodes or images connected to the garbage matte input on the node. The

garbage matte is applied directly to the alpha channel of the image. Generally, garbage mattes are

used to remove unwanted elements that cannot be keyed, such as microphones and booms. They are

also used to fill in areas that contain the color being keyed but that you wish to maintain.

Garbage mattes of different modes cannot be mixed within a single tool. A Matte Control node is often

used after a Keyer node to add a garbage matte with the opposite effect of the matte applied to the keyer.

Enabling Invert inverts the garbage matte before it is combined with the source alpha.

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

The Settings tab in the Inspector is also duplicated in other Matte nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Magic Mask [MagM]

The Magic Mask node

Magic Mask Node Introduction

The Magic Mask palette uses the DaVinci Neural Engine to automagically create a mask to isolate an

object in the frame, guided by user-applied paint strokes to identify the subject for isolation. Masks

can be generated for either an entire object or just a part of it. This allows you to create complicated

masks of complex shapes that may be difficult to isolate with other tools. For example, using the Magic

Mask to modify only the wood grain section of this guitar.

(Left) Multiple strokes isolating the wood grain of the guitar, while ignoring the

musician’s arm; (Right) The finished shot, with a warmer wood grain

NOTE: The Magic Mask tool in Fusion is based on the Object mode of the Magic Mask tool

in the Color page and is designed to be used for any subject that is not a person. Subjects

like cars, pets, and food are all good candidates for Object mode. If you are trying to isolate

a human being, using Magic Mask’s Person mode in the Color page will likely give you

better results.

Drawing Strokes in the Viewer

The Magic Mask tool works by drawing lines directly into the viewer. Once a stroke is drawn, the

viewer will automatically show the mask you’ve created. You can draw multiple strokes to create a

mask in an additive fashion and use negative strokes to remove areas from the mask. It is best to

choose a frame to draw on where the object is completely in view and unobstructed.

�To draw a positive stroke to add an object to a mask: Load the Magic Mask node in a viewer, and

left-click and drag the stroke across the object you want to choose. Alternatively you can change

the Stroke Mode to Add in the Inspector and left-click and drag to draw a new positive stroke.

Positive strokes are colored blue.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

�To draw a negative stroke to remove an object from a mask: Load the Magic Mask node

in a viewer, and Option-left-click and drag the stroke across the object you want to remove.

Alternatively you can change the Stroke Mode to Subtract in the Inspector and left-click and drag

to draw a new negative stroke. Negative strokes are colored red.

�To delete a stroke (or group of strokes) to remove them from the mask: Shift-drag around a

stroke or group of strokes to select them (green), and press the delete key to remove them.

Alternatively you can change the Stroke Mode to Select in the Inspector and left-click and drag a

selection window to select one or more strokes. Clicking the delete button removes them.

Drawing positive strokes will select areas of similar contrast and color, allowing you to link complex

shapes together. Generally you will need more strokes to actively define a complex object, due to the

greater variety of the shapes involved. Stroke position is usually more important than stroke length.

Drawing negative strokes removes areas from the object that you don’t want to isolate. This can

be something simple, like removing the wheels of a car from a mask, or more complicated like

removing specific books from a mask of a bookshelf. Stroke position is usually more important than

stroke length.

(Left) Multiple strokes isolating the car’s body, while removing the wheels and cabin; (Right) The

finished shot, fed through a color corrector node to change the color of just the car’s body