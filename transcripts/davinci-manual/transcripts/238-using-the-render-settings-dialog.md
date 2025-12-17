---
title: "Using the Render Settings Dialog"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 238
---

# Using the Render Settings Dialog

In Fusion Studio, you initiate rendering by clicking the Render button and opening the Render Settings

dialog. This dialog configures the quality, frame range, and network usage of the rendering.

To Render a comp in Fusion Studio:


Connect a Saver node at the end of your composition.


Enter a name and a location for the saved file(s) in the Save window.


Set the format using the Format tab in the Inspector, if necessary.


Click the Render button in the transport controls area or choose File > Render All Savers.

The Render Settings dialog opens providing options for the rendered output.

The Render Settings dialog options

Ensure that the frame range and other parameters are correct and click Start Render.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Saver nodes in the DaVinci Resolve Fusion page

The Fusion page also includes a Saver node, although it is used for a different purpose than

the Saver node in Fusion Studio. Rendering from the Fusion page is handled primarily through

the MediaOut node. There is no Render Settings dialog since the rendering location and

format is predetermined by DaVinci Resolve’s cache settings. Saver nodes in the Fusion page

are a special case, and are used to render OpenEXR files only. Once you add a Saver node,

you enter the filename with the extension. exr. Click the Browse button to select a location for

the EXR sequence, and then choose Fusion > Render All Savers.

Using the Saver node is useful for optimizing extremely complex and processor-intensive

compositions. For example, you can render out specific branches of a node tree that no

longer requires frequent adjustment to OpenEXR via a Saver node, and then reimport the

result to take the place of the original branch of nodes in order to improve the performance of

your composition.

Alternatively, you can render out multi-channel mattes or EXR images containing Arbitrary

Output Variables (AOVs) to bring into other applications.

Render Settings Dialog Options

Many of the options in the Fusion Studio Render Settings dialog are used when you need to create

a quick preview or a test render. The options in this dialog allow you to increase performance by

disabling some of the image-processing operations that are time consuming but deliver higher quality

results. Often the first settings you set are those in the Configurations section. This section determines

whether you want to produce a final high quality render or a faster preview render. Selecting Final

prevents you from modifying the options that will limit the quality.

Settings

When the Configuration section is set to Preview, the Settings section of the Render dialog includes

three options that determine the overall quality and appearance of your final output. These buttons

also have a significant impact on render times. When the Configurations setting is set to Final, these

options cannot be disabled

HiQ: When enabled, this setting renders in full image quality. If you need to see what the final

output of a node would look like, then you would enable the HiQ setting. If you are producing

a rough preview to test animation, you can save yourself time by disabling this setting.

MB: The MB in this setting stands for Motion Blur. When enabled, this setting renders with

motion blur applied if any node is set to produce motion blur. If you are generating a rough

preview and you aren’t concerned with the motion blur for animated elements, then you can

save yourself time by disabling this setting.

Some: When Some is enabled, only the nodes specifically needed to produce the image of

the node you’re previewing are rendered.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Size

When the Configurations section is set to Preview, you can use the Size options to render out frame

sizes lower than full resolution. This is helpful when using the Render dialog to create proxies or just

creating a smaller file size.

Network

The Network setting controls the distribution of rendering to multiple computers. For more information,

see the network rendering section in this chapter.

Shoot On

Again, this option is only available when Configurations is set to Preview. The Shoot On setting allows

you to skip frames when rendering. You can choose to render every second, third, or fourth to save

render time and get faster feedback. You can use the Step parameter to determine the interval at

which frames are rendered.

Frame Range

Regardless of whether the Configurations is set to Final or Preview, this option defaults to the current

Render In/Out Range set in the Time Ruler to determine the start and end frames for rendering. You

can modify the range to render more or fewer frames.

Configurations

When set to Final, the Render Settings are set to deliver the highest quality results, and you cannot

modify most of the options in this dialog. When set to Preview, you can set the options to gain faster

rendering performance. Once you’ve created a useful preview configuration, you can save it for later

use by clicking the Add button, giving it a name, and clicking OK.

Rendering Previews

You can render Flipbook previews into a viewer. These Flipbook previews exist entirely within RAM.

They are created by right-clicking over a node in the Node Editor and choosing Create > Play/Preview

on > Left viewer/Right viewer from the drop-down menu. The Render Settings dialog appears where

you can configure the preview and initiate the rendering. You can also Option-drag a node directly

from the Node Editor into a viewer. The Render Settings dialog will be displayed, and the preview will

appear on the viewer you target.

For more information on rendering RAM previews, see Chapter 69, “Using Viewers.” in the

DaVinci Resolve Reference Manual or Chapter 7 in the Fusion Reference Manual.

TIP: Option-Shift-dragging a node into a viewer will skip the Render dialog and

previously used settings.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Setting Up Network

Rendering in Fusion Studio

Fusion Studio is capable of distributing a variety of rendering tasks to an unlimited number of

computers on a network, allowing multiple computers to assist with creating network-rendered

previews, disk caches, and final renders.

Using the Render Settings dialog or the built-in Render Manager, you can submit compositions to be

rendered by other copies of Fusion Studio, as well as to one or more Fusion Render nodes. Rendering

can also be controlled through the command line for integration with third-party render managers like

Deadline, Rush, and Smedge.

Render nodes are computers that do not have the full Fusion application installed but do have Fusion

Render node software installed. The Render node software is not installed by default when you install

Fusion Studio, but it can be installed at any time using the Fusion Render node Installer. The installer is

located in the Blackmagic Fusion Studio installer.dmg on macOS and the Blackmagic Fusion Studio.zip

on Linux and Windows. Fusion Studio is licensed for an unlimited number of Render nodes, so you can

install the Render node software on as many macOS, Windows, and Linux computers that you want

involved in network rendering.

To install a Render node:


Download and unzip the Blackmagic Fusion Studio archive. Then locate the Render Node Installer.


Copy the Install Fusion Render Node [version] to each computer on the network that you want to

perform rendering operations.


Install the Render node.

By default, the Render node application will be added to the Start Menu on Windows under

Blackmagic Design. On macOS, it is added to the menu bar, and on Linux it appears in the app

launcher. Each time you log in to the computer, the Render node application will run automatically.

To disable the Render node application from starting up automatically, choose Quit from the Render

node icon in the macOS menu. On Linux, right-click over the icon and choose Kill Process, and on

Windows, delete the shortcut from the Windows Startup directory.

Licensing for Network Rendering

Most versions of Fusion Studio are licensed by connecting a single-seat hardware key (dongle) to the

same computer where Fusion is installed. Each dongle includes an unlimited number of cross-platform

Render node licenses, which you can install on as many macOS, Windows, and Linux computers as

you need. For Fusion Studio to access the Render nodes, the computer with the Fusion Studio dongle

needs to be on the same local network subnet as the Render nodes. The network licensing does

not require individual license files; instead, the Render nodes automatically search for the dongle on

the subnet, making it easy to set up. Single-seat dongles do not “float” over a network; they must be

connected to the same computer where Fusion Studio operates.

Multi-License Dongles

Using a multi-license dongle, you can license 10 copies of Fusion Studio by connecting the dongle to

any computer on the same subnet. Since these licenses “float” over a network, Fusion Studio does not

have to be running on the same computer where the dongle is connected. As long as Fusion Studio is

on the same subnet, it can automatically find the license server and check out an available license.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Multi-seat dongles can be combined together to tailor the number of Fusion seats in a larger facility.

For example, three dongles each licensed for 10 Fusion Studios would serve up 30 licenses. This

also allows for redundancy. For instance, in the example above, three computers can act as license

servers. If the first server fails for some reason, Fusion Studio will automatically try the next server.

Alternatively, multiple dongles can also be plugged into a single computer.

Setting Up a License Server

Setting up the license for network rendering begins by connecting either a single-seat or multi-seat

dongle to a computer that will act as the host for the license server. The Render node installer installs

Fusion Server, which acts as the license server, although the Render node does not have to run on

that same computer. The Fusion Server is set up to launch at startup and run unobtrusively in the

background as a service/daemon, ready to serve licenses and Fusion bins. The Fusion Server is used

to serve up multiple licenses so it must be running whenever you want to operate Fusion Studio or use

the Render nodes for network rendering. Its default is to start up automatically and remain running as

long as a license is being used by another computer or a Render node is operating. If nothing is using

the Fusion Server, it will quit after 30 seconds.

You will need your network administrator to set firewall rules allowing the Fusion Server, FusionScript,

and the Fusion Render node applications to communicate and confirm licensing with the computer that

has the Fusion Studio dongle.

If for some reason you remove a dongle or the network drops out, the licenses of any connected

Fusion Studio application will also drop. Upon losing its license, Fusion Studio will start searching for

another license, locally or on a different machine. If no license is found, Fusion pauses rendering and

displays a dialog with options to retry the search or autosave the comp and quit. Render nodes only

check for a license on the network once during startup, so they are not affected by removing the

dongle or network issues.

Setting Up a License Server with Environment Variables

Environment variables provide a way to specify flexible or “variable” configuration options. When

network rendering with Fusion, environment variables can be useful for temporarily setting a location

or choosing a preference file. Using the FUSION_LICENSE_SERVER environment variable, you can

set different locations for the File Server.

Instead of looking in a single location for the Fusion Server, you can set up multiple license servers

separated by semicolons. For instance, fu:SetPrefs("Global.EnvironmentVars.FUSION_LICENSE_

SERVER", "192.168.1.12; 192.168.10.55;*")

You can also use the environment variable to scan for license servers within a subnet—for example,

“bobs-mac.local;10.0.0.23;*;license.mystudio.com”. Including an asterisk (*) indicates a broadcast

search of the local subnet.

Like most environment variables, you can put the license server in the Global Preferences via the

Prefs text file. EnvironmentVars: fu:SetPrefs("Global.EnvironmentVars. FUSION_LICENSE_SERVER",

"10.0.0.23;*") fu:SavePrefs(), see Chapter 75, “Preferences,” in the DaVinci Resolve Reference Manual

or Chapter 15 in the Fusion Reference Manual for more information on using environment variables.

NOTE: The use of straight quotes (" ") in the environment variables above are intentional and

should not be replaced with typographer’s, or curly, quotes (“ ”).


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION