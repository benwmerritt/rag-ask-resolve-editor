---
title: "Organizing Your Timeline for Dolby Vision Mastering"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 50
---

# Organizing Your Timeline for Dolby Vision Mastering

One of the first things you need to do before doing a Dolby Vision grade is to organize your timeline

accordingly. Because each clip undergoes a visual analysis to facilitate the Dolby Vision workflow,

there are specific limitations to how clips can appear in a timeline.

�All clips to be analyzed in a Dolby Vision workflow need to be on video track V1; clips on other

tracks will be ignored.

�All clips that overlap one another as part of a composite must be turned into a single item in

the timeline in order to be correctly analyzed. This means that each group of clips that create

a composite in a timeline, be it multiple overlapping clips combined via keys or alpha channel

transparency, multiple overlapping clips combined using composite or blend modes, or text

generators appearing above one or more video clips, must be turned into a compound clip for

Dolby Vision analysis to work correctly.

Letterboxing for Dolby Vision Mastering

The analysis of clips in a Dolby Vision workflow keeps track of the timeline aspect ratio, as well as the

image aspect ratio of each clip in that timeline. Programs that mix different aspect ratios of letterboxing

(or blanking) will be accommodated by the Dolby Vision analysis, however Dolby Vision does not

support letterbox on two sides (both pillarbox and letterbox), only one at a time.

Setting Up Color Management for Dolby Vision Mastering

For an HDR signal to look correct, you need to output your graded program using the right EOTF for

the HDR standard you’re mastering. The EOTF maps the different levels DaVinci Resolve outputs to

your HDR display using the SMPTE ST.2084 PQ setting required for outputting Dolby Vision. You can

set this up in one of three different ways, as:

�Output Color Space and Gamma settings in RCM or ACES

�Color Space and Gamma settings within a series of Resolve FX Color Transform plugins that can

be used at the end of each grade or at the end of a Timeline grade

�3D LUTs used for converting signals from one standard to another that can be used at the end of

each grade or at the end of a Timeline grade

While Dolby Vision content is not limited to a particular color space, Resolve Color Management

provides a P3 D65 setting that matches the capabilities of most mastering displays in use at the time of

this writing.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

Choosing Mastering Displays for Dolby Vision

To do HDR grading, you need a suitable HDR display. Technically any monitor that supports SMPTE

ST.2084 (aka PQ) will work. Happily, a growing number of professional displays from Sony, Flanders

Scientific, TV-Logic, Canon, and Eizo are suitable for use in HDR grading suites. EBU Tech 3320

specifies the requirements for a Grade 1 HDR mastering monitor. Dolby recommends the following

minimum requirements for HDR monitors:

�A minimum Peak Luminance of 1000 nits

�A 200,000:1 contrast ratio

�Minimum black at 0.005 nits

�Capable of at least 99% of P3 gamut

For more information on Dolby best practices for color grading Dolby Vision, visit:

https://www.dolby.com/us/en/technologies/dolby-vision/dolby-vision-for-creative-

professionals.html.

Using the Dolby Vision Internal Content Mapping Unit (iCMU)

DaVinci Resolve has a GPU-accelerated “internal” software version of the Dolby Vision CMU (Content

Mapping Unit) for previewing Dolby Vision mapping right in DaVinci Resolve. iCMU support can be

enabled and set up in the Color Management panel of the Project Settings by turning on the Enable

Dolby Vision checkbox. This is a DaVinci Resolve Studio-only feature.

Dolby Vision settings in the Color Management panel of the Project Settings

The Dolby Vision group of settings also exposes menus for choosing the version of Dolby Vision you

want to use, the type of analysis and what kind of Master Display you’re using, and whether or not

to use an eCMU (assuming you possess the option). In addition, there are options to enable HDMI

tunneling (as described below). Finally, turning Dolby Vision on also enables the Dolby Vision palette

and controls in the Color page, which are described in greater detail later in this chapter.

To master with Dolby Vision in DaVinci Resolve using the built-in iCMU, you still need a more

specific hardware setup than the average grading and finishing workstation, consisting of the

following equipment:

�Your DaVinci Resolve grading workstation using a DeckLink 8K Pro or DeckLink 4K Extreme 12G

video interface.

�A mastering display capable of outputting HDR nit levels suitable for the deliverable you’re

required to produce


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

Simultaneous Master and Target

Display Output for Dolby Vision

When mastering HDR and trimming versions for more limited displays, it’s extremely useful to be able

to evaluate your HDR grade and SDR trim pass side-by-side. It’s possible to output both the Master

Display output and the Target Display output simultaneously when you’re grading with either Dolby

Vision or HDR10+ enabled.

Necessary Hardware

To work in this manner, you must have the following equipment:

�Your DaVinci Resolve grading workstation must output via a DeckLink 8K Pro via the attached

HDMI card. This will pass the Dolby Vision metadata through to the SDR display, so you will see

the SDR out from the HDR grade.

�Your Mastering Display must be capable of HDR nit levels suitable for the deliverable you’re

required to produce.

�A display that can be set to output calibrated SDR, probably using the BT.709 gamut

Enabling Simultaneous Monitoring

When you set up your display hardware, the HDR Master Display must be connected to output A,

and the Target Display must be connected to output B of whichever BMD video output device you’re

using. Then, you need to turn on the “Use dual outputs on SDI” checkbox in the Master Settings of

the Project Settings. At this point, assuming all of your connections are compatible with one another,

you should see an HDR image output to your HDR display, and a trimmed image output to your

SDR display.

HDMI Tunneling using DeckLink 8K Pro G2

HDMI Tunneling allows you to preview Dolby Vision content directly on a consumer display in real

time. The variables involved in display type and manufacturer all have their own processing behaviors,

so HDMI tunneling is not for reference grading but more of letting you get an idea of what the

audience will be seeing at home for QC purposes.

Performing HDMI tunneling in DaVinci Resolve is possible using lower cost Blackmagic DeckLink cards

instead of Dolby’s dedicated eCMU hardware. Currently, the only DeckLink card that supports Dolby

Vision HDMI tunneling is the DeckLink 8K Pro G2.

Setting up Dolby Vision HDMI Tunneling in DaVinci Resolve:


In Preferences > System > Video and Audio I/O, make sure that both the Capture Device and

Monitor Device are set to the DeckLink 8K Pro.


In Project Settings > Master Settings > Video Monitoring, set the following parameters:

�Use 4:4:4 SDI: Check this box.

�Video bit depth: Set this value to 12 bit.

�Enable HDR metadata: Check this box.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

The Project settings in Video Monitoring to enable Dolby Vision HDMI tunneling


In Project Settings > Color Management > Dolby Vision, set the following parameters:

�Enable Dolby Vision: Check this box.

�Enable Dolby Vision HDMI tunneling: Check this box.

�Enable L5 metadata on HDMI: Check this box.

The Project settings in Dolby Vision to enable HDMI tunneling


In the Color page, in the Dolby Vision palette, make sure that the Enable Tone Mapping Preview is

disabled (the box is not checked). HDMI tunneling will not work if this box is checked.

Disable the Enable Tone Mapping Preview box

in the Dolby Vision palette in the Color page


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

For more information on Dolby Vision HDMI tunneling go to Dolby’s website:

https://professionalsupport.dolby.com/s/article/HDMI-Tunneling?language=en_US

External Content Mapping Unit (eCMU) for Dolby Vision

DaVinci Resolve supports the use of a Dolby External Content Mapping Unit (eCMU) for studios doing

more intensive HDR mastering work, as it lets you monitor and adjust an HDR display simultaneously

to an SDR display for side-by-side trimming at high resolutions via hardware. The eCMU also has the

ability to preview Dolby Vision on a consumer display in real time via HDMI tunneling to view directly

what the audience will see at home.

Auto Analysis is Available to All Studio Users

Resolve Studio enables either unlicensed or licensed users to automatically analyze the image and

generate Dolby Vision analysis metadata. This metadata is used to deliver Dolby Vision content and

to render other HDR and SDR deliverables from the HDR grade that you’ve made. This enables any

DaVinci Resolve Studio user to create Dolby Vision deliverables with Level 1 metadata. However,

manual trimming of the analysis metadata requires a license from Dolby.

The commands governing Dolby Vision auto-analysis, which are available to all Resolve Studio

users, are available in the Color > Dolby Vision™ submenu, as well as the Dolby Vision palette,

and consist of the following:

•	 Analyze All Shots: Automatically analyzes each clip in the Timeline and stores

the results individually.

•	 Analyze Selected Shot(s): Only analyzes selected shots in the Timeline.

•	 Analyze Selected And Blend: Analyzes multiple selected shots as if they were a single

sequence. The result is the same analysis being saved to each clip. Useful to save time

when analyzing multiple clips that have identical content.

•	 Analyze Current Frame: A fast way to analyze clips where a single frame is representative

of the entire shot.

Once you analyze a clip, the Min, Max, and Average fields automatically populate with the

resulting L1 data; these fields are not editable.

The metadata fields for each clip

Additionally, clips that have been analyzed show an HDR badge in the Thumbnail timeline,

to help you keep track of which clips have been analyzed and which have yet to be.

Analyzed clips have HDR badges to identify them


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

Licensing DaVinci Resolve to Expose Dolby Vision Trim Controls

To expose the Dolby Vision controls in DaVinci Resolve Studio that let you make manual trims

on top of the automatic analysis that any copy of DaVinci Resolve Studio can do, you must email

dolbyvisionmastering@dolby.com to receive more information about obtaining a license.

Once you’ve obtained a license file from Dolby, you can import it by choosing File > Dolby Vision >

Load License, and its successful installation will enable the Dolby Vision controls to be enabled in

the Color page. You should also receive a display configuration file, which can be loaded via the File

> Dolby Vision > Load Configuration command and lets you populate the Dolby Vision drop-down

menus with the most up to date options.

Dolby Vision® Trim Controls in DaVinci Resolve

Once you’ve analyzed a clip, you’re in a position to trim the result. The latest version of the

Dolby Vision palette exposes four sets of controls. The first are the main controls:

�Target Display Output: This drop-down specifies what Dolby refers to as the Target Display, used

to display the tone mapped image. This menu lets you choose specific display properties to obtain

a preview of what the trimmed image will look like on different displays with different gamuts

and peak luminance capabilities. You can link the Target Display Output and the Trim Controls

For fields by clicking on the little chain icon directly to the left of the options. This automatically

changes the Trim Controls For field to the same value you set in the Target Display Output,

ensuring your trim controls are always right for the selected display.

�Trim Controls for: Which Target Display you’re currently trimming for. The default setting

(100-nit, BT.709, BT.1886, Full) lets you monitor an SDR version of the HDR image, so you can see

how the trim metadata tone maps the image on non-HDR televisions.

�Analyze controls: The commands governing Dolby Vision auto-analysis are available as buttons,

which perform the same functions as their similarly named counterparts in the Color > Dolby Vision

submenu. Please note that most trim controls are disabled until you perform an analysis, which is a

necessary first step.

All: Automatically analyzes each clip in the current Timeline and stores the results individually.

Selected: Only analyzes selected shots in the Timeline.

Blend: Analyzes multiple selected shots as if they were a single sequence. The result is the same

analysis being saved to each clip. You need to use the blend option when analyzing two clips that

meet at a through edit separating otherwise contiguous frames. It’s also typical to use the Blend

option when analyzing a scene of clips that take place at the same location at the same time, to

ensure that natural variations in lighting don’t add unwanted variations between the analyses of

clips that are supposed to already be balanced with one another. Blend also saves time when

analyzing multiple clips that have identical content.

Frame: Useful in situations where part of a clip has an extreme level of color or lightness that’s

not typical of the rest of the clip, that incorrectly biases the analysis and produces a poor result.

Placing the playhead on a frame that’s representative of how the clip is supposed to look and

using the Frame option bases the analysis on only that frame. This is also a fast way to analyze

clips where a single frame is representative of the entire shot.

�Enable Tone Mapping Preview: Lets you see the target display output in the Color page Viewer

and video output, so you can evaluate how the tone mapped version looks on your HDR display.

This control is disabled when you enable “Use dual-outputs on SDI” in the Master Settings of the

Project Settings, since the second output SDI now automatically displays the target display output.

�Mid Tone Offset (CM v4.0 only): This control is used to match the overall exposure between the

tone mapped SDR signal to the HDR master. This offset is applied to the L1 Mid values, allowing

the adjustment of mid tones without affecting the blacks and highlights. It can be used to shift


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

overall L1 analysis to ensure the best preservation of artistic intent. This setting is shared among all

trim passes you do at all nit levels, so if you’ve done two trim passes, one at 100 nits and another

at 1000 nits, adjusting this setting always adjusts both trim passes at once. Changes made to this

control are recorded to the L3 metadata for each clip.

The second are the Min, Mid, and Max metadata fields that are populated by the analyzed values

of the current clip. These fields cannot be edited, although analysis metadata can be copied and

pasted among clips. These values represent the L1 analysis and are used to calculate how the

HDR image should be trimmed to fit into the video standard specified by the Target Display.

The third are the Primary Trims, which are only editable if you’ve performed an analysis and if you

have a license from Dolby. Which controls are exposed depends on the version of Dolby Vision

you’ve selected in the Color Management panel of the Project Settings.

Dolby Vision CM v2.9 Controls

If you choose Dolby Vision 2.9 in the Color Management panel of the Project Settings, it activates the

2.9 version of Dolby’s content mapping algorithm and exposes the original Dolby Vision trim controls.

It is no longer suggested to use these, since you can do a Dolby Vision 4.0 analysis and trim, and still

export converted 2.9 metadata for legacy workflows.

�Lift/Gamma/Gain: These controls function similarly to the Y-only Lift, Gamma, and Gain master

wheels of the Color Wheels palette, to let you trim the overall contrast levels of the image. The

Dolby Best Practices Guide recommends to limit positive Lift to no more than 0.025, and mostly

restrict yourself to using Gamma and Gain if necessary to lighten the image.

�Saturation Gain: Lets you trim the saturation of the most highly saturated areas within a scene.

Lesser saturated values will be less affected.

�Chroma Weight: Darkens saturated parts of the image to preserve colorfulness in areas of

the image that are clipped by smaller gamuts that don’t have enough headroom for saturation

in the highlights.

�Tone Detail: Lets you preserve contrast detail in the highlights that might otherwise be lost when

the highlights are mapped to lower dynamic ranges, usually due to clipping. Increasing Tone Detail

Weight increases the amount of highlight detail that’s preserved. When used, can have the effect

of sharpening highlight detail.

Dolby Vision CM v4.0 Controls

If you choose Dolby Vision 4.0 in the Color Management panel of the Project Settings, it activates the

4.0 version of Dolby’s content mapping algorithm, and exposes the following controls.

�Lift/Gamma/Gain: These controls function similarly to the Y-only Lift, Gamma, and Gain master

wheels of the Color Wheels palette, to let you trim the overall contrast levels of the image. The

Dolby Best Practices Guide recommends to limit positive Lift to no more than 0.025, and mostly

restrict yourself to using Gamma and Gain if necessary to lighten the image.

�Saturation Gain: Lets you trim the saturation of the most highly saturated areas within a scene.

Lesser saturated values will be less affected.

�Chroma Weight: Darkens saturated parts of the image to preserve colorfulness in areas of

the image that are clipped by smaller gamuts that don’t have enough headroom for saturation

in the highlights.

�Tone Detail: Lets you preserve contrast detail in the highlights that might otherwise be lost when

the highlights are mapped to lower dynamic ranges, usually due to clipping. Increasing Tone Detail

Weight increases the amount of highlight detail that’s preserved. When used, can have the effect

of sharpening highlight detail.

�Mid Contrast Bias: Affects image contrast in the region around the computed average picture

level. This lets you increase or decrease contrast in the midtones of the image.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

�Highlight Clipping: Reduces details and affects the roll-off the brighter part of the image by

clipping the highlights as required. This is useful when the tone mapped image is displaying

unwanted details.

The Primary Trims controls that are found in the Dolby Vision palette are only enabled

once you’ve authorized your system with a special license, available from Dolby.

The fourth set of controls is available via a second palette mode, the Secondary Trims. These are only

editable if you’ve performed an analysis and if you have a license from Dolby.

�Secondary Saturations: A set of slider-based vector-style controls (similar to the Hue vs. Sat

curve) lets you adjust the Saturation of Red, Yellow, Green, Cyan, Blue, and Magenta to help you

selectively fine tune the results.

�Secondary Hues: Another set of slider-based vector-style controls (similar to the Hue vs.

Hue≈controls) lets you adjust the Hue of Red, Yellow, Green, Cyan, Blue, and Magenta to help you

fine tune the results.

The Secondary Trims controls, as seen on a licensed Dolby Vision system

Together, all of this trimming metadata lets the colorist guide how the iCMU or eCMU transforms

the image from the Mastering Display specified in the Project Settings to the Target Display

specified in the Dolby Vision palette. This metadata is carried throughout the ecosystem so that

your artistic intent is preserved on a variety of platforms and displays.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA