---
title: "Chapter 96"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 395
---

# Chapter 96

Deep Image Nodes

This chapter describes Fusion’s Deep Image Nodes for

compositing objects in 3D space.

The abbreviations next to each node name can be used in the Select Tool dialog when searching for

tools and in scripting references.

For purposes of this document, node trees showing MediaIn nodes in DaVinci Resolve are

interchangeable with Loader nodes in Fusion Studio, unless otherwise noted.

Contents

Deep Image Compositing Toolset (Studio Version Only)������������������������������������������������������������������������������������������������ 2179

dCrop [dCr]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2179

Deep to Image [DtI]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2181

Deep to Points [DtP]�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2183

dHoldout [dHld]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2187

dMerge [dMg]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2189

dRecolor [dRc]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2190

dResize [dRz]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2191

dTransform [dXf]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2192

Image to Deep [ItD]���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2194

The Common Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2195


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Deep Image Compositing Toolset

(Studio Version Only)

Fusion supports a subset of tools to load, utilize, and save deep image data. Deep image data,

particularly in formats like OpenEXR, stores multiple samples per pixel to represent data for objects at

different depths in the same pixel. The Fusion Deep Image toolset can utilize this valuable information

to layer complex 3D renders, particularly where multiple objects overlap, and integrate them with

rendered 3D scenes.

The tools can be found in the Deep Image subcategory with a d-prefix.

Additionally:

•	 Renderer3D nodes can output deep image data.

•	 Loader and the MediaIn node can import deep image data EXRs.

•	 Saver can export deep image EXRs.

•	 All deep compositing tools (outside of Image to Deep and Deep to Image) can automatically

convert 2D image inputs to a deep image.

NOTE: Deep compositing requires a linear colorspace. Once merged, users can convert the

results into their desired colorspace.

dCrop [dCr]

The dCrop node

dCrop Node Introduction

This tool crops Deep Image samples using specified min and max depth values. It also crops pixels

with an input mask.

Inputs

The dCrop tool uses one input.

Input: This orange input is the only required connection. It is connected from a node with

deep image data.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps from other tools.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Basic Node Setup

The dCrop node receives the media in containing the deep image data. It then lets you refine the

depth boundaries with which to pass to the next tool.

dCrop accepts deep image data

Inspector

dCrop controls

Controls Tab

The Controls tab includes parameters for adjusting the amount of depth information to include or

exclude from being passed on the the rest of the node tree.

Depth Crop

Lets you crop the Z parameters of the deep image data.

�Use Minimum Z: Check this box to use a Minimum Z depth for the crop.

�Use Minimum Z: Adjust the Minimum Z amount using this slider.

�Sample: Click and drag from the sample button into the Viewer to choose a value.

�Use Maximum Z: Check this box to use a Maximum Z depth for the crop.

�Keep Outside Depth Range: Use this control to invert the cropped selection. After setting a

minimum and/or maximum value in the sliders above, this control flips the selection so that the

cropped region is now visible.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Image nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Deep to Image [DtI]

The Deep to Image node

Deep to Image Node Introduction

This tool converts deep data into a 2D image by flattening its depth samples. This outputs the deep

composite ready for traditional 2D compositing.

Inputs

The Deep to Image tool uses one input.

Input: This orange input is the only required connection. It is connected from a node

with deep image data.

Basic Node Setup

The Deep to Image node receives the media in containing the deep image data. It then flattens the

image for further use in normal 2D compositing.

Deep to Image accepts deep image data, flattens it, then

sends the 2D image down the node tree.

Inspector

Deep to Image controls

Controls Tab

The Controls tab includes parameters for adjusting the depth information.

�Flip Depth: Inverts the depth information.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

�Volumetric Composition: The Volumetric Composition option blends overlapping deep

samples as semi-transparent volumes rather than flat surfaces, simulating accurate interaction

through elements such as fog or VDBs. This results in a more realistic compositing of semi-

transparent elements.

Image Tab

The controls in this tab are used to set the resolution, color depth, and pixel aspect of the rendered

image produced by the node.

The Deep to Image Image tab

Process Mode

Use this menu control to select the Fields Processing mode used by Fusion to render changes to

the image. The default option is determined by the Has Fields checkbox control in the Frame Format

preferences.

Depth

The Depth menu is used to set the pixel color depth of the particles. 32-bit pixels require 4X the

memory of 8-bit pixels but have far greater color accuracy. Float pixels allow high dynamic range

values outside the normal 0…1 range for representing colors that are brighter than white or darker

than black.

Source Color Space

You can use the Source Color Space menu to set the Color Space of the footage to help achieve a

linear workflow. Unlike the Gamut tool, this doesn‘t perform any actual color space conversion, but

rather adds the source space data into the metadata, if that metadata doesn‘t exist. The metadata can

then be used downstream by a Gamut tool with the From Image option, or in a Saver, if explicit output

spaces are defined there. There are two options to choose from:

�Auto: Automatically reads and passes on the metadata that may be in the image.

�Space: Displays a Color Space Type menu where you can choose the correct color space of

the image.


Fusion Page Effects | Chapter 96 Deep Image Nodes

FUSION

Source Gamma Space

Using the Curve type menu, you can set the Gamma Space of the footage and choose to remove it by

way of the Remove Curve checkbox when working in a linear workflow. There are three choices in the

Curve type menu:

�Auto: Automatically reads and passes on the metadata that may be in the image.

�Space: Displays a Gamma Space Type menu where you can choose the correct gamma curve of

the image.

�Log: Brings up the Log/Lin settings, similar to the Cineon tool.

For more information, see Chapter 99, “Film Nodes,” in the DaVinci Resolve Reference Manual

or Chapter 39 in the Fusion Reference Manual.

Remove Curve

Depending on the selected Gamma Space or on the Gamma Space found in Auto mode, the Gamma

Curve is removed from, or a log-lin conversion is performed on, the material, effectively converting it

to a linear output space.

Pre-Divide/Post-Multiply

Lets you convert “straight” Alpha channels into pre-multiplied Alpha channels, when necessary.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Deep Image nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.