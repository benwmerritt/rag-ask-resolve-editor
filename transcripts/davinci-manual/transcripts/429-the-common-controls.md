---
title: "The Common Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 429
---

# The Common Controls

Settings Tab

The Settings tab

The Common Settings tab can be found on most tools in Fusion. The following controls are specific

settings for Deep Image nodes.

Hide Incoming Connections

Enabling this checkbox can hide connection lines from incoming nodes, making a node tree appear

cleaner and easier to read. When enabled, empty fields for each input on a node are displayed in

the Inspector. Dragging a connected node from the node tree into the field hides that incoming

connection line as long as the node is not selected in the node tree. When the node is selected in the

node tree, the line reappears.

Comments Tab

The Comments tab contains a single text control that is used to add comments and notes to the tool.

When a note is added to a tool, a small red dot icon appears next to the setting's tab icon and a text

bubble appears on the node. To see the note in the Node Editor, hold the mouse pointer over the

node for a moment. The contents of the Comments tab can be animated over time, if required.

Scripting Tabs

The Scripting tab is present on every tool in Fusion. It contains several edit boxes used to add scripts

that process when the tool is rendering. For more details on the contents of this tab, please consult the

scripting documentation.


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION

Chapter 107

LUT Nodes

This chapter details the LUT nodes available in Fusion.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

For purposes of this document, node trees showing MediaIn/MediaOut nodes in

DaVinci Resolve are interchangeable with Loader/Saver nodes in Fusion Studio, unless

otherwise noted.

Contents

File LUT [FLU]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2378

LUT Cube Analyzer [LCA]�������������������������������������������������������������������������������������������������������������������������������������������������������������� 2380

LUT Cube Apply [LCP]���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2381

LUT Cube Creator [LCC]����������������������������������������������������������������������������������������������������������������������������������������������������������������� 2382

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2384


Fusion Page Effects | Chapter 107 LUT Nodes

FUSION

File LUT [FLU]

The File LUT node

File LUT Node Introduction

The File LUT node applies a Lookup table (LUT) to the image: either a simple 1D LUT or a supported

3D LUT. Unlike the Color Curves node, it does not use a spline-based LUT. Instead, it loads the

LUT from a file stored on your computer or server.

This approach has two advantages. The first is that the only part of the LUT stored in the composition

is the path to the file. Since LUT files can be large, this can dramatically reduce the file size of a

composition when several LUTs are present. The second advantage is that it becomes possible

to adjust all File LUT nodes using the same file at the same time, just by changing the contents

of the LUT. This can be useful when the same LUT-based color correction is applied in many

different compositions.

Inputs

The File LUT node includes two inputs: one for the main image and the other for an effect mask to limit

the area where the LUT is applied.

Input: This orange input is the only required connection. It accepts a 2D image output that gets the

LUT applied.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

applied LUT to only those pixels within the mask. An effects mask is applied to the tool after the tool is

processed.

Basic Node Setup

The File LUT node can be placed after a MediaIn node in DaVinci Resolve or a Loader node in Fusion

Studio. Sometimes this setup is used to convert the camera-original image to linear color space for

compositing. Other times, as in the example below, the File LUT is applied at the end as a grading LUT

to apply a look from the colorist.

A File LUT node applied at the end of a node tree as a colorist’s look


Fusion Page Effects | Chapter 107 LUT Nodes

FUSION

Inspector

File LUT controls

Controls Tab

The Controls tab includes options for loading a LUT and making adjustments to the gain, color space,

and Alpha channel, if one exists.

LUT File

This field is used to enter the path to the LUT file. Clicking the Browse button opens a file browser

window to locate the LUT file instead of entering it manually into the LUT File field. Currently, this node

supports LUTs exported from Fusion in .LUT and .ALUT formats, DaVinci Resolve’s .CUBE format, and

several 3D LUT formats. The node fails with an error message on the Console if it is unable to find or

load the specified file.

Pre-Gain:

This slider is a gain adjustment before the LUT being applied. This can be useful for pulling in

highlights before the LUT clips them.

Post-Gain

This slider is a gain adjustment after the LUT is applied.

Color Space

This menu is used to change the color space the LUT is applied in. The default is to apply the curves

described in the LUT to the RGB color space, but options for YUV, HLS, HSV, and others are also

available.

Pre-Divide/Post-Multiply

Selecting the Pre-Divide/Post-Multiply checkbox causes the image pixel values to be divided by the

Alpha values before applying the LUT, and then re-multiplied by the Alpha value after the correction.

This helps to prevent the creation of illegally additive images, particularly around the edges of a blue/

green key or when working with 3D-rendered objects.

Settings Tab

The Settings tab in the Inspector is also duplicated in other LUT nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 107 LUT Nodes

FUSION

LUT Cube Analyzer [LCA]

The LUT Cube Analyzer node

LUT Cube Analyzer Node Introduction

The LUT Cube Analyzer takes an image originated by the LUT Cube Creator as an input and allows the

user to create a 3D LUT file in ALUT3, ITX, or 3DL format.

Feeding the original LUT Cube Creator image into the node results in an unaltered, or 1:1, LUT file, and

nothing is displayed in the viewer.

You can, however, modify, grade, and color correct the original cube image with as many nodes as you

like and feed the result into the LUT Cube Analyzer. This creates a LUT that exactly resembles your

color pipeline.

Inputs

The LUT Cube Analyzer includes a single orange input.

Input: The orange input is used to take the output of any node modifying an image that originated with

the LUT Cube Creator.

Basic Node Setup

The example below shows a node tree starting with a LUT Cube Creator node and going through two

color adjustments. The adjusted image is then connected to a LUT Cube Analyzer, which generates

the LUT file.

Generating a LUT starts with the LUT Cube Creator and ends with a LUT Cube Analyzer.

Inspector

LUT Cube Analyzer controls


Fusion Page Effects | Chapter 107 LUT Nodes

FUSION

Controls Tab

The Controls tab for the LUT Cube Analyzer node is used to select the desired LUT output format,

specify a filename, and write the 3D LUT to disk.

Type

Select the desired output format of the 3D LUT.

Filename

Enter the path where you want the file saved and enter the name of the LUT file. Alternatively, you can

click the Browse button to open a file browser to select the location and filename.

Write File

Press this button to generate the 3D LUT file based on the settings above.

Settings Tab

The Settings tab in the Inspector is also duplicated in other LUT nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.