---
title: "Clean Plate"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 439
---

# Clean Plate

The Clean Plate node

Clean Plate Node Introduction

The Clean Plate tool is a pre-keying node used to generate an image of the green or blue color screen

to smooth out the lighting differences. The output of the Clean Plate is later connected to the Clean

Plate input on the Delta Keyer so it can key fine detail without choking or clipping the matte.

How to Create a Clean Plate

Creating a clean plate is the opposite of creating a key. When keying, you try to remove the green

or blue color. When creating a clean plate, you try to keep as much of the blue- or green-screen

as possible. By box selecting areas of the screen color in the viewer, you end up with an image of

the green/blue screen. A transparent cutout represents everything that is not part of the blue or

green screen.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Once you have the selection, the Erode control expands the pre-matte, removing any small pixels of non-green/blue

screen around the edges. Then, growing the pre‑matte fills in the holes until you have a solid blue or green image.

Inputs

The Clean Plate node includes three inputs in the Node Editor.

Input: The orange input accepts a 2D image that contains the green or blue screen.

Garbage Matte: The white garbage matte input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps masks. Connecting a mask to this input causes areas of the

image that fall within the matte to be excluded from the clean plate. For a clean plate, garbage mattes

should contain areas that are not part of the blue or green screen.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input limits the pixels where the

clean plate is generated. An effects mask is applied to the tool after the tool is processed.

Basic Node Setup

The Clean Plate node and the Delta Keyer are two separate branches stemming from the main image

you want to key. The green-screen or blue-screen clip is breached to connect to both the orange

image input on the Clean Plate and the orange image input on the Delta Keyer. The output of the clean

plate is then connected to the magenta clean plate input on the Delta Keyer. The output of the Delta

Keyer is then used as the foreground to a Merge.

A Clean Plate connected to a Delta Keyer


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Inspector

The Clean Plate tab

Plate Tab

The Plate tab contains the primary tools for creating a clean plate. Using this tab, you drag over the

areas in the viewer, and then use the Erode and Grow Edges sliders to create the clean plate.

Method

The Method menu selects the type of color selection you use when sampling colors in the viewer.

�Color: Color uses a difference method to separate the background color. This works well on

screen colors that are even.

�Ranges: Ranges uses a chroma range method to separate the background color. This is a better

option for shadowed screen or screens that have different colors.

Matte Threshold

This range slider sets the lower threshold using the handle on the left and sets the upper threshold

using the handle on the right.

Any value below the lower threshold becomes black or transparent in the matte.

Any value above the upper threshold becomes white or opaque in the matte. All values within the

range maintain their relative transparency values. This control is often used to reject salt and pepper

noise in the matte.

Erode

The Erode slider decreases the size of the screen area. It is used to eat away at small non-screen color

pixels that may interfere with creating a smooth green- or blue-screen clean plate.

Crop

Crop trims in from the edges of the image.

Grow Edges

The Grow Edges slider expands the color of the edges to fill in holes until fully green or blue screen

is created.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Fill

The Fill checkbox fills in remaining holes with color from the surrounding screen color.

Time Mode

�Sequence: Generates a new clean plate every frame.

�Hold Frame: Holds the clean plate at a single frame.

The Clean Plate Mask tab

Mask Tab

The Mask tab is used to invert the mask connected to the garbage mask input on the node.

The garbage mask can be applied to clear areas before growing edges or filling remaining holes.

Invert

Invert uses the transparent parts of the mask to clear the image.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other matte nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Cryptomatte [Cry] (Studio Version Only)

The Cryptomatte node

Cryptomatte Node Introduction

The Cryptomatte tool in Fusion allows you to read embedded mattes rendered into an EXR. Instead

of relying on manually-assigned masks or color keying, Cryptomatte reads encoded IDs and isolates

them in a way that allows for easy selection. This tool allows you to create mattes for specific objects

or materials in a 3D-rendered scene.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Inputs

The Cryptomatte node has only one input in the Node Editor.

Input: The orange input accepts a 2D EXR image with embedded mattes.

Basic Node Setup

The Cryptomatte node takes an EXR image with embedded mattes, then lets you select which mattes

to pass through to the rest of the comp.

Cryptomatte taking in an EXR, selecting its mattes, and then passing them on to the Color Corrector and Bitmap tools

Inspector

The Cryptomatte Controls

These parameters let you control the matte selection of an EXR file.

�View Layer: Change the layer and matte type to pick (Object, Material etc). This affects the type of

matte you can choose with the Pick control.

�View Mode: Changes the output of the Cryptomatte tool.

Colors: Shows the layer IDs as separate colors.

Edges: Shows the source EXR with outlined mattes overlayed the image.

Beauty: Shows the source EXR.

Matte: Outputs a black and white image of the selected matte.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

�Select Matte: Select mattes from the viewer or from a list.

Pick: Click to open a pick window with a matte list selection. Click and drag or use

Cmd/Control‑clicks to select multiple mattes from the list.

Mode: Click and drag the control to get an eye dropper cursor to select or remove mattes

from the viewer.

�Selected Matte List: The Selected Matte List displays the selected mattes in a list view.

The selection is highlighted in yellow on the viewer.

Clear: Click the bin icon to remove the selected mattes.

Clear All: Click this button to remove all mattes from the Selected Matte List.

Clear Selected Layer: Click to remove all mattes from the layer.

Matte Layers: Toggle between only the Selected layers, View, and All.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other matte nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.