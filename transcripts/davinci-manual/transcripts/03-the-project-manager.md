---
title: "The Project Manager"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 3
---

# The Project Manager

For most users, Project Manager is the first window you’ll see when you open DaVinci Resolve.

The Project Manager is a centralized interface for managing all projects belonging to the user

who’s currently logged in, whose name appears at the upper right-hand corner in a project title

bar. The Project Manager is also the place where you import and export projects to and from

DaVinci Resolve, whether you’re moving projects around from user to user, or moving projects from

one DaVinci Resolve workstation to another. Finally, the Project Manager also lets you organize

the project libraries that are used to manage everything in DaVinci Resolve using the Project

Library sidebar.

To open any project, double-click it. To create a new project, double-click the Untitled Project icon,

or click the New Project button.

The Project Manager shows all projects belonging to the current user.

For more information about the Project Manager, see Chapter 3, “Managing Projects and

Project Libraries.”


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Preferences and Project Settings

Once you open a project, you have the option of adjusting the System and User Preferences that

govern the installation of DaVinci Resolve on your workstation, and the Project Settings governing the

currently open project. When you first install DaVinci Resolve, the most important of these settings are

selected via the installer’s on boarding questions. However, if you’re opening DaVinci Resolve for the

first time, you should probably check these settings to make sure they’re optimal for your system.

Individual Preferences and Settings Based on Login

As of DaVinci Resolve 16, there are individual preferences and settings for each login account on a

given computer. This means that multiple artists can each have their own login, and DaVinci Resolve

will maintain separate workspace layouts and preference states for each artist, depending on who’s

logged in.

Preferences

The Preferences window, divided into System preferences and User preferences panels, lets you set

up the overall environment of your DaVinci workstation, choosing what hardware to use with DaVinci

Resolve and what user interface settings you prefer as you work.

The DaVinci Resolve preferences let you set up your environment


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

A quick overview of the most important System and User preferences appears below, with

guidance about the first settings you should adjust when you first set DaVinci Resolve up on

your workstation. However, for a comprehensive overview and for more information,

see Chapter 4, “System and User Preferences.”

System Preferences

The System preferences let you configure the hardware DaVinci Resolve works with. If you have a

system that doesn’t change very often, then you may only rarely use the Preferences window. On the

other hand, if you’re working with a mobile system with changing video interfaces, control panels, and

scratch volumes, then you may use this window more frequently.

NOTE: Whenever you change certain core System Settings in the Preferences, you may have

to quit and restart DaVinci Resolve for those changes to take effect.

Memory and GPU

Lets you choose various options governing how to use the GPUs attached to your computer, and

how to configure Viewers in different pages. This panel also provides an overview, for reference,

of all hardware and computer characteristics that are relevant to DaVinci Resolve running smoothly,

including a listing of installed GPUs.

Media Storage

This is a list within which you define the scratch disk used by your system. The first volume in this list

is where Gallery stills and cache files are stored, so you want to make sure that you choose the fastest

storage volume that’s connected.

Decode Options

These settings let you select various hardware options for decoding RAW files and H.264/H.265. It

also lets you choose to use the easy DCP decoder and the ability to refresh growing any files (files that

are in the process of being written) in the Media Pool.

Video and Audio I/O

The preferences in this panel let you choose which video and audio Capture and Monitor interfaces

you want DaVinci Resolve to use on your workstation. If you have multiple Blackmagic Design

I/O interfaces connected to your computer, you can choose between them.

Video Plugins

If you have any third-party Open FX  plugins installed, you can see them and enable/disable

them here.

Audio Plugins

If you have any third-party VST plugins installed, you can see them and enable/disable them here.

Control Panels

Lets you choose and configure (if necessary) a control panel that’s connected for use during grading in

DaVinci Resolve.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

General

Lets you choose from a variety of settings that modify DaVinci Resolve’s behavior. The LUT Locations

section lets you point DaVinci Resolve to any external folders containing LUTs for use in your project.

Internet Accounts

The Internet Accounts panel serves as a login manager for the Blackmagic Cloud and other social

media sites.

Advanced

This tab is used for special DaVinci Resolve configurations and SAN parameters that are applicable to

older file systems.

User Preferences

User preferences govern the setup of the user interface in DaVinci Resolve, letting you customize

it to work the way you like.

UI Settings

A Language drop-down menu at the top lets you specify which language the DaVinci Resolve user

interface displays. DaVinci Resolve currently supports English, Chinese, Japanese, and Spanish,

Portuguese, French, Russian, Thai, Vietnamese, and Korean. Additional checkboxes let you choose

options for which project to open during startup, and how to configure the Viewers that appear in

every page of DaVinci Resolve.

Project Save and Load

This panel contains the all-important auto-save controls, including the Live Save option that enables

Resolve to incrementally save your changes as you work.

Editing

Numerous controls in this panel let you customize the editing experience in the Edit page, including

default settings to use when making new timelines, and general settings that govern standard effects

durations and trim behaviors.

Color

These controls let you customize the grading experience in the Color page, with options controlling

video scope display, the look of UI overlays, and other color-specific functions.

Fairlight

These controls let you customize the editing experience in the Fairlight page with options controlling

video offset, automation, and general settings.

Playback Settings

These controls let you customize how DaVinci Resolves handles video playback. If your playback is

too slow, adjusting these settings may help.

Control Panels

These controls let you customize the settings of your connected control surface.

Metadata

These controls let you customize the Metadata Presets.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Project Settings

Once you’ve created a project, all project-specific settings are found in the Project Settings window.

To open the Project Settings window, just click the gear button at the bottom right on any page.

Project Manager and

Project Settings buttons

The Project Settings open in the middle of the screen, divided into a series of panels which can be

selected from a sidebar to the left. Each panel contains a collection of related settings that affects

some category of DaVinci Resolve functionality. To open a panel of settings, simply click its name in

the sidebar at the left.

The Project Settings show all project-specific settings and attributes.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

The Master Settings define the principal attributes of a project, such as the timeline resolution,

timeline frame rate, color science, and bit depth. Image Scaling settings define how clips that

don’t match the timeline resolution are scaled to fit. There are other panels for Color Management,

Camera Raw, Capture and Playback, etc.

For more information about Project Settings, see Chapter 4, “System and User Preferences.”