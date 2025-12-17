---
title: "Tips for Choosing Good Planes to Track"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 324
---

# Tips for Choosing Good Planes to Track

The region to track is specified by drawing a polygon on the reference frame. Make sure the

region selected belongs to a physically planar surface in the shot. Sometimes a region that is only

approximately planar can be used. In general, the less planar the surface, the poorer the quality of the

resulting track.

As a rule of thumb, the more pixels in the pattern, the better the quality of the track. In particular, this

means on the reference frame, the pattern to be tracked should:

�Be as large as possible.

�Be as much in frame as possible.

�Be as unoccluded as possible by any moving foreground objects.

�Be at its maximum size (e.g., when tracking an approaching road sign, it is good to pick a later

frame where it is 400 x 200 pixels rather than 80 x 40 pixels).

�Be relatively undistorted (e.g., when the camera orbits around a flat stop sign, it is better to pick

a frame where the sign is face on parallel to the camera rather than a frame where it is at a highly

oblique angle).

If the pattern contains too few pixels or not enough trackable features, this can cause problems with

the resulting track, such as jitter, wobble, and slippage. Sometimes dropping down to a simpler motion

type can help in this situation.


Fusion Fundamentals | Chapter 83 Planar Tracking

FUSION

Chapter 84

Using Open FX,

Resolve FX, and

Fuse Plugins

Fusion’s capabilities can be extended using different kinds of plugins.

All compositions in Fusion Studio and in the Fusion page of DaVinci Resolve

support third-party Open FX plugins.

Additionally, the Fusion page of DaVinci Resolve provides access to all of the Resolve FX that come

with DaVinci Resolve.

Lastly, you can develop your own plugins without using a computer development environment by

scripting Fusion’s native Fuse plugins.

Contents

What Are Open FX?�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1768

What Are Resolve FX?��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1768

Applying Open FX and Resolve FX Plugins������������������������������������������������������������������������������������������������������������������������� 1768

DaVinci Resolve OFX Renderer for Fusion Studio������������������������������������������������������������������������������������������������������������� 1769

Introduction to Fuse Plugins���������������������������������������������������������������������������������������������������������������������������������������������������������� 1771


Fusion Fundamentals | Chapter 84 Using Open FX, Resolve FX, and Fuse Plugins

FUSION

What Are Open FX?

Fusion is able to use compatible Open FX (OFX) plugins that are installed on your computer. Open FX

is an open standard for visual effects plugins. It allows plugins written to the standard to work on both

DaVinci Resolve and Fusion Studio as well as other applications that support the standard.

OFX plugins can be purchased and downloaded from third-party suppliers such as BorisFX, Red

Giant, and RE:Vision Effects. All OFX appear in the Open FX category of the Effects Library, alongside

all other effects that are available in Fusion.

What Are Resolve FX?

The Fusion page is DaVinci Resolve is also able to access Resolve FX. Resolve FX are filter effects

within DaVinci Resolve. Although most Resolve FX have the same capabilities on all DaVinci Resolve

pages, some are specific to the Color page and require the use of the Color page tracker for full

functionality. All Resolve FX appear in the Fusion page Effects Library in the Open FX category

alongside third-party OFX plugins. Resolve FX are not available in Fusion Studio.

For more information about Resolve FX, see Chapter 154, “Resolve FX.”

Applying Open FX and Resolve FX Plugins

Resolve FX and OFX plugins are applied to the Node Editor just as you would apply native Fusion

nodes. They can help you create fast, interesting looks and effects using the Color page, or

imaginative transitions and effects on your clips on the Edit page. Resolve FX are installed with

DaVinci Resolve,

After installing a set of OFX plugins, you can access them or Resolve FX plugins in Fusion by opening

the Open FX category in the Effects Library.

To add a plugin to the Node Editor, either click the Open FX or Resolve FX plugin name in the Effects

Library or drag and drop the plugin onto a connection line to insert it into the node tree. If the plugin

has editable settings, you can adjust these in the Inspector.


Fusion Fundamentals | Chapter 84 Using Open FX, Resolve FX, and Fuse Plugins

FUSION

DaVinci Resolve OFX Renderer

for Fusion Studio

You can use the OFX DaVinci Resolve Renderer plugin in Fusion Studio. This plugin allows Fusion

Studio to open and apply DaVinci Resolve’s color changes using exported DRX stills. Essentially this

turns an installation of DaVinci Resolve Studio into one large OFX plugin. This can be very useful when

round tripping between DaVinci Resolve Studio and Fusion Studio, where you may want to maintain

the exact look created in DaVinci Resolve.

Exporting a DRX still contains much more information about the grade than a simple LUT. DRX files

can include data like all the native color and sizing palettes and other items you stored in a Gallery still.

This ensures that the grade the colorist created can be exactly replicated in the VFX software.

As of this writing, the following attributes WILL transfer via

the DaVinci Resolve OFX Renderer Plugin:

�All native color palettes (Primaries, HDR, Curves, etc.).

�All native sizing palettes (Input, Output, Node, etc.).

�Most Resolve FX.

�Most third-party Open FX.

As of this writing, the following attributes WILL NOT transfer via the DaVinci Resolve OFX

Renderer Plugin:

�Resolve FX and Open FX that are temporal based.

�Magic Mask.

To set up the DaVinci Resolve OFX Renderer Plugin:


When installing DaVinci Resolve Studio, select Custom Install and then check the plugin option in

the program installer.

Select Custom Install, then check DaVinci Resolve

Open FX Renderer to install the plugin


Create your grade for a clip in the Color page, then save a still to the Gallery. From the Gallery,

export a .DRX file.


Fusion Fundamentals | Chapter 84 Using Open FX, Resolve FX, and Fuse Plugins

FUSION


In Fusion Studio, apply the DaVinci Resolve Renderer plugin where appropriate

for your composition.

ApplyRendererPluginFusion

Inserting the DaVinci Resolve Renderer OFX into a Fusion Studio node tree


In the DaVinci Resolve Renderer Inspector in Fusion Studio, choose the .DRX file you exported

from the file browser.

Select the .DRX file you exported from DaVinci Resolve in the plugin


Fusion Fundamentals | Chapter 84 Using Open FX, Resolve FX, and Fuse Plugins

FUSION