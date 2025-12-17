---
title: "Image Plane 3D [3Im]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 349
---

# Image Plane 3D [3Im]

The Image Plane 3D node

Image Plane 3D Node Introduction

The Image Plane node produces 2D planar geometry in 3D space. The node is most commonly used

to represent 2D images on “cards” in the 3D space. The aspect of the image plane is determined by

the aspect of the image connected to the material input. If you do not want the aspect ratio of the

image to modify the “card” geometry, then use a Shape 3D node instead.

Inputs

Of the two inputs on this node, the material input is the primary connection you use to add an image to

the planar geometry created in this node.

SceneInput: This orange input expects a 3D scene. As this node creates flat, planar geometry, this

input is not required.

MaterialInput: The green-colored material input accepts either a 2D image or a 3D material. It

provides the texture and aspect ratio for the rectangle based on the connected source such as a

Loader node in Fusion Studio or a MediaIn node in DaVinci Resolve. The 2D image is used as a diffuse

texture map for the basic material tab in the Inspector. If a 3D material is connected, then the basic

material tab is disabled.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Basic Node Setup

The Image Plane 3D node is primarily used to bring a video clip into a 3D composite. The MediaIn or

Loader node is connected to the Image Plane 3D node, and the Image Plane 3D is then connected

to a Merge 3D node. Viewing the Merge 3D node will show all the Image Plane 3D nodes and other

elements connected to it.

Multiple Image Plane 3D nodes connected to a Merge 3D

Inspector

Image Plane 3D controls


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Controls Tab

Most of the Controls tab is taken up by common controls. The Image Plane specific controls at the top

of the Inspector allow minor adjustments.

Lock Width/Height

When checked, the subdivision of the plane is applied evenly in X and Y. When unchecked, there are

two sliders for individual control of the subdivisions in X and Y. This defaults to on.

Subdivision Level

Use the Subdivision Level slider to set the number of subdivisions used when creating the image

plane. If the Open GL viewer and renderer are set to Vertex lighting, the more subdivisions in the

mesh, the more vertices are available to represent the lighting. So, high subdivisions can be useful

when working interactively with lights.

Wireframe

Enabling this checkbox causes the mesh to render only the wireframe for the object when using the

OpenGL renderer.

Common Controls

Controls, Materials, Transform, and Settings Tabs

The remaining controls for Visibility, Lighting, Matte, Blend Mode, Normals/Tangents, and Object

ID are common to many 3D nodes. The same is true of the Materials, Transform, and Settings tabs.

Their descriptions can be found in “The Common Controls” section at the end of this chapter.

Locator 3D [3Lo]

The Locator 3D node

Locator 3D Node Introduction

The Locator 3D node’s purpose is to transform a point in 3D space to 2D coordinates that other nodes

can use as part of expressions or modifiers.

When the Locator is provided with a camera and the dimensions of the output image, it transforms

the coordinates of a 3D control into 2D screen space. The 2D position is exposed as a numeric

output that can be connected to/from other nodes. For example, to connect the center of an ellipse

to the 2D position of the Locator, right-click on the Mask center control and select Connect To >

Locator 3D > Position.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Inputs

Two inputs accept 3D scenes as sources. The orange scene input is required, while the green Target

input is optional.

SceneInput: The required orange scene input accepts the output of a 3D scene. This scene should

contain the object or point in 3D space that you want to covert to 2D coordinates.

Target: The optional green target input accepts the output of a 3D scene. When provided, the

transform center of the scene is used to set the position of the Locator. The transformation controls for

the Locator become offsets from this position.

Basic Node Setup

The scene provided to the Locator’s input must contain the camera through which the coordinates are

projected. So, the best practice is to place the Locator after the Merge that introduces the camera to

the scene.

If an object is connected to the Locator node’s target input, the Locator is positioned at the object’s

center, and the Transformation tab’s translation XYZ sliders function in the object’s local coordinate

space instead of global scene space. This is useful for tracking an object’s position despite any

additional transformations applied further downstream.

Locator 3D connected after a Merge 3D with the SpotLight as the target

Inspector

Locator 3D controls


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Controls Tab

Most of the controls for the locator 3D are cosmetic, dealing with how the locator appears and whether

it is rendered in the final output. However, the Camera Settings are critical to getting the results you’re

looking for.

Size

The Size slider is used to set the size of the Locator’s onscreen crosshair.

Color

A basic Color control is used to set the color of the Locator’s onscreen crosshair.

Matte

Enabling the Is Matte option applies a special texture to this object, causing this object to not only

become invisible to the camera, but also making everything that appears directly behind the camera

invisible as well. This option overrides all textures.

�Is Matte: When activated, objects whose pixels fall behind the matte object’s

pixels in Z do not get rendered.

�Opaque Alpha: Sets the Alpha value of the matte object to 1. This checkbox is visible only when

the Is Matte option is enabled.

�Infinite Z: Sets the value in the Z-channel to infinity. This checkbox is visible only when the Is

Matte option is enabled.

For more information, see Chapter 85, “3D Compositing Basics,” in the DaVinci Resolve

Reference Manual, or Chapter 25 in the Fusion Reference Manual.

Sub ID

The Sub ID slider can be used to select an individual subelement of certain geometry, such as an

individual character produced by a Text 3D node or a specific copy created by a Duplicate 3D node.

Make Renderable

Defines whether the Locator is rendered as a visible object by the OpenGL renderer. The software

renderer is not currently capable of rendering lines and hence ignores this option.

Unseen by Camera

This checkbox control appears when the Make Renderable option is selected. If the Unseen by

Camera checkbox is selected, the Locator is visible in the viewers but not rendered into the output

image by the Renderer 3D node.

Camera

This drop-down control is used to select the Camera in the scene that defines the screen space used

for 3D to 2D coordinate transformation.

Use Frame Format Settings

Select this checkbox to override the width, height, and pixel aspect controls, and force them to use the

values defined in the composition’s Frame Format preferences instead.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Width, Height, and Pixel Aspect

In order for the Locator to generate a correct 2D transformation, it must know the dimensions and

aspect of the image. These controls should be set to the same dimensions as the image produced by

a renderer associated with the camera specified above. Right-clicking on these controls displays a

contextual menu containing the frame formats configured in the composition’s preferences.

Common Controls

Transform and Settings tabs

The remaining Transform and Settings tabs are common to many 3D nodes. Their descriptions can be

found in “The Common Controls” section at the end of this chapter.