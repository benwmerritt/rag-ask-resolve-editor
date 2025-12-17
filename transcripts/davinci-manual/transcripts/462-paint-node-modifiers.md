---
title: "Paint Node Modifiers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 462
---

# Paint Node Modifiers

Every paint stroke created in the viewer creates an associated modifier stroke. These modifier strokes

are represented as a list of paint stroke operations in the Modifiers tab of the Inspector. Each stroke

you create can be modified or deleted, or applied in a different order using the modifier stack.

NOTE: The MultiStroke tools are built for speed and can contain many strokes internally

without creating a huge list stack in the modifiers

Each Paint modifier stroke contains Brush controls, Apply controls, and Stroke controls

identical to those found in the main Controls tab of the Inspector.


Fusion Page Effects | Chapter 113 Paint Node

FUSION

Keyboard Shortcuts

Keyboard shortcuts allow you to adjust painting styles and color without having to navigate menus.

While painting:

Hold Command or Ctrl while left-dragging to change brush size.

Hold Option or Alt while clicking to pick a color in the viewer.

While cloning:

Option-click or Alt-click to set the clone source position. Strokes start cloning from the selected location.

Hold O to temporarily enable a 50% transparent overlay of the clone source (% can be changed with pref

Tweaks.CloneOverlayBlend).

Press P to toggle an opaque overlay of the clone source.

While overlay is showing:

Arrow keys change the clone source position; you can also drag crosshairs and adjust angle control or

size sliders.

Option + Left/Right or Alt + Left/Right Arrow keys change the clone source angle.

Option + Up/Down or Alt + Up/Down Arrow keys change the clone source size.

Shift + Command or Shift + Ctrl can be used with the above for greater or lesser adjustments. Left and

right square brackets, [ and ], change the clone source Time Offset (this requires a specific Clone Source

node to be set in the Source Node field).

Copy Rect/Ellipse:

Shift + drag out the source to constrain the shape.

With a single stroke selected (not available on multi or polyline strokes):

Press X or Y to flip the stroke.

Paint Groups:

Command + drag or Ctrl + drag to change the position of a group’s crosshair, without changing the

position of the group.


Fusion Page Effects | Chapter 113 Paint Node

FUSION

Chapter 114

Particle Nodes

This chapter details the Particle nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Particle Nodes������������������������������������������������������������ 2576

pAvoid [pAv]����������������������������������������������������������������� 2576

pBounce [pBn]������������������������������������������������������������ 2578

pChangeStyle [pCS]������������������������������������������������ 2580

pCustom [pCu]������������������������������������������������������������ 2582

pCustomForce [pCF]����������������������������������������������� 2586

pDirectionalForce [pDF]���������������������������������������� 2587

pEmitter [pEm]������������������������������������������������������������ 2589

pFlock [pFl]������������������������������������������������������������������� 2594

pFollow [pFo]��������������������������������������������������������������� 2596

pFriction [pFr]�������������������������������������������������������������� 2598

pGradientForce [pGF]�������������������������������������������� 2600

pImage Emitter [pIE]������������������������������������������������� 2601

pKill [pKI]������������������������������������������������������������������������ 2605

pMerge [pMg]�������������������������������������������������������������� 2606

pPoint Force [pPF]���������������������������������������������������� 2607

pRender [pRn]������������������������������������������������������������� 2608

About Pre-Roll�������������������������������������������������������������� 2611

Conditions���������������������������������������������������������������������� 2611

Scene Tab���������������������������������������������������������������������� 2612

Grid Tab�������������������������������������������������������������������������� 2613

Image Tab���������������������������������������������������������������������� 2613

pSpawn [pSp]��������������������������������������������������������������� 2616

pTangent Force [pTF]����������������������������������������������� 2618

pTurbulence [pTr]�������������������������������������������������������� 2619

pVortex [pVt]����������������������������������������������������������������� 2621

The Common Controls������������������������������������������ 2623


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Particle Nodes

The Particle nodes are used to generate a large number of duplicated objects that automatically

animate. They are used to create elements like falling rain, fireworks, smoke, pixie dust, and much

more. There are endless possibilities. Particles in Fusion consist of a set of nodes that are strung

together in a chain for generating, modifying, and rendering particles in a 2D or 3D scene.

To begin, every particle system you create must contain two fundamental nodes:

�pEmitter: Used to generate the particles and control their basic look, motion. and behavior.

�pRender: Used to render the output of the pEmitter into a 2D or 3D scene. When creating

particles, you only ever view the pRender node.

Particle Nodes

The remaining particle nodes modify the pEmitter results to simulate natural phenomena like gravity,

flocking, and bounce. The names of particle nodes all begin with a lowercase p to differentiate them

from non-particle nodes. They can be found in the particles category in the Effects Library.

pAvoid [pAv]

The pAvoid node

pAvoid Node Introduction

The pAvoid node is used to create a region or area within the image that affected particles attempt to

avoid entering and crossing.

It has two primary controls. The first determines the distance from the region a particle should be

before it begins to move away from the region. The second determines how strongly the particle

moves away from the region.

A pAvoid node creates a “desire” in a particle to move away from a specific region. If the velocity of the

particle is stronger than the combined distance and strength of the pAvoid region, the particle’s desire

to avoid the region does not overcome its momentum and the particle crosses that region regardless.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Inputs

The pAvoid node has a single orange input by default. Like most particle nodes, this orange input

accepts only other particle nodes. A green bitmap or mesh input appears on the node when you set

the Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Region: The green or magenta region input takes a 2D image or a 3D mesh depending on whether

you set the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is

selected first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area

particles avoid.

Basic Node Setup

The pAvoid node is placed in between the pEmitter and pRender. A Shape 3D node is used to create

the region the particles will avoid.

A pAvoid node using a Shape 3D node as the region to avoid

Inspector

The pAvoid controls

Randomize

The Random Seed slider and Randomize button are presented whenever a Fusion node relies on a

random result. Two nodes with the same seed values will produce the same random results. Click the

Randomize button to randomly select a new seed value, or adjust the slider to manually select a new

seed value.

Distance

Determines the distance from the region a particle should be before it begins to move away from the region.

Strength

Determines how strongly the particle moves away from the region. Negative values make the particles

move toward the region instead.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.