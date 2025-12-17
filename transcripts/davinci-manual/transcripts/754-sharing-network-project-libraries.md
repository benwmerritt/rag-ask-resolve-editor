---
title: "Sharing Network Project Libraries"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 754
---

# Sharing Network Project Libraries

via the Project Server

You can also use the DaVinci Resolve Project Server to easily set up a shared Project Server on your

local network. However, for this to work, you need to adhere to the following requirements:

•	 All workstations need to be connected to the Project Server on a local network.

•	 All network connections should be reasonably fast (preferably Gigabit Ethernet or faster).

•	 The computer functioning as the Project Server should be reasonably fast, but it doesn’t

need fast GPU processing.

The following procedures describe how to set up a shared Project Server, and how to export an

access key with which to easily set up other workstations to connect to it.

To configure the DaVinci Resolve Project Server:


Open the DaVinci Resolve Project Server application.


In the File > Network Interface menu choose the IP address you wish to use to connect to

the client workstations.

The Network Interface menu

IMPORTANT: You must select the appropriate Network Interface IP address that matches the

network the client computers are on before you create and share a project library or create

an access key, otherwise a connection error will occur.

To share a project library using the DaVinci Resolve Project Server:


Select or create a DaVinci Resolve project library you want to share, and click the Project Library

Enabled slider on. It’s at the top of the project library’s details section.


When a dialog appears asking if you want to authorize the configuration of your Project Server,

click Authorize. That project library can now be shared among other DaVinci Resolve workstations

on the same network.

Once you’ve set up a Project Server, it’s easy to connect other machines to that server using

access keys that you can create using the DaVinci Resolve Project Server application.


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER

To create an access key to enable easy connection to a Project Server:


Select a project library that you’ve set up to share, enter the library’s details section, and choose

the Export Access Key option from the settings icon in the upper right.


Choose a location via the Create Access Key dialog, and click Save. An access key file is saved to

the location you chose with the file extension .resolvedbkey.


Copy the .resolvedbkey file to the workstation you want to connect to the shared project library.


Open DaVinci Resolve, and when the Project Manager appears, open the Project Libraries

sidebar, and then drag the .resolvedbkey file and drop it anywhere within the Project Manager.

The shared project library should now appear in the Project Libraries sidebar, and if you select it,

you’ll see all of the projects that are located in that project library on the Project Server.

If necessary, you can also disable sharing for any project library, preventing remote access to it

from other workstations on the network.

To disable sharing:


With the DaVinci Resolve Project Server application open, select a project library you enabled

sharing for, and click the Project Library Enabled slider off. It’s at the top of the project library’s

details section.


When a dialog appears asking if you want to authorize the configuration of your PostgreSQL

server, click Authorize. That project library will no longer be shared.

IMPORTANT: If you enable sharing on a computer that is later moved to another network (for

example, if you set up Project Server sharing on a laptop), you’ll need to disable sharing and

then re-enable it before you create access key files that will successfully connect to the new

network location.

Cloud Project Libraries

Cloud project libraries are hosted on Blackmagic’s Project Library servers on the internet, allowing

DaVinci Resolve users to connect and collaborate on the same projects from any location in the world.

For more information on Cloud Project Libraries, see Chapter 191, “Blackmagic Cloud

Project Server.”


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER

Chapter 197

Collaborative

Workflow

Multi-user collaborative workflow uses “bin locking” to manage who has access to

what when multiple collaborators open the same project.

However, collaborative workflow also allows multiple artists to do simultaneous editing, compositing,

grading, and metadata entry to clips on the same timeline within a single project for which

Collaboration has been enabled. Multiple users can simultaneously access the same timeline within

the same project to edit, composite, and grade at the same time, while other editors and assistants

can open different bins containing different timelines within the same project to do editorial and

media management. This chapter describes how to set up multiple DaVinci Resolve workstations to

collaborate, and how to use bin locking to work together.

Contents

Introduction to Collaborative Workflow���������������������������������������������������������������������������������������������������������������������������������� 4179

Collaborative Render Cache Support���������������������������������������������������������������������������������������������������������������������������������������� 4179

Collaborative Support for Individual Monitoring������������������������������������������������������������������������������������������������������������������ 4179

Collaborative Marker, Flag, and Clip Color Support���������������������������������������������������������������������������������������������������������� 4180

Read Only Mode���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4180

Collaborative Support for HDR���������������������������������������������������������������������������������������������������������������������������������������������������� 4180

Collaborative Support for LUT and Colorspace Context Options������������������������������������������������������������������������������ 4180

Requirements for Collaboration������������������������������������������������������������������������������������������������������������������������������������������������� 4180

Enabling Multiple User Collaboration�������������������������������������������������������������������������������������������������������������������������������������� 4181

Opening Projects to Collaborate������������������������������������������������������������������������������������������������������������������������������������������������ 4181

Customizing Your Collaborator Identification��������������������������������������������������������������������������������������������������������������������� 4182

How Collaboration Works�������������������������������������������������������������������������������������������������������������������������������������������������������������� 4183

Automatic Bin and Timeline Locking����������������������������������������������������������������������������������������������������������������������������������������� 4183

Managing Bin Locks Manually������������������������������������������������������������������������������������������������������������������������������������������������������ 4184

Manually Locking and Unlocking Timelines�������������������������������������������������������������������������������������������������������������������������� 4185

Automatic Clip Locking�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4185

Receiving Changes Made by Collaborators�������������������������������������������������������������������������������������������������������������������������� 4186


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

Introduction to Collaborative Workflow

Multi-user collaborative workflow allows simultaneous editing, compositing, grading, and Media Pool

clip management by multiple people within a single project that has been enabled for collaboration.

Collaboration takes three different forms:

�Using bin locking, multiple editors can simultaneously edit different timelines in different bins of

the same project, while assistant editors can reorganize clips and edit the metadata in other bins

within the same project. Bins are automatically locked when selected by a particular user and

unlocked when deselected by that same user, or they can be manually set to be either locked or

unlocked as circumstances require.

�Using clip locking, multiple colorists and compositing artists can work together in the same

timeline, in either the Color page or Fusion page, without fear of overwriting one another’s work.

A clip is locked automatically when a user selects that clip to work on, and is unlocked (with the

work checked in) when that same user selects a different clip. Clip locking in the Fusion page is

maintained separately from clip locking on the Color page, so a compositing artist and colorist can

work together on the same shot.

�One editor, one compositing artist, and one colorist can work together on the same clip in the

same Timeline of the same project without conflict.

Overall, working in DaVinci Resolve in Collaborative Workflow mode is identical to working in non-

collaborative mode. However, there are a few collaborative capabilities that are worth knowing about.

Collaborative Render Cache Support

Each collaborator on a project will have the exact same render cache format settings automatically

configured across all machines. If you are collaborating across operating systems (Mac, Windows,

Linux), it is important that the Render Cache Format is set to a codec that is supported by all platforms.

Collaborative Support for Individual Monitoring

If necessary, each collaborator on a project can override the output and monitoring settings of

a project on their particular workstation. When a project is set to use Collaborative Workflow, a

“Use Local Overrides” checkbox appears in the Video Monitoring group of the Project Settings that

lets you choose how to monitor on your particular workstation.

Examples of Collaborators Working Together�������������������������������������������������������������������������������������������������������������������� 4188

Multiple Editors Working Together��������������������������������������������������������������������������������������������������������������������������������������������� 4188

Editors and Assistant Editors Working Together����������������������������������������������������������������������������������������������������������������� 4189

Editors and Compositing Artists Working Together���������������������������������������������������������������������������������������������������������� 4189

Multiple Compositing Artists Working Together����������������������������������������������������������������������������������������������������������������� 4190

Editors and Colorists Working Together��������������������������������������������������������������������������������������������������������������������������������� 4190

Multiple Colorists Working Together����������������������������������������������������������������������������������������������������������������������������������������� 4191

Managing Notes Among Collaborators����������������������������������������������������������������������������������������������������������������������������������� 4191

Collaboration Chat����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4192


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

Collaborative Marker, Flag, and Clip Color Support

Collaborative workflow supports the modification of markers, flags, clip metadata, and clip color from

the Color page. Additionally, FrameIO comment markers are supported by collaborative workflow.

Read Only Mode

Users can load collaborative projects in Read Only Mode.

Collaborative Support for HDR

Starting with DaVinci Resolve 16, there is support for Dolby Vision and HDR10+ in

collaborative workflows.

Collaborative Support for LUT and Colorspace Context Options

You can adjust LUTs and Colorspace options from nodes in multi-user projects, just by right-clicking

them and choosing the option you want from the context menu, similar to how it works in single

user projects.

Requirements for Collaboration

In order to use collaborative workflow:

�All users must be working on a project that’s been saved either in the Blackmagic Cloud, or on a

properly configured remote project library server. This remote project library server can be on one

of the actively used DaVinci Resolve workstations, or it can be another computer on your network

that simply hosts shared projects, but it should be on a computer that is never shut down or put to

sleep, to prevent projects suddenly becoming unavailable.

�All machines participating in a collaborative workflow must be networked. They can be on the

same local area network (LAN), but you can also connect computers on different subnets.

�Shared projects should ideally use media on some type of fast storage area network (SAN), with

each collaborator connected to that SAN so that every workstation that’s connected to the project

being collaborated on has direct access to the same media. In a pinch, shared volumes over a

network will work, but proper SANs will provide significant performance benefits. Facilities using

multiple computer platforms (macOS, Windows, and Linux) together can use the Mapped Mount

option of the Media Storage Locations list, found in the DaVinci Resolve System Preferences, to

facilitate cross platform drive connection.

�Alternatively, all workstations can be connected via the internet to the same cloud storage folder

with the proper Path Mapping set up in the Project Settings.

For more information on setting up a project library server, see Chapter 196, “Managing

Project Libraries and Project Servers.”


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER