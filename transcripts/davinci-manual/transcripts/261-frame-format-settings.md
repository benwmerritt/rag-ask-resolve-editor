---
title: "Frame Format Settings"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 261
---

# Frame Format Settings

In the Frame Format panel of the Fusion Settings window (available in the Fusion menu), there are two

film guide settings that you can use to customize these guides.

�Guide 1 contains four fields that specify the offset from the edges of the image for the left,

top, right, and bottom guides, in that order. As with all offsets in Fusion, this is a resolution-

independent number where 1 is the width of the full image and 0.5 is half the width of the image.

�Guide 2’s text box is used to set the aspect ratio of the projection area.

The Frame Format Guides settings


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Domain of Definition and Region of Interest

As a compositing environment, the Fusion page uses the standard compositing conventions of Region

of Interest (RoI) and Domain of Definition (DoD) to dramatically improve performance.

Domain of Definition (DoD)

In compositing, the Domain of Definition, frequently abbreviated to DoD, refers to a rectangular region

that defines what part of an image actually contains data. DoD makes the concept of an image’s actual

frame somewhat flexible, since rendering is no longer limited to the actual width and height of the

image. This has two effects on the way Fusion renders images.

Firstly, nodes will no longer be required to render portions of the image that will not be affected by

the node. This helps the renderer to optimize its performance. Secondly, Fusion can now keep track of

and apply a node’s effect to pixels that lie outside the visible portion of the image.

For example, consider the output of a Text+ node rendered against a transparent background. The

text occupies only a portion of the pixels in the image. Without Domain of Definition, you would be

required to process every pixel in the image needlessly. With a DoD, you are able to optimize effects

applied to the image, producing faster results and consuming less memory in the process.

The following image shows an image with the DoD outlined.

The DoD is shown as two XY coordinates indicating the corners of an axis-aligned bounding box (in pixels)

For the most part, the DoD is calculated automatically and without the need for manual intervention.

For example, all the nodes in the Generator category automatically generate the correct DoD. For

nodes like Fast Noise, Mandelbrot, and Background, this is usually the full dimensions of the image. In

the case of Text+ and virtually all of the Mask nodes, the DoD will often be much smaller or larger.

The OpenEXR format is capable of storing the data window of the image, and Fusion will apply this as

the DoD when loading such an image through a Loader node and will write out the DoD through the

Saver node.

When using the Fusion page in DaVinci Resolve, clips from the Edit page timeline or Media Pool will

typically have the DoD default to the full image width of the source media. The exception is media

stored in OpenEXR format.

The DoD is established as soon as the image is created or loaded into the composition. From there,

it passes downstream, where viewers combine it with their Region of Interest in order to determine

exactly what pixels should be affected by the node. As you work, different nodes will automatically

shrink, expand, or move the DoD as they apply their effect to an image, causing the DoD to change

from node to node.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Showing the DoD

If the current DoD for a node is different from the frame size of that image, it’s shown in the tooltip that

appears when the pointer hovers over a node in the Node Editor. The DoD is also visible in the viewer

when you right-click in a viewer and choose Region > Show DoD from the contextual menu.

Setting the DoD Manually in the Node Editor

It is also possible to set the DoD for an image manually using the Tools > Miscellaneous > Auto Domain

node in the Effects Library. This node can be useful when dealing with pre-created media that does

not occupy the full image dimensions. For example, a rendering of a 3D character that walks toward

the camera will frequently occupy only a portion of the image. The Auto Domain node can be used to

animate a DoD that covers the character and ignores the rest of the image, making image processing

more efficient.

Region of Interest (RoI)

The Region of Interest, frequently abbreviated to RoI, is a rectangular region similar to the Domain of

Definition. However, unlike the DoD, which tells the node what pixels are actually present in the image,

the RoI tells the node which pixels actually need to be rendered. When a node renders, it intersects

the current RoI with the current DoD to determine what pixels should be affected.

Enabling RoI Controls

You can turn on the RoI controls to restrict rendering to a small region of the image to significantly

improve performance when you’re only working on a small part of a high-resolution or complex

composition. For example, if you’re using paint to clean up some holes in a matte on the floor of a

composition with many, many high-resolution layers, 3D, and Lighting operations, you can use the

RoI controls to isolate the part of the floor you’re working on, which makes caching that part of the

composition much faster.

To enable the RoI controls, do one of the following:

�Click the RoI button in the 2D Viewer toolbar.

�Right-click in a viewer and choose Region > Show Region from the contextual menu.

When RoI is enabled and Show Region is selected from the menu, a rectangular RoI control appears in

the viewer. If this is the first time RoI has been enabled, it will be set to the full width and height of the

image. Otherwise, the last known position of the RoI for that view is used. However, if you want to set

the RoI to a custom area within the frame, you can do one of the following.

To adjust the RoI controls, do one of the following:

�Drag any edge of the RoI rectangle to adjust one side of the RoI.

�Drag a corner to adjust the size of the RoI rectangle from that corner.

�Drag the small circle found at the top left corner of the RoI rectangle to move the RoI without

adjusting its dimensions.

Sometimes, it’s faster to simply draw a rectangle where you want the RoI to be.

To quickly draw the RoI at the desired size:


Choose Set from the viewer menu next to the RoI button, or right-click anywhere within the viewer

and choose Region > Set Region.


When the pointer turns into an RoI drawing cursor, drag within the viewer to set a RoI rectangle.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Alternatively, an Auto command sets the RoI to fit whichever pixels are visible at the current zoom/

pan level in the viewer. This lets you quickly limit the RoI to whatever part of the composition

you’ve zoomed into.

To automatically draw the RoI:

�Choose Auto from the viewer menu next to the RoI button.

�Right-click anywhere within the viewer and choose Region > Auto Region.

�When you no longer need to use the RoI, you can reset it.

To reset the RoI to the full width and height of the current image, do one of the following:

�Choose Reset from the viewer menu next to the RoI button.

�Right-click anywhere within the viewer and choose Region > Reset Region from the contextual

menu or from the toolbar button menu.

�Disable the ROI control, which will also reset it.

While the RoI Is Active

The RoI is only used for previewing your composition while you work, not for output from Fusion. While

the RoI is active, Fusion will only request rendering of the pixels inside the region when it displays an

image in that viewer. Flipbook Previews that you create in that viewer will also respect the current RoI.

MediaOut and Saver nodes will always use the full image dimensions when writing the image to disk,

ignoring any RoI you’ve set in the viewers.

The RoI improves not only rendering speed and memory use, but it can also reduce file I/O, since

Loaders and MediaIn nodes only load pixels from within the RoI, if one is specified. This does require

that the file format used supports direct pixel access. Cineon, DPX, and many uncompressed file

formats support this feature, as well as OpenEXR and TIFF in limited cases.

Please note that changes to the viewed image size or color depth will cause the pixels outside the RoI

to be reset to the image’s canvas color. This also happens when switching in and out of Proxy mode,

as well as during Proxy mode switching with Auto Proxy enabled. When the image size is maintained,

so are the last rendered pixel values outside the RoI. This can be useful for comparing changes made

within the RoI with a previous node state.

TIP: Right-clicking in a viewer and choosing Options >  Show Controls for showing onscreen

controls will override the RoI, forcing renders of pixels for the entire image.

Managing Viewer Lookup Tables (LUTs)

Lookup Tables, or LUTs, can be used to help match the appearance of a viewer to its eventual

output destination. They’re essentially image-processing operations that affect only the image being

previewed in the viewer, not the image data itself. There are two basic ways that LUTs can calculate

color transformations: The first is a simple 1D LUT, and the second is a more sophisticated 3D LUT.

�The simplest form of a LUT is a 1D LUT. It accounts for one color channel at a time, so it can make

overall tonality changes but not very specific color changes.

�A 3D LUT looks at each possible color value (red, green, and blue) independently. A 3D LUT

allows for large global changes as well as very specific color changes to be applied to images

very quickly.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

How Lookup Tables Work in Fusion

A Lookup Table (LUT) is a table of values used to transform the color and luminance of an image.

A 1D LUT uses a two-column table for input color and output color, while a 3D LUT uses more of a

matrix. A LUT is used primarily to correct for variances in the monitor or the source color space of the

image. You can choose to apply a LUT to all the viewers or apply different LUTs to each viewer.

Image LUTs

Image LUTs can be applied to each viewer. In fact, you can even apply separate Image LUTs for

the A and B buffers of a single viewer. These LUTs can only be applied to 2D images and not to

3D scenes. Image LUTs are routinely used to get from one scene-referred color space to another.

For example, if you’re working with log-encoded media but want to see how the image will look in the

final color space, you can choose a LUT to make the image transform as a preview.

Buffer LUTs

The Buffer LUT is applied to the viewers regardless of contents, including 3D scenes, 3D materials,

and subview types. Only one Buffer LUT can be applied. If a 2D image is being displayed with an

Image LUT applied, then the Buffer LUT is applied to the result of the image LUT. Buffer LUTs are

typically used to simulate another output color space that’s unique to the display you’re using—for

instance, making a DCI-P3 projector show the image as it would look on an sRGB monitor.

To use a Buffer LUT:


Disable the LUT button above the viewer.


Right-click in the viewer and choose Global Options > Buffer LUT > Enable.


Right-click in the viewer and choose Global Options > Buffer LUT > Type of LUT you want to apply.

When dealing with nonlinear files from many of today’s digital cinema cameras, a modern workflow

would be to convert everything to linear at the beginning of the node tree, then create your composite,

and then apply an Image LUT or Buffer LUT that matches the color space you want it to be in for either

grading in the Color page or for final output.

However, in more elaborate production pipelines, you may need to apply multiple LUTs consecutively.

Types of Viewer LUTs

Aside from the industry standard 1D and 3D LUTs, other types of LUTs are supported, including script-

based Fuse node LUTs, OCIO files, and macros assembled from standard nodes. Generally, LUT

processing is performed on the graphics card’s GPU in real time, although the performance of macro-

based LUTs is based on the nodes they contain.

Fusion View LUT

The Fusion View LUT is the default and is a frequently used LUT type. It provides an RGBA curve

that can be used to assign IN/OUT value pairs. This control is identical to that provided by the Color

Curve node.

Since the purpose of the View LUT is to provide an unchanging correction for the monitor or the file’s

color space, however, these splines cannot be animated.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Log-Lin View LUT

The Log-Lin LUT converts logarithmic data to linear, and vice versa. This can be particularly useful

when used in conjunction with supplied LUT files that expect logarithmic data. It is similar to the

Cineon Log node.

Gamut View LUT

The Gamut LUT converts a source color space to an output color space, with options to deal with

gamma settings, alpha channels, and premultiplication. The Gamut LUT is a frequently used LUT type

to correct the viewer when working with Linear Gamma in the Node editor.

Macro LUTs

Any macro node can also be used as a viewer LUT simply by saving the macro’s .setting file to the

correct Fusion directory.

In DaVinci Resolve, LUTs are saved in the following locations:

On macOS: Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/

Fusion/LUTs/

On Windows: C:\Program Files\Blackmagic Design\Fusion\LUTs

On Linux: home/username/.local/share/DaVinciResolve/Fusion/LUTs

In Fusion Studio, LUTs are saved in the following locations:

On macOS: Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/

Fusion/LUTs/

On Windows: C:\Users\username\AppData\Roaming\Blackmagic Design\Fusion\LUTs

On Linux: home/username/.fusion/BlackmagicDesign/Fusion/LUTs

For this to work, the macro must have one image input and one image output. Any controls

exposed on the macro will be available when the Edit option is selected for the LUT.

For more information about creating macros, see Chapter 68, “Node Groups, Macros, and

Fusion Templates,” in the DaVinci Resolve Reference Manual or Chapter 6 in the Fusion

Reference Manual.

LUT Presets

All LUTs available to DaVinci Resolve are also accessible to the Fusion page, which includes custom

LUTs you’ve installed, as well as preset LUTs that come installed with DaVinci Resolve, such as the

highly useful VFX IO category that includes a wide variety of miscellaneous to Linear and Linear to

miscellaneous transforms. All of these LUTs appear by category in the viewer LUT menu.

Fuse LUTs

Fuses are scriptable plugins that are installed with the application or that you create in Fusion. A fuse

named CT_ViewLUTPlugin can be applied as a LUT to a viewer. You can also script fuses that use

graphics hardware shaders embedded into the LUT for real-time processing. Since fuse LUTs require

shader-capable graphics hardware, they cannot be applied in software. For more information about

Fuses, see the Fusion Scripting Guide located on the Blackmagic Design website.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION