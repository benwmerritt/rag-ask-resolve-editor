---
title: "Searching for Projects"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 16
---

# Searching for Projects

Clicking the magnifying glass button at the upper right-hand corner of the Project Manager exposes

the Search Options, which can be used to locate one or more projects based on the metadata that’s

selected in the Filter By drop-down menu to the right of it.

Search field open with Filter by search criteria selected

Using the drop-down menu, you can choose to search by name, or by project format. Once you’ve

chosen a criteria, begin typing into the search field, and the Project Manager will immediately and

dynamically begin to be filtered by your search text.

Organizing Projects in Folders

If you’re organizing a lot of projects, you can create folders to put them into.

A folder in the Project Manager

Methods of working with project folders:

�To create a folder: Click the New Folder button, then enter a name into the Create New Folder

dialog and click Create.

�To delete a folder: Right-click a folder, choose Delete, and click Yes when prompted. All projects

inside a deleted folder will be deleted as well.

�To rename a folder: Right-click a folder, choose Rename, then enter a new name and click OK.

�To copy a folder: Right-click on a folder and choose Copy from the drop-down menu, or select the

folder and press Command-C. Any projects enclosed inside that folder will also be copied.

�To paste a folder: Once a copy operation has been made, right-click on the background of the

Project Manager and choose Paste from the drop-down menu, or press Command-V. You can

paste into other project libraries, into other folders, or into the same location where a new version

of the folder will have the word (Copy) appended to it. All enclosed timelines will copy over as well.

�To open a folder: Double-click a folder to open it and view its contents. At the upper left-hand

corner of the Project Manager, a folder path view shows you which folder is open, as well as where

you are within a nested series of folders if that’s what you’ve set up.

�To exit a folder: Use the path control at the top of the Project Manager to click on a higher level

in the folder hierarchy.

�To move a project into a folder: Drag the project onto a folder icon, and drop it to place it

inside the folder.

�To move a project out of a folder: Open a folder, select one or more projects you want to move,

then right-click the selection and choose Cut from the contextual menu. Then, navigate to the next

place in the Project manager where you want to place the cut projects, right-click the background

of the Project Manager, and choose Paste. The projects should appear in the new location.


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA

Managing Project Libraries

Unlike other applications which save self-contained project files to user-specified locations

wherever you like in your file system, DaVinci Resolve takes a more centrally organized approach to

project management, using project libraries. By default, DaVinci Resolve uses a local project library

to keep track of every project you create. The Project Libraries sidebar lets you manage the projects

found within this project library, which are saved to a specific directory on your system (particular

to that project library). The default location of this local project library depends on the operating

system you use.

However, you can create additional project libraries with which to store other projects, if you like.

For example, you might create one project library each for each year in which you work. If you

work on series television, you could create multiple project libraries for each program you work

on. Or, you could create separate project libraries for each client you do work for. There’s no hard

and fast rule; ultimately how you use project libraries is entirely up to you and your individual

organizational preferences.

Project Library Types

Project libraries can be stored in three different project library types which work similarly in function

but have additional connectivity and sharing features based on your networking setup. You select the

Library Type at the top left of the Project Manager.

�Local: Stores your project libraries locally on your workstation. This is the default and is best for

individual users or single systems.

�Network: Stores your project libraries on an external computer that is connected to several

workstations on the same local network. It also allows you to control user access to the project

library. This is best for a facility composed of multiple workstations in the same building working

on the same material.

�Cloud: Stores your project libraries in the Blackmagic Cloud. This allows several workstations

to connect to the same project library over the internet. It also allows you to control user access

to the project library. This is best for multiple people working on the same project from different

locations around the world.

The three types of project libraries: local, network, and cloud.

For more information about setting up and configuring the different project library types,

see Chapter 196, “Managing Project Libraries and Project Servers.”


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA

Opening the Project Libraries Sidebar

If you already have multiple project libraries, then clicking the button at the upper-left hand corner of

the Projects Browser reveals a sidebar at the left of the Project Manager that lists every project library

on your workstation, with various options for managing these project libraries and for browsing the

projects found within them.

You can use this sidebar to open different project libraries and browse the projects

found inside.

Project Libraries

sidebar button

Project Manager with the Project Libraries sidebar displayed

Moving Projects From One Project Library

to Another on the Same Workstation

If you’ve used multiple project libraries to organize your projects, you can browse the contents of each

project library to search for what you’re looking for, and then copy one or more projects from one

project library to another if you need to rearrange how they’re organized.


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA

To view the contents of a project library:


Click the button at the upper-left hand corner of the Projects window to open the Project

Libraries sidebar.


Click to select a project library in the sidebar, and an orange highlight will appear

If you had a project already open, you’ll be asked if you want to save it before closing, because

all open projects must be closed prior to viewing the contents of another project library. Then,

the projects corresponding to that user within the selected project library appear in the Project

Manager window.

To import a project from another project library using the Project Libraries sidebar:


Click the button at the upper-left hand corner of the Projects window to open the Project

Libraries sidebar.


Click to select a project library in the sidebar, and if necessary use the drop-down menu at the

right of the project library listing to choose a specific user. The projects corresponding to that user

within the selected project library appear in the Project Manager window.


Select a project you want to import, and press Command-C to copy it.


Click to select the current project library again (the project library you want to work within).


Press Command-V to paste the project you copied. A copy appears in the current project library.

For more details on shared project library setup and operation, see Chapter 196, “Managing

Project Libraries and Project Servers.”

To import Project Settings from another project using the Project Libraries sidebar:


Click the button at the upper-left hand corner of the Projects window to open the Project

Libraries sidebar.


Select a project you want to import Project Settings to so that it’s highlighted.


Right-click any project and choose “Load Project Settings to Current Project.” That project’s

settings will be copied to the project you selected in step 2.

Managing Project Libraries in the Project Libraries Sidebar

Controls within the Project Libraries sidebar make it easy to create new project libraries (via the button

at the bottom), upgrade project libraries that have been flagged (via circular badges), import and

export project libraries (via buttons at the top), and reveal additional information about each project

library (via buttons at the top of this sidebar).

Project Libraries sidebar controls

The three controls at the top of the Project Libraries sidebar have the following functions:

�Sort Order drop-down menu: This menu lets you choose how to sort the various local and

network project libraries displayed in the sidebar. You can sort by Project Library Name, Schema

(by date), Status, or Location in Ascending or Descending order.


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA

�Restore: Imports .resolve.backup files to restore a backed up project library.

�Show Search Field: Displays a search field and search criteria drop-down that lets you search for

project libraries in the sidebar by Name, Schema, Status, or Location.

Clicking on the Display Project Library Details icon (the circled letter “i” to the right of the project

library),  shows additional information underneath each project library in the sidebar. What

information depends on the type of project library. Local project libraries display their status

(compatible/incompatible) and location (directory path). Network and cloud project libraries display

their schema (created and modified dates), their status (compatible/incompatible), their IP location,

and below any members that have access to the project library.

Creating and Connecting to Project Libraries

You can use local, network, and cloud libraries side by side for switching to the use of one or the

other, depending on your needs. These instructions will show you how to set up local project libraries.

Network and cloud libraries require additional configuration and setup first.

For more details on network and cloud project libraries setup and operation, see Chapter 196,

“Managing Project Libraries and Project Servers.”

To create a new local project library:


Click the button at the upper-left hand corner of the Projects window to open the Project

Libraries sidebar.


Click the Add Project Library button at the bottom of the sidebar.


Click on the Create tab. The Add Project Library window should look like the following screenshot:

Creating a local project library


In the remaining fields, do the following:

a)	 Type a name for the new project library into the Name field

b)	 Click within the Location field and use the Filesystem navigation dialog to choose where to

put the directory that will contain all of the DaVinci Resolve project directories


Click Create, and the new local project library will appear in the local project library section of the

Project Libraries sidebar.


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA

To connect to an existing local project library:


Click the button at the upper-left hand corner of the Projects window to open the Project

Libraries sidebar.


Click the Add Project Library button at the bottom of the sidebar.


Click on the Connect tab. The Add Project Library window should look like the following screenshot:

Connecting to an existing local project library


In the remaining fields, do the following:

a)	 Type a name for the new project library into the Name field.

b)	 Click within the Location field and use the Filesystem navigation dialog to choose the location

of the existing project library you wish to connect to.


Click Connect, and the new local project library will appear in the local project library section of

the Project Libraries sidebar.

Duplicating Project Libraries

Local Project Libraries can be duplicated in the same database for backup or iteration purposes.


Right-click on the Library, and select Duplicate from the drop-down menu.


Select the Resolve Database folder in the file system browser. This can either be the same one

you use for the original project or a new one.


Click on the Open button.


Rename the new Library in the Clone Library dialog.

Backing Up and Restoring Project Libraries

You can also back up project libraries by exporting them, and then reimport them later.

To backup/export a project library:


Click the button at the upper-left hand corner of the Projects window to open the Project

Libraries sidebar.


Select the project library you want to back up.


Click the Display Project Library Details icon (the circled letter “i” to the right of the project library).

The Display Project Library Details icon


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA


Select the Back Up button.


Choose a location to which to save the backup in the Backup Project Libraries dialog, and

click Save.

To import a project library:


Click the button at the upper-left hand corner of the Projects window to open the Project

Libraries sidebar.


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

Upgrading Project Libraries

Selected libraries display an upgrade warning in the Project Manager only when you’ve installed a

new version of DaVinci Resolve and you have project libraries that were created in older versions of

DaVinci Resolve that need upgrading.

The upgrade warning in the Project Manager indicates

that the project library needs to be upgraded

It’s generally a good idea to back up a project library prior to upgrading it, in case something

goes wrong. In general, upgrading from a whole version release to the next whole version release

of DaVinci Resolve usually requires an upgrade, while upgrading to a dot release of the same

version may or may not. If the currently used project library requires an update, you’ll be told on

application startup.


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA

To upgrade a project library from an old version of DaVinci Resolve:

Click on a project library that needs updating, and select the Upgrade Project Library button. A dialog

appears to confirm if you really want to upgrade that project library. Click Upgrade to proceed.

Disconnecting and Deleting Project Libraries

You cannot actually delete project libraries in DaVinci Resolve; you can only disconnect them so

they don’t appear in the Project Library list. However, disconnected project libraries can still be

reconnected if you remember their name. The only way to completely delete a project library entry in

PostgreSQL is to do so from the command line, or to use the PGAdmin III application that accompanies

the PostgreSQL installation that’s part of the DaVinci Resolve installation process.

To disconnect a project library you no longer need:

�Right-click a project library that is not currently selected, and choose Remove from the

contextual menu. A dialog appears to confirm if you really want to disconnect that project library.

Click Disconnect to proceed.

Locating Local Project Library Directories in Your File System

Because local project libraries have a link to a specific directory in your file system, there’s a way of

locating that directory.

To locate a project library on your system:

�Right-click any local project library, and choose “Reveal in Finder.” A file system window opens up

showing you the location of that local project library, inside which are all of its projects.