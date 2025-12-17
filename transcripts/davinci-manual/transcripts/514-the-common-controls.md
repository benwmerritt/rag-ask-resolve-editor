---
title: "The Common Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 514
---

# The Common Controls

Nodes that handle USD operations share several identical controls in the Inspector. This section

describes controls that are common among USD nodes.

Transform Tab

The Transform tab can be found in the Inspector in most USD nodes. The controls are the same as the

uTransform node, which can be applied separately.

Translation

Transform controls are used to position the USD shape in 3D space.

Rotation Order

Use these buttons to select the order used to apply the rotation along each axis of the object. For

example, XYZ would apply the rotation to the X-axis first, followed by the Y-axis, and then the Z-axis.

Rotation

Use these controls to rotate the shape around its pivot point. If the Use Target checkbox is selected,

then the rotation is relative to the position of the target; otherwise, the global axis is used.

Pivot

A pivot point is the point around which an object rotates. Normally, an object rotates around its own

center, which is considered to be a pivot of 0,0,0. These controls can be used to offset the pivot from

the center.

Scale

If the Lock X/Y/Z checkbox is checked, a single scale slider is shown. This adjusts the overall size of

the object. If the Lock checkbox is unchecked, individual X, Y, and Z sliders are displayed to allow

scaling in any dimension.

Settings Tab

The Settings tab in the Inspector can be found on every tool in the USD category. The controls are

consistent and work the same way for each tool.

Hide Incoming Connections

Enabling this checkbox can hide connection lines from incoming nodes, making a node tree appear

cleaner and easier to read. When enabled, empty fields for each input on a node will be displayed

in the Inspector. Dragging a connected node from the node tree into the field will hide that incoming

connection line as long as the node is not selected in the node tree. When the node is selected in the

node tree, the line will reappear.

Comments

The Comments field is used to add notes to a tool. Click in the empty field and type the text. When a

note is added to a tool, a small red square appears in the lower-left corner of the node when the full

tile is displayed, or a small text bubble icon appears on the right when nodes are collapsed. To see the

note in the Node Editor, hold the mouse pointer over the node to display the tooltip.

Scripts

Three Scripting fields are available on every tool in Fusion from the Settings tab. They each contain

edit boxes used to add scripts that process when the tool is rendering. For more details on scripting

nodes, please consult the Fusion scripting documentation.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Chapter 122

VR Nodes

This chapter details the Virtual Reality (VR) nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

VR Nodes����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2870

Fusion VR 180 Support (Studio Version Only)���������������������������������������������������������������������������������������������������������������������� 2871

Lat Long Patcher [LLP]��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2871

Pano Map [PaM]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2873

Spherical Camera [3SC]����������������������������������������������������������������������������������������������������������������������������������������������������������������� 2875

Spherical Stabilizer��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2875

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2878


Fusion Page Effects | Chapter 122 VR Nodes

FUSION

VR Nodes

You can create and fix spherical (360°) video, often described as Virtual Reality, or VR, using Fusion’s

set of VR nodes. Dome productions, planetariums, and other special-venue theaters have utilized the

flexibility of Fusion and its 3D system to produce and deliver special content for years.

The equirectangular (lat-long) format often used for 360° video is similar to how a globe is represented

by a flat world map, with the poles at the top and bottom edges of the image and the forward

viewpoint at the center.

TIP: You can create stereo VR using two stacked Lat Long images, one for each eye.

A VR Sphere displayed in the Node Editor and Fusion’s 3D viewer


Fusion Page Effects | Chapter 122 VR Nodes

FUSION

Fusion supports several common spherical image formats and can easily convert

between them.

VCross and HCross: VCross and HCross are the six square faces of a cube laid out in a cross,

vertically or horizontally, with the forward view in the center of the cross in a 3:4 or 4:3 image.

VStrip and HStrip: VStrip and HStrip are the six square faces of a cube laid vertically or

horizontally in a line, ordered as Left, Right, Up, Down, Back, Front (+X, -X, +Y, -Y, +Z, -Z)

in a 1:6 or 6:1 image.

LatLong: LatLong is a single 2:1 image in an equirectangular mapping.

You can display both spherical video and live 3D scenes from the comp directly to headsets,

including those from Oculus Rift and HTC Vive.

Fusion’s “Fix it in post” tools for VR make it easy to perform several important tasks that are

common in these types of productions.

Fusion VR 180 Support (Studio Version Only)

A number of Fusion’s existing VR tools now support 180-degree angle of view. The 180-degree

VR format allows you to produce immersive content and simplifies the production process for VR

experiences by focusing on a forward-facing perspective.

Lat Long Patcher [LLP]

The Lat Long Patcher node

NOTE: The VR category and Lat Long node are available only in Fusion Studio and DaVinci

Resolve Studio.

Lat Long Patcher Node Introduction

Equirectangular stitched images often need patches, paintwork, or other VFX applied. The Lat Long

Patcher extracts and de-warps a section of a lat-long (equirectangular) image to be treated, and can

warp and merge fixes back over the original. You can quickly pick a section of the spherical image

to patch or paint, and then apply it back to the original image. Note that matching rotations are used

in both Extract and Apply modes, allowing a node’s operation to be easily reversed by a copy or

instance with the same rotation settings.


Fusion Page Effects | Chapter 122 VR Nodes

FUSION

Input

The Lat Long Patcher node includes two inputs. The orange input accepts a 2D image in an

equirectangular format, where the X-axis represents 0–360 degrees longitude, and the Y-axis

represents –90 to +90 degrees latitude. The effect mask input is provided, although rarely used

on VR nodes.

Image Input: The orange image input accepts a equirectangular (lat-long) 2D RGBA image.

Effect Mask: The effect mask input is provided, although rarely used on VR nodes.

Basic Node Setup

The Loader node connects to the input on a Lat Long Patcher node. The output of a Lat Long Patcher

node is set to Extract. It is then connected to whatever image-processing operation is required. A

second Lat Long Patcher node set to Apply takes an input from the processed extraction and merges

it over the top of the original source.

Two Lat Long Patchers used to repair a section

Inspector

The Lat Long Patcher Controls tab

Controls Tab

The Controls tab is used to extract and later reapply a section from an equirectangular image. Rotation

controls allow you to select the exact portion you need to repair.


Fusion Page Effects | Chapter 122 VR Nodes

FUSION

Mode

�Extract: Pulls a de-warped 90-degree square image from the equirectangular image.

�Apply: Warps and merges a 90-degree square image over the equirectangular image. Because

the square image’s alpha is used, this allows, for example, paint strokes or text drawn over a

transparent black background to be applied to the original equirectangular image, avoiding any

double-filtering from de-warping and re-warping the original.

�Apply180: Use to extract and apply a patch to a VR180 image. This gives control to apply

traditional 2D effects, like paint, to a 180 distorted clip.

Rotation Order

These buttons choose the ordering of the rotations around each axis. For example, XYZ rotates first

around the X axis (pitch/tilt), then around the Y axis (pan/yaw), and then around the Z axis (roll). Any of

the six possible orderings can be chosen.

Rotation

These dials rotate the spherical image around each of the X, Y, and Z axes, offering independent

control over pitch/tilt, pan/yaw, and roll, respectively.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other VR nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.