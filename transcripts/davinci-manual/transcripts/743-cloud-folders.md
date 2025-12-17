---
title: "Cloud Folders"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 743
---

# Cloud Folders

Cloud Folders are online common storage folders that are not tied to a specific project. This lets you

create a pool of commonly used media assets, such as music, title sequences, credits, etc., and share

them online without having to import them separately into each individual project.

The Cloud Folders section of Cloud Storage

To create a new cloud folder:


In the Storage Space type drop-down, select Cloud Folders.


Click on the Create Cloud Folder icon, immediately to the right of the Storage Space drop-down.


Add a name for the new Cloud Folder.


Add whatever media you like to the folder for sharing.

To share a cloud folder:


In the Cloud Folders interface, click on the “i” information icon in the upper right of the toolbar.


Select the Sharing tab.


Click on the Sharing Settings button at the bottom of the tab.


Enter the users email addresses of the Blackmagic Accounts you want to share with.


Click on Save.

The users will be notified that they have permission to the shared folder, and can access it in DaVinci

Resolve by pressing the “Import Blackmagic Cloud Folder” icon in the Media Pool, as described later

in this chapter.

Personal Storage Folders

You can also create personal media storage folders that are accessible only by your account, and

not shared with other users or tied to a specific project. As of this writing, personal folders are only

available in the web interface and do not integrate with DaVinci Resolve.


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER

To create a new personal folder:


In the Storage Space type drop-down, select Personal Folders.


Click on the Create Cloud Folder icon, immediately to the right of the Storage Space drop-down.


Add a name for the new Personal Folder.


Add whatever media you like to the folder.

Setting up a Blackmagic Cloud

Project in DaVinci Resolve

Setting up a Blackmagic Cloud based project has been refined and simplified in 18.6, allowing you to

set up all the configuration options, including Blackmagic Cloud Storage, from one easy setup screen.

NOTE: To use Blackmagic Cloud, you must first sign up for a Blackmagic Cloud account at

cloud.blackmagicdesign.com and then sign into your account in DaVinci Resolve.

To setup a new Cloud Project:


From DaVinci Resolve’s Project Manager, select Cloud from the Project Library options in the

upper left. Your Blackmagic Cloud Library should be active (highlighted in orange).


Click the New Project button or right-click in the background and select New Project from the

contextual menu. Or import an existing local DaVinci Resolve project that you want to add to the

Blackmagic Cloud.


Choose the options you want in the Create New Cloud Project dialog.


Click the Create button.

The Create New Cloud Project dialog box lets you set up the media locations and sharing parameters

of your project.

Select Remove Unused Clips from the Media Pool option menu


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER

�Name Your Project: Type in a name for your Cloud Project.

�Choose a Location for your Project Media: Choose a location on your file system for imported

media files, graphics, and audio files you wish to use for the project.

�Share Project with Multiple Users?: Lets you determine if you want to share this project with

other users.

Allow Multiple Simultaneous Users: Enables collaboration mode for working with multiple people

on the same project concurrently.

Set Project to Single User: Disables collaboration mode and is designed for one person working

on the project at a time.

�Synchronize Storage with Blackmagic Cloud?: These options let you choose what media to

upload and sync to your Blackmagic Cloud Storage account for other users’ access.

Don’t Sync Media: Does not upload any media to Blackmagic Cloud Storage.

Sync Proxies Only: Uploads only proxy media to Blackmagic Cloud Storage.

Sync Proxies and Originals: Uploads both proxies and the original media to Blackmagic Cloud

Storage. This can use an extremely large amount of storage depending on the amount and size of

the original media.

�Allow Remote Camera Access: Sets permissions for users of the Blackmagic Camera app.

�Allow Remote Cameras Access: Allows Blackmagic Camera app users that are members of this

project to upload media from their phones to the Blackmagic Storage account and will add it to the

project’s Media Pool directly.

�Don’t Allow Remote Cameras: Does not allow Blackmagic Camera app users to upload footage to

this project, even if they happen to be a member of it.

One you press Create, a new project will be made with the parameters you’ve set above.

If at any time you wish to change these parameters after a project has been created, you can

access them again by opening the Project settings, and selecting the Blackmagic Cloud tab.

You can modify all the cloud settings of an existing Blackmagic Cloud project in the Project Settings.


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER

Blackmagic Cloud Sync Manager

When working with a project in a cloud library, several of the most common cloud management

functions can be accessed directly by clicking on the Blackmagic Cloud Sync Manager in the lower

right of the interface. This icon only shows up when working with a cloud library.

The Blackmagic Cloud Sync Manager opens

an array of useful cloud management tools.

From Left to Right on the top bar, the following tools are available:

Pause/Resume Sync: Pauses or Resumes the upload and download of media from the

host computer.

Enable/Disable Multi User Collaboration: Opens a dialog box to toggle between

Set to Single User or Allow Multiple Users (collaboration mode).

Enable/Disable Camera Capture: Opens a dialog box to toggle between

Allow or Don’t Allow Blackmagic Camera app users to upload footage to storage

and import the clips to the project’s Media Pool.

Open in Finder/File Explorer: Opens the Project Media Location in the computer’s

file system.


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER

Open Settings: Opens the Blackmagic Cloud tab in the Project Settings window.

Go to Blackmagic Cloud Storage: Opens up your web browser to the Blackmagic

Cloud Storage page on the internet.

Underneath this toolbar there are two status areas. The top one shows the user logged into

the Blackmagic Cloud account and how much Blackmagic Cloud Storage has been used

and is available. The ring display shows the total of all media in the outside ring, the amount

of media synced locally in the middle ring, and how much media is left to upload in the

inside ring.

The bottom one shows the progress of the media syncing over the internet. The top display

shows the progress bar on the sync status and how much material is left to sync. Directly

underneath that is the media list showing the current clip syncing, and a list of media that has

already synced.

Automatic Proxy Generation and

Upload to Blackmagic Cloud Storage

When in the Media, Cut, Edit and Fairlight pages, DaVinci Resolve can automatically generate proxies

in the background to upload to Blackmagic Cloud. In all pages, users can still explicitly generate proxy

media from the media pool to start uploads.

To enable automatic proxy generation and upload:


In the Project Settings, click on the Blackmagic Cloud tab.


In the “For media files” section, click on “Sync proxies only.”


Check the “Generate proxies automatically” box.


In the “Proxies are created as” section, select the codec you

want the proxy format to be rendered to.


Click on the Save button.

To disable automatic proxy generation and upload:


In the Project Settings, click on the Blackmagic Cloud tab.


In the “For media files” section, click on “Don’t sync media.”


Uncheck the “Generate proxies automatically” box.


Click on the Save button.

Cloud Storage Sync Icons

If you are working in a cloud library, there are Sync icons in the upper left of a clip in the Media Pool

that let you know the status of each clip’s status in the cloud.


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER

The Proxy Processing

icon in the upper left

White Cloud with 3 Dots: This icon

indicates that proxy media is currently

being processed.

The Upload Queue

icon in the upper left

Yellow Cloud with an Up Arrow: This

icon indicates that the clip is in the

queue for being uploaded to the cloud.

The Successful Sync

icon in the upper left

White Cloud with a Checkmark:

This icon indicates that the clip has

successfully been uploaded and synced

to the cloud.

Sync Specific Media Originals in Proxy Synced Cloud Projects

In Blackmagic Cloud projects where only proxies are being synced to Blackmagic Cloud, you have the

ability to sync originals for specific files in the Media Pool. This is useful in situations where you either

need to upload or download originals for certain files, but not all of them. You can right-click on the

Media Pool clips you need the originals for, and select Sync Original Media from the context menu.

You can select individual media proxies and download the original files for just those clips


Blackmagic Cloud | Chapter 192 Blackmagic Cloud Storage

DELIVER