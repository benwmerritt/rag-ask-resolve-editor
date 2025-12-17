---
title: "Audio Only"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 730
---

# Audio Only

This preset is specifically for rendering an audio-only media file from the Timeline. Video rendering

is disabled, and this preset defaults to rendering the Main 1 bus as a single clip, rendering one track

per channel using the MXF OP-Atom format set to the Linear PCM codec, at 16-bits. However, the

QuickTime, MP4, and WAV formats are also available, and you can also render 24- or 32-bit output.

Additionally, you have the option to render other Mains or Submixes, or to choose a specific Timeline

Track to render. Finally, you can choose to render the current program as Individual Clips.

Creating and Using Your Own Presets

If there is a particular group of settings that you find yourself using repeatedly, you can turn it into a

custom Easy Setup, for easy recall.

To create a new Easy Setup:


If you want to start from scratch, make sure to choose Custom from the preset panel to unlock

every setting in the Render Settings pane.


Choose the particular settings you require in the Video, Audio, and File panels for your

new preset.


Open the Render Settings Options menu, and choose Save as New Preset.


Type a name into the “Render Preset” dialog, and click Save. The new preset now appears in the

Preset panel.

To load a preset:

�Click any preset. Every setting in the Render Settings pane updates to reflect the

preset you selected.

To change a custom preset that you’ve created

�Click a preset you want to change, make whatever changes you need to in the Video, Audio, and

File panels, then click the Render Settings Option menu, and choose Update Current Preset.

To delete a custom preset that you’ve created:

�Click a preset you want to delete, then click the Render Settings Option menu, and choose

Delete Current Preset.

Import and Export Custom Presets

Custom render presets that you create can be imported and exported from the Deliver page. Presets

are saved in .xml files that can be easily sent to other users or workstations to ensure the exact same

delivery methods are used between machines. In addition, any newly created export presets are

available in the “Add to Render Queue Using” menu when you right-click a timeline.

Render presets can now be imported and exported from the Deliver page.


Deliver | Chapter 187 Rendering Media

DELIVER

To save a custom render preset:


In the Deliver page, adjust the Video, Audio, and File options in the Render Settings to your needs.


In the Render Settings Option (3-dot) menu, select Save as New Preset.


Enter a name for the new preset, and press OK.

The new preset will be available in the Render Settings Option menu, as well as an option in the

Custom Preset Settings icon in the Render Presets row at the top of the Render Settings.

To export a custom render preset:


In the Deliver page, click on the Render Settings Option (3-dot) menu.


Select the name of the saved preset you wish to export.


Select Export Preset from the dropdown menu.


Use the file browser to name and set the save location of the preset.

The new preset will be available as an .xml file.

To import a custom render preset:


In the Deliver page, click on the Render Settings Option (3-dot) menu.


Select Import Preset from the dropdown menu.


Select the Render Setting .xml file in your file browser.


Press Open.

The imported preset will be available in the Render Settings Option menu, as well as an option in

the Custom Preset Settings icon in the Render Presets row at the top of the Render Settings.

To update a custom render preset with new settings:


Make any changes you wish to the Video, Audio or File Render Settings.


In the Deliver page, click on the Render Settings Option (3-dot) menu.


Select the name of the saved preset you wish to update.


Select Update Preset from the dropdown menu.


Press the Update Button from the warning dialog. This action can not be undone.

The selected preset will be updated with the new settings you selected.

To delete a custom render preset:


In the Deliver page, click on the Render Settings Option (3-dot) menu.


Select the name of the saved preset you wish to delete.


Select Delete Preset from the dropdown menu.


Press the Delete Button from the warning dialog. This action can not be undone.

The selected preset will be permanently deleted from the Render Presets list.


Deliver | Chapter 187 Rendering Media

DELIVER

Choosing a Location to Render

The first decision you have to make when rendering your output is where it’s going to be rendered.

Accordingly, this is the first set of controls appearing at the top of the Render Settings parameters.

�Filename: A preview of what the file name will be based on the settings found in the File panel

described later. The Custom/Timeline name and File suffix fields, as well as the “Use x digits in the

filename” settings all determine what name appears here. The editable portions of this filename

preview can also be edited here.

�Location: Click the Browse button to choose a directory in which to write the media being

output by DaVinci Resolve. After you’ve selected a directory, the path name appears in the

“Render job to” field.

Single Clip vs. Individual Clips

While there are numerous options available in the Render Settings of the Deliver page, there are

basically two overarching ways you can render your project, depending on which of the “Render”

radio buttons you click in the Output group.

Render a single clip or individual clips

Single Clip

When you select the Single clip option, you’re setting up a render wherein all clips in the session are

output together, as a single media file in whatever format you choose. This means you’ll be rendering

the selected range of the session to a single MXF or QuickTime file, or as a single collection of

image sequences.

�Timecode: The timecode that’s written out is dictated by the “Start timeline timecode at” setting

of the timeline being rendered. Media files contain a continuous timecode track, while image

sequences have timecode written into each frame’s data header, and integrated into the file name

(as a frame count).

�Frame Rate: If you’re rendering a project that uses mixed frame rates, rendering to a single clip

converts every clip in the entire session to the project frame rate, using either the project-wide or

clip specific “Retime process” setting.

�Effects: Most effects are “baked into” the rendered output when you render a single clip.

IMPORTANT: Whenever clip filtering is enabled (via the dropdown menu to the right of the

Clips button), Single Clip rendering cannot be selected. You can see if clip filtering is enabled

by an orange line underneath the Clips button in the UI toolbar.


Deliver | Chapter 187 Rendering Media

DELIVER

Individual Clips

Selecting the Individual clips option sets up a render where each clip is rendered as an individual

media file in whichever format you choose. The result will be a collection of as many media files as

there are clips in the range you’ve selected to render.

�Timecode: The timecode written to each clip is cloned from the original source media, making it

easy to reconform media for projects being passed between DaVinci Resolve and NLEs.

�Frame Rate: If you’re rendering a project that uses mixed frame rates, rendering to source renders

each clip at its own individual frame rate, to accommodate round-trip workflows.

�Effects: You can choose whether any timeline-based effects are either ignored or “baked into” the

individual clips by checking/unchecking the Render Timeline Effects box.

�Resolution: You can choose whether the individual clips are rendered at the timeline size or their

original source resolution by checking/unchecking the Render at Source Resolution box.

All Other Render Settings for Output

This section covers the different render settings that are available for customizing your output.

Depending on which Render Setting mode you chose, some of these may be hidden, but this section

covers the full list found in the Advanced panel of controls.

If you choose one of the Easy Setups, then some of these settings will be locked, and others will be

editable, depending on the requirements of that setup. If none of the Easy Setups is suitable for the

task at hand, you can leave the Easy Setup dropdown menu set to none, and manually choose the

necessary settings for the task at hand.

Video Panel

This panel contains all video-oriented parameters.

Format and Codec Controls

These top-level parameters let you choose whether or not to render video, and which format to render

it to. Depending on which Format, Codec, and Type you choose, other options may or may not appear.

�Export Video: Turn this checkbox on to render the source video. Turn this checkbox off if you want

to render the source audio all by itself; this disables all video controls, and shows an Audio Format

dropdown menu in the audio section of settings.

�Format: A dropdown menu that gives access to the container formats that are currently

available on your system. The available options depend on whether you have Final Cut Pro and

QuickTime installed, and on the operating system you’re using. This list is constantly growing,

as new file formats are added over time, so be sure to check each new version for the latest

supported formats.

AVI: A now-deprecated file-based media format that, despite its age, remains popular with

Windows applications. Supports delivery using the Cineform, Grass Valley HQ and HQX, and

Uncompressed RGB and YUV codecs.

Cineon: An older uncompressed image sequence format developed by Kodak, designed for film

scanning and digital mastering, which delivers RGB 10-bit.

DCP: Native DCP encoding and decoding for creating unencoded DCP files only. If you have a

license for Frauenhofer’s EasyDCP, a setting in the Configuration panel of the System Preferences

enables you to choose whether to use EasyDCP (for creating encrypted DCP output), or the native

DaVinci Resolve encoding.


Deliver | Chapter 187 Rendering Media

DELIVER

DPX: An uncompressed image sequence format favored by the film industry for mastering and

delivery for DCDM mastering, which can be delivered as RGB 10-, 12-, 16-bit integer and half float,

or RGBA 8-bit.

easyDCP: (when installed) An option that allows you to master a DCP or IMF directly

from DaVinci Resolve in conjunction when you have an installed license of Fraunhofer’s

EasyDCP software.

EXR: The OpenEXR format is a high-dynamic-range image sequence format developed by ILM

for applications requiring high quality and multiple channels. Used for outputting ACES and HDR

deliverables. You can deliver to a variety of RGB Half and RGB Float settings. When choosing

the RGB half (DWAA) or (DWAB) compression codecs, an additional “Compression level” setting

appears that lets you choose how much compression to apply.

IMF: A native IMF encoding option that lets you export to the SMPTE ST.2067 Interoperable

Master Format (IMF) for tapeless deliverables to networks and distributors, with support for

encoding of JPEG2000 using a library licensed from Kakadu software. No additional licenses

or plugins are required to output to IMF. The IMF format supports multiple tracks of video,

multiple tracks of audio, and multiple subtitle and closed caption tracks, all of which are meant to

accommodate multiple output formats and languages from a single deliverable. This is done by

wrapping a timeline’s different video and audio tracks (media essences) and subtitle tracks (data

essences) into a “composition” within the Material eXchange Format (MXF).

JPEG 2000: DaVinci Resolve 15 introduced support for the encoding and decoding of JPEG2000

using a library licensed from Kakadu software. This includes a complete implementation of the

JPEG2000 Part 1 standard, as well as much of Parts 2 and 3. JPEG2000 is commonly used for IMF

and DCP workflows.

MJ2: The Motion JPEG 2000 format. DaVinci Resolve 15 introduced support for the encoding and

decoding of JPEG2000 using a library licensed from Kakadu software. This includes a complete

implementation of the JPEG2000 Part 1 standard, as well as much of Parts 2 and 3. JPEG2000 is

commonly used for IMF and DCP workflows.

MP4: Dedicated MP4 encoding lets you export H.264-encoded movies.

MXF OP–Atom: A simple standard for the Material eXchange Format, a file-based media format,

that’s often used when delivering DNxHD. This version conforms to the SMPTE 390M standard,

and can deliver using the DNxHD, DNxHR, Kakadu JPEG 2000, NTSC and PAL Avid, RGB Avid 10-

bit, and XDCAM MPEG2 codec options.

MXF OP1A: A version of the Material eXchange Format that conforms to the SMPTE 378M

standard, and can deliver using the 1080i Avid 8-bit, DNxHD, DNxHR, Kakadu JPEG 2000, NTSC

and PAL Avid, RGB Avid 10-bit, Sony MPEG4 422 and 444, and Sony XAVC Intra CBG and VBR,

and XDCAM MPEG2 codec options.

QuickTime: Apple’s file-based media format, used when delivering Apple ProRes, DNxHD or

DNxHR wrapped in QuickTime, GoPro Cineform RGB 16-bit and YUV 10-bit, Grass Valley HQ and

HQX, Kakadu JPEG 2000, H.264, HEVC, H.265 (single or multi-pass), Photo JPEG, Kakadu JPEG

2000, Uncompressed 8- and 10-bit formats with ARGB/BGRA/RGB/YUV channel orders, and VP9

at 8-, 10-, and 12-bits.

TIFF: “Tagged Image File Format,” an image sequence format compatible with many desktop

video applications on many platforms and is also used when delivering for DCDM mastering.

�Codec: A dropdown menu that lets you choose from a selection of codecs that are available to the

format you’ve selected above.

�Type: Different codec options may also present different bit depth and color space combinations,

as well, which are available from this menu.


Deliver | Chapter 187 Rendering Media

DELIVER

�Maximum Bit Rate: (Does not appear for all codecs) Codecs such as Kakadu JPEG 2000 let you

specify a maximum bit rate, in Mbits per second, with which to encode the delivered video.

�Field rendering: If you’re processing interlaced source material, this checkbox sets DaVinci

Resolve to render each field individually before reintegrating them back into a single frame, in

order to process clips most accurately with filtering operations that would otherwise violate field

boundaries and cause problems. If you’re not rendering interlaced media, you should leave this

checkbox turned off, as it is more processing intensive.

�Interlaced rendering: By default, frame-based media sources (image sequences, etc.) are

rendered progressively. You can now optionally render them as interlaced media instead by

checking this box. Once checked, select the Field Order to encode, either top or bottom field first.

�Export HDR10 Metadata: (Available in Single clip mode if HDR10+ is enabled in Project Settings)

Exports HDR10 metadata to the rendered file when you’re doing an HDR workflow.

�Embed HDR10 Metadata: (Available in Single clip mode if HDR10+ is enabled in Project Settings)

Exports HDR10 metadata to the rendered file when you’re doing an HDR workflow. Embeds

HDR10 metadata within the exported media of selected formats.

�Embed HDR Vivid Metadata: Exports HDR Vivid metadata to the rendered file when you’re doing

an HDR workflow. Embeds HDR Vivid metadata within the exported media of selected formats.

�Render at Source Resolution: (When rendering Individual Clips) This checkbox lets you render

each clip at the same resolution as its source media file, letting you preserve mixed frame sizes for

final delivery.

�Resolution: The output resolution for rendering. This setting defaults to Timeline Resolution;

this lets you create a preset that automatically updates its resolution settings dynamically and

automatically changed to the currently loaded timeline/project. However, you can change

the resolution here if you want to set a specific resolution for the preset. Using this setting,

you can queue up different render jobs at different resolutions, in order to output both HD

and SD resolution media in the same render session, for example. Some file formats require

specific resolutions, in which case the Output Size settings will be automatically set to the

necessary resolution.

�Frame rate: (When rendering Single Clip) This setting defaults to the Timeline Frame Rate;

this lets you create a preset that automatically updates its frame rate settings dynamically and

automatically changed to the currently loaded timeline/project. However, you may wish to set this

to a variation of the current conformed rate, for example choosing from between 23.98 or 24 fps.

Doing so will adjust the metadata written within the file, which is used to aid playback for the range

of systems available worldwide.

3:2 Pulldown Insertion Options: Starting with DaVinci Resolve Studio 12.5, you have the option

of outputting either 29.97 or 30 fps media with 3:2 pulldown insertion if your project’s playback

frame rate is either 23.98 or 24 fps. To output 29.97 media, the project must be 23.98 fps; simply

choose (23.976 3:2) from the Frame rate dropdown. Projects with 24 fps frame rates can only be

output at 30 fps.

�Chapters from Markers: (QuickTime or MP4 only) Embeds chapter points in the rendered file

corresponding to the marker’s position on the Timeline of the selected marker color.

�Export Alpha: (When rendering Individual Clips) Turning this checkbox on results in alpha

channels found in each clip’s source media file being output to each delivered clip, as well as

alpha information that you’re creating in DaVinci Resolve and inserting into that clip via the Alpha

output of the Color page Node Editor being output to each delivered clip.

�Alpha Mode: (When rendering Individual Clips) Lets you choose how to export alpha channels

when Export Alpha is enabled. You can choose Straight or Premultiplied.


Deliver | Chapter 187 Rendering Media

DELIVER

�Render Stereoscopic 3D: (Only appears if there are stereo clips in a timeline) Three options let

you choose how to render stereoscopic timelines, rendering just one eye’s worth of media at a

time, or rendering a single set of stereo media in one of four ways, depending on the option you

choose from the “Both eyes as” dropdown menu.

Left eye: Lets you render only the left-eye media from a stereo timeline.

Right eye: Lets you render only the right-eye media from a stereo timeline.

Both eyes as: Lets you select from four ways of rendering the left and right eyes of stereo media

as a single set of media files. “Separate files” lets you output both the left-eye and right-eye media

as individual media files, all at once. Side-by-side, Line-by-Line, and Top-Bottom let you output

frame-compatible media that can be output to stereo-capable displays. Anaglyph lets you output

a traditional anaglyph red/cyan stereo image for viewing on any display using red/cyan glasses.

MV-HEVC lets you output spatial video clips compatible with most VR headsets.

�Use Constant Bit Rate: If the Format and Codec you’ve specified allows you to switch

between variable and constant bit rate output, this checkbox lets you force video to render at a

constant bit rate.

Optional MP4, H.264, H.265, VP9, or HEVC Controls

If you choose MP4 as the format, or QuickTime with H.264, H.265, or VP9 as the codec, additional

options appear, described below. Workstations using NVIDIA GPUs that offer NVENC will present

alternative accelerated options, while other workstations offering QuickSync hardware encoding

instead will be able to use that option.

�Use hardware acceleration if available: DaVinci Resolve supports QuickSync hardware encoding

of H.264 and HEVC, if available on your workstation.

�Quality: If the currently selected option in the Render to dropdown menu has options for changing

the compression quality, this dropdown menu lets you choose the quality you want to use.

Otherwise, it’s disabled.

�Restrict to X Kb/s: You can choose Automatic, or select a maximum data rate with which to export.

�Encoding Profile: A dropdown that lets you choose among different encoding profiles, each

of which has been optimized for different purposes. The tradeoff is between quality and

computational intensity for encoding and playback. The available options are:

Auto: Automatically selects an encoding profile.

Base: For H.264, intended for video conferencing and mobile phone use; highly compressed.

Main: For H.264, intended for SD analog transmission. For H.265, intended for the compression of

4:2:0 video at up to 4K 60fps with a bit depth of 8-bits per channel.

Main10: (H.265 only) Intended for the compression of 4:2:0 video at up to 4K 60fps with a bit

depth of 10-bits per channel.

Main 4:2:2 10: (H.265 only) Intended for the compression of 4:2:2 video at up to 4K 60fps with a

bit depth of 10-bits per channel.

High: For H.264, intended for Blu-Ray and HD transmission.

�Entropy Mode: (called Entropy Coding Mode for compatible Nvidia GPUs) A dropdown that lets

you choose which algorithm the encoder should use for compression. The choices are:

CALVC (context-adaptive variable-length encoding): A lower-quality algorithm that’s less

computationally intensive to process and play.

CABAC (context-based adaptive binary arithmetic coding): A higher-quality algorithm that yields

better visual quality at lower bandwidth, at the cost of being more computationally expensive to

process and play.


Deliver | Chapter 187 Rendering Media

DELIVER

�Multi-pass encode: (Available for QuickTime H.264 and H.265) You can choose between Single

and Multi-pass encoding. Single pass is faster, but multi-pass yields superior results when quality

is important. When you enable Multi-pass, the number of passes performed is automatic.

�Key Frames: (Available for QuickTime H.264 and H.265) You can choose Automatic, or select a

duration for manual keyframe insertion.

�Frame Reordering: (Available for QuickTime H.264 and H.265) On by default, Frame Reordering

enables the encoding of B frames to improve the quality of the resulting compressed movie file.

Turning off Frame Reordering will speed encoding performance at the expense of visual quality.

�Rate Control: (Available for compatible NVIDIA GPUs) Provides six options for controlling Encoding

Profile and Entropy Mode.

�Lookahead: (Available for compatible NVIDIA GPUs) Lets you specify how many frames for the

encoder to examine in advance of compression.

Optional DCP and IMF Controls

If you choose DCP or IMF as the Format, additional options appear, described below.

�Use interop packaging: (DCP only, located under Type parameter) Lets you create an Interop DCP

package, based on an earlier standard of DCP delivery that is not forward compatible with SMPTE

DCP packages.

�Package Type: (IMF) Defaults to App2 Extended (App2e), for encoding JPEG 2000 up to 4K.

�Bit Depth: (IMF) The bit depth of the encoded IMF video.

�Encoding Profile: (IMF) A dropdown that lets you choose among Auto, IMF, and Broadcast.

�Encoding Level: (IMF) Provides different choices based on what is selected in Encoding Profile.

�Maximum bit rate: (DCP, IMF) Lets you choose how much to compress the result.

�Lossless Compression: (IMF) Lets you choose to encode using lossless compression.

�Slope-Rate Control: (DCP, IMF) A checkbox lets you specify lossless compression.

�QStep: (DCP, IMF) Lets you choose either automatic or manually specified DCP quantization levels

at which to compress the video signal when using the Kakadu JPEG 2000 encoder.

Advanced Controls

An advanced settings disclosure button hides the following additional controls, by default.

�Pixel aspect ratio: Lets you override the Project Settings and change the PAR of the rendered

output to either Square or Cinemascope.

�Data levels: Defaults to “Auto,” which simply renders all clips with the data level appropriate to

the currently selected codec in the “Render to” dropdown menu, which is usually the preferred

behavior. Choosing one of the other options (“Video” or “Full”) outputs all clips using the selected

data range. For more information, see Chapter 9, “Data Levels, Color Management, and ACES.”

Retain sub-black and super-white data: Turning this checkbox on lets you choose to output

media files that preserve overshoots and undershoots, data that’s above the maximum and

minimum data levels of the data level you’ve selected, assuming this is supported by the video

format and codec you’re exporting to. Otherwise, DaVinci Resolve clips these “out-of-bounds”

parts of the signal in an effort to keep your deliverables from violating whatever QC standards

you’re adhering to in your grade.

�Color Space Tag: A dropdown menu that lets you choose a color space to embed as metadata

in the rendered file. This setting defaults to Same as Project if your project’s color science is set

to DaVinci YRGB Color Managed, or the ACES Output Device Transform if your color science

is set to ACEScc or ACEScct. You can override this option manually from the choices on the

dropdown menu.


Deliver | Chapter 187 Rendering Media

DELIVER

�Gamma Tag: A dropdown menu that lets you choose the gamma to embed as metadata in the

rendered file. This setting defaults to Same as Project if your project’s color science is set to

DaVinci YRGB Color Managed, or you can override this option manually from the choices on the

dropdown menu.

�Data burn-in: A dropdown menu that defaults to “Same as Project,” which leaves the current Data

Burn In palette settings enabled while rendering, inserting a window burn into the media being

output. Choosing “None” disables window burns while rendering. Note that when rendering as

Individual Source Clips, individual clip burn in presets can be assigned if they’ve been created in

the Data Burn In palette.

�Bypass re-encode when possible: Turning this checkbox on makes it possible to do a direct

copy of the video essence of video items in the Timeline, directly from the source media to the

file being output, when the selected Format, Codec, and Type matches the source. This also

preserves Alpha channel data for compatible formats.

Bypass re-encode eliminates the need to re-encode video media, preserves quality, and speeds

up the output process dramatically, but it only works for clips in the Timeline to which no additional

effects have been added. Doing any grading, adding a Resolve FX plugin, adding any overlapping

effects or compositing to clips in the Timeline, resizing or stabilizing clips or altering the output sizing

of the Timeline, and adding Fusion effects will all necessitate re-encoding the entire clip in order to

process these effects. Transitions will require processing but only for the duration of each transition.

There are many situations where this is valuable:

Fast output of simple edits: You’ve edited a simple cuts-only promo using footage cut

from a previously rendered program using QuickTime ProResHQ 422 media, and you’re

exporting to the exact same format. You can output all of the media very quickly using

Bypass re‑encode when possible.

Fast output of previously output timelines with small changes: You need to replace

a few shots in an effects-intensive program that’s already been output. You can import

the media file that was output into a new timeline, replace only the required shots with

new media. DaVinci Resolve will do a direct copy of all previously rendered media, while

re-encoding only the new clips with whatever effects and grading they contain. This lets

you quickly re-output a high-quality master file, while preventing you from needing to re-

render the entire program.

Fast output of previously output timelines with new audio mixes: You’ve placed a

previously rendered Video+Audio clip onto a timeline and edited a new audio mix clip to

replace the old audio mix. In this situation, a new Video+Audio file will be quickly written

with the new audio, but the video component of that file won’t be re-encoded, again

resulting in a fast export at the highest quality.

TIP: For a list of which video formats are compatible with Bypass Re-encode on macOS,

Windows, and Linux, as well as which formats are compatible with Alpha channels,

see the “Supported Codec List” at the DaVinci Resolve Support page located at:

https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion.

�Use optimized media: When this checkbox is turned on, DaVinci Resolve will use optimized

media, when available, to do the final render, to save time. If your media has been optimized to

the same format as the one you’re outputting to (or better), this is convenient. However, if you’ve

optimized to a lower quality format than what you’re outputting to, you should turn this checkbox

off to force DaVinci Resolve to process all clips using the original media, guaranteeing the best

quality available.


Deliver | Chapter 187 Rendering Media

DELIVER

�Use proxy media: When this checkbox is turned on, DaVinci Resolve will use the generated proxy

media, when available, to do the final render, to save time. However, if your proxies are a lower-

quality format than what you’re outputting to, you should turn this checkbox off to force DaVinci

Resolve to process all clips using the original media, guaranteeing the best quality available.

�Use render cached images: When this checkbox is turned on, DaVinci Resolve will write media

from the cache to the files being output to save time. If you’re caching using the same media

format you’re outputting to (or better), this can be convenient. However, if you’re caching in a

lower-quality format than the one you’re outputting to, you’ll want to turn this checkbox off to force

DaVinci Resolve to process all media as it’s being rendered, writing at the maximum quality you’re

outputting to.

�Force sizing to highest quality: If you’ve been working with the “When resizing and scaling:”

option set to Bilinear to improve performance when working on slower workstations, turning this

checkbox on automatically renders all clips using the “Uses Sharper filter” setting of the Image

Scaling panel in the Project Settings.

For more information, see Chapter 4, “System and User Preferences.”

�Force debayer res to highest quality: When rendering camera raw media formats that allow

variable quality debayering, it’s common to lower the debayering quality to improve real time

performance while grading. Turning this checkbox on guarantees that media will always be

rendered at the highest available quality, saving you from forgetting to manually change the

debayer setting back when setting up a render at 3am.

�Render All Video Tracks: (When rendering Single Clips) You can un-check Render All Video

Tracks and select specific tracks in the Disable dropdown menu to exclude those tracks from the

final output on a per render job basis.

�Enable flat pass: Three options let you choose whether or not to render each clip with its

grade applied.

Off: DaVinci Resolve always applies each clip’s grade when rendering.

With clip settings: For each version of a clip, the system will check that version’s pass flat flag.

If it’s turned on, the system disables color correction for that version of the clip. Otherwise, that

version will be rendered with its grade intact. Versions can be individually flagged by right-clicking

a clip’s thumbnail in the Timeline, choosing the submenu of the version you want to flag, and

choosing Enable Flat Pass.

Always On: When checked, DaVinci Resolve disables the grade of every clip being rendered.

�Disable sizing and blanking output: When turned off, Output Blanking to create letterboxing or

pillarboxing is “baked” into the output, as are all sizing adjustments made on the Cut, Edit, and

Color pages, including Image stabilization.

When turned on, Output Blanking, Cut and Edit page sizing adjustments, Color page Input and

Output Sizing, and Image Stabilization are disabled. Rendered media is rendered either at the

source resolution if “Render at source resolution” is enabled in individual clips mode, or to the

currently specified resolution of the Timeline or project. If you’re outputting via Final Cut Pro or

Premiere Pro XML, or Avid AAF, sizing adjustments are output to the XML or AAF files that are

created for purposes of round-tripping these adjustments as editable metadata back to an NLE.

Be aware that “Disable sizing and blanking output” does not disable any transform operations that

happen within the Fusion page, nor does it disable transforms happening as a result of an OpenFX

or ResolveFX plugin applied to one or more clips in the Cut, Edit, or Color pages. All of these

effects will continue to be rendered into the final output.


Deliver | Chapter 187 Rendering Media

DELIVER

�Trigger script at: You now have the option of triggering a script to execute before or after

rendering a timeline, by checking the “Trigger script at” box.

Start: Executes the script before the render job.

End: Executes the script after the render job.

Script: Chooses the specific script to run. You can select the specific script to execute using the

corresponding dropdown menu. Scripts must be written for the Resolve scripting framework in

either Python or Lua, and placed in the following directory:

MacOS: /Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Deliver/

Windows: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Deliver

Linux: /opt/resolve/Fusion/Scripts/Deliver

�Render full extents: (When rendering Individual Clips) When this box is checked, the entire

original media clip is rendered out completely, instead of just the portion delineated by the In and

Out points of the timeline clip.

�Add X frame handles: (When rendering Individual Clips) Lets you specify front and rear handles

to be output in frames. This is particularly useful in round trips, when the finishing editor might

want additional handles with which to roll edit points or add transitions while fine-tuning the

graded edit.

�Tone Mapping: (Available in Single clip mode if Dolby Vision or HDR10+ is enabled in Project

Settings) When set to None, the timeline is output using the current color management settings.

When set to either Dolby Vision or HDR10+, you can choose to output the timeline at a specific

peak nit level, color space, gamma, and Data Level using either the Dolby Vision or HDR10+

metadata available to guide the tone mapping operation you’ve selected. This makes it easy to set

up multiple jobs to output HDR outputs at varying levels, as necessary.

DCP and IMF Composition Settings

If you’ve selected either DCP or IMF from the Format, a Composition Settings group appears with the

following parameters when you click the disclosure control, which let you populate generic DCP and

IMF composition metadata, as well as various studio specific settings:

�Composition name: The name of the exported composition.

�Issuer: The organization providing the composition.

�Use current date: A checkbox that lets the current date be used as the Issue date automatically.

�Issue date: The date the composition is issued.

�Content kind: A dropdown provides a list of acceptable choices for defining the content.

�Content originator: A text field to add who is responsible for this content.

�Include volume index and output profile list: Check this box to include these xml files in

the package.

�Content version label: Meant to identify the version of the content being provided.

�Annotate xml using composition name: Auto-populates Asset Map, Composition Playlist, and

Packing List with data from the project. Otherwise these three fields are manually editable.

�Annotate reel index as suffix (DCP only): Auto-populates Reel Annotation with data from the

project. Otherwise this is manually editable.

�Annotate media using filename: Auto-populates Main Video Track and Audio Track 1 with data

from the project. Otherwise these three fields are manually editable.


Deliver | Chapter 187 Rendering Media

DELIVER

Subtitle Controls

The Subtitle Settings group exposes controls governing how to export subtitles in your program:

�Export Subtitle checkbox: Lets you enable or disable subtitle/closed caption output.

�Format pop-up: Provides four options for outputting subtitles/closed captions.

As a separate file: Outputs each subtitle track you select as a separate file using the format

specified by the Export As pop-up. A set of checkboxes lets you choose which subtitle tracks you

want to output.

Burn into video: Renders all video with the currently selected subtitle track burned into the video.

As embedded captions: Outputs the currently selected subtitle track as an embedded metadata

layer within supported media formats. There is currently support for CEA-608 closed captions

within MXF OP1A and QuickTime files. You can choose the subtitle format from the Codec pop-up

that appears.

�Export As: (Only available when Format is set to “As a separate file.”) Lets you choose the subtitle/

closed captioning format to output to. Options include: IMSC1, DFXP, SRT, and WebVTT.

�Include the following subtitle tracks in the export: (Only available when Format is set to “As a

separate file.”) A series of checkboxes lets you turn on which subtitle tracks to output.

�Codec: (Only available when Format is set to “As embedded captions.”) Lets you choose how to

format embedded closed captions; choices include: Text and CEA-608.

NOTE: Neither analog (Line 21) nor digital (CEA-708) closed caption output via Decklink or

UltraStudio is supported at this time.