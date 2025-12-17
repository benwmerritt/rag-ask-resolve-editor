---
title: "CubeMap [3Cu]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 372
---

# CubeMap [3Cu]

The Cube Map node

Cube Map Node Overview

The Cube Map node creates texture maps using separate images for each face of the cube. It can also

extract the individual faces of the cube from a single image containing an unfolded cube in the Vertical

or Horizontal Cross layouts.

A cube map is produced by mounting six cameras at 90 degrees angle of views to point up, down, left,

right, front, and back.

The node provides options to set the reference coordinate system and rotation for the resulting

texture map. The Cube Map node is typically used to produce environment maps for distant areas

(such as skies or horizons) or reflection and refraction maps.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Sample cube map

Inputs

The Inputs on this node change based on the settings of the Layout menu in the Inspector. The single

input uses a 2D image for the entire cube, while six inputs can handle a different 2D image for each

side of a cube.

CrossImage: The orange Cross Image input is visible by default or when the Layout menu in the

Inspector is set to either Vertical Cross or Horizontal Cross. The input accepts a 2D image.

CubeMap.[DIRECTION]: These six multi-colored inputs are visible only when the Layout menu in the

Inspector is set to Separate Images. Each input accepts an image aligned to match the left, right, top,

bottom, front, and back faces.

Basic Node Setup

The Cube Map node uses a vertical or horizontal cross image represented by MediaIn2 node

connected into the orange cross image input. The Cube Map node is used similarly to the Sphere Map

node. It creates an environment that surrounds the geometry connected to a Shader node.

A Cube Map node receives a cross image input, creating an environment for the Shape 3D


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Inspector

Cube Map controls

Controls Tab

Layout

The Layout menu determines the type and number of inputs for the cube map texture.

Valid options are:

�Separate Images: This option exposes six inputs on the node, one for each face of the cube. If the

separate images are not square or not of the same size, they are rescaled into the largest 1:1 image

that can contain all of them.

�Vertical Cross: This option exposes a single input on the node. The image should be an

unwrapped texture of a cube containing all the faces organized into a Vertical Cross formation,

where the height is larger than the width. If the image aspect of the cross image is not 3:4, the

CubeMap node crops it down so it matches the applicable aspect ratio.

�Horizontal Cross: This option exposes a single input on the node. The image should be an

unwrapped texture of a cube containing all the faces organized into a Horizontal Cross formation,

where the width is larger than the height. If the image aspect of the cross image is not 4:3, the

CubeMap node crops it down so that matches the applicable aspect ratio.

Coordinate System

The coordinate system menu sets the position values used when converting the image into a texture.

�Model: This option orients the texture along the object local coordinate system.

�World: This option orients the resulting texture using the global or world coordinate system.

�Eye: This option aligns the texture map to the coordinate system of the camera or viewer.


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Rotation

The rotation controls are divided into buttons that select the order of rotation along each axis of the

texture. For example, XYZ would apply the rotation to the X axis first, followed by the Y axis, and finally

the Z axis. The other half of the rotation controls are dials that rotate the texture around its pivot point.

Warn About Bad Dimensions

Selecting this checkbox displays a warning message on the console if the dimensions of the image

provided did not meet the requirements of the selected orientation mode.

Material ID

This slider sets the numeric identifier assigned to this material. This value is rendered into the MatID

auxiliary channel if the corresponding option is enabled in the renderer.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Falloff [3Fa]

The Falloff node

Falloff Node Overview

The Falloff node blends two materials or textures together based on the incidence angle between

the object to which the material is applied and the camera. This is useful when you wish to use one

material for portions of the geometry that would reflect light directly back to the camera and a different

material for parts that reflect light back into the scene.

Falloff example


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Inputs

The two Inputs on the Falloff node are used to connect two images or materials. One is used to reflect

back at the camera, while the other reflects away from the camera and into the scene.

Face On Material: The orange Face On material input accepts a 2D image or a 3D material. If a 2D

image is provided, it is turned into a diffuse texture map using the basic material shader. This input is

used for the material that is reflecting directly back to the camera

Glancing Material: The green Glancing material input accepts a 2D image or a 3D material. If a 2D

image is provided, it is turned into a diffuse texture map using the basic material shader. This input is

used for the material that is reflecting away from the camera and into the scene.

While the inputs for this node can be images, the output is always a material.

Basic Node Setup

The Falloff node below is used to control the strength of the Blinn material and the Reflect material.

You connect the Face On input of the Falloff node to the material you want shown for the sides of the

object that face the camera and connect the Glance input to the material you want shown for the sides

not directly facing the camera.

The Falloff node uses one input for the material facing the camera and one for the material not directly facing the camera.

Inspector

Falloff controls


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION

Controls Tab

The parameters in the Controls tabs modify the tint and opacity of the Face On material and the

Glancing material. A Falloff slider controls the blending between the two.

Color Variation

�Two Tone: Two regular Color controls define the colors for Glancing and Face On.

�Gradient: A Gradient control defines the colors for Glancing and Face On. This can be

used for a multitude of effects, like creating Toon Shaders, for example.

Face On Color

The Face On Color defines the color of surface parts facing the camera. If the Face On texture map is

provided, then the color value provided here is multiplied by the color values in the texture.

Reducing the material’s opacity decreases the color and Alpha values of the Face On material, making

the material transparent.

Glancing Color

The Glancing Color defines the color of surface parts more perpendicular to the camera. If the

Glancing material port has a valid input, then this input is multiplied by this color.

Reducing the material’s opacity decreases the color and Alpha values of the Glancing material, making

the material transparent.

Falloff

This value controls the transition between Glancing and Face On strength. It is very similar to a gamma

operation applied to a gradient, blending one value into another.

Material ID

This slider sets the numeric identifier assigned to this material. This value is rendered into the MatID

auxiliary channel if the corresponding option is enabled in the renderer.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.