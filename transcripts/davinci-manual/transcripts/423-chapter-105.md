---
title: "Chapter 105"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 423
---

# Chapter 105

I/O Nodes

This chapter details the input and output of media using Loader and Saver

nodes within Fusion Studio as well as the MediaIn and MediaOut nodes in

DaVinci Resolve.

The abbreviations next to each node name can be used in the Select Tool dialog when

searching for tools and in scripting references.

Contents

Loader Node [Ld]������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2337

MediaIn Node [MI]����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2345

MediaOut Node [MO]����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2349

Saver Node [SV]��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2353

The Common Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2360


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

Loader Node [Ld]

The Loader node

Loader Node Introduction

NOTE: The Loader node in DaVinci Resolve is only used for importing EXR files.

When using Fusion Studio, the Loader node is the node you use to select and load footage from your

hard drive into the Node Editor. There are three ways to add a Loader node, and consequently a clip,

to the Node Editor.

�Add the Loader from the Effects Library or toolbar (Fusion Studio only), and then use Loader’s file

browser to bring a clip into the Node Editor

�Drag clips from an OS window directly into the Node Editor, creating a Loader node in the

Node Editor.

�Choose File > Import > Footage (Fusion Studio only), although this method creates a new

composition as well as adds the Loader node to the Node Editor.

When a Loader is added to the Node editor, a File dialog is displayed automatically to allow the

selection of a clip from your hard drives.

NOTE: You can disable the automatic display of the file browser by disabling Auto Clip

Browse in the Global > General Preferences.

Once clips are brought in using the Loader node, the Loader is used for trimming, looping, and

extending the footage, as well as setting the field order, pixel aspect, and color depth. The Loader is

arguably the most important tool in Fusion Studio.

Inputs

The single input on the Loader node is for an effect mask to crop the image brought in by the Loader.

Effect Mask: The blue input is for a mask shape created by polylines, basic primitive shapes, paint

strokes, or bitmaps from other tools. Connecting a mask to this input limits the loaded image to appear

only within the mask. An effects mask is applied to the tool after the tool is processed.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

Basic Node Setup

The Loader node is a 2D image of any format supported in Fusion Studio. It is limited to an EXR format

in DaVinci Resolve. Below, the LOADER imports an image, which is then masked using an Ellipse

matte. The output of the masked LOADER is passed onto 2D image-processing nodes.

A Loader node used for importing images

Inspector

Loader node File tab

File Tab

The File tab for the Loader includes controls for trimming, creating a freeze frame, looping, and

reversing the clip. You can also reselect the clip that the Loader links to on your hard drive.

Global In and Out

The Global In and Out handles are used to specify the position of this node within the project. Use

Global In to specify the frame on which that the clip starts and use Global Out to specify the frame on

which the clip ends within the project’s global range. The node does not produce an image on frames

outside of this range.

If the Global In and Out values are decreased to the point where the range between the In and Out

values is smaller than the number of available frames in the clip, Fusion automatically trims the clip

by adjusting the Trim range control. If the Global In/Out values are increased to the point where

the range between the In and Out values is larger than the number of available frames in the clip,

Fusion automatically lengthens the clip by adjusting the Hold First/Last Frame controls. Extended

frames are visually represented in the range control by changing the color of the held frames to green

in the control.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

To slide the clip in time or move it through the project without changing its length, place the mouse

pointer in the middle of the range control and drag it to the new location, or enter the value manually in

the Global In value box.

Filename

The Filename field shows the file path of the clip imported to the Node Editor by the Loader node.

Clicking on the Browse button opens a standard file browser. The path to the footage can also be

typed directly using the field provided. The text box supports filename completion. As the name of a

directory or file is typed in the text box, Fusion displays a pop-up that lists possible matches. Use the

arrow keys to select the correct match and complete the path.

NOTE: Loading image sequences is common practice for compositing, whether the image

sequence comes from a 3D renderer or a digital cinema camera. If the last part of a file’s

name is a number (not counting the file extension), Fusion automatically scans the directory

looking for files that match the sequence. For example, the following filenames would be

valid sequences:

image.0001.braw , image.0002.braw, image.0003.braw …

or

image151.exr , image152.exr, image153.exr …

The following would not be considered a sequence since the last characters are not numeric.

shot.1.fg.jpg, shot.2.fg.jpg, shot.3.fg.jpg

It is not necessary to select the first file in the sequence. Fusion searches the entire folder for

files matching the sequence in the selected filename. Also, Fusion determines the length of

the sequence based on the first and last numeric value in the filenames. Missing frames are

ignored. For example, if the folder contains two files with the following names:

image.0001.exr, image.0100.exr

Fusion sees this as a file sequence with 100 frames, not an image sequence containing

two frames. The Missing Frames drop-down menu is used to choose how Fusion handles

missing frames.

The Trim In/Trim Out control’s context menu can also be used to force a specific clip length or

to rescan the folder. Both controls are described in greater detail below.

Occasionally, you want to load only a single frame out of a sequence—e.g., a photograph

from a folder containing many other files as well. By default, Fusion detects those as a

sequence, but if you hold Shift while dragging the file from the OS window to the Node Editor,

Fusion takes only that specific file and disregards any sequencing.

Proxy Filename

The Proxy Filename control only appears once the filename control points to a valid clip. The Proxy

Filename can specify a clip that is loaded when the Proxy mode is enabled. This allows smaller

versions of the image to be loaded to speed up file I/O from disk, and processing. For example, create

a 1/4-scale version of an 8K EXR sequence to use as EXR proxy files. Whenever the Proxy mode of

the Composition is enabled, the smaller resolution proxy clip is loaded from disk, and all processing is

performed at the lower resolution, significantly improving render times. This is particularly useful when

working with large RAW plates stored on a remote file server. Lower-resolution versions of the plates

can be stored locally, reducing network bandwidth, interactive render times, and memory usage.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

The proxy clip must have the same number of frames as the source clip, and the sequence numbers

for the clip must start and end on the same frame numbers. It is strongly suggested that the proxies

are the same format as the main files. In the case of formats with options, such as Cineon, DPX, and

OpenEXR, the proxies use the same format options as the primary.

Trim

The Trim range control is used to trim frames from the start or end of a clip. Adjust the Trim In to

remove frames from the start and adjust Trim Out to specify the last frame of the clip. The values used

here are offsets. A value of 5 in Trim In would use the fifth frame in the sequence as the start, ignoring

the first four frames. A value of 95 would stop loading frames after the 95th.

Hold First Frame/Hold Last Frame:

The Hold First Frame and Hold Last Frame controls hold the first or last frame of the clip for the

specified amount of frames. Held frames are included in a loop if the footage is looped.

Reverse

Select this checkbox to reverse the footage so that the last frame is played first, and the first frame is

played last.

Loop

Select this checkbox to loop the footage until the end of the project. Any lengthening of the clip using

Hold First/Last Frame or shortening using Trim In/Out is included in the looped clip.

Missing Frames

The Missing Frames menu determines the Loader behavior when a frame is missing or is unable to

load for any reason.

�Fail: The Loader does not output any image unless a frame becomes available. Rendering

is aborted.

�Hold Previous Output: The last valid frame is held until a frame becomes available again. This fails

if no valid frame has been seen—for example, if the first frame is missing.

�Output Black: Outputs a black frame until a valid frame becomes available again.

�Wait: Fusion waits for the frame to become available, checking every few seconds. This is useful

for rendering a composition simultaneously with a 3D render. All rendering ceases until the

frame appears.

The Magic Comp Variable

Loaders and Savers use the absolute file paths for the location of media. However, if you are

using Fusion Studio, you can use a file path that is relative to the saved composition location.

The Comp variable works for Loaders and Savers and helps you to keep your work organized.

Entering Comp:\ in place of the full file path name is a shortcut for the folder where your Fusion

composition document is saved.

You can either enter the Comp:\ manually into the filename field of a Loader, or turn on

the Enable Reverse Mapping of Paths Preferences checkbox in the Path Map preferences.

Enabling the Path Map preference check box will use the Comp:\ automatically.

So as long as all your source footage is stored in subfolders of your Comp folder, Fusion finds

that footage regardless of the actual hard drive or network share name.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

You could, for example, copy an entire shot from the network to your local drive, set up your

Loaders and Savers to use the Comp variable, work all your magic locally (i.e., set up your

composition), and then copy just the composition back to the server and issue a net-render.

All render slaves automatically find the source footage.

Some examples:

Your composition is stored in:

X:\Project\Shot0815\Fusion\Shot0815.comp

Your source footage sits in:

X:\Project\Shot0815\Fusion\Greenscreen\0815Green_0000.dpx

The relative path in the Loader node would then be:

Comp:\Greenscreen\0815Green_0000.dpx

If your source footage is stored in:

X:\Project\Shot0815\Footage\Greenscreen\0815Green_0000.dpx

The relative path in the Loader node would then be:

Comp:\..\Footage\ Greenscreen\0815Green_0000.dpx

Observe how the two dots .. set the directory to go up one folder, much like CD .. in a

Command Shell window.

Import Tab

The Import tab includes settings for the frame format and how to deal with fields, pixel aspect, 3:2 pull

down/pull up conversion, and removing gamma curve types for achieving a linear workflow.

Loader Import tab


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

Process Mode

Use this menu to select the Fields Processing mode used by Fusion when loading the image. The

Has Fields checkbox control in the Frame Format preferences determines the default option, and the

default height as well. Available options include:

�Full frames

�NTSC fields

�PAL/HD fields

�PAL/HD fields (reversed)

�NTSC fields (reversed).

The two reversed options load fields in the opposite order and thus result in the fields being spatially

swapped both in time order and in vertical order as well.

Use the Swap Field Dominance checkbox (described below) to swap fields in time only.

Depth

The Depth menu is used to select the color depth used to process footage from this Loader.

The default option is Format.

�Format: The color depth is determined by the color depth supported in the file format loaded.

For example, JPEG files automatically process at 8 bit because the JPEG file format does not

store color depths greater than 8. EXR files load at Float. If the color depth of the format is

undetermined, the default depth defined in the Frame Format preferences is used. Formats that

support multiple color depths are set to the appropriate color depth automatically.

�Default: The color depth is determined by the settings in the composition’s Frame Format

Preferences panel.

�Int 8 Bit/Int 16 Bit/Float 16/Float 32: These options set the color depth for processing the image.

Pixel Aspect

This menu is used to determine the image’s pixel aspect ratio.

�From File: The loader conforms to the image aspect detected in the saved file. There are a few

formats that can store aspect information. TIFF, JPEG, and OpenEXR are examples of image

formats that may have the pixel aspect embedded in the file’s header. When no aspect ratio

information is stored in the file, the default frame format method is used.

�Default: Any pixel aspect ratio information stored in the header of the image file is ignored. The

pixel aspect set in the composition’s frame format preferences is used instead.

�Custom: Select this option to override the preferences and set a pixel aspect for the clip manually.

Selecting this button causes the X/Y Pixel Aspect control to appear.

Custom Pixel Aspect

This control is visible only when Custom is selected from the Pixel Aspect menu. Enter the desired

X and Y aspect or right-click on the control to display a menu of common frame formats and

their aspects.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

Import Mode

This menu provides options for removing pull-up from an image sequence. Pull-up is a reversible

method of combining frames used to convert 24 fps footage into 30 fps. It is commonly used to

broadcast NTSC versions of films.

�Normal: This passes the image without applying pull-up or pull-down 2:3.

�Pull Up: This removes existing 3:2 pull-down applied to the image sequence, converting from

30 fps to 24 fps 2:3.

�Pull Down: The footage has pull-down applied, converting 24 fps footage to 30 fps by creating

five frames out of every four. The process mode of a Loader set to Pull Down should always

be Full Frames.

First Frame

This menu appears when the Import Mode is set to either Pull Up or Pull Down. It is used to determine

which frame of the 3:2 sequence is used as the first frame of the loaded clip.

Detect Pull-Down Sequence

This button is used to detect and set the pull-up sequence of the footage automatically. It only works if

Pull-Up or Pull-Down is first selected from the Import Mode menu. If it succeeds in detecting the order,

the First Frame control automatically sets to the correct value.

Make Alpha Solid

When enabled, the original Alpha channel of the clip is cleared and set to solid white

(completely opaque).

Invert Alpha

When enabled, the original Alpha channel of the clip is inverted. This may also be used in conjunction

with Make Alpha Solid to set the Alpha to pure black (completely transparent).

Post-Multiply by Alpha

Enabling this option causes the color value of each pixel to be multiplied by the Alpha channel for

that pixel. This option can be used to convert subtractive (non-premultiplied) images to additive

(premultiplied) images.

Swap Field Dominance

When enabled, the field order (dominance) of the image is swapped, so the order in time the fields

appear is reversed. Unlike the Process Mode control, this is done without spatially swapping the

scanlines in the image

Color Space Type

This menu is used to set the Color Space of the footage to help achieve a linear color space workflow.

Unlike the Gamut tool, this doesn’t perform any actual color space conversion, but instead adds the

source color space data into the metadata, if that metadata doesn‘t already exist. The metadata can

then be used downstream by a Gamut tool with the From Image option, or in a Saver if explicit output

spaces are defined there.

�Auto: Passes along any metadata that might be in the incoming image.

�Space: Allows the user to set the color space based on the recording device used to capture

content or software settings used when rendering the content in another application.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

Curve Type

This menu is used to determine the gamma curve of the footage. Once the Gamma Curve Type is set,

you can choose to remove the curve to help achieve a linear workflow.

�Auto: Passes along any metadata that might be in the incoming image.

�Space: Allows the user to set the gamma curve based on the recording device used to capture

content or software settings used when rendering the content in another application.

�Log: Displays the Log/Lin settings, similar to the Cineon Log node.

For more information on the Log settings, see Chapter 99, "Film Nodes," in the

DaVinci Resolve Reference Manual and Chapter 39, in the Fusion Reference Manual.

Remove Curve

Depending on the selected Curve Type or on the Gamma Space found in Auto mode, the associated

Gamma Curve is removed from, or a log-lin conversion is performed on, the material, effectively

converting it to a linear output space.

Format Tab

The Format tab contains file format-specific controls that dynamically change based on the selected

Loader and the file it links to. Some formats contain a single control or no controls at all. Others like

Camera RAW formats contain RAW-specific debayering controls. A partial format list is provided below

for reference.

Format tab

�OpenEXR: EXR provides a compact and flexible format to support high dynamic range images

(float). The format also supports a variety of extra channels and metadata.The Format tab for

OpenEXR files provides a mechanism for mapping any non-RGBA channels to the channels

supported natively in Fusion. Using the Format tab, you can enter the name of a channel contained

in the OpenEXR file into any of the edit boxes next to the Fusion channel name. A command line

utility for dumping the names of the channels can be found at https://www.openexr.com.

�QuickTime: QuickTime files can potentially contain multiple tracks. Use the format options to

select one of the tracks.


Fusion Page Effects | Chapter 105 I/O Nodes

FUSION

�Cinema DNG: CinemaDNG is an open format capable of high-resolution raw image data with a

wide dynamic range. It was one of the formats recorded by Blackmagic Design cameras before

switching over to the BRAW format.

�Photoshop PSD Format: Fusion can load any one of the individual layers stored in the PSD file,

or the completed image with all layers. Transformation and adjustment layers are not supported.

To load all layers in a PSD file with appropriate blend modes, use File > Import > PSD.

Common Controls

Settings Tab

The Settings tab controls are common to both Loader and Saver nodes, so their descriptions can be

found in “The Common Controls” section at the end of this chapter.