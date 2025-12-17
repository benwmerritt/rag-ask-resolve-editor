---
title: "Chapter 150"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 613
---

# Chapter 150

Using LUTs

Lookup Tables, also known as LUTs, are one of the most ubiquitous means of

creating, exchanging, and applying image processing operations there is for

purposes of color management, display calibration, look management, and general-

purpose processing of image color and contrast. DaVinci Resolve has robust

support for LUTs throughout its image processing pipeline.

Contents

What is a LUT?������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3406

Supported LUT Formats���������������������������������������������������������������������������������������������������������������������������������������������������������������� 3407

LUTs and ACES����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3408

Adding Lookup Tables of Your Own���������������������������������������������������������������������������������������������������������������������������������������� 3408

Custom LUT Paths����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3408

LUT Paths for the macOS App Store Version of DaVinci Resolve����������������������������������������������������������������������������� 3409

LUT Controls in the Project Settings��������������������������������������������������������������������������������������������������������������������������������������� 3409

Applying LUTs to Source Clips��������������������������������������������������������������������������������������������������������������������������������������������������� 3409

Using the Color Page LUT Browser������������������������������������������������������������������������������������������������������������������������������������������ 3410

Applying a LUT Within a Node���������������������������������������������������������������������������������������������������������������������������������������������������� 3412

LUTs Are the Last Operation Within a Node������������������������������������������������������������������������������������������������������������������������� 3412

Favorite LUTs Submenu in Node Editor������������������������������������������������������������������������������������������������������������������������������������ 3413

Missing LUTs������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3413

Exporting LUTs������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3413


Color | Chapter 150 Using LUTs

COLOR

What is a LUT?

LUTs are simply files, similar to plugins but far more focused and with no user interface, that specify

image processing operations. These operations are accomplished in a variety of ways. The traditional

approach is to use a 1D table or 3D “cube” of pre-calculated values to perform an image color

transform. However, newer LUT formats including CLF and DCTL let you use mathematical scripts to

process an image.

Whatever type of LUT you use, these files can be loaded into DaVinci Resolve and applied at different

points of the image processing pipeline to apply image processing operations for different purposes.

There are several well-known uses of LUTs, but the important thing you should take away is that LUTs

are simply color transform operations that can be used for many things, and there’s no single use of a

LUT that’s more or less important than any other.

Here are some frequent uses for LUTs:

•	 While optionally superseded by Resolve Color Management (RCM), lookup tables (LUTs)

have been frequently used to create a starting point adjustment for media acquired with

some logarithmic encoding. DPX log film scans, digital media using the ARRI ALEXA’s Log-C

encoding, Sony’s S-Log exposure setting, or RED R3D media that is debayered using the

REDFilmLog setting are all examples of media using a logarithmic exposure curve, designed

to protect as much detail in the highlights and shadows of a digitally encoded image as

possible. While log-encoded media retains a lot of image data, the picture is initially flat and

unsuitable for use without grading. The exposure and color must be adjusted to “normalize”

the media, making it look closer to the way it’s supposed to, in order to start grading. While

you can do this manually, it’s usually faster to use a LUT that’s tailored to your type of media

and the exposures you’re using. Alternately, you can also use Resolve Color Management to

accomplish this.

•	 LUTs are commonly used in onset workflows where dailies for different scenes are managed

with corresponding LUTs. These LUTs were used to monitor the media as it was being

recorded to define a baseline reference for how each scene is meant to look, at least so far

as field monitoring is concerned. In more advanced workflows, LUTs are used as a baseline

look, defined prior to the shoot and used during the shoot, that then defines the creative

starting point for different scenes once grading begins after the shoot.

•	 LUTs are frequently used as a stylistic component of a grade, or “look” that gives users a

quick start when desiring some manner of creative adjustment. Over the years, companies

and individuals have created an ecosystem of such looks that are disseminated and sold in

various LUT formats supported by DaVinci Resolve.

In all of these instances, LUTs are simply image processing adjustments that are applied to

affect the color and contrast of a clip, in much the same way as you’d make adjustments using

any of the contrast or color controls in the Color page.


Color | Chapter 150 Using LUTs

COLOR

Supported LUT Formats

DaVinci Resolve uses both 1D and 3D LUTs, and supports LUTs in a variety of formats.

�.cube: DaVinci Resolve uses both 1D and 3D LUTs in the .cube format. 3D LUTs can be exported

as 17x17x17, 33x33x33, or 65x65x65 cubes with 32-bit floating point processing. DaVinci Resolve

can also read and use Shaper LUTs in the .cube format, but these must also be created outside

of DaVinci Resolve. You should note that while 17-point LUTs are not recommended to use for

grading, they are useful when exporting LUTs for on-set monitoring, to accommodate different

display, calibration, and signal conversion devices.

�Panasonic VLUT format: DaVinci Resolve can both read and generate this LUT format, designed

for use in the Panasonic VariCam camera ecosystem.

�Video Range LUTs: Beginning with DaVinci Resolve 17, support was added for importing LUTs

that include additional metadata specifying them as processing image data in Video Range, rather

than Full Range. More information about how to format LUTs as Video Range is included in the

Developer Documentation available from the Help menu. Being able to specify whether a LUT is

meant to be Video or Full Range allows LUT processing to automatically accommodate DaVinci

Resolve’s data range setting pipeline for clip attributes, project settings, and output settings.

�CLF (common LUT format): CLFs use an XML format that is capable of encompassing a

limited number of mathematical transforms in addition to traditional lookup-tables to do image

processing. Promoted by the academy as the ideal LUT format for use with ACES, LMTs for ACES

are recommended to be in the CLF format due to its increased precision and flexibility.

�DCTL: DCTL files are actually color transformation scripts that DaVinci Resolve sees and applies

just like any other LUT. Unlike other LUTs, which are 1D or 3D lookup tables of values that

approximate image transformations using interpolation, DCTL files are actually comprised of

computer code that directly transforms images using combinations of math functions that you

devise. Additionally, DCTL files run natively on the GPU of your workstation, so they can be fast.

For more information on DCTL, see Chapter 200, “Creating DCTL LUTs.”

What’s the Difference Between a LUT and a Shaper LUT?

DaVinci Resolve is capable of importing and using LUTs within its 32-bit floating point image

processing pipeline. The .cube format can be used as either a simple 33x33x33 3D LUT, or as

a shaper LUT, which is actually a method of using two LUTs, a 1D LUT and a 3D LUT together,

that addresses signal processing issues that 3D LUTs alone can’t handle.

For processor efficiency, 3D LUTs are designed with reasonable lower and upper limits for the

data they will handle. It’s well known that when a 3D LUT is fed values that are outside of the

range that LUT is designed to handle, the out-of-range data will be clipped. Since many LUTs

are designed with digital cinema workflows in mind, the practical result is that feeding a video

signal with super-white in it to a 3D LUT that’s designed for full-range data (0–1) will clip the

super-white part of the signal.

Shaper LUTs handle this issue by first using a 1D LUT to process video signals with out-of-

range data, fitting the signal into a range that the 3D LUT won’t clamp. The output of the 3D

LUT includes the reverse transformation, to effectively zero out the 1D LUTs transform, while

retaining whatever processing the 3D LUT was meant to apply.


Color | Chapter 150 Using LUTs

COLOR

Shaper LUTs are also useful for dealing with extremely large data sets, such as OpenEXR files

that can theoretically handle an image data range of –infinity to +infinity. Using a Shaper LUT,

you can remap the incoming data to fit more precision in the 0–1 range, leaving less important

data outside the range.

LUTs and ACES

The academy that promotes the correct use of ACES strongly recommends that LUTs be processed in

the ACES color space. For this reason, two project settings let you choose how this will be done:

�ACEScc AP1 Timeline Space: This setting works for either the ACEScc or ACEScct Color Science

settings depending on what you’ve selected in the Color Science pop-up at the top of the Color

Management panel in the Project Settings. This setting lets you use LUTs that were created for

ACES workflows that are similar to (but not the same as) LUTs you would create and use in a

traditional log-encoded workflow. LUTs designed for working with this setting should have a range

of –0.358 to 1.468 so that grading operations that clip an image from 0 to 1 won’t destroy the look

being applied.

The “ACEScc AP1 Timeline Space” setting is also good for workflows where you want to use

conventional LUTs that were designed for Rec. 709 workflows using the ResolveFX “ACES

Transform” plugin, which over a series of three nodes lets you transform the image from ACES to

709, apply a Rec. 709-designed LUT, and then convert the image from 709 back to ACES.

�ACES AP0 Linear: This setting requires you to apply an LMT LUT that has been specifically

created for ACES image data. Only use this setting if you’re using CLFs that are designed for ACES

using a range of –65504 to 65504, as specified by SMPTE 2065.

Adding Lookup Tables of Your Own

The menus in the Color Management panel of the Project settings include a series of factory preset

LUTs that were installed with DaVinci Resolve, along with any LUTs that have been generated by

DaVinci Resolve, or that you’ve imported into the proper directory for your operating system for

your own use.

By default, LUTs are saved to the following locations:

On OS X: Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/

On Windows: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT

On Linux: /home/resolve/LUT

Custom LUT Paths

A list in the General panel of the DaVinci Resolve System Preferences lets you add multiple file paths

for loading LUTs that you want to use in DaVinci Resolve. This works for network volumes for facilities

where multiple workstations are accessing a central collection of LUTs to be shared among multiple

artists. Clicking the Add button lets you add a file path to this table from a dialog. Selecting a location

in this list and clicking Remove removes that location.


Color | Chapter 150 Using LUTs

COLOR

A list in the General panel of the System Preferences lets you add multiple locations

where LUTs you want to use from within DaVinci Resolve are located.

LUT Paths for the macOS App Store Version of DaVinci Resolve

If you downloaded the non-studio version of DaVinci Resolve from the Apple App Store, LUTs are

saved in a different location in order for DaVinci Resolve to remain totally self-contained. In this case,

you can click the Open LUT Folder button in the Lookup Tables panel of the Project Settings, to open

up a Finder window at the location these LUTs are stored. You can use this window to copy LUTs that

you want DaVinci Resolve to have access to, or delete LUTs that you no longer need.

If you add a LUT to one of these directories after DaVinci Resolve has been opened, you can click the

Update Lists button to refresh the contents of the pop-up menus.

LUT Controls in the Project Settings

While there’s an entire group of LUT controls in the Color Management panel of the Project Settings,

those are designed to apply LUTs, at different parts of the image processing pipeline, to the entire

Timeline. This is useful when you want to apply a single color and contrast transformation to the entire

program at once, but less so if you want to apply different LUTs on a per clip basis.

For more information on using the Lookup Table settings, see Chapter 4, “System and User

Preferences.”

Applying LUTs to Source Clips

Another way of applying a LUT to a clip is to apply it directly to the source clip, which you can do to

any clip in the Media Pool, or in the Thumbnail Timeline of the Color page. This can be convenient, but

keep in mind that source clip LUTs cannot be copied from one timeline to another using ColorTrace,

so using source clip LUTs limits your potential workflows. For most workflows, it’s better to apply LUTs

directly in the Node Editor so they live in each clip’s grade.


Color | Chapter 150 Using LUTs

COLOR

To apply a LUT to one or more selected clips in the Media Pool:

�Right-click one of the selected clips, and choose a LUT from the 1D LUT or 3D LUT submenus.

To apply a LUT to one or more selected clips in the Thumbnail Timeline of the Color page:

�Right-click one of the selected thumbnails, and choose a LUT from the 1D LUT or

3D LUT submenus.

TIP: If you’re wanting to apply an image transformation to normalize log-encoded source

clips, you may also consider using Resolve Color Management (RCM). Depending on your

source media, it may be an easier and more automated process.

For more information, see Chapter 9, “Data Levels, Color Management, and ACES.”