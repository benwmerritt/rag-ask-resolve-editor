---
title: "Material Components"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 331
---

# Material Components

All the standard illumination models share certain characteristics that must be understood.

Diffuse

The Diffuse parameters of a material control the appearance of an object where light is absorbed

or scattered. This diffuse color and texture are the base appearance of an object, before taking into

account reflections. The opacity of an object is generally set in the diffuse component of the material.

Alpha

The Alpha parameter defines how much the object is transparent to diffuse light. It does not affect

specular levels or color. However, if the value of alpha, either from the slider or a Material input from

the diffuse color, is very close to or at zero, those pixels, including the specular highlights, will be

skipped and disappear.

Opacity

The Opacity parameter fades out the entire material, including the specular highlights. This value

cannot be mapped; it is applied to the entire material.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Specular

The Specular parameters of a material control the highlight of an object where the light is reflected

to the current viewpoint. This causes a highlight that is added to the diffuse component. The more

specular a material is, the glossier it appears. Surfaces like plastics and glass tend to have white

specular highlights, whereas metallic surfaces like gold have specular highlights that tend to inherit

their color from the material color.

Specularity is made up of color, intensity, and exponent. The specular color determines the color of

light that reflects from a shiny surface. Specular intensity is how bright the highlight will be.

Three spheres, left to right: diffuse only,

specular only, and combined

The specular exponent controls the falloff of the specular highlight. The larger the value, the sharper

the falloff and the smaller the specular component will be.

Left to right: white, complimentary, and matching specular colors

Transmittance

When using the software renderer, the Transmittance parameters control how light passes through a

semi-transparent material. For example, a solid blue pitcher will cast a black shadow, but one made of

translucent blue plastic would cast a much lower density blue shadow. The transmittance parameters

are essential to creating the appearance of stained glass.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

TIP: You can adjust the opacity and transmittance of a material separately. It is possible to

have a surface that is fully opaque yet transmits 100% of the light arriving upon it, so in a

sense it is actually a luminous/emissive surface.

Transmissive surfaces can be further limited using the Alpha and Color Detail control.

Attenuation

The transmittance color determines how much color is passed through the object. For an object to

have fully transmissive shadows, the transmittance color must be set to to RGB = (1, 1, 1), which means

100% of green, blue, and red light passes through the object. Setting this color to RGB = (1, 0, 0) means

that the material will transmit 100% of the red arriving at the surface but none of the green or blue light.

Alpha Detail

When the Alpha Detail slider is set to 0, the non-zero portions of the alpha channel of the diffuse color

are ignored and the opaque portions of the object casts a shadow. If it is set to 1, the alpha channel

determines how dense the object casts a shadow.

NOTE: The OpenGL renderer ignores alpha channels for shadow rendering, resulting in a

shadow always being cast from the entire object. Only the software renderer supports alpha

in the shadow maps.

The following examples for Alpha Detail and Color Detail cast a shadow using this image. It is

a green-red gradient from left to right. The outside edges are transparent, and inside is a small

semi‑transparent circle.

Alpha Detail set to 1; the alpha channel determines the density of the shadow


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Alpha Detail set to 0; a dense-colored shadow results

Color Detail

Color Detail is used to color the shadow with the object’s diffuse color. Increasing the Color Detail

slider from 0 to 1 brings in more diffuse color and texture into the shadow.

TIP: The OpenGL renderer will always cast a black shadow from the entire object, ignoring

the color. Only the software renderer supports color in the shadow maps.

Color Detail set to 0; no color is visible in the shadow.

Saturation

Saturation will allow the diffuse color texture to be used to define the density of the shadow without

affecting the color. This slider lets you blend between the full color and luminance only.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Transmittance and Shadows

The transmittance of an object’s material plays an important role in determining the appearance of

the shadow it casts. Normally, the transmittance behavior is defined in each object’s Materials tab as

explained above. However, selecting Force All Materials Non-Transmissive in the Spotlight Inspector

overrides this, causing the shadow map produced by the spotlight to ignore transmittance entirely.

Illumination Models

Now that you understand the different components that make up a material or shader, we’ll look at

them more specifically. Illumination models are advanced materials for creating realistic surfaces like

plastic, wood, or metal. Each illumination model has advantages and disadvantages, which make it

appropriate for particular looks. An illumination model determines how a surface reacts to light, so

these nodes require at least one light source to affect the appearance of the object. Four different

illumination models can be found in the Nodes > 3D > Material menu.

Illumination models left to right: Standard, Blinn, Phong, Cook-Torrance, and Ward

Standard

The Standard material provides a default Blinn material with basic control over the diffuse, specular,

and transmittance components. It only accepts a single texture map for the diffuse component with the

alpha used for opacity. The Standard Material controls are found in the Material tab of all nodes that

load or create geometry. Connecting any node that outputs a material to that node’s Material Input will

override the Standard material, and the controls in the Material tab will be hidden.

Blinn

The Blinn material is a general purpose material that is flexible enough to represent both metallic and

dielectric surfaces. It uses the same illumination model as the Standard material, but the Blinn material

allows for a greater degree of control by providing additional texture inputs for the specular color,

intensity, and exponent (falloff), as well as bump map textures.

Phong

The Phong material produces the same diffuse result as Blinn, but with wider specular highlights at

grazing incidence. Phong is also able to make sharper specular highlights at high exponent levels.

Cook-Torrance

The Cook-Torrance material combines the diffuse illumination model of the Blinn material with a

combined microfacet and Fresnel specular model. The microfacets need not be present in the mesh

or bump map; they are represented by a statistical function, Roughness, which can be mapped.

The Fresnel factor attenuates the specular highlight according to the Refractive Index, which can

be mapped.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Ward

The Ward material shares the same diffuse model as the others but adds anisotropic highlights,

ideal for simulating brushed metal or woven surfaces, as the highlight can be elongated in the U or

V directions of the mapping coordinates. Both the U and V spread functions are mappable.

This material does require properly structured UV coordinates on the meshes it is applied to.