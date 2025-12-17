---
title: "Reading Clips into Fusion Studio"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 236
---

# Reading Clips into Fusion Studio

Once the Frame Format preferences are set, you usually begin to create a composite by reading in

source media. When Fusion reads in media, it doesn’t convert or move the original files; it simply reads

the files in place, from whichever storage volume they’re on. You are always dealing with the original

source files in their original location.

Source media is read into a comp using a Loader tool. Although there are other tools within Fusion

Studio that you can use to generate images like gradients, fractals, or text, each still image, image

sequence, or movie file must be added to your comp using a Loader tool.

Loader and Saver tools are

used to add media to Fusion

Studio and render it out.

To add media to your comp, do one of the following:

�Click Effects to open the Effects Library, and then select Tools > I/O > Loader.

�Click the Loader icon in the toolbar.

�Right-click over the Node Editor, and then choose Add Tool > I/O > Loader.

�Drag a file from an OS file browser window into the Node Editor.

If multiple files are dragged into the Node Editor, a separate Loader is added for each file. However,

if you drag a single frame from an image sequence, the entire series of the image sequence is read

into the comp using one Loader, as long as the numbers are sequential.

To add only one frame of an image sequence to your comp:

�Hold Shift while you drag a single frame from an image sequence into the Node Editor.

This comes in handy when you want to read in photographs from a digital camera that are

numbered sequentially.

A Loader represents any clip, image file, or graphic that you bring into Fusion. However, other types of

media can also be brought into Fusion Studio. Photoshop PSD files, SVG splines, and 3D models in the

Alembic, FBX, and OBJ format can be imported using the File > Import menu.

TIP: Using File > Import > Footage creates a new composition along with a Loader node for

the footage. The selected media is automatically used for the name of the composition.

For more information about the Loader node, see Chapter 105, “I/O Nodes,” in the DaVinci

Resolve Reference Manual or Chapter 45 in the Fusion Reference Manual.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Aligning Clips in a Fusion Studio Composition

When you add a clip into a composition, the resulting Loader node is added at frame 0 of the

composition. However, the vital portion of the clip you are interested in may not start until a few

frames or even seconds later. To ensure you can align the timing of each piece of media, each

Loader includes timing and trimming options in the Inspector. You can also hold the first or last frame

for a longer duration than the original media, and reverse or loop the clip to get more range for

your composition.

At the top of the Inspector are the Global In and Global Out settings. This range slider determines

when in your composition the clip begins and ends. It is the equivalent of sliding a clip along a track in

a Timeline. The Hold First Frame and Hold Last Frame dials at the bottom of the Inspector allow you to

freeze frames in case the clip is shorter than the composition’s global time.

Use the Global In/Out range slider to slide a clip in time

to have it appear at the correct time in a comp.

Below the filename in the Inspector is a Trim In and Out range slider. This range slider determines the

start frame and end frame of the clip. Dragging the Trim In will remove frames from the start of the clip,

and dragging the Trim Out will remove frames from the end of the clip.

Although you may remove frames from the start of a clip, the Global In always determines where in

time the clip begins in your comp. For instance, if the Loader has a Global In starting on frame 0, and

you trim the clip to start on frame 10, then frame 10 of the source clip will appear at the comp’s starting

point on frame 0.

Use the Trim In/Out to remove unnecessary

frames from the start or end of a clip.

Instead of using the Inspector to adjust timing, it is visually more obvious if you use the

Keyframes Editor. For more information on the Keyframes Editor and adjusting a clip’s time,

see Chapter 71, “Animating in Fusion’s Keyframes Editor,” in the DaVinci Resolve Reference

Manual or Chapter 9 in the Fusion Reference Manual.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Loader Node Inputs

Loader nodes have one Effects mask input and one output. In the case of the Effects mask input,

connecting a mask node such as a Polygon or B-Spline node automatically creates an alpha channel in

the Loader node.

TIP: If you connect a Mask node without any shapes drawn, that mask outputs full

transparency, so the result is that the image output by the MediaIn node is blank. If you want

to rotoscope over a MediaIn node, first create a disconnected Mask node, and with the Mask

node selected and the Media In node loaded into the viewer, draw your mask. Once the

shape you’re drawing has been closed, connect the Mask node to the MediaIn node’s input,

and you’re good to go.

Using Proxies for Better Performance

For increased performance, you can do one of two things:

�Generate smaller media files and write them to disk using Optimized Media in DaVinci Resolve

�Render out proxy files using Saver nodes in Fusion Studio

Both applications also allow you to generate proxies on-the-fly without rendering new files to

disk using the Proxy and Auto Proxy options in the transport controls area.

To enable the Proxy and Auto Proxy options, you can do one of two things, depending on the

version of Fusion you are using:

•	 In the Fusion page, right-click the empty area behind the transport controls to enable the

Proxy option.

Proxy and Auto Proxy options in the

transport controls right-click menu.

•	 In Fusion Studio, click the Proxy (Prx) button in the transport area to enable the

usage of proxies.

The Proxy option reduces the resolution of the images as you view and work with them.

Instead of displaying every pixel, the Proxy option processes one out of every x pixels

interactively. In Fusion Studio, the value of x is determined by right-clicking the Prx button

and selecting a proxy ratio from the drop-down menu. For instance, choosing 5 from the menu

sets the ratio at 5:1. In the Fusion page, the proxy ratio is set by choosing Fusion > Fusion

Settings and setting the Proxy slider in the General panel.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

The Proxy menu sets the ratio for

skipping pixels when processing.

The Auto Proxy button enables Fusion to interactively degrade the image only while adjustments are

made. The image returns to normal resolution when the control is released. Similar to the Prx button in

Fusion Studio, you can set the Auto Proxy ratio by right-clicking the APrx button and choosing a ratio

from the menu.

When a Loader node is selected, the Inspector includes a Proxy Filename field where you can specify

a clip that will be loaded when the Proxy mode is enabled. This allows smaller versions of the image

to be loaded to speed up file I/O from disk and processing. This is particularly useful when working

with high resolution files like EXR that might be stored on a remote server. Lower resolution versions

of the elements can be stored locally, reducing network bandwidth, interactive render times, and

memory usage.

The proxy clip that you create must have the same number of frames as the original clip, and if using

image sequences, the sequence numbers for the clip must start and end on the same frame numbers.

If the proxies are the same format as the original files, the proxies will use the same format options in

the Inspector as the originals.

Presetting Proxy Quality

When using Fusion Studio, rather than right-clicking over the Proxy button to set the proxy quality,

you can preset the standard and Auto Proxy quality in the Fusion Preferences window. The General

pane in the Preferences window includes sliders for both standard Proxy files and Auto Proxy files.

These sliders designate the default ratio used to create proxies when the Proxy and Auto Proxy modes

are turned on. These settings do not affect the final render quality.

TIP: Even though the proxies are being processed smaller than their original size, the viewers

scale the images so they refer to original resolutions.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

File Format Options

The Fusion interface in DaVinci Resolve and Fusion Studio display specific options for various file

formats in slightly different ways. Where Fusion Studio displays most file-specific options in the

Loader’s Format tab, the Fusion page in most cases displays these options in the main Image tab of

the MediaIn node. The only exception being the OpenEXR format. Its extensive options are displayed

in a separate tab even in the MediaIn node of the Fusion page. Not all file formats have options. Only

the DPX, OpenEXR, PSD, and QuickTime formats provide additional options when loaded.

DPX

The Format tab in Fusion Studio’s Loader node for DPX files is used to convert image data from

logarithmic to linear. These settings are often left in bypass mode, and the Log to Linear conversion is

handled using a Cineon Log node.

OpenEXR

The OpenEXR format provides a compact and flexible high dynamic range (float) format. The format

supports a variety of extra non-RGBA channels and metadata. These channels can be viewed and

enabled in the Format tab of the Inspector.

The Format tab in a Loader node Inspector

displays Aux channels in EXR files.

Photoshop PSD

There are two methods for importing Photoshop PSD files. You can either import the PSD file and have

it represented as a single node in the Node Editor or import the PSD and have each layer represented

as a node in the Node Editor. If you do not need independent control over each layer or blend modes

are not used when creating the PSD file, then importing the PSD file as a single node will make for

a more manageable experience. If you do need control over each layer or Blend modes used in the

PSD file are critical, then you should import the file so each layer becomes a node in the Node Editor.

Each method is explained below for the Fusion page and Fusion Studio.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Using the Media Pool in DaVinci Resolve’s Fusion page: Any PSD file added to the Media

Pool in DaVinci Resolve can be accessed from the Fusion page. After dragging the PSD file

from the Media Pool into the Node Editor, the image appears as a MediaIn node. From there,

you can select which layer to use from the PSD file from the Layer drop-down menu in the

Inspector.

Using a Loader node in Fusion Studio: This lets you read in Photoshop PSD files with

the ability to select the layer in the PSD file that is used in the comp. Fusion can load any

one of the individual layers stored in the PSD file, or the completed image with all layers.

Transformation and adjustment layers are not supported.

The Format tab in the Inspector displays

specific controls for a Photoshop PSD file.

To load all layers individually from a PSD file, with appropriate blend modes, do one of the following:

�In DaVinci Resolve, switch to the Fusion page and choose Fusion > Import > PSD.

�In Fusion Studio, choose File > Import > PSD.

Using either of the methods above creates a node tree where each PSD layer is represented by a

node and one or more Merge nodes are used to combine the layers. The Merge nodes are set to

the Apply mode used in the PSD file and automatically named based on the Apply mode setting.

The two layers of a Photoshop PSD file are imported and

connected to a Merge node set to a Screen Apply mode.

QuickTime

QuickTime files can potentially contain multiple tracks. You can use the Format tab in the

Inspector to select one of the tracks.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION