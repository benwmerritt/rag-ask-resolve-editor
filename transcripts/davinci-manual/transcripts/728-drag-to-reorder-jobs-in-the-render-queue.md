---
title: "Drag to Reorder Jobs in the Render Queue"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 728
---

# Drag to Reorder Jobs in the Render Queue

You can manually reorder the Render Queue by dragging a job up and down in the stack. The

job numbers will remain in numerical order, but the actual render settings assigned to them will

be replaced.

Dragging Job 3 (H.264) in front of Job 2 (ProRes) in the Render Queue


Deliver | Chapter 186 Using the Deliver Page

DELIVER

Chapter 187

Rendering Media

This section describes the options that are available for file-based delivery.

The workflow is simple; you define the format and other settings that dictate how the media is to be

rendered, define a range of clips in the currently selected session, and then add a job containing

these settings to the Render Queue.

You can queue up as many different render jobs as you like, each with different formats, output

options, and ranges of clips, depending on what you’re trying to accomplish. When you’re ready to

render, simply click the Start Render button.

Contents

Using Presets for Fast Rendering��������������������� 4034

Custom���������������������������������������������������������������������������� 4034

Social Media Presets������������������������������������������������ 4034

ProRes Master������������������������������������������������������������� 4038

H.264 Master��������������������������������������������������������������� 4038

H.265 Master��������������������������������������������������������������� 4039

IMF (Studio Version Only)��������������������������������������� 4039

Frame.io�������������������������������������������������������������������������� 4039

Final Cut Pro 7 or X XML����������������������������������������� 4040

Premiere XML���������������������������������������������������������������� 4041

Avid AAF�������������������������������������������������������������������������� 4041

Pro Tools��������������������������������������������������������������������������� 4041

Audio Only��������������������������������������������������������������������� 4043

Creating and Using Your Own Presets������������ 4043

Import and Export Custom Presets����������������� 4043

Choosing a Location to Render������������������������� 4045

Single Clip vs. Individual Clips��������������������������� 4045

Single Clip���������������������������������������������������������������������� 4045

Individual Clips������������������������������������������������������������ 4046

All Other Render Settings for Output������������� 4046

Video Panel������������������������������������������������������������������� 4046

Audio Panel������������������������������������������������������������������� 4054

File������������������������������������������������������������������������������������� 4056

Additional Outputs��������������������������������������������������� 4058

How to Avoid Overwriting Clips

When Rendering Output Media������������������������� 4059

Defining a Range of Clips

and Versions to Render������������������������������������������ 4059

Choosing Which Versions

to Render for Each Clip������������������������������������������� 4060

Using the Render Queue���������������������������������������� 4061

Rendering Jobs from

Multiple Projects at Once�������������������������������������� 4063

Remote Rendering���������������������������������������������������� 4064

Using Multiple Project

Libraries in Remote Rendering���������������������������� 4064

Sharing Storage���������������������������������������������������������� 4064

Setting Up and Using Remote Rendering������ 4064

When You’re Finished Remote Rendering����� 4065

Setting Up a “Headless”

Remote Rendering Workstation�������������������������� 4065


Deliver | Chapter 187 Rendering Media

DELIVER

Using Presets for Fast Rendering

The very top of the Render Settings list has a set of presets for many of the most common rendering

workflows you’ll need to accomplish. If you want to create your very own settings, then choose

custom. Each preset automatically sets up what you need and locks you out of settings that are not

necessary for rendering that type of media.

Render presets selection

Custom

When custom is selected, nothing is automatically set, and all conventional media rendering

options are available, except for those that are specifically associated with particular presets.

You must manually choose the settings and options you need. All Render settings are saved on a

per‑project basis.

Social Media Presets

These presets let you render media specifically for video sharing services, with the option to upload

the rendered files automatically.

YouTube 720p/1080p/1440p/2160p

A dropdown menu lets you choose four different resolutions to render to and selects the appropriate

settings for exporting your program as a file suitable for uploading to YouTube and many other

video file sharing services. The preset renders a single clip at the timeline’s frame rate and sets the

following parameters:

�Format: MP4

�Video Codec: H.264

�Encoding Profile: High

�Audio: Main 1

�Audio Codec: AAC

�Data burn-in: Same as Project

�Normalize Audio: Checking this box will normalize the clip’s audio level to YouTube’s standard.

�Use Proxy Media: Lets your final render use the proxy media instead of the original source camera

files. Useful if speed is more important than quality.

�Render without Timecode: If you’re using certain editing tools on mobile devices that have issues

with timecode, checking this box lets you Render without Timecode.


Deliver | Chapter 187 Rendering Media

DELIVER

�Upload directly to YouTube: When this box is checked, the resulting render will automatically

upload to your YouTube account, and the following parameters will become available. If you have

multiple YouTube Channels on your account, you can select which channel to upload to.

Title: Enter the title of your video.

Description: Enter a description of your video.

Chapters from Markers: Checking this box embeds chapter points in the YouTube video

corresponding to the the selected marker color and the marker’s position on the Timeline.

Upload Thumbnail: Checking this box will open a file browser, allowing you to select a still image

that will become the thumbnail image for your video on YouTube.

Visibility: You can change how your video will be accessible on YouTube.

Category: You can select your video’s YouTube category.

Vimeo 720p/1080p/2160p

A dropdown menu lets you choose three different resolutions to render to and selects the appropriate

settings for exporting your program as a file suitable for uploading to Vimeo and many other video file

sharing services. The preset renders a single clip at the timeline’s frame rate and sets the following

parameters:

�Format: MP4

�Video Codec: H.264

�Encoding Profile: Auto

�Audio: Bus 1

�Audio Codec: AAC

�Data burn-in: Same as Project

�Use Proxy Media: Lets your final render use the proxy media instead of the original source camera

files. Useful if speed is more important than quality.

�Upload directly to Vimeo: When this box is checked, the resulting render will automatically upload

to your Vimeo account, and the following parameters will become available.

Title: Enter the title of your video.

Description: Enter a description of your video.

Visible To: You can change how your video will be accessible on Vimeo, including password protection.

TikTok Deliver Page Preset

A dropdown menu lets you choose two different resolutions to render to and selects the appropriate

settings for exporting your program as a file suitable for uploading to TikTok and many other video file

sharing services. The preset renders a single clip and sets the following parameters:

�Resolution: 1920x1080 HD

�Use Vertical Resolution: Unchecked. Check this box if you want to deliver your video in portrait

mode for proper display on phones. This should be on for TikTok.

�Frame rate: The chosen frame rate of your timeline. You can also override this and set another

frame rate manually.

�Format: MP4

�Video Codec: H.264

�Encoding Profile: Auto

�Audio: Bus 1

�Audio Codec: AAC


Deliver | Chapter 187 Rendering Media

DELIVER

�Data burn-in: Same as Project

�Use Proxy Media: Lets your final render use the proxy media instead of the original source camera

files. Useful if speed is more important than quality.

�Upload directly to TikTok: When this box is checked, the resulting render will automatically upload

to your TikTok account, and the following parameters will become available.

Title: Enter the title of your video.

Visible To: Lets you choose who will be able to view this video. The options are

Private, Public, and Friends.

Allow comments: Checking this box allows commenting on your TikTok video. Un-checking this

box forbids comments on your video.

Allow Duet: Checking this box will allow your video to be used side-by-side with a video from

another creator in TikTok using the Duet function.

Allow Stitch: Checking this box will allow your video to be edited and combined with a video from

another creator in TikTok using the Stitch function.

Presentations Preset

This setting lets you flag and format timelines to be used with Presentations in Blackmagic Cloud.

Unlike other presets, there are no codec settings to choose from. This setting simply adds the

metadata necessary for Presentations to share your timeline. You must have already created a

Presentation in Blackmagic Cloud before you can use this setting.

�File Name: Choose the name of the timeline to be uploaded to Presentations.

�Upload To: Choose the name of the existing Blackmagic Cloud Presentation to upload to.

�Use Proxy Media: Use the Proxy Media as the source for the compression and upload to

Blackmagic Cloud rather than the original media.

Dropbox or Dropbox Replay 720p/1080p/2160p

A dropdown menu lets you choose three different resolutions to render to and selects the appropriate

settings for exporting your program as a file suitable for uploading to Dropbox and many other video

file sharing services.

The preset renders a single clip at the timeline’s frame rate and sets the following parameters:

�Format: MP4

�Video Codec: H.264

�Encoding Profile: Auto

�Audio: Bus 1

�Audio Codec: AAC

�Data burn-in: Same as Project

�Use Proxy Media: Lets your final render use the proxy media instead of the original source camera

files. Useful if speed is more important than quality.

�Upload directly to Dropbox: When this box is checked, the resulting render will automatically

upload to your Dropbox account.


Deliver | Chapter 187 Rendering Media

DELIVER

Setting Up Video Sharing Uploads

DaVinci Resolve has account integration with YouTube, Vimeo, TikTok, Dropbox, and Frame.io that

allows you to render and upload directly to each service. An Internet Accounts panel in the System tab

of the DaVinci Resolve Preferences lets you sign into your YouTube, Vimeo, Dropbox, and Frame.io

accounts, as well as specify a local cache location for media being synced with Frame.io.

For each service you sign into, a floating window presents the interface in which you’ll need to enter

your login name and password to enable integration, followed by whatever two-factor identification

and other required steps are necessary. Once entered, DaVinci Resolve will sign in to each of these

services automatically when DaVinci Resolve opens.

For each service you sign into, the service’s upload parameters will also be available in the Custom

Export Video settings in the Deliver page. This allows you to create your own custom file settings that

can supersede the normal formats allowed by the service presets, while allowing you the convenience

of the all-in-one uploading and description entry of the preset.

The Internet Accounts panel of the System tab of the DaVinci Resolve Preferences window

NOTE: For Frame.io, the local cache location is used to store clips you import into a DaVinci

Resolve project from the Frame.io volume in the Media Storage panel of the Media page.


Deliver | Chapter 187 Rendering Media

DELIVER

Deliver and Upload to Social Media

When you’ve configured YouTube, Vimeo, TikTok or Dropbox access in the Internet Accounts panel

of the System Preferences, the YouTube, Vimeo, and Dropbox presets expose an “Upload directly to

YouTube/Vimeo/TikTok/Dropbox” checkbox, which lets you choose whether or not to automatically

upload the rendered result.

Choose the desired export options, then click the Add to Render Queue button to add this job to

the Render Queue as you would with any other export. When that job is rendered, it automatically

proceeds to upload to the selected video sharing service, and an upload percentage indicator

appears in the job listing to show how far along this upload is. This upload is done in the background,

so you can continue working on other things in DaVinci Resolve while the file uploads. If you want

to see how long the upload will take on any other page, you can choose Workspace > Background

Activity to see the Background Activity window.

Waiting for your movie to upload

Once the upload is finished, you can view the file directly on the social media site in a web browser by

right-clicking on the job in the Render Queue and selecting Reveal in Browser.

Review Before Upload

For an extra level of quality control before you send your video out live on the internet, you can select

Review Before Upload from the Render Queue option menu. This option will pause the automatic

upload process after the file has been rendered with a message, “Waiting for Upload.” You can then

right-click on the job in the Render Queue, and select Reveal in Finder to open and review your video.

Once you’ve made your decision, from that same menu, you can select either Upload to (service

name) to let your video go, or Cancel Upload if you’ve had second thoughts.