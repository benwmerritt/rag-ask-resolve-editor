---
title: "Inputs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 375
---

# Inputs

The Texture Transform node includes a single input that is used to connect the image or material you

want to transform.

Material Input: The orange Material input accepts a 2D image or 3D material whose texture

coordinates are transformed using the controls in the Inspector.

Basic Node Setup

The Texture Transform node below is used to take in a 2D image, transform it, and output a material to

be used on 3D geometry.

A Texture Transform node transforms a texture applied to 3D geometry.

Inspector

Texture Transform controls

NOTE: Not all Wrap modes are supported by all graphics cards.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Controls Tab

The Controls tab for the Texture Transform node includes many common transform controls that are

used to transform the texture using UVW coordinates.

Translation

The U, V, W translation sliders shift the texture along U, V, and W axes.

Rotation

Rotation Order buttons set the order in which the rotation is applied. In conjunction with the buttons,

the UVW dials define the rotation around the UVW axes.

Scale

U, V, W sliders scale the texture along the UVW axes.

Pivot

U, V, W Pivot sets the reference point for rotation and scaling.

Material ID

This slider sets the numeric identifier assigned to this material. This value is rendered into the MatID

auxiliary channel if the corresponding option is enabled in the renderer.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in the following “The Common Controls” section.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

The Common Controls

Nodes that handle 3D geometry share a number of identical controls in the Inspector. This section

describes controls that are common among 3D Texture nodes.

Settings Tab

Common Settings 3D controls

The Common Settings tab can be found on most tools in Fusion. The following controls are specific

settings for 3D nodes.

Hide Incoming Connections

Enabling this checkbox can hide connection lines from incoming nodes, making a node tree appear

cleaner and easier to read. When enabled, fields for each input on a node are displayed. Dragging a

connected node from the node tree into the field hides that incoming connection line as long as the

node is not selected in the node tree. When the node is selected in the node tree, the line reappears.

Comment Tab

The Comment tab contains a single text control that is used to add comments and notes to the tool.

When a note is added to a tool, a small red dot icon appears next to the setting’s tab icon, and a text

bubble appears on the node. To see the note in the Node Editor, hold the mouse pointer over the

node for a moment. The contents of the Comments tab can be animated over ime, if required.

Scripting Tab

The Scripting tab is present on every tool in Fusion. It contains several edit boxes used to add scripts

that process when the tool is rendering. For more details on the contents of this tab, please consult the

scripting documentation.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Chapter 93

Blur Nodes

This chapter details the Blur nodes available in Fusion. The abbreviations next to

each node name can be used in the Select Tool dialog when searching for tools

and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Blur [Blur]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2059

Defocus [Dfo]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2062

Directional Blur [DrBl]���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2064

Glow [Glo]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2066

Sharpen [Shrp]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2069

Soft Glow [SGlo]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2071

Unsharp Mask [UsM]������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2074

Vari Blur [VBl]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2076

Vector Motion Blur [VMB]�������������������������������������������������������������������������������������������������������������������������������������������������������������� 2078

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2080


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Blur [Blur]

The Blur node

Blur Node Introduction

The Blur node does exactly what its name implies – it blurs the input image. This is one of the most

commonly used image-processing operations.

Inputs

The two inputs on the Blur node are used to connect a 2D image and an effect mask that can be used

to limit the blurred area.

Input: The orange input is used for the primary 2D image that is blurred.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the blur to only those pixels

within the mask. An effect mask is applied to the tool after the tool is processed.

Basic Node Setup

The Blur node, like many 2D image-processing nodes, receives a 2D image like the MediaIn1 shown

below. The output continues the node tree by connecting to another 2D image-processing node or a

Merge node.

A Blur node applied to a MediaIn1 node

Inspector

Blur controls


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

NOTE: Since a perfect Gaussian filter would require examining an infinite number of pixels,

all practical Gaussians are, of necessity, approximations. The algorithm Fusion uses is a

highly-optimized approach that has many strengths, but can create visible ringing around the

edges in certain extreme cases. This ringing appears only when blurring float-depth images

and is normally far below the limits of visibility, especially in final renders or HiQ mode, but

may appear in subsequent processing. If you experience this, selecting the Multi-box filter

may be a good choice.

Controls Tab

The Controls tab contains the primary controls necessary for customizing the blur operation, including

five filter algorithms.

Filter

The Filter menu is where you select the type of filter used to create the blur.

�Box Blur: This option is faster than the Gaussian blur but produces a lower-quality result.

�Bartlett: This option is a more subtle, anti-aliased blur filter.

�Multi-box: Multi-box uses a Box filter layered in multiple passes to approximate a Gaussian shape.

With a moderate number of passes (e.g., four), a high-quality blur can be obtained, often faster

than the Gaussian filter and without any ringing.

�Gaussian: Gaussian applies a smooth, symmetrical blur filter, using a sophisticated constant-time

Gaussian approximation algorithm.

�Fast Gaussian: Gaussian applies a smooth, symmetrical blur filter, using a sophisticated constant-

time Gaussian approximation algorithm. This mode is the default filter method.

Color Channels (RGBA)

The filter defaults to operating on R, G, B, and A channels. Selective channel filtering is possible by

clicking each channel button to make them active or inactive.

NOTE: This is not the same as the RGBA checkboxes found under the common controls.

The node takes these selections into account before it processes the image, so deselecting a

channel causes the node to skip that channel when processing, speeding up the rendering of

the effect. In contrast, the channel controls under the Common Controls tab are applied after

the node has processed.

Lock X/Y

Locks the X and Y Blur sliders together for symmetrical blurring. This is enabled by default.

Blur Size

Sets the amount of blur applied to the image. When the Lock X and Y control is deselected,

independent control over each axis is provided.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION

Clipping Mode

This option determines how edges are handled when performing domain-of-definition rendering.

This is profoundly important for nodes like Blur, which may require samples from portions of the image

outside the current domain.

�Frame: The default option is Frame, which automatically sets the node’s domain of definition

to use the full frame of the image, effectively ignoring the current domain of definition. If the

upstream DoD is smaller than the frame, the remaining area in the frame is treated as black/

transparent.

�Domain: Setting this option to Domain respects the upstream domain of definition when applying

the node’s effect. This can have adverse clipping effects in situations where the node employs a

large filter.

�None: Setting this option to None does not perform any source image clipping at all. This means

that any data required to process the node’s effect that would normally be outside the upstream

DoD is treated as black/transparent.

Blend

The Blend slider determines the percentage of the affected image that is mixed with original image. It

blends in more of the original image as the value gets closer to 0.

This control is a cloned instance of the Blend slider in the Common Controls tab. Changes made to this

control are simultaneously made to the one in the common controls.

Examples

Following is a comparison of Blur filters visualized as “cross-sections” of a filtered edge. As you can

see, Box creates a linear ramp, while Bartlett creates a somewhat smoother ramp. Multi-box and

Gaussian are indistinguishable unless you zoom in really close on the slopes. They both lead to even

smoother ramps, but as mentioned above, Gaussian overshoots slightly and may lead to negative

values if used on floating-point images.

Blur filters visualized as “cross sections” of a filtered edge

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Blur nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 93 Blur Nodes

FUSION