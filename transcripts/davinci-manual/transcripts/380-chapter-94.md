---
title: "Chapter 94"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 380
---

# Chapter 94

Color Nodes

This chapter details the Color nodes available in Fusion. The abbreviations next to

each node name can be used in the Select Tool dialog when searching for tools

and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

ColorFX

ACESTransform [ATr]������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2084

Chromatic Adaptation [CRa]���������������������������������������������������������������������������������������������������������������������������������������������������������� 2086

Color Space Transform [CSt]��������������������������������������������������������������������������������������������������������������������������������������������������������� 2088

Gamut Limiter [GMl]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2091

Gamut Mapping [GMp]��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2093

Revival

Chromatic Aberration Removal [CAr]��������������������������������������������������������������������������������������������������������������������������������������� 2096

Color

Auto Gain [AG]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2099

Brightness Contrast [BC]������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2101

Channel Booleans [Bol]�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2104

Color Corrector [CC]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2107

Color Curves [CCv]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2118

Color Gain [Clr]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2121

Color Matrix [CMx]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2126

Color Space [CS]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2130

Copy Aux [CpA]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2132

Gamut [Gmt]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2135

Hue Curves [HCv]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2138

OCIO CDL Transform [OCD]������������������������������������������������������������������������������������������������������������������������������������������������������������ 2141

OCIO Color Space [OCC]���������������������������������������������������������������������������������������������������������������������������������������������������������������� 2144

OCIO Display [OCD]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2146


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

ColorFX

A sub category of the Color tools in Fusion that gives you access to various color

processing tools.

ACESTransform [ATr]

The ACES Transform node

ACES Transform Node Introduction

A simple node that lets you perform color transforms using the ACES Input Device Transform and

ACES Output Device Transform parameters.

Inputs

The two inputs on the ACES Transform node are the input and effect mask.

Input: The orange input connects the primary 2D image for the auto gain.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the adjustment to only

those pixels within the mask. An effect mask is applied to the tool after the tool is processed.

Basic Node Setup

The ACES Transform node, like many 2D image-processing nodes, receives a 2D image, such as a

Loader node or the MediaIn1 shown below. The output continues the node tree by connecting to

another 2D image-processing node or a Merge node.

An ACES Transform node applied to a MediaIn1 node

OCIO File Transform [OCF]�������������������������������������������������������������������������������������������������������������������������������������������������������������� 2147

Set Canvas Color [SCv]��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2149

White Balance [WB]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2151

The Common Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2155


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Inspector

ACES Transform controls

Controls Tab

The Controls tab contains the few primary controls necessary for performing the ACES transform on

the input.

ACES Version

Lets you choose which version of ACES you want to use.

Input Transform

This menu lets you choose which IDT (Input Device Transform) to use to process the image. Typically

you would pick the camera that your footage was shot with here.

Output Transform

This menu lets you choose an ODT (Output Device Transform) with which to transform the image data

to the color space for your exported timeline.

Gamut Compress Type

This lets you choose the type of ACES Gamut compression applied to the node. Choosing either

option can prevent monochromatic highly saturated light sources (LEDs, neon signs, tail lights, etc.)

from clipping the gamut.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Chromatic Adaptation [CRa]

The Chromatic Adaptation node

Chromatic Adaptation Node Introduction

A simple node that lets you precisely transform an image that has been lit or processed assuming one

specific color temperature to another user-selectable color temperature. This transformation alters the

appearance of all colors in the image as perceived by the human vision system in the same way that a

new illuminant would, whether that illuminant is a light in the environment being recorded or the color

temperature of a display on which the image is shown. This node is useful for performing specific color

temperature transformations as part of color management workflows or for setting up precise color

temperature adjustments.

Inputs

The two inputs on the Chromatic Adaptation node are the input and effect mask.

Input: The orange input connects the primary 2D image for the auto gain.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the adjustment to only

those pixels within the mask. An effect mask is applied to the tool after the tool is processed.

Basic Node Setup

The Chromatic Adaptation node, like many 2D image-processing nodes, receives a 2D image, such

as a Loader node or the MediaIn1 shown below. The output continues the node tree by connecting to

another 2D image-processing node or a Merge node.

A Chromatic Adaptation node applied to a MediaIn1 node


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Inspector

ACES Transform controls

Controls Tab

The Controls tab contains the primary controls necessary for adjusting the Chromatic Adaptation parameters.

Method

The Method pop-up menu provides a variety of different transform methods to choose from, defaulting

to CAT02. Each option in the Method pop-up menu uses different measurement datasets to create

individual CAT matrixes to guide this transformation. As a result, each method prioritizes different

levels of accuracy for different sets of colors. For example:

�CAT02 has a non-linear component that compensates for the tendency of extremely saturated

blues to go purple, a typical weakness of other methods. It usually gives the best result for the

widest variety of measured data sets and works best for emissive sources (displays) and dim

viewing environments.

�Bradford Linear is also a commonly used method, albeit one in which extremely saturated blues

will go purple during the transform. It works well for both emissive sources in dim environments

and for reflective sources (theater screens) and dark environments.

�Von Kries is one of the oldest methods in common use, although it’s also one in which extremely

saturated blues will go purple during the transform. This, as well as all other methods, are available

if you need to match work done in another image processing application.

NOTE: Be aware that all methods listed will match neutral colors perfectly; the only

differences lie in how different ranges of saturated color are transformed.

Source/Target Illuminant

You control this transformation by using pop-up menus to define the Illuminant Type of the source

(typically the color temperature the camera was set to) and that of the target that you want to

transform the image to. For both sets of controls, you can choose a Standard Illuminant from a list, a

Color Temperature via a slider, or CIE 1931 xy coordinate values. This image transform is extremely

precise because the image is first transformed from the Timeline Color Space to XYZ, and then it’s

transformed to match the LMS (long, medium, short) color space that models the cone response of the

human eye to colors lit by different illuminants.


Fusion Page Effects | Chapter 94 Color Nodes

FUSION

Current Color Space and Gamma

This node also takes into account the current color space and gamma of the clip, which default to

those set for the current timeline. If you wish to change these values, you can do so using the Color

Space and Gamma menus.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Color nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.