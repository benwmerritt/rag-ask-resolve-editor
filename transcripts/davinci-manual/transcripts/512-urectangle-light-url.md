---
title: "uRectangle Light [uRL]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 512
---

# uRectangle Light [uRL]

The USD Rectangle light

uRectangle Light Node Introduction

A uRectangle light is a flat light, similar to softlight or window . The Controls tab are used to set the

color and brightness of the uRectangle light. The position, direction, and scale of the light source is

controlled in the Transform tab.

Inputs

There is one Scene Input in yellow to attach a USD scene; this allows you to adjust any existing lights

within the scene.

Inspector

The USD Rectangle Light controls


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Controls Tab

The Controls tab is used to set the color and brightness of the uDome light. The position, direction,

and scale of the light source is controlled in the Transform tab.

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

Shaping Focus

This defines focus point of the lens effect in this light.

Shaping Cone Angle

Defines the angle of spread of the light.

Width

Defines how wide the light appears.

Height

Defines how high the light appears.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

uSphere Light [uSL]

The USD Sphere light

uSphere Light Node Introduction

A uSphere light is local light that is similar to point light but also has radius. This light shows an

onscreen control. The rotation of the control is used to determine from where in the scene the light

direction is pointing.

Inputs

There is one Scene Input in yellow to attach a USD scene; this allows you to adjust any existing lights

within the scene.

Inspector

The USD Sphere Light controls

Controls Tab

The Controls tab is used to set the color and brightness of the uSphere light. The position, direction,

and scale of the light source is controlled in the Transform tab.

Override Selection

Pressing the Pick button lets you choose an existing light in an attached USD file to allow adjusting the

lights in an imported scene.

Color

Use this standard Color control to set the color of the light.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

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

Treat as Point

This will make the light a simple classic point source.

Radius

This sets the size of the sphere light.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

USD Material

The uTexture, uTextureTransform, uNormalMap, and uShader nodes give you the ability to import and

manipulate textures directly in your USD scene without having to wrap them in a USD file first. These

tools add flexibility and control to your USD workflow within the Fusion page.

A sample texture replacement node tree using the USD Materials tools

The uTexture, uTextureFormat, and uNormalMap tools are designed to work around and feed a texture

to the uShader tool, where it is manipulated using either the USD or MaterialX models to change its

appearance. The uShader is commonly connected to a uReplaceMaterial node, which selects the

specific parts of the entire USD scene to apply the new texture to. This workflow lets you quickly

iterate texture changes internally in Fusion, without requiring the modification of the original USD

scene in external 3D modeling software.

uNormalMap [uNm]

The USD Normal Map

Introduction

The uNormalMap tool provides several controls to modify a “normals” texture before it's passed on to

the uShader. This allows you to manipulate the texture in various ways and ensure that it is optimized

for your specific needs. Once any necessary adjustments have been made, the modified image is then

passed on to the uShader.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION