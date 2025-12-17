---
title: "Delivering HDR Vivid"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 53
---

# Delivering HDR Vivid

Once you’re finished grading the HDR and trimming the SDR downconversion, you need to output

your program correctly in the Deliver page.

Rendering an HDR Vivid Master

To deliver an HDR Vivid master after you’ve finished grading, you want make sure that the Output

Color Space of the Color Management panel of the Project Settings is set to the appropriate HDR

ST.2084 setting based on the peak output you want to deliver (any values above will be clipped).

Then, you want to set your render up to export an H.265 codec in the Video Settings, check the

Embed HDR Vivid Metadata box, and select the appropriate HDR mode that you used to grade the

master in the drop-down box below.

HDR Vivid settings in the Video section of the Deliver page

Hybrid Log-Gamma (HLG)

The BBC and NHK jointly developed another method of encoding HDR video, referred to as Hybrid

Log-Gamma (HLG). The goal of HLG was to develop a method of mastering HDR video that would

support a range of displays of different peak luminance capabilities without additional metadata, that

could be broadcast via a single stream of data, that would fit into a 10-bit signal, and that in the words

of the ITU-R Draft Recommendation BT.HDR, “offers a degree of compatibility with legacy displays by

more closely matching the previous established television transfer curves.”

The basic idea is that the HLG EOTF functions very similarly to BT.1886 from 0 to 0.6 of the signal

(with a typical 0–1 range), while 0.6 to 1.0 smoothly segues into logarithmic encoding for the highlights.

This means that, if you just send an HDR Hybrid Log-Gamma signal to an SDR display, you’d be able

to see much of the image identically to the way it would appear on an HDR display, and the highlights

would be compressed to present an acceptable amount of detail for SDR broadcast.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

On a Hybrid Log-Gamma compatible HDR display, however, the log-like highlights of the image (not

the BT.1886-like bottom portion of the signal, just the highlights) would be stretched back out, relative

to whatever peak luminance level a given HDR television is capable of outputting, to return the image

to its true HDR glory. This is different from the HDR10 method of distribution described previously, in

which the graded signal is referenced to absolute luminance levels dictated by ST.2084, and levels

that cannot be represented by a given display will be clipped.

And while this facility to support multiple HDR displays with differing peak luminance levels is

somewhat analogous to Dolby Vision’s ability to tailor HDR output to the unique peak luminance levels

of any given Dolby Vision-compatible television, HLG requires no additional metadata to guide how

the highlights are scaled, which depending on your point of view is either a benefit (less work), or a

deficiency (no artistic guidance to make sure the highlights are being scaled in the best possible way).

As is true for most things, you don’t get something for nothing. The BBC White Paper WHP 309 states

that, for a 2000 cd/m2 HDR display with a black level of 0.01 cd/m2, up to 17.6 stops of dynamic range

without visible quantization artifacts (“banding”) is possible. BBC White Paper WHP 286 states that

the proposed HLG EOTF should support displays up to about 5000 nits. So, partially, the backward

compatibility that HLG makes possible is due in part to discarding long-term support for 10,000 nit

displays. However, it’s an open question whether or not over 5000 nits is even necessary for

consumer enjoyment.

Sony, LG, Panasonic, JVC, Phillips, Hisense, Hitachi, and Toshiba have all either announced or

are shipping consumer HDR televisions capable of displaying HLG encoded video, and of course

DaVinci Resolve supports this standard through Resolve Color Management.

Grading Hybrid Log‑Gamma in DaVinci Resolve

Monitoring an ST.2084 image is as simple as getting a Hybrid Log-Gamma-compatible HDR display,

and connecting the output of your video interface to the input of the display.

Setting up Resolve Color Management to grade for HLG is identical to setting up to grade for Dolby

Vision, except that there are four HLG settings to choose from for the Output Color Space:

�Rec.709 HLG ARIB STD-B67

�Rec.2020 HLG ARIB STD-B67

�Rec.2100 HLG

�Rec.2100 HLG (Scene)

Optionally, if you choose to enable “Use Separate Color Space and Gamma,” you can choose either

Rec. 2020 or Rec. 709 as your gamut, and Rec. 2100 HLG as your EOTF.

The levels you’ll be monitoring in your scopes will be different from the table of data to nit values listed

previously for grading to the PQ EOTF.

Ouputting Hybrid Log-Gamma

Once you’ve created an HLG grade for your program, you can output it to any high-quality 10-bit

capable media format.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

Generate HDR Light Level Report

(Studio Version Only)

You can now generate HDR Light Level reports from the Media Pool. To do so, select a clip in the

Media Pool, right-click it and choose Generate HDR Report from the context menu. The tool will

prompt you to select a location to save the HDR Light Level report in .pdf format.

This tool analyzes all frames in rendered HDR clips and presents light level statistics, including MaxCLL

and MaxFALL. It also includes a snapshot of the frame containing the maximum luminance level with a

box highlighting the point where the maximum values were found.

An HDR Light Level report exported from DaVinci Resolve


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

Chapter 11

Image Sizing

and Resolution

Independence

DaVinci Resolve is a resolution-independent application. This means that, whatever

the resolution of your source media, it can be output at whatever other resolution

you like, and just about every size‑dependent effect in your project, text, windows

of grades, edit and input clip scaling, and other effects will scale appropriately to

match the new output resolution.

This also means that you can freely mix clips of any resolution, fitting 4K, HD, and SD clips into the

same timeline, with each scaling to fit the project resolution as necessary.

Your project’s resolution can be changed at any time, allowing you to work at one resolution, and

then output at another resolution. This also makes it easy to output multiple versions of a program at

different resolutions, for example, outputting 4K, HD, and SD sized versions of the same timeline.

Additionally, most controls that let you transform clips, either to push into a clip for creative intent, or

to pan and scan media of one format to fit better into a different output format, are smart enough to

always refer back to the source resolution when combining resizing operations to shrink, then enlarge

an image for various reasons as you work in the Cut, Edit, Fusion, and Color pages.

This chapter covers the relationship among the different sizing and transform controls found in DaVinci

Resolve, showing how they work together to intelligently manage the sizing of clips and effects

as you work.

Contents

About Resolution Independence������������������������������������������������������������������������������������������������������������������������������������������������� 283

Timeline Resolution���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 283

Mixing Clip Resolutions���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 284

Changing the Timeline Resolution����������������������������������������������������������������������������������������������������������������������������������������������� 284

You Can Use Separate Timelines to Output Different Resolutions������������������������������������������������������������������������������ 284

You Don’t Need Separate Timelines to Output Different Resolutions����������������������������������������������������������������������� 284

Using High Resolution Media in Lower Resolution Projects������������������������������������������������������������������������������������������� 285


Setup and Workflows | Chapter 11 Image Sizing and Resolution Independence

MEDIA

About Resolution Independence

If you only read one paragraph of this chapter, read this: Resolution Independence in DaVinci Resolve

means you can add clips to a timeline in any combination of resolutions to fit the project resolution you’ve

chosen to work at, and you can later output that timeline to as many other resolutions as necessary

in order to create multiple deliverables. When you do so, all effects and transforms will automatically

readjust themselves to match the sizing of each new timeline resolution, and most transforms are

calculated and processed using the full native resolution of the source media you’ve linked to that clip.

In short, what this means is that you can create multiple deliverables in multiple resolutions by

simply changing the timeline resolution or by using a lower resolution setting in the Deliver page

compared to the timeline resolution when you create a new job to render out, and every effect will be

the right size automatically.

Timeline Resolution

The timeline resolution is one of the most fundamental settings of your project, defining its frame size.

It’s found in the Master Settings panel of the Project Settings, where you can choose a predefined

resolution from the “Timeline resolution” drop-down menu, or you can type a custom resolution into

the X and Y fields below.

The project-wide Timeline Resolution parameters found in the Master Settings panel of the Project Settings window

Clip Source Resolution���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 285

Pixel Aspect Ratio (PAR)��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 285

Clip Resolution��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 285

The DaVinci Resolve Sizing Pipeline������������������������������������������������������������������������������������������������������������������������������������������ 286

“Super Scale” High Quality Upscaling (Studio Version Only)������������������������������������������������������������������������������������������ 286

Fusion Effects and Resolution�������������������������������������������������������������������������������������������������������������������������������������������������������� 287

Image Scaling����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 289

Edit Sizing in the Cut and Edit pages������������������������������������������������������������������������������������������������������������������������������������������ 293

Image Stabilization������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 294

Input Sizing on the Color Page������������������������������������������������������������������������������������������������������������������������������������������������������� 294

Node Sizing on the Color Page������������������������������������������������������������������������������������������������������������������������������������������������������ 294

Output Sizing on the Color Page��������������������������������������������������������������������������������������������������������������������������������������������������� 294

Output Blanking������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 295

Format Resolution on the Delivery Page��������������������������������������������������������������������������������������������������������������������������������� 295

Rendering Sizing Adjustments and Blanking������������������������������������������������������������������������������������������������������������������������ 296


Setup and Workflows | Chapter 11 Image Sizing and Resolution Independence

MEDIA