---
title: "Drip [DRP]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 518
---

# Drip [DRP]

The Drip node

Drip Node Introduction

The Drip node creates a ripple effect over the entire image, which has the potential to animate

outward from a central source. There are a variety of different Drip effects from which to choose.

Inputs

The two inputs on the Drip node are used to connect a 2D image and an effect mask, which can be

used to limit the warped area.

Input: The orange input is used for the primary 2D image that is warped.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the warping to only those

pixels within the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

Below, the Drip node is used to make rippling water-style effects using a MediaIn node.

The Drip node can be connected directly after a

MediaIn node or any node providing a 2D output.

Inspector

The Drip Controls tab

Controls Tab

The Controls tab is used to change the style, position, size , strength, and phase for animating the

“ripples” of the Drip.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Shape

Use this control to select the shape of the Drip.

Circular

This creates circular ripples. This is the default Drip mode.

Square

This creates even-sided quadrilateral drips.

Random

This creates a randomly dispersed noise that distorts your image and is similar to a particle effect.

Horizontal

This creates horizontal waves that move in one direction.

Vertical

This creates vertical waves that move in one direction.

Exponential

This creates a Drip effect that looks like a diamond shape with inverted, curved sides (an exponential

curve flipped and mirrored).

Star

This creates an eight-way symmetrical star-shaped ripple that acts as a kaleidoscope when the phase

is animated.

Radial

This creates a star-shaped ripple that emits from a fixed pattern.

Center X and Y

Use this control to position the center of the Drip effect in the image. The default is 0.5, 0.5, which

centers the effect in the image.

Aspect

Control the aspect ratio of the various Drip shapes. A value of 1.0 causes the shapes to be

symmetrical. Smaller values cause the shape to be taller and narrower, while larger values cause

shorter and wider shapes.

Amplitude

The Amplitude of the Drip effect refers to the peak height of each ripple. Use the slider to change

the amount of distortion the Drip applies to the image. A value of 0.0 gives all ripples no height and

therefore makes the effect transparent. A maximum Amplitude of 10 makes each ripple extremely

visible and completely distorts the image. Higher numbers can be entered via the text entry boxes.

Dampening

Controls the Dampening, or falloff, of the amplitude as it moves away from the center of the effect. It

can be used to limit the size or area affected by the Drip.

Frequency

This changes the number of ripples emanating from the center of the Drip effect. A value of

0.0 indicates no ripples. Move the slider up to a value of 100 to correspond with the density of

desired ripples.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Phase

This controls the offset of the frequencies from the center. Animate the Phase value to make the ripple

emanate from the center of the effect.

Common Controls

Settings Tab

The Settings Tab in the Inspector is also duplicated in other Warp nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Grid Warp [Grd]

The Grid Warp node

Grid Warp Node Introduction

The Grid Warp node is a 2D deformation grid with flexible vertices. The image is deformed so that the

source grid matches the destination grid.

Inputs

The two inputs on the Grid Warp node are used to connect a 2D image and an effect mask, which can

be used to limit the warped area.

Input: The orange input is used for the primary 2D image that is warped.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the warping to only those

pixels within the mask. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

Below, two Grid Warp nodes are used to warp different areas of a frame. This can be useful for

chaining the framing in a shot or adding slight movement to a still. Using the Copy Src to Dest button,

only the area modified by Grid Warp 2 is pasted as the foreground in the Merge.

The Grid Warp can be used to shift areas within a shot for reframing or adding animation to a still.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Inspector

The Grid Warp Controls tab

Controls Tab

The Controls tab contains parameters that configure the onscreen grid as well the type of distortion

applied when a control point on the grid is moved.

Source and Destination

The Source and Destination buttons determine whether the source grid or destination grid is currently

active. Only one grid can be displayed or manipulated at a time. The selected button is highlighted to

indicate that it is the currently active grid.

All other controls in this tab affect the grid selected by this control.

Selection Type

These three buttons determine the selection types used for manipulating the points. There are three

options available.

Selected

When in Selected mode, adjustments to the grid are applied only to the currently selected points.

This mode is identical to normal polyline operation.

Region

In Region mode, all points within the area around the mouse pointer move when the mouse button is

clicked. New points that enter the region during the move are ignored. Choosing this option exposes

Magnet Distance and Magnet Strength controls to determine the size and falloff of the area.

Magnetic

In Magnetic mode, all points within the area around the mouse pointer move when the mouse button

is clicked. New points that enter the region during the move are affected as well. Choosing this option

exposes Magnet Distance and Magnet Strength controls to determine the size and falloff of the area.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Magnet Distance

The default node for selecting and manipulating the grid is a Magnet node. The magnet is represented

in the viewer by a circle around the mouse pointer. The Magnet Distance slider controls how large the

region of effect for the magnet is, as in the size of the circle. Drag on the grid and any vertex within the

range of the slider moves.

To increase the size of the magnet, increase the value of this slider. Alternately, adjust the size of the

magnet by holding down the D key while dragging the mouse.

Magnet Strength

The Magnet Strength slider increases or decreases the falloff of the magnet cursor’s effect. At a

setting of 0.0, the magnetic cursor has no effect, and vertices do not move at all. As the values

increase, the magnet causes a greater range of motion in the selected vertices. Use smaller values for

a more sensitive adjustment and larger values for broad-sweeping changes to the grid.

X and Y Grid Size

The X and Y Grid Size sliders control the number of divisions in the grid. Where the X and Y divisions

intersect, a control vertex is created.

Be aware that changing either of these controls after applying changes in the grid resets the entire

grid. Set the X and Y grid sizes to the appropriate resolution before making detailed adjustments

to the grid.

Subdivision Level

The Subdivision Level determines how many subdivisions there are between each set of divisions.

Subdivisions do not generate vertices at intersections. The more subdivisions, the smoother the

deformation is likely to be, but the slower it is to render.

Center

The Center coordinates determine the exact center of the grid. The onscreen Center control is

invisible while editing the grid. Select the Edit Rect mode, and the grid center becomes visible and

available for editing.

Use the Center control to move the grid through a scene without affecting the animation applied to the

individual vertices. For example, while deforming lips, track the motion of the face with a Tracker, and

connect the grid center to the Tracker. This matches the grid with slight movements of the head while

focusing on the deformation of the lips.

Angle

This Angle control rotates the entire grid.

Size

The Size control increases or decreases the scale of the grid.

Edit Buttons

There are four edit modes available, each of which can be selected by clicking on the

appropriate button.

Edit None

Set the grid to Edit None mode to disable the display of all onscreen controls.

Edit Grid

The Edit Grid mode is the default mode. While this mode is enabled, the grid is drawn in the viewer,

and the control vertices of the grid can be manipulated directly.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Edit Rectangle

When the grid is in Edit Rectangle mode, the onscreen controls display a rectangle that determines the

dimensions of the grid. The sides of the rectangle can be adjusted to increase or decrease the grid’s

dimension. This mode also reveals the onscreen Center control for the grid.

Edit Line

The Edit Line mode is beneficial for creating grids around organic shapes. When this mode is

enabled, all onscreen controls disappear, and a spline can be drawn around the shape or object to be

deformed. While drawing the spline, a grid is automatically created that best represents that object.

Additional controls for Tolerance, Over Size, and Snap Distance appear when this mode is enabled.

These controls are documented below.

Set Mesh to Entire Image

The Set Mesh to Entire Image button automatically resets the size of the grid to the exact dimensions

of the image. Any adjustments to vertices within the grid are reset.

Copy Buttons

These two buttons provide a technique for copying the exact shape and dimensions of the source

grid to the destination, or the destination grid to the source. This is particularly useful after setting the

source grid to ensure that the destination grid’s initial state matches the source grid before beginning

a deformation.

Point Tolerance

This control is visible only when the Edit Line mode is enabled. The Point Tolerance slider determines

how much tessellation the grid applies to match the density of points in the spline closely. The lower

this value, the fewer vertices there are in the resulting grid, and the more uniform the grid appears.

Higher values start applying denser grids with variations to account for regions in the spline that

require more detail.

Oversize Amount

This control is visible only when the Edit Line mode is enabled. The Oversize Amount slider is used to

set how large an area around the spline should be included in the grid. Higher values create a larger

border, which can be useful when blending a deformation back into the source image.

Snap Distance

This control is visible only when the Edit Line mode is enabled. The Snap Distance slider dictates how

strongly the drawn spline attracts surrounding vertices. If a vertex is close enough to a spline’s edge,

the vertex moves to line up with the spline. The higher the value, the farther the reach of the spline.

Right-Click Here for Mesh Animation

The grids are static by default. Right-clicking on the Right-Click Here for Mesh Animation label

provides a contextual menu with options for animating the grid or connecting it to another

grid in the composition.

The grid uses a Polychange spline. Any adjustment to the control points adds or modifies the

keyframe for all points on that spline.

Right-Click Here for Shape Animation

This label appears only in the Edit Line mode. Right-clicking on the Right-Click Here for Shape

Animation label reveals a pop-up menu used to animate the shaping polyline or to connect it to

other polylines.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

The Grid Warp Render tab

Render Tab

The Render tab controls the final rendered quality and appearance of the warping.

Render Method

The Render Method drop-down menu is used to select the rendering technique and quality applied to

the mesh. The three settings are arranged in order of quality, with the first, Wireframe, as the fastest

and lowest of quality. The default mode is Render, which produces final resolution, full-quality results.

Anti-Aliasing

The Anti-Aliasing control appears only as a checkbox when in Wireframe Render mode.

In other modes, it is a drop-down menu with three levels of quality. Higher degrees of anti-aliasing

improve image quality dramatically but vastly increase render times. The Low setting may be an

appropriate option while setting up a large dense grid or previewing a node tree, but rarely for a

final render.

Filter Type

When the Render Method is set to something other than Wireframe mode, the Filter Type menu is

visible and set to Area Sample. This setting prevents the grid from calculating area samples for each

vertex in the grid, providing good render quality. Super Sample can provide even better results but

requires much greater render times.

Wireframe Width

This slider appears only when the Render Method is set to Wireframe. It determines the width of the

lines that make up the wireframe.

Anti-Aliased

This checkbox appears only when the Render Method is set to Wireframe. Use this checkbox to

enable/disable anti-aliasing for the lines that make up the wireframe.

Black Background

The Black Background checkbox determines whether pixels outside of the grid in the source image

are set to black or if they are preserved.

Object ID and Material ID

Enable the Object ID or Material ID checkboxes to have the grid output the proper ID channel in the

final render.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Set Image Coordinates at Subdivision Level

This checkbox defaults to enabled and sets the image coordinates at the subdivision level.

Force Destination Render

This checkbox defaults to enabled and forces a destination render.

Grid Warp Contextual Menu options

Contextual Menu Options

The Grid Warp node places a submenu for both source and destination grids in the viewer’s contextual

menu. Both menus have the exact same name, where only the menu for the active grid is populated

with options. The other menu is empty. The contextual menu options are also available from the

toolbar that appears in the viewer.

Modify Only/Done

These two options set the mesh to Modify Only and Done modes, respectively. Select Modify Only to

edit the mesh or Modify Done to prevent any further changes to a mesh.

Smooth/Linear

Use Smooth and Linear options to apply or remove smoothing from selected vertices.

Auto Smooth Points

When Auto Smooth Points is enabled, the vertices in the grid are automatically smoothed whenever

they are moved. This is generally enabled by default.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION

Z Under/Z Same/Z Over

When two vertices in a grid overlap, one ends up getting clipped by the other. Z Under, Z Same, and Z

Over are used to select which vertices are rendered on top and which are rendered behind.

Select All

This option selects all points in the mesh.

Show Key Points, Handles, Grid, and Subdivisions

Use these four options to enable or disable the display of the grid, key points (vertices), Bézier

handles, and subdivisions in the viewers.

Reset Selected Points

This resets Selected Points (vertices) to their default positions.

Reset All Points

This resets all points (vertices) in the mesh to their default positions.

Stop Rendering

This option stops rendering, which disables all rendering of the Grid Warp node until the mode is

turned off. This is frequently useful when making a series of fine adjustments to a complex grid.

Grid Warp Toolbar

Whenever the Grid Warp node is selected and is in Edit Grid mode, the Grid Warp toolbar is displayed

in the views. This toolbar provides a variety of options for manipulating and adjusting the grid. The

toolbar buttons in this toolbar are described in the preceding “Contextual Menu Options” section.

The Grid Warp viewer toolbar

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Warp nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 123 Warp Nodes

FUSION