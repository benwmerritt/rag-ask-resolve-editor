---
title: "Modifier"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 360
---

# Modifier

Coordinate Transform 3D

Because of the hierarchical nature of the Fusion 3D node tree, the original position of an object in

the 3D scene often fails to indicate the current position of the object. For example, an image plane

might initially have a position at 1, 2, 1, but then be scaled, offset, and rotated by other nodes further

downstream in the 3D scene, ending up with an absolute location of 10, 20, 5.

This can complicate connecting an object further downstream in the composition directly to the position

of an upstream object. The Coordinate Transform modifier can be added to any set of XYZ coordinate

controls and calculate the current position of a given object at any point in the scene hierarchy.

To add a Coordinate Transform modifier, simply right-click a number field on any node and select

Modify With/CoordTransform Position from the Controls’ contextual menu.

Inspector

Weld 3D modifier tools

Target Object

This control should be connected to the 3D node that produces the original coordinates to be

transformed. To connect a node, drag and drop a node from the node tree into the Text Edit control,

or right-click the control and select the node from the contextual menu. It is also possible to type the

node’s name directly into the control.

Sub ID

The Sub ID slider can be used to target an individual sub-element of certain types of geometry, such as

an individual character produced by a Text 3D node or a specific copy created by a Duplicate 3D node.

Scene Input

This control should be connected to the 3D node that outputs the scene containing the object at the

new location. To connect a node, drag and drop a node from the node tree into the Text Edit control,

or right-click the control and select an object from the Connect To submenu.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

The Common Controls

Nodes that handle 3D geometry share several identical controls in the Inspector. This section

describes controls that are common among 3D nodes.

Common Controls Tab

Common Controls 3D tab

These controls are often displayed in the lower half of the Controls tab. They appear in nodes that

create or contain 3D geometry.

Visibility

�Visible: If this option is enabled, the object is visible in the viewers and in final renders. When

disabled, the object is not visible in the viewers nor is it rendered into the output image by the

Renderer 3D node. Also, a non-visible object does not cast shadows.

�Unseen by Cameras: When the Unseen by Cameras checkbox is enabled, the object is visible

in the viewers (unless the Visible checkbox is disabled), except when viewed through a camera.

Also, the object is not rendered into the output image by the Renderer 3D node. However,

shadows cast by an unseen object are still visible when rendered by the software renderer in the

Renderer 3D node, though not by the OpenGL renderer.

�Cull Front Face/Back Face: Use these options to eliminate rendering and display of certain

polygons in the geometry. If Cull Back Face is selected, polygons facing away from the camera are

not rendered and do not cast shadows. If Cull Front Face is selected, polygons facing toward the

camera are not rendered and do not cast shadows. Enabling both options has the same effect as

disabling the Visible checkbox.

�Suppress Aux Channels for Transparent Pixels: In previous versions of Fusion, transparent pixels

were excluded by the software and Open GL render options in the Renderer 3D node. To be

more specific, the software renderer excluded pixels with R,G,B,A set to 0, and the GL renderer


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

excluded pixels with A set to 0. This is now optional. The reason you might want to do this is to

get aux channels (e.g., Normals, Z, UVs) for the transparent areas. For example, suppose you want

to replace the texture on a 3D element that is transparent in certain areas with a texture that is

transparent in different areas. It would then be useful to have transparent areas set aux channels

(particularly UVs). As another example, suppose you are adding depth of field. You probably do

not want the Z-channel to be set on transparent areas, as this gives you a false depth. Also, keep

in mind that the exclusion is based on the final pixel color including lighting, if it is on. So, if you

have a specular highlight on a clear glass material, this checkbox does not affect it.

Lighting

�Affected by Lights: Disabling this checkbox causes lights in the scene to not affect the object.

The object does not receive nor cast shadows, and it is shown at the full brightness of its color,

texture, or material.

�Shadow Caster: Disabling this checkbox causes the object not to cast shadows on other objects

in the scene.

�Shadow Receiver: Disabling this checkbox causes the object not to receive shadows cast by

other objects in the scene.

Matte

Enabling the Is Matte option applies a special texture, causing the object to not only become invisible

to the camera, but also making everything that appears directly behind the camera invisible as well.

This option overrides all textures.

For more information on Fog 3D and Soft Clipping, see Chapter 85, “3D Compositing Basics,”

in the DaVinci Resolve Reference Manual, or Chapter 25 in the Fusion Reference Manual.

�Is Matte: When activated, objects whose pixels fall behind the matte object’s pixels in Z do not get

rendered. Two additional options are displayed when the Is Matte checkbox is activated.

�Opaque Alpha: When the Is Matte checkbox is enabled, the Opaque Alpha checkbox sets the

Alpha value of the matte object to 1.

�Infinite Z: This option sets the value in the Z-channel to infinite. This checkbox is visible only when

the Is Matte option is enabled.

Blend Mode

A Blend mode specifies which method is used by the renderer when combining this object with the

rest of the scene. The blend modes are essentially identical to those listed in the section for the 2D

Merge node. For a detailed explanation of each mode, see the section for that node.

The blending modes were originally designed for use with 2D images. Using them in a lit 3D

environment can produce undesirable results. For best results, use the Apply modes in unlit 3D

scenes using the software option in the Renderer 3D node.

�OpenGL Blend Mode: Use this menu to select the blending mode that is used when the geometry

is processed by the OpenGL renderer in the Renderer 3D node. This is also the mode used when

viewing the object in the viewers. Currently the OpenGL renderer supports a limited number of

blending modes.

�Software Blend Mode: Use this menu to select the blending mode that is used when the

geometry is processed by the software renderer. Currently, the software renderer supports all the

modes described in the Merge node documentation, except for the Dissolve mode.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Normal/Tangents

Normals are imaginary lines perpendicular to each point on the surface of an object. They are used

to illustrate the exact direction and orientation of every polygon on 3D geometry. Knowing the

direction and orientation determines how the object gets shaded. Tangents are lines that exists along

the surface’s plane. These lines are tangent to a point on the surface. The tangent lines are used to

describe the direction of textures you apply to the surface of 3D geometry.

�Scale: This slider increases or decreases the length of the vectors for both normals and tangents.

�Show Normals: Displays blue vectors typically extending outside the surface of the geometry.

These normal vectors help indicate how different areas of the surface are illuminated based on the

angle at which the light hits it.

�Show Tangents: Displays green vectors for Y and red vectors of X. The X and Y vectors represent

the direction of the image or texture you are applying to the geometry.

Object ID

Use this slider to select which ID is used to create a mask from the object of an image. Use the

Sample button in the same way as the Color Picker to grab IDs from the image displayed in the

viewer. The image or sequence must have been rendered from a 3D software package with those

channels included.

Common Materials Tab

The controls in the Materials tab are used to determine the appearance of the 3D object when lit.

Most of these controls directly affect how the object interacts with light using a basic shader. For more

advanced control over the objects appearance, you can use tools from the 3D Materials category of

the Effects Library. These tools can be used to assemble a more finely detailed and precise shader.

Common Materials 3D tab


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

When a shader is constructed using the 3D Material tools and connected to the 3D Object’s material

input, the controls in this tab are replaced by a label that indicates that an external material is

currently in use.

Diffuse

Diffuse describes the base surface characteristics without any additional effects like reflections or

specular highlights.

Diffuse Color

The Diffuse Color determines the basic color of an object when the surface of that object is either

lit indirectly or lit by an ambient light. If a valid image is provided to the tools diffuse texture input,

then the RGB values provided here are also multiplied by the color values of the pixels in the

diffuse texture. The Alpha channel of the diffuse material can be used to control the transparency of

the surface.

Alpha

This slider sets the material’s Alpha channel value. This affects diffuse and specular colors equally, and

affects the Alpha value of the material in the rendered output. If the tools diffuse texture input is used,

then the Alpha value provided here is multiplied by the Alpha channel of the pixels in the image.

Opacity

Reducing the material’s Opacity decreases the color and Alpha values of the specular and diffuse

colors equally, making the material transparent and allowing hidden objects to be seen through the

material.

Specular

The Specular section provides controls for determining the characteristics of light that reflects toward

the viewer. These controls affect the appearance of the specular highlight that appears on the surface

of the object.

Specular Color

Specular Color determines the color of light that reflects from a shiny surface. The more specular

a material is, the glossier it appears. Surfaces like plastics and glass tend to have white specular

highlights, whereas metallic surfaces like gold have specular highlights that tend to inherit their color

from the material color. The basic shader material does not provide an input for textures to control

the specularity of the object. Use tools from the 3D Material category when more precise control is

required over the specular appearance.

Specular Intensity

Specular Intensity controls how strong the specular highlight is. If the specular intensity texture input

has a valid connection, then this value is multiplied by the Alpha value of the input.

Specular Exponent

Specular Exponent controls the falloff of the specular highlight. The greater the value, the sharper

the falloff, and the smoother and glossier the material appears. The basic shader material does not

provide an input for textures to control the specular exponent of the object. Use tools from the 3D

Material category when more precise control is required over the specular exponent.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Transmittance

Transmittance controls the way light passes through a material. For example, a solid blue sphere

casts a black shadow, but one made of translucent blue plastic would cast a much lower density

blue shadow.

There is a separate opacity option. Opacity determines how transparent the actual surface is when

it is rendered. Fusion allows adjusting both opacity and transmittance separately. This might be a bit

counter-intuitive to artists who are unfamiliar with 3D software at first. It is possible to have a surface

that is fully opaque but transmits 100% of the light arriving upon it, effectively making it a luminous/

emissive surface.

Attenuation

Attenuation determines how much color is transmitted through the object. For an object to have

transmissive shadows, set the attenuation to (1, 1, 1), which means 100% of green, blue, red light passes

through the object. Setting this color to RGB (1, 0, 0) means that the material transmits 100% of the red

arriving at the surface but none of the green or blue light. This allows “stained glass” shadows.

Alpha Detail

When the Alpha Detail slider is set to 0, the Alpha channel of the object is ignored and the entire object

casts a shadow. If it is set to 1, the Alpha channel determines what portions of the object cast a shadow.

Color Detail

The Color Detail slider modulates light passing through the surface by the diffuse color + texture

colors. Use this to throw a shadow that contains color details of the texture applied to the object.

Increasing the slider from 0 to 1 brings in more of diffuse color + texture color into the shadow. Note

that the Alpha and opacity of the object are ignored when transmitting color, allowing an object with a

solid Alpha to still transmit its color to the shadow.

Saturation

The Saturation slider controls the saturation of the color component transmitted to the shadow. Setting

this to 0.0 results in monochrome shadows.

Receives Lighting/Shadows

These checkboxes control whether the material is affected by lighting and shadows in the scene.

If turned off, the object is always fully lit and/or unshadowed.

Two-Sided Lighting

This makes the surface effectively two-sided by adding a second set of normals facing the opposite

direction on the back side of the surface. This is normally off, to increase rendering speed, but can

be turned on for 2D surfaces or for objects that are not fully enclosed, to allow the reverse or interior

surfaces to be visible as well.

Normally, in a 3D application, only the front face of a surface is visible and the back face is culled, so

that if a camera were to revolve around a plane in a 3D application, when it reached the backside, the

plane would become invisible. Making a plane two sided in a 3D application is equivalent to adding

another plane on top of the first but rotated by 180 degrees so the normals are facing the opposite

direction on the backside. Thus, when you revolve around the back, you see the second image plane

that has its normals facing the opposite way.

Fusion does exactly the same thing as 3D applications when you make a surface two sided.

The confusion about what two-sided lighting does arises because Fusion does not cull backfacing

polygons by default. If you revolve around a one-sided plane in Fusion, you still see it from the backside

(but you are seeing the frontside bits duplicated through to the backside as if it were transparent).

Making the plane two sided effectively adds a second set of normals to the backside of the plane.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Note that this can become rather confusing once you make the surface transparent, as the same rules

still apply and produce a result that is counterintuitive. If you view from the frontside a transparent two-

sided surface illuminated from the backside, it looks unlit.

Material ID

This control is used to set the numeric identifier assigned to this material. The Material ID is an integer

number that is rendered into the MatID auxiliary channel of the rendered image when the Material ID

option is enabled in the Renderer 3D tool.

For more information, see Chapter 85, “3D Compositing Basics,” in the DaVinci Resolve

Reference Manual, or Chapter 25 in the Fusion Reference Manual.