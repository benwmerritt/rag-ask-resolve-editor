---
title: "Blackmagic"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 740
---

# Blackmagic

Cloud

CONTENTS

191	 Blackmagic Cloud Project Server����������������������������������������������������������������������������������������������������� 4102

192	 Blackmagic Cloud Storage������������������������������������������������������������������������������������������������������������������� 4112

193	 Blackmagic Cloud Presentations������������������������������������������������������������������������������������������������������ 4126

194	 Blackmagic Cloud Organizations������������������������������������������������������������������������������������������������������ 4138

195	 Live Sync����������������������������������������������������������������������������������������������������������������������������������������������������� 4150

Chapter 191

Blackmagic Cloud

Project Server

This chapter describes setting up and using the Blackmagic Cloud Project Server,

allowing you to share projects and collaborate with other DaVinci Resolve users

around the world.

Contents

Cloud Project Libraries�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4103

Connecting to a Blackmagic Cloud Project Library in DaVinci Resolve������������������������������������������������������������������ 4103

Accessing the Cloud Project Library in DaVinci Resolve������������������������������������������������������������������������������������������������ 4103

Blackmagic Cloud Project Server on the Web��������������������������������������������������������������������������������������������������������������������� 4104

Optimization and Performance of a Cloud Project Library��������������������������������������������������������������������������������������������� 4105

Creating a New Cloud Project Library�������������������������������������������������������������������������������������������������������������������������������������� 4106

Deleting or Renaming a Cloud Project Library��������������������������������������������������������������������������������������������������������������������� 4106

Upgrading a Cloud Project Library���������������������������������������������������������������������������������������������������������������������������������������������� 4107

Sharing a Cloud Project Library���������������������������������������������������������������������������������������������������������������������������������������������������� 4107

Removing a User from a Shared Cloud Project Library��������������������������������������������������������������������������������������������������� 4108

Backing up and Restoring a Cloud Project Library������������������������������������������������������������������������������������������������������������ 4109

Blackmagic Cloud Support for Importing ATEM Projects����������������������������������������������������������������������������������������������� 4109

Setting up a Cloud-Based Collaboration Workflow����������������������������������������������������������������������������������������������������������� 4109


Blackmagic Cloud | Chapter 191 Blackmagic Cloud Project Server

DELIVER

Cloud Project Libraries

Cloud project libraries are hosted on Blackmagic’s Project Library servers on the internet, allowing

DaVinci Resolve users to connect and collaborate on the same projects from any location in the world.

Connecting to a Blackmagic Cloud Project Library in

DaVinci Resolve

Blackmagic houses project library cloud servers in various locations around the world that users can

access for a nominal monthly fee.

To sign into to the Blackmagic cloud:


cloud:Sign up for a Blackmagic ID using your email address at http://blackmagicdesign.com


In the Project Manager window, select Cloud from the Project Library icons in the upper left.


Chose the Blackmagic Cloud option from the Sign In dialog, and input your Blackmagic ID

and password.


If you are a member of an Organization Profile, you can choose to sign into that account or your

personal account.

The Blackmagic Cloud login dialog box

Signing out of the Blackmagic cloud:


In the Project Manager window, select Cloud from the Project Library icons in the upper left, and

then click your account icon in the upper right, and select Log Out.


Select File > Blackmagic Cloud Account > Log Out.


Select Preferences > Internet Accounts Blackmagic Cloud > Log Out.

Accessing the Cloud Project Library in DaVinci Resolve

Once connected, cloud project libraries are accessed by clicking on the Show/Hide Project Libraries

icon in the upper left of the Project Manager. A sidebar then opens up showing all your connected

project libraries. Click on the Cloud icon to open up the cloud project library. It is split into two

sections: “My Cloud,” which manages all the project libraries that you create, and “Shared with me,”

which shows project libraries that other users have created but given you shared access to.


Blackmagic Cloud | Chapter 191 Blackmagic Cloud Project Server

DELIVER

If you don’t see your project library immediately, you can click on the circular arrow refresh icon in the

upper right of the Project Manager to force a refresh from the servers.

The Blackmagic cloud library

Blackmagic Cloud Project Server on the Web

Cloud project libraries are best managed from within DaVinci Resolve, however there is a web

interface as well. This interface lets you see what projects are in each library, search and sort, and

create new cloud project libraries.

The Blackmagic Cloud Project Server web interface


Blackmagic Cloud | Chapter 191 Blackmagic Cloud Project Server

DELIVER

When initially opened, the Project Server will show all the active projects in your last used project

library. All of your cloud project libraries will be listed in the left hand pane, and you can add new ones

by clicking on the Add Project Library button at the bottom.

When a cloud project library is selected, all of the projects it contains will be displayed and can be

searched for, sorted, and listed using the respective controls on the right side of the toolbar. As of

this writing, on the web interface, projects can only be viewable. In order to create, delete, copy

or otherwise manage an individual project, you must do it from within the DaVinci Resolve Project

Manager instead

By clicking on the information icon, on the right hand side of the toolbar, you can open the libraries’

sharing settings. Here you can add, enable, or disable the project library, or add a new presentation.

The Sharing tab shows you who currently has access to the project library, and you can add more

users by clicking on the Share Project Library button below. The Backups tab lets you create and

restore backups of your project library to the Blackmagic Cloud; you can optionally set automatic daily

backups for added safety.

Optimization and Performance of a Cloud Project Library

Before learning about how to create and manage cloud project libraries, it’s worthwhile addressing

server lag and optimizations. The project library is a database of all the edits, clip metadata, visual

effects, color corrections, and audio engineering applied to your timeline. This project library is

queried and updated constantly as you use DaVinci Resolve. When the project library is local to, or on

the same network as your workstation, these updates happen more or less instantaneously. However,

when the project server is half-way around the world on the internet, the speed of light and internet

routing start to insert perceptible lag time.

Luckily the majority of the changes required to mitigate this have been done by the DaVinci Resolve

team. They have re-written the underlying project library code over a period of several months to

optimize it for internet performance, and in most cases the responsiveness will be indistinguishable

from using a local project library. However, these types of processes involve intensive and persistent

project library operations, and some lag will become apparent when:

•	 Changing cloud project libraries

•	 Loading a project from the cloud project library

•	 Backing up and restoring cloud project libraries

It’s important to keep in mind, that once loaded, actually working in DaVinci Resolve will still

be as fluid and responsive as you are used to working with local libraries.

TIP: The major optimization that the user can make in cloud library performance is to decide

where to physically locate the server. The best performance will be found closest to the city

where the team is working. In some cases, the team will be working in multiple cities and

countries around the world. In those cases, the server should be hosted in the region of the

person who uses the project library the most, and that person is the editor. In the Edit and Cut

pages, the project library is written to whenever the user releases the mouse button, while on

the Color page the project library is only written to when you select a new clip. So for the best

performance, you want to host the server location as close to the editor as possible.


Blackmagic Cloud | Chapter 191 Blackmagic Cloud Project Server

DELIVER