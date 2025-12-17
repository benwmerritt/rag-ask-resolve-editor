---
title: "Channel Boolean [3Bol]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 366
---

# Channel Boolean [3Bol]

The Channel Boolean node

Channel Boolean Node Introduction

The Channel Boolean (not to be confused with the 2D Channel Booleans) can be used to remap and

modify channels of 3D materials using mathematical operations. For example, if you want to use the

red channel of a material to control a scalar input of an illumination model that uses the Alpha channel

(e.g., Blinn. SpecularExponent), you can remap the channels here. Furthermore, it allows the use of

geometry-specific information like texture space coordinates and normals.

Inputs

There are two inputs on the Channel Boolean Node: one for the foreground material, and one for the

background material. Both inputs accept either a 2D image or a 3D material like Blinn, Cook-Torrence,

or Phong node.

BackgroundMaterial: The orange background material input accepts a 2D image or a 3D material.

ForegroundMaterial: The green foreground input also accepts a 2D image or a 3D material.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Basic Node Setup

There are many uses for the material 3D Channel Boolean. Most often it is used to combine material

looks or manipulate UV texture coordinates

In the below example, the Channel Boolean node combines the Cook Torrance and Blinn materials. It

uses the math operands in the Channel Boolean to switch, invert, and mix the two inputs, creating a

neon flickering effect.

A Channel Boolean used to combine and operate on Cook Torrance and Blinn nodes

Inspector

Channel Boolean controls


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Controls Tab

The Controls tab includes a section for each RGBA channel. Within each channel are two input menus

called Operand A and Operand B. The function performed on these two inputs is selected in the

Operation menu.

Operand A/B

The Operand menus, one for each output RGBA channel, allow you to set the desired input information

for the corresponding channel.

Red/Green/Blue/Alpha FG

Reads the color information of the foreground material.

Red/Green/Blue/Alpha BG

Reads the color information of the background material.

Black/White/Mid Gray

Sets the value of the channel to 0, 0.5, or 1.

Hue/Lightness/Saturation FG

Reads the color information of the foreground material, converts it

into the HLS color space, and puts the selected information into the

corresponding channel.

Hue/Lightness/Saturation BG

Reads the color information of the background material, converts it

into the HLS color space, and puts the selected information into the

corresponding channel.

Luminance FG

Reads the color information of the foreground material and

calculates the luminance value for the channel.

Luminance BG

Reads the color information of the background material and

calculates the luminance value for the channel.

X/Y/Z Position FG

Sets the value of the channel to the position of the pixel in 3D space.

The vector information is returned in eye space.

U/V/W Texture FG

Applies the texture space coordinates of the foreground material to

the channels.

U/V/W EnvCoords FG

Applies the environment texture space coordinates to the channels.

Use it upstream of nodes modifying the environment texture

coordinates like the Reflect 3D node.

X/Y/Z Normal

Sets the value of the channel to the selected axis of the normal

vector. The vector is returned in eye space.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Operation

Determines the Operation of how the operands are combined.

A

Uses Operand A only for the output channel.

B

Uses Operand B only for the output channel.

1-A

Subtracts the value of Operand A from 1.

1-B

Subtracts the value of Operand B from 1.

A+B

Adds the value of Operand A and B.

A-B

Subtracts the value of Operand B from A.

A*B

Multiplies the value of both Operands.

A/B

Divides the value of Operand B from A.

min(A,B)

Compares the values of Operands A and B and returns the smaller one.

max(A,B)

Compares the values of Operands A and B and returns the bigger one.

avg(A,B)

Returns the average value of both Operands.

Material ID

This slider sets the numeric identifier assigned to this material. This value is rendered into the MatID

auxiliary channel if the corresponding option is enabled in the renderer.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Cook Torrance [3CT]

The Cook Torrance node

Cook Torrance Node Introduction

The Cook Torrance node is a basic illumination material that can be applied to geometry in the 3D

scene. The diffuse calculation for this node is similar to that used in the basic material and the Blinn

node, but the specular highlights are evaluated using an optimized Fresnel/Beckmann equation. This

illumination model is primarily used for shading metal or other shiny and highly reflective surfaces.

The Cook Torrance node outputs a 3D Material that can be connected to the material inputs on any

3D geometry node.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Inputs

There are six inputs on the Cook Torrance node that accept 2D images or 3D materials. These inputs

control the overall color and image used for the 3D object as well as controlling the color and texture

used in the specular highlight. Each of these inputs multiplies the pixels in the texture map by the

equivalently named parameters in the node itself. This provides an effective method for scaling parts

of the material.

Diffuse Color Material: The orange Diffuse Color material input accepts a 2D image or a 3D material

to be used as overall color and texture of the object.

Specular Color Material: The green Specular Color material input accepts a 2D image or a 3D material

to be used as the color and texture of the specular highlight.

Specular Intensity Material: The magenta Specular Intensity material input accepts a 2D image or

a 3D material to alter the intensity of the specular highlight. When the input is a 2D image, the Alpha

channel is used to create the map, while the color channels are discarded.

Specular Roughness Material: The white Specular Roughness material input accepts a 2D image or

a 3D material to be used as a map for modifying the roughness of the specular highlight. The Alpha of

the texture map is multiplied by the value of the roughness control.

Specular Refractive Index Material: The white Specular Refractive Index material input accepts a 2D

image or a 3D material, using the RGB channels as the refraction texture.

Bump Map Material: The white Bump Map material input accepts only a 3D material. Typically, you

connect the texture into a Bump Map node, and then connect the Bump Map node to this input. This

input uses the RGB information as texture-space normals.

Each of these inputs multiplies the pixels in the texture map by the equivalently named parameters in

the node itself. This provides an effective method for scaling parts of the material.

When nodes have as many inputs as this one does, it is often difficult to make connections with any

precision. Hold down the Option (macOS) or Alt (Windows) key while dragging the output from another

node over the node tile, and keep holding Option or Alt when releasing the left mouse button. A small

drop-down menu listing all the inputs provided by the node appears. Click on the desired input to

complete the connection.

Basic Node Setup

The output of a Cook Torrance node output is connected to the material input on a 3D scene or

3D geometry node to which you want the shader applied. The Cook Torrance inputs can use images

as the diffuse color material (yellow) and specular color material (green). This can result in a smooth,

shiny material.

A Cook Torrance shader with diffuse and specular color materials connected


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION