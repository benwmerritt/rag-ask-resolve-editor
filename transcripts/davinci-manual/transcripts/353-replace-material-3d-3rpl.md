---
title: "Replace Material 3D [3Rpl]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 353
---

# Replace Material 3D [3Rpl]

The Replace Material 3D node

Replace Material 3D Node Introduction

The Replace Material 3D node replaces the material applied to all the geometry in the input scene with

its own material input. Any lights or cameras in the input scene are passed through unaffected.

The scope of the replacement can be limited using Object and Material identifiers in the Inspector.

The scope can also be limited to individual channels, making it possible to use a completely different

material on the Red channel, for example.

Since the Text 3D node does not include a material input, you can use the Replace Material to add

material shaders to the text.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Inputs

The Replace Material node has two inputs: one for the 3D scene, object, or 3D text that contains the

original material, and a material input for the new replacement material.

SceneInput: The orange scene input accepts a 3D scene or 3D text that you want to replace the

material.

MaterialInput: The green material input accepts either a 2D image or a 3D material. If a 2D image is

provided, it is used as a diffuse texture map for the basic material built into the node. If a 3D material is

connected, then the basic material is disabled.

Basic Node Setup

The Replace Material 3D node is inserted directly after the 3D object or scene whose material

you want to replace. Below, it is used to replace the default material on a Text 3D node with a

chrome shader.

Replace Material 3D used to replace the default material of a Text 3D node

Inspector

Replace Material 3D controls

Controls Tab

Enable

This checkbox enables the material replacement. This is not the same as the red switch in the upper-

left corner of the Inspector. The red switch disables the tool altogether and passes the image on

without any modification. The enable checkbox is limited to the effect part of the tool. Other parts, like

scripts in the Settings tab, still process as normal.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Replace Mode

The Replace Mode section offers four methods of replacing each RGBA channel:

�Keep: Prevents the channel from being replaced by the input material.

�Replace: Replaces the material for the corresponding color channel.

�Blend: Blends the materials together.

�Multiply: Multiplies the channels of both inputs.

Limit by Object ID/Material ID

When enabled, a slider appears where the desired IDs can be set. Other objects keep their materials.

If both options are enabled, an object must satisfy both conditions.

Common Controls

Material and Settings Tabs

The remaining controls for the Material and Settings tabs are common to many 3D nodes.

Their descriptions can be found in “The Common Controls” section at the end of this chapter.

Replace Normals 3D [3RpN]

The Replace Normals 3D node

Replace Normals Node Introduction

In 3D modeling, normals are vectors used to determine the direction light reflects off surfaces. The

Replace Normals node is used to replace the normals/tangents on incoming geometry, effectively

adjusting the surface of an object between smooth and flat. All geometry connected to the scene

input on the node is affected. Lights/Cameras/PointClouds/Locators/Materials, and other non-mesh

nodes are passed through unaffected. The normals/tangents affected by this node are Per-vertex

normals/tangents, not Per-face normals/tangents. The input geometry must have texture coordinates

in order for tangents to be computed. Sometimes geometry does not have texture coordinates, or the

texture coordinates were set to All by the FBX import because they were not present on the FBX.

Inputs

The Replace Normals node has a single input for the 3D scene or incoming geometry.

SceneInput: The orange scene input accepts a 3D scene or 3D geometry that contains the normal

coordinates you want to modify.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Basic Node Setup

The Replace Normals 3D node is inserted directly after the 3D object or scene whose normals you

want to modify. Below, it is used to smooth the material on an imported 3D model.

Replace Normals 3D used to smooth normals on 3D geometry

Inspector

Replace Normals 3D controls

Control Tab

The options in the Control tab deal with repairing 3D geometry and then recomputing normals/tangents.

Pre-Weld Position Vertices

Sometimes position vertices are duplicated in a geometry, even though they have the same position,

causing normals/tangents to be miscomputed. The results of pre-welding are thrown away; they do

not affect the output geometry’s position vertices.

Recompute

Controls when normals/tangents are recomputed.

�Always: The normals on the mesh are always recomputed.

�If Not Present: The normals on the mesh are recomputed only if they are not present.

�Never: The normals are never computed. This option is useful when animating.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Smoothing Angle

Adjacent faces with angles in degrees smaller than this value have their adjoining edges smoothed

across. A typical value one might choose for the Smoothing Angle is between 20 and 60 degrees.

There is special case code for 0.0f and 360.0f (f stands for floating-point value). When set to 0.0f,

faceted normals are produced; this is useful for artistic effect.

Ignore Smooth Groups

If set to False, two faces that have different Smooth Groups are not smoothed across (e.g., the faces

of a cube or the top surfaces of a cylinder have different Smooth Groups). If you check this On and set

the smoothing angle large enough, the faces of a cube are smoothed across. There is currently no

way to visualize Smooth Groups within Fusion.

Flip Normals

Flipping of tangents can sometimes be confusing. Flip has an effect if the mesh has tangent vectors.

Most meshes in Fusion don’t have tangent vectors until they reach a Renderer 3D, though. Also,

when viewing tangent vectors in the viewers, the tangent vectors are created if they don’t exist. The

confusing thing is if you view a Cube 3D that has no tangent vectors and press the FlipU/FlipV button,

nothing happens. This is a result of there being no tangent vectors to create, but later the GL renderer

can create some (unflipped) tangent vectors.

There are five items you should be aware of when dealing with normals.

#1 The FBX importer recomputes the normals if they don’t exist, but you can get a higher-

quality result from the Replace Normals node.

#2 Bump maps can sometimes depend on the model’s normals. Specifically, when you

simplify a complex high polygon model to a low polygon model + bump map, the normals and

bump map can become “linked.” Recomputing the normals in this case can make the model

look funny. The bump map was intended to be used with the original normals.

#3 Most primitives in Fusion are not generated with tangents; when needed, they are

generated on the fly by a Renderer 3D and cached.

#4 Tangents currently are only needed for bump mapping. If a material needs bump mapping,

then tangents are created. These tangents are created with some default settings (e.g.,

Smoothing Angle, and so on). If you don’t want Fusion automatically creating tangents, you

can use the Replace Normals node to create them manually.

#5 All computations are done in the local coordinates of the geometries instead of in the

coordinate system of the Replace Normals 3D node. This can cause problems when there is a

non-uniform scale applied to the geometry before Replace Normals 3D is applied.

Common Controls

Settings Tab

The Settings tab is common to many 3D nodes. The description of these controls can be found in “The

Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION