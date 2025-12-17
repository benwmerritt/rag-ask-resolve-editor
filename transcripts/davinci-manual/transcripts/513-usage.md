---
title: "Usage"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 513
---

# Usage

The uNormal Map controls

To use uNormalMap, place it after a uTexture node and before a uShader node. This node node only

works between the the loaded texture and uShader.

uShader [uSd]

The USD Shader

uShader Node Introduction

The uShader node is used to create materials and looks using either the USD or MaterialX shader

tools. Used in conjunction with uReplaceMaterial, this tool gives an easy and intuitive way to iterate

material changes to a USD source.

Inputs

The uShader node has variable inputs that allow you to import different assets into the tool, such as

a texture, by using a uTexture node. When connecting the tool, you can choose from a drop list of

all possible connections. Connecting a texture to any input will disable its corresponding slider and

expose new Channel, Scale, and Bias controls to let you choose which channel the property uses, with

their strength and base values.

Attaching a uTexture node to the uShader node presents a

drop list, showing all possible inputs to connect to.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Basic Node Setup

The uShader is accepting an input from the uTexture node, modifying that texture, then

passing it to the uReplace Material node. uReplace Material is selecting specific materials

from the MonsterJumpDown USD scene to apply the newly modified texture to.

Inspector

The uShader controls in USD mode

Shader Model

Here you can choose what toolset to work with, either USD or MaterialX tools.

Shader Model: USD

Diffuse Mode

Diffuse describes the base surface characteristics without any additional effects like reflections or

specular highlights.

�Color: Provides controls to modify the shape’s diffuse color.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Emissive

Emissive adds a global lighting effect to a shape, creating a layer of color over the existing texture. It

can be adjusted to different levels of intensity and can be used to simulate the emission of light.

Workflow Mode

Lets you set the mode between Metallic and Specular.

�Metallic: When enabled, this control shows the Metallic slider. The Metallic slider adds a reflective

quality to objects, creating the appearance of metal. It enhances the reflective properties of

a shape.

�Specular: When enabled, this shows the Specular Color controls. Specular Color determines

the color of light that reflects from a shiny surface. The more specular a material is, the glossier

it appears.

Roughness

Affects the amount of light reflection and scattering on a surface, giving it a smoother or more textured

appearance, depending on the setting. It is a key element in creating realistic reflections.

Clearcoat

Affects the appearance of a surface by adding a glossy layer on top of it, mimicking the effect of a

protective coating. It is commonly used in creating materials like car paint or polished metal.

Clearcoat Roughness

Adjusts the level of imperfection or smoothness of the glossy layer added on top of a surface. This can

affect the realism and reflection of materials like car paint or polished metal.

Opacity

Reduces the material and object opacity, impacting the color and Alpha values of the shape.

Shader Model: MaterialX

The uShader controls in MaterialX mode


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

Controls

MaterialX is an open standard maintained by the Academy Software Foundation designed for creating

material and look development content that is platform independent. MaterialX is under constant

development, and you can find the latest specifications at the MaterialX website: materialx.org

uTexture [uTx]

The USD Texture

Introduction

To create a material/surface in the uShader, you can import a texture file using this tool. The uTexture

sources image files and uses them to build the material/surface in the uShader.

Usage

The uTexture controls

After adding the node to the Node Editor, use the Browse button to select an image file from your hard

drive. Alternatively, you can click and drag an image from the Media Pool directly onto the “File Name”

control in the Inspector to load an image which has already been imported into DaVinci Resolve.

Use the “Source Color Space” control to choose how the image will be read by the uTexture tool. It’s

important select Linear when loading a Normals image to get the best results.

U/V Address Mode controls offer a useful way to determine how the edges of the image are treated

when exposed due to scaling.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION

uTextureTransform [uTXf]

The USD Texture Transform

Introduction

uTextureTransform provides you with granular control over the scale, rotation, and position of each

loaded texture file. With uTexture Transform, you can quickly and easily tweak the size, orientation, and

placement of any texture file sourced from the uTexture node.

Usage

The uTexture Transform controls

To use uTextureTransform, place it after a uTexture node and before a uShader node. This node only

works between the the loaded texture and uShader.

Adjust the Scale, Rotation, and Position settings to your liking.

The Scale setting allows you to increase or decrease the size of the texture file, while the Position

setting lets you move the file around within your project. You can also use the Rotation setting to

rotate the texture file to any angle you desire.


Fusion Page Effects | Chapter 121 USD Nodes

FUSION