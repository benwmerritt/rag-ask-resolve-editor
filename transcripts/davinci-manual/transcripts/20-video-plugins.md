---
title: "Video Plugins"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 20
---

# Video Plugins

You can selectively enable and disable specific Open FX plugins on startup. You can use this function

to streamline and organize the Open FX list to just the plugins you commonly use, or to exclude a

problematic plugin that causes instability in the system. Additionally, DaVinci Resolve automatically

checks the last plugin loading result on startup, and skips any plugins that previously caused a

crash or hang.

Individual Open FX plugins can be manually enabled and disabled in the Video Plugins panel by

checking or unchecking the boxes corresponding to the plugins.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

The Video Plugins panel allows you to enable or disable specific Open FX plugins at startup.

Audio Plugins

Three sections of parameters let you manage VST effects, enabled plugins, and external audio

processes.

�VST Effects: A list at top lets you manually add and remove VST plugin effects directories,

if necessary. VST effects aren’t installed in a standard location, so it may sometimes be necessary

to add a newly installed directory of VST plugins that you’ve just installed on your system.

Audio Plugins Preferences - VST Effects

�Available Plugins: Once you’ve added one or more VST directories to the list, a second list

underneath shows all audio plugins that are available within these directories. Each plugin on the

list has a checkbox that shows whether or not it’s currently enabled. Any VST plugins that cause

DaVinci Resolve to crash while loading them during startup will be automatically disabled. You

can use this list to see which plugins have been disabled, for troubleshooting purposes, and to

reenable such “blacklisted” plugins by turning their checkboxes back on.

Category Column: VST and Audio Units plugins are organized into categories within the Fairlight

Mixer. You can move a plugin to a different category by clicking its category name and selecting a

new one from the Category popup list.

NOTE: This does not apply to Fairlight FX plugins.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Audio Plugins Preferences - Available Plugins

�Setup External Audio Processes: While working in the Fairlight page, you have the ability to

process an audio file using a third-party application, if necessary, in the event you need to use

another application’s capabilities to create an effect or solve an issue that can’t be accomplished

in the Fairlight page itself. To do this, you must first add one or more applications to the External

Audio Process list in the Audio Plugins panel of the System Preferences.

NOTE: VST is a trademark of Steinberg Media Technologies GmbH.

Audio Plugins Preferences - Setup External Audio Processes

To add an External Audio Process:


Click the Add button.


Double-click the text in the Name column and change the name to that of the application or

process you’re going to link to.


Click once in the Path column, and then use the file dialog to locate and select the application or

script you want to use as the external audio process.


Open the drop-down menu in the Type column, and choose how you want the selected audio

process to work: Reveal (open the application), Command Line (use from Terminal), or Clipboard

(copy the audio clip file path to the clipboard to paste into the open command of an application

or utility).


When you’re done, click Save, and restart DaVinci Resolve if you’re prompted to.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Control Panels

Two sections let you specify which Color Grading Panel and Audio Console is connected

to your workstation.

�Color Grading Panel: A menu lets you choose which color grading panel you have connected to

your workstation. Some panels expose additional controls.

If you have a DaVinci Resolve Mini or Micro Panel, leave this setting set to None and these panels

will be auto-detected by Resolve when you plug them in.

If you have a control panel that connects via USB, choose your panel from the list.

If you have a DaVinci Resolve Mini Panel connected over Ethernet, choose “DaVinci Resolve Mini

Panel (Ethernet)” and then choose your panel from the drop-down that appears.

If you’re using a JLCooper Eclipse, choose “JLCooper Eclipse CX” and then enter the IP and Port

number into the fields that appear.

�Audio Console: A menu lets you choose which Fairlight Audio Console you have connected to

your workstation. Some panels expose additional controls.

�Use MIDI Audio Console: A checkbox lets you enable the use of a third-party audio console that’s

connected to your workstation. Turning this on exposes three additional menus.

MIDI Protocol: Lets you choose either the HUI or MCU protocol, whichever is compatible with the

audio console you want to use.

MIDI Input: Lets you choose the MIDI input used to connect your console.

MIDI Output: Lets you choose the MIDI output used to connect your console.

�Head Tracker: A menu lets you choose which head tracker profile to use for immersive audio.

General

This panel provides various options for scripting, audio processing, monitoring, and sending

problem reports.

�External Scripting Using: (Resolve Studio only) Options include None, Local, and Network. When

set to None, only scripting in the Console window is allowed. When set to Local, external scripts

and applications on the same computer can control DaVinci Resolve. When set to Network,

external scripts and applications from other computers on the network (or via the internet) can

control DaVinci Resolve.

�Use 10-bit precision in viewers if available: This checkbox only appears on macOS installations

of DaVinci Resolve. Turning this checkbox on lets DaVinci Resolve display 10-bit images in

the Viewer.

�Use Mac Display Color Profile for viewers: If you’re using DaVinci Resolve on macOS, this

checkbox enables all viewers in DaVinci Resolve to use whatever display profile is selected in the

Displays panel of the System Preferences. This lets DaVinci Resolve use ColorSync on macOS so

your Viewer image should better match your output display.

�Optimize project library cloud data traffic: If you’re having difficulty accessing the Blackmagic

Cloud through a corporate firewall, check this box to connect without having to set port mapping

and firewall exceptions. https://blackmagicdesign.com still needs to be whitelisted for access.

�Automatically Tag Rec.709 Scene Clips as Rec.709-A: Turn this checkbox on to automatically tag

any Rec. 709 QuickTime files for Rec. 709-A playback. This setting is useful if your final QuickTime

video does not match what you see in the Resolve viewers (gamma shift), and you wish to export

for the web rather than broadcast.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

�Automatically Scan other project libraries for remote rendering jobs: Turn this checkbox on to

scan all connected project libraries, rather than just the current project library for possible remote

rendering jobs.

�Automatically Check for Updates: Turn this checkbox on to make it easier to ensure you’re using

the latest version of DaVinci Resolve. You can also choose DaVinci Resolve > Check For Updates

to notify you of new versions and download them when available.

�Automatically opt-in for new beta program notifications: Lets you know when public beta

versions of DaVinci Resolve become available, in case you’re interested in living on the edge.

�Send report when application quits unexpectedly: When this checkbox is turned on, this setting

enables DaVinci Resolve to automatically prepare a problem report whenever DaVinci Resolve

unexpectedly quits. You get to fill out some information (please be as specific as you can about

what you were doing when DaVinci Resolve had its issue) and click a button to send the report.

�Limit Presentations upload speed to X KB/s: Allows you to set a hard limit on the upload speed

while using Presentations to avoid saturating all your network bandwidth.

�Use Remote Monitoring without Blackmagic Cloud: Allows you to use remote monitoring on your

own network instead of going through Blackmagic Cloud.

�Use TURN server for Remote Monitoring: If you are not using Blackmagic Cloud for security

reasons and you are using a self-configured or cloud-based TURN servers to route and relay

monitoring streams, enter that server here.

�Prevent sleeping when Blackmagic Cloud sync enabled project is open: This checkbox is on by

default and prevents your computer from entering sleep mode while a Blackmagic Cloud project is

active to make sure all online data transfers complete. Uncheck this box to let your computer go to

sleep whenever it wants.

�Automatically send problem reports: When this checkbox is turned on, problem reports are

automatically sent, with no user intervention. You have the option of adding your name and email

address to be automatically included, but this information is optional.

Internet Accounts

The Internet Accounts panel serves as a login manager for the Blackmagic Cloud and other social

media sites.

DaVinci Resolve has tight integration with YouTube, Vimeo, TikTok, Dropbox, and Frame.io that allows

you to render and upload directly to each service. This panel provides buttons that let you sign into

your YouTube, Vimeo, TikTok, Dropbox, and Frame.io accounts, as well as specify a local cache

location for media being synced with Frame.io.

For each service you sign into, a floating window presents the interface in which you’ll need to enter

your login name and password to enable integration, followed by whatever two-factor identification

and other required steps are necessary. Once entered, DaVinci Resolve will sign in to each of these

services automatically when DaVinci Resolve opens.

Advanced

This tab is used for special Resolve configurations and SAN parameters that are applicable to

older file systems.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

The Internet Accounts panel of the System tab of the DaVinci Resolve Preferences window