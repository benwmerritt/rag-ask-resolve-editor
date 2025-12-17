---
title: "Loading Audio WAV Files in Fusion Studio"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 237
---

# Loading Audio WAV Files in Fusion Studio

You can load WAV format audio-only files into Fusion Studio. The entire WAV file is loaded into RAM in

order to quickly display the waveform in the Keyframe Editor. That being the case, it is best to use the

shortest possible audio file you need for the Comp, so as not to use up more memory than necessary.

TIP: AIFF files can be loaded on macOS.

You can either load the audio file independent of any nodes, or load an audio file into the Saver node.

The benefit of using a Saver node to load the audio is that you can view the audio waveforms in the

Keyframes Editor.

To load a WAV audio file, do the following:


Right-click over the speaker icon and select Choose from the contextual menu.


In the file browser window, select the audio WAV file track to be used.

To load a WAV audio file using a Saver node, do the following:


Add a Saver node to the Node Editor.


In the Inspector, click the Audio tab and click the Browse button.


In the file browser window, select the audio WAV file track to be used.

To view the Audio Waveform in Fusion Studio, do the following:


Open the Keyframes Editor.


Expand the Saver track to view the audio waveform.

When you want to find the precise location of an audio beat, transient, or cue, you can slowly drag

over the audio waveform to hear the audio.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Chapter 66

Rendering Using

Saver Nodes

This chapter covers how to render compositions using Saver nodes in Fusion Studio and the

Fusion page in DaVinci Resolve. It also covers how to render using multiple computers over a network

when using Fusion Studio.

Contents

Rendering Overview������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1292

Rendering in the Fusion Page������������������������������������������������������������������������������������������������������������������������������������������������������ 1292

Rendering in Fusion Studio������������������������������������������������������������������������������������������������������������������������������������������������������������ 1292

Rendering with the Saver Node�������������������������������������������������������������������������������������������������������������������������������������������������� 1293

Setting Filenames for Export��������������������������������������������������������������������������������������������������������������������������������������������������������� 1294

Using the Render Settings Dialog��������������������������������������������������������������������������������������������������������������������������������������������� 1295

Render Settings Dialog Options�������������������������������������������������������������������������������������������������������������������������������������������������� 1296

Rendering Previews���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1297

Setting Up Network Rendering in Fusion Studio�������������������������������������������������������������������������������������������������������������� 1298

Licensing for Network Rendering����������������������������������������������������������������������������������������������������������������������������������������������� 1298

Configuring the Render Master and Render nodes����������������������������������������������������������������������������������������������������������� 1300

Setting Up the Render Manager��������������������������������������������������������������������������������������������������������������������������������������������������� 1301

Submitting Comps to Network Render����������������������������������������������������������������������������������������������������������������������������������� 1304

Using the Render Settings Dialog for Network Rendering ������������������������������������������������������������������������������������������� 1304

Using the Render Manager Window for Network Rendering �������������������������������������������������������������������������������������� 1304

Working with Node Groups����������������������������������������������������������������������������������������������������������������������������������������������������������� 1305

Viewing the Render Log������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1306

Using Third-Party Render Managers with Fusion Studio������������������������������������������������������������������������������������������������ 1306

Preparing Compositions for Network Rendering�������������������������������������������������������������������������������������������������������������� 1308

Using Relative Paths�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1309

Using Mapped Drives������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1310

Installing All Fonts on Render Nodes ��������������������������������������������������������������������������������������������������������������������������������������� 1310

Installing Third-Party Plugins on Render Nodes������������������������������������������������������������������������������������������������������������������ 1310


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Rendering Overview

When you have finished creating a composition in Fusion, you need to render the files out to disk

for playback and integration into a larger timeline. Fusion Studio and the Fusion page in DaVinci

Resolve use very different workflows for rendering. To finish a composite in the Fusion Page, you use

a MediaOut node to cache the results into the Edit or Cut page Timeline. The DaVinci Resolve Deliver

page handles the final render of the entire Timeline. To get completed composites out of Fusion

Studio, you configure and render them starting with a Saver node in the Node Editor. Fusion Studio is

also capable of distributing a variety of rendering tasks to other machines on a network.

Rendering in the Fusion Page

In the Fusion page, a MediaOut node is required for getting your composite from the Fusion page

back into the Edit or Cut page Timeline. Whatever the MediaOut node displays when you see it in

the viewer is what gets rendered back into the Edit or Cut page. This process is semi-automatic

in DaVinci Resolve, where the Smart Render Cache setting begins caching the MediaOut node

almost immediately when you return to the Edit or Cut page Timeline. The cache file format and any

resolution scaling to fit the composition into the Timeline Resolution is handled in the DaVinci Resolve

Project Settings.

Rendering in Fusion Studio

In Fusion Studio, all rendering goes through Saver nodes. Similar to MediaOut nodes in the Fusion

page, Saver nodes are most often appended to the end of a node tree to render the final composite.

The Saver node determines the name, format, and location of the rendered files.

Other Uses of Network Rendering����������������������������������������������������������������������������������������������������������������������������������������������� 1311

Flipbook Previews��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1311

Disk Cache������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1311

When Renders Fail�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1311

Automatic Rejoining of the Queue������������������������������������������������������������������������������������������������������������������������������������������������ 1311

Relaunching Render Nodes with Fusion Server������������������������������������������������������������������������������������������������������������������� 1312

Frame Timeouts������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1312

Heartbeats���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1313

Managing Memory Use�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1313

Override Composition Settings���������������������������������������������������������������������������������������������������������������������������������������������������� 1313

Render Several Frames at Once��������������������������������������������������������������������������������������������������������������������������������������������������� 1313

Simultaneous Branching������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1313

Limitations of Render Nodes��������������������������������������������������������������������������������������������������������������������������������������������������������� 1314

Time Stretching������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1314

Linear Tools��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1314

Saving to Multi-Frame Formats����������������������������������������������������������������������������������������������������������������������������������������������������� 1314

Troubleshooting����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1314

Checking the Render Log���������������������������������������������������������������������������������������������������������������������������������������������������������������� 1314

Check the Composition ������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1315


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Rendering with the Saver Node

To begin rendering in Fusion Studio, you must add at least one Saver node to the node tree. Most of

the time, you will place at least one Saver node at the very end of your tree to render the final image.

A single Saver node is added to the end of a node tree to render the final composite.

You can attach multiple Saver nodes anywhere along the node tree to render out different parts

of a composite. In the example below, three Saver nodes are added at different points in the node

tree. The top two render out each half of the composite while the bottom renders the results of

the entire composite.

Multiple Saver nodes can be added to different parts of a node tree.

You can also use multiple Saver nodes stemming from the same node in order to create several output

formats. The below example uses the three Savers to export different formats of the same shot.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Multiple Saver nodes can be added to create different formats for output.

Adding a Saver node to a node tree automatically opens a Save dialog where you name the file

and navigate to where the exported file is saved. You can then use the Inspector to configure the

output format.

For more information on the Saver node, see Chapter 105, “I/O Nodes,” in the DaVinci Resolve

Reference Manual or Chapter 45 in the Fusion Reference Manual.

Setting Filenames for Export

If you use a file extension when naming the file, Fusion will set the output format accordingly.

For example, naming your file image_name.exr will set the Inspector to output an EXR file or naming

a file image_name.mov will set the Inspector for an H264 QuickTime movie. If you decide to change

or modify the setting of the file type, the Saver’s format tab in the Inspector contains the specific

parameters for the selected format.

The Saver’s Format tab with controls for QuickTime


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

If you decide to output an image sequence, a four-digit frame number is automatically added before

the filename extension. For example, naming your file image_name.exr results in files named

image_name0000.exr, image_name0001.exr, and so on. You can specify the frame padding by

adding several zeroes to indicate the number of digits. For example, entering a filename as image_

name_000.exr results in a sequence of images with the names Image_name_000.exr, Image_

name_001.exr, Image_name_002.exr, and so on.

NOTE: The starting frame number always uses the Time Ruler start frame number.