---
title: "Anatomy of a Simple Particle System"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 339
---

# Anatomy of a Simple Particle System

The simplest particle system you can create is a pEmitter node connected to a pRender node. The

pEmitter node includes the core controls for creating various kinds of particles in different ways, while

the pRender node is required to render a 2D or 3D result that can be composited with other scenes

within your composition.

The minimum node tree required to create a simple particle system

If your needs are more complicated, you can combine two or more pEmitter nodes using a pMerge

node (the particle system version of a Merge node), to create compound particle systems where

multiple types of particles combine with one another to create a result.

Compositing two pEmitter nodes to create a compound particle

system, combining two kinds of particles together

If you’re trying to create particle systems with more natural effects, you can add “forces” to each

emitter. These forces are essentially physics or behavioral simulations that automatically cause the

particles affected by them to be animated with different kinds of motion, or to be otherwise affected

by different objects within scenes.

Customizing the effect of pEmitter nodes using different forces

to add complexity to the particle animation

You can also attach the following types of nodes to a pEmitter node to deeply customize a

particle system:

�Attach a 2D image to a pEmitter node to create highly customized particle shapes. Make sure your

image has an appropriate alpha channel.

�Attach a Shape3D or other 3D geometry node to a pEmitter node to create a more specific region

of emission (by setting Region to Mesh in the Region tab).


Fusion Fundamentals | Chapter 87 Particle Systems

FUSION

Customizing pEmitter nodes using mesh geometry to define

regions and 2D images to define particle shape

The above examples assume that you’ll output 2D renders to combine into the rest of a

2D composition. However, because particle systems are fully 3D, you also have the option

of outputting your particle system in such a way as to be used from within other 3D scenes

in your composition.

Connecting a particle system to a Merge3D node so the particles

are subject to lighting and shadows within a 3D scene

The Output Mode of the pRender node, at the very top of the controls exposed in the Inspector, can

be set to either 2D or 3D, depending on whether you want to combine the result of the particle system

with 2D layers or with objects in a 3D scene.

Choosing whether a particle system’s output is 2D

or 3D in the pRender node’s Inspector controls


Fusion Fundamentals | Chapter 87 Particle Systems

FUSION

If you connect a pRender node to a Merge3D node, the Output Mode is locked to 3D, meaning that 3D

geometry is output by the pRender node for use within the Merge3D node’s scene. This means that

the particles can be lit, they can cast shadows, and they can interact with 3D objects within that scene.

The result of using a particle system within a 3D scene

NOTE: Once you set the pRender node to either 2D or 3D and make any change to the

nodes in the Inspector, you cannot change the output mode.

Particle System Distribution

To adjust the distribution of particles being emitted, select the pEmitter node to expose its controls in

the Inspector, then open the Velocity controls in the Controls tab, and use the Angle, Angle Variance,

Angle Z, and Angle Z Variance controls to adjust the direction and width over which particles are

emitted. All these controls can be animated.

A pEmitter node’s Velocity Angle and Angle

Variance controls let you adjust the direction

and width of particle distribution


Fusion Fundamentals | Chapter 87 Particle Systems

FUSION

Particle systems can be positioned and rotated by loading the pEmitter nodes that generate

particles into a viewer and using the onscreen 3D position and Rotation controls provided to move

the particle system around.

A pEmitter node loaded into the viewer with the rotation onscreen controls enabled

Alternatively, you can use the controls of the pEmitter’s Region tab in the Inspector to adjust

Translation, Rotation, and Pivot. All these controls can be animated.

A pEmitter node’s Region controls open in the Inspector


Fusion Fundamentals | Chapter 87 Particle Systems

FUSION

Particle Nodes Explained by Type

This section introduces the four types of particle system nodes available in the Effects Library.

Emitters

pEmitter nodes are the source of all particles. Each pEmitter node can be set up to generate a single

type of particle with enough customization so that you’ll never create the same type of particle

twice. Along with the pRender node, this is the only other node that’s absolutely required to create a

particle system.

pEmitter nodes have four parameters tabs:

Controls: The primary controls governing how many particles are generated (Number), how

long they live (Lifespan), how fast they move (Velocity) and how widely distributed they are

(Angle and Angle Variance), their rotation (Rotation Mode with X, Y, and Z controls), and

whether there’s spin (Spin X, Y, and Z controls). For each parameter of particle generation,

there’s an accompanying Variance control that lets you make that parameter less uniform and

more natural by introducing random variation.

Sets: This tab contains settings that affect the physics of the particles emitted by the node.

These settings do not directly affect the appearance of the particles. Instead, they modify

behaviors such as velocity, spin, quantity, and lifespan.

Style: While the Controls tab has a simple control for choosing a color for particles, the Style

tab has more comprehensive controls including color variance and Color Over Life controls.

Additionally, size controls including Size Over Life, fade controls, and blur controls let you

create sophisticated particle animations with a minimum of adjustments, while Merge controls

give you an additional level of control over how overlapping particles combine visually. A set

of controls at the bottom lets you choose how animated effects are timed.

Region: The Region tab lets you choose what kind of geometric region is used to disperse

particles into space and whether you’re emitting particles from the region’s volume or surface.

The Winding Rule and Winding Ray Direction controls determine how the mesh region will

handle particle creation with geometric meshes that are not completely closed, as is common

in many meshes imported from external applications. Tweaking these last parameters is

common when using imported mesh geometry as a region for emitting particles, since even

geometry that appears closed will frequently appear to “leak” particles thanks to improperly

welded vertices.

Forces

Many of the particle nodes found in the Particles bin of the Effects Library are “forces” that enhance

a particle simulation by simulating the effect of various forces acting upon the particles generated by

an emitter.

Some forces, including pDirectionalForce, pFlock, pFriction, pTurbulence, and pVortex, are rules that

act upon particles without the need for any other input. These are simply “acts of nature” that cause

particles to behave in different ways.

Other forces, such as pAvoid, pBounce, pFollow, and pKill, work in conjunction with 3D geometry in

a scene such as shapes or planes to cause things to happen when a particle interacts or comes near

that geometry. Note that some of the particles described previously can also use geometry to direct

their actions, so these two categories of forces are not always that clear-cut.


Fusion Fundamentals | Chapter 87 Particle Systems

FUSION