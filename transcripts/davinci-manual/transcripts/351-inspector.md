---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 351
---

# Inspector

Point Cloud 3D controls

Controls Tab

The Controls tab is where you can import the point cloud from a file and controls its appearance in

the viewer.

Style

The Style menu allows you to display the point cloud as cross hairs or points in the viewer.

Lock X/Y/Z

Deselect this checkbox to provide individual control over the size of the X, Y, and Z arms of the points

in the cloud.

Size X/Y/Z

These sliders can be used to increase the size of the onscreen crosshairs used to represent

each point.

Density

This slider defines the probability of displaying a specific point. If the value is 1, then all points are

displayed. A value of 0.2 shows only every fifth point.

Color

Use the standard Color control to set the color of onscreen crosshair controls.

Import Point Cloud

The Import Point Cloud button displays a dialog to import a point cloud from another application.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Supported file types are:

Alias's Maya

.ma

3DS Max ASCII Scene Export

.ase

NewTek's LightWave

.lws

Softimage XSI's

.xsi.

Make Renderable

Determines whether the point cloud is visible in the OpenGL viewer and in final renderings made

by the OpenGL renderer. The software renderer does not currently support rendering of visible

crosshairs for this node.

Unseen by Camera

This checkbox control appears when the Make Renderable option is selected. If the Unseen by

Cameras checkbox is selected, the point cloud is visible in the viewers but not rendered into the

output image by the Renderer 3D node.

Common Controls

Transform and Settings Tabs

The remaining Transform and Settings tabs are common to many 3D nodes. Their descriptions can be

found in “The Common Controls” section at the end of this chapter.

Onscreen Contextual Menu

Frequently, one or more of the points in an imported point cloud is manually assigned to track the

position of a specific feature. These points usually have names that distinguish them from the rest of

the points in the cloud. To see the current name for a point, hover the mouse pointer directly over a

point, and after a moment a small tooltip appears with the name of the point.

When the Point Cloud 3D node is selected, a submenu is added to the viewer’s contextual menu with

several options that make it simple to locate, rename, and separate these points from the rest of the

point cloud.

The contextual menu contains the following options:

Find: Selecting this option from the viewer contextual menu opens a dialog to search for and

select a point by name. Each point that matches the pattern is selected.

Rename: Rename any point by selecting Rename from the contextual menu. Type the new

name into the dialog that appears and press Return. The point now has that name, with a

four-digit number added to the end. For example, the Name window is window0000, and

multiple points would be window0000, window0001, and so on. Names must be valid Fusion

identifiers (i.e., no spaces allowed, and the name cannot start with a number).

Delete: Selecting this option deletes the currently selected points.

Publish: Normally, the exact position of a point in the cloud is not exposed. To expose the

position, select the points, and then select the Publish option from this contextual menu.

This adds a coordinate control to the control panel for each published point that displays the

point’s current location.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

The Point Cloud 3D contextual menu options

Additional Toolbar and Shortcuts

Action

Shortcuts

Delete Selected Points

Del

Select All

Shift+A

Find Points

Shift+F

Rename Selected Points

F2

Create New Point

Shift+C

Toggle Names on None/Selected/Published/All Points

Shift+N

Toggle Locations on None/Selected/Published/All Points

Shift+L

Publish Selected Points

Shift+P

Unpublish Selected Points

Shift+U

Create a Shape at Selected Points

Shift+S

Create and Fit an ImagePlane to Selected Points

Shift+I

Create a Locator at Selected Points

Shift+O


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Projector 3D [3Pj]

The Projector 3D node

Projector 3D Node Introduction

The Projector 3D node is used to project an image upon 3D geometry. This can be useful in many

ways: texturing objects with multiple layers, applying a texture across multiple separate objects,

projecting background shots from the camera’s viewpoint, image-based rendering techniques,

and more. The Projector node is just one of several nodes capable of projecting images and textures.

Each method has advantages and disadvantages.

For more information, see Chapter 85, “3D Compositing Basics,” in the DaVinci Resolve

Reference Manual, or Chapter 25 in the Fusion Reference Manual.

Projected textures can be allowed to “slide“ across the object if the object moves relative to the

Projector 3D, or, alternatively, by grouping the two with a Merge 3D so they can be moved as one and

the texture remains locked to the object.

The Projector 3D node’s capabilities and restrictions are best understood if the Projector is considered

to be a variant on the SpotLight node. The fact that the Projector 3D node is actually a light has several

important consequences when used in Light or Ambient Light projection mode:

�Lighting must be turned on for the results of the projection to be visible.

�The light emitted from the projector is treated as diffuse/specular light. This means that it is

affected by the surface normals and can cause specular highlights. If this is undesirable, set the

Projector 3D to project into the Ambient Light channel.

�Enabling Shadows causes Projector 3D to cast shadows.

�Just as with other lights, the light emitted by a Projector 3D only affects objects that feed into the

first Merge 3D that is downstream of the Projector 3D node in the node tree.

�Enabling Merge 3D’s Pass Through Lights checkbox allows the projection to light objects

further downstream.

�The light emitted by a Projector 3D is controlled by the Lighting options settings on objects and

the Receives Lighting options on materials.

�Alpha values in the projected image do not clip geometry in Light or Ambient Light mode.

Use Texture mode instead.

�If two projections overlap, their light contributions are added.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

To project re-lightable textures or textures for non-diffuse color channels (like Specular

Intensity or Bump), use the Texture projection mode instead:

•	 Projections in Texture mode only strike objects that use the output of the Catcher node for

all or part of the material applied to that object.

•	 Texture mode projections clip the geometry according to the Alpha channel of the

projected image.

See the section for the Catcher node for additional details.

Camera Projection vs. Projection 3D Node

The Camera 3D node also provides a projection feature, and should be used when the projection

is meant to match a camera, as this node has more control over aperture, film back, and clip planes.

The Projector 3D node was designed to be used as a custom light in 3D scenes for layering and

texturing. The projector provides better control over light intensity, color, decay, and shadows.

Inputs

The Projector 3D has two inputs: one for the scene you are projecting on to and another for the

projected image.

SceneInput: The orange scene input accepts a 3D scene. If a scene is connected to this input, then

transformations applied to the spotlight also affect the rest of the scene.

ProjectiveImage: The white input expects a 2D image to be used for the projection. This connection is

required.

Basic Node Setup

As an example, the Projector 3D node below is used to project a texture (MediaIn2) onto 3D primitives

as a way to create a simple 3D set. All the set elements are connected into a Merge 3D, which outputs

the projected set into a larger scene with camera, lights, and other elements. As an alternative, the

Projector 3D node could be inserted between the two Merge 3D nodes; however, the transform

controls in the Projector 3D node would then affect the entire scene.

Projector 3D texturing groups of shapes to construct a set


Fusion Page Effects | Chapter 89 3D Nodes

FUSION