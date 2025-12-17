---
title: "Inputs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 363
---

# Inputs

This node includes an optional orange input for a 3D scene or 3D geometry, and a white Dome

Texture input for connecting an image.

SceneInput: The orange input is an optional input that accepts a 3D scene. If a scene is provided, the

Transform controls in this node apply to the entire scene provided.

DomeTexture: The white input connects to an SDR or HDR image.

Basic Node Setup

The Dome Light node is designed to be part of a larger 3D scene. You connect the light directly into

a Merge 3D. Separating lights into different Merge 3D nodes allows you to control which lights affect

which objects.

Dome Light node structure

Inspector

The Dome Light controls

Controls Tab

The Controls tab is used to set the color and brightness of the uDome light. The position, direction,

and scale of the light source is controlled in the Transform tab.

Color

Use this standard Color control to set the color of the light.

Intensity

Use this slider to set the intensity of the light. A value of 0.2 indicates 20% percent light.


Fusion Page Effects | Chapter 90 3D Light Nodes

FUSION

Point Light [3PL]

The Point Light node

Point Light Node Introduction

A point light is a light source with a clear position in space that emits light in all directions. A light bulb

is a good example of a point light.

This light shows an onscreen control, although only the position and distance of the control affect the

light. Since the light is a 360-degree source, rotation has no meaning. Additionally, a point light may

fall off with distance, unlike an ambient or directional light.

Similar to a Camera 3D, you connect lights into a Merge 3D and view them in the scene by viewing the

Merge 3D node. Selecting a light node and loading it into the viewer does not show anything.

Inputs

The Point Light node includes a single optional orange input for a 3D scene or 3D geometry.

SceneInput: The orange input is an optional input that accepts a 3D scene. If a scene is provided, the

Transform controls in this node apply to the entire scene provided.

Basic Node Setup

The Point Light node is designed to be part of a larger 3D scene. You connect the light directly into

a Merge 3D. Separating lights into different Merge 3D nodes allows you to control which lights affect

which objects.

Point Light node structure


Fusion Page Effects | Chapter 90 3D Light Nodes

FUSION

Inspector

Point Light controls

Controls Tab

The Controls tab is used to set the color and brightness of the point light. The position and distance of

the light source are controlled in the Transform tab.

Enabled

When the Enabled checkbox is turned on, the point light affects the scene. When the checkbox is

turned off the light is turned off. This checkbox performs the same function as the red switch to the left

of the node’s name in the Inspector.

Color

Use this standard Color control to set the color of the light.

Intensity

Use this slider to set the Intensity of the point light. A value of 0.2 indicates 20% percent light.

Decay Type

A point light defaults to No Decay, meaning that its light has equal intensity at all points in the scene.

To cause the intensity to fall off with distance, set the Decay Type to either Linear or Quadratic modes.

Shadows

This section provides several controls used to define the shadow map used when this spotlight

creates shadows.

For more information, see Chapter 85, “3D Compositing Basics,” in the DaVinci Reference

Manual or Chapter 23 in the Fusion Reference Manual.

NOTE: The Point light requires Hardware Renderer set as the Rendering Type in the

Renderer3D node for shadows to be seen in the 3D viewer.


Fusion Page Effects | Chapter 90 3D Light Nodes

FUSION

Enable Shadows

The Enable Shadows checkbox should be selected if the light is to produce shadows. This defaults

to selected.

Shadow Color

Use this standard Color control to set the color of the shadow. This defaults to black (0, 0, 0).

Density

The shadow density determines the transparency of the shadow. A density of 1.0 produces a

completely opaque shadow, whereas lower values make the shadow more transparent.

Shadow Map Size

The Shadow Map Size control determines the size of the bitmap used to create the shadow map.

Larger values produce more detailed shadow maps at the expense of memory and performance.

Shadow Map Proxy

Shadow Map Proxy determines the size of the shadow map used when the Proxy or Auto Proxy

modes are enabled. A value of 0.5 would produce a shadow map at half the resolution defined in the

Shadow Map Size.

Multiplicative/Additive Bias

Shadows are essentially textures applied to objects in the scene, so there is occasionally Z-fighting,

where the portions of the object that should be receiving the shadows render over the top of the

shadow. Biasing works by adding a small depth offset to move the shadow away from the surface it is

shadowing, eliminating the Z-fighting. Too little bias and the objects can self-shadow themselves. Too

much bias and the shadow can become separated from the surface. Adjust the Multiplicative Bias first,

and then fine tune the result using the Additive Bias control.

For more information, see the Multiplicative and Additive Bias section of Chapter 85, “3D

Compositing Basics,” in the DaVinci Resolve Reference Manual, or Chapter 25 in the Fusion

Reference Manual.

Force All Materials Non-Transmissive

Normally, an RGBAZ shadow map is used when rendering shadows. By enabling this option, you

are forcing the renderer to use a Z-only shadow map. This can lead to significantly faster shadow

rendering while using a fifth as much memory. The disadvantage is that you can no longer cast

“stained glass”-like shadows.

Shadow Map Sampling

Sets the quality for sampling of the shadow map.

Softness

Soft edges in shadows are produced by filtering the shadow map when it is sampled. Fusion provides

two separate filtering methods for rendering shadows, which produce different effects.

�Constant: Shadows edges have a constant softness. A filter with a constant width is used when

sampling the shadow map. Adjusting the Constant Softness slider controls the size of the filter.

Note that the larger you make the filter, the longer it takes to render the shadows.

�Variable: The shadow edge softness grows the farther the shadow receiver is positioned from the

shadow caster. The variable softness is achieved by changing the size of the filter based on the

distance between the receiver and caster. When this option is selected, the Softness Falloff, Min

Softness, and Max Softness sliders appear.


Fusion Page Effects | Chapter 90 3D Light Nodes

FUSION

Constant Softness

If the Softness is set to Constant, then this slider appears. It can be used to set the overall softness of

the shadow.

Softness Falloff

The Softness Falloff slider appears when the Softness is set to variable. This slider controls how fast

the softness of shadow edges grows with distance. More precisely, it controls how fast the shadow

map filter size grows based upon the distance between the shadow caster and receiver. Its effect is

mediated by the values of the Min and Max Softness sliders.

Min Softness

The Min Softness slider appears when the Softness is set to Variable. This slider controls the Minimum

Softness of the shadow. The closer the shadow is to the object casting the shadow, the sharper it is,

up to the limit set by this slider.

Max Softness

The Max Softness slider appears when the Softness is set to Variable. This slider controls the

Maximum Softness of the shadow. The farther the shadow is from the object casting the shadow, the

softer it is, up to the limit set by this slider.

Common Controls

Transform and Settings Tabs

The options presented in the Transform and Settings tabs are commonly found in other lighting nodes.

For more detail on the controls found in these tabs, see “The Common Controls” section at the end of

this chapter.

Spot Light [3SL]

The Spot Light node

Spot Light Node Introduction

A spotlight is a light that comes from a specific point and that has a clearly defined cone, with falloff of

the light to the edges. Experienced stage and theatre lighting technicians may recognize the spotlight

as being very similar to practical lights used in live productions. This is the only type of light capable of

casting shadows.

Similar to a Camera 3D, you connect lights into a Merge 3D and view them in the scene by viewing the

Merge 3D node. Selecting a light node and loading it into the viewer does not show anything.


Fusion Page Effects | Chapter 90 3D Light Nodes

FUSION