---
title: "Rendering Edit and Input Sizing Adjustments"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 726
---

# Rendering Edit and Input Sizing Adjustments

Whether or not sizing is rendered into your final media depends on the “Disable sizing and blanking”

checkbox in the Advanced Settings options of the Render Settings panel. You can disable sizing and

blanking either when rendering the current Timeline as a single clip, or when rendering individual clips.

If “Disable sizing and blanking output” is turned off: Output Blanking, Cut and Edit page

sizing adjustments, Color page Input and Output Sizing adjustments, and Image Stabilization

are rendered into the final rendered media using the optical-quality sizing algorithms available

to DaVinci Resolve. This is best if your sizing adjustments are approved and final, and you

want to “bake” sizing adjustments into the final media you’re delivering.

If “Disable sizing and blanking output” is turned on: Output Blanking, Cut and Edit page

sizing adjustments, Color page Input and Output Sizing adjustments, and Image Stabilization

are not rendered, and each clip will be rendered either at the source resolution if “Render at

source resolution” is enabled in individual clips mode, or to the currently specified resolution

of the Timeline or project. However, the sizing adjustments you’ve made will be exported as

part of the XML or AAF file that you’re exporting. This is best for workflows where the editor

wants to continue adjusting sizing after you’ve handed off the graded project relative to the

original size of the clips.

Keep in mind that if you want to render Input Sizing adjustments into the media you’re outputting, the

“Force sizing to highest quality” checkbox guarantees that DaVinci Resolve will use the highest-quality

sizing setting, even if you’ve temporarily chosen a faster-processing option for a slower computer.

NOTE: “Disable sizing and blanking output” does not disable any transform operations that

happen within the Fusion page, nor does it disable transforms happening as a result of an

Open FX or Resolve FX plugin applied to one or more clips in the Cut, Edit, or Color pages.

All of these effects will continue to be rendered into the final output.

Rendering Mixed Frame Rate Timelines

Mixed frame rates are supported by DaVinci Resolve when any option other then none is selected in

the “Mixed Frame Rate format” dropdown menu, either in the Conform Options section of the General

Options panel of the Project Settings, or in the Import AAF or XML dialog. When you choose the

appropriate option that corresponds to the application you’re exchanging projects with (or DaVinci

Resolve if you’re working entirely within DaVinci Resolve), then DaVinci Resolve conforms and

processes all clips in the Timeline to play at whichever frame rate is selected in the “Timeline frame

rate” dropdown menu. For example, 23.98, 29.97, 30, 50, 59.94, and 60 fps clips will all play at 24 fps if

that’s what “Timeline frame rate” is set to in the Master Settings panel of the Project Settings.

How clips in mixed frame rate timelines are rendered out depends on whether the Render Settings are

set to render Individual source clips or a Single clip.

�Individual source clips: All clips are rendered individually at their original frame rate.

�Single clip: All clips are converted to the “Timecode calculated at” frame rate and rendered

as a single media file. Clips are converted using whatever method is selected in the Retime

process dropdown of the Master Settings panel of the Project Settings, or in the individual Retime

process setting found in the Video inspector of each clip that overrides the project-wide setting.

You can choose Optical Flow processing for the highest quality conversion that’s available in

DaVinci Resolve.


Deliver | Chapter 185 Delivery Effects Processing

DELIVER

Export Alpha Channels in Individual Clips Mode

This option only appears if you’re rendering to a media format that supports alpha channels. If your

media contains an Alpha channel, you have the option to turn on the Export Alpha checkbox in the

Video panel of the render settings whenever you render individual source clips. When you do so,

DaVinci Resolve renders clips with alpha channels in either of two cases:

�Whenever there is an Alpha channel embedded in the source media for that clip, the embedded

Alpha channel will be copied to the rendered version of that clip.

�Whenever a clip’s grade has a key connected to an Alpha output, the Alpha output will be

rendered as an Alpha channel for that clip.

In either case, you may only render Alpha channels out when you render individual source clips to an

RGBA format such as TIFF, OpenEXR, ProRes 4444, ProRes 4444 XQ, or DNxHR 444.

Export Alpha Channels in Single Clip Mode

DaVinci Resolve allows rendering Alpha channels in Single Clip mode if the selected codec supports

an Alpha channel (i.e., ProRes 4444, DNxHR 444, etc.). This lets you apply a single Alpha channel to an

entire timeline for export, rather than just at the individual clip level.

To Render an Alpha Channel in Single Clip Mode:


Select “Single Clip” mode in the Render Settings.


Select a codec that supports an Alpha channel in the Video tab’s Codec and Type

selection boxes.


Select the checkbox “Export Alpha” that appears under the Frame rate selector.


If supported by the codec, you can chose the Alpha Mode type. Premultiplied is the default.

If the codec you have selected does not support an Alpha channel, the “Export Alpha” box will not

appear as an option.


Deliver | Chapter 185 Delivery Effects Processing

DELIVER

Chapter 186

Using the

Deliver Page

Once you’ve finished grading your project, you need to either render it, or output

it to tape to deliver it to your client. This is where the Quick Export window and

Deliver page comes in.

This chapter describes how to use Quick Export, how to use the overall interface of the Deliver

page, and provides some general information about how effects are output from DaVinci Resolve

in different situations.

Contents

Using Quick Export�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4025

Assign Icons to User Presets������������������������������������������������������������������������������������������������������������������������������������������������������� 4026

The Deliver Page������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4027

The Interface Toolbar���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4027

The Render Settings������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 4028

Rendering Files vs. Outputting to Tape��������������������������������������������������������������������������������������������������������������������������������� 4029

The Deliver Page Timeline����������������������������������������������������������������������������������������������������������������������������������������������������������� 4029

Filtering the Thumbnail Timeline������������������������������������������������������������������������������������������������������������������������������������������������ 4029

The Viewer�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4030

Disabling Viewer Updates While Rendering������������������������������������������������������������������������������������������������������������������������� 4031

The Render Queue���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4031

Drag to Reorder Jobs in the Render Queue������������������������������������������������������������������������������������������������������������������������� 4032


Deliver | Chapter 186 Using the Deliver Page

DELIVER

Using Quick Export

Not every situation requires a complicated delivery setup. When you just need to quickly export a

project, and the full power of the Deliver page is unneeded, you can choose File > Quick Export to

use one of a variety of export presets to export your program from any page of DaVinci Resolve. You

can even use Quick Export to export and upload your program to one of the supported video sharing

services, including YouTube, Vimeo, and Frame.io. You can also add your own presets to the Quick

Export window.

To use Quick Export:


(Optional) In the Cut, Edit, Fusion, or Color page, set In and Out points in the Timeline to choose

a range of the current program to export. If no timeline In or Out points have been set, the entire

timeline will be exported.


Choose File > Quick Export.


Select a preset to use from the top row of icons in the Quick Export dialog, and click Export.


Choose a directory location and enter a file name using the export dialog, then click Save.

A progress bar dialog appears to let you know how long the export will take.

The Quick Export Dialog showing a custom preset.

To Create a New Custom Preset and Add it to Quick Export:


On the Deliver page, select Custom Export from the Render Settings, and adjust the Video, Audio,

and File settings for your new preset. Only Single Clip settings can be made Custom Presets, not

Individual Clips.


In the Render Settings 3-dot option Menu, select Save as New Preset.


Type in a name for your new Preset, and choose a preset icon to represent it.


Check the Add to quick export box.


Click Save.

Your preset and icon will now be added to the Quick Export dialog across all pages of

DaVinci Resolve, and also be added to the Render Settings in the Deliver page.


Deliver | Chapter 186 Using the Deliver Page

DELIVER

The List View icon (circled) in the Quick Export dialog

To View the Quick Export Options in List View:


Open the Quick Export Dialog.


Click on the List View icon in the Render Settings.

Assign Icons to User Presets

When you create a new Custom Preset in the Deliver page, in addition to entering a name, you can

now choose an icon from the list to represent it in the Render Settings and Quick Export dialog.

Creating a new Custom Preset in the Deliver page


Deliver | Chapter 186 Using the Deliver Page

DELIVER