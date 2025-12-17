---
title: "Propagating Auxiliary Channels"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 302
---

# Propagating Auxiliary Channels

Ordinarily, auxiliary channels are propagated along with RGBA image data, from node to node,

among gray-colored nodes, including those in the Blur, Filter, Effect, Transform, and Warp categories.

Basically, most nodes that simply manipulate channel data propagate (and potentially manipulate)

auxiliary channels with no problems.

However, when you composite two image layers using the Merge node, auxiliary channels only

propagate through the image that’s connected to the background input. The rationale for this is that in

most composites that include computer-generated imagery, the background is most often the CG layer

that contains auxiliary channels, while the foreground is a live-action green screen plate with subjects

or elements that are combined against the background, which lack auxiliary channels.

Nodes That Use Auxiliary Channels

The availability of auxiliary channels opens up a world of advanced compositing functionality.

This section describes every Fusion node that has been designed to work with images that contain

auxiliary channels.

�Copy Aux: The Copy Aux tool can copy auxiliary channels to RGB and then copy them back.

It includes some useful options for remapping values and color depths, as well as removing

auxiliary channels.

�Channel Booleans: The Channel Boolean tool can be used to combine or copy the values from

one channel to another in a variety of ways.

�Custom Tool, Custom Vertex 3D, pCustom: The “Custom” tools can sample data from the

auxiliary channels per pixel, vertex, or particle and use that for whatever processing you

would like.

�Depth Blur: The Depth Blur tool is used to blur an image based on the information present in

the Z-Depth. A focal point is selected from the Z-Depth values of the image and the extent of the

focused region is selected using the Depth of Field control. The Scale value default is based on

an 8-bit image so it is important to lower the scale value when using the Depth Blur with 16- or

32‑bit float files.

�Disparity to Z, Z to Disparity, Z to WorldPos: These tools use the inherent relationships between

depth, position, and disparity to convert from one channel to another.

�Fog: The Fog tool makes use of the Z-Depth to create a fog effect that is thin closer to the camera

and thickens in regions farther away from the camera. You use the Pick tool to select the Depth

values from the image and to define the Near and Far planes of the fog’s effect.


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

�Lumakeyer: The Lumakeyer tool can be used to perform a key on the Z-Depth channel by

selecting the Z-Depth in the channel drop-down list.

�Merge: In addition to regular compositing operations, Merge is capable of merging two or more

images together using the Z-Depth, Z-Coverage, and BG RGBA buffer data. This is accomplished

by enabling the Perform Depth Merge checkbox from the Channels tab.

�New Eye: For stereoscopic footage, New Eye uses the Disparity channels to create new

viewpoints or to transfer RGBA data from one eye to the other.

�Shader: The Shader tool applies data from the RGBA, UV and the Normal channels to modify the

lighting applied to objects in the image. Control is provided over specular highlights, ambient and

diffuse lighting, and position of the light source. A second image can be applied as a reflection or

refraction map.

�Shadow: The Shadow tool can use the Z-Depth channel for a Z-Map. This allows the shadow to fall

onto the shape of the objects in the image.

�Smooth Motion: Smooth Motion uses Vector and Back Vector channels to blend other channels

temporally. This can remove high frequency jitter from problematic channels such as Disparity.

�SSAO: SSAO is short for Screen Space Ambient Occlusion. Ambient Occlusion is the lighting

caused when a scene is surrounded by a uniform diffuse spherical light source. In the real world,

light lands on surfaces from all directions, not from just a few directional lights. Ambient Occlusion

captures this low frequency lighting, but it does not capture sharp shadows or specular lighting.

For this reason, Ambient Occlusion is usually combined with Specular lighting to create a full

lighting solution. The SSAO tool uses the Z-Depth channel but requires a Camera3D input.

�Stereo Align: For stereoscopic footage, the Disparity channels can be used by Stereo Align to

warp one or both of the eyes to correct misalignment or to change the convergence plane.

�Texture: The Texture tool uses the UV channels to apply an image from the second input as a

texture. This can replace textures on a specific object when used in conjunction with the Object ID

or Material ID masks.

�Time Speed and Time Stretcher: These tools can use the Vector and BackVector channels to

retime footage.

�Vector Distortion: The forward XY Vector channels can be used to warp an image with this tool.

�Vector Motion Blur: Using the forward XY Vector channels, the Vector Motion Blur tool can apply

blur in the direction of the velocity, creating a motion blur effect.

�Volume Fog: Volume Fog is a raymarcher that uses the World Position channels to determine ray

termination and volume dataset placement. It can also use cameras and lights from a 3D scene to

set the correct ray start point and Illumination parameters.

�Volume Mask: Volume Mask uses the World Position channels to set a mask in 3D space as

opposed to screen space. This allows a mask to maintain perfect tracking through a camera move.

TIP: The Object ID and Material ID auxiliary channels can be used by some tools in Fusion to

generate a mask. The “Use Object” and “Use Material” settings used to accomplish this are

found in the Settings tab of that node’s controls in the Inspector.


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

Image Formats That Support Aux Channels

Fusion supports auxiliary channel information contained in a variety of image formats. The number of

channels and methods used are different for each format.

�OpenEXR (*.exr): The OpenEXR file format is the primary format used to contain an arbitrary

number of additional image channels. Many renderers that will write to the OpenEXR format will

allow the creation of channels that contain entirely arbitrary data. For example, a channel with

specular highlights might exist in an OpenEXR. In most cases, the channel will have a custom

name that can be used to map the extra channel to one of the channels recognized by Fusion.

�SoftImage PIC (*.PIC, *.ZPIC and *.Z): The PIC image format (used by SoftImage) is an older image

format that can contain Z-Depth data in a separate file marked by the ZPIC file extension. These

files must be located in the same directory as the RGBA PIC files and must use the same names.

Fusion will automatically detect the presence of the additional information and load the ZPIC

images along with the PIC images.

�Wavefront RLA (*.RLA), 3ds Max RLA (*.RLA) and RPF (*.RPF): This is an older image format

capable of containing any of the image channels mentioned above. All channels are contained

within one file, including RGBA, as well as the auxiliary channels. These files are identified by the

RLA or RPF file extension. Not all RLA or RPF files contain auxiliary channel information, but most

do. RPF files have the additional capability of storing multiple samples per pixel, allowing different

layers of the image to be loaded for very complex depth composites.

�Fusion RAW (*.RAW): Fusion’s native RAW format is able to contain all of the auxiliary channels as

well as other metadata used within Fusion.

Creating Auxiliary Channels in Fusion

The following nodes create auxiliary channels:

�Renderer 3D: Creates these channels in the same way as any other 3D application would,

and you have the option of outputting every one of the auxiliary data channels that the

Fusion page supports.

�Optical Flow: Generates Vector and Back Vector channels by analyzing pixels over consecutive

frames to determine likely movements of features in the image.

�Disparity: Generates Disparity channels by comparing stereoscopic image pairs.


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

Chapter 79

Compositing

Layers in Fusion

This chapter is intended to give you a solid base for making the transition

from a layer-based compositing application to Fusion’s node‑based interface.

It provides practical information about how to start structuring a node tree for

simple layered composites.

Contents

Applying Effects���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1648

Adding a Node to the Tree������������������������������������������������������������������������������������������������������������������������������������������������������������� 1648

Editing Parameters in the Inspector������������������������������������������������������������������������������������������������������������������������������������������ 1649

Replacing Nodes��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1650

Adjusting Fusion Sliders������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1650

Compositing Two Clips Together������������������������������������������������������������������������������������������������������������������������������������������������ 1651

Adding Additional Media to Compositions����������������������������������������������������������������������������������������������������������������������������� 1651

Automatically Creating Merge Nodes�������������������������������������������������������������������������������������������������������������������������������������� 1652

Fixing Problem Edges in a Composite������������������������������������������������������������������������������������������������������������������������������������� 1652

Using Composite Modes in the Merge Node����������������������������������������������������������������������������������������������������������������������� 1654

Creating and Using Text����������������������������������������������������������������������������������������������������������������������������������������������������������������� 1655

Creating Text Using the Text+ Node����������������������������������������������������������������������������������������������������������������������������������������� 1655

Styling and Adjusting Text�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1656

Using Text as a Mask������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1658

Using Transform Controls in the Merge Node����������������������������������������������������������������������������������������������������������������������� 1661

Building a Simple Green-Screen Composite����������������������������������������������������������������������������������������������������������������������� 1662

Mapping Timeline Layers to Nodes in Fusion���������������������������������������������������������������������������������������������������������������������� 1662

Pulling a Green-Screen Key Using the Delta Keyer����������������������������������������������������������������������������������������������������������� 1664

Dealing with Spill��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1668

Masking a Graphic������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1668


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

Applying Effects

Before we dive into multi-layered composites, let’s start by looking at some very simple effects and

build up from there. Opening the Effects Library, then clicking the disclosure control to the left of Tools,

reveals a list of categories containing all the nodes available in Fusion. As mentioned before, each

node does one thing, and by using these nodes in concert you can create extremely complex results

from humble beginnings.

Clicking the Effect category reveals its contents. In this example we’ll use the TV effect.

Browsing the Effect category to find the TV node

Adding a Node to the Tree

Assuming that the MediaIn node in the Fusion page or the Loader node in Fusion Studio is the

currently selected node in the Node Editor, clicking once on the TV node, for example, in the Effects

Library automatically adds that node to the node tree to the right of the selected node. In the Fusion

page, it immediately takes effect in the viewer thanks to the fact that the MediaOut1 node is what’s

loaded in the viewer, since that means that all nodes upstream of the MediaOut1 node will be

processed and shown.

A new node added from the Effects Library

In Fusion Studio, you must press the 1 or 2 key on the keyboard to load the selected node in

the viewer.

There are many other ways of adding nodes to your node tree, but it’s good to know how to browse

the Effects Library as you get started.


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION