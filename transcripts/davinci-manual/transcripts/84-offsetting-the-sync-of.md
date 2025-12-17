---
title: "Offsetting the Sync of"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 84
---

# Offsetting the Sync of

Previously Synced Clips

If you need to offset the audio (or stereo 3D) sync of the items that make up a clip later on, you need

only select the synced clip you want to resync in the Media Pool, then click the Waveform button at the

top of the Audio panel to show the clip’s audio waveform, turn off the linked clip button, change either

the audio or video sync points, and turn the linked clip button back on again.

You can also use two sets of commands for slipping the sync of any clip:

•	 Trim > Slip Audio > Slip Audio One Frame Forward/Reverse: (Option-Period and Option-

Comma) Slips the audio/video sync of any clip in whole frame increments.

•	 Trim > Slip Audio > Slip Audio One Subframe Forward/Reverse: (Option-Right Arrow and

Option‑Left Arrow) Slips the audio/video sync of any clip in 1/10th frame increments.

•	 Trim > Slip Eye > Slip Eye One Frame Forward/Reverse: (Command-Option-Period and

Command-Option-Comma) Slips the sync relationship between the eyes within a stereo clip

in whole frame increments.

Finding Synced Audio Files

When you’ve synced dual-system audio and video clips together in DaVinci Resolve, you can find the

audio clip that a video clip has been synced to using the following procedure.

To find the audio clip that a video clip has been synced to:

�Show the Media Pool in List view, and reference file name in the Synced Audio column.

�Right-click a video clip that’s been synced to audio, and choose “Reveal synced audio in

Media Pool” from the contextual menu. The bin holding the synced audio clip is opened and that

clip is selected.


Ingest and Organize Media | Chapter 21 Syncing Audio and Video

MEDIA

Displaying Synced Audio

File Names on the Timeline

For certain workflows you may wish to see the name of the original audio file used in a synced dual

system audio pair on the timeline tracks, rather than the name of the video clip its attached to.

To display the filename of the original audio file used in a synced pair in the timeline:


Choose View > Show File Names. You cannot see synced audio file names unless you’ve set

DaVinci Resolve to display the original file names.


Choose View > Overlay Synced Audio File Names. You should now see the names of the synced

audio files superimposed on the audio clips in the Timelines, and the names of the video files

superimposed on the video clips in the Timelines, even when they’re synced.

Viewing the synced audio file names in the Edit page Timeline


Ingest and Organize Media | Chapter 21 Syncing Audio and Video

MEDIA

Chapter 22

Modifying Clips

and Clip Attributes

Once you’ve added clips to the Media Pool, you may find you have to make some

changes to prepare it for use in your project.

This chapter covers diverse tasks that include redefining the clip attributes associated with each

source clip to reinterpret video and audio attributes, timecode values, and clip names, converting

LTC timecode recorded on an audio track into usable timecode, chopping long clips into more

manageable subclips, and creating stereo clips from left and right eye media.

Contents

Adjusting Media Pool Clips in the Inspector�������������������������������������������������������������������������������������������������������������������������� 445

Changing Clip Attributes������������������������������������������������������������������������������������������������������������������������������������������������������������������ 445

Video Attributes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 446

Real-Time 3:2 Pulldown Removal�������������������������������������������������������������������������������������������������������������������������������������������������� 448

Audio Attributes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 449

Timecode Attributes���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 452

Reel Name Attributes�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 453

Update Timecode from Audio – LTC������������������������������������������������������������������������������������������������������������������������������������������ 454

Changing Clip Thumbnails in the Media Pool����������������������������������������������������������������������������������������������������������������������� 454

Creating Subclips��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 455

Removing or Changing Subclip Limits���������������������������������������������������������������������������������������������������������������������������������������� 455

Organizing Stereo 3D Media���������������������������������������������������������������������������������������������������������������������������������������������������������� 456

Camera Raw Decoding���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 456


Ingest and Organize Media | Chapter 22 Modifying Clips and Clip Attributes

MEDIA

Adjusting Media Pool Clips in the Inspector

You can directly modify Media Pool clips in the Inspector, before you edit those clips into a timeline.

This allows you to change the parameters of source media so that clips that are subsequently edited

into a timeline carry those new settings with it. For example, you can prepare your material prior to

editing by changing the clip’s file and RAW settings, adjusting the audio levels and EQ, or assigning

it a specific lens correction, etc. Once modified, any part of that clip would have the correct Inspector

parameters already in place when you edited them into your timeline.

For more information about using the Inspector in the Media Pool, see Chapter 20, “Using the

Inspector in the Media Page.”

Changing Clip Attributes

Using the Clip Attributes window, you can alter additional attributes for multiple clips all at once. This

window has some overlap with other clip attributes that are editable directly from submenus within the

Media Pool clip contextual menu.

To edit the attributes of one or more clips in the Media Pool of any page:


Select one or more clips in the Media Pool by Shift-clicking, Command-clicking, or dragging a

bounding box around them.


Right-click one of the selected clips, and choose Clip Attributes.


Click to open the panel of the attributes you want to edit. If you’ve selected multiple clips, then

making your alterations automatically checks the box of the attributes being changed.


When you’re finished, click OK to accept the changes.

You can also edit select clip attributes for clips that have been edited into the Timeline.

To edit the attributes of one or more clips in the Timeline of the Cut, Edit, or Color pages:


Select one or more clips in the Timeline by Shift-clicking, Command-clicking, or dragging a

bounding box around them.


Right-click one of the selected clips, and choose Clip Attributes.


Click to open the panel of the attributes you want to edit. If you’ve selected multiple clips, then

making your alterations automatically checks the box of the attributes being changed.


When you’re finished, click OK to accept the changes.


Ingest and Organize Media | Chapter 22 Modifying Clips and Clip Attributes

MEDIA

Video Attributes

These affect individual clip frame rate, geometry, and data levels.

The Video panel of the Clip Attributes Window

�Video Frame Rate: In cases where a clip’s frame rate was specified incorrectly by another

application or recording device, or if there is no frame rate metadata available at all, you can

change what DaVinci Resolve considers the frame rate of the source clip to be by either using

this menu to choose a frame rate from 1 to 120 fps, or choosing Custom and entering a value

from 1 to 32,000 fps (to accommodate high-speed and specialty format video). Changing a clip’s

Video Frame Rate will change its duration and relative playback speed in DaVinci Resolve. A clip’s

audio, however, will be unaffected. Please note, just because extremely high frame rate media is

supported, do not expect real time performance at excessively high frame rates, and understand

that what performance your workstation is capable of depends on its configuration and the speed

of your storage.

�Data Levels: In certain circumstances, you may find that you need to manually choose appropriate

data levels for clips that are not being interpreted correctly, choosing between Auto, Video,

and Full. For more information on this setting, and how it affects the image data in your project,

see Chapter 9, “Data Levels, Color Management, and ACES.”

�Pixel Aspect Ratio: In projects using a mix of media with different frame sizes, you can assign

specific pixel aspect ratios using this drop-down menu. You can also change the Pixel Aspect

Ratio to a manual value to adjust and compensate for various motion picture capture technologies.

Select Custom from the Pixel Aspect Ratio menu, and then enter a numeric value in the box

below. The value is the X in the 1:X ratio. For example, you would type in 1.6 to get a pixel aspect

ratio of 1:1.6.


Ingest and Organize Media | Chapter 22 Modifying Clips and Clip Attributes

MEDIA

�Horizontal and Vertical Image Flip: Modifies the horizontal and vertical image flip camera

metadata for r3d clips, which is useful for stereoscopic 3D projects shot with a mirrored camera

rig that reverses the media from one eye, or in cases where steadicam rigs result in upside-

down clips. These settings are different from the Flip Image controls in the Sizing palette of the

Color page.

�Image Orientation: For media that has an orientation setting, this lets you change the rotation

of that media so that it’s correctly oriented. Four settings let you adjust by 0º, 90º right, 180º,

and 90º left.

�Input Sizing Preset: You can use this panel to assign a Sizing palette preset to select clips. For

example, if you have a special Input Format Preset for standard definition PAL widescreen clips

that you’ve edited into a high definition project, you can do a sort in the Media Pool to isolate

them, and then select them all and apply this preset.

�Field Dominance: By default, the Auto setting enables DaVinci Resolve to automatically determine

whether a particular clip is Upper- or Lower-field dominant. If this automatic determination is

wrong, you can choose Upper or Lower to manually override this.

�Enable Deinterlacing: (only available in Studio version) This checkbox is only enabled if “Enable

video field processing” is turned off in the Master Settings panel of the Project Settings. Turning

the Enable Deinterlacing checkbox on sets DaVinci Resolve to deinterlace clips using the

Deinterlace quality setting that’s located in the Image Scaling panel of the Project Settings.

Normal is a high-quality deinterlacing method that is suitable for most clips, while High is a more

processor-intensive method that can sometimes yield better results, depending on the footage.

The DaVinci Neural Engine option uses advanced machine learning algorithms to reconstruct the

frame, which will ideally give even better results than the High setting.

�Alpha Mode: The options presented here depend on the format of the clip you’ve selected, since

only certain formats (such as ProRes 4444, QuickTime Animation, OpenEXR, TIFF sequences, and

so on) are capable of containing alpha channels. If you’ve imported clips with embedded alpha

channels, this panel lets you enable or disable their use in DaVinci Resolve (by choosing None),

choose the type of alpha channel (Premultiplied or Straight), or invert the alpha channel. If you

select a clip that doesn’t contain an alpha channel, then most of these options don’t appear.

The Alpha Mode options that are available when a clip has an embedded alpha channel

�Super Scale High Quality Upscaling: For instances when you need higher-quality upscaling than

the standard Resize Filters allow, you can now enable one of three “Super Scale” options in the

Video panel of the Clip Attributes window for one or more selected clips. Unlike using one of the

numerous scaling options in the Edit, Fusion, or Color pages, Super Scale actually increases the

source resolution of the clip being processed, which means that clip will have more pixels than

it did before and will be more processor-intensive to work with than before unless you optimize

the clip (which bakes in the Super Scale effect into the optimized media), or cache the clip

in some way.


Ingest and Organize Media | Chapter 22 Modifying Clips and Clip Attributes

MEDIA

The Super Scale drop-down menu provides the options of 2-3-4x and 2-3-4x Enhanced, as well

as Sharpness and Noise Reduction options to tune the quality of the scaled result. Most of the

Super Scale parameters are in fixed increments, however the Enhanced modes let you apply

Super Scale in variable amounts. Selecting one of these options enables DaVinci Resolve to

use advanced algorithms to improve the appearance of image detail when enlarging clips by a

significant amount, such as when editing SD archival media into a UHD timeline, or when you find

it necessary to enlarge a clip past its native resolution in order to create a closeup.

You may find that, depending on the source media you’re working with, setting Sharpness to

Medium yields a relatively subtle result that can be hard to notice, but setting Sharpness to high

should be immediately more preferable, while also sharpening grain and noise in the image to an

undesirable extent at the default settings. However, while raising Noise Reduction will ameliorate

this effect, it will also diminish the gains you obtained by raising Sharpness. In these cases, it’s

worth experimenting with keeping Sharpness at Low or Medium so that Super Scale sharpens all

aspects of a clip, but then using the Noise Reduction tools of the Color page (with their additional

ability to be fine-tuned) to diminish the unwanted noise.

Super Scale options in the Video panel of the Clip Attributes window

TIP: Super Scale, while incredibly useful, is an extremely processor-intensive operation,

so be aware that turning this on will likely prevent real-time playback. One way to get

around this is to create a string-out of all of the source media you’ll need to enlarge

at high quality, turn on Super Scale for all of them, and then render that timeline as

individual clips, while turning on the “Render at source resolution” and “Filename uses >

Source Name” options.