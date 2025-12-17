---
title: "Project Notes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 18
---

# Project Notes

Each DaVinci Resolve project now provides access to Project Notes, which is a simple “scratch pad”

for keeping track of text notes associated with each project. These notes can be accessed using the

File > Project Notes command, and there’s also a Project Notes command in the contextual menu

for project icons in the Project Manager, which makes these notes accessible to everyone who’s

connected to that project library.

Dynamic Project Switching

Dynamic Project Switching is an option in the Project Manager contextual menu that lets you open

multiple projects into RAM simultaneously, so you can quickly switch between projects when you

want to copy and paste clips, timelines, and node settings back and forth. If you plan on opening

many projects, or even just a few very large projects, you should be sure your workstation has an

appropriate amount of RAM installed or you could experience a slowdown in performance.

Switching among open projects using the Project

Title drop-down at the top of the DaVinci Resolve UI

Methods of using Dynamic Project Switching:

�To enable Dynamic Project Switching: Open the Project Manager, right-click anywhere within

the Project Manager and choose Dynamic Project Switching so that it’s checked. Dynamic Project

Switching will remain enabled until you turn it off.

�To open multiple projects in RAM: Open any project, then reopen the Project Manager and open

any other project. All projects you open are kept available in RAM.

�To switch among open projects: Choose File > Switch Project and select the project you want to

switch to from the submenu. You can also choose other projects that have been opened into RAM

from the drop-down menu that appears to the right of the project name at the top center of the

DaVinci Resolve user interface.

�To close a specific project: Choose File > Close Project and select the project you want to close

from the submenu. You may be prompted to save, after which the project closes.

�To close all other open projects: Open the Project Manager. All open projects appear with a

check mark in the upper right-hand corner; the currently open project has an orange corner

mark, while other projects open in memory have a gray corner mark. Right-click anywhere within

the Project Manager, and choose Close Projects in Memory to close all projects other than the

current one.


Setup and Workflows | Timeline Backups Managing Projects and Project Libraries

MEDIA

Using dynamic project switching, you can do the following:

�Copy and paste clips from the Media Pool of one project into another.

�Copy and paste timelines from the Media Pool of one project into another. When you paste a

timeline from another project, all of the clips used in that timeline will be pasted to the same

location as well.

�Copy and paste clips from a timeline in one project to a timeline in another.

�Copy a node’s settings from one project and paste them to a node in another project.

You can also copy and paste clips, timelines, and node settings from one project to another

without using dynamic project switching, but using switching makes this process faster.

Archiving and Restoring Projects

DaVinci Resolve has a convenient feature for quickly archiving every single media file used by

a project, including subtitle files, along with the project itself, to a single location. This can be done to

hand a project off to another DaVinci Resolve user, or to bundle a project and its media up for either

short- or long-term archiving using the backup methodology of your choice. The process is simple.

To Archive a project:


Open the Project Manager.


Locate and right-click the project you want to archive, and choose Archive.

The contextual menu command

for archiving projects


When the Archive Project window appears, choose a location to save the archive. Make sure you

choose a volume that’s large enough to accommodate the size of all the media from the project

you’re archiving, and click Save.


Setup and Workflows | Timeline Backups Managing Projects and Project Libraries

MEDIA


When the Archive dialog appears, verify the location the archive will be saved to, and choose

which optional media you want to save within the archive. You can optionally save Optimized

media and/or Render Cache media associated with a project.

A dialog letting you choose whether to save

Optimized and/or Render Cache media


Click Ok, and a dialog with a progress bar will show you how long the archive operation will take

to finish. If any errors come up, resulting from missing or offline media, they’ll be presented at the

end of the process.

The resulting archive that is written is a directory with the .dra file extension. Inside this folder are a

series of subdirectories containing all of the media that’s used by the archived project. Each directory

of media files used is saved within a directory path that mirrors the exact path it came from, so you

have a reference for where each clip came from originally.

To restore an Archived project:


Copy the .dra archive directory you want to restore to the volume where you want those media

files to be. Restoring doesn’t move this directory, it only adds the project file within to the Project

Manager, so you should make sure the .dra archive directory is located on a storage volume with

suitable performance for you to work.


Open the Project Manager, right-click anywhere, and choose Restore from the contextual menu.

Choose the .dra archive directory you just copied, and click Open.


At the prompt, enter a unique project name for the restored project, and click OK. The project is

restored to the Project Manager, and remains linked to the media located inside the .dra archive.


Alternatively you can simply drag the .dra folder from your file system directly into the

Project Manager.

If, after restoring an archive, you want to move its media to another location, you can use

Media Management to do a move operation for all clips in that project. For more information

on Media Management, see Chapter 46, “Media Management.”


Setup and Workflows | Timeline Backups Managing Projects and Project Libraries

MEDIA

Chapter 4

System and

User Preferences

This chapter covers the settings used for customizing the DaVinci Resolve

environment. System Preferences govern setup options that control the

hardware and software environment, while User Preferences control various

user controls within the software.

Contents

DaVinci Resolve Preferences������������������������������������ 97

Adjusting Preferences��������������������������������������������������� 97

Resetting Preferences��������������������������������������������������� 98

System����������������������������������������������������������������������������������� 98

Memory and GPU������������������������������������������������������������� 98

Media Storage������������������������������������������������������������������� 99

Decode Options�������������������������������������������������������������� 101

Video & Audio I/O���������������������������������������������������������� 102

Video Plugins������������������������������������������������������������������� 105

Audio Plugins������������������������������������������������������������������� 106

Control Panels����������������������������������������������������������������� 108

General������������������������������������������������������������������������������� 108

Internet Accounts����������������������������������������������������������� 109

Advanced��������������������������������������������������������������������������� 109

User��������������������������������������������������������������������������������������� 110

Saving User Preference Presets������������������������������ 110

UI Settings���������������������������������������������������������������������������� 111

Project Save and Load�������������������������������������������������� 112

Cache Management������������������������������������������������������ 115

Editing����������������������������������������������������������������������������������� 115

Color�������������������������������������������������������������������������������������� 118

Fairlight������������������������������������������������������������������������������� 120

Playback Settings������������������������������������������������������������ 121

Control Panels������������������������������������������������������������������� 121

Metadata���������������������������������������������������������������������������� 122

Keyboard Customization������������������������������������������� 123

Choosing Keyboard Shortcut

Emulation Presets���������������������������������������������������������� 123

Viewing Commands Assigned

to Specific Key Combinations����������������������������������� 124

Searching for Keyboard Shortcuts������������������������ 125

Managing Keyboard Mappings������������������������������� 126

Remapping a Command to One or More Keys 126

DaVinci Resolve Extras Download Manager�� 129


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

DaVinci Resolve Preferences

The DaVinci Resolve Preferences window contains workstation-specific settings for customizing how

DaVinci Resolve works, divided into System and User panes, selectable via buttons at the top of

this window.

To open the Project Settings window, do one of the following:

�Choose DaVinci Resolve > Preferences.

�Press Command-Comma.

TIP: You can open the preferences while the Project Manager is open when you first run

DaVinci Resolve by pressing Command-Comma.

System Settings of the Preferences window

Adjusting Preferences

The System and User panes are each divided into a series of panels which can be selected from a

sidebar at the left. Each panel contains a collection of related settings that affects some category of

DaVinci Resolve functionality.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

To alter any preference setting:


Click on the name of any group of settings in the sidebar at the left to open that panel.


Change whatever settings you need to change.


Click Save to apply the changes you’ve made and close the Preferences window.

If you’ve updated certain System Preferences, you’ll be prompted to restart DaVinci Resolve,

but if you’ve updated the User Preferences, this will probably be unnecessary.