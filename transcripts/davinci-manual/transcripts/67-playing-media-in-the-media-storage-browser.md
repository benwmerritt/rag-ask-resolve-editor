---
title: "Playing Media in the Media Storage Browser"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 67
---

# Playing Media in the Media Storage Browser

You can select media in the Media Storage Browser to play directly in the Media page Viewer, without

importing it, so long as it’s in a format that DaVinci Resolve supports. This is useful for previewing

clips that you’re considering using in a project, but it’s also useful for quality control review sessions

of media that you’ve exported from DaVinci Resolve. All clips that are played in the Media page

Viewer are also output to video, if you have a supported Blackmagic output interface. You can also

output the video to a second monitor by choosing Workspace > Video Clean Feed, and selecting your

monitor. Additionally, if you choose Workspace > Dual Screen > On, the second computer display is

capable of displaying a set of video scopes on the Media page, which can help you QC a program

you’re delivering.

Playing DCP and IMF Packages

It’s also possible to use the Media Storage Browser to select and play DCP and IMF packages that

have been exported either using EasyDCP or using the native DCP/IMF export capabilities of DaVinci

Resolve. Simply locate the package, select it, and play it in the Viewer like any other clip. It will be

output to video and analyzed by the video scopes.

DCP and IMF packages can also be imported from Media Storage to the Media Pool for

various workflows. For more information, see Chapter 188, “Delivering DCP and IMF.”

The Media Storage Browser’s Volume List

At the left of the Media Storage browser is a list of all volumes that are currently available to your DaVinci

Resolve workstation. It’s used to locate media that you want to import manually into your project.

Scratch volumes: Indicated by a usage statistic to the right of the volume name that lists

how full that volume is, these are disks that you’ve added to the Media Storage panel of the

System Preferences window. The topmost of these scratch disks is used to store Gallery stills

and cache files.

Available volumes: Indicated by disk icons, this is a list of all fixed, removable, and network

volumes that are currently available to your workstation. When the “Automatically display

attached local and network storage locations” checkbox is turned on in the Media Storage

panel of the DaVinci Resolve Preferences, new volumes that are attached to your workstation

should automatically appear in this list.

This is a hierarchical list; clicking the disclosure triangle to the left of any volume opens up an

additional list of that volume’s subdirectories, with additional disclosure triangles next to each

subdirectory. Using the Media Storage browser, you can drill down into as many subdirectories as

you need to.

Adding Volumes That Don’t Appear in This List

If you need to access a storage volume that doesn’t appear on this list, for example if you’re using the

version of DaVinci Resolve that is available in the Apple App Store, then you can right-click anywhere

in the background of the Volume list and choose “Add New Location” to open a dialog you can use to

choose a volume you want to add.


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA

If you’re using the Apple App Store version of DaVinci Resolve, auto-mounting of attached storage

volumes is not enabled automatically. However, you can enable this in the Media Storage panel of the

DaVinci Resolve Preferences.

For more information, refer to the DaVinci Resolve Preferences section of see Chapter 4,

“System and User Preferences.”

Media Storage Browser Favorites

Underneath this is the Favorites area. If there are special directories that you find yourself frequently

accessing, you can add them to the Favorites in order to avoid having to traverse complex hierarchies

in order to access the media you need. The Favorites can be easily customized and used.

Methods of organizing favorite file system locations in the Media Storage Browser:

�To add a favorite: Right-click any folder in the Media Storage browser folder list, and choose

“Add folder to favorites” from the contextual menu. The new favorite appears at the bottom of the

Favorites area.

�To open a favorite: Click any favorite to expose the contents of the corresponding directory in the

Media Storage browser.

�To remove a favorite: Right-click the favorite you want to remove, and choose “Remove folder

from favorites” from the contextual menu.

The Media Storage Browser Area

Once you’ve selected a volume or subdirectory in the Media Storage browser, you can view its

contents in List view, Thumbnail view, or Metadata view to search through the media that’s available to

you as you try to find what you need.

List View

In List view, the following columns are available for sorting media prior to importing it into the

Media Pool:

�File name: The name of a file.

�Reel name: The reel name as it’s currently derived according to the Conform Options that are

currently chosen in the General Options panel of the Project Settings.

�Start TC: The first timecode value in the source media.

�Start: The first frame number in the source media.

�End: The last frame number in the source media.

�Frames: The duration of each clip in frames.

�Resolution: The frame size of the source media.

�Bit Depth: The bit depth of the source media.

�Video Codec: The codec used for the video track of supported media.

�Audio Codec: The codec used for the audio tracks of supported media.

�FPS: The frame rate of the source media.

�Audio Ch: The number of audio channels within the source media.

�Date Created: The date a media file has been created.

�Date Modified: The date a media file has been changed in some way and saved.


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA

�Shot: Additional metadata from media formats that support it.

�Scene: Additional metadata from media formats that support it.

�Take: Additional metadata from media formats that support it.

�Angle: Additional metadata from media formats that support it.

�Good Take: Additional metadata from media formats that support it.

If you work in List view, you gain additional organizational control by exposing columns that show

the metadata that each clip contains, prior to media being added to your timeline. You can use these

columns to help organize your media.

Methods of customizing metadata columns in List view:

�To show or hide columns: Right-click at the top of any column in the Media Storage browser and

select an item in the contextual menu list to check or uncheck a particular column. Unchecked

columns cannot be seen.

�To rearrange column order: Drag any column header to the left or right to rearrange the column order.

�To resize any column: Drag the border between any two columns to the right or left to narrow or

widen that column.

�To sort by any column: Click the column header you want to sort with. Each additional time you

click, the same header toggles that column between ascending and descending sort order.

You can also customize column layouts in the Media Storage area. Once you’ve customized a column

layout that works for your particular purpose, you can save it for future recall.

Methods of saving and using custom column layout:

�To create a column layout: Show, hide, resize, and rearrange the columns you need for a

particular task, then right-click any column header in the Media Pool and choose Create Column

Layout. Enter a name in the Create Column Layout dialog, and click OK.

�To recall a column layout: Right-click any column header in the Media Pool and choose the name

of the column layout you want to use. All custom column layouts are at the top of the list.

�To delete a column layout: Right-click any column header in the Media Pool and choose the name

of the column layout you want to delete from the Delete Column Layout submenu.

The Thumbnail Sort drop-down

in the Media Storage browser


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA

Thumbnail View

While in Thumbnail view, you can scrub through a clip’s icon to see its contents, and you can also

click the Clip Info drop-down menu at the bottom right corner of any clip’s thumbnail to see an instant

summary of that clip’s vital information, including:

�File name: The name of that file.

�In timecode: The first frame in the source media.

�Out timecode: The last frame in the source media.

�Duration: The total duration of the source media.

�Resolution: The frame size of the source media.

�Frame Rate: The frame rate, in fps, of the source media.

�Pixel Aspect Ratio: The aspect ratio of the source media.

�Codec: Which codec is used by the source media.

�Date Created: The date created metadata from the source media file.

�Flags: Flag metadata applied either by the camera that shot the media,

in the Metadata Editor, or in the Color page Timeline.

Also while in Thumbnail view, you can use the Thumbnail Sort drop-down menu (between the Search

and Option menu) to choose a criteria by which to organize the thumbnails. A wide variety of metadata

options appear, including: File Name, Reel Name, Start TC, FPS, Audio Ch, etc. You can also sort in

ascending or descending order.

Revealing a Finder Location in the Media Browser

If you drag a folder from the macOS Finder into the Media Storage browser, the Media Storage

browser will immediately update to show the location of that folder.

Viewer

Clips that you select in any area of the Media page show their contents in the Viewer. The current

position of the playhead is shown in the timecode field at the upper right-hand corner of the Viewer.

The Media page Viewer


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA

Simple transport controls appear underneath the jog bar, letting you Jump to First Frame, Play

Backward, Stop, Play Forward, and Jump to Last Frame. A jog control to the left of these buttons lets

you move through a long clip more slowly; click it and drag to the left or right to move through a clip a

frame at a time.

Audio playback can be turned on or off by clicking on the speaker icon, or adjust the level by right-

clicking on the speaker icon and dragging the slider.

To the right of the transport controls, In and Out buttons let you set In and Out points for the current

clip. The clip’s timecode is also displayed at the top right.

A jog or scrubber bar appears directly underneath the image, letting you drag the playhead directly

with the pointer. The full width of the jog bar represents the full duration of the clip in the Viewer.

The Media Viewer has an option menu that looks like three dots in the upper right corner. Clicking on

this menu reveals the options below.

An optional info bar for showing the timecode and duration of a marked section of media

Media Viewer Option menu: Contains the following commands:

�Live Media Preview: Enabled by default, makes it possible for thumbnails that you’re skimming

in the Media Pool to show the skimmed frame in the Viewer. When skimming with Live Media

Preview enabled, the playhead that appears in the thumbnail is locked to the playhead displayed

in the Viewer’s jog bar.

�Show All Video Frames: When available processing power is insufficient to play the clip or clips

at the position of the playhead due to the grade, transforms, or effects that are applied at that

moment in the Timeline, you have the ability to choose exactly how performance in DaVinci

Resolve degrades. When off, DaVinci Resolve prioritizes audio playback at the expense of

dropping video frames when processing power is tight, resulting in a more conventional playback

experience. When on, audio quality is compromised while every frame of video plays in slower-

than-real time to maintain playback.

�Show Timecode Toolbar: The Timecode Toolbar shows the In/Out point timecodes as well as the

total duration set.

�Show Audio Waveforms in Source Clip: When enabled, shows an audio waveform overlay at the

bottom of the Source Viewer that displays the audio over the entire duration of the clip.

�Show Audio Waveforms Zoomed In: When enabled, shows an audio waveform overlay at the

bottom of the Source Viewer with a zoomed in section of the audio surrounding the current

position of the playhead.

�Previous Clip: Goes to the previous clip in the Media Pool.

�Next Clip: Goes to the next clip in the Media Pool.

�Clear Recently Viewed Clips: Clears the memory of the recent clips in the Source Viewer.

�Show Marker Overlays: Enabled by default, markers that intercept the playhead when playback is

paused appear superimposed in the Viewer.

�Markers submenu: When one or more markers are applied to the clip in the Source Viewer, they

appear in this list in chronological order, listed by Name and Note. Choosing a marker from this

menu jumps the playhead to that marker in the Source Viewer.

You can also put the Viewer into Cinema Viewer mode by choosing Workspace > Viewer Mode >

Cinema Viewer (Command-F), so that it fills the entire screen. This command toggles Cinema Viewer

mode on and off.


Ingest and Organize Media | Chapter 17 Using the Media Page

MEDIA