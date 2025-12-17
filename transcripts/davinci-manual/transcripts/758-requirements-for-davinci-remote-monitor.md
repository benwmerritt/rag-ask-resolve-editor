---
title: "Requirements for DaVinci Remote Monitor"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 758
---

# Requirements for DaVinci Remote Monitor

In order to reliably stream a high-quality video signal from one system to another, there are some

technical hardware and software limitations and requirements for the Host and Clients.

The Resolve Host must have the following hardware and

software requirements for DaVinci Remote Monitor:

•	 The Resolve Host needs to have the Mac, Linux, or Windows version of

DaVinci Resolve Studio installed.

•	 For Linux and Windows users, the Resolve Host needs an RTX series NVIDIA GPU

and drivers installed. AMD and Intel GPUs are currently unsupported.

•	 The Host must have a Blackmagic Cloud account.

The Resolve Client must have the following hardware and

software requirements for DaVinci Remote Monitor:

•	 The Resolve Client needs to have the Mac, Linux, or Windows version of DaVinci Resolve

Studio installed. The DaVinci Remote Monitor App is automatically installed in the same

folder as DaVinci Resolve.

•	 Apple iPhone and iPad devices are supported as Client platforms. Download the

DaVinci Remote Monitor app from the App Store (The Studio Version of DaVinci Resolve is

not required on these devices).

•	 For Linux and Windows users, the Resolve Client needs an RTX series NVIDIA GPU and

drivers installed. AMD and Intel GPUs are currently unsupported.

•	 All Clients must have a Blackmagic Cloud account.

Setting Up DaVinci Remote Monitor

Setting up a Remote Monitor session is easily done from the DaVinci Resolve Studio interface:

additionally, the Host and all Clients must have Blackmagic Cloud accounts.

To Start a DaVinci Remote Monitor session as the Resolve Host:


The Resolve Host needs to be running the full DaVinci Resolve Studio version of the software.


Select Workspace > Remote Monitor.


Sign into your Blackmagic Cloud account, if necessary.


In the Remote Monitor Window, select the Video Codec and Bitrate you wish to use for the

session. Please note, the Video Codec used must be one that all the client devices support.


Project Libraries, Collaborative, and Remote Workflows | Chapter 198 Remote Grading and Remote Monitor

DELIVER

For maximum compatibility, H.264 4:2:0 8-bit is a good choice, however accurate color monitoring

may necessitate using another 10- or 12-bit codec instead. Bandwidth needs to increase with the

number of clients that are connected. While Remote Monitoring over the internet is possible, the

best performance will be had with a wired ethernet connection.

The DaVinci Remote Monitor Session Setup


Check the “Automatically accept connections” box to let anyone with the Session Code connect

directly. If you wish to approve each connection manually, uncheck this box.


Click the Start Session button.


Copy the generated Session Code from its field, and disseminate it to all the Resolve Clients via

email, text message, etc.

At this point your Remote Monitor has started, and a timer will show the duration of the current

session. A Remote Monitor icon will appear in the lower right of the DaVinci Resolve interface,

and the top of it will turn red to indicate that at least one Client has connected and you are

now “live.” A Session Participants field shows you who is currently connected as a Client.


Project Libraries, Collaborative, and Remote Workflows | Chapter 198 Remote Grading and Remote Monitor

DELIVER

The DaVinci Remote Monitor showing the time

connected and the participants involved

To Connect to a DaVinci Remote Monitor session as a Resolve Client:


The Resolve Client needs to have the full DaVinci Resolve Studio version of the software installed,

or the iOS app installed.


Launch the DaVinci Remote Monitor app on your device. This is found in your DaVinci Resolve

folder on your computer where you installed the software.


Sign into your Blackmagic Cloud account.


Paste the Session Code you received from the Resolve Host into the provided field.


Select the Output Device you wish to use for monitoring. This can be a connected computer

display, or a Blackmagic Decklink or UltraStudio device for color accurate monitoring.


Click the Join button.

The DaVinci Remote Monitor app Join screen


Project Libraries, Collaborative, and Remote Workflows | Chapter 198 Remote Grading and Remote Monitor

DELIVER

At this point your Remote Monitor window will appear, and you will see and hear the output of

the current viewer of the Resolve Host as they work.

NOTE: Remote Monitoring uses WebRTC to initiate connections between DaVinci Resolve

Studio and multiple clients. However, some heavily restricted network setups may still block

the initiation of a session, and a VPN may be required. A wired connection is recommended

for the best performance.

To End a DaVinci Remote Monitor session as the Resolve Host:


Click on the DaVinci Remote Monitor icon in the lower right of the interface.


Click on the End Session button to stop the Remote Monitor for all users, or click on the X next to

the name of a Client to disconnect the session for that user only.

To Leave a DaVinci Remote Monitor session as a Resolve Client:


Make the DaVinci Remote Monitor app active (not the Remote Monitor window).


Click on the Leave button to end your session.

To Change the Codec and Bitrate of a current DaVinci Remote Monitor

session as the Resolve Host:


Click on the DaVinci Remote Monitor icon in the lower right of the interface.


Click on the Settings icon in the upper right of the Remote Monitor window.


Select a new Codec and Bitrate for the video stream.


Click on the Save button.

This will change the streaming settings to the new codec and bitrate that you chose. Existing Clients

will be automatically reconnected to the new stream without having to do anything on their end.

This lets you easily change the quality of the video stream on the fly to compensate for bandwidth and

hardware issues.

DaVinci Remote Monitoring

Using IP Address Connections

As an option, you can use Remote Monitoring over normal IP Address Connections, rather than having

to sign in through Blackmagic Cloud. However, you will need some technical knowledge on setting up

your network appropriately.

Setting up Remote Monitoring over IP connections on the Resolve Host

Follow the instructions below to set up your host grading computer for other people to monitor.


Make sure you are signed out of Blackmagic Cloud in Preferences > Internet Accounts.


In Preferences > System > General, check the “Use Remote Monitoring without

Blackmagic Cloud” box.


Select Workspace > Remote Monitoring.


Adjust the codec and bit-rate parameters you want, then click Start Session.


Share the IP Address or configured host name for the Resolve host with the clients.


Project Libraries, Collaborative, and Remote Workflows | Chapter 198 Remote Grading and Remote Monitor

DELIVER

Setting up Remote Monitoring over IP connections on the Resolve Clients

Follow the instructions below to set up your client computer to monitor the host’s workstation.

The Use Remote Monitor without

Blackmagic Cloud settings in the computer and iOS versions


Launch the DaVinci Remote Monitor application.


In the Remote Monitor setup dialog, choose “Use Remote Monitor without Blackmagic Cloud.”


In the iOS or iPadOS versions of the App, go to the iOS Settings > DaVinci Monitor, and toggle on

“Use Remote Monitor without Blackmagic Cloud.”


Enter the Resolve host’s server IP Address or Host Name in the Host field.


Click Join.

Firewall exceptions and appropriate port forwarding will need to be manually configured in order to

use this mode. The procedure to initiate a session and accept connections remains the same. This

mode uses TCP server port 16410 and TCP/UDP port 16411, 16412, etc. for each client.

DaVinci Remote Monitoring via User Specified TURN Servers

When collaborating across complex network security setups that restrict the WebRTC STUN protocol,

you may now decide to use self-configured or cloud-based TURN servers to route and relay

monitoring streams.

To use this function, check the box under Preferences > System > General > Use TURN server for

Remote Monitoring. Then add the URL of your custom TURN server.


Project Libraries, Collaborative, and Remote Workflows | Chapter 198 Remote Grading and Remote Monitor

DELIVER