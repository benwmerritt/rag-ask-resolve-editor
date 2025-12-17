---
title: "Pano Map [PaM]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 515
---

# Pano Map [PaM]

The Pano Map node

NOTE: The VR category and Pano Map node are available only in Fusion Studio and DaVinci

Resolve Studio.

Pano Map Node Introduction

The Pano Map node converts images from one spherical layout to another, such as from a cube

map to an equirectangular format. The node can also perform rotations of the spherical images

when converting.


Fusion Page Effects | Chapter 122 VR Nodes

FUSION

Input

The Pano Map node includes two inputs. The orange input accepts a 2D image in an equirectangular,

cube map or other spherical formats. The effect mask input is provided, although rarely used

on VR nodes.

Image Input: The orange Image input accepts a spherical formatted 2D RGBA image that gets

converted to another spherical format.

Effect Mask: The effect mask input is provided, although rarely used on VR nodes.

Basic Node Setup

In the example below, a Loader node containing a Lat Long image connects to the input on a

Pano Map node. The Pano Map node is used to convert the image to an H-Cross format. It is then

connected to whatever image-processing operation is required.

A Pano Map used to convert from one VR format to another

Inspector

The Pano Map Controls tab

Controls Tab

The Controls tab is used to determine the format of the input image and the desired output format.

From/To

�Auto: Auto detects the incoming image layout from the metadata and image frame aspect.

�VCross and HCross: VCross and HCross are the six square faces of a cube laid out in a cross,

vertically or horizontally, with the forward view in the center of the cross in a 3:4 or 4:3 image.

�VStrip and HStrip: VStrip and HStrip are the six square faces of a cube laid vertically or

horizontally in a line, ordered as Left, Right, Up, Down, Back, Front (+X, -X, +Y, -Y, +Z, -Z)

in a 1:6 or 6:1 image.

�LatLong: LatLong is a single 2:1 image in equirectangular mapping.

�VR 180 is a 1:1 180 degree stereoscopic image.


Fusion Page Effects | Chapter 122 VR Nodes

FUSION

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

Spherical Camera [3SC]

The Spherical Camera node

Spherical Camera Node Introduction

The Spherical Camera is not located in the VR category of the Effects Library but in the 3D category.

However, it is commonly used in creating and fixing VR content, so it is referenced here. The Spherical

Camera allows the 3D Renderer node to output an image covering all viewing angles, laid out in

several different formats. This image may be used, for example, as a skybox texture or reflection map

or viewed in a VR headset. The Image Width setting in the 3D Renderer sets the size of each square

cube face so that the resulting image may be a multiple of this size horizontally and vertically.

For more detail on the Spherical Camera node, see Chapter 89, "3D Nodes," in the

DaVinci Resolve Reference Manual or Chapter 29, in the Fusion Reference Manual.

Spherical Stabilizer

The Spherical Stabilizer node

NOTE: The VR category and Spherical Stabilizer node are available only in Fusion Studio and

DaVinci Resolve Studio.


Fusion Page Effects | Chapter 122 VR Nodes

FUSION

Spherical Stabilizer Node Introduction

VR live action often uses handheld cameras, causing shaky footage to be a common problem. The

Spherical Stabilizer node automatically identifies and tracks visible features in the footage, and then

analyzes their movement to identify pan, tilt, and roll rotations. After tracking, it is then possible to

smooth out or stabilize the rotation of the footage.

Inputs

The Spherical Stabilizer node has a single orange input.

Image: This orange image input node requires an image in a spherical layout, which can be any of Lat

Long (2:1 equirectangular), VR180, Horizontal/Vertical Cross, or Horizontal/Vertical Strip.

Basic Node Setup

In the example below, a 2:1 Lat Long image is connected to the input of the Spherical Stabilizer node.

Once the image is stabilized, the output of the Spherical Stabilizer node is a steadied clip.

Spherical Stabilizer set up to steady a 2:1 Lat Long clip

Inspector

The Spherical Stabilizer Controls tab

Controls Tab

The Controls tab contains parameters to initiate the tracking and modify the results for

stabilization or smoothing.

Reject Dominant Motion Outliers While Tracking

With this control activated (the default setting), features that move contrary to the majority of other

features are ignored. This helps ignore the movement of subjects in the shot, preferring stable and

consistent markers from the surrounding environment.


Fusion Page Effects | Chapter 122 VR Nodes

FUSION

Track Controls

These buttons initiate tracking and analysis of the shot. Be aware that the reference frame used for

stabilization is set to the first frame tracked.

�Track Backward from End Frame starts tracking backward from the end of the current render range.

�Track Backward from Current Time starts tracking backward from the current frame.

�Stop ceases tracking, preserving all results so far.

�Track Forward from Current Time starts tracking forward from the start of the current render range.

�Track Forward from Start Frame starts tracking forward from the current time.

Append to Track

�Replace causes the Track Controls to discard any previous tracking results and replace them with

the newly-created track.

�Append adds the new tracking results to any earlier tracks.

Stabilization Strength

This control varies the amount of smoothing or stabilization applied, from 0.0 (no change) to

1.0 (maximum).

Smoothing

The Spherical Stabilizer node can eliminate all rotation from a shot, fixing the forward viewpoint

(Still mode, 0.0) or gently smooth out any panning, rolling, or tilting to increase viewer comfort (Smooth

mode, 1.0). This slider allows either option or anything in between.

Offset Rotation

Often a shot is not entirely level and needs the horizon to be realigned, or perhaps a desired pan

should be reintroduced after fully stabilizing the shot. The Offset Rotation controls allow additional

manual control of the Spherical Stabilizer’s rotation of the footage, for pitch/tilt (X), pan/yaw (Y),

and roll (Z), respectively. Rotation is always performed in the order X, Y, Z.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other VR nodes. These common controls are

described in detail in the following “The Common Controls” section.


Fusion Page Effects | Chapter 122 VR Nodes

FUSION