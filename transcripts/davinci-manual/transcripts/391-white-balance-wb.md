---
title: "White Balance [WB]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 391
---

# White Balance [WB]

The White Balance node

White Balance Node Introduction

The White Balance node can be used to automatically remove color casts in the image caused by the

incorrect setup of a camera or bad lighting conditions.

Correction can be done by selecting a color temperature or by choosing a neutral color from the

original image that exhibits the color cast to be corrected.

IMPORTANT: When picking neutral colors using the Custom method, make sure you are

picking from the source image, not the results of the White Balance node. This ensures that

the image doesn’t change while you are still picking, and that the White Balance node gets an

accurate idea of the original colors it needs to correct.

Inputs

The White Balance node includes two inputs: one for the main image and the other for an effect mask

to limit the area where the white balance is applied.

Input: This orange input is the only required connection. It connects a 2D image for the white balance.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines,

basic primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input

limits the white balance to only those pixels within the mask. An effect mask is applied to the tool after

it is processed.

Basic Node Setup

The White Balance node, like many 2D image-processing nodes, receives a 2D image like the

MediaIn1 shown below. The output continues the node tree by connecting to another 2D image-

processing node or a Merge node.

A White Balance node applied to a MediaIn1 node


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Inspector

White Balance controls

Balance Tab

Space

Use this menu to select the color space of the source image, if it is known. This can make the

correction more accurate since the node can take the natural gamma of the color space into account

as part of the correction. If the color space that the image uses is unknown, leave this menu at its

default value.

Method

The White Balance node can operate using one of two methods: a Custom method or a color

Temperature method.

�Custom: The Custom method requires the selection of a pixel from the scene that should have

been pure gray. The node uses this information to calculate the color correction required to

convert the pixel so that it actually is gray. When the correction is applied without an effect

mask connected and the LockBlack/Mid/White checkbox enabled, the node white balances the

entire shot.

�Temperature: The color Temperature method requires that the actual color temperature of the

shot be specified.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Lock Black/Mid/White

This checkbox locks the Black, Midtones, and White points together so that the entire image is

affected equally. Unchecking the control provides individual controls for white balancing each range

separately. This control affects both methods equally.

Black/Mid/White Reference

These controls appear only if the Custom method is selected. They are used to select a color from a

pixel in the source image. The White Balance node color corrects the image so that the selected color

is transformed to the color set in the Result Color Picker below. Generally, this is gray. A color that is

supposed to be pure gray but is not truly gray for one reason or another should be selected.

If the Lock Black/Mid/White checkbox is deselected, different references can be selected for each

color range.

For example, try to select a pixel for the black and white references that are not clipped in any of the

color channels. In the high end, an example would be a pixel that is light pink with values of 255, 240,

240. The pixel is saturated/clipped in the red, although the color is not white. Similarly, a really dark

blue-gray pixel might be 0, 2, 10. It is clipped in red as well, although it is not black.

Neither example would be a good choice as a reference pixel because there would not be enough

headroom left for the White Balance node.

Black/Mid/White Result

These controls appear only if the Custom method is selected. They are used to select the color that

the node uses to balance the reference color. This generally defaults to pure, midrange gray.

If the Lock Black/Mid/White checkbox is deselected, different results can be selected for each

color range.

White Balance Temperature controls

Temperature Reference

When the Method menu is set to Temperature, the Temperature reference control is used to set the

color temperature of the source image. If the Lock Black/ Mid/White checkbox is deselected, different

references can be selected for each color range.

Temperature Result

Use this control to set the target color temperature for the image. If the Lock Black/Mid/White

checkbox is deselected, different results can be selected for each color range.

Use Gamma

This checkbox selects whether the node takes the gamma of the image into account when applying

the correction, using the default gamma of the color space selected in the Space menu at the top

of the tab.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

White Balance range tab

Ranges Tab

The Ranges tab can be used to customize the range of pixels in the image considered to be shadows,

midtones, and highlights by the node.

Spline Display

The ranges are selected by manipulating the spline handles. There are four spline points, each with

one Bézier handle. The two handles at the top represent the start of the shadow and highlight ranges,

whereas the two at the bottom represent the end of the range. The Bézier handles are used to control

the falloff.

The midtones range has no specific controls since its range is understood to be the space between

the shadow and the highlight ranges.

The X and Y text controls below the Spline display can be used to enter precise positions for the

selected Bézier point or handle.

Preset Simple/Smooth Ranges

These two buttons can be used to return the spline ranges to either Smooth (default) or Simple

(linear) settings.

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

The Common Controls

Nodes that handle Color adjustment operations share several identical controls in the Inspector. This

section describes controls that are common among color nodes.

Inspector

Color Settings Inspector

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Color category. The Settings

controls are even found on third-party color type plugin tools. The controls are consistent and work

the same way for each tool, although some tools do include one or two individual options that are also

covered here.

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image.

Normally, this causes the tool to skip processing entirely, copying the input straight to the output.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This can be useful if processing of this node

is scripted to trigger another task, but the value of the node is set to 0.0.

Red/Green/Blue/Alpha Channel Selector

These four buttons are used to limit the effect of the tool to specified color channels. This filter is often

applied after the tool has been processed.

For example, if the red button on a blur tool is deselected, the blur is first applied to the image, and

then the red channel from the original input is copied back over the red channel of the result.

There are some exceptions, such as tools for which deselecting these channels causes the tool to

skip processing that channel entirely. Tools that do this generally possess a set of identical RGBA

buttons on the Controls tab in the tool. In this case, the buttons in the Settings and the Controls tabs

are identical.

Apply Mask Inverted

Enabling the Apply Mask Inverted option inverts the complete mask channel for the tool. The mask

channel is the combined result of all masks connected to or generated in a node.

Multiply by Mask

Selecting this option causes the RGB values of the masked image to be multiplied by the mask

channel’s values. This causes all pixels not included in the mask (i.e., set to 0) to become black/

transparent.

Use Object/Use Material (Checkboxes)

Some 3D software can render to file formats that support additional channels. Notably, the EXR file

format supports Object and Material ID channels, which can be used as a mask for the effect. These

checkboxes determine whether the channels are used, if present. The specific Material ID or Object ID

affected is chosen using the next set of controls.

Correct Edges

This checkbox appears only when the Use Object or Use Material checkboxes are selected. It toggles

the method used to deal with overlapping edges of objects in a multi-object image. When enabled,

the Coverage and Background Color channels are used to separate and improve the effect around

the edge of the object. If this option disabled (or no Coverage or Background Color channels are

available), aliasing may occur on the edge of the mask.

For more information on the Coverage and Background Color channels, see Chapter 78,

“Understanding Image Channels,” in the DaVinci Resolve Reference Manual, or Chapter 18

in the Fusion Reference Manual.

Object ID/Material ID (Sliders)

Use these sliders to select which ID is used to create a mask from the object or material channels of

an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the viewer. The image or sequence must have been rendered from a 3D software

package with those channels included.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Clipping Mode

This option determines how edges are handled when performing domain of definition rendering.

This is mostly important for nodes like Blur, which may require samples from portions of the image

outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition. If

the upstream DoD is smaller than the frame, the remaining area in the frame is treated as

black/transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that would normally be outside the upstream

DoD is treated as black/transparent.

Use GPU

The Use GPU menu has three settings. Setting the menu to Disable turns off hardware-accelerated

rendering using the graphics card in your computer. Enabled uses the hardware. Auto uses a capable

GPU if one is available and falls back to software rendering when a capable GPU is not available.

Motion Blur

�Motion Blur: This toggles the rendering of Motion Blur on the tool. When this control is toggled

on, the tool’s predicted motion is used to produce the motion blur caused by the virtual camera’s

shutter. When the control is toggled off, no motion blur is created.

�Quality: Quality determines the number of samples used to create the blur. A quality setting of

2 causes Fusion to create two samples to either side of an object’s actual motion. Larger values

produce smoother results but increase the render time.

�Shutter Angle: Shutter Angle controls the angle of the virtual shutter used to produce the motion

blur effect. Larger angles create more blur but increase the render times. A value of 360 is the

equivalent of having the shutter open for one whole frame exposure. Higher values are possible

and can be used to create interesting effects.

�Center Bias: Center Bias modifies the position of the center of the motion blur. This allows the

creation of motion trail effects.

�Sample Spread: Adjusting this control modifies the weighting given to each sample. This affects

the brightness of the samples.

Comments

The Comments field is used to add notes to a tool. Click in the field and type the text. When a note

is added to a tool, a small red square appears in the lower-left corner of the node when the full tile is

displayed, or a small text bubble icon appears on the right when nodes are collapsed. To see the note

in the Node Editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more details on scripting

nodes, please consult the Fusion scripting documentation.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION