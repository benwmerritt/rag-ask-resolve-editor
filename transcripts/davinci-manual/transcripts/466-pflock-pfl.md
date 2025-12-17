---
title: "pFlock [pFl]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 466
---

# pFlock [pFl]

The pFlock node

pFlock Node Introduction

The pFlock node can be used to simulate the behavior of organic systems, such as a flock of birds or

a colony of ants. Its use can make an otherwise mindless particle system appear to be motivated, or

acting under the direction of intelligence.

The pFlock node works through two basic principles. Each particle attempts to stay close to other

particles and each particle attempts to maintain a minimum distance from other particles.

The strength of these “desires” produces the seemingly motivated behavior perceived by the viewer.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Inputs

The pFlock node has a single orange input by default. Like most particle nodes, this orange input

accepts only other particle nodes. A green or magenta bitmap or mesh input appears on the node

when you set the Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange background input takes the output of other particle nodes.

Region: The green or magenta region input takes a 2D image or a 3D mesh depending on whether

you set the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is

selected first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area

where the flocking takes effect.

Basic Node Setup

When combined with pFollow, the pFlock node can produce natural swarming behaviors that

change direction.

A pFlock node applying more herd-type mentality to particles

Inspector

The pFlock controls

Randomize

The Random Seed slider and Randomize button are presented whenever a Fusion node relies on a

random result. Two nodes with the same seed values will produce the same random results. Click the

Randomize button to randomly select a new seed value, or adjust the slider to manually select a new

seed value.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Flock Number

The value of this control represents the number of other particles that the affected particle will attempt

to follow. The higher the value, the more visible “clumping” will appear in the particle system and the

larger the groups of particles will appear.

Follow Strength

This value represents the strength of each particle’s desire to follow other particles. Higher values will

cause the particle to appear to expend more energy and effort to follow other particles. Lower values

increase the likelihood that a given particle will break away from the pack.

Attract Strength

This value represents the strength of attraction between particles. When a particle moves farther from

other particles than the Maximum Space defined in the pFlock node, it will attempt to move closer

to other particles. Higher values cause the particle to maintain its spacing energetically, resolving

conflicts in spacing more rapidly.

Repel Strength

This value represents the force applied to particles that get closer together than the distance defined

by the Minimum Space control of the pFlock node. Higher values will cause particles to move away

from neighboring particles more rapidly, shooting away from the pack.

Minimum/Maximum Space

This range control represents the distance each particle attempts to maintain between it and other

particles. Particles will attempt to get no closer or farther than the space defined by the Minimum/

Maximum values of this range control. Smaller ranges will give the appearance of more organized

motion. Larger ranges will be perceived as disorganized and chaotic.

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.

pFollow [pFo]

The pFollow node

pFollow Node Introduction

Inserting the pFollow node into a particle branch causes the particles to spring back and forth toward

a follow object. The follow object can be positioned in 3D or animated to create a new motion path for

the particles.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Inputs

The pFollow node has a single orange input by default. Like most particle nodes, this orange

background input accepts only other particle nodes. A green bitmap or mesh input appears on the

node when you set the Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Region: The green or magenta region input takes a 2D image or a 3D mesh depending on whether

you set the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is

selected first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area

where particles will follow the position point.

Basic Node Setup

When combined with pFlock, the pFollow node can produce natural swarming behaviors that

change direction.

A pFollow node introduces a follow object that influences the particles’ motion.

Inspector

The pFollow Controls tab

Random Seed

The Random Seed slider and Randomize button are presented whenever a Fusion node relies on a

random result. Two nodes with the same seed values will produce the same random results. Click the

Randomize button to randomly select a new seed value, or adjust the slider to manually select a new

seed value.

Position XYZ

The position controls are used to create the new path by positioning the follow object. Moving the

XYZ parameters displays the onscreen position of the follow object. Animating these parameters

creates the new path the particles will be influenced by.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Spring

The Spring setting causes the particles to move back and forth along the path. The spread of

the spring motion increases over the life of the particles depending on the distance between the

particles and the follow object. Higher spring settings increase the elasticity, while lower settings

decrease elasticity.

Dampen

This value attenuates the spring action. A lower setting offers less resistance to the back and forth

spring action. A higher setting applies more resistance.

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.

pFriction [pFr]

The pFriction node

pFriction Node Introduction

The pFriction node applies resistance to the motion of a particle, slowing the particle’s motion through

a defined region. This node produces two types of Friction. One type reduces the velocity of any

particle intersecting/crossing the defined region, and one reduces or eliminates spin and rotation.

Inputs

The pFriction node has a single orange input by default. Like most particle nodes, this orange input

accepts only other particle nodes. A green or magenta bitmap or mesh input appears on the node

when you set the Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Region: The green or magenta region input takes a 2D image or a 3D mesh depending on whether

you set the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is

selected first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area

where the friction occurs.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION