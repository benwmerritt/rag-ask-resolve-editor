---
title: "Previewing and Trimming At Different Levels"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 51
---

# Previewing and Trimming At Different Levels

Additionally, the iCMU or eCMU can be used to preview 100 nit, 600 nit, 1000 nit, and 2000 nit versions of

your program, with different gamuts, if you want to see how your master will scale to those combinations

of peak luminance levels and standards. This, of course, requires your DaVinci Resolve workstation or

eCMU to be connected to a display that’s capable of being set to those peak luminance output levels.

Though it’s not at all typical, you also have the option to set the “Trim Controls For” drop-down menu

to different combinations of peak luminance, gamut, and color temperature, in order to visually trim

the grades of your program at up to four different peak luminance levels, including 100 nit, 600 nit,

1000 nit, and 2000 nit reference points. Choosing a setting from the “Trim Controls For” drop-down

menu sets you up to adjust trim metadata for that setting.

Choosing different settings from the “Trim Controls For” drop-down menu lets you can optimize a

program’s visuals for the peak luminance and color volume performance of many different televisions

with a much finer degree of control. If you take this extra step of doing a complete trim pass of your

program at multiple nit levels (using the Dolby Vision controls), the Level 2, or Level 8 metadata you

generate in each trim pass ensures that the artistic intent is preserved as closely as possible across a

wide variety of displays, in an attempt to provide the viewer with the best possible representation of

the director’s intent, no matter where it appears.

For example, if a program were graded relative to a 4000 nit display, along with a single

100 nit BT.709 trim pass, then a Dolby Vision-compatible television with 750 nit peak output

will reference the 100 nit trim pass metadata in order to come up with the best way of “splitting

the difference” to output the signal correctly. On the other hand, were the colorist to do three

trim passes, the first at 100 nits, -cond at 600 nits, and a third at 1000 nits, then a 750 nit-

capable Dolby Vision television would be able to use the 600 and 1000 nit trim metadata

to output more accurately scaled color volume and HDR-strength highlights, relative to the

colorist’s adjustments, that take better advantage of the 750 nit output of that television.

Managing Dolby Vision Metadata

As you go through the process of analyzing and trimming the HDR grades displayed on your Master

Display to look appropriate on your Target Display, you’ll sometimes find it useful to copy and paste

metadata from one clip to another. You can copy and paste Analysis Metadata separately from Trim

Metadata and Mid Tone Offset, and you can choose to copy and paste metadata for all Target Displays

when you’re trimming multiple passes, or you can copy and paste metadata for only the current Target

Display if you’re trimming multiple passes and you only want to overwrite metadata for a single pass.

Methods of Copying and Pasting Dolby Vision Metadata:

To copy and paste Analysis Metadata: Select a clip you want to copy from, choose Copy Analysis

Metadata from the Dolby Vision palette option menu, then select a clip you want to paste to, and

choose Paste Analysis Metadata from the Dolby Vision palette option menu.

To copy and paste Trim Metadata for all Target Displays: Do one of the following:

�Select a clip you want to copy from, choose Edit > Dolby Vision > Copy Trim Metadata, then select

a clip you want to paste to, and choose Edit > Dolby Vision > Paste Trim Metadata.

�Select a clip you want to copy from, choose Copy Trim Metadata from the Dolby Vision palette

option menu, then select a clip you want to paste to, and choose Paste Trim Metadata from the

Dolby Vision palette option menu.

�Select a clip you want to paste to, then press and hold the Option-Shift keys, and middle-click the

clip you want to copy from.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

To copy and paste Trim Metadata for the current Target Display: Do one of the following:

�Select a clip you want to copy from, choose Copy Trim Metadata from the Dolby Vision palette

option menu, then select a clip you want to paste to, and choose Paste Trim Metadata to Current

from the Dolby Vision palette option menu.

�Select a clip you want to paste to, then press and hold the Option key, and middle-click the clip

you want to copy from.

To copy and paste Mid Tone Offset: Select a clip you want to copy from, choose Copy Mid Tone

Offset from the Dolby Vision palette option menu, then select a clip you want to paste to, and choose

Paste Mid Tone Offset from the Dolby Vision palette option menu.

Setting Up Resolve Color Management for Grading HDR

Once the hardware is set up, setting up Resolve itself to output HDR for Dolby Vision mastering is easy

using Resolve Color Management (RCM). This procedure is pretty much the same no matter which

HDR mastering technology you’re using; only specific Output Color Space settings will differ.


Set Color Science to DaVinci YRGB Color Managed in the Color Management panel of the

Project Settings.


Then, open the Color Management panel, and set the Output Color Space drop-down to the

ST.2084 setting that corresponds to the peak luminance, in nits, of the grading display you’re

using. For example, if you’re grading with a Sony BVM X300, choose ST.2084 1000 nit, but if

you’re grading with a Flanders Scientific XM310K, choose ST.2084 3000 nit, in order to use the full

capabilities of each display. Be aware that whichever HDR setting you choose will impose a hard

clip at the maximum nit value supported by that setting. This is to prevent accidentally overdriving

HDR displays for which there are negative consequences (not all HDR displays have this limitation).

�ST.2084 300 nit

�ST.2084 500 nit

�ST.2084 800 nit

�ST.2084 1000 nit

�ST.2084 2000 nit

�ST.2084 3000 nit

�ST.2084 4000 nit

This setting is only the output EOTF (a sort of gamma transform, if you will, using the terminology

that DaVinci Resolve’s UI has used up until now).


Next, choose a setting in the Timeline Color Space that corresponds to the gamut you want

to use for grading, and that will be output. For example, if you want to grade the Timeline as

a log-encoded signal and “normalize” it yourself, you can choose ARRI Log C or Cineon Film

Log (this workflow is highly recommended for the best results). If you would rather save time by

having DaVinci Resolve normalize the Timeline to P3-D65 and grade that way, you can choose

that setting as well. In terms of defining the output gamut, the rule is that if “Use Separate Color

Space and Gamma” is turned off, the Timeline Color Space setting will define your output gamut.

If “Use Separate Color Space and Gamma” is turned on, then you can specify whatever gamut you

want in the left Output Color Space drop-down menu, and choose the EOTF from the right drop-

down menu (as described in step 2).


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA


Be aware that, when it’s being properly output, HDR ST.2084 signals appear very “log-like,” in

order to pack a wide dynamic range into the bandwidth of a standard video signal. It’s the HDR

display itself that “normalizes” this log-encoded image to look as it should. For this reason, the

image you see in your Color page Viewer is going to appear flat and log-like, even though the

image being displayed on your HDR reference display looks vivid and correct. If you’re using a

typical SDR computer display, and you want to make the image in the Color Page Viewer look

“normalized” at the expense of clipping the HDR highlights (in the Viewer, not in the grade), you

can use the 3D Color Viewer Lookup Table setting in the Color Management panel of the Project

Settings to assign the appropriate ST.2084 setting with a peak nit level that corresponds to the

HDR broadcast display you’re outputting to.


Additionally, the “Timeline resolution” and “Pixel aspect ratio” (in the project settings) that your

project is set to use is saved to the Dolby Vision metadata, so make sure your project is set to the

final Timeline resolution and PAR before you begin grading.

DaVinci Resolve Grading Workflow For Dolby Vision

Once the hardware and software is all set up, you’re ready to begin grading HDR. The workflow is

fairly straightforward.


First, grade the HDR image on your HDR Monitor to look as you want it to. Dolby recommends

starting by setting the look of the HDR image, to set the overall intention for the grade.


When using various grading controls in the Color page to grade HDR images, you may find it

useful to enable the HDR Mode of the node you’re working on by right-clicking that node in

the Node Editor and choosing HDR Mode from the contextual menu. This setting adapts that

node’s controls to work within an expanded HDR range. Practically speaking, this makes controls

that operate by letting you make adjustments at different tonal ranges, such as Custom Curves,

Soft Clip, and so on, work more easily with wide-latitude signals.


When you’re happy with the HDR grade, click the Analysis button in the Dolby Vision palette.

This analyzes every pixel of every frame of the current shot, and performs and stores a statistical

analysis that is sent to the iCMU or eCMU to guide its automatic conversion of the HDR signal to

an SDR signal.


Choose “Target Display Output” and “Trim Controls For” settings that you want to trim to.

By default, these are set to “100-nit, BT.709, BT.1886, Full,” which is a typical SDR deliverable.

However, other options are available if you want to do multiple trim passes to obtain a more

accurate result. Whichever setting you choose from, “Trim Controls For” dictates which trim pass

you’re doing. You can do multiple trim passes by choosing another option from this menu.


If you’re not happy with the automatic conversion, use the trim controls in the Dolby Vision palette

to manually trim the result to the best possible BT.709 approximation of the HDR grade you

created in step 1.


If you obtain a good result, then move on to the next shot and continue work. If you cannot obtain a

good result, and worry that you may have gone too far with your HDR grade to derive an acceptable

SDR tone mapping, you can always trim the HDR grade a bit, and then retrim the SDR grade to try

and achieve a better tone mapping. Dolby recommends that if you make significant changes to the

HDR master, particularly if you modify the blacks or the peak highlights, you should reanalyze the

scene. However, if you only make small changes, then reanalyzing is not strictly required.

As you can see, the general idea promoted by Dolby is that a colorist will focus on grading the

HDR picture relative to the 1000, 2000, 4000, or higher nit display that is being used, and will then

rely on the colorist to use the Dolby Vision controls to “trim” this into a 100 nit SDR version. This

metadata is saved as part of the mastered media, and it’s used to more intelligently tone map the

entire image to fit within any given display’s parameters. The colorist’s artistic intent is used to guide

all dynamic adjustments to the content.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

Delivering Dolby Vision

Once you’re finished grading the HDR and trimming the SDR tone mapping, you need to output your

program correctly in the Deliver page.

Rendering a Dolby Vision Master

To deliver a Dolby Vision master after you’ve finished grading, you want make sure that the Output

Color Space of the Color Management panel of the Project Settings is set to the appropriate HDR

ST.2084 setting based on the peak output you want to deliver (any values above will be clipped).

Then, you want to set your render up to use one of the following Format/Codec combinations:

�TIFF, RGB 16-bit

�EXR, RBG-half (no compression)

When you render for tapeless delivery, all Dolby Vision metadata is recorded into a Dolby Vision XML

and delivered along side either the Tiffs or EXR renders. To export a Dolby Vision XML file, select

your timeline in the media pool and choose File > Export >Timeline. Navigate to where you want to

save the file and select Dolby Vision v2.9 (or v4.0) MXF files from the file type selector and click save.

These two sets of files are then delivered to a facility that’s capable of creating the Dolby Vision

deliverable file.

Rendering a Dolby Vision IMF

You can deliver directly to an IMF that includes an MXF with embedded Dolby Vision metadata in the

package. To export a Dolby Vision IMF use the following Video settings in the Deliver page:

�Format: IMF

�Codec: Kakadu JPEG 2000

�Type: Dolby Vision (HD, 2K, UHD, or 4K) depending on your deliverable resolution.

Configure the rest of the IMF settings as necessary for your project.

The Video settings to use for creating a Dolby

Vision IMF in the Deliver page

Rendering a Dolby Vision H.265 file

You can deliver directly to a Dolby Vision compatible H.265 file, which allows you to playback video

that triggers playback in the Dolby Vision mode on your television or computer screen. To export a

Dolby Vision H.265 file, use the following Video settings in the Deliver page:

�Format: MP4 or QuickTime

�Codec: H.265

�Dolby Vision Profile: Set the Dolby Vision profile you wish to use, or None to select the

Tone Mapping manually.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

�Tone Mapping: Choose None for no tone mapping, or Dolby Vision to expose a list of common

deliverables to tone map to.

Configure the rest of the H.265 settings as necessary for your project.

The Dolby Vision Profile and Tone Mapping settings in

the H.265 Video section of the Deliver page

Rendering an Ordinary SDR Media File or Other Specific HDR Trim Pass

If you want to export the SDR trim pass, then you can choose Dolby Vision from the Tone Mapping

drop-down menu in the Advanced Settings of the Render Settings list on the Deliver page, and

choose the 100-nit, BT.709, BT.1886, Full setting below. With this enabled, you can output the SDR

version of your program to any format you like.

You can also export the trims for other HDR nit levels for specific displays, at 600, 1000 or 2000 nits

and in the either the BT.2020 or P3 gamuts.

The Tone Mapping setting in the Advanced Settings of the Render Settings list

SMPTE ST.2084 and HDR10

Many display manufacturers who have no interest in licensing Dolby Vision for inclusion in their

displays are instead going with the simpler method of engineering their displays to be compatible with

SMPTE ST.2084. It requires only a single stream for distribution, there are no licensing fees, no special

hardware is required to master for it (other than an HDR mastering display), and there’s no special

metadata to write or deal with.

Interestingly, SMPTE ST.2084 ratifies the “PQ” EOTF that was originally developed by Dolby, and

which is used by Dolby Vision, into a general standard that accommodates encoding HDR at peak

luminance values up to 10,000 cd/m2. This standard requires at minimum a 10-bit signal for distribution,

and the EOTF is mathematically described such that the video signal utilizes the available code

values of a 10‑bit signal as efficiently as possible, while allowing for such a wide range of luminance in

the image.

SMPTE ST.2084 is also part of the “Ultra HD Premium” industry specification, which stipulates that

televisions bearing the Ultra HD Premium logo have the following capabilities:

�A minimum UHD resolution of 3840 x 2160

�A minimum gamut of 90% of P3

�A minimum dynamic range of either 0.05 nits black to 1000 nits peak luminance (to accommodate

LCD displays), or 0.0005 nits black to 540 nits peak luminance (to accommodate OLED displays)

�Compatibility with SMPTE ST.2084


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

Finally, ST.2084 has been included in the HDR 10 standard adopted by the Blu-ray Disc Association

(BDA) that covers Ultra HD Blu-ray. HDR 10 stipulates that Ultra HD Blu-ray discs have the following

characteristics:

�UHD resolution of 3840 x 2160

�Up to the Rec. 2020 gamut

�SMPTE ST.2084

�Mastered with a peak luminance of 1000 nits

The downside is that, by itself, an HDR10 mastered program is not backward compatible with BT.709

displays using BT.1886 (although the emerging HDR10+ standard described later addresses this).

Furthermore, no provision is made to scale the above-100 nit portion of the image to accommodate

different displays with differing peak luminance levels. For example, if you grade and master an image

to have peak luminance of 4000 nits, and you play that signal on an HDR10-compatible television

(using ST.2084) that’s only capable of 800 nits, then everything above 800 nits will be clipped, while

everything below 800 nits will look exactly as it should relative to your grade.

This is because ST.2084 is referenced to absolute luminance. If you grade an HDR image

referencing a 1000 nit peak luminance display, as is recommended by HDR10, then any display using

ST.2084 will respect and reproduce all levels from the HDR signal that it’s capable of reproducing

as you graded them, up to the maximum peak luminance level it can reproduce. For example, on an

HDR10-compatible television capable of outputting 500 nits, all mastered levels from 501–1000 will be

clipped, as seen in the screenshot below.

Comparing the original 1000 nit waveform representing the grading monitor

to a 500 nit clipped waveform representing the consumer television


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

How much of a problem this is really depends on how you choose to grade your HDR-

strength highlights. If you’re only raising the most extreme peak highlights to maximum HDR-

strength levels, then it’s entirely possible that the audience might not notice that the display

is only outputting 800 nits worth of signal and clipping any image details from 801–1000

nits because there weren’t that many details above 800 anyway. Or, if you’re grading large

explosive fireballs up above 800 nits in their entirety because it looks cool, then maybe the

audience will notice. The bottom line is, when you’re grading for displays that are only capable

of ST.2084, you need to think about these sorts of things.