---
title: "About Pre-Roll"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 469
---

# About Pre-Roll

Pre-Roll is necessary because the state of a particle system is entirely dependent on the last known

position of the particles. If the current time were changed to a frame where the last frame particle

state is unknown, the display of the particle is calculated on the last known position, producing

inaccurate results.

To demonstrate:


Add a pEmitter and a pRender node to the composition.


View the pRender in one of the viewers.


Set the Velocity of the particles to 0.1.


Place the pEmitter on the left edge of the screen.


Set the Current Frame to 0.


Set a Render Range from 0–100 and press the Play button.


Observe how the particle system behaves.


Stop the playback and return the current time to frame 0.


In the pRender node, disable the Automatic Pre-Roll option.

10	 Use the current time number field to jump to frame 10, and then to frames 60 and 90.

Notice how the particle system only adds to the particles it has already created and does not try to

create the particles that would have been emitted in the intervening frames. Try selecting the Pre-Roll

button in the pRender node. Now the particle system state is represented correctly.

For simple, fast-rendering particle systems, it is recommended to leave the Automatic Pre-Roll option

on. For slower particle systems with long time ranges, it may be desirable to only Pre-Roll manually,

as required.

�Only Render in Hi-Q

Selecting this checkbox causes the style of the particles to be overridden when the Hi-Q

checkbox is deselected, producing only fast rendering Point-style particles. This is useful when

working with a large quantity of slow Image-based or Blob-style particles. To see the particles as

they would appear in a final render, simply enable the Hi-Q checkbox.

�View

This drop-down list provides options to determine the position of the camera view in a 3D

particle system. The default option of Scene (Perspective) will render the particle system from

the perspective of a virtual camera, the position of which can be modified using the controls in

the Scene tab. The other options provide orthographic views of the front, top, and side of the

particle system.

It is important to realize that the position of the onscreen controls for Particle nodes is unaffected

by this control. In 2D mode, the onscreen controls are always drawn as if the viewer were showing

the front orthographic view. (3D mode gets the position of controls right at all times.)

The View setting is ignored if a Camera 3D node is connected to the pRender node’s Camera

input on the node tree, or if the pRender is in 3D mode.

Conditions

�Blur, Glow, and Blur Blend

When generating 2D particles, these sliders apply a Gaussian blur, glows, and blur blending to the

image as it is rendered, which can be used to soften the particles and blend them. The result is no

different than adding a Blur after the pRender node in the node tree.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

�Sub-Frame Calculation Accuracy

This determines the number of sub-samples taken between frames when calculating the particle

system. Higher values increase the accuracy of the calculation but also increase the amount of

time to render the particle system.

�Pre-Generate Frames

This control is used to cause the particle system to pre-generate a set number of frames before its

first valid frame. This is used to give a particle system an initial state from which to start.

A good example of when this might be useful is in a shot where particles are used to create the

smoke rising from a chimney. Set Pre-Generate Frames to a number high enough to ensure that

the smoke is already present in the scene before the render begins, rather than having it just

starting to emerge from the emitter for the first few frames.

�Kill Particles That Leave the View

Selecting this checkbox control automatically destroys any particles that leave the visible

boundaries of the image. This can help to speed render times. Particles destroyed in this

fashion never return, regardless of any external forces acting upon them.Generate Z Buffer

Selecting this checkbox causes the pRender node to produce a Z Buffer channel in the image.

The depth of each particle is represented in the Z Buffer. This channel can then be used for

additional depth operations like Depth Blur, Depth Fog, and Downstream Z Merging.

Enabling this option is likely to increase the render times for the particle system dramatically.

�Depth Merge Particles

Enabling this option causes the particles to be merged using Depth Merge techniques, rather than

layer-based techniques.

Scene Tab

The pRender Scene tab


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Z Clip

The Z Clip control is used to set a clipping plane in front of the camera. Particles that cross this

plane are clipped, preventing them from impacting on the virtual lens of the camera and dominating

the scene.

Grid Tab

These controls do not apply to 3D particles.

The grid is a helpful, non-rendering display guide used to orient the 2D particles in 3D space. The

grid is never seen in renders, just like a center crosshair is never seen in a render. The width, depth,

number of lines, and grid color can be set using the controls found in this tab.

These controls cannot be animated.

The pRender Grid tab

Image Tab

The controls in this tab are used to set the resolution, color depth, and pixel aspect of the rendered

image produced by the node.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

The pRender Image tab

Process Mode

Use this menu control to select the Fields Processing mode used by Fusion to render changes to

the image. The default option is determined by the Has Fields checkbox control in the Frame Format

preferences.

Use Frame Format Settings

When this checkbox is selected, the width, height, and pixel aspect of the rendered images by the

node will be locked to values defined in the composition’s Frame Format preferences. If the Frame

Format preferences change, the resolution of the image produced by the node will change to match.

Disabling this option can be useful to build a composition at a different resolution than the eventual

target resolution for the final render.

Width/Height

This pair of controls is used to set the Width and Height dimensions of the image to be rendered

by the node.

Pixel Aspect

This control is used to specify the Pixel Aspect ratio of the rendered particles. An aspect ratio of

1:1 would generate a square pixel with the same dimensions on either side (like a computer display

monitor), and an aspect of 0.9:1 would create a slightly rectangular pixel (like an NTSC monitor).

NOTE: Right-click on the Width, Height, or Pixel Aspect controls to display a menu listing the

file formats defined in the preferences Frame Format tab. Selecting any of the listed options

will set the width, height, and pixel aspect to the values for that format, accordingly.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION

Depth

The Depth menu is used to set the pixel color depth of the particles. 32-bit pixels require 4X the

memory of 8-bit pixels but have far greater color accuracy. Float pixels allow high dynamic range

values outside the normal 0…1 range, for representing colors that are brighter than white or darker

than black.

Source Color Space

You can use the Source Color Space menu to set the Color Space of the footage to help achieve a

linear workflow. Unlike the Gamut tool, this doesn‘t perform any actual color space conversion, but

rather adds the source space data into the metadata, if that metadata doesn‘t exist. The metadata can

then be used downstream by a Gamut tool with the From Image option, or in a Saver, if explicit output

spaces are defined there. There are two options to choose from:

�Auto: Automatically reads and passes on the metadata that may be in the image.

�Space: Displays a Color Space Type menu where you can choose the correct color

space of the image.

Source Gamma Space

Using the Curve type menu, you can set the Gamma Space of the footage and choose to remove it by

way of the Remove Curve checkbox when working in a linear workflow. There are three choices in the

Curve type menu:

�Auto: Automatically reads and passes on the metadata that may be in the image.

�Space: Displays a Gamma Space Type menu where you can choose the correct

gamma curve of the image.

�Log: Brings up the Log/Lin settings, similar to the Cineon tool.

For more information, see Chapter 99, "Film Nodes," in the DaVinci Resolve Reference Manual,

or Chapter 39 in the Fusion Reference Manual.

Remove Curve

Depending on the selected Gamma Space or on the Gamma Space found in Auto mode, the Gamma

Curve is removed from, or a log-lin conversion is performed on, the material, effectively converting it

to a linear output space.

Motion Blur

As with other 2D nodes in Fusion, Motion Blur is enabled from within the Settings tab. You may set

Quality, Shutter Angle, Sample Center, and Bias, and Blur will be applied to all moving particles.

NOTE: Motion Blur on 3D mode particles (rendered with a Renderer 3D) also requires that

identical motion blur settings are applied to the Renderer 3D node.


Fusion Page Effects | Chapter 114 Particle Nodes

FUSION