---
title: "Creating New Network Project Libraries"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 753
---

# Creating New Network Project Libraries

If necessary, you can create new network project libraries right within the DaVinci Resolve

Project Server.

To create a new network project library:


Click the Add Project Library button at the bottom of the Project Libraries list.


When the Create Project Library window appears, type a name for the new project library into

the Name field. Because all projects in a network project library are saved internally within the

network project library, no other changes are necessary.


Click Create, and the new network project library will appear in the Project Libraries list.


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER

Backing Up and Restoring Project Libraries

You can also back up and restore project libraries without needing to open DaVinci Resolve.

Furthermore, you can back up project libraries from older versions of DaVinci Resolve, making it easy

to back up project libraries for safety before you upgrade them.

To backup/export a project library:


Select the project library you want to back up.


Click the Display Project Library Details icon (the circled letter “i” to the right of the project library).


Click the Back Up button.


Choose a location to which to save the backup in the Backup Project library dialog, and click Save.

To restore/import a project library:


Click the Restore button at the top of the Project Libraries sidebar.

The Restore button


Find the project library you need to import using the file import dialog, and click Open.


In the Add Project Library dialog, type a name for the new project library into the Name field. This

will rename the imported project library but will not alter its contents. You can also name it the

same as the original project library.


Click Create, and the imported local project library will appear in the Project Libraries sidebar.

Upgrading Project Libraries

From time to time, new versions of DaVinci Resolve require changes to the way projects are created,

which requires project libraries created with older versions of DaVinci Resolve to be upgraded before

you can access the projects within. Fortunately, this is a simple process.

It’s generally a good idea to back up a project library prior to upgrading it, in case something

goes wrong. In general, upgrading from a whole version release to the next whole version release

of DaVinci Resolve usually requires an upgrade, while upgrading to a dot release of the same

version may or may not. If the currently used project library requires an update, you’ll be told on

application startup.

The upgrade warning in the Project Manager indicates

that project library needs to be upgraded


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER

To upgrade a project library from an older version of DaVinci Resolve:

Click on a project library that needs updating, and select the Upgrade Project Library

button. A dialog appears to confirm if you really want to upgrade that project library.

Click Upgrade to proceed.

Viewing Project Library Contents

If you’re using multiple project libraries to organize your projects, you can browse the contents of

each project library to search for what you’re looking for. Simply click to select a project library in the

sidebar, and an orange highlight will appear. All projects corresponding to that project library appear

in the Project Manager window.

Optimizing Project Libraries

Sometimes, project libraries in DaVinci Resolve can become so large that their size affects

performance. In these cases you may need to optimize them to improve access speed by “vacuuming”

the project library of unnecessary spaces and reindexing it. Using the Optimize command can also be

a valuable troubleshooting step in certain cases where you’re having problems opening, importing, or

otherwise using projects saved within network project libraries.

To optimize a project library:


Select the project library you want to optimize.


Click the Display Project Library Details icon (the circled letter “i” to the right of the project library).


Click the Optimize button.


A warning dialog will appear. Click Optimize to proceed, otherwise click cancel to leave the project

library in its current state.

Member Management in the DaVinci Resolve Project Server

It is possible to assign specific users to specific project libraries and adjust their roles. This gives extra

granularity for security for complex projects with many users. Every network project library starts

with the default user: postgres and password: DaVinci. This was until recently the only way to sign

into the DaVinci Resolve Project Server remotely, but now you can add custom users and passwords

as well. Members will be able to use their individual credentials to sign into network projects in the

Project Manager.


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER

The DaVinci Resolve Project Server Members management window

To add a new member to the DaVinci Resolve Project Server:


Click the Members button on the top right of the DaVinci Resolve Project Server.


Click the Create New Member button at the bottom of the Members window.


Select a username and password for the member, you can optionally add a thumbnail photo

as well. This thumbnail will be used to identify the user in collaboration mode.

The DaVinci Resolve Project Server

Create New Member window


Repeat as for as many new users as you want to add.


Click the Save button to store the new users, or click Cancel to discard your changes.


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER

To delete an existing member from the DaVinci Resolve Project Server:


Click the Members button on the top right of the DaVinci Resolve Project Server.


Find the user you want to delete and press the trash can icon in that user’s row. There is no

warning dialog for the deletion, and it is not undoable, so make sure you double check that you

have selected the correct user.

To modify an existing member’s permissions in the DaVinci Resolve Project Server:


Click the Members button on the top right of the DaVinci Resolve Project Server.


To change the user’s role between Administrator and Collaborator use the selection menu.


To edit a user’s name and password details select the Pencil icon.

Assigning Members to Specific Project Libraries

Once you have created some members, you can add them to specific project libraries. This lets you

have multiple teams of people, working on multiple projects off the same Project Server, without the

off chance that they accidentally delete another teams projects, or have access to sensitive material.

To add or remove a member from a specific project library:


Open a project library’s details settings by clicking on the “i” icon to the right of its name.


Click on the Manage Members button at the bottom of the project library.


To add a member, check the box next to their name in the All Members field.


To remove a member, click on the “x” next to their name in the Added Members field.

The DaVinci Resolve Project Server Mange Members window

Members added to a project library in this way will be able to log-in using their credentials in

the Network Libraries section of the Project Manager in DaVinci Resolve.


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER