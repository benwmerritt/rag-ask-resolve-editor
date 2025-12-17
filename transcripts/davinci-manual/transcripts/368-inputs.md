---
title: "Inputs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 368
---

# Inputs

There are five inputs on the Phong node that accept 2D images or 3D materials. These inputs

control the overall color and image used for the 3D object as well as controlling the color and texture

used in the specular highlight. Each of these inputs multiplies the pixels in the texture map by the

equivalently named parameters in the node itself. This provides an effective method for scaling parts

of the material.

Diffuse Material: The orange Diffuse material input accepts a 2D image or a 3D material to be used as

a main color and texture of the object.

Specular Color Material: The green Specular Color material input accepts a 2D image or a 3D material

to be used as a highlight color and texture of the object.

Specular Intensity Material: The magenta Specular Intensity material input accepts a 2D image or a

3D material to be used as an intensity map for the material’s highlights. When the input is a 2D image,

the Alpha channel is used to create the map, while the color channels are discarded.

Specular Exponent Material: The teal Specular Exponent material input accepts a 2D image or a 3D

material to be used as a falloff map for the material’s specular highlights. When the input is a 2D image,

the Alpha channel is used to create the map, while the color channels are discarded.

Bump Map Material: The white Bump Map texture input accepts only a 3D material. Typically, you

connect the texture into a Bump Map node, and then connect the Bump Map node to this input. This

input uses the RGB information as texture-space normals.

When nodes have as many inputs as this one does, it is often difficult to make connections with

any precision. Hold down the Option or Alt key while dragging the output from another node

over the node tile, and keep holding Option or Alt when releasing the left mouse button. A small

drop-down menu listing all the inputs provided by the node appears. Click on the desired input to

complete the connection.

Basic Node Setup

The output of a Phong node is connected to the material input on a 3D scene or 3D geometry node.

The Phong node below is taking in a base Color Diffuse input from the Fast Noise node and a bump

map texture also generated from a Fast Noise node.

A Phong node with a diffuse color and Bump Map input


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Inspector

Phong controls

Controls Tab

The Controls tab contains parameters for adjusting the main color, highlight, and lighting properties of

the Phong shader node.

Diffuse

Diffuse describes the base surface characteristics without any additional effects like reflections or

specular highlights. Besides defining the base color of an object, the diffuse color also defines the

transparency of the object.

The Alpha in a diffuse texture map can be used to make portions of the surface transparent.

Diffuse Color

A material’s Diffuse Color describes the base color presented by the material when it is lit indirectly or

by ambient light. If a diffuse texture map is provided, then the color value provided here is multiplied

by the color values in the texture.

Alpha

This slider sets the material’s Alpha channel value. This affects diffuse and specular colors equally and

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

Specular Exponent

Specular Exponent controls the falloff of the specular highlight. The greater the value, the sharper

the falloff, and the smoother and glossier the material appears. If the specular exponent texture is

provided, then this value is multiplied by the Alpha value of the texture map.

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


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

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

Fusion does exactly the same thing as 3D applications when you make a surface two sided. The

confusion about what two-sided lighting does arises because Fusion does not cull back-facing

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


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Reflect [3Rr]

The Reflect node

Reflect Node Introduction

The Reflect node is used to add environment map reflections and refractions to materials.

Control is offered over the face on and glancing strength, falloff, per channel refraction indexes, and

tinting. Several texture map inputs can modify the behavior of each parameter.

Environment mapping is an approximation that assumes an object’s environment is infinitely distant

from the object. It’s best to picture this as a cube or sphere with the object at the center. Specifically,

this infinite distance assumption means that objects cannot interact with themselves (e.g., the

reflections on the handle of a teapot do not show the body of the teapot but rather the infinite

environment map). It also means that if you use the same cube map on multiple objects in the scene,

those objects do not inter-reflect each other (e.g., two neighboring objects would not reflect each

other). If you want objects to reflect each other, you need to render a cube map for each object.

For more information, see Chapter 85, “3D Compositing Basics,” in the DaVinci Resolve

Reference Manual, or Chapter 25 in the Fusion Reference Manual.

Inputs

There are five inputs on the Reflect node that accept 2D images or 3D materials. These inputs control

the overall color and image used for the 3D object as well as controlling the color and texture used in

the reflective highlights.

Background Material: The orange Background material input accepts a 2D image or a 3D material. If a

2D image is provided, the node treats it as a diffuse texture map applied to a basic material.

Reflection Color Material: The white Reflection Color material input accepts a 2D image or a

3D material. The RGB channels are used as the reflection texture, and the Alpha is ignored.

Reflection Intensity Material: The white Reflection Intensity material input accepts a 2D image or a

3D material. The Alpha channel of the texture is multiplied by the intensity of the reflection.

Refraction Tint Material: The white Refraction Tint material input accepts a 2D image or a 3D material.

The RGB channels are used as the refraction texture.

Bump Map Texture: The white Bump Map texture input accepts only a 3D material. Typically, you

connect the texture into a Bump Map node, and then connect the Bump Map node to this input. This

input uses the RGB information as texture-space normals.

When nodes have as many inputs and some using the same color as this one does, it is often difficult

to make connections with any precision. Hold down the Option or Alt key while dragging the output

from another node over the node tile, and keep holding Option or Alt when releasing the left mouse

button. A small drop-down menu listing all the inputs provided by the node appears. Click on the

desired input to complete the connection.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION