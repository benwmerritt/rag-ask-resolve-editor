---
title: "Using Viewer LUTs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 262
---

# Using Viewer LUTs

Viewer LUTs can be enabled, edited, and turned off using the viewer LUT button and menu, as well as

by using the viewer contextual menu. This menu shows all LUTs available to Fusion, including custom

LUTs you’ve installed yourself.

The viewer LUT button and menu from

the Fusion page in DaVinci Resolve

To turn the current viewer LUT on and off:

�Click the LUT button in the viewer toolbar to toggle the viewer LUT on and off.

�The LUT menu can also be found as a submenu in the viewer’s contextual menu.

To choose another viewer LUT:

�Open the menu to the right of the viewer LUT button and choose an option from the

viewer LUT menu.

To apply a Buffer LUT:


Right-click anywhere within the viewer and choose Global Options > Buffer LUT > Enable.


To choose a specific Buffer LUT, right-click again and choose a LUT from the Global Options >

Buffer LUT submenu.

Buffer LUTs are often useful for applying monitor corrections, which do not usually change

between projects.

To remove a Buffer LUT:

�Right-click anywhere within a viewer and choose Global Options > Buffer LUT >

Enable to uncheck it.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Editing Viewer LUTs

The viewers are the primary area where composites are assessed, so it’s crucial that they provide an

accurate representation of what the content will look like when it’s played for an audience. The LUT

Editor allows you to customize your viewer’s output to match the gamma and color characteristics of

your eventual playback device, or to test how the current image looks in a completely different color

space, or how it holds up over a range of different color spaces.

To open any editable viewer LUT option’s Editor:


Click the LUT button in the viewer toolbar to enable it.


Do one of the following:

�Choose Edit from the top of the viewer LUT menu.

�Right-click in the viewer and then choose LUT > Edit from the contextual menu.

Editing the Fusion View Lookup Table

Similarly to the Color Curves node, the Fusion View LUT Editor uses spline-based color correction.

In addition to the ability to modify the separate color channels, the LUT has Gain and Gamma sliders.

The Gain slider is helpful for temporarily brightening or darkening the viewed image, allowing easier

examination of shadow or highlight detail. The Color Gamma and Alpha Gamma sliders are used to

duplicate the gamma values of the eventual output device. Video monitors, for example, commonly

have a gamma of 1.7, while computer monitors can range anywhere from 1.6 to 2.2. Alpha Gamma is

applied only when viewing the alpha channel of an image, or when viewing masks.

The LUT Editor for the default Fusion View LUT

Editing the Gamut View LUT

The Gamut View LUT Editor lets you choose a Source and Output color space to guide the

viewer transform.

The Remove and Add Gamma checkboxes let you choose to do the gamut conversion with linear

or nonlinear gamma, or they let you simply remove or add the appropriate gamma values without

changing the color space.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Selecting the Pre-Divide/Post-Multiply checkbox will cause the image’s pixel values to be divided

by the alpha values prior to this conversion, and then re-multiplied by the alpha value after this

conversion. This helps to avoid the creation of illegally additive images, particularly around the edges

of a blue/green key or when working with 3D rendered objects.

The Gamut View LUT Editor

Editing the Log-Lin View LUT

The Log-Lin LUT lets you apply a Log to Lin or Lin to Log operation using the Mode pop-up menu. You

can choose the type of log-encoding to process from the Log Type drop-down, and choose whether

to lock the R, G, and B channels together. A level adjustment lets you redefine the digital range of

values used for the output, while Soft Clip (Knee), Film Stock Gamma, and Conversion Gamma sliders

let you further customize the color transform. Lastly, a Conversion Table field and Browse button let

you add an additional LUT as part of this operation.

The Log-Lin LUT Editor


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

LUT Processing Order

In elaborate workflows, facilities may apply multiple LUTs in a row before the image is seen. The order

of these is important since each LUT delivers different outputs. For instance, for a Cineon file in Log

color space you may often apply three LUTs. First a Log to Lin conversion, followed by a Fusion View

LUT to apply a color calibration, and a third one to correct it for display on an sRGB monitor, or replace

the last with a 3D DCP LUT if you are viewing on a projector.

When you select a node to be displayed, the image produced is processed before it is shown in the

viewers. The processing order is slightly different for 2D images and 3D scenes.

2D images first have the image LUT applied, and the result is composited over the checker underlay.

3D scenes are instead rendered with OpenGL.

Image

Output

Image LUTs

Macro LUTs

Fusion View LUT

Post Processing

Checker underlay

Dithering

Order of processing

Buffer LUT

(single)

Viewer

Output

The order of processing for 2D images and 3D scenes

For either 2D or 3D, the result may be drawn to an offscreen buffer where a Buffer LUT can be applied,

along with dithering, a full view checker underlay, and any stereo processing. The final result is then

drawn to the viewer and any onscreen controls are drawn on top.

Applying Multiple LUTs

The viewer contextual menu can be used to apply multiple image LUTs into a processing chain.

To apply an additional LUT, do the following:


Right-click anywhere within the viewer.


From the viewer’s contextual menu, choose LUT > Add New.


From the Add New submenu, choose a LUT to add.

To remove a LUT other than the first LUT, do the following:


Right-click anywhere within the viewer.


From the viewer’s contextual menu, choose LUT > Delete.


From the Delete submenu, choose a LUT to remove.

A complete stacked LUT configuration can be saved to and loaded from a .viewlut file, as

described below.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Saving Custom LUTs

There are a variety of ways to create and use different viewer LUTs in Fusion. You can save LUTs

when you save viewer settings, you can import LUTs that have been exported from Fusion or other

applications, and you can open any one of the various supported LUT file types. In addition, you can

use the standard nodes in Fusion to create macros, which can then be saved and used as a LUT.

LUT Settings

The most straightforward way to save a LUT you have created using the Fusion View LUT Editor is to

use the LUT > Save menu found in the viewer contextual menu. The settings are saved as an ASCII

file with the extension .viewlut in the LUTs folder. Any files with this extension found in that folder will

appear in the Image LUT menus for ease of loading. You can also load the settings that are not found

in the menu by choosing LUT > Load from the viewer’s contextual menu.

Using Viewer Settings

If you’ve modified a LUT, choosing Settings > Save New from the viewer’s contextual menu will save

all the viewer’s settings, including all LUT curves and gain/gamma values. You can save these under

different names, and each settings file can be reloaded at any time by choosing Settings > filename

from the viewer’s contextual menu. Choosing Save Default from the same menu will make these

settings the standard for all new comps.

Using LUT Curves

The Viewer LUT Edit dialog can be used to import and export LUT curves. You can export the LUT

curves as either ASCII or Saved format. The ASCII (.alut) file format is useful for sharing LUT curves

with other software, whereas the Saved (.lut) file format is preferred for Fusion, as it is more compact,

accurate, and allows further editing.

To export a LUT, do the following:


Click the viewer LUT button to enable it.


Click the viewer LUT menu, and then choose Edit.


Right-click on the LUT Curve Editor, and then choose Export LUT.


Select a LUT format at the bottom of the file browser window.


Enter a name for the LUT and click Save.

The Import LUT option will load LUT files back into the Curve Editor, or alternatively, if the file has been

saved in Fusion’s LUTs folder, it will appear in the LUT drop-down menu list.

TIP: This is one way to move LUTs between viewers or to and from the Color Curves node or

any other LUT Editor in Fusion.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION