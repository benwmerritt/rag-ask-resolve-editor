---
title: "Textures"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 332
---

# Textures

Texture maps modify the appearance of a material on a per-pixel basis. This is done by connecting

an image or other material to the inputs on the Material nodes in the Node Editor. When a 2D image

is used, the UV mapping coordinates of the geometry are used to fit the image to the geometry, and

when each pixel of the 3D scene is rendered, the material will modify the material input according to

the value of the corresponding pixel in the map.

TIP: UV Mapping is the method used to wrap a 2D image texture onto 3D geometry. Similar

to X and Y coordinates in a frame, U and V are the coordinates for textures on 3D objects.

Texture maps are used to modify various material inputs, such as diffuse color, specular color, specular

exponent, specular intensity, bump map, and others. The most common uses of texture maps is the

diffuse color/opacity component.

The Fast Noise texture

used to control the

roughness of a Cook-

Torrance material

A node that outputs a material is frequently used, instead of an image, to provide other shading

options. Materials passed between nodes are RGBA samples; they contain no other information about

the shading or textures that produced them.

The Texture2D node is

used to translate a texture

in the UV space of the

object, as well as set the

filtering and wrap mode


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Composite Materials

Building complex materials is as easy as connecting the output of a Material node to one of the

Material inputs of another Material or Texture node. When a Material input is supplied just as with

a 2D image, its RGBA values are used per pixel as a texture. This allows for very direct compositing

of shaders.

For instance, if you want to combine an anisotropic highlight with a Blinn material, you can take the

output of the Blinn, including its specular, and use it as the diffuse color of the Ward material. Or, if you

do not want the output of the Blinn to be relit by the Ward material, you can use the Channel Boolean

material to add the Ward material’s anisotropic specular component to the Blinn material with a greater

degree of control.

Combining an anisotropic highlight with a Blinn

material using the Channel Boolean material

Reflections and Refractions

Environment maps can be applied with the Reflect material in the 3D > Material category. This

node can be used to simulate reflections and refractions on an object. Reflections are direct-

bounce light that hits an object, while refractions simulate the distortion of light seen through semi-

translucent surfaces.

The reflections and refractions use an environment mapping technique to produce an approximation

that balances realistic results with greater rendering performance. Environment maps assume an

object’s environment is infinitely distant from the object and rendered into a cubic or spherical texture

surrounding the object.

The Nodes > 3D > Texture > Cube Map and Sphere Map nodes can be used to help create

environment maps, applying special processing and transforms to create the cubic or spherical

coordinates needed.

Sphere map example


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

To produce reflections with real-time interactive feedback at a quality level appropriate for production

environment maps, you make some trade-offs on functionality when compared with slower but

physically accurate raytraced rendering. Environment-mapped reflections and refractions do not

provide self-reflection or any other kind of interaction between different objects. In particular, this

infinite distance assumption means that objects cannot interact with themselves (e.g., the reflections

on the handle of a teapot will not show the body of the teapot). It also means that objects using the

same cube map will not inter-reflect with each other. For example, two neighboring objects would not

reflect each other. A separate cube map must be rendered for each object.

The Reflect node outputs a material that can be applied to an object directly, but the material does

not contain an illumination model. As a result, objects textured directly by the Reflect node will not

respond to lights in the scene. For this reason, the Reflect node is usually combined with the Blinn,

Cook-Torrance, Phong, or Ward nodes.

Reflection

Reflection outputs a material making it possible to apply the reflection or refraction to other materials

either before or after the lighting model with different effects.

A Blinn material connected to a

background material input of the

Reflect This causes the reflection

to be added to the Blinn output

A Reflect is connected to the

Diffuse Color component of the

Blinn, causing the reflection to

be multiplied by the diffuse color

and modulated by the lighting

Refraction

Refraction occurs only where there is transparency in the background material, which is generally

controlled through the Opacity slider and/or the alpha channel of any material or texture used for the

Background Material Texture input. The Reflect node provides the following material inputs:

�Background Material: Defines both the opacity for refraction and the base color for reflection.

�Reflection Color Material: The environment reflection.

�Reflection Intensity Material: A multiplier for the reflection.

�Refraction Tint Material: The environment refraction.

�Bump Map Texture: Normal perturbing map for environment reflection/refraction vectors.

Working with reflection and refraction can be tricky. Here are some techniques to make it easier:

�Typically, use a small amount of reflection, between 0.1 and 0.3 strength. Higher values are used

for surfaces like chrome.

�Bump maps can add detail to the reflections/refractions. Use the same bump map in the

Illumination model shader that you combine with Reflect.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

�When detailed reflections are not required, use a relatively small cube map, such

as 128 x 128 pixels, and blur out the image.

�The alpha of refracted pixels is set to 1 even though the pixels are technically transparent.

Refracted pixels increase their alpha by the reflection intensity.

�If the refraction is not visible even when a texture is connected to the Refraction Tint Material

input, double-check the alpha/opacity values of the background material.

Bump Maps

Bump mapping helps add details and small irregularities to the surface appearance of an object. Bump

mapping modifies the geometry of the object or changes its silhouette.

Split screen of a

sphere—half with bump

map, half without

To apply a bump map, you typically connect an image containing the bump information to the

BumpMap node. The bump map is then connected to the Bump input of a Material node. There are

two ways to create a bump map for a 3D material: a height map and a bump map.

Image connected to a BumpMap connected to a CookTorrance material node

Using a Height Map

A height map is an image where the value of a pixel represents the height. It is possible to select

which color channel is used for bump creation. White means high and black means low; however, it

is not the value of a pixel in the height map that determines the bumpiness, but rather how the value

changes in the neighborhood of a pixel.

Using a Bump Map

A bump map is an image containing normals stored in the RGB channels.

TIP: Normals are generated by 3D modeling and animation software as a way to trick the eye

into seeing smooth surfaces, even though the geometry used to create the models uses only

triangles to build the objects.

Normals are 3 float values (nx, ny, nz) whose components are in the range [–1, +1]. Because you can

store only positive values in Fusion’s integer images, the normals are packed from the range [–1, +1]


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

to the range [0, 1] by multiplying by 0.5 and adding 0.5. You can use Brightness Contrast or a Custom

node to do the unpacking.

If you were to connect a bump map directly to the bump map input of a material, it will result in

incorrect lighting. Fusion prevents you from doing this, however, because Fusion uses a different

coordinate system for doing the lighting calculation. You first must use a BumpMap that expects a

packed bump map or height map and will do the conversion of the bump map to work correctly.

If your bump mapping doesn’t appear correct, here are a few things to look for:

�Make sure you have the nodes connected correctly. The height/bump map should connect into a

BumpMap and then, in turn, should connect into the bump map input on a material.

�Change the precision of the height map to get less banding in the normals. For low frequency

images, float32 may be needed.

�Adjust the Height scale on the BumpMap. This scales the overall effect of the bump map.

�Make sure you set the type to HeightMap or BumpMap to match the image input. Fusion cannot

detect which type of image you have.

�Check to ensure High Quality is on (right-click in the transport controls bar and choose High

Quality from the contextual menu). Some nodes like Text+ produce an anti-aliased version in High

Quality mode that will substantially improve bump map quality.

�If you are using an imported normal map image, make sure it is packed [0–1] in RGB and that it is in

tangent space. The packing can be done in Fusion, but the conversion to tangent space cannot.

Projection Mapping

Projection is a technique for texturing objects using a camera or projector node. This can be useful for

texturing objects with multiple layers, applying a texture across multiple separate objects, projecting

background shots from the camera’s viewpoint, image-based rendering techniques, and much more.

There are three ways to do projection mapping in Fusion.

Using the Projector/Camera Tool to Project Light

When lighting is enabled, a Camera 3D or Projector 3D can act as a light with all the lighting

features. When Camera Projection is enabled or you use a projector, you can choose whether the

projection behaves like a spotlight or an ambient light; however, alpha channels cannot be projected.

Overlapping projections add together like any other light node. An internal clipping plane (at

around 0.01 distance from camera) limits how close the projector or camera can get to the receivers

of the projection.

Camera node used for a projection map


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Project a Texture onto a Catcher Material

If you do not want to work with light sources, you can use the projector or camera as a texture

projector. To work without lighting, a catcher is required in order to receive the texture and apply it to

a material. Only objects using this material will receive the projection. This offers some advantages,

like the projection of alpha channels, and texturing other channels like specular color or roughness.

If the software renderer is used, overlapping projections can be combined in various ways (mean,

median, blend, and so on) via the Catcher node. When using the OpenGL renderer, one catcher

per projector is used, and the results can be combined using another material. Similar to the Light

Projection technique, an internal clipping plane (at around 0.01 distance from camera) limits how close

the projector/camera can get to the projection receivers.

Camera projection used with a Catcher node (example from an older version of Fusion)


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Project Using the UVMap Node

This mode requires a camera and a UVMap3D node downstream of the objects to which the texture

is being projected. In the Inspector, when the UVMap Map mode is set to Camera, it gathers the

information from the camera and creates new UVs for the input objects, which are used for texturing.

Because the UVs are stored in the vertices of the mesh, the object must be tessellated sufficiently.

Textures are assigned to the object like any other texturing technique. The UVs can be locked to the

vertices at a chosen frame using the Ref Time slider. This locking only works as long as vertices are

not created, destroyed, or reordered (e.g., projection locking will not work on particles because they

get created/destroyed, nor will they work on a Cube3D when its subdivision level slider is animated).

TIP: Projected textures can be allowed to slide across an object. If the object moves relative

to the Projector 3D, or alternatively, by grouping the two together with a Merge3D, they can

be moved as one and the texture will remain locked to the object.

In the following section of a much larger composition, an image (the Loader1 node) is projected into 3D

space by mapping it onto five planes (Shape3D nodes renamed ground, LeftWall, RightWall, Building,

and Background), which are positioned as necessary within a Merge3D node to apply reflections onto

a 3D car to be composited into that scene.

Excerpt of a composition that’s projecting an image of a street scene into 3D space

The output of the Merge3D node used to assemble those planes into a scene is then fed to a UV Map

node, which in conjunction with a Camera3D node correctly projects all of these planes into 3D space

so they appear as they would through that camera in the scene. Prior to this UVMap projection, you

can see the planes arranged in space at left, where each plane has the scene texture mapped to it.

At right is the image after the UVMap projection, where you can see that the scene once again looks

“normal,” with the exception of a car-shaped hole introduced to the scene.

Five planes positioning a street scene in 3D space in preparation for UV Projection (left), and the UV Map

node being used to project these planes so they appear as through a camera in the scene (right)


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

However, this is now a 3D scene, ready for a digital car to be placed within it, receiving reflections and

lighting and casting shadows into the scene as if it were there.

The new 3D scene casting reflections and lighting onto a 3D car,

and receiving shadows caused by the car