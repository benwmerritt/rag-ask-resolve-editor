---
title: "Using Resolve Color Management"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 296
---

# Using Resolve Color Management

If you’re using the Fusion page within Davinci Resolve, you have the option of enabling DaVinci

Resolve’s scene-referred color management, instead of inserting Gamut and CineonLog nodes.

When DaVinci YRGB Color Managed (RCM) is enabled, the color of MediaIn nodes in the Fusion

page is handled differently. The RCM automatically determines the input color spaces of all files used

for all MediaIn nodes in the Fusion page, which then automatically get converted to linear gamma.

The MediaOut node then gets converted back into the Color Processing mode to get graded in the

Color page or further edited in the Edit page Timeline.

Despite the seeming complexity of color management, using RCM is actually simple. In essence, all

you have to do is (A) turn on RCM, and (B) choose the Color Processing mode and Output Color Space

combination you want to use.

To enable Resolve Color Management:


Open the Color Management panel of the Project Settings.


Choose DaVinci YRGB Color Managed from the Color Science drop-down menu.


Check the Automatic color management box for a simplified selection, or un-check the box to

adjust the Color Processing mode and Output color spaces manually.


Set the desired options for the Color Processing mode and Output Color Space RCM settings.

When DaVinci YRGB Color Managed is enabled, Timeline color space

is used for all MediaIn nodes in the Fusion page.

To override the input color space for differently recorded clips in the Media Pool:


Enable DaVinci YRGB Color Management as explained above.


Save and close the Settings dialog.


In the Media Pool, select the clip or clips you want to assign a new Input Color space.


Right-click one of the selected clips.


Choose the Input Color Space that corresponds to those clips from the contextual menu.

Using RCM eliminates a few steps, since the input color space math used to transform the source

preserves all wide-latitude image data, making highlights easily retrievable without any extra steps.

With RCM enabled, there is no need to insert CineonLog or Gamut nodes while in the Fusion page.

The transforms from and to linear are done automatically based on the RCM settings. Switching to

the Fusion page converts the images to linear and enables the LUT button in the viewers with the

Managed LUT selected. The Managed LUT uses the RCM settings to take a linear image and display it

based on the RCM output color space.


Fusion Fundamentals | Chapter 77 Managing Color for Visual Effects

FUSION

For more information on Resolve Color Management, see Chapter 9, “Data Levels, Color

Management, and ACES.”

Using ACES Color Management in Resolve

The ACES (Academy Color Encoding Specification) color space is another standard for managing

color throughout an entire production. It’s designed to make start-to-finish, scene-referred color

management a reality for digital cinema workflows. Just like DaVinci’s RCM, ACES makes it easier to

extract high-precision, wide-latitude image data from raw camera formats, to preserve high-quality

image data from acquisition through the color grading process and to output high-quality data for

broadcast viewing, film printing, or digital cinema encoding.

ACES works by assigning an IDT (Input Device Transform) to every camera and acquisition device.

The IDT specifies how media from that device is converted into the ACES color space. At the end of

the pipeline, an ODT (Output Device Transform) is applied to convert the image data from ACES color

space into the gamut of your final output.

Similar to setting up RCM, DaVinci Resolve’s color management project settings can be configured

for ACES, which carries through the Edit, Fusion, and Color pages.

NOTE: When using Fusion Studio, the OpenColorIO (OCIO) framework is used for ACES

color management.

The Color Science drop-down menu in the Color Management panel of the Project Settings is used to

set up the ACES color management in DaVinci Resolve.

When ACES is enabled, IDT and ODT are used to identify input and output devices.


Fusion Fundamentals | Chapter 77 Managing Color for Visual Effects

FUSION

�Color Science: Using this drop-down menu, you can choose either ACEScct or ACEScc color

science. This is primarily a personal preference since they are mostly identical, but the shadows

respond differently to grading operations. In the Fusion page, images are automatically converted

to linear, so whoever does the grading has more of a reason to choose one or the other.

ACEScc: Choose ACEScc color science to apply a standard Cineon style log encoding to the

ACES data before it is processed by DaVinci Resolve.

ACEScct: This variation of ACEScc adds a roll-off at the toe of the image to make color correction

lift operations “feel” more like they do with film scans and LogC encoded images.

�ACES Version: When you’ve chosen one of the ACES color science options, this menu becomes

available to let you choose which version of ACES you want to use.

�ACES Input Device Transform: This menu lets you choose which IDT (Input Device Transform)

to use for the dominant media format in use.

�ACES Output Device Transform: This menu lets you choose an ODT (Output Device Transform)

with which to transform the image data to match your required deliverable.

�Process Node LUTs In: This menu lets you choose how you want to process LUTs in the

Color page and does not affect the Fusion page.

�Disable tone mapping for Fusion conversion: Checking this box will remove any tone mapping

from the ACES color management.

For more information on ACES within DaVinci Resolve, see Chapter 9, “Data Levels, Color

Management, and ACES.”

Using OCIO for ACES

Color Management in Fusion

When using Fusion Studio or not using color management in DaVinci Resolve, you have the option to

use OpenColorIO nodes in Fusion to composite in an ACES color space.

OpenColorIO (OCIO) is an open-source color management framework for visual effects and computer

animation. OCIO is compatible with the Academy Color Encoding Specification (ACES). Three

OCIO nodes located in the Color category of the Effects Library allow you to use OCIO color space

transforms in Fusion.

OCIO CDL Transform node allows you to create, save, load, and apply a Color Decision

List (CDL) grade.

OCIO Color Space allows sophisticated color space conversions based on an OCIO config file.

OCIO File Transform allows you to load and apply a variety of LookUp Tables (LUTs).

Using OCIO for converting MediaIn or Loader nodes to linear gamma is based on the OCIO Color

Space node. Placing the OCIO Color Space node directly after a Loader (or MediaIn in DaVinci

Resolve) displays the OCIO Source and Output controls in the Inspector.

OCIO Color Space nodes can be used to work in an ACES color managed environment.


Fusion Fundamentals | Chapter 77 Managing Color for Visual Effects

FUSION

Within the Inspector for OCIO Color Space node, Fusion includes default Source and Output

transforms for standard color spaces. However, to use the full OCIO standard, you’ll need to download

and install the OCIO config file. You can download the config file from the OCIO website. https://

opencolorio.org

Clicking the Browse button in the Inspector will allow you to navigate to the downloaded config file.

From the download, locate the ACES 1.0.3 or later folder and select the file config.ocio.

Source and Output menus are populated based

on the config.ocio file that you download.

The Source menu is used to choose the color profile for your Loader or MediaIn node. The default raw

setting shows an unaltered image, essentially applying no color management to the clip. The selection

you make from the menu is based on the recording profile of your media.

The Output menu is set based on your deliverables. When working in Fusion Studio, typically the

Output selected is ACEScg, to work in a scene linear space.

Applying OCIO LUTs in the Viewer

The viewer also includes OCIO View LUTs to calibrate the viewers. Once the OCIO Color Space View

LUT is selected from the LUT menu above the viewer, choosing Edit for the same menu opens a dialog

where you can load the OCIO config file.

The OCIO Color Space View LUT is located in

the Viewer LUT menu in Fusion Studio.


Fusion Fundamentals | Chapter 77 Managing Color for Visual Effects

FUSION

By default, the same standard options are available in the View LUT. However, clicking the Browse

button allows you to load the same config file you loaded into the OCIO Color Space node. Once

loaded, all the expanded OCIO options are available. If you selected the OCIO Color Space node to

output ACEScg, you use the OCIO View LUT to go from a source setting of linear sRGB to an output

setting of sRGB or Rec. 709 in most cases.

The OCIO Color Space View LUT dialog is used to configure the

viewer when using the OCIO Color Space node in the Node Editor.

TIP: If your monitor is calibrated differently, you will need to select a LUT that matches your

calibration.

To set the LUT using OCIO:


Click the LUT menu and choose the OCIO Color Space View LUT.


From the same menu, select Edit.


In the View LUT editor that opens, set the source’s color space to lin sRGB


Set the output space to sRGB or REC 709, assuming you are viewing on a standard computer

monitor. You now see a normalized image in the viewer, but all color operations will be on

linear images.

Whether you use the OCIO Color Space LUT or a LUT for your specific monitor calibration, you can

save the viewer setup as the default.

To save the OCIO ColorSpace LUT setup as the default viewer setup:

�Right-click in the viewer, and then choose Settings > Save Defaults. Now, for every comp, the

viewer is preconfigured based on the saved defaults.


Fusion Fundamentals | Chapter 77 Managing Color for Visual Effects

FUSION