---
title: "Setting the Origin"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 338
---

# Setting the Origin

When it comes time to add and position new objects into your 3D scene, you can make it easier by

setting the origin or center location.

To set the origin of the 3D scene, do the following:


Move to a frame that clearly shows the area you want to select as the center of the scene.


In the viewer, either select a single point or drag a selection box around a few marks located

where you want to position the center of the 3D scene.


In the inspector Origin section, click the Set from Selection button.

Setting the Scale

The Camera Tracker has no idea of the size of the 3D scene, so the scale parameter is used to scale

the scene output. This makes it possible to match the scale of two or more clips.

Realign the Scene

Before exporting the scene from the Camera Tracker, you must set the 3D scene Transform menu

back to Aligned. Now you’re ready to export.

Viewing the Exported Results

Clicking the Export button at the top of the Inspector creates a functional 3D scene with five new

nodes automatically added to the node tree.

�Camera 3D

�Point Cloud

�Ground Plane

�Merge 3D

�Camera Tracker Renderer (3D Renderer)


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION

Five nodes created as a result of exporting from the Camera Tracker

To work with the 3D scene, you can select the Merge 3D and load it into one of the viewers, and then

select the Camera Tracker Renderer and load that into a second viewer.

Viewing the Merge 3D shows the point cloud, ground plane, and camera


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION

When the Merge 3D is selected, a toolbar above the viewer can add 3D test geometry like an image

plane or cube to verify the precision of the 3D scene and camera. You can then connect actual

3D elements into the Merge 3D as you would any manually created 3D scene. The point cloud can

help align and guide the placement of objects, and the CameraTracker Renderer is a Renderer 3D

node with all the same controls.

Use the point cloud to accurately place different elements into a 3D scene

At this point, there is no need for the Camera Tracker node unless you find that you need to rerun the

solver. Otherwise, you can save some memory by deleting the Camera Tracker node.


Fusion Fundamentals | Chapter 86 3D Camera Tracking

FUSION

Chapter 87

Particle Systems

This chapter is designed to give you a brief introduction to the creation of fully

3D particle systems, one of Fusion’s most powerful features.

Once you understand these basics, for more Information on each particle system node that’s

available, see Chapter 114, “Particle Nodes,” in the DaVinci Resolve Reference Manual or

Chapter 54 in the Fusion Reference Manual.

Contents

Introduction to Particle Systems������������������������������������������������������������������������������������������������������������������������������������������������ 1846

Anatomy of a Simple Particle System��������������������������������������������������������������������������������������������������������������������������������������� 1847

Particle System Distribution��������������������������������������������������������������������������������������������������������������������������������������������������������� 1849

Particle Nodes Explained by Type���������������������������������������������������������������������������������������������������������������������������������������������� 1851

Emitters����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1851

Forces�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1851

Compositing������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1852

Rendering����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1852

Example Particle Systems�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1852


Fusion Fundamentals | Chapter 87 Particle Systems

FUSION

Introduction to Particle Systems

Particle systems are computer simulations that use customizable rules to automatically generate and

animate large numbers of elements to simulate smoke, dust, fire, leaves, sparks, or any other animated

system of shapes. As Fusion is a full-featured 3D compositing environment, particle systems can be

created in 2D or 3D, which makes them incredibly flexible and capable of producing all kinds of visual

effects or abstract animated content for use in motion graphics.

A 3D particle system, also created entirely within Fusion

The three most fundamental nodes required for creating particle systems are found on the toolbar.

As with the 3D nodes to the right, these are arranged, from left to right, in the order in which they must be

connected to work, so even if you can’t remember how to hook up a simple particle system, all you need

to do is click the three particle system nodes from left to right to create a functional particle system.

The pEmitter, pMerge, and pRender particle

system nodes available from the toolbar

However, these three nodes are only the tip of the iceberg. Opening the Particle category in the

Effects Library reveals many, many particle nodes designed to work together to create increasingly

complex particle interactions.

A sample of the nodes available in the

Particles bin of the Effects Library


Fusion Fundamentals | Chapter 87 Particle Systems

FUSION

All particle nodes begin with the letter “p,” and they’re designed to work together to produce

sophisticated effects from relatively simple operations and settings. The next section shows different

ways particle nodes can be connected to produce different effects.