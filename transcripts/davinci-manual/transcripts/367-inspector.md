---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 367
---

# Inspector

Cook Torrance controls

Controls Tab

The Controls tab contains parameters for adjusting the main color, highlight, and lighting properties of

the Cook Torrance shader node.

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

This slider sets the material’s Alpha channel value. This affects diffuse and specular colors equally, and

affects the Alpha value of the material in the rendered output. If a diffuse texture map is provided, then

the Alpha value set here is multiplied by the Alpha values in the texture map.

Opacity

Reducing the material’s Opacity decreases the color and Alpha values of the specular and diffuse

colors equally, making the material transparent.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

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

Roughness

The Roughness of the specular highlight describes diffusion of the specular highlight over the

surface. The greater the value, the wider the falloff, and the more brushed and metallic the surface

appears. If the roughness texture map is provided, then this value is multiplied by the Alpha value from

the texture.

Do Fresnel

Selecting this checkbox adds Fresnel calculations to the materials illumination model. This provides

more realistic-looking metal surfaces by taking into account the refractiveness of the material.

Refractive Index

This slider appears when the Do Fresnel checkbox is selected. The Refractive Index applies only to

the calculations for the highlight; it does not perform actual refraction of light through transparent

surfaces. If the refractive index texture map is provided, then this value is multiplied by the Alpha value

of the input.

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

the red arriving at the surface but none of the green or blue light. This can be used to create “stained

glass”-styled shadows.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

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


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Material Merge 3D [3MM]

The Material Merge node

Material Merge Node Introduction

The Material Merge node can be used to combine two separate materials together. This node can be

used to composite Material nodes, combining multiple illumination materials (Blinn, Cook Torrance)

with texture nodes (Bump Map, Reflection) to create complex shader networks.

The node also provides a mechanism for assigning a new material identifier to the combined material.

Inputs

The Material Merge node includes two inputs for the two materials you want to combine.

Background Material: The orange Background material input accepts a 2D image or a 3D material to

be used as the background material.

Foreground Material: The green Foreground material input accepts a 2D image or a 3D material to be

used as the foreground material. A 2D image is treated as a diffuse texture map in the basic shading

model.

Basic Node Setup

The output of a Material Merge node is connected to the material input on a 3D scene or 3D geometry

node. The Material Merge node below is taking in a background base layer from the Blinn shader and

combining it with a more textured bump map layer.

A Material Merge node combining a Blinn-based shader (teal underlay) and a Ward-based shader (orange underlay)


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Inspector

Material Merge controls

Controls Tab

The Controls tab includes a single slider for blending the two materials together.

Blend

The Blend behavior of the Material Merge is similar to the Dissolve (DX) node for images. The two

materials/textures are mixed using the value of the slider to determine the percentage each input

contributes. While the background and foreground inputs can be a 2D image instead of a material, the

output of this node is always a material.

Unlike the 2D Dissolve node, both foreground and background inputs are required.

Material ID

This slider sets the numeric identifier assigned to the resulting material. This value is rendered into the

MatID auxiliary channel if the corresponding option is enabled in the renderer.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Phong [3Ph]

The Phong node

Phong Node Introduction

The Phong node is a basic illumination material that can be applied to geometry in the 3D scene.

It describes how the object responds to light and provides multiple texture map inputs to allow fine

control over the diffuse, specular, and bump map components of the material.

While producing a highlight similar to that produced by the Blinn model, it is more commonly used for

shiny/polished plastic surfaces.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION