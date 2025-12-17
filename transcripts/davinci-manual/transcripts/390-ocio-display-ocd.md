---
title: "OCIO Display [OCD]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 390
---

# OCIO Display [OCD]

The OCIO Display node

OCD Display Node Introduction

The OCIO Display node allows you to load an OpenColorIO (OCIO) Display transform (.ocio)

to an input.

Inputs

The single input on the OCD Display node is used to connect the node you want to apply the OCIO

Display transform to, and an effect mask, which can be used to limit the display transform area.

Basic Node Setup

Connect the media or tool that you wish to apply the OCIO Display transform to the input. The output

of the node then gets passed to the remainder of the node tree.

A simple node tree showing the OCIO Display node taking the Media In

Node, performing the Display Transform, and passing it to Media Out

Inspector

The OCIO Display controls


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Controls

The OCIO Display controls lets you load and apply an .ocio configuration file and apply its color space

and display transform to to the node’s input.

�OCIO Config File: Click the Browse button to open up a file system prompt to locate the .ocio file.

�Source Space: Choose the color space of the source material from the list.

�Display: Choose which monitor your viewer is on.

�View: Choose which color space to view.

OCIO File Transform [OCF]

The OCIO File Transform node

OCIO File Transform Node Introduction

Fusion supports the Open Color IO color management workflow by way of three OCIO nodes.

�The OCIO CDL Transform node allows you to create, save, load,

and apply a Color Decision List (CDL) grade.

�The OCIO Color Space allows sophisticated color space conversions,

based on an OCIO config file.

�The OCIO File Transform allows you to load and apply a variety of Lookup tables (LUTs).

Generally, the OCIO color pipeline is composed from a set of color transformations defined by

OCIO-specific config files, commonly named with a “.ocio” extension. These config files allow

you to share color settings within or between facilities. The path to the config file to be used is

normally specified by a user-created environment variable called “OCIO,” though some tools

allow overriding this. If no other *.ocio config files are located, the DefaultConfig.ocio file in

Fusion’s LUTs directory is used.

For in-depth documentation of the format’s internals, please refer to the official pages on

opencolorio.org.

The functionality of the OCIO File Transform node is also available as a View LUT node from

the View LUT menu.

Inputs

The OCIO File Transform node includes two inputs: one for the main image and the other for an effect

mask to limit the area where the color space conversion is applied.

Input: This orange input is the only required connection. It connects a 2D image for the LUT.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits

the applied LUT to only those pixels within the mask. An effect mask is applied to the tool after

it is processed.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Basic Node Setup

The OCIO File Transform node is often applied after a Gamut node converts the Loader to linear color

in Fusion Studio.

An OCIO File Transform node applied to a Loader node after

a Gamut node conversion to linear color space

Inspector

OCIO File Transform controls

Controls Tab

The Controls tab for the OCIO File Transform node includes options to import the LUT, invert the

transform, and select the color interpolation method.

LUT File

Displays a File > Open dialog to load the desired LUT.

CCC ID

This is the ID key used to identify the specific file transform located within the ASC CDL color

correction XML file.

Direction

Toggles between Forward and Reverse. Forward applies the corrections specified in the node,

while Reverse tries to remove those corrections. Keep in mind that not every color correction can be

undone. Imagine that all slope values have been set to 0.0, resulting in a fully black image. Reversing

that operation is not possible, neither mathematically nor visually.

Interpolation

Allows the user to select the color interpolation to achieve the best quality/render time ratio. Nearest is

the fastest interpolation, while Best is the slowest.

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Set Canvas Color [SCv]

The Set Canvas Color node

Set Canvas Color Node Introduction

Set Canvas Color is used to set the color of the area outside the domain of definition (DoD). This is

the workspace area beyond the raster by default, which is invisible since outside the raster is not

rendered. However, the DoD can be within the raster as well. This can occur when compositing

images smaller than the raster, or with transforms. By default, the canvas color used is black/no

Alpha (transparent). However, since some nodes may change an image’s canvas color—for example,

inverting a mask changes the mask’s canvas from black to white—the Set Canvas Color allows you to

control the color of the canvas to whatever you require.

The Set Canvas Color node sets the color of the workspace outside the domain of definition (DOD).

For example, if you create a circular gradient, the DoD is a square around the circular gradient in

the viewer. Everything outside the DoD is understood to be black and therefore does not have

to be rendered. To change the area outside the DoD, attach the Set Canvas Color node after the

background and change the color.

NOTE: Position the mouse pointer in a black area outside the raster to view the RGB canvas

color in the status bar at the bottom left of the Fusion window.

Inputs

The Set Canvas Color node includes two inputs: one for the main image and a second for a

foreground.

Input: This orange input is the only required connection. It accepts a 2D image that reveals the canvas

color if the image’s DoD is smaller than the raster.

Foreground: The optional green foreground input allows the canvas color to be sampled from an

image connected to this input.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Basic Node Setup

The Set Canvas Color node is placed after the image is transformed to reveal part of the raster outside

the domain of definition.

A Set Canvas Color node applied to a transformed MediaIn 1 node

In this example, the footage from MediaIn1 has been shrunk in size using the Transform1 node, leaving

empty space around the image in the frame. Feeding that output into the SetCanvasColor node allows

you to change the color of the empty space around the frame.

Inspector

Set Canvas Color controls

Controls Tab

The Controls tab for the Set Canvas Color is used for simple color selection. When the green

foreground is connected, the tab is empty.

Color Picker

Use these controls to adjust the Color and the Alpha value for the image’s canvas. It defaults to black

with zero Alpha.

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION