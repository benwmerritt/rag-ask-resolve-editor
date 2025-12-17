---
title: "User"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 21
---

# User

This panel lets you choose user preferences, specific to your workstation, that govern such things as

UI behaviors and appearance, auto save settings, editing and color defaults, control panel action, and

keyboard shortcut mappings.

TIP: Many of the settings in the User panel used to be found in the Project Settings window

prior to version 14, but they were moved here to accommodate collaborative workflows with

each user having their own independent general, editing, and color settings, as well as their

own keyboard shortcuts.

Saving User Preference Presets

It’s possible to save multiple presets for instant recall of different User Preference settings, using the

Option menu in the UI Settings window.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

The commands for managing User Preference presets in

the Option menu of the UI Settings window

Methods of managing User Preference presets:

�To save a preset: Choose whatever settings you want to use, then click the UI Settings window

Option menu, and choose Save User Preferences as Preset. Enter a name into the dialog, and

click OK. That preset will now appear at the top of the Option menu.

�To load a preset: Click the UI Settings window Option menu, and choose Load Preset from the

submenu of the preset you want to load.

�To update a preset: Load a preset you want to edit, then change whatever settings you need to,

and choose Update Preset from the submenu of that preset in the Option menu.

�To export a preset: Choose Export Preset from the submenu of any preset in the Option menu.

A file with the .userprefs extension is saved at the location you chose.

�To import a preset: Choose Import User Preferences as Preset in the Option menu, use the dialog

to find the exported .userprefs preset file you want to import, and click Open.

�To delete a preset: Choose Delete Preset from the submenu of any preset in the Option menu.

�To reset all presets: Choose Reset User Preferences from the Option menu to restore all User

Preferences to their default settings.

UI Settings

A collection of operational preferences.

�Language: A Language drop-down at the top lets you specify which language the DaVinci

Resolve user interface displays. DaVinci Resolve currently supports English, Chinese, Japanese,

Spanish, Portuguese, French, German, Italian, Russian, Thai, Vietnamese, and Korean.

�Reload last working project on startup: Automatically reopens the last project a user had open

whenever that user logs back into DaVinci Resolve. This checkbox can only be enabled when

editing a preset configuration in the Presets panel, so that it’s always on no matter which project

you open as long as you’re using that particular preset.

�Show focus indicators in the User Interface: Lets you enable or disable a red line at the top of

each panel that indicates which panel currently has focus.

�Use gray background for user interface: By default, DaVinci Resolve uses a blue-gray

UI background, intended to provide a more attractive experience for users focused on the less

color-critical aspects of DaVinci Resolve, namely editing. Turning this checkbox on switches

DaVinci Resolve to a totally neutral, desaturated gray UI, which can be valuable as a point of

reference for colorists concerned about the blue-gray UI’s potential to bias the eye in the dark

environment of the grading suite.

�Use gray background in viewers: When turned on, sets the background of all viewers to gray,

making it easier to evaluate image blanking or minor sizing adjustments than with the default

dark background.

�Resize image in viewer to square pixels: This control will select between using a square or

non‑square pixel aspect ratio within the Viewer. This is important when working with SD images

which do not have a square pixel aspect ratio.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

�Delay viewer display by X frames: When turned on, you can enter a number of frames to delay

DaVinci Resolve Viewers as they appear on your computer displays so that the image on your

computer display better syncs up with the same image shown on external displays that are

delayed due to various signal processing processes.

�Output single field when paused: This setting will reduce flicker when grading using a computer

monitor or when working with interlaced material. Ordinarily, when viewing interlaced material in

Stop or Pause mode, field one is displayed followed by field two. Depending on the image, this can

result in a flicker on the display. When this option is enabled, only field one will be shown on the

monitor when playback is paused; however both fields will be shown when the clips are played.

�Stop playback when a dropped frame is detected: When enabled, sets DaVinci Resolve to stop

playback whenever a frame is dropped on output, to warn you that there are performance issues

on your workstation. This is particularly useful when you’re outputting to tape.

�Stop renders when a frame or clip cannot be processed: When enabled, this will halt a render if

DaVinci Resolve detects an error in the encoding, rather than continue to try to process it.

�Show playhead shadow: Checking this box turns on the playhead shadow, a transparent orange

range used for visually measuring that extends a certain number of frames before and after the

playhead. The number of frames in the range before or after the playhead can be adjusted in the

Editing section of the User Preferences.

�2D timeline scrolling: Checking this box will scroll the Timeline vertically through all the Video or

Audio tracks when moving the mouse wheel. Unchecking this box will scroll the entire Timeline

horizontally when moving the mouse wheel.

�Timeline sort order: A user setting that allows you to determine the default sort order of the

Timelines that appear in the Viewer drop-down menus throughout DaVinci Resolve.

Alphabetic: Sorts Timelines alphabetically A-Z.

Creation Date: Sorts Timelines by oldest creation date first.

Recently Used (default): Sorts Timelines by the last 10 actively used timelines.

Project Save and Load

The Project Save and Load panel lets you control how projects are opened, and how they’re saved.

Load Settings

The Load Settings preference lets you control a key aspect of project opening performance, namely

whether or not all timelines within a given project are loaded into memory at the time of opening.

�Load all timelines when opening projects: To improve the performance of longer projects with

multiple timelines, the “Load all timelines when opening projects” checkbox in the Project Save

and Load panel of the User Preferences defaults to off.

When this checkbox is off, opening a project only results in the last timeline you worked on being

opened into memory; all other timelines are not loaded into RAM. This speeds up the opening

of large projects. However, you may experience brief pauses when you open other timelines

within that project, as each new timeline must be loaded into RAM as you open it. If you open

a particularly gigantic timeline, a progress bar will appear letting you know how long it will take

to load. Another advantage of this is the reduction of each project’s memory footprint, which is

particularly valuable when working among multiple projects using Dynamic Project Switching.

If you turn this on, all timelines will be loaded into RAM, and you’ll experience no pauses when

opening timelines you haven’t opened already. However, projects with many timelines may take

longer to open and save.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Save Settings

The Save settings allow you to control how DaVinci Resolve handles automated saving and

project backups. These features can save you from the heartache of lost work resulting from an

unexpected problem.

�Live Save: Enabled by default, Live Save is a progressive, fast, always-on autosave mechanism

that “saves as you go.” All changes in the Cut, Edit, and Fairlight pages are saved as you make

them. All changes in the Fusion and Color pages are automatically saved when you switch to

another clip, and also periodically and invisibly in the background while you work to ensure that

your work is saved even if you haven’t switched clips in a while.

�Project Backups: Turning on the Project Backups checkbox in the Project Save and Load panel

of the User Preferences enables DaVinci Resolve to save multiple backup project files at periodic

intervals, using a method that’s analogous to a GFS (grandfather father son) backup scheme.

This can be done regardless of whether or not Live Save is turned on. Each project backup is a

complete project file, excluding stills and LUTs.

Once you’ve enabled Project Backups for a long enough time, whatever saved project backups

have been created are retrievable in the Project Manager via the contextual menu that appears

when you right-click a project, by choosing Project Backups. Opening a project backup does not

overwrite the original project; project backups are always opened as independent projects.

Restoring a project backup in the Project Browser

�Timeline Backups: Turning on the Timeline Backups checkbox in the Project Save and Load panel

of the User Preferences enables DaVinci Resolve to save multiple backups of a timeline at periodic

intervals, using a method that’s analogous to a GFS (grandfather-father-son) backup scheme. This

can be done regardless of whether or not Live Save is turned on.

If you want to revert to a previous backup of a timeline, simply right-click on the timeline in the

Media Pool, select Restore Timeline Backup from the contextual menu, and choose the backup

from the list of options. Backups are organized by date and time, making it easy to find the specific

timeline you want to restore.

Restoring a timeline backup does not overwrite your current timeline. Instead the selected backup

will be brought into the Media Pool as a new timeline, with the name “Backup” appended to it.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Restoring a timeline backup in the Media Pool

Project and Timeline backups are only saved when changes have been made to a project.

If DaVinci Resolve sits idle for any period of time, such as when your smart watch tells you to

go outside and walk around the block, no additional project backups are saved, preventing

DaVinci Resolve from overwriting useful backups with unnecessary ones.

Three fields let you specify how often to save a new backup, while the fourth lets you choose

where the backups will be saved. These settings apply to both Project and Timeline backups.

Perform backups every X minutes: The first field specifies how often to save a new backup within

the last hour you’ve worked. By default, a new backup is saved every 10 minutes, resulting in six

backups within the last hour. Once an hour of working has passed, an hourly backup is saved and

the per-minute backups begin to be discarded on a first in, first out basis. By default, this means

that you’ll only ever have six backups at a time that represent the last hour’s worth of work.

Hourly backups for the past X hours: The second field specifies how many hourly project

backups you want to save. By default, two hourly backups will be saved for the current day. Past

that number, hourly backups will begin to be discarded on a first in, first out basis.

Daily backups for the past X days: The third field specifies for how many days you want to save

backups. The very last backup saved on any given day is preserved as the daily backup for that

day, and by default daily backups are only saved for two days. Past that number, daily backups

will begin to be discarded on a first in, first out basis. If you’re working on a project over a longer

stretch of time, you can always raise this number.

Backup location: Click the Browse button to choose a location for these backups to be saved.

By default they’re saved to a “ProjectBackup” directory on your scratch disk, although you could

change this to a volume that better fits into your data backup methodology. This folder contains

both Project and Timeline backups.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA