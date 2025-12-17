---
title: "Inputs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 465
---

# Inputs

The pDirectional Force node has a single orange input by default. Like most particle nodes, this

orange input accepts only other particle nodes. A green or magenta bitmap or mesh input appears on

the node when you set the Region menu in the Region tab to either Bitmap or Mesh.

Input: The orange input takes the output of other particle nodes.

Region: The green or magenta region input takes a 2D image or a 3D mesh depending on whether

you set the Region menu to Bitmap or Mesh. The color of the input is determined by whichever is

selected first in the menu. The 3D mesh or a selectable channel from the bitmap defines the area

where the directional force takes effect.

Basic Node Setup

The pDirectional Force node is placed in between the pEmitter and pRender and is often used to

create gravity.

A pDirectional Force node placed between the pEmitter and pRender nodes

Inspector

The pDirectional Force controls

Randomize

The Random Seed slider and Randomize button are presented whenever a Fusion node relies on a

random result. Two nodes with the same seed values will produce the same random results. Click

the Randomize button to select a new seed value randomly, or adjust the slider to select a new seed

value manually.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Strength

Determines the power of the force. Positive values will move the particles in the direction set by the

controls; negative values will move the particles in the opposite direction.

Direction

Determines the direction in X/Y space.

Direction Z

Determines the direction in Z space.

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.

pEmitter [pEm]

The pEmitter node

pEmitter Node Introduction

The pEmitter node is the main source of particles (pImage Emitter is another) and will usually be the

first node used in any new particle system. This node contains controls for setting the initial position,

orientation, and motion of the particles, as well as controls for the visual style of each particle.

Like all other Particle nodes (with the exception of the pRender node), the pEmitter produces a particle

set, not a visible image, and therefore cannot be displayed directly in a viewer. To view the output of a

particle system, add a pRender node after the pEmitter.

Inputs

By default, the pEmitter node has no inputs at all. You can enable an image input by selecting Bitmap

from the Style menu in the Style tab. Also, two region inputs, one for bitmap and one for mesh, appear

on the node when you set the Region menu in the Region tab to either Bitmap or Mesh. The colors of

these inputs change depending on the order in which they are enabled.

Style Bitmap Input: This image input accepts a 2D image to use as the particles’ image. Since this

image duplicates into potentially thousands of particles, it is best to keep these images small and

square—for instance, 256 x 256 pixels.

Region: The region inputs takes a 2D image or a 3D mesh depending on whether you set the

Region menu to Bitmap or Mesh. The color of the input is determined by whichever is selected first in

the menu. The 3D mesh or a selectable channel from the bitmap defines the area where the particles

are emitted.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Basic Node Setup

The pEmitter node starts the branch of a particle system that always ends with a pRender node. The

pEmitter can feed directly into a pRender node to feed other particle nodes.

A pEmitter node connected to a pRender node is a typical setup for more particle systems.

Inspector

The pEmitter inspector is divided into four main tabs and a common settings tab. The controls tab

is the first tab displayed and it contains settings that affect the general setup of the particle cells

emitted by the node. These settings do not directly affect the appearance of the cells or shape of the

emitter region. They modify fundamental behaviors like quantity, duration, speed, and rotation of the

particle cells.

The pEmitter controls


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Randomize and Random Seed

The Random Seed slider is used to seed all the variance and random number generators used by

the node when creating the particle system. Two pEmitter nodes with exactly the same settings for

all controls and the same random seed will generate exactly the same particle system. Changing the

random seed will cause variation between the nodes. Click the Randomize button to automatically set

a randomly chosen value for the Random Seed.

Number

This control is used to set the amount of new particles generated on each frame. A value of 1 would

cause one new particle to be generated each frame. By frame 10, there would be a total of 10 particles

in existence (unless Particle Lifespan was set to fewer than 10 frames).

Animate this parameter to specify the number of particles generated in total. For example, if only 25

particles in total are desired, animate the control to produce five particles on frame 0–4, then set a key

on frame five to generate zero particles for the remainder of the project.

Number Variance

This modifies the amount of particles generated for each frame, as specified by the Number control.

For example, if Number is set to 10.0 and Number Variance is set to 2.0, the emitter will produce

anywhere from 9-11 particles per frame. If the value of Number Variance is more than twice as large as

the value of Number, it is possible that no particles will be generated for a given frame.

Lifespan

This control determines how long a particle will exist before it disappears or ‘dies.’ The default value

of this control is 100 frames, although this can be set to any value. The timing of many other particle

controls is relative to the Lifespan of the particle. For example, the size of a particle can be set to

increase over the last 80% of its life, using the Size Over Life graph in the Style tab of the pEmitter.

Lifespan Variance

Like Number Variance, the Lifespan Variance control allows the Lifespan of particles produced to be

modified. If Particle Lifespan was set to 100 frames and the Lifespan Variance to 20 frames, particles

generated by the emitter would have a lifespan of 90–110 frames.

Color

This provides the ability to specify from where the color of each particle is derived. The default setting

is Use Style Color, which will provide the color from each particle according to the settings in the Style

tab of the pEmitter node.

The alternate setting is Use Color From Region, which overrides the color settings from the Style tab

and uses the color of the underlying bitmap region.

The Use Color From Region option only makes sense when the pEmitter region is set to use a bitmap

produced by another node in the composition. Particles generated in a region other than a bitmap

region will be rendered as white when the Use Color From Region option is selected.

Position Variance

This control determines whether or not particles can be ‘born’ outside the boundaries of the pEmitter

region. By default, the value is set to zero, which will restrict the creation area for new particles to the

exact boundaries of the defined region. Increasing this control’s value above 0.0 will allow the particle

to be born slightly outside the boundaries of that region. The higher the value, the ‘softer’ the region’s

edge will become.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Temporal Distribution

In general, an effect is processed per frame, based on the comp frame rate. However, processing

some particles only at the exact frame boundaries can cause pulsing. To make the behavior subtly

more realistic, the particles can be birthed in subframe increments.

The default, At The Same Time setting renders on frame boundaries, where as the other two settings

take advantage of sub frame rendering. Randomly Distributed randomizes birth times +/- around the

frame number, eg birth 10 particles at random sub times 24.1 24.85, 24.21, 24.37 etc. one particle at a

time. Evenly Distributed births particles at regular sub times, eg 10 particles, birth 1 at at time at 24.0,

24.1, 24.2, 24.3, 24.4, 24.5 ... 24.8, 24.9.

These settings are influenced by the Sub Frame Accuracy setting in the pRender node. The Sub

Frame Accuracy slider controls how many in-between frames are calculated between each frame. The

higher the value the more accurate the particle calculation but the longer the render times.

Velocity

The controls in the Velocity section determine the speed and direction of the particle cells as the are

generated from the emitter region.

Velocity and Velocity Variance

These determine the initial speed or velocity of new particles. By default, the particle has no velocity

and will not move from its point of origin unless acted upon by outside forces. A velocity setting of 10.0

would cause the particle to cross the entire width of the image in one step so a velocity of 1.0 would

cause the particle to cross the width of the image over 10 frames.

Velocity Variance modifies the velocity of each particle at birth, in the same manner described in

Lifespan Variance and Number Variance above.

Inherit

Inherit Velocity passes the emitter region’s velocity on to the particles. This slider has a wide range

that includes negative and positive values. A negative value causes the particles to move in the

opposite direction, a value of 1 will cause the particles to move with a velocity that matches the emitter

region’s velocity, and a value of 2 causes the particles to move ahead of the emitter region.

Angle and Angle Variance

This determines the angle at which particles with velocity applied will be heading at their birth.

Angle Z and Angle Z Variance

This is as above, except this control determines the angle of the particles along the Z space axis

(toward or away from the camera).

Rotation

Rotation controls are used to set the orientation of particle cells and animating that orientation

over time .

Rotation Mode

This menu control provides two options to help determine the orientation of the particles emitted.

When the particles are spherical, the effect of this control will be unnoticeable.

�Absolute Rotation: The particles will be oriented as specified by the Rotation controls, regardless

of velocity and heading.

�Rotation Relative To Motion: The particles will be oriented in the same direction as the

particle is moving. The Rotation controls can now be used to rotate the particle‘s orientation away

from its heading.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Rotation XYZ and Rotation XYZ Variance

These controls allow for Rotation of the individual particles. This can be particularly useful when

dealing with a bitmap particle type, as the incoming bitmap may not be oriented in the desired

direction.

Rotation XYZ Variance can be used to randomly vary the rotation by a specified amount around the

center of the Rotation XYZ value to avoid having every particle oriented in the exact same direction.

Spin

Spin controls are auto animated controls that change the orientation of particle cells over time.

Spin XYZ and Spin Variance

These provide a spin to be applied to each particle at birth. The particles will rotate ‚x‘ degrees each

frame, as determined by the value of Spin XYZ.

The Spin XYZ variances will vary the amount of rotation applied to each frame in the manner

described by Number Variance and Lifespan Variance documented above.

Sets Tab

This tab contains settings that affect the physics of the particles emitted by the node. These settings

do not directly affect the appearance of the particles. Instead, they modify behavior like velocity, spin,

quantity, and lifespan.

The pEmitter Sets tab

Set 1-32

To assign the particles created by a pEmitter to a given set, simply select the checkbox of the set

number you want to assign. A single pEmitter node can be assigned to one or multiple sets. Once they

are assigned in the pEmitter, you can enable sets in other particle nodes so they only affect particles

from specific pEmitters.

Style Tab

The Style tab provides controls that affect the appearance of the particles. For detailed information

about the style Tab, see the “The Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

The pEmitter Style tab

Region Tab

The Region tab controls the shape, size, and location of the area that emits the particle cells. This is

often called the Emitter. Only one emitter region can be set for a single pEmitter node. If the pRender

is set to 2D, then the emitter region will produce particles along a flat plane in Z Space. 3D emitter

regions possess depth and can produce particles inside a user-defined, three-dimensional region.

For more detail on the Region tab, see “The Common Controls” section at the end of this chapter.

Common Controls

Conditions, Style, Region, and Settings Tabs

The Conditions, Style, Region, and Settings tabs are common to all Particle nodes, so their

descriptions can be found in “The Common Controls” section at the end of this chapter.