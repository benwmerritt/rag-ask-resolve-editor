---
title: "Transforming Cameras and Lights Using the Viewers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 328
---

# Transforming Cameras and Lights Using the Viewers

When the viewer is set to look through a 3D object in the scene, such as a camera or spotlight, the

usual controls for panning and rotating the viewer will now directly affect the position of the camera or

spotlight you’re viewing through. Here’s an example.

To adjust a camera’s position when looking through it in a viewer:


Right-click the viewpoint label, and choose a camera from the contextual menu. (Optional) If you’re

in dual-viewer mode, you can load the camera you’ve selected in one viewer into the other viewer

to see its position as you work.


Move the pointer into the viewer that’s displaying the camera’s viewpoint.


Hold the middle and left mouse buttons down and drag to zoom the viewer, or middle-click-

drag to pan the viewer, or option-middle-click-drag to rotate the viewer, all while also moving

the camera.

When a viewer is set to display the view of a camera or light, panning, zooming, or rotating the viewer

(seen at right) actually transforms the camera or light you’re viewing through (seen at left)

It is even possible to view the scene from the perspective of a Merge3D or Transform3D node by

selecting the object from the Camera > Others menu. The same transform techniques will then

move the position of the object. This can be helpful when you are trying to orient an object in a

certain direction.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Transparency Sorting

While generally the order of geometry in a 3D scene is determined by the Z-position of each object,

sorting every face of every object in a large scene can take an enormous amount of time. To provide

the best possible performance, a Fast Sorting mode is used in the OpenGL renderer and viewers.

This is set by right-clicking in the viewer and choosing Transparency > Z-buffer. While this approach

is much faster than a full sort, when objects in the scene are partially transparent it can also produce

incorrect results.

The Sorted (Accurate) mode can be used to perform a more accurate sort at the expense of performance.

This mode is selected from the Transparency menu of the viewer’s contextual menu. The Renderer3D

also presents a Transparency menu when the Renderer Type is set to OpenGL. Sorted mode does not

support shadows in OpenGL. The software renderer always uses the Sorted (Accurate) method.

Transparency Sorting in the viewer contextual menu

The basic rule is when a scene contains overlapping transparency, use the Full/Quick Sort modes,

and otherwise use the Z-buffer (Fast). If the Full Sort method is too slow, try switching back to

Z-buffer (Fast).

Material Viewer

When you view a node that comes from the 3D > Material category of nodes in the Effects Library, the

viewer automatically switches to display a Material Viewer. This Material Viewer allows you to preview

the material applied to a lit 3D sphere rendered with OpenGL by default.

The Material Viewer mode of the viewer


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

The type of geometry, the renderer, and the state of the lighting can all be set by right-clicking the

viewer and choosing options from the contextual menu. Each viewer supports A and B buffers to assist

with comparing multiple materials.

Methods of working with the Material Viewer:

�You can change the shape of the previewed geometry by right-clicking the viewer and choosing

an option from the Shape submenu of the contextual menu. The geometry that the material is

applied to is locked to the center of the viewer and scaled to fit. It is not possible to pan or scale

the Material Viewer.

�The Material Viewer can be rotated to provide a different angle on the material by holding Option

while pressing the middle mouse button and dragging to the left and right.

�You can adjust the position of the light used to preview the material by dragging with the middle

mouse button. Or, you can right-click the viewer and choose an option from the Lighting > Light

Position submenu of the contextual menu.

�You can also toggle lighting off and on by right-clicking the viewer and choosing Lighting > Enable

Lighting from the contextual menu.

�You can choose the renderer used to preview the material by right-clicking the viewer and

choosing an option from the Renderer submenu of the contextual menu.

Transformations

Merge3D, 3D Objects, and Transform3D all have Transform parameters that are collected together into

a Transform tab in the Inspector. The parameters found in this tab affect how the object is positioned,

rotated, and scaled within the scene.

The Transform tab of a Merge3D node

The Translation parameters are used to position the object in local space, the Rotation parameters

affect the object’s rotation around its own center, and the Scale slider(s) affect its size (depending

on whether or not they’re locked together). The same adjustments can be made in the viewer using

onscreen controls.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Onscreen Transform Controls

When an object is selected, it displays onscreen Transform controls in the viewers that allow you to

adjust the object’s position, rotation, and scale. Buttons in the Transform toolbar allow you to switch

modes, or you can use the keyboard shortcuts.

To switch Transform modes, use the following keyboard shortcuts:

�Press Q for Position

�Press W for Rotation

�Press E for Scaling

The Position, Rotation, and Scale

modes in the Transform toolbar

Using Onscreen Transform Controls

In all three modes, red indicates the object’s local X-axis, green the Y-axis, and blue the Z-axis,

respectively (just remember RGB = XYZ). You can drag directly on the red, green, or blue portion of

any onscreen control to constrain the transform to that axis, or if you drag the center of the onscreen

control, you can apply a transform without constraints. Holding Option and dragging in the viewer

allows you to freely translate in all three axes without clicking on a specific control.

From left to right, the Position, Rotation, and Scale onscreen Transform controls

If the Scale’s Lock XYZ checkbox is enabled in the Inspector, only the overall scale of the object is

adjusted by dragging the red or center onscreen control, while the green and blue portions of the

onscreen control have no effect. If you unlock the parameters, you are able to scale an object along

individual axes separately to squish or stretch the object.

Selecting Objects

With the onscreen controls visible in the viewer, you can select any object by clicking on its center

control. Alternatively, you can also select any 3D object by clicking its node in the Node Editor.


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

Pivot

In 3D scenes, objects rotate and scale around an axis called a pivot. By default, this pivot goes

through the object’s center. If you want to move the pivot so it is offset from the center of the object,

you can use the X, Y, and Z Pivot parameters in the Inspector.

Target

Targets are used to help orient a 3D object to a specific point in the scene. No matter where the object

moves, it will rotate in the local coordinate system so that it always faces its target, which you can

position and animate.

To enable a target for a 3D object:


Select that object’s node.


Open the object’s Transform panel in the Inspector.


Turn on the Use Target checkbox.

Turning on the Use Target checkbox of a 3D object


Use the X/Y/Z Target Position controls in the Inspector or the Target onscreen control in the

viewer to position the target and in turn position the object it’s attached to.

In the viewer, a line is drawn between the target and the center of the 3D object it’s attached to, to

show the relationship between these two sets of controls. Whenever you move the target, the object

is automatically transformed to face its new position.

A torus facing its onscreen Target controls


Fusion Fundamentals | Chapter 85 3D Compositing Basics

FUSION

For example, if a spotlight is required in the scene to point at an image plane, enable the spotlight’s

target in the Transform tab and connect the target’s XYZ position to the image plane’s XYZ position.

Now, no matter where the spotlight is moved, it will rotate to face the image plane.

A light made to face the wall using its enabled target control