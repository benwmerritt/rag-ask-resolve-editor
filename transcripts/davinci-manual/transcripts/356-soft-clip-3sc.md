---
title: "Soft Clip [3SC]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 356
---

# Soft Clip [3SC]

The Soft Clip node

Soft Clip Node Introduction

The Soft Clip node is used to fade out geometry and particles that get close to the camera. This helps

avoid the visible “popping off” that affects many particle systems and 3D flythroughs.

This node is very similar to the Fog 3D node, in that it is dependent on the geometry’s distance from

the camera.

Inputs

The Soft Clip includes only a single input for a 3D scene that includes a camera connected to it.

SceneInput: The orange scene input is a required connection. It accepts a 3D scene input that

includes a Camera 3D node.

Basic Node Setup

The Soft Clip node is usually placed just before the Renderer 3D node to ensure that downstream

adjustments to lighting and textures do not affect the result. It can be placed in any part of the 3D

portion of the node tree if the soft clipping effect is only required for a portion of the scene.

Soft Clip placed between a Merge 3D and a Renderer 3D node


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Inspector

Soft Clip controls

Controls Tab

The Controls tab determines how an object transitions between opaque and transparent as it moves

closer to the camera.

Enable

This checkbox can be used to enable or disable the node. This is not the same as the red switch in the

upper-left corner of the Inspector. The red switch disables the tool altogether and passes the image

on without any modification. The Enable checkbox is limited to the effect of the tool. Other parts, like

scripts in the Settings tab, still process as normal.

Smooth Transition

By default, an object coming closer and closer to the camera slowly fades out with a linear

progression. With the Smooth Transition checkbox enabled, the transition changes to a nonlinear

curve, arguably a more natural-looking transition.

Radial

By default, the soft clipping is done based on the perpendicular distance to a plane (parallel with the

near plane) passing through the eye point. When the Radial option is checked, the Radial distance to

the eye point is used instead of the Perpendicular distance. The problem with Perpendicular distance

soft clipping is that when you move the camera about, as objects on the left or right side of the frustum

move into the center, they become less clipped, although they remain the same distance from the eye.

Radial soft clip fixes this. Sometimes Radial soft clipping is not desirable.

For example, if you apply soft clip to an object that is close to the camera, like an image plane, the

center of the image plane could be unclipped while the edges could be fully clipped because they are

farther from the eye point.

Show In Display Views

Normally, the effect is only visible when the scene is viewed using a Camera node. When enabled, the

soft clip becomes visible in the scene from all points of view.

Transparent/Opaque Distance

Defines the range of the soft clip. The objects begin to fade in from an opacity of 0 at the Transparent

distance and are fully visible at the Opaque distance. All units are expressed as distance from the

camera along the Z-axis.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Spherical Camera [3SC]

The Spherical Camera node

Spherical Camera Node Introduction

The Spherical Camera allows the 3D Renderer node to output an image covering all viewing angles,

laid out in several different formats. This image may be used, for example, as a skybox texture or

reflection map or viewed in a VR headset. The Image Width setting in the 3D Renderer sets the size of

each square cube face, so the resulting image may be a multiple of this size horizontally and vertically.

Inputs

The Spherical camera node has two inputs.

Image: This orange image input requires an image in a spherical layout, which can be any of LatLong

(2:1 equirectangular), VR180, Horizontal/Vertical Cross, or Horizontal/Vertical Strip.

Stereo Input: The green input for a right stereo camera if you are working in stereo VR.

Neither input is required.

Basic Node Setup

In many ways, the Spherical Camera is set up identically to the regular Camera 3D node. The output

of the camera connects into a Merge 3D. Typically, the Merge 3D has an image from a LatLong or H

Cross/V Cross formatted image either directly or through a Panomap node. The image is wrapped

around a sphere, and the camera is placed inside the sphere.

Spherical Camera placed inside a sphere


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Inspector

Spherical Camera controls

Controls Tab

Layout

�VCross and HCross: VCross and HCross are the six square faces of a cube laid out in a cross,

vertical or horizontal, with the forward view in the center of the cross, in a 3:4 or 4:3 image.

�VStrip and HStrip: VStrip and HStrip are the six square faces of a cube laid vertically or

horizontally in a line, ordered as Left, Right, Up, Down, Back, Front (+X, -X, +Y, -Y, +Z, -Z),

in a 1:6 or 6:1 image.

�LatLong: LatLong is a single 2:1 image in equirectangular mapping.

�VR 180 is a 1:1 180 degree stereoscopic image.

Near/Far Clip

The clipping plane is used to limit what geometry in a scene is rendered based on the object’s

distance from the camera’s focal point. This is useful for ensuring that objects that are extremely close

to the camera are not rendered and for optimizing a render to exclude objects that are too far away to

be useful in the final rendering.

The default perspective camera ignores this setting unless the Adaptively Adjust Near/Far Clip

checkbox control below is disabled.

The values are expressed in units, so a far clipping plane of 20 means that any objects more than

20 units from the camera are invisible to the camera. A near clipping plane of 0.1 means that any

objects closer than 0.1 units are also invisible.

Adaptively Adjust Near/Far Clip

When selected, the Renderer automatically adjusts the camera’s near/far clipping plane to match the

extents of the scene. This setting overrides the values of the Near and Far clip range control described

above. This option is not available for orthographic cameras.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Viewing Volume Size

The Viewing Volume Size control appears only when the Projection Type is set to Orthographic.

It determines the size of the box that makes up the camera’s field of view. The Z distance of an

orthographic camera from the objects it sees does not affect the scale of those objects, only the

viewing size does.

NOTE: A smaller range between the near and far clipping plane allows greater accuracy

in all depth calculations. If a scene begins to render strange artifacts on distant objects,

try increasing the distance for the near clip plane. Use the vertical aperture size to get the

vertical angle of view and the horizontal aperture size to get the horizontal angle of view.

Plane of Focus (for Depth of Field)

This value is used by the OpenGL renderer to calculate depth of field. It defines the distance to a

virtual target in front of the camera.

Stereo Method

This control allows you to adjust your stereoscopic method to your preferred working model.

Toe In

Both cameras point at a single focal point. Though the result is stereoscopic, the vertical parallax

introduced by this method can cause discomfort by the audience.

Off Axis

Often regarded as the correct way to create stereo pairs, this is the default method in Fusion. Off Axis

introduces no vertical parallax, thus creating less stressful stereo images.

Parallel

The cameras are shifted parallel to each other. Since this is a purely parallel shift, there is no Convergence

Distance control. Parallel introduces no vertical parallax, thus creating less stressful stereo images.

Eye Separation

Defines the distance between both stereo cameras. If the Eye Separation is set to a value larger

than 0, controls for each camera are shown in the viewer when this node is selected. There is no

Convergence Distance control in Parallel mode.

Convergence Distance

This control sets the stereoscopic convergence distance, defined as a point located along the Z-axis

of the camera that determines where both left and right eye cameras converge.

Control Visibility

Allows you to selectively activate the onscreen controls that are displayed along with the camera.

�Frustum: Displays the actual viewing cone of the camera.

�View Vector: Displays a white line inside the viewing cone, which can be used to determine the

shift when in Parallel mode.

�Near Clip: The Near clipping plane. This plane can be subdivided for better visibility.

�Far Clip: The Far clipping plane. This plane can be subdivided for better visibility.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

�Plane of Focus: The camera focal point according to the Plane of Focus slider explained above.

This plane can be subdivided for better visibility.

�Convergence Distance: The point of convergence when using Stereo mode. This plane can be

subdivided for better visibility.

Common Controls

Settings Tab

The Settings tab in the Inspector is duplicated in other 3D nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.