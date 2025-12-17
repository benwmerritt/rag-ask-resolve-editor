---
title: "Creating a New Cloud Project Library"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 741
---

# Creating a New Cloud Project Library

Creating a new cloud library requires manually adding it on the Blackmagic Cloud website.

To create a new cloud project library:


Tap on the Cloud icon to Sign into the Blackmagic cloud server in the Project Manager.


Tap on the Show/Hide Project Libraries icon in the upper left of the Project Manager to

expose the sidebar.


Tap on the “Go to Blackmagic Cloud” button at the bottom of the sidebar, which takes you to the

Web Project Server.


A web browser will open up, automatically taking you to the Blackmagic Cloud web interface.


Tap on the “Add Project Library” button at the bottom of the sidebar in your web browser


Enter a new name for your cloud project library, and then select the region in the world in

which you want to host the server. It is best to select a server closest to the project’s editor, and

then the Version of Davinci Resolve you want the library to be compatible with.


Press the Add button.

You can now create or import new projects directly into your new cloud project library.

Deleting or Renaming a Cloud Project Library

If you are finished with a particular cloud project library and want to delete it or wish to change its

name you can do so through the Project Libraries interface.

To delete a cloud project library:


Sign into the Blackmagic cloud server in the Project Manager.


Click on the Show/Hide Project Libraries icon in the upper left of the Project Manager to

expose the sidebar.


Right-click on the library you want to delete in the Project Libraries sidebar, and select Delete

from the drop-down menu.


Click the Delete button on the confirmation dialog box that opens.

Deleting a cloud project library is a permanent and not undoable action. Make sure you have

everything you need from this library before you click delete. Once it’s gone, it’s gone.

To rename a cloud project library:


Sign into the Blackmagic cloud server in the Project Manager.


Click on the Show/Hide Project Libraries icon in the upper left of the Project Manager to

expose the sidebar.


Right-click on the library you want to rename in the Project Libraries sidebar, and enter the new

name in the dialog box.


Click the OK button.

TIP: You can not delete or change the name of the currently connected project library

(indicated by an orange highlight around it). In order to do so, you must select and connect to

another project library first, and then apply the steps above.


Blackmagic Cloud | Chapter 191 Blackmagic Cloud Project Server

DELIVER

Upgrading a Cloud Project Library

From time to time, new versions of DaVinci Resolve require changes to the way projects are created,

which requires project libraries created with older versions of DaVinci Resolve to be upgraded before

you can access the projects within. Fortunately, this is a simple process, but it can only be performed

in DaVinci Resolve, not the web interface.

To upgrade a cloud project library:


Sign into the Blackmagic cloud server in the Project Manager.


Click on the Show/Hide Project Libraries icon in the upper left of the Project Manager to expose

the sidebar.


Right-click on the library you want to upgrade in the Project Libraries sidebar, and select Upgrade

from the drop-down menu.


Click the upgrade button on the confirmation dialog box that opens.

Sharing a Cloud Project Library

You can share a cloud project library with other users around the world with a Blackmagic ID.

To share a cloud project library:


Sign into the Blackmagic cloud server in the Project Manager.


Click on the Show/Hide Project Libraries icon in the upper left of the Project Manager to expose

the sidebar.


Click on the Details icon (the circled letter “i”) on the cloud project library you wish to share to

open the details settings.


A members list (or a sharing tab in the web interface) will appear, and your user name and email

will be first on the list with a little crown icon, showing that you are the owner of this project library.


Click the Share button at the bottom of the sidebar.


Enter the Blackmagic ID (email address) of the person you want to share this project library with.


Press the Share button.

The user will instantly have access to this shared library, and an email will inform them of their

access as well.

IMPORTANT: The users you share your project library with have access to modifying and

deleting any projects within that shared library, so be judicious about who you give access to.


Blackmagic Cloud | Chapter 191 Blackmagic Cloud Project Server

DELIVER

The Members section of the Blackmagic cloud library

Removing a User from a Shared Cloud Project Library

If you are the owner of a shared cloud project library, you can remove another shared user’s

access to it.

Removing a shared user from a cloud project library:


Sign into the Blackmagic cloud server in the Project Manager.


Click on the Show/Hide Project Libraries icon in the upper left of the Project Manager to expose

the sidebar.


Click on the Details icon (the circled letter “i”) on the cloud project library you wish to share to

open the details settings.


A members list (or a sharing tab in the web interface) will appear, showing all users that have

access to this project library.


Right-click on the user you wish to remove and select Remove Member from the drop-down list.


Blackmagic Cloud | Chapter 191 Blackmagic Cloud Project Server

DELIVER

Backing up and Restoring a Cloud Project Library

You can back up and restore a cloud project library in the Blackmagic cloud itself.

To back up a cloud project library:


Sign into the Blackmagic cloud server in the Project Manager.


Click on the Show/Hide Project Libraries icon in the upper left of the Project Manager to expose

the sidebar.


Click on the Details icon (the circled letter “i”) on the cloud project library you wish to back up to

open the details settings.


Click the Back Up button.


After some time, a dialog box will appear confirming the backup has been made to the cloud.

To restore an older version of a cloud project library:


Sign into the Blackmagic cloud server in the Project Manager.


Click on the Show/Hide Project Libraries icon in the upper left of the Project Manager to expose

the sidebar.


Click on the Details icon (the circled letter “i”) on the cloud project library you wish to restore to an

earlier version to open the details settings.


Click the Restore button.


Navigate to the version that you want to restore in the Backups list.


Assign a new name to the restored library.


Click the Restore button.

Blackmagic Cloud Support for Importing ATEM Projects

If you’re working with ATEM switchers, and use the workflow of creating multiple ISO feeds and the

accompanying DaVinci Resolve project, you can now log into a Blackmagic Cloud project library,

select an existing DaVinci Resolve cloud project, and use the Camera Uploads mechanism to

synchronize recorded media to DaVinci Resolve. DaVinci Resolve collaborators can see the edit

decisions made from the switcher as a new timeline in that project.

�The DaVinci Resolve project needs to be set to synchronize camera originals to

see the uploaded media from the switcher.

�New timelines may use custom settings if the ATEM resolution or frame rate

differs from project settings.

Setting up a Cloud-Based Collaboration Workflow

As internet bandwidth has increased over the years, it has recently become possible to collaborate

on a project completely online. While once you needed to be in the same building connected to a

fast LAN, and Network Attached Storage (NAS), it is now possible to collaborate in real time from all

around the world using the internet and cloud storage instead. Below are instructions for setting up a

completely cloud-based workflow using the tools and settings in DaVinci Resolve 18 or higher.

This sample workflow consists of Editor A, Colorist B, and Audio Engineer C, all in different parts of the

world, and wanting to collaborate on the same project at the same time. The ideal is to minimize the

amount of media management involved and to not have to send individual project files back and forth.


Blackmagic Cloud | Chapter 191 Blackmagic Cloud Project Server

DELIVER

Set up the Blackmagic Cloud and a Cloud Library

�Users A, B, and C sign up for the Blackmagic cloud service.

�Users A, B, and C log into the cloud in the Project Manger in their own copies of DaVinci Resolve.

�User A creates a new cloud library, and invites Users B and C to share it. Since User A is the editor,

they will locate the cloud library’s server nearest themselves.

Set up the Cloud Storage

�Users A, B, and C sign up for a cloud storage provider (Dropbox, iCloud, OneDrive,

Google Drive, etc.)

�Users A, B, and C configure their cloud storage so they all can share access to the same cloud-

based folder. This folder should be at the top level of the cloud storage. They decide to name the

folder Episode 12.

�Users A, B, and C create a file hierarchy system in their shared Episode 12 folder, such as new

subfolders for Audio, Proxies, and Graphics.

�Users A, B, and C mount their shared storage folder on their own computers. Editor A adds

some logos and still photos to the Graphics folder. Audio Engineer C adds some music and

sound effects to the Audio folder. This takes a while to upload and distribute from the cloud, but

eventually all users have the same media locally on their computers.

Create the Proxy Media

�Colorist B has the RAW camera masters on a hard drive connected to their system. Since only

they need access to the RAW camera files for color grading, they will make low bandwidth proxies

for the Editor and Audio Engineer to work with. These files are small enough to upload and store in

their cloud storage folder.

�Colorist B creates proxy files of the RAW media in the Blackmagic Proxy Generator application.

For more information on using the Blackmagic Proxy Generator, see Chapter 8,

“Improving Performance, Proxies, and the Render Cache.”

�Colorist B uploads the proxy files to the Proxies folder in their cloud storage.

Setup the DaVinci Resolve Project and Settings

�Colorist B creates the new project in the cloud library, and sets up its resolution

and frame rate, etc.

�Colorist B turns on the File > Multiple User Collaboration setting.

�Users A, B, and C open the project and set their individual file paths to their cloud storage folder

“Episode 12” in the Path Mapping section of the Project Settings.

For more information on Path Mapping, see Chapter 6, “Project Settings.”


Blackmagic Cloud | Chapter 191 Blackmagic Cloud Project Server

DELIVER

�Colorist B imports the RAW media from their local hard drive into their Media Pool, and links

them to the proxies he uploaded to the Episode12/Proxies folder. At this point, Editor A, and

Audio Engineer C now have access to the proxy media, while Colorist B can switch back and forth

between RAW media and Proxies as needed. If necessary, Colorist B can also decide to upload

the RAW media to the shared folder if space and time allow. While the other users are waiting

for this media to upload, if they have the “Prefer Camera Originals” setting checked in Playback

> Proxy Handling menu, they can continue to edit using the proxies, and as the RAW media files

upload, they will automatically replace the proxy files as they come in.

�Editor A imports their still photos to the Media Pool from the Episode 12/Graphics folder.

They immediately become available to Users B and C without relinking.

�Audio Engineer C imports their music tracks to the Media Pool from the Episode 12/Audio folder.

They immediately become available to Users A and B without relinking.

�As the users continue to add more media into the shared folder and bring it into the Media Pool,

there may be a lag as the media is uploaded to the cloud storage, and then downloaded to the

other users. During this time the clip will appear as media offline but will relink automatically once

the file finishes its download to the local computer.

Continue working in DaVinci Resolve’s Collaborative Workflow

From here, the editor edits, the colorist colors, and the audio engineer handles the sound design all

using DaVinci Resolve’s existing collaborative workflow tools.

For more information on using these tools, see Chapter 197, “Collaborative Workflow.”


Blackmagic Cloud | Chapter 191 Blackmagic Cloud Project Server

DELIVER