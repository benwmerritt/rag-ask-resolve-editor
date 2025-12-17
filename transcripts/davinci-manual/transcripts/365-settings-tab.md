---
title: "Settings Tab"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 365
---

# Settings Tab

Common Settings 3D controls

The Common Settings tab can be found on almost every tool found in Fusion. The following controls

are specific settings for 3D nodes.

Hide Incoming Connections

Enabling this checkbox can hide connection lines from incoming nodes, making a node tree appear

cleaner and easier to read. When enabled, fields for each input on a node are displayed. Dragging a

connected node from the node tree into the field hides that incoming connection line as long as the

node is not selected in the node tree. When the node is selected in the node tree, the line reappears.


Fusion Page Effects | Chapter 90 3D Light Nodes

FUSION

Comment Tab

The Comment tab contains a single text control that is used to add comments and notes to the tool.

When a note is added to a tool, a small red dot icon appears next to the setting’s tab icon, and a text

bubble appears on the node. To see the note in the Node Editor, hold the mouse pointer over the

node for a moment. The contents of the Comments tab can be animated over time, if required.

Scripting Tab

The Scripting tab is present on every tool in Fusion. It contains several edit boxes used to add scripts

that process when the tool is rendering. For more details on the contents of this tab, please consult the

scripting documentation.


Fusion Page Effects | Chapter 90 3D Light Nodes

FUSION

Chapter 91

3D Material Nodes

This chapter details the 3D Material nodes available when creating 3D composites

in Fusion. The abbreviations next to each node name can be used in the Select

Tool dialog when searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Blinn [3Bl]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2005

Channel Boolean [3Bol]������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2009

Cook Torrance [3CT]������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2012

Material Merge 3D [3MM]��������������������������������������������������������������������������������������������������������������������������������������������������������������� 2017

Phong [3Ph]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2018

Reflect [3Rr]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2023

Stereo Mix [3SMM]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2026

Ward [3Wd]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2027

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2032


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Blinn [3Bl]

The Blinn node

Blinn Node Introduction

The Blinn node is a basic illumination material that can be applied to geometry in the 3D scene. It

describes how the object responds to light and provides multiple texture map inputs to allow fine

control over the diffuse, specular, and bump map components of the material.

The standard basic material provided in the Materials tab of most geometry nodes is a simplified

version of the Blinn node. The primary difference is that the Blinn node provides additional texture

map inputs beyond just diffuse.

The Blinn node outputs a 3D Material that can be connected to the material inputs on any

3D geometry node.

The Blinn model in Fusion calculates the highlight as the dot product of the surface normal and the half

angle vector between light source and viewer (dot(N, H)). This may not always match the Blinn model

illumination model used by other 3D applications.

Inputs

There are five inputs on the Blinn node that accept 2D images or 3D materials. These inputs control

the overall color and image used for the 3D object as well as the color and texture used in the

specular highlight. Each of these inputs multiplies the pixels in the texture map by the equivalently

named parameters in the node itself. This provides an effective method for scaling parts of

the material.

Diffuse Texture: The orange Diffuse Texture input accepts a 2D image or a 3D material to be used as

a main object texture map.

Specular Color Material: The green Specular Color material input accepts a 2D image or a 3D material

to be used as the color texture map for specula highlight areas.

Specular Intensity Materials: The magenta Specular Intensity material input accepts a 2D image or a

3D material to be used to alter the intensity of specular highlights. When the input is a 2D image, the

Alpha channel is used to create the map, while the color channels are discarded.

Specular Exponent Material: The teal Specular Exponent material input accepts a 2D image or a

3D material that is used as a falloff map for the material’s specular highlights. When the input is a 2D

image, the Alpha channel is used to create the map, while the color channels are discarded.

Bump Map Material: The white Bump Map material input accepts only a 3D material. Typically, you

connect the texture into a Bump Map node, and then connect the Bump Map node to this input. This

input uses the RGB information as texture-space normals.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

When nodes have as many inputs as this one does, it is often difficult to make connections with any

precision. Hold down the Option (macOS) or Alt (Windows) key while dragging the output from another

node over the node tile, and keep holding Option or Alt when releasing the left mouse button. A small

drop-down menu listing all the inputs provided by the node appears. Click on the desired input to

complete the connection. Alternatively, you can drag the output from a node with the right mouse

button to activate the same menu.

Basic Node Setup

The output of a Blinn node output is connected to the material input on a 3D scene or 3D geometry

node to which you want the shader applied. The Blinn inputs can use images as the diffuse color

material (orange) and specular color material (green). This can lead to a smooth, shiny material.

A Blinn shader with diffuse and specular color materials connected

Inspector

Blinn controls


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Controls Tab

The Controls tab is the primary tab for the Blinn node. It controls the color and shininess applied to the

surface of the 3D geometry.

Diffuse

Diffuse describes the base surface characteristics without any additional effects like reflections or

specular highlights. Besides defining the base color of an object, the diffuse color also defines the

transparency of the object. The Alpha in a diffuse texture map can be used to make portions of the

surface transparent.

Diffuse Color

A material’s Diffuse Color describes the base color presented by the material when it is lit indirectly or

by ambient light. If a diffuse texture map is provided, then the color value provided here is multiplied

by the color values in the texture.

Alpha

This slider sets the material’s Alpha channel value. This affects diffuse and specular colors equally and

affects the Alpha value of the material in the rendered output. If a diffuse texture map is provided, then

the Alpha value set here is multiplied by the Alpha values in the texture map.

Opacity

Reducing the material’s opacity decreases the color and Alpha values of the specular and diffuse

colors equally, making the material transparent.

Specular

The parameters in the Specular section describe the look of the specular highlight of the surface.

These values are evaluated in a different way for each illumination model.

Specular Color

Specular Color determines the color of light that reflects from a shiny surface. The more specular

a material is, the glossier it appears. Surfaces like plastics and glass tend to have white specular

highlights, whereas metallic surfaces like gold have specular highlights that inherit their color from the

material color. If a specular texture map is provided, then the value provided here is multiplied by the

color values from the texture.

Specular Intensity

Specular Intensity controls how strong the specular highlight is. If the specular intensity texture is

provided, then this value is multiplied by the Alpha value of the texture.

Specular Exponent

Specular Exponent controls the falloff of the specular highlight. The greater the value, the sharper

the falloff, and the smoother and glossier the material appears. If the specular exponent texture is

provided, then this value is multiplied by the Alpha value of the texture map.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Transmittance

Transmittance controls the way light passes through a material. For example, a solid blue sphere

casts a black shadow, but one made of translucent blue plastic would cast a much lower density

blue shadow.

There is a separate Opacity option. Opacity determines how transparent the actual surface is when

it is rendered. Fusion allows adjusting both opacity and transmittance separately. At first, this might

be a bit counterintuitive to those who are unfamiliar with 3D software. It is possible to have a surface

that is fully opaque but transmits 100% of the light arriving upon it, effectively making it a luminous/

emissive surface.

Attenuation

Attenuation determines how much color is passed through the object. For an object to have

transmissive shadows, set the attenuation to (1, 1, 1), which means 100% of green, blue, and red light

passes through the object. Setting this color to RGB (1, 0, 0) means that the material transmits 100% of

the red arriving at the surface but none of the green or blue light. This can be used for “stained glass”-

styled shadows.

Alpha Detail

When the Alpha Detail slider is set to 0, the Alpha channel of the object is ignored and the entire

object casts a shadow. If it is set to 1, the Alpha channel determines what portions of the object

cast a shadow.

Color Detail

The Color Detail slider modulates light passing through the surface by the diffuse color + texture

colors. Use this to throw a shadow that contains color details of the texture applied to the object.

Increasing the slider from 0 to 1 brings in more diffuse color + texture color into the shadow. Note that

the Alpha and opacity of the object are ignored when transmitting color, allowing an object with a solid

Alpha to still transmit its color to the shadow.

Saturation

The Saturation slider controls the saturation of the color component transmitted to the shadow. Setting

this to 0.0 results in monochrome shadows.

Receives Lighting/Shadows

These checkboxes control whether the material is affected by lighting and shadows in the scene. If

turned off, the object is always fully lit and/or unshadowed.

Two-Sided Lighting

This effectively makes the surface two sided by adding a second set of normals facing the opposite

direction on the backside of the surface. This is normally off to increase rendering speed, but it can

be turned on for 2D surfaces or for objects that are not fully enclosed, to allow the reverse or interior

surfaces to be visible as well.

Normally, in a 3D application, only the front face of a surface is visible and the back face is culled, so

that if a camera were to revolve around a plane in a 3D application, when it reached the backside, the

plane would become invisible. Making a plane two sided in a 3D application is equivalent to adding

another plane on top of the first but rotated by 180 degrees so the normals are facing the opposite

direction on the backside. Thus, when you revolve around the back, you see the second image plane,

which has its normals facing the opposite way.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Fusion does exactly the same thing as 3D applications when you make a surface two sided.

The confusion about what two-sided lighting does arises because Fusion does not cull back-facing

polygons by default. If you revolve around a one-sided plane in Fusion, you still see it from the

backside (but you are seeing the frontside duplicated through to the backside as if it were transparent).

Making the plane two sided effectively adds a second set of normals to the backside of the plane.

NOTE: This can become rather confusing once you make the surface transparent, as the

same rules still apply and produce a result that is counterintuitive. If you view from the

frontside a transparent two-sided surface illuminated from the backside, it looks unlit.

Material ID

This slider sets the numeric identifier assigned to this material. This value is rendered into the MatID

auxiliary channel if the corresponding option is enabled in the renderer.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.