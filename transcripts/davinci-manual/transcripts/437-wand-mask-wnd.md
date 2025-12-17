---
title: "Wand Mask [Wnd]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 437
---

# Wand Mask [Wnd]

The Wand node

Wand Mask Node Introduction

The Wand mask masks an image based on a wand-style selection, similar to the Magic Wand tool

found in Adobe Photoshop. As with a Bitmap mask, any image in the composition can be the source

of the mask. Generally, the default is most useful, where the source image is the input of the node to

which the mask is applied.

When adding a Wand mask to a node, a crosshair appears in the viewers. This crosshair should be

positioned in the image to select the color used to create the Wand mask. The mask is created by

examining the pixel color beneath the selection point and adding that color to the mask. The mask

then expands to examine the pixels surrounding the selection point. Surrounding pixels are added to

the mask if they are the same color. The mask stops expanding when no connecting pixels fall within

the color range of the mask.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Inputs

The Wand mask node includes two inputs in the Node Editor.

Input: The orange input accepts a 2D image from which the mask is created.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input combines the masks. How

masks are combined is handled in the Paint mode menu in the Inspector.

Basic Node Setup

The Wand mask node is not required for connecting an image into the effect mask input, but like the

Bitmap node, it does provide options that are otherwise unavailable. It allows for selecting channels

other than RGBA for the mask, as well as softness and clipping. In the node tree below, the Wand

node takes the composite out of the merge, creating a mask for the color correction.

A Wand node selects a specific area in the image to create a mask.

Inspector

Wand Mask controls

Controls Tab

The Controls tab is used to refine how the mask appears after the Wand makes a selection in

the viewer.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Show View Controls

The Show View Controls checkbox is used to enable/disable the display of the mask’s onscreen

controls in the viewer. Onscreen controls, including center position, polylines, angles, and others,

do not appear when this checkbox is disabled, even when the node is selected.

Level

The Level control sets the transparency level of the pixels in the mask channel. When the value is 1.0,

the mask is completely opaque (unless it has a soft edge). Lower values cause the mask to be partially

transparent. The result is identical to lowering the Blend control of an effect.

NOTE: Lowering the level of a mask lowers the values of all pixels covered by the mask in

the mask channel. For example, if a Circle mask is placed over a Rectangle mask, lowering

the level of the Circle mask lowers the values of all the pixels in the mask channel, even

though the Rectangle mask beneath it is still opaque.

Filter

This control selects the filtering algorithm used when applying Soft Edge to the mask.

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

Soft Edge

Use the Soft Edge slider to blur (feather) the mask, using the selected filter. Higher values cause

the edge to fade off well beyond the boundaries of the mask. A value of 0.0 creates a crisp, well-

defined edge.

Paint Mode

Connecting a mask to the effect mask input displays the Paint mode menu. The Paint mode is used

to determine how the incoming mask for the effect mask input and the mask created in the node

are combined.

�Merge: Merge is the default for all masks. The new mask is merged with the input mask.

�Add: The mask’s values add to the input mask’s values.

�Subtract: In the intersecting areas, the new mask values subtract from the input mask’s values.

�Minimum:  Comparing the input mask’s values and the new mask, this displays the lowest

(minimum) value.

�Maximum:  Comparing the input mask’s values and the new mask, this displays the highest

(maximum) value.

�Average: This calculates the average (half the sum) of the new mask and the input mask.

�Multiply: This multiplies the values of the input mask by the new mask’s values.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

�Replace: The new mask completely replaces the input mask wherever they intersect. Areas that

are zero (completely black) in the new mask do not affect the input mask.

�Invert: Areas of the input mask that are covered by the new mask are inverted; white becomes

black and vice versa. Gray areas in the new mask are partially inverted.

�Copy: This mode completely discards the input mask and uses the new mask for all values.

�Ignore: This mode completely discards the new mask and uses the input mask for all values.

Invert

Selecting this checkbox inverts the entire mask. Unlike the Invert Paint mode, this checkbox affects all

pixels, regardless of whether the new mask covers them.

Selection Point

The Selection Point is a pair of X and Y coordinates that determines where in the source image the

Wand mask derives its initial color sample. This control is also seen as a crosshair in the viewers. The

selection point can be positioned manually, connected to a tracker, path, or other expressions.

Color Space

The Color Space button group determines the color space used when selecting the source color for

the mask. The Wand mask can operate in RGB, YUV, HLS, or LAB color spaces.

Channel

The Channel button group is used to select whether the color that is masked comes from all three

color channels of the image, the alpha channel, or an individual channel only.

The exact labels of the buttons depend on the color space selected for the Wand mask operation.

If the color space is RGB, the options are R, G, or B. If YUV is the color space, the options are Y, U, or V.

Range

The Range slider controls the range of colors around the source color that are included in the mask.

If the value is left at 0.0, only pixels of the same color as the source are considered part of the mask.

The higher the value, the more that similar colors in the source are considered to be wholly part

of the mask.

Range Soft Edge

The Range Soft Edge determines the falloff range of the colors selected. Any pixel within the range

defined above are treated as 100% within the mask. If the soft range is set to 0.0, no other pixels are

considered for the mask. Increasing the soft range increases the number of colors close to, but not

quite within, the range included in the mask. These pixels are semitransparent in the mask


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

The Common Controls

Nodes that create masks share several identical controls in the Inspector. This section describes

controls that are common among mask nodes.

Inspector

Mask node Image tab

Image Tab

The controls in this tab set the resolution and clipping method used by the generated mask.

Output Size

The Output size menu sets the resolution of the mask node’s output. The three options include the

default resolution of the comp, the source input’s resolution on nodes that have an input, or a custom

resolution.

Custom

When selecting Custom from the Output Size menu, the width, height, and pixel aspect of the mask

created are locked to values defined in the composition’s Frame Format preferences. If the Frame

Format preferences change, the resolution of the mask produced is changed to match. Disabling

this option can be useful for building a composition at a different resolution than the eventual target

resolution for the final render.

�Width and Height: This pair of controls is used to set the Width and Height dimensions of the

mask to be created.

�Pixel Aspect: This control is used to specify the Pixel Aspect ratio of the created mask. An aspect

ratio of 1:1 would generate a square pixel with the same dimensions on either side (like a computer

monitor), and an aspect of 0.91 would create a slightly rectangular pixel (like an NTSC monitor).

�Depth: The Depth drop-down menu is used to set the pixel color depth of the image created by

the mask. 32-bit pixels require four times the memory of 8-bit pixels but have far greater accuracy.

Float pixels allow high dynamic range values outside the normal 0..1 range, for representing colors

that are brighter than white or darker than black.

NOTE: Right-click on the Width, Height, or Pixel Aspect controls to display a menu listing the

file formats defined in the preferences Frame Format tab. Selecting any of the listed options

sets the width, height, and pixel aspect to the values for that format.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Clipping Mode

This option determines how the domain of definition rendering handles edges. The Clipping mode

is most important when blur or softness is applied, which may require samples from portions of the

image outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition. If

the upstream DoD is smaller than the frame, the remaining area in the frame is treated as

black/transparent.

�None: Setting this option to None does not perform any source image clipping. Any data required

to process the node’s effect that would usually be outside the upstream DoD is treated as

black/transparent.

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Mask category. The Settings

controls are even found on third-party plugin tools. The controls are consistent and work the same

way for each tool, although some tools do include one or two individual options, which are also

covered here.

Common Mask Settings controls


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION

Motion Blur

�Motion Blur: This toggles the rendering of Motion Blur on the tool. When this control is toggled

on, the tool’s predicted motion is used to produce the motion blur caused by the virtual camera’s

shutter. When the control is toggled off, no motion blur is created.

�Quality: Quality determines the number of samples used to create the blur. A quality setting of

2 causes Fusion to create two samples to either side of an object’s actual motion. Larger values

produce smoother results but increase the render time.

�Shutter Angle: Shutter Angle controls the angle of the virtual shutter used to produce the motion

blur effect. Larger angles create more blur but increase the render times. A value of 360 is the

equivalent of having the shutter open for one full frame exposure. Higher values are possible and

can be used to create interesting effects.

�Center Bias: Center Bias modifies the position of the center of the motion blur. This allows for the

creation of motion trail effects.

�Sample Spread: Adjusting this control modifies the weighting given to each sample. This affects

the brightness of the samples.

Use GPU

The Use GPU menu has three settings. Setting the menu to Disable turns off hardware-accelerated

rendering using the graphics card in your computer. Enabled uses the hardware, and Auto uses

a capable GPU if one is available and falls back to software rendering when a capable GPU is

not available

Comments

The Comments field is used to add notes to a tool. Click in the empty field and type the text. When a

note is added to a tool, a small red square appears in the lower-left corner of the node when the full

tile is displayed, or a small text bubble icon appears on the right when nodes are collapsed. To see the

note in the Node Editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more details on scripting

nodes, please consult the Fusion scripting documentation.


Fusion Page Effects | Chapter 108 Mask Nodes

FUSION