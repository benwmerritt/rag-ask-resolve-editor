---
title: "Local Project Libraries"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 751
---

# Local Project Libraries

Local project libraries are the simplest and most common type of project library and require no

additional set up or configuration by the user, other than installing DaVinci Resolve. These libraries are

saved locally to your workstation; by default they are placed in a folder called Resolve Disk Database,

though they can be placed manually anywhere on your file system.

Creating a New Local Project Library

Creating a new local library is a simple and straightforward process.

To Create a New Local Project Library:


Click on the Show/Hide Project Libraries icon in the upper left of the Project Manager

to expose the sidebar.


Select the Local icon from the Project Library options.


Click on the “Add Project Library” button at the bottom of the sidebar.


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER


Select the Create option to make a new project library.


Enter a new name for your project library.


Press the Browse button next to Location, to select where on your local computer to save the

project library.


Press the Create button.

You can now create or import new projects directly into your new local project library.

Creating a local project library

Connecting to an Existing Local Project Library

You can reconnect to an already existing project library using the following steps.

To connect to an existing project library:


Click on the Show/Hide Project Libraries icon in the upper left of the Project Manager, to expose

the sidebar.


Select the Local icon from the Project Library options.


Click on the “Add Project Library” button at the bottom of the sidebar.


Select the Connect option to access the existing project library.


Enter a new name for your project library.


Press the Browse button next to Location, to select where on your local computer the folder

containing the existing project library is. It is commonly named “Resolve Disk Project library.”


Press the Connect button.

You can now view and use all the existing projects directly from the existing local project library.

Connecting to an existing local project library


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER

Disconnecting from a Local Project Library

You can disconnect and remove an already existing project library from the Project Libraries list using

the following steps.

To disconnect from a project library:


Click on the Show/Hide Project Libraries icon in the upper left of the Project Manager to expose

the sidebar.


Select the Local icon from the Project Library options.


Right-click on the project library that you want to disconnect from, and select disconnect from the

context menu.


Press the disconnect button in the confirmation dialog.

Disconnecting a project library simply removes it from the available options in the Project Libraries

sidebar. It does not delete the project library. You can either manually delete it in the OS filesystem, or

reconnect to it using the steps described in Connecting to an Existing Local Project Library.

Duplicating Project Libraries

Local Project Libraries can be duplicated in the same database for backup or iteration purposes.


Right-click on the Library, and select Duplicate from the dropdown menu.


Select the Resolve Database Folder in the file system browser. This can either be the same one

you use for the original project or a new one.


Click on the Open button.


Rename the new Library in the Clone Library dialog.

Backing up a Local Project Library

You can also back up project libraries by exporting them, and then reimport them later.

To backup/export a project library:


Select the project library you want to back up.


Click the Display Project Library Details icon (the circled letter “i” to the right of the project library).

The Display Project

Library Details icon


Select the Back Up button.


Choose a location to which to save the backup in the Backup Project Library dialog, and

click Save.


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER

Restoring a Local Project Library

You can import existing project libraries to pass multiple projects between systems.

To restore/import a project library:


Click the Restore button at the top of the Project Libraries sidebar.

The Restore button


Find the project library you need to import using the file import dialog, and click Open.


In the Add Project Library dialog, do the following:

a)	 Type a name for the new project library into the Name field. This will rename the imported

project library but will not alter its contents. You can also name it the same as the original

project library.

b)	 Click within the Location field and use the Filesystem navigation dialog to choose the

directory that contains the existing DaVinci Resolve project libraries.


Click Create, and the imported local project library will appear in the Local section of the Project

Libraries sidebar.

Upgrading a Local Project Library

Selected libraries display an upgrade warning in the Project Manager only when you’ve installed a

new version of DaVinci Resolve and you have project libraries that were created in older versions of

DaVinci Resolve that need upgrading.

The upgrade warning in the Project Manager indicates that project library needs to be upgraded.

It’s generally a good idea to back up a project library prior to upgrading it, in case something

goes wrong. In general, upgrading from a whole version release to the next whole version release

of DaVinci Resolve usually requires an upgrade, while upgrading to a dot release of the same

version may or may not. If the currently used project library requires an update, you’ll be told on

application startup.


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER

To upgrade a project library from an old version of DaVinci Resolve:

Click on a project library that needs updating, and select the Upgrade Project Library button.

A dialog appears to confirm if you really want to upgrade that project library. Click Upgrade

to proceed.

Network Project Libraries

Multiple DaVinci Resolve workstations can access the same project when you set up a Project Server

that shares one or more network project libraries over a local network. Once you’ve set this up, there

are two ways of using a shared project library.

Multiple Users Sharing Projects

The simplest case is for users to simply open up a project on the Project Server and work on it.

Working this way, if you ever have to change rooms, or switch workstations, you can easily open that

same project from any machine that’s connected to the server on the same network without needing

to export and import it first. For example, an assistant could be working with a colorist to prepare files

for the next reel by conforming shots, managing VFX replacements, doing dust busting repairs, and so

on in an unsupervised editing suite anywhere in the building, before saving their work and closing the

project so the colorist can immediately open that same project in the grading theater across the hall.

Another way of taking advantage of shared Project Servers is to split large projects into sections, so

multiple artists can work in parallel on different pieces of the whole in different suites, handing them

off when necessary. For example, a feature film may be split into reels, or a film can be separated from

the trailer and electronic press kit projects that it shares media with. In this case, each project can be

edited, mixed, and graded by different people accessing the Project Server.

When a shared project is opened by someone else after it’s already been opened, a dialog informs

you that it’s being opened in Read-only mode to prevent multiple users from accessing the project at

the same time. If you load a Read-only project and decide you want to make changes anyway, you’ll

need to use the Save As command to create a duplicate project file using a new name in order to

preserve your work.

Using Collaborative Workflow for Network Project Libraries

Alternately, you can use the Collaborative Workflow features in DaVinci Resolve to enable multiple

collaborators on multiple workstations in multiple rooms to open and work on the very same project at

the same time. For example, an editor can be editing a project’s main timeline in one room, while an

assistant organizes media and adds metadata within the same project in another room, and a colorist

grades dailies in that same project in yet another room, all accessing the same Project Server which

allows them to work together in parallel.

For more information, see Chapter 197, “Collaborative Workflow.”

All participants in a Collaborative Workflow must be using a network project library on a

Project Server that’s properly set up.


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER