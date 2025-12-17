---
title: "Highlight [HIL]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 403
---

# Highlight [HIL]

The Highlight node

Highlight Node Introduction

The Highlight filter creates star-shaped highlights or glints in bright regions of the image, similar to a

lens star filter effect.

Inputs

There are three Inputs on the Highlight node: one for the image, one for the effects mask, and another

for a highlight mask.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Input: The orange input is used for the primary 2D image that gets the highlight applied.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input restricts the highlight to be within

the pixels of the mask. An effects mask is applied to the tool after the tool is processed.

Highlight Mask: The Highlight node supports pre-masking using the white highlight mask input. The

image is filtered before the highlight is applied. The highlight is then merged back over the original

image. Unlike regular effect masks, it does not crop off highlights from source pixels when the

highlight extends past the edges of the mask.

Highlight masks are identical to effects masks in every other respect.

Basic Node Setup

The Highlight node below is used to create glint-type highlights on an incoming image. The highlight

mask is used to limit the area where the effect is applied.

A Highlight node applied to an image, with a

highlight mask limiting the area of the effect

Inspector

Highlight controls

Controls Tab

The Controls tab includes parameters for the highlight style except for color, which is handled in the

Color Scale tab.

Low and High

This range control designates the range of Luminance values in the image that generates highlights.

Values less than the Low value do not receive highlights. Values above the High value receive the full

highlight effect.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Curve

The Curve value changes the drop-off over the length of the highlight. Higher values cause the

brightness of the flares to drop off closer to the center of the highlight, whereas lower values drop off

farther from the center.

Length

This designates the length of the flares from the highlight.

Number of Points

This determines the number of flares emanating from the highlight.

Angle

Use this control to rotate the highlights.

Merge Over

When enabled, the effect is overlaid on the original image. When disabled, the output is the highlights

only. This is useful for downstream color correction of the highlights.

Highlight Color Scale controls

Color Scale Tab

The Color Scale tab controls the color of the highlight.

By click and holding on the Pick button, then dragging the pointer over the viewer, you can select a

specific color from the image.

Red, Green, and Blue Scale

Moving the sliders of one or all of these channels down changes the falloff color of the highlight.

Alpha Scale

Moving the Alpha slider down makes highlight falloff more transparent.

Common Controls

Setting Tab

The Settings tab controls are common to all Effect nodes, so their descriptions can be found in

“The Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Hot Spot [Hot]

The Hot Spot node

Hot Spot Node Introduction

The Hot Spot node is used to create lens flare, spotlight, and burn/dodge effects of various types.

In the real world, lens flares occur when extremely bright light sources in the scene by the reflections

are reflected off elements inside the lens of the camera. One might see lens flares in a shot when

viewing a strong light source through a camera lens, like the sun or another bright star.

Inputs

There are three inputs on the Hot Spot node: one for the image, one for the effects mask, and another

for an Occlusion image.

Input: The required orange input is used for the primary 2D image that gets the hot spot applied.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input restricts the hot spot to be within

the pixels of the mask. An effects mask is applied to the tool after the tool is processed.

Occlusion: The green Occlusion input accepts an image to provide the occlusion matte. The matte

is used to block the hot spot, causing it to “wink.” The white pixels in the image occlude the hot spot.

Gray pixels partially suppress the hot spot.

Basic Node Setup

The Hot Spot node is not a stand-alone generator, so it must have an image input that gets the hot

spot applied.

Hot Spot node applied to an image


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Inspector

Hot Spot controls

Hot Spot Tab

The Hotspot tab is used to control the primary and secondary hot spots. You can adjust their position,

size, strength, angle, and apply mode.

Primary Center X and Y

This is the position of the primary hot spot within the scene. Secondary lens elements and reflections

are positioned relative to the position of the primary hot spot.

Primary Strength

This control determines the brightness of the primary hot spot.

Hot Spot Size

This control determines the diameter of the primary hot spot. A value of 1.0 represents a circle the full

width of the image.

Aspect

This controls the aspect of the spot. A value of 1.0 produces a perfectly circular hot spot. Values

above 1.0 elongate the circle horizontally, and values below 1.0 elongate the circle vertically.

Aspect Angle

This control can be used to rotate the primary hot spot.

Secondary Strength

This control determines the strength, which is to say the brightness, of the secondary hot spot. The

secondary hot spot is a reflection of the primary hot spot. It is always positioned on the opposite side

of the image from the primary hot spot.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Secondary Size

This determines the size of the secondary hot spot.

Apply Mode

This control determines how the hot spot affects the underlying image.

�Add (Burn): This causes the spots created to brighten the image.

�Subtract (Dodge): This causes the spots created to dim the image.

�Multiply (Spotlight): This causes the spots created to isolate a portion of the image with light and

to darken the remainder of the image.

Occlude

This menu is used to select which channel of the image connected to the Hot Spot node’s Occlusion

input is used to provide the occlusion matte. Occlusion can be controlled from Alpha or R, G, or B

channels of any image connected to the Occlusion input on the node’s tile.

Lens Aberration

Aberration changes the shape and behavior of the primary and secondary hot spots.

�In and Out Modes: Elongates the shape of the hot spot into a flare. The hot spot stretches toward

the center when set to In mode and stretches toward the corners when set to Out mode.

�Flare In and Flare Out Modes: This option is a lens distortion effect that is controlled by the

movement of the lens effect. Flare In causes the effect to become more severe, the closer the hot

spot gets to the center. Flare Out causes the effect to increase as the hot spot gets closer to the

edges of the image.

�Lens: This mode emulates a round, ringed lens effect.

Aberration

The Aberration slider controls the overall strength of the lens aberration effect.

Color Tab

The Color tab is used to modify the color of the primary and secondary hot spots.

Hot Spot color controls


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Color Mode

This menu allows you to choose between animated or static color modifications using the small curves

editor in the Inspector.

�None: The default None setting retains a static curve adjustment for the entire range.

�Animated Points: This setting allows the color curves in the spline area to be animated over time.

Once this option is selected, moving to the desired frame and making a change in the Spline

Editor sets a keyframe.

�Dissolve mode: Dissolve mode is mostly obsolete and is included for compatibility reasons only.

Color Channel and Mix

When selected, these checkboxes enable the editing of the chosen splines in the small Inspector

Spline Editor. The Mix checkbox enables the Mix Spline, which is used to determine the influence of

the controls that the Radial tab has along the radius of the hot spot.

Red, Green, Blue, and Alpha Splines

The Spline Window shows the curves for the individual channels. It is a miniature Spline Editor. The

Red, Green, Blue, and Alpha splines are used to adjust the color of the spotlight along the radius of

the hot spot.

The vertical axis represents the intensity or strength of the color channel. The horizontal axis

represents the hot spot position along the radius, from the left outside edge to the inside right edge.

The default curve indicates that the red, green, blue, and Alpha channels all have a linear falloff.

Mix Spline

The Mix spline is used to determine the influence that the Radial controls have along the radius of the

hot spot. The horizontal axis represents the position along the circle’s circumference, with 0 being 0

degrees and 1.0 being 360 degrees. The vertical axis represents the amount of the radial hot spot to

blend with the color hot spot. A value of 0 is all radial hot spot, while a value of 1.0 is all color hot spot.

NOTE: Right-clicking in the LUT displays a contextual menu with options related to modifying

spline curves.

For more information on the LUT Editor, see Chapter 69, “Using Viewers.” in the

DaVinci Resolve Reference Manual, or Chapter 7 in the Fusion Reference Manual.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Hot Spot Radial tab

Radial Tab

Radial On

This control enables the Radial splines. Otherwise, the radial matte created by the splines is not

applied to the hot spot, and the Mix spline in the color controls does not affect the hot spot.

Radial Mode

Similar to the Color mode menu, this menu allows you to choose between animated or static radial hot

spot modifications using the small curves editor in the Inspector.

�No Animation: The default setting retains a static curve adjustment for the entire range.

�Animated Points: This setting allows the radial curves in the spline area to be animated over time.

Once this option is selected, moving to the desired frame and making a change in the Spline

Editor sets a keyframe.

The Interpolated Values option is mostly obsolete and is included for compatibility reasons only.

Radial Length and Radial Density Splines

The Spline window shows curves for the Length and Density of the hot spot. It is a miniature Spline

Editor. The key to these splines is realizing that the horizontal axis in Inspector’s Spline Editor

represents a position around the circumference of the hot spot. A value of 0.0 is 0 degrees, and 1.0 is

360 degrees. With that in mind, the length determines the radius of light making up the hot spot along

the circumference. The density represents how bright the light is along the circumference.

Radial Repeat

This control repeats the effect of the radial splines by x number of times. For example, a repeat of 2.0

causes the spline to take effect between 0 and 180 degrees instead of 0 and 360, repeating the spline

between 180 and 360.

Length Angle

This control rotates the effect of the Radial Length spline around the circumference of the hot spot.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Density Angle

This control rotates the effect of the Radial Density spline around the circumference of the hot spot.

NOTE: Right-clicking in the spline area displays a contextual menu containing options related

to modifying spline curves.

A complete description of LUT Editor controls and options, see Chapter 107, “LUT Nodes,”

in DaVinci Resolve Reference Manual and Chapter 47 in the Fusion Reference Manual.

L1, L2, and L3 Tab

L1 tab

L2 tab

L3 tab

Lens Reflect Tabs

The three Lens Reflect tabs are used to enable and design additional lens flare elements beyond the

primary and secondary hot spots.

Lens Reflect 1-3

Each of these three checkboxes enables a pair of lens reflection elements that you can modify using

the controls in this tab. The parameters affect all the enabled Lens reflection elements in this tab.

Element Strength

This determines the brightness of element reflections.

Element Size

This determines the size of element reflections.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Element Position

This determines the distance of element reflections from the axis. The axis is calculated as a line

between the hot spot position and the center of the image.

Element Type

Use this group of buttons to choose the shape and density of the element reflections. The presets

available are described below.

�Circular: This creates slightly soft-edged circular shaped reflections.

�Soft Circular: This creates very soft-edged circular shaped reflections.

�Circle: This creates a hard-edged circle shape.

�NGon Solid: This creates a filled polygon with a variable number of sides.

�NGon Star: This creates a very soft-edged star shape with a variable number of sides.

�NGon Shaded Out: This creates soft-edged circular shapes.

�NGon Shaded In: This creates a polygon with a variable number of sides, which has a very soft

reversed (dark center, bright radius) circle.

�NGon Angle: This control is used to determine the angle of the NGon shapes.

�NGon Sides: This control is used to determine the number of sides used when the Element Type is

set to Ngon Star, Ngon Shaded Out, and Ngon Shaded In.

�NGon Starriness: This control is used to bend polygons into star shapes. The higher the value, the

more star-like the shape.

Lens Color Controls

These controls determine the color of the lens that affects the colors of the reflections. To choose a

lens color, pick one from a displayed image or enter RGBA values using the sliders or input boxes.

Common Controls

Settings Tab

The Settings tab controls are common to all Effect nodes, so their descriptions can be found in “The

Common Controls” section at the end of this chapter.