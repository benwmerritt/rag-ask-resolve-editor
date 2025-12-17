---
title: "ACES AMF 2.0"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 48
---

# ACES AMF 2.0

DaVinci Resolve supports ACES AMF 2.0 files for import and export. ACES AMF is a sidecar file written

in XML that defines the input and output transforms of the clip. This makes sure that the correct input

and output transforms are applied throughout the post production pipeline. These files can either

be loaded at a project level or a clip level. Clips with the “applied” attribute set to true are tagged

appropriately with no transforms applied. However, if they are set as false, the transform is applied

within DaVinci Resolve.

NOTE: You must use version 1.3 or above of the ACEScc or ACEScct Color Science to

use AMF files.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Working with AMF Files

Project level AMF: These will have all transforms applied. (i.e., any defined input, look, or output

transforms which have their “applied” attribute set to false will be applied.) The input and output

transforms are applied via the project settings “ACES Input Transform” and “ACES Output Transform”

menus, and these menus will display “From AMF” if they are using a transform from the loaded AMF file.

Clip level AMF:  An AMF can be loaded from the Color page clip thumbnail context menu from the

Clip AMF menu. This list is also populated from the ACES Transforms AMF subfolder. A clip-level AMF

will not apply the output transform; that can only be applied from project settings. Any input or look

transforms will have their “applied” attribute set to false. The look transforms are applied within a

compound node labeled AMF LMTs.

ACES Gamut Compression: If the ACES reference gamut compress algorithm is specified in a look

transform within the AMF, it will set the “Apply ACES reference gamut compress” checkbox to checked.

The user can see what input, gamut compress, look and output transforms are applied by clicking the

“View Transforms” button at the bottom of the “Color Space & Transforms” section of the Settings >

Color Management section.

To Import an AMF


Place your AMF files in the ACES Transforms/AMF directory on your computer. This is

folder is found:

�MacOS: the users Library/Application Support/Blackmagic Design/DaVinci Resolve/Aces

Transforms/AMF

�Windows: the users AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\ACES

Transforms\AMF

�Linux: opt/resolve/Developer/DaVinciCTL/AcesTransforms/AMF


In the Project Settings, set the Color Management > Color Science setting to ACEScc or ACEScct.


Select the ACES version to be 1.3 or above.


Click on the ACES AMF drop-down menu, and select the AMF from the list.

Exporting AMF Files

There are three choices to select from when you export an AMF file.

Source Master mode:

•	 All the applied attributes will be set to false.

•	 A source master is not associated with any clips or images.

Dailies Request mode:

•	 You can select the folder to store the output AMFs.

•	 A dailies AMF is created for and associated with each clip, and the applied attribute will be

set to false.

VFX Request mode:

•	 A VFX AMF will only have the input transform with the applied attribute set to false.


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

AMF Delivery Behaviors

�For AMF delivery, the export AMF option can be chosen in the Deliver page render settings.

�When using Source Master, the images are rendered to ACES AP0 or Linear masters with only the

input transforms applied; all other transforms are set to applied false.

�The resulting AMF is not associated with any clips or images with an aim to define and transmit a

color pipeline with its post production look alongside ACES AP0 or Linear data.

�In Dailies Request, all transforms are applied on the rendered images and all transforms are

set to applied true.

�The resulting AMF is associated with each clip in the project.

�In VFX Request, the clips are rendered to ACES AP0 or Linear with only the input transform

applied and all other transformed are set to false.

To Export an AMF


Right-click on your timeline in the Media Pool.


Select Timelines > Export > AMF in the contextual menu.


Choose the type of AMF file to export: Source Master, Dailies Request, or VFX Request.


Enter the name of the AMF file and its save location in the file browser.


Click on the Save button.

The Timeline Color Space in ACES Workflows is Fixed

When you’re working in ACES, you do not get to change the Timeline Color Space as you do in

Resolve Color Management. The ACES working color space is a log-encoded color space, which

encourages a more traditional, film-oriented approach to grading.

Tips for Rendering Out of an ACES Project

When choosing an output format in the Deliver page, keep the following in mind:

•	 If you’ve delivering graded media for broadcast, set the ACES Output Device Transform to

be Rec. 709, then you can output to whatever media format is convenient for your workflow.

•	 When you’re delivering graded media files to another ACES-capable facility using the

DCDM or ADX ODCs, you should choose the OpenEXR RGB Half (uncompressed) format

in the Render Settings, and set the ACES Output Device Transform to “No Output Device

Transform.”

•	 When you’re rendering media for long-term archival, you should choose the OpenEXR

RGB Half (uncompressed) format in the Render Settings, and set the ACES Output Device

Transform to “No Output Device Transform.”


Setup and Workflows | Chapter 9 Data Levels, Color Management, and ACES

MEDIA

Chapter 10

HDR Setup

and Grading

High Dynamic Range (HDR) grading for cinema, television, and streaming is the

latest evolution of the consumer media experience.While HDR workflows in

high‑end cinema and television aren’t new, this way of mastering media has been

slow to expand to less expensive programming.

However, new developments and an expanding array of affordable HDR-capable consumer devices

are poised to make HDR mastering of visual content increasingly ubiquitous.

This chapter describes what HDR is for the uninitiated and covers the operational details that will let

you set up DaVinci Resolve to do HDR grading.

Contents

High Dynamic Range (HDR) Grading in DaVinci Resolve������������������������������������������������������������������������������������������������ 254

HDR Isn’t Just for Televisions��������������������������������������������������������������������������������������������������������������������������������������������������������� 255

The Different Ways of Mastering HDR���������������������������������������������������������������������������������������������������������������������������������������� 255

What Do I Do With HDR?������������������������������������������������������������������������������������������������������������������������������������������������������������������� 256

Analyzing HDR Signals Using Video Scopes�������������������������������������������������������������������������������������������������������������������������� 256

Dolby Vision® ������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 258

Organizing Your Timeline for Dolby Vision Mastering�������������������������������������������������������������������������������������������������������� 260

Letterboxing for Dolby Vision Mastering���������������������������������������������������������������������������������������������������������������������������������� 260

Setting Up Color Management for Dolby Vision Mastering�������������������������������������������������������������������������������������������� 260

Choosing Mastering Displays for Dolby Vision����������������������������������������������������������������������������������������������������������������������� 261

Using the Dolby Vision Internal Content Mapping Unit (iCMU)��������������������������������������������������������������������������������������� 261

Simultaneous Master and Target Display Output for Dolby Vision������������������������������������������������������������������������������ 262

HDMI Tunneling using DeckLink 8K Pro G2���������������������������������������������������������������������������������������������������������������������������� 262

External Content Mapping Unit (eCMU) for Dolby Vision������������������������������������������������������������������������������������������������� 264

Auto Analysis is Available to All Studio Users������������������������������������������������������������������������������������������������������������������������ 264

Licensing DaVinci Resolve to Expose Dolby Vision Trim Controls������������������������������������������������������������������������������� 265

Dolby, Dolby Vision, and the double-D symbol are registered trademarks of Dolby Laboratories Licensing Corporation.


Setup and Workflows | Chapter 10 HDR Setup and Grading

MEDIA

High Dynamic Range (HDR)

Grading in DaVinci Resolve

The HDR features found in DaVinci Resolve are only available in DaVinci Resolve Studio.

High Dynamic Range (HDR) video describes an emerging family of video encoding and distribution

technologies designed to enable a new generation of television displays to play video capable of

intensely bright highlights and increased saturation. The general idea is that the majority of an HDR

image will be graded similarly to how a Standard Dynamic Range (SDR) image is graded now, with the

shadows and midtones being mostly the same between traditionally SDR and HDR-graded images.

This is mostly because shadows are shadows and are meant to be dark; however this philosophy

also maintains a comfortable viewing experience and easier backward compatibility when you need

to master both SDR and HDR versions of a program. The difference is that HDR provides abundant

additional headroom for very bright highlights and color saturation that far exceed what has been

previously visible in SDR television and cinema. This enables the colorist to create more vivid and

life‑like highlights in images, such as sunsets, lit clouds, firelight, explosions, sparkles, and other

intensely bright and colorful imagery. In short, you can now “open up” the highlights in an image just

Dolby Vision® Trim Controls in DaVinci Resolve�������������������������������������������������������������������������������������������������������������������� 265

Previewing and Trimming At Different Levels������������������������������������������������������������������������������������������������������������������������� 268

Managing Dolby Vision Metadata������������������������������������������������������������������������������������������������������������������������������������������������ 268

Setting Up Resolve Color Management for Grading HDR����������������������������������������������������������������������������������������������� 269

DaVinci Resolve Grading Workflow For Dolby Vision�������������������������������������������������������������������������������������������������������� 270

Delivering Dolby Vision���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 271

SMPTE ST.2084 and HDR10���������������������������������������������������������������������������������������������������������������������������������������������������������� 272

Monitoring and Grading to ST.2084 in DaVinci Resolve���������������������������������������������������������������������������������������������������� 274

Connecting to HDR-Capable Displays using HDMI 2.0a��������������������������������������������������������������������������������������������������� 274

HDR10+™����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 275

Monitoring and Grading to ST.2084 for HDR10+������������������������������������������������������������������������������������������������������������������� 275

HDR10+ Grading Workflow�������������������������������������������������������������������������������������������������������������������������������������������������������������� 275

Simultaneous Master and Target Display Output for HDR10+���������������������������������������������������������������������������������������� 275

HDR10+ Auto Analysis Commands���������������������������������������������������������������������������������������������������������������������������������������������� 276

Delivering HDR10+������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 276

HDR Vivid������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 277

Monitoring and Grading to ST.2084 for HDR Vivid�������������������������������������������������������������������������������������������������������������� 277

HDR Vivid Grading Workflow���������������������������������������������������������������������������������������������������������������������������������������������������������� 277

Simultaneous Master and Target Display Output for HDR Vivid����������������������������������������������������������������������������������� 277

HDR Vivid Trim Controls in DaVinci Resolve��������������������������������������������������������������������������������������������������������������������������� 278

Delivering HDR Vivid�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 279

Hybrid Log-Gamma (HLG)���������������������������������������������������������������������������������������������������������������������������������������������������������������� 279

Grading Hybrid Log‑Gamma in DaVinci Resolve������������������������������������������������������������������������������������������������������������������ 280

Ouputting Hybrid Log-Gamma������������������������������������������������������������������������������������������������������������������������������������������������������� 280

Generate HDR Light Level Report (Studio Version Only)��������������������������������������������������������������������������������������������������� 281


Setup and Workflows | Chapter 10 HDR Setup and Grading

MEDIA

as you’ve always been able to open up, or expand, the detail of the shadows. This not only provides

more life‑like lighting intensity and saturation, but it also dramatically expands the contrast available

in the scene. For example, a calibrated SDR display should have a peak luminance level of 100 nits

(cd/m2), but existing HDR displays can provide peak luminance levels of 700, 1000, or even 4000 nits.

However, because it’s an evolving technology, the technical standards that have been developed

far exceed what current consumer televisions, projectors, phones, and tablets are capable of. At the

time of this writing, consumer televisions are capable of outputting 700 to 1600 nits. Furthermore,

consumer displays are often saddled with automatic brightness limiting (ABL) circuits that limit power

consumption to acceptable levels for home use, which means that only a certain percentage of the

picture may reach these peak values at any one time. This is fine, because the point of HDR is not that

you’re making the entire image brighter, it’s that you have more headroom for specific bright highlights

and additional saturation.

For all of these reasons, HDR standards focus on describing what displays should be capable of, not

how these levels are to be used. That is a creative decision.