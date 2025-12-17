---
title: "Compositing"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 340
---

# Compositing

The pMerge node is a simple way to combine multiple emitters so that different types of particles work

together to create a sophisticated result. The pMerge node has no parameters; you simply connect

emitters to it, and they’re automatically combined.

Rendering

The pRender node is required whether you’re connecting a particle system’s output to a 2D Merge

node or to a Merge3D node for integration into a 3D scene. Along with the pEmitter node, this is the

only other node that’s absolutely required to create a particle system.

�Controls: The main controls that let you choose whether to output 2D or 3D image data, and

whether to add blur or glow effects to the particle systems, along with a host of other details

controlling how particles will be rendered.

�Scene: These controls let you transform the overall particle scene all at once.

�Grid: The grid is a helpful, non-rendering guide used to orient 2D particles in 3D space. The grid

is never output in renders. The width, depth, number of lines, and grid color can be set using the

controls found in this tab.

�Image: Controls the output of the pRender node, with controls over the process mode, resolution,

and color space settings of the output.

Example Particle Systems

The Templates category in the Inspector in the Fusion page of DaVinci Resolve or in the Bins window

in Fusion Studio includes over 20 different examples of particle systems creating a variety of effects.

One of the best ways of learning how to create and customize particle systems is to open these and

investigate how they’re made.

Different particle system presets in the Templates category of the Bins window in Fusion Studio


Fusion Fundamentals | Chapter 87 Particle Systems

FUSION

Simply drag and drop any of the particle presets into the Node Editor, load the last node into the

viewer, and you’ll see how things are put together.

The Blowing Leaves preset from the Templates category


Fusion Fundamentals | Chapter 87 Particle Systems

FUSION

Chapter 88

Optical Flow and

Stereoscopic Nodes

This chapter covers the numerous stereoscopic and optical flow‑based nodes

available in Fusion and their related workflows.

Contents

Overview������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1855

Stereoscopic Overview�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1855

Optical Flow Overview��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1855

Toolset Overview�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1856

Working with Aux Deep Channels��������������������������������������������������������������������������������������������������������������������������������������������� 1856

Optical Flow Workflows������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1857

OpticalFlow�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1857

TimeSpeed, TimeStretcher������������������������������������������������������������������������������������������������������������������������������������������������������������ 1858

SmoothMotion�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1858

Repair Frame, Tween������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1858

Advanced Optical Flow Processing������������������������������������������������������������������������������������������������������������������������������������������� 1858

Stereoscopic Workflows����������������������������������������������������������������������������������������������������������������������������������������������������������������� 1859

Stereo Camera������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1859

Stereo Materials����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1860

Disparity�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1860

NewEye, StereoAlign������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1860

DisparityToZ, ZToDisparity�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1861

Separate vs. Stack������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1861

Setting Up Stereo in the Node Editor��������������������������������������������������������������������������������������������������������������������������������������� 1861

About the Disparity Channel�������������������������������������������������������������������������������������������������������������������������������������������������������� 1862

Viewing of Disparity and Vector Channels��������������������������������������������������������������������������������������������������������������������������� 1862


Fusion Fundamentals | Chapter 88 Optical Flow and Stereoscopic Nodes

FUSION

Overview

Fusion includes 3D stereoscopic and optical flow-based nodes, which can work together or

independently of each other to create, repair, and enhance 3D stereoscopic shots.

Stereoscopic comp displayed in the viewers.

Stereoscopic Overview

All stereoscopic features are fully integrated into Fusion’s 3D environment. Stereoscopic images can

be created using a single camera, which supports eye separation and convergence distance, and a

Renderer 3D for the virtual left and right eye. It is also possible to combine two different cameras for a

stereo camera rig.

Stereoscopic nodes can be used to solve 3D stereoscopic shooting issues, like 3D rig misalignment,

image mirror polarization differences, camera timing sync issues, color alignment, convergence, and

eye separation issues. The stereo nodes can also be used for creating depth maps.

Optical Flow Overview

Optical Flow analyzes the motion in a clip and generates motion vectors between neighboring frames.

It generates X and Y vectors from the previous frame to the current frame (Back Vectors) and to the

next frame in sequence (Forward Vectors). Once calculated, optical flow data can be used by other

nodes to create smooth slow motion and variable retiming of clips, repair missing frames, and even

correct disparity in stereo 3D clips.

Stereo and Optical Flow Best Practices��������������������������������������������������������������������������������������������������������������������������������� 1863

Semi-Transparent Objects�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1863

Motion Blur��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1863

Depth of Field��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1863

Where to Calculate Disparity and Optical Flow?����������������������������������������������������������������������������������������������������������������� 1863

Cropping the Source������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1864

Nodes with Multiple Outputs�������������������������������������������������������������������������������������������������������������������������������������������������������� 1864

Picking from Aux Channels������������������������������������������������������������������������������������������������������������������������������������������������������������ 1864

Vector and Disparity Channels���������������������������������������������������������������������������������������������������������������������������������������������������� 1864


Fusion Fundamentals | Chapter 88 Optical Flow and Stereoscopic Nodes

FUSION

NOTE: The stereoscopic nodes in the Fusion page work independently of the stereoscopic

tools in the other DaVinci Resolve pages.

Toolset Overview

Here is an overview of the available nodes.

Optical Flow Nodes

�Optical Flow > OpticalFlow: Analyzes motion between neighboring frames in a sequence to

generate motion vectors, which can then be used by other nodes for retiming, motion blur, and

other effects.

�Miscellaneous > TimeSpeed: Retimes a clip at a constant speed using Flow Interpolation mode.

�Miscellaneous > TimeStretcher: Retimes a clip at variable speeds using Flow Interpolation mode.

�Optical Flow > RepairFrame: Generates a new frame using the motion vectors between two

neighboring frames.

�Optical Flow > SmoothMotion: Smoothes the color or aux channels using motion vectors.

�Optical Flow > Tween: Interpolates between two non-sequential images to generate a new frame.

�Color > CopyAux: Copies aux channels, including motion vectors, into RGBA more efficiently than

Channel Booleans.

Stereoscopic Nodes

�Stereo > Anaglyph: Combines stereo images to create a single anaglyph image for viewing.

�Stereo > Combiner: sStacks a separate stereo images into a single stacked pair,

so they can be processed together.

�Stereo > Disparity: Generates disparity between left/right images.

�Stereo > DisparityToZ: Converts disparity to Z-depth.

�Stereo > Global Align: Shifts each stereo eye manually to do basic alignment of stereo images.

�Stereo > NewEye: Replaces left and/or right eye with interpolated eyes.

�Stereo > Splitter: Separates a stacked stereo image into to left and right images.

�Stereo > StereoAlign: Adjusts vertical alignment, convergence, and eye separation.

�Stereo > ZToDisparity: Converts Z-depth to disparity.

Working with Aux Deep Channels

Certain image formats can contain channels other than RGBA color, called aux deep channels. Stereo

Disparity and OpticalFlow deal directly with auxiliary deep channels.

Aux channels supported in Fusion include:

�RGBA: These are the standard colors.

�Z: The eyespace Z coordinate is almost always negative because in eyespace, Fusion’s camera

sits at (0, 0, 0) looking down the Z-axis. Z values start at Z = 0 at the camera focal point and

progressively become more negative for objects deeper in the scene.

�Coverage: The percentage of the pixel covered by the frontmost pixel, used for antialiased

Z-compositing.


Fusion Fundamentals | Chapter 88 Optical Flow and Stereoscopic Nodes

FUSION

�Object ID: These are user-assigned integers to meshes.

�Material ID: These are user-assigned integers to materials.

�Texture Coords: Normalized texture coordinates stored as (u, v) pairs.

�Normal Vector: Normal vector (nx, ny, nz) where the components are typically in the range [–1, +1].

�Background Color: The color of the pixel if the frontmost layer were removed,

used for antialiased Z-compositing.

�Vector: The forward motion vector is an offset (vx, vy) that compares every pixel’s

position in one frame to the same pixel’s position in the next frame.

�Back Vector: The backward motion vector is an offset (vx, vy) that compares every

pixel’s position in one frame to the same pixel’s position in the previous frame.

�World Position: The position (wx, wy, wz) of the pixel in world coordinates.

�Disparity: An offset (dx, dy) that maps a pixel in the Left > Right or Right > Left frames.

Some extra channels are used by specific Fusion nodes.

For example:

�Merge can use the Z channel to perform a depth merge. If the Coverage and BackgroundColor

channels are present, it can do a better job on antialiased edges during the Z merge.

�Most image-processing nodes (e.g., BrightnessContrast) have options on their common controls

tab to limit their processing by MaterialID and ObjectID.

�The Fog and DepthBlur nodes make use of the Z channel.

�The Texture node makes use of the TexCoord channel.

�The Shader node makes use of the Normal channel.

There are a couple of ways to retrieve or generate those extra channels within Fusion.

For example:

�The Renderer3D node is capable of generating most of these channels.

�The OpticalFlow node generates the Vector and BackVector channels, and then TimeStretcher

and TimeSpeed can make use of these channels.

�The Disparity node generates the Disparity channels, and then DisparityToZ, NewEye, and

StereoAlign nodes can make use of the Disparity channels.

�The OpenEXR format can be used to import or export aux channels into Fusion by specifying a

mapping from EXR attributes to Fusion Aux channels using CopyAux.