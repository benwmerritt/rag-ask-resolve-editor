---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 407
---

# Inspector

TV node controls

Controls Tab

The Controls tab is the first of three tabs used to customize the analog TV distortion. The Controls tab

modifies the scan lines and image distortion of the effect.

Scan Lines

This slider is used to emulate the interlaced look by dropping lines out of the image. Setting it to black,

with a transparent Alpha, drops a line. A value of 1 (default) drops every second line. A value of 2

shows one line, and then drops the second and third and repeats. A value of zero turns off the effect.

Horizontal

Use this slider to apply a simple Horizontal offset to the image.

Vertical

Use this slider to apply a simple Vertical offset to the image.

Skew

This slider is used to apply a diagonal offset to the image. Positive values skew the image to the

top left. Negative values skew the image to the top right. Pixels pushed off frame wrap around and

reappear on the other side of the image.

Amplitude

The Amplitude slider can be used to introduce smooth sine wave-type deformation to the edges

of the image. Higher values increase the intensity of the deformation. Use the Frequency control to

determine how often the distortion is repeated.

Frequency

The Frequency slider sets the frequency of the sine wave used to produce distortion along the edges

of the image when the amplitude control is greater than 1.

Offset

Use Offset to adjust the position of the sine wave, causing the deformation applied to the image via

the Amplitude and Frequency controls to see across the image.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

The TV Noise tab

Noise Tab

The Noise tab is the second of three tabs used to customize the analog TV distortion. The Noise tab

modifies the noise in the image to simulate a weak analog antenna signal.

Power

Increase the value of this slider above 0 to introduce noise into the image. The higher the value, the

stronger the noise.

Size

Use this slider to scale the noise map larger.

Random

If this thumbwheel control is set to 0, the noise map is static. Change the value over time to cause the

static to change from frame to frame.

The TV Roll Bar tab

Roll Bar Tab

The Roll Bar tab is the third of three tabs used to customize the analog TV distortion. The Roll Bar tab

animates the bar.

Bar Strength

At the default value of 0, no bar is drawn. The higher the value, the darker the area covered by the

bar becomes.

Bar Size

Increase the value of this slider to make the bar taller.

Bar Offset

Animate this control to scroll the bar across the screen.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Common Controls

Settings Tab

The Settings tab controls are common to all Effect nodes, so their descriptions can be found in the

following “The Common Controls” section.

The Common Controls

Effect nodes share several identical controls in the Inspector. This section describes controls that are

common among Effect nodes.

Inspector

The Common Effects Settings tab

Settings Tab

The Settings tab in the Inspector can be found on every tool in the Effects category. The Settings

controls are even found on third-party Effects-type plugin tools. The controls are consistent and work

the same way for each tool, although some tools do include one or two individual options, which are

also covered here.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming image. This

causes the tool to skip processing entirely, copying the input straight to the output.

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This is useful when this node is scripted to

trigger another task, but the blend is set to 0.0.

Red/Green/Blue/Alpha Channel Selector

These four buttons are used to limit the effect of the tool to specified color channels. This filter is often

applied after the tool has been processed.

For example, if the red button on a Blur tool is deselected, the blur is first applied to the image, and

then the red channel from the original input is copied back over the red channel of the result.

There are some exceptions, such as tools for which deselecting these channels causes the tool to skip

processing that channel entirely. Tools that do this possess a set of like RGBA buttons on the Controls

tab in the tool. In this case, the buttons in the Settings and the Control tabs are identical.

Apply Mask Inverted

Enabling the Apply Mask Inverted option inverts the complete mask channel for the tool. The mask

channel is the combined result of all masks connected to or generated in a node.

Multiply by Mask

Selecting this option causes the RGB values of the masked image to be multiplied by the mask

channel’s values. This causes all pixels of the image not included in the mask (i.e., set to 0) to become

black/transparent.

Use Object/Use Material (Checkboxes)

Some 3D software can render to file formats that support additional channels. Notably, the EXR

file format supports Object and Material ID channels, which can be used as a mask for the effect.

These checkboxes determine whether the channels are used, if present. The specific Material ID or

Object ID affected is chosen using the next set of controls.

Correct Edges

This checkbox appears only when the Use Object or Use Material checkboxes are selected. It toggles

the method used to deal with overlapping edges of objects in a multi-object image. When enabled,

the Coverage and Background Color channels are used to separate and improve the effect around

the edge of the object. If this option is disabled (or no Coverage or Background Color channels are

available), aliasing may occur on the edge of the mask.

For more information on coverage and background channels, see Chapter 78, “Understanding

Image Channels,” in the DaVinci Resolve Reference Manual, or Chapter 18 in the Fusion

Reference Manual.

Object ID/Material ID (Sliders)

Use these sliders to select which ID is used to create a mask from the object or material channels of

an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the view. The image or sequence must have been rendered from a 3D software package

with those channels included.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION

Clipping Mode

This option determines how the domain of definition rendering handles edges. The Clipping mode

is most important when blur or softness is applied, which may require samples from portions of the

image outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition.

If the upstream DoD is smaller than the frame, the remaining area in the frame is treated as

black/transparent.

�None: Setting this option to None does not perform any source image clipping. Any data required

to process the node’s effect that would usually be outside the upstream DoD is treated as

black/transparent.

Use GPU

The Use GPU menu has three settings. Setting the menu to Disable turns off hardware-accelerated

rendering using the graphics card in your computer. Enabled uses the hardware. Auto uses a capable

GPU if one is available and falls back to software rendering when a capable GPU is not available

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

Comments

The Comments field is used to add notes to a tool. Click in the empty field and type the text. When a

note is added to a tool, a small red square appears in the lower-left corner of the node when the full

tile is displayed, or a small text bubble icon appears on the right when nodes are collapsed. To see the

note in the Node Editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more details on scripting

nodes, please consult the Fusion scripting documentation.


Fusion Page Effects | Chapter 98 Effect Nodes

FUSION