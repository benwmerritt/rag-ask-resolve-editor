---
title: "Introduction to Fuse Plugins"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 325
---

# Introduction to Fuse Plugins

Fuses are plugins developed for Fusion using the Lua built-in scripting language. Being script-based,

Fuses are compiled on-the-fly in Fusion without the need of a computer programming environment.

While a Fuse may be slower than an identical Open FX plugin created using Fusion’s C++ SDK, a Fuse

will still take advantage of Fusion’s existing nodes and GPU acceleration.

To install a Fuse:


Use the .fuse extension at the end of the document name.


For DaVinci Resolve, save it in one of the following locations:

On macOS: Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/

DaVinci Resolve/Fusion/Fuses

On Windows: C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\

Support\Fusion\Fuses

On Linux: home/username/.local/share/DaVinciResolve/Fusion/Fuses

For Fusion Studio, save it in one of the following locations:

On macOS: Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/

Fusion/Fuses/

On Windows: C:\Users\username\AppData\Roaming\Blackmagic Design\Fusion\Fuses

On Linux: home/username/.fusion/BlackmagicDesign/Fusion/Fuses

You can open and edit Fuses by selecting the Fuse node in the Node Editor and clicking

the Edit button at the top of the Inspector. The Fuse opens in the text editor specified in the

Global Preferences/Scripting panel.

TIP: Changes made to a Fuse in a text editor do not immediately propagate to other

instances of that Fuse in the composition. Reopening a composition updates all Fuses

in the composition based on the current saved version. Alternatively, you can click the

Reload button in the Inspector to update the selected node without closing and reopening

the composition.


Fusion Fundamentals | Chapter 84 Using Open FX, Resolve FX, and Fuse Plugins

FUSION

Chapter 85

3D Compositing

Basics

This chapter covers many of the nodes used for creating 3D composites, the tasks

they perform, and how they can be combined to produce effective 3D scenes.

Contents

An Overview of 3D Compositing������������������������ 1773

3D Compositing Fundamentals��������������������������� 1774

Creating a Minimal 3D Scene��������������������������������� 1774

The Elements of a 3D Scene��������������������������������� 1776

Geometry Nodes���������������������������������������������������������� 1776

The Merge3D Node���������������������������������������������������� 1778

The Renderer3D Node����������������������������������������������� 1781

Software vs. GPU Rendering��������������������������������� 1782

Software Renderer������������������������������������������������������ 1782

OpenGL Renderer������������������������������������������������������� 1782

OpenGL UV Renderer����������������������������������������������� 1783

Loading 3D Nodes into the Viewer�������������������� 1784

Navigating the 3D View�������������������������������������������� 1785

Transforming Cameras and

Lights Using the Viewers����������������������������������������� 1786

Transparency Sorting������������������������������������������������ 1787

Material Viewer������������������������������������������������������������ 1787

Transformations����������������������������������������������������������� 1788

Onscreen Transform Controls������������������������������� 1789

Pivot������������������������������������������������������������������������������������ 1790

Target��������������������������������������������������������������������������������� 1790

Parenting�������������������������������������������������������������������������� 1791

Cameras��������������������������������������������������������������������������� 1792

Quickly Viewing a Scene Through a Camera 1793

Plane of Focus and Depth of Field���������������������� 1793

Importing Cameras����������������������������������������������������� 1794

Lighting and Shadows���������������������������������������������� 1795

Enabling Lighting in the Viewer���������������������������� 1795

Enabling Lighting to Be Rendered����������������������� 1795

Cotrolling Lighting within Each 3D Object������ 1795

Lighting Types Explained����������������������������������������� 1796

Materials and Textures�������������������������������������������� 1800

Material Components������������������������������������������������ 1801

Alpha Detail������������������������������������������������������������������� 1803

Illumination Models���������������������������������������������������� 1805

Textures��������������������������������������������������������������������������� 1806

Reflections and Refractions������������������������������������ 1807

Bump Maps�������������������������������������������������������������������� 1809

Projection Mapping���������������������������������������������������� 1810

Geometry�������������������������������������������������������������������������� 1813

Common Visibility Parameters������������������������������� 1814

Adding FBX Models ���������������������������������������������������� 1814

Using Text3D������������������������������������������������������������������ 1816

Fog 3D and Soft Clipping��������������������������������������� 1820

Material and Object IDs������������������������������������������ 1822

World Position Pass��������������������������������������������������� 1822

Point Clouds������������������������������������������������������������������� 1824


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

An Overview of 3D Compositing

Traditional image-based compositing is a two-dimensional process. Image layers have only the

amount of depth needed to define one as foreground and another as background. This is at odds

with the realities of production, since all images are either captured using a live-action camera

with freedom in all three dimensions, in a shot that has real depth, or have been created in a true

3D modeling and rendering application.

Within the Fusion Node Editor, you have a GPU-accelerated 3D compositing environment that includes

support for imported geometry, point clouds, and particle systems for taking care of such things as:

�Converting 2D images into image planes in 3D space

�Creating rough primitive geometry

�Importing mesh geometry from FBX or Alembic scenes

�Creating realistic surfaces using illumination models and shader compositing

�Rendering with realistic depth of field, motion blur, and supersampling

�Creating and using 3D particle systems

�Creating, extruding, and beveling 3D text

�Lighting and casting shadows across geometry

�3D camera tracking

�Importing cameras, lights, and materials from 3D applications such as Maya,

3ds Max, or LightWave

�Importing matched cameras and point clouds from applications such as SynthEyes or PF Track

An example 3D scene in Fusion


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

3D Compositing Fundamentals

The 3D category of nodes (which includes the Light, Material, and Texture subcategories) work

together to create 3D scenes. Examples are nodes that generate geometry, import geometry, modify

geometry, create lights and cameras, and combine all these elements into a scene. Nearly all these

nodes are collected within the 3D category of nodes found in the Effects Library.

The 3D category of nodes in the Effects Library

Conveniently, at no point are you required to specify whether your overall composition is 2D or 3D,

because you can seamlessly combine any number of 2D and 3D “scenes” together to create a single

output. However, the nodes that create these scenes must be combined in specific ways for this to

work properly.

Creating a Minimal 3D Scene

Creating a 3D scene couldn’t be easier, but you need to connect the required nodes in the right way.

At minimum, you need only connect a geometry node (such as a Text3D node) to a Renderer3D node

to output a 2D image that can be combined with other 2D images in your composition, as seen below.

However, you’ll only get a simply shaded piece of geometry for your trouble, although you can color

and transform it in the Inspector using controls internal to whichever geometry node you’re using.

A simple 3D scene with a Text3D node connected directly to a Renderer3D node


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

More realistically, each 3D scene that you want to create will probably have three to five nodes to give

you a better lit and framed result. These include:

�One of the available geometry nodes (such as Text3D or Image Plane 3D)

�A light node (such as DirectionalLight or SpotLight)

�A camera node

�A Merge3D node

�A Renderer3D node

All these should be connected together as seen below, with the resultantly more complex 3D scene

shown below.

The same text, this time lit and framed using Text3D, Camera, and SpotLight nodes to a Merge3D node

To briefly explain how this node tree works, the geometry node (in this case Text3D) creates an

object for the scene, and then the Merge3D node provides a virtual stage that combines the attached

geometry with the light and camera nodes to produce a lit and framed result with highlights and

shadows, while the aptly named Renderer3D node renders the resulting 3D scene to produce 2D

image output that can then be merged with other 2D images in your composition.

In fact, these nodes are so important that they appear at the right of the toolbar, enabling you to

quickly produce 3D scenes whenever you require. You might notice that the order of the 3D buttons

on the toolbar, from left to right, corresponds to the order in which these nodes are ordinarily used. So,

if you simply click on each one of these buttons from left to right, you cannot fail to create a properly

assembled 3D scene, ready to work on, as seen in the previous screenshot.

The 3D nodes available from the toolbar include

the ImagePlane3D, Shape3D, Text3D, Merge3D,

Camera3D, SpotLight3D, and Renderer3D nodes


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION