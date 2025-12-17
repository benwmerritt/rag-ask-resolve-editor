---
title: "OCIO CDL Transform [OCD]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 389
---

# OCIO CDL Transform [OCD]

The OCIO CDL Transform node

OCIO CDL Transform Node Introduction

Fusion supports the Open Color IO color management workflow by way of three OCIO nodes.

�The OCIO CDL Transform node allows you to create, save, load, and apply a Color Decision

List (CDL) grade.

�The OCIO Color Space allows sophisticated color space conversions, based on an

OCIO config file.

�The OCIO File Transform allows you to load and apply a variety of Lookup tables (LUTs).

Generally, the OCIO color pipeline is composed from a set of color transformations defined by OCIO-

specific config files, commonly named with a “.ocio” extension. These config files allow you to share

color settings within or between facilities. The path to the config file to be used is normally specified

by a user-created environment variable called “OCIO,” although some tools allow overriding this. If no

other *.ocio config files are located, the DefaultConfig.ocio file in Fusion’s LUTs directory is used.

For in-depth documentation of the format’s internals, please refer to the official pages on

opencolorio.org.

Inputs

The OCIO CDL Transform node includes two inputs: one for the main image and the other for an effect

mask to limit the area where the CDL is applied.

Input: This orange input is the only required connection. It connects a 2D image output for

the CDL grade.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines,

basic primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input

limits the CDL grade to only those pixels within the mask. An effect mask is applied to the tool after it

is processed.

Basic Node Setup

The OCIO CDL Transform node is often applied after a Gamut node converts the Loader to linear color

in Fusion Studio.

A OCIO CDL Transform node applied to a Loader node after

a Gamut conversion to linear in Fusion Studio


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Inspector

OCIO Transform controls

Controls Tab

The Controls tab for the OCIO CDL Transform contains primary color grading color correction controls

in a format compatible with CDLs. You can make R, G, B adjustments based on the Slope, Offset, and

Power. There is also overall Saturation control. You can also use the Controls tab to import and export

the CDL compatible adjustments.

Operation

This menu switches between File and Controls. In File mode, standard ASC-CDL files can be loaded.

In Controls mode, manual adjustments can be made to Slope, Offset, Power, and Saturation, and the

CDL file can be saved.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

NOTE: Using DaVinci Resolve terminology, slope is similar to gain. It controls mids-to-high

contrast. Offset is the overall offset of color balance and exposure. Power is very similar to

contrast with a raised pivot, giving you control over shadow contrast.

Direction

Toggles between Forward and Reverse. Forward applies the corrections specified in the node,

while Reverse tries to remove those corrections. Keep in mind that not every color correction can

be undone.

Imagine that all slope values have been set to 0.0, resulting in a fully black image. Reversing that

operation is not possible, neither mathematically nor visually.

Slope

Slope multiplies the color values; this is the same as Gain in the Brightness Contrast node.

Offset

Offset adds to the color values; this is the same as Brightness in the Brightness Contrast node.

Power

Applies a Gamma Curve. This is an inverse of the Gamma function of the Brightness Contrast node.

Saturation

Enhances or decreases the color saturation. This works the same as Saturation in the Brightness

Contrast node.

Export File

Allows the user to export the settings as a CDL file.

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

OCIO Color Space [OCC]

The OCIO Color Space node

OCIO Color Space Node Introduction

Fusion supports the Open Color IO color management workflow by way of three OCIO nodes.

�The OCIO CDL Transform node allows you to create, save, load, and apply a Color Decision

List (CDL) grade.

�The OCIO Color Space allows sophisticated color space conversions, based on an

OCIO config file.

�The OCIO File Transform allows you to load and apply a variety of Lookup tables (LUTs).

Generally, the OCIO color pipeline is composed from a set of color transformations defined by

OCIO-specific config files, commonly named with a “.ocio” extension. These config files allow

you to share color settings within or between facilities. The path to the config file to be used is

normally specified by a user-created environment variable called “OCIO,” though some tools

allow overriding this. If no other *.ocio config files are located, the DefaultConfig.ocio file in

Fusion’s LUTs directory is used.

For in-depth documentation of the format’s internals, please refer to the official pages on

opencolorio.org.

Sample configs can be obtained from https://opencolorio.readthedocs.io/en/latest/

configurations/_index.html#configurations

The functionality of the OCIO Color Space node is also available as a View LUT node from the

View LUT menu.

Inputs

The OCIO Color Space node includes two inputs: one for the main image and the other for an effect

mask to limit the area where the color space conversion is applied.

Input: This orange input is the only required connection. It connects a 2D image for the color space

conversion.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input limits the

color space conversion to only those pixels within the mask. An effect mask is applied to the tool after

it is processed.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Basic Node Setup

The OCIO Color Space node is typically placed directly after a MediaIn node in DaVinci Resolve or

a Loader node in Fusion Studio. Another OCIO Color Space node is placed just before a Media Out

node in DaVinci Resolve or a Saver node in Fusion Studio.

An OCIO Color Space node applied to a Loader node and a Saver node in Fusion Studio

Inspector

OCIO Color Space controls

Controls Tab

The Controls tab for the OCIO Color Space node allows you to convert an image from one color

space to another based on an OCIO config file. By default, it uses the config file included with Fusion;

however, the Controls tab does allow you to load your own config file as well.

OCIO Config

Displays a File > Open dialog to load the desired config file.

Source Space

Based on the config file, the available source color spaces are listed here.

The content of this list is based solely on the loaded profile and hence can vary immensely. If no other

OCIO config file is loaded, the DefaultConfig.ocio file in Fusion’s LUTs directory is used to populate

this menu.

Output Space

Based on the config file, the available output color spaces are listed here.

The content of this list is based solely on the loaded profile and hence can vary immensely. If no other

OCIO config file is loaded, the DefaultConfig.ocio file in Fusion’s LUTs directory is used to populate

this menu.

Look

Installed OCIO Color Transform Looks appear in this menu. If no looks are installed, this menu has only

None listed as an option.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.