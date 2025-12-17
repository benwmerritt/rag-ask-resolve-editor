---
title: "Live Sync in DaVinci Resolve"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 750
---

# Live Sync in DaVinci Resolve

Setting up a Cloud Project in DaVinci Resolve

Before starting a Live Sync editing session, you will have to create a Cloud project in DaVinci Resolve

that the camera can link to. This can be a new or existing Cloud project. For Live Sync to function, the

“Allow Remote Camera Access” button in the Create New Cloud Project dialog box must be turned on.

For more information on setting up a Cloud Project, see Chapter 192, “Blackmagic

Cloud Storage.”

Editing Live Sync in DaVinci Resolve

Once you’ve opened your Cloud project in DaVinci Resolve, you can start editing live footage as it

comes in. You can edit from either the Cut or Edit pages.

In the Media Pool, a folder called Camera Uploads is created. This folder is where all the Live Sync

media will be accessed from. Each thumbnail in the folder has icons that tell you the status of each clip.

A red dot in the upper-right corner of a clip shows you which clip is currently “live” and being recorded

to at the moment.

The Cut page Media Pool showing the proxy and sync status of the clips in the Camera Uploads

Folder. The clip with the red dot in the upper-right corner is currently being recorded “live.”

Working with Live Sync Clips

Working with Live Sync clips in the Cut or Edit pages is very similar to working with normal clips with

the exception that the Live Sync clip is constantly expanding. What this means in practice is while you

are scrubbing the footage and marking In and Out points in the Viewer, the Live Sync clip automatically

gets longer as new material is downloaded. This process does not require any action on the part of

the editor to “refresh” the clip, so there is never any need to leave the Viewer. As the clip grows and

something newly interesting happens, you can update the clip with a new set of In and Out points to

edit it into the timeline. You can always leave the Live Sync clip to edit with other previously recorded

shots, and it will still be there when you return… quietly growing….


Blackmagic Cloud | Chapter 195 Live Sync

DELIVER

The Edit page showing a Live Sync clip growing in the Source Viewer. As the clip grows in size, you

can update the In and Out points in the Viewer to add new sections of the clip into the timeline.

The Live Sync clip is limited in length only by your storage capacity, and the speed at which

it updates is dependent on the speed of the internet connection for both the Blackmagic

Camera and the DaVinci Resolve workstation.


Blackmagic Cloud | Chapter 195 Live Sync

DELIVER

DELIVER

Project Libraries,

Collaborative, and

Remote Workflows

CONTENTS

196	 Managing Project Libraries and Project Servers������������������������������������������������������������������������ 4158

197	 Collaborative Workflow������������������������������������������������������������������������������������������������������������������������ 4178

198	 Remote Grading and Remote Monitor�������������������������������������������������������������������������������������������� 4193

Chapter 196

Managing Project

Libraries and

Project Servers

This chapter describes how to set up and use project libraries in greater detail,

giving you more control over how projects are saved and organized.

The chapter details how to set up local, network, and cloud project libraries you can use to administer

DaVinci Resolve projects that are available to multiple DaVinci Resolve workstations.

Contents

What is a Project Library?�������������������������������������������������������������������������������������������������������������������������������������������������������������� 4159

Using Project Libraries�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4159

Local Project Libraries��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4160

Creating a New Local Project Library��������������������������������������������������������������������������������������������������������������������������������������� 4160

Connecting to an Existing Local Project Library������������������������������������������������������������������������������������������������������������������� 4161

Disconnecting from a Local Project Library��������������������������������������������������������������������������������������������������������������������������� 4162

Duplicating Project Libraries��������������������������������������������������������������������������������������������������������������������������������������������������������� 4162

Backing up a Local Project Library��������������������������������������������������������������������������������������������������������������������������������������������� 4162

Restoring a Local Project Library������������������������������������������������������������������������������������������������������������������������������������������������ 4163

Upgrading a Local Project Library���������������������������������������������������������������������������������������������������������������������������������������������� 4163

Network Project Libraries�������������������������������������������������������������������������������������������������������������������������������������������������������������� 4164

Multiple Users Sharing Projects�������������������������������������������������������������������������������������������������������������������������������������������������� 4164

Using Collaborative Workflow for Network Project Libraries��������������������������������������������������������������������������������������� 4164

Connecting to a Network Project Library on a DaVinci Resolve Project Server������������������������������������������������� 4165

Creating a New Network Project Library�������������������������������������������������������������������������������������������������������������������������������� 4165

Connecting to an Existing Network Project Library���������������������������������������������������������������������������������������������������������� 4166

Disconnecting from a Network Project Library��������������������������������������������������������������������������������������������������������������������� 4167

Backing up a Network Project Library��������������������������������������������������������������������������������������������������������������������������������������� 4167

Restoring a Network Project Library������������������������������������������������������������������������������������������������������������������������������������������ 4167


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER

Duplicating a Network Project Library������������������������������������������������������������������������������������������������������������������������������������� 4168

Optimizing a Project Library���������������������������������������������������������������������������������������������������������������������������������������������������������� 4168

Sharing a Key to a Network Project Library��������������������������������������������������������������������������������������������������������������������������� 4168

Using the DaVinci Resolve Project Server Application�������������������������������������������������������������������������������������������������� 4169

Installing the DaVinci Resolve Project Server���������������������������������������������������������������������������������������������������������������������� 4169

The DaVinci Resolve Project Server Interface��������������������������������������������������������������������������������������������������������������������� 4169

Creating New Network Project Libraries����������������������������������������������������������������������������������������������������������������������������������� 4171

Backing Up and Restoring Project Libraries��������������������������������������������������������������������������������������������������������������������������� 4172

Upgrading Project Libraries������������������������������������������������������������������������������������������������������������������������������������������������������������ 4172

Viewing Project Library Contents������������������������������������������������������������������������������������������������������������������������������������������������ 4173

Optimizing Project Libraries����������������������������������������������������������������������������������������������������������������������������������������������������������� 4173

Member Management in the DaVinci Resolve Project Server�������������������������������������������������������������������������������������� 4173

Sharing Network Project Libraries via the Project Server��������������������������������������������������������������������������������������������� 4176

Cloud Project Libraries��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4177

What is a Project Library?

A Project Library (formerly project database), is a database file storing one or more DaVinci Resolve

projects. When you create or load a project from the Project Manager, or save a current project,

you read from or write to a project library. A project library contains multiple projects, and each

project contains all the timelines, grades, clip metadata, visual effects, audio mixing, etc. for your film.

A project library does not store the original media itself, only the instructions on how to use that media

to create a finished film. DaVinci Resolve can access multiple project libraries, but can only connect to

one project library at a time.

Using Project Libraries

Setting up a structure for storing projects and project libraries is an important part of creating

streamlined and efficient workflows. For example, creating a separate project library for each TV

series, commercial, or film a post house is working on helps compartmentalize your clients, and

improves performance by only loading up what you need for a specific project.

There are three ways DaVinci Resolve uses to access project libraries, and the choice of which to use

is largely determined by the amount of people working on the same project, and where they are in the

world. Each option is described in detail below.

The three types of Project Libraries: local, network, and cloud

�Local Project Libraries: (the default option) Best used for productions using a single workstation

to complete the entire film. Multiple people may work on the same project, but they work one

at a time on the same machine. Your project libraries are stored locally on the computer where

DaVinci Resolve is installed, and all media drives in the project are connected locally.


Project Libraries, Collaborative, and Remote Workflows | Chapter 196 Managing Project Libraries and Project Servers

DELIVER

�Network Project Libraries: Best used for post houses or productions that have multiple DaVinci

Resolve workstations in the same building, and want to be able to work on the same project from

each room, or collaboratively at the same time. Your project libraries are stored on a separate

computer, running the DaVinci Resolve Project Server application. All workstations must be

connected to this computer on the same local area network (LAN), and either connected to the

same media drives via a NAS or MAM system, or each having a locally connected copy (or proxies)

of the media available.

�Cloud Project Libraries: Best used for post houses, companies or productions that have multiple

DaVinci Resolve workstations in different places around the world, and want to be able to work on

the same project from each location individually, or collaboratively at the same time. Your project

libraries are stored in the Blackmagic cloud service. All workstations must be connected to the

internet, and each system must have a locally connected copy (or proxies) of the media available.

Navigating and using the Project Libraries sidebar is common to all the above types of

project libraries.

Project Library: Each accessible project library is listed by name, and clicking on it will

connect that library and its contained projects to DaVinci Resolve. You can choose from many

libraries, but only one library can be active at a time.

Project Libraries sidebar controls

(L-R): Sort, Restore, Search

•	 Sort Libraries: Selects the sort order of how the project libraries appear, options are

Name, Schema (date), Status, and Location. They can be sorted in both Ascending and

Descending order.

•	 Restore: Allows you to load a project library that you previously backed up.

•	 Search: Allows you to search for a specific project library by text, and you can limit the

search by Name, Schema, Status, and Location.