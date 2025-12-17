---
title: "Vector Warping Toolset"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 459
---

# Vector Warping Toolset

(Studio Version Only)

You can use the Vector Warping 2D imaging toolset below to map and warp a reference frame

to all the other frames in the sequence. This is useful in face replacements, digital makeup, sign

replacements, etc. to track and warp assets in tandem with the background. At its simplest, you:

�Apply VFX changes—make-up, face paint, scars, black eyes—on one frame,

�Ensure the areas of the reference frame are visible in the frames you are tracking,

�Add Vector Warp, set reference frame, select Generate + Texture Map and track the changes to

the sequence using optical flow.

Vector Denoise [VDn]

The Vector Denoise node

Vector Denoise Node Introduction

This tool allows for a general purpose averaging operation across neighboring frames. While similar to

temporal noise reduction, the source pixels to average are motion vector compensated.

Inputs

The Vector Denoise node includes a single orange image input.

Input: The orange image input accepts a 2D image. This image must have precomputed Vector

and Back Vector channels, either generated from an Optical Flow node or saved in EXR format

with vector channels.

Basic Node Setup

The Vector Denoise node takes the output of the Optical Flow node for the required Vector and Back

Vector channels and removes noise across multiple frames.

A Vector Denoise node using Vector and Back Vector channels from the Optical Flow node


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Inspector

The Vector Denoise Controls tab

Controls Tab

The Controls tab lets you adjust the Vector Denoise settings.

�Average: Define the temporal window in number of frames.

�Threshold: Set an upper threshold to ignore flashes and brief highlights when averaging

pixel values.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Optical Flow nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.

Vector Transform [VXf]

The Vector Transform node

Vector Transform Node Introduction

This tool allows custom transforms on the vector channel information, allowing tracking information to

be resized, rotated and translated to be applied on another image or sequence. Use this to simulate

transfer of kinetic energy, object responses and difference in material properties in a dynamic scene.

Inputs

The Vector Transform node includes an orange image input, and an attenuate mask input.

�Input: The orange image input accepts a 2D image.

�Attenuate Mask: The white input accepts a mask shape.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Basic Node Setup

The Vector Transform node takes the output of the Optical Flow node for the required Vector and

Back Vector channels and transforms vector channel information.

A Vector Transform node using Vector and Back Vector channels from the Optical Flow node

Inspector

The Vector Transform Controls tab

Controls Tab

The Controls tab lets you adjust the Vector Transform settings.

�Smooth UV: Use this to average the results with the neighboring UV values. This can be used to

smooth out anomalies and unwanted variations in the UV channels.

�Smooth Vector: Use this to smoothen vectors across neighboring frames. Useful as a pre-

processing step before a Vector Warp with texture map.

�Attenuate UV: Amplify, decrease, or zero out the warp map effect from the vector magnitudes.

This control can also decrease the strength of the UV channels.

�Attenuate Vector: Reduces the motion vector length, letting you control the amount of warping

applied from full down to nothing.

�Center X/Y: Use this control to reposition the UV channels.

�Size X/Y: Use this control to rescale the UVs.

�Use Size and Aspect: Check this box to activate the parameters below.

Size: Scales the image equally along both the X and Y axes.

Aspect: Lets you set the aspect ratio of the image.

�Angle: Adjusts the angle of the UV.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Optical Flow nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.

Vector Warp [VWp]

The Vector Warp node

Vector Warp Node Introduction

The Vector Warp node has a main image input sequence (the background) and the map input image

(a still to be warped). The output is an RGBA image and may contain extra motion vector channels (Vx,

Vy. BVx, BVy) with forward and backward tracking information for use in downstream tools.

This tool distorts a nominated reference frame or image according to the motion of the source clip.

The tool has two inputs: the Input Layer, which is for your source clip along with its motion vectors

(generated using an Optical Flow tool) and the Texture Layer. Any clip or image connected to the

Texture Layer will be warped based on the movement of the incoming vectors from the Input Layer.

For warping to occur, motion vectors need to be generated for the source clip.

It is generally expected that Vector Warp follows an Optical Flow tool, which creates the

required vectors.

Because Vector Warp uses motion vectors to follow movement in a clip, it’s particularly useful for

adding or removing elements from non-solid surfaces like fabric or skin. This tool can be used to add

or remove logos from clothing, add a scar to someone’s face, or add texture to skin

Inputs

The Vector Warp node uses two inputs.

Input: The orange image input accepts a 2D image sequence. This image must have precomputed

Vector and Back Vector channels, either generated from an Optical Flow node or saved in EXR format

with vector channels.

Texture: The green input accepts a 2D still image to be used as the texture for warping.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

Basic Node Setup

The Vector Warp node takes the output of a clip and a 2D still image and warps them together.

A Vector Warp node

Inspector

The Vector Warp Controls tab

Controls Tab

The Controls tab lets you adjust the Vector Warp settings.

�Set Frame: Uses the current frame as the reference frame. Pressing this button sets the Reference

Frame below.

�Reference Frame: Set the reference frame for the Main sequence that the Map overlay was

created for.

�Operation: Choose the operation you wish to perform.

Generate Warp:  Creates a warp map from the reference frame to the current frame, saved in the

UV channels.

Generate Warp + Map:  Creates a warp map from the reference frame to the current frame and

warps the map frame.

Apply Warp Map:  Warps the map frame from a previously generated texture map from input.

UnWarp:  Freezes the map at reference frame and reverse warps the main current frame to

resemble the reference frame.


Fusion Page Effects | Chapter 112 Optical Flow

FUSION

�Smooth UV: This will average the results with the neighboring UV values. This can be used to

smooth out anomalies and unwanted variations in the UV channels.

�Grid Overlay: Displays the warping as a viewer overlay.

�Merge Warp over BG: Displays the composited map image on the main image sequence.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Optical Flow nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.