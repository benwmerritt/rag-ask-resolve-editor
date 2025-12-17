---
title: "uSwitch [uSw]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 509
---

# uSwitch [uSw]

The uSwitch node

uSwitch Node Introduction

uSwitch functions similarly to Switch but is specifically designed for the USD environment.

uSwitch is a tool that enables artists to alternate between multiple USD input sources, allowing

the selection of one output from the chosen inputs. This capability is especially useful for toggling

between different visual elements within a composition. The number of input connections can vary,

with the node supporting a dynamic number of inputs that can be renamed as needed. Controls in the

Config tab allow users to add or remove inputs and change their names.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Inputs

You can add up to nine inputs to a uSwitch node, using the slider in the Config tools. If you need more

than nine sources, you can type that number manually into the Number of Inputs field.

Basic Node Setup

Connect as many input sources as you wish to the uSwitch Node and connect its output to the rest of

the node tree.

The uSwitch tool receiving five USD media inputs, allowing you to choose one to go out to uRender.

Inspector

The uSwitch controls let you choose a

source to pass through the switch.

Controls

The Switch Controls consist of a Source switcher that lets you choose which source to pass through

the switch.

The uSwitch configuration


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Config

The uSwitch configuration lets you choose the number of inputs and rename them.

�Number of Inputs: Adjust the slider to add the number of inputs you wish to use, up to nine. If you

want more than nine inputs, you can click in the number field and type the number manually.

�Name X: You can change the name of the input from numerical to something more descriptive.

Settings Tab

The Settings tab in the Inspector is also duplicated in other USD nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

uTransform [uXf]

The USD Transform node

uTransform Node Introduction

If you have multiple objects or prims in your USD scene, the uTransform node allows you to choose

individual groups of objects and adjust their transform independently from the rest of the scene.

Inputs

The uTransform node has a single required input for a USD scene or USD object.

Scene Input: The orange scene input is connected to a USD scene or USD object to apply a second

set of transformation controls.

Basic Node Setup

The uTransform node adds 3D position, rotation, and pivot control onto any existing transforms in

the USD node prior to it. You can combine multiple uTransform nodes together to build parenting or

hierarchical movement.

The uTransform node gives you another set of 3D transform controls that can

be used to modify those in the Transform tab on the uShape node.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Inspector

The USD Transform controls

Controls Tab

Pick

Pick opens the Scene Tree window that lets you choose specific materials or objects in a USD scene.

For more information on using the USD Scene Tree, see its section at the beginning of this chapter.

Translation

Transform controls are used to position the USD shape in 3D space.

Rotation Order

Use these buttons to select the order used to apply the rotation along each axis of the object.

For example, XYZ would apply the rotation to the X-axis first, followed by the Y-axis, and then the Z-axis.

Rotation

Use these controls to rotate the shape around its pivot point. If the Use Target checkbox is selected,

then the rotation is relative to the position of the target; otherwise, the global axis is used.

Pivot

A pivot point is the point around which an object rotates. Normally, an object rotates around its own

center, which is considered to be a pivot of 0,0,0. These controls can be used to offset the pivot from

the center.

Scale

If the Lock X/Y/Z checkbox is checked, a single scale slider is shown. This adjusts the overall size of

the object. If the Lock checkbox is unchecked, individual X, Y, and Z sliders are displayed to allow

scaling in any dimension.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Scale

Selecting the Use Target checkbox enables a set of controls for positioning an XYZ target. When the

target is enabled, the object always rotates to face the target. The rotation of the object becomes

relative to the target.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other USD nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

uVariant [uVa]

The uVariant node

uVariant Node Introduction

Connecting the uVariant node to the USD loader lets you switch between different alternatives or

“variants” for assets that have been set in the USD scene.

Inputs

The uVariant node has a single required input for a USD scene or USD object.

Basic Node Setup

The uVariant node lets you choose between any of the set variants created inside a USD scene. It

accepts a USD scene input.

The uVariant node accepts the input from the MonsterJumpDown USD scene.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION