---
title: "Chapter 89"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 343
---

# Chapter 89

3D Nodes

This chapter covers, in great detail, the nodes used for creating 3D composites.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Alembic Mesh 3D [Abc]������������������������������������������ 1868

Bender 3D [3Bn]���������������������������������������������������������� 1871

Camera 3D [3Cm]������������������������������������������������������� 1873

Cube 3D [3Cb]������������������������������������������������������������� 1883

Custom Vertex 3D [3CV]���������������������������������������� 1885

Displace 3D [3Di]�������������������������������������������������������� 1891

Duplicate 3D [3Dp]���������������������������������������������������� 1893

Extrude 3D [3Ex]��������������������������������������������������������� 1899

FBX Exporter 3D [FBX]��������������������������������������������� 1901

FBX Mesh 3D [FBX]�������������������������������������������������� 1904

Fog 3D [3Fo]����������������������������������������������������������������� 1906

Image Plane 3D [3Im]����������������������������������������������� 1909

Locator 3D [3Lo]����������������������������������������������������������� 1911

Merge 3D [3Mg]����������������������������������������������������������� 1914

Override 3D [3Ov]������������������������������������������������������� 1916

Point Cloud 3D [3PC]������������������������������������������������ 1918

Projector 3D [3Pj]������������������������������������������������������� 1922

Renderer 3D [3Rn]����������������������������������������������������� 1927

Replace Material 3D [3Rpl]������������������������������������ 1935

Replace Normals 3D [3RpN]��������������������������������� 1937

Replicate 3D [3Rep]�������������������������������������������������� 1940

Ribbon 3D [3Ri]����������������������������������������������������������� 1945

Shape 3D [3Sh]������������������������������������������������������������ 1948

Soft Clip [3SC]�������������������������������������������������������������� 1951

Spherical Camera [3SC]����������������������������������������� 1953

Text 3D [3Txt]��������������������������������������������������������������� 1956

Transform 3D [3Xf]���������������������������������������������������� 1966

Triangulate 3D [3Tri]������������������������������������������������� 1969

UV Map 3D [3UV]������������������������������������������������������ 1970

Weld 3D [3We]������������������������������������������������������������� 1973

Modifier�������������������������������������������������������������������������� 1976

The Common Controls�������������������������������������������� 1977


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Alembic Mesh 3D [Abc]

The Alembic Mesh 3D node

Alembic Mesh Node Introduction

At times, you may need to import 3D geometry from applications like Blender, Cinema4D, or Maya.

One of the formats you can use for importing 3D geometry is the Alembic file format. This file

type is a 3D scene interchange format that contains baked animation with its geometry. In other

words, it eliminates the animation calculation times by embedding fixed, uneditable animation with

3D geometry. The animation is typically embedded using a point cache, which saves the dynamic data

such as velocity after it has been calculated. Alembic objects can contain mesh geometry, cameras,

points, UVs, normals, and baked animation.

You can import Alembic files (.abc) into Fusion in two ways:

�Choose File > Import > Alembic Scene in Fusion or Fusion > Import > Alembic Scene in

DaVinci Resolve’s Fusion page.

�Add an AlembicMesh3D node to the Node Editor.

The first method is the preferred method; both Alembic and FBX nodes by themselves import the

entire model as one object. However, the Import menu breaks down the model, lights, camera, and

animation into a string of individual nodes. This makes it easy to edit and modify and use subsections

of the imported Alembic mesh. Also, transforms in the file are read into Fusion splines and into the

Transform 3D nodes, which get saved with the comp. Later, when reloading the comp, the transforms

are loaded from the comp and not the Alembic file. Fusion handles the meshes differently, always

reloading them from the Alembic file.

Arbitrary user data varies depending on the software creating the Alembic file, and therefore this type

of metadata is mostly ignored.

Alembic Import Dialog

An Alembic Import dialog is displayed once you select the file to import

Alembic Import options


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

The top half of the Import dialog displays information about the selected file including the name of the

plugin/application that created the Alembic file, the version of the Alembic software developer kit used

during the export, the duration of the animation in seconds, if available, and the frame rate(s) in the file.

Various objects and attributes can be imported by selecting the checkboxes in the Import section.

�Hierarchy: When enabled, the full parenting hierarchy is recreated in Fusion using multiple

Transform 3D nodes. When disabled, the transforms in the Alembic file are flattened down into

the cameras and meshes. The flattening results in several meshes/cameras connected to a single

Merge node in Fusion. It is best to have this disabled when the file includes animation. If enabled,

the many rigs used to move objects in a scene will result in an equally large number of nodes in

Fusion, so flattening will reduce the number of nodes in your node tree.

�Orphaned Transforms: When the hierarchy option is enabled, an Orphaned Transforms setting is

displayed. Activating this Orphan Transforms setting imports transforms that parent a mesh or camera.

For example, if you have a skeleton and associated mesh model, the model is imported as an Alembic

mesh, and the skeleton as a node tree of Merge3Ds. If this is disabled, the Merge3Ds are not created.

�Cameras: When enabled, importing a file includes cameras along with Aperture, Angles of View,

Plane of Focus, as well as Near and Far clipping plane settings. The resolution Gate Fit may be

imported depending on whether the application used to export the file correctly tagged the

resolution Gate Fit metadata. If your camera does not import successfully, check the setting for the

Camera3D Resolution Gate Fit. Note that 3D Stereoscopic information is not imported.

�InverseTransform: Imports the Inverse Transform (World to Model) for cameras.

�Points: Alembic files support a Points type. This is a collection of 3D points with position

information. Some 3D software exports particles as points. However, keep in mind that while

position is included, the direction and orientation of the particles are lost.

�Meshes: This setting determines whether importing includes 3D models from the Alembic file.

If it is enabled, options to include UVs and normals are displayed.

Animation

This section includes one option for the Resampling rate. When exporting an Alembic

animation, it is saved to disk using frames per second (fps). When importing Alembic data

into Fusion, the fps are detected and entered into the Resample Rate field unless you have

changed it previously in the current comp. Ideally, you should maintain the exported frame

rate as the resample rate, so your samples match up with the original. The Detected Sampling

Rates information at the top of the dialog can give an idea of what to pick if you are unsure.

However, using this field, you can change the frame rate to create effects like slow motion.

Not all objects and properties in a 3D scene have an agreed upon universal convention in the

Alembic file format. That being the case, Lights, Materials, Curves, Multiple UVs, and Velocities

are not currently supported when you import Alembic files.

Since the FBX file format does support materials and lights, we recommend the use of FBX for

lights, cameras, and materials. Use Alembic for meshes only.

Inputs

The AlembicMesh3D node has two inputs in the Node Editor. Both are optional since the node is

designed to use the imported mesh.

SceneInput: The orange input can be used to connect an additional 3D scene or model. The imported

Alembic objects combine with the other 3D geometry.

MaterialInput: The optional green input is used to apply a material to the geometry by connecting a

2D bitmap image. It applies the connected image to the surface of the geometry in the scene.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Basic Node Setup

The AlembicMesh3D node is designed to be part of a larger 3D scene. Typically, when imported, a

3D geometry model is represented by one node, and any transforms are in another node. The nodes

imported as part of the Alembic file connect into a Merge 3D node along with a camera, lights, and

other elements that may be required for the scene.

Alembic node structure

Inspector

Alembic mesh 3D controls

Controls Tab

The first tab in the Inspector is the Controls tab. It includes a series of unique controls specific to

the Alembic Mesh 3D node as well as six groupings of controls that are common to most 3D nodes.

The Common Controls section at the end of this chapter includes detailed descriptions of the

common controls.

Below are descriptions of the Alembic Mesh 3D specific controls.

Filename

The complete file path of the imported Alembic file is displayed here. This field allows you to change

or update the file linked to this node.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Object Name

This text field shows the name of the imported Alembic mesh, which is also used to rename the

Alembic Mesh 3D node in the Node Editor.

When importing with the Alembic Mesh 3D node, if this text field is blank, the entire contents of the

Alembic geometry are imported as a single mesh. When importing geometry using File > Import >

Alembic Scene, this field is set by Fusion.

Wireframe

Enabling this option causes the mesh to display only the wireframe for the object in the viewer. When

enabled, there is a second option for wireframe anti-aliasing. You can also render these wireframes

out to a file if the Renderer 3D node has the OpenGL render type selected.

Common Controls

Controls, Materials, Transform, and Settings Tabs

The controls for Visibility, Lighting, Matte, Blend Mode, Normals/Tangents, and Object ID in the

Controls tab are common in many 3D nodes. The Materials tab, Transforms tab and Settings tab in the

Inspector are also duplicated in other 3D nodes. These common controls are described in detail at the

end of this chapter in “The Common Controls” section.

Bender 3D [3Bn]

The Bender 3D node

Bender 3D Introduction

The Bender 3D node is used to bend, taper, twist, or shear 3D geometry based on the geometry’s

bounding box. It works by connecting any 3D scene or object to the orange input on the Bender 3D

node, and then adjusting the controls in the Inspector. Only the geometry in the scene is modified.

Any lights, cameras, or materials are passed through unaffected.

The Bender node does not produce new vertices in the geometry; it only alters existing vertices in the

geometry. So, when applying the Bender 3D node to primitives, like the Shape 3D, or Text 3D nodes,

increase the Subdivision setting in the primitive’s node to get a higher-quality result.

Inputs

The following inputs appear on the Bender 3D node in the Node Editor.

SceneInput: The orange scene input is the required input for the Bender 3D node. You use this input

to connect another node that creates or contains a 3D scene or object.

Basic Node Setup

The Bender 3D node works by connecting a 3D node that contains geometry, like an image plane 3D,

Shape 3D or Text 3D. The element you connect to the Bender 3D node will be distorted based on the


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

controls in the Inspector. The Bender 3D node is designed to be part of a larger 3D scene, with the

output typically connecting into a Merge 3D.

Bender 3D node structure