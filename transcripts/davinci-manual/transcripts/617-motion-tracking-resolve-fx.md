---
title: "Motion Tracking Resolve FX"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 617
---

# Motion Tracking Resolve FX

and Compatible OFX Plugins

When using Resolve FX in the Color page, Resolve FX that have position parameters, including Dent,

Lens Flare, Light Rays (when “From a Location” is selected), Mirrors, Radial Blur, Ripples, Vortex, and

Zoom Blur can all be motion tracked to follow the position of a moving subject in the frame using the

the easier and more reliable IntelliTrack mode (described below) or the legacy point-based tracking in

the FX mode of the Tracker palette.

To match move Resolve FX to a feature using the FX tracker:


Create a new node, and drag the Resolve FX filter you want to apply onto that node to apply

the effect. In this example, we’re adding a Lens Flare effect, that has the position parameters

necessary to be match moved to follow the motion of the shot, and we’re choosing the

MIR-I 2.8/37 preset, which looks like a sun.

Applying a Lens Flare to the shot


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR


If necessary, use the onscreen controls in the Viewer or the X Position and Y Position sliders to

move the Resolve FX effect to where you want it.

Moving the Lens Flare using the onscreen controls


Next, open the Tracker Palette and choose the fx icon in the upper right.

Opening the FX tracker mode of the Tracker palette


Click the Add Tracker Point button, at the bottom left-hand side of the Tracker palette, to add

tracker crosshairs to the center of the Viewer.

Adding a point tracker


Drag the crosshairs to a high-contrast detail (such as a small object or corner), and click the

Track Forward button. In this example, there’s a rock out at sea that will make a good plane

of motion for tracking a far-away sun. There is no inner or outer box to position or resize while

you do this; you just need to drag the crosshairs to center on the feature you want to track.


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR

Positioning the point tracker on a feature you want to track


Now, click the Track Forward button, and DaVinci Resolve will track the feature. The Resolve FX

applied to that node will simultaneously move to follow the track, and when the tracking is done,

you’re finished.

A successful track


After you’ve finished tracking, you can freely reposition the Resolve FX to offset it from the track.

For more information about single-point tracking, refer to the “Point Tracker Workflows”

section, see Chapter 140, “Motion Tracking Windows.”


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR

IntelliTrack AI Point Tracker (Studio Version Only)

The DaVinci Neural Engine powered IntelliTrack point tracker is available in the FX tracker in

DaVinci Resolve Studio. The IntelliTrack setting can be used for tracking your Resolve FX.

IntelliTrack, like other AI tools, doesn’t use predetermined rulesets or heuristics. Instead, it is trained

on real world examples. This makes it less likely to fail in scenarios like tracking a subject behind brief

occlusions. For most cases it will be more precise and more robust than the normal Point Tracker.

Using IntelliTrack: All the IntelliTrack analysis happens behind the scenes, and there is no

additional user input required other than to choose the IntelliTrack setting, set the tracking

crosshairs over high contrast areas on the same moving subject, and then press one of the

tracker direction controls.

Setting the IntelliTrack mode for the Color page window tracker


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR

Chapter 152

Sizing and

Image Stabilization

DaVinci Resolve has a powerful toolset for making geometric transforms,

using advanced algorithms for optical-quality sizing operations.

This section covers the nuts and bolts of resolution independence in DaVinci Resolve, and how to use

the Sizing palette. This chapter also covers how to use the Stabilizer mode of the Tracker palette to

subdue unwanted camera wiggle.

Contents

The Five Color Page Sizing Modes������������������������������������������������������������������������������������������������������������������������������������������ 3430

Sizing Order of Processing on the Color Page�������������������������������������������������������������������������������������������������������������������� 3430

Sizing Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3430

Blanking Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3431

Resetting the Sizing Palette���������������������������������������������������������������������������������������������������������������������������������������������������������� 3432

Input and Output Sizing Presets������������������������������������������������������������������������������������������������������������������������������������������������� 3432

Using Node Sizing for Channel and Paint Effects������������������������������������������������������������������������������������������������������������ 3433

Image Stabilization in the Tracker Palette���������������������������������������������������������������������������������������������������������������������������� 3435

Using the Stabilizer��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3435

Using the Classic Stabilizer������������������������������������������������������������������������������������������������������������������������������������������������������������ 3437

Using Stabilization to Create a Match Move����������������������������������������������������������������������������������������������������������������������� 3442


Color Page Effects | Chapter 152 Sizing and Image Stabilization

COLOR