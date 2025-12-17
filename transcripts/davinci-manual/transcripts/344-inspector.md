---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 344
---

# Inspector

Bender 3D controls

Controls Tab

The first tab in the Inspector is the Controls tab. It includes all the controls for the Bender 3D node.

Bender Type

The Bender Type menu is used to select the type of deformation to apply to the geometry. There are

four modes available: Bend, Taper, Twist, and Shear.

Amount

Adjusting the Amount slider changes the strength of the deformation.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Axis

The Axis control determines the axis along which the deformation is applied. It has a different

meaning depending on the type of deformation. For example, when bending, this selects the elbow in

conjunction with the Angle control. In other cases, the deform is applied around the specified axis.

Angle

The Angle thumbwheel control determines what direction about the axis a bend or shear is applied.

It is not visible for taper or twist deformations.

Range

The Range control can be used to limit the effect of a deformation to a small portion of the geometry.

The Range control is not available when the Bender Type is set to Shear.

Group Objects

If the input of the Bender 3D node contains multiple 3D objects, either through a Merge 3D or strung

together, the Group Objects checkbox treats all the objects in the input scene as a single object, and the

common center is used to deform the objects, instead of deforming each component object individually.

Common Controls

Settings

The Settings tab in the Inspector is common to all 3D nodes. This common tab is described in detail at

the end of this chapter in “The Common Controls” section.

Camera 3D [3Cm]

The Camera 3D node

Camera 3D Node Introduction

The Camera 3D node generates a virtual camera for viewing the 3D environment. It closely emulates

the settings used in real cameras to make matching live-action or 3D-rendered elements as seamless

as possible. Adding any cameras to a 3D composite allows you to frame the elements in a composite

how you want and animate the camera during a scene to create moving camera shots.

Camera Projection

The Camera 3D node can also be used to perform Camera Projection by projecting a 2D image

through the camera into 3D space. Projecting a 2D image can be done as a simple Image Plane

aligned with the camera, or as an actual projection, similar to the behavior of the Projector 3D node,

with the added advantage of being aligned precisely with the camera. The Image Plane, Projection,

and Materials tabs do not appear until you connect a 2D image to the magenta image input on the

Camera 3D node in the Node Editor.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Stereoscopic

The Camera node has built-in stereoscopic features. They offer control over eye separation and

convergence distance. The camera for the right eye can be replaced using a separate camera node

connected to the green left/right stereo camera input. Additionally, the plane of focus control for depth

of field rendering is also available here.

If you add a camera by dragging the camera icon from the toolbar onto the 3D view, it automatically

connects to the Merge 3D you are viewing. Also, the current viewer is set to look through the new camera.

Alternatively, it is possible to copy the current viewer to a camera (or spotlight or any other object) by

selecting the Copy PoV To option in the viewer’s contextual menu, under the Camera submenu.

Inputs

There are three optional inputs on the Camera 3D node in the Node Editor.

SceneInput: The orange input is used to connect a 3D scene or object. When connected, the

geometry links to the camera’s field of view. It acts similarly to an image attached to the Image Plane

input. If the camera’s Projection tab has projection enabled, the image attached to the orange image

input projects on to the geometry.

ImageInput: The optional magenta input is used to connect a 2D image. When camera projection is

enabled, the image can be used as a texture. Alternatively, when the camera’s image plane controls

are used, the parented planar geometry is linked to the camera’s field of view.

RightStereoCamera: The green input should be connected to another Camera 3D node when

creating 3D stereoscopic effects. It is used to override the internal camera used for the right eye in

stereoscopic renders and viewers.

Basic Node Setup

The output of a camera 3D node should be connected to a Merge 3D node. You then view the Merge

3D node and select the camera from the viewer’s right-click menu or by right-clicking over the axis

label in the viewer.

Camera node connected to and viewed through the Merge 3D

Displaying a camera node directly in the viewer shows only an empty scene; there is nothing for the

camera to see. To view the scene through the camera, view the Merge 3D node where the camera

is connected, or any node downstream of that Merge 3D. Then right-click on the viewer and select

Camera > [Camera name] from the contextual menu. Right-clicking on the axis label found in the lower

corner of each 3D viewer also displays the Camera submenu.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

The aspect of the viewer may be different from the aspect of the camera, so the camera view may not

match the actual boundaries of the image rendered by the Renderer 3D node. Guides can be enabled

to represent the portion of the view that the camera sees and assist you in framing the shot. Right-click

on the viewer and select an option from the Guides > Frame Aspect submenu. The default option uses

the format enabled in the Composition > Frame Format preferences. To toggle the guides on or off,

select Guides > Show Guides from the viewers’ contextual menu, or use the Command-G (macOS) or

Ctrl-G (Windows) keyboard shortcut when the viewer is active.

Inspector

Camera 3D controls

Controls Tab

The Camera3D Inspector includes six tabs along the top. The first tab, called the Controls tab, contains

some of the most fundamental camera settings, including the camera’s clipping plains, field of view,

focal length, and stereoscopic properties. Some tabs are not displayed until a required connection is

made to the Camera 3D node.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Projection Type

The Projection Type menu is used to select between Perspective and Orthographic cameras.

Generally, real-world cameras are perspective cameras. An orthographic camera uses parallel

orthographic projection, a technique where the view plane is perpendicular to the viewing direction.

This produces a parallel camera output that is undistorted by perspective.

Orthographic cameras present controls only for the near and far clipping planes, and a control to set

the viewing scale.

Near/Far Clip

The clipping planes are used to limit what geometry in a scene is rendered based on an object’s

distance from the camera’s focal point. Clipping planes ensure objects that are extremely close to the

camera, as well as objects that are too far away to be useful, are excluded from the final rendering.

The default perspective camera ignores this setting unless the Adaptive Near/Far Clip checkbox

located under the Near/Far Clip control is disabled.

The clip values use units, so a far clipping plane of 20 means that any object more than 20 units from

the camera is invisible to the camera. A near clipping plane of 0.1 means that any object closer than 0.1

units is also invisible.

NOTE: A smaller range between the near and far clipping planes allows greater accuracy

in all depth calculations. If a scene begins to render strange artifacts on distant objects, try

increasing the distance for the Near Clip plane.

Adaptive Near/Far Clip

When selected, the renderer automatically adjusts the camera’s near/far clipping plane to match

the extents of the scene. This setting overrides the values of the Near and Far clip range controls

described above. This option is not available for orthographic cameras.

Viewing Volume Size

When the Projection Type is set to Orthographic, the viewing volume size adjustment appears.

It determines the size of the box that makes up the camera’s field of view.

The Z-distance of an orthographic camera from the objects it sees does not affect the scale of those

objects, only the viewing size does.

Angle of View Type

Use the Angle of View Type buttons to choose how the camera’s angle of view is measured. Some

applications use vertical measurements, some use horizontal, and others use diagonal measurements.

Changing the Angle of View type causes the Angle of View control below to recalculate.

Angle of View

Angle of View defines the area of the scene that can be viewed through the camera. Generally, the

human eye can see more of a scene than a camera, and various lenses record different degrees of the

total image. A large value produces a wider angle of view, and a smaller value produces a narrower, or

more tightly focused, angle of view.

Just as in a real-world camera, the angle of view and focal length controls are directly related. Smaller

focal lengths produce a wider angle of view, so changing one control automatically changes the

other to match.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Focal Length

In the real world, a lens’ Focal Length is the distance from the center of the lens to the film plane.

The shorter the focal length, the closer the focal plane is to the back of the lens. The focal length

is measured in millimeters. The angle of view and focal length controls are directly related. Smaller

focal lengths produce a wider angle of view, so changing one control automatically changes the

other to match.

The relationship between focal length and angle of view is angle = 2 * arctan[aperture / 2 /

focal_length].

Use the vertical aperture size to get the vertical angle of view and the horizontal aperture size to get

the horizontal angle of view.

Plane of Focus (For Depth of Field)

Like a focal point on a real-world camera, this setting defines the distance from the camera to an

object. It is used by the OpenGL renderer in the Renderer 3D node to calculate depth of field.

Stereo

The Stereo section includes options for setting up 3D stereoscopic cameras. 3D stereoscopic

composites work by capturing two slightly different views, displayed separately to the left and right

eyes. The mode menu determines if the current camera is a stereoscopic setup or a mono camera.

When set to the default mono setting, the camera views the scene as a traditional 2D film camera.

Three other options in the mode menu determine the method used for 3D stereoscopic cameras.

Toe In

In a toe-in setup, both cameras are rotating

in on a single focal point. Though the result is

stereoscopic, the vertical parallax introduced

by this method can cause discomfort by the

audience. Toe-in stereoscopic works for

convergence around the center of the images

but exhibits keystoning, or image separation,

to the left and right edges. This setup is can be

used when the focus point and the convergence

point need to be the same. It is also used in

cases where it is the only way to match a live-

action camera rig.

Toe In 3D camera setup

Off Axis

Regarded as the correct way to create stereo

pairs, this is the default method in Fusion.

Off Axis introduces no vertical parallax, thus

creating stereo images with less eye strain.

Sometimes called a skewed-frustum setup, this

is akin to a lens shift in the real world. Instead of

rotating the two cameras inward as in a toe-in

setup, Off Axis shifts the lenses inward.

Off axis 3D camera setup


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Parallel

The cameras are shifted parallel to each other.

Since this is a purely parallel shift, there is

no Convergence Distance control that limits

your control over placing objects in front of or

behind the screen. However, Parallel introduces

no vertical parallax, thus creating less strain

on the eyes.

Parallel 3D camera setup

Rig Attached To

This drop-down menu allows you to control which camera is used to transform the stereoscopic setup.

Based on this menu, transform controls appear in the viewer either on the right camera, left camera,

or between the two cameras. The ability to switch the transform controls through rigging can assist in

matching the animation path to a camera crane or other live-action camera motion. The Center option

places the transform controls between the two cameras and moves each evenly as the separation and

convergence are adjusted. Left puts the transform controls on the left camera, and the right camera

moves as the separation and convergence are adjusted. Right puts the transform controls on the right

camera, and the left camera moves as adjustments are made to separation and convergence.

Eye Separation

Eye Separation defines the distance between both stereo cameras. Setting Eye Separation to a value

larger than 0 shows controls for each camera in the viewer when this node is selected. Note that there

is no Convergence Distance control in Parallel mode.

Convergence Distance

This control sets the stereoscopic convergence distance, defined as a point located along the Z-axis

of the camera that determines where both left- and right-eye cameras converge.

The Convergence Distance controls are only available when setting the Mode menu to Toe-In

or Off Axis.

Film Back

Film Gate

The size of the film gate represents the dimensions of the aperture. Instead of setting the aperture’s

width and height, you can choose it using the list of preset camera types in the Film Gate menu.

Selecting one of the options automatically sets the aperture width and aperture height to match.

Aperture Width/Height

The Aperture Width and Height sliders control the dimensions of the camera’s aperture or the portion

of the camera that lets light in on a real-world camera. In video and film cameras, the aperture is the

mask opening that defines the area of each frame exposed. The Aperture control uses inches as its

unit of measurement.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Resolution Gate Fit

Determines how the film gate is fitted within the resolution gate. This only has an effect when the

aspect of the film gate is not the same aspect as the output image.

NOTE: This setting corresponds to Maya’s Resolution Gate. The modes Overscan, Horizontal,

Vertical, and Fill correspond to Inside, Width, Height, and Outside.

�Inside: The image source defined by the film gate is scaled uniformly until one of its dimensions

(X or Y) fits the inside dimensions of the resolution gate mask. Depending on the relative

dimensions of image source and mask background, either the image source’s width or height may

be cropped to fit the dimension of the mask.

�Width: The image source defined by the film gate is scaled uniformly until its width (X) fits the

width of the resolution gate mask. Depending on the relative dimensions of image source and

mask, the image source’s Y-dimension might not fit the mask’s Y-dimension, resulting in either

cropping of the image source in Y or the image source not covering the mask’s height entirely.

�Height: The image source defined by the film gate is scaled uniformly until its height (Y) fits the

height of the resolution gate mask. Depending on the relative dimensions of image source and

mask, the image source’s X-dimension might not fit the mask’s X-dimension, resulting in either

cropping of the image source in X or the image source not covering the mask’s width entirely.

�Outside: The image source defined by the film gate is scaled uniformly until one of its dimensions

(X or Y) fits the outside dimensions of the resolution gate mask. Depending on the relative

dimensions of image source and mask, either the image source’s width or height may be cropped

or not fit the dimension of the mask.

�Stretch: The image source defined by the film gate is stretched in X and Y to accommodate the

full dimensions of the generated resolution gate mask. This might lead to visible distortions of

the image source.

Control Visibility

This section allows you to selectively activate the onscreen controls that are displayed along with

the camera.

�Show View Controls: Displays or hides all camera onscreen controls in the viewers.

�Frustum: Displays the actual viewing cone of the camera.

�View Vector: Displays a white line inside the viewing cone, which can be used to determine the

shift when in Parallel mode.

�Near Clip: The Near clipping plane. This plane can be subdivided for better visibility.

�Far Clip: The Far clipping plane. This plane can be subdivided for better visibility.

�Focal Plane: The plane based on the Plane of Focus slider explained in the Controls tab above.

This plane can be subdivided for better visibility.

�Convergence Distance: The point of convergence when using Stereo mode. This plane can be

subdivided for better visibility.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Import Camera

The Import Camera button displays a dialog to import a camera from another application.

It supports the following file types:

*LightWave Scene

.lws

*Max Scene

.ase

*Maya Ascii Scene

.ma

*dotXSI

.xsi

NOTE: FBX cameras can be imported using DaVinci Resolve’s Fusion > Import > FBX Scene

menu or File > Import > FBX Scene in Fusion Studio.

Image Tab

When a 2D image is connected to the magenta image input on the Camera3D node, an Image tab

is created at the top of the inspector. The connected image is always oriented so it fills the camera’s

field of view.

Except for the controls listed below, the options in this tab are identical to those commonly found

in other 3D nodes. For more detail on visibility, lighting, matte, blend mode, normals/tangents, and

Object ID, see “The Common Controls” section at the end of this chapter.

Camera 3D image plane tab

Enable Image Plane

Use this checkbox to enable or disable the usage of the Image Plane.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Fill Method

This menu configures how to scale the image plane if the camera has a different aspect ratio.

�Inside: The image plane is scaled uniformly until one of its dimensions (X or Y) fits the inside

dimensions of the resolution gate mask. Depending on the relative dimensions of image source

and mask background, either the image source’s width or height may be cropped to fit the

dimensions of the mask.

�Width: The image plane is scaled uniformly until its width (X) fits the width of the mask.

Depending on the relative dimensions of image source and the resolution gate mask, the image

source’s Y-dimension might not fit the mask’s Y-dimension, resulting in either cropping of the

image source in Y or the image source not covering the mask’s height entirely.

�Height: The image plane is scaled uniformly until its height (Y) fits the height of the mask.

Depending on the relative dimensions of image source and the resolution gate mask, the image

source’s X-dimension might not fit the mask’s X-dimension, resulting in either cropping of the

image source in X or the image source not covering the mask’s width entirely.

�Outside: The image plane is scaled uniformly until one of its dimensions (X or Y) fits the outside

dimensions of the resolution gate mask. Depending on the relative dimensions of image source

and mask, either the image source’s width or height may be cropped or not fit the respective

dimension of the mask.

�Depth: The Depth slider controls the image plane’s distance from the camera.

NOTE: The Camera Z position has no effect on the image plane’s distance from the camera.

Materials Tab

The options presented in the Materials tab are identical to those commonly found in other 3D nodes.

For more detail on Diffuse, Specular, Transmittance, and Martial ID controls, see “The Common

Controls” section at the end of this chapter.

Projection Tab

When a 2D image is connected to the camera node, a fourth projection tab is displayed at the top of

the Inspector. Using this Projection tab, it is possible to project the image into the scene. A projection

is different from an image plane in that the projection falls onto the geometry in the scene exactly as if

there were a physical projector present in the scene. The image is projected as light, which means the

Renderer 3D node must be set to enable lighting for the projection to be visible.

Enable Camera Projection

Select this checkbox to enable projection of the 2D image connected to the magenta input on the

Camera node.

Projection Fit Method

This menu can be used to select the method used to match the aspect of the projected image to the

camera’s field of view.

Projection Mode

�Light: Defines the projection as a spotlight.

�Ambient Light: Defines the projection as an ambient light.

�Texture: Allows a projection that can be relighted using other lights. Using this setting requires a

Catcher node connected to the applicable inputs of the specific material.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Camera 3D projection tab

Common Controls

Transform and Settings Tabs

The options presented in the Transform and Settings tabs are commonly found in other 3D nodes.

For more detail on the controls found in these tabs, see “The Common Controls” section at the end of

this chapter.

Tips for Camera 3D

Camera Projection: When importing a camera from a 3D application that is also used as a

projector, make sure that the Fit Resolution Gate options on the Controls tab as well as the

Projection tab are in sync. Only the first one automatically sets to what the 3D app was using.

The latter might have to be adjusted manually.

Image Plane: The camera’s image plane isn‘t just a virtual guide for you in the viewers.

It‘s actual geometry that you can also project on to. To use a different image on the image

plane, you need to insert a Replace Material node after your Camera node.

Parallel Stereo: There are three ways you can achieve real Parallel Stereo mode:

•	 Connect an additional external (right) camera to the green Right Stereo Camera

input of your camera.

•	 Create separate left and right cameras.

•	 When using Toe-In or Off Axis, set the Convergence Distance slider to a very large

value of 999999999.

Rendering Overscan: If you want to render an image with overscan, you also must modify

your scene‘s Camera3D. Since overscan settings aren’t exported along with camera data from

3D applications, this is also necessary for cameras you’ve imported via .fbx or .ma files. The

solution is to increase the film back’s width and height by the factor necessary to account for

extra pixels on each side.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION