---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 447
---

# Inspector

The Relight controls

Controls

The Controls let you adjust all the parameters of the Relight tool. There are additional on-screen

controls in the viewer as well, depending on the type of Relight effect you choose.

For more information on using Relight controls, see Chapter 162, “Resolve FX Refine.”

�Surface Map: This chooses which mode you will use to create the Surface Map.

Use Internal: Generates the Surface Map internally to the tool.

Use Normals Input: Receives an externally created Surface Map from another node. Connect that

map to the green input of the Relight node.

�Output Surface Map: Checking this box causes this copy of the effect to output a multi-colored

map of the input frame. This Surface Map can then be fed into a second Relight node where the

light sources are placed and adjusted.

�Directional / Point Source / Spotlight:

Directional: Creates a light source that emits from a specific direction at an infinite distance.

Point Source: Creates a light source that emits from a central point.

Spotlight: Is also a point source but it is directed into a cone shape.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

�Relighting Map Preview: Checking this box reveals the Alpha channel of the effect of this light.

Unchecking this box shows the current image but with the light mask in the Alpha channel. Bright

areas of the Map Preview show where the Relight is affecting the image.

The image of a car with the Map Preview box checked. Brighter areas

show where and how the Relight tool will affect the image.

Light Properties

�Brightness: This controls the strength of any grading that is applied to the scene. It does not add

brightness changes on its own but amplifies the changes you make in the grading tools.

�Reach: This controls how much reflections will dim with distance from the light source.

�Contrast: This determines how harsh or gentle the gradient is between light and dark.

Surface Properties

�Glossiness: Gives the illusion of a metallic sheen to reflective surfaces.

�Specularity: When there is any glossiness added, this controls how metallic/shiny that

glossiness is.

�Shadow Softness: Controls how much the light penetrates into shadows due to ambient

reflections, beyond where it would reach otherwise.

Light Direction (Directional only)

�Azimuth/Elevation XY : Controls the direction the light is coming from.

Spotlight (Spotlight only)

�Beam Angle: Sets how broad the cone of light is. This control is also available graphically in

the viewer.

�Edge Softness: Controls the softness of the edges of the light cone/beam. Light Position (Point

Source and Spotlight).

Light Position (Point and Spotlight only)

�These controls are for the the position of the light emitter for Point and Spotlight types. They can

be adjusted here directly, but they are adjusted graphically using the Viewer controls more easily.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

External Map

�Rescale Oversaturated: Different applications use different scalings of the Surface Map.

A common format looks like the Relight plugin’s internal ones but with the colors intensely

saturated and can be dark or black in some areas. If your imported surface map has this

appearance, check this box to re-interpret it.

�Reinterpret Left/Right: Check this box to swap the direction of your external surface map, if your

map surfaces are appearing concave instead of convex.

�Reinterpret Up/Down: Check this box to swap the direction of your external surface map, if your

map surfaces are appearing lit from below when the light is above them.

Ultra Keyer [UKy]

The Ultra Keyer node

Ultra Keyer Node Introduction

Like the newer Delta Keyer, the Ultra Keyer node has two keyers built in to it: a pre-matte keyer acts

as a garbage matte creator and the color difference keyer that extracts fine detail and transparency.

Generally, you start with the Delta Keyer as your first keyer of choice. If you do not get good results, try

Primatte if you are using Fusion Studio. A good third choice is to try the Ultra Keyer.

Inputs

The Ultra Keyer node includes four inputs in the Node Editor.

Input: The orange input accepts a 2D image that contains the color you want to be keyed for

transparency.

Garbage Matte: The gray garbage matte input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps masks. Connecting a mask to this input causes areas of the

image that fall within the matte to be made transparent. The garbage matte is applied directly to the

alpha channel of the image.

Solid Matte: The white solid matte input accepts a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input causes areas of the image

that fall within the matte to be fully opaque.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input limits the pixels where the

keying occurs. An effects mask is applied to the tool after the tool is processed.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Basic Node Setup

A single keyer can rarely get perfect results because most green- or blue-screen shots have problems

the keyer is not made to handle. Keyers often need the help of garbage mattes or solid mattes created

with a Polygon or B-Spline node. Shots can also require more than just one keyer to achieve perfect

results. Below, the Ultra Keyer node has the blue-screen content connected to the orange input. The

result is an image with alpha that can then be connected into the foreground of a Merge node.

An Ultra Keyer node combined with polygon matte as a garbage

matte and connected to the foreground of a Merge

Inspector

The Ultra Keyer Pre-Matte tab


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Pre-Matte Tab

The Pre-Matte tab is where most keying begins. It is used to select the screen color and smooth out

the color of the screen.

Background Color

The Background Color is used to select the color of the blue or green screen of the images. It is good

practice to select the screen color close to the subject to be separated from the screen background.

Red Level, Green Level, Blue Level

These color sliders tune the level of the difference channels to help separate the color. When the

background color is green, Red and Blue level options are provided. When the background color is

blue, Red and Green level options are provided.

Background Correction

Depending on the background color selected above, the keyer iteratively merges the pre-keyed

image over either a blue or green background before processing it further.

In some instances, this leads to better, more subtle edges.

Matte Separation

Matte Separation performs a pre-process on the image to help separate the foreground from the

background before color selection. Generally, increase this control while viewing the alpha to eliminate

the bulk of the background, but stop just before it starts cutting holes in the subject or eroding fine

detail on the edges of the matte.

Pre-Matte Range

These R,G,B, and Luminance range controls update automatically to represent the current color

selection. Colors are selected by selecting the Ultra Keyer node’s tile in the node tree and dragging

the Eyedropper into the viewer to select the colors to be used to create the matte. These range

controls can be used to tweak the selection slightly, although selecting colors in the viewer is all that

is required.

Lock Color Picking

This checkbox prevents accidentally selecting more colors from the view. It is a good idea to

activate this checkbox once the color selection is made for the matte. All other controls in the node

remain editable.

Pre Matte Size

The Pre Matte Size control can be used to soften the general area around the keyed image. This is

used to close holes in the matte often caused by spill in semitransparent areas of the subject. This can

cause a small halo around the subject, which can be removed using the Matte Contract tools found

later in the tool.

Reset Pre Matte Ranges

This discards all color selection by resetting the ranges but maintains all other slider and

control values.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

The Ultra Keyer Image tab

Image Tab

The Image tab handles the majority of spill suppression in the Ultra Keyer. Spill suppression is a form of

color correction that attempts to remove the screen color from the fringe of the matte.

Spill is the transmission of the screen color through the semitransparent areas of the alpha channel. In

the case of blue- or green-screen keying, this usually causes the color of the background to become

apparent in the edges of the foreground subject.

Spill Suppression

When this slider is set to 0, no spill suppression is applied to the image. Increasing the slider increases

the strength of the spill method.

Spill Method

This selects the strength of the algorithm used to apply spill suppression to the image.

�None: None is selected when no spill suppression is required.

�Rare: This removes very little of the spill color and is the lightest of all methods.

�Medium: This works best for green screens.

�Well Done: This works best for blue screens.

�Burnt: This works best for blue screens. Use this mode only for very troublesome shots.

Fringe Gamma

This control can be used to adjust the brightness of the fringe or halo that surrounds the keyed image.

Fringe Size

This expands and contracts the size of the fringe or halo surrounding the keyed image.

Fringe Shape

Fringe Shape presses the fringe toward the external edge of the image or pulls it toward the inner

edge of the fringe. Its effect is most noticeable while the Fringe Size value is large.

Cyan/Red, Magenta/Green, and Yellow/Blue

Use these three controls to color correct the fringe of the image.

This is useful for correcting semitransparent pixels that still contain color from the original background

to match the new background.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

.

The Ultra Keyer Matte tab

Matte Tab

The Matte tab refines the alpha of the key, combined with any solid and garbage masks connected to

the node. When using the Matte tab, set the viewer to display the alpha channel of the Delta Keyer’s

final output.

Filter

This control selects the filtering algorithm used when applying blur to the matte.

�Box: This is the fastest method but at reduced quality. Box is best suited for minimal

amounts of blur.

�Bartlett: Otherwise known as a Pyramid filter, Bartlett makes a good compromise between speed

and quality.

�Multi-Box: When selecting this filter, the Num Passes slider appears and lets you control the

quality. At 1 and 2 passes, results are identical to Box and Bartlett, respectively. At 4 passes and

above, results are usually as good as Gaussian, in less time and with no edge “ringing.”

�Gaussian: The Gaussian filter uses a true Gaussian approximation and gives excellent results, but

it is a little slower than the other filters. In some cases, it can produce an extremely slight edge

“ringing” on floating-point pixels.

Blur

Matte Blur blurs the edge of the matte based on the Filter menu setting. A value of zero results in a

sharp, cutout-like hard edge. The higher the value, the more blur applied to the matte.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Clipping Mode

This option determines how edges are handled when performing domain of definition rendering.

This is profoundly important when blurring the matte, which may require samples from portions of the

image outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition. If

the upstream DoD is smaller than the frame, the remaining areas in the frame are treated

as black/transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that would normally be outside the upstream

DoD is treated as black/transparent.

Contract/Expand

This slider shrinks or grows the semitransparent areas of the matte. Values above 0.0 expand the

matte, while values below 0.0 contract it.

This control is usually used in conjunction with the Matte Blur to take the hard edge of a matte and reduce

fringing. Since this control affects only semitransparent areas, it has no effect on a matte’s hard edge.

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


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Solid Matte

Solid mattes are mask nodes or images connected to the solid matte input on the node. The solid

matte is applied directly to the alpha channel of the image. Generally, solid mattes are used to hold out

keying in areas you want to remain opaque, such as someone with blue eyes against a blue screen.

Enabling Invert inverts the solid matte before it is combined with the source alpha.

Garbage Matte

Garbage mattes are mask nodes or images connected to the garbage matte input on the node.

The garbage matte is applied directly to the alpha channel of the image. Generally, garbage mattes

are used to remove unwanted elements that cannot be keyed, such as microphones and booms.

They are also used to fill in areas that contain the color being keyed but that you wish to maintain.

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

in the DaVinci Resolve Reference Manual, or Chapter 35 in the Fusion Reference Manual.

Subtract Background

This option color corrects the edges when the screen color is removed and anti-aliased to a black

background. By enabling this option, the edges potentially become darker. Disabling this option allows

you to pass on the color of the screen to use in other processes down the line.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other matte nodes. These common controls

are described in detail in the following “The Common Controls” section.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION