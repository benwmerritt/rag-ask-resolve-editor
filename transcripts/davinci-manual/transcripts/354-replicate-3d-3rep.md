---
title: "Replicate 3D [3Rep]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 354
---

# Replicate 3D [3Rep]

The Replicate 3D node

Replicate 3D Node Introduction

The Replicate 3D node replicates input geometry at positions of destination vertices. The vertices can

be mesh vertices as well as particle positions. For each copy of the replicated input geometry, various

transformations can be applied. The options in the Jitter tab allow non-uniform transformations, such

as random positioning or sizes.

Inputs

There are two inputs on the Replicate 3D node: one for the destination geometry that contains the

vertices, and one for the 3D geometry you want to replicate.

Destination: The orange destination input accepts a 3D scene or geometry with vertex positions,

either from the mesh or 3D particle animations.

Input[#]: The input accepts the 3D scene or geometry for replicating. Once this input is connected, a

new input for alternating 3D geometry is created.

At least one connected input is required.

Basic Node Setup

In the example below, a Replicate 3D node is inserted directly after the pRender node. A spaceship

FBX node is connected to the green input representing the object that will be replicated based on the

particles. Each particle cell takes on the shape of the 3D geometry connected to the input.

Replicate 3D used to create an armada of swarming spaceships


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Inspector

Replicated 3D Jitter controls

Controls Tab

Step

Defines how many positions are skipped. For example, a step of 3 means that only every third vertice

of the destination mesh is used, while a step of 1 means that all positions are used.

The Step setting helps to keep reasonable performance for big destination meshes. On parametric

geometry like a torus, it can be used to isolate certain parts of the mesh.

Point clouds are internally represented by six points once the Make Renderable option has been set.

To get a single point, use a step of 6 and set an X offset of –0.5 to get to the center of the point cloud.

Use –0.125 for Locator 3Ds. Once these have been scaled, the offset may differ.

Input Mode

This menu defines in which order multiple input scenes are replicated at the destination. No matter

which setting you choose, if only one input scene is supplied this setting has no effect.

The Input Mode Loop vs. Random order

When set to Loop, the inputs are used successively. The first input is at the first position, the second

input at the second position, and so on. If there are more positions in the destination present than

inputs, the sequence is looped.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

When set to Random, a definite but random input for each position is used based on the seed in the

Jitter tab. This input mode can be used to simulate variety with few input scenes.

The Death of Particles setting causes the input geometries’ IDs to change; therefore, their copy order

may change.

Time Offset

Use the Time Offset slider to offset any animations that are applied to the input geometry by a set

amount per copy. For example, set the value to –1.0 and use a cube set to rotate on the Y-axis as the

source. The first copy shows the animation from a frame earlier; the second copy shows animation

from a frame before that, etc.

This can be used with great effect on textured planes—for example, where successive frames of a

video clip can be shown.

Alignment

Alignment specifies how to align the copies in respect of the destination mesh normal or

particle rotation.

Not Aligned: Does not align the copy. It stays rotated in the same direction as its input mesh.

Replicate 3D Not Aligned layout

Aligned: This mode uses the point’s normal and tries to reconstruct an upvector. It works best

with organic meshes that have unwelded vertices, like imported FBX meshes, since it has the

same rotations for vertices at the same positions. On plane geometric meshes, a gradual shift in

rotation is noticeable. For best results, it is recommended to use this method at the origin before

any transformations.

Replicate 3D Aligned layout


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Aligned TBN: This mode results in a more accurate and stable alignment based on the tangent,

binormal, and normal of the destination point. This works best for particles and geometric shapes.

On unwelded meshes, two copies of multiple unwelded points at the same position may lead to

different alignments because of their individual normals.

Replicate 3D Aligned TBN layout

Color

Affects the diffuse color or shader of each copy based on the input’s particle color.

Use Object Color: Does not use the color of the destination particle.

Combine Particle Color: Uses the shader of any input mesh and modifies the diffuse color to match

the color from the destination particle.

Use Particle Color: Replaces the complete shader of any input mesh with a default shader. Its

diffuse color is taken from the destination particle.

Replicate 3D Color options


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Translation

These three sliders tell the node how much offset to apply to each copy. An X Offset of 1 would offset

each copy one unit, one unit along the X-axis from the last copy.

Rotation Order

These buttons can be used to set the order in which rotations are applied to the geometry. Setting the

rotation order to XYZ would apply the rotation on the X-axis first, followed by the Y-axis rotation, and

then the Z-axis rotation.

XYZ Rotation

These three rotation sliders tell the node how much rotation to apply to each copy.

XYZ Pivot

The pivot controls determine the position of the pivot point used when rotating each copy.

Lock XYZ

When the Lock XYZ checkbox is selected, any adjustment to the scale is applied to all three axes

simultaneously.

If this checkbox is disabled, the Scale slider is replaced with individual sliders for the X, Y,

and Z scales.

Scale

The Scale control sets how much scaling to apply to each copy.

Jitter Tab

The Jitter tab can be used to introduce randomness to various parameters.

Replicated 3D Jitter controls


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Random Seed/Randomize

The Random Seed is used to generate the jitter applied to the replicated objects. Two Replicate

nodes with identical settings but different random seeds will produce two completely different results.

Click the Randomize button to assign a Random Seed value.

Time Offset

Use the Time Offset slider to offset any animations that are applied to the source geometry. Unlike

Time Offset on the Controls tab, Jitter Time Offset is random, based on the Random Seed setting.

Translation XYZ Jitter

Use these three controls to adjust the variation in the translation of the replicated objects.

Rotation XYZ Jitter

Use these three controls to adjust the variation in the rotation of the replicated objects.

Pivot XYZ Jitter

Use these three controls to adjust the variation in the rotational pivot center of the replicated objects.

This affects only the additional jitter rotation, not the rotation produced by the rotation settings in the

Controls tab.

Scale XYZ Jitter

Use this control to adjust the variation in the scale of the replicated objects. Uncheck the Lock XYZ

checkbox to adjust the scale variation independently on all three axes.

Common Controls

Settings Tab

The Settings tab is common to many 3D nodes. The description of these controls can be found in “The

Common Controls” section at the end of this chapter.