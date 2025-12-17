---
title: "KDM Generation and Management"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 736
---

# KDM Generation and Management

Key Delivery Messages (KDMs) are required to allow an encrypted DCP play on a designated

projector at a particular theater at a specified time. DaVinci Resolve is capable of creating KDMs,

which is convenient for exporting KDMs for select screenings, but commercial distributors may require

thousands of KDMs. Fortunately, easyDCP allows you to use external Distribution KDM (DKDM) utilities

to generate KDMs for your clients, so you don’t have to tie up your DaVinci Resolve workstation

with this task.


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER

Publishing Your Encrypted Digital Cinema Package

While you can play your encrypted DCP on the same DaVinci Resolve system that generated it, if you

wish to publish the DCP so other players can decode and play you need to generate a KDM to send to

the player. The user of the other player, or players, will need to generate a Server Certificate for each

of their players and send this to you so when you generate the KDM it will be just for those players.

Select the DCP in the Media page Library. Right-click and select Generate KDMs. From the dropdown

select the location of the Server Certificate file if the KDM is for one player, or folder for multiple

players. Set the start and end dates that the KDM will be valid for, an output folder to place the KDM,

and then select Generate.

You can now send your DCP and the KDMs to the player you authorized. The user there will import the

KDM and the DCP will play between the start and end dates.

Playing Your Digital Cinema Package

To play a DCP you’ve output from DaVinci Resolve, use the Media page to add it to the Media Pool and

edit it into a timeline like any other clip.

Decoding the JPEG2000 images embedded within the DCP in real time is computationally intensive.

If your system is underpowered you can reduce the decoded resolution of the files by selecting Half

or Quarter Resolution Decode from the File > easyDCP menu. A smaller, less bandwidth-intensive

version of the JPEG2000 files will be decoded by discarding some levels of the wavelet stage inside

the decoder, which will directly increase the playback performance.

Playing Third-Party Digital Cinema Packages

To play a non-encrypted DCP simply select the DCP in the Media page like any other clip. To play

an encrypted DCP from a third party you first must publish your Server Certificate. They use the

certificate to generate KDMs for their DCP to play on your DaVinci Resolve system. From the File menu

choose easyDCP > Export Server Certificate, and on the dropdown menu choose a location to save

the file. Send this to the third party for KDM generation.

When you receive a KDM or a Digest for an encrypted DCP you must first import the file into your

DaVinci Resolve system. Choose File > easyDCP menu > Import KDM/Digest, and then select the file.

Then simply select the encrypted DCP in the Media Page Library to play.


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER

Chapter 189

Delivering to Tape

This section covers how to use the Deliver page to output a timeline, either

in whole or in part, to a device-controllable VTR connected to a compatible

Blackmagic Design video interface.

For whichever output interface you use, you need to make sure that the RS-422 interface is connected

to that of the VTR, and that device control has been established.

Contents

The Tape Output Interface����������������������������������������������������������������������������������������������������������������������������������������������������������� 4083

Gang Timecode to Tape����������������������������������������������������������������������������������������������������������������������������������������������������������������� 4083

Insert/Assemble Dropdown Menu�������������������������������������������������������������������������������������������������������������������������������������������� 4084

Start Record Button�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4084

Setting Up for Tape Output���������������������������������������������������������������������������������������������������������������������������������������������������������� 4084

General Options��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4084

Capture and Playout Settings������������������������������������������������������������������������������������������������������������������������������������������������������ 4084

Capture��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4085

Playout Settings���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4086

Edit to Tape Queue Option Menu Settings�������������������������������������������������������������������������������������������������������������������������� 4087

Tape Output Procedures��������������������������������������������������������������������������������������������������������������������������������������������������������������� 4087

Power Mastering�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4087

Outputting a Program From the Timeline������������������������������������������������������������������������������������������������������������������������������ 4087

Batch Outputting Multiple Clips�������������������������������������������������������������������������������������������������������������������������������������������������� 4088


Deliver | Chapter 189 Delivering to Tape

DELIVER

The Tape Output Interface

Tape output is accomplished on the Deliver page, which has to be placed in the Tape mode before

you can proceed.

To switch to tape output in the Deliver page:

�Click the Tape button, which is the third button from the left on the Interface toolbar at the top of

DaVinci Resolve. The Deliver page updates to reflect the relevant controls for editing to tape.

While in Edit to Tape mode, the Deliver page is used to control the VTR, in order to establish In and

Out points for insert or assemble editing of the selected portion of the current Timeline to tape.

�Capture and Playout: The Render Settings panel turns into the Capture and Playout panel, with

controls and settings governing how DaVinci Resolve will output your program to tape.

�Edit to Tape Queue: The Render Queue turns into the Edit to Tape Queue, which lets you set up

a batch of either previously rendered media files, or In and Out point‑defined segments of the

current Timeline for simultaneous output to tape.

�Transport controls: The transport controls, while similar in appearance to those used while in

Render mode, now control the VTR.

�Shuttle control: A shuttle control appears in what was formerly the jog or scrubber bar, which lets

you shuttle through the range of reverse and forward speeds compatible with that deck.

�In and Out controls: In Edit to Tape mode, the In and Out buttons to the right of the transport

controls define a range of the tape to Insert or Assemble edit to, within the current Timeline.

While in Edit to Tape mode, you can still define In and Out points to define a specific range of

the Timeline by right-clicking a clip in the Thumbnail or Mini‑Timeline, and choosing Mark In or

Mark Out. You can only add In or Out points to the beginning and end of clips.

�Cue In and Cue Out controls: Buttons next to the timecode In and Out fields cue the tape to those

frames on tape.

Edit to Tape controls

Gang Timecode to Tape

When the Deliver page is in Tape mode, you can right-click the ruler running along the top of the

Timeline and choose “Gang Timecode to Tape,” which puts DaVinci Resolve into a mode where every

time you set an In point on the Deliver page Timeline, a corresponding In point is automatically set on

the tape deck. Setting both In and Out points on the Deliver page Timeline results in the In and Out

points on the tape deck being set at the same timecode, making it easy to set up insert edits to tape

on top of a previously output program.

The Gang Timecode to Tape option


Deliver | Chapter 189 Delivering to Tape

DELIVER

Insert/Assemble Dropdown Menu

A dropdown menu under the In and Out buttons lets you choose how to edit the selected part of the

Timeline to tape. There are two options:

�Insert: Performs an insert edit to tape, in which selected tape tracks are seamlessly and frame-

accurately overwritten without interrupting the timecode or control track. You must be outputting

to either a blacked tape, or a prerecorded tape to make an insert edit.

�Assemble: Performs an assemble edit, in which every track of tape is overwritten, including the

video, audio, timecode, and control tracks.

�Crash: (Only appears if “Output Source Timecode” has been enabled in the Playout section of the

Capture and Playback panel of the Project Settings) Similar to an assemble edit, except there is no

pre-roll period to let the VTR get up to speed. A crash edit also overwrites every track of the tape,

including the video, audio, timecode, and control tracks, and may result in a more visible jump

at the resulting edit point. However, in some instances crash edits may be the only option for a

particular operation.

NOTE: When DaVinci Resolve is performing a Batch Output operation, you can only output

clips using assemble editing or crash recording.

Start Record Button

Once you’ve set In and Out points to define how much of the tape to record to, the Start Record button

initiates device-controlled tape output.

Setting Up for Tape Output

Before you perform an edit to tape, the Capture and Playback panel of the Project Settings has a

number of options that you should set to match the format and type of tape output you’re doing.

General Options

The Output LTC checkbox, when turned on, directs DaVinci Resolve to output LTC timecode.

Capture and Playout Settings

These settings affect both capture and playback when using the Tape Ingest options of the Media

page, or the Tape Output options of the Deliver page.

�Video capture and playback: You can choose the video format (frame size and frame rate) with

which to output to tape from this dropdown menu. HD timelines can be downconverted to SD, and

SD timelines can be upconverted to HD using the format conversion of your DeckLink card.

�Use left and right eye SDI: A checkbox that enables supported video interfaces to ingest and

output muxed stereoscopic video when used with supported VTRs, such as HDCAM SR decks

with 4:2:2 x 2 mode. (When muxed stereoscopic signals are ingested, each eye is separated into

individual left-eye and right-eye image files.) This parameter only appears when your hardware is

set up appropriately.

�Video connection operates as: Selects between the available signal options: Use 4:4:4 SDI,

and enable Single Link. Which options are available depend on which video capture card you

are using.


Deliver | Chapter 189 Delivering to Tape

DELIVER

�Data Levels: Lets you specify the data range (normally scaled or full range) that’s used when

ingesting from or outputting to tape. This option switches the data range of the signal output by

your video capture card, but only during capture from tape in the Media page, or output to tape in

the Deliver page. When capture or output is not currently occurring, your video capture card goes

back to using the identically named data range setting in the Master Settings panel of the Project

Settings, which governs how you monitor the signal being output on an external broadcast display

or projector.

�Video bit depth: Choose the bit depth that corresponds to the capability of your deck. You can

choose between 8-bit and 10-bit. Outputting to 10-bit is more processor intensive, but higher

quality for compatible devices, and is the default setting.

�Use deck autoedit: If supported by your video deck, this is the best method to record video

to the deck, as it enables the deck to roll the edit using the specified preroll, and control the

edits via serial device control. If this checkbox is turned off, a basic edit On/Off mode is used

by the deck, with the potential for frame inaccuracies if the “Non auto edit timing” setting is not

properly adjusted.

�Non auto edit timing: Adjusts the edit synchronization of the connected deck when auto edit is

turned off.

�Deck preroll: Sets the number of seconds for preroll. How much is appropriate depends on the

performance of your deck.

�Video output sync source: When using a DeckLink card this is set to Auto. Other capture

cards may require you to set the sync source to “Reference” for playout and “Input” for ingest.

This setting is only available if you have a DVS card installed on your system.

�Add 3:2 pulldown: Inserts or removes the 3:2 pulldown required to record or play 23.98 fps media

to or from a 29.97 tape format.