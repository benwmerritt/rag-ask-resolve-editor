---
title: "Geometry"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 333
---

# Geometry

There are five nodes used for creating geometry in Fusion. These nodes can be used for a variety

of purposes. For instance, the Image Plane 3D is primarily used to place image clips into a 3D scene,

while the Shapes node can add additional building elements to a 3D set, and Text 3D can add three-

dimensional motion graphics for title sequences and commercials. Although each node is covered in

more detail in the “3D Nodes” chapter, a summary of the 3D creation nodes is provided below.

�Cube 3D

The Cube 3D creates a cube with six inputs that allow mapping of different textures to each of the

cube’s faces.

�Image Plane 3D

The Image Plane 3D is the basic node used to place a 2D image into a 3D scene with an

automatically scaled plane.

�Shape 3D

This node includes several basic primitive shapes for assembling a 3D scene. It can create planes,

cubes, spheres, cylinders, cones, and toruses.

�Text 3D

The Text 3D is a 3D version of the Text+ node. This version supports beveling and extrusion but

does not have support for the multi-layered shading model available from Text+.

�Particles

When a pRender node is connected to a 3D view, it will export its particles into the 3D environment.

The particles are then rendered using the Renderer3D instead of the Particle renderer.

For more information, see Chapter 114, “Particle Nodes,” in the DaVinci Resolve Reference

Manual or Chapter 54 in the Fusion Reference Manual.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Common Visibility Parameters

Visibility parameters are found in the Controls tab of most 3D geometry-producing nodes, exposed

via a disclosure control. These parameters let you control object visibility in the viewers and in the

final render.

A 3D geometry node’s visibility parameters

�Visible

If the Visibility checkbox is not selected, the object will not be visible in a viewer, nor will it be

rendered into the output image by a Renderer3D. A non-visible object does not cast shadows.

This is usually enabled by default, so objects that you create are visible in both the viewers and

final renders.

�Unseen by Cameras

If the Unseen by Cameras checkbox is selected, the object will be visible in the viewers but

invisible when viewing the scene through a camera, so the object will not be rendered into the

output image by a Renderer3D. Shadows cast by an Unseen object will still be visible.

�Cull Front Face/Back Face

Use these options to cull (exclude) rendering of certain polygons in the geometry. If Cull Back Face

is selected, all polygons with normals pointing away from the view will not be rendered and will

not cast shadows. If Cull Front Face is selected, all polygons with normals pointing away from the

view will likewise be excluded. Selecting both checkboxes has the same effect as deselecting the

Visible checkbox.

�Ignore Transparent Pixels in Aux Channels

For any piece of geometry, the Renderer3D rejects transparent pixels in the auxiliary image

channels. The reason this is the default is to prevent aux channels (e.g., normals, Z-channel, UVs)

from filling in where there should be blank space or full transparency. For example, suppose in

post you want to add some fog to the rendered image. If you had fully transparent geometry in

the foreground affecting the Z-channel, you would get incorrect fog rendering. By deselecting

this checkbox, the transparency will not be considered and all the aux channels will be filled for

all the pixels. This could be useful if you wanted to replace texture on a 3D element that is fully

transparent in certain areas with a texture that is transparent in different areas; it would be useful

to have the whole object set aux channels (in particular UVs).

Adding FBX Models

The Filmbox FBX format is a scene interchange format that facilitates moving 3D scene information

from one application to another. Fusion’s FBX format support extends model import support to other

3D files such as Collada and OBJ.

Importing an FBX Scene

To import an entire FBX scene, you add an FBXMesh3D node to your node tree. After being prompted

to choose a scene or object file, Fusion imports it to create a composition with the same lights,

cameras, materials, and geometry found in an FBX file.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

An imported model, via the FBXMesh3D node

FBX Scene Import Dialog

The FBX Mesh node is used to import mesh geometry from an FBX file. The first texture applied to a

mesh will also be imported, if available.

Since different 3D applications use different units to measure their 3D scenes, the imported geometry

may be enormous compared to the rest of the scene, because Fusion treats its scale of measurement

as equal to its own system. For example, if your 3D application defaults to using millimeters as its

scale, an object that was 100 millimeters in size will import as a massive 100 units.

You can use the Size slider in the FBX Mesh Inspector parameters to reduce the scale of such files to

something that matches Fusion’s 3D scene.

FBX Exporter

You can export a 3D scene from Fusion to other 3D packages using the FBX Exporter node. On

render, it saves geometry, cameras lights, and animation into different file formats such as .dae or .fbx.

The animation data can be included in one file, or it can be baked into sequential frames. Textures and

materials cannot be exported.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Using Text3D

The Text3D node is probably the most ubiquitous node employed by motion graphics artists looking

to create titles and graphics from Fusion. It’s a powerful node filled with enough controls to create

nearly any text effect you might need, all in three dimensions. This section seeks to get you started

quickly with what the Text3D node is capable of.

For more information, see Chapter 89, “3D Nodes,” in the DaVinci Resolve Reference Manual

or Chapter 29 in the Fusion Reference Manual.

Assembling Text Objects

Each Text3D node is a self-contained scene within which each character of text is an individual object.

Because of this, the ideal way to combine numerous text objects that you might want to animate or

style independently from one another is to connect as many Text3D objects as you want to be able to

independently animate or style to one or more Merge3D nodes.

Merging multiple text objects to create

an intricately styled scene

TIP: If you click the Text icon in the toolbar to create a Text3D node, and then you click it

again while the Text3D node you just created is selected, a Merge3D node is automatically

created and selected to connect the two. If you keep clicking the Text icon, more Text3D

nodes will be added to the same selected Merge3D node.

Entering Text

When you select a Text3D node and open the Inspector, the Text tab shows a “Styled Text” text entry

field at the very top into which you can type the text you want to appear onscreen. Below, a set of

overall styling parameters are available to set the Font, Color, Size, Tracking, and so on. All styling you

do in this tab affects the entire set of text at once, which is why you need multiple text objects if you

want differently styled words in the same scene.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

The text entry and styling parameters in the Text tab

Near the bottom of the Text tab are the Extrusion parameters, available within a disclosure control.

The Extrusion parameters near the bottom of the Text tab

By default, all text created with the Text3D node is flat, but you can use the Extrusion Style,

Extrusion Depth, and various Bevel parameters to give your text objects thickness.

Unextruded text (left), and Extruded text (right)

Positioning and Transforming Text

By default, every new Text3D node is positioned at 0, 0, 0, so when you add multiple Text3D nodes,

they’re all in the same place. Fortunately, every Text3D node has built-in transform controls in the

Transform tab.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Text3D nodes also have Transform parameters built-in

Additionally, selecting a Text3D node exposes all the onscreen transform controls discussed

elsewhere in this chapter. Using these controls, you can position and animate each text object

independently.

Repositioned text objects to create a title sequence

Combining Text3D nodes using Merge3D nodes doesn’t just create a scene; it also enables

you to transform your text objects either singly or in groups:

Selecting an individual Text3D node or piece of text in the viewer lets you move that one text

object around by itself, independently of other objects in the scene.

Selecting a Merge3D node exposes a transform control that affects all objects connected to

that Merge3D node at once, letting you transform the entire scene.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Layout Parameters

The Layout tab presents parameters you can use to choose how text is drawn: on a straight line, a

frame, a circle, or a custom spline path, along with contextual parameters that change depending on

which layout you’ve selected (all of which can be animated).

Text using two different layouts

“Sub” Transforms

Another Transform tab (which the documentation has dubbed the “Sub” Transform tab) lets you apply

a separate level of transform to either characters, words, or lines of text, which lets you create even

more layout variations. For example, choosing to Transform by Words lets you change the spacing

between words, rotate each word, and so on. You can apply simultaneous transforms to characters,

words, and lines, so you can use all these capabilities at once if you really need to go for it. And, of

course, all these parameters are animatable.

Transforming individual words in two different ways

Shading

The Shading tab lets you shade or texture a text object using standard Material controls.

Shading controls for text objects


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION