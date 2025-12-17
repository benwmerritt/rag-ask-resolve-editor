---
title: "Speed Effect Processing"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 199
---

# Speed Effect Processing

Once you’ve retimed a clip, you have the additional ability to change how the retimed clip is processed

in order to improve its visual playback quality, especially in the case of clips that are slowed down.

There are two ways you can set this. First, there’s a project-wide setting available in the Master

Settings of the Project Settings. Secondly, you can change how clips are retimed via a per-clip setting

available in the Inspector.

To change the Retime Process setting of an entire project:


Open the Project Settings and click to open the Master Settings panel.


Choose an option from the Frame Interpolation group Retime Process pop-up menu.

To change an individual clip’s Retime Process setting:

Select a clip, then open the Inspector and choose an option from the Retime Process pop-up in the

Retime and Scaling group. If you choose Optical Flow, you can also choose an option from the Motion

Estimation pop-up.

Here are the different options you have for processing speed effects:

Retime Process: Lets you choose a default method of processing clips in mixed frame rate timelines

and those with speed effects (fast forward or slow motion) applied to them, on a clip-by-clip basis.

The default setting is “Project Settings,” so all speed effected clips are treated the same way. There

are three options: Nearest, Frame Blend, and Optical Flow, which are explained in more detail in the

Frame Interpolation section of Chapter 4, “System and User Preferences.”

�Nearest: The most processor efficient and least sophisticated method of processing; frames are

either dropped for fast motion, or duplicated for slow motion.

�Frame Blend: Also processor efficient, but can produce smoother results; adjacent duplicated

frames are dissolved together to smooth out slow or fast motion effects. This option can provide

better results when Optical Flow displays unwanted artifacts.

�Optical Flow: The most processor intensive but highest quality method of speed effect

processing. Using motion estimation, new frames are generated from the original source frames

to create slow or fast motion effects. The result can be exceptionally smooth when motion in a

clip is linear. However, two moving elements crossing in different directions or unpredictable

camera movement can cause unwanted artifacts.


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT

Motion estimation mode: When using Optical Flow to process speed change effects or clips with

a different frame rate than that of the Timeline, the Motion Estimation pop-up lets you choose the

best-looking rendering option for a particular clip. Each method has different artifacts, and the highest

quality option isn’t always the best choice for a particular clip. The default setting is “Project Settings,”

so all speed effected clips are treated the same way. There are several options.

�“Standard Faster” and “Standard Better” are the same options that have been available in previous

versions of DaVinci Resolve. They’re more processor-efficient and yield good quality that are

suitable for most situations.

�“Enhanced Faster” and “Enhanced Better” should yield superior results in nearly every case where

the standard options exhibit artifacts, at the expense of being more computationally intensive, and

thus slower on most systems.

�“Speed Warp Faster” and “Speed Warp Better” are available for even higher-quality slow motion

effects using the DaVinci Neural Engine. Your results with this setting will vary according to the

content of the clip, but in ideal circumstances this will yield higher visual quality with fewer artifacts

than even the Enhanced Better setting.

Optical Flow Quality Settings Affecting Speed Effects

The “Motion estimation mode” pop-up in the Master Settings panel of the Project Settings let you

choose the tradeoff between quality and processing speed to use when processing optical flow-

based slow motion and frame rate retiming effects. The “Standard Faster” and “Standard Better”

settings are the same options that have been available in previous versions of DaVinci Resolve.

They’re more processor-efficient and yield good quality that are suitable for most situations. However,

“Enhanced Faster” and “Enhanced Better” should yield superior results in nearly every case where the

standard options exhibit artifacts, at the expense of being more computationally intensive, and thus

slower on most systems.


Editing Effects and Transitions | Chapter 51 Speed Effects

EDIT

Chapter 52

Subtitles and

Closed Captioning

DaVinci Resolve supports subtitles and closed captioning in sophisticated ways,

and the inclusion of automatic subtitling tools dramatically reduces the time and

effort required to build accurate subtitle tracks.

With dedicated subtitle/closed caption tracks that can be shown or hidden, subtitle file import

and export, sophisticated subtitle editing and styling at the track and clip level, and comprehensive

export options, adding subtitles and closed captions to finish your project is a clear and

straightforward workflow.

Contents

Subtitles and Closed Captioning Support����������������������������������������������������������������������������������������������������������������������������� 1084

Viewing Subtitle/Caption Tracks������������������������������������������������������������������������������������������������������������������������������������������������� 1084

Adjusting QC Thresholds For Subtitle/Caption Timing���������������������������������������������������������������������������������������������������� 1084

Importing Subtitles and Captions���������������������������������������������������������������������������������������������������������������������������������������������� 1086

Adding Subtitles and Captions Manually������������������������������������������������������������������������������������������������������������������������������ 1088

Create Subtitles from Audio (Studio Version Only)������������������������������������������������������������������������������������������������������������ 1090

Create Subtitles from Audio Language Support����������������������������������������������������������������������������������������������������������������� 1092

Editing Subtitles and Captions���������������������������������������������������������������������������������������������������������������������������������������������������� 1092

Styling Subtitles and Captions����������������������������������������������������������������������������������������������������������������������������������������������������� 1093

AI Animated Subtitles (Studio Version Only)�������������������������������������������������������������������������������������������������������������������������� 1096

Subtitle Tracks Using Fusion Templates for Styling����������������������������������������������������������������������������������������������������������� 1096

Linking Subtitles to Clips����������������������������������������������������������������������������������������������������������������������������������������������������������������� 1097

Using Subtitles in Nested Timelines������������������������������������������������������������������������������������������������������������������������������������������ 1098

Subtitle Regions���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1098

Adding and Deleting Subtitle Regions������������������������������������������������������������������������������������������������������������������������������������� 1098

Using Subtitle Regions��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1098

Naming Subtitle Tracks�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1100

Exporting Subtitles and Closed Captions������������������������������������������������������������������������������������������������������������������������������� 1101

Exporting Subtitles Via the File Menu���������������������������������������������������������������������������������������������������������������������������������������� 1101

Exporting Subtitles Via the Subtitle Track Header��������������������������������������������������������������������������������������������������������������� 1101

Exporting, Burning, or Embedding Subtitles During Delivery��������������������������������������������������������������������������������������� 1102


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

Subtitles and Closed Captioning Support

Subtitles are supported in DaVinci Resolve using specially typed subtitle tracks containing specifically

designed subtitle generators to add and edit subtitles for a program. Typically each subtitle track

corresponds to a single language or use, and you can change the name of a subtitle track to

reflect its contents.

Subtitle tracks can be locked, have Auto Select controls, and can be enabled or disabled like any

other track. Additionally, a special subtitle-only destination control lets you choose which subtitle track

to edit subtitle clips into. Furthermore, subtitle generator clips can be resized, moved, edited, and

overwritten like most other clips.

Subtitle track with lock, Auto Select, and enable/disable controls

Viewing Subtitle/Caption Tracks

One important difference between subtitle tracks and other kinds of tracks is that only one subtitle

track can be visible at any given time. That means if you have multiple subtitle tracks, each for a

different language, clicking the Enable control for one subtitle track disables all others.

Viewing one subtitle track at a time

Adjusting QC Thresholds For Subtitle/Caption Timing

To help you adhere to guidelines that specify the recommended duration, line length, and speed

of captions and subtitles, the Subtitles panel of the Project Settings has parameters you can set to

warn you when a particular subtitle clip exceeds thresholds of Characters Per Line, Minimum Caption

Duration, and Maximum Characters Per Second.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

The Subtitles Setup parameters in the Subtitles panel of the Project Settings

As you edit a subtitle clip, these thresholds are used to automatically calculate how many lines and

characters are allowable for a particular subtitle clip given its duration. For example, if you exceed the

calculated threshold, the CPS value of that caption turns red to warn you.

The CPS value of a subtitle has turned red because it

exceeds the current QC threshold

Adjusting QC Thresholds for Individual Subtitle Tracks

While setting the QC thresholds for subtitles in the Project Settings is usually fine for a single

deliverable, those deliverables with multiple subtitle tracks in different languages may need different

parameters for each track, allowing longer line lengths, time on the screen, etc. for the unique

characteristics of each language.

To individually adjust the subtitle settings per track:


Select the subtitle track you want to change in the Timeline.


Open the Inspector, and select the Track tab.


In the Subtitle Settings pane, uncheck Use Project Settings.


Make any necessary adjustments to the Max Line Length, Min Duration, and Max CPS controls.

These settings will now override the Subtitle Project Settings for the selected track only.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

The Subtitle Settings in the Track pane of the Inspector lets

you customize parameters for individual subtitle tracks.