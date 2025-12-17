---
title: "Multiple Colorists Working Together"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 757
---

# Multiple Colorists Working Together

Only one colorist can work on a particular clip at a particular time, and the first colorist to select a

clip puts a lock on that clip. Other collaborators looking at the Thumbnail timeline in the Color page

will see a small icon that shows it’s locked, letting them know they can’t make any changes to it until

whoever is grading that clip moves to another clip.

A small icon indicates that you’re locked out

because another colorist is grading that clip.

In order to prevent half-finished work from being disseminated to other colorists or editors, a clip that’s

in the process of being graded isn’t updated for other collaborators that are looking at that timeline

until the colorist who’s working on it selects another clip. These changes are then automatically made

available to all other collaborators working in the Color page, who see badges appear in the Edit and

Color pages to indicate which clips have updates available.

This makes it easy for multiple colorists to work together. For example, an assistant colorist can be

notified via Collaborative Chat to draw a custom window that a senior colorist needs for a grade.

The assistant opens that timeline in another suite, selects the appropriate clip, and draws the window.

Once finished, the assistant simply selects a different clip, and the changes they’ve made are

immediately available to the senior colorist, who sees a badge on that clip in the Thumbnail timeline

and can click to update it.

Managing Notes Among Collaborators

If an editor wants to send a note to colorists or compositing artists, they can do one of the following:

�They can add a marker with note text to the Timeline ruler (the marker appears in the marker

submenu in the Color page Viewer option menu)

�They can add a marker with note text to a clip (that marker appears in the mini-timeline of

the Color page)

�They can color code clips in different ways to get the colorist’s attention (clip color coding appears

as a dot in the Thumbnail timeline).

�Of course, the editor and colorist can always interact via the collaborative chat window, as well.


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

Collaboration Chat

To facilitate communication among collaborators, DaVinci Resolve has built-in text chat, called

Collaboration Chat. Simply click the Collaboration Chat button to open the chat window, and

chat away.

The Collaboration Chat window for

communication among collaborators

The Collaboration Chat button at the bottom of the DaVinci Resolve interface highlights

orange whenever someone texts while this window is closed, letting you know you have

messages that are waiting.

The Collaboration Chat

button highlights to let you

know you have a message.


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

Chapter 198

Remote Grading

and Remote Monitor

This chapter describes how to set up Remote Grading using two separate

DaVinci Resolve systems in different locations via the internet, to have one system

remotely control the other for color grading. While DaVinci Remote Monitor allows

you to stream a high quality video signal from one DaVinci Resolve system to

another workstation over the internet or on the same network.

Contents

Introduction to Remote Grading������������������������������������������������������������������������������������������������������������������������������������������������� 4194

Requirements for Remote Grading������������������������������������������������������������������������������������������������������������������������������������������� 4194

Setting Up for Remote Grading�������������������������������������������������������������������������������������������������������������������������������������������������� 4194

Remote Grading Restrictions������������������������������������������������������������������������������������������������������������������������������������������������������� 4195

DaVinci Remote Monitor (Studio Version Only)������������������������������������������������������������������������������������������������������������������� 4195

Requirements for DaVinci Remote Monitor�������������������������������������������������������������������������������������������������������������������������� 4196

Setting Up DaVinci Remote Monitor���������������������������������������������������������������������������������������������������������������������������������������� 4196

DaVinci Remote Monitoring Using IP Address Connections�������������������������������������������������������������������������������������� 4199

DaVinci Remote Monitoring via User Specified TURN Servers���������������������������������������������������������������������������������� 4200

DaVinci Remote Monitor Restrictions�������������������������������������������������������������������������������������������������������������������������������������� 4201


Project Libraries, Collaborative, and Remote Workflows | Chapter 198 Remote Grading and Remote Monitor

DELIVER

Introduction to Remote Grading

To enable colorists to work interactively with clients across the globe, DaVinci Resolve offers a remote

grading option. It allows two matching DaVinci Resolve systems to be synchronized via an Internet

connection such that changes made on the colorist’s workstation are immediately applied on the

remote client’s workstation.

Cue commands are also synchronized to ensure that both systems are always on the same frame in

the Timeline. Starting or stopping playback on the colorist’s DaVinci Resolve also starts and stops the

remote client system. While a remote grading session is in progress, input from the user at the remote

client’s DaVinci Resolve workstation is ignored.

Currently, the remote grading feature supports only color correction and does not allow editing

or conforming during a session. The two colorist and remote DaVinci Resolve systems must have

matching timelines and the number of clips, clip durations, and system resolutions must match. The

requirements and limitations of a remote grading session are summarized below.

Requirements for Remote Grading

�The same version of DaVinci Resolve must be installed on both systems.

�The Timeline to be graded must be conformed on both machines prior to the start of the remote

grading session.

�The number of clips on the Timeline and the duration of each clip must be identical.

�While grading, the active Timeline and versions on the remote client system are constantly

updated. Creating, deleting, or switching the Timeline on the client’s DaVinci Resolve is not

allowed. Doing so will terminate the remote grading session immediately.

�You cannot make any grading adjustments on the remote client’s DaVinci Resolve workstation

until the remote grading session has ended.

NOTE: Remote grading does not require a shared project library.

Setting Up for Remote Grading

To start a remote grading session, the client’s DaVinci Resolve must be able to connect to the

colorist’s system using TCP/IP.


Open DaVinci Resolve on the remote client’s workstation (the one that’s being remotely

controlled), log in, and open the project that will be remotely graded.


Choose Workspace > Remote Grading (Ctrl-G) on the remote client’s workstation. A window is

displayed with text fields to enter the IP address and port number of the colorist’s system.


Set the IP address field to the IP of the colorist’s DaVinci Resolve workstation. If the colorist’s

system already has a public IP address, the port number can be left at its default value (15000).

If the colorist’s system is on a private network, the colorist or their network administrator should

set the port number to one on the public IP router that is internally routed to port 15000 of the

colorist’s DaVinci Resolve.


Project Libraries, Collaborative, and Remote Workflows | Chapter 198 Remote Grading and Remote Monitor

DELIVER


Once the remote client clicks Connect, the client’s DaVinci Resolve system will attempt to

establish a connection with the remote colorist’s workstation.


Once the connection is established, a pop-up appears on the colorist’s screen asking for

permission to accept a Remote Grading connection.


Click OK to accept, minimize the size of this dialog window, and continue grading normally.

The Remote Grading session will remain active until one of the users chooses to disconnect or an

error occurs causing DaVinci Resolve to automatically terminate the session.

Remote Grading Restrictions

To allow operation over low bandwidth and a potentially long latency Internet connection there are

some restrictions to remote operation.

•	 When playback is started, the playback speeds on the two DaVinci Resolve systems

may differ. The frame positions are only guaranteed to be synchronized when playback

is stopped.

•	 Input/output/display LUTs applied from the Config page on the colorist’s DaVinci Resolve

will not have any effect on the client system. LUTs selected on the client’s DaVinci Resolve

will be applied instead.

•	 Presets applied from the Config/Color pages on the colorist’s system will not have any

effect on the client’s system. Presets selected on the client’s DaVinci Resolve will be

applied instead.

DaVinci Remote Monitor

(Studio Version Only)

DaVinci Remote Monitor is an application that allows you to have access to a low latency, high quality

video signal over a network for monitoring, editing, and color grading purposes. The DaVinci Remote

Monitor shows the output of the host’s Viewer in real time as they work in DaVinci Resolve. This

allows producers to monitor a session, while editors and colorists have the ability to work remotely

using the DaVinci Resolve interface and a data stream from a remote DaVinci Resolve workstation.

This data stream is of high enough quality that you can run the signal through a Blackmagic DeckLink

or UltraStudio device to a grading monitor and have the same confidence in the output as if it was

connected locally.

The stream quality can be adjusted for your particular needs and available bandwidth. For example, an

editor may only need an HD h.264 8-bit 4:2:0 codec for offline editing, while a colorist may need the

full UHD h.265 12 bit 4:4:4 RGB codec for HDR grading.

NOTE: For clarity in this section we will refer to the main DaVinci Resolve workstation in the

post house or data center that is streaming the video as the “Resolve Host” and the devices

that are receiving the stream as the “Resolve Clients.” However, in reality these are all just

devices running the same version of the DaVinci Resolve Studio and the DaVinci Remote

Monitoring apps.


Project Libraries, Collaborative, and Remote Workflows | Chapter 198 Remote Grading and Remote Monitor

DELIVER