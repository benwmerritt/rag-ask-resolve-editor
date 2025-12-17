---
title: "Basic Node Setup"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 505
---

# Basic Node Setup

The output of a uDuplicate node typically connects to a uMerge node, integrating it into a larger

scene. The USD scene you want duplicated, in this case a USD scene of a Tokyo shophouse, is

connected to the orange input.

A USD scene of a Tokyo shophouse is duplicated.

Usage

The uDuplicate controls


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Controls Tab

The Controls tab includes all the parameters you can use to create, offset, and scale copies of the USD

object connected to the scene input on the node.

USD Instancing

With this setting enabled, Fusion uses the same USD data for each copy, to increase efficiency.

However, in some occasions, when the copies differ too much from each other, it will reduce efficiency

instead, so you can disable this setting if that’s the case.

Copies

Use this range control to set the number of copies made. Each copy is a copy of the last copy, so if this

control is set to [0,3], the parent is copied, then the copy is copied, then the copy of the copy is copied,

and so on. This allows some interesting effects when transformations are applied to each copy using

the controls below.

Setting the First Copy to a value greater than 0 excludes the original object and shows only

the copies.

Time Offset

Use the Time Offset slider to offset any animations that are applied to the source geometry by a set

amount per copy. For example, set the value to -1.0 and use a cube set to rotate on the Y-axis as the

source. The first copy shows the animation from a frame earlier; the second copy shows animation

from a frame before that, etc. This can be used with great effect on textured planes—for example,

where successive frames of a clip can be shown.

Transform Method

�Linear: When set to Linear, transforms are multiplied by the number of the copy, and the total

scale, rotation, and translation are applied in turn, independent of the other copies.

�Accumulated: When set to Accumulated, each object copy starts at the position of the previous

object and is transformed from there. The result is transformed again for the next copy

Transform Order


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

With this menu, the order in which the transforms are calculated can be set. It defaults to Scale-

Rotation-Transform (SRT).

Using different orders results in different positions of your final objects.

Translation

The X, Y, and Z Offset sliders set the offset position applied to each copy. An X offset of 1 would offset

each copy 1 unit along the X-axis from the last copy.

Rotation

The buttons along the top of this group of rotation controls set the order in which rotations are applied

to the geometry. Setting the rotation order to XYZ would apply the rotation on the X-axis first, followed

by the Y-axis rotation, then the Z-axis rotation.

The three Rotation sliders set the amount of rotation applied to each copy.

Pivot

The pivot controls determine the position of the pivot point used when rotating each copy.

Scale

�Lock: When the Lock XYZ checkbox is selected, any adjustment to the duplicate scale is applied

to all three axes simultaneously. If this checkbox is disabled, the Scale slider is replaced with

individual sliders for the X, Y, and Z scales.

�Scale: The Scale controls tell Duplicate how much scaling to apply to each copy.

Jitter

The options in the Jitter tab allow you to randomize the position, rotation, and size of all the copies

created in the Controls tab.

uDuplicate Jitter tab


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Random Seed

The Random Seed slider is used to generate a random starting point for the amount of jitter applied

to the duplicated objects. Two Duplicate nodes with identical settings but different random seeds

produce two completely different results.

Randomize

Click the Randomize button to auto generate a random seed value.

Jitter Probability

Adjusting this slider determines the percentage of copies that are affected by the jitter. A value of 1.0

means 100% of the copies are affected, while a value of 0.5 means 50% are affected.

Time Offset

Use the Time Offset slider to offset any animations that are applied to the source geometry by a set

amount per copy. For example, set the value to –1.0 and use a cube set to rotate on the Y-axis as the

source. The first copy shows the animation from a frame earlier; the second copy shows animation

from a frame before that, etc. This can be used with great effect on textured planes—for example,

where successive frames of a clip can be shown.

Translation Jitter

Use these three controls to adjust the amount of variation in the X, Y, and Z translation of the

duplicated objects.

Rotation Jitter

Use these three controls to adjust the amount of variation in the X, Y, and Z rotation of the

duplicated objects.

Pivot Jitter

Use these three controls to adjust the amount of variation in the rotational pivot center of the

duplicated objects. This affects only the additional jitter rotation, not the rotation produced by the

Rotation settings in the Controls tab.

Scale Jitter

Use this control to adjust the amount of variation in the scale of the duplicated objects. Disable the

Lock XYZ checkbox to adjust the scale variation independently on all three axes.

Region Tab

The options in the Region tab allow you to define an area in the viewer where the copies can appear

or are prevented from appearing. Like most parameters in Fusion, this area can be animated to cause

the copied object to pop on and off the screen based on the region’s shape and setting.

uDuplicate Region tab


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Region Tab

The Region section includes two settings for controlling the shape of the region and the affect the

region has on the duplicate objects.

�Region Mode: There are three options in the Region Mode menu. The default, labeled “Ignore

region” bypasses the node entirely and causes no change to the copies of objects from how they

are set in the Controls and Jitter tabs. The menu option labeled “When inside region” causes the

copied objects to appear only when their position falls inside the region defined in this tab. The

last menu option, “When not Inside region” causes the copied objects to appear only when their

position falls outside the region defined in this tab.

�Region: The Region menu determines the shape of the region. The five options include cube,

sphere, and rectangle primitive shapes. The mesh option allows you to connect a 3D model into

the green mesh input on the node. The green input appears only after the Region menu is set

to Mesh. The All setting refers to the entire scene. This allows the copies to pop on and off if the

Region mode is animated. When the Region menu is set to Mesh, two other options are displayed.

These are described below.

Limit by Object ID: When a scene with multiple meshes is connected to the green Mesh input on

the node, all the meshes are used as the region. Enabling this checkbox allows you to use the

Object ID slider to select the ID for the mesh you want to use as the Region.

Object ID: When the Limit by Object ID checkbox is enabled, this slider selects the number ID for

the mesh object you want to use for the Region.

uExport [uEx]

The uExport node

uExport Node Introduction

The uExport node is designed to export scenes in the Universal Scene Description (USD) format.

The node allows users to export their USD scene, including geometry, materials, animations, and

lighting, into a USD file. This upgrade marks an important advancement in Fusion’s functionality,

enabling users to seamlessly share complex USD assets, and facilitating smoother workflows in

collaborative environments.

The node offers controls to choose between different USD formats such as usd, .usda, .usdc, and

.usdz. It is also possible to export specific nodes in the source tree as a hierarchy of linked USD files.

Inputs

There is one input on the Background node for a USD scene input.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION