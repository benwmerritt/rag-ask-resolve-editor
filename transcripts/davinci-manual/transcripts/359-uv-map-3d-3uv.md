---
title: "UV Map 3D [3UV]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 359
---

# UV Map 3D [3UV]

The UVMap 3D node

UV Map 3D Node Introduction

The UV Map 3D node replaces the UV texture coordinates on the geometry in the scene. These

coordinates tell Fusion how to apply a texture to an object. While it is possible to adjust the global

properties of the selected mapping mode, it is not possible to manipulate the UV coordinates of

individual vertices directly from within Fusion. The onscreen controls drawn in the viewers are for

reference only and cannot be manipulated.

Camera Projections with UV Map 3D

The Camera Mapping mode makes it possible to project texture coordinates onto geometry through a

camera. Once you select Camera from the Mapping mode menu, then connect the Camera 3D node

that you want to use to create the UV coordinates.

NOTE: That this does not directly project an image through the camera. The image to be

projected should be connected to the diffuse texture input of whatever material is assigned

to the objects. When the texture is applied, it uses the UV coordinates created by the camera.

Because this is a texture projection and not light, the Alpha channel of the texture correctly

sets the opacity of the geometry.

See the Camera 3D and Projector 3D nodes for alternate approaches to projection.

The projection can optionally be locked to the vertices as it appears on a selected frame.

This fails if the number of vertices in the mesh changes over time, as Fusion must be able to match up

the mesh at the reference time and the current time. To be more specific, vertices may not be created

or destroyed or reordered. So, projection locking does not work for many particle systems, or for

primitives with animated subdivisions, or with duplicate nodes using non-zero time offsets.

NOTE: The UV Map 3D node does not put a texture or material on the mesh; it only modifies

the texture coordinates that the materials use. This may be confusing because the material

usually sits upstream, as seen in the Basic Node Setup example below.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Inputs

The UV Map 3D node has two inputs: one for a 3D scene or 3D object and another optional input for a

Camera 3D node.

Scene Input: The orange scene input is connected to the 3D scene or 3D object you want to

triangulate.

CameraInput: This input expects the output of the Camera 3D node. It is only visible when the Camera

Map mode menu is set to Camera.

Basic Node Setup

The UV Map 3D node is placed after all the geometry and set to Camera Map. Connecting a camera to

the UV map allows you to line up the texture based on a centered camera position and 3D geometry.

UV Map 3D is placed after the Merge 3D, with a camera connected to line up the texture

Inspector

UV Map 3D controls

Controls Tab

The UV Map 3D Controls tab allows you to select Planar, Cylindrical, Spherical, XYZ, and Cubic

mapping modes, which can be applied to basic Fusion primitives as well as imported geometry. The

position, rotation, and scale of the texture coordinates can be adjusted to allow fine control over the

texture’s appearance. An option is also provided to lock the UV produced by this node to animated


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

geometry according to a reference frame. This can be used to ensure that textures applied to

animated geometry do not slide.

Map Mode

The Map mode menu is used to define how the texture coordinates are created. You can think of this

menu as a way to select the virtual geometry that projects the UV space on the object.

�Planar: Creates the UV coordinates using a plane.

�Cylindrical: Creates the UV coordinates using a cylindrical-shaped object.

�Spherical: The UVs are created using a sphere.

�XYZ to UVW: The position coordinates of the vertices are converted to UVW coordinates directly.

This is used for working with procedural textures.

�CubeMap: The UVs are created using a cube.

�Camera: Enables the Camera input on the node. After connecting a camera to the node, the

texture coordinates are created based on camera projection.

Orientation X/Y/Z

Defines the reference axis for aligning the Map mode.

Fit

Clicking this button fits the Map mode to the bounding box of the input scene.

Center

Clicking this button moves the center of the Map mode to the bounding box center of the input scene.

Lock UVs on Animated Objects

If the object is animated, the UVs can be locked to it by enabling this option. The option also reveals

the Ref Time slider, where it is possible to choose a reference frame for the UV mapping. Using this

feature, it is not required to animate the UV map parameters. It is enough to set up the UV map at the

reference time.

Size X/Y/Z

Defines the size of the projection object.

Center X/Y/Z

Defines the position of the projection object.

Rotation/Rotation Order

Use these buttons to select which order is used to apply the rotation along each axis of the object. For

example, XYZ would apply the rotation to the X-axis first, followed by the Y-axis, and then the Z-axis.

Rotation X/Y/Z

Sets the orientation of the projection object for each axis, independent from the rotation order.

Tile U/V/W

Defines how often a texture fits into the projected UV space on the applicable axis. Note that the UVW

coordinates are transformed, not a texture. This works best when used in conjunction with the Create

Texture node.

Flip U/V/W

Mirrors the texture coordinates around the applicable axis.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Flip Faces (Cube Map Mode Only)

Mirrors the texture coordinates on the individual faces of the cube.

NOTE: To utilize the full capabilities of the UV Map 3D node, it helps to have a basic

understanding of how 2D images are mapped onto 3D geometry. When a 2D image is

applied to a 3D surface, it is converted into a texture map that uses UV coordinates to

determine how the image translates to the object. Each vertex on a mesh has a (U, V) texture

coordinate pair that describes the appearance the object takes when it is unwrapped and

flattened. Different mapping modes use different methods for working out how the vertices

transform into a flat 2D texture. When using the UV Map 3D node to modify the texture

coordinates on a mesh, it’s best to do so using the default coordinate system of the mesh or

primitive. So the typical workflow would look like Shape 3D > UV Map 3D > Transform 3D. The

Transformation tab on the Shape node would be left to its default values, and the Transform

3D node following the UV Map 3D does any adjustments needed to place the node in the

scene. Modifying/animating the transform of the Shape node causes the texture to slide

across the shape, which is generally undesirable. The UV Map 3D node modifies texture

coordinates per vertex and not per pixel. If the geometry the UV map is applied to is poorly

tessellated, then undesirable artifacts may appear.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Weld 3D [3We]

The Weld 3D node

Weld 3D Node Introduction

Sometimes 3D geometry has vertices that should have been joined when the geometry was created,

but for one reason or another they are not joined. This can cause artifacts, especially when the two

vertices have different normals.

For example, you may find:

�The different normals produce hard shading/lighting edges where none were intended.

�If you try to Displace 3D the vertices along their normals, they crack.

�Missing pixels or doubled-up pixels in the rendered image.

�Particles pass through the tiny invisible cracks.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Instead of round tripping back to your 3D modeling application to fix the “duplicated” vertices, the

Weld 3D node allows you to do this in Fusion. Weld 3D welds together vertices with the same or

nearly the same positions. This can be used to fix cracking issues when vertices are displaced by

welding the geometry before the Displace. There are no user controls to pick vertices. Currently, this

node welds together just position vertices; it does not weld normals, texcoords, or any other vertex

stream. So, although the positions of two vertices have been made the same, their normals still have

their old values. This can lead to hard edges in certain situations.

Inputs

The Weld 3D node has a single input for a 3D scene or 3D object you want to repair.

Scene Input: The orange scene input is connected to the 3D scene or 3D object you want to fix.

Basic Node Setup

The Weld 3D node is placed after the geometry that has duplicate vertices problems. Sometimes

problems are exposed when displacing the geometry. In that case, placing the weld after the

geometry but before the Displace 3D can repair the issues.

Weld 3D is placed after the 3D geometry that needs repair

Inspector

Weld 3D controls

Controls Tab

The Controls tab for the Weld 3D node includes a simple Weld Mode menu. You can choose between

welding vertices or fracturing them.

Fracture

Fracturing is the opposite of welding, so all vertices are unwelded. This means that all polygon

adjacency information is lost. For example, an Image Plane 3D normally consists of connected quads

that share vertices. Fracturing the image plane causes it to become a bunch of unconnected quads.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Tolerance

In auto mode, the Tolerance value is automatically detected. This should work in most cases.

It can also be adjusted manually if needed.

USAGE Use Weld 3D when issues occur with the geometry. Don’t use it everywhere just

because it’s there, as it influences render time.

Weld 3D is intended to be used as a mesh robustness tool and not as a mesh editing tool to

merge vertices. If you can see the gap between the vertices you want to weld in the 3D view,

you are probably misusing Weld 3D. Unexpected things may happen when you do this; do so

at your own peril.

LIMITATIONS Setting the tolerance too large can cause edges/faces to collapse to points.

If your model has detail distributed over several orders of scale, picking a tolerance value can

be hard or impossible.

For example, suppose you have a model of the International Space Station and there are

lots of big polygons and lots of really tiny polygons. If you set the tolerance too large, small

polygons that shouldn’t merge do; if you set the tolerance too small, some large polygons

won’t be merged.

Vertices that are far from the origin can fail to merge correctly. This is because bignumber +

epsilon can exactly equal bignumber in float math. This is one reason it may be best to merge

in local coordinates and not in world coordinates.

Sometimes Weld 3D-ing a mesh can make things worse. Take Fusion’s cone, for instance.

The top vertex of the cone is currently duplicated for each adjoining face, and they all have

different normals. If you weld the cone, the top vertices merge and only have one normal,

making the lighting look weird.

Weld 3D is not multithreaded.

WARNING Do not misuse Weld 3D to simplify (reduce the polygon count of) meshes. It

is designed to efficiently weld vertices that differ by only very small values, like a 0.001

distance.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION