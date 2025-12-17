---
title: "Using the Project Manager"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 15
---

# Using the Project Manager

Ordinarily, the Project Manager is the first window you’ll see when DaVinci Resolve starts up. It’s a

convenient, centralized browser for creating, organizing, and managing all of your projects. Unlike

other applications that rely on your file manager for organizing projects, DaVinci Resolve requires you

to do most project organization in the Project Manager.

Project Manager

If you’ve already opened a project, you can reopen the Project Manager at any time by clicking the

Home button at the bottom right-hand corner of the DaVinci Resolve window, in the Page Navigation

bar. If you’ve hidden the Page Navigation bar at the bottom of the DaVinci Resolve window, you can

open the Project Manager by choosing File > Project Manager.

The Project Manager button at

the bottom-right corner of the

DaVinci Resolve interface


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA

Launching DaVinci Resolve for the First Time?

If you’ve just installed DaVinci Resolve and have opened it for the first time, it’s time to

set the preferences in order to specify your language, scratch disk volume, and hardware

configuration for video and audio I/O and control panels (if you have one).

For more information about setting the preferences in DaVinci Resolve, see Chapter 4,

“System and User Preferences.”

Creating a New Project

The first step into DaVinci Resolve is to create a new Project in the Project Manager, which is

conveniently the first thing that opens when you launch the program. Each project contains links to

all of the media, graphics, and sound files used in your film, as well as timelines where all the editing,

color correction, motion graphics, and audio post work is done.

There are several settings, options, and preferences attached to each project (you can access them by

clicking on the small gear icon in the very bottom right of the interface), and all of them are described

in detail later in this section. However, actually creating a project requires only four steps.

Creating a New Project:


Click on the New Project button at the bottom of the Project Manager.


Type in a name for your project.


Observe the folder where any media created by DaVinci Resolve will be stored in Media Location.

Make sure you have some space on this drive. Clicking on the Change Location button lets you

select another drive/folder instead of the default.


Click the Create button.

The Create New Project dialog

Project Management

The Project Manager provides an in-application interface for creating, renaming, and deleting projects.

Many of these commands exist within the contextual menu that appears when you right-click the

background of the Project Manager.

Methods of project management:

�To create a new project: Double-click the Default Project icon, or click the New Project button

at the bottom of the window. A new project is created, and DaVinci Resolve opens up the Media

page. Once a project is open, you can alter its project settings by clicking the gear icon.

�To open a previously saved project: Double-click any Project icon, or Item if you’re in List view.

You can also select a project and click the Open button.


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA

�To open a project in Read-Only Mode: Right-click a Project icon or Item, and choose Open in

Read Only Mode. This lets you open a project without danger of altering it. If you make changes,

you can use the Save As command to save a new copy of the project with a new name.

�To rename a project: Right-click a Project icon or Item, choose Rename, and type a new name in

the dialog that appears, clicking OK when you’re finished.

�To load project settings from another project to the currently open project: Right-click a

Project icon or Item (other than the currently open project), and choose “Load Project Settings to

Current Project.” This lets you change a project’s settings prior to opening it in cases where the

project settings are causing some kind of problem that prevents you from opening the project.

�To update the thumbnails of a project in the Project Manager: Right-click any project, and

choose “Update Thumbnails.”

�To delete a project: Select one or more projects, then either press the Backspace key, or

right-click one of the selected projects and choose Delete. Click OK when a dialog asks you to

confirm the operation.

NOTE: You cannot move or delete the currently open or loaded project.

Importing and Exporting DaVinci Resolve Projects (.drp Files)

DaVinci Resolve projects are saved with the file extension .drp and enable you to exchange files

with other DaVinci Resolve users. If you double-click a DaVinci Resolve .drp file in the Windows or

macOS file system, this will automatically open DaVinci Resolve, import that project into the Project

Manager regardless of what kind of project library you’re using, and open that project so that you’re

ready to work.

Importing and Exporting Projects in Local Project Libraries

If you’re using local project libraries to manage your projects, you can copy and import

projects using the project folders in the file manager of either macOS or Windows. This

method does not work for DaVinci Resolve on Linux.

Moving projects from one local project library into another using macOS or Windows:


Locate the local project library directory in which the project you want to copy is stored. If you

don’t know where the designated local project library directory is, you can open DaVinci Resolve

and check the directory path for the current local project library in the Project Libraries sidebar.


Copy the project folder from the source workstation to the designated local project library

directory on the destination workstation. If you don’t know where the designated local project

library directory is, you can open DaVinci Resolve on the workstation you’re copying the project to

and check the directory path for the current local project library in the Project Libraries sidebar.


Once you’ve copied the project folder into the correct location, you’ll need to quit and reopen

DaVinci Resolve. Afterwards, the imported project should appear in the Project Manager.

Importing and Exporting Projects in Network Project Libraries

If you’re using a network project library, another set of commands let you import and export

projects using the .drp file format. You can also export .drp files from local project libraries if

you want to export a more self-contained item to transport.


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA

To import a .drp project file, do one of the following:

�Select the Import button at the bottom of the Project Manager, then find and select a .drp project

file using the Import Project File dialog, and click Open.

�Drag the .drp file you want to import from your file system and drop it anywhere into the

Project Manager window.

�Right-click any empty area of the Project Manager and choose Import, then find and select a .drp

project file using the Import Project File dialog, and click Open.

To import a .drp project file and reconfigure the gallery path at the same time:

�Hold the Option key down while right-clicking any empty area of the Project Manager, and choose

Import+, then find and select a .drp project file, and click Open. Upon opening, the gallery path will

automatically be updated to that of your workstation.

To export the currently open project as a .drp file:

�Choose File > Export Project, and when the Save dialog appears, choose a location, enter

a name, and click Save. The result is a self-contained file with a .drp file suffix saved at the

location you chose.

To export a .drp project file from the Project Manager:

�Select the Export button at the bottom of the Project Manager, and when the Save dialog appears,

choose a location, enter a name, and click Save. The result is a self-contained file with a .drp file

suffix saved at the location you chose.

�Right-click a Project icon or Item in the Project Manager, then choose one of the

following commands;

�Export Project: Exports project data with no LUTs and no stills. Best when you need to export

the smallest possible file.

�Export Project With Stills and LUTs: Exports the project, including both still frames in the

Gallery and LUTs used in grades. Best when you want to export the most self-contained file and

you can’t guarantee the recipient will have the same LUTs you do.

�When the Save dialog appears, choose a location, enter a name, and click Save. The result is a

self-contained file with a .drp file suffix saved at the location you chose.

TIP: You can export multiple projects from the Project Manager at the same time by either

command-clicking or lassoing the projects, right-clicking on one of them, and selecting

Export Projects from the drop-down menu. All projects will be saved in the same location.

Project Manager View Options

Four buttons at the top right let you control how projects are viewed in the Project Manager.

Select Thumbnail or List View

�Zoom slider: (Only appears in Thumbnail view) Lets you adjust the size of the thumbnails in

Thumbnail view.

�Project Sort Order drop-down: (Only appears in Thumbnail view) Lets you choose the sort order

of projects in Thumbnail view.


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA

�Information: (Only appears in Thumbnail view) Lets you show or hide additional project

information displayed underneath each project’s thumbnail, including the frame size, number of

timelines within, and when that project was last modified.

�Thumbnail view: Each project is represented by a large image that can be hover-scrubbed to

reveal five representative images from that project.

Hover-scrub over Project icon;

information is enabled

�List view: Every project appears as an item in a list that has seven columns: Name, Last Modified,

Timelines, Format, Frame Rate, Date Created, and Note. You can click any column header to sort

the contents of the Project Manager by that criteria; clicking the header a second time toggles that

column between ascending and descending sorting.

Project List view


Setup and Workflows | Chapter 3 Managing Projects and Project Libraries

MEDIA