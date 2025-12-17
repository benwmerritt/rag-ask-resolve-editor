---
title: "Remote Rendering"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 733
---

# Remote Rendering

If you have multiple DaVinci Resolve workstations on the same network, you can send a job in the

Render Queue from the workstation you’re using (referred to as the “artist workstation”) to one of

the “remote workstations” on the network using remote rendering. This lets you use any one of

your currently unused secondary workstations to render your jobs, while you continue working on

your main workstation.

In order to use remote rendering, you must adhere to the following three criteria:

�Both the artist workstation and the remote workstation must have DaVinci Resolve Studio

installed. Remote rendering does not work with the free version of DaVinci Resolve.

�Both the artist workstation and the remote workstation can use the same shared network project

library, or any other Postgres project library that is connected to either one of the machines, or to a

dedicated Remote Project Library Server.

For more information on setting up and using shared project libraries, see Chapter 196,

“Managing Project Libraries and Project Servers.”

�Both the artist workstation and the remote workstation must have access to the same media files

on either the same storage volumes, or identically named storage volumes.

Using Multiple Project Libraries in Remote Rendering

You can set up remote renders for projects in all connected Davinci Resolve project libraries,

not just the currently active one. To activate this feature, check the “Automatically scan other

project libraries for Remote Rendering jobs” box in the General settings of the System tab, of the

DaVinci Resolve Preferences.

Sharing Storage

It’s important that both the artist and remote workstations have access to the same media on the same

named storage volume for remote rendering to work properly. This can be done via some manner of

shared storage, such as a SAN. However, it can also be done by mounting the same volume over your

network. This will be slower, but it will work.

If you’re mixing Mac OS X, Windows, and Linux workstations for remote rendering, you’ll need to use

the Mapped Mount column of the Media Storage Locations list in the Media Storage panel of the

System Preferences to add each volume’s path as it’s understood on the workstation it’s attached to.

For example, on a Windows workstation that’s accessing volumes from a Linux workstation, type in the

Linux-style file paths in the Mapped Mount column for each scratch disk that’s listed.

Setting Up and Using Remote Rendering

Using remote rendering is easy, but it does require a bit of preparation.


Make sure the storage volume containing the media being referenced by the project you want to

render is mounted on both the artist and remote workstations.


Open DaVinci Resolve on the remote workstation, and do one of the following:

�When the Project Browser opens, right-click anywhere and choose Remote Rendering.

�If you’ve already opened a project in DaVinci Resolve, you can also choose Workspace >

Remote Rendering.


Deliver | Chapter 187 Rendering Media

DELIVER

DaVinci Resolve will automatically open to the Deliver page, awaiting jobs to be assigned for

automatic rendering.


On the artist workstation, add a job to the render queue as you normally would.


Click the Remote Rendering button for that job in the Render Queue and one of the options from

the list that appears:

Any: Automatically assigns that job to the next workstation that isn’t currently rendering anything.

If all remote rendering workstations are rendering, assigns it as the next job in line.

YourComputer.local: The artist workstation with the name “YourComputer.” Choose this if you

want to render the job locally, and not remotely.

Other Workstations on Network: All other remote rendering workstations are listed below, so you

can choose which specific workstation you want to assign a job to.

Clicking the Remote Render button

to remotely render a job


Click Start Render. The job is sent to the remote workstation you selected and is rendered, while

you’re free to continue working on your artist workstation.

When You’re Finished Remote Rendering

Once you’re done using a particular DaVinci Resolve workstation in Remote Rendering mode and you

want to go back to using it as an artist workstation, choose Workspace > Remote Rendering to exit

remote rendering and return to the Project Manager.

Setting Up a “Headless” Remote Rendering Workstation

DaVinci Resolve allows remote rendering clients to operate in a so-called “headless” mode, with no

GUI. This can be accomplished from the command line, by opening the directory where the app is

located and then running DaVinci Resolve in Remote Rendering (–rr) mode using the correct command

line syntax for your operating system. Once run in this way, DaVinci Resolve silently and invisibly waits

on that system for remote rendering jobs to be sent to that workstation.

On macOS

Open Terminal.

Change the directory to:

cd /Applications//DaVinci\ Resolve/DaVinci\ Resolve.app/

Contents/MacOS/

Run the following command:

./Resolve -rr


Deliver | Chapter 187 Rendering Media

DELIVER

On Windows

Open the Command Prompt.

Change the directory to:

C:\Program Files\Blackmagic Design\DaVinci Resolve\

Run the following command:

Resolve.exe -rr

On a Linux CentOS 6.8 system

Open Terminal.

Change the directory to:

cd /home/resolve/Cyclone/

Run the following command:

./script.start -rr

On a Linux CentOS 7.x system

Open Terminal.

Change the directory to:

cd /opt/resolve/bin

Run the following command:

./resolve -rr


Deliver | Chapter 187 Rendering Media

DELIVER

Chapter 188

Delivering

DCP and IMF

For projects requiring Digital Cinema Package (DCP) or Interoperable Master

Format (IMF) mastering for digital cinema or broadcast distribution, DaVinci Resolve

allows native DCP and IMF encoding and decoding for the creation and playback

of unencrypted DCP and IMF deliverables, or it can be integrated with Fraunhofer’s

easyDCP application in order to master fully encrypted DCP files, play them back

for testing, and generate Key Delivery Messages (KDMs) for theatrical distribution,

all directly within DaVinci Resolve.

This means you can encode a DCP or IMF master straight from your program’s source media, all

within the 32-bit floating point image processing pipeline of DaVinci Resolve, for the highest possible

quality result.

Contents

Native IMF Encoding and Decoding (Studio Version Only)������������������������������������������������������������������������������������������ 4068

Native Unencrypted DCP Encoding and Decoding (Studio Version Only)����������������������������������������������������������� 4070

Native DCP Encoding Parameters��������������������������������������������������������������������������������������������������������������������������������������������� 4070

Rendering IMF Segments and DCP Reels���������������������������������������������������������������������������������������������������������������������������� 4072

Creating DCP/IMF Supplemental Packages����������������������������������������������������������������������������������������������������������������������� 4073

Importing a DCP or IMF Into a Timeline �������������������������������������������������������������������������������������������������������������������������������� 4073

Editing the Resulting Timeline ����������������������������������������������������������������������������������������������������������������������������������������������������� 4074

Dolby Vision Metadata ������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4075

Exporting ���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4075

Photon Validation of IMF Packages����������������������������������������������������������������������������������������������������������������������������������������� 4076

Validating in the Media Pool ������������������������������������������������������������������������������������������������������������������������������������������������������� 4076

Validating on Export ������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4077

Using and Licensing EasyDCP��������������������������������������������������������������������������������������������������������������������������������������������������� 4078

Requesting Your Server Certificate Set���������������������������������������������������������������������������������������������������������������������������������� 4078

Importing Your Server Certificate Set�������������������������������������������������������������������������������������������������������������������������������������� 4078

Switching Between Native DCP and EasyDCP Encoding�������������������������������������������������������������������������������������������� 4079


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER

Native IMF Encoding and Decoding

(Studio Version Only)

The Format dropdown in the Video panel of the Render Settings now has a native IMF option that

lets you export to the SMPTE ST.2067 Interoperable Master Format (IMF) for tapeless deliverables to

networks and distributors. No additional licenses or plugins are required to output to IMF.

The IMF format supports multiple tracks of video, multiple tracks of audio, and multiple

subtitle and closed caption tracks, all of which are meant to accommodate multiple output formats and

languages from a single deliverable. As of DaVinci Resolve 16, IMF export also supports exporting

IMF packages that use ST.2098 and Dolby immersive audio via selected Main busses. All of this is

done by wrapping a timeline’s different video and audio tracks (media essences) and subtitle tracks

(data essences) into a “composition” within the Material eXchange Format (MXF).

Additionally, a dropdown menu to the right of this preset provides options for Generic,

20th Century Fox, and Netflix versions of this preset.

The IMF Generic preset in the Render Settings has

options for different resolutions of output

When IMF is selected from the Format dropdown, the Codec drop-down menu presents options for

Kakadu or EasyDCP encoding, with Kakadu being the method that’s included with DaVinci Resolve

Studio. A Type dropdown lets you choose what kind of JPEG2000 output you want, with options

including RGB, YUV, and Dolby Vision. Additional parameters include:

�Package Type: Defaults to App2 Extended (App2e), for encoding JPEG 2000 up to 4K.

�Bit Depth: The bit depth of the encoded IMF video.

�Encoding Profile: A dropdown that lets you choose among Auto, IMF, and Broadcast.

�Encoding Level: Provides different choices based on what is selected in Encoding Profile.

�Maximum bit rate: Lets you choose how much to compress the result.

�Lossless Compression: Lets you choose to encode using lossless compression.

�Slope-Rate Control: A checkbox lets you specify lossless compression.

�QStep: (DCP, IMF) Lets you choose either automatic or manually specified DCP quantization levels

at which to compress the video signal when using the Kakadu JPEG 2000 encoder.

EasyDCP Color Management����������������������������������������������������������������������������������������������������������������������������������������������������� 4079

EasyDCP Output in the Deliver Page������������������������������������������������������������������������������������������������������������������������������������� 4079

KDM Generation and Management����������������������������������������������������������������������������������������������������������������������������������������� 4080

Publishing Your Encrypted Digital Cinema Package��������������������������������������������������������������������������������������������������������� 4081

Playing Your Digital Cinema Package��������������������������������������������������������������������������������������������������������������������������������������� 4081

Playing Third-Party Digital Cinema Packages���������������������������������������������������������������������������������������������������������������������� 4081


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER

Render settings in the Export Video section for the IMF format

A separate group of parameters named Composition Settings, underneath the Advanced Settings, lets

you add metadata to your IMF package, including:

�Composition name: The name of the exported composition.

�Issuer: The organization providing the composition.

�Use current date: A checkbox that lets the current date be used as the Issue date automatically.

�Issue date: The date the composition is issued.

�Content kind: A dropdown provides a list of acceptable choices for defining the content.

�Content version label: Meant to identify the version of the content being provided.

�Annotate xml using composition name: Auto-populates Asset Map, Composition Playlist, and

Packing List with data from the project. Otherwise these three fields are manually editable.

�Annotate media using filename: Auto-populates Main Video Track and Audio Track 1 with data

from the project. Otherwise these three fields are manually editable.

Parameters for adding composition metadata


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER