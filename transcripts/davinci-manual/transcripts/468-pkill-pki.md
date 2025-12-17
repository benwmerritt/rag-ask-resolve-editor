---
title: "pKill [pKI]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 468
---

# pKill [pKI]

The pKill node

pKill Node Introduction

The Kill node is used to destroy (kill) any particle that crosses or intersects its region. It has no specific

controls, as it has only one possible affect on a particle. The controls found in the Region tab are

normally used to limit this node by restricting the effect to particles that fall within a certain region, age,

set, or by reducing the probability of the node applying to a given particle.

Inputs

The pKill node has a single orange input by default. Like most particle nodes, this orange input

accepts only other particle nodes. A green bitmap or mesh input appears on the node when you set

the Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Region: The green or magenta region input takes a 2D image or a 3D mesh depending on whether

you set the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is

selected first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area

particles are killed.

Basic Node Setup

The pKill node is placed in between the pEmitter and pRender nodes. A Shape 3D node is used to

create the region where the particles die.

A pKill node using a Shape 3D node as the region where particles die

Inspector

This node only contains common controls in the Conditions and Regions tabs. The Conditions and

Regions controls are used to define the location, age, and set of particles that are killed.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.

pMerge [pMg]

The pMerge node

pMerge Node Introduction

This node has no controls whatsoever. It serves to combine particles from two streams. Any nodes

downstream of the pMerge node will treat the two streams as one.

The combined particles will preserve any sets assigned to them when they were created, making it

possible for nodes downstream of the pMerge to isolate specific particles when necessary.

Inputs

The pMerge node has two identical inputs, one orange and one green. These two inputs accept only

other particle nodes.

Particle 1 and 2 Input: The two inputs accept two streams of particles and merge them.

Basic Node Setup

The pMerge node connects two pEmitter nodes. The output of the pMerge can go on to feed other

particle nodes or to a pRender.

A pMerge node combining two pEmitter nodes.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

pPoint Force [pPF]

The pPoint Force node

pPoint Force Node Introduction

This node applies a force to the particles that emanate from a single point in 3D space. The pPoint

Force can either attract or repel particles within its sphere of influence. There are four controls specific

to the pPoint Force node.

Inputs

The pPoint Force node has a single orange input by default. Like most particle nodes, this orange

input accepts only other particle nodes. A green bitmap or mesh input appears on the node when you

set the Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Region: The green or magenta region input takes a 2D image or a 3D mesh depending on whether

you set the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is

selected first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area

where the point force affects the particles.

Basic Node Setup

The pPoint Force node is inserted between a pEmitter and a pRender node.

The pPoint Force node positions a tangent force that particles are attracted to or repelled from.

Inspector

The pPoint Force controls


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Randomize

The Random Seed slider and Randomize button are presented whenever a Fusion node relies on a

random result. Two nodes with the same seed values will produce the same random results. Click the

Randomize button to randomly select a new seed value, or adjust the slider to manually select a new

seed value.

Strength

This parameter sets the Strength of the force emitted by the node. Positive values represent attractive

forces; negative values represent repellent forces.

Power

This determines the degree to which the Strength of the force falls off over distance. A value of zero

causes no falloff of strength. Higher values will impose an ever-sharper falloff in strength of the force

with distance.

Limit Force

The Limit Force control is used to counterbalance potential problems with temporal sub-sampling.

Because the position of a particle is sampled only once a frame (unless sub-sampling is increased in

the pRender node), it is possible that a particle can overshoot the Point Force’s position and end up

getting thrown off in the opposite direction. Increasing the value of this control reduces the likelihood

that this will happen.

X, Y, Z Center Position

These controls are used to represent the X, Y, and Z coordinates of the point force in 3D space.

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.

pRender [pRn]

The pRender node

pRender Node Introduction

The pRender node converts the particle system to either an image or geometry. The default is a 3D

particle system, which must be connected to a Renderer 3D to produce an image. This allows the

particles to be integrated with other elements in a 3D scene before they are rendered.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Inputs

The pRender node has one orange input, a green camera input, and a blue effects mask input. Like

most particle nodes, this orange input accepts only other particle nodes. A green bitmap or mesh

input appears on the node when you set the Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Camera Input: The optional green camera input accepts a camera node directly or a 3D scene with a

camera connected that is used to frame the particles during rendering.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input for 2D particles

crops the output of the particles so they are seen only within the mask.

Basic Node Setup

The pRender node is always placed at the end of a particle branch. If the pRender is set to 2D, then

the output connects to other 2D nodes like a Merge node. If the pRender is set to 3D, the output

connects to a 3D node like a Merge 3D.

All particle branches end with a pRender node.

Inspector

The pRender controls


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Output Mode (2D/3D)

While the pRender defaults to 3D output, it can be made to render a 2D image instead. This is done

with the 3D and 2D buttons on the Output Mode control. If the pRender is not connected to a 3D-only

or 2D-only node, you can also switch it by selecting View > 2D Viewer from the viewer’s pop-up menu.

In 3D mode, the only controls in the pRender node that have any effect at all are Restart, Pre-Roll

and Automatic Pre-Roll, Sub-Frame Calculation Accuracy, and Pre-Generate frames. The remaining

controls affect 2D particle renders only. The pRender node also has a Camera input on the node tree

that allows the connection of a Camera 3D node. This can be used in both 2D and 3D modes to allow

control of the viewpoint used to render an output image.

Render and the Viewers

When the pRender node is selected in a node tree, all the onscreen controls from Particle nodes

connected to it are presented in the viewers. This provides a fast, easy-to-modify overview of the

forces applied to the particle system as a whole.

Pre-Roll Options

Particle nodes generally need to know the position of each particle on the last frame before they can

calculate the effect of the forces applied to them on the current frame. This makes changing current

time manually by anything but single frame intervals likely to produce an inaccurate image.

The controls here are used to help accommodate this by providing methods of calculating the

intervening frames.

Restart

This control also works in 3D. Clicking on the Restart button will restart the particle system at the

current frame, removing any particles created up to that point and starting the particle system from

scratch at the current frame.

Pre-Roll

This control also works in 3D. Clicking on this button causes the particle system to recalculate,

starting from the beginning of the render range up to the current frame. It does not render the image

produced. It only calculates the position of each particle. This provides a relatively quick mechanism to

ensure that the particles displayed in the views are correctly positioned.

If the pRender node is displayed when the Pre-Roll button is selected, the progress of the pre-roll is

shown in the viewer, with each particle shown as point style only.

Automatic Pre-Roll

Selecting the Automatic Pre-Roll checkbox causes the particle system to automatically pre-roll the

particles to the current frame whenever the current frame changes. This prevents the need to manually

select the Pre-Roll button whenever advancing through time in jumps larger than a single frame. The

progress of the particle system during an Automatic Pre-Roll is not displayed to the viewers to prevent

distracting visual disruptions.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION