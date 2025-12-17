---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 370
---

# Inspector

Ward controls

Controls Tab

The Controls tab contains parameters for adjusting the main color, highlight, and lighting properties of

the Ward shader node.

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

Spread U

Spread U controls the falloff of the specular highlight along the U-axis in the UV map of the object.

The smaller the value, the sharper the falloff, and the smoother and glossier the material appears in

this direction. If the Spread U texture is provided, then this value is multiplied by the Alpha value of

the texture.

Spread V

Spread V controls the falloff of the specular highlight along the V-axis in the UV map of the object.

The smaller the value, the sharper the falloff, and the smoother and glossier the material appear in

this direction. If the Spread V texture is provided, then this value is multiplied by the Alpha value of

the texture.

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

When the Alpha Detail slider is set to 0, the Alpha channel of the object is ignored, and the entire

object casts a shadow. If it is set to 1, the Alpha channel determines what portions of the object

cast a shadow.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

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

Fusion does exactly the same thing as 3D applications when you make a surface two sided. The

confusion about what two-sided lighting does arises because Fusion does not cull back-facing

polygons by default. If you revolve around a one-sided plane in Fusion you still see it from the

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

described in detail in the following “The Common Controls” section.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

The Common Controls

Nodes that handle 3D geometry share a number of identical controls in the Inspector. This section

describes controls that are common among 3D Material nodes.

Settings Tab

Common Settings 3D controls

Common Settings tab can be found on most tools in Fusion The following controls are specific settings

for 3D nodes

Hide Incoming Connections

Enabling this checkbox can hide connection lines from incoming nodes, making a node tree appear

cleaner and easier to read. When enabled, fields for each input on a node are displayed. Dragging a

connected node from the node tree into the field hide that incoming connection line as long as the

node is not selected in the node tree. When the node is selected in the node tree, the line reappears.

Comment Tab

The Comment tab contains a single text control that is used to add comments and notes to the tool.

When a note is added to a tool, a small red dot icon appears next to the setting’s tab icon, and a text

bubble appears on the node. To see the note in the Node Editor, hold the mouse pointer over the

node for a moment. The contents of the Comments tab can be animated over time, if required.

Scripting Tab

The Scripting tab is present on every tool in Fusion. It contains several edit boxes used to add scripts

that process when the tool is rendering. For more details on the contents of this tab, please consult the

scripting documentation.


Fusion Page Effects | Chapter 91 3D Material Nodes

FUSION

Chapter 92

3D Texture Nodes

This chapter details the 3D Texture nodes available when creating 3D composites

in Fusion. The abbreviations next to each node name can be used in the

Select Tool dialog when searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Bump Map [3Bu]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2034

Catcher [3Ca]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2037

CubeMap [3Cu]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2039

Falloff [3Fa]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2042

Fast Noise Texture [3FN]���������������������������������������������������������������������������������������������������������������������������������������������������������������� 2044

Gradient 3D [3Gd]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2047

Sphere Map [3SpM]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2050

Texture 2D [3Tx]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2052

Texture Transform [3TT]����������������������������������������������������������������������������������������������������������������������������������������������������������������� 2054

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2057


Fusion Page Effects | Chapter 92 3D Texture Nodes

FUSION