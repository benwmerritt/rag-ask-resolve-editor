---
title: "Time Code"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 422
---

# Time Code

The Time Code only works on Text+ nodes. It sets the Styled text to become a counter based on the

current frame. This is quite useful for automating burn-ins for daily renderings.

It can be applied by right-clicking in the Styled Text field of a Text+ node and selecting Time Code.

Inspector

Time Code modifier Controls tab

Controls Tab

The Controls tab for the Time Code modifier is used to set up the time code display that is generated

by this modifier.

Hrs, Mins, Secs, Frms, Flds

Activate or deactivate these options to customize the time code display to show hours, minutes,

seconds, frames, and fields, respectively. Activating frames will only give you a plain frame counter.

Start Offset

Introduce a positive or negative offset to Fusion’s current time to match up with existing time codes.

Frames per Second

This should match with your composition’s FPS setting to provide accurate time measurement.

Drop Frame

Activate this checkbox to match the time code with footage that has drop frames—for example, certain

NTSC formats.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

The Common Controls

Nodes that generate images share a number of identical controls in the Inspector. This section

describes controls that are common among Generator nodes.

Inspector

Background node Image tab

Image Tab

The controls in this tab are used to set the resolution, color depth, and pixel aspect of the image

produced by the node.

Process Mode

Use this menu control to select the Fields Processing mode used by Fusion to render changes

to the image. The default option is determined by the Has Fields checkbox control in the Frame

Format preferences.

Global In and Out

Use this control to specify the position of this node within the project. Use Global In to specify which

frame that starts the clip and Global Out to specify which frame ends the clip (inclusive) within the

project’s Global Range.

The node will not produce an image on frames outside this range.

Use Frame Format Settings

When this checkbox is selected, the width, height, and pixel aspect of the image created by the node

will be locked to values defined in the composition’s Frame Format preferences. If the Frame Format

preferences change, the resolution of the image produced by the node will change to match. Disabling

this option can be useful to build a composition at a different resolution than the eventual target

resolution for the final render.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Width/Height

This pair of controls is used to set the Width and Height dimensions of the image to be created

by the node.

Pixel Aspect

This control is used to specify the Pixel Aspect ratio of the created images. An aspect ratio of 1:1 would

generate a square pixel with the same dimensions on either side (like a computer display monitor), and

an aspect of 0.9:1 would create a slightly rectangular pixel (like an NTSC monitor).

NOTE: Right-click on the Width, Height, or Pixel Aspect controls to display a menu listing the

file formats defined in the preferences Frame Format tab. Selecting any of the listed options

will set the width, height, and pixel aspect to the values for that format, accordingly.

Depth

The Depth drop-down menu is used to set the pixel color depth of the image created by the Creator

node. 32-bit pixels require 4X the memory of 8-bit pixels but have far greater color accuracy. Float

pixels allow high dynamic range values outside the normal 0…1 range, for representing colors that are

brighter than white or darker than black.

Source Color Space

You can use the Source Color Space menu to set the Color Space of the footage to help achieve a

linear workflow. Unlike the Gamut tool, this doesn‘t perform any actual color space conversion, but

rather adds the source space data into the metadata, if that metadata doesn‘t exist. The metadata can

then be used downstream by a Gamut tool with the From Image option, or in a Saver, if explicit output

spaces are defined there. There are two options to choose from:

�Auto: Automatically reads and passes on the metadata that may be in the image.

�Space: Displays a Color Space Type menu where you can choose the correct color

space of the image.

Source Gamma Space

Using the Curve type menu, you can set the Gamma Space of the footage and choose to remove it by

way of the Remove Curve checkbox when working in a linear workflow. There are three choices in the

Curve type menu:

�Auto: Automatically reads and passes on the metadata that may be in the image.

�Space: Displays a Gamma Space Type menu where you can choose the correct gamma

curve of the image.

�Log: Brings up the Log/Lin settings, similar to the Cineon tool.

For more information, see Chapter 99, "Film Nodes," in the DaVinci Resolve Reference Manual,

or Chapter 39 in the Fusion Reference Manual.

Remove Curve

Depending on the selected Gamma Space or on the Gamma Space found in Auto mode, the Gamma

Curve is removed from, or a log-lin conversion is performed on, the material, effectively converting it

to a linear output space.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Fast Noise Image Tab Options

The following controls are specific the Image tab in the Fast Noise Node.

Mask Map Inputs

These external connections allow you to use masks to control the value of the Noise Detail and

Brightness controls individually for each pixel. This can allow some interesting and creative effects.

Noise Detail Map

A soft-edged mask connected to the Noise Detail Map will give a flat noise map (zero detail) where the

mask is black, and full detail where it is white, with intermediate values smoothly reducing in detail. It is

applied before any gradient color mapping. This can be very helpful for applying maximum noise detail

in a specific area, while smoothly falling off elsewhere.

Noise Brightness Map

A mask connected to this input can be used to control the noise map completely, such as boosting it

in certain areas, combining it with other textures, or if Detail is set to 0, replacing the Perlin Noise map

altogether.

Settings Tab

The Settings Tab in the Inspector can be found on every tool in the Color category. The Settings

controls are even found on third-party Color-type plugin tools. The controls are consistent and work

the same way for each tool, although some tools do include one or two individual options, which are

also covered here.

Common Generator settings


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Blend

The Blend control is used to blend between the tool’s original image input and the tool’s final modified

output image. When the blend value is 0.0, the outgoing image is identical to the incoming. Normally,

this will cause the tool to skip processing entirely, copying the input straight to the output.

Process When Blend Is 0.0

The tool is processed even when the input value is zero. This can be useful if processing of this node

is scripted to trigger another task, but the value of the node is set to 0.0.

Red/Green/Blue/Alpha Channel Selector

These four buttons are used to limit the effect of the tool to specified color channels. This filter is often

applied after the tool has been processed.

For example, if the red button on a Blur tool is deselected, the blur will first be applied to the image,

and then the red channel from the original input will be copied back over the red channel of the result.

There are some exceptions, such as tools for which deselecting these channels causes the tool to

skip processing that channel entirely. Tools that do this will generally possess a set of identical RGBA

buttons on the Controls tab in the tool. In this case, the buttons in the Settings and the Controls tabs

are identical.

Apply Mask Inverted

Enabling the Apply Mask Inverted option inverts the complete mask channel for the tool. The mask

channel is the combined result of all masks connected to or generated in a node.

Multiply by Mask

Selecting this option will cause the RGB values of the masked image to be multiplied by the mask

channel’s values. This will cause all pixels of the image not in the mask (i.e., set to 0) to become black/

transparent.

Use Object/Use Material (Checkboxes)

Some 3D software can render to file formats that support additional channels. Notably, the EXR file

format supports Object ID and Material ID channels, which can be used as a mask for the effect. These

checkboxes determine whether the channels will be used if present. The specific Material ID or Object

ID affected is chosen using the next set of controls.

Correct Edges

This checkbox appears only when the Use Object or Use Material checkboxes are selected. It toggles

the method used to deal with overlapping edges of objects in a multi-object image. When enabled,

the Coverage and Background Color channels are used to separate and improve the effect around

the edge of the object. If this option disabled (or no Coverage or Background Color channels are

available), aliasing may occur on the edge of the mask.

For more information see Chapter 78, "Understanding Image Channels," in the DaVinci

Resolve Reference Manual, or Chapter 18 in the Fusion Reference Manual.

Object ID/Material ID (Sliders)

Use these sliders to select which ID will be used to create a mask from the object or material channels

of an image. Use the Sample button in the same way as the Color Picker: to grab IDs from the image

displayed in the view. The image or sequence must have been rendered from a 3D software package

with those channels included.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Motion Blur

�Motion Blur: This toggles the rendering of Motion Blur on the tool. When this control is toggled

on, the tool’s predicted motion is used to produce the motion blur caused by the virtual camera’s

shutter. When the control is toggled off, no motion blur is created.

�Quality: Quality determines the number of samples used to create the blur. A quality setting of 2

will cause Fusion to create two samples to either side of an object’s actual motion. Larger values

produce smoother results but increase the render time.

�Shutter Angle: Shutter Angle controls the angle of the virtual shutter used to produce the motion

blur effect. Larger angles create more blur but increase the render times. A value of 360 is the

equivalent of having the shutter open for one whole frame exposure. Higher values are possible

and can be used to create interesting effects.

�Center Bias: Center Bias modifies the position of the center of the motion blur. This allows the

creation of motion trail effects.

�Sample Spread: Adjusting this control modifies the weighting given to each sample. This affects

the brightness of the samples.

Use GPU

The user GPU menu has three settings. Setting the menu to Disable turns off hardware-accelerated

rendering using the graphics card in your computer. Enabled uses the hardware, and Auto uses

a capable GPU if one is available and falls back to software rendering when a capable GPU is

not available

Comments

The Comments field is used to add notes to a tool. Click in the field and type the text. When a note

is added to a tool, a small red square appears in the lower-left corner of the node when the full tile is

displayed, or a small text bubble icon appears on the right when nodes are collapsed. To see the note

in the Node Editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more details on scripting

nodes, please consult the Fusion scripting documentation.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION