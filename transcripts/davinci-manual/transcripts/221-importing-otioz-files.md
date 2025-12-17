---
title: "Importing .otioz Files"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 221
---

# Importing .otioz Files

The process for importing .otioz files is the same as above with the following difference:

�If an .otioz file was selected for import, the media assets will unzip themselves into a folder at

the same place as the .otioz file and automatically link themselves. Make sure you have enough

space for this.


Import and Conform Projects | Chapter 61 Conforming OTIO Files

EDIT

Chapter 62

Conforming

ADL Files

This chapter covers all workflows that let you import and conform timelines using

the AES31 Audio Decision List format (.adl).

Contents

More About Conforming ADL Files������������������������������������������������������������������������������������������������������������������������������������������� 1208

Importing ADL Project Files���������������������������������������������������������������������������������������������������������������������������������������������������������� 1208


Import and Conform Projects | Chapter 62 Conforming ADL Files

EDIT

More About Conforming ADL Files

DaVinci Resolve supports the AES31 Audio Decision List (.adl) format for import. ADL is a timeline

interchange format created by the Audio Engineering Society. It’s designed to be application

and platform agnostic, allowing you to pass your timeline and its media assets between digital

audio workstations.

As of this writing DaVinici Resolve does not export ADL files.

Importing ADL Project Files

This section covers the import of ADL files using one simple procedure.

The AES31 Audio Decision List (.adl) import progress dialog

To import and Audio Decision List (.adl) file and automatically link to its referenced media:


Do one of the following:

�From any page, choose File > Import Timeline (Shift-Command-I).

�Open the Edit page, right-click anywhere in the Media Pool, and choose Timelines >

Import > AAF/EDL/XML/DRT/ADL/OTIO.


Using the file system dialog that appears, find the .adl project file you want to import, select the

file and press the Open button.


DaVinci Resolve will import the timeline, and proceed to import all the associated .wav files with

the ADL. An Import AES31 File dialog box will show you the progress of the import.

Unlike any of the other Timeline Import formats, there are no additional controls for importing an ADL

file. The timeline and associated media are imported directly to the open bin in the Media Pool.


Import and Conform Projects | Chapter 62 Conforming ADL Files

EDIT

FUSION

Fusion

Fundamentals

CONTENTS


Introduction to Compositing in Fusion��������� 1210


Exploring the Fusion Interface������������������������� 1216


Getting Clips into Fusion����������������������������������� 1264


Rendering Using Saver Nodes������������������������� 1291


Working in the Node Editor������������������������������� 1316


Node Groups, Macros,

and Fusion Templates����������������������������������������� 1366


Using Viewers�������������������������������������������������������� 1389


Editing Parameters in the Inspector�������������� 1432


Animating in Fusion’s Keyframes Editor������ 1458


Animating in Fusion’s Spline Editor���������������� 1476


Animating with Motion Paths��������������������������� 1508


Using Modifiers, Expressions,

and Custom Controls������������������������������������������ 1526


Preferences������������������������������������������������������������� 1538


Controlling Image Processing

and Resolution�������������������������������������������������������� 1587


Managing Color for Visual Effects����������������� 1598


Understanding Image Channels������������������������ 1611


Compositing Layers in Fusion�������������������������� 1647

80	 Rotoscoping with Masks������������������������������������ 1672


Paint��������������������������������������������������������������������������� 1696


Using the Tracker Node�������������������������������������� 1724


Planar Tracking������������������������������������������������������ 1760


Using Open FX, Resolve FX,

and Fuse Plugins��������������������������������������������������� 1767


3D Compositing Basics��������������������������������������� 1772


3D Camera Tracking��������������������������������������������� 1827


Particle Systems���������������������������������������������������� 1845


Optical Flow and Stereoscopic Nodes�������� 1854

Chapter 63

Introduction to

Compositing

in Fusion

This introduction is designed explicitly to help users who are new to Fusion get

started learning this exceptionally powerful environment for creating and editing

visual effects and motion graphics right from within DaVinci Resolve or using the

stand-alone Fusion Studio application.

This documentation covers both the Fusion Page inside DaVinci Resolve and the

stand-alone Fusion Studio application.

Contents

What Is Fusion?�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1211

The Fusion Page within DaVinci Resolve���������������������������������������������������������������������������������������������������������������������������������� 1211

The Fusion Studio Stand-Alone Application�������������������������������������������������������������������������������������������������������������������������� 1213

What Kinds of Effects Does Fusion Offer?������������������������������������������������������������������������������������������������������������������������������� 1213

How Hard Will This Be to Learn?�������������������������������������������������������������������������������������������������������������������������������������������������� 1215


Fusion Fundamentals | Chapter 63 Introduction to Compositing in Fusion

FUSION