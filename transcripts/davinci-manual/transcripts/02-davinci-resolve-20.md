---
title: "DaVinci Resolve 20"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 2
---

# DaVinci Resolve 20

Getting Started

When you install DaVinci Resolve and then open it for the first time, there are a few things you’re going

to want to know before you begin learning how to work.

Automatic DaVinci Resolve Updates

To make it easier to ensure you’re using the latest version of DaVinci Resolve, you can now

choose DaVinci Resolve > Check For Updates to notify you of new versions and download them

when available.

Why Is This Manual So Big?

Over the years, DaVinci Resolve has evolved to encompass professional editing, compositing, and

audio mixing tools and workflows in addition to the grading tools that were the original core of

DaVinci Resolve. Each one of these domains of functionality is incredibly deep. Consequently, the

documentation has grown with each new page, tool, and parameter that’s been added, to make life

easier and to solve the countless problems that can emerge during the postproduction process.

While it is regretted that this user manual contains such a staggeringly overwhelming amount of

information, our emphasis has always been to ensure that (hopefully) every control and workflow

you encounter in DaVinci Resolve is explained somewhere within the contents of these pages.

Consequently, we hope that you find the hyperlinked table of contents (TOC) and search functionality

of your preferred PDF browser helpful in finding the information you need, along with context and tips

to help you get the most out of the tools provided.


DaVinci Resolve 20 Getting Started

INTRO

Navigation Guide

For ease of use navigating this manual, each table of contents (TOC) listed on this manual are

hyperlinked, and by clicking on each title or page number, you will be taken to the appropriate

part of the manual. On the right hand side of each page includes a hyperlink tab. As you hover the

pointer over the tab and by clicking on the tab you will be taken to main TOC page.

Chapter 131

Primaries Palette

This chapter focuses on the core color adjustments that you’ll be making to

create “primary” corrections that alter the overall color and contrast of the image

using both the Lift/Gamma/Gain adjustments in the Wheels and Bars modes of

the Primaries palette, and the Shadow/Midtone/Highlight/Offset controls in the

Log mode, both of which have traditionally formed the foundation of most grades.

Contents

Introduction to the Primaries Palette �������������������������������������������������������������������������������������������������������������������������������������� 3059

HDR Grading With the Primaries Palette �������������������������������������������������������������������������������������������������������������������������������� 3060

Which Do I Start With, the Primaries or HDR Palette? ������������������������������������������������������������������������������������������������������ 3060

Shared Controls in the Primaries Palette ������������������������������������������������������������������������������������������������������������������������������ 3060

Switching Between Primaries Tools������������������������������������������������������������������������������������������������������������������������������������������ 3060

Color Balance Controls �������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3061

Master Wheels �������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3061

Numeric Parameters ������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3062

Shared Adjustment Controls �������������������������������������������������������������������������������������������������������������������������������������������������������� 3062

Auto Correction ���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3064

Reset Controls ������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3064

Color Wheels and Bars ������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3065

3-Way Master Wheel Adjustments �������������������������������������������������������������������������������������������������������������������������������������������� 3066

Offset Color and Master Controls ���������������������������������������������������������������������������������������������������������������������������������������������� 3067

Color Bars Mode �������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3068

Log Wheels Mode ����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3068

Using the Log Mode Controls to Grade Log-Encoded Media ������������������������������������������������������������������������������������� 3069

Using the Log Mode Controls to Stylize Normalized Media ������������������������������������������������������������������������������������������ 3071

Adjusting the Default Tone Ranges in Log Mode �������������������������������������������������������������������������������������������������������������� 3073

Adjusting Contrast in Log Mode ������������������������������������������������������������������������������������������������������������������������������������������������� 3073

Log Offset Color and Master Controls ������������������������������������������������������������������������������������������������������������������������������������� 3073

Offset and Printer Points ���������������������������������������������������������������������������������������������������������������������������������������������������������������� 3074

Adjusting Printer Points in the Bars Mode ������������������������������������������������������������������������������������������������������������������������������ 3074

Adjusting Printer Points Via Keyboard Shortcuts��������������������������������������������������������������������������������������������������������������� 3075

Printer Light Step Project Settings �������������������������������������������������������������������������������������������������������������������������������������������� 3076


Color | Chapter 131 Primaries Palette

COLOR

Saving and Wiping Stills in the Gallery and Timeline

The Gallery on the Color page provides fast access to stills that you’ve saved from various clips in the

Timeline. While the dedicated Gallery page provides a more comprehensive interface for browsing

presaved “looks,” as well as for importing stills from other projects, you can save, organize, and

browse stills directly within the Gallery of the Color page.

Stills are saved in the DPX file format. Once you’ve saved one or more stills, you can set up split

screen wipes in the Viewer, which will be mirrored to your external display.

Stills from the Gallery can be compared to the current shot, making it easier to match grades.

This section provides an abbreviated summary of still store and split screen functionality to get you

started quickly.

To save a still, do one of the following:

�Choose Color > Stills > Grab Still (Option-Command-G).

�Right-click on the Viewer and choose Grab Still.

To wipe a still, do one of the following:

�Select a still in the Gallery, and click the Image Wipe button on the top Viewer toolbar.

�Choose Color > Stills > Play Still (Command-W), or right-click in the Viewer and choose Toggle Wipe.

�Double-click a still in the Gallery.

To adjust a wipe in the Viewer, do one of the following:

�Drag the pointer within the Viewer to move the wipe.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Hyperlink Tab

Section Name

COLOR

Color

CONTENTS


Introduction to Color Grading ���� 2953


Using the Color Page �������������������� 2965


Viewers, Monitoring,

and Video Scopes �������������������������� 2983


Color Page Timeline

and Lightbox �������������������������������������� 3023


Automated Grading Commands

and Imported Grades �������������������� 3038


Camera Raw Palette ���������������������� 3052


Primaries Palette ����������������������������� 3058


HDR Palette ���������������������������������������� 3077


Primary Grading Controls �������������� 3101


Curves ��������������������������������������������������� 3107


ColorSlice ��������������������������������������������� 3128


Color Warper ��������������������������������������� 3135


Secondary Qualifiers ����������������������� 3157


Secondary Windows ����������������������� 3185


Magic Mask ������������������������������������������ 3201


Motion Tracking Windows ����������� 3229


Using the Gallery ����������������������������� 3256


Grade Management ������������������������ 3273


Node Editing Basics ����������������������� 3308


Image Processing

Order of Operations ������������������������ 3329


Serial, Parallel,

and Layer Nodes ������������������������������ 3332


Combining Keys

and Using Mattes ���������������������������� 3340


Channel Splitting

and Image Compositing ��������������� 3365


Keyframing in the Color Page ���� 3380


Copying and Importing

Grades Using ColorTrace ������������� 3395


Using LUTs ����������������������������������������� 3405


Tracking Nodes ������������������������������������������������������������������������������������������������������������������������������������������������������� 2732


Transform Nodes ���������������������������������������������������������������������������������������������������������������������������������������������������� 2788


USD Nodes ��������������������������������������������������������������������������������������������������������������������������������������������������������������� 2816


VR Nodes ������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2869


Warp Nodes ������������������������������������������������������������������������������������������������������������������������������������������������������������� 2880


Modifiers �������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2910

Color


Introduction to Color Grading ������������������������������������������������������������������������������������������������������������������������� 2953


Using the Color Page ������������������������������������������������������������������������������������������������������������������������������������������ 2965


Viewers, Monitoring, and Video Scopes ���������������������������������������������������������������������������������������������������� 2983


Color Page Timeline and Lightbox ���������������������������������������������������������������������������������������������������������������� 3023


Automated Grading Commands and Imported Grades ���������������������������������������������������������������������� 3038


Camera Raw Palette �������������������������������������������������������������������������������������������������������������������������������������������� 3052


Primaries Palette ��������������������������������������������������������������������������������������������������������������������������������������������������� 3058


HDR Palette �������������������������������������������������������������������������������������������������������������������������������������������������������������� 3077


Primary Grading Controls ������������������������������������������������������������������������������������������������������������������������������������ 3101


Curves �������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3107


ColorSlice ������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3128


Color Warper ������������������������������������������������������������������������������������������������������������������������������������������������������������ 3135


Secondary Qualifiers ��������������������������������������������������������������������������������������������������������������������������������������������� 3157


Secondary Windows ��������������������������������������������������������������������������������������������������������������������������������������������� 3185


Magic Mask ��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3201


Motion Tracking Windows ��������������������������������������������������������������������������������������������������������������������������������� 3229


Using the Gallery��������������������������������������������������������������������������������������������������������������������������������������������������� 3256


Grade Management ���������������������������������������������������������������������������������������������������������������������������������������������� 3273


Node Editing Basics ��������������������������������������������������������������������������������������������������������������������������������������������� 3308


Image Processing Order of Operations ������������������������������������������������������������������������������������������������������ 3329


Serial, Parallel, and Layer Nodes �������������������������������������������������������������������������������������������������������������������� 3332


Combining Keys and Using Mattes ��������������������������������������������������������������������������������������������������������������� 3340


Channel Splitting and Image Compositing ����������������������������������������������������������������������������������������������� 3365


Keyframing in the Color Page ������������������������������������������������������������������������������������������������������������������������� 3380


Copying and Importing Grades Using ColorTrace ��������������������������������������������������������������������������������� 3395


Using LUTs ��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3405

Contents

INTRO

MEDIA

CUT

EDIT

FUSION

COLOR

FAIRLIGHT

DELIVER

MENU


Section Page

Main TOC

Page Number

Chapter Number

Chapter Page

Page Number

Chapter Name


DaVinci Resolve 20 Getting Started

INTRO

INTRO

DaVinci Resolve

Interface

CONTENTS


Introduction to DaVinci Resolve������������������������������������������������������������������������������������������������������������� 14


Using the DaVinci Resolve User Interface���������������������������������������������������������������������������������������� 56

Chapter 1

Introduction to

DaVinci Resolve

DaVinci Resolve integrates editing, compositing and motion graphics,

color correction, audio recording and mixing, and finishing within a single,

easy to learn application. The editing, compositing, grading, and audio tools

found in DaVinci Resolve should be immediately familiar to experienced artists

who’ve used other applications, but they’re also approachable to folks who are

new to post-production.

Additionally, dedicated tools available for on-set workflows integrate tasks such as media duplication,

shot and metadata organization, and on-location look management into a complete toolset that lets

you smoothly segue from the camera original media being acquired in the field to the organization and

use of that media in a wide variety of post‑production workflows with DaVinci Resolve at their heart.

In particular, the tight integration in DaVinci Resolve means that you can freely move from one task to

the next of your project’s workflow without skipping a beat, making it easy to back up and organize a

shoot’s media before immediately diving into editing, while switching over to add a quick composite

or to color-correct clips in the middle of your editing spree, and then getting right back to cutting,

with a bit of mixing to make sure things sound right, all without needing to export projects or launch

other applications.

And you can go further, using the collaborative features of DaVinci Resolve to enable multiple artists,

for example an editor, a colorist, and assistants, to work together on the same timeline simultaneously,

for the ultimate integrated workflow.

Of course, no post-production professional works in a vacuum, and DaVinci Resolve makes it easy to

work with other facilities by importing projects and exporting project exchange formats and rendered

or managed media among applications such as Apple’s Final Cut Pro X, Adobe’s Premiere Pro, Avid’s

Media Composer and Pro Tools, Autodesk’s Flame Premium, and many other applications via robust

support of XML, AAF, and EDL import and export workflows.

This chapter introduces the DaVinci Resolve user interface (UI), explaining where to find each group

of features, and how the highly focused and tightly integrated Media, Edit, Fusion, Color, Fairlight,

and Deliver pages work together to let you pursue nearly any post‑production workflow you can

imagine. After this brief tour, the rest of Part 1 of this manual provides much more in‑depth information

about project management, preferences, project settings, and other topics of general interest for

getting started.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Contents

The Project Manager����������������������������������������������������� 16

Preferences and Project Settings��������������������������� 17

Individual Preferences

and Settings Based on Login������������������������������������� 17

Preferences������������������������������������������������������������������������� 17

System Preferences�������������������������������������������������������� 18

User Preferences������������������������������������������������������������� 19

Project Settings�������������������������������������������������������������� 20

Switching Among Pages���������������������������������������������� 21

Minimizing the Resolve Page Bar����������������������������� 21

Switching Pages Using Keyboard Shortcuts������ 21

Hide Pages You Don’t Use������������������������������������������ 21

Hide Page Navigation Altogether�������������������������� 22

The Media Page������������������������������������������������������������� 22

The Media Storage Browser�������������������������������������� 23

Viewer���������������������������������������������������������������������������������� 23

Media Pool������������������������������������������������������������������������� 24

Metadata Editor��������������������������������������������������������������� 25

Audio Panel������������������������������������������������������������������������ 25

The Cut Page�������������������������������������������������������������������� 26

The Media Pool���������������������������������������������������������������� 26

The Viewer������������������������������������������������������������������������� 27

Audio Meter����������������������������������������������������������������������� 28

The Timeline���������������������������������������������������������������������� 28

The Edit Page������������������������������������������������������������������ 29

The Media Pool��������������������������������������������������������������� 30

Effects Library Browsing�������������������������������������������� 30

Edit Index����������������������������������������������������������������������������� 31

Source/Offline and Timeline Viewers������������������� 32

Inspector����������������������������������������������������������������������������� 33

Toolbar��������������������������������������������������������������������������������� 33

Timeline������������������������������������������������������������������������������� 33

Floating Timecode Window��������������������������������������� 34

Motion Graphics and

Visual Effects in DaVinci Resolve�������������������������� 34

VFX Connect��������������������������������������������������������������������� 35

The Fusion Page������������������������������������������������������������� 36

The Work Area������������������������������������������������������������������ 36

Viewers�������������������������������������������������������������������������������� 37

Toolbar��������������������������������������������������������������������������������� 37

Effects Library������������������������������������������������������������������� 38

Node Editor������������������������������������������������������������������������ 38

Inspector����������������������������������������������������������������������������� 39

Thumbnail Timeline������������������������������������������������������ 40

Media Pool������������������������������������������������������������������������ 40

Status Bar����������������������������������������������������������������������������� 41

The Console����������������������������������������������������������������������� 41

The Color Page���������������������������������������������������������������� 42

Viewer���������������������������������������������������������������������������������� 42

Gallery���������������������������������������������������������������������������������� 43

Node Editor������������������������������������������������������������������������ 44

Timeline������������������������������������������������������������������������������� 44

Left Palettes����������������������������������������������������������������������� 45

Center Palettes���������������������������������������������������������������� 45

Keyframe Editor��������������������������������������������������������������� 46

The Fairlight Page���������������������������������������������������������� 47

The Audio Timeline�������������������������������������������������������� 47

Toolbar��������������������������������������������������������������������������������� 49

Mixer������������������������������������������������������������������������������������� 49

Dedicated Channel Strip Controls�������������������������� 49

The Monitoring Panel���������������������������������������������������� 51

Floating Timecode Window��������������������������������������� 52

The Deliver Page������������������������������������������������������������ 52

The Render Settings List��������������������������������������������� 53

The Deliver Page Timeline����������������������������������������� 53

The Viewer������������������������������������������������������������������������� 54

The Render Queue�������������������������������������������������������� 55


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO