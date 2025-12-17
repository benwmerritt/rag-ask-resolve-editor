---
title: "Customizing Preferences"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 292
---

# Customizing Preferences

Fusion Studio’s preferences configure Fusion’s overall application default settings and settings for

each new composition. Although you access and set these preferences through the Preferences

window, Fusion saves them in a simple text format called Fusion.prefs.

These default preferences are located in a \Profiles\Default folder and shared by all Fusion users on

the computer. However, you may want to allow each user to have separate preferences and settings,

and this requires saving the preferences to different locations based on a user login.

To change the saved location of the preferences file requires the use of environment variables.

Setting the Preferences Location

When you fist open Fusion, the environment variable FUSION_PROFILE_DIR defines the folder that

contains the Profiles folder. If this variable defines a valid path, then the preferences are saved to this

folder. If the FUSION_PROFILE_DIR does not exist, then Fusion attempts to create it. If it cannot create

the path, then the preferences are stored in the default Path Map location: AllData:\Profiles.

Typically, all users share the same preferences.If you want each user to save separate

preferences within their home folder, you must create another environment variable with the name

FUSION_PROFILE (e.g., FUSION_PROFILE=jane). Using this second environment variable, Fusion will

look for the preferences in the PROFILE_DIR of the user profile. Using a login script, you can make

sure the FUSION_PROFILE is set to the name of the logged in user.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Creating a Master Preferences File

When working with multiple Fusion users in a studio, you may want to standardize on a few settings.

Using the FUSION_MasterPrefs environment variable, you can create one or more site-wide

preferences in addition to your local personal preferences.

FUSION_MasterPrefs must contain the full path to at least one preferences file. If you have multiple

preferences paths, separate them using semicolons. Fusion does not write to these prefs files, and

they may contain a subset of all available settings. You may change settings in these files and use

them only where local prefs do not already exist unless you set the Locked flag.

Locking Preferences

If the line “Locked = true,” appears in the main table of a master file, all settings in that file are locked

and override any other preferences. Locked preferences cannot be altered by the user.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Chapter 76

Controlling Image

Processing

and Resolution

This chapter covers the overall image-processing pipeline.

It discusses color bit-depth and how to control the output resolution

in a resolution‑independent environment.

Contents

Fusion’s Place in the DaVinci Resolve Image-Processing Pipeline������������������������������������������������������������������������� 1588

Source Media into the Fusion Page������������������������������������������������������������������������������������������������������������������������������������������� 1588

Forcing Effects into the Fusion Page���������������������������������������������������������������������������������������������������������������������������������������� 1589

Output from the Fusion Page to the Color Page����������������������������������������������������������������������������������������������������������������� 1589

What Viewers Show in Different DaVinci Resolve Pages��������������������������������������������������������������������������������������������� 1589

Managing Resolution In Fusion�������������������������������������������������������������������������������������������������������������������������������������������������� 1590

Changing the Resolution of a Clip���������������������������������������������������������������������������������������������������������������������������������������������� 1590

Compositing with Different-Resolution Clips������������������������������������������������������������������������������������������������������������������������� 1591

Sizing Between DaVinci Resolve Pages����������������������������������������������������������������������������������������������������������������������������������� 1591

Color Bit Depths���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1592

Understanding Integer vs. Float�������������������������������������������������������������������������������������������������������������������������������������������������� 1592

Setting Color Depth in Fusion Studio��������������������������������������������������������������������������������������������������������������������������������������� 1593

Combining Images with Different Color Depths������������������������������������������������������������������������������������������������������������������ 1595

Advantages of Floating-Point Processing������������������������������������������������������������������������������������������������������������������������������ 1595


Fusion Fundamentals | Chapter 76 Controlling Image Processing and Resolution

FUSION

Fusion’s Place in the DaVinci Resolve

Image-Processing Pipeline

When working in a single unified environment like DaVinci Resolve, it is important to understand the

order of operations among the pages. DaVinci Resolve exposes some of this via the order of the page

buttons at the bottom of the screen, with the Media, Cut, and Edit page at the beginning of the chain

and the Color, Fairlight, and Deliver page at the end. However, this isn’t the whole story, especially

when it comes to the Fusion page. The following sections describe where the Fusion page fits in the

image-processing chain of DaVinci Resolve.

Source Media into the Fusion Page

For ordinary, single clips coming in from the Edit or Cut page, the MediaIn node in the Fusion page

represents the source media, as modified by the Clip Attributes window. Although you select the clip

from the Edit or Cut page Timeline, in the Fusion page, the clip is accessed from the Media Pool.

TIP: The decoding or debayering of RAW files occurs prior to all other operations, and as

such, any RAW adjustments will be displayed correctly in the Fusion page.

This means you have access to the entire source clip in the Fusion page, but the render range is set

to match the duration of the clip in the Timeline. You also use the full resolution of the source clip,

even if the Timeline is set to a lower resolution. However, none of the Edit or Cut page Inspector

adjustments carry over into the Fusion page, with the exception of the Lens Correction adjustment.

When you make Zoom, Position, Crop, or Stabilization changes in the Edit or Cut page, they are not

visible in the Fusion page. The same applies to any Resolve FX or Open FX third-party plugins. If you

add these items to a clip in the Edit or Cut page, and then you open the Fusion page, you won’t

see them taking effect. All Edit and Cut page timeline effects and Inspector adjustments, with the

exception of the Lens Correction adjustment, are computed after the Fusion page but before the

Color page. If you open the Color page, you’ll see the Edit and Cut page transforms and plugins

applied to that clip, effectively as an operation before the grading adjustments and effects you apply

in the Color page Node Editor.

With this in mind, the order of effects processing in the different pages of DaVinci Resolve can be

described as follows:

Source

Media

RAW

Debayering

Clip

Attributes

Fusion

Effects

Edit/Cut Page

Inspector

Adjustments

Edit/Cut

Plug-ins

Resolve FX

Color

Effects

TIP: Retiming applied to the clip in the Edit page Timeline is also not carried over into the

Fusion page.


Fusion Fundamentals | Chapter 76 Controlling Image Processing and Resolution

FUSION

Forcing Effects into the Fusion Page

There is a way you can force clips with Edit page Inspector adjustments, plugins, retiming, and Color

page grades into the Fusion page, and that is to turn that clip into a compound clip or a Fusion clip.

When Edit page effects and Color page grading are embedded within compound or Fusion clips,

MediaIn nodes corresponding to compound clips route the effected clip into the Fusion page.

However, bringing a compound clip or Fusion clip into the Fusion page changes the resolution of the

source clip to match the Timeline resolution. For more information, see the section “Sizing Between

DaVinci Resolve Pages” in this chapter.

Output from the Fusion Page to the Color Page

The composition output from the Fusion page’s MediaOut node are passed on via the Color page’s

source input, with the sole exception that if you’ve added plugins to that clip in the Edit or Cut page,

then the handoff from the Fusion page to the Color page is as follows:

Fusion

Effects

Edit/Cut Page

Inspector

Adjustments

Edit Page

Plugins

Color

Effects

What Viewers Show in Different

DaVinci Resolve Pages

Owing to the different needs of compositing artists, editors, and colorists, the viewers show different

states of the clip.

�The Edit page source viewer: Always shows the source media, unless you’re opening a

compound clip that’s been saved in the Media Pool. If Resolve Color Management is enabled, then

the Edit page source viewer shows the source media at the Timeline color space and gamma.

�The Edit page Timeline viewer: Shows clips with all Edit page effects, Color page grades,

and Fusion page effects applied, so editors see the program within the context of all effects

and grading.

�The Fusion page viewer: Shows Media Pool source clips at the Timeline color space and gamma,

including Resolve Color Management adjustments. but no Edit page Inspector adjustments or

Resolve FX effects and no Color page grades.

�The Color page viewer: Shows clips with all Edit page effects, Color page grades, and

Fusion page effects applied.


Fusion Fundamentals | Chapter 76 Controlling Image Processing and Resolution

FUSION