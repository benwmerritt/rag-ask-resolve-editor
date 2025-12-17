---
title: "Ribbon 3D [3Ri]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 355
---

# Ribbon 3D [3Ri]

The Ribbon 3D node

Ribbon 3D Node Introduction

Ribbon 3D generates an array of subdivided line segments or a single line between two points. It is

quite useful for motion graphics, especially in connection with Replicate 3D to attach other geometry

to the lines, and with Displace3D for creating lightning bolt-like structures. The array of lines is, by

default, assigned with texture coordinates, so they can be used with a 2D texture. As usual, UVMap 3D

can be used to alter the texture coordinates. This node relies heavily on certain OpenGL features and

does not produce any visible result when the Renderer 3D node is set to use the software renderer.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Furthermore, the way lines are drawn is completely up to the graphics card capabilities, so

the ribbon appearance may vary based on your computer’s graphics card.

Inputs

There are two inputs on the Ribbon 3D node: one for the destination geometry that contains the

vertices, and one for the 3D geometry you want to replicate.

3D Scene: The orange input accepts a 3D scene or geometry.

Material: The input accepts the 2D texture for the ribbon.

Neither connected input is required.

Basic Node Setup

In the example below, a Ribbon 3D node is used to generate lines. A gradient background is

connected to “colorize” the lines. Additional nodes are then used after the Ribbon 3D to bend and

distort the lines.

Ribbon 3D generates lines distorted by additional nodes

Inspector

Ribbon 3D controls


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Controls Tab

The Controls tab determines the number of ribbon strands, their size, length, and spacing.

Number of Lines

The number of parallel lines drawn between the start point and end point.

Line Thickness

Line thickness is allowed in the user interface to take on a floating-point value, but some graphics

cards allow only integer values. Some cards may only allow lines equal to or thicker than one, or max

out at a certain value.

Subdivision Level

The number of vertices on each line between start point and end points. The higher the number, the

more precise and smoother 3D displacement appears.

Ribbon Width

Determines how far the lines are apart from each other.

Start

XYZ control to set the start point of the ribbon.

End

XYZ control to set the end point of the ribbon.

Ribbon Rotation

Allows rotation of the ribbon around the virtual axis defined by start point and end points.

Anti-Aliasing

Allows you to apply anti-aliasing to the rendered lines. Using anti-aliasing isn’t necessarily

recommended. When activated, there may be be gaps between the line segments. This is especially

noticeable with high values of line thickness. Again, the way lines are drawn is completely up to the

graphics card, which means that these artifacts can vary from card to card.

Common Controls

Controls, Materials, and Settings Tabs

The controls for Visibility, Lighting, Matte, Blend Mode, Normals/Tangents, and Object ID in the

Controls tab are common in many 3D nodes. The Materials tab and Settings tab in the Inspector are

also duplicated in other 3D nodes. These common controls are described in detail at the end of this

chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Shape 3D [3Sh]

The Shape 3D node

Shape 3D Node Introduction

The Shape 3D node is used to produce several basic primitive 3D shapes, including planes, cubes,

spheres, and cylinders.

Inputs

There are two optional inputs on the Shape 3D. The scene input can be used to combine additional

geometry with the Shape 3D, while the material input can be used to texture map the Shape

3D object.

SceneInput: Although the Shape 3D creates its own 3D geometry, you can use the orange scene

input to combine an additional 3D scene or geometry.

MaterialInput: The green input accepts either a 2D image or a 3D material. If a 2D image is provided, it

is used as a diffuse texture map for the basic material built into the node. If a 3D material is connected,

then the basic material is disabled.

Basic Node Setup

In the example below, four Shape 3D nodes are used to create the primitives of a 3D set. Two of the

Shape 3D nodes are connected creating a more complex primitive shape. Those shapes can then be

used with a Projector 3D to texture them with a realistic material.

Shape 3D nodes combined with Projector 3D to create a realistic 3D set


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Inspector

Shape 3D controls

Controls Tab

The Controls tab allows you to select a shape and modify its geometry. Different controls appear

based on the specific shape that you choose to create.

Shape

This menu allows you to select the primitive geometry produced by the Shape 3D node.

The remaining controls in the Inspector change to match the selected shape.

�Lock Width/Height/Depth: [plane, cube] If this checkbox is selected, the width, height, and depth

controls are locked together as a single size slider. Otherwise, individual controls over the size of

the shape along each axis are provided.

�Size Width/Height/Depth: [plane, cube] Used to control the size of the shape.

Cube Mapping

When Cube is selected in the shape menu, the Cube uses cube mapping to apply the Shape node’s

texture (a 2D image connected to the material input on the node).

Radius

When a Sphere, Cylinder, Cone, or Torus is selected in the shape menu, this control sets the radius of

the selected shape.

Top Radius

When a cone is selected in the Shape menu, this control is used to define a radius for the top of a

cone, making it possible to create truncated cones.

Start/End Angle

When the Sphere, Cylinder, Cone, or Torus shape is selected in the Shape menu, this range control

determines how much of the shape is drawn. A start angle of 180° and end angle of 360° would only

draw half of the shape.

Start/End Latitude

When a Sphere or Torus is selected in the Shape menu, this range control is used to crop or slice the

object by defining a latitudinal subsection of the object.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Bottom/Top Cap

When Cylinder or Cone is selected in the Shape menu, the Bottom Cap and Top Cap checkboxes are

used to determine if the end caps of these shapes are created or if the shape is left open.

Section

When the Torus is selected in the Shape menu, Section controls the thickness of the tube making up

the torus.

Subdivision Level/Base/Height

The Subdivision controls are used to determine the tessellation of the mesh on all shapes. The higher

the subdivision, the more vertices each shape has.

Wireframe

Enabling this checkbox causes the mesh to render only the wireframe for the object.

Common Controls

Controls, Materials, Transform and Settings Tabs

The controls for Visibility, Lighting, Matte, Blend Mode, Normals/Tangents, and Object ID in the

Controls tab are common in many 3D nodes. The Materials tab, Transforms tab, and Settings tab in the

Inspector are also duplicated in other 3D nodes. These common controls are described in detail at the

end of this chapter in “The Common Controls” section.

Sphere Map vs. Connecting the Texture to a Sphere Directly

You can connect a LatLong (equirectangular) texture map directly to a sphere instead of piping it

through the Sphere Map node first. This results in a different rendering if you set the start/end angle

and latitude to less than 360°/180°. In the first case, the texture is squashed. When using the Sphere

Map node, the texture is cropped. Compare:

Spherical mapping differences

NOTE: If you pipe the texture directly into the sphere, it is also mirrored horizontally. You can

change this by using a Transform node first.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION