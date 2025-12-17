---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 506
---

# Inspector

The uExport controls

Export

The Export controls let you set the format of the exported USD scene.

�Export Stage: Press this button to open a file browser to select where to store your USD scene.

�Format: Choose a format for your USD scene.

USD (*.usd)

USD UTF-8 (*.usda)

USD binary (*.usdc)

USD packaged (*.usdz)

Settings Tab

The Settings tab in the Inspector is also duplicated in other USD nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

uImage Plane [uIm]

The USD Image Plane node

uImage Plane Node Introduction

The uImage Plane node produces 2D planar geometry in 3D space. The node is most commonly used

to represent 2D images on “cards” in the 3D space. The aspect of the image plane is determined by

the aspect of the image that is input.

Inputs

The input on this node is for the image that will be texture mapped to the plane.

Input: The yellow input is used for the connection of a MediaIn image.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Basic Node Setup

The uImage Plane Node accepts a 2D image and places it into a 3D USD scene.

Inspector

The uImage Plane controls

Controls Tab

Most of the Controls tab is taken up by common controls. The Image Plane-specific controls at the top

of the Inspector allow minor adjustments.

Filename

The uImagePlane has an input so an image can be piped directly into the node. This node can also

directly load an image by browsing, and it will show the name and path in the filename. Use the

Browse button to open the file browser and select an image.

Size

Size will set the size of the image plane in the USD 3D scene.

Common Controls

Transform and Settings Tab

The Transform and Settings tab in the Inspector are also duplicated in other USD nodes. These

common controls are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

uLoader [uLd]

The USD Loader node

uLoader Node Introduction

The uLoader node is used for importing USD files into your Fusion Composition. It will load .usd, .usda,

.usdc, and .usdz formats.

Replacing Materials with Imported MaterialX files

Users can load MaterialX files (.mtlx) from the the USD Loader and use the uReplaceMaterial tool to

assign imported materials to a nominated USD object to achieve a desired look.

Inputs

None.

Basic Node Setup

The uLoader node imports a USD scene and then

merges it with a USD Camera for view control.

Inspector

The USD Loader controls


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Controls Tab

Filename

This control allows you to source a USD file to bring into the Fusion project. Use the Browse button to

open the file browser and select a USD file (.usd, .usda, .usdc, or .usdz).

Trim

Lets you select an In and Out point of a USD file to bring only that range into the Fusion project.

Time Scale

Animated .usd scenes can have their animation speed adjusted to be faster and slower using

time scale.

Frame Offset

Will define when an animation will start, so timing can be moved along the timeline.

Reverse

When checked, this will reverse the animation of the USD file.

Loop

When checked, this will loop the animation of the USD file.

Reload

This button will reload the USD file set in the Filename field above. This lets you make changes to the

USD file in another application and see the results in Fusion by reloading it.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other USD nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

uMaterialX [uMX]

The uMaterialX node

uMaterialX Node Introduction

The uMaterialX node simply loads a MaterialX (.mtlx) definition file and creates a USD scene file

creating only those materials.

Inputs

There are no inputs to the uMaterialX node. Only a file requester to load the .mtlx file.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Basic Node Setup

Connect the material output to the rest of the USD tools.

A node tree showing a MaterialX definition (.mtlx) file called Material4 loaded

into a uMaterialX node, then passing that material to a uReplaceMaterial

node to change the material in a USD scene called JogBackwards.

Inspector

The uMaterialX controls

Controls

The single control is a a Material File selector with a browse button to load the .mtlx file from

your computer.

Settings Tab

The Settings tab in the Inspector is also duplicated in other USD nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION