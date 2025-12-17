---
title: "FBX Mesh 3D [FBX]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 348
---

# FBX Mesh 3D [FBX]

The FBX Mesh node

FBX Mesh 3D Node Introduction

The FBX Mesh 3D node is used to import polygonal geometry from scene files that are saved in the FilmBox

(FBX) format. It is also able to import geometry from OBJ, 3DS, DAE, and DXF scene files. This provides

a method for working with more complex geometry than is available using Fusion‘s built-in primitives.

When importing geometry with this node, all the geometry in the FBX file is combined into one

mesh with a single pivot and transformation. The FBX Mesh node ignores any animation applied to

the geometry.

Alternatively, in Fusion Studio, the File > Import > FBX Scene or in DaVinci Resolve, the Fusion > Import

> FBX Scene menu can be used to import an FBX scene. This option creates individual nodes for each

camera, light, and mesh in the file. This menu option can also be used to preserve the animation of

the objects.

Setting the Preferences > Global > General > Auto Clip Browse option in Fusion Studio, or the Fusion >

Fusion Settings > General > Auto Clip Browse option in DaVinci Resolve to Enabled (default), and then

adding this node to a composition automatically displays a file browser allowing you to choose the file

to import.

Inputs

SceneInput: The orange scene input is an optional connection if you wish to combine other 3D

geometry nodes with the imported FBX file.

Material Input: The green input is the material input that accepts either a 2D image or a 3D material. If

a 2D image is provided, it is used as a diffuse texture map for the basic material tab in the node. If a 3D

material is connected, then the basic material tab is disabled.

Basic Node Setup

The FBX Mesh 3D node can be used as a stand-alone node without any other nodes connected to it.

The output is connected to a Merge 3D, integrating the FBX model into a larger scene. Below, the FBX

Mesh 3D node also has a chrome material connected to its material input.

An FBX Mesh 3D node with chrome material applied


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Inspector

FBX Mesh 3D controls

Controls Tab

Most of the Controls tab is taken up by common controls. The FBX-specific controls included on this

tab are primarily information and not adjustments.

Size

The Size slider controls the size of the FBX geometry that is imported. FBX meshes have a tendency

to be much larger than Fusion’s default unit scale, so this control is useful for scaling the imported

geometry to match the Fusion environment.

FBX File

This field displays the filename and file path of the currently loaded FBX mesh. Click the Browse

button to open a file browser that can be used to locate a new FBX file. Despite the node’s name, this

node is also able to load a variety of other formats.

FBX ascii

(*.fbx)

FBX 5.0 binary

(*.fbx)

Autocad DXF

(*.dxf)

3D Studio 3Ds

(*.3ds)

Alias OBJ

(*.obj)

Collada DAE

(*.dae)

Object Name

This input shows the name of the mesh from the FBX file that is being imported. If this field is blank,

then the contents of the FBX geometry are imported as a single mesh. You cannot edit this field; it is

set by Fusion when using the File > Import > FBX Scene menu.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Take Name

FBX files can contain multiple instances of an animation, called Takes. This field shows the name of the

animation take to use from the FBX file. If this field is blank, then no animation is imported. You cannot

edit this field; it is set by Fusion when using the File > Import > FBX Scene menu.

Wireframe

Enabling this checkbox causes the mesh to render only the wireframe for the object. Only the OpenGL

renderer in the Renderer 3D node supports wireframe rendering.

Common Controls

Controls, Materials, Transform, and Settings Tabs

The remaining controls for Visibility, Lighting, Matte, Blend Mode, Normals/Tangents, and Object

ID are common to many 3D nodes. The same is true of the Materials, Transform, and Settings tabs.

Their descriptions can be found in “The Common Controls” section at the end of this chapter.

Fog 3D [3Fo]

The Fog 3D node

Fog 3D Node Introduction

The Fog 3D node applies fog to the scene based on a depth cue. It is the 3D version of the Fog node

in the Deep Pixel category. It is designed to work completely in 3D space and takes full advantage of

anti-aliasing and depth of field effects during rendering.

The Fog 3D node essentially retextures the geometry in the scene by applying a color correction

based on the object’s distance from the camera. An optional density texture image can be used to

apply variation to the correction.

Inputs

The Fog 3D node has two inputs in the Node Editor, only one of which is required for the Fog 3D to

project onto a 3D scene.

SceneInput: The required orange-colored input accepts the output of a 3D scene on which the fog is

“projected.”

DensityTexture: This optional green-colored input accepts a 2D image. The color of the fog created

by this node is multiplied by the pixels in this image. When creating the image for the density texture,

keep in mind that the texture is effectively projected onto the scene from the camera.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Basic Node Setup

The Fog 3D node is placed after the Merge 3D node that contains the scene. Viewing the Fog node

will show the fog applied to the objects in the 3D scene based on their Z position.

A Fog 3D node placed after the Merge 3D scene

Inspector

Fog node controls

Controls Tab

The Controls tab includes all the parameters you use to decide how the Fog looks and projects onto

the geometry in the scene.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Enable

Use this checkbox to enable or disable parts of the node from processing. This is not the same as the

red switch in the upper-left corner of the inspector. The red switch disables the tool altogether and

passes the image on without any modification. The Enable checkbox is limited to the effect part of the

tool. Other parts like scripts in the Settings tab still processes as normal.

Show Fog in View

By default, the fog created by this node is visible only when the scene is viewed using a camera node.

When this checkbox is enabled, the fog becomes visible in the scene from all points of view.

Color

This control can be used to set the color of the fog. The color is also multiplied by the density texture

image, if one is connected to the green input on the node.

Radial

By default, the fog is created based on the perpendicular distance to a plane (parallel with the near

plane) passing through the eye point. When the Radial option is checked, the radial distance to the

eye point is used instead of the perpendicular distance. The problem with perpendicular distance fog

is that when you move the camera about, as objects on the left or right side of the frustum move into

the center, they become less fogged although they remain the same distance from the eye. Radial fog

fixes this. Radial fog is not always desirable, however.

For example, if you are fogging an object close to the camera, like an image plane, the center

of the image plane could be unfogged while the edges could be fully fogged.

Radial vs. Perpendicular fog effect


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Type

This control is used to determine the type of falloff applied to the fog.

�Linear: Defines a linear falloff for the fog.

�Exp: Creates an exponential nonlinear falloff.

�Exp2: Creates a stronger exponential falloff.

Near/Far Fog Distance

This control expresses the range of the fog in the scene as units of distance from the camera. The

Near Distance determines where the fog starts, while the Far Distance sets the point where the fog

has its maximum effect. Fog is cumulative, so the farther an object is from the camera, the thicker the

fog should appear.

Common Controls

Settings Tab

The Settings tab controls are common to many 3D nodes, and their descriptions can be found in “The

Common Controls” section at the end of this chapter.