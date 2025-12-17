---
title: "The Elements of a 3D Scene"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 326
---

# The Elements of a 3D Scene

All 3D nodes can be divided into a number of categories.

Geometry Nodes

You can add 3D geometry to a composition using the ImagePlane3D node, the Shape3D node, the

Cube3D node, the Text3D node, or optionally by importing a model via the FBX Mesh 3D node.

Furthermore, you can add particle geometry to scenes from pEmitter nodes. You can connect

these to a Merge3D node either singularly or in multiples to create sophisticated results combining

multiple elements.

A more complex 3D scene combining several geometry nodes

including the Text3D, Shape3D, and ImagePlane3D nodes

Texturing Geometry

By itself, geometry nodes can only consist of a simple flat color. However, you can alter the look of 3D

geometry by texturing it using clips (either still images or movies), using material nodes such as the

Blinn and Phong nodes to create more sophisticated textures with combinations of 2D images and

environment maps, or you can use a preset shader from the Templates > Shader bin of the Effects

Library, which contains materials and texture presets that are ready to use.

If you’re working with simple geometric primitives, you can texture them by connecting either an image

(a still image or movie) or a shader from the Templates bin of the Effects Library directly to the material

input of a Shape3D, Cube3D, or other compatible node, as shown below.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

An image connected to the material input of a Shape3D node set to

Torus, with the image (left), and the shaded torus (right)

If you’re shading or texturing Text3D nodes, you need to add a texture in a specific way since each

node is actually a scene with individual 3D objects (the characters) working together. In the following

example, the RustyMetal shader preset is applied to a Text3D node using the ReplaceMaterial3D

node. The interesting thing about the ReplaceMaterial3D node is that it textures every geometric

object within a scene at once, meaning that if you put a ReplaceMaterial3D node after a Text3D node,

you texture every character within that node. However, if you place a ReplaceMaterial3D node after

a Merge3D node, then you’ll end up changing the texture of every single geometric object being

combined within that Merge3D node, which is quite powerful.

The geometry created by a Text3D node is textured using a shader connected to a

ReplaceMaterial3D node that’s connected downstream of the object you want to shade


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

The Merge3D Node

The Merge3D node combines the output of one or more 3D nodes into a single scene. Unlike the

Merge2D node, the ordering of elements in the scene is not restricted to only background and

foreground inputs. Instead, the Merge3D node lets you connect an unlimited number of inputs, with

the resulting output combined according to each object’s absolute position in 3D space.

Merging many objects together in a

3D scene using the Merge3D node

Combining Objects Directly

While the Merge3D node provides a structured way of combining objects, you can also combine

3D objects such as Text3D and Shape3D nodes by connecting the output of one 3D object node

to the input of another, as seen in the following screenshot. When you do this, you must use each

node’s internal transform parameters to transform their position, size, and rotation directly, but the

transform control of downstream 3D object nodes also transforms all upstream 3D object nodes. This

even works for lights and the Camera3D node, giving you a fast way of combining a set of objects

that always go together, which you can later connect to a Merge3D node for additional lighting and

eventual connection to a Renderer3D node.

Connecting one Shape3D node to another

directly to combine them Transforming

the last downstream 3D object also

transforms all upstream objects; the last

Shape3D node is viewed, showing both


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Combining Multiple Merge3D Nodes

Furthermore, Merge3D nodes can be combined with other Merge3D nodes, allowing you to

create composite 3D scenes made up of multiple “sub-scenes,” each put together within individual

Merge3D nodes.

You can build elaborate scenes using multiple Merge3D nodes connected together

Lighting Multiple Merge3D Nodes

Once you’ve combined multiple Merge3D nodes, there’s an easy way to control how lights that

are connected to upstream Merge3D nodes affect the results of other Merge3D nodes connected

downstream. Each Merge3D node’s Controls tab contains a single checkbox, Pass Through Lights,

which enables lighting to pass through the output of an upstream Merge3D node in order to shine

onto objects connected to downstream Merge3D nodes.

You can light downstream Merge3D scenes with lights connected

to upstream Merge3D scenes by turning on Pass Through Lights

This checkbox is disabled by default, which lets you light elements in one Merge3D scene without

worrying about how the lighting will affect geometry attached to other Merge3D nodes further

downstream. For example, you may want to apply a spotlight to brighten the wall of a building in one

Merge3D node without having that spotlight spill over onto the grass or pavement at the foot of the

wall modeled in another Merge3D node. In the example shown below, the left image shows how the

cone and torus connected to a downstream node remain unlit by the light in an upstream node with

Pass Through Lights disabled, while the right image shows how everything becomes lit when turning

Pass Through Lights on.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

The result of lights on the text in one Merge3D node not affecting the cone and torus added

in a downstream Merge3D node (left). Turning on Pass Through Lights in the upstream

Merge3D node results in those lights also illuminating the downstream shapes (right).

Transforming Merge3D Scenes

Each Merge3D node includes a Transform tab. These transform parameters adjust the position, scale,

and rotation of all objects being combined within that Merge3D node together, including lighting

and particles. All transformations take place around a common pivot point. This forms the basis of

parenting in the 3D environment.

The Transform tab of a Merge3D node

If you transform a Merge3D node that’s connected to other Merge3D nodes, what happens depends

on which node you’re transforming, an upstream node or the downstream node:

�If you transform a downstream Merge3D node, you also transform all upstream nodes connected

to it as if they were all a single scene.

�If you transform an upstream Merge3D node, this has no effect on downstream Merge3D nodes,

allowing you to make transforms specific to that particular node’s scene.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Transforming Upstream, Lighting Downstream

When building complex scenes using multiple Merge3D nodes being combined together, it’s common

to use one last downstream node to combine light and camera nodes to illuminate the final scene,

while leaving the upstream Merge3D nodes free for controlling object transforms and animation. This

way, you can transform and animate subsets of your overall scene without worrying about accidentally

altering the overall lighting scheme or cameras for that scene, unless you’ve specifically connected

lights or cameras upstream that are meant to be attached to the geometry you’re transforming.

An example of a 3D scene using multiple Merge3D nodes working together; the upstream Merge3D nodes arrange

the 3D objects placed within the scene, while the last Merge3D node (orange) lights and frames the scene.