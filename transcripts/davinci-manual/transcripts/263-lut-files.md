---
title: "LUT Files"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 263
---

# LUT Files

Any supported LUT files in the LUTs folder can be used by choosing them either from the LUT drop-

down menu or the viewer’s contextual menu. This includes 1D and 3D LUTs such as Fusion’s .lut, .alut

and .alut3 formats, as well as .cube, .shlut, .look, .3dl, and .itx formats. This is a convenient way to

access standard format LUT files for different projects.

Settings and Macros

Since LUTs are a form of color correction, you can also use any node, macro, or group of nodes as a

viewer LUT.

To use a node, group, or macro as a viewer LUT, do the following:


Select the node, group, or macro.


Right-click over the selected node, and then choose Settings > Save As from the menu.


In the file browser, go to the LUTs folder as set in Preferences > Global > Path Map > LUTS.


Click Save to save the .settings file.

This allows almost any combination of nodes to be used as a viewer LUT. This is the most flexible

approach but is also potentially the slowest. The LUT nodes must be rendered solely on the CPU,

whereas other methods are GPU-accelerated.

Setting a Default LUT

The default LUT applied when a new composition is created can be assigned in the Viewer panel of

the Fusion Settings window. Clicking the Enable Display LUT checkbox allows you to select a LUT from

the Display LUT plugins list.

The LUT default settings found in the View panel of the Fusion Settings window


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Viewer Preferences and Settings

The default settings for each viewer can be changed using the Viewer panel in the Preferences. The

position and size of each floating viewer can also be saved using the Layout menu in the Preferences.

Viewer Settings

It is often preferable to switch between entirely different viewer configurations while working.

For example, while keying, the image may be in the main viewer, and the alpha channel may be in a

subview. Viewer settings toward the end of a project may consist of the histogram, vectorscope, and

waveform, as well as the image in a view set to Quad view.

Fusion provides the ability to quickly load and save viewer settings to help reduce the amount of effort

required to change from one configuration to another.

To save a viewer setting, do the following:


Right-click over the viewer you want to save.


From the contextual menu, choose Setting > Save New.


Enter a name for the settings and click Save.

To load a viewer setting, do the following:


Right-click over the viewer you want to load a setting into.


From the contextual menu, choose Settings > filename.

Loading and Saving Defaults for a Viewer

The viewer can save new defaults and be returned to its defaults using the Load Defaults and the

Save Defaults options in the Settings portion of the View contextual menu.

The Viewer Options Menu

The Options menu of the viewer contains several ways you can customize the look and behavior of

the viewer. Many of these options are also in the viewer contextual menu.

Show Controls

When onscreen controls are not necessary or are getting in the way of evaluating the image, you can

temporarily hide them using the Show Controls option. This option is toggled using Command-K.

Checker Underlay

The Checker Underlay shows a checkerboard beneath transparent pixels to make it easier to

identify transparent areas. This is the default option for 2D viewers. Disabling this option replaces the

checkerboard with black.

Show Pixel Grid

Enabling this option will show a light black grid that outlines the exact boundaries of pixels in the

image when the image is scaled past a certain threshold. The default is Off.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Smooth Resize

The Smooth Resize option uses a smoother bilinear interpolated resizing method when zooming into

an image in the viewer. When Smooth Resize is disabled, scaling uses the nearest neighbor method

and shows noticeable aliasing artifacts but is more useful for seeing the actual pixels of the viewed

image when you zoom all the way down to a pixel level since there is no interpolation. This option is

enabled by default and can be toggled by clicking on the SmR button in the viewer toolbar.

Show Square Pixels

Depending on the frame format preferences and the type of footage loaded, many images may have

pixels that are rectangular instead of square. Both the NTSC and PAL video standards, as well as some

anamorphic film formats, use rectangular pixels. A computer monitor uses perfectly square pixels.

To compensate for this, aspect correction is automatically performed when viewing non-square pixels.

This prevents non-square pixel images from appearing squashed or stretched in the viewer.

You can enable the Show Square Pixels option to override the aspect correction. Show Square Pixels

can also be toggled on and off using the 1:1 button in the viewer toolbar.

Gain/Gamma

Exposes or hides a simple pair of Gain and Gamma sliders that let you adjust the viewed image.

Especially useful for “gamma slamming” a composite to see how well it holds up with a variety of

gamma settings. Defaults to no change.

360° View

Sets the Fusion page viewer to properly display spherical imagery in a variety of formats, selectable

from this submenu. Disable toggles 360 viewing on or off, while Auto, LatLong, Vert Cross, Horiz

Cross, Vert Strip, and Horiz Strip let you properly display different formats of 360º video.

Locking the Viewer (Command-L)

You can lock a viewer to prevent it from updating. The node that’s loaded into that viewer still

processes and the new image is queued for display in the viewer, but until you unlock it, the viewer

does not update. By default, the viewer is unlocked.

Additional Viewer Options

There are additional commands when you right-click anywhere within a viewer and choose from the

generically named Options submenu.

Alpha Overlay

When you enable the alpha overlay, the viewer will show the alpha channel overlaid on top of the

color channels. This can be helpful when trying to see where one image stops and another begins in a

composite. This option is disabled by default.

Overlay Color

When you turn the alpha overlay on, the default color is to show white for the area the alpha covers.

There are times when white does not show clearly enough, depending on the colors in the image.

You can change the color by choosing a color from the list of Overlay Color options.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Follow Active

Enabling the Follow Active option will cause the viewer to always display the currently active node in

the Node Editor. This option is disabled by default, so you can view a different node than what you

control in the Control Panel.

Show Controls

When onscreen controls are not necessary or are getting in the way of evaluating the image, you can

temporarily hide them using the Show Controls option. This option is toggled using Command-K.

Show Full Color Range

When working with floating-point images, you will occasionally need to visualize the values that fall

outside the normal luminance range. Enabling the Show Full Color Range option using the toolbar

button automatically normalize any image displayed in the viewer. Normalization causes the brightest

pixel in a color channel to be mapped to a value of 1.0 (white) and the darkest pixel to be mapped to

a value of 0.0 (black). Midrange values are scaled appropriately to fit within that range. It is also useful

when viewing Z-buffer or other auxiliary channels, which often use value ranges far different from

those in the color channels.

Show Labels

The Show Labels option lets you toggle the display of the text that sometimes accompanies onscreen

controls in the viewer without disabling the functions that are showing those overlays, and without

hiding the onscreen controls themselves.

Status Bar Information

The status bar at the bottom of the Fusion window provides the exact RGBA and Z values for the pixel

beneath the pointer when it’s hovering within one of the viewers. Additional information about the

X and Y coordinates of the cursor and the exact pixel position are also displayed.

The status bar showing coordinates and color information


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Chapter 70

Editing Parameters

in the Inspector

The Inspector is where you adjust the parameters of each node to do what needs

to be done. This chapter covers the various node parameters and methods for

working with the available controls.

Contents

Overview of the Inspector������������������������������������������������������������������������������������������������������������������������������������������������������������� 1433

The Tools and Modifiers Panels��������������������������������������������������������������������������������������������������������������������������������������������������� 1434

Customizing the Inspector������������������������������������������������������������������������������������������������������������������������������������������������������������ 1434

Inspector Height���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1434

Inspector Display Preferences����������������������������������������������������������������������������������������������������������������������������������������������������� 1435

Opening Nodes in the Inspector������������������������������������������������������������������������������������������������������������������������������������������������ 1436

Pinning Multiple Nodes in the Inspector��������������������������������������������������������������������������������������������������������������������������������� 1437

Hiding Inspector Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1438

Using the Inspector Header��������������������������������������������������������������������������������������������������������������������������������������������������������� 1438

Selecting and Viewing Nodes in the Inspector������������������������������������������������������������������������������������������������������������������� 1438

Using Header Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1439

Versioning Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1439

Parameter Tabs����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1440

The Settings Tab��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1440

Inspector Controls Explained������������������������������������������������������������������������������������������������������������������������������������������������������ 1444

Fusion Slider Controls���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1444

Thumbwheel������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1444

Range Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1445

Checkboxes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1445

Drop-Down Menus����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1445

Button Arrays���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1446

Color Chooser and Picker��������������������������������������������������������������������������������������������������������������������������������������������������������������� 1446

Modifiers���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1451


Fusion Fundamentals | Chapter 70 Editing Parameters in the Inspector

FUSION