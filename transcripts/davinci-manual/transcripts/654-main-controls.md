---
title: "Main Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 654
---

# Main Controls

The “Show controls for” pop-up menu lets you choose one of four pages of controls that take you

through the match moving workflow. The Output pop-up menu lets you choose what you want to

output, with choices for Disabled, Positioning Reference, and Composite.

Tracking Controls

The Tracking Controls govern the first stage of the match moving process, and this page of controls

provides everything you need for setting up, executing, and refining multi-patch motion tracks.

The controls that are exposed when

Main Controls is set to Tracking Controls

The Tracking Controls group

The primary controls used to initiate tracking. These consist of the tracking buttons that let you

execute tracks either automatically using the outer Track Forward or Track Backward buttons,

or manually using the inner Track Next or Track Previous buttons. The middle button lets you

pause tracking.

The Next Track End and Previous Track End let you jump to previous and subsequent tracked sections

of frames; in cases where there may be gaps in your tracking data, these controls let you jump to

different segments of contiguous tracking data.

Two checkboxes let you choose whether you want to track and analyze Zoom and/or Rotation. These

must be set before you begin tracking.

The Manage Tracking Patches group

The two buttons at the top let you choose which tracking patches are enabled to contribute to the

overall match moving result, or disabled. Activate None and Deactivate All let you turn all patches on

or off at once.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Clear Past and Clear Future let you clear bad tracking data forward or back in time from the playhead’s

current position, for enabled tracker controls. Delete Tracking lets you delete the tracking data at the

current frame only for enabled tracker controls.

Refresh Tracks updates a tracker control’s patch when the feature it’s tracking changes shape, color, or

lighting enough to interrupt the track. Select one or more trackers and click Place New Patch in Track

to update the tracked feature at that frame.

The Display Options group

This group lets you turn the visibility of different onscreen controls off and on. Checkboxes let you

Show Trackers, Show Center (the red tracking center point), Show Paths (the tracked motion paths),

and Show Active Patches. A slider lets you adjust the size of each patch window.

Show Comp Result lets you see the composited foreground layer against the background layer.

Positioning

The Positioning controls govern the second stage of the match moving process. They provide

everything you need to transform the foreground image to fit against the background by moving,

corner-pinning, and resizing.

The controls that are exposed when Main

Controls is set to Positioning

Canvas Options

The Canvas Controls pop-up menu lets you switch between corner-pin controls, where dragging the

four corners lets you corner-pin, dragging the center lets you reposition, and dragging the top, bottom,

and sides lets you resize vertically or horizontally.

A Reset Corners button lets you reset the grid to full screen, if you need to scrap what you’re doing

and try again.

The Display Options group

This group lets you turn the visibility of different onscreen controls off and on. Checkboxes let

you Show Trackers, Show Center (the red tracking center point), and Show Paths (the tracked

motion paths).

Show Comp Result lets you see the composited foreground layer against the background layer.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Compositing

The Compositing controls govern the third stage of the match moving process, to use when fitting the

foreground image against the background image to make a seamless composite. Note, if you need

to color correct the foreground image to match the background, you’ll need to add a corrector node

between the Ext. Matte that’s routing in the foreground image into the Color page and the FX node

that’s doing the compositing.

The controls that are exposed when

Main Controls is set to Compositing

Rendering Options

The Composite Type pop-up menu lets you choose whether the composite that’s being

output is an overlay of the Ext. Matte over the background, or the background Plate only.

Plate Cropping

Four sliders let you crop the Left, Right, Top, and Bottom of the image, if necessary.

Global Blend

The Blend slider, present in every Resolve FX plugin in DaVinci Resolve, lets you adjust the

opacity of the effect, effectively controlling the opacity of the foreground layer.

Stabilizing

The Stabilizing controls actually have nothing to do with match moving, but instead allow you to use

the motion tracking accomplished with the Tracking Controls to stabilize the image. An Edge Behavior

pop-up menu lets you choose how to handle blanking around the edges as a result of the background

image being transformed to keep the subject of the frame in place.

The controls that are exposed when Main Controls is set to Stabilizing


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Surface Tracker (Studio Version Only)

The Surface Tracker is used for applying textures and effects to flexible or deformable moving

surfaces, like cloth and skin. The Surface Tracker ensures that the folding and deforming of the texture

or effect is realistically matched to the folding and deforming of the surface that it is attached to in

the image.

The Surface tracker is a complex effect, with many different options and controls to create the most

realistic composites possible. But in all cases you simply move from left to right, using the buttons in

the effect’s settings.


Click the Bounds button, and click on the screen to define the area on the surface where you wish to

apply the new texture. The bounds should select one surface at a time and not go over/on object edges.


Click on the Mesh button to define the control points along the natural folds and curves of the

surface within the bounds.


Click on the Track button to analyze the motion of the surface over time, using the Mesh you just set.


Click on the Result button to composite the texture on top of the moving Mesh.

It is recommended that you use the Surface Tracker as a separate FX Node (dragged from the effects

library directly into the node tree), rather than applied to a normal corrector node. This allows you to have

access to an additional Alpha input for applying textures that have some transparency built in to them.

Across all the tabs in the Surface Tracker, the Tracked Range shows the start and end frame numbers

of your clip that contain tracking data. Any existing tracking data will be reset if you modify the bounds,

or mesh layout, and you will need to re-track it.

(Previous Page) The Surface Tracker in action, (Above) overlaying the logo,

and warping and conforming it realistically to the folds of the shirt.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Bounds

This is where you are prompted to draw an area on the image that you want to apply the texture to.

Ideally, you want to choose a frame in the clip that has the surface you want to track as close and

as flat-on to the camera as possible. This frame becomes the default reference frame for the effect.

Make sure that the Open FX Overlay controls are active in the Viewer to use the tool. Simply click

on the image to make multiple points around the area you want to define (a minimum of three points

are required), and the effect will connect them automatically as a polygon. Boundary points should

be on the surface for tracking, not around it. If points are accidentally placed on object edges or the

background instead, it will cause errors in the tracking.

You may add multiple boundaries and multiple holes to the same image, and all boundaries will join

together into one shape before subtracting the holes. The purpose of multiple boundaries and holes

are to allow you to mask out complex surfaces with regions not for tracking. For example, you can

make a boundary around someone’s face, but use multiple holes to exclude the eyes and mouth

as those change appearance quickly as the subject blinks and talks, making them exceptionally

difficult to track.

Multiple boundaries are designed to work on the same surface; using multiple boundaries on different

surfaces within the image will cause poor results. Separate surfaces are best tracked by using multiple

instances of the Surface Tracker instead.

The boundary is not useful for rotoscoping objects, only for analyzing the motion of a surface.

Rotoscoping of foreground objects can be done as described in the Tracking Using a Mask

section below.

Click to Add Points: These are the controls used to make boundary areas on the image.

•	 Boundary: The currently selected boundary area on the image. You can change the

current boundary or hole by using the drop-down menu. If there are issues with the

boundary (i.e., crossed edges, too few points, etc.), an error message will appear next to the

boundary name.

•	 + Bound: Adds a boundary polygon to the image. You can have multiple boundaries defined

for the same surface, and they will be joined together into one shape.

•	 + Hole: Adds an area to exclude tracking from the surface. Used to remove overly complex

and changing parts of a surface from the effect’s calculations.

•	 Delete: Lets you delete the boundary or hole selected in the Boundary field. Currently, this

operation is not undo-able, so be careful around this button.

•	 Clear All: Lets you delete all boundaries and holes in the effect.

Mesh

With the boundaries now defined, you can establish the mesh over the surface to be tracked.

The initial mesh serves as the starting point for tracking, so for best results the mesh should be placed

when your surface is as flat-on and closest to the camera as possible.

The mesh can be manually adjusted by dragging current points (multiple points can be moved by

holding command and dragging an area around the points) or clicking on an area to place new ones.

Option-clicking a point will remove it from the mesh. Manually adding mesh points can be useful if

there are flexible portions of the surface known to be a point where the texture should fold but which

is not initially identified when placing the mesh. For example, an extended arm may not have a mesh


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

point active at the elbow, but with a mouse click (and a basic knowledge of human anatomy), you can

manually add one there. Another use case would be to add points to an area with little detail, but

you know will develop detail as it rotates into view. Placing mesh points in blank areas that show little

detail will not improve results and may actually degrade them, so very few points on smooth areas is

desirable. A good rule of thumb is that if more than five points are created inside the boundaries, the

mesh may be good enough for tracking. Points cannot be added or deleted after tracking.

A good mesh is a sign of good tracking as they go hand in hand. If your mesh has few points detected

and the results don’t track tightly, you can artificially improve your results. For example, make sure that

the content is clearly visible. Tracking and point detection can fail if the surface is too bright (HDR), too

dark, or low contrast due to working in log. To improve results, you can add a corrector node before

the Surface Tracker to adjust contrast and levels manually, then run the Surface Tracker. You could

also use a corrector node with the Contrast Pop effect before the Surface Tracker to help track

surfaces that are too smooth. In both cases simply disable the corrector node again after the tracking

has finished.

�Regenerate Mesh: This button recreates the mesh at the current frame and settings and discards

any manual changes that have been made.

�Point Locations: These controls determine which mode is used to generate the mesh points.

Automatic: The Surface Tracker automatically locates the best details for tracking, and places

mesh points on those details. In most cases Automatic will give you the best results.

Point Number Limit: Lets you set the maximum amount of mesh points to place. The number of

mesh points affects how the overlay will flex and fold, and should be set by the expected flexibility

of the surface. They do not directly affect tracking speed.

Minimum Point Spacing: Lets you set the minimum distance between mesh points. This

prevents mesh points from bunching together too tightly in highly detailed areas and interfering

with each other.

�Uniform Grid: Creates a regular grid of points in the boundary and relies on internal shape models

to deform the grid during tracking. This may give better results than Automatic mode if your

surface is highly detailed.

Horizontal Spacing: Adjusts the horizontal distance between adjacent points in the uniform mesh.

Vertical Spacing: Adjusts the vertical distance between adjacent points in the uniform mesh.