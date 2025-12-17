---
title: "Working with Versions"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 589
---

# Working with Versions

Each clip can have as many local and remote versions as you like. There are commands for creating,

renaming, and deleting the versions that are available to each clip when using the pointer or

keyboard shortcuts.

Additionally, DaVinci Resolve 15 introduced the ability to batch create, rename, load, and delete

versions for multiple clips that are selected at the same time.

To create a new local or remote version

quickly for one or more selected clips:

�Choose Color > Grade Version > Add (Command-Y).

A new version is created, identical to the type of version that was previously selected (remote

or local), named “Version x” where x is the number of the versions that have been created. All

keyframes and motion tracking are copied from the previously selected version to the new one.

To create a new version for one or more selected clips,

with the option to set a name and whether to copy keyframes:


Right-click one of the selected clip thumbnails, and choose one of the following:

�Local Versions > Create New Version

�Remote Versions > Create New Version


Type a name for the version in the dialog that appears, and choose either “Copy all marks” or

“Copy the first mark only,” depending on whether or not you want to copy all the keyframes into

the new version.

NOTE: Motion tracking will be copied regardless of whether “Copy all marks”

is selected or not.


Color | Chapter 142 Grade Management

COLOR


Optionally, you can choose one of the preset version names from the drop-down list. These

names are defined in the Versions section of the General Options panel of the Project Settings.


Click OK.

To delete a specific version for one or more selected clips:

�Right-click one of the selected clip thumbnails, choose the submenu of the remote version you

want to delete (it can’t be the currently selected version), and choose Delete.

To delete all versions for one or more selected clips:

�Right-click one of the selected clip thumbnails, and choose one of the following commands from

the contextual menu corresponding to the scope of the versions you want to delete;

�Local Versions > Delete All Versions

�Remote Versions > Delete All Versions

�Delete All Versions

All versions are deleted as specified, except for the currently selected version, which is now the only

one remaining.

To load a particular remote or local version for one or more selected clips:

�Right-click one of the selected clip thumbnails, choose the submenu of the corresponding remote

version you want to copy, and choose Load.

To rename the version of one or more selected clips:


Right-click one of the selected clip thumbnails, choose the submenu of the corresponding remote

version you want to rename, and choose Rename.


In the Version Name dialog, type a name into the text field. Optionally, you can choose one of the

preset version names from the drop-down list. These names are defined in the Versions section of

the General Options panel of the Project Settings.

Selecting a Version name from the dropdown list, the names

on the list come from assignments made using the Versions

section of the General Options panel of the Project Settings


Click OK.

That name now appears underneath the clip thumbnail in the Timeline.


Color | Chapter 142 Grade Management

COLOR

If you’re going to use predefined names for versions, you need to define these in the Versions group

of the General Options panel of the Project Settings. Ten drop-down menus let you choose from

preset version names, or enter your own. These names will appear in the drop-down menu of the

Version Name dialog.

The Versions section of the Project Settings

The Importance of “Version 1”

There are specific operations in DaVinci Resolve where “Version 1,” otherwise known as “the default

version,” is the only version that’s used, regardless of how many other versions are available, or which

version was previously selected. The default version can be named anything you want, but whatever

its name, the default version is the first version in the list, and it’s important. Here are some examples:

Importing additional timelines that use the same clips: In this case, if you’re importing

timelines and ”Use local version for new clips in timeline” is disabled in the Color section of

the General Options panel of the Project Settings, then only the default version of each clip is

relinked.

Whenever you switch a timeline between local and remote versions: In this case, every

clip in the Timeline will be switched to the default version, regardless of what you had

selected previously.

Consequently, if you plan to reconform your clips to a newer version of the edit that you’re importing,

or pursue other workflows that are off the beaten path, it’s a good idea to make sure, no matter

how many versions you end up creating, that the most important grade is always copied back to the

default version.

To copy any version quickly to the default version:


Choose Color > Memories > Save Memory A (Option-1). You can use any memory you want, but

Memory A is convenient for this example.


Choose Color > Grade Version > Default (Command-U).


Choose Color > Memories > Load Memory A (Command-1) to apply the saved memory to the

default version.

To jump immediately to the default version, do one of the following:

�Choose Color > Grade Version > Default (Command-U).

�Press DEFAULT VERSION on the T-bar panel.


Color | Chapter 142 Grade Management

COLOR

Deleting Unused Versions

In cases where you want to make absolutely sure there’s no alternative to the grade you want a clip to

have, there’s an easy way to delete all versions except for the version that’s currently in use, thereby

making it the default version.

To eliminate either local or remote versions except for the current version:


Choose the local or remote version you want a clip to use.


Right-click the thumbnail of the clip you want to eliminate extra versions from, and choose Delete

Unused Versions from the contextual menu.

If you selected a local version, all unused local versions will be deleted, but remote versions will be left

alone. Similarly, if you selected a remote version, all unused remote versions will be deleted, but local

versions will be left alone.

To eliminate all other local and remote versions except for the current version:


Choose the version you want a clip to use.


Right-click the thumbnail of the clip you want to eliminate extra versions from, and choose Delete

All Versions from the contextual menu.

Regardless of whether you selected a local or remote version, all other local and remote versions

not in use will be deleted.

Rendering Versions

When the time comes to render your clips in the Deliver page, each clip’s currently selected version

will be rendered. If you need to render a different version for a given clip, you can either make sure it’s

selected in the Color Page timeline before you open the Deliver page, or use the Versions submenu

in the Color mode of the Deliver page Thumbnail timeline. This contextual menu also provides access

to the Stereo 3D commands, the Edit PAR (Pixel Aspect Ratio) command, and a command for updating

the Render Window Timeline thumbnails to reflect any changes you’ve made in case they haven’t

updated automatically.

Additionally, the Commercial Workflow output option, located in the Deliver page, provides

a method of rendering multiple versions for each clip when outputting your project in Source

Order (as individual media files). There are two additional options in the Version submenus of

each clip in the Thumbnail timeline contextual menu that let you control which versions are

rendered when you use Commercial Workflow.

Render Disabled: Turning this option on excludes that version from being rendered when

Commercial Workflow is enabled.

Enable Flat Pass: Turning this option on forces the selected version to render with the grade

turned off, essentially outputting the original media.

For more information on rendering versions using the Commercial Workflow option,

see Chapter 187, “Rendering Media.”


Color | Chapter 142 Grade Management

COLOR

Copying Grades

There are various methods you can use to copy grades from one clip to another. Which is appropriate

to your need depends on your style of working with DaVinci Resolve.

Protecting Adjustments with the Copy Grade Options

Before going into the myriad of ways that grades can be copied from one clip to another, you should

know of a series of options, available from the contextual menu of the Gallery (right-click anywhere

in the gray area of the Gallery), that let you carefully specify grading, sizing, and stereo data to be

preserved when overwriting grades in clips you’re copying to. There are three options:

Copy Grade: Preserve number of nodes: Lets you choose 0–10 nodes to be protected when applying

a grade. When set to 1, the first node of the copied grade is ignored, but all other nodes are copied.

When set to 5, the first five nodes of a copied grade are ignored, as long as there are at least five

nodes in the grade of the clip you’re copying to. This option is useful for colorists who routinely use

the first few nodes for shot matching and scene balancing, with additional nodes applying individual or

stylistic adjustments.

Copy Grade: Preserve Camera Raw Settings: When enabled, the camera raw Source settings of the

current clip are preserved, letting you apply stylistic grades from unrelated clips without overwriting

clip-specific source settings.

Copy Grade: Preserve Input Sizing: When enabled, Input Sizing adjustments are not overwritten by

those of the copied grade.

Copy Grade: Preserve Convergence: When enabled, Convergence adjustments in the

Stereo 3D palette are not overwritten by those of the copied grade.

Copy Grade: Preserve Floating Windows: When enabled, Floating Windows adjustments in the

Stereo 3D palette are not overwritten by those of the copied grade.

Copy Grade: Preserve Auto Align: When enabled, Auto Alignment adjustments in the

Stereo 3D palette are not overwritten by those of the copied grade.

Copy Grade: Preserve Dolby Vision™ Analysis Metadata: When enabled, Dolby Vision Analysis

Metadata is not overwritten by that of the copied grade. Only available if you’re set up to do Dolby

Vision grading.

For more information, see Chapter 9, “Data Levels, Color Management, and ACES.”

Copy Grade: Preserve Dolby Vision™ Trim Metadata: When enabled, Dolby Vision Trim Metadata in

the Dolby Vision palette is not overwritten by that of the copied grade. Only available if you’re set up

to do Dolby Vision grading.

For more information, see Chapter 9, “Data Levels, Color Management, and ACES.”


Color | Chapter 142 Grade Management

COLOR