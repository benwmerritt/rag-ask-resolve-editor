---
title: "pSpawn [pSp]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 470
---

# pSpawn [pSp]

The pSpawn node

pSpawn Node Introduction

The pSpawn node makes each affected particle act as an emitter that can produce one or more

particles of its own. The original particle continues until the end of its lifespan, and each of the

particles it emits becomes wholly independent with a lifespan and properties of its own.

As long as a particle falls under the effect of the pSpawn node, it will continue to generate particles.

It is important to restrict the effect of the node with limiters like Start and End Age, Probability, Sets

and Regions, and by animating the parameters of the emitter so that the node is operative only

when required.

Inputs

By default, the pSpawn node has a single orange input. Like most particle nodes, this orange input

accepts only other particle nodes. You can enable an image input by selecting Bitmap from the Style

menu in the Style tab. Also, two region inputs, one for bitmap and one for mesh, appear on the node

when you set the Region menu in the Region tab to either Bitmap or Mesh. The colors of these inputs

change depending on the order they are enabled.

Input: The orange input accepts the output of other particle nodes.

Style Bitmap Input: This image input accepts a 2D image to use as the particles’ image. Since this

image duplicates into potentially thousands of particles, it is best to keep these images small and

square—for instance, 256 x 256 pixels.

Region: The region inputs take a 2D image or a 3D mesh depending on whether you set the

Region menu to Bitmap or Mesh. The color of the input is determined by whichever is selected

first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area where the

particles are emitted.

Basic Node Setup

The pSpawn node is placed between the pEmitter and pRender nodes. Using the Age parameter in

the pSpawn’s Conditions tab, you can spawn new particles as the old ones die off. This is one way to

have a trail of particles shoot up in the air like a rocket and burst into sparkling fireworks.

A pSpawn node used to generate new particles at specific points in the old particles’ life


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Inspector

The pSpawn node has a large number of controls, most of which exactly duplicate those found within

the pEmitter node. There are a few controls that are unique to the pSpawn node, and their effects are

described below.

The pSpawn controls

Affect Spawned Particles

Selecting this checkbox causes particles created by spawning to also become affected by the pSpawn

node on subsequent frames. This can exponentially increase the number of particles in the system,

driving render times up to an unreasonable degree. Use this checkbox cautiously.

Velocity Transfer

This control determines how much velocity of the source particle is transferred to the particles it

spawns. The default value of 1.0 causes each new particle to adopt 100 percent of the velocity

and direction from its source particle. Lower values will transfer less of the original motion to the

new particle.

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

pTangent Force [pTF]

The pTangent Force node

pTangent Force Node Introduction

This node is used to apply a tangential force to the particles—a force that is applied perpendicularly to

the vector between the pTangent Force’s region and the particle it is affecting.

Inputs

The pTangent Force node has a single orange input by default. Like most particle nodes, this orange

input accepts only other particle nodes. A green bitmap or mesh input appears on the node when you

set the Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Region: The green or magenta region input takes a 2D image or a 3D mesh depending on whether

you set the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is

selected first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area

where the tangent force effects the particles.

Basic Node Setup

The pTangent Force node is inserted between a pEmitter and a pRender node.

The pTangent Force node positions a tangent force that particles maneuver around.

Inspector

The pTangent Force controls


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

The controls for this node are used to position the offset in 3D space and to determine the strength of

the tangential force along each axis independently.

Randomize

The Random Seed slider and Randomize button are presented whenever a Fusion node relies on a

random result.

Two nodes with the same seed values will produce the same random results. Click the Randomize

button to randomly select a new seed value, or adjust the slider to manually select a new seed value.

X, Y, Z Center Position

These controls are used to represent the X, Y, and Z coordinates of the Tangent force in 3D space.

X, Y, Z Center Strength

These controls are used to determine the Strength of the Tangent force in 3D space.

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.

pTurbulence [pTr]

The pTurbulence node

pTurbulence Node Introduction

The pTurbulence node imposes a frequency-based chaos on the position of each particle, causing

the motion to become unpredictable and uneven. The controls for this node affect the strength and

density of the Turbulence along each axis.

Inputs

The pTurbulence node has a single orange input by default. Like most particle nodes, this orange input

accepts only other particle nodes. A green bitmap or mesh input appears on the node when you set

the Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Region: The green or magenta region input takes a 2D image or a 3D mesh depending on whether

you set the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is

selected first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area of

turbulence.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Basic Node Setup

The pTurbulence node is inserted between a pEmitter and a pRender node.

The pTurbulence node disturbs the rigid flow of particles for a more natural motion.

Inspector

The pTurbulence controls

Randomize

The Random Seed slider and Randomize button are presented whenever a Fusion node relies on a random

result. Two nodes with the same seed values will produce the same random results. Click the Randomize

button to randomly select a new seed value, or adjust the slider to manually select a new seed value.

X, Y, and Z Strength

The Strength control affects the amount of chaotic motion imparted to particles.

Strength Over Life

This mini Spline Editor control can be used to control the amount of turbulence applied to a particle

according to its age. For example, a fire particle may originally have very little turbulence applied at

the start of its life, and as it ages, the turbulence increases.

Density

Use this control to adjust the density in the turbulence field. Lower values causes more particle cells

to be affected similarly, almost as if “waves” of the turbulence field run through the particles, affecting

groups of cells at the same time. Higher values add finer variations to more individual particle cells

causing more of a spread in the turbulence field.

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION