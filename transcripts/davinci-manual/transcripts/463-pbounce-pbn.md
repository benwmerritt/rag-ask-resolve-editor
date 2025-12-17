---
title: "pBounce [pBn]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 463
---

# pBounce [pBn]

The pBounce node

pBounce Node Introduction

The pBounce tool is used to create a region from which affected particles will bounce off when they

come into contact.

Inputs

The pBounce node has a single orange input by default. Like most particle nodes, this orange input

accepts only other particle nodes. A green or magenta bitmap or mesh input appears on the node

when you set the Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Region: The green or magenta region input takes a 2D image or a 3D mesh depending on whether

you set the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is

selected first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area

particles bounce off.

Basic Node Setup

The pBounce node is placed in between the pEmitter and pRender. A Shape 3D node is used to

create the region the particles bounce off.

A pBounce node using a Shape 3D node as the region on which particles bounce off


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Inspector

The pBounce controls

Randomize

The Random Seed slider and Randomize button are presented whenever a Fusion node relies on a

random result.

Two nodes with the same seed values will produce the same random results. Click the Randomize

button to randomly select a new seed value, or adjust the slider to manually select a new seed value.

Elasticity

Elasticity affects the strength of a bounce, or how much velocity the particle will have remaining after

impacting upon the Bounce region. A value of 1.0 will cause the particle to possess the same velocity

after the bounce as it had entering the bounce. A value of 0.1 will cause the particle to lose 90% of its

velocity upon bouncing off of the region.

The range of this control is 0.0 to 1.0 by default, but greater values can be entered manually. This will

cause the particles to gain momentum after an impact, rather than lose it. Negative values will be

accepted but do not produce a useful result.

Variance

By default, particles that strike the Bounce region will reflect evenly off the edge of the Bounce region,

according to the vector or angle of the region. Increasing the Variance above 0.0 will introduce a degree

of variation to that angle of reflection. This can be used to simulate the effect of a rougher surface.

Spin

By default, particles that strike the region will not have their angle or orientation affected in any way.

Increasing or decreasing the Spin value will cause the Bounce region to impart a spin to the particle

based on the angle of collision, or to modify any existing spin on the particle. Positive values will

impart a forward spin, and negative values impart a backward spin. The larger the value, the faster the

spin applied to the particle will be.

Roughness

This slider varies the bounce off the surface to slightly randomize particle direction.

Surface Motion

This slider makes the bounce surface behave as if it had motion, thus affecting the particles.

Surface Motion Direction

This thumbwheel control sets the angle relative to the bounce surface.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.

pChangeStyle [pCS]

The pChange Style node

pChange Style Node Introduction

The pChange Style node provides a mechanism for changing the appearance or style of particles

that interact with a defined region. The primary controls mirror those found in the Style tab of the

pEmitter node. Particles that intersect or enter the defined region change based on the parameters of

this node.

Except for the pCustom node, this is the only node that modifies the particles’ appearance rather than

its motion. It is often used to trigger a change in the appearance in response to some event, such as

striking a barrier.

Inputs

The pChange Style node has a single orange input by default. Like most particle nodes, this orange

input accepts only other particle nodes. A green or magenta bitmap or mesh input appears on the

node when you set the Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Region: The green or magenta region input takes a 2D image or a 3D mesh depending on whether

you set the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is

selected first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area

where the custom particle node takes effect.

Basic Node Setup

Opposite of what you may think, to create a change in style that appears to be caused by some

physical event, the pChange Style node should be placed before the node that creates the event.

For example, below, the particles generated by the Emitter node change style after bouncing off

a pBounce. Both the pChange Style and pBounce use the same Shape 3D node as the region.

The pChange Style must be placed before the pBounce. If the pChange Style node is placed after

the pBounce, the particles bounce off the region before the pChange Style calculates its effect.

The particle will never get to intersect with the pChange Style node’s region, and so the style

never changes.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

A pChange Style node placed before the pBounce node

Inspector

The pChange Style controls

Randomize

The Random Seed slider and Randomize button are presented whenever a Fusion node relies on a

random result. Two nodes with the same seed values will produce the same random results. Click

the Randomize button to randomly select a new seed value, or adjust the slider to manually select a

new seed value.

Change Sets

This option allows the user to change the particle’s Set to become influenced by forces other than the

original particle. See “The Common Controls” in this chapter to learn more about Sets.

Style

This option allows the user to change the particle’s Style and thus the look. See

“The Common Controls” in this chapter to learn more about Styles.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.

pCustom [pCu]

The pCustom node

pCustom Node Introduction

The pCustom node is used to create custom expressions that affect the properties of particles. This

node is similar to the Custom node, except the calculations affect particles rather than pixels.

Inputs

The pCustom node has three inputs. Like most particle nodes, this orange input accepts only other

particle nodes. The green and magenta inputs are 2D image inputs for custom image calculations.

Optionally, there are teal or white bitmap or mesh inputs, which appear on the node when you set the

Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Image 1 and 2: The green and magenta image inputs accept 2D images that are used for per pixel

calculations and compositing functions.

Region: The teal or white region input takes a 2D image or a 3D mesh depending on whether you set

the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is selected first

in the menu. The 3D mesh or a selectable channel from the bitmap defines the area where the custom

particle node takes effect.

Basic Node Setup

The pCustom node is placed in between the pEmitter and pRender. A Shape 3D node is used to

create the region where the Custom particle event occurs.

A pCustom node using a Shape 3D node as the region where the custom event occurs


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION