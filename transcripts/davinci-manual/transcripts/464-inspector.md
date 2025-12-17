---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 464
---

# Inspector

All the same operators, functions, and conditional statements described for the Custom node apply

to the pCustom node as well, including Pixel-read functions for the two image inputs (e.g., getr1w(x,y),

getz2b(x,y), and so on).

The pCustom controls

Number 1-8

Numbers are variables with a dial control that can be animated or connected to modifiers exactly as

any other control might. The numbers can be used in equations on particles at current time: n1, n2,

n3, n4, … or at any time: n1_at(float t), n2_at(float t), n3_at(float t), n4_at(float t), where t is the time you

want. The values of these controls are available to expressions in the Setup and Intermediate tabs.

pCustom Position tab


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Position 1-8

These eight point controls include 3D X,Y,Z position controls. They are normal positional controls and

can be animated or connected to modifiers as any other node might. They are available to expressions

entered in the Setup, Intermediate, and Channels tabs.

pCustom Setup tab

Setup 1-8

Up to eight separate expressions can be calculated in the Setup tab of the pCustom node. The Setup

expressions are evaluated once per frame, before any other calculations are performed. The results

are then made available to the other expressions in the node as variables s1, s2, s3, and s4.

Think of them as global setup scripts that can be referenced by the intermediate and channel scripts.

pCustom Intermediate tab


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Inter 1-8

An additional eight expressions can be calculated in the Intermediate tab. The Intermediate

expressions are evaluated once per frame, after the Setup expressions are evaluated. Results are

available as variables i1, i2, i3, i4, i5, i6, i7, i8, which can be referenced by channel scripts.

Particle

Particle position, velocity, rotation, and other controls are available in the Particle tab.

The following particle properties are exposed to the pCustom control:

px, py, pz

particle position on the x, y, and z axis

vx, vy, vz

particle velocity on the x, y and z axis

rx, ry, rz

particle rotation on the x, y, and z axis

sx, sy, sz

particle spin on the x, y, and z axis

pxi1, pyi1

the 2d position of a particle, corrected for image 1’s aspect

pxi2, pyi2

the 2d position of a particle, corrected for image 2’s aspect

mass

not currently used by anything

size

the current size of a particle

id

the particle’s identifier

r, g, b, a

the particles red, green, blue and alpha color values

rgnhit

this value is 1 if the particle hit the pCustom node’s defined region

rgndist

this variable contains the particles distance from the region

condscale

the strength of the region at the particle’s position

rgnix, rgniy, rgniz

values representing where on the region the particle hit

rgnnx, rgnny, rgnnz

region surface normal of the particle when it hit the region

w1, h1

image 1 width and height

w2 h2

image 2 width and height

i1, i2, i3, i4

the result of the intermediate calculations 1 through 4

s1, s2, s3, s4

the result of the setup calculations 1 through 4

n1..n8

the values of numeric inputs 1 through 8

p1x, p1y, p1z .. p4x, p4y, p4z

the values of position inputs 1 through 4

time

the current time or frame of the compositions

age

the current age of the particle

lifespan

the lifespan of the current particle

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

pCustomForce [pCF]

The pCustom Force node

pCustom Force Node Introduction

The pCustom Force node allows you to change the forces applied to a particle system or subset. This

node is one of the most complex and the most powerful node in Fusion. If you are experienced with

scripting or C++ programming, you should find the structure and terminology used by the Custom

Force node to be familiar.

The forces on a particle within a system can have their positions and rotations affected by forces. The

position in XYZ and the Torque, which is the spin of the particle, are controlled by independent custom

equations. The Custom Force node is used to create custom expressions and filters to modify the

behavior. In addition to providing three image inputs, this node will allow for the connection of up to

eight numeric inputs and as many as four XY position values from other controls and parameters in the

node tree.

Inputs

The pCustom Force node has three inputs. Like most particle nodes, this orange input accepts only

other particle nodes. A green and magenta are 2D image inputs for custom image calculations.

Optionally there are teal or white bitmap or mesh inputs, which appear on the node when you set the

Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Image 1 and 2: The green and magenta image inputs accept 2D images that are used for per-pixel

calculations and compositing functions.

Region: The teal or white region input takes a 2D image or a 3D mesh depending on whether you set

the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is selected

first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area where the

pCustom Force takes effect.

Basic Node Setup

The pCustom Force node is inserted between a pEmitter and pRender node to serve as a catalyst for

particles using advanced C++ and scripting.

A pCustom Force is applied to the particles generated by the pEmitter.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Inspector

The pCustom Force controls

The tabs and controls located in the Inspector are similar to the controls found in the pCustom node.

Refer to the pCustom node in this chapter for more information.

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.

pDirectionalForce [pDF]

The pDirectional Force node

pDirectional Force Node Introduction

This node applies a unidirectional force that pulls the affected particles in a specified direction.

Its primary controls affect the strength of the force, and the angle of the force’s pull along the

X, Y, and Z axis.

Since the most common use of this node is to simulate gravity, the default direction of the pull is down

along the Y axis (-90 degrees), and the default behavior is to ignore regions and affect all particles.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION