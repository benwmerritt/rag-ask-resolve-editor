---
title: "DaVinci Remote Monitor Restrictions"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 759
---

# DaVinci Remote Monitor Restrictions

There are currently some limitations to the DaVinci Remote Monitor application to be aware of.

•	 When connecting over the internet, bandwidth restrictions can hamper performance.

If the bandwidth drops too low or cuts out completely, the Host will disconnect with an

error message.

•	 Currently DaVinci Remote Monitor only works in the Media, Cut, Edit, Color, and

Deliver pages.

•	 Currently Audio is limited to only 2 channels.


Project Libraries, Collaborative, and Remote Workflows | Chapter 198 Remote Grading and Remote Monitor

DELIVER

DELIVER

Advanced

Workflows

CONTENTS

199	 Workflow Integrations ������������������������������������������������������������������������������������������������������������������������� 4203

200	 Creating DCTL LUTs������������������������������������������������������������������������������������������������������������������������������� 4210

201	 TCP Protocol for DaVinci Resolve Transport Control���������������������������������������������������������������� 4215

Chapter 199

Workflow

Integrations

This chapter describes third party Workflow Integration and Codec plugins for

DaVinci Resolve.

Contents

DaVinci Resolve Renderer Plugin for OFX VFX Applications (Studio Version Only)�������������������������������������� 4204

Workflow Integrations in DaVinci Resolve (Studio Version Only)������������������������������������������������������������������������������ 4207

Creating Workflow Integration Plugins����������������������������������������������������������������������������������������������������������������������������������� 4207

Workflow Integration Plugins������������������������������������������������������������������������������������������������������������������������������������������������������ 4207

EditShare������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4207

Studio Network Solutions (SNS)������������������������������������������������������������������������������������������������������������������������������������������������� 4208

Codec Plugins (Studio Version Only)���������������������������������������������������������������������������������������������������������������������������������������� 4209

MainConcept���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4209


Advanced Workflows | Chapter 199 Workflow Integrations

DELIVER

DaVinci Resolve Renderer Plugin for

OFX VFX Applications (Studio Version Only)

The Open FX plugin DaVinci Resolve Renderer allows third-party applications to open and apply

DaVinci Resolve’s color changes using exported DRX stills. Essentially this turns an installation of

DaVinci Resolve Studio into one large OFX plugin. This can be very useful when round tripping

with various VFX authoring applications where you may want to maintain the exact look created in

DaVinci Resolve.

Exporting a DRX still contains much more information about the grade than a simple LUT. DRX files

can include data like all the native color and sizing palettes and other items you stored in a Gallery still.

This ensures that the grade the colorist created can be exactly replicated in the VFX software.

As of this writing, the following attributes WILL

transfer via the DaVinci Resolve OFX Renderer Plugin:

•	 All native color palettes (Primaries, HDR, Curves etc.).

•	 All native sizing palettes (Input, Output, Node etc.).

•	 Most Resolve FX.

•	 Most third-party Open FX.

As of this writing, the following attributes WILL NOT

transfer via the DaVinci Resolve OFX Renderer Plugin:

•	 Resolve and Open FX that are temporal based.

•	 Magic Mask.

To set up the DaVinci Resolve OFX Renderer Plugin:


When installing DaVinci Resolve Studio, select Custom Install and then check the plugin option in

the program installer.

Select Custom Install, then check DaVinci Resolve

Open FX Renderer to install the plugin


Advanced Workflows | Chapter 199 Workflow Integrations

DELIVER


Create your grade for a clip in the Color page, then save a still to the Gallery. From the Gallery,

export a .DRX file.


In the third-party application, apply the DaVinci Resolve Renderer plugin where appropriate for

your composition.

Inserting the DaVinci Resolve Renderer OFX into a Nuke node tree


In the DaVinci Resolve Renderer plugin in your application, choose the .DRX file you exported

from the file browser.

Select the .DRX file you exported from DaVinci Resolve in the plugin.

The Color Grade Plugin should work with most Open FX-capable VFX software, such as Autodesk

Flame and The Foundry’s Nuke.


Advanced Workflows | Chapter 199 Workflow Integrations

DELIVER

The DaVinci Resolve Renderer OFX Plugin in Nuke (below), showing a balanced grade with

green and orange Power Windows from multiple nodes in DaVinci Resolve (above).

IMPORTANT: Use of the plugin requires a DaVinci Resolve Studio license on the system that

is running the third party application.


Advanced Workflows | Chapter 199 Workflow Integrations

DELIVER