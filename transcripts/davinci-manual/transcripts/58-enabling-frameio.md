---
title: "Enabling Frame.io"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 58
---

# Enabling Frame.io

Integration in Preferences

An Internet Accounts panel in the System tab of the DaVinci Resolve Preferences lets you sign into

your Frame.io account and specify a local cache location for media being synced with Frame.io.

You’ll need to enter your login name and password to enable Frame.io integration, but once entered,

DaVinci Resolve will sign in automatically when DaVinci Resolve opens.

The Internet Accounts panel of the System tab of the

DaVinci Resolve Preferences window (login deliberately obscured)

The local cache location is used to store clips you import into a DaVinci Resolve project from the

Frame.io volume in the Media Storage panel of the Media page.

Deliver and Upload to Frame.io

A Frame.io preset at the top of the Deliver page’s Render Settings panel lets you render and upload

a program for review. All options in the Render Settings panel update to present suitable controls for

this process.

When you choose the Frame.io preset, the Location field turns into an Upload To field, and the Browse

button lets you choose a project and folder path to which to upload the exported result.


Setup and Workflows | Chapter 13 Frame.io and Dropbox Replay Integration

MEDIA

Choosing the Frame.io preset

Choosing a Frame.io account to deliver a program to

When you export to Frame.io, the available choices in the Resolution, Format, Video Codec, and Type

pop-up menus are limited to those that are most suitable for Frame.io file sharing. Choose the desired

export options, then click the Add to Render Queue button to add this job to the Render Queue as you

would with any other export. When that job is rendered, it automatically proceeds to upload to Frame.

io, and an upload percentage indicator appears in the job listing to show how far along this upload is.

When it’s finished, the job displays the text “Upload completed.”

The job in the Render Queue shows you the

percentage the file has uploaded so far

This upload is done in the background, so you can continue working on other things in DaVinci

Resolve while the file uploads. If you want to see how long the upload will take on any other page, you

can choose Workspace > Background Activity to see the Background Activity window.

Frame.io Comments Sync

with Timeline Markers

When you render a timeline directly to Frame.io, that timeline is automatically linked to the movie

that’s been uploaded to Frame.io, and all comments, “Likes,” and graphical annotations (drawings

and arrows) from reviewers that are added online via the Frame.io interface are automatically synced

to Frame.io markers on your timeline (so long as your computer has an active internet connection).

Frame.io markers are distinct from all other markers and can be independently shown and hidden,

or deleted. Drawings and arrows from Frame.io are converted into their equivalent DaVinci Resolve

annotation graphics for visibility in DaVinci Resolve.


Setup and Workflows | Chapter 13 Frame.io and Dropbox Replay Integration

MEDIA

Comments and graphical annotations from Frame.io appear as markers with

their corresponding overlays in your DaVinci Resolve Timeline

Working With Frame.io Markers

Double-clicking any Frame.io marker in the Timeline opens a dialog that lets you send replies to

comments that appear on Frame.io, enabling editors to respond directly to commenters.

You can also place Frame.io markers on the Timeline to have them automatically sync back to Frame.

io, giving you the ability to send your own comments back to commenters (be kind).

If you delete one or more Frame.io markers on the DaVinci Resolve timeline, those markers will

also be deleted in Frame.io. This includes the Mark > Delete All Markers > Frame.io command.

This is not undoable.

The editor talking to himself

using the Frame.io comment

dialog that appears when

you open a Frame.io marker


Setup and Workflows | Chapter 13 Frame.io and Dropbox Replay Integration

MEDIA

Frame.io Marker Navigation

You can specifically navigate only the markers created in Frame.io while in the comment dialog of

a Frame.io marker, using the Previous Marker (Shift-UpArrow) and Next Marker (Shift-DownArrow)

commands. This allows you to skip directly from comment to comment in Frame.io without having to

either navigate all markers in-between, or double-click each Frame.io marker individually to respond.

Frame.io interoperability is a Studio Only feature.

Importing Media from Frame.io

A Frame.io volume appears in the Media Storage panel of the Media page that lets you access

the media available from your Frame.io account. Within this Frame.io volume, a top-level directory

represents your account directory, and within that each project you’ve created in Frame.io appears as

a sub-directory.

Accessing the directories of a Frame.io account from the Media Storage browser

Any media files that can be accessed in Media Storage can be imported into the Media Pool via the

usual methods. Once added to the Media Pool, that media file downloads in the background to the

specified local cache location, but it’s immediately available via your internet link until the download is

complete, so you can begin working immediately. If you want to see how long the download will take,

you can choose Workspace > Background Activity to see the Background Activity window.

The Background Activity window lets you see what’s

happening in the background while you work


Setup and Workflows | Chapter 13 Frame.io and Dropbox Replay Integration

MEDIA

Linking Media Pool Clips and

Timelines with Frame.io Clips

You can also use Frame.io accessibility in the Media Storage panel of the Media page to link clips or

timelines with media that’s already uploaded to your Frame.io account. Just locate and select a Frame.

io clip in Media Storage, then right-click the clip or timeline you want to link it to in the Media Pool and

choose Link to Frame.io Media from the contextual menu.

If you’ve linked a Frame.io clip to a timeline, comments made on that Frame.io clip appear on the

linked timeline as Frame.io markers, just as if you’d exported that timeline directly to Frame.io.

Enabling Dropbox Replay

Integration in Preferences

An Internet Accounts panel in the System tab of the DaVinci Resolve Preferences lets you sign

into your Dropbox account. You’ll need to enter your login name and password to enable Dropbox

integration, but once entered, DaVinci Resolve will sign in automatically when DaVinci Resolve opens.

The Dropbox Login window in the Internet Accounts panel

of the System tab of the DaVinci Resolve Preferences window.


Setup and Workflows | Chapter 13 Frame.io and Dropbox Replay Integration

MEDIA