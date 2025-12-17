---
title: "Corner Positioner [CPn]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 517
---

# Corner Positioner [CPn]

The Corner Positioner node

Corner Positioner Node Introduction

The Corner Positioner can be used to position the four corners of an image interactively. This would

typically be used to replace a sign or other rectangular portion of a scene. Connect all corners to

Paths or Trackers for animation purposes.

Inputs

The two inputs on the Corner Positioner node are used to connect a 2D image and an effect mask,

which can be used to limit the warped area.

Input: The orange input is used for the primary 2D image that is warped.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the Corner Positioner to

only those pixels within the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

Below, the Corner Positioner is used to position the rectangular corners of the MediaIn2 to fit within

a specific area of the MediaIn1 node. A Planar Tracker tracks the background, and then a Planar

Transform is used to keep the Corner Positioner in place as the background clip moves. Once the

planar tracking is completed, and the Planar Transform is created, the Planar Tracker node is no longer

needed, and you can delete it.

The Corner Positioner corner pins a clip in place and uses a Planar

Transform to match move it to the background.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Inspector

The Corner Positioner Controls tab

Controls Tab

The Controls tab includes transform and offset adjustments for the four corners of the image

Mapping Type

This determines the method used to project the image caused by the Corner Positioner. In Bi-Linear

mode, a straight 2D warping takes place. In Perspective mode, the image is calculated with the offsets

in 2D space and then mapped into a 3D perspective.

Corners X and Y

There are four points in the Corner Positioner. Drag these around to position each corner of the image

interactively. Attach these control points to any of the usual modifiers.

The image input is deformed and perspective corrected to match the position of the four corners.

Offset X and Y

These controls can be used to offset the position of the corners slightly. This is useful when the

corners are attached to Trackers with patterns that may not be positioned exactly where they

are needed.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Warp nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Dent [Dnt]

The Dent node

Dent Node Introduction

The Dent node creates a circular deformation of an image similar to a Fish Eye Lens effect, with the

choice of six different Dent filters.

Inputs

The two inputs on the Dent node are used to connect a 2D image and an effect mask, which can be

used to limit the warped area.

Input: The orange input is used for the primary 2D image that is warped.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the Dent to only those

pixels within the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Dent node is used below to make a circular pattern based on a Fast Noise and a Mosaic Blur

(DaVinci Resolve Resolve FX only). The Crop node at the end is used to set the desired resolution.

The Dent node can help create lens distortion effects or a motion graphics background.

Inspector

The Dent Controls tab

Controls Tab

The adjustments in the Controls tab are used to change the Dent style, position, size, and strength.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Type

Select the type of Dent filter to use from this menu. All parameters for the Dent can be keyframed.

Dent 1

This creates a bulge dent.

Kaleidoscope

This creates a dent, mirrors it, and inverts it.

Dent 2

This creates a displacement dent.

Dent 3

This creates a deform dent.

Cosine Dent

This creates a fracture to a center point.

Sine Dent

This creates a smooth rounded dent.

Center X and Y

This positions the Center of the Dent effect on the image. The default values are 0.5, 0.5, which center

the effect in the image.

Size

This changes the size of the area affected by the dent. Animate this slider to make the dent grow.

Strength

This changes the overall strength of the dent.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Warp nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Displace [Dsp]

The Displace node

Displace Node Introduction

The Displace node uses a map image to displace or refract another image. This is useful for creating a

vast range of effects from bevels and heat distortion to glass and water effects.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Inputs

There are three inputs on the Displace node: The primary image, the displacement map foreground

image, and an effect mask.

Input: The orange image input is a required connection for the primary image you wish to displace.

Foreground Image: The green input is also required as the image used to displace the background.

Once connected, you can choose red, green, blue, alpha, or luminance channel to create the

displacement.

Effect Mask: The optional blue effect mask input expects a mask shape created by polylines,

basic primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input

limits the displacement to only those pixels within the mask. An effects mask is applied to the tool

after it is processed.

Basic Node Setup

Below, the Displace node uses a Fast Noise to generate the Displace map. Increasing the seethe rate

can produce heat distortion or flag waving effects.

The Displace node using a Fast Noise node for the Displace map

Inspector

The Displace Controls tab

Controls Tab

The Controls tab is used to change the style, position, size , strength, and lighting (embossing) of the

displacement.

Type

The Type menu is used to choose in what mode the Displace node operates. The Radial mode uses

the map image that refracts each pixel out from the center, while X/Y mode provides control over the

amount of displacement along each axis individually.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

NOTE: There is one set of Refraction controls while in Radial mode, and two sets in XY

mode-one for each of the X and Y channels.

Center (Radial Only)

The Center control defines the point from which pixels are displaced toward or away.

Refraction Channel

This drop-down menu controls which channel from the foreground image is used to displace the

image. Select from Red, Green, Blue, Alpha, or Luminance channels. In XY mode, this control appears

twice, once for the X displacement and once for the Y displacement.

Refraction Strength (Radial)

Controls the strength of the refraction. Higher values cause stronger or more pronounced refraction.

X and Y Refraction (X/Y)

Two separate sliders appear to control the Refraction strength along the X- and Y-axis separately.

Otherwise, this is exactly like Refraction Strength.

Light Power

This controls the intensity, or strength, of the simulated light, causing bright and dim areas to form

according to the contour of the refraction image. Higher values cause the bright and dim areas to be

more pronounced.

Light Angle

This sets the angle of the simulated light source.

Spread

This widens the Displacement effect and takes the edge off the Refraction map. Higher values cause

the ridges or edges to spread out.

Light Channel

Select the channel from the refraction image to use as the simulated light source. Select from Color,

Red, Green, Blue, Alpha, or Luminance channels.

NOTE: The Radial mode pushes pixels inward or outward from a center point, based on

pixel values from the Displacement map. The XY mode uses two different channels from the

map to displace pixels horizontally and vertically, allowing more precise results. Using the XY

mode, the Displace node can even accomplish simple morphing effects. The Light controls

allow directional highlighting of refracted pixels for simulating a beveled look.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Warp nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION