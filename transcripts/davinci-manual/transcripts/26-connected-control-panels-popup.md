---
title: "Connected Control Panels Popup"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 26
---

# Connected Control Panels Popup

In the lower-right corner of the DaVinci Resolve interface, you will find a Control Panels popup box.

Clicking on this icon shows you all currently connected control panels, how they are connected, and

their battery status.

The Control Panels popup


Setup and Workflows | Chapter 5 DaVinci Control Panels Setup

MEDIA

Chapter 6

Project Settings

This chapter covers the settings used for defining the properties of each individual

project. It’s a good idea to familiarize yourself with the information in this chapter

prior to setting up your first project.

Contents

What Are the Project Settings?������������������������������ 138

Opening and Editing Project Settings����������������� 138

Presets�������������������������������������������������������������������������������� 139

Master Settings���������������������������������������������������������������� 141

Timeline Format���������������������������������������������������������������� 141

Video Monitoring������������������������������������������������������������ 143

Optimized Media and Render Cache������������������� 144

Working Folders������������������������������������������������������������� 145

Frame Interpolation������������������������������������������������������ 146

Image Scaling������������������������������������������������������������������� 147

Image Scaling������������������������������������������������������������������� 147

Input Scaling��������������������������������������������������������������������� 148

Output Scaling����������������������������������������������������������������� 148

Color Management������������������������������������������������������� 149

Color Space and Transforms������������������������������������ 149

Dolby Vision™������������������������������������������������������������������� 150

HDR10+��������������������������������������������������������������������������������� 151

HDR Vivid����������������������������������������������������������������������������� 151

Lookup Tables������������������������������������������������������������������� 151

Broadcast Safe���������������������������������������������������������������� 153

General Options������������������������������������������������������������� 154

Conform Options������������������������������������������������������������ 154

Color������������������������������������������������������������������������������������� 156

Dynamics Profile�������������������������������������������������������������� 157

Versions������������������������������������������������������������������������������ 158

Camera Raw��������������������������������������������������������������������� 158

Capture and Playback������������������������������������������������� 159

Deck Settings������������������������������������������������������������������� 159

Capture������������������������������������������������������������������������������� 160

Playout��������������������������������������������������������������������������������� 160

Subtitles and Transcription���������������������������������������� 161

Fusion������������������������������������������������������������������������������������ 161

Fairlight������������������������������������������������������������������������������� 162

Timeline Sample Rate�������������������������������������������������� 162

Bussing������������������������������������������������������������������������������� 162

Audio Metering��������������������������������������������������������������� 162

Path Mapping������������������������������������������������������������������ 163

Project Media Locations��������������������������������������������� 164


Setup and Workflows | Chapter 6 Project Settings

MEDIA

What Are the Project Settings?

The Project Settings window contains all project-specific parameters that are saved along

with that project. These include essential project properties such as the timeline format, video

monitoring settings, how to optimize media, and where to save cache files. It also includes image

scaling properties, color management settings, and many other properties that affect projects in

fundamental ways.

Opening and Editing Project Settings

All of these project-specific settings are easily accessed from anywhere in DaVinci Resolve by clicking

the gear button at the bottom right of the page bar.

Project Manager and Project

Settings buttons

The Project Settings window opens in the middle of the screen.

Project Settings window


Setup and Workflows | Chapter 6 Project Settings

MEDIA

The Project Settings window is divided into a series of panels which can be selected from a sidebar

at the left. Each panel contains a collection of related settings that affects some category of DaVinci

Resolve functionality.

To alter project settings:


Click on the name of any group of settings in the sidebar at the left to open that panel.


Change whatever settings you need to change.


Do one of the following to apply your changes:

Click Save to apply the changes you’ve made and close the Project Settings.

Option-click Save to apply the changes you’ve made and keep the Project Settings window open,

so you can make other changes. This option is available because it’s sometimes necessary to

keep the Project Settings window open as you continue making changes that may visibly affect

the clips and timelines in your project.

Presets

The Presets menu lets you save customized collections of Project Settings for future recall. Presets

can save the state of nearly every parameter and setting in every panel of the Project Settings

window, and make it easy to switch among different setups for different tasks, or to accommodate

different types of projects.

The Presets menu is accessed by clicking on the option menu (three dots) in the upper-right corner of

the Project Settings window. The Presets menu shows the following items:

Project Settings Presets: The list of all current Project Presets is shown here, headed by the

Default Preset.

Set Current Settings as Default Preset: This option saves the current Project Settings as the new

Default Preset.

Save Current Settings as Preset:  This option allows you to save the current Project Settings as a

new preset that will show up in the menu list above.

Import Preset: This option will open a file browser to let you import a DaVinci Resolve Project

Settings Preset file. The extension for these files is .preset.

You can use this menu to create, import, and export your own presets, adding as many as you need to

accommodate the types of projects you work on.

The Presets Menu is accessed by clicking on the option

menu of the Project Settings window


Setup and Workflows | Chapter 6 Project Settings

MEDIA

To create a new preset:


Do one of the following:

�Right-click a project in the Project Manager, and choose Project Settings from the

contextual menu.

�Open any project, then open the Project Settings.


Use the different panels of the Project Settings window to alter whichever settings you need to.

There’s no need to save your changes as you go; you’ll save them all at once later.


Click on the option menu (three dots) in the upper right-hand corner of the Project

Settings window.


Select Save Current Settings as Preset.


Enter a descriptive name for your new preset in the dialog box, and press the OK button.


Your new preset name will now appear in the Project Settings Preset menu.

Once you’ve created one or more custom presets, you can load them into a project at any time.

To load a preset’s settings into a project:


Open a project with a preset you want to update.


Open the Project Settings window.


Click on the option menu in the Project Settings window.


Click on the Project Preset name you want to use for the open project.


Select Load Preset from the drop-down menu.

The Project Settings will be updated to the new preset immediately. There is no undo for this function.

To update a preset:


Open the Project Settings window.


Use the different panels of the Project Settings window to alter whichever settings you need

to update.


Click on the option menu in the Project Settings window.


Click on the Project Preset name you want to update.


Select Update Preset from the drop-down menu, and select Update from the dialog box.

The preset will be replaced with your current settings. There is no undo for this function.

To set the default preset:


Select the preset from the Project Settings Presets list you want to be loaded each time you make

a new project.


Click on the preset and select Set As Default Preset.

or


Select “Set Current Settings as Default Preset” from the option menu of the Project Settings

window to make whatever your project settings are currently the new default preset.


Select Update from the dialog box.

The preset will be replaced with your current settings. There is no undo for this function.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

To export a preset:


Click on the preset from the Project Settings Presets list you want to export.


Choose Export Preset from the drop-down menu.


Enter a name for the preset and where you want to save it in the file browser, and press Save.

The DaVinci Resolve Project Settings Preset file will export to that destination with a

“.preset” extension.

To import a preset:


Click on the option menu in the Project Settings window.


Select Import Preset.


Navigate the file browser to the DaVinci Resolve Project Settings Preset file you wish to import.

The file will have a “.preset” extension. Press Open.

To delete a preset:


Click on the preset from the Project Settings Presets list you want to delete.


Choose Delete Preset from the drop-down menu.


Press Delete in the dialog box.

The Project Settings will be deleted immediately. There is no undo for this function.