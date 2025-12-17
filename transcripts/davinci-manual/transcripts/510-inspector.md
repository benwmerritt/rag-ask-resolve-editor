---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 510
---

# Inspector

The uVariant controls

Controls Tab

Pick

Pick opens the Scene Tree window that lets you choose specific materials or objects in a USD scene.

For more information on using the USD Scene Tree, see its section at the beginning of this chapter.

Selected Prims

Shows a list of the prims that have been picked.

Invert Prim Selection

Check this box to swap the selected prims with the unselected ones. This action is animatable

using keyframes.

Variant Set

This drop-down menu will show which of the scene elements have variants to choose from. If no

variants are available it will show No Selection.

Variant

Once you have selected a variant set above, the variant options to choose between will appear in

this dropdown.

uVisibility [uVis]

The uVisibility node

uVisibility Node Introduction

Connecting the uVisibility node to the USD loader lets you control the visibility of an object or branch

of objects in a scene.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Inputs

The uVisibility node has a single required input for a USD scene or USD object.

Scene Input: The orange scene input is connected to a USD scene or USD object to apply a second

set of transformation controls.

Basic Node Setup

The uVisibility node accepts a USD scene and then outputs the visible elements to the rest of the

node tree.

The uVisibility node

Using the uVisibility tool, you can show or hide individual 3D assets. In the above, the cityscape

model (left) has been marked visible, and below it is hidden with the visible box unchecked.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Inspector

The uVisibility controls

Controls Tab

Pick

Pick opens the Scene Tree Dialog that lets you choose specific materials or objects in a USD scene.

As you select the prims, they will highlight in the viewer. See the beginning of this chapter for

information on using the Scene Tree Dialog.

Selected Prims

Shows a list of the prims that have been picked.

Invert Prim Selection

Check this box to swap the selected prims with the unselected ones. This action is animatable using

keyframes.

Visible

Toggling this checkbox will add or remove the selected prims from the view. This action is animatable

using keyframes.

uVolume [uVo]

The uVolume tool

Introduction

uVolume is a versatile and powerful tool that simplifies the process of importing volumetric VDB files

into a USD environment. This node allows you to adjust VDB parameters such as density, temperature,

and color, giving you complete control over the appearance and behavior of the imported VDB file.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Usage

When uVolume is added to the Node Editor, a File dialog is displayed automatically allowing the

selection of a VDB file from your media drive.

You can add either a single VDB file or a VDB sequence (animated VDB).

Once a VDB is brought in using the uVolume node, the uVolume can be used for trimming, looping,

and changing the speed of the imported asset.

The uVolume controls for manipulating VDB files

You can adjust the density with the Scale control, allowing for precise and fine-tuned adjustments.

The Emission section provides color controls for the VDB. Using the Mode selection pulldown will give

you the option to select a method for how to change the color of the VDB. Emission modes include:

�Color: Applies an overall ‘diffuse’ color to import VDB. Note, USD lights will not affect a VDB with

color set to white.

�Field: Scatters an overall color to a nominated Emission Field.

�Blackbody: Applies color and intensity based on temperature; this is suitable for rendering fire and

explosions.

�Gradient: Allows you to map a range of colors over a specified field. The Gradient option provides

you with a number of controls to target a field, then apply nominated colors to that field.

The uVolume provides the standard transformation controls found on most nodes in Fusion’s

USD suite.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

USD Lights

USD light tools are a powerful addition to Fusion's USD toolset. They allow for greater control and

flexibility when creating and manipulating lighting in your USD scenes. There are six lights available in

the USD toolset, they are:

uCylinder Light [uCL]

The USD Cylinder light

uCylinder Light Node Introduction

A uCylinder light is geometric light that has length and diameter, similar to fluorescent light. This light

shows an onscreen control. Translation and rotation of the control place this in the scene.

Inputs

There is one Scene Input in yellow to attach a USD scene; this allows you to adjust any existing lights

within the scene.

Inspector

The USD Cylinder Light controls

Controls Tab

The Controls tab is used to set the color and brightness of the uCylinder light. The position, direction,

and scale of the light source is controlled in the Transform tab.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Override Selection

Pressing the Pick button lets you choose an existing light in an attached USD file to allow adjusting the

lights in an imported scene.

Color

Use this standard Color control to set the color of the light.

Intensity

Use this slider to set the intensity of the light. A value of 0.2 indicates 20% percent light.

Exposure

This will change how much light will expose a scene; this is similar to Intensity.

Color Temperature/Enable

This sets the color temperature of a light source. Its default is 6500K, which is daylight temperature.

Diffuse Response

Controls the amount the light will contribute to the Diffuse color of a material.

Specular Response

Controls the amount the light will contribute to the Specular color of a material.

Normalize

This will normalize the light’s contribution in the scene.

Treat As Line

This will make the light a simpler line light source.

Length

Defines the length of the light.

Radius

Defines the diameter of the light.